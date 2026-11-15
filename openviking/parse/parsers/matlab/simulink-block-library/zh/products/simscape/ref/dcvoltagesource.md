---
type: simulink-block
title: 'DC Voltage Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Electrical Models / Electrical Sources'
documentation_page: 'dcvoltagesource'
documentation_source_path: 'ref/dcvoltagesource.html'
language: zh-CN
chinese_source: official
---

# DC Voltage Source

## 端口

### 守恒

### **+** — 正极端子 电气

与电气源正极端子相关联的电气守恒端口。

### **-** — 负极端子 电气

与电气源负极端子相关联的电气守恒端口。

## 参数

### **恒定电压** — 输出电压 `1 V` (默认) | 标量

电压源两端的电压。您可以指定正值，也可以指定负值。

## 所属库

Simscape / Foundation Library / Electrical / Electrical Sources

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007a 中推出**

## 描述

理想的恒定电压源

DC Voltage Source 模块表示理想的电压源，无论流过该电压源的电流多大，它都能将其两端的电压保持在指定值。

您可以使用**恒定电压**参数指定输出电压，可以是正值，也可以是负值。

连接端 **+** 和 **-** 是分别对应于电压源的正极端子和负极端子的守恒电气端口。如果电流从正极流向负极，则电流为正，电压源两端的电压等于正极端子电压与负极端子电压之差，即 *V*(+) – *V*(-)。
