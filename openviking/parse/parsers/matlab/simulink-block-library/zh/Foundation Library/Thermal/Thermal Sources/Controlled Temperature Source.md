---
type: simulink-block
title: 'Controlled Temperature Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal / Thermal Sources'
documentation_page: 'controlledtemperaturesource'
documentation_source_path: 'ref/controlledtemperaturesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Controlled Temperature Source

## 端口

### 输入

### **S** — 温度控制信号，K 物理信号

输入物理信号，用于指定源两端的温差。

### 守恒

### **A** — 源入口热端口

与源入口关联的热守恒端口。

### **B** — 源出口热端口

与源出口关联的热守恒端口。

## 参数

R2025b 中未记录。

## 所属库

Simscape / Foundation Library / Thermal / Thermal Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007b 中引入**

## 描述

以温度为特性的可变热能源

Controlled Temperature Source 模块表示一个理想热能源，其功率足以在源两端维持指定的温差，而不管系统消耗的热流如何。

连接 A 和 B 是对应于源入口和出口的热守恒端口。端口 S 是物理信号端口，通过该端口施加驱动源的控制信号。您可以使用各种 Simulink® 信号源来生成所需的热流变化曲线。源两端的温差与控制端口 S 处的信号成正比。

模块正方向为从端口 A 到端口 B。这意味着温差确定为 *TB* –
*TA*，其中
*TB* 和
*TA* 是源端口处的温度。
