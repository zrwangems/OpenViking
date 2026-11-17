---
type: simulink-block
title: 'Three-Winding Nonlinear Transformer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Transformers'
documentation_page: 'threewindingnonlineartransformer'
documentation_source_path: 'ref/threewindingnonlineartransformer.html'
language: zh-CN
chinese_source: worker-translation
---

# Three-Winding Nonlinear Transformer

## 端口
```yaml
ports:
- name: 1+
  summary: 线路 1 正极端子电气端口
  direction: conserving
- name: 1-
  summary: 线路 1 负极端子电气端口
  direction: conserving
- name: 2+
  summary: 线路 2 正极端子电气端口
  direction: conserving
- name: 2-
  summary: 线路 2 负极端子电气端口
  direction: conserving
- name: 3+
  summary: 线路 3 正极端子电气端口
  direction: conserving
- name: 3-
  summary: 线路 3 负极端子电气端口
  direction: conserving
```

### 守恒端口

### **1+** — 线路 1 正极端子电气端口

与线路 1 正极端子关联的电气守恒端口。

### **1-** — 线路 1 负极端子电气端口

与线路 1 负极端子关联的电气守恒端口。

### **2+** — 线路 2 正极端子电气端口

与线路 2 正极端子关联的电气守恒端口。

### **2-** — 线路 2 负极端子电气端口

与线路 2 负极端子关联的电气守恒端口。

### **3+** — 线路 3 正极端子电气端口

与线路 3 正极端子关联的电气守恒端口。

### **3-** — 线路 3 负极端子电气端口

与线路 3 负极端子关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Primary number of turns
  summary: 绕组 1 一次侧匝数 100（默认）| 正标量整数
  group: 主回路
- name: First secondary number of turns
  summary: 绕组 2 匝数 200（默认）| 正标量整数
  group: 主回路
- name: Second secondary number of turns
  summary: 绕组 3 匝数 200（默认）| 正标量整数
  group: 主回路
- name: Primary winding resistance
  summary: 绕组 1 电阻 0.01 Ohm（默认）| 非负标量
  group: 主回路
- name: Primary leakage inductance
  summary: 绕组 1 漏电感 0.0001 H（默认）| 非负标量
  group: 主回路
- name: First secondary winding resistance
  summary: 绕组 2 电阻 0.01 Ohm（默认）| 非负标量
  group: 主回路
- name: First secondary leakage inductance
  summary: 绕组 2 漏电感 0.0001 H（默认）| 非负标量
  group: 主回路
- name: Second secondary winding resistance
  summary: 绕组 3 电阻 0.01 Ohm（默认）| 非负标量
  group: 主回路
- name: Second secondary leakage inductance
  summary: 绕组 3 漏电感 0.0001 H（默认）| 非负标量
  group: 主回路
- name: Magnetization resistance
  summary: 磁化电阻 100 Ohm（默认）
  group: 磁化
- name: Magnetization inductance parameterized by
  summary: 非线性磁化电感参数化方式 Single saturation point（默认）| Single inductance (linear) | Magnetic flux versus current characteristic
    | Magnetic flux density versus field strength characteristic | Magnetic flux density versus field strength characteristic
    with hysteresis
  group: 磁化
- name: Unsaturated inductance
  summary: 未饱和电感 4e-2 H（默认）
  group: 磁化
- name: Saturated inductance
  summary: 饱和电感 1e-2 H（默认）
  group: 磁化
- name: Saturation magnetic flux
  summary: 饱和磁通 1.6e-04 Wb（默认）
  group: 磁化
- name: Current vector, i
  summary: 电流数据 [0, .4, .8, 1.2, 1.6, 2] A（默认）
  group: 磁化
- name: Magnetic flux vector, phi
  summary: 磁通向量 [0, .161, .25, .284, .295, .299] .* 1e-3 Wb（默认）
  group: 磁化
- name: Magnetic field strength vector, H
  summary: 磁场强度向量 [0, 200, 400, 600, 800, 1000] A/m（默认）| 向量
  group: 磁化
- name: Magnetic flux density vector, B
  summary: 磁通密度向量 [0, .81, 1.25, 1.42, 1.48, 1.49] T（默认）| 向量
  group: 磁化
- name: Effective length
  summary: 有效铁芯长度 0.2 m（默认）| 正有限标量
  group: 磁化
