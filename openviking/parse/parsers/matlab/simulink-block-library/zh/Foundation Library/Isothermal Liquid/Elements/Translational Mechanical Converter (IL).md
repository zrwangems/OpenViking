---
type: simulink-block
title: 'Translational Mechanical Converter (IL)'
family: 'simscape'
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
```yaml
ports:
- name: p
  summary: 端口 R 相对于端口 C 的位移，m physical signal
  direction: input
- name: A
  summary: 转换器入口等温液体
  direction: input
- name: R
  summary: 杆机械平移
  direction: input
- name: C
  summary: 壳体机械平移
  direction: input
```

### 输入

### **p** — 端口 R 相对于端口 C 的位移，m physical signal

输入物理信号，用于传递来自 Simscape™ Multibody™ 关节的位置信息。将此端口连接到关节的位置传感端口 **p**。有关详细信息，请参阅 Connecting Simscape Networks to Simscape Multibody Joints。

#### 依赖关系

要启用此端口，请将 **Interface displacement** 参数设置为 `Provide input signal from Multibody joint`。

### 守恒

### **A** — 转换器入口等温液体

与转换器入口关联的等温液体守恒端口。

### **R** — 杆机械平移

与运动界面关联的机械平移守恒端口。

### **C** — 壳体机械平移

与转换器壳体关联的机械平移守恒端口。
## 参数
```yaml
parameters:
- name: Mechanical orientation
  summary: 选择转换器方向 Pressure at A causes positive displacement of R relative to C（默认）| Pressure at A causes negative displacement
    of R relative to C
  group: ''
- name: Interface displacement
  summary: 选择确定相对端口位置的方法 Calculate from velocity of port R relative to port C（默认）| Provide input signal from Multibody joint
  group: ''
- name: Initial interface displacement
  summary: 仿真开始时端口 R 相对于端口 C 的平移偏移量 0 m（默认）| 标量
  group: ''
- name: Interface cross-sectional area
  summary: 液体施加压力以产生平移力的面积 0.01 m^2（默认）| 正标量
  group: ''
- name: Dead volume
  summary: 界面位移为 0 时的液体体积 1e-5 m^3（默认）| 正标量
  group: ''
- name: Environment pressure specification
  summary: 选择环境压力 Atmospheric pressure（默认）| Specified pressure 的指定方法
  group: ''
- name: Environment pressure
  summary: 转换器外部压力 0.101325 MPa（默认）| 正标量
  group: ''
- name: Enable dynamic compressibility
  summary: 选择是否对流体动态可压缩性建模 On（默认）| Off
  group: ''
- name: Initial liquid pressure
  summary: 时间为零时的液体压力 0.101325 MPa（默认）| 正标量
  group: ''
- name: Nominal liquid pressure
  summary: 额定工况下的液体压力 0.101325 MPa（默认）
  group: ''
```

### **Mechanical orientation** — 选择转换器方向 `Pressure at A causes positive displacement of R relative to C`（默认）| `Pressure at A causes negative displacement of R relative to C`

选择运动界面相对于流体压力的对齐方式：

- `Pressure at A causes positive displacement of R relative to C` — 流体压力增加导致端口 **R** 相对于端口 **C** 产生正位移。
- `Pressure at A causes negative displacement of R relative to C` — 流体压力增加导致端口 **R** 相对于端口 **C** 产生负位移。

### **Interface displacement** — 选择确定相对端口位置的方法 `Calculate from velocity of port R relative to port C`（默认）| `Provide input signal from Multibody joint`

选择确定端口 **R** 相对于端口 **C** 位移的方法：

- `Calculate from velocity of port R relative to port C` — 基于质量平衡方程，根据相对端口速度计算位移。这是默认方法。
- `Provide input signal from Multibody joint` — 启用输入物理信号端口 **p**，以传递来自 Multibody 关节的位移信息。仅当使用 Translational Multibody Interface 模块将转换器连接到 Multibody 关节时，才使用此方法。有关详细信息，请参阅 How to Pass Position Information。

### **Initial interface displacement** — 仿真开始时端口 R 相对于端口 C 的平移偏移量 `0 m`（默认）| 标量

仿真开始时端口 **R** 相对于端口 **C** 的平移偏移量。值为 0 对应于初始液体体积等于 **Dead volume**。

#### 依赖关系

当 **Interface displacement** 参数设置为 `Calculate from velocity of port R relative to port C` 时启用。

- 如果 **Mechanical orientation** 为 `Pressure at A causes positive displacement of R relative to C`，则参数值必须大于或等于 0。
- 如果 **Mechanical orientation** 为 `Pressure at A causes negative displacement of R relative to C`，则参数值必须小于或等于 0。

### **Interface cross-sectional area** — 液体施加压力以产生平移力的面积 `0.01 m^2`（默认）| 正标量

