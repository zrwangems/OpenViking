# R2025b Library Browser 对账

## 数量口径

- 公共目录有块库 XML 的产品：74；产品→库→块出现条目：5431。
- 产品内去重文档路径：4603，英文和中文各 4603 份完整正文。此前的 4609 是错误数字，实际为 4603。
- 4603 不是用户本机全部块数，也不是全局不同块名数；同一块可属于多个库，同一文档路径也可被多个块引用。
- 用户截图有 66 个本机顶层入口。旧生成器有 77 个：63 个相同，14 个仅属于公共目录，漏掉 3 个本机入口。现在 Browser 根目录严格保留截图的 66 项及其顺序。

## 旧目录真实差异

| 差异 | 数量 | 项目 |
| --- | ---: | --- |
| 旧 Browser 有、截图无 | 14 | 5G Toolbox, Bluetooth Toolbox, MATLAB Coder, Deep Learning HDL Toolbox, Simscape Fluids, LTE Toolbox, Simulink PLC Coder, Simscape Driveline, Simscape Battery, Simscape Multibody, Simscape Electrical, System Composer, Wireless Testbench, WLAN Toolbox |
| 截图有、旧 Browser 无 | 3 | Motor Control Blockset HDL Support、Report Generator、Simulink Extras |
| 两边都有 | 63 | 60 个公共产品库及 Communications/DSP System/Fixed-Point Designer 3 个 HDL Support 入口 |

## 本机与公开文档边界

- 截图只能证明这 66 个顶层入口，不能证明隐藏子库、第三方自定义库或未展开硬件支持包的完整性。截图中没有可识别的第三方自定义库，不能据此写成第三方库为 0。
- Motor Control Blockset HDL Support 是本机支持库入口；公开目录没有独立 XML。当前只链接关联产品参考文档，不把关联产品块冒充支持库全量。
- Report Generator、Simulink Extras 同样没有独立公共块库 XML，保留入口并明确等待本机枚举。
- 公共 Simulink XML 还含硬件支持文档：236 个出现条目、232 个独立文档路径。它们计入 4603 的公共正文范围，但不因此断言已经安装在用户本机，也不混入截图的 Simulink 基础库目录。
- `zh/`、`en/` 是正文参考存储及旧基础分类；`browser/zh/`、`browser/en/` 才是按截图组织的产品树。`catalog/` 保留所有公共产品，`products/*/ref/` 保存去重正文。
