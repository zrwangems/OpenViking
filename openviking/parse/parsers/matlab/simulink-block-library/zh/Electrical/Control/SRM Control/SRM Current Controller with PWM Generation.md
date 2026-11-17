---
type: simulink-block
title: 'SRM Current Controller with PWM Generation'
family: 'control'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SRM Control'
documentation_page: 'srmcurrentcontrollerwithpwmgeneration'
documentation_source_path: 'ref/srmcurrentcontrollerwithpwmgeneration.html'
language: zh-CN
chinese_source: worker-translation
---

# SRM Current Controller with PWM Generation

## 端口

### 输入

### **IsRef** — 参考电流标量

用于控制的参考电流。

**数据类型：** `single` | `double`

### **Is** — 测得电流标量

实际电流。

**数据类型：** `single` | `double`

### **Reset** — 积分器复位标量

用于积分器的外部复位信号（上升沿）。

**数据类型：** `Boolean`

### **theta** — Theta 转子角度标量

转子角度，在区间 [0, *β* ] 内。

**数据类型：** `single` | `double`

### **thetaON** — 开通角标量

用于接通相供电的角度。

**数据类型：** `single` | `double`

### **thetaOFF** — 关断角标量

用于关断相供电的角度。

**数据类型：** `single` | `double`
### 输出

### **G** — 门极控制向量

决定开关行为的脉冲波形。

**数据类型：** `single` | `double`

## 参数

### 控制参数

### **比例增益** — 控制器的比例增益，*Kp* `1`（默认）| 正标量

控制器的比例增益，*Kp*。

### **积分增益** — 控制器的积分增益，*Ki* `5`（默认）| 正标量

控制器的积分增益，*Ki*。

### **抗积分饱和增益** — 控制器的抗积分饱和增益，*Kaw* `1`（默认）| 正标量

控制器的抗积分饱和增益，*Kaw*。

### **采样时间（-1 表示继承）** — 模块采样时间 `-1`（默认）| 正标量

连续模块执行之间的时间，以 s 为单位。执行期间，模块产生输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

如果此模块位于触发子系统内，请将此参数设置为 `-1` 以继承采样时间。如果此模块位于连续可变步长模型中，请使用正标量显式指定采样时间。

### PWM 发生器

### **载波计数器** — 载波计数器模型 `Up`（默认）| `Down` | `Up-Down`

使用载波计数器策略更改 PWM 输出的初始行为：

- Up 计数器 — PWM 输出从 on 状态开始时开始。
- Down 计数器 — PWM 输出从 off 状态开始时开始。
- Up-down 计数器 — PWM 输出从 on 状态中间开始。

### **定时器周期 (s)** — PWM 定时器周期 `0.001`（默认）| 正标量

脉冲宽度调制定时器周期，*Tper*，以秒为单位。

### **基本采样时间 (s)** — 用于 PWM 生成的采样时间 `0.0001`（默认）| 正标量

连续 PWM 发生器执行之间的时间，以 s 为单位。执行期间，模块产生 PWM 输出，并在适当时更新其内部状态。有关详细信息，请参阅 What Is Sample Time? 和 Specify Sample Time。

为确保生成的 PWM 信号具有足够分辨率，请设置基本采样时间，使 0<Ts\_pwm≤10Tper，其中：

- *Ts\_pwm* 是 **基本采样时间 (s)**。
- *Tper* 是 **定时器周期 (s)**。

## 所属库

Simscape / Electrical / Control / SRM Control

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

用于开关磁阻电机的具有内部脉冲宽度调制的电流控制器

SRM Current Controller with PWM Generation 模块为 Switched Reluctance Machine (SRM) 模块执行离散时间比例积分 (PI) 电流控制。该模块包含脉冲宽度调制 (PWM)。

### PWM 生成模型

该图显示了 SRM 的变换器结构。

如图所示，PWM 生成信号用于高侧开关器件。

当控制信号大于载波计数器值时，PWM 发生器输出 1。否则，输出 0。

### 方程

为确定占空比，该模块根据以下方程在转子参考坐标系中实现 PI 电流控制。

D=(Kp+KiTszz−1)(Is\_ref−Is)

其中：

- *D* 是占空比。
- *Kp* 是比例增益。
- *Ki* 是积分增益。
- *Ts* 是采样时间。
- *Is\_ref* 是参考电流。
- *Is* 是测得电流。

为获得三相控制信号，该模块随后将占空比与换相信号相乘。得到的三路控制信号在区间 [0, 1] 上归一化。
