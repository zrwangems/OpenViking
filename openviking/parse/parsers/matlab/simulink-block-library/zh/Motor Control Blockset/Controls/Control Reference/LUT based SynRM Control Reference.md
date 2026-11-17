---
type: simulink-block
title: 'LUT based SynRM Control Reference'
family: 'mcb'
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

参考转矩输入值（单位：Nm），模块根据该值计算参考电流。

**数据类型：** `single` | `double` | `fixed point`

### **⍵m** — 机械转速标量

参考机械转速值（单位：rad/sec），模块根据该值计算参考电流。

**数据类型：** `single` | `double` | `fixed point`

### **Vdc** — 直流母线电压标量

可变直流母线电压（单位：伏特）。

#### 依赖

要启用此端口，请将 **Vdc input method** 设置为 `Input
port - use 3D LUT (voltage slice based)` 或
`输入端口 - 使用二维查找表（缩放-w
based)`。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **Id ref** — 参考 *d* 轴电流标量

参考 *d* 轴相电流（单位：安培）。

**数据类型：** `single` | `double` | `fixed point`

### **Iq ref** — 参考 *q* 轴电流标量

参考 *q* 轴相电流（单位：安培）。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### 电机参数

### **Motor topology** — 同步磁阻电机拓扑 `Synchronous reluctance motor`（默认）| `PM-assisted synchronous reluctance motor`

同步磁阻电机的类型。

### **Definition of d-axis and q-axis** — *d* 轴和 *q* 轴的对齐方式 `Ld > Lq (different from PMSM)`（默认）| `Lq > Ld (same as PMSM)`

*d* 轴和 *q* 轴的对齐类型。您可以选择以下选项之一：

- `Ld > Lq (different from PMSM)` — 选择此选项以使用与 PMSM 不同的 *d* 轴和 *q* 轴对齐方式。
- `Lq > Ld (same as PMSM)` — 选择此选项以使用与 PMSM 相同的 *d* 轴和 *q* 轴对齐方式。

有关对齐类型的更多信息，请参阅 SynRM Constraint Curves and Their Application。

### **Number of pole pairs** — 电机中可用的极对数 `4`（默认）| 标量

电机中可用的极对数。

### **Stator resistance per phase, Rs (Ohm)** — 定子相绕组电阻（欧姆） `0.8`（默认）| 标量

定子相绕组的电阻（单位：欧姆）。

### **Vdc input method** — Vdc 的输入方法 `Specify via dialog`（默认）| `Input port - use 3D LUT (voltage slice based)` | `输入端口 - 使用二维查找表（缩放-w based)`

使用以下方法之一来指定 *Vdc* 输入。

- `Specify via dialog` — 使用 **DC voltage
  to compute LUTs (V)** 参数指定固定参考电压 *Vdc*。
- `输入端口 - 使用三维查找表（电压切片
  based)` — 使用输入端口 **Vdc** 指定可变参考电压 *Vdc*。使用此选项时，模块通过基于电压切片的 3-D 查找表（LUT）计算给定电压下的参考电流数据。
- `输入端口 - 使用二维查找表（缩放-w
  based)` — 使用输入端口 `Vdc` 指定可变参考电压 *Vdc*。使用此选项时，模块通过基于电机转速（ω）缩放的 2-D LUT 计算给定电压下的参考电流数据。

### **DC voltage to compute LUTs (V)** — 直流母线电压（伏特） `24`（默认）| 标量

模块用于计算 LUT 的直流母线电压（单位：伏特）。

#### 依赖

要启用此参数，请将 **Vdc input method** 设置为 `Specify via dialog` 或 `Input port
- use 2D LUT (scaled-w based)`。

### **DC voltage breakpoint vector, VdcVec (V)** — 直流母线电压查找向量（伏特） `[18,30]`（默认）| 向量

用于 *id* 和 *iq* 查找表的直流母线电压查找向量（单位：伏特）。

#### 依赖

要启用此参数，请将 **Vdc input method** 设置为 `Input port - use 3D LUT (voltage slice
based)`。

### **Motor parameter input method** — 电机参数类型 `Linear model with lumped parameters`（默认）| `非线性模型，采用 D、Q 磁链 LUTs` | `Non-linear model with Ld and Lq LUTs` | `非线性模型，采用 Ld、Lq 和 FluxPM LUTs` | `非线性模型，采用 id 和 iq LUTs`

