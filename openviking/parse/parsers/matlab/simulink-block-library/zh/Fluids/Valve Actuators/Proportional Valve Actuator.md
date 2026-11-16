---
type: simulink-block
title: 'Proportional Valve Actuator'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Valve Actuators'
documentation_page: 'proportionalvalveactuator'
documentation_source_path: 'ref/proportionalvalveactuator.html'
language: zh-CN
chinese_source: worker-translation
---

# Proportional Valve Actuator

## 端口

### 输入

### **A** — 阀门开启信号 物理信号

指示阀门开启或关闭的物理信号，指定为物理信号。该信号乘以 **Actuator gain** 的值。
### 输出

### **S** — 阀门开启距离，m 物理信号

所连接阀门的开启距离，以 m 为单位，指定为物理信号。

如果将 Proportional Valve Actuator 模块与来自 Gas Library 的阀门一起使用，气体模块会将执行器信号单位从 m 转换为 1。

## 参数

### **Actuator gain** — 输入信号乘数 `5e-4 m`（默认）| 正标量

用于阀门开启距离的输入信号乘数。

### **Time constant** — 开启信号时间常数 `0.01 s`（默认）| 正标量

该常数表示执行过程中达到稳态条件所需的时间。此参数影响对阀门开启或关闭信号的响应滞后。

### **Valve stroke** — 最大阀门开启距离 `0.005 m`（默认）| 正标量

所连接阀门的最大开启距离。

## 所属库

Simscape / Fluids / Valve Actuators Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Valve Actuators & Forces / Valve Actuators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

任意流体域中的功率控制阀执行器

Proportional Valve Actuator 模块对一种功率控制执行器进行建模，该执行器可在任意流体域中与阀门模块配合使用。您可以将其与任何以物理信号作为输入的阀门模块组合使用。用于打开或关闭阀门的信号在端口 **A** 处接收。所连接阀门的开启距离作为物理信号在端口 **S** 处返回。

您可以使用 **Actuator gain** 参数调整开启或关闭的幅度。对执行距离应用一阶时间滞后：

(IG−d)τ,

其中：

- *IG* 是在端口 **A** 处接收的信号乘以 **Actuator gain**。在阀门行程限制之外，如果完全伸出，*IG* 为 **Valve stroke**；如果完全缩回，*IG* 为 **Valve stroke** 的负值。
- *d* 是当前执行器位置。
- *τ* 是 **Time constant**。
