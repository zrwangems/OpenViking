---
type: simulink-block
title: 'Two-Winding Transformer (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Transformers'
documentation_page: 'twowindingtransformerthreephase'
documentation_source_path: 'ref/twowindingtransformerthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Two-Winding Transformer (Three-Phase)

## 端口

### 守恒端口

### **~1** — 一次绕组电压电气端口

与绕组 1 的三相 [*a1*
*b1*
*c1*] 电压相关联的可扩展三相电气守恒端口。

### **n1** — 一次绕组中性点电气端口

与一次绕组中性点相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding 1 connection
type** 设置为 `Wye with neutral
port`。

### **~2** — 二次绕组电压电气端口

与二次绕组的三相 [*a2*
*b2*
*c2*] 电压相关联的可扩展三相电气守恒端口。

### **n2** — 二次绕组中性点电气端口

与二次绕组中性点相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Winding 2 connection
type** 设置为 `Wye with neutral
port`。

## 参数

### **Modeling option** — 是对复合三相端口还是扩展三相端口进行建模 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是对复合三相端口还是扩展三相端口进行建模。

复合三相端口用单个模块端口表示三个独立的电气守恒端口。您可以使用复合三相端口来构建对应于三相电力系统单线图的模型。

扩展三相端口使用三个独立的电气守恒端口来表示三相系统的各相。

### 主回路

### **Rated apparent power** — 额定容量下的视在功率 `100e6`（默认）| 正标量

变压器在额定容量下运行时流过的视在功率。该值必须大于 `0`。

### **Rated electrical frequency** — 所连接电网的电气频率 `60`（默认）| 正标量

变压器所连接的交流电网的额定频率或标称频率。该值必须大于 `0`。

### **Winding 1 connection type** — 一次绕组配置 `Wye with floating neutral`（默认）| `Wye with neutral port` | `Wye with grounded neutral` | `Delta 1 o'clock` | `Delta 11 o'clock`

一次绕组类型。

### **Primary rated voltage** — 施加到一次绕组的 RMS 线电压 `4160`（默认）| 正标量

在正常工作条件下施加到一次绕组的 RMS 线电压。该值必须大于 `0`。

### **Winding 2 connection type** — 二次绕组配置 `Wye with floating neutral`（默认）| `Wye with neutral port` | `Wye with grounded neutral` | `Delta 1 o'clock` | `Delta 11 o'clock`

二次绕组类型。

### **Secondary rated voltage** — 施加到二次绕组的 RMS 线电压 `24e3`（默认）| 正标量

在正常工作条件下施加到二次绕组的 RMS 线电压。该值必须大于 `0`。

### **Core type** — 铁芯柱数量 `Three-phase three-limb`（默认）| `Three-phase five-limb`

构成磁路的铁芯柱数量。

### 阻抗

### **Primary winding resistance (pu)** — 一次绕组功率损耗 `0.01`（默认）| 正标量

一次绕组的标幺功率损耗。该值必须大于 `0`。

### **Secondary winding resistance (pu)** — 二次绕组功率损耗 `0.01`（默认）| 正标量

二次绕组的标幺功率损耗。该值必须大于 `0`。

### **Leakage reactance** — 漏电抗建模 `Exclude`（默认）| `Include`

是否对磁通损耗进行建模。

### **Primary leakage reactance (pu)** — 一次绕组磁通损耗 `0.001`（默认）| 正标量

一次绕组的标幺磁通损耗。该值必须大于 `0`。

#### 依赖关系

要启用此参数，请将 **Leakage
reactance** 设置为
`Include`。

### **Secondary leakage reactance (pu)** — 二次绕组磁通损耗 `0.001`（默认）| 正标量

二次绕组的标幺磁通损耗。该值必须大于 `0`。

#### 依赖关系

要启用此参数，请将 **Leakage
reactance** 设置为
`Include`。

### **Magnetizing resistance** — 励磁电阻建模 `Exclude`（默认）| `Include`

是否对变压器铁芯损耗进行建模。

### **Shunt magnetizing resistance (pu)** — 变压器铁芯损耗 `500`（默认）| 正标量

变压器铁芯的标幺损耗。该值必须大于 `0`。

#### 依赖关系

要启用此参数，请将 **Magnetizing
resistance** 设置为
`Include`。

### **Magnetizing reactance** — 励磁电抗建模 `Exclude`（默认）| `Include`

是否对变压器铁芯的磁效应进行建模。

### **Magnetic saturation representation** — 磁饱和的表示方式 `None`（默认）| `Lookup table (phi versus i)`

选择是否以及如何表示磁饱和。

#### 依赖关系

