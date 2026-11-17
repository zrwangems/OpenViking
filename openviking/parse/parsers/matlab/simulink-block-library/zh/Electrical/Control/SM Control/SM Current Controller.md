---
type: simulink-block
title: 'SM Current Controller'
family: 'control'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smcurrentcontroller'
documentation_source_path: 'ref/smcurrentcontroller.html'
language: zh-CN
chinese_source: worker-translation
---

# SM Current Controller

## 端口

### 输入

### **idqfRef** — 参考电流，A 向量

用于控制同步电机的参考 d-q 和励磁电流。

**数据类型：** `single` | `double`

### **idqf** — 测量电流，A 向量

受控同步电机的实际 d-q 和励磁轴电流。

**数据类型：** `single` | `double`

### **vdqFF** — 用途，V 向量

前馈预控制电压。

**数据类型：** `single` | `double`

### **VphMax** — 最大相电压，V 标量

每相允许的最大电压。

**数据类型：** `single` | `double`

### **VfMax** — 最大励磁电压，V 标量

允许的最大励磁电压。

**数据类型：** `single` | `double`

### **Reset** — 外部复位标量

用于积分器的外部复位信号（上升沿）。

**数据类型：** `single` | `double`
### 输出

### **vdqfRef** — 参考电压，V 向量

用于控制同步电机的参考 d-q 和励磁电压。

**数据类型：** `single` | `double`

## 参数

#### 常规

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| 正标量

连续模块执行之间的时间，以 s 为单位。执行期间，模块产生输出，并在适当情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

如果此模块位于触发子系统中，请将此参数设置为 `-1` 以继承采样时间。如果此模块位于连续变步长模型中，请使用正标量显式指定采样时间。

### **Discretization sample time** — 模块离散化采样时间 `0.001`（默认）| `-1` 或正数

当零消除处于活动状态且采样时间设置为 -1 时（例如，当模块在触发子系统内使用时），指定离散化采样时间。

### **Axis prioritization** — 电压限制器的轴优先级 `q-axis`（默认）| `d-axis` | `d-q equivalence`

当模块限制电压时，优先处理或保持 d 轴和 q 轴之间的比例。

### **Enable zero cancellation** — 前馈零消除 `off`（默认）| `on`

启用或禁用前馈路径上的零消除。

### **Enable pre-control voltage** — 预控制电压 `on`（默认）| `off`

启用或禁用预控制电压。

#### d-q Control

### **D-axis current proportional gain** — d 轴比例增益 `1`（默认）| 正数

用于直轴电流控制的 PI 控制器的比例增益。

### **D-axis current integral gain** — d 轴积分增益 `100`（默认）| 正数

用于直轴电流控制的 PI 控制器的积分增益。

### **D-axis current anti-windup gain** — d 轴抗饱和增益 `1`（默认）| 正数

用于直轴电流控制的 PI 控制器的抗饱和增益。

### **Q-axis current proportional gain** — q 轴比例增益 `1`（默认）| 正数

用于交轴电流控制的 PI 控制器的比例增益。

### **Q-axis current integral gain** — q 轴积分增益 `100`（默认）| 正数

用于交轴电流控制的 PI 控制器的积分增益。

### **Q-axis current anti-windup gain** — q 轴抗饱和增益 `1`（默认）| 正数

用于交轴电流控制的 PI 控制器的抗饱和增益。

#### Field Control

### **Field current proportional gain** — 励磁电流比例增益 `9`（默认）| 正数

用于励磁电流控制的 PI 控制器的比例增益。

### **Field current integral gain** — 励磁电流积分增益 `350`（默认）| 正数

用于励磁电流控制的 PI 控制器的积分增益。

### **Field current anti-windup gain** — 励磁电流抗饱和增益 `1`（默认）| 正数

用于励磁电流控制的 PI 控制器的抗饱和增益。

## 所属库

Simscape / Electrical / Control / SM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

离散时间同步电机电流 PI 控制器

SM Current Controller 模块在转子 *d*-*q* 参考坐标系中实现基于 PI 的离散时间同步电机 (SM) 电流控制器。

### 定义方程

该模块使用后向欧拉法进行离散化，因为它具有一阶简单性和稳定性。

