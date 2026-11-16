---
type: simulink-block
title: 'Induction Machine Current Controller'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Control / Induction Machine Control'
documentation_page: 'inductionmachinecurrentcontroller'
documentation_source_path: 'ref/inductionmachinecurrentcontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# Induction Machine Current Controller

## 端口

### 输入

### **idqRef** — 参考电流矢量

用于控制感应电机的期望 *d*- 和 *q* 轴电流，单位为 A。

**数据类型：** `single` | `double`

### **idq** — 测量电流矢量

受控感应电机的实际 *d*- 和 *q* 轴电流，单位为 A。

**数据类型：** `single` | `double`

### **vdqFF** — 前馈电压矢量

前馈预控制电压，单位为 V。

**数据类型：** `single` | `double`

### **VphMax** — 最大相电压标量

每相允许的最大电压，单位为 V。

**数据类型：** `single` | `double`

### **Reset** — 外部复位标量

用于积分器的外部复位信号（上升沿）。

**数据类型：** `Boolean`

### 输出

### **vdqRef** — 参考电压矢量

用于控制感应电机的期望 *d*- 和 *q* 轴电压，单位为 V。

**数据类型：** `single` | `double`

## 参数

#### 控制参数

### **D 轴电流比例增益** — *d* 轴比例增益 `1`（默认）

直轴电流控制的比例增益。

### **D 轴电流积分增益** — *d* 轴积分增益 `100`（默认）

直轴电流控制的积分增益。

### **D 轴电流抗饱和增益** — *d* 轴抗饱和增益 `1`（默认）

直轴电流控制的抗饱和增益。

### **Q 轴电流比例增益** — *q* 轴比例增益 `1`（默认）

交轴电流控制的比例增益。

### **Q 轴电流积分增益** — *q* 轴积分增益 `100`（默认）

交轴电流控制的积分增益。

### **Q 轴电流抗饱和增益** — *q* 轴抗饱和增益 `1`（默认）

交轴电流控制的抗饱和增益。

### **采样时间（-1 表示继承）** — 模块采样时间 `-1`（默认）| 正标量

连续模块执行之间的时间，单位为 s。执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅“什么是采样时间？”和“指定采样时间”。

如果此模块位于触发子系统中，请将此参数设置为 `-1` 以继承采样时间。如果此模块位于连续变步长模型中，请使用正标量显式指定采样时间。

### **轴优先级** — 电压限制器的轴优先级 `Q-axis`（默认）| `D-axis` | `D-Q equivalence`

当模块限制电压时，优先处理或保持 *d* 轴和 *q* 轴之间的比率。

### **启用预控制电压** — 预控制电压 `on`（默认）| `off`

启用或禁用预控制电压。

## 所属库

Simscape / Electrical / Control / Induction Machine Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2017b 中引入**

## 描述

离散时间感应电机电流 PI 控制器

Induction Machine Current Controller 在转子 *d*-*q* 参考坐标系中实现基于离散时间比例积分（PI）的感应电机电流控制。通常，您会在构成控制结构的一系列模块中使用 Induction Machine Current Controller。例如，为了将 *dq0* 参考坐标系输出电压转换为 *abc* 参考坐标系中的电压，请在控制结构中将 Induction Machine Current Controller 连接到 Inverse Clarke Transform。

### 方程

该模块使用后向欧拉离散化方法。

在转子参考坐标系中实现的两个 PI 电流控制器产生参考电压矢量：

vdref=(Kp\_id+Ki\_idTszz−1)(idref−id)+vd\_FF,

和

vqref=(Kp\_iq+Ki\_iqTszz−1)(iqref−iq)+vq\_FF,

其中

- vdref 和 vqref 分别是 *d* 轴和 *q* 轴参考电压。
- idref 和 iqref 分别是 *d* 轴和 *q* 轴参考电流。
- id 和 iq 分别是 *d* 轴和 *q* 轴电流。
- *Kp\_id* 和 *Kp\_iq* 分别是 *d* 轴和 *q* 轴控制器的比例增益。
- *Ki\_id* 和 *Ki\_iq* 分别是 *d* 轴和 *q* 轴控制器的积分增益。
- *vd\_FF* 和 *vq\_FF* 分别是 *d* 轴和 *q* 轴的前馈电压。前馈电压从电机数学方程获得，并作为输入提供。
- *Ts* 是离散控制器的采样时间。

### 电压饱和

当定子电压矢量超过相电压限值 *Vph\_max* 时，施加饱和：

vd2+vq2≤Vph\_max,

其中 *vd* 和 *vq* 分别是 *d* 轴和 *q* 轴电压。

在轴优先级的情况下，引入电压 *v1* 和 *v2*，其中：

- 对于 *d* 轴优先级 — *v1 = vd* 和 *v2 = vq*。
- 对于 *q* 轴优先级 — *v1 = vq* 和 *v2 = vd*。

受约束（饱和）电压 v1sat 和 v2sat 通过以下方式获得：

v1sat=min(max(v1unsat,−Vph\_max),Vph\_max)

和

v2sat=min(max(v2unsat,−V2\_max),V2\_max),

其中：

- v1unsat 和 v2unsat 是未约束（未饱和）电压。
- *v2\_max* 是不超过相电压限值的 *v2* 最大值。定义 *v2\_max* 的方程为 v2\_max=(Vph\_max)2−(v1sat)2。

在 *d*-*q* 等价的情况下，直轴和交轴具有相同优先级，并且受约束电压为：

vdsat=min(max(vdunsat,−Vd\_max),Vd\_max)

和

vqsat=min(max(vqunsat,−Vq\_max),Vq\_max),

其中：

Vd\_max=Vph\_max|vdunsat|(vdunsat)2+(vqunsat)2

和

Vq\_max=Vph\_max|vqunsat|(vqunsat)2+(vqunsat)2.

### 积分抗饱和

采用抗饱和机制以避免积分器输出饱和。在这种情况下，积分器增益变为：

Ki\_id+Kaw\_id(vdsat−vdunsat)

和

Ki\_iq+Kaw\_iq(vqsat−vqunsat),

其中 *Kaw\_id*、*Kaw\_iq* 和 *Kaw\_if* 分别是 *d* 轴、*q* 轴和磁场控制器的抗饱和增益。

### 假设和限制

- 直轴和交轴的被控对象模型可以用一阶系统近似。
