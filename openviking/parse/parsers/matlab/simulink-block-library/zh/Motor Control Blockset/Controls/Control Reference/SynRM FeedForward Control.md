---
type: simulink-block
title: 'SynRM FeedForward Control'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'synrmfeedforwardcontrol'
documentation_source_path: 'ref/synrmfeedforwardcontrol.html'
language: zh-CN
chinese_source: worker-translation
---

# SynRM FeedForward Control

## 端口

### 输入

### **Id** — D 轴电流标量

沿旋转 *dq* 参考坐标系 *d* 轴的电流（单位：安培）。

**数据类型：** `single` | `double` | `fixed point`

### **Iq** — Q 轴电流标量

沿旋转 *dq* 参考坐标系 *q* 轴的电流（单位：安培）。

**数据类型：** `single` | `double` | `fixed point`

### **ωm** — 转子机械速度标量

转子的机械速度（单位：rad/s）。

**数据类型：** `single` | `double` | `fixed point`

### **Ld** — D 轴电感标量

D 轴绕组电感（单位：亨利）。

#### 依赖关系

要启用此输入端口，请将 **Motor parameter input method** 设置为 `Input port based Ld and Lq` 或 `Input port based Ld, Lq and FluxPM`。

**数据类型：** `single` | `double` | `fixed point`

### **Lq** — Q 轴电感标量

Q 轴绕组电感（单位：亨利）。

#### 依赖关系

要启用此输入端口，请将 **Motor parameter input method** 设置为 `Input port based Ld and Lq` 或 `Input port based Ld, Lq and FluxPM`。

**数据类型：** `single` | `double` | `fixed point`

### **FluxPM** — 永磁磁链标量

峰值永磁磁链（单位：韦伯）。

#### 依赖关系

要启用此输入端口，请将 **Motor topology** 设置为 `PM-assisted synchronous reluctance motor`，并将 **Motor parameter input method** 设置为 `Input port based Ld, Lq and FluxPM`。

**数据类型：** `single` | `double` | `fixed point`

### **Vsat** — 输出电压饱和限值标量

输出电压 *Vd FF* 和 *Vq FF* 的可变饱和限值（单位：伏特）。

#### 依赖关系

要启用此端口，请将 **Vsat input method** 设置为 `Input port`。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **Vd FF** — D 轴前馈电压增益标量

沿旋转 *dq* 参考坐标系 *d* 轴的前馈电压增益（单位：伏特）。

**数据类型：** `single` | `double` | `fixed point`

### **Vq FF** — Q 轴前馈电压增益标量

沿旋转 *dq* 参考坐标系 *q* 轴的前馈电压增益（单位：伏特）。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### 电机参数

### **Motor topology** — 同步磁阻电机拓扑 `Synchronous reluctance motor`（默认）| `PM-assisted synchronous reluctance motor`

同步磁阻电机的类型。

### **Definition of d-axis and q-axis** — *d* 轴和 *q* 轴的对齐方式 `Ld > Lq (different from PMSM)`（默认）| `Lq > Ld (same as PMSM)`

*d* 轴和 *q* 轴的对齐类型。您可以选择以下选项之一：

- `Ld > Lq (different from PMSM)` — 选择此选项可使用与 PMSM 不同的 *d* 轴和 *q* 轴对齐方式。
- `Lq > Ld (same as PMSM)` — 选择此选项可使用与 PMSM 相同的 *d* 轴和 *q* 轴对齐方式。

有关对齐类型的更多信息，请参阅 SynRM Constraint Curves and Their Application。

### **Number of pole pairs** — 电机中可用的极对数 `4`（默认）| 标量

电机中可用的极对数。

### **Motor parameter input method** — 电机参数类型 `Linear model with lumped parameters`（默认）| `Non-linear model with D,Q-flux linkage LUTs` | `Non-linear model with Ld and Lq LUTs` | `Non-linear model with Ld, Lq and FluxPM LUTs` | `Input port based Ld and Lq` | `Input port based Ld, Lq, and FluxPM`

