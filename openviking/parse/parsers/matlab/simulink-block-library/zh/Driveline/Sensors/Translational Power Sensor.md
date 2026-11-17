---
type: simulink-block
title: 'Translational Power Sensor'
family: 'sdl'
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
```yaml
ports:
- name: P
  summary: 平移功率，W 物理信号
  direction: input
- name: S
  summary: 驱动源机械平移
  direction: input
- name: R
  summary: 杆机械平移
  direction: input
- name: C
  summary: 壳体机械平移
  direction: input
```

### 输入

### **P** — 平移功率，W 物理信号

与平移功率相关联的物理信号输入端口，单位为 W。
### 守恒

### **S** — 驱动源机械平移

与驱动源相关联的机械平移守恒端口。

### **R** — 杆机械平移

与杆或轴相关联的机械平移守恒端口。

### **C** — 壳体机械平移

与壳体相关联的机械平移守恒端口。
## 参数
```yaml
parameters:
- name: Measurement type
  summary: 测量功率的选项 Instantaneous power（默认）| Average power over a specified period | Average power over a vibration
  group: ''
- name: Averaging period
  summary: 功率平均周期 1 s（默认）| 正标量
  group: ''
- name: Maximum vibration frequency
  summary: 最大振动频率 1000 Hz（默认）| 正标量
  group: ''
```

### **Measurement type** — 测量功率的选项 `Instantaneous power`（默认）| `Average power over a specified period` | `Average power over a vibration`

是测量瞬时功率、指定时间段内的平均功率，还是一个振动周期内的平均功率。

- `Instantaneous power` — 输出当前时间步长测得的功率。
- `Average power over a specified period` — 输出在固定时间段内平均的功率。
- `Average power over a vibration` — 输出在一个振动周期内平均的功率。

### **Averaging period** — 功率平均周期 `1` `s`（默认）| 正标量

对功率进行平均的时间段。典型值包括往复式设备的循环长度或致动力。

### **Maximum vibration frequency** — 最大振动频率 `1000` `Hz`（默认）| 正标量

对功率进行平均的最大振动频率。非常高的值往往会降低仿真速度。非常低的值往往会导致较低的功率测量值。
## 所属库

Simscape / Driveline / Sensors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

平均或瞬时平移功率传感器

Translational Power Sensor 模块表示一个传感器，用于测量由于连接在端口 **R** 和 **C** 之间的一个或多个传动系统组件引起的平移功率变化。功率输出可以是瞬时值或平均值。提供两种平均选项：周期平均和振动平均。

瞬时功率是当前速度和力的乘积。使用瞬时功率来分析峰值功率传输并识别重载组件。

时间平均功率是瞬时功率在一个采样周期内的积分除以该周期。对于小于采样周期的仿真时间，平均功率为零。功率在每个采样周期内是恒定的。

振动平均功率是功率在一个振动周期内的积分除以该周期。振动周期是速度值从负到正连续两次交叉之间的时间。仅对速度过零的振荡使用此平均方法。如果振动具有可变频率，则平均周期可能会变化。对于小于振动周期的仿真时间，平均功率为零。功率输出在每个振动周期内是恒定的。
