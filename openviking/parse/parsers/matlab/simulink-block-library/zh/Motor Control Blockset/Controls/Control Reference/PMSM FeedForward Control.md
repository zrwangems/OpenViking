---
type: simulink-block
title: 'PMSM Feed Forward Control'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'pmsmfeedforwardcontrol'
documentation_source_path: 'ref/pmsmfeedforwardcontrol.html'
language: zh-CN
chinese_source: worker-translation
---

# PMSM Feed Forward Control

## 端口

### 输入

### **Id** — D 轴电流标量

沿旋转 *dq* 参考系 *d* 轴的电流（单位：安培）。

**数据类型：** `single` | `double` | `fixed point`

### **Iq** — Q 轴电流标量

沿旋转 *dq* 参考系 *q* 轴的电流（单位：安培）。

**数据类型：** `single` | `double` | `fixed point`

### **ωm** — 转子机械速度标量

转子的机械速度（单位：rad/s）。

**数据类型：** `single` | `double` | `fixed point`

### **Ld** — D 轴电感标量

D 轴绕组电感（单位：亨利）。

#### 依赖

要启用此输入端口，请将 **Motor parameter input method** 设置为 `Input port based Ld, Lq and FluxPM`。

**数据类型：** `single` | `double` | `fixed point`

### **Lq** — Q 轴电感标量

Q 轴绕组电感（单位：亨利）。

#### 依赖

要启用此输入端口，请将 **Motor parameter input method** 设置为 `Input port based Ld, Lq and FluxPM`。

**数据类型：** `single` | `double` | `fixed point`

### **FluxPM** — 永磁体磁链标量

峰值永磁体磁链（单位：韦伯）。

#### 依赖

要启用此输入端口，请将 **Motor parameter input method** 设置为 `Input port based Ld, Lq and FluxPM`。

**数据类型：** `single` | `double` | `fixed point`

### **Vsat** — 输出电压饱和限值标量

输出电压 *VdFF* 和 *VqFF* 的可变饱和限值（单位：伏特）。

#### 依赖

要启用此端口，请将 **Vsat input method** 设置为 `Input port`。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **VdFF** — D 轴前馈电压增益标量

沿旋转 *dq* 参考系 *d* 轴的前馈电压增益（单位：伏特）。

**数据类型：** `single` | `double` | `fixed point`

### **VqFF** — Q 轴前馈电压增益标量

沿旋转 *dq* 参考系 *q* 轴的前馈电压增益（单位：伏特）。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### 电机参数

### **Number of pole pairs** — 电机中可用的极对数 `4`（默认）| 标量

电机中可用的极对数。

### **Motor parameter input method** — 电机参数类型 `Linear model with lumped parameters`（默认）| `Non-linear model with D,Q-flux linkage LUTs` | `Non-linear model with Ld, Lq, and FluxPM LUTs` | `Input port based Ld, Lq, and FluxPM`

模块用于生成前馈增益的电机参数。

- `Linear model with lumped parameters` — 使用电机参数 *Ld*、*Lq* 和 *FluxPM* 的集中电路值生成前馈电压。
- `Non-linear model with D,Q-flux linkage LUTs` — 使用 *d* 轴磁链 *FluxD* 和 *q* 轴磁链 *FluxQ* 查找表（LUT）生成前馈电压。
- `Non-linear model with Ld, Lq, and FluxPM LUTs` — 使用指定为模块参数的 *Ld*、*Lq* 和 *FluxPM* 查找表生成前馈电压。
- `Input port based Ld, Lq, and FluxPM` — 使用指定为模块输入的 *Ld*、*Lq* 和 *FluxPM* 查找表生成前馈电压。

### **Vsat input method** — Vsat 的输入方法 `Specify via dialog`（默认）| `Input port`

使用以下方法之一指定输出电压饱和限值（*Vsat*）。

- `Specify via dialog` — 使用 **Output voltage saturation (V)** 参数指定固定输出电压饱和限值 *Vsat*。
- `Input port` — 使用输入端口 **Vsat** 指定可变输出电压饱和限值 *Vsat*。

### **Output saturation (V)** — 输出值的饱和限值 `24/sqrt(3)`（默认）| 标量

输出电压 *VdFF* 和 *VqFF* 的饱和限值（单位：伏特）。

#### 依赖

要启用此参数，请将 **Vsat input method** 设置为 `Specify via dialog`。

