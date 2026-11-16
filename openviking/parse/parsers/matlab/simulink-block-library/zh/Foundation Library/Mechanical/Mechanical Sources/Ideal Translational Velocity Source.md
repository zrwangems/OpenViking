---
type: simulink-block
title: 'Ideal Translational Velocity Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Mechanical Sources'
documentation_page: 'idealtranslationalvelocitysource'
documentation_source_path: 'ref/idealtranslationalvelocitysource.html'
language: zh-CN
chinese_source: official
---

# Ideal Translational Velocity Source

## 端口

### 输入

### **S** — 控制信号，单位为 m/s 物理信号

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

机械平移系统中的理想速度源

Ideal Translational Velocity Source 模块表示理想速度源，可在其端子处产生与输入物理信号成比例的速度差。从某种意义上说，这是一个理想源，因为它假设无论施加在系统上的力多大，它都能将速度保持在指定值。

连接端 R 和 C 是机械平移守恒端口。端口 S 是物理信号端口，通过该端口应用驱动该源的控制信号。源两端的相对速度（速度差）与控制端口 S 处的信号成正比。各种 Simulink® 信号源均可用于生成所需的速度变化曲线。

此模块的正方向是从端口 R 到端口 C。这意味着速度测量为 *v* = *v*R – *v*C，其中 *v*R 和 *v*C 分别是端口 R 和端口 C 处的绝对速度，并且如果通过源的力是从 R 作用于 C，则该力为正。如果源向端口 R 输送能量，则源产生的功率为负。