模块用于生成前馈增益的电机参数。

- `Linear model with lumped parameters` —
  使用电机参数的集中电路值 *Ld*、*Lq* 和 *FluxPM* 生成前馈电压。
- `Non-linear model with D,Q-flux linkage LUTs`
  — 使用 *d* 轴磁链 *FluxD* 和 *q* 轴磁链
  *FluxQ* 查找表（LUT）生成前馈电压。
- `Non-linear model with Ld and Lq LUTs` —
  使用 *Ld* 和
  *Lq* 查找表生成前馈电压，查找表以模块参数形式指定。
- `具有 Ld、Lq 和 FluxPM 的非线性模型
  LUTs` — 使用 *Ld*、
  *Lq* 和 *FluxPM* 查找表生成前馈电压，查找表以模块参数形式指定。
- `Input port based Ld and Lq` — 使用 *Ld* 和 *Lq* 查找表生成前馈电压，查找表以模块输入形式指定。
- `Input port based Ld, Lq, and FluxPM` —
  使用 *Ld*、*Lq* 和 *FluxPM* 查找表生成前馈电压，查找表以模块输入形式指定。

#### 依赖

- 要启用 `Non-linear model with Ld and Lq
  LUTs` 和 `Input port based Ld and
  Lq` 选项，请将 **Motor topology**
  设置为 `Synchronous reluctance motor`。
- 要启用 `Non-linear model with Ld, Lq, and FluxPM
  LUTs` 和 `Input port based Ld, Lq, and
  FluxPM` 选项，请将 **Motor
  topology** 设置为 `PM-assisted synchronous
  reluctance motor`。

### **Vsat input method** — Vsat 输入方法 `Specify via dialog`（默认）| `Input port`

使用以下方法之一指定输出电压饱和限值
（*Vsat*）。

- `Specify via dialog` — 使用 **Output voltage
  saturation (V)** 参数指定固定的输出电压
  饱和限值 *Vsat*。
- `Input port` — 使用输入端口
  **Vsat** 指定可变的输出电压
  饱和限值 *Vsat*。

### **Output saturation (V)** — 输出值的饱和限值 `24/sqrt(3)`（默认）| 标量

输出电压
*Vd
FF* 和 *Vq
FF* 的饱和限值（以伏特为单位）。

#### 依赖

要启用此参数，请将 **Vsat input method** 设置为
`Specify via dialog`。

### **D-axis current breakpoint vector (A)** — D 轴电流查找向量 `[0,10,20,30]`（默认）| 向量

以下查找表中的 D 轴电流向量（以安培为单位），具体取决于
用于指定电机参数的方法。

- *FluxD(id,iq)*
  和
  *FluxQ(id,iq)*
  用于 `Non-linear model with D,Q-flux linkage
  LUTs` 方法。
- *Ld(id,iq)*、
  *Lq(id,iq)*
  和
  *FluxPM(id,iq)*
  用于 `Non-linear model with Ld, Lq, and FluxPM
  LUTs` 方法。

#### 依赖

要启用此参数，请将 **Motor parameter input
method** 设置为 `Non-linear model with D,Q-flux linkage
LUT`、`具有 Ld 和 Lq 的非线性模型
LUTs` 或 `Non-linear model with Ld, Lq, and
FluxPM LUTs`。

### **Q-axis current breakpoint vector (A)** — Q 轴电流查找向量 `[0,10,20,30,40]`（默认）| 向量

以下查找表中的 Q 轴电流向量（以安培为单位），具体取决于
用于指定电机参数的方法。

- *FluxD(id,iq)*
  和
  *FluxQ(id,iq)*
  用于 `Non-linear model with D,Q-flux linkage
  LUTs` 方法。
- *Ld(id,iq)*、
  *Lq(id,iq)*
  和
  *FluxPM(id,iq)*
  用于 `Non-linear model with Ld, Lq, and FluxPM
  LUTs` 方法。

#### 依赖

