---
type: simulink-block
title: 'Three-Level Converter (Three-Phase)'
family: 'semiconductors-converters'
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

### 守恒端口

### **G** — 栅极端子 electrical

与开关器件栅极端子关联的矢量输入端口。将此端口连接到一个 Twelve-Pulse Gate Multiplexer 模块。

### **~** — 三相端口 electrical

可扩展三相端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`。

### **a** — *a* 相 electrical

与 *a* 相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **b** — *b* 相 electrical

与 *b* 相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **c** — *c* 相 electrical

与 *c* 相相关的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **+** — 正极端子 electrical

与直流正极端子相关的电气守恒端口。

### **0** — 中性点端子 electrical

与直流中性点端子相关的电气守恒端口。

### **-** — 负极端子 electrical

与直流负极端子相关的电气守恒端口。

## 参数

### **Electrical connection** — Electrical connection `Composite three-phase ports` (default) | `Expanded three-phase ports`

是否使用复合三相端口或展开三相端口。

### **Switching device** — Switching device `Ideal Semiconductor Switch` (default) | `GTO` | `IGBT` | `MOSFET` | `Averaged Switch`

变换器开关器件。默认值为 `Ideal Semiconductor Switch`。

可选择的开关器件包括：

- 开关器件：GTO
- 开关器件：Ideal Semiconductor Switch
- 开关器件：IGBT
- 开关器件：MOSFET
- 开关器件：Averaged Switch

#### 依赖关系

根据所选特定开关器件，将会显示多个附加参数。

### 开关器件：GTO

有关详细信息，请参阅 GTO。

仅当你在 **Switching device** 参数中选择此开关器件时，才会显示该开关器件的参数。

### **Forward voltage, Vf** — Forward voltage `0.8` `V` (default)

为使器件 i-v 特性的斜率为 1/Ron，阳极和阴极块端口之间所需的最小电压，其中 Ron 是 **On-state resistance** 的值。

### **On-state resistance** — On-state resistance `0.001` `Ohm` (default)

在正向电压以上，电压相对于电流的变化率。

### **Off-state Conductance** — Off-state conductance `1e-6` `1/Ohm` (default)

器件关断时的阳极-阴极电导。该值必须小于 1/R，其中 R 是 **On-state resistance** 的值。

### **Gate trigger voltage, Vgt** — Gate trigger voltage `1` `V` (default)

栅极-阴极电压阈值。当栅极-阴极电压高于此值时，器件导通。

### **Gate turn-off voltage, Vgt\_off** — Gate turn-off voltage `-1` `V` (default)

栅极-阴极电压阈值。当栅极-阴极电压低于此值时，器件关断。

### **Holding current** — Holding current `1` `A` (default)

电流阈值。当电流高于此值时，即使栅极-阴极电压降至栅极触发电压以下，器件仍保持导通。

### 开关器件：Ideal Semiconductor Switch

有关详细信息，请参阅 Ideal Semiconductor Switch。

仅当你在 **Switching device** 参数中选择此开关器件时，才会显示该开关器件的参数。

### **On-state resistance** — On-state resistance `0.001` `Ohm` (default)

器件导通时的阳极-阴极电阻。

### **Off-state Conductance** — Off-state conductance `1e-6` `1/Ohm` (default)

器件关断时的阳极-阴极电导。该值必须小于 1/R，其中 R 是 **On-state resistance** 的值。

### **Threshold voltage, Vth** — Threshold voltage `6` `V` (default)

栅极-阴极电压阈值。当栅极-阴极电压高于此值时，器件导通。

### 开关器件：IGBT

有关详细信息，请参阅 IGBT (Ideal, Switching)。

仅当你在 **Switching device** 参数中选择此开关器件时，才会显示该开关器件的参数。

### **Forward voltage, Vf** — Forward voltage `0.8` `V` (default)

为使二极管 i-v 特性的斜率为 1/Ron，集电极和发射极块端口之间所需的最小电压，其中 Ron 是 **On-state resistance** 的值。

### **On-state resistance** — On-state resistance `0.001` `Ohm` (default)

器件导通时的集电极-发射极电阻。

### **Off-state Conductance** — Off-state conductance `1e-6` `1/Ohm` (default)

器件关断时的集电极-发射极电导。该值必须小于 1/R，其中 R 是 **On-state resistance** 的值。

### **Threshold voltage, Vth** — Threshold voltage `6` `V` (default)

使器件导通的栅极-发射极电压。

### 开关器件：MOSFET

有关详细信息，请参阅 MOSFET (Ideal, Switching)。

仅当你在 **Switching device** 参数中选择此开关器件时，才会显示该开关器件的参数。

### **Drain-source on resistance, R\_DS(on)** — Drain-source on resistance `0.001` `Ohm` (default)

器件导通时的漏极-源极电阻。

### **Off-state Conductance** — Off-state conductance `1e-6` `1/Ohm` (default)

器件关断时的漏极-源极电导。该值必须小于 1/R，其中 R 是 **On-state resistance** 的值。

### **Threshold voltage, Vth** — Threshold voltage `6` `V` (default)

栅极-源极电压阈值。当栅极-源极电压高于此值时，器件导通。

### 开关器件：Averaged Switch

仅当你在 **Switching device** 参数中选择此开关器件时，才会显示该开关器件的参数。

### **On-state resistance** — On-state resistance `0.001` `Ohm` (default)

器件导通时的阳极-阴极电阻。

### **Integer for piecewise constant approximation of gate input (0 for disabled)** — Integer mode for FPGA deployment `0` (default) | nonnegative scalar

用于对 FPGA 部署的栅极输入执行分段常数近似的整数。

#### 依赖关系

要启用此参数，请将 **Switching device** 设置为 `Averaged Switch`。

### 集成二极管

### **Integral protection diode** — Integral protection diode `Diode with no dynamics` (default) | `Diode with charge dynamics`

每个开关器件的集成保护二极管。

可选择的二极管包括：

- `Diode with no dynamics`
- `Diode with charge dynamics`

**注意**

如果你在 **Switching Device** 设置中为 **Switching Device** 参数选择 `Averaged Switch`，则此参数不可见，并且会自动选择 `Diode with no dynamics`。

### **Forward voltage** — Forward voltage `0.8` `V` (default)

为使二极管 I-V 特性的斜率为 1/Ron，`+` 和 `-` 块端口之间所需的最小电压，其中 Ron 是 **On resistance** 的值。

### **On resistance** — On resistance `0.001` `Ohm` (default)

在 **Forward voltage** 以上，电压相对于电流的变化率。

### **Off conductance** — Off conductance `1e-5` `1/Ohm` (default)

反向偏置二极管的电导。

### **Junction capacitance** — Junction capacitance `50e-9` `F` (default)

二极管结电容。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Diode with charge dynamics`。

