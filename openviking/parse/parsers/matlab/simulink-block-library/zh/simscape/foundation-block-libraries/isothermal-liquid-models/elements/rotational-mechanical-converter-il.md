---
type: simulink-block
title: 'Rotational Mechanical Converter (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Isothermal Liquid Models / Elements'
documentation_page: 'rotationalmechanicalconverteril'
documentation_source_path: 'ref/rotationalmechanicalconverteril.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotational Mechanical Converter (IL)

## 端口

### 输入

### **q** — 端口 R 相对于端口 C 的旋转，rad 物理信号

输入物理信号，用于传递来自 Simscape™ Multibody™ 关节的位置信息。将此端口连接到关节的位置传感端口 **q**。有关详细信息，请参阅将 Simscape 网络连接到 Simscape Multibody 关节。

#### 依赖关系

要启用此端口，请将 **Interface rotation** 参数设置为 `Provide input signal from Multibody joint`。

### 守恒

### **A** — 转换器入口等温液体

与转换器入口关联的等温液体守恒端口。

### **R** — 杆机械旋转

与移动界面关联的机械旋转守恒端口。

### **C** — 外壳机械旋转

与转换器外壳关联的机械旋转守恒端口。

## 参数

### **Mechanical orientation** — 选择转换器方向 `Pressure at A causes positive rotation of R relative to C`（默认）| `Pressure at A causes negative rotation of R relative to C`

选择移动界面相对于流体压力的对齐方式：

- `Pressure at A causes positive rotation of R relative to C` — 流体压力增加会导致端口 **R** 相对于端口 **C** 产生正旋转。
- `Pressure at A causes negative rotation of R relative to C` — 流体压力增加会导致端口 **R** 相对于端口 **C** 产生负旋转。

### **Interface rotation** — 选择确定相对端口位置的方法 `Calculate from angular velocity of port R relative to port C`（默认）| `Provide input signal from Multibody joint`

选择确定端口 **R** 相对于端口 **C** 的旋转的方法：

- `Calculate from angular velocity of port R relative to port C` — 基于质量平衡方程，根据相对端口角速度计算旋转。这是默认方法。
- `Provide input signal from Multibody joint` — 启用输入物理信号端口 **q**，以传递来自 Multibody 关节的旋转信息。仅当使用 Rotational Multibody Interface 模块将转换器连接到 Multibody 关节时，才使用此方法。有关详细信息，请参阅如何传递位置信息。

### **Initial interface rotation** — 仿真开始时端口 **R** 相对于端口 **C** 的旋转偏移 `0 rad`（默认）| scalar

仿真开始时端口 **R** 相对于端口 **C** 的旋转偏移。值 0 对应于初始液体体积等于 **Dead volume**。

#### 依赖关系

当 **Interface rotation** 参数设置为 `Calculate from angular velocity of port R relative to port C` 时启用。

- 如果 **Mechanical orientation** 为 `Pressure at A causes positive rotation of R relative to C`，则参数值必须大于或等于 0。
- 如果 **Mechanical orientation** 为 `Pressure at A causes negative rotation of R relative to C`，则参数值必须小于或等于 0。

### **Interface volume displacement** — 每单位旋转所排出的液体体积 `0.001 m^3/rad`（默认）| positive scalar

移动界面每单位旋转所排出的液体体积。

### **Dead volume** — 当界面旋转为 0 时的液体体积 `1e-5 m^3`（默认）| positive scalar

当界面旋转为 0 时的液体体积。

### **Cross-sectional area at port A** — 转换器入口处垂直于流动路径的面积 `0.01 m^2`（默认）| positive scalar

转换器入口的横截面积，方向垂直于流动路径。

### **Environment pressure specification** — 选择环境压力的指定方法 `Atmospheric pressure`（默认）| `Specified pressure`

选择转换器外部压力的指定方法：

- `Atmospheric pressure` — 使用由连接到回路的 Thermal Liquid Settings (TL) 或 Thermal Liquid Properties (TL) 模块指定的大气压。
- `Specified pressure` — 使用 **Environment pressure** 参数指定值。

### **Environment pressure** — 转换器外部的压力 `0.101325 MPa`（默认）| positive scalar

