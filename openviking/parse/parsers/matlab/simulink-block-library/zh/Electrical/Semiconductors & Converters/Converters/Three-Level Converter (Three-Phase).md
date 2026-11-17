---
type: simulink-block
title: 'Three-Level Converter (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'threelevelconverterthreephase'
documentation_source_path: 'ref/threelevelconverterthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Three-Level Converter (Three-Phase)

## 端口
```yaml
ports:
- name: G
  summary: 门极端子 electrical
  direction: conserving
- name: '~'
  summary: 三相端口 electrical
  direction: conserving
- name: a
  summary: '*a* 相 electrical'
  direction: conserving
- name: b
  summary: '*b* 相 electrical'
  direction: conserving
- name: c
  summary: '*c* 相 electrical'
  direction: conserving
- name: +
  summary: 正极端子 electrical
  direction: conserving
- name: '0'
  summary: 中性端子 electrical
  direction: conserving
- name: '-'
  summary: 负极端子 electrical
  direction: conserving
```

### 守恒端口

### **G** — 门极端子 electrical

与开关器件门极端子关联的矢量输入端口。将此端口连接到一个 Twelve-Pulse Gate Multiplexer 模块。

### **~** — 三相端口 electrical

可扩展三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`。

### **a** — *a* 相 electrical

与 *a* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **b** — *b* 相 electrical

与 *b* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **c** — *c* 相 electrical

与 *c* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **+** — 正极端子 electrical

与直流正极端子关联的电气守恒端口。

### **0** — 中性端子 electrical

与直流中性端子关联的电气守恒端口。

### **-** — 负极端子 electrical

与直流负极端子关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Electrical connection
  summary: 电气连接 Composite three-phase ports（默认）| Expanded three-phase ports
  group: ''
- name: Switching device
  summary: 开关器件 Ideal Semiconductor Switch（默认）| GTO | IGBT | MOSFET | Averaged Switch
  group: ''
- name: Forward voltage, Vf
  summary: 正向电压 0.8 V（默认）
  group: 'Switching Devices: GTO'
- name: On-state resistance
  summary: 导通电阻 0.001 Ohm（默认）
  group: 'Switching Devices: GTO'
- name: Off-state Conductance
  summary: 关断电导 1e-6 1/Ohm（默认）
  group: 'Switching Devices: GTO'
- name: Gate trigger voltage, Vgt
  summary: 门极触发电压 1 V（默认）
  group: 'Switching Devices: GTO'
- name: Gate turn-off voltage, Vgt_off
  summary: 门极关断电压 -1 V（默认）
  group: 'Switching Devices: GTO'
- name: Holding current
  summary: 维持电流 1 A（默认）
  group: 'Switching Devices: GTO'
- name: On-state resistance
  summary: 导通电阻 0.001 Ohm（默认）
  group: 'Switching Devices: Ideal Semiconductor Switch'
- name: Off-state Conductance
  summary: 关断电导 1e-6 1/Ohm（默认）
  group: 'Switching Devices: Ideal Semiconductor Switch'
- name: Threshold voltage, Vth
  summary: 阈值电压 6 V（默认）
  group: 'Switching Devices: Ideal Semiconductor Switch'
- name: Forward voltage, Vf
  summary: 正向电压 0.8 V（默认）
  group: 'Switching Devices: IGBT'
- name: On-state resistance
  summary: 导通电阻 0.001 Ohm（默认）
  group: 'Switching Devices: IGBT'
- name: Off-state Conductance
  summary: 关断电导 1e-6 1/Ohm（默认）
  group: 'Switching Devices: IGBT'
- name: Threshold voltage, Vth
  summary: 阈值电压 6 V（默认）
  group: 'Switching Devices: IGBT'
- name: Drain-source on resistance, R_DS(on)
  summary: 漏源导通电阻 0.001 Ohm（默认）
  group: 'Switching Devices: MOSFET'
- name: Off-state Conductance
  summary: 关断电导 1e-6 1/Ohm（默认）
  group: 'Switching Devices: MOSFET'
- name: Threshold voltage, Vth
  summary: 阈值电压 6 V（默认）
  group: 'Switching Devices: MOSFET'
- name: On-state resistance
  summary: 导通电阻 0.001 Ohm（默认）
  group: 'Switching Devices: Averaged Switch'
- name: Integer for piecewise constant approximation of gate input (0 for disabled)
  summary: 用于 FPGA 部署的整数模式 0（默认）| 非负标量
  group: 'Switching Devices: Averaged Switch'
- name: Integral protection diode
  summary: 集成保护二极管 Diode with no dynamics（默认）| Diode with charge dynamics
  group: 集成二极管
- name: Forward voltage
  summary: 正向电压 0.8 V（默认）
  group: 集成二极管
- name: On resistance
  summary: 导通电阻 0.001 Ohm（默认）
  group: 集成二极管
- name: Off conductance
  summary: 关断电导 1e-5 1/Ohm（默认）
  group: 集成二极管
- name: Junction capacitance
  summary: 结电容 50e-9 F（默认）
  group: 集成二极管
- name: Peak reverse current, iRM
  summary: 峰值反向电流 -235 A（默认）| 负标量
  group: 集成二极管
- name: Initial forward current when measuring iRM
  summary: 测量 iRM 时的初始正向电流 300 A（默认）| 正标量
  group: 集成二极管
- name: Rate of change of current when measuring iRM
  summary: 测量 iRM 时的电流变化率 -50A/μs（默认）| 负标量
  group: 集成二极管
- name: Reverse recovery time parameterization
  summary: 反向恢复时间参数化 Specify reverse recovery time directly（默认）| Specify stretch factor | Specify reverse recovery charge
  group: 集成二极管
- name: Reverse recovery time, trr
  summary: 反向恢复时间 15 μs（默认）
  group: 集成二极管
- name: Reverse recovery time stretch factor
  summary: 反向恢复时间拉伸因子 3（默认）
  group: 集成二极管
- name: Reverse recovery charge, Qrr
  summary: 反向恢复电荷 1500 μAs（默认）
  group: 集成二极管
- name: Snubber
  summary: 缓冲器 None（默认）| RC snubber
  group: 缓冲器
- name: Snubber resistance
  summary: 缓冲电阻 0.1 Ohm（默认）
  group: 缓冲器
- name: Snubber capacitance
  summary: 缓冲电容 1e-7 F（默认）
  group: 缓冲器
```

