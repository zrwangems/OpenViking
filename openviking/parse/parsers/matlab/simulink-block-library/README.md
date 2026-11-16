# Simulink Block Library

MATLAB/Simulink R2025b 资源添加时使用的本地块参考库。`zh/` 和 `en/` 的顶层库、子目录、块名及顺序严格对应 `scripts/matlab/tree_full.md`；解析器按块原始名称及 `SourceBlock` 匹配文档，无需联网。

- [中文块库](zh/index.md)
- [English block library](en/index.md)

当前包含 75 个顶层库、4572 个块条目，所有保留块都有完整中英文官方正文或经结构校验的中文工作译本。实机树中的示例、启动器、产品链接及查无官方块页的条目已按 `r2025b-block-exclusions.json` 剔除，目录层级保持不变。预配置变体复用对应基础块官方页；少数支持包老块使用页面标注的实际旧版官方文档。

`manifest.json` 是解析器和离线生成脚本使用的机器元数据，不是 OV 资源页面。重新生成使用 `scripts/matlab/` 下的 R2025b 脚本；缓存和失败日志保存在库目录之外。
