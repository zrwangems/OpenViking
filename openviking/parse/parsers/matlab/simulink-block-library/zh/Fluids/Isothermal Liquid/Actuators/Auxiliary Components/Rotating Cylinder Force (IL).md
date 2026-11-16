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

### 守恒

### **X** — 液体密度端口（等温液体）

与流体密度关联的液体端口。通过端口 **X** 没有质量流量。将端口 **X** 连接到 Single-Acting Actuator (IL) 或 Translational Mechanical Converter (IL) 模块的端口 **A**。

### **C** — 缸体机械平移

与缸体参考速度和力关联的机械平移守恒端口。

### **R** — 活塞机械平移

与由压差引起的活塞速度和力关联的机械平移守恒端口。

### 输入

### **W** — 角速度，rad/s 物理信号

以 rad/s 为单位的角速度，指定为物理信号。

## 参数

### **Piston outer radius** — Piston outer radius `0.1` m (默认) | positive scalar

活塞外半径。

### **Piston inner radius** — Piston inner radius `0.05` m (默认) | positive scalar

活塞内半径。

### **Fluid entry radius** — Fluid channel radius `0.06` m (默认) | positive scalar

缸体中流体开口的半径，从旋转轴测量。此值必须大于或等于 **Piston inner radius**，且小于或等于 **Piston outer radius**。

### **Actuator mechanical orientation** — Piston displacement direction `Pressure at A causes positive displacement of R relative to C` (默认) | `Pressure at A causes negative displacement of R relative to C`

所连接执行器模块的活塞位移方向。当 **R** – **C** 为正时，`Pressure at A causes positive displacement of R relative to C` 对应于正位移，即执行器轴伸出。当 **R** – **C** 为正时，`Pressure at A causes negative displacement of R relative to C` 对应于负位移，即执行器轴回缩。

## 所属库

Simscape / Fluids / Isothermal Liquid / Actuators / Auxiliary Components

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体系统中组件的离心压力梯度

Rotating Cylinder Force (IL) 模块对旋转轴绕其对称轴因离心压力梯度产生的轴向力进行建模，此类应用包括摩擦离合器、方形爪式正离合器、犬牙离合器和制动器。将此模块与 Single-Acting Actuator (IL) 或 Translational Mechanical Converter (IL) 模块并联，以对旋转执行器进行建模。流体密度记录在等温液体端口 **X** 处。角速度作为物理信号在端口 **W** 处接收。端口 **R** 与活塞速度关联，该速度相对于端口 **C** 处的壳体。

轴的角速度假定为恒定或近似恒定，因此流体被视为处于刚体旋转。

离心力完全由轴旋转引起的流体角动量产生。除去流体通道中静压的贡献后，轴的旋转对轴向力的贡献为：

Frotational=ρπW24(ro4−ri4−2rp2(ro2−ri2)),

其中：

- *ρ* 是端口 **X** 处的流体密度。
- *W* 是旋转管道的角速度，作为物理信号在端口 **W** 处接收。
- *r*o 是 **Piston outer radius**。
- *r*i 是 **Piston inner radius**。
- *r*p 是 **Fluid entry radius**。
