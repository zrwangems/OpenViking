---
type: simulink-block
title: 'SynRM Torque Estimator'
family: 'controls'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'synrmtorqueestimator'
documentation_source_path: 'ref/synrmtorqueestimator.html'
language: zh-CN
chinese_source: worker-translation
---

# SynRM Torque Estimator

## 端口

### 输入

### **Id** — D 轴电流标量

沿旋转 *dq* 参考系的 *d* 轴的电流（以 amperes 为单位）。

**数据类型：** `single` | `double` | `fixed point`

### **Iq** — Q 轴电流标量

沿旋转 *dq* 参考系的 *q* 轴的电流（以 amperes 为单位）。

**数据类型：** `single` | `double` | `fixed point`

### **ωm** — 转子机械速度标量

转子的机械速度（以 rad/s 为单位）。

**数据类型：** `single` | `double` | `fixed point`

### **Ld** — D 轴电感标量

D 轴绕组电感（以 henries 为单位）。

#### 依赖关系

要启用此输入端口，请将 **电机参数输入方法** 设置为 `Input port based Ld and Lq` 或 `Input port based Ld, Lq and FluxPM`。

**数据类型：** `single` | `double` | `fixed point`

### **Lq** — Q 轴电感标量

Q 轴绕组电感（以 henries 为单位）。

#### 依赖关系

要启用此输入端口，请将 **电机参数输入方法** 设置为 `Input port based Ld and Lq` 或 `Input port based Ld, Lq and FluxPM`。

**数据类型：** `single` | `double` | `fixed point`

### **FluxPM** — 永磁体磁链标量

峰值永磁体磁链（以 weber 为单位）。

#### 依赖关系

要启用此输入端口，请将 **电机拓扑** 设置为 `PM-assisted synchronous reluctance motor`，并将 **电机参数输入方法** 设置为 `Input port based Ld, Lq and FluxPM`。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **Te** — 估计转矩标量

电机输出的机械转矩（以 Nm 为单位）。

**数据类型：** `single` | `double` | `fixed point`

### **Pe** — 估计功率标量

电机的功率输出（以 watts 为单位）。

**数据类型：** `single` | `double` | `fixed point`

## 参数

#### 电机参数

### **电机拓扑** — 同步磁阻电机拓扑 `Synchronous reluctance motor` (默认) | `PM-assisted synchronous reluctance motor`

同步磁阻电机的类型。

### **d 轴和 q 轴的定义** — *d* 轴和 *q* 轴的排列 `Ld > Lq (different from PMSM)` (默认) | `Lq > Ld (same as PMSM)`

*d* 轴和 *q* 轴的排列类型。您可以选择以下选项之一：

- `Ld > Lq (different from PMSM)` — 选择此选项以使用不同于 PMSM 的 *d* 轴和 *q* 轴排列。
- `Lq > Ld (same as PMSM)` — 选择此选项以使用与 PMSM 相同的 *d* 轴和 *q* 轴排列。

有关排列类型的更多信息，请参阅 SynRM 约束曲线及其应用。

### **极对数** — 电机中可用的极对数 `4` (默认) | scalar

电机中可用的极对数。

### **电机参数输入方法** — 电机参数的类型 `Linear model with lumped parameters` (默认) | `Non-linear model with D,Q-flux linkage LUTs` | `Non-linear model with Ld and Lq LUTs` | `Non-linear model with Ld, Lq, and FluxPM LUTs` | `Input port based Ld and Lq` | `Input port based Ld, Lq, and FluxPM`

模块用于生成转矩和功率估计的电机参数。

