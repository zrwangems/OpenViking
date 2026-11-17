---
type: simulink-block
title: 'LUT based PMSM Control Reference'
family: 'controls'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'lutbasedpmsmcontrolreference'
documentation_source_path: 'ref/lutbasedpmsmcontrolreference.html'
language: zh-CN
chinese_source: worker-translation
---

# LUT based PMSM Control Reference

## 端口

### 输入

### **Tref** — 参考转矩值标量

用于计算参考电流的参考转矩输入值（单位：Nm）。

**数据类型：** `single` | `double` | `fixed point`

### **⍵m** — 机械速度标量

用于计算参考电流的参考机械速度值（单位：rad/sec）。

**数据类型：** `single` | `double` | `fixed point`

### **Vdc** — 直流母线电压标量

可变直流母线电压（单位：volts）。

#### 依赖关系

要启用此端口，请将 **Vdc input method** 设置为 `Input port - use 3D LUT (voltage slice based)` 或 `Input port - use 2D LUT (scaled-w based)`。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **Idref** — 参考 *d* 轴电流标量

参考 *d* 轴相电流（单位：amperes）。

**数据类型：** `single` | `double` | `fixed point`

### **Iqref** — 参考 *q* 轴电流标量

参考 *q* 轴相电流（单位：amperes）。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### 电机参数

### **Motor topology** — PMSM 类型 `Interior PMSM`（默认） | `Surface PMSM`

基于永磁体放置位置的 PMSM 类型。

### **Field weakening control method** — 弱磁控制类型 `CVCP`（默认） | `CCCP` | `VCLMT` | `NONE`

弱磁控制类型，指定为以下之一：

- `CVCP` — 恒压恒功率（CVCP）控制方法。
- `CCCP` — 恒流恒功率（CCCP）控制方法。
- `VCLMT` — 电压和电流受限最大转矩（VCLMT）控制方法。

仅可为表贴式 PMSM 配置此参数。对于表贴式 PMSM，仅当您使用 `VCLMT` 控制方法时，该模块才会启用电机参数 **Motor parameter input method** 和 **Vdc input method**（因此，本页中描述的 **Motor Parameters** 及其依赖关系的可用性才有效）。

对于表贴式 PMSM，如果将 **Field weakening control method** 设置为 `CVCP`、`CCCP` 或 `NONE`，则该模块仅显示以下电机参数：

- **Number of pole pairs**
- **Stator resistance per phase, Rs (Ohm)**
- **Stator d-axis inductance, Ld (H)**
- **Permanent magnet flux linkage (Wb)**
- **DC voltage to compute LUTs (V)**
- **Enable custom breakpoint vectors for torque and speed**
- **Current Limit, I\_limit (A)**
- **Viscous damping coefficient, Bv (Nm-s/rad)**

#### 依赖关系

要启用此参数，请将 **Motor topology** 设置为 `Surface PMSM`，并将 **Motor parameter input method** 设置为 `Linear model with lumped parameters` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

### **Number of pole pairs** — 电机中可用的极对数 `4`（默认） | 标量

电机中可用的极对数。

### **Stator resistance per phase, Rs (Ohm)** — 定子相绕组电阻（ohms） `0.36`（默认） | 标量

定子相绕组的电阻（单位：ohms）。

### **Vdc input method** — Vdc 输入方法 `Specify via dialog`（默认） | `Input port - use 3D LUT (voltage slice based)` | `Input port - use 2D LUT (scaled-w based)`

使用以下方法之一指定 *Vdc* 输入。

- `Specify via dialog` — 使用 **DC voltage to compute LUTs (V)** 参数指定固定参考电压 *Vdc*。
- `Input port - use 3D LUT (voltage slice based)` — 使用输入端口 **Vdc** 指定可变参考电压 *Vdc*。使用此选项时，该模块通过基于电压切片的 3-D 查找表（LUT）计算给定电压下的参考电流数据。
- `Input port - use 2D LUT (scaled-w based)` — 使用输入端口 `Vdc` 指定可变参考电压 *Vdc*。使用此选项时，该模块通过基于电机速度 (ω) 缩放的 2-D LUT 计算给定电压下的参考电流数据。

#### 依赖关系

要启用此参数：

- 将 **Motor topology** 设置为 `Interior PMSM`。

或

- 将 **Motor topology** 设置为 `Surface PMSM`。
- 将 **Field-weakening control** 方法设置为 `VCLMT`。