- name: Effective cross-sectional area
  summary: 有效铁芯横截面积 2e-4 m^2（默认）| 正有限标量
  group: 磁化
- name: Anhysteretic B-H gradient when H is zero
  summary: 零磁场强度附近无磁滞 B-H 曲线梯度 0.005 m*T/A（默认）| 标量
  group: 磁化
- name: Flux density point on anhysteretic B-H curve
  summary: 无磁滞 B-H 曲线上的磁通密度点 1.49 T（默认）| 标量
  group: 磁化
- name: Corresponding field strength
  summary: 测量点处的磁场强度 1000 A/m（默认）| 标量
  group: 磁化
- name: Coefficient for reversible magnetization, c
  summary: 可逆磁化系数 0.1（默认）| 范围 [0,1] 内的标量
  group: 磁化
- name: Bulk coupling coefficient, K
  summary: 体耦合系数 200 A/m（默认）| 有限正标量
  group: 磁化
- name: Inter-domain coupling factor, alpha
  summary: 域间耦合因子 1e-4（默认）| 标量
  group: 磁化
- name: Interpolation option
  summary: 插值选项 Linear（默认）| Smooth
  group: 磁化
- name: Primary leakage inductance initial current
  summary: 一次漏电感初始电流 0 A（默认）
  group: 初始条件
- name: First secondary leakage inductance initial current
  summary: 第一个二次漏电感初始电流 0 A（默认）
  group: 初始条件
- name: Second secondary leakage inductance initial current
  summary: 第二个二次漏电感初始电流 0 A（默认）
  group: 初始条件
- name: Specify magnetization inductance initial state by
  summary: 初始状态指定选项 Current（默认）| Magnetic flux
  group: 初始条件
- name: Magnetization inductance initial current
  summary: 磁化电感初始电流 0 A（默认）
  group: 初始条件
- name: Magnetization inductance initial magnetic flux
  summary: 磁化电感初始磁通 0 Wb（默认）
  group: 初始条件
- name: Magnetization inductance initial magnetic flux density
  summary: 磁化电感初始磁通密度 0 T（默认）
  group: 初始条件
- name: Magnetization inductance initial field strength
  summary: 磁化电感初始磁场强度 0 A/m（默认）
  group: 初始条件
- name: Primary leakage inductance parasitic parallel conductance
  summary: 绕组 1 漏电感寄生并联电导 1e-9 1/Ohm（默认）| 非负标量
  group: 寄生效应
- name: First secondary leakage inductance parasitic parallel conductance
  summary: 绕组 2 漏电感寄生并联电导 1e-9 1/Ohm（默认）| 非负标量
  group: 寄生效应
- name: Second secondary leakage inductance parasitic parallel conductance
  summary: 绕组 3 漏电感寄生并联电导 1e-9 1/Ohm（默认）| 非负标量
  group: 寄生效应
