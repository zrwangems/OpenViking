---
type: simulink-block
title: 'Ideal Force Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Mechanical Models / Mechanical Sources'
documentation_page: 'idealforcesource'
documentation_source_path: 'ref/idealforcesource.html'
language: zh-CN
chinese_source: official
---

# Ideal Force Source

## 端口

### 输入

### **S** — 控制信号，N 物理信号

物理信号输入端口，通过该端口应用驱动该源的控制信号。
### 守恒

### **R** — 杆 机械平移

与源移动部件（杆）相关联的机械平移守恒端口。

### **C** — 外壳 机械平移

与源参考点（外壳）相关联的机械平移守恒端口。

## 参数

R2025b 官方文档未提供。

## 所属库

Simscape / Foundation Library / Mechanical / Mechanical Sources

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2007a 中推出**

## 描述

产生与输入信号成比例的力的理想机械能量源

Ideal Force Source 模块表示理想的机械能量源，可产生与输入物理信号成比例的力。从某种意义上说，这是一个理想源，因为它假设无论源端子处的速度多大，它都能将输出端的力保持在指定值。

连接端 R 和 C 是机械平移守恒端口。端口 S 是物理信号端口，通过该端口应用驱动该源的控制信号。您可以使用各种 Simulink® 信号源来生成所需的力变化曲线。端口 S 处的正信号产生从 C 作用到 R 的力。源产生的力与控制端口 S 处的信号成正比。

此模块的正方向是从端口 C 到端口 R。这意味着，如果力从 C 作用到 R，则该力为正。相对速度确定为 *v* = *v*C – *v*R，其中 *v*R 和 *v*C 分别是端口 R 和 C 处的绝对速度，并且如果端口 R 处的速度大于端口 C 处的速度，则它为负。如果源向端口 R 输送能量，则源产生的功率为负。
