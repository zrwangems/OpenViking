---
type: simulink-block
title: 'Nonlinear Transformer'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Transformers'
documentation_page: 'nonlineartransformer'
documentation_source_path: 'ref/nonlineartransformer.html'
language: zh-CN
chinese_source: worker-translation
---

# Nonlinear Transformer

## 端口

### 守恒端口

### **1+** — 一次绕组正极性电气

与一次绕组正极性关联的电气守恒端口。

### **1-** — 一次绕组负极性电气

与一次绕组负极性关联的电气守恒端口。

### **2+** — 二次绕组正极性电气

与二次绕组正极性关联的电气守恒端口。

### **2-** — 二次绕组负极性电气

与二次绕组负极性关联的电气守恒端口。

## 参数

### 主回路

### **Primary number of turns** — 一次绕组匝数 `100`（默认）

变压器一次绕组的导线匝数。

### **Secondary number of turns** — 二次绕组匝数 `200`（默认）

变压器二次绕组的导线匝数。

### **Winding parameterized by** — 绕组漏感参数化方式 `Combined primary and secondary values`（默认）| `Separate primary and secondary values`

绕组漏感的参数化选项。选择以下方法之一：

- `Combined primary and secondary values` —
  使用集总电阻和电感值来表示一次和二次绕组中的合并漏感。
- `Separate primary and secondary values` —
  使用单独的电阻和电感来表示一次和二次绕组中的漏感。

### **Combined winding resistance** — 合并绕组电阻 `0.01` `Ohm`（默认）

集总等效电阻 *Req*，表示一次和二次绕组的合并功率损耗。

#### 依赖关系

要启用此参数，请将 **Winding parameterized by** 设置为
`Combined 主值和次值`。

### **Combined leakage inductance** — 合并漏感 `0.0001` `H`（默认）

集总等效电感 *Leq*，表示一次和二次绕组的合并磁通损耗。

#### 依赖关系

要启用此参数，请将 **Winding parameterized by** 设置为
`Combined 主值和次值`。

### **Primary winding resistance** — 一次绕组电阻 `0.01` `Ohm`（默认）

电阻 *R1*，表示一次绕组的功率损耗。

#### 依赖关系

要启用此参数，请将 **Winding parameterized by** 设置为
`Separate 主值和次值`。

### **Primary leakage inductance** — 一次漏感 `0.0001` `H`（默认）

电感 *L1*，表示一次绕组的磁通损耗。

#### 依赖关系

要启用此参数，请将 **Winding parameterized by** 设置为
`Separate 主值和次值`。

### **Secondary winding resistance** — 二次绕组电阻 `0.01` `Ohm`（默认）

电阻 *R2*，表示二次绕组的功率损耗。

#### 依赖关系

要启用此参数，请将 **Winding parameterized by** 设置为
`Separate 主值和次值`。

### **Secondary leakage inductance** — 二次漏感 `0.0001` `H`（默认）

电感 *L2*，表示二次绕组的磁通损耗。

#### 依赖关系

要启用此参数，请将 **Winding parameterized by** 设置为
`Separate 主值和次值`。

### **Averaging period for power logging** — 功率记录平均周期 `0` `s`（默认）

功率记录的平均周期。

### 磁化

### **Magnetization resistance** — 磁化电阻 `100` `Ohm`（默认）

电阻 *Rm*，表示变压器铁芯中的磁损耗。

### **Magnetization inductance parameterized by** — 非线性磁化电感参数化方式 `Single saturation point`（默认）| `Single inductance (linear)` | `Magnetic flux versus current characteristic` | `Magnetic flux density versus field strength characteristic` | `Magnetic flux density versus field strength characteristic with hysteresis`

选择以下非线性磁化电感参数化方法之一：

- `Single inductance (linear)` — 提供
  未饱和电感值。
- `Single saturation point` — 提供
  未饱和和饱和电感值，以及饱和
  磁通。
- `Magnetic flux versus current characteristic`
  — 提供电流向量和磁通向量，以填充
  磁通对电流查找表。
- `Magnetic flux density versus field strength
  characteristic` — 提供有效铁芯
  长度和横截面积值，以及磁场强度向量
  和磁通密度向量，以填充磁通密度
  对磁场强度查找表。
- `Magnetic flux density versus field strength characteristic with
  hysteresis` — 除了匝数和
  有效铁芯长度及横截面积外，提供
  初始无磁滞 *B*-*H* 曲线梯度值、
  *B*-*H* 曲线上某点的磁通密度和磁场强度，
  以及可逆磁化系数、体耦合系数和域间
  耦合因子，以将磁通密度定义为
  电流值和磁场强度历史的函数。

