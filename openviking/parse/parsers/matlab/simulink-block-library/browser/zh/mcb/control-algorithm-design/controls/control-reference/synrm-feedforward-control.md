---
type: simulink-block
title: 'SynRM FeedForward Control'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Control Algorithm Design / Controls / Control Reference'
documentation_page: 'synrmfeedforwardcontrol'
documentation_source_path: 'ref/synrmfeedforwardcontrol.html'
language: zh-CN
chinese_source: worker-translation
---

# SynRM FeedForward Control

## 端口

### 输入

### **Id** — d 轴电流标量

沿旋转 *dq* 参考系的 *d* 轴的电流（单位：amperes）。

**数据类型：** `single` | `double` | `fixed point`

### **Iq** — q 轴电流标量

沿旋转 *dq* 参考系的 *q* 轴的电流（单位：amperes）。

**数据类型：** `single` | `double` | `fixed point`

### **ωm** — 转子机械转速标量

转子的机械转速（单位：rad/s）。

**数据类型：** `single` | `double` | `fixed point`

### **Ld** — d 轴电感标量

d 轴绕组电感（单位：henries）。

#### 依赖项

要启用此输入端口，请将 **Motor parameter input method** 设置为 `Input port based Ld and Lq` 或 `Input port based Ld, Lq and FluxPM`。

**数据类型：** `single` | `double` | `fixed point`

### **Lq** — q 轴电感标量

q 轴绕组电感（单位：henries）。

#### 依赖项

要启用此输入端口，请将 **Motor parameter input method** 设置为 `Input port based Ld and Lq` 或 `Input port based Ld, Lq and FluxPM`。

**数据类型：** `single` | `double` | `fixed point`

### **FluxPM** — 永磁体磁链标量

峰值永磁体磁链（单位：weber）。

#### 依赖项

要启用此输入端口，请将 **Motor topology** 设置为 `PM-assisted synchronous reluctance motor`，并将 **Motor parameter input method** 设置为 `Input port based Ld, Lq and FluxPM`。

**数据类型：** `single` | `double` | `fixed point`

### **Vsat** — 输出电压饱和限值标量

输出电压 *Vd FF* 和 *Vq FF* 的可变饱和限值（单位：volts）。

#### 依赖项

要启用此端口，请将 **Vsat input method** 设置为 `Input port`。

**数据类型：** `single` | `double` | `fixed point`

### 输出

### **Vd FF** — d 轴前馈电压增益标量

沿旋转 *dq* 参考系的 *d* 轴的前馈电压增益（单位：volts）。

**数据类型：** `single` | `double` | `fixed point`

### **Vq FF** — q 轴前馈电压增益标量

沿旋转 *dq* 参考系的 *q* 轴的前馈电压增益（单位：volts）。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### 电机参数

### **Motor topology** — 同步磁阻电机拓扑 `Synchronous reluctance motor` (default) | `PM-assisted synchronous reluctance motor`

同步磁阻电机的类型。

### **Definition of d-axis and q-axis** — *d* 轴和 *q* 轴的对齐 `Ld > Lq (different from PMSM)` (default) | `Lq > Ld (same as PMSM)`

*d* 轴和 *q* 轴的对齐类型。您可以选择以下选项之一：

- `Ld > Lq (different from PMSM)` — 选择此选项可使用不同于 PMSM 的 *d* 轴和 *q* 轴对齐。
- `Lq > Ld (same as PMSM)` — 选择此选项可使用与 PMSM 相同的 *d* 轴和 *q* 轴对齐。

有关对齐类型的更多信息，请参阅 SynRM 约束曲线及其应用。

### **Number of pole pairs** — 电机中可用的极对数 `4` (default) | scalar

电机中可用的极对数。

### **Motor parameter input method** — 电机参数类型 `Linear model with lumped parameters` (default) | `Non-linear model with D,Q-flux linkage LUTs` | `Non-linear model with Ld and Lq LUTs` | `Non-linear model with Ld, Lq and FluxPM LUTs` | `Input port based Ld and Lq` | `Input port based Ld, Lq, and FluxPM`

模块用于生成前馈增益的电机参数。

- `Linear model with lumped parameters` — 使用电机参数 *Ld*、*Lq* 和 *FluxPM* 的集总电路值生成前馈电压。
- `Non-linear model with D,Q-flux linkage LUTs` — 使用 *d* 轴磁链 *FluxD* 和 *q* 轴磁链 *FluxQ* 查找表（LUT）生成前馈电压。
- `Non-linear model with Ld and Lq LUTs` — 使用指定为模块参数的 *Ld* 和 *Lq* LUT 生成前馈电压。
- `Non-linear model with Ld, Lq and FluxPM LUTs` — 使用指定为模块参数的 *Ld*、*Lq* 和 *FluxPM* LUT 生成前馈电压。
- `Input port based Ld and Lq` — 使用指定为模块输入的 *Ld* 和 *Lq* LUT 生成前馈电压。
- `Input port based Ld, Lq, and FluxPM` — 使用指定为模块输入的 *Ld*、*Lq* 和 *FluxPM* LUT 生成前馈电压。

