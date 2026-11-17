---
type: simulink-block
title: 'Two-Quadrant Chopper'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'twoquadrantchopper'
documentation_source_path: 'ref/twoquadrantchopper.html'
language: zh-CN
chinese_source: worker-translation
---

# Two-Quadrant Chopper

## 端口
```yaml
ports:
- name: G
  summary: 开关器件栅极控制 electrical | vector
  direction: conserving
  data_types: double
- name: 1+
  summary: 直流电压 1 正极 electrical | scalar
  direction: conserving
  data_types: double
- name: 1-
  summary: 直流电压 1 负极 electrical | scalar
  direction: conserving
  data_types: double
- name: 2+
  summary: 直流电压 2 正极 electrical | scalar
  direction: conserving
  data_types: double
- name: 2-
  summary: 直流电压 2 负极 electrical | scalar
  direction: conserving
  data_types: double
```

### 守恒端口

### **G** — 开关器件栅极控制 electrical | vector

与开关器件栅极端子相关联的电气守恒端口。

**数据类型：** `double`

### **1+** — 直流电压 1 正极 electrical | scalar

与第一个直流电压正极端子相关联的电气守恒端口。

**数据类型：** `double`

### **1-** — 直流电压 1 负极 electrical | scalar

与第一个直流电压负极端子相关联的电气守恒端口。

**数据类型：** `double`

### **2+** — 直流电压 2 正极 electrical | scalar

与第二个直流电压正极端子相关联的电气守恒端口。

**数据类型：** `double`

### **2-** — 直流电压 2 负极 electrical | scalar

与第二个直流电压负极端子相关联的电气守恒端口。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 斩波器工作象限 First and second quadrant（默认）| First and fourth quadrant
  group: ''
- name: Switching device
  summary: 开关类型 Ideal Semiconductor Switch（默认）| GTO | IGBT | MOSFET | Thyristor | Averaged Switch
  group: 开关器件
- name: Forward voltage
  summary: 电压 0.8 Ohm（默认）| scalar
  group: 开关器件
- name: On-state resistance
  summary: 电阻 0.001 Ohm（默认）| scalar
  group: 开关器件
- name: Drain-source on resistance
  summary: 电阻 0.001 Ohm（默认）| scalar
  group: 开关器件
- name: Off-state conductance
  summary: 电导 1e-5 1/Ohm（默认）| scalar
  group: 开关器件
- name: Threshold voltage
  summary: 电压阈值 6 V（默认）| scalar
  group: 开关器件
- name: Gate trigger voltage, Vgt
  summary: 电压阈值 1 V（默认）| scalar
  group: 开关器件
- name: Gate turn-off voltage, Vgt_off
  summary: 电压阈值 -1 V（默认）| scalar
  group: 开关器件
- name: Holding current
  summary: 电流阈值 1 A（默认）| scalar
  group: 开关器件
- name: Model dynamics
  summary: 二极管模型 Diode with no dynamics（默认）| Diode with charge dynamics
  group: 保护二极管
- name: Forward voltage
  summary: 电压 0.8 V（默认）| scalar
  group: 保护二极管
- name: On resistance
  summary: 电阻 0.001 Ohm（默认）| scalar
  group: 保护二极管
- name: Off conductance
  summary: 电导 1e-5 1/Ohm（默认）| scalar
  group: 保护二极管
- name: Junction capacitance
  summary: 电容 50 nF（默认）| scalar
  group: 保护二极管
- name: Peak reverse current, iRM
  summary: 电流 -235 A（默认）| scalar less than 0
  group: 保护二极管
- name: Initial forward current when measuring iRM
  summary: 电流 300 A（默认）| scalar greater than 0
  group: 保护二极管
- name: Rate of change of current when measuring iRM
  summary: 电流变化率 -50 A/us（默认）| scalar
  group: 保护二极管
- name: Reverse recovery time parameterization
  summary: 恢复时间模型 Specify stretch factor（默认）| Specify reverse recovery time directly | Specify reverse recovery charge
  group: 保护二极管
- name: Reverse recovery time stretch factor
  summary: 拉伸因子 3（默认）| scalar greater than 1
  group: 保护二极管
- name: Reverse recovery time, trr
  summary: 时间 15 us（默认）| scalar
  group: 保护二极管
- name: Reverse recovery charge, Qrr
  summary: 电荷 1500 s*uA（默认）| scalar
  group: 保护二极管
- name: Snubber
  summary: 缓冲器模型 None（默认）| RC snubber
  group: 缓冲器
- name: Snubber resistance
  summary: 电阻 0.1 Ohm（默认）| scalar
  group: 缓冲器
