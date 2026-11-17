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
```yaml
ports:
- name: A
  summary: 阀门开度信号 物理信号
  direction: input
- name: S
  summary: 阀门开度距离，m 物理信号
  direction: output
```

### 输入

### **A** — 阀门开度信号 物理信号

指示阀门打开或关闭的物理信号，指定为物理信号。该信号乘以 **Actuator gain** 值。

### 输出

### **S** — 阀门开度距离，m 物理信号

所连接阀门的开度距离，以 m 为单位，指定为物理信号。

如果将 Proportional Valve Actuator 模块与 Gas Library 中的阀门配合使用，气体模块会将执行器信号单位从 m 转换为单位 1。
## 参数
```yaml
parameters:
- name: Actuator gain
  summary: 输入信号乘数 5e-4 m（默认）| 正标量
  group: ''
- name: Time constant
  summary: 开度信号时间常数 0.01 s（默认）| 正标量
  group: ''
- name: Valve stroke
  summary: 最大阀门开度距离 0.005 m（默认）| 正标量
  group: ''
```

### **Actuator gain** — 输入信号乘数 `5e-4 m`（默认）| 正标量

阀门开度距离的输入信号乘数。

### **Time constant** — 开度信号时间常数 `0.01 s`（默认）| 正标量

用于表征执行过程中达到稳态条件所需时间的常数。该参数影响对阀门打开或关闭信号的响应滞后。

### **Valve stroke** — 最大阀门开度距离 `0.005 m`（默认）| 正标量

所连接阀门的最大开度距离。
## 所属库

Simscape / Fluids / Valve Actuators Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Valve Actuators & Forces / Valve Actuators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

任意流体域中的功率控制阀门执行器

Proportional Valve Actuator 模块对用于任意流体域中与阀门模块配合使用的功率控制执行器进行建模。您可以将其与任何以物理信号作为输入的阀门模块组合使用。打开或关闭阀门的信号在端口 **A** 处接收。所连接阀门的开度距离作为物理信号在端口 **S** 处返回。

您可以使用 **Actuator gain** 参数调整打开或关闭的幅度。对执行距离施加一阶时间滞后：

(IG−d)τ，

其中：

- *IG* 是在端口 **A** 处接收的信号乘以 **Actuator gain**。在阀门行程限值之外，如果完全伸出，*IG* 为 **Valve stroke**；如果完全缩回，*IG* 为负的 **Valve stroke**。
- *d* 是当前执行器位置。
- *τ* 是 **Time constant**。