### **Peak reverse current, iRM** — Peak reverse current `-235` `A` (default) | negative scalar

由外部测试电路测得的峰值反向电流。该值必须小于零。默认值为 `-235` `A`。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Diode with charge dynamics`。

### **Initial forward current when measuring iRM** — Initial forward current when measuring iRM `300` `A` (default) | positive scalar

测量峰值反向电流时的初始正向电流。该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Diode with charge dynamics`。

### **Rate of change of current when measuring iRM** — Rate of change of current when measuring iRM `-50``A/μs` (default) | negative scalar

测量峰值反向电流时的电流变化率。该值必须小于零。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Diode with charge dynamics`。

### **Reverse recovery time parameterization** — Reverse recovery time parameterization `Specify reverse recovery time directly` (default) | `Specify stretch factor` | `Specify reverse recovery charge`

确定在模块中如何指定反向恢复时间。默认值为 `Specify reverse recovery time directly`。

如果你选择 `Specify stretch factor` 或 `Specify reverse recovery charge`，则需指定一个值，模块将使用该值推导反向恢复时间。有关这些选项的详细信息，请参阅模块如何计算 TM 和 Tau。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Diode with charge dynamics`。

### **Reverse recovery time, trr** — Reverse recovery time `15` `μs` (default)

电流最初降为零（二极管关断时）的时刻与电流降至峰值反向电流 10% 以下的时刻之间的时间间隔。**Reverse recovery time, trr** 参数的值必须大于 **Peak reverse current, iRM** 参数的值除以 **Rate of change of current when measuring iRM** 参数的值。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Diode with charge dynamics`，并将 **Reverse recovery time parameterization** 设置为 `Specify reverse recovery time directly`。

### **Reverse recovery time stretch factor** — Reverse recovery time stretch factor `3` (default)

模块用于计算 **Reverse recovery time, trr** 的值。该值必须大于 `1`。与指定反向恢复电荷相比，指定拉伸因子是更简便的反向恢复时间参数化方法。拉伸因子的值越大，反向恢复电流耗散所需的时间越长。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Diode with charge dynamics`，并将 **Reverse recovery time parameterization** 设置为 `Specify stretch factor`。

### **Reverse recovery charge, Qrr** — Reverse recovery charge `1500` `μAs` (default)

模块用于计算 **Reverse recovery time, trr** 的值。如果你的二极管器件数据手册指定的是反向恢复电荷值而不是反向恢复时间值，请使用此参数。

反向恢复电荷是二极管关断时继续耗散的总电荷。该值必须小于 −i2RM2a，

其中：

