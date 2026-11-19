# MATLAB ingest fixture OVPack（不含向量）

- Pack: `matlab-ingest-fixture.ovpack`
- Size: 106,867,510 bytes (101.9 MiB)
- SHA-256: `e8af2b63e3681cca0a8ac8fa6b0b48800c8bea5b9da9be3a613b9cb41aea67c8`
- content_sha256 (inside the pack manifest): `09b2ed60531bcc2104470445271aed157977388b1199053db951021acb4de285`
- OVPack format: version 3, **no dense vector snapshot** (`_ovpack/index_records.jsonl` only)
- Source: `tests/matlab_repos/matlab-ingest-fixture` on `feat/matlab` (commit `4797ae7f9`)
- Resource: `viking://resources/matlab-ingest-fixture`
- Produced by: `ov add-resource <local fixture dir> --to viking://resources/matlab-ingest-fixture`, then `ov export` (without `--include-vectors`)

This pack replaces the with-vectors pack published in commit `4ca811794`; that
one is still downloadable by commit id if needed (see “Previous export” below).

The pack is larger than GitHub's 100 MB per-file limit, so it is stored as two
parts. Concatenate them in order to restore the original file:

```bash
cat matlab-ingest-fixture.ovpack.part0 matlab-ingest-fixture.ovpack.part1 > matlab-ingest-fixture.ovpack
sha256sum matlab-ingest-fixture.ovpack   # e8af2b63e3681cca0a8ac8fa6b0b48800c8bea5b9da9be3a613b9cb41aea67c8
```

| Part | Bytes | SHA-256 |
|---|---|---|
| `artifacts/matlab-ingest-fixture.ovpack.part0` | 72,000,000 | `43ca20bf830427153d038af4ecef0868c05d11d6efa6a382436d2a22f152e3d5` |
| `artifacts/matlab-ingest-fixture.ovpack.part1` | 34,867,510 | `9a7ddbf2a93f027f79a2e3046bc13dbe8d41ce8a9510ac9ec6dad48dbc81ee40` |

## Contents

- 9,581 files and 1,761 directories under the resource root
- 9,581 context records, no vectors stored (importing recomputes them with the
  target's own embedding configuration)
- Every directory has an `.abstract.md` and an `.overview.md` (L0/L1 summaries)
- Import result behind this pack: fixture 2,717 files → 2,644 imported, 73 skipped
  (71 `matlab build/cache`, 2 `matlab derived file`), `failed 0`, `unsupported 0`
- The 99 MB `model/VirtualVehicle/VehicleData/Dictionaries/Environment/entries.jsonl`
  is the parse output of an 18.9 MB `.sldd` and dominates the pack size

The pack is the parsed resource, not a byte-exact copy of the project: `.slx`,
`.sldd`, `.mlx` and similar structured sources are stored as their parse output,
so it cannot be used to reconstruct the original project tree.

## Import

```bash
ov import ./matlab-ingest-fixture.ovpack viking://resources --on-conflict overwrite
```

The parent URI decides where the pack lands; the command above yields
`viking://resources/matlab-ingest-fixture`. Because the pack carries no vector
snapshot, `--vector-mode auto` (default) recomputes vectors on the target.

Prerequisites that this fixture needs, otherwise the import fails:

1. `OPENVIKING_PRIVACY_MAX_CONTENT_BYTES` must exceed 99,365,256 (default 16 MiB)
   or the import fails with `Content exceeds the Privacy sanitizer size limit`.
2. `scipy` (and `h5py` for v7.3 `.mat`) must be installed, otherwise 6
   `.mat`/`.fig` files fail with `MAT parsing requires scipy`.

## Previous export

With vectors (143,376,297 bytes, dense 9,580 × 2048), commit `4ca811794`:

```bash
curl -LO https://raw.githubusercontent.com/zrwangems/OpenViking/4ca811794/artifacts/matlab-ingest-fixture.ovpack.part0
curl -LO https://raw.githubusercontent.com/zrwangems/OpenViking/4ca811794/artifacts/matlab-ingest-fixture.ovpack.part1
```
