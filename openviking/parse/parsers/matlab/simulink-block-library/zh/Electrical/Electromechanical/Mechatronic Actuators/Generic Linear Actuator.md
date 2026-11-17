---
type: simulink-block
title: 'Generic Linear Actuator'
family: 'electromechanical'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Mechatronic Actuators'
documentation_page: 'genericlinearactuator'
documentation_source_path: 'ref/genericlinearactuator.html'
language: zh-CN
chinese_source: worker-translation
---

# Generic Linear Actuator

## 端口

### 守恒

### **+** — 正端子电气

与执行器正端子关联的电气守恒端口。

### **-** — 负端子电气

与执行器负端子关联的电气守恒端口。

### **C** — 外壳机械

与执行器外壳关联的机械平移守恒端口。

### **R** — 柱塞机械

与柱塞关联的机械平移守恒端口。

### **H** — 热端口 热

热端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port` (默认) | `Show thermal port`

是否启用模块的热端口，并对将功率转换为热量的损耗效应进行建模。

### 电气力

### **Speed values** — 速度值 `[-15, -10, -5, 0, 5, 10, 15, 20, 25, 30]` `m/s` (默认)

指定一个速度向量（包含其单位），用于力-速度数据。

### **Force values** — 力值 `[4, 3.5, 3, 2.5, 2, 1.5, 1, .5, 0, -.5]` `N` (默认)

指定一个力向量（包含其单位），用于力-速度数据。

### **Rated voltage** — 额定电压 `12` `V` (默认)

指示您所建模设备的额定电压。

### **Motor efficiency (percent)** — 电机效率 `70` (默认)

模块用于计算与力相关的电气损耗的效率。

### **Speed at which efficiency is measured** — 测量效率时的速度 `20` `m/s` (默认)

模块用于计算与力相关的电气损耗的速度。

### **Force-independent electrical losses** — 与力无关的电气损耗 `2` `W` (默认)

当力为零时，与执行器关联的固定电气损耗。

### **Simulation mode** — 仿真模式 `PWM` (默认) | `Averaged`

如果将 **Simulation mode** 参数设置为 `PWM`，则向模块的电气端子施加在零伏与额定电压之间切换的 PWM 波形。从电源汲取的电流等于传递机械功率并补偿电气损耗所需的量。如果施加的电压超过额定电压，则产生的力按比例缩放。然而，施加除额定电压以外的任何电压都可能提供不具有代表性的结果。

如果将 **Simulation mode** 参数设置为 `Averaged`，则响应于施加电压 Vav 生成的力为

VavVrated×F(v)

其中F(v) 是在速度 v 下的力值。从电源汲取的电流使得电流与 Vav 的乘积等于所消耗的平均功率。

### 机械

### **Plunger mass** — 柱塞质量 `0.1` `kg` (默认)

电机运动部件的质量。该值可以为零。

### **Linear damping** — 线性阻尼 `1e-5` `N/(m/s)` (默认)

线性阻尼。该值可以为零。

### 温度依赖性

要启用这些参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Resistance temperature coefficient** — 电阻温度系数 `3.93e-3` `1/K` (默认)

电阻温度系数。

### **Measurement temperature** — 测量温度 `25` `degC` (默认)

定义执行器参数所对应的温度。

### 热端口

要启用此参数，请将 **Modeling option** 设置为 `Show thermal port`。

### **Thermal mass** — 热质量 `100` `J/K` (默认)

热质量是将温度升高一度所需的能量。

## 所属库

Simscape / Electrical / Electromechanical / Mechatronic Actuators

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009b 中引入**

## 描述

由直流电压源或 PWM 驱动器驱动的通用线性执行器

Generic Linear Actuator 模块实现了一个通用线性执行器的模型，该执行器设计为由直流电压源或 PWM 驱动器驱动。通过表格值定义力-速度特性，以在额定电压下驱动电机。此功能使您无需参考等效电路即可对电机建模。

电机或执行器架构决定了电气损耗依赖于力的方式。例如，直流电机的损耗与电流的平方成正比。由于力与电流成正比，损耗也与机械力成正比。大多数电机都有一个与机械力平方成正比的电气损耗项。Generic Linear Actuator 模块使用您提供的 **Motor efficiency (percent)** 和 **Speed at which efficiency is measured** 参数来计算此损耗项。

某些电机还具有与力无关的损耗项。一个例子是并励电机，其中励磁绕组无论负载如何都汲取恒定电流。**Force-independent electrical losses** 参数用于考虑此效应。

电机效率是机械功率除以机械功率与两个电气损耗项之和。该模块假定定义电机效率时的速度处于电动象限，因此为正。

您可以通过改变所施加电压的符号来使模块反向运行。例如，如果 REV 端口处的电压大于 **Reverse threshold voltage** 参数，则 H-Bridge 模块会反转电机方向。但是，如果您要反向使用该模块，请按正向运行指定力-速度数据：

- 在电动象限中的正力与正速度。
- 在逆时针发电象限中的正力与负速度。
- 在顺时针发电象限中的负力与正速度。

### 对热效应建模

您可以公开热端口，以对将功率转换为热量的损耗效应进行建模。要公开热端口，请将 **Modeling option** 参数设置为以下任一项：

- `No thermal port` — 该模块不包含热端口。
- `Show thermal port` — 该模块包含一个热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。
