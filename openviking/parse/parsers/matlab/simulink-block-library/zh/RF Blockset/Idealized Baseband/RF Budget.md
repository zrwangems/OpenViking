---
type: simulink-block
title: 'RF Budget'
family: 'simrf'
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

### **Port\_1** — 时变输入信号 实数标量 | 实数列 | 复数标量 | 复数列

时变输入信号，指定为实数标量、实数列、复数标量或复数列。列表示连续的时间点。

**数据类型：** `double` | `single`
### 输出

### **Port\_1** — 时变输出信号 复数标量 | 复数列

时变输出信号，返回为复数标量或复数列。时变输出信号的大小与时变输入信号相等。

**数据类型：** `double` | `single`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的**仿真**选项卡中，在**准备**库中选择**属性检查器**。

### 主要

### **RF budget source** — RF 预算源 `rfbudget object`（默认）| `RF Budget Analyzer App`

RF 预算源，指定为 `rfbudget object` 或 `RF Budget Analyzer App`

### **rfbudget object** — 作为源的 `rfbudget` 对象 `rfbudget([],2.1e9,-30,100e6)`（默认）| `rfbudget` 对象

指定一个 `rfbudget` 对象作为源来对失配损耗进行建模。

#### 依赖关系

要启用此参数，请将 **RF budget source** 设置为 `rfbudget object`。

### **Open RF Budget Analyzer App** — 作为源的 RF Budget Analyzer 应用 按钮

点击此按钮可打开 RF Budget Analyzer 应用以创建 RF 链，并将其用作源来对失配损耗进行建模。创建 RF 链后，点击 **Update Block** 按钮以使用所设计的 RF 链更新 RF Budget 模块。

#### 依赖关系

要启用此参数，请将 **RF budget source** 设置为 `RF Budget Analyzer App`。

### **Simulate supported blocks using code generation** — 使用生成的 C 代码仿真模型 `off`（默认）| `on`

选择此选项可使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。只要模型不发生变化，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间，但后续仿真的速度快于解释执行仿真。

### **Edit System** — 编辑或展开 RF Budget 模块 按钮

点击此按钮可断开 RF Budget 模块与库的链接，并将变量替换为模块使用模块参数估计的值。点击此按钮时，软件会将 RF Budget 模块转换为简单的非封装子系统，或将其展开。

点击此按钮会打开一个对话框，其中包含以下选项：

- **Edit System** — 在不展开子系统的情况下编辑内部变量。
- **Expand System** — 编辑子系统并在 Simulink 画布中展开子系统。该模块将展开为一系列元件。

  **注意**

  如果两个元件是单向且完全匹配的，则不会计算它们之间的失配损耗。
- **Cancel** — 取消操作。

**注意**

点击 **Edit System** 或 **Expand System** 按钮后，无法撤销该操作。

### 高级

### **Frequency resolution** — 用于计算失配损耗的频率分辨率 `51`（默认）| 正标量

模块对失配损耗进行建模的频率分辨率，指定为正标量。您可以：

- 如果输入信号快速变化，则增大频率分辨率。
- 如果输入信号缓慢变化，则减小频率分辨率。此选项可减少计算时间。
- 如果输入信号为常量，则将频率分辨率设置为 `1`。

### **Modeling bandwidth (Hz)** — 用于计算失配损耗的建模带宽 `100e6`（默认）| 正标量

用于建模失配损耗的带宽，指定为正标量。您可以

- 如果您的输入信号带宽更宽，则增大建模带宽。
- 如果您的输入信号带宽更窄，则减小建模带宽。
  在这种情况下，您还可以降低频率分辨率以减少
  计算时间。

## 所属库

RF Blockset / Idealized Baseband

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2025a 中引入**

## 描述

在 Idealized Baseband 仿真环境中仿真 2 端口元件的 RF 预算链

使用 RF Budget 模块在 Idealized Baseband 仿真环境中仿真 2 端口元件链的 RF 预算结果。在仿真 RF 预算时，该模块通过考虑反射和双向功率流的影响来计算失配损耗。您可以使用 `rfbudget` 对象或将 RF Budget Analyzer 应用用作 RF Budget 模块的来源。