模块用于生成控制参考电流的电机参数。将该参数设置为以下值之一：

- `Linear model with lumped parameters` — 使用电机参数 *Ld*、*Lq* 和 *FluxPM* 的集中电路值生成电流参考表。
- `非线性模型，采用 D、Q 磁链 LUTs` — 使用 *d* 轴和 *q* 轴磁链查找表生成电流参考表。
- `Non-linear model with Ld and Lq LUTs` — 使用 *Ld* 和 *Lq* 查找表生成电流参考表。
- `非线性模型，采用 Ld、Lq 和 FluxPM LUTs` — 使用 *Ld*、*Lq* 和 *FluxPM* 查找表生成电流参考表。
- `非线性模型，采用 id 和 iq LUTs` — 使用 *id* 和 *iq* 查找表确定电流参考。

#### 依赖关系

- 要启用 `Non-linear model with Ld and Lq LUTs` 选项，请将 **Motor topology** 设置为 `Synchronous reluctance motor`。
- 要启用 `非线性模型，采用 Ld、Lq 和 FluxPM LUTs` 选项，请将 **Motor topology** 设置为 `PM-assisted synchronous reluctance motor`。

### **Enable percentages for torque breakpoint vector** — 启用转矩断点向量的百分比值 `off`（默认）| on

选择此参数可指定百分比转矩断点向量值以及速度断点向量的转矩包络值（在以下参数中）：

- **Reference percentage torque breakpoint vector, Trefpct (%)**
- **Torque envelope for speed breakpoint vector, wrpm (rpm)**

### **Enable custom breakpoint vectors for torque and speed** — 使用转矩和速度的自定义断点 `off`（默认）| on

