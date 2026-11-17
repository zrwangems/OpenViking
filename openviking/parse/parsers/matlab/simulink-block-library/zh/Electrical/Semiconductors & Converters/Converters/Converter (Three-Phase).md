---
type: simulink-block
title: 'Converter (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'converterthreephase'
documentation_source_path: 'ref/converterthreephase.html'
language: zh-CN
chinese_source: worker-translation
---

# Converter (Three-Phase)

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
- name: '-'
  summary: 负极端子 electrical
  direction: conserving
- name: H
  summary: 热端口 thermal
  direction: conserving
```

### 守恒端口

### **G** — 门极端子 electrical

与开关器件门极端子关联的矢量输入端口。将此端口连接到 Six-Pulse Gate Multiplexer 模块。

### **~** — 三相端口 electrical

复合三相端口。

有关复合和扩展三相端口的详细信息，请参阅 Three-Phase Ports。

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

### **-** — 负极端子 electrical

与直流负极端子关联的电气守恒端口。

### **H** — 热端口 thermal

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
```yaml
parameters:
- name: Electrical connection
  summary: 电气连接 Composite three-phase ports（默认）| Expanded three-phase ports
  group: 主要参数
- name: Fidelity level
  summary: 保真度级别 Detailed model - switching devices（默认）| Equivalent model - PWM-controlled
  group: 主要参数
- name: Switching device
  summary: 开关器件 Ideal Semiconductor Switch（默认）| GTO | IGBT | MOSFET | Thyristor | Averaged Switch
  group: 'Switching Devices: GTO'
- name: Model thermal effects
  summary: 热效应建模选项 Off（默认）| On
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
- name: Forward voltage, Vf
  summary: 正向电压 0.8 V（默认）
  group: 'Switching Devices: GTO'
- name: On-state resistance
  summary: 导通电阻 0.001 Ohm（默认）
  group: 'Switching Devices: GTO'
- name: Off-state Conductance
  summary: 关断电导 1e-6 1/Ohm（默认）
  group: 'Switching Devices: GTO'
- name: Switching device
  summary: 开关器件 Ideal Semiconductor Switch（默认）| GTO | IGBT | MOSFET | Thyristor | Averaged Switch
  group: 'Switching Devices: Ideal Semiconductor Switch'
- name: Threshold voltage, Vth
  summary: 阈值电压 6 V（默认）
  group: 'Switching Devices: Ideal Semiconductor Switch'
- name: On-state resistance
  summary: 导通电阻 0.001 Ohm（默认）
  group: 'Switching Devices: Ideal Semiconductor Switch'
- name: Off-state Conductance
  summary: 关断电导 1e-6 1/Ohm（默认）
  group: 'Switching Devices: Ideal Semiconductor Switch'
- name: Switching device
  summary: 开关器件 Ideal Semiconductor Switch（默认）| GTO | IGBT | MOSFET | Thyristor | Averaged Switch
  group: 'Switching Devices: IGBT'
- name: Model thermal effects
  summary: 热效应建模选项 Off（默认）| On
  group: 'Switching Devices: IGBT'
- name: Threshold voltage, Vth
  summary: 阈值电压 6 V（默认）
  group: 'Switching Devices: IGBT'
- name: Forward voltage, Vf
  summary: 正向电压 0.8 V（默认）
  group: 'Switching Devices: IGBT'
- name: On-state resistance
  summary: 导通电阻 0.001 Ohm（默认）
  group: 'Switching Devices: IGBT'
- name: Off-state Conductance
  summary: 关断电导 1e-6 1/Ohm（默认）
  group: 'Switching Devices: IGBT'
- name: Switching device
  summary: 开关器件 Ideal Semiconductor Switch（默认）| GTO | IGBT | MOSFET | Thyristor | Averaged Switch
  group: 'Switching Devices: MOSFET'
- name: Model thermal effects
  summary: 热效应建模选项 Off（默认）| On
  group: 'Switching Devices: MOSFET'
- name: Threshold voltage, Vth
  summary: 阈值电压 6 V（默认）
  group: 'Switching Devices: MOSFET'
- name: Drain-source on resistance, R_DS(on)
  summary: 漏源导通电阻 0.001 Ohm（默认）
  group: 'Switching Devices: MOSFET'
- name: Off-state Conductance
  summary: 关断电导 1e-6 1/Ohm（默认）
  group: 'Switching Devices: MOSFET'
- name: Switching device
  summary: 开关器件 Ideal Semiconductor Switch（默认）| GTO | IGBT | MOSFET | Thyristor | Averaged Switch
  group: 'Switching Devices: Thyristor'
- name: Model thermal effects
  summary: 热效应建模选项 Off（默认）| On
  group: 'Switching Devices: Thyristor'
- name: Gate trigger voltage, Vgt
  summary: 门极触发电压 1 V（默认）
  group: 'Switching Devices: Thyristor'
- name: Holding current
  summary: 维持电流 1 A（默认）
  group: 'Switching Devices: Thyristor'
- name: Forward voltage, Vf
  summary: 正向电压 0.8 V（默认）
  group: 'Switching Devices: Thyristor'
- name: On-state resistance
  summary: 导通电阻 0.001 Ohm（默认）
  group: 'Switching Devices: Thyristor'
- name: Off-state Conductance
  summary: 关断电导 1e-6 1/Ohm（默认）
  group: 'Switching Devices: Thyristor'
- name: Switching device
  summary: 开关器件 Ideal Semiconductor Switch（默认）| GTO | IGBT | MOSFET | Thyristor | Averaged Switch
  group: 'Switching Devices: Averaged Switch'
- name: Integer for piecewise constant approximation of gate input (0 for disabled)
  summary: FPGA 部署的整数模式 0（默认）| 非负标量
  group: 'Switching Devices: Averaged Switch'
- name: On-state resistance
  summary: 导通电阻 0.001 Ohm（默认）
  group: 'Switching Devices: Averaged Switch'
