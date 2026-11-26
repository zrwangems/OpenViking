# slxkeydes

每个块描述 key 一份模板，中英各一套，供 `.slx` / `.mdl` 入库时渲染块描述。本目录是
`openviking-engineering-resources` 仓库 `matlab/simulink/slxkeydes/` 的原样副本
（`en/` 与 `zh/` 两个子树、`index.json` 及每 key 一个 JSON），随包分发，导入时不需要
再拉别的仓库。要换一套模板，把 `OPENVIKING_MATLAB_KEYDES_DIR` 指向另一个含
`en/index.json` 与 `zh/index.json` 的目录即可。

```text
slxkeydes/
├── en/                       英文模板，3,372 个 key
│   ├── index.json            key → 文件、工具箱、变体数、参数数
│   └── <工具箱>/<key>.json
└── zh/                       中文模板，key 与 en 一一对应
    ├── index.json
    └── <工具箱>/<key>.json
```

模板文件的字段（`key`、`title`、`toolbox`、`kind`、`source_docs`、`text`、`variants`、
`ports`、`params`）和写法规则见上游仓库的 `matlab/simulink/slxkeydes/README.md`。这个
分支只用而不改它们：`text` 是带 `{参数名}` 占位符的一句话，`variants[].when` 是开关型
参数的取值组合，`params[].default` 是实例没带该参数时的取值。

## 渲染

`openviking/parse/parsers/matlab/keydes.py` 做三件事：

1. `block_keys.py` 按块算出 key（`SourceType` → `SourceBlock` 末段 → `BlockType`），
   key 决定用哪个模板；`SubSystem` 没有 key，子系统由解析器展开成下层的 JSON。
2. 参数绑定：模板里的参数名是文档里的写法（`Port number`、`Table data`、
   `Sample time (-1 for inherited)`），SLX 里存的是 API 标识（`Port`、`Table`、
   `SampleTime`）。先按小写字母数字比对（去掉首个括号后的部分）取完全相同者，再取互为前缀者，
   共享前缀最长优先、一个实例参数只用一次，仍然分不清就退回模板默认值，不猜。
   中文模板的参数名和默认值都是译过的，所以绑定一律按同 key 的英文模板取名字和默认值。
3. 渲染：占位符换成实例值（实例没有就用默认值）；值超过 120 字符截断；一段里没有任何值、
   或者整段只有一个值没有文字时，整段丢掉，避免出现「、[]、」这种残句。

默认用中文模板渲染（`language="zh"`），导入时 `--args language:en` 改走英文模板。

结果写进每个系统 JSON 的 `blocks[].description`，`blocks[].key` 记录渲染用的是哪个 key。
没有模板的块（不在文档覆盖里的第三方库块，如 `autolibutils/LPF IC`）`description` 留空，
`coverage.blocks_without_description` 列出这些 key，`coverage.described_blocks` 计数。

## 覆盖

模板覆盖 4,690 个库块算出的 3,372 个 key。实测 `tests/matlab_repos/matlab-ingest-fixture`
里 260 个 `.slx`、43,491 个块，39,643 个块（91.2%）渲染出描述，其余是子系统块和
没有文档的第三方库块。
