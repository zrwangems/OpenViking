---
type: simulink-block
title: 'Ideal Torque Sensor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Mechanical Models / Mechanical Sensors'
documentation_page: 'idealtorquesensor'
documentation_source_path: 'ref/idealtorquesensor.html'
language: zh-CN
chinese_source: official
---

# Ideal Torque Sensor

## 端口

### 输出

### **T** — 扭矩 (N\*m) 物理信号

扭矩的物理信号输出端口。
### 守恒

### **R** — 杆（正极探头） 机械旋转

与传感器正极探头相关联的机械旋转守恒端口。

### **C** — 外壳（参考探头） 机械旋转

与传感器负极（参考）探头相关联的机械旋转守恒端口。

## 参数

R2025b 官方文档未提供。

## 所属库

Simscape / Foundation Library / Mechanical / Mechanical Sensors

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007a 中推出**

## 描述

机械旋转系统中的扭矩传感器

Ideal Torque Sensor 模块表示一种可将通过传感器的变量转换为与扭矩成比例的控制信号的器件。这是一种理想的传感器，因为它不考虑惯性、摩擦、延迟和能耗等因素。

连接端 **R** 和 **C** 是机械旋转守恒端口。将此传感器与您想要测量扭矩的模块进行串联，因为（对于机械旋转域来说）扭矩是一个流变量。传感器对端口 **R** 和 **C** 施加限制，不允许它们之间有运动，所以将传感器并联可能会影响仿真结果，这是因为并联类似于在连接点之间添加旁路连接线。在现有线路中进行串联不会影响仿真结果，能提供准确的测量值。

连接端 **T** 是输出测量结果的物理信号端口。模块的正方向是从端口 **R** 到端口 **C**。这意味着施加到端口 **R**（传感器正极探头）的正向扭矩会生成一个正的输出信号。