#### 依赖项

- 要启用 `Non-linear model with Ld and Lq LUTs` 和 `Input port based Ld and Lq` 选项，请将 **Motor topology** 设置为 `Synchronous reluctance motor`。
- 要启用 `Non-linear model with Ld, Lq, and FluxPM LUTs` 和 `Input port based Ld, Lq, and FluxPM` 选项，请将 **Motor topology** 设置为 `PM-assisted synchronous reluctance motor`。

### **Vsat input method** — Vsat 的输入方法 `Specify via dialog` (default) | `Input port`

使用以下方法之一指定输出电压饱和限值（*Vsat*）。

- `Specify via dialog` — 使用 **Output voltage saturation (V)** 参数指定固定输出电压饱和限值 *Vsat*。
- `Input port` — 使用输入端口 **Vsat** 指定可变输出电压饱和限值 *Vsat*。

### **Output saturation (V)** — 输出值的饱和限值 `24/sqrt(3)` (default) | scalar

输出电压 *Vd FF* 和 *Vq FF* 的饱和限值（单位：volts）。

#### 依赖项

要启用此参数，请将 **Vsat input method** 设置为 `Specify via dialog`。

### **D-axis current breakpoint vector (A)** — d 轴电流查找向量 `[0,10,20,30]` (default) | vector

这些查找表中的 d 轴电流向量（单位：amperes），具体取决于您用于指定电机参数的方法。

- 对于 `Non-linear model with D,Q-flux linkage LUTs` 方法，为 *FluxD(id,iq)* 和 *FluxQ(id,iq)*。
- 对于 `Non-linear model with Ld, Lq, and FluxPM LUTs` 方法，为 *Ld(id,iq)*、*Lq(id,iq)* 和 *FluxPM(id,iq)*。

#### 依赖项

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with D,Q-flux linkage LUTs`、`Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

### **Q-axis current breakpoint vector (A)** — q 轴电流查找向量 `[0,10,20,30,40]` (default) | vector

这些查找表中的 q 轴电流向量（单位：amperes），具体取决于您用于指定电机参数的方法。

- 对于 `Non-linear model with D,Q-flux linkage LUTs` 方法，为 *FluxD(id,iq)* 和 *FluxQ(id,iq)*。
- 对于 `Non-linear model with Ld, Lq, and FluxPM LUTs` 方法，为 *Ld(id,iq)*、*Lq(id,iq)* 和 *FluxPM(id,iq)*。

#### 依赖项

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with D,Q-flux linkage LUTs`、`Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

### 集总参数线性模型

### **Stator d-axis inductance (H)** — d 轴定子绕组电感 `0.9e-3` (default) | scalar

沿旋转 *dq* 参考系直轴的定子绕组电感（单位：henries）。

#### 依赖项

要启用此参数，请将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`。

### **Stator q-axis inductance (H)** — q 轴定子绕组电感 `0.15e-3` (default) | scalar

沿旋转 *dq* 参考系交轴的定子绕组电感（单位：henries）。

#### 依赖项

要启用此参数，请将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`。

### **Permanent magnet flux linkage (Wb)** — PM 磁链 `6.4e-3` (default) | scalar

峰值永磁体磁链（单位：weber）。

#### 依赖项

要启用此参数，请将 **Motor topology** 设置为 `PM-assisted synchronous reluctance motor`，并将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`。

### 采用 D,Q 磁链 LUT 的非线性模型

### **D-axis flux linkage LUT, FluxD(id,iq) (Wb)** — d 轴磁链查找数据 `[0,0,0,0,0;0,0,0,0,0.0090;0,0,0,0,0.0180;0,0,0,0,0.0270]` (default) | matrix

d 轴磁链 *FluxD(id,iq)* 查找表数据（单位：weber）。

#### 依赖项

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with D,Q-flux linkage LUTs`。

### **Q-axis flux linkage LUT, FluxQ(id,iq) (Wb)** — q 轴磁链查找数据 `[0,0,0,0,0.0060;0,0,0,0,0.0060;0,0,0,0,0.0060;0,0,0,0,0.0060]` (default) | matrix

q 轴磁链 *FluxQ(id,iq)* 查找表数据（单位：weber）。

#### 依赖项

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with D,Q-flux linkage LUTs`。

### 采用 *Ld* 和 *Lq*（以及 *Ld*、*Lq* 和 *FluxPM*）LUT 的非线性模型

### **Ld LUT, Ld(id,iq) (H)** — d 轴电感查找数据 `0.9e-3 * ones(4, 5)` (default) | matrix

d 轴电感 *Ld(id,iq)* 查找表数据（单位：henries）。

#### 依赖项

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

### **Lq LUT, Lq(id,iq) (H)** — q 轴电感查找数据 `0.15e-3 * ones(4, 5)` (default) | matrix

q 轴电感 *Lq(id,iq)* 查找表数据（单位：henries）。

#### 依赖项

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

### **PM flux linkage LUT, FluxPM(id,iq) (Wb)** — PM 磁链查找数据 `6.4e-3 * ones(4, 5)` (default) | matrix

永磁体磁链 *FluxPM(id,iq)* 查找表数据（单位：weber）。

#### 依赖项

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with Ld, Lq and FluxPM LUTs`。