### **Electrical connection** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

选择使用复合三相端口还是扩展三相端口。

### **Switching device** — 开关器件 `Ideal Semiconductor Switch`（默认）| `GTO` | `IGBT` | `MOSFET` | `Averaged Switch`

变换器开关器件。默认值为 `Ideal Semiconductor Switch`。

可供选择的开关器件包括：

- Switching Devices: GTO
- Switching Devices: Ideal Semiconductor Switch
- Switching Devices: IGBT
- Switching Devices: MOSFET
- Switching Devices: Averaged Switch

#### 依赖关系

根据所选特定开关器件的不同，将显示多个附加参数。

### Switching Devices: GTO

有关详细信息，请参阅 GTO。

仅当在 **Switching device** 参数中选择此开关器件时，该开关器件的参数才会显示。

### **Forward voltage, Vf** — 正向电压 `0.8` `V`（默认）

使器件 i-v 特性的斜率为 1/Ron 时，阳极和阴极块端口两端所需的最小电压，其中 Ron 为 **On-state resistance** 的值。

### **On-state resistance** — 导通电阻 `0.001` `Ohm`（默认）

高于正向电压时电压随电流的变化率。

### **Off-state Conductance** — 关断电导 `1e-6` `1/Ohm`（默认）

器件关断时的阳极-阴极电导。该值必须小于 1/R，其中 R 为 **On-state resistance** 的值。

### **Gate trigger voltage, Vgt** — 门极触发电压 `1` `V`（默认）

门极-阴极电压阈值。当门极-阴极电压高于此值时，器件导通。

### **Gate turn-off voltage, Vgt\_off** — 门极关断电压 `-1` `V`（默认）

门极-阴极电压阈值。当门极-阴极电压低于此值时，器件关断。

