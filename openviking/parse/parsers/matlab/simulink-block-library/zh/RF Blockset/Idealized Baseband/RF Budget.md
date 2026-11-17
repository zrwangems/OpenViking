---
type: simulink-block
title: 'RF Budget'
family: 'idealized-baseband'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Idealized Baseband'
documentation_page: 'rfbudget'
documentation_source_path: 'ref/rfbudget.html'
language: zh-CN
chinese_source: worker-translation
---

# RF Budget

## 端口

### 输入

### **Port\_1** — 随时间变化的输入信号 实数标量 | 实数列 | 复数标量 | 复数列

随时间变化的输入信号，指定为实数标量、实数列、复数标量或复数列。列表示连续的时间点。

**数据类型：** `double` | `single`
### 输出

### **Port\_1** — 随时间变化的输出信号 复数标量 | 复数列

随时间变化的输出信号，返回为复数标量或复数列。随时间变化的输出信号的大小与随时间变化的输入信号相同。

**数据类型：** `double` | `single`

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条中，在 **仿真** 选项卡上的
**准备** 库中，选择 **属性检查器**。

### 主要

### **RF 预算源** — RF 预算源 `rfbudget object` (默认) | `RF Budget Analyzer App`

RF 预算源，指定为 `rfbudget object` 或 `RF Budget Analyzer App`。

### **rfbudget object** — 作为源的 `rfbudget` 对象 `rfbudget([],2.1e9,-30,100e6)` (默认) | `rfbudget` 对象

指定一个 `rfbudget` 对象作为源来对失配损耗建模。

#### 依赖关系

要启用此参数，请将 **RF 预算源** 设置为
`rfbudget object`。

### **打开 RF Budget Analyzer App** — 作为源的 RF Budget Analyzer app 按钮

单击此按钮以打开 RF Budget Analyzer app，创建 RF 链并将其用作源来对失配损耗建模。创建您的 RF 链后，单击 **更新模块** 按钮，用设计好的 RF 链更新 RF Budget 模块。

#### 依赖关系

要启用此参数，请将 **RF 预算源** 设置为
`RF Budget Analyzer App`。

### **使用代码生成仿真支持的模块** — 使用生成的 C 代码仿真模型 `off` (默认) | `on`

选择此选项可使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不变，C 代码就会在后续仿真中重用。此选项需要额外的启动时间，但后续仿真的速度比解释执行仿真更快。

### **编辑系统** — 编辑或展开 RF Budget 模块按钮

单击此按钮会断开 RF Budget 模块与库的链接，并将变量替换为该模块使用模块参数估计得到的值。单击此按钮时，软件会转换 RF Budget 模块，使其成为简单的未屏蔽子系统，或者将其展开。

单击此按钮将打开一个对话框，其中包含以下选项：

- **编辑系统** — 在不展开子系统的情况下编辑内部变量。
- **展开系统** — 编辑子系统，并在 Simulink 画布中展开子系统。该模块将展开为元件链。

  **注意**

  如果两个元件是单向且完全匹配的，则不会计算它们之间的失配损耗。
- **取消** — 取消该操作。

**注意**

单击 **编辑系统** 或 **展开系统** 按钮后，无法撤消该操作。

### 高级

### **频率分辨率** — 用于计算失配损耗的频率分辨率 `51` (默认) | 正标量

该模块对失配损耗建模时使用的频率分辨率，指定为正标量。您可以：

- 如果输入信号快速变化，则增大频率分辨率。
- 如果输入信号缓慢变化，则减小频率分辨率。此选项可减少计算时间。
- 如果输入信号恒定，则将频率分辨率设置为 `1`。

### **建模带宽 (Hz)** — 用于计算失配损耗的建模带宽 `100e6` (默认) | 正标量

对失配损耗建模时使用的带宽，指定为正标量。您可以

- 如果输入信号带宽更宽，则增大建模带宽。
- 如果输入信号带宽更窄，则减小建模带宽。在这种情况下，您还可以减小频率分辨率以减少计算时间。

## 所属库

RF Blockset / Idealized Baseband

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

在 Idealized Baseband 仿真环境中仿真 2 端口元件的 RF 预算链

使用 RF Budget 模块在 Idealized Baseband 仿真环境中仿真 2 端口元件链的 RF 预算结果。在仿真 RF 预算时，该模块通过考虑反射和双向功率流的影响来计入失配损耗。可以使用 `rfbudget` 对象，或使用 RF Budget Analyzer app 作为 RF Budget 模块的源。