- name: Switch-on loss
  summary: 开通损耗 22.86e-3 J（默认）| 正标量
  group: Switching Losses
- name: Switch-off loss
  summary: 强制换相关断损耗 17.14e-3 J（默认）| 正标量
  group: Switching Losses
- name: Natural commutation rectification loss
  summary: 自然换相整流损耗 10e-3 J（默认）| 正标量
  group: Switching Losses
- name: Off-state voltage for switching loss data
  summary: 开关损耗数据的关断电压 300 V（默认）| 正标量
  group: Switching Losses
- name: On-state current for switching loss data
  summary: 输出电流 600 A（默认）| 正标量
  group: Switching Losses
- name: Wait time before switch-on current measurement
  summary: 开通电流测量前的等待时间 0 s（默认）| 非负标量
  group: Switching Losses
- name: Use last on-state current from previous cycle for turn-on loss
  summary: 使用上一周期的最后导通电流计算开通损耗的选项 Off（默认）| On
  group: Switching Losses
- name: Use last off-state current from previous cycle for turn-offloss
  summary: 使用上一周期的最后关断电流计算关断损耗的选项 Off（默认）| On
  group: Switching Losses
- name: Integral protection diode
  summary: 集成保护二极管模型 None（默认）| Diode with no dynamics | Diode with charge dynamics
  group: Integral Diodes
- name: Forward voltage
  summary: 正向电压 0.8 V（默认）
  group: Integral Diodes
- name: On resistance
  summary: 导通电阻 0.001 Ohm（默认）
  group: Integral Diodes
- name: Off conductance
  summary: 关断电导 1e-5 1/Ohm（默认）
  group: Integral Diodes
- name: Reverse recovery loss model
  summary: 反向恢复损耗模型 Fixed loss（默认）| Tabulated loss
  group: Integral Diodes
- name: Reverse recovery loss
  summary: 反向恢复损耗 0 J（默认）| 非负标量
  group: Integral Diodes
- name: Scale reverse recovery loss with current and voltage
  summary: 反向恢复损耗随电流和电压缩放的选项 On（默认）| Off
  group: Integral Diodes
- name: Forward current when measuring recovery loss, Irec
  summary: 模块测量恢复损耗时的正向电流 10 A（默认）| 正标量
  group: Integral Diodes
- name: Turn-off voltage when measuring recovery loss, Vrec
  summary: 模块测量恢复损耗时的关断电压 10 V（默认）| 正标量
  group: Integral Diodes
- name: Filter time constant for voltage and current values
  summary: 电压和电流值的滤波时间常数 1 / 1000 / 100 s（默认）| 正标量
  group: Integral Diodes
- name: Reverse recovery loss table, Erec(Tj, If)
  summary: 反向恢复损耗 zeros(2, 3) J（默认）| 非负标量向量
  group: Integral Diodes
- name: Temperature vector for recovery loss table, Tj
  summary: 恢复损耗表的温度向量 [298.15, 398.15] K（默认）| 向量
  group: Integral Diodes
- name: Forward current vector for recovery loss table, If
  summary: 恢复损耗表的正向电流向量 [.1, 1, 10] A（默认）| 非负标量向量
  group: Integral Diodes
- name: Junction capacitance
  summary: 结电容 50e-9 F（默认）
  group: Integral Diodes
- name: Peak reverse current, iRM
  summary: 峰值反向电流 -235 A（默认）| 负标量
  group: Integral Diodes
- name: Initial forward current when measuring iRM
  summary: 测量 iRM 时的初始正向电流 300 A（默认）| 正标量
  group: Integral Diodes
- name: Rate of change of current when measuring iRM
  summary: 测量 iRM 时的电流变化率 -50A/μs（默认）| 负标量
  group: Integral Diodes
- name: Reverse recovery time parameterization
  summary: 反向恢复时间参数化 Specify reverse recovery time directly（默认）| Specify stretch factor | Specify reverse recovery charge
  group: Integral Diodes
- name: Reverse recovery time, trr
  summary: 反向恢复时间 15 μs（默认）
  group: Integral Diodes
- name: Reverse recovery time stretch factor
  summary: 反向恢复时间拉伸因子 3（默认）| 大于 1 的标量
  group: Integral Diodes
- name: Reverse recovery charge, Qrr
  summary: 反向恢复电荷 1500 μAs（默认）
  group: Integral Diodes
- name: Snubber
  summary: 缓冲器 None（默认）| RC snubber
  group: 缓冲器
- name: Snubber resistance
  summary: 缓冲电阻 0.1 Ohm（默认）
  group: 缓冲器
- name: Snubber capacitance
  summary: 缓冲电容 1e-7 F（默认）
  group: 缓冲器
- name: Thermal network
  summary: 热网络建模选项 External（默认）| Specify junction and case thermal parameters | Cauer model | Cauer model parameterized with
    Foster coefficients
  group: 热端口
- name: Thermal mass parameterization
  summary: 热质量参数化选项 By thermal time constants（默认）| By thermal mass
  group: 热端口
- name: Junction case and case-ambient (or case-heatsink) thermal resistances, [R_JC R_CA]
  summary: 结-壳和壳-环境（或壳-散热器）热阻 [.08, .5] K/W（默认）| 正值向量
  group: 热端口
- name: Junction and case thermal time constants, [t_J t_C]
  summary: 结和壳热时间常数 [.001, .2] s（默认）| 正值向量
  group: 热端口
- name: Junction and case thermal masses, [M_J M_C]
  summary: 结和壳热质量 [.01, .5] J/K（默认）| 正值向量
  group: 热端口
- name: Junction and case initial temperatures, [T_J T_C]
  summary: 结和壳初始温度 [25, 25] degC（默认）| 正值向量
  group: 热端口