### **Unsaturated inductance** — 未饱和电感 `4e-2` `H`（默认）

磁化电感 *Lm* 在其线性区域工作时的电感。

#### 依赖关系

要启用此参数，请将 **Magnetization inductance parameterized
by** 设置为 `Single inductance (linear)` 或
`Single saturation point`。

### **Saturated inductance** — 饱和电感 `1e-2` `H`（默认）

磁化电感 *Lm* 超出其饱和点工作时的电感。

#### 依赖关系

要启用此参数，请将 **Magnetization inductance parameterized
by** 设置为 `Single saturation point`。

### **Saturation magnetic flux** — 饱和磁通 `1.6e-04` `Wb`（默认）

磁化电感 *Lm* 饱和时的磁通。

#### 依赖关系

要启用此参数，请将 **Magnetization inductance parameterized
by** 设置为 `Single saturation point`。

### **Current vector, i** — 电流数据 `[0, .4, .8, 1.2, 1.6, 2]` `A`（默认）

模块用于填充磁通对电流查找表的电流数据。

#### 依赖关系

要启用此参数，请将 **Magnetization inductance parameterized
by** 设置为 `Magnetic flux versus current
characteristic`。

### **Magnetic flux vector, phi** — 磁通向量 `[0, .161, .25, .284, .295, .299] .* 1e-3` `Wb`（默认）

模块用于填充磁通对电流查找表的磁通数据。

#### 依赖关系

要启用此参数，请将 **Magnetization inductance parameterized
by** 设置为 `Magnetic flux versus current
characteristic`。

### **Magnetic field strength vector, H** — 磁场强度 `[0, 200, 400, 600, 800, 1000]` `A/m`（默认）| 向量

磁场强度 *H*，指定为与磁通密度向量 *B* 元素数量相同的向量。

#### 依赖关系

要启用此参数，请将 **Magnetization inductance parameterized
by** 设置为 `Magnetic flux density versus field strength
characteristic`。

### **Magnetic flux density vector, B** — 磁通密度 `[0, .81, 1.25, 1.42, 1.48, 1.49]` `T`（默认）| 向量

磁通密度 *B*，指定为与磁场强度向量 *H* 元素数量相同的向量。

#### 依赖关系

