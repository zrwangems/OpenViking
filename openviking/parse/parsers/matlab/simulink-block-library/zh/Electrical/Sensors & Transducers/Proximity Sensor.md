---
type: simulink-block
title: 'Proximity Sensor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'proximitysensor'
documentation_source_path: 'ref/proximitysensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Proximity Sensor

## 端口

### 输入

### **R** — 径向距离物理信号

与到传感器的径向距离相关联的物理信号端口。

### **Z** — 垂直距离物理信号

与到传感器的垂直距离相关联的物理信号端口。
### 守恒

### **+** — 正电压电气

与接近传感器正电压相关联的电气守恒端口。

### **-** — 负电压电气

与接近传感器负电压相关联的电气守恒端口。

## 参数

### **Vector of radial offset distances R** — 径向偏移距离向量 `[-25, -20, -15, -10, -5, 0, 5, 10, 15, 20, 25]` `mm`（默认）

从传感器到物体的距离在平行于传感器头部的平面上的投影距离向量。

### **Corresponding sensing distances Z** — 对应感测距离 `[0, 0, 5, 8, 9.5, 10, 9.5, 8, 5, 0, 0]` `mm`（默认）

从传感器到物体的距离相对于传感器头部法向量的投影距离向量。

### **Output when not detected** — 未检测到时的输出 `Normally Open (N.O.)`（默认）| `Normally Closed (N.C.)`

指示输出是 `Normally Open (N.O.)`（即仅在检测到物体时输出闭合），还是 `Normally Closed (N.C.)`（即仅在检测到物体时输出断开）。

### **Closed resistance R\_closed** — 闭合电阻 `0.01` `Ohm`（默认）

输出触点闭合时 + 和 - 端口之间的电阻。

### **Open conductance G\_open** — 断开电导 `1e-8` `1/Ohm`（默认）

输出触点断开时 + 和 - 端口之间的电导。

## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

简单距离传感器的理想行为模型

Proximity Sensor 模块表示一个简单的接近传感器。感测距离 *Z* 定义为对于给定的径向偏移 *R*，传感器检测到物体时沿传感器表面法线方向的距离，如下图所示。

下图显示了典型的感测距离曲线：

如果 **R** 和 **Z** 输入位于感测曲线下方（即检测区域内），传感器切换到检测到物体状态。

输出由电气开关建模，当未检测到物体时，该开关可以是常开（N.O.）或常闭（N.C.）。