- name: Thermal resistances, [R1 R2 … Rn]
  summary: 热阻 [.08,.1,.5] K/W（默认）| [.08,.14,.22,.16] K/W | 正值向量
  group: 热端口
- name: Thermal masses, [M1 M2 … Mn]
  summary: 热质量 [.01,.1,.5] J/K | [.001,.005,.05,.5] J/K | 正值向量
  group: 热端口
- name: Thermal masses initial temperatures, [T1 T2 … Tn]
  summary: 热质量初始温度 [25, 25, 25] degC（默认）| 正值向量
  group: 热端口
- name: Thermal time constants, [t1 t2 … tn]
  summary: 热时间常数 [.001,.1,.2] s | [7e-05, .0007, .01, .08] s | 正值向量
  group: 热端口
- name: 初始节点温度，[T1 T2 ... Tn]
  summary: 初始节点温度 [25, 25, 25, 25] degC（默认）| 正值向量
  group: 热端口
- name: 结热质量
  summary: 结的热质量 0.01 J/K（默认）| 正标量
  group: 热端口
```

### 主要参数

### **Electrical connection** — 电气连接 `Composite three-phase ports`（默认）| `Expanded three-phase ports`

选择使用复合还是扩展三相端口。有关详细信息，请参阅 Three-Phase Ports。

### **Fidelity level** — 保真度级别 `Detailed model - switching devices`（默认）| `Equivalent model - PWM-controlled`

*自 R2024a 起*

模型的保真度级别。

要优先考虑仿真精度或获取各个开关器件的结果，请将此参数设置为 `Detailed model - switching devices`。

要优先考虑仿真速度，请将此参数设置为 `Equivalent model - PWM-controlled`。

### Switching Devices: GTO

要启用这些参数，请将 **Fidelity level** 设置为 `Detailed model - switching devices`，并将 **Switching device** 设置为 `GTO`。

### **Switching device** — 开关器件 `Ideal Semiconductor Switch`（默认）| `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

变流器开关器件。

### **Model thermal effects** — 热效应建模选项 `Off`（默认）| `On`

热效应建模选项。

### **Gate trigger voltage, Vgt** — 门极触发电压 `1` `V`（默认）

门极-阴极电压阈值。当门极-阴极电压高于此值时，器件导通。

### **Gate turn-off voltage, Vgt\_off** — 门极关断电压 `-1` `V`（默认）

门极-阴极电压阈值。当门极-阴极电压低于此值时，器件关断。

### **Holding current** — 维持电流 `1` `A`（默认）

电流阈值。当电流高于此值时，即使门极-阴极电压降至门极触发电压以下，器件仍保持导通。

### **Forward voltage, Vf** — 正向电压 `0.8` `V`（默认）

使器件 i-v 特性梯度为 1/Ron 时，阳极和阴极模块端口两端所需的最小电压，其中 Ron 为 **On-state resistance** 的值。

### **On-state resistance** — 导通电阻 `0.001` `Ohm`（默认）

正向电压以上电压随电流的变化率。

### **Off-state Conductance** — 关断电导 `1e-6` `1/Ohm`（默认）

器件关断时的阳极-阴极电导。该值必须小于 1/R，其中 R 为 **On-state resistance** 的值。

### Switching Devices: Ideal Semiconductor Switch

要启用这些参数，请将 **Fidelity level** 设置为 `Detailed model - switching devices`，并将 **Switching device** 设置为 `Ideal semiconductor switch`。

### **Switching device** — 开关器件 `Ideal Semiconductor Switch`（默认）| `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

变流器开关器件。

### **Threshold voltage, Vth** — 阈值电压 `6` `V`（默认）

门极-阴极电压阈值。当门极-阴极电压高于此值时，器件导通。

### **On-state resistance** — 导通电阻 `0.001` `Ohm`（默认）

器件导通时的阳极-阴极电阻。

### **Off-state Conductance** — 关断电导 `1e-6` `1/Ohm`（默认）

器件关断时的阳极-阴极电导。该值必须小于 1/R，其中 R 为 **On-state resistance** 的值。

### Switching Devices: IGBT

要启用这些参数，请将 **Fidelity level** 设置为 `Detailed model - switching devices`，并将 **Switching device** 设置为 `IGBT`。

### **Switching device** — 开关器件 `Ideal Semiconductor Switch`（默认）| `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

变流器开关器件。

### **Model thermal effects** — 热效应建模选项 `Off`（默认）| `On`

热效应建模选项。

### **Threshold voltage, Vth** — 阈值电压 `6` `V`（默认）

器件导通时的门极-发射极电压。

### **Forward voltage, Vf** — 正向电压 `0.8` `V`（默认）

使二极管 i-v 特性梯度为 1/Ron 时，集电极和发射极模块端口两端所需的最小电压，其中 Ron 为 **On-state resistance** 的值。

### **On-state resistance** — 导通电阻 `0.001` `Ohm`（默认）

器件导通时的集电极-发射极电阻。

### **Off-state Conductance** — 关断电导 `1e-6` `1/Ohm`（默认）

器件关断时的集电极-发射极电导。该值必须小于 1/R，其中 R 为 **On-state resistance** 的值。

### Switching Devices: MOSFET

要启用这些参数，请将 **Fidelity level** 设置为 `Detailed model - switching devices`，并将 **Switching device** 设置为 `MOSFET`。

### **Switching device** — 开关器件 `Ideal Semiconductor Switch`（默认）| `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

变流器开关器件。

### **Model thermal effects** — 热效应建模选项 `Off`（默认）| `On`

热效应建模选项。

### **Threshold voltage, Vth** — 阈值电压 `6` `V`（默认）

门极-源极电压阈值。当门极-源极电压高于此值时，器件导通。

### **Drain-source on resistance, R\_DS(on)** — 漏源导通电阻 `0.001` `Ohm`（默认）

器件导通时的漏极-源极电阻。