- `Linear model with lumped parameters` — 使用电机参数 *Ld*、*Lq* 和 *FluxPM* 的集总电路值生成估计。
- `Non-linear model with D,Q-flux linkage LUTs` — 使用 *d* 轴磁链 *FluxD* 和 *q* 轴磁链 *FluxQ* 查找表 (LUT) 生成估计。
- `Non-linear model with Ld and Lq LUTs` — 使用指定为模块参数的 *Ld* 和 *Lq* LUT 生成估计。
- `Non-linear model with Ld, Lq, and FluxPM LUTs` — 使用指定为模块参数的 *Ld*、*Lq* 和 *FluxPM* LUT 生成估计。
- `Input port based Ld and Lq` — 使用指定为模块输入的 *Ld* 和 *Lq* LUT 生成估计。
- `Input port based Ld, Lq and FluxPM` — 使用指定为模块输入的 *Ld*、*Lq* 和 *FluxPM* LUT 生成估计。

### **D 轴电流断点向量，id (A)** — D 轴电流查找向量 `[0,10,20,30]` (默认) | vector

根据用于指定电机参数的方法，以下查找表中使用的 D 轴电流向量。

- 对于 `Non-linear model with D,Q-flux linkage LUTs` 方法，使用 *FluxD(id,iq)* 和 *FluxQ(id,iq)*。
- 对于 `Non-linear model with Ld, Lq, and FluxPM LUTs` 方法，使用 *Ld(id,iq)*、*Lq(id,iq)* 和 *FluxPM(id,iq)*。

#### 依赖关系

要启用此参数，请将 **电机参数输入方法** 设置为 `Non-linear model with D,Q-flux linkage LUTs`、`Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

### **Q 轴电流断点向量，iq (A)** — Q 轴电流查找向量 `[0,10,20,30,40]` (默认) | vector

根据用于指定电机参数的方法，以下查找表中使用的 Q 轴电流向量。

- 对于 `Non-linear model with D,Q-flux linkage LUTs` 方法，使用 *FluxD(id,iq)* 和 *FluxQ(id,iq)*。
- 对于 `Non-linear model with Ld, Lq, and FluxPM LUTs` 方法，使用 *Ld(id,iq)*、*Lq(id,iq)* 和 *FluxPM(id,iq)*。

#### 依赖关系

要启用此参数，请将 **电机参数输入方法** 设置为 `Non-linear model with D,Q-flux linkage LUTs`、`Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

#### 集总参数线性模型

### **定子 d 轴电感，Ld (H)** — D 轴定子绕组电感 `0.9e-3` (默认) | scalar

沿旋转 *dq* 参考系直轴的定子绕组电感（以 henry 为单位）。

#### 依赖关系

要启用此参数，请将 **电机参数输入方法** 设置为 `Linear model with lumped parameters`。

### **定子 q 轴电感，Lq (H)** — Q 轴定子绕组电感 `0.15e-3` (默认) | scalar

沿旋转 *dq* 参考系交轴的定子绕组电感（以 henry 为单位）。

#### 依赖关系

要启用此参数，请将 **电机参数输入方法** 设置为 `Linear model with lumped parameters`。

### **永磁体磁链，FluxPM (Wb)** — 永磁体磁链 `0.4e-4` (默认) | scalar

峰值永磁体磁链（以 weber 为单位）。

#### 依赖关系

要启用此参数，请将 **电机拓扑** 设置为 `PM-assisted synchronous reluctance motor`，并将 **电机参数输入方法** 设置为 `Linear model with lumped parameters`。

#### 使用 D,Q 磁链 LUT 的非线性模型

### **D 轴磁链 LUT，FluxD(id,iq) (Wb)** — D 轴磁链查找数据 `[0,0,0,0,0;0.009,0.009,0.009,0.009,0.0090;0.018,0.018,0.018,0.018,0.0180;0.027,0.027,0.027,0.027,0.0270]` (默认) | matrix

D 轴磁链 *FluxD(id,iq)* 查找表数据（以 weber 为单位）。

#### 依赖关系

要启用此参数，请将 **电机参数输入方法** 设置为 `Non-linear model with D,Q-flux linkage LUTs`。

