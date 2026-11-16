---
type: simulink-block
title: 'Controlled Temperature Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Thermal Models / Thermal Sources'
documentation_page: 'controlledtemperaturesource'
documentation_source_path: 'ref/controlledtemperaturesource.html'
language: zh-CN
chinese_source: official
---

# Controlled Temperature Source

## 端口

### 输入

### **S** — 温度控制信号 (K) 物理信号

指定源两端温差的输入物理信号。
### 守恒

### **A** — 源入口 热

与源入口相关联的热守恒端口。

### **B** — 源出口 热

与源出口相关联的热守恒端口。

## 参数

R2025b 官方文档未提供。

## 所属库

Simscape / Foundation Library / Thermal / Thermal Sources

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007b 中推出**

## 描述

可变热能源，以温度为特征

Controlled Temperature Source 模块表示理想的热能源，无论系统消耗的热流多大，它都足以在源两端维持指定的温差。

连接端 A 和 B 是分别对应于源入口和出口的热守恒端口。端口 S 是物理信号端口，通过该端口应用驱动该源的控制信号。您可以使用各种 Simulink® 信号源来生成所需的热流变化曲线。源两端的温差与控制端口 S 处的信号成正比。

此模块的正方向是从端口 A 到端口 B。这意味着温差确定为 *TB* – *TA*，其中 *TB* 和 *TA* 是源端口处的温度。