### **Off-state Conductance** — 关断电导 `1e-6` `1/Ohm`（默认）

器件关断时的漏极-源极电导。该值必须小于 1/R，其中 R 为 **On-state resistance** 的值。

### Switching Devices: Thyristor

要启用这些参数，请将 **Fidelity level** 设置为 `Detailed model - switching devices`，并将 **Switching device** 设置为 `Thyristor`。

### **Switching device** — 开关器件 `Ideal Semiconductor Switch`（默认）| `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

变流器开关器件。

### **Model thermal effects** — 热效应建模选项 `Off`（默认）| `On`

热效应建模选项。

### **Gate trigger voltage, Vgt** — 门极触发电压 `1` `V`（默认）

门极-阴极电压阈值。当门极-阴极电压高于此值时，器件导通。

### **Holding current** — 维持电流 `1` `A`（默认）

电流阈值。当电流高于此值时，即使门极-阴极电压降至门极触发电压以下，器件仍保持导通。

### **Forward voltage, Vf** — 正向电压 `0.8` `V`（默认）

器件导通时的正向电压。

### **On-state resistance** — 导通电阻 `0.001` `Ohm`（默认）

器件导通时的阳极-阴极电阻。

### **Off-state Conductance** — 关断电导 `1e-6` `1/Ohm`（默认）

