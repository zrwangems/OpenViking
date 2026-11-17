---
type: simulink-block
title: 'Ideal Torque Sensor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Mechanical Sensors'
documentation_page: 'idealtorquesensor'
documentation_source_path: 'ref/idealtorquesensor.html'
language: zh-CN
chinese_source: worker-translation
---

# Ideal Torque Sensor

## 端口
```yaml
ports:
- name: T
  summary: 扭矩，N\*m 物理信号
  direction: output
- name: R
  summary: 杆（正探头）机械旋转
  direction: output
- name: C
  summary: 壳体（参考探头）机械旋转
  direction: output
```

### 输出

### **T** — 扭矩，N\*m 物理信号

扭矩的物理信号输出端口。
### 守恒

### **R** — 杆（正探头）机械旋转

与传感器正探头关联的机械旋转守恒端口。

### **C** — 壳体（参考探头）机械旋转

与传感器负（参考）探头关联的机械旋转守恒端口。
## 参数
```yaml
parameters: []
```

在 R2025b 中未记录。
## 所属库

Simscape / Foundation Library / Mechanical / Mechanical Sensors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

机械旋转系统中的扭矩传感器

Ideal Torque Sensor 模块表示一种设备，它将通过传感器的变量转换为与扭矩成比例的控制信号。该传感器是理想的，因为它不考虑惯性、摩擦、延迟、能量消耗等。

连接 **R** 和 **C** 是机械旋转守恒端口。将此传感器与被测模块串联连接，因为扭矩是（机械旋转领域的）Through 变量。该传感器约束端口 **R** 和 **C** 以允许它们之间无运动，因此并联连接传感器可能会影响仿真结果，因为它类似于在连接点之间添加旁路连接线。在现有线路中串联连接不会影响仿真结果，并能提供准确的测量。

连接 **T** 是输出测量结果的物理信号端口。模块正方向是从端口 **R** 到端口 **C**。这意味着施加到端口 **R**（传感器正探头）的正扭矩会产生正输出信号。
