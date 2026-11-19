# Copyright (c) 2026 Beijing Volcano Engine Technology Co., Ltd.
# SPDX-License-Identifier: AGPL-3.0
"""Small, dependency-free readers for ASAM MDF and Vector BLF measurement files.

The readers cover the common uncompressed layout used by MATLAB/Simulink
measurement exports. Unknown blocks are reported instead of guessed.
"""

from __future__ import annotations

import csv
import io
import re
import struct
import zlib
from pathlib import Path
from typing import Any


def _slug(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]+", "_", text).strip("._")[:80] or "channel"


def _csv(values: list[float | int | None]) -> str:
    output = io.StringIO(newline="")
    writer = csv.writer(output, lineterminator="\n")
    writer.writerow(["sample", "value"])
    for index, value in enumerate(values, 1):
        writer.writerow([index, "" if value is None else value])
    return output.getvalue()


def _stats(values: list[float | int | None]) -> dict[str, Any]:
    numbers = [value for value in values if isinstance(value, (int, float))]
    return {
        "sample_count": len(values),
        "minimum": min(numbers) if numbers else None,
        "maximum": max(numbers) if numbers else None,
        "first": values[0] if values else None,
        "last": values[-1] if values else None,
    }


def _mdf4_blocks(data: bytes):
    offset = 64
    seen: set[int] = set()
    while offset + 24 <= len(data) and data[offset : offset + 2] == b"##":
        if offset in seen:
            break
        seen.add(offset)
        length = struct.unpack_from("<Q", data, offset + 8)[0]
        link_count = struct.unpack_from("<Q", data, offset + 16)[0]
        if length < 24 or link_count > 512:
            break
        links = [
            struct.unpack_from("<Q", data, offset + 24 + 8 * index)[0]
            for index in range(link_count)
            if offset + 24 + 8 * index + 8 <= len(data)
        ]
        data_offset = offset + 24 + 8 * link_count
        yield offset, data[offset : offset + 4], length, links, data_offset
        offset += length


def _tx_text(data: bytes, offset: int) -> str:
    if not offset or offset + 24 > len(data):
        return ""
    return data[offset + 24 : offset + min(256, length_at(data, offset))].split(b"\0", 1)[
        0
    ].decode("utf-8", errors="replace").strip()


def length_at(data: bytes, offset: int) -> int:
    if offset + 24 > len(data):
        return 0
    return int(struct.unpack_from("<Q", data, offset + 8)[0])


def _decode_mdf4(data: bytes) -> dict[str, Any]:
    blocks = list(_mdf4_blocks(data))
    groups = [item for item in blocks if item[1] == b"##CG"]
    channels: list[dict[str, Any]] = []
    sample_count = 0
    record_size = 0
    data_payload = bytearray()
    # Channel groups define the record layout; data blocks repeat that layout.
    for group_index, group in enumerate(groups, 1):
        _, _, _, group_links, group_data = group
        if group_data + 32 > len(data):
            continue
        cycle_count = struct.unpack_from("<Q", data, group_data + 8)[0]
        size = struct.unpack_from("<Q", data, group_data + 24)[0]
        sample_count = max(sample_count, int(cycle_count))
        record_size = int(size) or record_size
        first_channel = group_links[1] if len(group_links) > 1 else 0
        offset = first_channel
        while offset and len(channels) < 4096:
            block = next((item for item in blocks if item[0] == offset), None)
            if block is None:
                break
            _, _, _, links, channel_data = block
            if channel_data + 16 > len(data):
                break
            name = _tx_text(data, links[2]) if len(links) > 2 else ""
            channels.append(
                {
                    "name": name or f"channel_{len(channels) + 1}",
                    "group": group_index,
                    "byte_offset": struct.unpack_from("<I", data, channel_data + 4)[0],
                    "bit_count": struct.unpack_from("<I", data, channel_data + 8)[0],
                    "data_type": data[channel_data + 2],
                    "channel_type": data[channel_data],
                    "values": [],
                }
            )
            offset = links[0] if links else 0
    for _, tag, length, _, data_offset in blocks:
        if tag != b"##DT" or not record_size:
            continue
        payload = data[data_offset : data_offset + length - 24]
        usable = len(payload) - (len(payload) % record_size)
        data_payload.extend(payload[:usable])
    if record_size and data_payload:
        for channel in channels:
            offset = channel["byte_offset"]
            if channel["data_type"] not in {4, 5} or channel["bit_count"] not in {32, 64}:
                continue
            width = 8 if channel["bit_count"] == 64 else 4
            values: list[float] = []
            for start in range(0, len(data_payload) - record_size + 1, record_size):
                position = start + offset
                if position + width > len(data_payload):
                    break
                try:
                    values.append(
                        struct.unpack_from(
                            "<d" if width == 8 else "<f", data_payload, position
                        )[0]
                    )
                except struct.error:
                    break
            channel["values"] = values
    for channel in channels:
        channel.update(_stats(channel["values"]))
    return {
        "version": "4",
        "channel_groups": len(groups),
        "record_size": record_size,
        "sample_count": sample_count
        or (len(channels[0]["values"]) if channels else 0),
        "channels": channels,
        "parse_status": "parsed"
        if any(channel["values"] for channel in channels)
        else "metadata-only",
    }


def _find_mdf3_blocks(data: bytes):
    for match in re.finditer(rb"(CG|CN|DG|DT|CC|HD)", data):
        offset = match.start()
        if offset + 6 > len(data):
            continue
        length = struct.unpack_from("<H", data, offset + 2)[0]
        if length < 6 or offset + length > len(data):
            continue
        yield offset, data[offset : offset + 2], length