### **D-axis current breakpoint vector (A)** — D 轴电流查找向量 `[-40, -20, 0, 20]`（默认）| 向量

这些查找表中的 D 轴电流向量（单位为安培），取决于你用于指定电机参数的方法。

- *FluxD(id,iq)* 和
  *FluxQ(id,iq)*
  用于 `Non-linear model with D,Q-flux linkage LUTs`
  方法。
- *Ld(id,iq)*、
  *Lq(id,iq)*
  和 *FluxPM(id,iq)*
  用于 `Non-linear model with Ld, Lq, and FluxPM LUTs`
  方法。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method**
设置为 `Non-linear model with D,Q-flux linkage LUTs` 或
`Non-linear model with Ld, Lq, and FluxPM LUTs`。

### **Q-axis current breakpoint vector (A)** — Q 轴电流查找向量 `[-40, -20, 0, 20, 40]`（默认）| 向量

这些查找表中的 Q 轴电流向量（单位为安培），取决于你用于指定电机参数的方法。

- *FluxD(id,iq)* 和
  *FluxQ(id,iq)*
  用于 `Non-linear model with D,Q-flux linkage LUTs`
  方法。
- *Ld(id,iq)*、
  *Lq(id,iq)*
  和 *FluxPM(id,iq)*
  用于 `Non-linear model with Ld, Lq, and FluxPM LUTs`
  方法。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method**
设置为 `Non-linear model with D,Q-flux linkage LUTs` 或
`Non-linear model with Ld, Lq, and FluxPM LUTs`。

### 集总参数线性模型

### **Stator d-axis inductance (H)** — D 轴定子绕组电感 `0.2e-3`（默认）| 标量

旋转 *dq* 参考系直轴上的定子绕组电感（单位为亨利）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method**
设置为 `Linear model with lumped parameters`。

### **Stator q-axis inductance (H)** — Q 轴定子绕组电感 `0.2e-3`（默认）| 标量

旋转 *dq* 参考系交轴上的定子绕组电感（单位为亨利）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method**
设置为 `Linear model with lumped parameters`。

### **Permanent magnet flux linkage (Wb)** — PM 磁链 `6.4e-3`（默认）| 标量

峰值永磁磁链（单位为韦伯）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method**
设置为 `Linear model with lumped parameters`。

### 带 D、Q 磁链 LUT 的非线性模型

### **D-axis flux linkage LUT, FluxD(id,iq) (Wb)** — D 轴磁链查找数据 `[-1.6,-1.6,-1.6,-1.6,-1.6;2.4,2.4,2.4,2.4,2.4;6.4,6.4,6.4,6.4,6.4;10.4,10.4,10.4,10.4,10.4]*1e-3`（默认）| 矩阵

D 轴磁链
*FluxD(id,iq)*
查找表数据（单位为韦伯）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method**
设置为 `Non-linear model with D,Q-flux linkage LUTs`。

### **Q-axis flux linkage LUT, FluxQ(id,iq) (Wb)** — Q 轴磁链查找数据 `[-8,-4,0,4,8;-8,-4,0,4,8;-8,-4,0,4,8;-8,-4,0,4,8]*1e-3`（默认）| 矩阵

Q 轴磁链
*FluxQ(id,iq)*
查找表数据（单位为韦伯）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method**
设置为 `Non-linear model with D,Q-flux linkage LUTs`。

### 带 *Ld*、*Lq* 和 *FluxPM* LUT 的非线性模型

### **Ld LUT, Ld(id,iq) (H)** — D 轴电感查找数据 `0.2e-3 * ones(4, 5)`（默认）| 矩阵

D 轴电感
*Ld(id,iq)*
查找表数据（单位为亨利）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method**
设置为 `Non-linear model with Ld, Lq and FluxPM LUTs`。

### **Lq LUT, Lq(id,iq) (H)** — Q 轴电感查找数据 `0.2e-3 * ones(4, 5)`（默认）| 矩阵

Q 轴电感
*Lq(id,iq)*
查找表数据（单位为亨利）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method**
设置为 `Non-linear model with Ld, Lq and FluxPM LUTs`。

### **PM flux linkage LUT, FluxPM(id,iq) (Wb)** — PM 磁链查找数据 `6.4e-3 * ones(4, 5)`（默认）| 矩阵

永磁磁链
*FluxPM(id,iq)*
查找表数据（单位为韦伯）。

#### 依赖关系

要启用此参数，请将 **电机参数输入方法** 设置为 `Non-linear model with Ld, Lq and FluxPM LUTs`。

