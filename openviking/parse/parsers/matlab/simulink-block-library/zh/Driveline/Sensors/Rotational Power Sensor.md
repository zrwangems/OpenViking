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

### **P** — 旋转功率变化，W 物理信号

输出旋转功率变化的物理信号端口。
### 守恒

### **C** — 从动端口 机械旋转

与外壳关联的机械旋转守恒端口。

### **R** — 基准端口 机械旋转

与负载关联的机械旋转守恒端口。

### **S** — 源端口 机械旋转

与驱动源关联的机械旋转守恒端口。

## 参数

### **测量类型** — 功率测量方法 `Instantaneous power`（默认） | `Average power over a specified period` | `Average power over a vibration` | `Average power over a revolution`

用于测量瞬时功率或平均功率的选项。

- `Instantaneous power` — 输出在当前仿真时间
  步测得的旋转功率。
- `Average power over a specified
  period` — 输出在固定时间段内
  平均的旋转功率。
- `Average power over a vibration` —
  输出在一个振动周期内平均的旋转
  功率。
- `Average power over a revolution` —
  输出在一个旋转周期内平均的旋转
  功率。

### **平均周期** — 在指定周期内平均功率的时间跨度 `1` `s`（默认） | positive scalar

模块用于计算平均功率的时间段。例如，
您可以将此值设置为旋转设备的循环长度。

#### 依赖关系

要启用此参数，请将 **测量类型** 设置为
`Average power over a specified
period`.

### **最大振动频率** — 在振动周期内平均功率时要使用的最高频率 `1000` `Hz`（默认） | positive scalar

用于平均旋转功率的最高振动频率。非常
高的值会降低仿真速度。非常低的值可能导致功率
测量值偏低。

#### 依赖关系

要启用此参数，请将 **测量类型** 设置为
`Average power over a vibration`.

### **最大旋转速度** — 在旋转周期内平均功率时要使用的最高角速度 `1000` `rpm`（默认） | positive scalar

用于平均旋转功率的最高速度。非常高的值会
降低仿真速度。非常低的值可能导致功率测量值
偏低。

#### 依赖关系

要启用此参数，请将 **测量类型** 设置为
`Average power over a revolution`.

## 所属库

Simscape / Driveline / Sensors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

测量平均或瞬时旋转功率

Rotational Power Sensor 模块测量端口 **R** 和 **C** 之间的旋转
功率变化。物理信号输出可以是瞬时值或平均值，具体取决于您
为 **测量类型** 参数选择的内容。

当您设置：

- **测量类型** 为 `Instantaneous
  power` 时，瞬时功率是当前
  角速度与转矩的乘积。使用此设置可分析峰值功率传输
  并识别重载组件。
- **测量类型** 为 `Average power over a
  specified period` 时，时间平均功率是
  瞬时功率在一个采样周期上的积分，除以该周期。对于
  小于采样周期的仿真时间，平均功率为零。功率
  输出在每个采样周期内恒定。
- **测量类型** 为 `Average power over a
  vibration` 时，平均振动功率是
  功率在一个振动周期上的积分，除以该周期。振动周期是
  速度值从负到正连续两次交叉之间的时间。如果振动具有可变频率，平均周期可能
  变化。对于小于振动周期的仿真时间，平均
  功率为零。功率输出在每个振动周期内恒定。
- **测量类型** 为 `Average power over a
  revolution` 时，平均旋转功率是
  瞬时功率在一个旋转周期上的积分，除以该周期。旋转周期
  定义为角位置零点的连续两次交叉之间的时间。如果旋转具有可变频率，平均
  周期可能变化。对于小于旋转周期的仿真时间，平均功率
  为零。功率输出在每个旋转周期内恒定。
