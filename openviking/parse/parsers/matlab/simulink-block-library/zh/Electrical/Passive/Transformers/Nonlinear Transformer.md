---
type: simulink-block
title: 'Nonlinear Transformer'
family: 'passive'
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

### 守恒

### **1+** — 一次绕组正极性电气

与一次绕组正极性关联的电气守恒端口。

### **1-** — 一次绕组负极性电气

与一次绕组负极性关联的电气守恒端口。

### **2+** — 二次绕组正极性电气

与二次绕组正极性关联的电气守恒端口。

### **2-** — 二次绕组负极性电气

与二次绕组负极性关联的电气守恒端口。

## 参数

### 主

### **一次绕组匝数** — 一次绕组匝数 `100`（默认）

变压器一次绕组上的导线匝数。

### **二次绕组匝数** — 二次绕组匝数 `200`（默认）

变压器二次绕组上的导线匝数。

### **绕组参数化方式** — 绕组漏电感参数化 `Combined primary and secondary values`（默认） | `Separate primary and secondary values`

绕组漏电感的参数化选项。选择以下方法之一：

- `Combined primary and secondary values` —
  使用集中电阻和电感值表示一次和二次绕组中的组合漏电感。
- `Separate primary and secondary values` —
  使用单独的电阻和电感表示一次和二次绕组中的漏电感。

### **组合绕组电阻** — 组合绕组电阻 `0.01` `Ohm`（默认）

集中等效电阻 *Req*，表示一次和二次绕组的组合功率损耗。

#### 依赖关系

要启用此参数，请将 **绕组参数化方式** 设置为 `Combined primary and secondary values`。

### **组合漏电感** — 组合漏电感 `0.0001` `H`（默认）

集中等效电感 *Leq*，表示一次和二次绕组的组合磁通损耗。

#### 依赖关系

要启用此参数，请将 **绕组参数化方式** 设置为 `Combined primary and secondary values`。

### **一次绕组电阻** — 一次绕组电阻 `0.01` `Ohm`（默认）

电阻 *R1*，表示一次绕组的功率损耗。

#### 依赖关系

要启用此参数，请将 **绕组参数化方式** 设置为 `Separate primary and secondary values`。

### **一次漏电感** — 一次漏电感 `0.0001` `H`（默认）

电感 *L1*，表示一次绕组的磁通损耗。

#### 依赖关系

要启用此参数，请将 **绕组参数化方式** 设置为 `Separate primary and secondary values`。

### **二次绕组电阻** — 二次绕组电阻 `0.01` `Ohm`（默认）

电阻 *R2*，表示二次绕组的功率损耗。

#### 依赖关系

要启用此参数，请将 **绕组参数化方式** 设置为 `Separate primary and secondary values`。

### **二次漏电感** — 二次漏电感 `0.0001` `H`（默认）

电感 *L2*，表示二次绕组的磁通损耗。

#### 依赖关系

要启用此参数，请将 **绕组参数化方式** 设置为 `Separate primary and secondary values`。

### **功率记录平均周期** — 功率记录平均周期 `0` `s`（默认）

功率记录平均周期。

### 磁化

### **磁化电阻** — 磁化电阻 `100` `Ohm`（默认）

电阻 *Rm*，表示变压器磁芯中的磁损耗。

### **磁化电感参数化方式** — 非线性磁化电感参数化 `Single saturation point`（默认） | `Single inductance (linear)` | `Magnetic flux versus current characteristic` | `Magnetic flux density versus field strength characteristic` | `Magnetic flux density versus field strength characteristic with hysteresis`

选择以下非线性磁化电感参数化方法之一：

