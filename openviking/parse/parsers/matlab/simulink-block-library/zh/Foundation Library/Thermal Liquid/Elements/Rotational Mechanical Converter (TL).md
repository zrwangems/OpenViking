---
type: simulink-block
title: 'Rotational Mechanical Converter (TL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal Liquid / Elements'
documentation_page: 'rotationalmechanicalconvertertl'
documentation_source_path: 'ref/rotationalmechanicalconvertertl.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotational Mechanical Converter (TL)

## 端口

### 输入

### **q** — 端口 R 相对于端口 C 的旋转，rad，物理信号

输入物理信号，用于传递来自 Simscape™ Multibody™ 关节的位置信息。将此端口连接到关节的位置传感端口 **q**。有关详细信息，请参阅 Connecting Simscape Networks to Simscape Multibody Joints。

#### 依赖关系

要启用此端口，请将 **Interface rotation** 参数设置为 `Provide input signal from Multibody joint`。

### 守恒

### **A** — 转换器入口热液体

与转换器入口相关联的热液体守恒端口。

### **H** — 转换器内部温度热

与转换器内部液体温度相关联的热守恒端口。

### **R** — 杆机械旋转

与运动界面相关联的机械旋转守恒端口。

### **C** — 壳体机械旋转

与转换器壳体相关联的机械旋转守恒端口。

## 参数

### 主要

### **Mechanical orientation** — 选择转换器方向 `Pressure at A causes positive rotation of R relative to C`（默认）| `Pressure at A causes negative rotation of R relative to C`

选择运动界面相对于转换器液体体积的对齐方式：

- `Pressure at A causes positive rotation of R relative to C` — 液体体积增加导致端口 **R** 相对于端口 **C** 产生正旋转。
- `Pressure at A causes negative rotation of R relative to C` — 液体体积增加导致端口 **R** 相对于端口 **C** 产生负旋转。

### **Interface rotation** — 选择确定相对端口位置的方法 `Calculate from angular velocity of port R relative to port C`（默认）| `Provide input signal from Multibody joint`

选择确定端口 **R** 相对于端口 **C** 旋转的方法：

- `Calculate from angular velocity of port R relative to port C` — 基于模块方程，从相对端口角速度计算旋转。这是默认方法。
- `Provide input signal from Multibody joint` — 启用输入物理信号端口 **q**，以传递来自 Multibody 关节的旋转信息。仅当使用 Rotational Multibody Interface 模块将转换器连接到 Multibody 关节时，才使用此方法。有关详细信息，请参阅 How to Pass Position Information。

### **Initial interface rotation** — 仿真开始时端口 R 相对于端口 C 的旋转偏移 `0 rad`（默认）

仿真开始时端口 **R** 相对于端口 **C** 的旋转偏移。值为 0 对应于初始液体体积等于 **Dead volume**。

#### 依赖关系

当 **Interface rotation** 参数设置为 `Calculate from angular velocity of port R relative to port C` 时启用。

- 如果 **Mechanical orientation** 为 `Pressure at A causes positive rotation of R relative to C`，则参数值必须大于或等于 0。
- 如果 **Mechanical orientation** 为 `Pressure at A causes negative rotation of R relative to C`，则参数值必须小于或等于 0。

### **Interface volume displacement** — 单位旋转的排液体积 `1.2e-4 m^3/rad`（默认）

运动界面单位旋转所排出的液体体积。

### **Dead volume** — 界面旋转为 0 时的液体体积 `1e-5 m^3`（默认）

界面旋转为 0 时的液体体积。

### **Cross-sectional area at port A** — 转换器入口处垂直于流路的面积 `0.01 m^2`（默认）

转换器入口的横截面积，方向垂直于流路。

### **Environment pressure specification** — 选择环境压力 `Atmospheric pressure`（默认）| `Specified pressure` 的指定方法

选择转换器外部压力的指定方法：

- `Atmospheric pressure` — 使用由连接到回路的热液设置（TL）或热液属性（TL）模块指定的大气压。
- `Specified pressure` — 使用 **Environment pressure** 参数指定一个值。

### **Environment pressure** — 转换器外部压力 `0.101325 MPa`（默认）

作用于转换器液体体积压力之上的转换器外部压力。值为 0 表示转换器向真空膨胀。

#### 依赖关系

当 **Environment pressure specification** 参数设置为 `Specified pressure` 时启用。

### 效应和初始条件

