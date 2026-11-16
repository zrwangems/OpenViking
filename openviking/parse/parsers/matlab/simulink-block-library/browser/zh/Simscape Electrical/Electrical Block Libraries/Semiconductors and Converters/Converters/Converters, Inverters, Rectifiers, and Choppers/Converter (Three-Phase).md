---
type: simulink-block
title: 'Converter (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Semiconductors and Converters / Converters / Converters, Inverters, Rectifiers, and Choppers'
documentation_page: 'converterthreephase'
documentation_source_path: 'ref/converterthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Converter (Three-Phase)

## 端口

### 守恒

### **G** — 门极端子 电气

与开关器件门极端子关联的向量输入端口。将此端口连接到 Six-Pulse Gate Multiplexer 模块。

### **~** — 三相端口 电气

复合三相端口。

有关复合和展开三相端口的更多信息，请参阅 Three-Phase Ports。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Composite three-phase ports`。

### **a** — *a* 相 电气

与 *a* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **b** — *b* 相 电气

与 *b* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **c** — *c* 相 电气

与 *c* 相关联的电气守恒端口。

#### 依赖关系

要启用此端口，请将 **Electrical connection** 设置为 `Expanded three-phase ports`。

### **+** — 正极端子 电气

与直流正极端子关联的电气守恒端口。

### **-** — 负极端子 电气

与直流负极端子关联的电气守恒端口。

### **H** — 热端口 热

*自 R2024b 起*

与开关器件热质量关联的热守恒端口。

#### 依赖关系

要启用此端口：

- 在 **Main** 设置中，将 **Fidelity level** 参数设置为 `Detailed model - switching devices`。
- 在 **Switching Devices** 设置中，将 **Switching device** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 在 **Switching Devices** 设置中，选中 **Model thermal effects** 参数。

## 参数

### 主设置

### **Electrical connection** — 电气连接 `Composite three-phase ports` (默认) | `Expanded three-phase ports`

用于选择复合或展开三相端口的选项。有关更多信息，请参阅 Three-Phase Ports。

### **Fidelity level** — 保真度级别 `Detailed model - switching devices` (默认) | `Equivalent model - PWM-controlled`

*自 R2024a 起*

模型的保真度级别。

若要优先考虑仿真精度或获取各开关器件的结果，请将此参数设置为 `Detailed model - switching devices`。

若要优先考虑仿真速度，请将此参数设置为 `Equivalent model - PWM-controlled`。

### 开关器件：GTO

要启用这些参数，请将 **Fidelity level** 设置为 `Detailed model - switching devices`，并将 **Switching device** 设置为 `GTO`。

### **Switching device** — 开关器件 `Ideal Semiconductor Switch` (默认) | `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

变换器开关器件。

### **Model thermal effects** — 用于对热效应建模的选项 `Off` (默认) | `On`

用于对热效应建模的选项。

### **Gate trigger voltage, Vgt** — 门极触发电压 `1` `V` (默认)

门极-阴极电压阈值。当门极-阴极电压高于此值时，器件导通。

### **Gate turn-off voltage, Vgt\_off** — 门极关断电压 `-1` `V` (默认)

门极-阴极电压阈值。当门极-阴极电压低于此值时，器件关断。

### **Holding current** — 保持电流 `1` `A` (默认)

电流阈值。当电流高于此值时，即使门极-阴极电压降至门极触发电压以下，器件仍保持导通。

### **Forward voltage, Vf** — 正向电压 `0.8` `V` (默认)

为使器件 i-v 特性的斜率为 1/Ron（其中 Ron 为 **On-state resistance** 的值），阳极和阴极模块端口之间所需的最小电压。

### **On-state resistance** — 通态电阻 `0.001` `Ohm` (默认)

在高于正向电压时，电压相对于电流的变化率。

### **Off-state Conductance** — 关断态电导 `1e-6` `1/Ohm` (默认)

器件关断时的阳极-阴极电导。该值必须小于 1/R，其中 R 为 **On-state resistance** 的值。

### 开关器件：Ideal Semiconductor Switch

要启用这些参数，请将 **Fidelity level** 设置为 `Detailed model - switching devices`，并将 **Switching device** 设置为 `Ideal semiconductor switch`。

### **Switching device** — 开关器件 `Ideal Semiconductor Switch` (默认) | `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

变换器开关器件。

### **Threshold voltage, Vth** — 阈值电压 `6` `V` (默认)

门极-阴极电压阈值。当门极-阴极电压高于此值时，器件导通。

### **On-state resistance** — 通态电阻 `0.001` `Ohm` (默认)

器件导通时的阳极-阴极电阻。

### **Off-state Conductance** — 关断态电导 `1e-6` `1/Ohm` (默认)

器件关断时的阳极-阴极电导。该值必须小于 1/R，其中 R 为 **On-state resistance** 的值。

### 开关器件：IGBT

要启用这些参数，请将 **Fidelity level** 设置为 `Detailed model - switching devices`，并将 **Switching device** 设置为 `IGBT`。

