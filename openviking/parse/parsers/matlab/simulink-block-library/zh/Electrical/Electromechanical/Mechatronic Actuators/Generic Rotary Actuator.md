---
type: simulink-block
title: 'Generic Rotary Actuator'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electromechanical / Mechatronic Actuators'
documentation_page: 'genericrotaryactuator'
documentation_source_path: 'ref/genericrotaryactuator.html'
language: zh-CN
chinese_source: worker-translation
---

# Generic Rotary Actuator

## 端口
```yaml
ports:
- name: +
  summary: 正极端子电气
  direction: conserving
- name: '-'
  summary: 负极端子电气
  direction: conserving
- name: C
  summary: 壳体机械
  direction: conserving
- name: R
  summary: 转子机械
  direction: conserving
- name: H
  summary: 热端口热
  direction: conserving
```

### 守恒端口

### **+** — 正极端子电气

与执行器正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与执行器负极端子关联的电气守恒端口。

### **C** — 壳体机械

与执行器壳体关联的机械旋转守恒端口。

### **R** — 转子机械

与转子关联的机械旋转守恒端口。

### **H** — 热端口热

热端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Show thermal port`。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 是否启用热端口 No thermal port（默认）| Show thermal port
  group: ''
- name: Speed values
  summary: 转速向量 [-1500, -1000, -500, 0, 500, 1000, 1500, 2000, 2500, 3000] rpm（默认）
  group: 电磁转矩
- name: Torque values
  summary: 转矩向量 [.04, .035, .03, .025, .02, .015, .01, .005, 0, -.005] Nm（默认）
  group: 电磁转矩
- name: Rated voltage
  summary: 额定电压 12 V（默认）
  group: 电磁转矩
- name: Motor efficiency (percent)
  summary: 电机效率 80（默认）
  group: 电磁转矩
- name: Speed at which efficiency is measured
  summary: 测量效率时的转速 2000 rpm（默认）
  group: 电磁转矩
- name: Torque-independent electrical losses
  summary: 固定电气损耗 0.1 W（默认）
  group: 电磁转矩
- name: Simulation mode
  summary: 仿真模式 PWM（默认）| Averaged
  group: 电磁转矩
- name: Rotor inertia
  summary: 转子惯量 0.0001 kg*m^2（默认）
  group: 机械
- name: Rotor damping
  summary: 转子阻尼 1e-8 N*m/(rad/s)（默认）
  group: 机械
- name: Resistance temperature coefficient
  summary: 电阻温度系数 3.93e-3 1/K（默认）
  group: 温度依赖性
- name: Measurement temperature
  summary: 测量温度 25 degC（默认）
  group: 温度依赖性
- name: Thermal mass
  summary: 热质量 100 J/K（默认）
  group: 热端口
```

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口并对将功率转换为热量的损耗效应进行建模。

### 电磁转矩

### **Speed values** — 转速向量 `[-1500, -1000, -500, 0, 500, 1000, 1500, 2000, 2500, 3000]` `rpm`（默认）

指定转速向量（包含单位），用于转矩-转速数据。

### **Torque values** — 转矩向量 `[.04, .035, .03, .025, .02, .015, .01, .005, 0, -.005]` `Nm`（默认）

指定转矩向量（包含单位），用于转矩-转速数据。

### **Rated voltage** — 额定电压 `12` `V`（默认）

指示您所建模设备的额定电压。

### **Motor efficiency (percent)** — 电机效率 `80`（默认）

模块用于计算转矩相关电气损耗的效率。

### **Speed at which efficiency is measured** — 测量效率时的转速 `2000` `rpm`（默认）

模块用于计算转矩相关电气损耗的转速。

### **Torque-independent electrical losses** — 固定电气损耗 `0.1` `W`（默认）

当转矩为零时与执行器关联的固定电气损耗。

### **Simulation mode** — 仿真模式 `PWM`（默认）| `Averaged`

如果将 **Simulation mode** 参数设置为
`PWM`，则向模块电气端子施加在零电压和额定电压之间切换的 PWM 波形。从电源汲取的电流等于输出机械功率并补偿电气损耗所需的电流量。如果施加的电压超过额定电压，则产生的转矩按比例缩放。但是，施加除额定电压以外的任何电压可能会产生不具有代表性的结果。

如果将 **Simulation mode** 参数设置为
`Averaged`，则响应施加电压 Vav 产生的转矩为

VavVrated×T(ω)

其中 T(ω) 是转速 ω 处的转矩值。从电源汲取的电流使得电流与 Vav 的乘积等于所消耗的平均功率。

### 机械

### **Rotor inertia** — 转子惯量 `0.0001` `kg*m^2`（默认）

转子对电机运动变化的阻力。该值可以为零。

### **Rotor damping** — 转子阻尼 `1e-8` `N*m/(rad/s)`（默认）

转子阻尼。该值可以为零。

### 温度依赖性

要启用这些参数，请将 **Modeling option** 设置为
`Show thermal port`。

### **Resistance temperature coefficient** — 电阻温度系数 `3.93e-3` `1/K`（默认）

电阻温度系数。

### **Measurement temperature** — 测量温度 `25` `degC`（默认）

定义执行器参数时所对应的温度。

### 热端口

要启用此参数，请将 **Modeling option** 设置为
`Show thermal port`。

### **Thermal mass** — 热质量 `100` `J/K`（默认）

热质量是使温度升高一度所需的能量。
## 所属库

Simscape / Electrical / Electromechanical / Mechatronic Actuators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009b 中引入**

## 描述

由直流电压源或 PWM 驱动器驱动的通用旋转执行器

Generic Rotary Actuator 模块实现了一个通用旋转执行器模型，设计为由直流电压源或 PWM 驱动器驱动。您可以通过在额定电压下驱动电机时的表格值来定义转矩-转速特性。此功能允许您在不参考等效电路的情况下对电机进行建模。

电机或执行器架构决定了电气损耗依赖于转矩的方式。例如，直流电机的损耗与电流的平方成正比。由于转矩与电流成正比，损耗也与机械转矩成正比。大多数电机都有一个与机械转矩平方成正比的电气损耗项。Generic Rotary Actuator 模块使用您提供的 **Motor efficiency (percent)** 和 **Speed at which efficiency is measured** 参数来计算此损耗项。

某些电机还具有与转矩无关的损耗项。一个例子是他励电机，其中励磁绕组无论负载如何都汲取恒定电流。**Torque-independent electrical losses** 参数用于考虑此效应。

电机效率是机械功率除以机械功率与两个电气损耗项之和。模块假定定义电机效率时的转速位于电动象限，因此为正值。

您可以通过改变所施加电压的符号来使模块反向运行。例如，如果 REV 端口处的电压大于 **Reverse threshold voltage** 参数，则 H-Bridge 模块会反转电机方向。但是，如果您反向使用该模块，请为正向运行指定转矩-转速数据：

- 电动象限中的正转矩和正转速。
- 发电逆时针象限中的正转矩和负转速。
- 发电顺时针象限中的负转矩和正转速。

### 热效应建模

您可以暴露热端口以对将功率转换为热量的损耗效应进行建模。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 模块不包含热端口。
- `Show thermal port` — 模块包含一个热守恒端口。

有关在执行器模块中使用热端口的详细信息，请参阅 Simulating Thermal Effects in Rotational and Translational Actuators。
