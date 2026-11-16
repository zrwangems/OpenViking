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

### 守恒

### **1+** — 线路 1 正极端子电气

与线路 1 正极端子关联的电气守恒端口。

### **1-** — 线路 1 负极端子电气

与线路 1 负极端子关联的电气守恒端口。

### **2+** — 线路 2 正极端子电气

与线路 2 正极端子关联的电气守恒端口。

### **2-** — 线路 2 负极端子电气

与线路 2 负极端子关联的电气守恒端口。

### **3+** — 线路 3 正极端子电气

与线路 3 正极端子关联的电气守恒端口。

### **3-** — 线路 3 负极端子电气

与线路 3 负极端子关联的电气守恒端口。

## 参数

### 主要

### **初级匝数** — 绕组 1 初级匝数 `100`（默认）| positive scalar integer

变压器第一个初级绕组的导线匝数。

### **第一次级匝数** — 绕组 2 匝数 `200`（默认）| positive scalar integer

变压器第一个次级绕组的导线匝数。

### **第二次级匝数** — 绕组 3 匝数 `200`（默认）| positive scalar integer

变压器第二个次级绕组的导线匝数。

### **初级绕组电阻** — 绕组 1 电阻 `0.01` `Ohm`（默认）| nonnegative scalar

*R1* 的电阻，表示初级绕组的功率损耗。

### **初级漏感** — 绕组 1 漏感 `0.0001` `H`（默认）| nonnegative scalar

*L1* 的电感，表示初级绕组的磁通损耗。

### **第一次级绕组电阻** — 绕组 2 电阻 `0.01` `Ohm`（默认）| nonnegative scalar

*R2* 的电阻，表示第一次级绕组的功率损耗。

### **第一次级漏感** — 绕组 2 漏感 `0.0001` `H`（默认）| nonnegative scalar

*L2* 的电感，表示第一次级绕组的磁通损耗。

### **第二次级绕组电阻** — 绕组 3 电阻 `0.01` `Ohm`（默认）| nonnegative scalar

*R3* 的电阻，表示第二次级绕组的功率损耗。

### **第二次级漏感** — 绕组 3 漏感 `0.0001` `H`（默认）| nonnegative scalar

*L3* 的电感，表示第二次级绕组的磁通损耗。

### 磁化

### **磁化电阻** — 磁化电阻 `100` `Ohm`（默认）

*Rm* 的电阻，表示变压器铁芯中的磁损耗。

### **磁化电感参数化方式** — 非线性磁化电感参数化 `Single saturation point`（默认）| `Single inductance (linear)` | `Magnetic flux versus current characteristic` | `Magnetic flux density versus field strength characteristic` | `Magnetic flux density versus field strength characteristic with hysteresis`

非线性磁化电感参数化的方法：

- `Single inductance (linear)`
  — 提供未饱和电感值。
- `Single saturation point`
  — 提供未饱和和饱和电感的值，以及饱和磁通。
- `Magnetic flux versus current characteristic` — 提供电流向量和磁通向量，然后填充磁通对电流查找表。
- `Magnetic flux density versus field strength characteristic` — 提供有效铁芯长度、横截面积、磁场强度向量和磁通密度向量的值，然后填充磁通密度对磁场强度查找表。
- `Magnetic flux density versus field strength characteristic with hysteresis` —
  通过提供匝数、有效铁芯长度和横截面积、初始无磁滞 B-H 曲线梯度、B-H 曲线上某一点的磁通密度和磁场强度、可逆磁化系数、体耦合系数以及域间耦合因子，将磁通密度定义为电流值和磁场强度历史的函数。

### **未饱和电感** — 未饱和电感 `4e-2` `H`（默认）

当磁化电感 *Lm* 在其线性区域中运行时的电感。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 参数设置为 `Single inductance (linear)` 或 `Single saturation point`。

### **饱和电感** — 饱和电感 `1e-2` `H`（默认）

当磁化电感 *Lm* 超出其饱和点运行时对应的电感。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 参数设置为 `Single saturation point`。

### **饱和磁通** — 饱和磁通 `1.6e-04` `Wb`（默认）

磁化电感 *Lm* 饱和时的磁通。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 参数设置为 `Single saturation point`。

### **电流向量，i** — 电流数据 `[0, .4, .8, 1.2, 1.6, 2]` `A`（默认）

模块用于填充磁通对电流查找表的电流数据。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 参数设置为 `Magnetic flux versus current characteristic`。

### **磁通向量，phi** — 磁通向量 `[0, .161, .25, .284, .295, .299] .* 1e-3` `Wb`（默认）

