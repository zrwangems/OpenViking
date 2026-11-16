---
type: simulink-block
title: 'Rectifier (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Semiconductors and Converters / Converters / Converters, Inverters, Rectifiers, and Choppers'
documentation_page: 'rectifierthreephase'
documentation_source_path: 'ref/rectifierthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Rectifier (Three-Phase)

## 端口

### 守恒

### **~** — 三相端口电气

可扩展三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`。

### **a** — *a* 相电气

与 *a* 相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **b** — *b* 相电气

与 *b* 相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **c** — *c* 相电气

与 *c* 相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **+** — 正极端子电气

与正极端子相关的电气守恒端口。

### **-** — 负极端子电气

与负极端子相关的电气守恒端口。

## 参数

### 主要

### **Electrical connection** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

是否使用复合三相端口或扩展三相端口。

### **Forward voltage** — 正向电压 `0.8` `V`（默认）

每个二极管的 `+` 和 `-` 端口两端所需的最小电压，使得二极管 i-v 特性的斜率为 1/*Ron*，其中 *Ron* 是 **On resistance** 的值。

### **On resistance** — 导通电阻 `0.001` `Ohm`（默认）

每个二极管在正向电压以上时电压相对于电流的变化率。

### **Off conductance** — 关断电导 `1e-5` `1/Ohm`（默认）

每个反向偏置二极管的电导。

### 电荷动态

### **Model dynamics** — 二极管电荷动态 `No dynamics`（默认）| `Model charge dynamics`

二极管电荷动态。默认值为 `No dynamics`。

可供选择的电荷动态选项包括：

- `No dynamics`
- `Model charge dynamics`

### **Junction capacitance** — 结电容 `50e-9` `F`（默认）

二极管结电容。

#### 依赖关系

仅当 **Model dynamics** 参数设置为 `Model charge dynamics` 时，此参数才可见。

### **Peak reverse current, iRM** — 峰值反向电流 `-235` `A`（默认）| negative scalar

由外部测试电路测得的峰值反向电流。该值必须小于零。

#### 依赖关系

仅当 **Model dynamics** 参数设置为 `Model charge dynamics` 时，此参数才可见。

### **Initial forward current when measuring iRM** — 测量 iRM 时的初始正向电流 `300` `A`（默认）| positive scalar

测量峰值反向电流时的初始正向电流。该值必须大于零。

#### 依赖关系

仅当 **Model dynamics** 参数设置为 `Model charge dynamics` 时，此参数才可见。

### **Rate of change of current when measuring iRM** — 测量 iRM 时的电流变化率 `-50``A/μs`（默认）| negative scalar

测量峰值反向电流时的电流变化率。该值必须小于零。

#### 依赖关系

仅当 **Model dynamics** 参数设置为 `Model charge dynamics` 时，此参数才可见。

### **Reverse recovery time parameterization** — 反向恢复时间参数化 `Specify stretch factor`（默认）| `Specify reverse recovery time directly` | `Specify reverse recovery charge`

确定在模块中如何指定反向恢复时间。默认值为 `Specify reverse recovery time directly`。

如果选择 `Specify stretch factor` 或 `Specify reverse recovery charge`，则指定一个值，模块将使用该值推导反向恢复时间。有关这些选项的详细信息，请参阅模块如何计算 TM 和 Tau。

#### 依赖关系

仅当 **Model dynamics** 参数设置为 `Model charge dynamics` 时，此参数才可见。

### **Reverse recovery time, trr** — 反向恢复时间 `15` `μs`（默认）

电流最初变为零（当二极管关断时）的时间与电流降至峰值反向电流的 10% 以下的时间之间的间隔。**Reverse recovery time, trr** 参数的值必须大于 **Peak reverse current, iRM** 参数的值除以 **Rate of change of current when measuring iRM** 参数的值。

#### 依赖关系

仅当 **Model dynamics** 参数设置为 `Model charge dynamics` 且 **Reverse recovery time parameterization** 参数设置为 `Specify reverse recovery time directly` 时，此参数才可见。

### **Reverse recovery time stretch factor** — 反向恢复时间拉伸因子 `3`（默认）

模块用于计算 **Reverse recovery time, trr** 的值。该值必须大于 `1`。与指定反向恢复电荷相比，指定拉伸因子是参数化反向恢复时间的一种更简单方法。拉伸因子的值越大，反向恢复电流耗散所需的时间越长。

#### 依赖关系

仅当 **Model dynamics** 参数设置为 `Model charge dynamics` 且 **Reverse recovery time parameterization** 参数设置为 `Specify stretch factor` 时，此参数才可见。

### **Reverse recovery charge, Qrr** — 反向恢复电荷 `1500` `μAs`（默认）

模块用于计算 **Reverse recovery time, trr** 的值。如果二极管器件的数据手册指定的是反向恢复电荷值而不是反向恢复时间值，请使用此参数。

反向恢复电荷是二极管关断时继续耗散的总电荷。该值必须小于 −i2RM2a，

其中：

- *iRM* 是为 **Peak reverse current, iRM** 指定的值。
- *a* 是为 **Rate of change of current when measuring iRM** 指定的值。

#### 依赖关系

仅当 **Model dynamics** 参数设置为 `Model charge dynamics` 且 **Reverse recovery time parameterization** 参数设置为 `Specify reverse recovery charge` 时，此参数才可见。

有关这些参数的详细信息，请参阅 Diode。

## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2021b：电气连接端口更新

从 R2021b 开始，要在复合端口和扩展端口之间切换，请将 **Electrical connection** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。

由于这些更改，在早期版本中保存的模型内，请检查此模块的 **Electrical connection** 参数。

## 描述

非受控三相交流到直流电压

Rectifier (Three-Phase) 模块对将三相交流电压转换为直流电压的三臂二极管桥式电路进行建模。该图显示了该三臂二极管桥式电路的等效电路。

使用模块对话框的电荷动态选项卡，可以选择三臂桥式电路所使用的二极管类型。该表显示了如何根据目标设置 **Model dynamics** 参数。

| 目标 | 要选择的值 | 模块行为 |
| --- | --- | --- |
| 优先考虑仿真速度。 | `No dynamics` | 桥式电路的每个臂使用 Diode 模块的一个副本。模块对话框不显示其他参数。 |
| 精确指定反向模式电荷动态。 | `Model charge dynamics` | 桥式电路的每个臂使用 Diode 模块的换流模型的一个副本。模块对话框显示与该模块换流模型相关的参数。 |