### **DC voltage to compute LUTs (V)** — 直流母线电压（volts） `24`（默认） | 标量

直流母线电压（单位：volts）。

#### 依赖关系

要启用此参数，请将 **Vdc input method** 设置为 `Specify via dialog` 或 `Input port - use 2D LUT (scaled-w based)`。

### **DC bus voltage breakpoint vector, Vdc (V)** — 直流母线电压查找向量（volts） `[18,30]`（默认） | 向量

用于 *id* 和 *iq* 查找表的直流母线电压查找向量（单位：volts）。

#### 依赖关系

要启用此参数，请将 **Vdc input method** 设置为 `Input port - use 3D LUT (voltage slice based)`。

### **Motor parameter input method** — 电机参数类型 `Linear model with lumped parameters`（默认） | `Non-linear model with D,Q-flux linkage LUTs` | `Non-linear model with Ld, Lq, and FluxPM LUTs` | `Non-linear model with id and iq LUTs`

该模块用于生成控制参考电流的电机参数。将该参数设置为以下值之一：

- `Linear model with lumped parameters` — 使用电机参数 *Ld*、*Lq* 和 *FluxPM* 的集总电路值生成电流参考表。
- `Non-linear model with D,Q-flux linkage LUTs` — 使用 *d* 轴和 *q* 轴磁链查找表生成电流参考表。
- `Non-linear model with Ld, Lq, and FluxPM LUTs` — 使用 *Ld*、*Lq* 和 *FluxPM* 查找表生成电流参考表。
- `Non-linear model with id and iq LUTs` — 使用 *id* 和 *iq* 查找表确定电流参考。

#### 依赖关系

要启用此参数：

- 将 **Motor topology** 设置为 `Interior PMSM`。

或

- 将 **Motor topology** 设置为 `Surface PMSM`。
- 将 **Field-weakening control** 方法设置为 `VCLMT`。

### **Enable percentages for torque breakpoint vector** — 为转矩断点向量启用百分比值 `off`（默认） | on

选择此参数可指定百分比转矩断点向量值以及速度断点向量的转矩包络值（在以下参数中）：

- **Reference percentage torque breakpoint vector, Trefpct (%)**
- **Torque envelope for speed breakpoint vector, wrpm (rpm)**

### **Enable custom breakpoint vectors for torque and speed** — 为转矩和速度使用自定义断点 `off`（默认） | on

选择此参数可为电机转矩和速度量使用自定义查找向量。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`、`Non-linear model with D,Q-flux linkage LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

### **Reference percentage torque breakpoint vector, Trefpct (%)** — 转矩参考查找向量（百分比） `[0,50,100]`（默认） | 向量

用于 *id* 和 *iq* 查找表的转矩参考查找向量（百分比）。该向量可包含任意数量的元素。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`、`Non-linear model with D,Q-flux linkage LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。
- 选择 **Enable custom breakpoint vectors for torque and speed** 参数。
- 选择 **Enable percentages for torque breakpoint vector** 参数。

或

- 将 **Motor parameter input method** 设置为 `Non-linear model with id and iq LUTs`。
- 选择 **Enable percentages for torque breakpoint vector** 参数。

### **Torque envelope for speed breakpoint vector, wrpm (rpm)** — 速度断点向量的转矩包络值 `[0.3 0.3 0.15 0.05]`（默认） | 向量

用于计算转矩参考查找向量百分比值的转矩包络值（在 **Reference percentage torque breakpoint vector, Trefpct (%)** 参数中指定）。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`、`Non-linear model with D,Q-flux linkage LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。
- 选择 **Enable custom breakpoint vectors for torque and speed** 参数。
- 选择 **Enable percentages for torque breakpoint vector** 参数。

或

- 将 **Motor parameter input method** 设置为 `Non-linear model with id and iq LUTs`。
- 选择 **Enable percentages for torque breakpoint vector** 参数。

### **Reference torque breakpoint vector, Tref (Nm)** — 转矩参考查找向量 `[0,0.15,0.3]`（默认） | 向量

用于 *id* 和 *iq* 查找表的转矩参考查找向量（单位：Nm）。该向量可包含任意数量的元素。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`、`Non-linear model with D,Q-flux linkage LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。
- 选择 **Enable custom breakpoint vectors for torque and speed** 参数。

或