器件关断时的阳极-阴极电导。该值必须小于 1/*R*，其中 *R* 为 **On-state resistance** 的值。

### Switching Devices: Averaged Switch

要启用这些参数，请将 **Fidelity level** 设置为 `Detailed model - switching devices`，并将 **Switching device** 设置为 `Averaged switch`。

### **Switching device** — 开关器件 `Ideal Semiconductor Switch`（默认）| `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

变流器开关器件。

### **Integer for piecewise constant approximation of gate input (0 for disabled)** — FPGA 部署的整数模式 `0`（默认）| 非负标量

用于对门极输入进行分段常数近似以进行 FPGA 部署的整数。

### **On-state resistance** — 导通电阻 `0.001` `Ohm`（默认）

器件导通时的阳极-阴极电阻。

### Switching Losses

要启用这些参数：

- 在 **Main** 设置中，将 **Fidelity level** 参数设置为 `Detailed model - switching devices`。
- 在 **Switching Devices** 设置中，将 **Switching device** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 在 **Switching Devices** 设置中，选中 **Model thermal effects** 参数。

### **Switch-on loss** — 开通损耗 `22.86e-3` `J`（默认）| 正标量

*自 R2024b 起*

单次开通事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **Switching Device** 设置为 `GTO`、`IGBT`、`MOSFET` 或 `Thyristor`。

### **Switch-off loss** — 强制换相关断损耗 `17.14e-3` `J`（默认）| 正标量

*自 R2024b 起*

单次关断事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **Switching Device** 设置为 `GTO`、`IGBT` 或 `MOSFET`。

### **Natural commutation rectification loss** — 自然换相整流损耗 `10e-3` `J`（默认）| 正标量

*自 R2024b 起*

当电流降至 **Holding current** 参数值以下且模块关断时适用的整流损耗。

#### 依赖关系

要启用此参数，请将 **Switching Device** 设置为 `GTO` 或 `Thyristor`。

### **Off-state voltage for switching loss data** — 开关损耗数据的关断电压 `300` `V`（默认）| 正标量

*自 R2024b 起*

器件在关断状态期间的输出电压。此值是您定义开通损耗和关断损耗数据时的阻断电压。

#### 依赖关系

要启用此参数，请将 **Switching Device** 设置为 `GTO`、`IGBT`、`MOSFET` 或 `Thyristor`。

### **On-state current for switching loss data** — 输出电流 `600` `A`（默认）| 正标量

*自 R2024b 起*

您定义开通损耗和关断损耗时的输出电流。

**注意**

模块在门极电压降至 **Gate trigger voltage, Vgt** 参数值以下时测量此参数。开通脉冲持续时间长于电流达到最大值所需的时间。

#### 依赖关系

要启用此参数，请将 **Switching Device** 设置为 `GTO`、`IGBT`、`MOSFET` 或 `Thyristor`。

### **Wait time before switch-on current measurement** — 开通电流测量前的等待时间 `0` `s`（默认）| 非负标量

*自 R2024b 起*

记录导通电流前的等待时间。

#### 依赖关系

要启用此参数，请将 **Switching Device** 设置为 `GTO` 或 `Thyristor`。

### **Use last on-state current from previous cycle for turn-on loss** — 使用上一周期的最后导通电流计算开通损耗的选项 `Off`（默认）| `On`

*自 R2024b 起*

使用上一周期的最后导通电流计算开通损耗的选项。

#### 依赖关系

要启用此参数，请将 **Switching Device** 设置为 `GTO`、`IGBT` 或 `MOSFET`。

### **Use last off-state current from previous cycle for turn-offloss** — 使用上一周期的最后关断电流计算关断损耗的选项 `Off`（默认）| `On`

*自 R2024b 起*

使用上一周期的最后关断电流计算关断损耗的选项。

#### 依赖关系

要启用此参数，请将 **Switching Device** 设置为 `GTO`、`IGBT` 或 `MOSFET`。

### Integral Diodes

要启用这些参数，请将 **Fidelity level** 设置为 `Detailed model - switching devices`。

### **Integral protection diode** — 集成保护二极管模型 `None`（默认）| `Diode with no dynamics` | `Diode with charge dynamics`

Converter (Three-Phase) 模块用于每个开关器件的保护二极管的模型。请选择以下选项之一：

- `None` — Converter (Three-Phase) 不建模保护二极管。
- `Diode with no dynamics` — Converter (Three-Phase) 模块使用与 Diode 模块（无动态特性）相同的方程来建模保护二极管。选择此选项以优先考虑仿真速度。
- `Diode with charge dynamics` — Converter (Three-Phase) 模块使用与 Diode 模块（含电荷动态特性）相同的方程来建模保护二极管。选择此选项以优先考虑详细的仿真结果。

### **Forward voltage** — 正向电压 `0.8` `V`（默认）

使二极管 I-V 特性梯度为 1/Ron 时，`+` 和 `-` 模块端口两端所需的最小电压，其中 Ron 为 **On resistance** 参数的值。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将 **Switching device** 设置为 `Averaged Switch`。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。

### **On resistance** — 导通电阻 `0.001` `Ohm`（默认）

**Forward voltage** 参数值以上电压随电流的变化率。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将 **Switching device** 设置为 `Averaged Switch`。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。

### **Off conductance** — 关断电导 `1e-5` `1/Ohm`（默认）

反向偏置二极管的电导。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将 **Switching device** 设置为 `Averaged Switch`。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics` 或 `Diode with charge dynamics`。

### **Reverse recovery loss model** — 反向恢复损耗模型 `Fixed loss`（默认）| `Tabulated loss`

*自 R2024b 起*

选择建模固定反向恢复损耗还是表格化反向恢复损耗。

#### 依赖关系

要启用此参数：

- 将 **Switching device** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 选中 **Model thermal effects parameter** 参数。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics`。

### **Reverse recovery loss** — 反向恢复损耗 `0` `J`（默认）| 非负标量

*自 R2024b 起*

每次关断事件中耗散的能量。无论开关事件前后二极管的状态如何，模块都会耗散此能量。

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

### **Scale reverse recovery loss with current and voltage** — 反向恢复损耗随电流和电压缩放的选项 `On`（默认）| `Off`

*自 R2024b 起*

反向恢复损耗随电流和电压缩放的选项。

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

### **Forward current when measuring recovery loss, Irec** — 模块测量恢复损耗时的正向电流 `10` `A`（默认）| 正标量

*自 R2024b 起*

在模块用于测量恢复损耗的反向恢复事件之前，流过二极管的正向电流。

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
- 选中 **Scale reverse recovery loss with current and voltage** 参数。

### **Turn-off voltage when measuring recovery loss, Vrec** — 模块测量恢复损耗时的关断电压 `10` `V`（默认）| 正标量

*自 R2024b 起*

在模块用于测量恢复损耗的反向恢复事件之后，二极管两端的电压。

#### 依赖关系

要启用此参数：

- 将 **Switching device** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 选中 **Model thermal effects parameter** 参数。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics`。
- 从以下选项中选择一项：

  - 将 **Reverse recovery loss model** 设置为 `Fixed loss` 并选中 **Scale reverse recovery loss with current and voltage** 参数。
  - 将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Filter time constant for voltage and current values** — 电压和电流值的滤波时间常数 `1 / 1000 / 100` `s`（默认）| 正标量

*自 R2024b 起*

模块用于计算反向恢复损耗的电压和电流值的滤波时间常数。将此参数设置为低于最快开关周期的值。

#### 依赖关系

要启用此参数：

- 将 **Switching device** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 选中 **Model thermal effects parameter** 参数。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics`。
- 从以下选项中选择一项：

  - 将 **Reverse recovery loss model** 设置为 `Fixed loss` 并选中 **Scale reverse recovery loss with current and voltage** 参数。
  - 将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Reverse recovery loss table, Erec(Tj, If)** — 反向恢复损耗 `zeros(2, 3)` `J`（默认）| 非负标量向量

*自 R2024b 起*

作为开关事件之前正向电流 *If* 以及二极管处于关断状态后的最终关断电压的函数的耗散能量。

#### 依赖关系

要启用此参数：

- 将 **Switching device** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 选中 **Model thermal effects parameter** 参数。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics`。
- 将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Temperature vector for recovery loss table, Tj** — 恢复损耗表的温度向量 `[298.15, 398.15]` `K`（默认）| 向量

*自 R2024b 起*

模块用于将反向恢复损耗制成表格的温度向量。

#### 依赖关系

要启用此参数：

- 将 **Switching device** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 选中 **Model thermal effects parameter** 参数。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics`。
- 将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Forward current vector for recovery loss table, If** — 恢复损耗表的正向电流向量 `[.1, 1, 10]` `A`（默认）| 非负标量向量

*自 R2024b 起*

模块用于将反向恢复损耗制成表格的正向电流向量。

#### 依赖关系

要启用此参数：

- 将 **Switching device** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 选中 **Model thermal effects parameter** 参数。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics`。
- 将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Junction capacitance** — 结电容 `50e-9` `F`（默认）

二极管结电容。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Diode with charge dynamics`。

### **Peak reverse current, iRM** — 峰值反向电流 `-235` `A`（默认）| 负标量

由外部测试电路测得的峰值反向电流。此值必须小于零。默认值为 `-235` `A`。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Diode with charge dynamics`。

### **Initial forward current when measuring iRM** — 测量 iRM 时的初始正向电流 `300` `A`（默认）| 正标量

测量峰值反向电流时的初始正向电流。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Diode with charge dynamics`。

### **Rate of change of current when measuring iRM** — 测量 iRM 时的电流变化率 `-50``A/μs`（默认）| 负标量

测量峰值反向电流时的电流变化率。此值必须小于零。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Diode with charge dynamics`。

### **Reverse recovery time parameterization** — 反向恢复时间参数化 `Specify reverse recovery time directly`（默认）| `Specify stretch factor` | `Specify reverse recovery charge`

确定如何在模块中指定反向恢复时间。默认值为 `Specify reverse recovery time directly`。

如果选择 `Specify stretch factor` 或 `Specify reverse recovery charge`，则指定一个值，模块使用该值推导反向恢复时间。有关这些选项的详细信息，请参阅 How the Block Calculates TM and Tau。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Diode with charge dynamics`。

### **Reverse recovery time, trr** — 反向恢复时间 `15` `μs`（默认）

电流初始降至零（二极管关断时）与电流降至峰值反向电流的 10% 以下之间的时间间隔。**Reverse recovery time, trr** 参数的值必须大于 **Peak reverse current, iRM** 参数的值除以 **Rate of change of current when measuring iRM** 参数的值。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Diode with charge dynamics`，并将 **Reverse recovery time parameterization** 设置为 `Specify reverse recovery time directly`。

### **Reverse recovery time stretch factor** — 反向恢复时间拉伸因子 `3`（默认）| 大于 `1` 的标量

模块用于计算反向恢复时间的拉伸因子。指定拉伸因子比指定反向恢复电荷更容易参数化反向恢复时间。拉伸因子的值越大，反向恢复电流消散所需的时间越长。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Diode with charge dynamics`，并将 **Reverse recovery time parameterization** 设置为 `Specify stretch factor`。

### **Reverse recovery charge, Qrr** — 反向恢复电荷 `1500` `μAs`（默认）

模块用于计算反向恢复时间的反向恢复电荷。如果您的二极管器件数据手册指定了反向恢复电荷的值而不是反向恢复时间的值，请使用此参数。

反向恢复电荷是二极管关断时继续耗散的总电荷。该值必须小于 −i2RM2a，其中：

- *iRM* 是为 **Peak reverse current, iRM** 指定的值。
- *a* 是为 **Rate of change of current when measuring iRM** 指定的值。

#### 依赖关系

要启用此参数，请将 **Integral protection diode** 设置为 `Diode with charge dynamics`，并将 **Reverse recovery time parameterization** 设置为 `Specify reverse recovery charge`。

有关这些参数的详细信息，请参阅 Diode。

### 缓冲器

要启用这些参数，请将 **Fidelity level** 设置为 `Detailed model - switching devices`，并将 **Switching device** 设置为以下选项之一：

- `Ideal Semiconductor Switch`
- `GTO`
- `IGBT`
- `MOSFET`
- `Thyristor`

### **Snubber** — 缓冲器 `None`（默认）| `RC snubber`

每个开关器件的缓冲器。

### **Snubber resistance** — 缓冲电阻 `0.1` `Ohm`（默认）

缓冲电阻。

#### 依赖关系

要启用此参数，请将 **Snubber** 设置为 `RC snubber`。

### **Snubber capacitance** — 缓冲电容 `1e-7` `F`（默认）

缓冲电容。

#### 依赖关系

要启用此参数，请将 **Snubber** 设置为 `RC snubber`。

### 热端口

要启用这些参数：

- 在 **Main** 设置中，将 **Fidelity level** 参数设置为 `Detailed model - switching devices`。
- 在 **Switching Devices** 设置中，将 **Switching device** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 在 **Switching Devices** 设置中，选中 **Model thermal effects** 参数。

有关使用热端口和 **Thermal Port** 参数的详细信息，请参阅 Simulating Thermal Effects in Semiconductors。

### **Thermal network** — 热网络建模选项 `External`（默认）| `Specify junction and case thermal parameters` | `Cauer model` | `Cauer model parameterized with Foster coefficients`

*自 R2024b 起*

用于对模块热网络建模的选项。

### **Thermal mass parameterization** — 热质量参数化选项 `By thermal time constants`（默认）| `By thermal mass`

*自 R2024b 起*

用于参数化热质量的选项：

- `By thermal time constants` — 根据热时间常数参数化热质量。
- `By thermal mass` — 直接指定热质量值。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`、`Cauer model` 或 `Cauer model parameterized with Foster coefficients`。

### **Junction case and case-ambient (or case-heatsink) thermal resistances, [R\_JC R\_CA]** — 结-壳和壳-环境（或壳-散热器）热阻 `[.08, .5]` `K/W`（默认）| 正值向量

*自 R2024b 起*

由两个导热模块表示的两个热阻值的行向量 [ *R\_JC* *R\_CA* ]。第一个值 *R\_JC* 是结与壳之间的热阻。第二个值 *R\_CA* 是端口 **H** 与器件壳之间的热阻。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。

### **Junction and case thermal time constants, [t\_J t\_C]** — 结和壳热时间常数 `[.001, .2]` `s`（默认）| 正值向量

*自 R2024b 起*

两个热时间常数值的行向量 [ *t\_J* *t\_C* ]。第一个值 *t\_J* 是结时间常数。第二个值 *t\_C* 是壳时间常数。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`，并将 **Thermal mass parameterization** 设置为 `By thermal time constants`。

### **Junction and case thermal masses, [M\_J M\_C]** — 结和壳热质量 `[.01, .5]` `J/K`（默认）| 正值向量

*自 R2024b 起*

两个热质量值的行向量 [ *M\_J* *M\_C* ]。第一个值 *M\_J* 是结热质量。第二个值 *M\_C* 是壳热质量。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`，并将 **Thermal mass parameterization** 设置为 `By thermal mass`。

### **Junction and case initial temperatures, [T\_J T\_C]** — 结和壳初始温度 `[25, 25]` `degC`（默认）| 正值向量

*自 R2024b 起*

两个温度值的行向量 [ *T\_J* *T\_C* ]。第一个值 *T\_J* 是结初始温度。第二个值 *T\_C* 是壳初始温度。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`。

### **Thermal resistances, [R1 R2 … Rn]** — 热阻 `[.08,.1,.5]` `K/W`（默认）| `[.08,.14,.22,.16]` `K/W` | 正值向量

*自 R2024b 起*

由热网络中使用的 Cauer 元件表示的 *n* 个热阻值的行向量。

如果将 **Thermal network** 设置为 `Cauer model`，则默认值为 `[.08,.1,.5]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[.08,.14,.22,.16]`。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`。

### **Thermal masses, [M1 M2 … Mn]** — 热质量 `[.01,.1,.5]` `J/K` | `[.001,.005,.05,.5]` `J/K` | 正值向量

*自 R2024b 起*

*n* 个热质量值的行向量，其中 *n* 是热网络中 Cauer 元件的数量。

如果将 **Thermal network** 设置为 `Cauer model`，则默认值为 `[.01,.1,.5]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[.001,.005,.05,.5]`。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`，并将 **Thermal mass parameterization** 设置为 `By thermal mass`。

### **Thermal masses initial temperatures, [T1 T2 … Tn]** — 热质量初始温度 `[25, 25, 25]` `degC`（默认）| 正值向量

*自 R2024b 起*

与模型中每个热容两端温差相对应的温度值行向量。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model`。

### **Thermal time constants, [t1 t2 … tn]** — 热时间常数 `[.001,.1,.2]` `s` | `[7e-05, .0007, .01, .08]` `s` | 正值向量

*自 R2024b 起*

*n* 个热时间常数值的行向量，其中 *n* 是热网络中 Cauer 元件的数量。此向量的长度必须与 **Thermal resistances, [R1 R2 … Rn]** 的长度匹配。使用此参数化时，模块将热质量计算为 `Mi = ti/Ri`，其中 `Mi`、`ti` 和 `Ri` 分别是第 i 个 Cauer 元件（如果将 **Thermal network** 设置为 `Cauer model`）或 Foster 元件（如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`）的热质量、热时间和热阻。

如果将 **Thermal network** 设置为 `Cauer model`，则默认值为 `[.001,.1,.2]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，则默认值为 `[7e-05, .0007, .01, .08]`。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`，并将 **Thermal mass parameterization** 设置为 `By thermal time constants`。

### **初始节点温度，[T1 T2 ... Tn]** — 初始节点温度 `[25, 25, 25, 25]` `degC`（默认）| 正值向量

*自 R2024b 起*

从结点开始的每个节点的温度值行向量。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`。

### **结热质量** — 结的热质量 `0.01` `J/K`（默认）| 正标量

*自 R2024b 起*

结的热质量。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `External`。
## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2024b：使用热端口对热效应建模

您现在可以使用热端口对产生的热量和设备温度的影响进行建模。当您暴露热端口时，Converter (Three-Phase) 模块会对开关器件的导通损耗以及开通和关断损耗进行建模。如果您启用热端口并将 **Integral protection diode** 参数设置为 `Diode with no dynamics`，该模块还会对保护二极管的反向恢复损耗进行建模。

### R2024a：使用等效模型提高仿真速度

您现在可以从两个保真度级别中选择变流器模型。等效模型选项不对单个开关器件进行建模，但会返回等效结果。如果您需要开关器件动态的详细结果，请使用详细模型选项。否则，请使用等效模型以加快仿真速度。要进行实时仿真，请使用等效模型。要验证结果，请使用详细模型和变步长求解器。

要使用详细模型，请将 **Fidelity level** 参数设置为 `Detailed model - switching devices`。要使用等效模型，请将 **Fidelity level** 参数设置为 `Equivalent model - PWM-controlled`。

在 R2024a 之前，您只能使用详细模型。

### R2021b：电气连接端口更新

从 R2021b 起，要在复合端口和扩展端口之间切换，请将 **Electrical connection** 参数设置为 `Composite three-phase ports` 或 `Expanded three-phase ports`。

由于这些更改，在早期版本中保存的模型内，请检查此模块的 **Electrical connection** 参数。

## 描述

控制器驱动的双向 AC/DC 三臂变流器

Converter (Three-Phase) 模块对由三个桥臂组成的六脉冲三相可控变流器进行建模。每个桥臂包含两个开关器件。该变流器电路将三相交流网络连接到直流网络。

您可以从两个保真度级别中选择变流器模型。等效模型选项不对单个开关器件进行建模，但会返回等效结果。如果您需要开关器件动态的详细结果，请使用详细模型选项。否则，请使用等效模型以加快仿真速度。要进行实时仿真，请使用等效模型。要验证结果，请使用详细模型和变步长求解器。要使用详细模型，请将 **Fidelity level** 参数设置为 `Detailed model - switching devices`。要使用等效模型，请将 **Fidelity level** 参数设置为 `Equivalent model - PWM-controlled`。

如果您选择详细模型，三臂电路中的每个组件都是相同的开关器件，您可以通过设置 **Switching device** 参数来指定。您可以指定的开关器件是 **Simscape** > **Electrical** > **Semiconductors & Converters** 库中模块的实现：

- GTO — 门极关断晶闸管。有关该器件的 I-V 特性信息，请参阅 GTO。
- Ideal semiconductor switch — 有关该器件的 I-V 特性信息，请参阅 Ideal Semiconductor Switch。
- IGBT — 绝缘栅双极晶体管。有关该器件的 I-V 特性信息，请参阅 IGBT (Ideal, Switching)。
- MOSFET — N 沟道金属氧化物半导体场效应晶体管。有关该器件的 I-V 特性信息，请参阅 MOSFET (Ideal, Switching)。
- Thyristor — 有关该器件的 I-V 特性信息，请参阅 Thyristor (Piecewise Linear)。
- Averaged Switch — 带反并联二极管的半导体开关。控制信号端口 **G** 接受区间 [0,1] 内的值。当 **G** 等于 `0` 或 `1` 时，平均开关分别完全断开或完全闭合。该开关的行为类似于带反并联二极管的 Ideal Semiconductor Switch 模块。当 **G** 介于 0 和 1 之间时，平均开关部分断开。您可以在指定周期内对脉宽调制 (PWM) 信号取平均。然后您可以对模型进行欠采样，并使用调制波形代替 PWM 信号。

此图显示了具有全控开关器件（例如 IGBT、GTO）的变流器的等效电路。

此图显示了具有半控开关器件（例如晶闸管）的变流器的等效电路。

通过 Converter (Three-Phase) 模块上端口 **G** 的输入来控制六个开关器件的门极端口：

1. 使用 Six-Pulse Gate Multiplexer 模块将所有六个门极信号多路复用为单个向量。
2. 将 Six-Pulse Gate Multiplexer 模块的输出连接到 Converter (Three-Phase) 模块的 **G** 端口。

您可以为每个开关器件指定一个集成保护二极管。集成二极管通过为反向电流提供导通路径来保护半导体器件。当半导体器件突然切断负载的电压供应时，感性负载可能产生高反向电压尖峰。

下表显示了如何根据您的目标设置 **Integral protection diode** 参数。

| 目标 | | 要选择的值 | 集成保护二极管 |
| --- | --- | --- | --- |
| 不包含保护。 | | `None` | 无 |
| 包含保护。 | 优先考虑仿真速度。 | `Diode with no dynamics` | Diode 模块 |
| 通过精确指定反向模式电荷动态来优先考虑模型保真度。 | | `Diode with charge dynamics` | Diode 模块的动态模型 |

**注意**

如果您将 **Switching device** 参数设置为 `Averaged Switch`，该模块会对无动态的保护二极管进行建模，并且 **Integral protection diode** 参数不可见。

您可以为每个开关器件包含一个缓冲电路，该电路由串联连接的电阻和电容组成。缓冲电路保护开关器件免受感性负载在器件切断负载的电压供应时产生的高电压的影响。缓冲电路还可以防止开关器件导通时出现过大的电流变化率。

要将等效模型用作整流器，请将 PWM 信号的所有元素设置为零。该模型的行为类似于三相二极管整流器。

### 对热效应建模

*自 R2024b 起*

您可以暴露热端口来对产生的热量和设备温度的影响进行建模。要暴露热端口：

- 在 **Main** 设置中，将 **Fidelity level** 参数设置为 `Detailed model - switching devices`。
- 在 **Switching Devices** 设置中，将 **Switching device** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 在 **Switching Devices** 设置中，选中 **Model thermal effects** 参数。

有关使用热端口和 **Thermal Port** 参数的更多信息，请参阅 Simulating Thermal Effects in Semiconductors。

当您暴露热端口时，Converter (Three-Phase) 模块会对开关器件的导通损耗以及开通和关断损耗进行建模。该模块使用与以下模块相同的方法来计算这些损耗，这些模块的 **On-state behavior and switching losses** 参数设置为 `Specify constant values`：

- GTO
- IGBT (Ideal, Switching)
- MOSFET (Ideal, Switching)
- Thyristor (Piecewise Linear)

有关 Converter (Three-Phase) 模块如何计算这些损耗的更多信息，请参阅与您为 **Switching device** 参数选择的选项相匹配的模块文档。

如果您启用热端口并将 **Integral protection diode** 参数设置为 `Diode with no dynamics`，该模块还会对保护二极管的反向恢复损耗进行建模。该模块使用与 Diode 模块相同的方法来计算这些损耗，该模块的 **Fidelity level** 参数设置为 `Ideal switching`，**Diode model** 参数设置为 `Piecewise linear`。

对于理想开关，该模块不使用基于物理的电荷模型。该模块将电荷在反向恢复期间产生的损耗表示为瞬时损耗。

该模块通过将结温升高一个等于反向恢复损耗除以结处总热质量的值来施加反向恢复损耗。

如果您将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`，则 **Reverse recovery loss table, Erec(Tj, If)** 参数的值指定了作为结温和开关事件前正向电流的函数的耗散能量。断态电压相对于 **Turn-off voltage when measuring recovery loss, Vrec** 参数值线性缩放损耗。该表使用电流和电压的延迟值。要使用查找表中接近瞬时值的值，请将 **Filter time constant for voltage and current values** 参数设置为低于最快开关周期的值。

如果您将 **Reverse recovery loss model** 参数设置为 `Fixed loss`，则 **Reverse recovery loss** 参数的值指定了每次关断事件期间耗散的能量。如果您选中 **Scale reverse recovery loss with current and voltage** 参数，则该模块会按通态电流和断态电压线性缩放此损耗值。要使用接近瞬时值的缩放值，请将 **Filter time constant for voltage and current values** 设置为低于最快开关周期的值。

### 用于 FPGA 部署的平均开关分段常数近似

如果您将 **Switching device** 参数设置为 `Averaged switch`，并且您的模型使用分区求解器，则该模块会产生非线性分区，因为平均模式方程包含作为输入 **G** 的函数的模式 *Gsat*。为了使这些方程与硬件描述语言 (HDL) 代码生成兼容，从而支持 FPGA 部署，请将 **Integer for piecewise constant approximation of gate input (0 for disabled)** 参数设置为大于 `0` 的值。然后该模块将 *Gsat* 模式视为具有固定范围的分段常数整数。这将之前的非线性分区转换为线性时变分区。

范围 `[0,K]` 内的整数值（其中 *K* 是 **Integer for piecewise constant approximation of gate input (0 for disabled)** 的值）现在与范围 `[0,1]` 内的每个实值模式相关联。该模块通过将原始模式除以 K 将其归一化回范围 `[0,1]` 来计算分段常数模式：

uI=(floor(u⋅K))u^=uIK

### 假设和限制

- 如果在您模型内的 Solver Configuration 模块中，您将 **Solver type** 参数设置为 `Partitioning`，则平均开关会在死区时间期间引入不稳定性，此时所有门极输入都设置为 0。在可能的情况下，通过将所有高侧开关设置为 0 并将所有低侧开关设置为 1 来使用开零状态。
- 要将 Converter (Three-Phase) 模块用作有源前端整流器，如果您将 **Fidelity level** 参数设置为 `Equivalent model - PWM-controlled` 或将 **Switching device** 参数设置为 `Averaged Switch`，则必须在直流侧添加中点接地系统。此图显示了如何使用两个电阻或两个电容构建中点接地系统。