### **Holding current** — 维持电流 `1` `A`（默认）

电流阈值。当电流高于此值时，即使门极-阴极电压降至门极触发电压以下，器件仍保持导通。

### Switching Devices: Ideal Semiconductor Switch

有关详细信息，请参阅 Ideal Semiconductor Switch。

仅当在 **Switching device** 参数中选择此开关器件时，该开关器件的参数才会显示。

### **On-state resistance** — 导通电阻 `0.001` `Ohm`（默认）

器件导通时的阳极-阴极电阻。

### **Off-state Conductance** — 关断电导 `1e-6` `1/Ohm`（默认）

器件关断时的阳极-阴极电导。该值必须小于 1/R，其中 R 为 **On-state resistance** 的值。

### **Threshold voltage, Vth** — 阈值电压 `6` `V`（默认）

门极-阴极电压阈值。当门极-阴极电压高于此值时，器件导通。

### Switching Devices: IGBT

有关详细信息，请参阅 IGBT (Ideal, Switching)。

仅当在 **Switching device** 参数中选择此开关器件时，该开关器件的参数才会显示。

### **Forward voltage, Vf** — 正向电压 `0.8` `V`（默认）

使二极管 i-v 特性的斜率为 1/Ron 时，集电极和发射极块端口两端所需的最小电压，其中 Ron 为 **On-state resistance** 的值。

### **On-state resistance** — 导通电阻 `0.001` `Ohm`（默认）

器件导通时的集电极-发射极电阻。

### **Off-state Conductance** — 关断电导 `1e-6` `1/Ohm`（默认）

器件关断时的集电极-发射极电导。该值必须小于 1/R，其中 R 为 **On-state resistance** 的值。

### **Threshold voltage, Vth** — 阈值电压 `6` `V`（默认）

器件导通时的门极-发射极电压。

### Switching Devices: MOSFET

有关详细信息，请参阅 MOSFET (Ideal, Switching)。

仅当在 **Switching device** 参数中选择此开关器件时，该开关器件的参数才会显示。

### **Drain-source on resistance, R\_DS(on)** — 漏源导通电阻 `0.001` `Ohm`（默认）

器件导通时的漏源电阻。

### **Off-state Conductance** — 关断电导 `1e-6` `1/Ohm`（默认）

器件关断时的漏源电导。该值必须小于 1/R，其中 R 为 **On-state resistance** 的值。

### **Threshold voltage, Vth** — 阈值电压 `6` `V`（默认）

门极-源极电压阈值。当门极-源极电压高于此值时，器件导通。

### Switching Devices: Averaged Switch

仅当在 **Switching device** 参数中选择此开关器件时，该开关器件的参数才会显示。

### **On-state resistance** — 导通电阻 `0.001` `Ohm`（默认）

器件导通时的阳极-阴极电阻。

### **Integer for piecewise constant approximation of gate input (0 for disabled)** — 用于 FPGA 部署的整数模式 `0`（默认）| 非负标量

用于对门极输入进行分段常数近似以进行 FPGA 部署的整数。

#### 依赖关系

要启用此参数，请将 **Switching device** 设置为 `Averaged Switch`。

### 集成二极管

### **Integral protection diode** — 集成保护二极管 `Diode with no dynamics`（默认）| `Diode with charge dynamics`

每个开关器件的集成保护二极管。

可供选择的二极管包括：

- `Diode with no dynamics`
- `Diode with charge dynamics`

**注意**

如果在 **Switching Device** 设置中为 **Switching Device** 参数选择 `Averaged Switch`，则此参数不可见，并自动选择 `Diode with no dynamics`。

### **Forward voltage** — 正向电压 `0.8` `V`（默认）

使二极管 I-V 特性的斜率为 1/Ron 时，`+` 和 `-` 块端口两端所需的最小电压，其中 Ron 为 **On resistance** 的值。

### **On resistance** — 导通电阻 `0.001` `Ohm`（默认）

高于 **Forward voltage** 时电压随电流的变化率。

### **Off conductance** — 关断电导 `1e-5` `1/Ohm`（默认）

反向偏置二极管的电导。

