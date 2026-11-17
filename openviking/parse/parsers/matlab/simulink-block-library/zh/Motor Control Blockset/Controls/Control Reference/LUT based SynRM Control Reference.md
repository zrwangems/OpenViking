---
type: simulink-block
title: 'LUT based SynRM Control Reference'
family: 'controls'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'lutbasedsynrmcontrolreference'
documentation_source_path: 'ref/lutbasedsynrmcontrolreference.html'
language: zh-CN
chinese_source: worker-translation
---

# LUT based SynRM Control Reference

## 端口

### 输入

### **Tref** — 参考转矩值标量

模块用于计算参考电流的参考转矩输入值（以 Nm 为单位）。

**数据类型：** `single` | `double` | `fixed point`

### **⍵m** — 机械速度标量

模块用于计算参考电流的参考机械速度值（以 rad/sec 为单位）。

**数据类型：** `single` | `double` | `fixed point`

### **Vdc** — 直流母线电压标量

可变直流母线电压（以 volts 为单位）。

#### 依赖关系

要启用此端口，请将 **Vdc input method** 设置为 `Input
port - use 3D LUT (voltage slice based)` 或
`Input port - use 2D LUT (scaled-w
based)`。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **Id ref** — 参考 *d* 轴电流标量

参考 *d* 轴相电流（以 amperes 为单位）。

**数据类型：** `single` | `double` | `fixed point`

### **Iq ref** — 参考 *q* 轴电流标量

参考 *q* 轴相电流（以 amperes 为单位）。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### 电机参数

### **Motor topology** — 同步磁阻电机拓扑 `Synchronous reluctance motor`（默认值）| `PM-assisted synchronous reluctance motor`

同步磁阻电机的类型。

### **Definition of d-axis and q-axis** — *d* 轴和 *q* 轴的对齐方式 `Ld > Lq (different from PMSM)`（默认值）| `Lq > Ld (same as PMSM)`

*d* 轴和 *q* 轴的对齐类型。您可以选择以下选项之一：

- `Ld > Lq (different from PMSM)` — 选择此选项可使用不同于 PMSM 的 *d* 轴和 *q* 轴对齐方式。
- `Lq > Ld (same as PMSM)` — 选择此选项可使用与 PMSM 相同的 *d* 轴和 *q* 轴对齐方式。

有关对齐类型的详细信息，请参阅 SynRM 约束曲线及其应用。

### **Number of pole pairs** — 电机中可用的极对数 `4`（默认值）| 标量

电机中可用的极对数。

### **Stator resistance per phase, Rs (Ohm)** — 定子相绕组电阻（ohms） `0.8`（默认值）| 标量

定子相绕组的电阻（以 ohms 为单位）。

### **Vdc input method** — Vdc 的输入方法 `Specify via dialog`（默认值）| `Input port - use 3D LUT (voltage slice based)` | `Input port - use 2D LUT (scaled-w based)`

使用以下方法之一指定 *Vdc* 输入。

- `Specify via dialog` — 使用 **DC voltage to compute LUTs (V)** 参数指定固定参考电压 *Vdc*。
- `Input port - use 3D LUT (voltage slice based)` — 使用输入端口 **Vdc** 指定可变参考电压 *Vdc*。使用此选项时，模块通过基于电压切片的 3-D 查找表 (LUT) 计算给定电压下的参考电流数据。
- `Input port - use 2D LUT (scaled-w based)` — 使用输入端口 `Vdc` 指定可变参考电压 *Vdc*。使用此选项时，模块通过基于电机速度 (ω) 缩放的 2-D LUT 计算给定电压下的参考电流数据。

### **DC voltage to compute LUTs (V)** — 直流母线电压（volts） `24`（默认值）| 标量

模块用于计算 LUT 的直流母线电压（以 volts 为单位）。

#### 依赖关系

要启用此参数，请将 **Vdc input method** 设置为 `Specify via dialog` 或 `Input port - use 2D LUT (scaled-w based)`。

