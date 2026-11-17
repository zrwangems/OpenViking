# Simulink Block Library

MATLAB/Simulink R2025b 资源添加时使用的本地块参考库。`zh/` 和 `en/` 的顶层库、子目录、块名及顺序严格对应 `scripts/matlab/tree_full.md`；解析器按块原始名称及 `SourceBlock` 匹配文档，无需联网。

- [中文块库](zh/index.md)
- [English block library](en/index.md)

当前包含 75 个顶层库、4792 个块条目，所有原树条目都有完整中英文官方正文或经逐段中文完整性校验的中文工作译本。示例、启动器和产品链接保留原路径并复用对应官方主题页；原树无删减，目录层级和叶子条目一一对应。预配置变体复用对应基础块官方页；少数支持包老块使用页面标注的实际旧版官方文档。

`manifest.json` 是解析器和离线生成脚本使用的机器元数据，不是 OV 资源页面。重新生成使用 `scripts/matlab/` 下的 R2025b 脚本；缓存和失败日志保存在库目录之外。
