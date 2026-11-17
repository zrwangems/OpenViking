---
type: simulink-block
title: 'PMSM Torque Estimator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'pmsmtorqueestimator'
documentation_source_path: 'ref/pmsmtorqueestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# PMSM Torque Estimator

## 端口

### 输入

### **Id** — D 轴电流标量

沿旋转 *dq* 参考系 *d* 轴的电流。

该端口的单位取决于 **Input units** 参数值。如果将该参数设置为 `SI Units`，则该端口接受以安培为单位的输入信号。

**数据类型：** `single` | `double` | `fixed point`

### **Iq** — Q 轴电流标量

沿旋转 *dq* 参考系 *q* 轴的电流。

该端口的单位取决于 **Input units** 参数值。如果将该参数设置为 `SI Units`，则该端口接受以安培为单位的输入信号。

**数据类型：** `single` | `double` | `fixed point`

### **ωm** — 转子机械转速标量

转子的机械转速。

该端口的单位取决于 **Input units** 参数值。如果将该参数设置为 `SI Units`，则该端口接受以 rad/s 为单位的输入信号。

**数据类型：** `single` | `double` | `fixed point`

### **Ld** — D 轴电感标量

D 轴绕组电感。

该端口的单位取决于 **Input units** 参数值。如果将该参数设置为 `SI Units`，则该端口接受以亨利为单位的输入信号。

#### 依赖

要启用此输入端口，请将 **Motor parameter input method** 设置为 `Input port based Ld, Lq, and FluxPM`。

**数据类型：** `single` | `double` | `fixed point`

### **Lq** — Q 轴电感标量

Q 轴绕组电感（单位为亨利）。

该端口的单位取决于 **Input units** 参数值。如果将该参数设置为 `SI Units`，则该端口接受以亨利为单位的输入信号。

#### 依赖

要启用此输入端口，请将 **Motor parameter input method** 设置为 `Input port based Ld, Lq, and FluxPM`。

**数据类型：** `single` | `double` | `fixed point`

### **FluxPM** — 永磁体磁链标量

峰值永磁体磁链。

该端口的单位取决于 **Input units** 参数值。如果将该参数设置为 `SI Units`，则该端口接受以韦伯为单位的输入信号。

#### 依赖

要启用此输入端口，请将 **Motor parameter input method** 设置为 `Input port based Ld, Lq, and FluxPM`。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **Te** — 估算转矩标量

电机的机械转矩输出。

该端口的单位取决于由 **Input units** 参数定义的模块输入单位。如果将该参数设置为 `SI Units`，则该端口输出以 Nm 为单位的信号。

**数据类型：** `single` | `double` | `fixed point`

### **Pe** — 估算功率标量

电机的功率输出。

该端口的单位取决于由 **Input units** 参数定义的模块输入单位。如果将该参数设置为 `SI Units`，则该端口输出以瓦特为单位的信号。

**数据类型：** `single` | `double` | `fixed point`

## 参数

#### 电机参数

### **Number of pole pairs** — 电机中可用的极对数 `4`（默认）| 标量

电机中可用的极对数。

### **Motor parameter input method** — 电机参数类型 `Linear model with lumped parameters`（默认）| `Non-linear model with D,Q-flux linkage LUTs` | `Non-linear model with Ld, Lq, and FluxPM LUTs` | `Input port based Ld, Lq, and FluxPM`

模块用于生成转矩和功率估算的电机参数。

- `Linear model with lumped parameters` — 使用电机参数 *Ld*、*Lq* 和 *FluxPM* 的集中电路值生成估算。
- `Non-linear model with D,Q-flux linkage LUTs` — 使用 *d* 轴磁链 *FluxD* 和 *q* 轴磁链 *FluxQ* 查找表（LUT）生成估算。
- `Non-linear model with Ld, Lq, and FluxPM LUTs` — 使用指定为模块参数的 *Ld*、*Lq* 和 *FluxPM* LUT 生成估算。
- `Input port based Ld, Lq, and FluxPM` — 使用指定为模块输入的 *Ld*、*Lq* 和 *FluxPM* LUT 生成估算。

### **D 轴电流断点向量，id (A)** — D 轴电流查找向量 `[-40, -20, 0, 20]`（默认）| 向量

用于以下查找表的 D 轴电流向量，具体取决于用于指定电机参数的方法。

