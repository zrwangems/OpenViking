---
type: simulink-block
title: 'Translational Mechanical Converter (IL)'
family: 'isothermal-liquid'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Elements'
documentation_page: 'translationalmechanicalconverteril'
documentation_source_path: 'ref/translationalmechanicalconverteril.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Mechanical Converter (IL)

## 端口

### 输入

### **p** — 端口 R 相对于端口 C 的位移，m physical signal

输入物理信号，用于从 Simscape™ Multibody™ 关节传递位置信息。将此端口连接到关节的位置感测端口 **p**。有关详细信息，请参阅将 Simscape 网络连接到 Simscape Multibody 关节。

#### 依赖关系

要启用此端口，请将 **接口位移** 参数设置为 `Provide input signal from Multibody joint`。

### 守恒

### **A** — 转换器入口等温液体

与转换器入口关联的等温液体守恒端口。

### **R** — 杆机械平移

与移动接口关联的机械平移守恒端口。

### **C** — 壳体机械平移

与转换器外壳关联的机械平移守恒端口。

## 参数

### **机械方向** — 选择转换器方向 `Pressure at A causes positive displacement of R relative to C`（默认）| `Pressure at A causes negative displacement of R relative to C`

选择移动接口相对于流体压力的对齐方式：

- `Pressure at A causes positive displacement of R relative to C` — 流体压力增加会导致端口 **R** 相对于端口 **C** 产生正位移。
- `Pressure at A causes negative displacement of R relative to C` — 流体压力增加会导致端口 **R** 相对于端口 **C** 产生负位移。

### **接口位移** — 选择确定相对端口位置的方法 `Calculate from velocity of port R relative to port C`（默认）| `Provide input signal from Multibody joint`

选择确定端口 **R** 相对于端口 **C** 位移的方法：

- `Calculate from velocity of port R relative to port C` — 根据质量平衡方程，由相对端口速度计算位移。这是默认方法。
- `Provide input signal from Multibody joint` — 启用输入物理信号端口 **p**，以传递来自 Multibody 关节的位移信息。仅当使用 Translational Multibody Interface 模块将转换器连接到 Multibody 关节时，才使用此方法。有关详细信息，请参阅如何传递位置信息。

### **初始接口位移** — 仿真开始时端口 R 相对于端口 C 的平移偏移 `0 m`（默认）| scalar

仿真开始时端口 **R** 相对于端口 **C** 的平移偏移。值 0 对应于初始液体体积等于 **死区体积**。

#### 依赖关系

当 **接口位移** 参数设置为 `Calculate from velocity of port R relative to port C` 时启用。

- 如果 **机械方向** 为 `Pressure at A causes positive displacement of R relative to C`，则参数值必须大于或等于 0。
- 如果 **机械方向** 为 `Pressure at A causes negative displacement of R relative to C`，则参数值必须小于或等于 0。

### **接口横截面积** — 液体施加压力以产生平移力的面积 `0.01 m^2`（默认）| positive scalar

液体施加压力以产生平移力的面积。

### **死区体积** — 接口位移为 0 时的液体体积 `1e-5 m^3`（默认）| positive scalar

接口位移为 0 时的液体体积。

### **环境压力规格** — 选择环境压力的规格方法 `Atmospheric pressure`（默认）| `Specified pressure`

选择转换器外部压力的规格方法：

- `Atmospheric pressure` — 使用由连接到回路的 Isothermal Liquid Properties (IL) 模块指定的大气压。
- `Specified pressure` — 使用 **环境压力** 参数指定值。

### **环境压力** — 转换器外部压力 `0.101325 MPa`（默认）| positive scalar

转换器外部作用在转换器液体体积压力上的压力。值 0 表示转换器向真空膨胀。

#### 依赖关系

当 **环境压力规格** 参数设置为 `Specified pressure` 时启用。

### **启用动态可压缩性** — 选择是否对流体动态可压缩性建模 `On`（默认）| `Off`

选择是否考虑液体的动态可压缩性。动态可压缩性使液体密度依赖于压力和温度，从而影响系统在小时间尺度上的瞬态响应。

### **初始液体压力** — 时间零点的液体压力 `0.101325 MPa`（默认）| positive scalar

仿真开始时转换器中的液体压力。

#### 依赖关系

要启用此参数，请选中 **启用动态可压缩性** 复选框。

### **标称液体压力** — 标称工作条件下的液体压力 `0.101325 MPa`（默认）

标称工作条件下的热液体压力。当禁用动态可压缩性时，该模块使用此值计算质量守恒方程中使用的标称密度。

#### 依赖关系

要启用此参数，请清除 **启用动态可压缩性** 复选框。

## 所属库

Simscape / Foundation Library / Isothermal Liquid / Elements

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体网络与机械平移网络之间的接口

Translational Mechanical Converter (IL) 模块对等温液体网络与机械平移网络之间的接口进行建模。该模块将等温液体压力转换为机械力，反之亦然。它可用作线性执行器的构建块。

转换器包含可变体积的液体。如果选中 **启用动态可压缩性** 复选框，则压力根据液体体积的动态可压缩性演变。**机械方向** 参数允许您指定压力增加使端口 **R** 远离还是移向端口 **C**。

端口 **A** 是与转换器入口关联的等温液体守恒端口。端口 **R** 和 **C** 分别是与移动接口和转换器外壳关联的机械平移守恒端口。

### 质量平衡

机械转换器体积中的质量守恒方程为

m˙A={ε ρIS v,if fluid dynamic compressibility is offε ρIS v+1βIdpIdtρIV,if fluid dynamic compressibility is onv=dxdtv=vR−vCV=Vdead+εSx

其中：

- m˙A 是进入转换器通过端口 **A** 的质量流量。
- *ε* 是转换器的机械方向（如果流体压力增加导致 R 相对于 C 产生正位移，则为 `1`；如果流体压力增加导致 R 相对于 C 产生负位移，则为 `-1`）。
- *ρ*I 是转换器内部的流体密度。
- *β*I 是转换器内部的流体体积模量。
- *S* 是转换器接口的横截面积。
- *v* 是转换器接口的平移速度。
- *v*R 和 *v*C 分别是端口 **R** 和 **C** 的平移速度。
- *x* 是转换器接口的位移。
- *V* 是转换器内部的液体体积。
- *V*dead 是死区体积，即接口位移为 0 时的液体体积。
- *p*I 是转换器内部的压力。

如果将转换器连接到 Multibody 关节，请使用物理信号输入端口 **p** 指定端口 **R** 相对于端口 **C** 的位移。否则，该模块根据上述方程，由相对端口速度计算接口位移。当液体体积等于死区体积时，接口位移为零。然后，根据 **机械方向** 参数值：

- 如果为 `Pressure at A causes positive displacement of R relative to C`，则当液体体积从死区体积增加时，接口位移增加。
- 如果为 `Pressure at A causes negative displacement of R relative to C`，则当液体体积从死区体积增加时，接口位移减小。

用于计算流体混合物密度和体积模量的方程取决于所选的等温液体模型。有关详细信息，请参阅等温液体建模选项。

### 动量平衡

机械转换器体积中的动量守恒方程为

F=ε(penv−p)S,

其中：

- *F* 是液体施加在转换器接口上的力。
- *p*env 是转换器外部的环境压力。

### 假设与限制

- 转换器壁完全刚性。
- 转换器不包含机械硬限位。要包括硬限位，请使用 Translational Hard Stop 模块。
- 入口与转换器内部之间的流动阻力可忽略不计。
- 转换器内流体的动能可忽略不计。
