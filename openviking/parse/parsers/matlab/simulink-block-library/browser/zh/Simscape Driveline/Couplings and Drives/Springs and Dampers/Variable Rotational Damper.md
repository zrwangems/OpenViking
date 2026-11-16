---
type: simulink-block
title: 'Variable Rotational Damper'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Couplings and Drives / Springs and Dampers'
documentation_page: 'variablerotationaldamper'
documentation_source_path: 'ref/variablerotationaldamper.html'
language: zh-CN
chinese_source: worker-translation
---

# Variable Rotational Damper

## 端口

### 输入

### **B** — 可变阻尼系数物理信号

与可变阻尼系数关联的物理信号输入端口。
### 守恒

### **C** — 基座端口（旋转机械）

与基座关联的旋转机械守恒端口。

### **R** — 从动端口（旋转机械）

与从动件关联的旋转机械守恒端口。

## 参数

### **最小阻尼系数** — 阻尼限制值 `0` `N*m/(rad/s)`（默认） | 非负标量

阻尼系数允许的最小值。物理信号输入在该水平以下饱和。

## 所属库

Simscape / Driveline / Couplings & Drives / Springs & Dampers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

具有可变阻尼系数的旋转阻尼器

Variable Rotational Damper 模块表示一个具有可变阻尼系数的旋转黏性阻尼器。物理信号输入端口提供阻尼系数的幅值。阻尼力矩的幅值等于物理信号输入与两个旋转机械守恒端口 **R** 和 **C** 之间的相对角速度的乘积。最小阻尼系数可防止非物理的负阻尼值。

阻尼力矩满足以下表达式：

T={B⋅ωB≥BminBmin⋅ωB<Bmin,

其中

- *T* 是通过阻尼器传递的力矩。
- *B* 是黏性阻尼系数。
- *ω* 是根据 ω=ωR−ωC 测量的两个旋转机械守恒端口之间的相对角速度。
- *ωR* 是旋转机械守恒端口 **R** 的角速度。
- *ωC* 是旋转机械守恒端口 **C** 的角速度。

该模块在旋转机械守恒端口上施加大小相等、方向相反的阻尼力矩。作用在端口 **R** 上的阻尼力矩的符号等于相对角速度的符号。正的相对角速度对应于作用在端口 **R** 上的正阻尼力矩，以及作用在端口 **C** 上的大小相等的负阻尼力矩。

### 假设与限制

- 该模块仅表示黏性阻尼。
- 阻尼系数的值必须大于或等于零。