- name: Snubber capacitance
  summary: 电容 1e-7（默认）| F | scalar
  group: 缓冲器
```

### **Modeling option** — 斩波器工作象限 `First and second quadrant`（默认）| `First and fourth quadrant`

选择建模的斩波器工作在第一和第二象限，还是第一和第四象限。

### 开关器件

下表显示了 **Switching Devices** 参数的可见性如何取决于您选择的 **Switching device**。要了解如何阅读该表，请参阅参数依赖关系。

**开关器件参数依赖关系**

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

### **Switching device** — 开关类型 `Ideal Semiconductor Switch`（默认）| `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

变换器的开关器件类型。

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Forward voltage** — 电压 `0.8` `Ohm`（默认）| scalar

对于不同的开关器件类型，**Forward voltage** 的含义如下：

- GTO — 使器件 I-V 特性梯度为 1/*Ron* 所需的阳极和阴极模块端口之间的最小电压，其中 *Ron* 为 **On-state resistance** 的值
- IGBT — 使二极管 I-V 特性梯度为 1/*Ron* 所需的集电极和发射极模块端口之间的最小电压，其中 *Ron* 为 **On-state resistance** 的值
- Thyristor — 使器件导通所需的最小电压

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **On-state resistance** — 电阻 `0.001` `Ohm`（默认）| scalar

对于不同的开关器件类型，**On-state resistance** 的含义如下：

- GTO — 正向电压以上电压对电流的变化率
- Ideal semiconductor switch — 器件导通时的阳极-阴极电阻
- IGBT — 器件导通时的集电极-发射极电阻
- Thyristor — 器件导通时的阳极-阴极电阻
- Averaged switch — 器件导通时的阳极-阴极电阻

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Drain-source on resistance** — 电阻 `0.001` `Ohm`（默认）| scalar

漏极和源极之间的电阻，该电阻还取决于栅极-源极电压。

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Off-state conductance** — 电导 `1e-5` `1/Ohm`（默认）| scalar

器件关断时的电导。该值必须小于 1/*R*，其中 *R* 为 **On-state resistance** 的值。

对于不同的开关器件类型，**On-state resistance** 的含义如下：

- GTO — 阳极-阴极电导
- Ideal semiconductor switch — 阳极-阴极电导
- IGBT — 集电极-发射极电导
- MOSFET — 漏极-源极电导
- Thyristor — 阳极-阴极电导

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Threshold voltage** — 电压阈值 `6` `V`（默认）| scalar

栅极电压阈值。当栅极电压高于此值时，器件导通。
对于不同的开关器件类型，所关注的器件电压为：

- Ideal semiconductor switch — 栅极-阴极电压
- IGBT — 栅极-发射极电压
- MOSFET — 栅极-源极电压

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Gate trigger voltage, Vgt** — 电压阈值 `1` `V`（默认）| scalar

栅极-阴极电压阈值。当栅极-阴极电压高于此值时，器件导通。

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Gate turn-off voltage, Vgt\_off** — 电压阈值 `-1` `V`（默认）| scalar

栅极-阴极电压阈值。当栅极-阴极电压低于此值时，器件关断。

#### 依赖关系

请参阅开关器件参数依赖关系表。

### **Holding current** — 电流阈值 `1` `A`（默认）| scalar

栅极电流阈值。当电流高于此值时，即使栅极-阴极电压降至栅极触发电压以下，器件仍保持导通。

#### 依赖关系

请参阅开关器件参数依赖关系表。

### 保护二极管

**Diode** 参数的可见性取决于您如何配置保护二极管的 **Model dynamics** 和 **Reverse recovery time parameterization** 参数。要了解如何阅读该表，请参阅参数依赖关系。

**保护二极管参数依赖关系**

| 参数和选项 | | | |
| --- | --- | --- | --- |
| **Model dynamics** | | | |
| *Diode with no dynamics* | *Diode with charge dynamics* | | |
| Forward voltage | Forward voltage | | |
| On resistance | On resistance | | |
| Off conductance | Off conductance | | |
| Junction capacitance | | |
| Peak reverse current, iRM | | |
| Initial forward current when measuring iRM | | |
| Rate of change of current when measuring iRM | | |
| **Reverse recovery time parameterization** | | |
| *`Specify stretch factor`* | *`Specify reverse recovery time directly`* | *`Specify reverse recovery charge`* |
| Reverse recovery time stretch factor | Reverse recovery time, trr | Reverse recovery charge, Qrr |

### **Model dynamics** — 二极管模型 `Diode with no dynamics`（默认）| `Diode with charge dynamics`

二极管类型。选项包括：

- `Diode with no dynamics` — 选择此选项以使用 Diode 模块优先考虑仿真速度。
- `Diode with charge dynamics` — 选择此选项以使用 Diode 模块的换流二极管模型，在反向模式电荷动态方面优先考虑模型保真度。

**注意**

如果您在 **Switching Device** 设置中为 **Switching Device** 参数选择 `Averaged Switch`，则此参数不可见，并且会自动选择 `Diode with no dynamics`。

#### 依赖关系

请参阅保护二极管参数依赖关系表。

### **Forward voltage** — 电压 `0.8` `V`（默认）| scalar

使二极管 I-V 特性梯度为 1/*Ron* 所需的正极和负极模块端口之间的最小电压，其中 *Ron* 为 **On resistance** 的值。

### **On resistance** — 电阻 `0.001` `Ohm`（默认）| scalar

**Forward voltage** 以上电压对电流的变化率。

### **Off conductance** — 电导 `1e-5` `1/Ohm`（默认）| scalar

反向偏置二极管的电导。

### **Junction capacitance** — 电容 `50` `nF`（默认）| scalar

二极管结电容。

#### 依赖关系

请参阅保护二极管参数依赖关系表。

### **Peak reverse current, iRM** — 电流 `-235` `A`（默认）| scalar less than `0`

由外部测试电路测得的峰值反向电流。

#### 依赖关系

请参阅保护二极管参数依赖关系表。

### **Initial forward current when measuring iRM** — 电流 `300` `A`（默认）| scalar greater than `0`

测量峰值反向电流时的初始正向电流。该值必须大于零。

#### 依赖关系

请参阅保护二极管参数依赖关系表。

### **Rate of change of current when measuring iRM** — 电流变化率 `-50` `A/us`（默认）| scalar

测量峰值反向电流时的电流变化率。

#### 依赖关系

请参阅保护二极管参数依赖关系表。

### **Reverse recovery time parameterization** — 恢复时间模型 `Specify stretch factor`（默认）| `Specify reverse recovery time directly` | `Specify reverse recovery charge`

用于参数化恢复时间的模型。当您选择 `Specify stretch factor` 或 `Specify reverse recovery charge` 时，可以指定一个值，模块使用该值来推导反向恢复时间。有关这些选项的更多信息，请参阅 How the Block Calculates TM and Tau。

#### 依赖关系

请参阅保护二极管参数依赖关系表。

### **Reverse recovery time stretch factor** — 拉伸因子 `3`（默认）| scalar greater than `1`

模块用于计算 **Reverse recovery time, trr** 的值。与指定反向恢复电荷相比，指定拉伸因子是参数化反向恢复时间的一种更简单的方法。拉伸因子的值越大，反向恢复电流消散所需的时间越长。

#### 依赖关系

请参阅保护二极管参数依赖关系表。

### **Reverse recovery time, trr** — 时间 `15` `us`（默认）| scalar

电流最初降至零（二极管关断时）与电流降至峰值反向电流的 10% 以下之间的时间间隔。

**Reverse recovery time, trr** 参数的值必须大于 **Peak reverse current, iRM** 参数的值除以 **Rate of change of current when measuring iRM** 参数的值。

#### 依赖关系

请参阅保护二极管参数依赖关系表。

### **Reverse recovery charge, Qrr** — 电荷 `1500` `s*uA`（默认）| scalar

模块用于计算 **Reverse recovery time, trr** 的值。如果您的二极管器件数据手册指定了反向恢复电荷的值而不是反向恢复时间的值，请使用此参数。

反向恢复电荷是二极管关断时继续消散的总电荷。该值必须小于 −i2RM2a，

其中：

- *iRM* 是为 **Peak reverse current, iRM** 指定的值。
- *a* 是为 **Rate of change of current when measuring iRM** 指定的值。

#### 依赖关系

请参阅保护二极管参数依赖关系表。

### 缓冲器

如果将 **Switching device** 设置为 `Averaged Switch`，则 **Snubbers** 参数选项卡不可见。

下表总结了 **Snubbers** 参数依赖关系。要了解如何阅读该表，请参阅参数依赖关系。

**缓冲器参数依赖关系**

| 缓冲器参数依赖关系 | |
| --- | --- |
| **Snubber** | |
| *`None`* | *`RC Snubber`* |
| Snubber resistance |
| Snubber capacitance |

### **Snubber** — 缓冲器模型 `None`（默认）| `RC snubber`

开关器件缓冲器。

#### 依赖关系

请参阅缓冲器参数依赖关系表。

### **Snubber resistance** — 电阻 `0.1` `Ohm`（默认）| scalar

开关器件缓冲器的电阻。

#### 依赖关系

请参阅缓冲器参数依赖关系表。

### **Snubber capacitance** — 电容 `1e-7`（默认）| `F` | scalar

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

**在 R2018a 中引入**

## 描述

两象限受控 DC-DC 斩波器

Two-Quadrant Chopper 模块表示一个两象限受控斩波器，用于将固定直流输入转换为可变直流输出。该模块包含两个开关器件。开关器件类型的选项包括：

- GTO — 门极关断晶闸管。有关该器件 I-V 特性的信息，请参阅 GTO。
- Ideal semiconductor switch — 有关该器件 I-V 特性的信息，请参阅 Ideal Semiconductor Switch。
- IGBT — 绝缘栅双极晶体管。有关该器件 I-V 特性的信息，请参阅 IGBT (Ideal, Switching)。
- MOSFET — N 沟道金属氧化物半导体场效应晶体管。有关该器件 I-V 特性的信息，请参阅 MOSFET (Ideal, Switching)。
- Thyristor — 有关该器件 I-V 特性的信息，请参阅 Thyristor (Piecewise Linear)。
- Averaged Switch — 带反并联二极管的半导体开关。控制信号端口 **G** 接受区间 [0,1] 内的值。当 **G** 等于 `0` 或 `1` 时，平均开关分别完全断开或完全闭合。该开关的行为类似于带反并联二极管的 Ideal Semiconductor Switch 模块。当 **G** 介于 0 和 1 之间时，平均开关部分断开。您可以在指定周期内对脉宽调制（PWM）信号取平均。然后可以对模型进行欠采样，并使用调制波形代替 PWM 信号。

### 指定斩波器象限

您可以选择 Two-Quadrant Chopper 工作的象限。要选择象限，请将 **Modeling option** 参数设置为以下之一：

- `First and second quadrant`。图中显示了第一和第二象限模型的等效电路和工作原理。
- `First and fourth quadrant`。图中显示了第一和第四象限模型的等效电路和工作原理。

### 保护

该模块为每个开关器件包含一个集成保护二极管。集成二极管通过为反向电流提供导通路径来保护半导体器件。当半导体器件突然切断负载的电压供应时，感性负载可能产生高反向电压尖峰。

要配置内部保护二极管模块，请使用 **Diode** 参数。下表显示了如何根据您的目标设置 **Model dynamics** 参数。

| 目标 | 要选择的值 | 集成保护二极管 |
| --- | --- | --- |
| 优先考虑仿真速度。 | `Diode with no dynamics` | Diode 模块 |
| 通过精确指定反向模式电荷动态来优先考虑模型保真度。 | `Diode with charge dynamics` | Diode 模块的动态模型 |

您还可以为每个开关器件包含缓冲电路。缓冲电路包含串联连接的电阻和电容。它们保护开关器件免受感性负载在器件切断负载电压供应时产生的高电压的影响。缓冲电路还可以防止开关器件导通时出现过大的电流变化率。

要为每个开关器件包含并配置缓冲电路，请使用 **Snubbers** 参数。

### Gate Control

要将 Simulink® 门控电压信号连接到内部开关器件的栅极端口：

1. 使用 Simulink-PS Converter 模块转换每个电压信号。
2. 使用 Two-Pulse Gate Multiplexer 模块将转换后的栅极信号多路复用为单个向量。
3. 将该向量信号连接到 **G** 端口。

### Piecewise Constant Approximation in Averaged Switch for FPGA Deployment

如果将 **Switching device** 参数设置为 `Averaged switch`，并且您的模型使用分区求解器，则该模块会产生非线性分区，因为平均模式方程包含作为输入 **G** 函数的模式 *Gsat*。为了使这些方程与硬件描述语言 (HDL) 代码生成兼容，从而支持 FPGA 部署，请将 **Integer for piecewise constant approximation of gate input (0 for disabled)** 参数设置为大于 `0` 的值。该模块随后会将 *Gsat* 模式视为具有固定范围的分段常数整数。这会将先前的非线性分区转换为线性时变分区。

范围 `[0,K]` 内的整数值（其中 *K* 是 **Integer for piecewise constant approximation of gate input (0 for disabled)** 的值）现在与范围 `[0,1]` 内的每个实值模式相关联。该模块通过将原始模式除以 K 将其归一化回范围 `[0,1]` 来计算分段常数模式：

uI=(floor(u⋅K))u^=uIK
