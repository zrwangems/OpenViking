---
type: simulink-block
title: 'Sliding Mode Observer'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Sensorless Estimators'
documentation_page: 'slidingmodeobserver'
documentation_source_path: 'ref/slidingmodeobserver.html'
language: zh-CN
chinese_source: worker-translation
---

# Sliding Mode Observer

## 端口

### 输入

### **Vα** — *α* 轴电压标量

静止 *αβ* 参考坐标系中沿 *α* 轴的电压分量。

**数据类型：** `single` | `double` | `fixed point`

### **Vβ** — *β* 轴电压标量

静止 *αβ* 参考坐标系中沿 *β* 轴的电压分量。

**数据类型：** `single` | `double` | `fixed point`

### **Iα** — *α* 轴电流标量

静止 *αβ* 参考坐标系中沿 *α* 轴的电流分量。

**数据类型：** `single` | `double` | `fixed point`

### **Iβ** — *β* 轴电流标量

静止 *αβ* 参考坐标系中沿 *β* 轴的电流分量。

**数据类型：** `single` | `double` | `fixed point`

### **Rst** — 复位模块标量

用于复位并重新启动模块算法处理的脉冲（真值）。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **θe** — PMSM 电位置标量

转子的估计电位置。

**数据类型：** `single` | `double` | `fixed point`

### **⍵m** — PMSM 机械速度标量

转子的估计机械速度。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### **Input units** — 模块输入的单位 `SI unit`（默认）| `Per-unit`

静止 *αβ* 参考坐标系中沿 *α* 轴和 *β* 轴的输入电压和电流分量的单位。

### **Discrete step size (s)** — 模块再次执行前的采样时间 `50e-6`（默认）| 标量

每两次连续模块执行之间的固定时间间隔（以秒为单位）。

### 电机参数

### **Stator resistance (ohm)** — 电阻 `0.36`（默认）| 标量

定子相绕组电阻（以欧姆为单位）。

### **Stator inductance (H)** — 电感 `0.2e-3`（默认）| 标量

定子相绕组电感（以亨利为单位）。

### **Maximum application speed (RPM)** — 支持的最大机械速度 `6000`（默认）| 标量

模块可支持的最大机械速度（以 RPM 为单位）。超过此值时，模块将生成错误的输出。

**注意**

模块使用此参数滤除估计速度信号中的噪声。

### **Number of pole pairs** — 电机中可用的极对数 `4`（默认）| 标量

电机中可用的极对数。

### **Base voltage (V)** — 对应一个标幺值的标称电压 `13.8564`（默认）| 标量

施加到 PMSM 的最大相电压。有关详细信息，请参阅 Per-Unit System。

### **Base current (A)** — 对应一个标幺值的标称电流 `21.4286`（默认）| 标量

提供给 PMSM 的最大可测量电流。有关详细信息，请参阅 Per-Unit System。

**注意**

Sliding Mode Observer 模块偶尔可能会显示警告消息 `Wrap on overflow detected`。

### 观测器参数

### **Back-emf observer gain** — 反电动势的滑模观测器增益 `0.9`（默认）| 标量

确保反电动势观测器收敛的增益。

### **Current observer gain** — 电流的滑模观测器增益 `0.50881`（默认）| 标量

确保电流观测器收敛的增益。

### **Filter cut-off frequency (Hz)** — 内部滤波器的截止频率 `1200`（默认）| 标量

内部低通 IIR 滤波器的截止频率。截止频率值必须大于或等于最大电频率。

点击 **Compute default parameters** 以计算近似观测器增益和滤波器系数并更新这些字段。对于此计算，我们将 *g* 设置为 `0.9`，在额定速度的两倍处计算 *m*，并将 *η* 设置为 1.1(bmg)。

### 数据类型

### **Position unit** — 位置输出的单位 `Radians`（默认）| `Degrees` | `Per unit`

位置输出的单位。