- 对于 `Non-linear model with D,Q-flux linkage LUTs` 方法，用于 *FluxD(id,iq)* 和 *FluxQ(id,iq)*。
- 对于 `Non-linear model with Ld, Lq, and FluxPM LUTs` 方法，用于 *Ld(id,iq)*、*Lq(id,iq)* 和 *FluxPM(id,iq)*。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with D,Q-flux linkage LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

### **Q 轴电流断点向量，iq (A)** — Q 轴电流查找向量 `[-40, -20, 0, 20, 40]`（默认）| 向量

用于以下查找表的 Q 轴电流向量，具体取决于用于指定电机参数的方法。

- 对于 `Non-linear model with D,Q-flux linkage LUTs` 方法，用于 *FluxD(id,iq)* 和 *FluxQ(id,iq)*。
- 对于 `Non-linear model with Ld, Lq, and FluxPM LUTs` 方法，用于 *Ld(id,iq)*、*Lq(id,iq)* 和 *FluxPM(id,iq)*。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with D,Q-flux linkage LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

#### 带集中参数的线性模型

### **定子 d 轴电感，Ld (H)** — D 轴定子绕组电感 `0.2e-3`（默认）| 标量

沿旋转 *dq* 参考系直轴的定子绕组电感（亨利）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`。

### **定子 q 轴电感，Lq (H)** — Q 轴定子绕组电感 `0.2e-3`（默认）| 标量

沿旋转 *dq* 参考系交轴的定子绕组电感（亨利）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`。

### **永磁体磁链，FluxPM (Wb)** — 永磁体磁链 `6.4e-3`（默认）| 标量

峰值永磁体磁链（韦伯）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`。

#### 带 D,Q 磁链查找表的非线性模型

### **D 轴磁链查找表，FluxD(id,iq) (Wb)** — D 轴磁链查找数据 `[-1.6,-1.6,-1.6,-1.6,-1.6;2.4,2.4,2.4,2.4,2.4;6.4,6.4,6.4,6.4,6.4;10.4,10.4,10.4,10.4,10.4]*1e-3`（默认）| 矩阵

D 轴磁链 *FluxD(id,iq)* 查找表数据（单位：韦伯）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with D,Q-flux linkage LUTs`。

### **Q 轴磁链查找表，FluxQ(id,iq) (Wb)** — Q 轴磁链查找数据 `[-8,-4,0,4,8;-8,-4,0,4,8;-8,-4,0,4,8;-8,-4,0,4,8]*1e-3`（默认）| 矩阵