### **DC voltage breakpoint vector, VdcVec (V)** — 直流母线电压查找向量（volts） `[18,30]`（默认值）| 向量

用于 *id* 和 *iq* 查找表的直流母线电压查找向量（以 volts 为单位）。

#### 依赖关系

要启用此参数，请将 **Vdc input method** 设置为 `Input port - use 3D LUT (voltage slice based)`。

### **Motor parameter input method** — 电机参数类型 `Linear model with lumped parameters`（默认值）| `Non-linear model with D,Q-flux linkage LUTs` | `Non-linear model with Ld and Lq LUTs` | `Non-linear model with Ld, Lq, and FluxPM LUTs` | `Non-linear model with id and iq LUTs`

模块用于生成控制参考电流的电机参数。将此参数设置为以下值之一：

- `Linear model with lumped parameters` — 使用电机参数 *Ld*、*Lq* 和 *FluxPM* 的集中电路值生成电流参考表。
- `Non-linear model with D,Q-flux linkage LUTs` — 使用 *d* 轴和 *q* 轴磁链查找表生成电流参考表。
- `Non-linear model with Ld and Lq LUTs` — 使用 *Ld* 和 *Lq* 查找表生成电流参考表。
- `Non-linear model with Ld, Lq, and FluxPM LUTs` — 使用 *Ld*、*Lq* 和 *FluxPM* 查找表生成电流参考表。
- `Non-linear model with id and iq LUTs` — 使用 *id* 和 *iq* 查找表确定电流参考。

#### 依赖关系

- 要启用 `Non-linear model with Ld and Lq LUTs` 选项，请将 **Motor topology** 设置为 `Synchronous reluctance motor`。
- 要启用 `Non-linear model with Ld, Lq, and FluxPM LUTs` 选项，请将 **Motor topology** 设置为 `PM-assisted synchronous reluctance motor`。

### **Enable percentages for torque breakpoint vector** — 为转矩断点向量启用百分比值 `off`（默认值）| on

选择此参数可指定百分比转矩断点向量值以及速度断点向量的转矩包络值（在以下参数中）：

- **Reference percentage torque breakpoint vector, Trefpct (%)**
- **Torque envelope for speed breakpoint vector, wrpm (rpm)**

### **Enable custom breakpoint vectors for torque and speed** — 为转矩和速度使用自定义断点 `off`（默认值）| on

启用此参数可对电机转矩和速度量使用自定义查找向量。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`、`Non-linear model with D,Q-flux linkage LUTs`、`Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs` 之一。

### **Reference percentage torque breakpoint vector, Trefpct (%)** — 转矩参考查找向量（百分比） `[0,50,100]`（默认值）| 向量

用于 *id* 和 *iq* 查找表的转矩参考查找向量（以百分比为单位）。该向量可以包含任意数量的元素。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`、`Non-linear model with D,Q-flux linkage LUTs`、`Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs` 之一。
- 选择 **Enable custom breakpoint vectors for torque and speed** 参数。
- 选择 **Enable percentages for torque breakpoint vector** 参数。

或

- 将 **Motor parameter input method** 设置为 `Non-linear model with id and iq LUTs`。
- 选择 **Enable percentages for torque breakpoint vector** 参数。

### **Torque envelope for speed breakpoint vector, wrpm (rpm)** — 速度断点向量的转矩包络值 `[0.3 0.3 0.15 0.05]`（默认值）| 向量

用于计算转矩参考查找向量百分比值的转矩包络值（在 **Reference percentage torque breakpoint vector, Trefpct (%)** 参数中指定）。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`、`Non-linear model with D,Q-flux linkage LUTs`、`Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs` 之一。
- 选择 **Enable custom breakpoint vectors for torque and speed** 参数。
- 选择 **Enable percentages for torque breakpoint vector** 参数。

或

- 将 **Motor parameter input method** 设置为 `Non-linear model with id and iq LUTs`。
- 选择 **Enable percentages for torque breakpoint vector** 参数。

### **Reference torque breakpoint vector, Tref (Nm)** — 转矩参考查找向量 `[0,0.15,0.3]`（默认值）| 向量

用于 *id* 和 *iq* 查找表的转矩参考查找向量（以 Nm 为单位）。该向量可以包含任意数量的元素。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`、`Non-linear model with D,Q-flux linkage LUTs`、`Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs` 之一。
- 选择 **Enable custom breakpoint vectors for torque and speed** 参数。

