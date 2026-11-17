---
type: simulink-block
title: 'Logic-Controlled Clutch'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Clutches'
documentation_page: 'logiccontrolledclutch'
documentation_source_path: 'ref/logiccontrolledclutch.html'
language: zh-CN
chinese_source: worker-translation
---

# Logic-Controlled Clutch

## 端口

### 输入

### **E** — 控制离合器接合的物理信号

与离合器逻辑关联的物理信号端口。
### 守恒

### **B** — 基座接口机械旋转

与基座接口关联的机械旋转守恒端口。

### **F** — 从动接口机械旋转

与从动接口关联的机械旋转守恒端口。

## 参数

### **Transition model** — 离合器接合参数化 `Instantaneous`（默认）| `First-order lag` | `Scaled by input`

离合器接合过渡控制。当您选择：

- `Instantaneous` — 当端口 **E** 处的输入信号舍入为 1 时离合器接合，当输入信号舍入为 0 时离合器不接合。
- `First-order lag` — 该模块根据您为 **Transition time constant** 参数指定的值，为离合器接合引入一阶延迟。
- `Scaled by input` — 该模块平滑端口 **E** 处的信号输入。当输入信号大于或等于 1 时，该模块施加完整的静摩擦和动摩擦；当信号非正时，不施加静摩擦或动摩擦力矩。当输入信号介于 0 和 1 之间时，该模块对摩擦力矩进行线性缩放。

### **Transition time constant** — 一阶滞后时间常数 `0.1` `s`（默认）| 正标量

一阶滞后离合器接合的时间常数。

#### 依赖关系

要启用此参数，请将 **Transition model** 设置为 `First-order lag`。

### **Kinetic friction torque** — 动摩擦力矩阈值 `10` `N*m`（默认）| 非负标量

维持离合器片之间相对运动的最小力矩阈值。

### **Static friction torque** — 静摩擦力矩阈值 `20` `N*m`（默认）| 正标量

引起离合器片之间相对运动的最小力矩阈值。

### **Clutch velocity tolerance** — 运动边界条件 `0.001` `rad/s`（默认）| 非负标量

离合器最小角速度。

### **Initial State** — 仿真开始时的离合器状态 `Unlocked`（默认）| `Locked`

选择以离合器解锁或锁定状态开始仿真。

## 所属库

Simscape / Driveline / Clutches

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

带输入控制的摩擦离合器

Logic-Controlled Clutch 表示一种通过摩擦传递旋转动力的逻辑控制机构。该模块是 Fundamental Friction Clutch 模块的高级版本。您可以通过端口 **E** 处的物理信号控制 Logic-Controlled Clutch 模块。

如果离合器正在接合且处于运动状态，该模块施加动摩擦力矩。如果离合器正在接合且未处于运动状态，该模块施加静摩擦力矩。