Q 轴磁链 *FluxQ(id,iq)* 查找表数据（单位：韦伯）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with D,Q-flux linkage LUTs`。

#### 带 *Ld*、*Lq* 和 *FluxPM* 查找表的非线性模型

### **Ld 查找表，Ld(id,iq) (H)** — D 轴电感查找数据 `0.2e-3 * ones(4, 5)`（默认）| 矩阵

D 轴电感 *Ld(id,iq)* 查找表数据（单位：亨利）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

### **Lq 查找表，Lq(id,iq) (H)** — Q 轴电感查找表数据 `0.2e-3 * ones(4, 5)`（默认）| 矩阵

Q 轴电感 *Lq(id,iq)* 查找表数据（单位：亨利）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

### **PM 磁链查找表，FluxPM(id,iq) (Wb)** — PM 磁链查找数据 `6.4e-3 * ones(4, 5)`（默认）| 矩阵

永磁体磁链 *FluxPM(id,iq)* 查找表数据（单位：韦伯）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为
`Non-linear model with Ld, Lq, and FluxPM LUTs`。

#### 输入单位

### **Input units** — 输入值的单位 `Per-Unit (PU)`（默认）| `SI Units`

输入值的单位。

### **Base Voltage (V)** — 标称电压限值 `24/sqrt(3)`（默认）| 标量

标幺系统的基准电压（单位：伏特）。

#### 依赖关系

要启用此参数，请将 **Input units** 设置为
`Per-Unit (PU)`。

### **Base Current (A)** — 标称电流限值 `19.3`（默认）| 标量

标幺系统的基准电流（单位：安培）。

#### 依赖关系

要启用此参数，请将 **Input units** 设置为
`Per-Unit (PU)`。

### **Base Speed (rpm)** — 标称转速限值 `4107`（默认）| 标量

标幺系统的基准转速（单位：rpm）。

#### 依赖关系

要启用此参数，请将 **Input units** 设置为
`Per-Unit (PU)`。

### **Base torque (Nm)** — 标称转矩限值 `0.74112`（默认）| 标量

标幺系统的基准转矩（单位：Nm）。有关更多详细信息，请参阅 Per-Unit System 页面。

当您将 **Motor parameter input method** 设置为 `Linear model with lumped parameters` 或
`Non-linear model with Ld, Lq, and FluxPM LUTs` 时，无法配置此参数。模块会使用其他参数计算其值。

#### 依赖关系

要显示此参数，请将 **Input units** 设置为
`Per-Unit (PU)`。

### **Base power (W)** — 标称功率限值 `401.143`（默认）| 标量

标幺系统的基准功率（单位：W）。有关更多详细信息，请参阅 Per-Unit System 页面。

当您将 **Motor parameter input method** 设置为 `Linear model with lumped parameters` 或
`Non-linear model with Ld, Lq, and FluxPM LUTs` 时，无法配置此参数。模块会使用其他参数计算其值。

#### 依赖关系

要显示此参数，请将 **Input units** 设置为
`Per-Unit (PU)`。

### **Allow scaled-down motor parameters with CodeGen (higher precision with Fixed-Point data type)** — 缩小内部参数以匹配标幺比例 `on`（默认）| `off`

在生成代码时，缩小内部参数以匹配标幺比例的选项。

- 当您启用此选项时，模块会缩小内部常量和系数以匹配标幺比例。当您使用定点数据类型时，这可以实现更高的精度。如果您将此选项与 single 或 double 数据类型一起使用，根据分配给整数部分的位数，可能会发生一些精度损失。
- 当您禁用此选项时，模块会将用于内部计算的所有常量和系数转换为 SI 单位，然后再将它们转换回 PU 比例。这允许您更新生成代码中的查找表值，通常用于控制器整定或下线操作等应用。您也可以手动更新这些值，用于调试或重用之前生成的代码。

#### 依赖关系

要启用此参数，请将 **Input units** 设置为
`Per-Unit (PU)`。

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

估计机电转矩和功率

PMSM Torque Estimator 模块生成机电转矩和功率估计值，以实现永磁同步电机（PMSM）的磁场定向控制。该模块根据给定的电机参数输出数学计算得到的机电转矩。为准确测量转矩值，请考虑使用物理传感器。

该模块接受 *d* 轴和 *q* 轴电流以及机械转速的反馈值作为输入。

该模块根据通过以下方法之一指定的电机参数生成这些估计值。

- `Linear model with lumped parameters` — 具有 *d* 轴和 *q* 轴定子绕组电感及永磁体磁链的集中参数模型。
- `Non-linear model with D,Q-flux linkage LUTs` — 具有 *d* 轴和 *q* 轴磁链查找表的非线性模型。
- `Non-linear model with Ld, Lq, and FluxPM LUTs` — 具有 *d* 轴和 *q* 轴定子绕组电感及永磁体磁链查找表的非线性模型。
- `Input port based Ld, Lq, and FluxPM` — 通过单独输入端口提供的 *d* 轴和 *q* 轴定子绕组电感及永磁体磁链值。

### 方程

如果在 **Input units** 参数中选择 `Per-Unit (PU)`，该模块默认将内部参数按比例缩小以匹配标幺值尺度。您还可以通过 **Allow scaled-down motor parameters with CodeGen (higher precision with Fixed-Point data type)** 参数配置该模块，使其在执行任何计算之前将输入转换为 SI 单位，并在计算输出后将其转换回标幺值。

以下方程描述了该模块对机电转矩和功率估计值的计算。

Te=32p{ψmIq+(Ld−Lq)IdIq}

或

Te=32p(ψdiq−ψqid)

Pe=Te⋅ωm

其中：

- Ld 和 Lq 是 *d* 轴和 *q* 轴定子绕组电感（亨利）。
- Id 和 Iq 是 *d* 轴和 *q* 轴电流（安培）。
- *ψm* 是永磁体磁链（韦伯）。
- *ψd* 和 *ψq* 是沿 *d* 轴和 *q* 轴的磁通量（韦伯）。
- p 是电机中可用的极对数。
- ωm 是转子的机械转速（rad/s）。

有关 Motor Control Blockset™ 用于 PMSM 的详细方程组和假设，请参阅 Mathematical Model of PMSM。
