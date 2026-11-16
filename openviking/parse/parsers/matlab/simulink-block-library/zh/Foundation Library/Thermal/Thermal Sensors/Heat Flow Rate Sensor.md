---
type: simulink-block
title: 'Heat Flow Rate Sensor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal / Thermal Sensors'
documentation_page: 'heatflowratesensor'
documentation_source_path: 'ref/heatflowratesensor.html'
language: zh-CN
chinese_source: official
---

# Heat Flow Rate Sensor

## 端口

### 输出

### **H** — 热流量测量 (W) 物理信号

用于热流测量的物理信号输出端口。
### 守恒

### **A** — 传感器入口 热

热守恒端口。当端口 **A** 处的值大于端口 **B** 处的值时，测量值为正。

### **B** — 传感器出口 热

热守恒端口。当端口 **A** 处的值大于端口 **B** 处的值时，测量值为正。

## 参数

R2025b 官方文档未提供。

## 所属库

Simscape / Foundation Library / Thermal / Thermal Sensors

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007b 中推出**

## 描述

理想的热流计

Heat Flow Rate Sensor 模块表示一个理想的热流计，即一种可将通过计量表的热流转换为与该流成比例的控制信号的设备。

将此传感器与您想要测量热流的模块进行串联，因为（对于热域来说）热流是一个流变量。并联传感器可能会影响仿真结果，这是因为并联类似于在连接点之间添加旁路连接线。在现有线路中进行串联不会影响仿真结果，能提供准确的测量值。

连接端 **A** 和 **B** 是热守恒端口。端口 **T** 是输出热流值的物理信号端口。

此模块的正方向是从端口 **A** 到端口 **B**。