### **Switching device** — 开关器件 `Ideal Semiconductor Switch` (默认) | `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

变换器开关器件。

### **Model thermal effects** — 用于对热效应建模的选项 `Off` (默认) | `On`

用于对热效应建模的选项。

### **Threshold voltage, Vth** — 阈值电压 `6` `V` (默认)

器件导通时的栅极-发射极电压。

### **Forward voltage, Vf** — 正向电压 `0.8` `V` (默认)

为使二极管 i-v 特性的斜率为 1/Ron（其中 Ron 为 **On-state resistance** 的值），集电极和发射极模块端口之间所需的最小电压。

### **On-state resistance** — 通态电阻 `0.001` `Ohm` (默认)

器件导通时的集电极-发射极电阻。

### **Off-state Conductance** — 关断态电导 `1e-6` `1/Ohm` (默认)

器件关断时的集电极-发射极电导。该值必须小于 1/R，其中 R 为 **On-state resistance** 的值。

### 开关器件：MOSFET

要启用这些参数，请将 **Fidelity level** 设置为 `Detailed model - switching devices`，并将 **Switching device** 设置为 `MOSFET`。

### **Switching device** — 开关器件 `Ideal Semiconductor Switch` (默认) | `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

变换器开关器件。

### **Model thermal effects** — 用于对热效应建模的选项 `Off` (默认) | `On`

用于对热效应建模的选项。

### **Threshold voltage, Vth** — 阈值电压 `6` `V` (默认)

栅极-源极电压阈值。当栅极-源极电压高于此值时，器件导通。

### **Drain-source on resistance, R\_DS(on)** — 漏极-源极导通电阻 `0.001` `Ohm` (默认)

器件导通时的漏极-源极电阻。

### **Off-state Conductance** — 关断态电导 `1e-6` `1/Ohm` (默认)

器件关断时的漏极-源极电导。该值必须小于 1/R，其中 R 为 **On-state resistance** 的值。

### 开关器件：Thyristor

要启用这些参数，请将 **Fidelity level** 设置为 `Detailed model - switching devices`，并将 **Switching device** 设置为 `Thyristor`。

### **Switching device** — 开关器件 `Ideal Semiconductor Switch` (默认) | `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

变换器开关器件。

### **Model thermal effects** — 用于对热效应建模的选项 `Off` (默认) | `On`

用于对热效应建模的选项。

### **Gate trigger voltage, Vgt** — 门极触发电压 `1` `V` (默认)

门极-阴极电压阈值。当门极-阴极电压高于此值时，器件导通。

### **Holding current** — 保持电流 `1` `A` (默认)

电流阈值。当电流高于此值时，即使门极-阴极电压降至门极触发电压以下，器件仍保持导通。

### **Forward voltage, Vf** — 正向电压 `0.8` `V` (默认)

器件导通时的正向电压。

### **On-state resistance** — 通态电阻 `0.001` `Ohm` (默认)

器件导通时的阳极-阴极电阻。

### **Off-state Conductance** — 关断态电导 `1e-6` `1/Ohm` (默认)

