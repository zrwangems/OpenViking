---
type: simulink-block
title: 'Rotating Cylinder Force (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Actuators / Auxiliary Components'
documentation_page: 'rotatingcylinderforceil'
documentation_source_path: 'ref/rotatingcylinderforceil.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotating Cylinder Force (IL)

## 端口

### 守恒端口

### **X** — 液体密度端口，等温液体

与流体密度关联的液体端口。没有质量流量通过端口 **X**。将端口 **X** 连接到 Single-Acting Actuator (IL) 或 Translational Mechanical Converter (IL) 模块的端口 **A**。

### **C** — 缸体机械平动

与缸体参考速度和力关联的机械平动守恒端口。

### **R** — 活塞机械平动

与活塞速度和由压差引起的力关联的机械平动守恒端口。
### 输入

### **W** — 角速度，rad/s，物理信号

角速度，单位为 rad/s，指定为物理信号。

## 参数

### **Piston outer radius** — 活塞外半径 `0.1` m（默认）| 正标量

活塞外半径。

### **Piston inner radius** — 活塞内半径 `0.05` m（默认）| 正标量

活塞内半径。

### **Fluid entry radius** — 流体通道半径 `0.06` m（默认）| 正标量

缸体中流体开口的半径，从旋转轴测量。该值必须大于或等于 **Piston inner radius** 且小于或等于 **Piston outer radius**。

### **Actuator mechanical orientation** — 活塞位移方向 `Pressure at A causes positive displacement of R relative to C`（默认）| `Pressure at A causes negative displacement of R relative to C`

所连接执行器模块的活塞位移方向。`Pressure at A causes positive displacement of R relative to C` 对应于当 **R** – **C** 为正时的正位移，即执行器轴伸出。`Pressure at A causes negative displacement of R relative to C` 对应于当 **R** – **C** 为正时的负位移，即执行器轴缩回。

## 所属库

Simscape / Fluids / Isothermal Liquid / Actuators / Auxiliary Components

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体系统中组件的向心压力梯度

Rotating Cylinder Force (IL) 模块对旋转轴绕其对称轴因向心压力梯度产生的轴向力进行建模，该模型适用于摩擦离合器、方牙正离合器、犬牙离合器和制动器等应用。将此模块与 Single-Acting Actuator (IL) 或 Translational Mechanical Converter (IL) 模块并联连接，以对旋转执行器进行建模。流体密度在等温液体端口 **X** 处记录。角速度作为物理信号在端口 **W** 处接收。端口 **R** 与活塞速度关联，相对于端口 **C** 处的壳体。

假设轴的角速度恒定或近似恒定，因此流体被视为处于刚体旋转状态。

向心力完全由轴旋转引起的流体角动量产生。去除流体通道中静压力的贡献后，轴旋转对轴向力的贡献为：

Frotational=ρπW24(ro4−ri4−2rp2(ro2−ri2)),

其中：

- *ρ* 是端口 **X** 处的流体密度。
- *W* 是旋转管的角速度，作为物理信号在端口 **W** 处接收。
- *r*o 是 **Piston outer radius**。
- *r*i 是 **Piston inner radius**。
- *r*p 是 **Fluid entry radius**。