### 输入单位

### **输入单位** — 输入值的单位 `Per-Unit (PU)`（默认）| `SI Units`

输入值的测量单位。

### **基准电压 (V)** — 标称电压限值 `24/sqrt(3)`（默认）| 标量

标幺制系统的基准电压（单位：伏特）。

#### 依赖关系

要启用此参数，请将 **输入单位** 设置为 `Per-Unit (PU)`。

### **基准电流 (A)** — 标称电流限值 `19.3`（默认）| 标量

标幺制系统的基准电流（单位：安培）。

#### 依赖关系

要启用此参数，请将 **输入单位** 设置为 `Per-Unit (PU)`。

### **基准转速 (rpm)** — 标称转速限值 `4107`（默认）| 标量

标幺制系统的基准转速（单位：rpm）。

#### 依赖关系

要启用此参数，请将 **输入单位** 设置为 `Per-Unit (PU)`。

### **允许在代码生成时按比例缩小电机参数（使用定点数据类型时精度更高）** — 按比例缩小内部参数以匹配标幺制比例 `on`（默认）| `off`

在生成代码时按比例缩小内部参数以匹配标幺制比例的选项。

- 启用此选项时，模块会按比例缩小内部常量和系数以匹配标幺制比例。这样在使用定点数据类型时可以获得更高的精度。如果将此选项与 single 或 double 数据类型一起使用，根据分配给整数部分的位数，可能会发生一些精度损失。
- 禁用此选项时，模块会将其用于内部计算的所有常量和系数转换为 SI 单位，然后再转换回 PU 比例。这样您就可以更新生成代码中的查找表值，通常用于控制器整定或下线操作等应用。您也可以手动更新这些值，以便调试或重用之前生成的代码。

#### 依赖关系

要启用此参数，请将 **输入单位** 设置为 `Per-Unit (PU)`。

## 所属库

Motor Control Blockset / Controls / Control Reference

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中引入**

## 描述

解耦 d 轴和 q 轴电流以消除扰动

PMSM FeedForward Control 模块解耦 *d* 轴和 *q* 轴电流控制，并生成相应的前馈电压增益，以实现永磁同步电机（PMSM）的磁场定向控制。

您可以输入 *d* 轴和 *q* 轴电流的反馈值以及转子的机械转速。

该模块使用以下方法之一根据指定的电机参数生成前馈增益：

- `Linear model with lumped parameters` — 具有 *d* 轴和 *q* 轴定子绕组电感及永磁体磁链的集中参数模型。
- `Non-linear model with D,Q-flux linkage LUTs` — 具有 *d* 轴和 *q* 轴磁链查找表的非线性模型。
- `Non-linear model with Ld, Lq, and FluxPM LUTs` — 具有 *d* 轴和 *q* 轴定子绕组电感及永磁体磁链查找表的非线性模型。
- `Input port based Ld, Lq, and FluxPM` — 通过单独的输入端口提供 *d* 轴和 *q* 轴定子绕组电感及永磁体磁链值。

此外，您可以使用 **Vsat 输入方法** 参数将模块配置为通过 **输出饱和电压 (V)** 参数接受固定饱和电压，或通过单独的输入端口 **Vsat** 接受可变饱和电压。

### 方程

如果在 **Input units** 参数中选择 `Per-Unit (PU)`，则模块默认会按比例缩小内部参数以匹配标幺值尺度。您还可以通过 **Allow scaled-down motor parameters with CodeGen (higher precision with Fixed-Point data type)** 参数，将模块配置为在执行任何计算之前将输入转换为 SI 单位，并在计算输出后再将其转换回标幺值。

这些方程描述了模块如何计算前馈增益。

ωe=pωm

VdFF=−ωeψq=−ωeLqIq

VqFF=ωeψd=ωeLdId+ωeψm

其中：

- p 是电机中可用的极对数。
- ωe 是对应于定子电压频率的电角速度（rad/s）。
- Ld 和 Lq 是 *d* 轴和 *q* 轴定子绕组电感（henries）。
- Id 和 Iq 是 *d* 轴和 *q* 轴电流（amperes）。
- *ψd* 和 *ψq* 是沿 *d-* 轴和 *q-* 轴的磁通量（weber）。
- *ψm* 是永磁体磁链（weber）。

有关 Motor Control Blockset™ 用于 PMSM 的详细方程组和假设，请参阅 Mathematical Model of PMSM。