在转子参考坐标系中实现的三个 PI 电流控制器产生参考电压向量：

vdref=(Kp\_id+Ki\_idTszz−1)(idref−id)+vd\_FF,

vqref=(Kp\_iq+Ki\_iqTszz−1)(iqref−iq)+vq\_FF,

以及

vfref=(Kp\_if+Ki\_ifTszz−1)(ifref−if),

其中：

- vdref、vqref 和 vfref 分别是 *d* 轴、*q* 轴和励磁参考电压。
- idref、vqref 和 ifref 分别是 *d* 轴、*q* 轴和励磁参考电流。
- id、iq 和 if 分别是 *d* 轴、*q* 轴和励磁电流。
- *Kp\_id*、*Kp\_iq* 和 *Kp\_if* 分别是 *d* 轴、*q* 轴和励磁控制器的比例增益。
- *Ki\_id*、*Ki\_iq* 和 *Ki\_if* 分别是 *d* 轴、*q* 轴和励磁控制器的积分增益。
- *vd\_FF* 和 *vq\_FF* 分别是 *d* 轴和 *q* 轴的前馈电压，由电机数学方程得到并作为输入提供。
- *Ts* 是离散控制器的采样时间。

使用 PI 控制会在闭环传递函数中产生一个零点，可以通过在前馈路径中引入零消除模块来抵消。离散时间下的零消除传递函数为：

GZC\_id(z)=TsKi\_idKp\_idz+(Ts−Kp\_idKi\_idKp\_idKi\_id),

GZC\_iq(z)=TsKi\_iqKp\_iqz+(Ts−Kp\_iqKi\_iqKp\_iqKi\_iq),

以及

GZC\_if(z)=TsKi\_ifKp\_ifz+(Ts−Kp\_ifKi\_ifKp\_ifKi\_if).

当定子电压向量超过电压相限 *Vph\_max* 时，必须施加饱和：

vd2+vq2≤Vph\_max,

其中 *vd* 和 *vq* 分别是 *d* 轴和 *q* 轴电压。

在轴优先级情况下，引入电压 *v1* 和 *v2*，其中：

- 对于 *d* 轴优先级，*v1 = vd* 且 *v2 = vq*。
- 对于 *q* 轴优先级，*v1 = vq* 且 *v2 = vd*。

约束（饱和）电压 v1sat 和 v2sat 如下获得：

v1sat=min(max(v1unsat,−Vph\_max),Vph\_max),

以及

v2sat=min(max(v2unsat,−V2\_max),V2\_max),

其中：

- v1unsat 和 v2unsat 是无约束（未饱和）电压。
- *v2\_max* 是不超过电压相限的 *v2* 最大值，由 v2\_max=(Vph\_max)2−(v1sat)2 给出。

在直轴和交轴具有相同优先级（d-q 等效）的情况下，约束电压如下获得：

vdsat=min(max(vdunsat,−Vd\_max),Vd\_max),

以及

vqsat=min(max(vqunsat,−Vq\_max),Vq\_max),

其中

Vd\_max=Vph\_max|vdunsat|(vdunsat)2+(vqunsat)2,

以及

Vq\_max=Vph\_max|vqunsat|(vdunsat)2+(vqunsat)2.

约束（饱和）励磁电压 vfsat 根据最大允许值进行限制：

vfsat=min(max(vfunsat,−Vf\_max),Vf\_max),

其中：

- vfunsat 是无约束（未饱和）励磁电压。
- *Vf\_max* 是最大允许励磁电压。

采用抗饱和机制以避免积分器输出饱和。在这种情况下，积分器增益变为：

Ki\_id+Kaw\_id(vdsat−vdunsat),

Ki\_iq+Kaw\_iq(vqsat−vqunsat),

以及

Ki\_if+Kaw\_if(vfsat−vfunsat),

其中 *Kaw\_id*、*Kaw\_iq* 和 *Kaw\_if* 分别是 *d* 轴、*q* 轴和励磁控制器的抗饱和增益。

### 假设

- 直轴和交轴的被控对象模型可以近似为一阶系统。
- 此控制解决方案仅用于具有正弦磁通分布和励磁绕组的同步电机。