### **Junction capacitance** — 结电容 `50e-9` `F`（默认）

二极管结电容。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Diode with charge dynamics`。

### **Peak reverse current, iRM** — 峰值反向电流 `-235` `A`（默认）| 负标量

由外部测试电路测得的峰值反向电流。此值必须小于零。默认值为 `-235` `A`。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Diode with charge dynamics`。

### **Initial forward current when measuring iRM** — 测量 iRM 时的初始正向电流 `300` `A`（默认）| 正标量

测量峰值反向电流时的初始正向电流。此值必须大于零。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Diode with charge dynamics`。

### **Rate of change of current when measuring iRM** — 测量 iRM 时的电流变化率 `-50``A/μs`（默认）| 负标量

测量峰值反向电流时的电流变化率。此值必须小于零。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Diode with charge dynamics`。

### **Reverse recovery time parameterization** — 反向恢复时间参数化 `Specify reverse recovery time directly`（默认）| `Specify stretch factor` | `Specify reverse recovery charge`

确定如何在模块中指定反向恢复时间。默认值为 `Specify reverse recovery time directly`。

如果选择 `Specify stretch factor` 或 `Specify reverse recovery charge`，则需要指定一个值，模块将使用该值推导反向恢复时间。有关这些选项的详细信息，请参阅 How the Block Calculates TM and Tau。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Diode with charge dynamics`。

### **Reverse recovery time, trr** — 反向恢复时间 `15` `μs`（默认）

电流最初降至零（二极管关断时）到电流降至峰值反向电流的 10% 以下之间的时间间隔。**Reverse recovery time, trr** 参数的值必须大于 **Peak reverse current, iRM** 参数的值除以 **Rate of change of current when measuring iRM** 参数的值。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Diode with charge dynamics`，并将 **Reverse recovery time parameterization** 设置为 `Specify reverse recovery time directly`。

### **Reverse recovery time stretch factor** — 反向恢复时间拉伸因子 `3`（默认）

模块用于计算 **Reverse recovery time, trr** 的值。此值必须大于 `1`。指定拉伸因子比指定反向恢复电荷更容易参数化反向恢复时间。拉伸因子的值越大，反向恢复电流消散所需的时间越长。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Diode with charge dynamics`，并将 **Reverse recovery time parameterization** 设置为 `Specify stretch factor`。

### **Reverse recovery charge, Qrr** — 反向恢复电荷 `1500` `μAs`（默认）

模块用于计算 **Reverse recovery time, trr** 的值。如果您的二极管器件数据手册指定了反向恢复电荷的值而不是反向恢复时间的值，请使用此参数。

反向恢复电荷是二极管关断时继续消散的总电荷。该值必须小于 −i2RM2a，

其中：

- *iRM* 是为 **Peak reverse current, iRM** 指定的值。
- *a* 是为 **Rate of change of current when measuring iRM** 指定的值。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Diode with charge dynamics`，并将 **Reverse recovery time parameterization** 设置为 `Specify reverse recovery charge`。

有关这些参数的详细信息，请参阅 Diode。

### 缓冲器

如果将 **Switching device** 设置为 `Averaged Switch`，则 **Snubbers** 参数选项卡不可见。

### **Snubber** — 缓冲器 `None`（默认）| `RC snubber`

每个开关器件的缓冲器：

- `None` - 这是默认值。
- `RC snubber`

### **Snubber resistance** — 缓冲电阻 `0.1` `Ohm`（默认）

缓冲电阻。

#### 依赖关系

仅当 **Snubber** 参数设置为 `RC snubber` 时，此参数才可见。

### **Snubber capacitance** — 缓冲电容 `1e-7` `F`（默认）

缓冲电容。

#### 依赖关系

仅当 **Snubber** 参数设置为 `RC snubber` 时，此参数才可见。
## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014b 中引入**

### R2021b：电气连接端口更新

从 R2021b 开始，要在复合端口和扩展端口之间切换，请将 **Electrical connection** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。

由于这些更改，在早期版本中保存的模型内，请检查此模块的 **Electrical connection** 参数。

## 描述

十二脉冲三相三电平中性点钳位受控变换器

