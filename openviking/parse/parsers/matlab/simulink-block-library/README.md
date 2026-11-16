# Simulink Block Library

MATLAB/Simulink R2025b 资源添加时使用的本地块参考库。`zh/` 和 `en/` 是正式 Library Browser 目录，按产品、子库和块组织；解析器按块原始名称及 `SourceBlock` 匹配文档，无需联网。

- [中文块库](zh/index.md)
- [English block library](en/index.md)

当前包含 3899 个库中块条目，中英文正文均已生成。`manifest.json` 是解析器和离线生成脚本使用的机器元数据，不是 OV 资源页面。重新生成使用 `scripts/matlab/` 下的 R2025b 脚本；抓取缓存和失败日志保存在库目录之外。
