# MATLAB ingest fixture OVPack

- Pack: `matlab-ingest-fixture.ovpack`
- Size: 143,376,297 bytes (136.7 MiB)
- SHA-256: `1efc899d21dd8b6299603581961c09c1ab978e5e5f2805c80ec6ec998cab9f3c`
- content_sha256 (inside the pack manifest): `66df5d6eb68ace3cfc8955bf1c0c61b0cd06612fa7851429696fde5969e6f5ef`
- OVPack format: version 3, dense vectors 2048 dimensions
- Source: `tests/matlab_repos/matlab-ingest-fixture` on `feat/matlab`
- Resource: `viking://resources/matlab-ingest-fixture`

The pack is larger than GitHub's 100 MB per-file limit, so it is stored as two
parts. Concatenate them in order to restore the original file:

```bash
cat matlab-ingest-fixture.ovpack.part0 matlab-ingest-fixture.ovpack.part1 > matlab-ingest-fixture.ovpack
sha256sum matlab-ingest-fixture.ovpack   # 1efc899d21dd8b6299603581961c09c1ab978e5e5f2805c80ec6ec998cab9f3c
```

| Part | Bytes | SHA-256 |
|---|---|---|
| `artifacts/matlab-ingest-fixture.ovpack.part0` | 72,000,000 | `0ac8e5dc4dce6e4d4e1271409f7745fb60deae3bb41009e9a8fab463ca0e02cc` |
| `artifacts/matlab-ingest-fixture.ovpack.part1` | 71,376,297 | `fdf3b9e2c02bbb6ed24cbcd98802999c601e15477444e2cea9933d7783b3b178` |

## Contents

- 9,581 files and 1,761 directories under the resource root
- 9,580 context records, every one with a 2048-dimension dense vector
- Every directory has an `.abstract.md` and an `.overview.md` (L0/L1 summaries)
- Per-file parse output as described in `tests/matlab_repos/matlab-ingest-plan.html`
  (`main.json` + subsystem JSON for `.slx`, `entries.jsonl` for `.sldd`,
  `stateflow.json`, `variables.json` + CSVs for `.mat`, `channels.json` for MDF/MF4/BLF,
  manifests for `.mlproj/.mltbx/.mlapp/.sltx/.mlpkginstall/.fmu`,
  `metadata.json` for native binaries, `skipped.json` / `matlab-classification.json`
  for what was excluded)

The pack is the parsed-and-embedded resource, not a byte-exact copy of the
project: `.slx`, `.sldd`, `.sldd` and other structured sources are stored as
their parse output, so it cannot be used to reconstruct the original project tree.

## Import

```bash
ov import ./matlab-ingest-fixture.ovpack viking://resources --on-conflict overwrite
```

- `--vector-mode require` restores the vectors shipped in the pack and does not call
  the embedding model; with `auto` (the default) a differing embedding configuration
  falls back to recomputing all 9,580 records (about 25 minutes).
- `/api/v1/pack/import` is an admin endpoint: a server started with
  `auth_mode = "dev"` answers 403. Use `api_key` or `trusted` mode with `X-API-Key`.

## Import result recorded when the pack was exported

- Fixture files: 2,717 total — 2,644 imported, 73 skipped (71 `matlab build/cache`,
  2 `matlab derived file`), 0 failed, 0 unsupported
- Spot checks: `EvPowertrainController2EM/main.json` has 41 blocks and 39 edges;
  `.sldd` has `entries.jsonl`; Stateflow has `stateflow.json`; `.mat` has
  `variables.json`; MDF/MF4/BLF have `channels.json`

Older packs published on this branch (`chore(matlab): publish the ingest fixture OVPack`
and `chore(matlab): refresh fixture pack with semantic summaries`) were produced
before the plan-level parse output was completed; this one supersedes them.