### 输入单位

### **Input units** — 输入值的单位 `Per-Unit (PU)` (default) | `SI Units`

输入值的度量单位。

### **Base voltage (V)** — 标称电压限值 `24/sqrt(3)` (default) | scalar

标幺制系统的基准电压（单位：volts）。

#### 依赖项

要启用此参数，请将 **Input units** 设置为 `Per-Unit (PU)`。

### **Base current (A)** — 标称电流限值 `19.3` (default) | scalar

标幺制系统的基准电流（单位：amperes）。

#### 依赖项

要启用此参数，请将 **Input units** 设置为 `Per-Unit (PU)`。

### **Base speed (rpm)** — 标称速度限值 `4107` (default) | scalar

标幺制系统的基准速度（单位：rpm）。

#### 依赖项

要启用此参数，请将 **Input units** 设置为 `Per-Unit (PU)`。

### **Allow scaled-down motor parameters with CodeGen (higher precision with Fixed-Point data type)** — 缩小内部参数以匹配标幺尺度 `on` (default) | `off`

用于在生成代码时缩小内部参数以匹配标幺尺度的选项。

- 启用此选项时，模块会缩小内部常量和系数以匹配标幺尺度。这样在使用定点数据类型时可获得更高精度。如果将此选项与 single 或 double 数据类型一起使用，则根据分配给整数部分的位数，可能会发生一些精度损失。
- 禁用此选项时，模块会将其用于内部计算的所有常量和系数转换为 SI 单位，然后再转换回 PU 尺度。这样，您可以更新生成代码中的查找表值，通常用于控制器调优或下线操作等应用。您也可以手动更新这些值，以便调试或重用之前生成的代码。

#### 依赖项

要启用此参数，请将 **Input units** 设置为 `Per-Unit (PU)`。

## 所属库

Motor Control Blockset / Controls / Control Reference

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

解耦 d 轴和 q 轴电流以消除扰动

SynRM FeedForward Control 模块解耦 *d* 轴和 *q* 轴电流控制，并生成相应的前馈电压增益，以实现同步磁阻电机 (SynRM) 和永磁辅助同步磁阻电机 (PMaSynRM) 的磁场定向控制。

您可以输入 *d* 轴和 *q* 轴电流以及转子机械转速的反馈值。

模块使用以下方法之一，根据指定的电机参数生成前馈增益：

- `Linear model with lumped parameters` — 具有 *d* 轴和 *q* 轴定子绕组电感以及永磁体磁链的集总参数。
- `Non-linear model with D,Q-flux linkage LUTs` — 具有 *d* 轴和 *q* 轴磁链查找表的非线性模型。
- `Non-linear model with Ld and Lq LUTs` — 具有 *d* 轴和 *q* 轴定子绕组电感查找表的非线性模型。
- `Non-linear model with Ld, Lq, and FluxPM LUTs` — 具有 *d* 轴和 *q* 轴定子绕组电感以及永磁体磁链查找表的非线性模型。
- `Input port based Ld and Lq` — 使用单独输入端口提供的 *d* 轴和 *q* 轴定子绕组电感值。
- `Input port based Ld, Lq, and FluxPM` — 使用单独输入端口提供的 *d* 轴和 *q* 轴定子绕组电感以及永磁体磁链值。

此外，您可以使用 **Vsat input method** 参数将模块配置为通过 **Output saturation (V)** 参数接受固定饱和电压，或通过单独的输入端口 **Vsat** 接受可变饱和电压。

### 方程

如果您在 **Input units** 参数中选择 `Per-Unit (PU)`，则默认情况下，模块会缩小内部参数以匹配标幺尺度。您还可以使用 **Allow scaled-down motor parameters with CodeGen (higher precision with Fixed-Point data type)** 参数，将模块配置为在执行任何计算之前将输入转换为 SI 单位，并在计算输出后将其转换回标幺值。

这些方程描述模块如何计算前馈增益。

**注意**

以下用于 SynRM 和 PMaSynRM 的方程遵循与永磁同步电机 (PMSM) 相同的 *d*-*q* 轴表示法。

ωe=pωm

对于 SynRM 和 PMaSynRM 两者：

VdFF=−ωeψq=−ωeLqIq

对于 SynRM：

VqFF=ωeψd=ωeLdId

对于 PMSynRM：

VqFF=ωeψd=ωeLdId+ωeψm

其中：

- p 是电机中可用的极对数。
- ωe 是对应于定子电压频率的电速度（单位：rad/s）。
- Ld 和 Lq 是 *d* 轴和 *q* 轴定子绕组电感（单位：henries）。
- Id 和 Iq 是 *d* 轴和 *q* 轴电流（单位：amperes）。
- *ψd* 和 *ψq* 是沿 *d-* 和 *q* 轴的磁通（单位：weber）。
- *ψm* 是永磁体磁链（单位：weber）。

有关 Motor Control Blockset™ 用于同步磁阻电机的详细方程组和假设，请参阅 Synchronous Reluctance Machine (Simscape Electrical)。
