---
type: simulink-block
title: 'Ideal Torque Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Mechanical Sources'
documentation_page: 'idealtorquesource'
documentation_source_path: 'ref/idealtorquesource.html'
language: zh-CN
chinese_source: worker-translation
---

# Ideal Torque Source

## 端口

### 输入

### **S** — 控制信号，N\*m 物理信号

物理信号输入端口，通过该端口施加驱动源的的控制信号。
### 守恒

### **R** — 杆机械旋转

与源运动部件（杆）关联的机械旋转守恒端口。

### **C** — 壳体机械旋转

与源参考点（壳体）关联的机械旋转守恒端口。

## 参数

R2025b 中未记录。

## 所属库

Simscape / Foundation Library / Mechanical / Mechanical Sources

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2007a 中引入**

## 描述

产生与输入信号成比例的扭矩的理想机械能源

Ideal Torque Source 模块表示一个理想机械能源，它产生与输入物理信号成比例的扭矩。该源是理想的，因为它被假定具有足够的功率，无论源端子处的角速度如何，都能维持指定的扭矩。

连接 R 和 C 是机械旋转守恒端口。端口 S 是物理信号端口，通过该端口施加驱动源的控制信号。您可以使用各种 Simulink® 信号源来生成所需的扭矩变化曲线。端口 S 上的正信号产生从 C 到 R 作用的扭矩。源产生的扭矩与控制端口 S 上的信号成正比。

模块正方向是从端口 C 到端口 R。这意味着如果扭矩沿从 C 到 R 的方向作用，则扭矩为正。相对速度定义为 *ω* = *ω*C –
*ω*R，其中
*ω*R、
*ω*C 分别是端口 R 和 C 处的绝对角速度，如果端口 R 处的速度大于端口 C 处的速度，则为负。如果源向端口 R 提供能量，则源产生的功率为负。