液体施加压力以产生平移力的面积。

### **Dead volume** — 界面位移为 0 时的液体体积 `1e-5 m^3`（默认）| 正标量

界面位移为 0 时的液体体积。

### **Environment pressure specification** — 选择环境压力 `Atmospheric pressure`（默认）| `Specified pressure` 的指定方法

选择转换器外部压力的指定方法：

- `Atmospheric pressure` — 使用由连接到回路中的 Isothermal Liquid Properties (IL) 模块指定的大气压。
- `Specified pressure` — 使用 **Environment pressure** 参数指定一个值。

### **Environment pressure** — 转换器外部压力 `0.101325 MPa`（默认）| 正标量

作用于转换器液体体积压力之上的转换器外部压力。值为 0 表示转换器向真空膨胀。

#### 依赖关系

当 **Environment pressure specification** 参数设置为 `Specified pressure` 时启用。

### **Enable dynamic compressibility** — 选择是否对流体动态可压缩性建模 `On`（默认）| `Off`

选择是否考虑液体的动态可压缩性。动态可压缩性使液体密度依赖于压力和温度，从而影响系统在小时间尺度上的瞬态响应。

### **Initial liquid pressure** — 时间为零时的液体压力 `0.101325 MPa`（默认）| 正标量

仿真开始时转换器中的液体压力。

#### 依赖关系

要启用此参数，请选中 **Enable dynamic compressibility** 复选框。

### **Nominal liquid pressure** — 额定工况下的液体压力 `0.101325 MPa`（默认）

额定工况下的热液体压力。当动态可压缩性被禁用时，该模块使用此值计算质量守恒方程中使用的额定密度。

#### 依赖关系

要启用此参数，请清除 **Enable dynamic compressibility** 复选框。
## 所属库

Simscape / Foundation Library / Isothermal Liquid / Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

等温液体与机械平移网络之间的接口

Translational Mechanical Converter (IL) 模块对等温液体网络与机械平移网络之间的接口进行建模。该模块将等温液体压力转换为机械力，反之亦然。它可用作线性执行器的构建模块。

该转换器包含可变体积的液体。如果选中 **Enable dynamic compressibility** 复选框，则压力基于液体体积的动态可压缩性演变。**Mechanical orientation** 参数允许您指定压力增加时端口 **R** 是远离还是朝向端口 **C** 移动。

端口 **A** 是与转换器入口相关联的等温液体守恒端口。端口 **R** 和 **C** 分别是与移动接口和转换器外壳相关联的机械平移守恒端口。

### Mass Balance

机械转换器体积内的质量守恒方程为

m˙A={ε ρIS v,if fluid dynamic compressibility is offε ρIS v+1βIdpIdtρIV,if fluid dynamic compressibility is onv=dxdtv=vR−vCV=Vdead+εSx

其中：

- m˙A 是通过端口 **A** 流入转换器的质量流量。
- *ε* 是转换器的机械方向（如果流体压力增加导致 R 相对于 C 产生正位移，则为 `1`；如果流体压力增加导致 R 相对于 C 产生负位移，则为 `-1`）。
- *ρ*I 是转换器内部的流体密度。
- *β*I 是转换器内部的流体体积模量。
- *S* 是转换器界面的横截面积。
- *v* 是转换器界面的平移速度。
- *v*R 和 *v*C 分别是端口 **R** 和 **C** 的平移速度。
- *x* 是转换器界面的位移。
- *V* 是转换器内部的液体体积。
- *V*dead 是死体积，即界面位移为 0 时的液体体积。
- *p*I 是转换器内部的压力。

如果将转换器连接到 Multibody 关节，请使用物理信号输入端口 **p** 来指定端口 **R** 相对于端口 **C** 的位移。否则，模块根据上述方程从相对端口速度计算界面位移。当液体体积等于死体积时，界面位移为零。然后，根据 **Mechanical orientation** 参数值：

- 如果为 `Pressure at A causes positive displacement of R relative to C`，则当液体体积从死体积增加时，界面位移增加。
- 如果为 `Pressure at A causes negative displacement of R relative to C`，则当液体体积从死体积增加时，界面位移减小。

用于计算流体混合物密度和体积模量的方程取决于所选的等温液体模型。有关详细信息，请参阅 Isothermal Liquid Modeling Options。

### Momentum Balance

机械转换器体积内的动量守恒方程为

F=ε(penv−p)S,

其中：

- *F* 是液体施加在转换器界面上的力。
- *p*env 是转换器外部的环境压力。

### 假设和限制

- 转换器壁完全刚性。
- 转换器不包含机械硬限位。要包含硬限位，请使用 Translational Hard Stop 模块。
- 入口与转换器内部之间的流动阻力可忽略不计。
- 转换器中流体的动能可忽略不计。
