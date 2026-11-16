---
type: simulink-block
title: 'Modular Multilevel Converter Arm'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'modularmultilevelconverterarm'
documentation_source_path: 'ref/modularmultilevelconverterarm.html'
language: zh-CN
chinese_source: worker-translation
---

# Modular Multilevel Converter Arm

## 端口

### 输入

### **G** — 子模块门极控制物理信号向量

与模块化多电平换流器桥臂所有子模块的门极信号关联的物理信号端口，指定为物理信号向量。

如果将 **Converter topology** 参数设置为 `Half-bridge`，则输出是长度为 *2 \* Nsm* 的向量，其中 *Nsm* 是 **Number of power submodules**。

如果将 **Converter topology** 参数设置为 `Full-bridge`，则输出是长度为 *4\* Nsm* 的向量。

#### 依赖关系

要启用此端口，请将 **Fidelity level** 设置为 `Detailed model - switching devices` 或 `Equivalent model - PWM-controlled`。

### **ref** — 子模块参考波形物理信号

与参考波形关联的物理信号端口，指定为物理信号。

#### 依赖关系

要启用此端口，请将 **Fidelity level** 设置为 `Equivalent model - waveform-controlled`。

### 输出

### **vc** — 电容器电压物理信号向量

与模块化多电平换流器桥臂中每个子模块的电容器电压关联的物理信号端口，指定为物理信号向量。

#### 依赖关系

要启用此端口，请将 **Capacitor voltages** 设置为 `Instrumented`。

### 守恒

### **+** — 正极端子电气

与模块化多电平换流器桥臂正极端子关联的电气守恒端口。

### **-** — 负极端子电气

与模块化多电平换流器桥臂负极端子关联的电气守恒端口。

## 参数

### 主要

### **Converter topology** — 换流器拓扑 `Half-bridge` (默认) | `Full-bridge`

模块化多电平换流器的拓扑。

### **Fidelity level** — 模型保真度 `Detailed model - switching devices` (默认) | `Equivalent model - PWM-controlled` | `Equivalent model - waveform-controlled`

模型的保真度级别。

### **Capacitor voltages** — 电容器电压测量 `Instrumented` (默认) | `Uninstrumented`

是否测量电容器电压。

### **Number of power submodules** — 子模块数量 `1` (默认) | positive scalar

模块化多电平换流器的功率子模块数量。

### **Capacitance** — 子模块电容 `1e-7` `F` (默认) | scalar | vector

子模块的电容。如果输入向量，该向量的长度必须为 *Nsm*，其中 *Nsm* 是 **Number of power submodules**。

### **Capacitor effective series resistance** — 电容器等效串联电阻 `1e-6` `Ohm` (默认) | scalar | vector

电容器等效串联电阻。如果输入向量，该向量的长度必须为 *Nsm*，其中 *Nsm* 是 **Number of power submodules**。

#### 依赖关系

要启用此参数，请将 **Fidelity level** 设置为 `Detailed model - switching devices`。

### **Capacitor initial voltage** — 电容器初始电压 `500` `V` (默认) | scalar | vector

电容器的初始电压。如果输入向量，该向量的长度必须为 *Nsm*，其中 *Nsm* 是 **Number of power submodules**。

### 开关器件

此表显示 **Switching Devices** 设置中启用的参数如何取决于您选择的 **Switching device**。要了解如何阅读该表，请参阅参数依赖关系。要启用这些设置，请将 **Fidelity level** 设置为 `Detailed model - switching devices`。

**开关器件参数依赖关系**

