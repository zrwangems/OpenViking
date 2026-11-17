---
type: simulink-block
title: 'Induction Machine Field-Oriented Control'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / Induction Machine Control'
documentation_page: 'inductionmachinefieldorientedcontrol'
documentation_source_path: 'ref/inductionmachinefieldorientedcontrol.html'
language: zh-CN
chinese_source: worker-translation
---

# Induction Machine Field-Oriented Control

## 端口

### 输入

### **imRef** — 电流标量

标幺制下的励磁参考电流。

**数据类型：** `single` | `double`

### **wrRef** — 速度标量

标幺制下的转子参考速度。

**数据类型：** `single` | `double`

### **iabc** — 电流向量

标幺制下测量的相电流。

**数据类型：** `single` | `double`

### **wr** — 速度标量

标幺制下测量的角速度。

**数据类型：** `single` | `double`

### **Vdc** — 电压标量

测量的直流母线电压，单位为 V。

**数据类型：** `single` | `double`
### 输出

### **G** — 门极脉冲向量 | `0` 或 `1`

逆变器门极脉冲。该模块不考虑任何死区时间。

**数据类型：** `single` | `double`

### **Visualization** — 可视化信号向量

包含用于可视化的信号的总线。

**数据类型：** `single` | `double` | `bus`

## 参数

### 通用

### **Rated voltage, rms line-to-line (V)** — 电压 `550`（默认值）

额定电压。

### **Rated electrical frequency (Hz)** — 频率 `60`（默认值）

额定电气频率。

### **Rotor resistance, referred to the stator side (pu)** — 电阻 `0.01`（默认值）

标幺制下折算到定子侧的转子电阻。

### **Rotor leakage inductance, referred to the stator side (pu)** — 电感 `0.06`（默认值）

标幺制下折算到定子侧的转子漏电感。

### **Magnetizing inductance (pu)** — 电感 `2.7`（默认值）

标幺制下的励磁电感。

### **Time constant for dq currents filters (s)** — 时间常数 `1e-4`（默认值）

用于滤波 *d* 轴和 *q* 轴电流的时间常数。

### **Inverter dc-link voltage threshold (V)** — 电压 `500`（默认值）

激活功率逆变器的电压阈值。

### **Fundamental sample time (s)** — 时间 `5e-6`（默认值） | 小于控制采样时间的正标量

基本采样时间必须小于控制采样时间。

### **Control sample time (s)** — 时间 `5e-5`（默认值） | 大于基本采样时间的正标量

控制采样时间必须大于基本采样时间。

### 外环

### **Magnetizing current controller proportional gain** — 增益 `10`（默认值）

励磁电流控制器的比例增益。

### **Magnetizing current controller integral gain** — 增益 `1000`（默认值）

励磁电流控制器的积分增益。

### **Magnetizing current controller integral anti-windup gain** — 增益 `1000`（默认值）

励磁电流控制器的积分抗饱和增益。

### **Speed controller proportional gain** — 增益 `10`（默认值）

速度控制器的比例增益。

### **Speed controller integral gain** — 增益 `1000`（默认值）

速度控制器的积分增益。

### **Speed controller integral anti-windup gain** — 增益 `1000`（默认值）

速度控制器的积分抗饱和增益。

### **Maximum d-axis current [pu]** — 电流 `2`（默认值）

*d* 轴的最大电流。

### **Maximum q-axis current [pu]** — 电流 `2`（默认值）

*q* 轴的最大电流。

#### 内环

### **Phase-a axis alignment** — *dq0* 参考坐标系对齐 `Q-axis`（默认值） | `D-axis`

将 *abc* 参考坐标系的 *a* 相向量对齐到旋转参考坐标系的 *d* 轴或 *q* 轴。

### **D-axis current proportional gain** — *D* 轴比例增益 `1`（默认值） | 正数

用于直轴电流控制的 PI 控制器的比例增益。

### **D-axis current integral gain** — *D* 轴积分增益 `100`（默认值） | 正数

用于直轴电流控制的 PI 控制器的积分增益。

### **D-axis current anti-windup gain** — *D* 轴抗饱和增益 `1`（默认值） | 正数

用于直轴电流控制的 PI 控制器的抗饱和增益。

### **Q-axis current proportional gain** — *Q* 轴比例增益 `1`（默认值） | 正数

用于交轴电流控制的 PI 控制器的比例增益。

### **Q-axis current integral gain** — *Q* 轴积分增益 `100`（默认值） | 正数

用于交轴电流控制的 PI 控制器的积分增益。

### **Q-axis current anti-windup gain** — *Q* 轴抗饱和增益 `1`（默认值） | 正数

用于交轴电流控制的 PI 控制器的抗饱和增益。

### **Axis prioritization** — 电压限制器的轴优先级 `Q-axis`（默认值） | `D-axis` | `D-Q equivalence`

当模块限制电压时，优先处理 *d* 轴和 *q* 轴或维持二者之间的比例。

#### PWM

### **PWM method** — 脉宽调制方法 `SVM: space vector modulation`（默认值） | `SPWM: sinusoidal PWM`

指定波形技术。

### **Sampling mode** — 波形采样方法 `Natural`（默认值） | `Asymmetric` | `Symmetric`

采样模式决定了模块在波形相交时或在载波处于一个或两个边界条件时对调制波形进行采样。

### **Switching frequency (Hz)** — 开关频率 `1000`（默认值） | 正整数

指定功率变换器中开关的切换速率。

## 所属库

Simscape / Electrical / Control / Induction Machine Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

标幺制离散时间感应电机 FOC

Induction Machine Field-Oriented Controller 模块使用标幺制实现感应电机磁场定向控制（FOC）结构。为了解耦转矩和磁通，FOC 使用转子 *d*-*q* 参考坐标系。下图显示了控制结构。

图中：

- *ωr* 是测量的角速度。
- *ωref* 是参考角速度。
- *id* 和 *iq* 分别是 *d* 轴和 *q* 轴定子电流。
- *ia*、*ib* 和 *ic* 分别是 *a* 相、*b* 相和 *c* 相定子绕组电流。
- *imr\_ref* 是参考励磁电流。
- *imr* 是励磁电流。
- *vd* 和 *vq* 分别是 *d* 轴和 *q* 轴定子电压。
- *va*、*vb* 和 *vc* 分别是 *a* 相、*b* 相和 *c* 相定子绕组电压。
- *θe* 是转子电角度。
- *GAH*、*GAL*、*GBH*、*GBL*、*GCH* 和 *GCL* 分别是 *a* 相、*b* 相和 *c* 相的高（H）和低（L）门极脉冲。

### 假设和限制

- 电机参数已知。
- 实现使用标幺制。
- 控制结构实现使用单一采样率。