要启用此参数，请将 **Motor parameter input
method** 设置为 `Non-linear model with D,Q-flux linkage
LUT`、`具有 Ld 和 Lq 的非线性模型
LUTs` 或 `Non-linear model with Ld, Lq, and
FluxPM LUTs`。

### 集总参数线性模型

### **Stator d-axis inductance (H)** — D 轴定子绕组电感 `0.9e-3`（默认）| 标量

沿旋转 *dq* 参考系直轴的定子绕组电感（以亨利为单位）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`。

### **Stator q-axis inductance (H)** — Q轴定子绕组电感 `0.15e-3`（默认值）| 标量

沿旋转 *dq* 参考系交轴的定子绕组电感（单位：亨利）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`。

### **Permanent magnet flux linkage (Wb)** — 永磁体磁链 `6.4e-3`（默认值）| 标量

峰值永磁体磁链（单位：韦伯）。

#### 依赖关系

要启用此参数，请将 **Motor topology** 设置为 `PM-assisted synchronous reluctance motor`，并将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`。

### 带D、Q轴磁链LUT的非线性模型

### **D-axis flux linkage LUT, FluxD(id,iq) (Wb)** — D轴磁链查找数据 `[0,0,0,0,0;0,0,0,0,0.0090;0,0,0,0,0.0180;0,0,0,0,0.0270]`（默认值）| 矩阵

D轴磁链
*FluxD(id,iq)*
查找表数据（单位：韦伯）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with D,Q-flux linkage LUTs`。

### **Q-axis flux linkage LUT, FluxQ(id,iq) (Wb)** — Q轴磁链查找数据 `[0,0,0,0,0.0060;0,0,0,0,0.0060;0,0,0,0,0.0060;0,0,0,0,0.0060]`（默认值）| 矩阵

Q轴磁链
*FluxQ(id,iq)*
查找表数据（单位：韦伯）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with D,Q-flux linkage LUTs`。

### 带 *Ld* 和 *Lq*（以及 *Ld*、*Lq* 和 *FluxPM*）LUT的非线性模型

### **Ld LUT, Ld(id,iq) (H)** — D轴电感查找数据 `0.9e-3 * ones(4, 5)`（默认值）| 矩阵

D轴电感
*Ld(id,iq)*
查找表数据（单位：亨利）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

### **Lq LUT, Lq(id,iq) (H)** — Q轴电感查找数据 `0.15e-3 * ones(4, 5)`（默认值）| 矩阵

Q轴电感
*Lq(id,iq)*
查找表数据（单位：亨利）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

### **PM flux linkage LUT, FluxPM(id,iq) (Wb)** — 永磁体磁链查找数据 `6.4e-3 * ones(4, 5)`（默认值）| 矩阵

永磁体磁链
*FluxPM(id,iq)*
查找表数据（单位：韦伯）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with Ld, Lq and FluxPM LUTs`。

### 输入单位

### **Input units** — 输入值的单位 `Per-Unit (PU)`（默认值）| `SI Units`

输入值的度量单位。

### **Base voltage (V)** — 标称电压限值 `24/sqrt(3)`（默认值）| 标量

标幺值系统的基准电压（单位：伏特）。

#### 依赖关系

要启用此参数，请将 **Input units** 设置为 `Per-Unit (PU)`。

### **Base current (A)** — 标称电流限值 `19.3`（默认值）| 标量

标幺值系统的基准电流（单位：安培）。

#### 依赖关系

要启用此参数，请将 **Input units** 设置为 `Per-Unit (PU)`。

### **Base speed (rpm)** — 标称转速限值 `4107`（默认值）| 标量

标幺值系统的基准转速（单位：rpm）。

#### 依赖关系

要启用此参数，请将 **Input units** 设置为 `Per-Unit (PU)`。

### **Allow scaled-down motor parameters with CodeGen (higher precision with Fixed-Point data type)** — 按标幺值比例缩小内部参数 `on`（默认）| `off`

