---
type: simulink-block
title: 'PMSM Current Controller with Pre-Control'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / PMSM Control'
documentation_page: 'pmsmcurrentcontrollerwithprecontrol'
documentation_source_path: 'ref/pmsmcurrentcontrollerwithprecontrol.html'
language: zh-CN
chinese_source: worker-translation
---

# PMSM Current Controller with Pre-Control

## 端口

### 输入

### **idqRef** — 参考电流向量

用于控制 PMSM 的期望 *d* 轴和 *q* 轴电流，单位为 A。

**数据类型：** `single` | `double`

### **idq** — 测得电流向量

受控 PMSM 的实际 *d* 轴和 *q* 轴电流，单位为 A。

**数据类型：** `single` | `double`

### **wElectrical** — 测得的电角速度向量

用于前馈预控制的转子电角速度，单位为 rad/s。

**数据类型：** `single` | `double`

### **VphMax** — 最大相电压标量

每相最大允许电压，单位为 V。

**数据类型：** `single` | `double`

### **Reset** — 外部复位标量

用于积分器的外部复位信号（上升沿）。

**数据类型：** `single` | `double`
### 输出

### **vdqRef** — 参考电压向量

用于控制 PMSM 的期望 *d* 轴和 *q* 轴电压，单位为 V。

**数据类型：** `single` | `double`

## 参数

#### 控制参数

### **D 轴电流比例增益** — D 轴比例增益 `1`（默认）| 正数

用于 D 轴电流控制的 PI 控制器的比例增益。

### **D 轴电流积分增益** — D 轴积分增益 `100`（默认）| 正数

用于 D 轴电流控制的 PI 控制器的积分增益。

### **D 轴电流抗饱和增益** — D 轴抗饱和增益 `1`（默认）| 正数

用于 D 轴电流控制的 PI 控制器的抗饱和增益。

### **Q 轴电流比例增益** — Q 轴比例增益 `1`（默认）| 正数

用于 Q 轴电流控制的 PI 控制器的比例增益。

### **Q 轴电流积分增益** — Q 轴积分增益 `100`（默认）| 正数

用于 Q 轴电流控制的 PI 控制器的积分增益。

### **Q 轴电流抗饱和增益** — Q 轴抗饱和增益 `1`（默认）| 正数

用于 Q 轴电流控制的 PI 控制器的抗饱和增益。

### **采样时间（-1 表示继承）** — 模块采样时间 `-1`（默认）| `-1` 或正数

模块的采样时间（-1 表示继承）。如果在触发子系统内使用此模块，请将采样时间设置为 -1。如果在连续可变步长模型中使用此模块，可以显式指定采样时间。

### **轴优先级** — 电压限制器的轴优先级 `q-axis`（默认）| `d-axis` | `d-q equivalence`

当模块限制电压时，优先考虑或保持 *d* 轴和 *q* 轴之间的比例。

### **启用零点对消** — 前馈零点对消 `off`（默认）| `on`

启用或禁用前馈路径上的零点对消。

### **启用预控制电压** — 预控制电压 `on`（默认）| `off`

启用或禁用预控制电压。

#### 预控制参数

### **D 轴电流向量，id (A)** — D 轴电流断点向量 `[-200,0,200]``A`（默认）| 单调递增向量

用于参数确定的查找表中的直轴电流向量。对于恒定电机参数，请勿更改默认值。

### **Q 轴电流向量，iq (A)** — Q 轴电流断点向量 `[-200,0,200]``A`（默认）| 单调递增向量

用于确定参数的查找表中的交轴电流向量。对于恒定电机参数，请勿更改默认值。

### **Ld 矩阵，Ld(id,iq) (H)** — D 轴电感查找数据 `0.0002 * ones(3, 3)``H`（默认）| 正矩阵

*Ld* 矩阵用作查找表数据。对于恒定电机参数，仅更改常数因子，例如 *Ld* \* `ones(3, 3)`。

### **Lq 矩阵，Lq(id,iq) (H)** — Q 轴电感查找数据 `0.0002 * ones(3, 3)``H`（默认）| 正矩阵

*Lq* 矩阵用作查找表数据。对于恒定电机参数，仅更改常数因子，例如 *Lq* \* `ones(3, 3)`。

### **永磁体磁链矩阵，PM(id,iq) (Wb)** — 磁链查找数据 `0.04 * ones(3, 3)``Wb`（默认）| 实数矩阵

查找表中使用的永磁体磁链矩阵。对于恒定电机参数，仅更改常数因子，例如 *psim* \* `ones(3, 3)`。

## 所属库

Simscape / Electrical / Control / PMSM Control

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

