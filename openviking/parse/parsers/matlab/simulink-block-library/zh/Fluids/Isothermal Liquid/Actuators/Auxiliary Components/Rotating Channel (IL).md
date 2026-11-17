---
type: simulink-block
title: 'Rotating Channel (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Actuators / Auxiliary Components'
documentation_page: 'rotatingchannelil'
documentation_source_path: 'ref/rotatingchannelil.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotating Channel (IL)

## 端口

### 守恒端口

### **A** — 液体端口，等温液体

液体进入或出口端口。

### **B** — 液体端口，等温液体

液体进入或出口端口。

### 输入

### **W** — 角速度，rad/s，物理信号

旋转轴角速度，单位为 rad/s，指定为物理信号。

## 参数

### **Channel area** — 轴通道横截面积 `1e-3` m^2（默认）| 正标量

液体进入/出口的轴通道横截面积。

### **Port B radius of rotation** — 旋转半径 `0.01` m（默认）| 正标量

管道旋转的扫掠圆半径，在端口 **B** 处指定。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

用于修正理论流动中排放损失的修正系数。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过孔口的层流的上限雷诺数。

## 所属库

Simscape / Fluids / Isothermal Liquid / Pipes & Fittings

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体网络中带流体通道的旋转管道

Rotating Channel (IL) 模块用于在等温液体网络中建模带流体通道的旋转管道。管道角速度由端口 **W** 处的物理信号设定。端口 **A** 和 **B** 为等温液体入口和出口端口。

流体通过旋转通道时，由于通过壳体孔口的阻力以及流体的角动量，会经历压力变化。内部连接到 Orifice (IL) 模块用于考虑局部阻力。模块中的压力变化建模为：

P=ρAW2rB22，

其中：

- *ρ*A 是端口 **A** 处的流体密度。
- *W* 是轴角速度，作为物理信号在端口 **W** 处接收。
- *r*B 是端口 **B** 处的旋转半径。

等温液体出口端口可连接到 Rotating Cylinder Force (IL) 模块，以建模诸如 Rotating Single-Acting Actuator (IL) 等组件。

### 假设与限制

- 不计算流体惯性的影响。
- 假设管道角速度恒定或变化非常缓慢。