或

- 将 **Motor parameter input method** 设置为 `Non-linear model with id and iq LUTs`。

### **Mechanical speed breakpoint vector, wrpm (rpm)** — 转子速度查找向量 `[0,1000,2000,6000]`（默认值）| 向量

用于 *id* 和 *iq* 查找表的转子速度查找向量（以 rpm 为单位）。该向量可以包含任意数量的元素。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`、`Non-linear model with D,Q-flux linkage LUTs`、`Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs` 之一。
- 选择 **Enable custom breakpoint vectors for torque and speed** 参数。

或

- 将 **Motor parameter input method** 设置为 `Non-linear model with id and iq LUTs`。

### **Current Limit, I\_limit (A)** — 电机最大相电流限值（amperes） `7.1`（默认值）| 标量

电机的最大相电流限值（以 amperes 为单位）。

### **Viscous damping coefficient, Bv (Nm-s/rad)** — 粘性阻尼系数 `1e-6`（默认值）| 标量

电机的粘性阻尼系数 *Bv*，单位为 N·m/(rad/s)。

### **D-axis current breakpoint vector, id (A)** — D 轴电流查找向量 `[0,10,20,30]`（默认值）| 向量

*Ld*、*Lq* 和 *FluxPM* 查找表中的 D 轴电流向量（以 amperes 为单位）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 参数设置为 `Non-linear model with D,Q-flux linkage LUTs`、`Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs` 之一。

### **Q-axis current breakpoint vector, iq (A)** — Q 轴电流查找向量 `[0, 10, 20, 30, 40]`（默认值）| 向量

*Ld*、*Lq* 和 *FluxPM* 查找表中的 Q 轴电流向量（以 amperes 为单位）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 参数设置为 `Non-linear model with D,Q-flux linkage LUTs`、`Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs` 之一。

### **Use measured (instead of computed) torque** — 使用转矩的测量值 `off`（默认值）| on

启用此参数可向模块提供测量（而不是计算）的转矩查找数据。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with D,Q-flux linkage LUTs`、`Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs` 之一。

### **Measured torque LUT, T(id,iq) (Nm)** — 测量查找数据 `[0,0,0,0,0;0,0.4500,0.9000,1.3500,1.8000;0,0.9000,1.8000,2.7000,3.6000;0,1.3500,2.7000,4.0500,5.4000]`（默认值）| 向量

测量的转矩查找表数据（以 weber 为单位）。

#### 依赖关系

要启用此参数：

- 将 **Motor parameter input method** 设置为 `Non-linear model with D,Q-flux linkage LUTs`、`Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs` 之一。
- 选择 **Use measured (instead of computed) torque** 参数。

### 线性集中参数模型

### **Stator d-axis inductance, Ld (H)** — D 轴定子绕组电感 `0.9e-3`（默认值）| 标量

沿旋转 *dq* 参考系的直轴的定子绕组电感（以 henries 为单位）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`。

### **Stator q-axis inductance, Lq (H)** — Q 轴定子绕组电感 `0.15e-3`（默认值）| 标量

沿旋转 *dq* 参考系交轴的定子绕组电感（以 henries 为单位）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`。

### **Permanent magnet flux linkage (Wb)** — 永磁体磁链 `0.4e-3`（默认值）| 标量

峰值永磁体磁链（以 weber 为单位）。

#### 依赖关系

要启用此参数，请将 **Motor topology** 设置为 `PM-assisted synchronous reluctance motor`，并将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`。

### 使用 D,Q 磁链 LUT 的非线性模型

### **D-axis flux linkage LUT, FluxD (id,iq) (Wb)** — 参考 d 轴磁链查找数据 `[0,0,0,0,0;0.009,0.009,0.009,0.009,0.0090;0.018,0.018,0.018,0.018,0.0180;0.027,0.027,0.027,0.027,0.0270]`（默认值）| 向量

D 轴磁链查找表数据（以 weber 为单位）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with D,Q-flux linkage LUTs`。