```

### 主回路

### **Primary number of turns** — 绕组 1 一次侧匝数 `100`（默认）| 正标量整数

变压器第一个一次绕组的导线匝数。

### **First secondary number of turns** — 绕组 2 匝数 `200`（默认）| 正标量整数

变压器第一个二次绕组的导线匝数。

### **Second secondary number of turns** — 绕组 3 匝数 `200`（默认）| 正标量整数

变压器第二个二次绕组的导线匝数。

### **Primary winding resistance** — 绕组 1 电阻 `0.01` `Ohm`（默认）| 非负标量

*R1* 的电阻，表示一次绕组的功率损耗。

### **Primary leakage inductance** — 绕组 1 漏电感 `0.0001` `H`（默认）| 非负标量

*L1* 的电感，表示一次绕组的磁通损耗。

### **First secondary winding resistance** — 绕组 2 电阻 `0.01` `Ohm`（默认）| 非负标量

*R2* 的电阻，表示第一个二次绕组的功率损耗。

### **First secondary leakage inductance** — 绕组 2 漏电感 `0.0001` `H`（默认）| 非负标量

*L2* 的电感，表示第一个二次绕组的磁通损耗。

### **Second secondary winding resistance** — 绕组 3 电阻 `0.01` `Ohm`（默认）| 非负标量

*R3* 的电阻，表示第二个二次绕组的功率损耗。

### **Second secondary leakage inductance** — 绕组 3 漏电感 `0.0001` `H`（默认）| 非负标量

*L3* 的电感，表示第二个二次绕组的磁通损耗。

### 磁化

### **Magnetization resistance** — 磁化电阻 `100` `Ohm`（默认）

*Rm* 的电阻，表示变压器铁芯中的磁损耗。

### **Magnetization inductance parameterized by** — 非线性磁化电感参数化方式 `Single saturation point`（默认）| `Single inductance (linear)` | `Magnetic flux versus current characteristic` | `Magnetic flux density versus field strength characteristic` | `Magnetic flux density versus field strength characteristic with hysteresis`

非线性磁化电感的参数化方法：

- `Single inductance (linear)`
  — 提供未饱和电感值。
- `Single saturation point`
  — 提供未饱和电感值和饱和电感值，以及饱和磁通。
- `Magnetic flux versus current
  characteristic` — 提供电流向量和磁通向量，然后填充磁通对电流查找表。
- `Magnetic flux density versus field strength
  characteristic` — 提供有效铁芯长度、横截面积、磁场强度向量和磁通密度向量的值，然后填充磁通密度对磁场强度查找表。
- `Magnetic flux density versus field strength
  characteristic with hysteresis` —
  通过提供匝数、有效铁芯长度和横截面积、初始无磁滞 B-H 曲线梯度、B-H 曲线上某点的磁通密度和磁场强度、可逆磁化系数、体耦合系数以及域间耦合因子，将磁通密度定义为电流值和磁场强度历史的函数。

### **Unsaturated inductance** — 未饱和电感 `4e-2` `H`（默认）

磁化电感 *Lm* 在其线性区域工作时的电感。

#### 依赖关系

要启用此参数，请将 **Magnetization inductance parameterized
by** 参数设置为 `Single inductance
(linear)` 或 `Single saturation
point`。

### **Saturated inductance** — 饱和电感 `1e-2` `H`（默认）

磁化电感 *Lm* 超过其饱和点工作时的电感。

#### 依赖关系

要启用此参数，请将 **Magnetization
inductance parameterized by** 参数设置为
`Single saturation point`。

### **Saturation magnetic flux** — 饱和磁通 `1.6e-04` `Wb`（默认）

磁化电感 *Lm* 饱和时的磁通。

#### 依赖关系

要启用此参数，请将 **Magnetization
inductance parameterized by** 参数设置为
`Single saturation point`。

### **Current vector, i** — 电流数据 `[0, .4, .8, 1.2, 1.6, 2]` `A`（默认）

模块用于填充磁通对电流查找表的电流数据。

#### 依赖关系

要启用此参数，请将 **Magnetization
inductance parameterized by** 参数设置为
`Magnetic flux versus current
characteristic`。

### **Magnetic flux vector, phi** — 磁通向量 `[0, .161, .25, .284, .295, .299] .* 1e-3` `Wb`（默认）

模块用于填充磁通对电流查找表的磁通数据。

#### 依赖关系

要启用此参数，请将 **Magnetization
inductance parameterized by** 参数设置为
`Magnetic flux versus current
characteristic`。

### **Magnetic field strength vector, H** — 磁场强度向量 `[0, 200, 400, 600, 800, 1000]` `A/m`（默认）| 向量

磁场强度 *H*，指定为与磁通密度向量 *B* 具有相同元素数量的向量。

#### 依赖关系

要启用此参数，请将 **Magnetization
inductance parameterized by** 参数设置为
`Magnetic flux density versus field strength
characteristic`。

### **Magnetic flux density vector, B** — 磁通密度向量 `[0, .81, 1.25, 1.42, 1.48, 1.49]` `T`（默认）| 向量

磁通密度 *B*，指定为与磁场强度向量 *H* 具有相同元素数量的向量。

#### 依赖关系

要启用此参数，请将 **Magnetization
inductance parameterized by** 参数设置为
`Magnetic flux density versus field strength
characteristic`。

### **Effective length** — 有效铁芯长度 `0.2` `m`（默认）| 正有限标量

有效铁芯长度。此参数表示铁芯周围磁路的平均长度。

#### 依赖关系

要启用此参数，请将 **Magnetization inductance parameterized
by** 参数设置为 `Magnetic flux density versus field
strength characteristic` 或 `Magnetic flux density
versus field strength characteristic with hysteresis`。

### **Effective cross-sectional area** — 有效铁芯横截面积 `2e-4` `m^2`（默认）| 正有限标量

有效铁芯横截面积。此参数表示铁芯周围磁路的平均面积。

#### 依赖关系

要启用此参数，请将
**Magnetization inductance parameterized
by** 参数设置为 `Magnetic
flux density versus field strength
characteristic` 或
`Magnetic flux density versus field
strength characteristic with
hysteresis`。

### **Anhysteretic B-H gradient when H is zero** — 零磁场强度附近无磁滞 B-H 曲线梯度 `0.005` `m*T/A`（默认）| 标量

零磁场强度附近无磁滞 *B*-*H* 曲线的梯度。将此参数设置为上升和下降磁滞曲线的平均梯度。

#### 依赖关系

要启用此参数，请将 **Magnetization inductance parameterized
by** 参数设置为 `Magnetic flux density versus field
strength characteristic with hysteresis`。

### **Flux density point on anhysteretic B-H curve** — 无磁滞 B-H 曲线上的磁通密度点 `1.49` `T`（默认）| 标量

用于磁场强度测量的点的磁通密度。您必须通过提供磁通密度值来指定无磁滞曲线上的一个点。为获得准确结果，请选择高磁场强度处上升和下降磁滞曲线重合的点。

#### 依赖关系

要启用此参数，请将 **Magnetization inductance parameterized by** 参数设置为 `Magnetic flux density versus field strength characteristic with hysteresis`。

### **Corresponding field strength** — 测量点处的磁场强度 `1000` `A/m`（默认）| 标量

与您使用 **Flux density
point on anhysteretic B-H curve** 参数定义的点相对应的磁场强度。

#### 依赖关系

要启用此参数，请将 **Magnetization inductance parameterized by** 设置为 `Magnetic flux density versus field strength characteristic with hysteresis`。

### **Coefficient for reversible magnetization, c** — 可逆磁化系数 `0.1`（默认）| 范围 [0,1] 内的标量

Jiles-Atherton 方程中的可逆磁化系数 *c*。此参数表示可以可逆的磁化比例。

#### 依赖关系

要启用此参数，请将 **Magnetization
inductance parameterized by** 设置为
`Magnetic flux density versus magnetic
field strength characteristic with
hysteresis`。

### **Bulk coupling coefficient, K** — 体耦合系数 `200` `A/m`（默认）| 有限正标量

Jiles-Atherton 方程中的体耦合系数 *K*。此参数主要控制 *B*-*H* 曲线穿过零磁通密度线时的磁场强度大小。

#### 依赖关系

要启用此参数，请将 **Magnetization inductance parameterized by** 设置为 `Magnetic flux density versus field strength characteristic with hysteresis`。

### **Inter-domain coupling factor, alpha** — 域间耦合因子 `1e-4`（默认）| 标量

Jiles-Atherton 方程中的域间耦合因子 *α*。此参数主要影响 *B*-*H* 曲线与零磁场强度线相交的点。典型值在 `1e-4` 到 `1e-3` 范围内。

#### 依赖关系

要启用此参数，请将 **Magnetization inductance parameterized by** 参数设置为 `Magnetic flux density versus field strength characteristic with hysteresis`。

### **Interpolation option** — 插值选项 `Linear`（默认）| `Smooth`

查找表插值选项。选择以下插值方法之一：

- `Linear` — 选择此选项以获得最佳性能。
- `Smooth` — 生成具有连续一阶导数的连续曲线。

有关插值算法的更多信息，请参阅
PS Lookup Table
(1D) 模块参考页。

#### 依赖关系

要启用此参数，请将 **Magnetization
inductance parameterized by** 参数设置为
`Magnetic flux versus current
characteristic` 或 `Magnetic flux
density versus field strength characteristic`
。

### 初始条件

### **Primary leakage inductance initial current** — 一次漏电感初始电流 `0` `A`（默认）

零时刻流过一次漏电感 *L1* 的电流。

### **First secondary leakage inductance initial current** — 第一个二次漏电感初始电流 `0` `A`（默认）

零时刻流过第一个二次漏电感 *L2* 的电流。

### **Second secondary leakage inductance initial current** — 第二个二次漏电感初始电流 `0` `A`（默认）

零时刻流过第二个二次漏电感 *L3* 的电流。

### **Specify magnetization inductance initial state by** — 初始状态指定选项 `Current`（默认）| `Magnetic flux`

初始状态指定。选择以下选项之一：

- `Current` — 通过初始电流指定磁化电感 *Lm* 的初始状态。
- `Magnetic flux` — 通过磁通指定磁化电感 *Lm* 的初始状态。

#### 依赖关系

要启用此参数，请在
**Magnetization** 设置中，将
**Magnetization inductance parameterized by**
参数设置为：

- `Single inductance
  (linear)`
- `Single saturation
  point`
- `Magnetic flux versus current
  characteristic`
- `Magnetic flux density versus field
  strength characteristic`

### **Magnetization inductance initial current** — 磁化电感初始电流 `0` `A`（默认）

模块用于计算零时刻磁化电感 *Lm* 内磁通的初始电流值。此参数是流过磁化电感 *Lm* 的电流。总磁化电流由流过磁化电阻 *Rm* 的电流和流过磁化电感 *Lm* 的电流组成。

#### 依赖关系

要启用此参数，请将 **Specify magnetization
inductance initial state by** 参数设置为
`Current`

### **Magnetization inductance initial magnetic flux** — 磁化电感初始磁通 `0` `Wb`（默认）

零时刻磁化电感 *Lm* 中的磁通。

#### 依赖关系

要启用此参数，请将 **Specify magnetization
inductance initial state by** 参数设置为
`Magnetic flux`

### **Magnetization inductance initial magnetic flux density** — 磁化电感初始磁通密度 `0` `T`（默认）

零时刻的磁通密度。

#### 依赖关系

要启用此参数，请在
**Magnetization** 设置中，将
**Magnetization inductance parameterized by**
参数设置为 `Magnetic flux density versus field
strength characteristic with hysteresis`

### **Magnetization inductance initial field strength** — 磁化电感初始磁场强度 `0` `A/m`（默认）

零时刻的磁场强度。

#### 依赖关系

要启用此参数，请在
**Magnetization** 设置中，将
**Magnetization inductance parameterized by**
参数设置为 `Magnetic flux density versus field
strength characteristic with hysteresis`

### 寄生效应

### **Primary leakage inductance parasitic parallel conductance** — 绕组 1 漏电感寄生并联电导 `1e-9` `1/Ohm`（默认）| 非负标量

与一次漏电感 *L1* 并联的小寄生效应。要仿真某些电路拓扑，您需要一个小并联电导。

### **First secondary leakage inductance parasitic parallel conductance** — 绕组 2 漏电感寄生并联电导 `1e-9` `1/Ohm`（默认）| 非负标量

与第一个二次漏电感 *L2* 并联的小寄生效应。要仿真某些电路拓扑，您需要一个小并联电导。

### **Second secondary leakage inductance parasitic parallel conductance** — 绕组 3 漏电感寄生并联电导 `1e-9` `1/Ohm`（默认）| 非负标量

与第二个二次漏电感 *L3* 并联的小寄生效应。要仿真某些电路拓扑，您需要一个小并联电导。
## 所属库

Simscape / Electrical / Passive / Transformers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

单相非线性三绕组变压器

三绕组非线性变压器模块表示一个具有非理想铁芯的单相非线性三绕组变压器。铁芯可能因其磁特性或尺寸而非理想。下图展示了等效电路拓扑，

其中：

- *R1* 是一次绕组电阻。
- *L1* 是一次漏电感。
- *R2* 是第一次级绕组电阻。
- *L2* 是第一次级漏电感。
- *R3* 是第二次级绕组电阻。
- *L3* 是第二次级漏电感。
- *Rm* 是磁化电阻。
- *Lm* 是磁化电感。

要参数化非线性磁化电感，请将 **Magnetization inductance parameterized by** 参数设置为以下选项之一：

- `Single inductance (linear)`
- `Single saturation point`
- `Magnetic flux versus current characteristic`
- `Magnetic flux density versus magnetic field strength
  characteristic`
- `Magnetic flux density versus magnetic field strength
  characteristic with hysteresis`

有关这些参数化选项的更多信息，包括模块用于建模非线性磁化电感的方程，请参阅 Nonlinear Inductor 模块参考页。

Simscape™ 和 Simscape Electrical™ 库包含若干可以建模相同类型变压器设备的模块。然而，这些模块做出了不同的建模假设。要为您的应用选择正确的模块，您必须理解这些假设如何影响模块行为随频率的变化。有关更多信息，请参阅 Choose Blocks to Model Transformers。