- `Single inductance (linear)` — 提供未饱和电感值。
- `Single saturation point` — 提供未饱和电感和饱和电感值，以及饱和磁通。
- `Magnetic flux versus current characteristic` — 提供电流向量和磁通向量，以填充磁通-电流查找表。
- `Magnetic flux density versus field strength characteristic` — 提供有效磁芯长度和截面积值，以及磁场强度向量和磁通密度向量，以填充磁通密度-磁场强度查找表。
- `Magnetic flux density versus field strength characteristic with hysteresis` — 除了匝数以及有效磁芯长度和截面积之外，还提供初始无磁滞 *B*-*H* 曲线梯度、*B*-*H* 曲线上某一点的磁通密度和磁场强度，以及可逆磁化系数、体耦合系数和域间耦合因子，以将磁通密度定义为电流值和磁场强度历史的函数。

### **未饱和电感** — 未饱和电感 `4e-2` `H`（默认）

磁化电感 *Lm* 在其线性区域工作时的电感。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 设置为 `Single inductance (linear)` 或 `Single saturation point`。

### **饱和电感** — 饱和电感 `1e-2` `H`（默认）

磁化电感 *Lm* 在其饱和点之外工作时的电感。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 设置为 `Single saturation point`。

### **饱和磁通** — 饱和磁通 `1.6e-04` `Wb`（默认）

磁化电感 *Lm* 饱和时的磁通。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 设置为 `Single saturation point`。

### **电流向量, i** — 电流数据 `[0, .4, .8, 1.2, 1.6, 2]` `A`（默认）

模块用来填充磁通-电流查找表的电流数据。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 设置为 `Magnetic flux versus current characteristic`。

### **磁通向量, phi** — 磁通向量 `[0, .161, .25, .284, .295, .299] .* 1e-3` `Wb`（默认）

模块用来填充磁通-电流查找表的磁通数据。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 设置为 `Magnetic flux versus current characteristic`。

### **磁场强度向量, H** — 磁场强度 `[0, 200, 400, 600, 800, 1000]` `A/m`（默认） | vector

磁场强度 *H*，指定为与磁通密度向量 *B* 具有相同元素数量的向量。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 设置为 `Magnetic flux density versus field strength characteristic`。

### **磁通密度向量, B** — 磁通密度 `[0, .81, 1.25, 1.42, 1.48, 1.49]` `T`（默认） | vector

磁通密度 *B*，指定为与磁场强度向量 *H* 具有相同元素数量的向量。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 设置为 `Magnetic flux density versus field strength characteristic`。

### **有效长度** — 有效磁芯长度 `0.2` `m`（默认） | positive finite scalar

有效磁芯长度。此参数表示围绕磁芯的磁路径平均长度。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 参数设置为 `Magnetic flux density versus field strength characteristic` 或 `Magnetic flux density versus field strength characteristic with hysteresis`。

### **有效截面积** — 有效磁芯截面积 `2e-4` `m^2`（默认） | positive finite scalar

有效磁芯截面积。此参数表示围绕磁芯的磁路径平均面积。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 参数设置为 `Magnetic flux density versus field strength characteristic` 或 `Magnetic flux density versus field strength characteristic with hysteresis`。

### **H 为零时的无磁滞 B-H 梯度** — 零磁场强度附近无磁滞 B-H 曲线的梯度 `0.005` `m*T/A`（默认） | scalar

零磁场强度附近无磁滞 *B*-*H* 曲线的梯度。将此参数设置为上升和下降磁滞曲线的平均梯度。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 参数设置为 `Magnetic flux density versus field strength characteristic with hysteresis`。

### **无磁滞 B-H 曲线上的磁通密度点** — 无磁滞 B-H 曲线上的磁通密度点 `1.49` `T`（默认） | scalar

用于磁场强度测量的点的磁通密度。必须通过提供磁通密度值来指定无磁滞曲线上的点。为获得准确结果，请选择高磁场强度处上升和下降磁滞曲线重合的点。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 参数设置为 `Magnetic flux density versus field strength characteristic with hysteresis`。

### **对应磁场强度** — 测量点处的磁场强度 `1000` `A/m`（默认） | scalar