Three-Level Converter (Three-Phase) 模块对十二脉冲三相三电平中性点钳位受控变换器进行建模。您可以使用此模块将三相交流网络连接到三电平直流网络。

### Model

该模块包含三个桥臂，每个桥臂有四个开关器件及相关的反并联二极管。开关器件类型选项包括：

- GTO — 门极关断晶闸管。有关该器件的 I-V 特性信息，请参阅 GTO。
- Ideal semiconductor switch — 有关该器件的 I-V 特性信息，请参阅 Ideal Semiconductor Switch。
- IGBT — 绝缘栅双极型晶体管。有关该器件的 I-V 特性信息，请参阅 IGBT (Ideal, Switching)。
- MOSFET — N 沟道金属氧化物半导体场效应晶体管。有关该器件的 I-V 特性信息，请参阅 MOSFET (Ideal, Switching)。
- Averaged Switch — 带反并联二极管的半导体开关。控制信号端口 **G** 接受 `[0,1]` 区间内的值。当端口 **G** 的值等于 `0` 或 `1` 时，平均开关要么完全断开，要么完全闭合，其行为类似于带反并联二极管的 Ideal Semiconductor Switch 模块。当端口 **G** 的值介于 `0` 和 `1` 之间时，平均开关部分断开。然后可以在指定周期内对 PWM 信号取平均。这允许对模型进行欠采样，或使用调制波形代替 PWM 信号。

三桥臂电路中的每个组件都是您指定的相同开关器件。这些开关器件与 **Semiconductors** > **Fundamental Components** 子库中的器件相同。

该图展示了使用 Ideal Semiconductor 模块作为开关器件的模块等效电路。

您通过 Three-Level Converter (Three-Phase) 模块 **G** 端口的输入来控制 12 个开关器件的门极端口。

1. 使用 Twelve-Pulse Gate Multiplexer 模块将所有 12 个门极信号多路复用为单个向量。
2. 将 Twelve-Pulse Gate Multiplexer 模块的输出连接到 Three-Level Converter (Three-Phase) 模块的 **G** 端口。

您使用模块对话框的 **Diodes** 选项卡为每个开关器件包含一个集成保护二极管。集成二极管通过为反向电流提供导通路径来保护半导体器件。当半导体器件突然切断负载的电压供应时，感性负载可能产生高反向电压尖峰。

下表显示了如何根据您的目标设置 **Integral protection diode** 参数。

| 目标 | 要选择的值 | 集成保护二极管 |
| --- | --- | --- |
| 优先考虑仿真速度。 | `Diode with no dynamics` | Diode 模块 |
| 通过精确指定反向模式电荷动态来优先考虑模型保真度。 | `Diode with charge dynamics` | Diode 模块的动态模型 |

您使用模块对话框的 **Snubbers** 选项卡为每个开关器件包含一个缓冲电路。每个缓冲电路由一个电阻和一个电容串联组成。通常，缓冲电路保护开关器件免受感性负载在器件切断负载电压供应时产生的极高电压的影响。缓冲电路还可以防止开关器件导通时电流变化率过大。

### Piecewise Constant Approximation in Averaged Switch for FPGA Deployment

如果将 **Switching device** 参数设置为 `Averaged switch`，并且您的模型使用分区求解器，则该模块会产生非线性分区，因为平均模式方程包含作为输入 **G** 函数的模式 *Gsat*。为了使这些方程与硬件描述语言 (HDL) 代码生成兼容，从而支持 FPGA 部署，请将 **Integer for piecewise constant approximation of gate input (0 for disabled)** 参数设置为大于 `0` 的值。然后，该模块将 *Gsat* 模式视为具有固定范围的分段常数整数。这将之前的非线性分区转换为线性时变分区。

范围 `[0,K]` 内的整数值（其中 *K* 是 **Integer for piecewise constant approximation of gate input (0 for disabled)** 的值）现在与范围 `[0,1]` 内的每个实值模式相关联。该模块通过将原始模式除以 K 将其归一化回范围 `[0,1]` 来计算分段常数模式：

uI=(floor(u⋅K))u^=uIK