带预控制的离散时间永磁同步电机电流控制器

PMSM Current Controller with Pre-Control 模块在转子 *d*-*q* 参考坐标系中实现带内部前馈预控制的离散时间基于 PI 的永磁同步电机 (PMSM) 电流控制器。

通常将该模块用于构成控制结构的一系列模块中。

- 可以使用 PMSM Current Reference Generator 在 d-q 坐标系中生成电流参考，作为该模块的输入。
- 可以使用 Inverse Park Transform 模块转换该模块的输出，从而在 abc 域中获得电压参考。

可以在 PMSM Field-Oriented Control 模块中查看完整控制结构（从电机测量到电机输入）的示例。

### 方程

该模块采用后向欧拉法离散化，因为其具有一阶简单性和稳定性。

在转子参考坐标系中实现的两个 PI 电流控制器产生参考电压向量：

vdref=(Kp\_id+Ki\_idTszz−1)(idref−id)+vd\_FF,

and

vqref=(Kp\_iq+Ki\_iqTszz−1)(iqref−iq)+vq\_FF,

其中：

- vdref 和 vqref 分别是 *d* 轴和 *q* 轴参考电压。
- idref 和 iqref 分别是 *d* 轴和 *q* 轴参考电流。
- id 和 iq 分别是 *d* 轴和 *q* 轴电流。
- *Kp\_id* 和 *Kp\_iq* 分别是 *d* 轴和 *q* 轴控制器的比例增益。
- *Ki\_id* 和 *Ki\_iq* 分别是 *d* 轴和 *q* 轴控制器的积分增益。
- *Ts* 是离散控制器的采样时间。
- *vd\_FF* 和 *vq\_FF* 分别是 *d* 轴和 *q* 轴的前馈电压。

前馈电压由电机数学方程获得：

vd\_FF=−ωeLqiqref,

and

vq\_FF=ωe(Ldidref+ψm),

其中：

- *ωe* 是转子电角速度。
- *Ld* 和 *Lq* 分别是 *d* 轴和 *q* 轴电感。
- *ψm* 是永磁体磁链。

### 零点对消

使用 PI 控制会在闭环传递函数中产生一个零点，这可能导致闭环响应中出现不期望的超调。可以通过在前馈路径中引入零点对消模块来对消该零点。离散时间下的零点对消传递函数为：

GZC\_id(z)=TsKi\_idKp\_idz+(Ts−Kp\_idKi\_idKp\_idKi\_id),

and

GZC\_iq(z)=TsKi\_iqKp\_iqz+(Ts−Kp\_iqKi\_iqKp\_iqKi\_iq).

### 电压饱和

当定子电压向量超过相电压限值 *Vph\_max* 时，必须施加饱和：

vd2+vq2≤Vph\_max,

其中 *vd* 和 *vq* 分别是 *d* 轴和 *q* 轴电压。

在轴优先级情况下，引入电压 *v1* 和 *v2*，其中：

- 对于 *d* 轴优先级，*v1 = vd* 且 *v2 = vq*。
- 对于 *q* 轴优先级，*v1 = vq* 且 *v2 = vd*。

受限（饱和）电压 v1sat 和 v2sat 按下式获得：

v1sat=min(max(v1unsat,−Vph\_max),Vph\_max)

and

v2sat=min(max(v2unsat,−V2\_max),V2\_max),

其中：

- v1unsat 和 v2unsat 是无约束（未饱和）电压。
- *v2\_max* 是不超过相电压限值的 *v2* 最大值，由 v2\_max=(Vph\_max)2−(v1sat)2 给出。

当 d 轴和 q 轴具有相同优先级（d-q equivalence）时，受限电压按下式获得：

vdsat=min(max(vdunsat,−Vd\_max),Vd\_max)

and

vqsat=min(max(vqunsat,−Vq\_max),Vq\_max),

其中：

Vd\_max=Vph\_max|vdunsat|(vdunsat)2+(vqunsat)2

and

Vq\_max=Vph\_max|vqunsat|(vqunsat)2+(vqunsat)2.

### 积分抗饱和

采用抗饱和机制避免积分器输出饱和。在这种情况下，积分增益变为：

Ki\_id+Kaw\_id(vdsat−vdunsat)

and

Ki\_iq+Kaw\_iq(vqsat−vqunsat),

其中 *Kaw\_id*、*Kaw\_iq* 和 *Kaw\_if* 分别是 *d* 轴、*q* 轴和磁场控制器的抗饱和增益。

### 假设

- 直轴和交轴的被控对象模型可以近似为一阶系统。
- 该控制方案仅用于具有正弦磁通分布和励磁绕组的永磁同步电机。