转换器外部压力，抵抗转换器液体体积的压力。值为 0 表示转换器向真空膨胀。

#### 依赖关系

当 **Environment pressure specification** 参数设置为 `Specified pressure` 时启用。

### **Enable dynamic compressibility** — 选择是否对流体动态压缩性建模 `On`（默认）| `Off`

选择是否考虑液体的动态压缩性。动态压缩性使液体密度依赖于压力和温度，从而影响系统在小时间尺度上的瞬态响应。

### **Initial liquid pressure** — 时间为零时的液体压力 `0.101325 MPa`（默认）| positive scalar

仿真开始时转换器中的液体压力。

#### 依赖关系

要启用此参数，请选中 **Enable dynamic compressibility** 复选框。

### **Nominal liquid pressure** — 标称工况下的液体压力 `0.101325 MPa`（默认）

标称工况下的热液体压力。当禁用动态压缩性时，该模块使用此值计算质量守恒方程中要使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

## 所属库

Simscape / Foundation Library / Isothermal Liquid / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2020a 中引入**

## 描述

等温液体与机械旋转网络之间的接口

Rotational Mechanical Converter (IL) 模块对等温液体网络与机械旋转网络之间的接口进行建模。该模块将等温液体压力转换为机械转矩，反之亦然。它可用作旋转执行器的构建模块。

该转换器包含可变体积的液体。如果选中 **Enable dynamic compressibility** 复选框，则压力基于液体体积的动态压缩性演变。**Mechanical orientation** 参数允许您指定液体体积增加是否导致端口 **R** 相对于端口 **C** 产生正旋转或负旋转。

端口 **A** 是与转换器入口关联的等温液体守恒端口。端口 **R** 和 **C** 分别是与移动界面和转换器外壳关联的机械旋转守恒端口。

### 质量平衡

机械转换器体积中的质量守恒方程为

m˙A={ε ρID ω,if fluid dynamic compressibility is offε ρID ω+1βIdpIdtρIV,if fluid dynamic compressibility is onω=dθdtω=ωR−ωCV=Vdead+εDθ

其中：

- m˙A 是通过端口 **A** 进入转换器的质量流量。
- *ε* 是转换器的机械方向（如果流体压力增加导致 R 相对于 C 产生正旋转，则为 `1`；如果流体压力增加导致 R 相对于 C 产生负旋转，则为 `-1`）。
- *ρ*I 是转换器内部的流体密度。
- *β*I 是转换器内部的流体体积模量。
- *D* 是转换器体积排量，即使轴每旋转单位角度所需的流体体积。
- *ω* 是转换器界面的角速度。
- *ω*R 和 *ω*C 分别是端口 **R** 和 **C** 的角速度。
- *θ* 是转换器界面旋转。
- *V* 是转换器内部的液体体积。
- *V*dead 是死区体积，即界面旋转为 0 时的液体体积。
- *p*I 是转换器内部的压力。

如果将转换器连接到 Multibody 关节，请使用物理信号输入端口 **q** 指定端口 **R** 相对于端口 **C** 的旋转。否则，该模块根据上述方程从相对端口角速度计算界面旋转。当液体体积等于死区体积时，界面旋转为零。然后，根据 **Mechanical orientation** 参数值：

- 如果 `Pressure at A causes positive rotation of R relative to C`，则当液体体积从死区体积增加时，界面旋转增加。
- 如果 `Pressure at A causes negative rotation of R relative to C`，则当液体体积从死区体积增加时，界面旋转减小。

用于计算流体混合物密度和体积模量的方程取决于所选的等温液体模型。有关详细信息，请参阅等温液体建模选项。

### 动量平衡

机械转换器体积中的动量守恒方程为

τ=ε(penv−p)D,

其中：

- *τ* 是液体施加在转换器界面上的转矩。
- *p*env 是转换器外部的环境压力。

### 假设和限制

- 转换器壁完全刚性。
- 转换器不包含机械硬限位。要包含硬限位，请使用 Rotational Hard Stop 模块。
- 入口与转换器内部之间的流动阻力可忽略不计。
- 转换器中流体的动能可忽略不计。