- *iRM* 是为 **Peak reverse current, iRM** 指定的值。
- *a* 是为 **Rate of change of current when measuring iRM** 指定的值。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Diode with charge dynamics`，并将 **Reverse recovery time parameterization** 设置为 `Specify reverse recovery charge`。

有关这些参数的详细信息，请参阅 Diode。

### 缓冲器

如果 **Switching device** 设置为 `Averaged Switch`，则 **Snubbers** 参数选项卡不可见。

### **Snubber** — Snubber `None` (default) | `RC snubber`

每个开关器件的缓冲器：

- `None` - 这是默认值。
- `RC snubber`

### **Snubber resistance** — Snubber resistance `0.1` `Ohm` (default)

缓冲器电阻。

#### 依赖关系

仅当 **Snubber** 参数设置为 `RC snubber` 时，此参数才可见。

### **Snubber capacitance** — Snubber capacitance `1e-7` `F` (default)

缓冲器电容。

#### 依赖关系

仅当 **Snubber** 参数设置为 `RC snubber` 时，此参数才可见。

## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014b 中引入**

### R2021b：Electrical connection 端口更新

从 R2021b 起，要在复合端口和展开端口之间切换，请将 **Electrical connection** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。

由于这些更改，在早期版本保存的模型中，请检查此模块的 **Electrical connection** 参数。

## 描述

十二脉冲三相三电平中性点钳位受控变换器

Three-Level Converter (Three-Phase) 模块对十二脉冲三相三电平中性点钳位受控变换器进行建模。你可以使用此模块将三相交流网络连接到三电平直流网络。

### 模型

该模块包含三个桥臂，每个桥臂有四个开关器件以及相关的反并联二极管。开关器件类型选项包括：

- GTO — 门极关断晶闸管。关于该器件的 I-V 特性信息，参阅 GTO。
- Ideal semiconductor switch — 关于该器件的 I-V 特性信息，参阅 Ideal Semiconductor Switch。
- IGBT — 绝缘栅双极晶体管。关于该器件的 I-V 特性信息，参阅 IGBT (Ideal, Switching)。
- MOSFET — N 沟道金属氧化物半导体场效应晶体管。关于该器件的 I-V 特性信息，参阅 MOSFET (Ideal, Switching)。
- Averaged Switch — 带反并联二极管的半导体开关。控制信号端口 **G** 接受 `[0,1]` 区间内的值。当端口 **G** 处的值等于 `0` 或 `1` 时，平均开关要么完全打开，要么完全关闭，并且其行为类似于带反并联二极管的 Ideal Semiconductor Switch 模块。当端口 **G** 处的值介于 `0` 和 `1` 之间时，平均开关部分打开。然后您可以在指定周期内对 PWM 信号求平均。这允许对模型进行欠采样，或使用调制波形代替 PWM 信号。

三桥臂电路中的每个组件都是您指定的同一开关器件。这些开关器件与 **Semiconductors** > **Fundamental Components** 子库中的器件相同。

该图显示了使用 Ideal Semiconductor 模块作为开关器件时该模块的等效电路。

您通过 Three-Level Converter (Three-Phase) 模块 **G** 端口的输入来控制 12 个开关器件的门极端口。

1. 使用 Twelve-Pulse Gate Multiplexer 模块将所有 12 个门极信号多路复用为单个向量。
2. 将 Twelve-Pulse Gate Multiplexer 模块的输出连接到 Three-Level Converter (Three-Phase) 模块的 **G** 端口。

您使用模块对话框的 **Diodes** 选项卡为每个开关器件包含一个集成保护二极管。集成二极管通过为反向电流提供导通路径来保护半导体器件。当半导体器件突然切断向负载供电的电压时，感性负载可能产生高反向电压尖峰。

下表显示了如何根据您的目标设置 **Integral protection diode** 参数。

| 目标 | 要选择的值 | 集成保护二极管 |
| --- | --- | --- |
| 优先考虑仿真速度。 | `Diode with no dynamics` | Diode 模块 |
| 通过精确指定反向模式电荷动态来优先考虑模型保真度。 | `Diode with charge dynamics` | Diode 模块的动态模型 |

您使用模块对话框的 **Snubbers** 选项卡为每个开关器件包含一个缓冲电路。每个缓冲电路由串联连接的电阻器和电容器组成。通常，缓冲电路在器件切断向负载供电的电压时保护开关器件免受感性负载产生的非常高电压的影响。缓冲电路还可防止开关器件导通时电流变化率过大。

### Averaged Switch 中用于 FPGA 部署的分段常数近似

如果您将 **Switching device** 参数设置为 `Averaged switch`，并且您的模型使用分区求解器，则此模块会产生非线性分区，因为平均模式方程包含作为输入 **G** 的函数的模式 *Gsat*。为使这些方程与硬件描述语言 (HDL) 代码生成兼容，并因此与 FPGA 部署兼容，请将 **Integer for piecewise constant approximation of gate input (0 for disabled)** 参数设置为大于 `0` 的值。然后，此模块将 *Gsat* 模式视为具有固定范围的分段常数整数。这将先前非线性的分区转换为线性时变分区。

范围 `[0,K]` 中的整数值现在与范围 `[0,1]` 中的每个实值模式相关联，其中 *K* 是 **Integer for piecewise constant approximation of gate input (0 for disabled)** 的值。该模块通过将原始模式除以 K 以将其归一化回范围 `[0,1]` 来计算分段常数模式：

uI=(floor(u⋅K))

u^=uI/K