要启用此参数，请将 **Magnetization inductance parameterized
by** 设置为 `Magnetic flux density versus field strength
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

### **Coefficient for reversible magnetization, c** — 可逆磁化系数 `0.1`（默认）| [0,1] 范围内的标量

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

- `Linear` — 选择此选项以获得最佳
  性能。
- `Smooth` — 选择此选项以生成具有连续一阶导数的
  连续曲线。

有关插值算法的更多信息，请参见 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，请将 **Magnetization inductance parameterized
by** 设置为 `Magnetic flux versus current
characteristic` 或 `Magnetic flux density versus field
strength characteristic`。

### 初始条件

### **Combined leakage inductance initial current** — 合并漏感初始电流 `0` `A`（默认）

零时刻流过合并漏感 *Leq* 的电流。

#### 依赖关系

要启用此参数，请在 **Main** 设置中将
**Winding parameterized by** 参数设置为 `Combined
主值和次值`。

### **Primary leakage inductance initial current** — 一次漏感初始电流 `0` `A`（默认）

零时刻流过一次漏感 *L1* 的电流。

#### 依赖关系

要启用此参数，请在 **Main** 设置中将
**Winding parameterized by** 参数设置为 `Separate
主值和次值`。

### **Secondary leakage inductance initial current** — 二次漏感初始电流 `0` `A`（默认）

零时刻流过二次漏感 *L2* 的电流。

#### 依赖关系

要启用此参数，请在 **Main** 设置中将
**Winding parameterized by** 参数设置为 `Separate
主值和次值`。

### **Specify magnetization inductance initial state by** — 初始状态指定选项 `Current`（默认）| `Magnetic flux`

初始状态指定方法。选择以下选项之一：

- `Current` — 通过初始电流指定
  磁化电感 *Lm* 的初始状态。
- `Magnetic flux` — 通过磁通指定
  磁化电感 *Lm* 的初始状态。

#### 依赖关系

要启用此参数，请在 **Magnetization** 设置中
将 **Magnetization inductance parameterized by** 参数设置为
以下选项之一：

- `Single inductance (linear)`
- `Single saturation point`
- `Magnetic flux versus current
  characteristic`
- `Magnetic flux density versus magnetic field strength
  characteristic`

### **Magnetization inductance initial current** — 磁化电感初始电流 `0` `A`（默认）

模块用于计算零时刻磁化电感 *Lm* 内磁通的初始电流值。此参数是流过磁化电感 *Lm* 的电流。总磁化电流由流过磁化电阻 *Rm* 的电流和流过磁化电感 *Lm* 的电流组成。

#### 依赖关系

要启用此参数，请将 **Specify magnetization inductance initial
state by** 设置为 `Current`。

### **Magnetization inductance initial magnetic flux** — 磁化电感初始磁通 `0` `Wb`（默认）

零时刻磁化电感 *Lm* 中的磁通。

#### 依赖关系

要启用此参数，请将 **Specify magnetization inductance initial
state by** 设置为 `Magnetic flux`。

### **Magnetization inductance initial magnetic flux density** — 磁化电感初始磁通密度 `0` `T`（默认）

零时刻的磁通密度。

#### 依赖关系

要启用此参数，请在 **Magnetization** 设置中
将 **Magnetization inductance parameterized by** 参数设置为
`Magnetic flux density versus field strength characteristic with
hysteresis`。

### **Magnetization inductance initial field strength** — 磁化电感初始磁场强度 `0` `A/m`（默认）

零时刻的磁场强度。

#### 依赖关系

要启用此参数，请在 **Magnetization** 设置中
将 **Magnetization inductance parameterized by** 参数设置为
`Magnetic flux density versus field strength characteristic with
hysteresis`。

### 寄生参数

### **Combined leakage inductance parasitic parallel conductance** — Combined leakage inductance parasitic parallel conductance `1e-9` `1/Ohm`（默认值）

使用此参数表示与组合漏感 *Leq* 并联的小寄生效应。要仿真某些电路拓扑，您需要一个小并联电导。

#### 依赖关系

要启用此参数，请在 **Main** 设置中将 **Winding parameterized by** 设置为 `Combined 主值和次值`。

### **Primary leakage inductance parasitic parallel conductance** — Primary leakage inductance parasitic parallel conductance `1e-9` `1/Ohm`（默认值）

使用此参数表示与初级漏感 *L1* 并联的小寄生效应。要仿真某些电路拓扑，您需要一个小并联电导。

#### 依赖关系

要启用此参数，请在 **Main** 设置中将 **Winding parameterized by** 设置为 `Separate 主值和次值`。

### **Secondary leakage inductance parasitic parallel conductance** — Secondary leakage inductance parasitic parallel conductance `1e-9`（默认值）

使用此参数表示与次级漏感 *L2* 并联的小寄生效应。要仿真某些电路拓扑，您需要一个小并联电导。

#### 依赖关系

要启用此参数，请在 **Main** 设置中将 **Winding parameterized by** 设置为 `Separate 主值和次值`。

## 所属库

Simscape / Electrical / Passive / Transformers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

## 描述

具有非理想铁芯的变压器

Nonlinear Transformer 模块表示具有非理想铁芯的变压器。铁芯可能因其磁特性和尺寸而非理想。等效电路拓扑取决于您选择用于参数化绕组漏感的方式。

如果将 **Winding parameterized by** 设置为 `Combined primary and secondary values`，则使用集总电阻和电感值来表示初级和次级绕组中的组合漏感。

在此图中：

- *Req* 是组合绕组电阻。
- *Leq* 是组合漏感。
- *L2* 是次级漏感。
- *Rm* 是磁化电阻。
- *Lm* 是磁化电感。

如果将 **Winding parameterized by** 设置为 `Separate primary and secondary values`，则使用单独的电阻和电感来表示初级和次级绕组中的漏感。

在此图中：

- *R1* 是初级绕组电阻。
- *L1* 是初级漏感。
- *R2* 是次级绕组电阻。
- *L2* 是次级漏感。
- *Rm* 是磁化电阻。
- *Lm* 是磁化电感。

要参数化非线性磁化电感，请将 **Magnetization inductance parameterized by** 参数设置为以下选项之一：

- `Single inductance (linear)`
- `Single saturation point`
- `Magnetic flux versus current characteristic`
- `Magnetic flux density versus magnetic field strength characteristic`
- `Magnetic flux density versus magnetic field strength characteristic with hysteresis`

有关这些参数化选项（包括模块用于对非线性磁化电感建模的方程）的更多信息，请参阅 Nonlinear Inductor 模块参考页。

Simscape™ 和 Simscape Electrical™ 库包含多个可以对同一类型变压器设备建模的模块。但是，这些模块做出不同的建模假设。要为您的应用选择正确的模块，您必须了解这些假设如何影响模块行为随频率的变化。有关更多信息，请参阅 Choose Blocks to Model Transformers。