### **Position data type** — 位置输出的数据类型 `single`（默认）| `double` | `fixed point`

位置输出的数据类型。

### **Speed unit** — 速度输出的单位 `RPM`（默认）| `Degrees/sec` | `Radians/sec` | `Per unit`

速度输出的单位。

### **Speed data type** — 速度输出的数据类型 `single`（默认）| `double` | `fixed point`

速度输出的数据类型。

## 所属库

Motor Control Blockset / Sensorless Estimators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2021b 中引入**

## 描述

计算表贴式 PMSM 的电角度位置和机械转速

Sliding Mode Observer 模块通过使用静止 *αβ* 参考坐标系中沿 *α* 轴和 *β* 轴的电压和电流值，计算表贴式 PMSM 的电角度位置和机械转速。

### 方程

这些方程描述了 PMSM 的离散时间运行：

iαβ(k+1)=Aiαβ(k)+Bvαβ(k)−Beαβ(k)

eαβ(k+1)=eαβ(k)+Tsωe(k)Jeαβ(k)

J=[0−110]

Φ=[−RL00−RL]

A=eΦTs

B=∫0TseΦτdτ=[b00b]

b=1−e−RTs/LR

这些方程描述了表贴式 PMSM 的离散时间滑模观测器运行：

i^αβ(k+1)=Ai^αβ(k)+Bvαβ(k)−Be^αβ(k)−ηSign(i˜αβ(k))

e^αβ(k+1)=e^αβ(k)+B−1g(i˜αβ(k)−Ai˜αβ(k−1)+ηSign(i˜αβ(k−1)))

i˜αβ(k)=i^αβ(k)−iαβ(k)

e˜αβ(k)=e^αβ(k)−eαβ(k)

如果反电动势观测器满足条件 |eαβ(k+1)−eαβ(k)|≤m 和 g∈(0,1)，则存在一个 *k0*，使得：

e˜αβ(k)<mg

如果滑模观测器满足以下条件：

- g∈(0,1)
- |eαβ(k+1)−eαβ(k)|≤m
- η>bmg

则存在一个 *k=k0*，使得对于 *k≥k0*：

|i˜αβ(k)|≤η+bmg

其中：

- *eα* 和 *iα* 是 *α* 轴的定子反电动势和电流。
- *eβ* 和 *iβ* 是 *β* 轴的定子反电动势和电流。
- *ẽα* 和 *ĩα* 是 *α* 轴的定子反电动势和电流误差。
- *ẽβ* 和 *ĩβ* 是 *β* 轴的定子反电动势和电流误差。
- *vα* 和 *vβ* 是定子供电电压。
- *R* 是定子电阻。
- *L* 是定子电感。
- *g* 是反电动势观测器增益。
- *η* 是电流观测器增益。
- *ωe* 是电角速度。
- *Ts* 是采样周期。
- *k* 是采样计数。

### 调节滑模观测器

使用以下步骤，通过 **Current observer gain**（*η*）和 **Back-emf observer gain**（*g*）参数来调节该模块。

- 选择反电动势观测器增益（*g*）值，使得 g∈(0,1)。将 *g* 接近值 `1` 会导致估计反电动势的误差更小。但是，这会使收敛变慢。
- 根据模块采样时间和工作反电动势的最大斜率选择 *m* 的值（使得 |eαβ(k+1)−eαβ(k)|≤m）。
- 根据 *b*、*m* 和 *g* 选择电流观测器增益（*η*）值（使得 η>bmg）。

**注意**

当您调节滑模观测器增益时，模块才能正常工作。

当使用开环控制运行电机时，使用滑模观测器和实际传感器硬件同时计算转子位置，并比较计算得到的位置值。如果差值可接受，则模块工作正常。否则，手动调节滑模观测器增益以确保模块准确工作。

由于电流和电压中的噪声，从开环控制到闭环控制的过渡可能会失败。为了成功过渡，请尝试减小 **Filter cut-off frequency (Hz)** 参数的值。
