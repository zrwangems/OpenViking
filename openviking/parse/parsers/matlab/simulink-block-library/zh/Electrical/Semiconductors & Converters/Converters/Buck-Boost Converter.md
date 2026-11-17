---
type: simulink-block
title: 'Buck-Boost Converter'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'buckboostconverter'
documentation_source_path: 'ref/buckboostconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Buck-Boost Converter

## 端口

### 输入

### **G** — 开关器件栅极控制物理信号 | 标量

与开关器件栅极端子关联的物理信号端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Inverting converter`，并将
**Gate-control port** 设置为
`PS`。

**数据类型：** `double`
### 守恒

### **G** — 开关器件栅极控制电气 | 向量

与开关器件栅极端子关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Four-switch converter`。

**数据类型：** `double`

### **G+** — 开关器件栅极控制正极端子电气 | 标量

与开关器件栅极正极端子关联的正极电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Inverting converter`，并将
**Gate-control port** 设置为
`Electrical`。

**数据类型：** `double`

### **G-** — 开关器件栅极控制负极端子电气 | 标量

与开关器件栅极负极端子关联的负极电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Inverting converter`，并将
**Gate-control port** 设置为
`Electrical`。

**数据类型：** `double`

### **1+** — 正极直流电压 1 电气 | 标量

与第一个直流电压正极端子关联的电气守恒端口。

**数据类型：** `double`

### **1-** — 负极直流电压 1 电气 | 标量

与第一个直流电压负极端子关联的电气守恒端口。

**数据类型：** `double`

### **2+** — 正极直流电压 2 电气 | 标量

与第二个直流电压正极端子关联的电气守恒端口。

**数据类型：** `double`

### **2-** — 负极直流电压 2 电气 | 标量

与第二个直流电压负极端子关联的电气守恒端口。

**数据类型：** `double`

## 参数

### **Modeling option** — 建模为反相还是四开关升降压变换器 `Inverting converter`（默认）| `Four-switch converter`

建模为反相还是四开关升降压变换器。

### 开关器件

此表显示了 **Switching Devices** 参数的可见性如何取决于您选择的 **Switching device**。要了解如何阅读此表，请参阅参数依赖关系。

**Switching Devices 参数依赖关系**

| 参数和选项 | | | | | |
| --- | --- | --- | --- | --- | --- |
| **Switching device** | | | | | |
| *`Ideal Semiconductor Switch`* | *`GTO`* | *`IGBT`* | *`MOSFET`* | *`Thyristor`* | *`Averaged Switch`* |
| On-state resistance | Forward voltage | Forward voltage | Drain-source on resistance | Forward voltage | On-state resistance |
| Off-state conductance | On-state resistance | On-state resistance | Off-state conductance | On-state resistance |
| Threshold voltage | Off-state conductance | Off-state conductance | Threshold voltage | Off-state conductance |
| 栅极触发电压，Vgt | 阈值电压 | 栅极触发电压，Vgt | 用于栅极输入分段常数近似的整数（0 表示禁用） |
| Gate turn-off voltage, Vgt\_off | Gate turn-off voltage, Vgt\_off |
| Holding current | Holding current |

### **Gate-control port** — 为开关栅极指定物理控制端口还是电气控制端口 `PS`（默认）| `Electrical`

为开关栅极指定物理控制端口还是电气控制端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为
`Inverting converter`。

### **Switching device** — 开关类型 `Ideal Semiconductor Switch`（默认）| `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

变换器的开关器件类型。对于四开关模型，开关是相同的。

模型。

#### 依赖关系

请参阅 Switching Devices 参数依赖关系表。

### **Forward voltage** — 电压 `0.8` `V`（默认）| 标量

对于不同的开关器件类型，**Forward voltage** 取值如下：