启用此参数可使用电机转矩和速度量的自定义查找向量。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`、`非线性模型，采用 D、Q 磁链 查找表`、`非线性模型，采用 Ld 和 Lq LUTs` 或 `非线性模型，采用 Ld、Lq 和 FluxPM LUTs`。

### **Reference percentage torque breakpoint vector, Trefpct (%)** — 转矩参考查找向量（以百分比表示）`[0,50,100]`（默认）| 向量

用于 *id* 和 *iq* 查找表的转矩参考查找向量（以百分比表示）。该向量可以具有任意数量的元素。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 将 **Motor parameter input method** 设置为 `Linear model with lumped parameters`、`非线性模型，采用 D、Q 磁链 查找表`、`非线性模型，采用 Ld 和 Lq LUTs` 或 `非线性模型，采用 Ld、Lq 和 FluxPM LUTs`。
- 选择 **Enable custom breakpoint vectors for torque and speed** 参数。
- 选择 **Enable percentages for torque breakpoint vector** 参数。

或

- 将 **Motor parameter input method** 设置为 `非线性模型，采用 id 和 iq LUTs`。
- 选择 **Enable percentages for torque breakpoint vector** 参数。

### **Torque envelope for speed breakpoint vector, wrpm (rpm)** — 速度断点向量的转矩包络值 `[0.3 0.3 0.15 0.05]`（默认）| 向量

用于计算转矩参考查找向量百分比值的转矩包络值（在 **Reference percentage torque breakpoint vector, Trefpct (%)** 参数中指定）。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 将 **电机参数输入方法** 设置为
  `Linear model with lumped parameters`、
  `非线性模型，采用 D、Q 磁链
  查找表`、`非线性模型，采用 Ld 和 Lq
  LUTs` 或 `Non-linear model with Ld,
  Lq, and FluxPM LUTs`。
- 选中 **启用转矩和转速的自定义断点向量** 参数。
- 选中 **启用转矩断点向量的百分比** 参数。

或

- 将 **电机参数输入方法** 设置为
  `非线性模型，采用 id 和 iq
  LUTs`。
- 选中 **启用转矩断点向量的百分比** 参数。

### **参考转矩断点向量，Tref (Nm)** — 转矩参考查找向量 `[0,0.15,0.3]`（默认）| 向量

用于 *id* 和 *iq* 查找表（以 Nm 为单位）的转矩参考查找向量。该向量可以包含任意数量的元素。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 将 **电机参数输入方法** 设置为
  `Linear model with lumped parameters`、
  `非线性模型，采用 D、Q 磁链
  查找表`、`非线性模型，采用 Ld 和 Lq
  LUTs` 或 `Non-linear model with Ld,
  Lq, and FluxPM LUTs`。
- 选中 **启用转矩和转速的自定义断点向量** 参数。

或

- 将 **电机参数输入方法** 设置为
  `非线性模型，采用 id 和 iq
  LUTs`。

### **机械转速断点向量，wrpm (rpm)** — 转子转速查找向量 `[0,1000,2000,6000]`（默认）| 向量

用于 *id* 和 *iq* 查找表（以 rpm 为单位）的转子转速查找向量。该向量可以包含任意数量的元素。

#### 依赖关系

要启用此参数，请执行以下任一操作：

- 将 **电机参数输入方法** 设置为
  `Linear model with lumped parameters`、
  `非线性模型，采用 D、Q 磁链
  查找表`、`非线性模型，采用 Ld 和 Lq
  LUTs` 或 `Non-linear model with Ld,
  Lq, and FluxPM LUTs`。
- 选中 **启用转矩和转速的自定义断点向量** 参数。

或

- 将 **电机参数输入方法** 设置为
  `非线性模型，采用 id 和 iq
  LUTs`。

### **电流限值，I\_limit (A)** — 电机最大相电流限值（安培）`7.1`（默认）| 标量

电机的最大相电流限值（以安培为单位）。

### **粘性阻尼系数，Bv (Nm-s/rad)** — 粘性阻尼系数 `1e-6`（默认）| 标量

电机的粘性阻尼系数 *Bv*，单位为 N·m/(rad/s)。

### **D 轴电流断点向量，id (A)** — D 轴电流查找向量 `[0,10,20,30]`（默认）| 向量

*Ld*、*Lq* 和 *FluxPM* 查找表中的 D 轴电流向量（以安培为单位）。

#### 依赖关系

要启用此参数，请将 **电机参数输入方法** 参数设置为 `Non-linear model with
D、Q 磁链查找表`、`非线性模型，采用
Ld and Lq LUTs` 或 `Non-linear model with Ld,
Lq, and FluxPM LUTs`。

### **Q 轴电流断点向量，iq (A)** — Q 轴电流查找向量 `[0, 10, 20, 30, 40]`（默认）| 向量

*Ld*、*Lq* 和 *FluxPM* 查找表中的 Q 轴电流向量（以安培为单位）。

#### 依赖关系

要启用此参数，请将 **电机参数输入方法** 参数设置为 `Non-linear model with
D、Q 磁链查找表`、`非线性模型，采用
Ld and Lq LUTs` 或 `Non-linear model with Ld,
Lq, and FluxPM LUTs`。

### **使用实测（而非计算）转矩** — 使用转矩实测值 `off`（默认）| on

启用此参数以向模块提供实测（而非计算）的转矩查找数据。

#### 依赖关系

要启用此参数，请将 **电机参数输入方法** 设置为 `Non-linear model with D,Q-flux
linkage 查找表`、`非线性模型，采用 Ld 和 Lq
LUTs` 或 `Non-linear model with Ld, Lq, and
FluxPM LUTs`。

### **实测转矩 LUT，T(id,iq) (Nm)** — 实测查找数据 `[0,0,0,0,0;0,0.4500,0.9000,1.3500,1.8000;0,0.9000,1.8000,2.7000,3.6000;0,1.3500,2.7000,4.0500,5.4000]`（默认）| 向量

实测转矩查找表数据（以 weber 为单位）。

#### 依赖关系

要启用此参数：

- 将 **Motor parameter input method** 设置为
  `非线性模型，采用 D、Q 磁链
  查找表`、`非线性模型，采用 Ld 和 Lq
  LUTs` 或 `Non-linear model with Ld, Lq,
  and FluxPM LUTs`。
- 选中 **Use measured (instead of computed)
  torque** 参数。

### 集总参数线性模型

### **Stator d-axis inductance, Ld (H)** — D 轴定子绕组电感 `0.9e-3`（默认）| 标量

沿旋转 *dq* 参考坐标系直轴的定子绕组电感（单位：亨利）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input
method** 设置为 `Linear model with lumped
parameters`。

### **Stator q-axis inductance, Lq (H)** — Q 轴定子绕组电感 `0.15e-3`（默认）| 标量

沿旋转 *dq* 参考坐标系交轴的定子绕组电感（单位：亨利）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input
method** 设置为 `Linear model with lumped
parameters`。

### **Permanent magnet flux linkage (Wb)** — 永磁体磁链 `0.4e-3`（默认）| 标量

峰值永磁体磁链（单位：韦伯）。

#### 依赖关系

要启用此参数，请将 **Motor topology** 设置为
`PM-assisted synchronous reluctance motor`，并将
**Motor parameter input method** 设置为 `Linear
集总参数模型`。

### 带 D、Q 磁链 LUT 的非线性模型

### **D-axis flux linkage LUT, FluxD (id,iq) (Wb)** — 参考 d 轴磁链查找数据 `[0,0,0,0,0;0.009,0.009,0.009,0.009,0.0090;0.018,0.018,0.018,0.018,0.0180;0.027,0.027,0.027,0.027,0.0270]`（默认）| 向量

D 轴磁链查找表数据（单位：韦伯）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input
method** 设置为 `非线性模型，采用 D、Q 磁链
LUTs`。

### **Q-axis flux linkage LUT, FluxQ (id,iq) (Wb)** — 参考 q 轴磁链查找数据 `[0,0.0015,0.003,0.0045,0.0060;0,0.0015,0.003,0.0045,0.0060;0,0.0015,0.003,0.0045,0.0060;0,0.0015,0.003,0.0045,0.0060]`（默认）| 向量

Q 轴磁链查找表数据（单位：韦伯）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input
method** 设置为 `非线性模型，采用 D、Q 磁链
LUTs`。

### 带 *Ld* 和 *Lq*（以及 *Ld*、*Lq* 和 *FluxPM*）LUT 的非线性模型

### **Ld LUT, Ld(id,iq) (H)** — D 轴电感查找数据 `0.9e-3 * ones(4, 5)`（默认）| 矩阵

D 轴电感查找表数据（单位：亨利）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input
method** 设置为 `Non-linear model with Ld and Lq
LUTs` 或 `Non-linear model with Ld, Lq, and
FluxPM LUTs`。

### **Lq LUT, Lq(id,iq) (H)** — Q 轴电感查找数据 `0.15e-3 * ones(4, 5)`（默认）| 矩阵

Q 轴电感查找表数据（单位：亨利）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input
method** 设置为 `Non-linear model with Ld and Lq
LUTs` 或 `Non-linear model with Ld, Lq, and
FluxPM LUTs`。

### **PM flux linkage LUT, FluxPM(id,iq) (Wb)** — 永磁体磁链查找数据 `0.4e-4 * ones(4, 5)`（默认）| 矩阵

永磁体磁链查找表数据（单位：韦伯）。

#### 依赖关系

要启用此参数：

- 将 **Motor topology** 设置为 `PM-assisted
  synchronous reluctance motor`。
- 将 **Motor parameter input method** 设置为
  `非线性模型，采用 Ld、Lq 和 FluxPM
  LUTs`。

### 带 *id* 和 *iq* LUT 的非线性模型

### **Reference id LUT, id(Tref,wrpm) (A)** — 参考 d 轴电流查找数据 `[0,0,0,0;3.9091,3.9091,3.9091,0;7.1,7.1,7.1,0]`（默认）| 矩阵

D 轴电流参考二维查找表数据（单位：安培）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input
method** 设置为 `非线性模型，采用 id 和 iq
LUTs`，并将 **Vdc input method** 设置为
`Specify via dialog` 或 `Input port
- use 2D LUT (scaled-w based)`。

### **Reference id LUT, id(Tref,wrpm,Vdc) (A)** — 参考 d 轴电流查找表数据 `cat(3,[0,0,0,0;3.8539,3.8539,3.8539,0;6.9513,6.9513,6.9513,0],[0,0,0,0;3.8539,3.8539,3.8539,3.7611;6.9513,6.9513,6.9513,5.4848])`（默认）| 矩阵

d 轴电流参考三维查找表数据（单位为安培）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `非线性模型，采用 id 和 iq LUTs`，并将 **Vdc input method** 设置为 `Input port - use 3D LUT (voltage slice based)`。

### **Reference iq LUT, iq(Tref,wrpm) (A)** — 参考 q 轴电流查找表数据 `-1*[0,0,0,-7.1;0,0,0,-7.1;0,0,0,-7.1]`（默认）| 矩阵

q 轴电流参考二维查找表数据（单位为安培）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `非线性模型，采用 id 和 iq LUTs`，并将 **Vdc input method** 设置为 `Specify via dialog` 或 `输入端口 - 使用二维查找表（缩放-w based)`。

### **Reference iq LUT, iq(Tref,wrpm,Vdc) (A)** — 参考 q 轴电流查找表数据 `-1*cat(3,[0,0,0,-7.1;-0.4579,-0.4579,-0.4579,-7.1;-1.4457,-1.4457,-1.4457,-7.1],[0,0,0,0;-0.4579,-0.4579,-0.4579,-1.2581;-1.4457,-1.4457,-1.4457,-4.5085])`（默认）| 矩阵

q 轴电流参考三维查找表数据（单位为安培）。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `非线性模型，采用 id 和 iq LUTs`，并将 **Vdc input method** 设置为 `Input port - use 3D LUT (voltage slice based)`。

### 输入单位

### **Input units** — 模块输入值的测量单位 `Per-Unit (PU)`（默认）| `SI Units`

模块输入值的测量单位。

### **Base voltage (V)** — 标称电压限值 `24/sqrt(3)`（默认）| 标量

标幺制系统的基准电压（单位为伏特）。

#### 依赖关系

要启用此参数，请将 **Input units** 设置为 `Per-Unit (PU)`。

### **Base current (A)** — 标称电流限值 `19.3`（默认）| 标量

标幺制系统的基准电流（单位为安培）。

#### 依赖关系

要启用此参数，请将 **Input units** 设置为 `Per-Unit (PU)`。

### **Base speed (rpm)** — 标称转速限值 `4107`（默认）| 标量

标幺制系统的基准转速（单位为 rpm）。

#### 依赖关系

要启用此参数，请将 **Input units** 设置为 `Per-Unit (PU)`。

### **Base torque (Nm)** — 标称转矩限值 `0.74112`（默认）

对应于 1 标幺值的转矩（单位为 Nm）。有关更多详细信息，请参阅 Per-Unit System 页面。

您无法配置此参数。模块使用其他参数在内部计算此值。

#### 依赖关系

要启用此参数，请将 **Input units** 设置为 `Per-Unit (PU)`。

### **Allow scaled-down motor parameters with CodeGen (higher precision with Fixed-Point data type)** — 缩小内部参数以匹配标幺比例 `on`（默认）| `off`

在生成代码时缩小内部参数以匹配标幺比例的选项。

- 启用此选项时，模块会缩小内部常量和系数以匹配标幺比例。这允许您在使用定点数据类型时获得更高的精度。如果将此选项与 single 或 double 数据类型一起使用，则根据分配给整数部分的位数，可能会发生一些精度损失。
- 禁用此选项时，模块会将其用于内部计算的所有常量和系数转换为 SI 单位，然后再转换回标幺比例。这允许您在生成的代码中更新查找表值，通常用于控制器调优或下线操作等应用。您也可以手动更新这些值，以便调试或重用之前生成的代码。

#### 依赖关系

要启用此参数，请将 **Motor parameter input method** 设置为 `非线性模型，采用 id 和 iq LUTs`，并将 **Input units** 设置为 `Per-Unit (PU)`。

### 绘图选项

仅当您满足以下条件时，该模块才会启用此选项卡：

- 将 **Motor parameter input method** 设置为
  `Linear model with lumped parameters`、
  `非线性模型，采用 D、Q 磁链 LUTs`、
  `Non-linear model with Ld and Lq LUTs` 或
  `非线性模型，采用 Ld、Lq 和 FluxPM
  LUTs`。
- 将 **Vdc input method** 设置为 `Specify via
  dialog`。

### **Enable saving the computed LUTs** — 启用模块保存计算得到的 LUT `off`（默认）| `on`

启用模块保存当您点击 **Compute (and plot) id and iq LUTs**
按钮时模块计算得到的查找表数据。

有关更多详细信息，请参阅 Plot Constraint Curves and Drive Characteristics for PMSM and SynRM Directly from Block Parameters Dialog Box。

### **Compute (and plot) id and iq LUTs** — 计算（并绘制）*id* 和 *iq* 查找数据按钮

当您点击此按钮时，模块会计算（并绘制）*id* 和 *iq* 电流的查找表数据。

有关更多详细信息，请参阅 Plot Constraint Curves and Drive Characteristics for PMSM and SynRM Directly from Block Parameters Dialog Box。

### **Use default options for plotting** — 使用默认选项绘制约束曲线 `on`（默认）| `off`

启用模块在您点击 **Plot constraint curves** 按钮绘制电机约束曲线时使用默认绘图选项。

有关更多详细信息，请参阅 Plot Constraint Curves and Drive Characteristics for PMSM and SynRM Directly from Block Parameters Dialog Box。

### **Motor speed (RPM)** — 用于绘制约束曲线的电机转速 `3000`（默认）| 标量

当您点击 **Plot constraint curves** 按钮绘制电机约束曲线时，模块应使用的电机转速（单位为 RPM）。

有关更多详细信息，请参阅 Plot Constraint Curves and Drive Characteristics for PMSM and SynRM Directly from Block Parameters Dialog Box。

#### 依赖关系

要启用此参数，请清除 **Use default options for
plotting** 参数。

### **Motor torque (Nm)** — 用于绘制约束曲线的电机转矩 `0.1`（默认）| 标量

当您点击 **Plot constraint curves** 按钮绘制电机约束曲线时，模块应使用的电机转矩（单位为 Nm）。

有关更多详细信息，请参阅 Plot Constraint Curves and Drive Characteristics for PMSM and SynRM Directly from Block Parameters Dialog Box。

#### 依赖关系

要启用此参数，请清除 **Use default options for
plotting** 参数。

### **Enable plotting the drive characteristics** — 启用模块绘制驱动特性 `off`（默认）| `on`

启用模块在您点击 **Plot constraint curves** 按钮绘制电机约束曲线时绘制驱动特性。

有关更多详细信息，请参阅 Plot Constraint Curves and Drive Characteristics for PMSM and SynRM Directly from Block Parameters Dialog Box。

#### 依赖关系

要启用此参数，请清除 **Use default options for
plotting** 参数。

### **Include the drive characteristics for an increased motor current** — 启用模块绘制增大电机电流时的驱动特性 `off`（默认）| `on`

启用模块在点击 **Plot constraint
curves** 按钮后生成的图中包含增大电机电流时的驱动特性。

**注意**

要成功绘制增大电机电流时的特性，该电流必须高于电机的额定电流。

有关更多详细信息，请参阅 Plot Constraint Curves and Drive Characteristics for PMSM and SynRM Directly from Block Parameters Dialog Box。

#### 依赖关系

要启用此参数，请清除 **Use default options for
plotting** 参数，并选中 **Enable plotting
the drive characteristics** 参数。

### **Plot constraint curves** — 绘制电机约束曲线按钮

当您点击此按钮时，模块会绘制电机的约束曲线。

有关更多详细信息，请参阅 Plot Constraint Curves and Drive Characteristics for PMSM and SynRM Directly from Block Parameters Dialog Box。

### **Compute and show** — 计算并显示特性转矩和转速按钮

当您点击此按钮时，模块将计算并显示以下转矩和转速特性：

- Rated torque — 电机额定转矩（单位：Nm）。
- Rated speed — 电机额定转速（单位：RPM）。
- Maximum speed — 电机最大转速（单位：RPM）。

有关更多详细信息，请参阅 Plot Constraint Curves and Drive Characteristics for PMSM and SynRM Directly from Block Parameters Dialog Box。

## 所属库

Motor Control Blockset / Controls / Control Reference

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

为 SynRM 和 PMaSynRM 的磁场定向控制生成基于查找表的控制参考电流

基于 LUT 的 SynRM 控制参考模块为同步磁阻电机（SynRM）和永磁辅助同步磁阻电机（PMaSynRM）的磁场定向控制和弱磁控制生成 *d* 轴和 *q* 轴参考电流。您可以指定参考转矩和反馈机械转速，模块输出对应的参考电流值。该模块还支持最大转矩每安培（MTPA）和最大转矩每电压（MTPV）运行区域。

该模块使用 *id(T,ω)* 和 *iq(T,ω)* 查找表（LUT）来生成参考电流值。根据您用于指定电机参数的输入方法，模块可以生成 LUT 或使用您提供的数据。

您可以使用以下方法之一指定电机参数。

**注意**

以下 SynRM 和 PMaSynRM 的方程遵循与永磁同步电机（PMSM）相同的 *d*-*q* 轴符号约定。

- `Linear model with lumped parameters` — 具有 *Ld* 和 *Lq* 的集中参数（适用于 SynRM），或具有 *Ld*、*Lq* 和 *FluxPM* 的集中参数（适用于 PMaSynRM）

  此方法使用集中参数来计算 *id* 和 *iq* LUT。模块通过求解与这些曲线相关的方程，为给定的 *ω* 和 *T* 输入获得 *id* 和 *iq*。

  最大转矩每安培（MTPA）曲线（适用于 SynRM）

  id+iq=0

  最大转矩每安培（MTPA）曲线（适用于 PMaSynRM）

  id2+idψm(Ld−Lq)=iq2.

  恒定转矩轨迹（适用于 SynRM）

  iq=T1.5Pp(Ld−Lq)id

  恒定转矩轨迹（适用于 PMaSynRM）

  iq=T1.5Pp(ψm+(Ld−Lq)id).

  电流限制曲线

  id2+iq2=imax2.

  电压限制曲线（适用于 SynRM）

  (VDC3)2=(idRs−ωeLqiq)2+(iqRs+ωeLdid)2.

  电压限制曲线（适用于 PMaSynRM）

  (VDC3)2=(idRs−ωeLqiq)2+(iqRs+ωeLdid+ωeψm)2.

  - 当电机在电压约束范围内运行时，模块求解 MTPA 线与恒定转矩轨迹的交点。
  - 当电机超出电压约束运行时，模块求解电压约束曲线与恒定转矩轨迹的交点。

  在根据 *ω* 和 *T* 值的网格计算出 *id* 和 *iq* 表之后，模块使用插值来为落在表值范围内的任何 *ω* 和 *T* 输入找到 *id ref* 和 *iq ref*。对于超出边界的 *ω* 和 *T* 值，表值将被裁剪。

- `Non-linear model with Ld and Lq LUTs` 或 `非线性模型，采用 Ld、Lq 和 FluxPM LUTs` — 具有 *d* 轴和 *q* 轴定子绕组电感以及永磁磁链查找表的非线性模型

  此方法使用与集中参数方法类似的方法，不同之处在于模块在每次计算 *id* 和 *iq* 时更新 *Ld(id,iq)*、*Lq(id,iq)* 和 *FluxPM(id,iq)* 的值。模块迭代这些计算，直到 *id* 和 *iq* 值收敛。

  **注意**

  *FluxPM(id,iq)* 值仅适用于 PMaSynRM。*Ld(id,iq)* 和 *Lq(id,iq)* 值适用于 SynRM 和 PMaSynRM。

- `非线性模型，采用 D、Q 磁链 LUTs` — 具有 *d* 轴和 *q* 轴磁链查找表的非线性模型。

  此方法使用与集中参数方法类似的方法，不同之处在于模块在每次计算 *id* 和 *iq* 时更新 *ψd(id,iq)* 和 *ψq(id,iq)* 的值。模块迭代这些计算，直到 *id* 和 *iq* 值收敛。

- `非线性模型，采用 id 和 iq LUTs` — 当您想要手动提供 *id(T,ω)* 和 *iq(T,ω)* 表时，使用此方法。通常，您通过仿真或测功机测试获得这些表。

您还可以使用 Motor Control Blockset™ 中的 `mcb.generateMotorLUT` 函数生成这些表。

有关 Motor Control Blockset 用于同步磁阻电机的详细方程组和假设，请参阅 Synchronous Reluctance Machine (Simscape Electrical)。

此外，您可以使用 **Vdc input method** 参数将模块配置为通过 **DC voltage to compute LUTs (V)** 参数接受固定参考直流电压，或通过单独的输入端口 **Vdc** 接受可变参考直流电压。

根据您在 **Motor parameter input method** 参数中选择的方法，您可以使用集中参数或非线性模型来计算参考电流，如下表所示。

| **Motor parameter input method** | **Vdc input method** | 用于计算参考电流的技术 |
| --- | --- | --- |
| `Linear model with lumped parameters` | `Specify via dialog` | 模块使用集中参数为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压计算 *id* 和 *iq* LUT，并使用这些 LUT 确定参考电流。 |
| `Input port - use 3D LUT (voltage slice based)` | 模块使用集中参数计算 3-D *id* 和 *iq* LUT，其中包含不同电压的数据（或 **DC bus voltage breakpoint vector, Vdc (V)** 参数中指定的电压切片）。它使用这些数据确定与输入端口 **Vdc** 处指定电压对应的参考电流。 |
| `输入端口 - 使用二维查找表（缩放-w based)` | 模块使用集中参数为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压计算 2-D *id* 和 *iq* LUT。它使用这些 LUT 通过对速度 (ω) 进行缩放来计算参考电流（对应于输入端口 **Vdc** 处提供的电压）。 |
| `非线性模型，采用 D、Q 磁链 LUTs` | `Specify via dialog` | 模块使用 *d* 轴和 *q* 轴磁链 LUT，为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压计算参考电流。 |
| `Input port - use 3D LUT (voltage slice based)` | 模块使用 3-D *d* 轴和 *q* 轴磁链 LUT，其中包含不同电压的数据（或 **DC bus voltage breakpoint vector, Vdc (V)** 参数中指定的电压切片）。它使用这些 LUT 计算与输入端口 **Vdc** 处提供的电压对应的参考电流。 |
| `输入端口 - 使用二维查找表（缩放-w based)` | 模块使用 2-D *d* 轴和 *q* 轴磁链 LUT，为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压进行计算。它使用这些 LUT 通过对速度 (ω) 进行缩放来计算参考电流（对应于输入端口 **Vdc** 处提供的电压）。 |
| `Non-linear model with Ld and Lq LUTs` | `Specify via dialog` | 模块使用给定的 *Ld* 和 *Lq* LUT，为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压计算参考电流。 |
| `Input port - use 3D LUT (voltage slice based)` | 模块使用给定的 3-D *Ld* 和 *Lq* LUT，其中包含不同电压的数据（或 **DC bus voltage breakpoint vector, Vdc (V)** 参数中指定的电压切片）。它使用这些 LUT 计算与输入端口 **Vdc** 处提供的电压对应的参考电流。 |
| `输入端口 - 使用二维查找表（缩放-w based)` | 模块使用给定的 2-D *Ld* 和 *Lq* LUT，为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压进行计算。它使用这些 LUT 通过对速度 (ω) 进行缩放来计算参考电流（对应于输入端口 **Vdc** 处提供的电压）。 |
| `非线性模型，采用 Ld、Lq 和 FluxPM LUTs` | `Specify via dialog` | 模块使用给定的 *Ld*、*Lq* 和永磁体磁链 LUT，为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压计算参考电流。 |
| `Input port - use 3D LUT (voltage slice based)` | 模块使用给定的 3-D *Ld*、*Lq* 和永磁体磁链 LUT，其中包含不同电压的数据（或 **DC bus voltage breakpoint vector, Vdc (V)** 参数中指定的电压切片）。它使用这些 LUT 计算与输入端口 **Vdc** 处提供的电压对应的参考电流。 |
| `输入端口 - 使用二维查找表（缩放-w based)` | 模块使用给定的 2-D *Ld*、*Lq* 和永磁体磁链 LUT，为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压进行计算。它使用这些 LUT 通过对速度 (ω) 进行缩放来计算参考电流（对应于输入端口 **Vdc** 处提供的电压）。 |
| `非线性模型，采用 id 和 iq LUTs` | `Specify via dialog` | 模块使用给定的 *id*、*iq* LUT，为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压确定参考电流。 |
| `Input port - use 3D LUT (voltage slice based)` | 模块使用给定的 3-D *id*、*iq* LUT，其中包含不同电压的数据（或 **DC bus voltage breakpoint vector, Vdc (V)** 参数中指定的电压切片）。它使用这些 LUT 确定与输入端口 **Vdc** 处提供的电压对应的参考电流。 |
| `输入端口 - 使用二维查找表（缩放-w based)` | 模块使用给定的 2-D *id*、*iq* LUT，为 **DC bus voltage, Vdc (V)** 参数中指定的固定电压进行计算。它使用这些 LUT 通过对速度 (ω) 进行缩放来计算参考电流（对应于输入端口 **Vdc** 处提供的电压）。 |
