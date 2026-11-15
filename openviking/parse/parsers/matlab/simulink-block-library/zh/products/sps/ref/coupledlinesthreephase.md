---
type: simulink-block
title: 'Coupled Lines (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Passive / Lines'
documentation_page: 'coupledlinesthreephase'
documentation_source_path: 'ref/coupledlinesthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Coupled Lines (Three-Phase)

## 端口

### 守恒端口

### **~1** — 线路正极端子电气

与线路 *a*、*b* 和 *c* 的正极端子关联的可扩展三相电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Composite three-phase ports`

### **~2** — 线路负极端子电气

与线路 *a*、*b* 和 *c* 的负极端子关联的可扩展三相电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Composite three-phase ports`

### **a1** — 线路 *a* 正极端子电气

与线路 *a* 的正极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`

### **a2** — 线路 *a* 负极端子电气

与线路 *a* 的负极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`

### **b1** — 线路 *b* 正极端子电气

与线路 *b* 的正极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`

### **b2** — 线路 *b* 负极端子电气

与线路 *b* 的负极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`

### **c1** — 线路 *c* 正极端子电气

与线路 *c* 的正极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`

### **c2** — 线路 *c* 负极端子电气

与线路 *c* 的负极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **电气连接** 设置为 `Expanded three-phase ports`

## 参数

### 主要

### **电气连接** — 是对复合三相端口还是扩展三相端口建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是对复合三相端口还是扩展三相端口建模。

复合三相端口使用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口构建与三相电力系统单线图对应的模型。

扩展三相端口使用三个独立的电气守恒端口表示三相系统的各相。

### **参数化** — 线路阻抗参数化 `Balanced impedance`（默认）| `General impedance`

指定如何对三条线路的阻抗进行参数化：

- `Balanced impedance` — 为所有线路指定相同的串联电阻、串联电感和并联泄漏电导。
- `General impedance` — 为每条线路分别指定串联电阻、串联电感和并联泄漏电导。

### **线路 a 电感** — 线路 *a* 自感 `1e-3` `H`（默认）| 正标量

线路 *a* 的自感。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `General impedance`。

### **线路 b 电感** — 线路 *b* 自感 `1e-3` `H`（默认）| 正标量

线路 *b* 的自感。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `General impedance`。

### **线路 c 电感** — 线路 *c* 自感 `1e-3` `H`（默认）| 正标量

线路 *c* 的自感。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `General impedance`。

### **线路电感** — 自感 `1e-3` `H`（默认）| 正标量

线路 *a*、*b* 和 *c* 的自感。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Balanced impedance`。

### **线路 a-b 互感** — *a*-*b* 之间的互感 `3e-4` `H`（默认）| 正标量

线路 *a* 和 *b* 之间的互感。如果已知耦合系数，请将此值设置为 kLaLb。为使互感在物理上可实现，此值必须满足：

−LaLb<Lm,ab<LaLb.

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `General impedance`。

### **线路 b-c 互感** — *b*-*c* 之间的互感 `3e-4` `H`（默认）| 正标量

线路 *b* 和 *c* 之间的互感。如果已知耦合系数，请将此值设置为 kLbLc。为使互感在物理上可实现，此值必须满足：

−LbLc<Lm,bc<LbLc.

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `General impedance`。

### **线路 a-c 互感** — *a*-*c* 之间的互感 `3e-4` `H`（默认）| 正标量

线路 *a* 和 *c* 之间的互感。如果已知耦合系数，请将此值设置为 kLaLc。为使互感在物理上可实现，此值必须满足：

−LaLc<Lm,ac<LaLc.

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `General impedance`。

### **互感** — 互感 `3e-4` `H`（默认）| 正标量

每对线路之间的互感。如果已知耦合系数，请将此值设置为 *kL*，其中 *L* 是每条线路的串联电感。为使互感在物理上可实现，此值必须满足：

