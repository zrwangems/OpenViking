# Simulink Block Library

MATLAB/Simulink R2025b 资源添加时使用的本地块参考库。`zh/` 和 `en/` 的顶层库、子目录、块名及顺序严格对应 `scripts/matlab/tree_full.md`；解析器按块原始名称及 `SourceBlock` 匹配文档，无需联网。

- [中文块库](zh/index.md)
- [English block library](en/index.md)

当前包含 75 个顶层库、4736 个块条目，所有真实块条目都有完整中英文官方正文或经逐段中文完整性校验的中文工作译本。Info、Demos、Examples、函数、启动器和产品导航等非块叶子不生成说明页；原树目录保留，真实块与叶子条目一一对应。预配置变体复用对应基础块官方页；少数支持包老块使用页面标注的实际旧版官方文档。

每份正文的 `Ports` / `端口` 和 `Parameters` / `参数` 栏目都以一个 YAML 围栏开头，分别包含 `ports` 和 `parameters` 列表。端口记录提供 `name`、`direction`、`summary`、`data_types`，参数记录提供 `name`、`group`、`summary` 以及官方文档实际给出的 `block_parameter`、`type`、`values`、`default`。字段名在中英文页面保持一致；YAML 后面的 Markdown 完整保留说明、依赖、示例、方程和领域知识，不用固定字段替代正文。

`manifest.json` 是解析器和离线生成脚本使用的机器元数据，不是 OV 资源页面，不另存平行 JSON 正文。重新生成使用 `scripts/matlab/` 下的 R2025b 脚本；`structure_r2025b_block_library.py --check` 校验 YAML 可解析、记录与正文一致、浏览器副本一致且原文无损。缓存和失败日志保存在库目录之外。

## 导入 OpenViking 时的参数

打进资源库时必须一个块一个页面，导入命令要带 `parse_mode=no_split`：

```bash
ov add-resource <language-tree> --to viking://resources/simulink-block-library \
    --args '{"parse_mode":"no_split"}'
```

默认的拆分模式会把一篇文档展开成 `<文档>/<章节>.md`；当章节标题和块名相同时，资源里会出现
`.../LTE_OFDM_Modulator/LTE_OFDM_Modulator/参数.md` 这种同名套两层的目录。`no_split` 下每篇块文档保持
`.../LTE_OFDM_Modulator.md` 一个文件。代码侧对应 `library_pack.INGEST_ARGS`。
