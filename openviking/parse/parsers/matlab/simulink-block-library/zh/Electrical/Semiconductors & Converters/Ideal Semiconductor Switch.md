---
type: simulink-block
title: 'Ideal Semiconductor Switch'
family: 'semiconductors-converters'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'idealsemiconductorswitch'
documentation_source_path: 'ref/idealsemiconductorswitch.html'
language: zh-CN
chinese_source: worker-translation
---

# Ideal Semiconductor Switch

## 端口

### 输入

### **G** — 栅极端子物理信号

与栅极端子关联的物理信号端口。

#### 依赖项

要启用此端口，请将 **Gate-control port** 设置为 `PS control port`。

### 守恒

### **G** — 栅极端子电气

与栅极端子关联的电气守恒端口。

#### 依赖项

要启用此端口，请将 **Gate-control port** 设置为 `Electrical control port`。

### **A** — 阳极端子电气

与阳极端子关联的电气守恒端口。

### **K** — 阴极端子电气

与阴极端子关联的电气守恒端口。

## 参数

### 主要

### **Gate-control port** — 指定物理控制端口还是电气控制端口 `PS`（默认） | `Electrical`

指定开关栅极的物理控制端口还是电气控制端口。

### **On-state resistance** — 导通状态电阻 `0.001` `Ohm`（默认）

器件处于 on 状态时的阳极-阴极电阻。

### **Off-state conductance** — 关断状态电导 `1e-6` `1/Ohm`（默认）

器件处于 off 状态时的阳极-阴极电导。该值必须小于 1/R，其中 R 是 **On-state resistance** 的值。

### **Threshold voltage, Vth** — 阈值电压 `0.5` `V`（默认）

栅极-阴极电压阈值。当栅极-阴极电压高于此值时，器件导通。

### 积分二极管

### **Integral protection diode** — 积分保护二极管 `External diode`（默认） | `Protection diode with no dynamics` | `Protection diode with charge dynamics`

指定模块是否包含积分保护二极管。

如果要包含积分保护二极管，有两个选项：

- `Protection diode with no dynamics`
- `Protection diode with charge dynamics`

### **Forward voltage** — 正向电压 `0.8` `V`（默认）

使二极管 I-V 特性的斜率为 1/Ron 所需的跨 `+` 和 `-` 模块端口的最小电压，其中 Ron 是 **On resistance** 的值。

#### 依赖项

要启用此参数，请将 **Integral protection diode** 设置为 `Protection diode with no dynamics` 或 `Protection diode with charge dynamics`。

### **On resistance** — 导通电阻 `0.001` `Ohm`（默认）

高于 **Forward voltage** 时电压相对电流的变化率。

#### 依赖项

要启用此参数，请将 **Integral protection diode** 设置为 `Protection diode with no dynamics` 或 `Protection diode with charge dynamics`。

### **Off conductance** — 关断电导 `1e-5` `1/Ohm`（默认）

反向偏置二极管的电导。

#### 依赖项

仅当 **Integral protection diode** 参数设置为 `Protection diode with no dynamics` 或 `Protection diode with charge dynamics` 时，此参数可见。

### **Junction capacitance** — 结电容 `50e-9` `F`（默认）

二极管结电容。

#### 依赖项

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 时，此参数可见。

### **Initial forward current when measuring iRM** — 测量 iRM 时的初始正向电流 `300` `A`（默认） | positive scalar

测量峰值反向电流时的初始正向电流。

#### 依赖项

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 时，此参数可见。

### **Rate of change of current when measuring iRM** — 测量 iRM 时的电流变化率 `-50``A/μs`（默认） | negative scalar

测量峰值反向电流时的电流变化率。该值必须小于零。

#### 依赖项

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 时，此参数可见。

### **Reverse recovery time parameterization** — 反向恢复时间参数化 `Specify reverse recovery time directly`（默认） | `Specify stretch factor` | `Specify reverse recovery charge`

确定在模块中如何指定反向恢复时间。默认值为 `Specify reverse recovery time directly`。

如果选择 `Specify stretch factor` 或 `Specify reverse recovery charge`，则指定一个值，模块使用该值推导反向恢复时间。有关这些选项的更多信息，请参阅 How the Block Calculates TM and Tau。

#### 依赖项

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 时，此参数可见。

### **Reverse recovery time, trr** — 反向恢复时间 `15` `μs`（默认） | scalar

电流初始降至零（二极管关断时）与电流降至小于峰值反向电流的 10% 之间的时间间隔。**Reverse recovery time, trr** 参数的值必须大于 **Peak reverse current, iRM** 参数的值除以 **Rate of change of current when measuring iRM** 参数的值。

#### 依赖项

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 且 **Reverse recovery time parameterization** 参数设置为 `Specify reverse recovery time directly` 时，此参数可见。

### **Reverse recovery time stretch factor** — 反向恢复时间拉伸因子 `3`（默认） | scalar greater than `1`

模块用于计算反向恢复时间的拉伸因子。指定拉伸因子比指定反向恢复电荷更容易参数化反向恢复时间。拉伸因子的值越大，反向恢复电流消散所需的时间越长。

#### 依赖项

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 且 **Reverse recovery time parameterization** 参数设置为 `Specify stretch factor` 时，此参数可见。

### **Reverse recovery charge, Qrr** — 反向恢复电荷 `1500` `μAs`（默认）

模块用于计算反向恢复时间的反向恢复电荷。如果您的二极管器件数据表指定的是反向恢复电荷值而不是反向恢复时间值，请使用此参数。

反向恢复电荷是二极管关断时继续消散的总电荷。该值必须小于 −i2RM2a，其中：

- *iRM* 是为 **Peak reverse current, iRM** 指定的值。
- *a* 是为 **Rate of change of current when measuring iRM** 指定的值。

#### 依赖项

仅当 **Integral protection diode** 参数设置为 `Diode with charge dynamics` 且 **Reverse recovery time parameterization** 参数设置为 `Specify reverse recovery charge` 时，此参数可见。

有关这些参数的更多信息，请参阅 Diode。

## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

Ideal Semiconductor Switch

Ideal Semiconductor Switch 模块对理想半导体开关器件进行建模。

该图显示了理想半导体开关的典型 *i-v 特性*。

如果栅极-阴极电压超过指定的阈值电压，则理想半导体开关处于 on 状态。否则，器件处于 off 状态。

在 on 状态下，阳极-阴极路径表现为具有导通电阻 *Ron* 的线性电阻。

在 off 状态下，阳极-阴极路径表现为具有低关断状态电导 *Goff* 的线性电阻。

使用 **Integral Diode** 参数，您可以包含一个积分阴极-阳极二极管。积分二极管通过为反向电流提供导电路径来保护半导体器件。当半导体器件突然切断向负载的电压供应时，感性负载可能产生高反向电压尖峰。

下表显示了如何根据您的目标设置 **Integral protection diode** 参数。

| 目标 | 要选择的值 | 模块行为 |
| --- | --- | --- |
| 优先考虑仿真速度。 | `Diode with no dynamics` | 该模块包含 Diode 模块的积分副本。要参数化内部 Diode 模块，请使用 **Protection** 参数。 |
| 精确指定反向模式电荷动态。 | `Diode with charge dynamics` | 该模块包含 Diode 模块动态模型的积分副本。要参数化内部 Diode 模块，请使用 **Protection** 参数。 |