−L<Lm<L.

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Balanced impedance`。

### 电阻

### **线路 a 电阻** — 线路 *a* 串联电阻 `0.001` `Ohm`（默认）| 非负标量

线路 *a* 的串联电阻。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `General impedance`。

### **线路 b 电阻** — 线路 *b* 串联电阻 `0.001` `Ohm`（默认）| 非负标量

线路 *b* 的串联电阻。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `General impedance`。

### **线路 c 电阻** — 线路 *c* 串联电阻 `0.001` `Ohm`（默认）| 非负标量

线路 *c* 的串联电阻。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `General impedance`。

### **线路 a-b 互电阻** — *a*-*b* 之间的互电阻 `0` `Ohm`（默认）| 非负标量

*自 R2025a 起*

线路 *a* 和 *b* 之间的互电阻。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `General impedance`。

### **线路 a-c 互电阻** — *a*-*c* 之间的互电阻 `0` `Ohm`（默认）| 非负标量

*自 R2025a 起*

线路 *a* 和 *c* 之间的互电阻。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `General impedance`。

### **线路 b-c 互电阻** — *b*-*c* 之间的互电阻 `0` `Ohm`（默认）| 非负标量

*自 R2025a 起*

线路 *b* 和 *c* 之间的互电阻。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `General impedance`。

### **线路电阻** — 串联电阻 `0.001` `Ohm`（默认）| 非负标量

线路 *a*、*b* 和 *c* 的串联电阻。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Balanced impedance`。

### **互电阻** — 互电阻 `0` `Ohm`（默认）| 非负标量

