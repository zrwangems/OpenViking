---
type: simulink-block
title: 'Current Sensor'
family: 'simscape'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Electrical / Electrical Sensors'
documentation_page: 'currentsensor'
documentation_source_path: '../simscape/ref/currentsensor.html'
language: zh-CN
chinese_source: official
---

# Current Sensor

## 端口

### 输出

### **I** — 电流（单位：A） 物理信号

电流测量值的物理信号输出端口。
### 守恒

### **+** — 正极端子 电气

与传感器正极端子相关联的电气守恒端口。

### **-** — 负极端子 电气

与传感器负极端子相关联的电气守恒端口。

## 参数

R2025b 官方文档未提供。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Sensors Simscape / Electrical / Sensors & Transducers

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007a 中推出**

## 描述

电气系统中的电流传感器

Current Sensor 模块表示理想的电流传感器，即一种将在任何电气分支中测量的电流转换为与该电流成比例的物理信号的器件。

使用 **+** 和 **-** 端口将传感器与您想要测量电流的支路中的其他模块串联起来。端口 **I** 将测量结果输出为一个物理信号。使用 PS-Simulink Converter 模块将此端口连接到 Simulink® 模块，例如 Scope 或 Display。