### **Q 轴磁链 LUT，FluxQ(id,iq) (Wb)** — Q 轴磁链查找数据 `[0,0.0015,0.0030,0.0045,0.0060;0,0.0015,0.0030,0.0045,0.0060;0,0.0015,0.0030,0.0045,0.0060;0,0.0015,0.0030,0.0045,0.0060]` (默认) | matrix

Q 轴磁链 *FluxQ(id,iq)* 查找表数据（以 weber 为单位）。

#### 依赖关系

要启用此参数，请将 **电机参数输入方法** 设置为 `Non-linear model with D,Q-flux linkage LUTs`。

#### 使用 *Ld* 和 *Lq*（以及 *Ld*、*Lq* 和 *FluxPM*）LUT 的非线性模型

### **Ld LUT，Ld(id,iq) (H)** — D 轴电感查找数据 `0.9e-3 * ones(4, 5)` (默认) | matrix

D 轴电感 *Ld(id,iq)* 查找表数据（以 henry 为单位）。

#### 依赖关系

要启用此参数，请将 **电机参数输入方法** 设置为 `Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

### **Lq LUT，Lq(id,iq) (H)** — Q 轴电感查找表数据 `0.15e-3 * ones(4, 5)` (默认) | matrix

Q 轴电感 *Lq(id,iq)* 查找表数据（以 henry 为单位）。

#### 依赖关系

要启用此参数，请将 **电机参数输入方法** 设置为 `Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

### **PM 磁链 LUT，FluxPM(id,iq) (Wb)** — PM 磁链查找数据 `0.4e-4 * ones(4, 5)` (默认) | matrix

永磁体磁链 *FluxPM(id,iq)* 查找表数据（以 weber 为单位）。

#### 依赖关系

要启用此参数，请将 **电机拓扑** 设置为 `PM-assisted synchronous reluctance motor`，并将 **电机参数输入方法** 设置为 `Non-linear model with Ld, Lq and FluxPM LUTs`。

#### 输入单位

### **输入单位** — 输入值的单位 `Per-Unit (PU)` (默认) | `SI Units`

输入值的单位。

### **基准电压 (V)** — 标称电压限值 `24/sqrt(3)` (默认) | scalar

用于标幺值系统的基准电压（以 volts 为单位）。

#### 依赖关系

要启用此参数，请将 **输入单位** 设置为 `Per-Unit (PU)`。

### **基准电流 (A)** — 标称电流限值 `19.3` (默认) | scalar

用于标幺值系统的基准电流（以 amperes 为单位）。

#### 依赖关系

要启用此参数，请将 **输入单位** 设置为 `Per-Unit (PU)`。

### **基准速度 (rpm)** — 标称速度限值 `4107` (默认) | scalar

用于标幺值系统的基准速度（以 rpm 为单位）。

#### 依赖关系

要启用此参数，请将 **输入单位** 设置为 `Per-Unit (PU)`。

### **基准转矩 (Nm)** — 标称转矩限值 `0.93271` (默认) | scalar

用于标幺值系统的基准转矩（以 Nm 为单位）。有关更多详细信息，请参阅 Per-Unit System 页面。

当您将 **电机参数输入方法** 设置为 `Linear model with lumped parameters`、`Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs` 时，无法配置此参数。模块使用其他参数计算其值。

#### 依赖关系

要显示此参数，请将 **输入单位** 设置为 `Per-Unit (PU)`。

### **基准功率 (W)** — 标称功率限值 `401.143` (默认) | scalar

用于标幺值系统的基准功率（以 W 为单位）。有关更多详细信息，请参阅 Per-Unit System 页面。

当您将 **电机参数输入方法** 设置为 `Linear model with lumped parameters`、`Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs` 时，无法配置此参数。模块使用其他参数计算其值。

#### 依赖关系

要显示此参数，请将 **输入单位** 设置为 `Per-Unit (PU)`。

### **允许在 CodeGen 中使用缩放后的电机参数（使用 Fixed-Point 数据类型时精度更高）** — 缩放内部参数以匹配标幺值尺度 `on` (默认) | `off`