| 参数和选项 | | | | | |
| --- | --- | --- | --- | --- | --- |
| **Switching device** | | | | | |
| *`Ideal Semiconductor Switch`* | *`GTO`* | *`IGBT`* | *`MOSFET`* | *`Thyristor`* | *`Averaged Switch`* |
| **On-state resistance** | **Forward voltage** | **Forward voltage** | **Drain-source on resistance** | **Forward voltage** | **On-state resistance** |
| **Off-state conductance** | **On-state resistance** | **On-state resistance** | **Off-state conductance** | **On-state resistance** |
| **Threshold voltage** | **Off-state conductance** | **Off-state conductance** | **Threshold voltage** | **Off-state conductance** |
| **Gate trigger voltage, Vgt** | **Threshold voltage** | **Gate trigger voltage, Vgt** | **Integer for piecewise constant approximation of gate input (0 for disabled)** |
| **Gate turn-off voltage, Vgt\_off** | **Holding current** |
| **Holding current** |

### **Switching device** — 开关类型 `Ideal Semiconductor Switch` (默认) | `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

换流器的开关器件类型。

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Forward voltage** — 电压 `0.8` `V` (默认) | scalar

对于不同的开关器件类型，**Forward voltage** 是：

- GTO — 使器件 I-V 特性的斜率为 1/*Ron* 所需的阳极与阴极模块端口两端的最小电压，其中 *Ron* 是 **On-state resistance** 的值
- IGBT — 使二极管 I-V 特性的斜率为 1/*Ron* 所需的集电极与发射极模块端口两端的最小电压，其中 *Ron* 是 **On-state resistance** 的值
- Thyristor — 器件导通所需的最小电压

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **On-state resistance** — 电阻 `0.001` `Ohm` (默认) | scalar

对于不同的开关器件类型，**On-state resistance** 是：

- GTO — 高于正向电压时电压对电流的变化率
- Ideal semiconductor switch — 器件导通时的阳极-阴极电阻
- IGBT — 器件导通时的集电极-发射极电阻
- Thyristor — 器件导通时的阳极-阴极电阻
- Averaged switch — 器件导通时的阳极-阴极电阻

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Drain-source on resistance** — 电阻 `0.001` `Ohm` (默认) | scalar

漏极与源极之间的电阻。栅极-源极电压也会影响 **Drain-source on resistance** 参数。

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Off-state conductance** — 器件关断时的电导 `1e-5` `1/Ohm` (默认) | scalar

器件关断时的电导。该值必须小于 1/*R*，其中 *R* 是 **On-state resistance** 的值。

对于不同的开关器件类型，**On-state resistance** 是：

- GTO — 阳极-阴极电导
- Ideal semiconductor switch — 阳极-阴极电导
- IGBT — 集电极-发射极电导
- MOSFET — 漏极-源极电导
- Thyristor — 阳极-阴极电导

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Threshold voltage** — 电压阈值 `6` `V` (默认) | scalar

栅极电压阈值。当栅极电压高于此值时，器件导通。电压阈值根据所使用的开关器件应用于不同的器件：

- Ideal semiconductor switch — 门极-阴极电压
- IGBT — 栅极-发射极电压
- MOSFET — 栅极-源极电压

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Gate trigger voltage, Vgt** — 门极-阴极激活电压阈值 `1` `V` (默认) | scalar

门极-阴极电压阈值。当门极-阴极电压高于此值时，器件导通。

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Gate turn-off voltage, Vgt\_off** — 门极-阴极关断电压阈值 `-1` `V` (默认) | scalar

门极-阴极电压阈值。当门极-阴极电压低于此值时，器件关断。

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Holding current** — 电流阈值 `1` `A` (默认) | scalar

门极电流阈值。当电流高于此值时，即使门极-阴极电压降至门极触发电压以下，器件仍保持导通。

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Integer for piecewise constant approximation of gate input (0 for disabled)** — FPGA 部署的整数模式 `0` (默认) | nonnegative scalar

用于对 FPGA 部署的门极输入执行分段常数近似的整数。

#### 依赖关系

要启用此参数，请将 **Switching device** 设置为 `Averaged Switch`。

### 保护二极管

有关这些参数的详细信息，请参阅 Diode。

### **Model dynamics** — 二极管模型 `Diode with no dynamics` (默认) | `Diode with charge dynamics` | `None`

二极管类型。选项包括：

- `None` — 该模块不对二极管动态特性建模。
- `Diode with no dynamics` — 选择此选项可使用 Diode 模块优先考虑仿真速度。
- `Diode with charge dynamics` — 选择此选项可使用 Diode 模块的换流二极管模型，优先考虑反向模式电荷动态方面的模型保真度。

**注意**

如果在 **Switching Device** 设置中将 **Switching device** 设置为 `Averaged Switch`，则会自动选择 `Diode with no dynamics` 设置。

#### 依赖关系

要启用此参数，请将 **Switching device** 设置为 `GTO`、`Ideal Semiconductor Switch`、`IGBT`、`MOFSET` 或 `Thyristor`。

### **Forward voltage** — 正向电压 `0.8` `V` (默认) | scalar

使二极管 I-V 特性的斜率为 1/*Ron* 所需的 `+` 和 `-` 模块端口两端的最小电压，其中 *Ron* 是 **On resistance** 的值。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。

### **On resistance** — 导通电阻 `0.001` `Ohm` (默认) | scalar

高于 **Forward voltage** 时电压对电流的变化率。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。

### **Off conductance** — 关断电导 `1e-5` `1/Ohm` (默认) | scalar

反向偏置二极管的电导。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。

### **Junction capacitance** — 结电容 `50` `nF` (默认) | scalar

二极管结电容。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with charge dynamics`。

### **Peak reverse current, iRM** — 峰值反向电流 `-235` `A` (默认) | negative scalar

由外部测试电路测得的峰值反向电流。该值必须小于零。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with charge dynamics`。

### **Initial forward current when measuring iRM** — 测量 iRM 时的初始正向电流 `300` `A` (默认) | positive scalar

测量峰值反向电流时的初始正向电流。该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with charge dynamics`。

### **Rate of change of current when measuring iRM** — 测量 iRM 时的电流变化率 `-50` `A/μs` (默认) | negative scalar

测量峰值反向电流时的电流变化率。该值必须小于零。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with charge dynamics`。

### **Reverse recovery time parameterization** — 反向恢复时间选项 `Specify stretch factor` (默认) | `Specify reverse recovery time directly` | `Specify reverse recovery charge`

确定如何指定反向恢复时间。

如果选择 `Specify stretch factor` 或 `Specify reverse recovery charge`，则指定一个值，模块使用该值推导反向恢复时间。有关这些选项的详细信息，请参阅模块如何计算 TM 和 Tau。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with charge dynamics`。

### **Reverse recovery time, trr** — 反向恢复时间 `15` `μs` (默认) | scalar

电流初始降至零（二极管关断时）的时间与电流降至峰值反向电流的 10% 以下的时间之间的间隔。**Reverse recovery time, trr** 参数的值必须大于 **Peak reverse current, iRM** 参数的值除以 **Rate of change of current when measuring iRM** 参数的值。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with charge dynamics`，并将 **Reverse recovery time parameterization** 设置为 `Specify reverse recovery time directly`。

### **Reverse recovery time stretch factor** — 反向恢复时间拉伸因子 `3` (默认) | scalar

模块用于计算 **Reverse recovery time, trr** 的值。该值必须大于 `1`。与指定反向恢复电荷相比，指定拉伸因子是参数化反向恢复时间的一种更简单方法。拉伸因子的值越大，反向恢复电流消散所需的时间越长。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with charge dynamics`，并将 **Reverse recovery time parameterization** 设置为 `Specify stretch factor`。

### **Reverse recovery charge, Qrr** — 反向恢复电荷 `1500` `s*μA` (默认) | scalar

模块用于计算 **Reverse recovery time, trr** 的值。如果二极管的数据手册指定了反向恢复电荷的值而不是反向恢复时间的值，请使用此参数。

反向恢复电荷是二极管关断时继续消散的总电荷。该值必须小于 −i2RM2a，其中：

- *iRM* 是为 **Peak reverse current, iRM** 指定的值。
- *a* 是为 **Rate of change of current when measuring iRM** 指定的值。

#### 依赖关系

要启用此参数，请将 **Model dynamics** 设置为 `Diode with charge dynamics`，并将 **Reverse recovery time parameterization** 设置为 `Specify reverse recovery charge`。

### 缓冲电路

要启用 **Snubbers** 设置，请将 **Fidelity level** 设置为 `Detailed model - switching devices`，并将 **Switching device** 设置为 `GTO`、`Ideal Semiconductor Switch`、`IGBT`、`MOFSET` 或 `Thyristor`。

### **Snubber** — 缓冲电路 `None` (默认) | `RC snubber`

每个开关器件的缓冲电路：

- `None`
- `RC snubber`

### **Snubber resistance** — 缓冲电阻 `0.1` `Ohm` (默认) | scalar

缓冲电阻。

#### 依赖关系

要启用此参数，请将 **Snubber** 设置为 `RC snubber`。

### **Snubber capacitance** — 缓冲电容 `1e-7` `F` (默认) | scalar

缓冲电容。

#### 依赖关系

要启用此参数，请将 **Snubber** 设置为 `RC snubber`。

## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

带串联功率子模块的模块化多电平换流器桥臂

Modular Multilevel Converter Arm 模块将模块化多电平换流器桥臂建模为若干串联的功率子模块。

**半桥拓扑**

**全桥拓扑**

该模块允许您通过在采用开关器件的详细模型或等效模型之间进行选择，来选择模型保真度级别。可选择的开关器件包括：

- GTO — 门极可关断晶闸管。关于该器件的 I-V 特性信息，请参阅 GTO。
- Ideal semiconductor switch — 关于该器件的 I-V 特性信息，请参阅 Ideal Semiconductor Switch。
- IGBT — 绝缘栅双极型晶体管。关于该器件的 I-V 特性信息，请参阅 IGBT (Ideal, Switching)。
- MOSFET — N 沟道金属氧化物半导体场效应晶体管。关于该器件的 I-V 特性信息，请参阅 MOSFET (Ideal, Switching)。
- Thyristor — 关于该器件的 I-V 特性信息，请参阅 Thyristor (Piecewise Linear)。
- Averaged Switch — 带反并联二极管的半导体开关。控制信号端口 **G** 接受区间 [0,1] 内的值。当 **G** 等于 `0` 或 `1` 时，平均开关分别完全断开或完全闭合。该开关的行为类似于带反并联二极管的 Ideal Semiconductor Switch 模块。当 **G** 介于 0 和 1 之间时，平均开关部分断开。您可以在指定周期内对脉宽调制 (PWM) 信号取平均。然后可以对模型进行欠采样，并使用调制波形代替 PWM 信号。

### Averaged Switch 中用于 FPGA 部署的分段常数近似

如果将 **Switching device** 参数设置为 `Averaged switch`，并且您的模型使用分区求解器，则该模块会产生非线性分区，因为平均模式方程包含模式 *Gsat*，而该模式是输入 **G** 的函数。为使这些方程与硬件描述语言 (HDL) 代码生成兼容，并因此可用于 FPGA 部署，请将 **Integer for piecewise constant approximation of gate input (0 for disabled)** 参数设置为大于 `0` 的值。然后，该模块将 *Gsat* 模式视为具有固定范围的分段常数整数。这将把先前的非线性分区转变为线性时变分区。

现在，范围 `[0,K]` 内的一个整数值与范围 `[0,1]` 内的每个实值模式相关联，其中 *K* 是 **Integer for piecewise constant approximation of gate input (0 for disabled)** 的值。该模块通过将原始模式除以 K 来计算分段常数模式，以将其归一化回范围 `[0,1]`：

uI=(floor(u⋅K))u^=uIK