- GTO — 使器件 I-V 特性梯度为
  1/*Ron* 所需的阳极和阴极块端口之间的最小电压，其中
  *Ron* 是
  **On-state resistance** 的值
- IGBT — 使二极管 I-V 特性梯度为
  1/*Ron* 所需的集电极和发射极块端口之间的最小电压，其中
  *Ron* 是
  **On-state resistance** 的值
- Thyristor — 使器件导通所需的最小电压

#### 依赖关系

请参阅 Switching Devices 参数依赖关系表。

### **On-state resistance** — 电阻 `0.001` `Ohm`（默认）| 标量

对于不同的开关器件类型，**On-state resistance** 取值如下：

- GTO — 高于正向电压时电压对电流的变化率
- Ideal semiconductor switch — 器件导通时的阳极-阴极电阻
- IGBT — 器件导通时的集电极-发射极电阻
- Thyristor — 器件导通时的阳极-阴极电阻
- Averaged switch — 器件导通时的阳极-阴极电阻

#### 依赖关系

请参阅 Switching Devices 参数依赖关系表。

### **Drain-source on resistance** — 电阻 `0.001` `Ohm`（默认）| 标量

漏极和源极之间的电阻，该电阻还取决于栅极-源极电压。

#### 依赖关系

请参阅 Switching Devices 参数依赖关系表。

### **Off-state conductance** — 电导 `1e-5` `1/Ohm`（默认）| 标量

器件关断时的电导。该值必须小于
1/*R*，其中 *R* 是
**On-state resistance** 的值。

对于不同的开关器件类型，**On-state resistance** 取值如下：

- GTO — 阳极-阴极电导
- Ideal semiconductor switch — 阳极-阴极电导
- IGBT — 集电极-发射极电导
- MOSFET — 漏极-源极电导
- Thyristor — 阳极-阴极电导

#### 依赖关系

请参阅 Switching Devices 参数依赖关系表。

### **Threshold voltage** — 电压阈值 `6` `V`（默认）| 标量

栅极电压阈值。当栅极电压高于此值时，器件导通。对于不同的开关器件类型，所关注的器件电压为：

- Ideal semiconductor switch — 栅极-阴极电压
- IGBT — 栅极-发射极电压
- MOSFET — 栅极-源极电压

#### 依赖关系

请参阅 Switching Devices 参数依赖关系表。

### **Gate trigger voltage, Vgt** — 电压阈值 `1` `V`（默认）| 标量

栅极-阴极电压阈值。当栅极-阴极电压高于此值时，器件导通。

#### 依赖关系

请参阅 Switching Devices 参数依赖关系表。

### **Gate turn-off voltage, Vgt\_off** — 电压阈值 `-1` `V`（默认）| 标量

栅极-阴极电压阈值。当栅极-阴极电压低于此值时，器件关断。

#### 依赖关系

请参阅 Switching Devices 参数依赖关系表。

### **Holding current** — 电流阈值 `1` `A`（默认）| 标量

栅极电流阈值。当电流高于此值时，即使栅极-阴极电压降至栅极触发电压以下，器件仍保持导通。

#### 依赖关系

请参阅 Switching Devices 参数依赖关系表。

### **Integer for piecewise constant approximation of gate input (0 for disabled)** — 用于 FPGA 部署的整数模式 `0`（默认）| 非负标量

用于对 FPGA 部署的栅极输入执行分段常数逼近的整数。

#### 依赖关系

要启用此参数，请将 **Switching device** 设置为 `Averaged Switch`。

### 二极管

此表显示了 **Diode** 参数的可见性如何取决于您如何配置 **Model dynamics** 和 **Reverse recovery time parameterization** 参数。要了解如何阅读此表，请参阅参数依赖关系。

**Diode 参数依赖关系**

| 参数和选项 | | | |
| --- | --- | --- | --- |
| **Model dynamics** | | | |
| *`Diode with no dynamics`* | *`Diode with charge dynamics`* | | |
| Forward voltage | Forward voltage | | |
| On resistance | On resistance | | |
| Off conductance | Off conductance | | |
| Junction capacitance | | |
| Peak reverse current, iRM | | |
| Initial forward current when measuring iRM | | |
| Rate of change of current when measuring iRM | | |
| **Reverse recovery time parameterization** | | |
| *`Specify stretch factor`* | *`Specify reverse recovery time directly`* | `Specify reverse recovery charge` |
| Reverse recovery time stretch factor | Reverse recovery time, trr | Reverse recovery charge, Qrr |

### **Model dynamics** — 二极管模型 `Diode with no dynamics`（默认）| `Diode with charge dynamics`

二极管类型。选项包括：

- `Diode with no dynamics` — 选择此选项以使用
  Diode 模块优先考虑仿真速度。
- `Diode with charge dynamics` —
  选择此选项以使用 Diode 模块的换向二极管模型，在反向模式电荷动态方面优先考虑模型保真度。

**注意**

如果您在 **Switching Device** 设置中为 **Switching Device** 参数选择 `Averaged Switch`，则此参数不可见，并且会自动选择 `Diode with no dynamics`。

#### 依赖关系

请参阅 Diode 参数依赖关系表。

### **Forward voltage** — 电压 `0.8` `V`（默认）| 标量

使二极管 I-V 特性梯度为
1/*Ron* 所需的正极和负极块端口之间的最小电压，其中
*Ron* 是
**On resistance** 的值。

### **On resistance** — 电阻 `0.001` `Ohm`（默认）| 标量

高于 **Forward voltage** 时电压对电流的变化率。

### **Off conductance** — 电导 `1e-5` `1/Ohm`（默认）| 标量

反向偏置二极管的电导。

### **Junction capacitance** — 电容 `50` `nF`（默认）| 标量

二极管结电容。

#### 依赖关系

请参阅 Diode 参数依赖关系表。

### **Peak reverse current, iRM** — 电流 `-235` `A`（默认）| 小于 `0` 的标量

由外部测试电路测得的峰值反向电流。

#### 依赖关系

请参阅 Diode 参数依赖关系表。

### **Initial forward current when measuring iRM** — 电流 `300` `A`（默认）| 大于 `0` 的标量

测量峰值反向电流时的初始正向电流。此值必须大于零。

#### 依赖关系

请参阅 Diode 参数依赖关系表。

### **Rate of change of current when measuring iRM** — 电流变化率 `-50` `A/us`（默认）| 标量

测量峰值反向电流时的电流变化率。

#### 依赖关系

请参阅 Diode 参数依赖关系表。

### **Reverse recovery time parameterization** — 恢复时间模型 `Specify stretch factor`（默认）| `Specify reverse recovery time directly` | `Specify reverse recovery charge`

用于参数化恢复时间的模型。当您选择
`Specify stretch factor` 或
`Specify reverse recovery charge` 时，可以指定一个值，模块使用该值来推导反向恢复时间。

#### 依赖关系

请参阅 Diode 参数依赖关系表。

### **Reverse recovery time stretch factor** — 拉伸因子 `3`（默认）| 大于 `1` 的标量

模块用于计算 **Reverse recovery time, trr** 的值。指定拉伸因子比指定反向恢复电荷更容易参数化反向恢复时间。拉伸因子的值越大，反向恢复电流消散所需的时间越长。

#### 依赖关系

请参阅 Diode 参数依赖关系表。

### **Reverse recovery time, trr** — 时间 `15` `us`（默认）| 标量

电流最初降至零（二极管关断时）与电流降至峰值反向电流的 10% 以下之间的时间间隔。

**Reverse recovery time, trr** 参数的值必须大于 **Peak reverse current, iRM** 参数的值除以 **Rate of change of current when measuring iRM** 参数的值。

#### 依赖关系

请参阅 Diode 参数依赖关系表。

### **Reverse recovery charge, Qrr** — 电荷 `1500` `s*uA`（默认）| 标量

模块用于计算 **Reverse recovery time, trr** 的值。如果您的二极管器件数据手册指定了反向恢复电荷的值而不是反向恢复时间的值，请使用此参数。

反向恢复电荷是二极管关断时继续消散的总电荷。该值必须小于 −i2RM2a，

其中：

- *iRM* 是为 **Peak reverse current, iRM** 指定的值。
- *a* 是为 **Rate of change of current when measuring iRM** 指定的值。

#### 依赖关系

请参阅 Diode 参数依赖关系表。

### LC 参数

### **Inductance** — 电感 `1e-6` `H`（默认）| 正标量

电感。

### **Inductor series resistance** — 电感串联电阻 `0` `Ohm`（默认）| 零或正标量

电感的串联电阻。

### **Capacitance** — 电容 `1e-7` `F`（默认）| 正标量

电容。

### **Capacitor effective series resistance** — 电容电阻 `1e-6` `Ohm`（默认）| 零或正标量

电容的串联电阻。

### 缓冲器

如果您将 **Switching device** 设置为 `Averaged Switch`，则 **Snubbers** 参数选项卡不可见。

下表总结了 **Snubbers** 参数依赖关系。要了解如何阅读此表，请参阅参数依赖关系。

**Snubbers 参数依赖关系**

| Snubbers 参数依赖关系 | |
| --- | --- |
| **Snubber** | |
| *`None`* | *`RC Snubber`* |
| Snubber resistance |
| Snubber capacitance |

### **Snubber** — 缓冲器模型 `None`（默认）| `RC snubber`

开关器件缓冲器。

#### 依赖关系

请参阅 Snubbers 参数依赖关系表。

### **Snubber resistance** — 电阻 `0.1`（默认）| `Ohm` | 标量

开关器件缓冲器的电阻。

#### 依赖关系

请参阅 Snubbers 参数依赖关系表。

### **Snubber capacitance** — 电容 `1e-7`（默认）| `F` | 标量

开关器件缓冲器的电容。

#### 依赖关系

请参阅 Snubbers 参数依赖关系表。

## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

## 描述

由控制器驱动的 DC-DC 反相或四开关升压或降压电压调节器

Buck-Boost Converter 模块表示一个 DC-DC 转换器，它可以在附加控制器和门极信号发生器的驱动下，将 DC 电压从转换器的一侧升压或降压到另一侧。升降压转换器也称为升压/降压电压调节器，因为它们可以增大或减小电压幅值。

该模块还可以反相电压，使输出电压的极性与输入电压的极性相反。输出电压的幅值取决于占空比。

Buck-Boost Converter 模块允许您对具有一个开关器件的反相升降压转换器或具有四个开关器件的升降压转换器进行建模。开关器件类型的选项包括：

- GTO — 门极关断晶闸管。有关该器件的 I-V 特性信息，请参阅 GTO。
- Ideal semiconductor switch — 有关该器件的 I-V 特性信息，请参阅 Ideal Semiconductor Switch。
- IGBT — 绝缘栅双极晶体管。有关该器件的 I-V 特性信息，请参阅 IGBT (Ideal, Switching)。
- MOSFET — N 沟道金属氧化物半导体场效应晶体管。有关该器件的 I-V 特性信息，请参阅 MOSFET (Ideal, Switching)。
- Thyristor — 有关该器件的 I-V 特性信息，请参阅 Thyristor (Piecewise Linear)。
- Averaged Switch — 带反并联二极管的半导体开关。控制信号端口 **G** 接受区间 [0,1] 内的值。当 **G** 等于 `0` 或 `1` 时，平均开关分别完全断开或完全闭合。该开关的行为类似于带反并联二极管的 Ideal Semiconductor Switch 模块。当 **G** 介于 0 和 1 之间时，平均开关部分断开。您可以在指定周期内对脉宽调制（PWM）信号进行平均。然后您可以对模型进行欠采样，并使用调制波形代替 PWM 信号。

### 转换器拓扑

您可以将此转换器建模为具有物理信号门极控制端口或两个电气控制端口的反相升降压转换器，或建模为具有电气控制端口的四开关升降压转换器。要选择转换器拓扑，请将 **Modeling option** 参数设置为以下之一：

- `Inverting converter` — 具有物理或电气门极控制端口的反相升降压转换器。
- `Four-switch converter` — 具有多路复用门极信号的四开关升降压转换器。

反相转换器模型包含一个开关器件、一个二极管、一个电感器和一个输出电容器。

四开关转换器模型包含四个开关器件、一个电感器和一个输出电容器。

在每种情况下，电容器都会平滑输出电压。

### 保护

您可以为每个开关器件包含一个缓冲电路。缓冲电路包含串联连接的电阻器和电容器。它们保护开关器件免受感性负载在器件关断负载电压供应时产生的高电压的影响。缓冲电路还可以防止开关器件导通时电流变化率过大。

要为每个开关器件包含和配置缓冲电路，请使用 **Snubbers** 参数。

### 门极控制

要将门极控制电压信号连接到开关器件的门极端口，对于：

- 反相转换器模型：

  - PS 控制端口模型：

    1. 使用 Simulink-PS Converter 模块将 Simulink® 门极控制电压信号转换为物理信号。
    2. 将 Simulink-PS Converter 模块连接到 **G** 端口。
  - 电气控制端口模型：

    1. 将 Simscape™ 电气域正 DC 电压信号连接到 **G+** 端口。
    2. 将 Simscape 电气域负 DC 电压信号连接到 **G-** 端口。
- 同步转换器模型：

  1. 使用 Simulink-PS Converter 模块将每个 Simulink 门极控制电压信号转换为物理信号。
  2. 使用 Four-Pulse Gate Multiplexer 将转换后的门极控制信号多路复用为单个向量。
  3. 将向量信号连接到 **G** 端口。

### 用于 FPGA 部署的平均开关中的分段常数近似

如果您将 **Switching device** 参数设置为 `Averaged switch`，并且您的模型使用分区求解器，则该模块会产生非线性分区，因为平均模式方程包含作为输入 **G** 函数的模式 *Gsat*。为了使这些方程与硬件描述语言（HDL）代码生成兼容，从而支持 FPGA 部署，请将 **Integer for piecewise constant approximation of gate input (0 for disabled)** 参数设置为大于 `0` 的值。该模块随后将 *Gsat* 模式视为具有固定范围的分段常数整数。这将之前的非线性分区转换为线性时变分区。

范围 `[0,K]` 内的整数值（其中 *K* 是 **Integer for piecewise constant approximation of gate input (0 for disabled)** 的值）现在与范围 `[0,1]` 内的每个实值模式相关联。该模块通过将原始模式除以 K 将其归一化回范围 `[0,1]` 来计算分段常数模式：

uI=(floor(u⋅K))u^=uIK

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可以提高仿真鲁棒性。您可以使用不同的来源指定标称值，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