- 将 **Motor parameter input method** 设置为 `Non-linear model with id and iq LUTs`。

### **Mechanical speed breakpoint vector, wrpm (rpm)** — 转子速度查找向量 `[0,1000,2000,6000]`（默认） | 向量

用于 *id* 和 *iq* 查找表的转子速度查找向量（单位：rpm）。该向量可包含任意数量的元素。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`、`Non-linear model with D,Q-flux linkage LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。
- 选择 **Enable custom breakpoint vectors for torque and speed** 参数。

或

- 将 **Motor parameter input method** 设置为 `Non-linear model with id and iq LUTs`。

### **Current Limit, I\_limit (A)** — 电机最大相电流限值（amperes） `7.1`（默认） | 标量

电机的最大相电流限值（单位：amperes）。

### **Viscous damping coefficient, Bv (Nm-s/rad)** — 粘性阻尼系数 `2.636875217824e-6`（默认） | 标量

电机的粘性阻尼系数 *Bv*，单位为 N·m/(rad/s)。

### **D-axis current breakpoint vector, id (A)** — D 轴电流查找向量 `[-40, -20, 0, 20]`（默认） | 向量

*Ld*、*Lq* 和 *FluxPM* 查找表中的 D 轴电流向量（单位：amperes）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 参数设置为 `Non-linear model with D,Q-flux linkage LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

### **Q-axis current breakpoint vector, iq (A)** — Q 轴电流查找向量 `[-40, -20, 0, 20, 40]`（默认） | 向量

*Ld*、*Lq* 和 *FluxPM* 查找表中的 Q 轴电流向量（单位：amperes）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 参数设置为 `Non-linear model with D,Q-flux linkage LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

### **Use measured (instead of computed) torque** — 使用转矩的测量值 `off`（默认） | on

启用此参数以向该模块提供测量（而不是计算）的转矩查找数据。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with D,Q-flux linkage LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

### **Measured torque LUT, T(id,iq) (Nm)** — 测量查找数据 `[-3.4560,-1.7280,0, 1.7280, 3.4560;-2.4960,-1.2480,0, 1.2480, 2.4960;-1.5360,-0.7680,0, 0.7680, 1.5360;-0.5760,-0.2880,0, 0.2880, 0.5760]`（默认） | 向量

测量的转矩查找表数据（单位：weber）。

#### 依赖关系

要启用此参数：

- 将 **Motor parameter input method** 设置为 `Non-linear model with D,Q-flux linkage LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。
- 选择 **Use measured (instead of computed) torque** 参数。

### 线性集总参数模型

### **Stator d-axis inductance, Ld (H)** — D 轴定子绕组电感 `0.2e-3`（默认） | 标量

沿旋转 *dq* 参考坐标系直轴的定子绕组电感（单位：henry）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`。

### **Stator q-axis inductance, Lq (H)** — Q 轴定子绕组电感 `0.4e-3`（默认） | 标量

沿旋转 *dq* 参考坐标系交轴的定子绕组电感（单位：henry）。

#### 依赖关系

要启用此参数，请将 **Motor topology** 设置为 `Interior PMSM`，并将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`。

### **Permanent magnet flux linkage (Wb)** — 永磁体磁链 `6.4e-3`（默认） | 标量

峰值永磁体磁链（单位：weber）。

#### 依赖关系

要启用此参数，请在 **Motor parameter input method** 参数中选择 `Linear model with lumped parameters` 选项。

### 使用 D,Q 磁链 LUT 的非线性模型

### **D-axis flux linkage LUT, FluxD (id,iq) (Wb)** — 参考 d 轴磁链查找数据 `[-1.6,-1.6,-1.6,-1.6,-1.6;2.4,2.4,2.4,2.4,2.4;6.4,6.4,6.4,6.4,6.4;10.4,10.4,10.4,10.4,10.4]*1e-3`（默认） | 向量

D 轴磁链查找表数据（单位：weber）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with D,Q-flux linkage LUTs`。

### **Q-axis flux linkage LUT, FluxQ (id,iq) (Wb)** — 参考 q 轴磁链查找数据 `2*[-8,-4,0,4,8;-8,-4,0,4,8;-8,-4,0,4,8;-8,-4,0,4,8]*1e-3`（默认） | 向量