def _decode_mdf3(data: bytes) -> dict[str, Any]:
    blocks = list(_find_mdf3_blocks(data))
    channels: list[dict[str, Any]] = []
    record_size = 0
    for offset, tag, length in blocks:
        if tag != b"CG":
            continue
        payload = data[offset + 6 : offset + length]
        if len(payload) >= 16:
            candidate = struct.unpack_from("<H", payload, 14)[0]
            if candidate:
                record_size = candidate
        if not record_size and len(payload) >= 2:
            record_size = struct.unpack_from("<H", payload, len(payload) - 2)[0]
    for offset, tag, length in blocks:
        if tag != b"CN":
            continue
        payload = data[offset + 6 : offset + length]
        strings = [
            item.decode("ascii", errors="replace")
            for item in re.findall(rb"[ -~]{3,}", payload)
            if item not in {b"CN", b"CC"} and not item.startswith(b"##")
        ]
        name = next(
            (
                item.strip()
                for item in strings
                if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_ .-]{1,60}", item.strip())
            ),
            f"channel_{len(channels) + 1}",
        )
        channels.append(
            {
                "name": name,
                "group": 1,
                "byte_offset": 8 * len(channels),
                "bit_count": 64,
                "data_type": 4,
                "channel_type": 0,
                "values": [],
            }
        )
    dt = next((item for item in blocks if item[1] == b"DT"), None)
    if dt is not None and record_size:
        offset, _, length = dt
        payload = data[offset + 6 : offset + length]
        for channel in channels:
            values: list[float] = []
            for start in range(0, len(payload) - record_size + 1, record_size):
                position = start + channel["byte_offset"]
                if position + 8 > len(payload):
                    break
                value = struct.unpack_from("<d", payload, position)[0]
                values.append(value if value == value and abs(value) != float("inf") else None)
            channel["values"] = values
    for channel in channels:
        channel.update(_stats(channel["values"]))
    return {
        "version": "3",
        "channel_groups": 1,
        "record_size": record_size,
        "sample_count": len(channels[0]["values"]) if channels else 0,
        "channels": channels,
        "parse_status": "parsed" if any(channel["values"] for channel in channels) else "metadata-only",
    }


def _decode_blf(data: bytes) -> dict[str, Any]:
    channels: dict[int, dict[str, Any]] = {}
    object_types: dict[str, int] = {}
    frames: list[dict[str, Any]] = []
    offset = struct.unpack_from("<I", data, 4)[0] if data.startswith(b"LOGG") else 0
    while offset + 32 <= len(data) and data[offset : offset + 4] == b"LOBJ":
        size = struct.unpack_from("<I", data, offset + 8)[0]
        if size < 32 or offset + size > len(data):
            break
        try:
            payload = zlib.decompress(data[offset + 32 : offset + size])
        except zlib.error:
            payload = b""
        nested = 0
        while payload.startswith(b"LOBJ", nested) and nested + 32 <= len(payload):
            object_size = struct.unpack_from("<I", payload, nested + 8)[0]
            object_type = struct.unpack_from("<I", payload, nested + 12)[0]
            object_types[hex(object_type)] = object_types.get(hex(object_type), 0) + 1
            if object_type == 0x41 and nested + 54 <= len(payload):
                channel = struct.unpack_from("<H", payload, nested + 16)[0]
                frame_id = struct.unpack_from("<I", payload, nested + 20)[0]
                dlc = struct.unpack_from("<I", payload, nested + 32)[0]
                raw = payload[nested + 36 : nested + 36 + min(dlc, 8)].hex().upper()
                timestamp = struct.unpack_from("<Q", payload, nested + 40)[0]
                frames.append(
                    {
                        "channel": channel,
                        "id": frame_id,
                        "dlc": dlc,
                        "data": raw,
                        "timestamp": timestamp,
                    }
                )
                channels.setdefault(
                    channel,
                    {"name": f"CAN{channel}", "frame_count": 0, "ids": {}},
                )
                channels[channel]["frame_count"] += 1
                channels[channel]["ids"][hex(frame_id)] = (
                    channels[channel]["ids"].get(hex(frame_id), 0) + 1
                )
            if object_size <= 0:
                break
            next_nested = payload.find(b"LOBJ", nested + 4)
            if next_nested <= nested:
                break
            nested = next_nested
        offset = (offset + size + 3) & ~3
    channel_rows = [channels[key] for key in sorted(channels)]
    return {
        "version": "BLF",
        "object_types": object_types,
        "frame_count": len(frames),
        "channels": channel_rows,
        "frames": frames,
        "sample_count": len(frames),
        "parse_status": "parsed" if frames else "metadata-only",
    }


def parse_measurement(path: str | Path) -> tuple[dict[str, Any], dict[str, str]]:
    """Return ``channels.json`` content plus per-channel CSV documents."""
    path = Path(path)
    data = path.read_bytes()
    suffix = path.suffix.lower()
    if suffix == ".mf4":
        result = _decode_mdf4(data)
    elif suffix == ".mdf":
        result = _decode_mdf3(data)
    else:
        result = _decode_blf(data)
    documents: dict[str, str] = {}
    for index, channel in enumerate(result["channels"], 1):
        values = channel.pop("values", [])
        name = f"data/{index:04d}_{_slug(channel['name'])}.csv"
        channel["data"] = name
        documents[name] = _csv(values)
    payload = {
        "schema": "ov.matlab.measurement/1",
        "file": path.name,
        "format": suffix.removeprefix("."),
        **result,
        "boundary": "Uncompressed channels are decoded; unknown compressed/vendor blocks are reported, not guessed.",
    }
    documents["channels.json"] = (
        __import__("json").dumps(payload, ensure_ascii=False, indent=2) + "\n"
    )
    return documents, {}
