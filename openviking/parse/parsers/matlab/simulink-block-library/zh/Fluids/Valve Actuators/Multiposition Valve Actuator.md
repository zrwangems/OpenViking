---
type: simulink-block
title: 'Multiposition Valve Actuator'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Valve Actuators'
documentation_page: 'multipositionvalveactuator'
documentation_source_path: 'ref/multipositionvalveactuator.html'
language: zh-CN
chinese_source: worker-translation
---

# Multiposition Valve Actuator

## 端口

### 输入

### **A** — 输入信号 物理信号

输入端口，指定为物理信号。

当 **Actuator positions** 设置为 `2` 时，根据 **Actuator travel direction** 设置，此端口可以控制执行器的正向或负向运动。

当 **Actuator positions** 设置为 `3` 时，此端口接收对应于正向执行器位移方向的物理信号。

### **B** — 输入信号 物理信号

负向执行器位移的输入端口，以物理信号形式接收。

#### 依赖关系

要启用此端口，请将 **Actuator positions** 设置为 `3`。

### 输出

### **S** — 执行器位置，m 物理信号

执行器位置，以 m 为单位，指定为物理信号。

如果将 Multiposition Valve Actuator 模块与 Gas Library 中的阀门配合使用，气体模块会将执行器信号单位从 m 转换为单位 1。

## 参数

### **Actuator positions** — 阀门位置信号数量 `2`（默认）| `3`

阀门位置信号的数量。设置为 `2` 时，执行器接收一个信号并设置一个位置信号。设置为 `3` 时，执行器接收一个正向信号和一个负向信号，并设置一个位置信号。

### **Push-pin stroke** — 推杆最大伸出量 `0.01` m（默认）| 正标量

推杆最大伸出量。

### **Switching-on time** — 信号过渡时间段 `0.1` s（默认）| 正标量

达到 **Push-pin stroke** 参数值所需的时间段。该时间段在输入信号上升超过 **Nominal signal value** 参数值的 50% 后开始。

### **Switching-off time** — 信号过渡时间段 `0.1` s（默认）| 正标量

从 **Push-pin stroke** 参数返回到 **Initial position** 参数所需的时间段。该时间段在输入信号下降到 **Nominal signal value** 的 50% 以下后开始。

### **Nominal signal value** — 执行器完全伸出的标称信号 `24`（默认）| 正标量

执行器完全伸出的标称信号。当输入信号达到 **Nominal signal value** 的 50% 时，触发执行器运动。

### **Initial position** — 执行器起始位置 `Retracted`（默认）| `Extended` | `Neutral`

执行器的起始位置。`Retracted` 和 `Extended` 对应于执行器推杆行程限位。

当 **Actuator positions** 设置为 `2` 时，**Initial position** 默认为 `Retracted`。当 **Actuator positions** 设置为 `3` 时，**Initial position** 默认为 `Neutral`。`Neutral` 对应于 **Push-pin stroke** 的中间位置。

### **Actuator travel direction** — 执行器运动方向 `Positive`（默认）| `Negative`

执行器响应物理信号输入的运动方向。`Positive` 设置对应于推杆伸出。

#### 依赖关系

要启用此参数，请将 **Actuator positions** 设置为 `2`。

## 所属库

Simscape / Fluids / Valve Actuators Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Valve Actuators & Forces / Valve Actuators

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

任意流体域中的多位置执行器

Multiposition Valve Actuator 模块对任意流体域中的多位置执行器进行建模。您可以将其与任何以物理信号作为输入的阀门模块组合使用。输入信号和切换时间会影响执行器位置。

### Two-Position Actuator Movement

当端口 **A** 处信号的值超过 **Nominal signal value** 参数值的 50% 时，致动开始。经过等于 **Switching-on time** 参数值三分之一的时间段后，致动器开始朝 **Push-pin stroke** 参数指定的限位移动。

当端口 **A** 处信号的值低于 **Nominal signal value** 参数值的 50% 时，致动器在经过等于 **Switching-off time** 参数值三分之一的时间段后反向。运动可在行程中途中断。

在上图中，*ton* 是 **Switching-on time** 参数的值。*ton* 期间的致动器运动包含初始静止、二次运动和线性运动，分别由 *tde*、*tae* 和 *tve* 表示。*tde*、*tae* 和 *tve* 长度均相等。

当控制信号关闭时，致动器切换方向。*toff* 是 **Switching-off time** 参数的值，在此期间致动器重复与开启运动相同的阶段。*tdr* 是静止阶段，*tar* 是二次运动阶段，*tvr* 是线性运动阶段。在 *toff* 结束时，致动器位置处于 **Initial position** 参数的值。*tdr*、*tar* 和 *tvr* 长度均相等。

当 **Actuator positions** 为 `2` 时，**Actuator travel direction** 参数设置推杆运动的方向。

致动器运动可在任何时候中断。如果推杆运动在行程中途被打断，则开启和关闭时间会根据推杆位置相对于推杆行程按比例调整。

### Three-Position Actuator Movement

当 **Actuator positions** 设置为 `3` 时，端口 **A** 处的信号使致动器沿正方向移动，端口 **B** 处接收的信号使致动器沿负方向移动。一次仅处理来自一个端口的一个信号。要在端口 **A** 和 **B** 之间切换控制，或在正位移控制和负位移控制之间切换，致动器必须首先移动到中立位置。如果推杆运动在行程中途被打断，则开启和关闭时间会根据推杆位置相对于推杆行程按比例调整。致动器运动可在任何时候中断。

当由端口 **A** 处的信号控制时，三位置致动器具有与 **Actuator travel direction** 设置为 `Positive` 时的两位置致动器相同的位移曲线。当由端口 **B** 处的信号控制时，其曲线与 **Actuator travel direction** 设置为 `Negative` 时的两位置致动器相同。