Q 轴磁链查找表数据（单位：weber）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with D,Q-flux linkage LUTs`。

### 使用 *Ld*、*Lq* 和 *FluxPM* LUT 的非线性模型

### **Ld LUT, Ld(id,iq) (H)** — D 轴电感查找数据 `0.2e-3 * ones(4, 5)`（默认） | 矩阵

D 轴电感查找表数据（单位：henry）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

### **Lq LUT, Lq(id,iq) (H)** — Q 轴电感查找数据 `0.4e-3 * ones(4, 5)`（默认） | 矩阵

Q 轴电感查找表数据（单位：henry）。

#### 依赖关系

要启用此参数，请将 **Motor topology** 设置为 `Interior PMSM`，并将 **Motor parameter input method** 设置为 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

### **PM flux linkage LUT, FluxPM(id,iq) (Wb)** — 永磁体磁链查找数据 `6.4e-3 * ones(4, 5)`（默认） | 矩阵

永磁体磁链查找表数据（单位：weber）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

### 使用 *id* 和 *iq* LUT 的非线性模型

### **Reference torque breakpoint vector, Tref (Nm)** — 转矩参考查找向量 `[0 0.15 0.3]`（默认） | 向量

用于 *id* 和 *iq* 查找表的转矩参考查找向量（单位：Nm）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with id and iq LUTs`。

### **Mechanical speed breakpoint vector, wrpm (rpm)** — 转子速度查找向量 `[0 1000 2000 6000]`（默认） | 向量

用于 *id* 和 *iq* 查找表的转子速度查找向量（单位：rpm）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with id and iq LUTs`。

### **Reference id LUT, id(Tref,wrpm) (A)** — 参考 d 轴电流查找数据 `[0,0,0,-7.1;0,0,0,-7.1;0,0,0,-7.1]`（默认） | 矩阵

D 轴电流参考 2-D 查找表数据（单位：amperes）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with id and iq LUTs`，并将 **Vdc input method** 设置为 `Input port - use 2D LUT (scaled-w based)`。

### **Reference id LUT, id(Tref,wrpm,Vdc) (A)** — 参考 d 轴电流查找表数据 `cat(3,[0,0,0,-7.1;-0.4579,-0.4579,-0.4579,-7.1;-1.4457,-1.4457,-1.4457,-7.1],[0,0,0,0;-0.4579,-0.4579,-0.4579,-1.2581;-1.4457,-1.4457,-1.4457,-4.5085])`（默认）| matrix

d 轴电流参考 3-D 查找表数据（单位为安培）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with id and iq LUTs`，并将 **Vdc input method** 设置为 `Input port - use 3D LUT (voltage slice based)`。

### **Reference iq LUT, iq(Tref,wrpm) (A)** — 参考 q 轴电流查找表数据 `[0,0,0,0;3.9091,3.9091,3.9091,0;7.1,7.1,7.1,0]`（默认）| matrix

q 轴电流参考 2-D 查找表数据（单位为安培）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with id and iq LUTs`，并将 **Vdc input method** 设置为 `Input port - use 2D LUT (scaled-w based)`。

### **Reference iq LUT, iq(Tref,wrpm,Vdc) (A)** — 参考 q 轴电流查找表数据 `cat(3,[0,0,0,0;3.8539,3.8539,3.8539,0;6.9513,6.9513,6.9513,0],[0,0,0,0;3.8539,3.8539,3.8539,3.7611;6.9513,6.9513,6.9513,5.4848])`（默认）| matrix

