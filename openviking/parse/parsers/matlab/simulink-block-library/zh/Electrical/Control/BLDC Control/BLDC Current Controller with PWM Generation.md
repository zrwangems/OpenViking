---
type: simulink-block
title: 'BLDC Current Controller with PWM Generation'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / BLDC Control'
documentation_page: 'bldccurrentcontrollerwithpwmgeneration'
documentation_source_path: 'ref/bldccurrentcontrollerwithpwmgeneration.html'
language: zh-CN
chinese_source: worker-translation
---

# BLDC Current Controller with PWM Generation

## 端口

### 输入

### **IsRef** — 参考电流标量

用于控制的参考电流。

**数据类型：** `single` | `double`

### **Is** — 测量电流标量

实际电流。

**数据类型：** `single` | `double`

### **Reset** — 外部复位标量

积分器的外部复位信号（上升沿）。

**数据类型：** `single` | `double`

### **Hall** — 霍尔传感器向量

霍尔传感器数据。

**数据类型：** `single` | `double`

### **Direction** — 电机方向标量

电机旋转方向。

**数据类型：** `single` | `double`
### 输出

### **G** — 门极脉冲向量

确定所连接模块中开关行为的脉冲波形。

**数据类型：** `single` | `double`

## 参数

### 控制参数

### **Proportional gain** — 控制器比例增益，*Kp* `1`（默认）| 正标量

控制器的比例增益，*Kp*。

### **Integral gain** — 积分增益，*Ki* `5`（默认）| 正标量

控制器的积分增益，*Ki*。

### **Anti-windup gain** — 抗积分饱和增益，*Kaw* `1`（默认）| 正标量

控制器的抗积分饱和增益，*Kaw*。

### **Sample time (-1 for inherited)** — 模块采样时间 `-1`（默认）| 正标量

连续模块执行之间的时间，单位为 s。在执行期间，模块产生输出，并在适当的情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

如果此模块位于触发子系统内，请将此参数设置为 `-1` 以继承采样时间。如果此模块位于连续变步长模型中，请使用正标量显式指定采样时间。

#### 依赖关系

如果将 **Sample time (-1 for inherited)** 设置为 `-1` 并选择 **Enable zero cancellation** 选项，则 **Discretization sample time** 参数变为可见。

### **Discretization sample time** — 离散化采样时间 `0.001`（默认）| 正标量

连续离散化之间的时间，单位为 s。零点对消需要离散化。

#### 依赖关系

仅当同时满足以下两个条件时，此参数才可见：

- **Sample time** 设置为 `-1`。
- 已选择 **Enable zero cancellation**。

### **Enable zero cancellation** — 前馈零点对消 off（默认）| on

在前馈路径上使用零点对消的选项。

#### 依赖关系

如果选择 **Enable zero cancellation** 选项并将 **Sample time (-1 for inherited)** 设置为 `-1`，则 **Discretization sample time** 参数变为可见。

### PWM Generator

### **Carrier counter** — 载波计数器模型 `Up`（默认）| `Down` | `Up-Down`

使用载波计数器策略来更改 PWM 输出的初始行为：

- Up 计数器 — PWM 输出在导通状态开始时启动。
- Down 计数器 — PWM 输出在关断状态开始时启动。
- Up-down 计数器 — PWM 输出在导通状态中间启动。

### **Timer period (s)** — PWM 定时器周期 `0.001`（默认）| 正标量

脉宽调制定时器周期，*Tper*，单位为秒。

### **Fundamental sample time (s)** — PWM 生成采样时间 `0.0001`（默认）| 正标量

连续 PWM 生成器执行之间的时间，单位为 s。在执行期间，模块产生 PWM 输出，并在适当的情况下更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

为确保生成的 PWM 信号具有足够的分辨率，请设置基波采样时间，使得 0<Ts\_pwm≤10Tper，其中：

- *Ts\_pwm* 是 **Fundamental sample time (s)**。
- *Tper* 是 **Timer period (s)**。

## 所属库

Simscape / Electrical / Control / BLDC Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

带脉宽调制生成的离散时间无刷直流电机电流 PI 控制器

BLDC Current Controller with PWM Generation 模块生成脉宽调制（PWM）信号并控制无刷直流电机中的电流。控制器使用此算法。

### 方程

BLDC Current Controller with PWM Generation 通过使用以下方程实现比例积分（PI）电流控制，为 BLDC 模块产生占空比

D=(Kp+KiTszz−1)(Is\_ref−Is)

其中：

- *D* 是占空比。
- *Kp* 是比例增益。
- *Ki* 是积分增益。
- *Ts* 是时间周期。
- *Is\_ref* 是参考电流。
- *Is* 是测量电流。
- *Gzc* 是零点对消多项式。

PI 控制算法的闭环传递函数产生一个零点，可以通过在前馈路径中使用零点对消模块来对消。离散时间下的零点对消传递函数为：

GZC(z)=TsKiKpz+(Ts−KpKiKpKi)。

该模块通过将占空比乘以换向信号来获得三相的控制信号。所得的三路控制信号在区间 [-1, 1] 上归一化。

当控制信号的值大于载波计数器值时，PWM 生成器输出 1。否则，PWM 生成器输出 0。