要启用此参数，请将 **Magnetizing
reactance** 设置为
`Include`。

### **Current vector (pu), i** — 电流的标幺向量 `[0, .002, 1, 2]`（默认）

电流的标幺向量。第一个值必须为 `0`。此参数必须严格递增。

#### 依赖关系

要启用此参数，请将 **Magnetizing
reactance** 设置为 `Include`，并将
**Magnetic saturation representation** 设置为
`Lookup table (phi versus i)`。

### **Magnetic flux vector (pu), phi** — 磁通的标幺向量 `[0, 1.2, 1.5, 1.51]`（默认）

磁通的标幺向量。第一个值必须为 `0`。此参数必须严格递增。

#### 依赖关系

要启用此参数，请将 **Magnetizing
reactance** 设置为 `Include`，并将
**Magnetic saturation representation** 设置为
`Lookup table (phi versus i)`。

### **Shunt magnetizing reactance (pu)** — 变压器铁芯磁效应 `500`（默认）| 正标量

变压器铁芯在线性区域运行时的标幺磁效应。该值必须大于 `0`。

#### 依赖关系

要启用此参数，请将 **Magnetizing
reactance** 设置为 `Include`，并将
**Magnetic saturation representation** 设置为
`None`。

### **Zero sequence reactance (pu)** — 零序电抗 `0.5`（默认）| 正标量

标幺零序电抗。该值必须大于或等于一次绕组磁通损耗。

#### 依赖关系

要启用此参数，请将 **Core type**（一个
**Main** 参数）设置为 `Three-phase
three-limb`。

## 所属库

Simscape / Electrical / Passive / Transformers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019a 中引入**

## 描述

具有饱和能力的三相线性非理想星形和三角形可配置双绕组变压器

Two-Winding Transformer (Three-Phase) 模块表示一个线性非理想三相双绕组变压器，它通过电磁感应在两个或多个电路之间传输电能。该模块包含线性绕组漏抗和线性铁芯磁化效应。您可以使用标幺值对模块阻抗进行参数化。一次和二次绕组类型、三角形-星形相位角以及铁芯类型均可配置。

一次和二次绕组的配置选项包括：

- Wye with floating neutral — 带 Floating
  Neutral (Three-Phase) 的星形或 T 形配置
- Wye with neutral port — 带 Neutral Port
  (Three-Phase) 的星形或 T 形配置
- Wye with grounded neutral — 带 Grounded
  Neutral (Three-Phase) 的星形或 T 形配置
- Delta 1 o'clock — 相对于所连接星形配置的电压具有滞后 30 度相移的网状配置
- Delta 11 o'clock — 相对于所连接星形配置的电压具有超前 30 度相移的网状配置

铁芯类型的选项包括：

- Three-phase five-limb
- Three-phase three-limb

尽管三柱铁芯通常成本较低，但五柱铁芯具有以下优势：

- 在不平衡负载情况下，即线路与中性点之间的零序电流分量阻抗更低
- 散热更好

### 方程

**三柱铁芯**

此模块在磁域中使用基本磁阻、绕组和涡流模块实现。

确定模块掩码中的电域参数与模型中所用磁域参数之间的关系非常重要：

- *n1* 是一次绕组匝数。
- *n2* 是二次绕组匝数。
- *Lm* 是并联励磁电感。
- *L0* 是零序电感。
- *Lp* 是一次绕组漏电感。
- *Ls* 是二次绕组漏电感。
- *Rm* 是并联励磁电阻。
- *R* 是相间励磁磁阻。

  R=n12Lm
- *R0* 是零序磁阻。

  R0=13n12L0−Lp
- *Rl1* 是一次绕组漏磁阻。

  Rl1=n12Lp
- *Rl2* 是二次绕组漏磁阻。

  Rl2=n22Ls
- *Leddy* 是涡流回路电导

  Leddy=n12Rm

对于双绕组变压器（三相），每相中不同绕组之间的耦合是相同的。

**五柱铁芯**

对于五柱变压器，额外铁芯柱提供的额外磁通路径可以用零序磁阻表示，这些磁阻最初是为三柱变压器中通过空气的磁路设计的。

在五柱模型中，从各相到额外铁芯柱的磁阻假定等于相间磁阻。

R=R0

因此我们推导出：

R=R0=n12Lm

### 显示选项

您可以使用模块上下文菜单在 MATLAB® 命令窗口中显示变压器标幺基准值。要显示这些值，请右键单击模块并选择 **Electrical** > **Display Base Values**。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或属性检查器中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。您可以使用不同的来源指定标称值，包括模块对话框或属性检查器中的 **Nominal
Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
