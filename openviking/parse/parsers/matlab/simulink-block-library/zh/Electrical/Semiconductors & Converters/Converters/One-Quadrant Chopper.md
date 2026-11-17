---
type: simulink-block
title: 'One-Quadrant Chopper'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'onequadrantchopper'
documentation_source_path: 'ref/onequadrantchopper.html'
language: zh-CN
chinese_source: worker-translation
---

# One-Quadrant Chopper

## 端口

### 输入

### **G** — 开关器件门极控制物理信号 | 标量

与开关器件门极端子关联的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `PS`。

**数据类型：** `double`
### 守恒

### **G+** — 开关器件门极控制正极端子电气 | 标量

与开关器件正极门极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `Electrical`。

**数据类型：** `double`

### **G-** — 开关器件门极控制负极端子电气 | 标量

与开关器件负极门极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Gate-control port** 设置为 `Electrical`。

**数据类型：** `double`

### **1+** — 正直流电压 1 电气 | 标量

与第一个直流电压正极端子关联的电气守恒端口。

**数据类型：** `double`

### **1-** — 负直流电压 1 电气 | 标量

与第一个直流电压负极端子关联的电气守恒端口。

**数据类型：** `double`

### **2+** — 正直流电压 2 电气 | 标量

与第二个直流电压正极端子关联的电气守恒端口。

**数据类型：** `double`

### **2-** — 负直流电压 2 电气 | 标量

与第二个直流电压负极端子关联的电气守恒端口。

**数据类型：** `double`

## 参数

### 开关器件

此表显示了 **Switching Devices** 参数的可见性如何取决于您选择的 **Switching device**。要了解如何阅读此表，请参阅参数依赖关系。

**开关器件参数依赖关系**

| 开关器件 | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Chopper type** — 选择 `Class A - first quadrant` 或 `Class B - second quadrant`。 | | | | | | | | | | |
| **Switching device** — 选择 `Ideal Semiconductor Switch`、`GTO`、`IGBT`、`MOSFET`、`Thyristor` 或 `Averaged Switch`。 | | | | | | | | | | |
| **Ideal Semiconductor Switch** | | **GTO** | | **IGBT** | | **MOSFET** | | **Thyristor** | | **Averaged Switch** |
| 导通状态电阻 | | 正向电压 | | 正向电压 | | 漏源导通电阻 | | 正向电压 | | 导通状态电阻 |
| 关断状态电导 | | 导通状态电阻 | | 导通状态电阻 | | 关断状态电导 | | 导通状态电阻 | |
| 阈值电压 | | 关断状态电导 | | 关断状态电导 | | 阈值电压 | | 关断状态电导 | |
| 门极触发电压，Vgt | | 阈值电压 | | 门极触发电压，Vgt | | 用于门极输入分段常数近似的整数（0 表示禁用） |
| 门极关断电压，Vgt\_off | | 门极关断电压，Vgt\_off | |
| 保持电流 | | 保持电流 | |

### **Gate-control port** — 指定物理控制端口还是电气控制端口 `PS`（默认）| `Electrical`

指定开关器件门极使用物理控制端口还是电气控制端口。

### **Chopper type** — 斩波器类别 `Class A - first quadrant`（默认）| `Class B - second quadrant`

斩波器类别。

### **Switching device** — 开关类型 `Ideal Semiconductor Switch`（默认）| `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

变换器的开关器件类型。

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Forward voltage** — 电压 `0.8` `Ohm`（默认）| 标量

对于不同的开关器件类型，**Forward voltage** 取值如下：