q 轴电流参考 3-D 查找表数据（单位为安培）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with id and iq LUTs`，并将 **Vdc input method** 设置为 `Input port - use 3D LUT (voltage slice based)`。

### 输入单位

### **Input units** — 模块输入值的测量单位 `Per-Unit (PU)`（默认）| `SI Units`

模块输入值的测量单位。

### **Base voltage (V)** — 标称电压限制 `24/sqrt(3)`（默认）| scalar

用于 per-unit 系统的基准电压（单位为伏特）。

#### 依赖关系

要启用此参数，请将 **Input units** 设置为 `Per-Unit (PU)`。

### **Base current (A)** — 标称电流限制 `19.3`（默认）| scalar

用于 per-unit 系统的基准电流（单位为安培）。

#### 依赖关系

要启用此参数，请将 **Input units** 设置为 `Per-Unit (PU)`。

### **Base speed (rpm)** — 标称转速限制 `4107`（默认）| scalar

用于 per-unit 系统的基准转速（单位为 rpm）。

#### 依赖关系

要启用此参数，请将 **Input units** 设置为 `Per-Unit (PU)`。

### **Base torque (Nm)** — 标称转矩限制 `0.74112`（默认）

对应于 1 per-unit 的转矩（单位为 Nm）。有关详细信息，请参阅 Per-Unit System 页面。

您无法配置此参数。模块使用其他参数在内部计算此值。

#### 依赖关系

要启用此参数，请将 **Input units** 设置为 `Per-Unit (PU)`。

### **Allow scaled-down motor parameters with CodeGen (higher precision with Fixed-Point data type)** — 将内部参数按比例缩小以匹配 per-unit 标度 `on`（默认）| `off`

在生成代码时，将内部参数按比例缩小以匹配 per-unit 标度的选项。

- 当您启用此选项时，模块会将内部常量和系数按比例缩小，以匹配 per-unit 标度。当您使用 fixed-point 数据类型时，这允许更高的精度。如果将此选项与 single 或 double 数据类型一起使用，则根据分配给整数部分的位数，可能会出现一些精度损失。
- 当您禁用此选项时，模块会将其用于内部计算的所有常量和系数转换为 SI 单位，然后再转换回 per-unit 标度。这允许您在生成的代码中更新查找表值，通常用于控制器调优或下线操作等应用。您也可以手动更新这些值，以进行调试或重用以前生成的代码。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with id and iq LUTs`，并将 **Input units** 设置为 `Per-Unit (PU)`。

### 绘图选项

仅当满足以下条件时，模块才启用此选项卡：

