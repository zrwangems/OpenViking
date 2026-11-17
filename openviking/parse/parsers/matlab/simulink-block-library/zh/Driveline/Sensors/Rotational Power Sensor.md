---
type: simulink-block
title: 'Rotational Power Sensor'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Sensors'
documentation_page: 'rotationalpowersensor'
documentation_source_path: 'ref/rotationalpowersensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotational Power Sensor

## 端口

### 物理信号

### **P** — 旋转功率变化量，W 物理信号

输出旋转功率变化量的物理信号端口。
### 守恒

### **C** — 跟随端口 机械旋转

与壳体关联的机械旋转守恒端口。

### **R** — 基座端口 机械旋转

与负载关联的机械旋转守恒端口。

### **S** — 源端口 机械旋转

与驱动源关联的机械旋转守恒端口。

## 参数

### **Measurement type** — 功率测量方法 `Instantaneous power`（默认）| `Average power over a specified period` | `Average power over a vibration` | `Average power over a revolution`

用于测量瞬时功率或平均功率的选项。

- `Instantaneous power` — 输出在当前仿真时间步测得的旋转功率。
- `Average power over a specified period` — 输出在固定时间段内平均的旋转功率。
- `Average power over a vibration` — 输出在一个振动周期内平均的旋转功率。
- `Average power over a revolution` — 输出在一个旋转周期内平均的旋转功率。

### **Averaging period** — 指定时间段内功率平均的时间跨度 `1` `s`（默认）| 正标量

模块用于计算平均功率的时间段。例如，您可以将此值设置为旋转设备的循环长度。

#### 依赖关系

要启用此参数，请将 **Measurement type** 设置为 `Average power over a specified period`。

### **Maximum vibration frequency** — 对振动进行功率平均时使用的最高频率 `1000` `Hz`（默认）| 正标量

用于对旋转功率进行平均的最高振动频率。非常高的值可能会降低仿真速度。非常低的值可能会导致功率测量值偏低。

#### 依赖关系

要启用此参数，请将 **Measurement type** 设置为 `Average power over a vibration`。

### **Maximum rotational speed** — 对旋转进行功率平均时使用的最高角速度 `1000` `rpm`（默认）| 正标量

用于对旋转功率进行平均的最高速度。非常高的值可能会降低仿真速度。非常低的值可能会导致功率测量值偏低。

#### 依赖关系

要启用此参数，请将 **Measurement type** 设置为 `Average power over a revolution`。

## 所属库

Simscape / Driveline / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

测量平均或瞬时旋转功率

Rotational Power Sensor 模块测量端口 **R** 和 **C** 之间的旋转功率变化。根据 **Measurement type** 参数的选择，物理信号输出可以是瞬时值或平均值。

当您将：

- **Measurement type** 设置为 `Instantaneous power` 时，瞬时功率是当前角速度与扭矩的乘积。使用此设置可分析峰值功率传输并识别重载组件。
- **Measurement type** 设置为 `Average power over a specified period` 时，时间平均功率是瞬时功率在一个采样周期内的积分除以该周期。对于小于采样周期的仿真时间，平均功率为零。每个采样周期的功率输出是恒定的。
- **Measurement type** 设置为 `Average power over a vibration` 时，平均振动功率是功率在一个振动周期内的积分除以该周期。振动周期是速度值从负到正两次连续穿越之间的时间。如果振动具有可变频率，则平均周期可能会改变。对于小于振动周期的仿真时间，平均功率为零。每个振动周期的功率输出是恒定的。
- **Measurement type** 设置为 `Average power over a revolution` 时，平均旋转功率是瞬时功率在一个旋转周期内的积分除以该周期。旋转周期定义为角位置两次连续过零之间的时间。如果旋转具有可变频率，则平均周期可能会改变。对于小于旋转周期的仿真时间，平均功率为零。每个旋转周期的功率输出是恒定的。