在生成代码时缩放内部参数以匹配标幺值尺度的选项。

- 启用此选项时，模块会缩放内部常量和系数以匹配标幺值尺度。当您使用 fixed-point 数据类型时，这允许更高的精度。如果您将此选项与 single 或 double 数据类型一起使用，则根据分配给整数部分的位数，可能会发生一些精度损失。
- 禁用此选项时，模块会将用于内部计算的所有常量和系数转换为 SI 单位，然后将它们转换回 PU 尺度。这允许您更新生成代码中的查找表值，通常用于控制器调优或下线操作等应用。您也可以手动更新这些值，以调试或重用之前生成的代码。

#### 依赖关系

要启用此参数，请将 **输入单位** 设置为 `Per-Unit (PU)`。

## 所属库

Motor Control Blockset / Controls / Control Reference

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

估计机电转矩和功率

SynRM Torque Estimator 模块生成机电转矩和功率估计，以实现同步磁阻电机 (SynRM) 和永磁辅助同步磁阻电机 (PMaSynRM) 的磁场定向控制。该模块根据给定的电机参数输出数学计算得到的机电转矩。要准确测量转矩值，请考虑使用物理传感器。

该模块接受 *d* 轴和 *q* 轴电流以及机械速度的反馈值作为输入。

该模块根据使用以下方法之一指定的电机参数生成这些估计。

- `Linear model with lumped parameters` — 具有 *d* 轴和 *q* 轴定子绕组电感以及永磁体磁链的集总参数。
- `Non-linear model with D,Q-flux linkage LUTs` — 具有 *d* 轴和 *q* 轴磁链查找表的非线性模型。
- `Non-linear model with Ld and Lq LUTs` — 具有 *d* 轴和 *q* 轴定子绕组电感查找表的非线性模型。
- `Non-linear model with Ld, Lq, and FluxPM LUTs` — 具有 *d* 轴和 *q* 轴定子绕组电感以及永磁体磁链查找表的非线性模型。
- `Input port based Ld and Lq` — 使用单独输入端口提供的 *d* 轴和 *q* 轴定子绕组电感值。
- `Input port based Ld, Lq, and FluxPM` — 使用单独输入端口提供的 *d* 轴和 *q* 轴定子绕组电感以及永磁体磁链值。

### 方程

如果您在 **输入单位** 参数中选择 `Per-Unit (PU)`，则默认情况下，模块会缩放内部参数以匹配标幺值尺度。您还可以通过使用 **允许在 CodeGen 中使用缩放后的电机参数（使用 Fixed-Point 数据类型时精度更高）** 参数，配置模块在执行任何计算之前将输入转换为 SI 单位，并在计算输出之后将它们转换回标幺值。

以下方程描述了该模块对机电转矩和功率估计的计算。

**注意**

以下针对 SynRM 和 PMaSynRM 的方程遵循与永磁同步电机 (PMSM) 相同的 *d*-*q* 轴标记法。

对于 SynRM：

Te=32p(Ld−Lq)IdIq

对于 PMSynRM：

Te=32p{ψmIq+(Ld−Lq)IdIq}

或

对于 SynRM 和 PMaSynRM 二者：

Te=32p(ψdiq−ψqid)

Pe=Te⋅ωm

其中：

- Ld 和 Lq 是 *d* 轴和 *q* 轴定子绕组电感（以 henry 为单位）。
- Id 和 Iq 是 *d* 轴和 *q* 轴电流（以 amperes 为单位）。
- *ψm* 是永磁体磁链（以 weber 为单位）。
- *ψd* 和 *ψq* 是沿 *d* 轴和 *q* 轴的磁通量（以 weber 为单位）。
- p 是电机中可用的极对数。
- ωm 是转子的机械速度（以 rad/s 为单位）。

有关 Motor Control Blockset™ 用于同步磁阻电机的详细方程组和假设，请参阅 Synchronous Reluctance Machine (Simscape Electrical)。