与使用 **无磁滞 B-H 曲线上的磁通密度点** 参数定义的点对应的磁场强度。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 设置为 `Magnetic flux density versus field strength characteristic with hysteresis`。

### **可逆磁化系数, c** — 可逆磁化系数 `0.1`（默认） | scalar in the range [0,1]

Jiles-Atherton 方程中的可逆磁化系数 *c*。此参数表示可反向的磁化比例。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 设置为 `Magnetic flux density versus magnetic field strength characteristic with hysteresis`。

### **体耦合系数, K** — 体耦合系数 `200` `A/m`（默认） | finite positive scalar

Jiles-Atherton 方程中的体耦合系数 *K*。此参数主要控制 *B*-*H* 曲线穿过零磁通密度线时的磁场强度幅值。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 设置为 `Magnetic flux density versus field strength characteristic with hysteresis`。

### **域间耦合因子, alpha** — 域间耦合因子 `1e-4`（默认） | scalar

Jiles-Atherton 方程中的域间耦合因子 *α*。此参数主要影响 *B*-*H* 曲线与零磁场强度线相交的点。典型值在 `1e-4` 到 `1e-3` 范围内。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 参数设置为 `Magnetic flux density versus field strength characteristic with hysteresis`。

### **插值选项** — 插值选项 `Linear`（默认） | `Smooth`

查找表插值选项。选择以下插值方法之一：

- `Linear` — 选择此选项可获得最佳性能。
- `Smooth` — 选择此选项可生成具有连续一阶导数的连续曲线。

有关插值算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 设置为 `Magnetic flux versus current characteristic` 或 `Magnetic flux density versus field strength characteristic`。

### 初始条件

### **组合漏电感初始电流** — 组合漏电感初始电流 `0` `A`（默认）

在时间为零时流过组合漏电感 *Leq* 的电流。

#### 依赖关系

要启用此参数，请在 **主** 设置中，将 **绕组参数化方式** 参数设置为 `Combined primary and secondary values`。

### **一次漏电感初始电流** — 一次漏电感初始电流 `0` `A`（默认）

在时间为零时流过一次漏电感 *L1* 的电流。

#### 依赖关系

要启用此参数，请在 **主** 设置中，将 **绕组参数化方式** 参数设置为 `Separate primary and secondary values`。

### **二次漏电感初始电流** — 二次漏电感初始电流 `0` `A`（默认）

在时间为零时流过二次漏电感 *L2* 的电流。

#### 依赖关系

要启用此参数，请在 **主** 设置中，将 **绕组参数化方式** 参数设置为 `Separate primary and secondary values`。

### **通过以下方式指定磁化电感初始状态** — 初始状态指定选项 `Current`（默认） | `Magnetic flux`

初始状态指定方法。选择以下选项之一：

- `Current` — 通过初始电流指定磁化电感 *Lm* 的初始状态。
- `Magnetic flux` — 通过磁通指定磁化电感 *Lm* 的初始状态。

#### 依赖关系

要启用此参数，请在 **磁化** 设置中，将 **磁化电感参数化方式** 参数设置为以下选项之一：

- `Single inductance (linear)`
- `Single saturation point`
- `Magnetic flux versus current characteristic`
- `Magnetic flux density versus magnetic field strength characteristic`

### **磁化电感初始电流** — 磁化电感初始电流 `0` `A`（默认）

模块用来计算时间为零时磁化电感 *Lm* 内磁通的初始电流值。此参数是流过磁化电感 *Lm* 的电流。总磁化电流由流过磁化电阻 *Rm* 的电流和流过磁化电感 *Lm* 的电流组成。

#### 依赖关系

要启用此参数，请将 **通过以下方式指定磁化电感初始状态** 设置为 `Current`。

### **磁化电感初始磁通** — 磁化电感初始磁通 `0` `Wb`（默认）

时间为零时磁化电感 *Lm* 中的磁通。

#### 依赖关系