模块用于填充磁通对电流查找表的磁通数据。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 参数设置为 `Magnetic flux versus current characteristic`。

### **磁场强度向量，H** — 磁场强度向量 `[0, 200, 400, 600, 800, 1000]` `A/m`（默认）| vector

磁场强度 *H*，指定为与磁通密度向量 *B* 元素数量相同的向量。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 参数设置为 `Magnetic flux density versus field strength characteristic`。

### **磁通密度向量，B** — 磁通密度向量 `[0, .81, 1.25, 1.42, 1.48, 1.49]` `T`（默认）| vector

磁通密度 *B*，指定为与磁场强度向量 *H* 元素数量相同的向量。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 参数设置为 `Magnetic flux density versus field strength characteristic`。

### **有效长度** — 有效铁芯长度 `0.2` `m`（默认）| positive finite scalar

有效铁芯长度。此参数表示铁芯周围磁路的平均长度。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 参数设置为 `Magnetic flux density versus field strength characteristic` 或 `Magnetic flux density versus field strength characteristic with hysteresis`。

### **有效横截面积** — 有效铁芯横截面积 `2e-4` `m^2`（默认）| positive finite scalar

有效铁芯横截面积。此参数表示铁芯周围磁路的平均面积。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 参数设置为 `Magnetic flux density versus field strength characteristic` 或 `Magnetic flux density versus field strength characteristic with hysteresis`。

### **H 为零时的无磁滞 B-H 梯度** — 零磁场强度附近无磁滞 B-H 曲线的梯度 `0.005` `m*T/A`（默认）| scalar

零磁场强度附近无磁滞 *B*-*H* 曲线的梯度。将此参数设置为上升和下降磁滞曲线的平均梯度。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 参数设置为 `Magnetic flux density versus field strength characteristic with hysteresis`。

### **无磁滞 B-H 曲线上的磁通密度点** — 无磁滞 B-H 曲线上的磁通密度点 `1.49` `T`（默认）| scalar

用于磁场强度测量的点的磁通密度。您必须通过提供其磁通密度值来指定无磁滞曲线上的点。为获得准确结果，请选择高磁场强度处上升和下降磁滞曲线重合的点。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 参数设置为 `Magnetic flux density versus field strength characteristic with hysteresis`。

### **对应磁场强度** — 测量点处的磁场强度 `1000` `A/m`（默认）| scalar

与使用 **无磁滞 B-H 曲线上的磁通密度点** 参数定义的点对应的磁场强度。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 设置为 `Magnetic flux density versus field strength characteristic with hysteresis`。

### **可逆磁化系数，c** — 可逆磁化系数 `0.1`（默认）| scalar in the range [0,1]

Jiles-Atherton 方程中的可逆磁化系数 *c*。此参数表示可以反转的磁化比例。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 设置为 `Magnetic flux density versus magnetic field strength characteristic with hysteresis`。

### **体耦合系数，K** — 体耦合系数 `200` `A/m`（默认）| finite positive scalar

Jiles-Atherton 方程中的体耦合系数 *K*。此参数主要控制 *B*-*H* 曲线穿过零磁通密度线时的磁场强度大小。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 设置为 `Magnetic flux density versus field strength characteristic with hysteresis`。

### **域间耦合因子，alpha** — 域间耦合因子 `1e-4`（默认）| scalar

Jiles-Atherton 方程中的域间耦合因子 *α*。此参数主要影响 *B*-*H* 曲线与零磁场强度线相交的点。典型值在 `1e-4` 到 `1e-3` 范围内。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 参数设置为 `Magnetic flux density versus field strength characteristic with hysteresis`。

### **插值选项** — 插值选项 `Linear`（默认）| `Smooth`

查找表插值选项。选择以下插值方法之一：

- `Linear` — 选择此选项以获得最佳性能。
- `Smooth` — 生成具有连续一阶导数的连续曲线。

有关插值算法的详细信息，请参阅 PS Lookup Table (1D) 模块参考页。

#### 依赖关系

要启用此参数，请将 **磁化电感参数化方式** 参数设置为 `Magnetic flux versus current characteristic` 或 `Magnetic flux density versus field strength characteristic`。

### 初始条件

### **初级漏感初始电流** — 初级漏感初始电流 `0` `A`（默认）

时间零时通过初级漏感 *L1* 的电流。

### **第一次级漏感初始电流** — 第一次级漏感初始电流 `0` `A`（默认）

时间零时通过第一次级漏感 *L2* 的电流。