器件关断时的阳极-阴极电导。该值必须小于 1/*R*，其中 *R* 为 **On-state resistance** 的值。

### 开关器件：Averaged Switch

要启用这些参数，请将 **Fidelity level** 设置为 `Detailed model - switching devices`，并将 **Switching device** 设置为 `Averaged switch`。

### **Switching device** — 开关器件 `Ideal Semiconductor Switch` (默认) | `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

变换器开关器件。

### **Integer for piecewise constant approximation of gate input (0 for disabled)** — FPGA 部署的整数模式 `0` (默认) | nonnegative scalar

用于对门极输入执行分段常数近似以进行 FPGA 部署的整数。

### **On-state resistance** — 通态电阻 `0.001` `Ohm` (默认)

器件导通时的阳极-阴极电阻。

### 开关损耗

要启用这些参数：

- 在 **Main** 设置中，将 **Fidelity level** 参数设置为 `Detailed model - switching devices`。
- 在 **Switching Devices** 设置中，将 **Switching device** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 在 **Switching Devices** 设置中，选中 **Model thermal effects** 参数。

### **Switch-on loss** — 开通损耗 `22.86e-3` `J` (默认) | positive scalar

*自 R2024b 起*

单次开通事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **Switching Device** 设置为 `GTO`、`IGBT`、`MOSFET` 或 `Thyristor`。

### **Switch-off loss** — 强制换相关断损耗 `17.14e-3` `J` (默认) | positive scalar

*自 R2024b 起*

单次关断事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **Switching Device** 设置为 `GTO`、`IGBT` 或 `MOSFET`。

### **Natural commutation rectification loss** — 自然换相整流损耗 `10e-3` `J` (默认) | positive scalar

*自 R2024b 起*

当电流降至 **Holding current** 参数值以下且模块关断时适用的整流损耗。

#### 依赖关系

要启用此参数，请将 **Switching Device** 设置为 `GTO` 或 `Thyristor`。

### **Off-state voltage for switching loss data** — 损耗数据的关断态电压 `300` `V` (默认) | positive scalar

*自 R2024b 起*

器件在关断态期间的输出电压。此值是在定义开通损耗和关断损耗数据时所使用的阻断电压。

#### 依赖关系

要启用此参数，请将 **Switching Device** 设置为 `GTO`、`IGBT`、`MOSFET` 或 `Thyristor`。

### **On-state current for switching loss data** — 输出电流 `600` `A` (默认) | positive scalar

*自 R2024b 起*

定义开通损耗和关断损耗时所用的输出电流。

**注意**

模块在栅极电压降至 **Gate trigger voltage, Vgt** 参数值以下时测量此参数。开通脉冲长于电流达到其最大值所需的时间。

#### 依赖关系

要启用此参数，请将 **Switching Device** 设置为 `GTO`、`IGBT`、`MOSFET` 或 `Thyristor`。

### **Wait time before switch-on current measurement** — 开通电流测量前的等待时间 `0` `s` (默认) | nonnegative scalar

*自 R2024b 起*

记录通态电流之前等待的时间。

#### 依赖关系

要启用此参数，请将 **Switching Device** 设置为 `GTO` 或 `Thyristor`。

### **Use last on-state current from previous cycle for turn-on loss** — 使用上一周期的最后一个通态电流计算开通损耗的选项 `Off` (默认) | `On`

*自 R2024b 起*

使用上一周期的最后一个通态电流计算开通损耗的选项。

#### 依赖关系

要启用此参数，请将 **Switching Device** 设置为 `GTO`、`IGBT` 或 `MOSFET`。

### **Use last off-state current from previous cycle for turn-offloss** — 使用上一周期的最后一个关断态电流计算关断损耗的选项 `Off` (默认) | `On`

*自 R2024b 起*

使用上一周期的最后一个关断态电流计算关断损耗的选项。

#### 依赖关系

要启用此参数，请将 **Switching Device** 设置为 `GTO`、`IGBT` 或 `MOSFET`。

### 集成二极管

要启用这些参数，请将 **Fidelity level** 设置为 `Detailed model - switching devices`。

### **Integral protection diode** — 集成保护二极管模型 `None` (默认) | `Diode with no dynamics` | `Diode with charge dynamics`

Converter (Three-Phase) 模块为每个开关器件用于保护二极管的模型。请选择以下选项之一：

- `None` — Converter (Three-Phase) 不对保护二极管建模。
- `Diode with no dynamics` — Converter (Three-Phase) 模块使用与 Diode 模块（无动态）相同的方程对保护二极管建模。选择此选项可优先考虑仿真速度。
- `Diode with charge dynamics` — Converter (Three-Phase) 模块使用与 Diode 模块（电荷动态）相同的方程对保护二极管建模。选择此选项可优先考虑详细仿真结果。

### **Forward voltage** — 正向电压 `0.8` `V` (默认)

为使二极管 I-V 特性的斜率为 1/Ron（其中 Ron 为 **On resistance** 参数的值），`+` 和 `-` 模块端口之间所需的最小电压。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将 **Switching device** 设置为 `Averaged Switch`。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。

### **On resistance** — 导通电阻 `0.001` `Ohm` (默认)

在高于 **Forward voltage** 参数值时，电压相对于电流的变化率。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将 **Switching device** 设置为 `Averaged Switch`。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。

### **Off conductance** — 关断电导 `1e-5` `1/Ohm` (默认)

反向偏置二极管的电导。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将 **Switching device** 设置为 `Averaged Switch`。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。

### **Reverse recovery loss model** — 反向恢复损耗模型 `Fixed loss` (默认) | `Tabulated loss`

*自 R2024b 起*

是对固定反向恢复损耗建模还是对表格化反向恢复损耗建模。

#### 依赖关系

要启用此参数：

- 将 **Switching device** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 选中 **Model thermal effects parameter** 参数。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics`。

### **Reverse recovery loss** — 反向恢复损耗 `0` `J` (默认) | nonnegative scalar

*自 R2024b 起*

每次关断事件中耗散的能量。无论开关事件之前或之后二极管的状态如何，模块都会耗散该能量。

#### 依赖关系

要启用此参数：

- 将 **Switching device** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 选中 **Model thermal effects parameter** 参数。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics`。
- 将 **Reverse recovery loss model** 设置为 `Fixed loss`。

### **Scale reverse recovery loss with current and voltage** — 根据电流和电压缩放反向恢复损耗的选项 `On` (默认) | `Off`

*自 R2024b 起*

根据电流和电压缩放反向恢复损耗的选项。

#### 依赖关系

要启用此参数：

- 将 **Switching device**
  参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 选择 **Model thermal effects
  parameter** 参数。
- 将 **Integral protection diode** 设置为
  `Diode with no
  dynamics`。
- 将 **Reverse recovery loss model**
  设置为 `Fixed loss`。

### **Forward current when measuring recovery loss, Irec** — 模块测量恢复损耗时使用的正向电流 `10` `A`（默认值）| 正标量

*自 R2024b 起*

在反向恢复事件之前，模块用于测量恢复损耗的通过二极管的正向电流。

#### 依赖关系

要启用此参数：

- 将 **Switching device**
  参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 选择 **Model thermal effects
  parameter** 参数。
- 将 **Integral protection diode** 设置为
  `Diode with no
  dynamics`。
- 将 **Reverse recovery loss model**
  设置为 `Fixed loss`。
- 选择 **Scale reverse recovery loss with
  current and voltage** 参数。

### **Turn-off voltage when measuring recovery loss, Vrec** — 测量恢复损耗时的关断电压 `10` `V`（默认值）| 正标量

*自 R2024b 起*

在反向恢复事件之后二极管两端的电压，模块用它来测量恢复损耗。

#### 依赖关系

要启用此参数：

- 将 **Switching device**
  参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 选择 **Model thermal effects
  parameter** 参数。
- 将 **Integral protection diode** 设置为
  `Diode with no
  dynamics`。
- 从以下选项中选择一项：

  - 将 **Reverse recovery loss
    model** 设置为 `Fixed
    loss`，并选择 **Scale
    reverse recovery loss with current and
    voltage** 参数。
  - 将 **Reverse recovery loss
    model** 参数设置为
    `Tabulated loss`。

### **Filter time constant for voltage and current values** — 电压和电流值的滤波器时间常数 `1 / 1000 / 100` `s`（默认值）| 正标量

*自 R2024b 起*

模块用于计算反向恢复损耗的电压和电流值的滤波器时间常数。将此参数设置为低于最快开关周期的值。

#### 依赖关系

要启用此参数：

- 将 **Switching device**
  参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 选择 **Model thermal effects
  parameter** 参数。
- 将 **Integral protection diode** 设置为
  `Diode with no
  dynamics`。
- 从以下选项中选择一项：

  - 将 **Reverse recovery loss
    model** 设置为 `Fixed
    loss`，并选择 **Scale
    reverse recovery loss with current and
    voltage** 参数。
  - 将 **Reverse recovery loss
    model** 参数设置为
    `Tabulated loss`。

### **Reverse recovery loss table, Erec(Tj, If)** — 反向恢复损耗 `zeros(2, 3)` `J`（默认值）| 非负标量向量

*自 R2024b 起*

耗散能量，作为切换事件之前正向电流 *If* 和二极管进入关断状态后的最终关断状态电压的函数。

#### 依赖关系

要启用此参数：

- 将 **Switching device**
  参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 选择 **Model thermal effects
  parameter** 参数。
- 将 **Integral protection diode** 设置为
  `Diode with no
  dynamics`。
- 将 **Reverse recovery loss
  model** 参数设置为 `Tabulated
  loss`。

### **Temperature vector for recovery loss table, Tj** — 恢复损耗表的温度向量 `[298.15, 398.15]` `K`（默认值）| 向量

*自 R2024b 起*

模块用于将反向恢复损耗制成表格的温度向量。

#### 依赖关系

要启用此参数：

- 将 **Switching device**
  参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 选择 **Model thermal effects
  parameter** 参数。
- 将 **Integral protection diode** 设置为
  `Diode with no
  dynamics`。
- 将 **Reverse recovery loss
  model** 参数设置为 `Tabulated
  loss`。

### **Forward current vector for recovery loss table, If** — 恢复损耗表的正向电流向量 `[.1, 1, 10]` `A`（默认值）| 非负标量向量

*自 R2024b 起*

模块用于将反向恢复损耗制成表格的正向电流向量。

#### 依赖关系

要启用此参数：

- 将 **Switching device**
  参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 选择 **Model thermal effects
  parameter** 参数。
- 将 **Integral protection diode** 设置为
  `Diode with no
  dynamics`。
- 将 **Reverse recovery loss
  model** 参数设置为 `Tabulated
  loss`。

### **Junction capacitance** — 二极管结电容 `50e-9` `F`（默认值）

二极管结电容。

#### 依赖关系

要启用此参数，请将 **Integral protection
diode** 设置为 `Diode with charge
dynamics`。

### **Peak reverse current, iRM** — 峰值反向电流 `-235` `A`（默认值）| 负标量

由外部测试电路测得的峰值反向电流。此值必须小于零。默认值为 `-235` `A`。

#### 依赖关系

要启用此参数，请将 **Integral protection
diode** 设置为 `Diode with charge
dynamics`。

### **Initial forward current when measuring iRM** — 测量 iRM 时的初始正向电流 `300` `A`（默认值）| 正标量

测量峰值反向电流时的初始正向电流。

#### 依赖关系

要启用此参数，请将 **Integral protection
diode** 设置为 `Diode with charge
dynamics`。

### **Rate of change of current when measuring iRM** — 测量 iRM 时的电流变化率 `-50``A/μs`（默认值）| 负标量

测量峰值反向电流时的电流变化率。此值必须小于零。

#### 依赖关系

要启用此参数，请将 **Integral protection
diode** 设置为 `Diode with charge
dynamics`。

### **Reverse recovery time parameterization** — 反向恢复时间参数化 `Specify reverse recovery time directly`（默认值）| `Specify stretch factor` | `Specify reverse recovery charge`

确定在模块中如何指定反向恢复时间。默认值为 `Specify reverse recovery time
directly`。

如果选择 `Specify stretch factor` 或
`Specify reverse recovery charge`，则需要指定一个值，模块用该值推导反向恢复时间。有关这些选项的详细信息，请参阅 How the Block Calculates TM and Tau。

#### 依赖关系

要启用此参数，请将 **Integral protection
diode** 设置为 `Diode with charge
dynamics`。

### **Reverse recovery time, trr** — 反向恢复时间 `15` `μs`（默认值）

从电流最初降为零（二极管关断时）到电流降至峰值反向电流的 10% 以下之间的时间间隔。**Reverse recovery time, trr** 参数的值必须大于 **Peak reverse current, iRM** 参数的值除以 **Rate of change of current when measuring iRM** 参数的值。

#### 依赖关系

要启用此参数，请将 **Integral protection
diode** 设置为 `Diode with charge
dynamics`，并将 **Reverse recovery time
parameterization** 设置为 `Specify reverse
recovery time directly`。

### **Reverse recovery time stretch factor** — 反向恢复时间拉伸因子 `3`（默认值）| 大于 `1` 的标量

模块用于计算反向恢复时间的拉伸因子。指定拉伸因子比指定反向恢复电荷更容易参数化反向恢复时间。拉伸因子的值越大，反向恢复电流消散所需的时间越长。

#### 依赖关系

要启用此参数，请将 **Integral protection
diode** 设置为 `Diode with charge
dynamics`，并将 **Reverse recovery time
parameterization** 设置为 `Specify stretch
factor`。

### **Reverse recovery charge, Qrr** — 反向恢复电荷 `1500` `μAs`（默认值）

模块用于计算反向恢复时间的反向恢复电荷。如果二极管器件的数据手册指定了反向恢复电荷值而不是反向恢复时间值，请使用此参数。

反向恢复电荷是二极管关断时继续耗散的总电荷。该值必须小于 −i2RM2a，其中：

- *iRM* 是为 **Peak reverse current,
  iRM** 指定的值。
- *a* 是为 **Rate
  of change of current when measuring iRM** 指定的值。

#### 依赖关系

要启用此参数，请将 **Integral protection
diode** 设置为 `Diode with charge
dynamics`，并将 **Reverse recovery time
parameterization** 设置为 `Specify reverse
recovery charge`。

有关这些参数的详细信息，请参阅 Diode。

### 缓冲器

要启用这些参数，请将 **Fidelity level** 设置为
`Detailed model - switching devices`，并将
**Switching device** 设置为以下选项之一：

- `Ideal Semiconductor Switch`
- `GTO`
- `IGBT`
- `MOSFET`
- `Thyristor`

### **Snubber** — 缓冲器 `None`（默认值）| `RC snubber`

每个开关器件的缓冲器。

### **Snubber resistance** — 缓冲电阻 `0.1` `Ohm`（默认值）

缓冲电阻。

#### 依赖关系

要启用此参数，请将 **Snubber** 设置为
`RC snubber`。

### **Snubber capacitance** — 缓冲电容 `1e-7` `F`（默认值）

缓冲电容。

#### 依赖关系

要启用此参数，请将 **Snubber** 设置为
`RC snubber`。

### 热端口

要启用这些参数：

- 在 **Main** 设置中，将
  **Fidelity level** 参数设置为
  `Detailed model - switching
  devices`。
- 在 **Switching Devices** 设置中，将
  **Switching device** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 在 **Switching Devices** 设置中，选择
  **Model thermal effects** 参数。

有关使用热端口和
**Thermal Port** 参数的详细信息，请参阅半导体热效应仿真。

### **Thermal network** — 热网络建模的选项 `External`（默认值）| `Specify junction and case thermal parameters` | `Cauer model` | `Cauer model parameterized with Foster coefficients`

*自 R2024b 起*

用于对模块的热网络建模的选项。

### **Thermal mass parameterization** — 用于参数化热质量的选项 `By thermal time constants`（默认值）| `By thermal mass`

*自 R2024b 起*

用于参数化热质量的选项：

- `By thermal time constants` —
  根据热时间常数对热质量进行参数化。
- `By thermal mass` — 直接指定热质量值。

#### 依赖关系

要启用此参数，请将 **Thermal network**
设置为 `Specify junction and case thermal
parameters`、`Cauer
model` 或 `Cauer model parameterized with
Foster coefficients`。

### **Junction case and case-ambient (or case-heatsink) thermal resistances, [R\_JC R\_CA]** — 结壳和壳-环境（或壳-散热器）热阻 `[.08, .5]` `K/W`（默认值）| 正值向量

*自 R2024b 起*

行向量 [ *R\_JC*
*R\_CA* ]，包含两个热阻值，由两个 Conductive Heat Transfer 模块表示。第一个值
*R\_JC* 是结与壳之间的热阻。第二个值 *R\_CA* 是端口 **H** 与器件壳之间的热阻。

#### 依赖关系

要启用此参数，请将 **Thermal network**
设置为 `Specify junction and case thermal
parameters`。

### **Junction and case thermal time constants, [t\_J t\_C]** — 结和壳热时间常数 `[.001, .2]` `s`（默认值）| 正值向量

*自 R2024b 起*

行向量 [ *t\_J*
*t\_C* ]，包含两个热时间常数值。第一个值
*t\_J* 是结时间常数。第二个值
*t\_C* 是壳时间常数。

#### 依赖关系

要启用此参数，请将 **Thermal network**
设置为 `Specify junction and case thermal
parameters`，并将 **Thermal mass
parameterization** 设置为 `By thermal time
constants`。

### **Junction and case thermal masses, [M\_J M\_C]** — 结和壳热质量 `[.01, .5]` `J/K`（默认值）| 正值向量

*自 R2024b 起*

行向量 [ *M\_J*
*M\_C* ]，包含两个热质量值。第一个值
*M\_J* 是结热质量。第二个值
*M\_C* 是壳热质量。

#### 依赖关系

要启用此参数，请将 **Thermal network**
设置为 `Specify junction and case thermal
parameters`，并将 **Thermal mass
parameterization** 设置为 `By thermal
mass`。

### **Junction and case initial temperatures, [T\_J T\_C]** — 结和壳初始温度 `[25, 25]` `degC`（默认值）| 正值向量

*自 R2024b 起*

行向量 [ *T\_J* *T\_C* ]，包含两个温度值。第一个值 *T\_J* 是结初始温度。第二个值 *T\_C* 是壳初始温度。

#### 依赖关系

要启用此参数，请将 **Thermal network**
设置为 `Specify junction and case thermal
parameters`。

### **Thermal resistances, [R1 R2 … Rn]** — 热阻 `[.08,.1,.5]` `K/W`（默认值）| `[.08,.14,.22,.16]` `K/W` | 正值向量

*自 R2024b 起*

由热网络中使用的 Cauer 元件表示的行向量，包含 *n* 个热阻值。

如果将 **Thermal network** 设置为 `Cauer
model`，默认值为
`[.08,.1,.5]`。如果将 **Thermal
network** 设置为 `Cauer model parameterized with
Foster coefficients`，默认值为
`[.08,.14,.22,.16]`。

#### 依赖关系

要启用此参数，请将 **Thermal network**
设置为 `Cauer model` 或 `Cauer
model parameterized with Foster
coefficients`。

### **Thermal masses, [M1 M2 … Mn]** — 热质量 `[.01,.1,.5]` `J/K` | `[.001,.005,.05,.5]` `J/K` | 正值向量

*自 R2024b 起*

行向量，包含 *n* 个热质量值，其中
*n* 是热网络中 Cauer 元件的数量。

如果将 **Thermal network** 设置为 `Cauer
model`，默认值为
`[.01,.1,.5]`。如果将 **Thermal
network** 设置为 `Cauer model parameterized with
Foster coefficients`，默认值为
`[.001,.005,.05,.5]`。

#### 依赖关系

要启用此参数，请将 **Thermal network**
设置为 `Cauer model` 或 `Cauer
model parameterized with Foster coefficients`，并将
**Thermal mass parameterization** 设置为
`By thermal mass`。

### **Thermal masses initial temperatures, [T1 T2 … Tn]** — 热质量的初始温度 `[25, 25, 25]` `degC`（默认值）| 正值向量

*自 R2024b 起*

行向量，包含与模型中每个热容上的温差相对应的温度值。

#### 依赖关系

要启用此参数，请将 **Thermal network**
设置为 `Cauer model`。

### **Thermal time constants, [t1 t2 … tn]** — 热时间常数 `[.001,.1,.2]` `s` | `[7e-05, .0007, .01, .08]` `s` | 正值向量

*自 R2024b 起*

行向量，包含 *n* 个热时间常数值，其中
*n* 是热网络中 Cauer 元件的数量。此向量的长度必须与
**Thermal resistances, [R1 R2 … Rn]** 的长度匹配。使用此参数化方法时，模块将热质量计算为
`Mi =
ti/Ri`，其中 `Mi`、
`ti` 和
`Ri` 分别是第 i 个 Cauer 元件（如果将
**Thermal network** 设置为 `Cauer
model`）或 Foster 元件（如果将 **Thermal
network** 设置为 `Cauer model parameterized with
Foster coefficients`）的热质量、热时间和热阻。

如果将 **Thermal network** 设置为 `Cauer
model`，默认值为
`[.001,.1,.2]`。如果将 **Thermal
network** 设置为 `Cauer model parameterized with
Foster coefficients`，默认值为
`[7e-05, .0007, .01, .08]`。

#### 依赖关系

要启用此参数，请将 **Thermal network**
设置为 `Cauer model` 或 `Cauer
model parameterized with Foster coefficients`，并将
**Thermal mass parameterization** 设置为
`By thermal time constants`。

### **初始节点温度，[T1 T2 ... Tn]** — 初始节点温度 `[25, 25, 25, 25]` `degC`（默认）| 正值向量

*自 R2024b 起*

从结开始的每个节点的温度值的行向量。

#### 依赖关系

要启用此参数，请将 **热网络** 设置为 `Cauer model parameterized with Foster coefficients`。

### **结热质量** — 结的热质量 `0.01` `J/K`（默认）| 正标量

*自 R2024b 起*

结的热质量。

#### 依赖关系

要启用此参数，请将 **热网络** 设置为 `External`。

## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2024b：使用热端口对热效应建模

现在可以使用热端口对产生的热量和设备温度的影响进行建模。当您暴露热端口时，Converter (Three-Phase) 模块会对开关器件的导通损耗以及开通和关断损耗进行建模。如果启用热端口，并将 **集成保护二极管** 参数设置为 `Diode with no dynamics`，该模块还会对保护二极管的反向恢复损耗进行建模。

### R2024a：使用等效模型提高仿真速度

现在可以从转换器模型的两种保真度级别中进行选择。等效模型选项不会对各个开关器件建模，但会返回等效结果。如果需要开关器件动态的详细结果，请使用详细模型选项。否则，请使用等效模型以加快仿真。要进行实时仿真，请使用等效模型。要验证结果，请使用详细模型和可变步长求解器。

要使用详细模型，请将 **保真度级别** 参数设置为 `Detailed model - switching devices`。要使用等效模型，请将 **保真度级别** 参数设置为 `Equivalent model - PWM-controlled`。

在 R2024a 之前，只能使用详细模型。

### R2021b：电气连接端口更新

从 R2021b 开始，要在复合端口和扩展端口之间切换，请将 **电气连接** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。

由于这些更改，在较早版本中保存的模型内，请检查此模块的 **电气连接** 参数。

## 描述

控制器驱动的双向 AC/DC 三桥臂转换器

Converter (Three-Phase) 模块对由三个桥臂组成的六脉冲三相可控转换器进行建模。每个桥臂包含两个开关器件。转换器电路将三相交流网络连接到直流网络。

您可以从转换器模型的两种保真度级别中进行选择。等效模型选项不会对各个开关器件建模，但会返回等效结果。如果需要开关器件动态的详细结果，请使用详细模型选项。否则，请使用等效模型以加快仿真。要进行实时仿真，请使用等效模型。要验证结果，请使用详细模型和可变步长求解器。要使用详细模型，请将 **保真度级别** 参数设置为 `Detailed model - switching devices`。要使用等效模型，请将 **保真度级别** 参数设置为 `Equivalent model - PWM-controlled`。

如果选择详细模型，三桥臂电路中的每个组件都是相同的开关器件，可通过设置 **开关器件** 参数来指定。可以指定的开关器件是 **Simscape** > **Electrical** > **Semiconductors & Converters** 库中模块的实现：

- GTO — 门极可关断晶闸管。有关该器件的 I-V 特性信息，请参阅 GTO。
- Ideal semiconductor switch — 有关该器件的 I-V 特性信息，请参阅 Ideal Semiconductor Switch。
- IGBT — 绝缘栅双极型晶体管。有关该器件的 I-V 特性信息，请参阅 IGBT (Ideal, Switching)。
- MOSFET — N 沟道金属氧化物半导体场效应晶体管。有关该器件的 I-V 特性信息，请参阅 MOSFET (Ideal, Switching)。
- Thyristor — 有关该器件的 I-V 特性信息，请参阅 Thyristor (Piecewise Linear)。
- Averaged Switch — 带反并联二极管的半导体开关。控制信号端口 **G** 接受区间 [0,1] 中的值。当 **G** 等于 `0` 或 `1` 时，平均开关分别完全打开或完全闭合。该开关的行为类似于带有反并联二极管的 Ideal Semiconductor Switch 模块。当 **G** 介于 0 和 1 之间时，平均开关部分打开。您可以在指定周期内对脉宽调制 (PWM) 信号取平均。然后可以对模型进行欠采样，并使用调制波形代替 PWM 信号。

此图显示具有全控开关器件（例如 IGBT、GTO）的转换器的等效电路。

此图显示具有半控开关器件（例如晶闸管）的转换器的等效电路。

通过 Converter (Three-Phase) 模块上端口 **G** 的输入来控制六个开关器件的栅极端口：

1. 使用 Six-Pulse Gate Multiplexer 模块将所有六个栅极信号多路复用为单个向量。
2. 将 Six-Pulse Gate Multiplexer 模块的输出连接到 Converter (Three-Phase) 模块的 **G** 端口。

您可以为每个开关器件指定一个集成保护二极管。集成二极管通过为反向电流提供导通路径来保护半导体器件。当半导体器件突然切断负载的电压供应时，感性负载可能产生高反向电压尖峰。

下表说明了如何根据您的目标设置 **集成保护二极管** 参数。

| 目标 | | 要选择的值 | 集成保护二极管 |
| --- | --- | --- | --- |
| 不包含保护。 | | `None` | 无 |
| 包含保护。 | 优先考虑仿真速度。 | `Diode with no dynamics` | Diode 模块 |
| 优先考虑模型保真度，通过精确指定反向模式电荷动态。 | `Diode with charge dynamics` | Diode 模块的动态模型 |

**注意**

如果将 **开关器件** 参数设置为 `Averaged Switch`，该模块会使用无动态的保护二极管建模，并且 **集成保护二极管** 参数不可见。

您可以为每个开关器件包含一个由串联电阻和电容组成的缓冲电路。缓冲电路保护开关器件免受感性负载在器件切断负载电压供应时产生的高电压影响。缓冲电路还可防止开关器件开通时电流变化率过大。

要将等效模型用作整流器，请将 PWM 信号的所有元素设置为零。该模型的行为如同三相二极管整流器。

### 热效应建模

*自 R2024b 起*

您可以暴露热端口，以对产生的热量和设备温度的影响进行建模。要暴露热端口：

- 在 **Main** 设置中，将 **保真度级别** 参数设置为 `Detailed model - switching devices`。
- 在 **Switching Devices** 设置中，将 **开关器件** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 在 **Switching Devices** 设置中，选择 **对热效应建模** 参数。

有关使用热端口和 **Thermal Port** 参数的详细信息，请参阅《半导体中的热效应仿真》。

当您暴露热端口时，Converter (Three-Phase) 模块会对开关器件的导通损耗以及开通和关断损耗进行建模。该模块使用与以下模块相同的方法来计算这些损耗：这些模块的 **导通状态行为和开关损耗** 参数设置为 `Specify constant values`：

- GTO
- IGBT (Ideal, Switching)
- MOSFET (Ideal, Switching)
- Thyristor (Piecewise Linear)

有关 Converter (Three-Phase) 模块如何计算这些损耗的详细信息，请参阅与您为 **开关器件** 参数选择的选项匹配的模块文档。

如果启用热端口，并将 **集成保护二极管** 参数设置为 `Diode with no dynamics`，该模块还会对保护二极管的反向恢复损耗进行建模。该模块使用与 Diode 模块相同的方法来计算这些损耗：该模块的 **保真度级别** 参数设置为 `Ideal switching`，**二极管模型** 参数设置为 `Piecewise linear`。

对于理想开关，该模块不使用基于物理的电荷模型。该模块将反向恢复期间电荷产生的损耗表示为瞬时损耗。

该模块通过将结温升高一个等于反向恢复损耗除以结处总热质量的值来施加反向恢复损耗。

如果将 **反向恢复损耗模型** 参数设置为 `Tabulated loss`，则 **反向恢复损耗表，Erec(Tj, If)** 参数的值指定耗散能量，它是结温和开关事件前正向电流的函数。断态电压会相对于 **测量恢复损耗时的关断电压，Vrec** 参数值线性缩放损耗。该表使用电流和电压的延迟值。要使用查找表中接近瞬时值的值，请将 **电压和电流值的滤波时间常数** 参数设置为小于最快开关周期的值。

如果将 **反向恢复损耗模型** 参数设置为 `Fixed loss`，则 **反向恢复损耗** 参数的值指定每个关断事件期间耗散的能量。如果选择 **按电流和电压缩放反向恢复损耗** 参数，则该模块按导通状态电流和断态电压线性缩放此损耗值。要使用接近瞬时值的缩放值，请将 **电压和电流值的滤波时间常数** 设置为小于最快开关周期的值。

### 用于 FPGA 部署的 Averaged Switch 分段常数近似

如果将 **开关器件** 参数设置为 `Averaged switch`，并且您的模型使用分区求解器，则该模块会产生非线性分区，因为平均模式方程包含模式 *Gsat*，这些模式是输入 **G** 的函数。为了使这些方程与硬件描述语言 (HDL) 代码生成兼容，从而可用于 FPGA 部署，请将 **门输入的分段常数近似的整数（0 表示禁用）** 参数设置为大于 `0` 的值。然后，该模块将 *Gsat* 模式视为具有固定范围的分段常数整数。这会将先前的非线性分区转换为线性时变分区。

`[0,K]` 范围内的整数值（其中 *K* 是 **门输入的分段常数近似的整数（0 表示禁用）** 的值）现在与 `[0,1]` 范围内的每个实值模式相关联。该模块通过将原始模式除以 K 来将其归一化回 `[0,1]` 范围，从而计算分段常数模式：

uI=(floor(u⋅K))u^=uIK

### 假设和限制

- 如果在模型内的 Solver Configuration 模块中，将 **求解器类型** 参数设置为 `Partitioning`，则当所有栅极输入都设置为 0 时，平均开关会在死区时间内引入不稳定。在可能的情况下，通过将所有高侧开关设置为 0 并将所有低侧开关设置为 1 来使用 open-zero 状态。
- 要将 Converter (Three-Phase) 模块用作有