- GTO — 使器件 I-V 特性梯度为 1/*Ron* 所需的阳极和阴极块端口之间的最小电压，其中 *Ron* 为 **On-state resistance** 的值
- IGBT — 使二极管 I-V 特性梯度为 1/*Ron* 所需的集电极和发射极块端口之间的最小电压，其中 *Ron* 为 **On-state resistance** 的值
- Thyristor — 使器件导通所需的最小电压

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **On-state resistance** — 电阻 `0.001` `Ohm`（默认）| 标量

对于不同的开关器件类型，**On-state resistance** 取值如下：

- GTO — 正向电压以上电压对电流的变化率
- Ideal semiconductor switch — 器件导通时的阳极-阴极电阻
- IGBT — 器件导通时的集电极-发射极电阻
- Thyristor — 器件导通时的阳极-阴极电阻
- Averaged switch — 器件导通时的阳极-阴极电阻

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Drain-source on resistance** — 电阻 `0.001` `Ohm`（默认）| 标量

漏极和源极之间的电阻，该电阻还取决于栅源电压。

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Off-state conductance** — 电导 `1e-5` `1/Ohm`（默认）| 标量

器件关断时的电导。该值必须小于 1/*R*，其中 *R* 为 **On-state resistance** 的值。

对于不同的开关器件类型，**On-state resistance** 取值如下：

- GTO — 阳极-阴极电导
- Ideal semiconductor switch — 阳极-阴极电导
- IGBT — 集电极-发射极电导
- MOSFET — 漏源电导
- Thyristor — 阳极-阴极电导

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Threshold voltage** — 电压阈值 `6` `V`（默认）| 标量

栅极电压阈值。当栅极电压高于此值时，器件导通。
对于不同的开关器件类型，所关注的器件电压为：

- Ideal semiconductor switch — 栅极-阴极电压
- IGBT — 栅极-发射极电压
- MOSFET — 栅极-源极电压

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Gate trigger voltage, Vgt** — 电压阈值 `1` `V`（默认）| 标量

栅极-阴极电压阈值。当栅极-阴极电压高于此值时，器件导通。

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Gate turn-off voltage, Vgt\_off** — 电压阈值 `-1` `V`（默认）| 标量

栅极-阴极电压阈值。当栅极-阴极电压低于此值时，器件关断。

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Holding current** — 电流阈值 `1` `A`（默认）| 标量

栅极电流阈值。当电流高于此值时，即使栅极-阴极电压降至门极触发电压以下，器件仍保持导通。

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Integer for piecewise constant approximation of gate input (0 for disabled)** — FPGA 部署的整数模式 `0`（默认）| 非负标量

用于对门极输入进行分段常数近似以进行 FPGA 部署的整数。

#### 依赖关系

要启用此参数，请将 **Switching device** 设置为 `Averaged Switch`。

### 二极管

**Diode** 参数的可见性取决于您如何配置保护二极管 **Model dynamics** 和 **Reverse recovery time parameterization** 参数。要了解如何阅读此表，请参阅参数依赖关系。

**二极管参数依赖关系**

| 二极管 | | | |
| --- | --- | --- | --- |
| **Model dynamics** — 选择 `Diode with no dynamics` 或 `Diode with charge dynamics`。 | | | |
| ****Diode with no dynamics**** | ****Diode with charge dynamics**** | | |
| 正向电压 | 正向电压 | | |
| 导通电阻 | 导通电阻 | | |
| 关断电导 | 关断电导 | | |
| 结电容 | | |
| 峰值反向电流，iRM | | |
| 测量 iRM 时的初始正向电流 | | |
| 测量 iRM 时的电流变化率 | | |
| **Reverse recovery time parameterization** — 选择 `Specify stretch factor`、`Specify reverse recovery time directly` 或 `Specify reverse recovery charge`。 | | |
| **Specify stretch factor** | **Specify reverse recovery time directly** | **Specify reverse recovery charge** |
| 反向恢复时间拉伸因子 | 反向恢复时间，trr | 反向恢复电荷，Qrr |

### **Model dynamics** — 二极管模型 `Diode with no dynamics`（默认）| `Diode with charge dynamics`

二极管类型。选项包括：

- `Diode with no dynamics` — 选择此选项以使用 Diode 模块优先考虑仿真速度。
- `Diode with charge dynamics` — 选择此选项以使用 Diode 模块的换流模型优先考虑反向模式电荷动态方面的模型保真度。

**注意**

如果您在 **Switching Device** 设置中为 **Switching Device** 参数选择 `Averaged Switch`，则此参数不可见，并自动选择 `Diode with no dynamics`。

#### 依赖关系

请参阅二极管参数依赖关系表。

### **Forward voltage** — 电压 `0.8` `V`（默认）| 标量

使二极管 I-V 特性梯度为 1/*Ron* 所需的正极和负极块端口之间的最小电压，其中 *Ron* 为 **On resistance** 的值。

### **On resistance** — 电阻 `0.001` `Ohm`（默认）| 标量

**Forward voltage** 以上电压对电流的变化率。

### **Off conductance** — 电导 `1e-5` `1/Ohm`（默认）| 标量

反向偏置二极管的电导。

### **Junction capacitance** — 电容 `50` `nF`（默认）| 标量

二极管结电容。

#### 依赖关系

请参阅二极管参数依赖关系表。

### **Peak reverse current, iRM** — 电流 `-235` `A`（默认）| 小于 `0` 的标量

由外部测试电路测得的峰值反向电流。

#### 依赖关系

请参阅二极管参数依赖关系表。

### **Initial forward current when measuring iRM** — 电流 `300` `A`（默认）| 大于 `0` 的标量

测量峰值反向电流时的初始正向电流。此值必须大于零。

#### 依赖关系

请参阅二极管参数依赖关系表。

### **Rate of change of current when measuring iRM** — 电流变化率 `-50` `A/us`（默认）| 标量

测量峰值反向电流时的电流变化率。

#### 依赖关系

请参阅二极管参数依赖关系表。

### **Reverse recovery time parameterization** — 恢复时间模型 `Specify stretch factor`（默认）| `Specify reverse recovery time directly` | `Specify reverse recovery charge`

用于参数化恢复时间的模型。当您选择 `Specify stretch factor` 或 `Specify reverse recovery charge` 时，可以指定一个值，模块使用该值来推导反向恢复时间。有关这些选项的更多信息，请参阅 How the Block Calculates TM and Tau。

#### 依赖关系

请参阅二极管参数依赖关系表。

### **Reverse recovery time stretch factor** — 拉伸因子 `3`（默认）| 大于 `1` 的标量

模块用于计算 **Reverse recovery time, trr** 的值。与指定反向恢复电荷相比，指定拉伸因子是参数化反向恢复时间的一种更简单的方法。拉伸因子的值越大，反向恢复电流消散所需的时间越长。

#### 依赖关系

请参阅二极管参数依赖关系表。

### **Reverse recovery time, trr** — 时间 `15` `µs`（默认）| 标量

电流最初降为零（二极管关断时）的时刻与电流降至峰值反向电流的 10% 以下的时刻之间的时间间隔。

**Reverse recovery time, trr** 参数的值必须大于 **Peak reverse current, iRM** 参数的值除以 **Rate of change of current when measuring iRM** 参数的值。

#### 依赖关系

请参阅二极管参数依赖关系表。

### **Reverse recovery charge, Qrr** — 电荷 `1500` `s*µA`（默认）| 标量

模块用于计算 **Reverse recovery time, trr** 的值。如果您的二极管器件数据手册指定了反向恢复电荷的值而不是反向恢复时间的值，请使用此参数。

反向恢复电荷是二极管关断时继续消散的总电荷。该值必须小于 −i2RM2a，

其中：

- *iRM* 是为 **Peak reverse current, iRM** 指定的值。
- *a* 是为 **Rate of change of current when measuring iRM** 指定的值。

#### 依赖关系

请参阅二极管参数依赖关系表。

### 缓冲器

如果您将 **Switching device** 设置为 `Averaged Switch`，则 **Snubbers** 参数选项卡不可见。

下表总结了 **Snubbers** 参数依赖关系。要了解如何阅读此表，请参阅参数依赖关系。

**缓冲器参数依赖关系**

| 缓冲器 | |
| --- | --- |
| **Snubber** — 选择 `None` 或 `RC Snubber`。 | |
| **None** | **RC Snubber** |
| 缓冲电阻 |
| 缓冲电容 |

### **Snubber** — 缓冲器模型 `None`（默认）| `RC snubber`

开关器件缓冲器。

#### 依赖关系

请参阅缓冲器参数依赖关系表。

### **Snubber resistance** — 电阻 `0.1` `Ohm`（默认）| 标量

开关器件缓冲器的电阻。

#### 依赖关系

请参阅缓冲器参数依赖关系表。

### **Snubber capacitance** — 电容 `1e-7`（默认）| `F` | 标量

开关器件缓冲器的电容。

#### 依赖关系

请参阅缓冲器参数依赖关系表。

## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

控制器驱动的一象限斩波器

One-Quadrant Chopper 模块表示一个一象限受控斩波器，用于将固定的直流输入转换为可变的直流输出。

电路拓扑和象限取决于您指定的斩波器类别。

第一象限或 A 类斩波器包含一个功率开关和一个二极管。

第二象限或 B 类斩波器也包含一个功率开关和一个二极管。

对于任一拓扑，开关 *S* 可以是全控开关器件（例如 IGBT 或 GTO）或半控开关器件（例如晶闸管）。

开关器件类型的选项包括：

- GTO — 门极关断晶闸管。有关该器件 I-V 特性的信息，请参阅 GTO。
- Ideal semiconductor switch — 有关该器件 I-V 特性的信息，请参阅 Ideal Semiconductor Switch。
- IGBT — 绝缘栅双极晶体管。有关该器件 I-V 特性的信息，请参阅 IGBT (Ideal, Switching)。
- MOSFET — N 沟道金属氧化物半导体场效应晶体管。有关该器件 I-V 特性的信息，请参阅 MOSFET (Ideal, Switching)。
- Thyristor — 有关该器件 I-V 特性的信息，请参阅 Thyristor (Piecewise Linear)。
- Averaged Switch — 带反并联二极管的半导体开关。控制信号端口 **G** 接受区间 [0,1] 内的值。当 **G** 等于 `0` 或 `1` 时，平均开关分别完全断开或完全闭合。该开关的行为类似于带反并联二极管的 Ideal Semiconductor Switch 模块。当 **G** 介于 0 和 1 之间时，平均开关部分断开。您可以在指定周期内对脉宽调制（PWM）信号进行平均。然后可以对模型进行欠采样，并使用调制波形代替 PWM 信号。

### Protection

当半导体器件突然切断负载的电压供应时，感性负载会产生很高的反向电压尖峰。为了保护半导体器件，一个集成保护二极管为反向电流提供导通路径。

要为 *S* 开关器件包含并配置内部保护二极管模块，请使用 **Diode** 参数。下表显示了如何根据您的目标设置 **Model dynamics** 参数。

| 目标 | 要选择的值 | 积分保护二极管 |
| --- | --- | --- |
| 优先考虑仿真速度。 | `Diode with no dynamics` | Diode 模块 |
| 通过精确指定反向模式电荷动态来优先考虑模型保真度。 | `Diode with charge dynamics` | Diode 模块的动态模型 |

您还可以为每个开关器件包含缓冲电路。缓冲电路包含一个串联连接的电阻和电容。它们保护开关器件免受感性负载在器件切断负载电压供应时产生的高电压影响。缓冲电路还可以防止开关器件导通时出现过大的电流变化率。

要为每个开关器件包含并配置缓冲电路，请使用 **Snubbers** 参数。

### Gate Control

您可以将栅极控制电压信号连接到开关器件的栅极端口。

- 对于 PS control port 模型：

  1. 使用 Simulink-PS Converter 模块将 Simulink® 栅极控制电压信号转换为物理信号。
  2. 将 Simulink-PS Converter 模块连接到 **G** 端口。
- 对于 electrical control ports 模型：

  1. 将 Simscape™ 电气域正直流电压信号连接到 **G+** 端口。
  2. 将 Simscape 电气域负直流电压信号连接到 **G-** 端口。

### Piecewise Constant Approximation in Averaged Switch for FPGA Deployment

如果您将 **Switching device** 参数设置为 `Averaged switch`，并且您的模型使用分区求解器，则此模块会产生非线性分区，因为平均模式方程包含作为输入 **G** 的函数的模式 *Gsat*。为了使这些方程与硬件描述语言 (HDL) 代码生成兼容，从而适用于 FPGA 部署，请将 **Integer for piecewise constant approximation of gate input (0 for disabled)** 参数设置为大于 `0` 的值。此模块随后会将 *Gsat* 模式视为具有固定范围的分段常数整数。这会将先前的非线性分区转换为线性时变分区。

范围 `[0,K]` 中的整数值现在与范围 `[0,1]` 中的每个实值模式相关联，其中 *K* 是 **Integer for piecewise constant approximation of gate input (0 for disabled)** 的值。该模块通过将原始模式除以 K 将其归一化回范围 `[0,1]` 来计算分段常数模式：

uI=(floor(u⋅K))u^=uIK