要启用此参数，请将 **通过以下方式指定磁化电感初始状态** 设置为 `Magnetic flux`。

### **磁化电感初始磁通密度** — 磁化电感初始磁通密度 `0` `T`（默认）

时间为零时的磁通密度。

#### 依赖关系

要启用此参数，请在 **磁化** 设置中，将 **磁化电感参数化方式** 参数设置为 `Magnetic flux density versus field strength characteristic with hysteresis`。

### **磁化电感初始磁场强度** — 磁化电感初始磁场强度 `0` `A/m`（默认）

时间为零时的磁场强度。

#### 依赖关系

要启用此参数，请在 **磁化** 设置中，将 **磁化电感参数化方式** 参数设置为 `Magnetic flux density versus field strength characteristic with hysteresis`。

### 寄生

### **组合漏感寄生并联电导** — 组合漏感寄生并联电导 `1e-9` `1/Ohm`（默认）

使用此参数表示与组合漏感 *Leq* 并联的小寄生效应。为了仿真某些电路拓扑，您需要一个小的并联电导。

#### 依赖关系

要启用此参数，请在 **Main** 设置中，将**绕组参数化方式**设置为 `Combined primary and secondary values`。

### **初级漏感寄生并联电导** — 初级漏感寄生并联电导 `1e-9` `1/Ohm`（默认）

使用此参数表示与初级漏感 *L1* 并联的小寄生效应。为了仿真某些电路拓扑，您需要一个小的并联电导。

#### 依赖关系

要启用此参数，请在 **Main** 设置中，将**绕组参数化方式**设置为 `Separate primary and secondary values`。

### **次级漏感寄生并联电导** — 次级漏感寄生并联电导 `1e-9`（默认）

使用此参数表示与次级漏感 *L2* 并联的小寄生效应。为了仿真某些电路拓扑，您需要一个小的并联电导。

#### 依赖关系

要启用此参数，请在 **Main** 设置中，将**绕组参数化方式**设置为 `Separate primary and secondary values`。

## 所属库

Simscape / Electrical / Passive / Transformers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012b 中引入**

## 描述

具有非理想铁芯的变压器

Nonlinear Transformer 模块表示具有非理想铁芯的变压器。铁芯可能因其磁特性和尺寸而是非理想的。等效电路拓扑取决于您选择用于参数化绕组漏感的选项。

如果将**绕组参数化方式**设置为 `Combined primary and secondary values`，则使用集中电阻和电感值来表示初级和次级绕组中的组合漏感。

在此图中：

- *Req* 是组合绕组电阻。
- *Leq* 是组合漏感。
- *L2* 是次级漏感。
- *Rm* 是磁化电阻。
- *Lm* 是磁化电感。

如果将**绕组参数化方式**设置为 `Separate primary and secondary values`，则使用单独的电阻和电感来表示初级和次级绕组中的漏感。

在此图中：

- *R1* 是初级绕组电阻。
- *L1* 是初级漏感。
- *R2* 是次级绕组电阻。
- *L2* 是次级漏感。
- *Rm* 是磁化电阻。
- *Lm* 是磁化电感。

要参数化非线性磁化电感，请将**磁化电感参数化方式**参数设置为以下选项之一：

- `Single inductance (linear)`
- `Single saturation point`
- `Magnetic flux versus current characteristic`
- `Magnetic flux density versus magnetic field strength characteristic`
- `Magnetic flux density versus magnetic field strength characteristic with hysteresis`

有关这些参数化选项（包括该模块用于对非线性磁化电感建模的方程）的详细信息，请参阅 Nonlinear Inductor 模块参考页。

Simscape™ 和 Simscape Electrical™ 库包含多个可以对同一类型变压器设备建模的模块。但是，这些模块做出不同的建模假设。要为您的应用选择正确的模块，您必须了解这些假设如何影响模块行为随频率的变化。有关详细信息，请参阅 Choose Blocks to Model Transformers。