每对线路之间的互电阻。使用此值来考虑公共返回路径中的损耗。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Balanced impedance`。

### **线路 a 泄漏电导** — 线路 *a* 并联泄漏电导 `1e-9` `1/Ohm`（默认）| 非负标量

线路 *a* 的并联泄漏电导。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `General impedance`。

### **线路 b 泄漏电导** — 线路 *b* 并联泄漏电导 `1e-9` `1/Ohm`（默认）| 非负标量

线路 *b* 的并联泄漏电导。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `General impedance`。

### **线路 c 泄漏电导** — 线路 *c* 并联泄漏电导 `1e-9` `1/Ohm`（默认）| 非负标量

线路 *c* 的并联泄漏电导。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `General impedance`。

### **线路泄漏电导** — 并联泄漏电导 `1e-9` `1/Ohm`（默认）| 非负标量

线路 *a*、*b* 和 *c* 的并联泄漏电导。

#### 依赖关系

要启用此参数，请将 **参数化** 设置为 `Balanced impedance`。

### 故障

### **端口 1 连接故障** — 向端口 1 添加故障的选项 `Add fault`

*自 R2025a 起*

向模块的三相连接端口 **~1** 添加故障的选项。

要添加故障，请点击 **Add fault** 超链接。

### **故障类型** — 故障类型 `Single-phase to ground (a-g)`（默认）| `Single-phase to ground (b-g)` | `Single-phase to ground (c-g)` | `Two-phase (a-b)` | `Two-phase (b-c)` | `Two-phase (c-a)` | `Two-phase to ground (a-b-g)` | `Two-phase to ground (b-c-g)` | `Two-phase to ground (c-a-g)` | `Three-phase (a-b-c)` | `Three-phase to ground (a-b-c-g)`

*自 R2025a 起*

要建模的故障类型。相关参数的可见性取决于故障模型。

#### 依赖关系

要启用此参数，请点击 **端口 1 连接故障** 参数的 **Add fault** 超链接。

### **故障时相线-中性点电阻** — 相线连接与中性点之间的故障电阻 `1e-3` `Ohm`（默认）| 正标量

*自 R2025a 起*

故障激活时，相线连接与中性点之间的电阻。

#### 依赖关系

要启用此参数，请点击 **端口 1 连接故障** 参数的 **Add fault** 超链接，并将 **故障类型** 设置为以下选项之一：

- `Single-phase to ground (a-g)`
- `Single-phase to ground (b-g)`
- `Single-phase to ground (c-g)`
- `Two-phase (a-b)`
- `Two-phase (b-c)`
- `Two-phase (c-a)`
- `Two-phase to ground (a-b-g)`
- `Two-phase to ground (b-c-g)`
- `Two-phase to ground (c-a-g)`
- `Three-phase (a-b-c)`
- `Three-phase to ground (a-b-c-g)`

### **故障时中性点-地电阻** — 中性点与电气参考之间的故障电阻 `1e-3` `Ohm`（默认）| 正标量

*自 R2025a 起*

故障激活时，中性点与电气参考之间的电阻。

#### 依赖关系

要启用此参数，请点击 **端口 1 连接故障** 参数的 **Add fault** 超链接，并将 **故障类型** 设置为以下选项之一：

- `Single-phase to ground (a-g)`
- `Single-phase to ground (b-g)`
- `Single-phase to ground (c-g)`
- `Two-phase to ground (a-b-g)`
- `Two-phase to ground (b-c-g)`
- `Two-phase to ground (c-a-g)`
- `Three-phase to ground (a-b-c-g)`

### **未故障时相线-中性点电导** — 相线连接与中性点之间的未故障电导 `1e-6` `1/Ohm`（默认）| 正标量

*自 R2025a 起*

故障未激活时，相线连接与中性点之间的电导。

#### 依赖关系

要启用此参数，请点击 **端口 1 连接故障** 参数的 **Add fault** 超链接，并将 **故障类型** 设置为以下选项之一：

- `Single-phase to ground (a-g)`
- `Single-phase to ground (b-g)`
- `Single-phase to ground (c-g)`
- `Two-phase (a-b)`
- `Two-phase (b-c)`
- `Two-phase (c-a)`
- `Two-phase to ground (a-b-g)`
- `Two-phase to ground (b-c-g)`
- `Two-phase to ground (c-a-g)`
- `Three-phase (a-b-c)`
- `Three-phase to ground (a-b-c-g)`

### **触发类型** — 触发类型 `Always on`（默认）| `Timed` | `Additional triggers` | `Conditional` | `Manual`

触发类型，指定为以下选项之一：

- `Always On` — 故障在仿真开始时注入。
- `Timed` — 当仿真时间达到您为 **在时间点触发故障** 参数指定的值时，故障注入。
- `Additional triggers` — 故障因模块对话框中不可用的附加触发器而注入。选择此选项，并点击 **Open fault properties** 超链接，以在 Property Inspector 中将 **触发类型** 设置为以下值之一：

  - `Conditional` — 故障因反映与信号关联行为的条件而注入。条件会在每个时间步计算 **Condition** 参数中的布尔表达式。要了解更多信息，请参阅 Create and Manage Conditionals。
  - `Manual` — 当您在 **Fault Dashboard** 窗格中切换状态时，故障注入或清除。要了解更多信息，请参阅 Manually Trigger Faults in Models。

#### 依赖关系

要启用此参数，请点击 **端口 1 连接故障** 参数的 **Add fault** 超链接。

### **在时间点触发故障** — 进入故障状态之前的时间 `0` `s`（默认）| 非负标量

模块进入故障状态的仿真时间。

#### 依赖关系

要启用此参数，请点击 **端口 1 连接故障** 参数的 **Add fault** 超链接，并将 **触发类型** 设置为 `Timed`。

### **触发配置** — 启用附加触发类型的选项 `Open fault properties`

启用模块对话框中不可用的附加触发类型的选项。要将 **触发类型** 参数设置为 `Conditional` 或 `Manual`，请点击 **Open fault properties** 超链接，并在 Property Inspector 中设置 **触发类型**。

要启用此参数，请点击 **端口 1 连接故障** 参数的 **Add fault** 超链接，并将 **触发类型** 设置为 `Additional triggers`。

### **端口 2 连接故障** — 向端口 2 添加故障的选项 `Add fault`

*自 R2025a 起*

向模块的三相连接端口 **~2** 添加故障的选项。

要添加故障，请点击 **Add fault** 超链接。

### **故障类型** — 故障类型 `Single-phase to ground (a-g)`（默认）| `Single-phase to ground (b-g)` | `Single-phase to ground (c-g)` | `Two-phase (a-b)` | `Two-phase (b-c)` | `Two-phase (c-a)` | `Two-phase to ground (a-b-g)` | `Two-phase to ground (b-c-g)` | `Two-phase to ground (c-a-g)` | `Three-phase (a-b-c)` | `Three-phase to ground (a-b-c-g)`

*自 R2025a 起*

要建模的故障类型。相关参数的可见性取决于故障模型。

#### 依赖关系

要启用此参数，请点击 **端口 2 连接故障** 参数的 **Add fault** 超链接。

### **故障时相线-中性点电阻** — 相线连接与中性点之间的故障电阻 `1e-3` `Ohm`（默认）| 正标量

*自 R2025a 起*

故障激活时，相线连接与中性点之间的电阻。

#### 依赖关系

要启用此参数，请点击 **端口 2 连接故障** 参数的 **Add fault** 超链接，并将 **故障类型** 设置为以下选项之一：

- `Single-phase to ground (a-g)`
- `Single-phase to ground (b-g)`
- `Single-phase to ground (c-g)`
- `Two-phase (a-b)`
- `Two-phase (b-c)`
- `Two-phase (c-a)`
- `Two-phase to ground (a-b-g)`
- `Two-phase to ground (b-c-g)`
- `Two-phase to ground (c-a-g)`
- `Three-phase (a-b-c)`
- `Three-phase to ground (a-b-c-g)`

### **故障时中性点-地电阻** — 中性点与电气参考之间的故障电阻 `1e-3` `Ohm`（默认）| 正标量

*自 R2025a 起*

故障激活时，中性点与电气参考之间的电阻。

#### 依赖项

要启用此参数，请单击 **端口 2 连接故障** 参数的 **添加故障** 超链接，并将 **故障类型** 设置为以下选项之一：

- `Single-phase to ground
  (a-g)`
- `Single-phase to ground
  (b-g)`
- `Single-phase to ground
  (c-g)`
- `Two-phase to ground
  (a-b-g)`
- `Two-phase to ground
  (b-c-g)`
- `Two-phase to ground
  (c-a-g)`
- `Three-phase to ground
  (a-b-c-g)`

### **未故障相中性点电导** — 相连接与中性点之间的未故障电导 `1e-6` `1/Ohm` （默认） | positive scalar

*自 R2025a 起*

当故障未激活时，相连接与中性点之间的电导。

#### 依赖项

要启用此参数，请单击 **端口 2 连接故障** 参数的 **添加故障** 超链接，并将 **故障类型** 设置为以下选项之一：

- `Single-phase to ground
  (a-g)`
- `Single-phase to ground
  (b-g)`
- `Single-phase to ground
  (c-g)`
- `Two-phase (a-b)`
- `Two-phase (b-c)`
- `Two-phase (c-a)`
- `Two-phase to ground
  (a-b-g)`
- `Two-phase to ground
  (b-c-g)`
- `Two-phase to ground
  (c-a-g)`
- `Three-phase (a-b-c)`
- `Three-phase to ground
  (a-b-c-g)`

### **触发类型** — 触发类型 `Always on` （默认） | `Timed` | `Additional triggers` | `Conditional` | `Manual`

触发类型，指定为以下选项之一：

- `Always On` — 故障在仿真开始时注入。
- `Timed` — 当仿真时间达到您为 **触发故障时间** 参数指定的值时，故障注入。
- `Additional triggers` — 故障因模块对话框中不可用的附加触发器而注入。选择此选项，并单击 **打开故障属性** 超链接，以在 Property Inspector 中将 **触发类型** 设置为以下值之一：

  - `Conditional` — 故障因反映与信号关联行为的条件而注入。条件会在每个时间步计算 **条件** 参数中的布尔表达式。要了解详细信息，请参阅 Create and Manage Conditionals。
  - `Manual` — 当您在 **Fault Dashboard** 窗格中切换状态时，故障注入或清除。要了解详细信息，请参阅 Manually Trigger Faults in Models。

#### 依赖项

要启用此参数，请单击 **端口 2 连接故障** 参数的 **添加故障** 超链接。

### **触发故障时间** — 进入故障状态前的时间 `0` `s` （默认） | nonnegative scalar

模块进入故障状态时的仿真时间。

#### 依赖项

要启用此参数，请单击 **端口 2 连接故障** 参数的 **添加故障** 超链接，并将 **触发类型** 设置为 `Timed`。

### **触发配置** — 用于启用附加触发器类型的选项 `Open fault properties`

用于启用模块对话框中不可用的附加触发器类型的选项。要将 **触发类型** 参数设置为 `Conditional` 或 `Manual`，请单击 **打开故障属性** 超链接，并在 Property Inspector 中设置 **触发类型**。

要启用此参数，请单击 **端口 2 连接故障** 参数的 **添加故障** 超链接，并将 **触发类型** 设置为 `Additional triggers`。

## 所属库

Simscape / Electrical / Passive / Lines

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2025a：在三相连接端口处建模故障

现在可以在该模块的两个三相连接端口中的每一个端口处建模相对地故障或相间故障。要指定故障电阻和未故障电导的值，请使用 **故障相中性点电阻**、**故障中性点接地电阻** 和 **未故障相中性点电导** 参数。

### R2025a：**建模选项** 参数已更改

**建模选项** 参数已替换为模块对话框或 Property Inspector 中 **Main** 部分内的 **电气连接** 参数。

如果您在较早版本中创建的模型包含此模块，软件会自动将 **电气连接** 参数的值设置为您为 **建模选项** 参数指定的值。

## 描述

磁耦合三相线路

Coupled Lines (Three-Phase) 模块对三条磁耦合线路进行建模。每条线路具有自感、串联电阻和并联电导。此外，每对线路之间存在互感和互电阻。

当三相网络中的磁耦合不可忽略时，请使用此模块。这些效应在以下情况下最为显著：

- 线路平行且彼此靠近。
- 线路的自感较高。
- 网络的交流频率较高。

要对单对线路的磁耦合进行建模，请使用 Coupled Lines (Pair) 模块。要对线路之间的容性耦合进行建模，请使用 Transmission Line 模块。

### 等效电路

等效电路展示两个任意相 *i* 和 *j* 之间的耦合。该模块在三相 *a*、*b* 和 *c* 中的每一对之间使用此类等效电路来建模磁耦合。

在此图中：

- *Ri* 和
  *Rj* 分别是线路 *i* 和 *j*
  的串联电阻。
- *Li* 和
  *Lj* 分别是线路 *i* 和 *j*
  的自感。
- *Rm,ij* 是线路 *i* 和 *j* 之间的互电阻。
- *Lm,ij* 是线路 *i* 和 *j* 之间的互感。
- *Gi* 和
  *Gj* 分别是线路 *i* 和 *j* 的泄漏电导。
- *Vi* 和
  *Vj* 分别是线路 *i* 和 *j* 两端的电压降。
- *Ii* 和
  *Ij* 分别是流过电阻
  *Ri-Rm,ij*
  和
  *Rj-Rm,ij*
  的电流。

### 方程

此模块的定义方程为：

V=[RaRm,abRm,acRm,abRbRm,bcRm,acRm,bcRc]I+[LaLm,abLm,acLm,abLbLm,bcLm,acLm,bcLc]dIdt,

其中：

V=[VaVbVc],

I=[IaIbIc].

*Ia*、
*Ib* 和
*Ic* 通常不等于线路 *a*、*b* 和
*c* 中的电流。这些端子电流构成向量：

Itotal=I+[Ga000Gb000Gc]V.

### 电感耦合

为了量化两条线路之间耦合的强度，可以使用耦合因子或耦合系数 *k*。该耦合因子将互感与线路自感关联起来：

Lm,ij=kLiLj.

该耦合因子必须处于范围 −1<k<1 内，其中负耦合因子表示其中一个线圈的方向反转。*k* 的大小表示：

- |k|=0 — 两条线路之间没有磁耦合。
- 0<|k|<0.5 — 两条线路松耦合，互磁效应较小。
- 0.5≤|k|<1 — 两条线路强耦合，互磁效应较大。

### 互电阻

如果三条线路共享公共返回路径，您可以使用 **互电阻** 参数 *Rm* 来对该返回路径的电阻建模。此工作流程等效于将 **互电阻** 设置为零，并显式建模返回路径电阻 *Rm*，如此图所示。

如果三条线路不共享公共返回路径，请将互电阻参数设置为零，并显式建模每个返回电阻。

### 故障

*自 R2025a 起*

要在 Coupled Lines (Three-Phase) 模块中建模故障，请在 **故障** 部分中，单击要建模的故障旁边的 **添加故障**。有关故障建模的详细信息，请参阅 Fault Behavior Modeling and Fault Triggering。

Coupled Lines (Three-Phase) 模块允许您建模以下类型的故障：

- 单相接地故障 (a-g, b-g, or c-g)
- 两相故障 (a-b, b-c, or c-a)
- 两相接地故障 (a-b-g, b-c-g, or c-a-g)
- 三相故障 (a-b-c)
- 三相接地故障 (a-b-c-g)

您可以在两个三相连接端口中的一个端口处建模故障，也可以同时在两个端口处建模故障。

此图展示该模块如何对两个三相端口处的故障进行建模：

有关向模块添加故障以及指定故障触发器的详细信息，请参阅 Introduction to Simscape Faults。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **初始目标** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量值的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **标称值** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