生成代码时，按标幺值比例缩小内部参数的选项。

- 启用此选项时，模块会按标幺值比例缩小内部常量和系数。这样在使用定点数据类型时可以获得更高的精度。如果将此选项与 single 或 double 数据类型一起使用，根据分配给整数部分的位数，可能会出现一些精度损失。
- 禁用此选项时，模块会将其用于内部计算的所有常量和系数转换为 SI 单位，然后再转换回 PU 比例。这样您就可以更新生成代码中的查找表值，通常用于控制器整定或下线操作等应用。您也可以手动更新这些值，以便调试或复用之前生成的代码。

#### 依赖关系

要启用此参数，请将 **Input units** 设置为
`Per-Unit (PU)`。

## 所属库

Motor Control Blockset / Controls / Control Reference

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

解耦 d 轴和 q 轴电流以消除扰动

SynRM FeedForward Control 模块解耦 *d* 轴
和 *q* 轴电流控制，并生成相应的前馈电压增益，以实现同步磁阻电机 (SynRM)
和永磁辅助同步磁阻电机 (PMaSynRM) 的磁场定向控制。

您可以输入 *d* 轴和 *q* 轴
电流的反馈值以及转子的机械速度。

该模块使用以下方法之一根据指定的电机参数生成前馈增益：

- `Linear model with lumped parameters` — 具有 *d* 轴和 *q* 轴定子绕组
  电感和永磁磁链的集中参数。
- `Non-linear model with D,Q-flux linkage LUTs` — 具有 *d* 轴和 *q* 轴磁链
  查找表的非线性模型。
- `Non-linear model with Ld and Lq LUTs` — 具有 *d* 轴和 *q* 轴定子绕组
  电感查找表的非线性模型。
- `Non-linear model with Ld, Lq, and FluxPM LUTs` —
  具有 *d* 轴和 *q* 轴定子
  绕组电感和永磁磁链查找表的非线性模型。
- `Input port based Ld and Lq` — 通过
  单独输入端口提供 *d* 轴
  和 *q* 轴定子绕组电感值。
- `Input port based Ld, Lq, and FluxPM` —
  通过单独输入端口提供 *d* 轴和 *q* 轴定子绕组电感
  以及永磁磁链值。

此外，您可以使用 **Vsat input method** 参数
将模块配置为通过 **Output
saturation (V)** 参数接受固定饱和电压，或通过单独
输入端口 **Vsat** 接受可变饱和电压。

### 方程

如果在 **Input units** 参数中选择 `Per-Unit (PU)`，则模块默认会按比例缩小内部参数以匹配标幺值尺度。您还可以通过 **Allow scaled-down motor parameters with CodeGen (higher precision with Fixed-Point data type)** 参数，将模块配置为在执行任何计算之前将输入转换为 SI 单位，并在计算输出之后将其转换回标幺值。

这些方程描述了模块如何计算前馈增益。

**注意**

以下针对 SynRM 和 PMaSynRM 的方程遵循与永磁同步电机 (PMSM) 相同的 *d*-*q* 轴记法。

ωe=pωm

对于 SynRM 和 PMaSynRM 两者：

VdFF=−ωeψq=−ωeLqIq

对于 SynRM：

VqFF=ωeψd=ωeLdId

对于 PMSynRM：

VqFF=ωeψd=ωeLdId+ωeψm

其中：

- p 是电机中可用的极对数。
- ωe 是对应于定子电压频率的电角速度 (rad/s)。
- Ld 和 Lq 是 *d* 轴和 *q* 轴定子绕组电感（亨利）。
- Id 和 Iq 是 *d* 轴和 *q* 轴电流（安培）。
- *ψd* 和 *ψq* 是沿 *d-* 轴和 *q*-轴的磁通量（韦伯）。
- *ψm* 是永磁磁链（韦伯）。

有关 Motor Control Blockset™ 用于同步磁阻电机的详细方程组和假设，请参阅 Synchronous Reluctance Machine (Simscape Electrical)。