### **Q-axis flux linkage LUT, FluxQ (id,iq) (Wb)** — 参考 q 轴磁链查找数据 `[0,0.0015,0.003,0.0045,0.0060;0,0.0015,0.003,0.0045,0.0060;0,0.0015,0.003,0.0045,0.0060;0,0.0015,0.003,0.0045,0.0060]`（默认值）| 向量

Q 轴磁链查找表数据（以 weber 为单位）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with D,Q-flux linkage LUTs`。

### 使用 *Ld* 和 *Lq*（以及 *Ld*、*Lq* 和 *FluxPM*）LUT 的非线性模型

### **Ld LUT, Ld(id,iq) (H)** — D 轴电感查找数据 `0.9e-3 * ones(4, 5)`（默认值）| 矩阵

D 轴电感查找表数据（以 henries 为单位）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

### **Lq LUT, Lq(id,iq) (H)** — Q 轴电感查找数据 `0.15e-3 * ones(4, 5)`（默认值）| 矩阵

Q 轴电感查找表数据（以 henries 为单位）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

### **PM flux linkage LUT, FluxPM(id,iq) (Wb)** — 永磁体磁链查找数据 `0.4e-4 * ones(4, 5)`（默认值）| 矩阵

永磁体磁链查找表数据（以 weber 为单位）。

#### 依赖关系

要启用此参数：

- 将 **Motor topology** 设置为 `PM-assisted synchronous reluctance motor`。
- 将 **Motor parameter input method** 设置为 `Non-linear model with Ld, Lq, and FluxPM LUTs`。

### 使用 *id* 和 *iq* LUT 的非线性模型

### **Reference id LUT, id(Tref,wrpm) (A)** — 参考 d 轴电流查找数据 `[0,0,0,0;3.9091,3.9091,3.9091,0;7.1,7.1,7.1,0]`（默认值）| 矩阵

D 轴电流参考 2-D 查找表数据（以 amperes 为单位）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with id and iq LUTs`，并将 **Vdc input method** 设置为 `Specify via dialog` 或 `Input port - use 2D LUT (scaled-w based)`。

### **Reference id LUT, id(Tref,wrpm,Vdc) (A)** — 参考 d 轴电流查找数据 `cat(3,[0,0,0,0;3.8539,3.8539,3.8539,0;6.9513,6.9513,6.9513,0],[0,0,0,0;3.8539,3.8539,3.8539,3.7611;6.9513,6.9513,6.9513,5.4848])`（默认值）| 矩阵