### **Enable dynamic compressibility** — 选择是否对流体动态可压缩性建模 `On`（默认）| `Off`

选择是否考虑液体的动态可压缩性。动态可压缩性使液体密度依赖于压力和温度，在小时间尺度上影响系统的瞬态响应。

### **Initial liquid pressure** — 零时刻的液体压力 `0.101325 MPa`（默认）

仿真开始时转换器中的液体压力。

#### 依赖关系

要启用此参数，请选中 **Enable dynamic compressibility** 复选框。

### **Initial liquid temperature** — 零时刻的液体温度 `293.15 K`（默认）

仿真开始时转换器中的液体温度。

### **Nominal liquid pressure** — 标称工况下的液体压力 `0.101325 MPa`（默认）

标称工况下的热液压力。当动态可压缩性禁用时，模块使用此值计算质量和能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

### **Nominal liquid temperature** — 标称工况下的液体温度 `293.15 K`（默认）

标称工况下的热液温度。当动态可压缩性禁用时，模块使用此值计算质量和能量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。

## 所属库

Simscape / Foundation Library / Thermal Liquid / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

热液网络与机械旋转网络之间的接口

Rotational Mechanical Converter (TL) 模块对热液网络与机械旋转网络之间的接口进行建模。该模块将热液压力转换为机械扭矩，反之亦然。它可用作旋转执行器的构建模块。

该转换器包含可变体积的液体。温度基于该体积的热容量演变。如果选中 **Enable dynamic compressibility** 复选框，则压力也基于液体体积的动态可压缩性演变。**Mechanical orientation** 参数允许您指定液体体积的增加是否导致端口 **R** 相对于端口 **C** 的正旋转或负旋转。

端口 **A** 是与转换器入口相关联的热液守恒端口。端口 **H** 是与转换器内部液体温度相关联的热守恒端口。端口 **R** 和 **C** 分别是与移动接口和转换器外壳相关联的机械旋转守恒端口。

### Mass Balance

机械转换器体积内的质量守恒方程为

m˙A=ερDΩ+{0,if fluid dynamic compressibility is offVρ(1βdpdt+αdTdt),if fluid dynamic compressibility is on

其中：

- m˙A 是通过端口 A 流入转换器的液体质量流量。
- *ε* 是转换器的机械方向
  （如果流体压力增加导致 R 相对于 C 正向旋转，则为 `1`；如果流体压力增加导致 R 相对于 C 负向旋转，则为 `-1`）。
- *ρ* 是液体质量密度。
- *D* 是转换器排量。
- *Ω* 是转换器界面的角速度。
- *V* 是转换器内部的液体体积。
- *β* 是转换器内部液体的体积模量。
- *α* 是液体的热膨胀系数。
- *p* 是转换器内部的液体压力。
- *T* 是转换器内部的液体温度。

如果将转换器连接到 Multibody 关节，请使用物理信号输入端口
**q** 来指定端口 **R** 相对于
端口 **C** 的旋转。否则，模块会根据模块方程，由相对端口角速度计算界面旋转。
当液体体积等于死区体积时，界面旋转为零。然后，根据
**Mechanical orientation** 参数值：

- 如果为 `Pressure at A causes positive rotation of R relative to
  C`，则当液体体积从死区体积增加时，界面旋转增加。
- 如果为 `Pressure at A causes negative rotation of R relative to
  C`，则当液体体积从死区体积增加时，界面旋转减小。

### Momentum Balance

机械转换器体积内的动量守恒方程为

τ=−ε(p−pAtm)D，

其中：

- *τ* 是液体施加在转换器
  界面上的扭矩。
- *p*Atm 是大气压力。

### Energy Balance

机械转换器体积内的能量守恒方程为

d(ρuV)dt=ϕA+QH−pDεΩ，

其中：

- *u* 是转换器内液体的内能。
- *ϕ*A 是通过端口 A 进入
  机械转换器体积的总能量流率。
- *Q*H 是进入
  机械转换器体积的热流率。

### 假设和限制

- 转换器壁不可柔顺。无论内部
  压力和温度如何，它们都不能变形。
- 转换器不包含机械硬限位。要包含硬限位，请使用
  Rotational Hard Stop 模块。
- 入口与转换器内部之间的流动阻力
  可忽略不计。
- 热端口与转换器内部之间的热阻
  可忽略不计。
- 转换器内流体的动能可忽略不计。