### **第二次级漏感初始电流** — 第二次级漏感初始电流 `0` `A`（默认）

时间零时通过第二次级漏感 *L3* 的电流。

### **指定磁化电感初始状态的方式** — 初始状态指定选项 `Current`（默认）| `Magnetic flux`

初始状态指定。选择以下选项之一：

- `Current` — 通过初始电流指定磁化电感 *Lm* 的初始状态。
- `Magnetic flux` — 通过磁通指定磁化电感 *Lm* 的初始状态。

#### 依赖关系

要启用此参数，请在 **磁化** 设置中，将 **磁化电感参数化方式** 参数设置为：

- `Single inductance (linear)`
- `Single saturation point`
- `Magnetic flux versus current characteristic`
- `Magnetic flux density versus field strength characteristic`

### **磁化电感初始电流** — 磁化电感初始电流 `0` `A`（默认）

模块用于计算时间零时磁化电感 *Lm* 内磁通的初始电流值。此参数是通过磁化电感 *Lm* 的电流。总磁化电流由通过磁化电阻 *Rm* 的电流和通过磁化电感 *Lm* 的电流组成。

#### 依赖关系

要启用此参数，请将 **指定磁化电感初始状态的方式** 参数设置为 `Current`。

### **磁化电感初始磁通** — 磁化电感初始磁通 `0` `Wb`（默认）

时间零时磁化电感 *Lm* 中的磁通。

#### 依赖关系

要启用此参数，请将 **指定磁化电感初始状态的方式** 参数设置为 `Magnetic flux`。

### **磁化电感初始磁通密度** — 磁化电感初始磁通密度 `0` `T`（默认）

时间零时的磁通密度。

#### 依赖关系

要启用此参数，请在 **磁化** 设置中，将 **磁化电感参数化方式** 参数设置为 `Magnetic flux density versus field strength characteristic with hysteresis`。

### **磁化电感初始磁场强度** — 磁化电感初始磁场强度 `0` `A/m`（默认）

时间零时的磁场强度。

#### 依赖关系

要启用此参数，请在 **磁化** 设置中，将 **磁化电感参数化方式** 参数设置为 `Magnetic flux density versus field strength characteristic with hysteresis`。

### 寄生

### **初级漏感寄生并联电导** — 绕组 1 漏感寄生并联电导 `1e-9` `1/Ohm`（默认）| nonneagative scalar

与初级漏感 *L1* 并联的小寄生效应。为仿真某些电路拓扑，您需要一个小并联电导。

### **第一次级漏感寄生并联电导** — 绕组 2 漏感寄生并联电导 `1e-9` `1/Ohm`（默认）| nonneagative scalar

与第一次级漏感 *L2* 并联的小寄生效应。为仿真某些电路拓扑，您需要一个小并联电导。

### **第二次级漏感寄生并联电导** — 绕组 3 漏感寄生并联电导 `1e-9` `1/Ohm`（默认）| nonneagative scalar

与第二次级漏感 *L3* 并联的小寄生效应。为仿真某些电路拓扑，您需要一个小并联电导。

## 所属库

Simscape / Electrical / Passive / Transformers

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

单相非线性三绕组变压器

Three-Winding Nonlinear Transformer 模块表示具有非理想铁芯的单相非线性三绕组变压器。铁芯可能因其磁特性或尺寸而非理想。该图展示了等效电路拓扑：

其中：

- *R1* 是原边绕组电阻。
- *L1* 是原边漏电感。
- *R2* 是第一次级绕组电阻。
- *L2* 是第一次级漏电感。
- *R3* 是第二次级绕组电阻。
- *L3* 是第二次级漏电感。
- *Rm* 是磁化电阻。
- *Lm* 是磁化电感。

要参数化非线性磁化电感，请将 **磁化电感参数化方式** 参数设置为以下选项之一：

- `Single inductance (linear)`
- `Single saturation point`
- `Magnetic flux versus current characteristic`
- `Magnetic flux density versus magnetic field strength characteristic`
- `Magnetic flux density versus magnetic field strength characteristic with hysteresis`

有关这些参数化选项的更多信息，包括该模块用于对非线性磁化电感建模的方程，请参阅 Nonlinear Inductor 模块参考页。

Simscape™ 和 Simscape Electrical™ 库包含多个可对同一类型的变压器设备建模的模块。但是，这些模块做出不同的建模假设。要为您的应用选择正确的模块，您必须了解这些假设如何影响模块随频率变化的行为。有关更多信息，请参阅 Choose Blocks to Model Transformers。