- 将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`、`Non-linear model with D,Q-flux linkage LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs` 中的任一项。
- 将 **Vdc input method** 设置为 `Specify via dialog`。

### **Enable saving the computed LUTs** — 使模块能够保存计算得到的 LUTs `off`（默认）| `on`

使模块能够在您点击 **Compute (and plot) id and iq LUTs** 按钮时保存模块计算得到的查找表数据。

有关详细信息，请参阅直接从模块参数对话框绘制 PMSM 和 SynRM 的约束曲线和驱动特性。

### **Compute (and plot) id and iq LUTs** — 计算（并绘制）*id* 和 *iq* 查找数据按钮

当您点击此按钮时，模块会计算（并绘制）*id* 和 *iq* 电流的查找表数据。

有关详细信息，请参阅直接从模块参数对话框绘制 PMSM 和 SynRM 的约束曲线和驱动特性。

### **Use default options for plotting** — 使用默认选项绘制约束曲线 `on`（默认）| `off`

使模块能够在您点击 **Plot constraint curves** 按钮绘制电机约束曲线时使用默认绘图选项。

有关详细信息，请参阅直接从模块参数对话框绘制 PMSM 和 SynRM 的约束曲线和驱动特性。

### **Motor speed (RPM)** — 用于绘制约束曲线的电机转速 `3000`（默认）| scalar

当您点击 **Plot constraint curves** 按钮绘制电机约束曲线时，模块应使用的电机转速（单位为 RPM）。

有关详细信息，请参阅直接从模块参数对话框绘制 PMSM 和 SynRM 的约束曲线和驱动特性。

#### 依赖关系

要启用此参数，请清除 **Use default options for plotting** 参数。

### **Motor torque (Nm)** — 用于绘制约束曲线的电机转矩 `0.1`（默认）| scalar

当您点击 **Plot constraint curves** 按钮绘制电机约束曲线时，模块应使用的电机转矩（单位为 Nm）。

有关详细信息，请参阅直接从模块参数对话框绘制 PMSM 和 SynRM 的约束曲线和驱动特性。

#### 依赖关系

要启用此参数，请清除 **Use default options for plotting** 参数。

### **Enable plotting the drive characteristics** — 使模块能够绘制驱动特性 `off`（默认）| `on`

使模块能够在您点击 **Plot constraint curves** 按钮绘制电机约束曲线时绘制驱动特性。

有关详细信息，请参阅直接从模块参数对话框绘制 PMSM 和 SynRM 的约束曲线和驱动特性。

#### 依赖关系

要启用此参数，请清除 **Use default options for plotting** 参数。

### **Include the drive characteristics for an increased motor current** — 使模块能够绘制电机电流增大时的驱动特性 `off`（默认）| `on`

使模块能够包括电机电流增大时的驱动特性（在点击 **Plot constraint curves** 按钮后生成的绘图中）。

**注意**

要成功绘制电机电流增大时的特性，该电流必须高于电机的额定电流。

有关详细信息，请参阅直接从模块参数对话框绘制 PMSM 和 SynRM 的约束曲线和驱动特性。

#### 依赖关系

要启用此参数，请清除 **Use default options for plotting** 参数，并选择 **Enable plotting the drive characteristics** 参数。

### **Plot constraint curves** — 绘制电机约束曲线按钮

当您点击此按钮时，模块会绘制电机的约束曲线。

有关详细信息，请参阅直接从模块参数对话框绘制 PMSM 和 SynRM 的约束曲线和驱动特性。

### **Compute and show** — 计算并显示特性转矩和转速按钮

当您点击此按钮时，模块会计算并显示以下转矩和转速特性：

- 额定转矩 — 电机额定转矩（单位为 Nm）。
- 额定转速 — 电机额定转速（单位为 RPM）。
- 最大转速 — 电机最大转速（单位为 RPM）。

有关详细信息，请参阅直接从模块参数对话框绘制 PMSM 和 SynRM 的约束曲线和驱动特性。

## 所属库

Motor Control Blockset / Controls / Control Reference

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真 fixed-point 系统。

## 版本历史

**在 R2022b 中引入**

## 描述

为永磁同步电机的磁场定向控制生成基于查找表的控制参考电流

LUT based PMSM Control Reference 模块生成用于永磁同步电机（PMSM）磁场定向控制和弱磁控制的 *d* 轴和 *q* 轴参考电流。您可以指定参考转矩和反馈机械转速，模块输出相应的参考电流值。该模块还支持最大转矩电流比（MTPA）和最大转矩电压比（MTPV）运行区域。

该模块使用 *id(T,ω)* 和 *iq(T,ω)* 查找表（LUT）生成参考电流值。根据您用于指定电机参数的输入方法，模块可以生成 LUT，也可以使用您提供的数据。

您可以使用以下方法之一指定电机参数。

- `Linear model with lumped parameters` — 具有 *Ld*、*Lq* 和 *FluxPM* 的集总参数

  此方法使用集总参数计算 *id* 和 *iq* LUT。该模块通过求解与这些曲线关联的方程，针对给定的 *ω* 和 *T* 输入获得 *id* 和 *iq*。

  最大转矩电流比（MTPA）曲线（IPMSM），

  id2+idψm(Ld−Lq)=iq2.

  MTPA 线（SPMSM），*id = 0*。

  恒转矩轨迹

  iq=T1.5Pp(ψm+(Ld−Lq)id).

  电流限制曲线

  id2+iq2=imax2.

  电压限制曲线

  (VDC3)2=(idRs−ωeLqiq)2+(iqRs+ωeLdid+ωeψm)2.

  - 当电机在电压约束内运行时，模块求解 MTPA 线与恒转矩轨迹的交点。
  - 当电机在电压约束之外运行时，模块求解电压约束曲线与恒转矩轨迹的交点。

  在根据 *ω* 和 *T* 值网格计算 *id* 和 *iq* 表之后，模块使用插值来查找 *idref* 和 *iqref*，适用于落在表值范围内的任何 *ω* 和 *T* 输入。对于超出边界的 *ω* 和 *T* 值，表值会被限幅。

- `Non-linear model with Ld, Lq, and FluxPM LUTs` — 具有 *d* 轴和 *q* 轴定子绕组电感及永磁体磁链查找表的非线性模型

  此方法使用与集总参数方法类似的方法，不同之处在于，模块在每次计算 *id* 和 *iq* 时更新 *Ld(id,iq)*、*Lq(id,iq)* 和 *FluxPM(id,iq)* 的值。模块迭代这些计算，直到 *id* 和 *iq* 值收敛。

- `Non-linear model with D,Q-flux linkage LUTs` — 具有 *d* 轴和 *q* 轴磁链查找表的非线性模型

  此方法使用与集总参数方法类似的方法，不同之处在于，模块在每次计算 *id* 和 *iq* 时更新 *ψd(id,iq)* 和 *ψq(id,iq)* 的值。模块迭代这些计算，直到 *id* 和 *iq* 值收敛。

- `Non-linear model with id and iq LUTs` — 当您想手动提供 *id(T,ω)* 和 *iq(T,ω)* 表时，使用此方法。通常，您通过仿真或测功机测试获得这些表。

您还可以使用 Motor Control Blockset™ 中的 `mcb.generateMotorLUT` 函数生成这些表。

有关 Motor Control Blockset 用于 PMSM 的详细方程组和假设，请参阅 Mathematical Model of PMSM。

此外，您可以使用 **Vdc input method** 参数将模块配置为通过 **DC voltage to compute LUTs (V)** 参数接受固定参考直流电压，或通过单独的输入端口 **Vdc** 接受可变参考直流电压。

根据您在 **Motor parameter input method** 参数中选择的方法，您可以使用集总参数或非线性模型来计算参考电流，如下表所示。

| **Motor parameter input method** | **Vdc input method** | 用于计算参考电流的技术 |
| --- | --- | --- |
| `Linear model with lumped parameters` | `Specify via dialog` | 模块使用集总参数，为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压计算 *id* 和 *iq* LUT，并使用该 LUT 确定参考电流。 |
|  | `Input port - use 3D LUT (voltage slice based)` | 模块使用集总参数计算 3-D *id* 和 *iq* LUT，其中包含不同电压（或 **DC bus voltage breakpoint vector, Vdc (V)** 参数中指定的电压切片）的数据。它使用此数据确定与输入端口 **Vdc** 处指定电压对应的参考电流。 |
|  | `Input port - use 2D LUT (scaled-w based)` | 模块使用集总参数，为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压计算 2-D *id* 和 *iq* LUT。它使用这些 LUT，通过缩放转速（ω）来计算（与输入端口 **Vdc** 处提供的电压对应的）参考电流。 |
| `Non-linear model with D,Q-flux linkage LUTs` | `Specify via dialog` | 模块使用 *d* 轴和 *q* 轴磁链 LUT，为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压计算参考电流。 |
|  | `Input port - use 3D LUT (voltage slice based)` | 模块使用 3-D *d* 轴和 *q* 轴磁链 LUT，其中包含不同电压（或 **DC bus voltage breakpoint vector, Vdc (V)** 参数中指定的电压切片）的数据。它使用这些 LUT 计算与输入端口 **Vdc** 处提供的电压对应的参考电流。 |
|  | `Input port - use 2D LUT (scaled-w based)` | 模块使用 2-D *d* 轴和 *q* 轴磁链 LUT，为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压。它使用这些 LUT，通过缩放转速（ω）来计算（与输入端口 **Vdc** 处提供的电压对应的）参考电流。 |
| `Non-linear model with Ld, Lq, and FluxPM LUTs` | `Specify via dialog` | 模块使用给定的 *Ld*、*Lq* 和永磁体磁链 LUT，为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压计算参考电流。 |
|  | `Input port - use 3D LUT (voltage slice based)` | 模块使用给定的 3-D *Ld*、*Lq* 和永磁体磁链 LUT，其中包含不同电压（或 **DC bus voltage breakpoint vector, Vdc (V)** 参数中指定的电压切片）的数据。它使用这些 LUT 计算与输入端口 **Vdc** 处提供的电压对应的参考电流。 |
|  | `Input port - use 2D LUT (scaled-w based)` | 模块使用给定的 2-D *Ld*、*Lq* 和永磁体磁链 LUT，用于 **DC bus voltage, Vdc (V)** 参数中指定的固定电压。它使用这些 LUT，通过缩放转速（ω）来计算（与输入端口 **Vdc** 处提供的电压对应的）参考电流。 |
| `Non-linear model with id and iq LUTs` | `Specify via dialog` | 模块使用给定的 *id*、*iq* LUT，为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压确定参考电流。 |
|  | `Input port - use 3D LUT (voltage slice based)` | 模块使用给定的 3-D *id*、*iq* LUT，其中包含不同电压（或 **DC bus voltage breakpoint vector, Vdc (V)** 参数中指定的电压切片）的数据。它使用这些 LUT 确定与输入端口 **Vdc** 处提供的电压对应的参考电流。 |
|  | `Input port - use 2D LUT (scaled-w based)` | 模块使用给定的 2-D *id*、*iq* LUT，用于 **DC bus voltage, Vdc (V)** 参数中指定的固定电压。它使用这些 LUT，通过缩放转速（ω）来计算（与输入端口 **Vdc** 处提供的电压对应的）参考电流。 |