D 轴电流参考 3-D 查找表数据（以 amperes 为单位）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Non-linear model with id and iq LUTs`，并将 **Vdc input method** 设置为 `Input port - use 3D LUT (voltage slice based)`。

### **Reference iq LUT, iq(Tref,wrpm) (A)** — 参考 q 轴电流查找数据 `-1*[0,0,0,-7.1;0,0,0,-7.1;0,0,0,-7.1]`（默认值）| 矩阵

Q 轴电流参考 2-D 查找表数据（以 amperes 为单位）。

#### 依赖关系

要启用此参数，请将 **电机参数输入方法** 设置为 `Non-linear model with id and iq LUTs`，并将 **Vdc 输入方法** 设置为 `Specify via dialog` 或 `Input port - use 2D LUT (scaled-w based)`。

### **参考 iq LUT，iq(Tref,wrpm,Vdc) (A)** — 参考 q 轴电流查找表数据 `-1*cat(3,[0,0,0,-7.1;-0.4579,-0.4579,-0.4579,-7.1;-1.4457,-1.4457,-1.4457,-7.1],[0,0,0,0;-0.4579,-0.4579,-0.4579,-1.2581;-1.4457,-1.4457,-1.4457,-4.5085])` (默认) | matrix

q 轴电流参考 3-D 查找表数据（以 amperes 为单位）。

#### 依赖关系

要启用此参数，请将 **电机参数输入方法** 设置为 `Non-linear model with id and iq LUTs`，并将 **Vdc 输入方法** 设置为 `Input port - use 3D LUT (voltage slice based)`。

### 输入单位

### **输入单位** — 模块输入值的度量单位 `Per-Unit (PU)` (默认) | `SI Units`

模块输入值的度量单位。

### **基准电压 (V)** — 标称电压限值 `24/sqrt(3)` (默认) | scalar

用于标幺值系统的基准电压（以 volts 为单位）。

#### 依赖关系

要启用此参数，请将 **输入单位** 设置为 `Per-Unit (PU)`。

### **基准电流 (A)** — 标称电流限值 `19.3` (默认) | scalar

用于标幺值系统的基准电流（以 amperes 为单位）。

#### 依赖关系

要启用此参数，请将 **输入单位** 设置为 `Per-Unit (PU)`。

### **基准转速 (rpm)** — 标称转速限值 `4107` (默认) | scalar

用于标幺值系统的基准转速（以 rpm 为单位）。

#### 依赖关系

要启用此参数，请将 **输入单位** 设置为 `Per-Unit (PU)`。

### **基准转矩 (Nm)** — 标称转矩限值 `0.74112` (默认)

对应于 1 标幺值的转矩（以 Nm 为单位）。更多详细信息，请参阅标幺值系统页面。

您无法配置此参数。模块使用其他参数在内部计算此值。

#### 依赖关系

要启用此参数，请将 **输入单位** 设置为 `Per-Unit (PU)`。

### **允许在 CodeGen 中使用按比例缩小的电机参数（使用 Fixed-Point 数据类型时精度更高）** — 缩小内部参数以匹配标幺值比例 `on` (默认) | `off`

在生成代码时缩小内部参数以匹配标幺值比例的选项。

- 启用此选项时，模块会缩小内部常量和系数以匹配标幺值比例。这在使用 fixed-point 数据类型时可以获得更高精度。如果将此选项与 single 或 double 数据类型一起使用，根据分配给整数部分的位数，可能会发生一些精度损失。
- 禁用此选项时，模块会将其用于内部计算的所有常量和系数转换为 SI 单位，然后再将它们转换回标幺值比例。这允许您在生成的代码中更新查找表值，通常用于控制器调优或下线操作等应用。您也可以手动更新这些值，以便调试或重用以前生成的代码。

#### 依赖关系

要启用此参数，请将 **电机参数输入方法** 设置为 `Non-linear model with id and iq LUTs`，并将 **输入单位** 设置为 `Per-Unit (PU)`。

### 绘图选项

仅当您满足以下条件时，模块才会启用此选项卡：

- 将 **电机参数输入方法** 设置为 `Linear model with lumped parameters`、`Non-linear model with D,Q-flux linkage LUTs`、`Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs`。
- 将 **Vdc 输入方法** 设置为 `Specify via dialog`。

### **启用保存计算出的 LUTs** — 启用模块以保存计算出的 LUTs `off` (默认) | `on`

启用模块以保存当您点击 **计算（并绘制）id 和 iq LUTs** 按钮时模块计算出的查找表数据。

更多详细信息，请参阅直接从模块参数对话框绘制 PMSM 和 SynRM 的约束曲线和驱动特性。

### **计算（并绘制）id 和 iq LUTs** — 计算（并绘制）*id* 和 *iq* 查找数据按钮

当您点击此按钮时，模块会计算（并绘制）*id* 和 *iq* 电流的查找表数据。

更多详细信息，请参阅直接从模块参数对话框绘制 PMSM 和 SynRM 的约束曲线和驱动特性。

### **使用默认绘图选项** — 使用默认选项绘制约束曲线 `on` (默认) | `off`

启用模块以在您点击 **绘制约束曲线** 按钮绘制电机约束曲线时使用默认绘图选项。

更多详细信息，请参阅直接从模块参数对话框绘制 PMSM 和 SynRM 的约束曲线和驱动特性。

### **电机转速 (RPM)** — 用于绘制约束曲线的电机转速 `3000` (默认) | scalar

当您点击 **绘制约束曲线** 按钮绘制电机约束曲线时，模块应使用的电机转速（以 RPM 为单位）。

更多详细信息，请参阅直接从模块参数对话框绘制 PMSM 和 SynRM 的约束曲线和驱动特性。

#### 依赖关系

要启用此参数，请清除 **使用默认绘图选项** 参数。

### **电机转矩 (Nm)** — 用于绘制约束曲线的电机转矩 `0.1` (默认) | scalar

当您点击 **绘制约束曲线** 按钮绘制电机约束曲线时，模块应使用的电机转矩（以 Nm 为单位）。

更多详细信息，请参阅直接从模块参数对话框绘制 PMSM 和 SynRM 的约束曲线和驱动特性。

#### 依赖关系

要启用此参数，请清除 **使用默认绘图选项** 参数。

### **启用绘制驱动特性** — 启用模块以绘制驱动特性 `off` (默认) | `on`

启用模块以在您点击 **绘制约束曲线** 按钮绘制电机约束曲线时绘制驱动特性。

更多详细信息，请参阅直接从模块参数对话框绘制 PMSM 和 SynRM 的约束曲线和驱动特性。

#### 依赖关系

要启用此参数，请清除 **使用默认绘图选项** 参数。

### **包含增大电机电流时的驱动特性** — 启用模块以绘制增大电机电流时的驱动特性 `off` (默认) | `on`

启用模块以包含增大电机电流时的驱动特性（在点击 **绘制约束曲线** 按钮后生成的绘图中）。

**注意**

要成功绘制增大电机电流时的特性，该电流必须高于电机的额定电流。

更多详细信息，请参阅直接从模块参数对话框绘制 PMSM 和 SynRM 的约束曲线和驱动特性。

#### 依赖关系

要启用此参数，请清除 **使用默认绘图选项** 参数，并选择 **启用绘制驱动特性** 参数。

### **绘制约束曲线** — 绘制电机约束曲线按钮

当您点击此按钮时，模块会绘制电机的约束曲线。

更多详细信息，请参阅直接从模块参数对话框绘制 PMSM 和 SynRM 的约束曲线和驱动特性。

### **计算并显示** — 计算并显示特性转矩和转速按钮

当您点击此按钮时，模块会计算并显示以下转矩和转速特性：

- 额定转矩 — 电机的额定转矩（以 Nm 为单位）。
- 额定转速 — 电机的额定转速（以 RPM 为单位）。
- 最大转速 — 电机的最大转速（以 RPM 为单位）。

更多详细信息，请参阅直接从模块参数对话框绘制 PMSM 和 SynRM 的约束曲线和驱动特性。

## 所属库

Motor Control Blockset / Controls / Control Reference

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

为 SynRM 和 PMaSynRM 的磁场定向控制生成基于查找表的控制参考电流

LUT based SynRM Control Reference 模块生成同步磁阻电机 (SynRM) 和永磁辅助同步磁阻电机 (PMaSynRM) 的磁场定向控制和弱磁控制的 *d* 轴和 *q* 轴参考电流。您可以指定参考转矩和反馈机械转速，该模块输出对应的参考电流值。该模块还支持每安培最大转矩 (MTPA) 和每伏特最大转矩 (MTPV) 运行区域。

该模块使用 *id(T,ω)* 和 *iq(T,ω)* 查找表 (LUT) 生成参考电流值。根据用于指定电机参数的输入方法，该模块可以生成 LUT，或使用您提供的数据。

您可以使用以下方法之一指定电机参数。

**注意**

以下用于 SynRM 和 PMaSynRM 的方程采用与永磁同步电机 (PMSM) 相同的 *d*-*q* 轴符号表示法。

- `Linear model with lumped parameters` — 具有 *Ld* 和 *Lq* 的集中参数（用于 SynRM），或具有 *Ld*、*Lq* 和 *FluxPM* 的集中参数（用于 PMaSynRM）

  此方法使用集中参数计算 *id* 和 *iq* LUT。该模块通过求解与这些曲线相关的方程，针对给定的 *ω* 和 *T* 输入获得 *id* 和 *iq*。

  每安培最大转矩 (MTPA) 曲线（用于 SynRM）

  id+iq=0

  每安培最大转矩 (MTPA) 曲线（用于 PMaSynRM）

  id2+idψm(Ld−Lq)=iq2.

  恒定转矩轨迹（用于 SynRM）

  iq=T1.5Pp(Ld−Lq)id

  恒定转矩轨迹（用于 PMaSynRM）

  iq=T1.5Pp(ψm+(Ld−Lq)id).

  电流限制曲线

  id2+iq2=imax2.

  电压限制曲线（用于 SynRM）

  (VDC3)2=(idRs−ωeLqiq)2+(iqRs+ωeLdid)2.

  电压限制曲线（用于 PMaSynRM）

  (VDC3)2=(idRs−ωeLqiq)2+(iqRs+ωeLdid+ωeψm)2.

  - 当电机在电压约束内运行时，该模块求解 MTPA 线与恒定转矩轨迹的交点。
  - 当电机超出电压约束运行时，该模块求解电压约束曲线与恒定转矩轨迹的交点。

  在根据 *ω* 和 *T* 值网格计算出 *id* 和 *iq* 表之后，该模块使用插值来为处于表值范围内的任何 *ω* 和 *T* 输入找到 *id ref* 和 *iq ref*。对于超出边界的 *ω* 和 *T* 值，表值会被裁剪。
- `Non-linear model with Ld and Lq LUTs` 或 `Non-linear model with Ld, Lq, and FluxPM LUTs` — 具有 *d* 轴和 *q* 轴定子绕组电感以及永磁体磁链查找表的非线性模型

  此方法使用与集中参数方法类似的方法，不同之处在于，该模块在每次计算 *id* 和 *iq* 时更新 *Ld(id,iq)*、*Lq(id,iq)* 和 *FluxPM(id,iq)* 的值。该模块迭代这些计算，直到 *id* 和 *iq* 值收敛。

  **注意**

  *FluxPM(id,iq)* 值仅适用于 PMaSynRM。*Ld(id,iq)* 和 *Lq(id,iq)* 值适用于 SynRM 和 PMaSynRM。
- `Non-linear model with D,Q-flux linkage LUTs` — 具有 *d* 轴和 *q* 轴磁链查找表的非线性模型。

  此方法使用与集中参数方法类似的方法，不同之处在于，该模块在每次计算 *id* 和 *iq* 时更新 *ψd(id,iq)* 和 *ψq(id,iq)* 的值。该模块迭代这些计算，直到 *id* 和 *iq* 值收敛。
- `Non-linear model with id and iq LUTs` — 当您想手动提供 *id(T,ω)* 和 *iq(T,ω)* 表时，使用此方法。通常，您通过仿真或测功机测试获得这些表。

您还可以使用 Motor Control Blockset™ 中的 `mcb.generateMotorLUT` 函数生成这些表。

有关 Motor Control Blockset 用于同步磁阻电机的详细方程组和假设，请参阅 Synchronous Reluctance Machine (Simscape Electrical)。

此外，您可以使用 **Vdc input method** 参数将该模块配置为通过 **DC voltage to compute LUTs (V)** 参数接受固定参考直流电压，或通过单独输入端口 **Vdc** 接受可变参考直流电压。

根据您在 **Motor parameter input method** 参数中选择的方法，您可以使用集中参数或非线性模型按此表所示计算参考电流。

| **Motor parameter input method** | **Vdc input method** | **用于计算参考电流的技术** |
| --- | --- | --- |
| `Linear model with lumped parameters` | `Specify via dialog` | 该模块使用集中参数为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压计算 *id* 和 *iq* LUT，并使用这些 LUT 确定参考电流。 |
| `Input port - use 3D LUT (voltage slice based)` | 该模块使用集中参数计算 3-D *id* 和 *iq* LUT，其中包含不同电压（或 **DC bus voltage breakpoint vector, Vdc (V)** 参数中指定的电压切片）的数据。它使用这些数据确定与输入端口 **Vdc** 处指定电压对应的参考电流。 |
| `Input port - use 2D LUT (scaled-w based)` | 该模块使用集中参数为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压计算 2-D *id* 和 *iq* LUT。它使用这些 LUT 通过缩放转速 (ω) 来计算（与输入端口 **Vdc** 处提供的电压对应的）参考电流。 |
| `Non-linear model with D,Q-flux linkage LUTs` | `Specify via dialog` | 该模块通过使用 *d* 轴和 *q* 轴磁链 LUT，为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压计算参考电流。 |
| `Input port - use 3D LUT (voltage slice based)` | 该模块使用 3-D *d* 轴和 *q* 轴磁链 LUT，其中包含不同电压（或 **DC bus voltage breakpoint vector, Vdc (V)** 参数中指定的电压切片）的数据。它使用这些 LUT 计算与输入端口 **Vdc** 处提供的电压对应的参考电流。 |
| `Input port - use 2D LUT (scaled-w based)` | 该模块使用 2-D *d* 轴和 *q* 轴磁链 LUT，为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压。它使用这些 LUT 通过缩放转速 (ω) 来计算（与输入端口 **Vdc** 处提供的电压对应的）参考电流。 |
| `Non-linear model with Ld and Lq LUTs` | `Specify via dialog` | 该模块通过使用给定的 *Ld* 和 *Lq* LUT，为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压计算参考电流。 |
| `Input port - use 3D LUT (voltage slice based)` | 该模块使用给定的 3-D *Ld* 和 *Lq* LUT，其中包含不同电压（或 **DC bus voltage breakpoint vector, Vdc (V)** 参数中指定的电压切片）的数据。它使用这些 LUT 计算与输入端口 **Vdc** 处提供的电压对应的参考电流。 |
| `Input port - use 2D LUT (scaled-w based)` | 该模块使用给定的 2-D *Ld* 和 *Lq* LUT，为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压。它使用这些 LUT 通过缩放转速 (ω) 来计算（与输入端口 **Vdc** 处提供的电压对应的）参考电流。 |
| `Non-linear model with Ld, Lq, and FluxPM LUTs` | `Specify via dialog` | 该模块通过使用给定的 *Ld*、*Lq* 和永磁体磁链 LUT，为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压计算参考电流。 |
| `Input port - use 3D LUT (voltage slice based)` | 该模块使用给定的 3-D *Ld*、*Lq* 和永磁体磁链 LUT，其中包含不同电压（或 **DC bus voltage breakpoint vector, Vdc (V)** 参数中指定的电压切片）的数据。它使用这些 LUT 计算与输入端口 **Vdc** 处提供的电压对应的参考电流。 |
| `Input port - use 2D LUT (scaled-w based)` | 该模块使用给定的 2-D *Ld*、*Lq* 和永磁体磁链 LUT，为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压。它使用这些 LUT 通过缩放转速 (ω) 来计算（与输入端口 **Vdc** 处提供的电压对应的）参考电流。 |
| `Non-linear model with id and iq LUTs` | `Specify via dialog` | 该模块通过使用给定的 *id*、*iq* LUT，为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压确定参考电流。 |
| `Input port - use 3D LUT (voltage slice based)` | 该模块使用给定的 3-D *id*、*iq* LUT，其中包含不同电压（或 **DC bus voltage breakpoint vector, Vdc (V)** 参数中指定的电压切片）的数据。它使用这些 LUT 确定与输入端口 **Vdc** 处提供的电压对应的参考电流。 |
| `Input port - use 2D LUT (scaled-w based)` | 该模块使用给定的 2-D *id*、*iq* LUT，为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压。它使用这些 LUT 通过缩放转速 (ω) 来计算（与输入端口 **Vdc** 处提供的电压对应的）参考电流。 |
