# Simulink Block Library

MATLAB/Simulink R2025b 资源添加时使用的本地块参考库。`zh/` 和 `en/` 的顶层库、子目录、块名及顺序严格对应 `scripts/matlab/tree_full.md`；解析器按块原始名称及 `SourceBlock` 匹配文档，无需联网。

- [中文块库](zh/index.md)
- [English block library](en/index.md)

当前包含 75 个顶层库、4792 个块条目。其中 3993 个条目复用完整官方正文，其余 799 个为本机树中有条目、但没有可安全复用独立正文的块，保留真实名称与目录并明确标为 `tree_only`，不猜写端口或参数。

`manifest.json` 是解析器和离线生成脚本使用的机器元数据，不是 OV 资源页面。重新生成使用 `scripts/matlab/` 下的 R2025b 脚本；缓存和失败日志保存在库目录之外。
