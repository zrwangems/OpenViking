---
type: simulink-block
title: 'Translational Power Sensor'
family: 'sensors'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Sensors'
documentation_page: 'translationalpowersensor'
documentation_source_path: 'ref/translationalpowersensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Power Sensor

## 端口

### 输入

### **P** — 平移功率，W 物理信号

与平移功率关联的物理信号输入端口，单位为 W。
### 守恒

### **S** — 驱动源机械平移

与驱动源关联的机械平移守恒端口。

### **R** — 杆机械平移

与杆或轴关联的机械平移守恒端口。

### **C** — 壳体机械平移

与壳体关联的机械平移守恒端口。

## 参数

### **Measurement type** — 用于测量功率的选项 `Instantaneous power` (默认) | `Average power over a specified period` | `Average power over a vibration`

是否测量瞬时功率、指定时间段内的平均功率或一次振动内的平均功率。

- `Instantaneous power` — 输出为当前时间步测量的功率。
- `Average power over a specified period` — 输出在固定时间段内平均后的功率。
- `Average power over a vibration` — 输出在一个振动周期内平均后的功率。

### **Averaging period** — 功率平均周期 `1` `s` (默认) | positive scalar

用于对功率进行平均的时间段。典型值包括往复设备的循环长度或致动力。

### **Maximum vibration frequency** — 最大振动频率 `1000` `Hz` (默认) | positive scalar

用于对功率进行平均的最大振动频率。非常高的值往往会降低仿真速度。非常低的值往往会导致功率测量值偏低。

## 所属库

Simscape / Driveline / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

平均或瞬时平移功率传感器

Translational Power Sensor 模块表示一个传感器，用于测量由一个或多个连接在端口 **R** 和 **C** 之间的传动系统组件引起的平移功率变化。功率输出可以是瞬时值或平均值。提供两种平均选项：周期平均和振动平均。

瞬时功率是当前速度与力的乘积。使用瞬时功率分析峰值功率传输并识别重载组件。

时间平均功率是瞬时功率在一个采样周期上的积分除以该周期。对于小于采样周期的仿真时间，平均功率为零。每个采样周期内功率为常数。

振动平均功率是功率在一个振动周期上的积分除以该周期。振动周期是速度值从负到正连续两次穿越之间的时间。仅对速度经过零的振荡使用此平均方法。如果振动具有可变频率，平均周期可能会变化。对于小于振动周期的仿真时间，平均功率为零。每个振动周期内功率输出为常数。
