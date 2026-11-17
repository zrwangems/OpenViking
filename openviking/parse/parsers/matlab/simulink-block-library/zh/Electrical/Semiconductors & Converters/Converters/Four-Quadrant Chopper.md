---
type: simulink-block
title: 'Four-Quadrant Chopper'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'fourquadrantchopper'
documentation_source_path: 'ref/fourquadrantchopper.html'
language: zh-CN
chinese_source: worker-translation
---

# Four-Quadrant Chopper

## 端口
```yaml
ports:
- name: G
  summary: 开关器件门极控制 电气 | 向量
  direction: conserving
  data_types: double
- name: 1+
  summary: 直流电压 1 正极 电气 | 标量
  direction: conserving
  data_types: double
- name: 1-
  summary: 直流电压 1 负极 电气 | 标量
  direction: conserving
  data_types: double
- name: 2+
  summary: 直流电压 2 正极 电气 | 标量
  direction: conserving
  data_types: double
- name: 2-
  summary: 直流电压 2 负极 电气 | 标量
  direction: conserving
  data_types: double
- name: H
  summary: 热端口 热
  direction: conserving
```

### 守恒端口

### **G** — 开关器件门极控制 电气 | 向量

与开关器件门极端子关联的电气守恒端口。

**数据类型：** `double`

### **1+** — 直流电压 1 正极 电气 | 标量

与第一个直流电压正极端子关联的电气守恒端口。

**数据类型：** `double`

### **1-** — 直流电压 1 负极 电气 | 标量

与第一个直流电压负极端子关联的电气守恒端口。

**数据类型：** `double`

### **2+** — 直流电压 2 正极 电气 | 标量

与第二个直流电压正极端子关联的电气守恒端口。

**数据类型：** `double`

### **2-** — 直流电压 2 负极 电气 | 标量

与第二个直流电压负极端子关联的电气守恒端口。

**数据类型：** `double`

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
```yaml
parameters:
- name: Fidelity level
  summary: 保真度级别 Detailed model - switching devices（默认）| Equivalent model - PWM-controlled
  group: 主要参数
- name: Switching device
  summary: 开关类型 Ideal Semiconductor Switch（默认）| GTO | IGBT | MOSFET | Thyristor | Averaged Switch
  group: Switching Devices
- name: Model thermal effects
  summary: 热效应建模选项 Off（默认）| On
  group: Switching Devices
- name: Gate trigger voltage, Vgt
  summary: 电压阈值 1 V（默认）| 标量
  group: Switching Devices
- name: Gate turn-off voltage, Vgt_off
  summary: 电压阈值 -1 V（默认）| 标量
  group: Switching Devices
- name: Holding current
  summary: 电流阈值 1 A（默认）| 标量
  group: Switching Devices
- name: Forward voltage
  summary: 电压 0.8 Ohm（默认）| 标量
  group: Switching Devices
- name: On-state resistance
  summary: 电阻 0.001 Ohm（默认）| 标量
  group: Switching Devices
- name: Drain-source on resistance
  summary: 电阻 0.001 Ohm（默认）| 标量
  group: Switching Devices
- name: Off-state conductance
  summary: 电导 1e-5 1/Ohm（默认）| 标量
  group: Switching Devices
- name: Threshold voltage
  summary: 电压阈值 6 V（默认）| 标量
  group: Switching Devices
- name: Integer for piecewise constant approximation of gate input (0 for disabled)
  summary: FPGA 部署的整数模式 0（默认）| 非负标量
  group: Switching Devices
- name: Switch-on loss
  summary: 开通损耗 22.86e-3 J（默认）| 正标量
  group: Switching Losses
- name: Switch-off loss
  summary: 关断损耗 17.14e-3 J（默认）| 正标量
  group: Switching Losses
- name: Natural commutation rectification loss
  summary: 自然换流整流损耗 10e-3 J（默认）| 正标量
  group: Switching Losses
- name: Off-state voltage for switching loss data
  summary: 损耗数据的断态电压 300 V（默认）| 正标量
  group: Switching Losses
- name: On-state current for switching loss data
  summary: 输出电流 600 A（默认）| 正标量
  group: Switching Losses
- name: Wait time before switch-on current measurement
  summary: 开通电流测量前的等待时间 0 s（默认）| 非负标量
  group: Switching Losses
- name: Use last on-state current from previous cycle for turn-on loss
  summary: 使用上一周期的最后通态电流计算开通损耗的选项 Off（默认）| On
  group: Switching Losses
- name: Use last off-state current from previous cycle for turn-offloss
  summary: 使用上一周期的最后断态电流计算关断损耗的选项 Off（默认）| On
  group: Switching Losses
- name: Model dynamics
  summary: 二极管模型 None（默认）| Diode with no dynamics | Diode with charge dynamics
  group: Protection Diodes
- name: Forward voltage
  summary: 正向电压 0.8 V（默认）| 标量
  group: Protection Diodes
- name: On resistance
  summary: 导通电阻 0.001 Ohm（默认）| 标量
  group: Protection Diodes
- name: Off conductance
  summary: 断态电导 1e-5 1/Ohm（默认）| 标量
  group: Protection Diodes
- name: Reverse recovery loss model
  summary: 反向恢复损耗模型 Fixed loss（默认）| Tabulated loss
  group: Protection Diodes
- name: Reverse recovery loss
  summary: 反向恢复损耗 0 J（默认）| 非负标量
  group: Protection Diodes
- name: Scale reverse recovery loss with current and voltage
  summary: 根据电流和电压缩放反向恢复损耗的选项 On（默认）| Off
  group: Protection Diodes
- name: Forward current when measuring recovery loss, Irec
  summary: 模块测量恢复损耗时的正向电流 10 A（默认）| 正标量
  group: Protection Diodes
- name: Turn-off voltage when measuring recovery loss, Vrec
  summary: 测量恢复损耗时的关断电压 10 V（默认）| 正标量
  group: Protection Diodes
- name: Filter time constant for voltage and current values
  summary: 电压和电流值的滤波时间常数 1 / 1000 / 100 s（默认）| 正标量
  group: Protection Diodes
- name: Reverse recovery loss table, Erec(Tj, If)
  summary: 反向恢复损耗 zeros(2, 3) J（默认）| 非负标量向量
  group: Protection Diodes
- name: Temperature vector for recovery loss table, Tj
  summary: 恢复损耗表的温度向量 [298.15, 398.15] K（默认）| 向量
  group: Protection Diodes
- name: Forward current vector for recovery loss table, If
  summary: 恢复损耗表的正向电流向量 [.1, 1, 10] A（默认）| 非负标量向量
  group: Protection Diodes
- name: Junction capacitance
  summary: 结电容 50 nF（默认）| 标量
  group: Protection Diodes
- name: Peak reverse current, iRM
  summary: 峰值反向电流 -235 A（默认）| 负标量
  group: Protection Diodes
- name: Initial forward current when measuring iRM
  summary: 测量 iRM 时的初始正向电流 300 A（默认）| 正标量
  group: Protection Diodes
- name: Rate of change of current when measuring iRM
  summary: 测量 iRM 时的电流变化率 -50 A/us（默认）| 标量
  group: Protection Diodes
- name: Reverse recovery time parameterization
  summary: 恢复时间模型 Specify stretch factor（默认）| Specify reverse recovery time directly | Specify reverse recovery charge
  group: Protection Diodes
- name: Reverse recovery time stretch factor
  summary: 反向恢复时间拉伸因子 3（默认）| 大于 1 的标量
  group: Protection Diodes
- name: Reverse recovery time, trr
  summary: 反向恢复时间 15 us（默认）| 标量
  group: Protection Diodes
- name: Reverse recovery charge, Qrr
  summary: 反向恢复电荷 1500 s*uA（默认）| 标量
  group: Protection Diodes
- name: Snubber
  summary: 缓冲器模型 None（默认）| RC snubber
  group: 缓冲器
- name: Snubber resistance
  summary: 电阻 0.1 Ohm（默认）| 标量
  group: 缓冲器
- name: Snubber capacitance
  summary: 电容 1e-7（默认）| F | 标量
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
  summary: 热阻 [.08,.1,.5] K/W | [.08,.14,.22,.16] K/W | 正值向量
  group: 热端口
- name: Thermal masses, [M1 M2 … Mn]
  summary: 热质量 [.01,.1,.5] J/K | [.001,.005,.05,.5] J/K | 正值向量
  group: 热端口
- name: Thermal masses initial temperatures, [T1 T2 … Tn]
  summary: 热质量初始温度 [25, 25, 25] degC（默认）| 正值向量
  group: 热端口
- name: 热时间常数，[t1 t2 … tn]
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

### **Fidelity level** — 保真度级别 `Detailed model - switching devices`（默认）| `Equivalent model - PWM-controlled`

*自 R2024a 起*

模型的保真度级别。

要优先考虑仿真精度或获取各个开关器件的结果，请将此参数设置为 `Detailed model - switching devices`。

要优先考虑仿真速度，请将此参数设置为 `Equivalent model - PWM-controlled`。

### Switching Devices

要启用这些参数，请将 **Fidelity level** 设置为 `Detailed model - switching devices`。

此表显示了 **Switching Devices** 参数的可见性如何取决于您所选择的开关器件。要了解如何阅读该表，请参阅参数依赖关系。

**Switching Devices 参数依赖关系**

| 参数和选项 | | | | | |
| --- | --- | --- | --- | --- | --- |
| **Switching device** | | | | | |
| *`Ideal Semiconductor Switch`* | *`GTO`* | *`IGBT`* | *`MOSFET`* | *`Thyristor`* | *`Averaged Switch`* |
| On-state resistance | Model thermal effects | Model thermal effects | Model thermal effects | Model thermal effects | On-state resistance |
| Gate trigger voltage, Vgt | Gate trigger voltage, Vgt |
| Gate turn-off voltage, Vgt\_off | Gate turn-off voltage, Vgt\_off |
| Holding current | Holding current |
| Forward voltage | Forward voltage | Forward voltage |
| On-state resistance | On-state resistance | Drain-source on resistance | On-state resistance |
| 关断电导 | 关断电导 | 关断电导 | 关断电导 | 关断电导 | 用于栅极输入分段常数逼近的整数（0 表示禁用） |
| Threshold voltage | Threshold voltage | Threshold voltage |

### **Switching device** — 开关类型 `Ideal Semiconductor Switch`（默认）| `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

变换器的开关器件类型。

#### 依赖关系

请参阅 Switching Devices 参数依赖关系表。

### **Model thermal effects** — 热效应建模选项 `Off`（默认）| `On`

热效应建模选项。

#### 依赖关系

请参阅 Switching Devices 参数依赖关系表。

### **Gate trigger voltage, Vgt** — 电压阈值 `1` `V`（默认）| 标量

门极-阴极电压阈值。当门极-阴极电压高于此值时，器件导通。

#### 依赖关系

请参阅 Switching Devices 参数依赖关系表。

### **Gate turn-off voltage, Vgt\_off** — 电压阈值 `-1` `V`（默认）| 标量

门极-阴极电压阈值。当门极-阴极电压低于此值时，器件关断。

#### 依赖关系

请参阅 Switching Devices 参数依赖关系表。

### **Holding current** — 电流阈值 `1` `A`（默认）| 标量

门极电流阈值。当电流高于此值时，即使门极-阴极电压降至门极触发电压以下，器件仍保持导通。

#### 依赖关系

请参阅 Switching Devices 参数依赖关系表。

### **Forward voltage** — 电压 `0.8` `Ohm`（默认）| 标量

对于不同的开关器件类型，**Forward voltage** 取值如下：

- GTO — 使器件 I-V 特性梯度为 1/*Ron* 时，阳极和阴极模块端口两端所需的最小电压，其中 *Ron* 为 **On-state resistance** 的值
- IGBT — 使二极管 I-V 特性梯度为 1/*Ron* 时，集电极和发射极模块端口两端所需的最小电压，其中 *Ron* 为 **On-state resistance** 的值
- Thyristor — 器件导通所需的最小电压

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

漏极与源极之间的电阻，该电阻还取决于栅极-源极电压。

#### 依赖关系

请参阅 Switching Devices 参数依赖关系表。

### **Off-state conductance** — 电导 `1e-5` `1/Ohm`（默认）| 标量

器件关断时的电导。该值必须小于 1/*R*，其中 *R* 为 **On-state resistance** 的值。

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

- Ideal semiconductor switch — 门极-阴极电压
- IGBT — 栅极-发射极电压
- MOSFET — 栅极-源极电压

#### 依赖关系

请参阅 Switching Devices 参数依赖关系表。

### **Integer for piecewise constant approximation of gate input (0 for disabled)** — FPGA 部署的整数模式 `0`（默认）| 非负标量

用于对 FPGA 部署的门极输入执行分段常数逼近的整数。

#### 依赖关系

要启用此参数，请将 **Switching device** 设置为 `Averaged Switch`。

### Switching Losses

要启用这些参数：

- 在 **Main** 设置中，将 **Fidelity level** 参数设置为 `Detailed model - switching devices`。
- 在 **Switching Devices** 设置中，将 **Switching device** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 在 **Switching Devices** 设置中，选择 **Model thermal effects** 参数。

此表显示了 **Switching Loss** 参数的可见性如何取决于 **Switching Devices** 设置中的 **Switching device** 参数。要了解如何阅读此表，请参阅 Parameter Dependencies。

**Switching Losses Parameter Dependencies**

| Parameters and Options | | | |
| --- | --- | --- | --- |
| **Switching device** | | | |
| *`GTO`* | *`IGBT`* | *`MOSFET`* | *`Thyristor`* |
| Switch-on loss | Switch-on loss | Switch-on loss | Switch-on loss |
| Switch-off loss | Switch-off loss | Switch-off loss |
| Natural commutation rectification loss | Natural commutation rectification loss |
| 用于开关损耗数据的关断电压 | 用于开关损耗数据的关断电压 | 用于开关损耗数据的关断电压 | 用于开关损耗数据的关断电压 |
| 用于开关损耗数据的导通电流 | 用于开关损耗数据的导通电流 | 用于开关损耗数据的导通电流 | 用于开关损耗数据的导通电流 |
| Wait time before switch-on current measurement | Wait time before switch-on current measurement |
| 使用上一周期的最后导通电流计算开通损耗 | 使用上一周期的最后导通电流计算开通损耗 | 使用上一周期的最后导通电流计算开通损耗 |
| 使用上一周期的最后关断电压计算开通损耗 | 使用上一周期的最后导通电流计算开通损耗 | 使用上一周期的最后导通电流计算开通损耗 |

### **Switch-on loss** — 开通损耗 `22.86e-3` `J`（默认）| 正标量

*自 R2024b 起*

单次开通事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **Switching Device** 设置为 `GTO`、`IGBT`、`MOSFET` 或 `Thyristor`。

### **Switch-off loss** — 关断损耗 `17.14e-3` `J`（默认）| 正标量

*自 R2024b 起*

单次关断事件期间耗散的能量。

#### 依赖关系

要启用此参数，请将 **Switching Device** 设置为 `GTO`、`IGBT` 或 `MOSFET`。

### **Natural commutation rectification loss** — 自然换流整流损耗 `10e-3` `J`（默认）| 正标量

*自 R2024b 起*

当电流降至 **Holding current** 参数值以下且模块关断时适用的整流损耗。

#### 依赖关系

要启用此参数，请将 **Switching Device** 设置为 `GTO` 或 `Thyristor`。

### **Off-state voltage for switching loss data** — 损耗数据的断态电压 `300` `V`（默认）| 正标量

*自 R2024b 起*

器件在断态期间的输出电压。此值是您定义开通损耗和关断损耗数据时的阻断电压。

#### 依赖关系

要启用此参数，请将 **Switching Device** 设置为 `GTO`、`IGBT`、`MOSFET` 或 `Thyristor`。

### **On-state current for switching loss data** — 输出电流 `600` `A`（默认）| 正标量

*自 R2024b 起*

您定义开通损耗和关断损耗时的输出电流。

**注意**

模块在栅极电压降至 **Gate trigger voltage, Vgt** 参数值以下时测量此参数。开通脉冲长于电流达到其最大值所需的时间。

#### 依赖关系

要启用此参数，请将 **Switching Device** 设置为 `GTO`、`IGBT`、`MOSFET` 或 `Thyristor`。

### **Wait time before switch-on current measurement** — 开通电流测量前的等待时间 `0` `s`（默认）| 非负标量

*自 R2024b 起*

记录通态电流之前等待的时间。

#### 依赖关系

要启用此参数，请将 **Switching Device** 设置为 `GTO` 或 `Thyristor`。

### **Use last on-state current from previous cycle for turn-on loss** — 使用上一周期的最后通态电流计算开通损耗的选项 `Off`（默认）| `On`

*自 R2024b 起*

使用上一周期的最后通态电流计算开通损耗的选项。

#### 依赖关系

要启用此参数，请将 **Switching Device** 设置为 `GTO`、`IGBT` 或 `MOSFET`。

### **Use last off-state current from previous cycle for turn-offloss** — 使用上一周期的最后断态电流计算关断损耗的选项 `Off`（默认）| `On`

*自 R2024b 起*

使用上一周期的最后断态电流计算关断损耗的选项。

#### 依赖关系

要启用此参数，请将 **Switching Device** 设置为 `GTO`、`IGBT` 或 `MOSFET`。

### Protection Diodes

要启用这些参数，请将 **Fidelity level** 设置为 `Detailed model - switching devices`。

**Diode** 参数的可见性取决于您如何配置 **Model dynamics** 和 **Reverse recovery time parameterization** 参数。要了解如何阅读此表，请参阅 Parameter Dependencies。

**Protection Diodes Parameter Dependencies**

| Parameters and Options | | | | |
| --- | --- | --- | --- | --- |
| **Model dynamics** | | | | |
| *None* | *Diode with no dynamics* | *Diode with charge dynamics* | | |
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

**注意**

如果您将 **Switching device** 参数设置为 `Averaged Switch`，则模块对保护二极管建模时无动态特性，并且 **Model dynamics** 参数不可见。

### **Model dynamics** — 二极管模型 `None`（默认）| `Diode with no dynamics` | `Diode with charge dynamics`

Four-Quadrant Chopper 模块用于每个开关器件保护二极管的模型。选择以下选项之一：

- `None` — Four-Quadrant Chopper 不对保护二极管建模。
- `Diode with no dynamics` — Four-Quadrant Chopper 模块使用与无动态特性的 Diode 模块相同的方程对保护二极管建模。选择此选项可优先考虑仿真速度。
- `Diode with charge dynamics` — Four-Quadrant Chopper 模块使用与具有电荷动态特性的 Diode 模块相同的方程对保护二极管建模。选择此选项可优先考虑详细的仿真结果。

#### 依赖关系

请参阅 Protection Diodes Parameter Dependencies 表。

### **Forward voltage** — 正向电压 `0.8` `V`（默认）| 标量

使二极管 I-V 特性的梯度为 1/*Ron* 所需的跨模块正负端口的最小电压，其中 *Ron* 是 **On resistance** 参数的值。

#### 依赖关系

请参阅 Protection Diodes Parameter Dependencies 表。

### **On resistance** — 导通电阻 `0.001` `Ohm`（默认）| 标量

高于 **Forward voltage** 参数值时电压随电流的变化率。

#### 依赖关系

请参阅 Protection Diodes Parameter Dependencies 表。

### **Off conductance** — 断态电导 `1e-5` `1/Ohm`（默认）| 标量

反向偏置二极管的电导。

#### 依赖关系

请参阅 Protection Diodes Parameter Dependencies 表。

### **Reverse recovery loss model** — 反向恢复损耗模型 `Fixed loss`（默认）| `Tabulated loss`

*自 R2024b 起*

是对固定反向恢复损耗建模还是对表格化反向恢复损耗建模。

#### 依赖关系

要启用此参数：

- 将 **Switching device** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 选择 **Model thermal effects parameter** 参数。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics`。

### **Reverse recovery loss** — 反向恢复损耗 `0` `J`（默认）| 非负标量

*自 R2024b 起*

每次关断事件中耗散的能量。无论开关事件前后二极管的状态如何，该模块都会耗散此能量。

#### 依赖关系

要启用此参数：

- 将 **Switching device** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 选择 **Model thermal effects parameter** 参数。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics`。
- 将 **Reverse recovery loss model** 设置为 `Fixed loss`。

### **Scale reverse recovery loss with current and voltage** — 根据电流和电压缩放反向恢复损耗的选项 `On`（默认）| `Off`

*自 R2024b 起*

根据电流和电压缩放反向恢复损耗的选项。

#### 依赖关系

要启用此参数：

- 将 **Switching device** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 选择 **Model thermal effects parameter** 参数。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics`。
- 将 **Reverse recovery loss model** 设置为 `Fixed loss`。

### **Forward current when measuring recovery loss, Irec** — 模块测量恢复损耗时的正向电流 `10` `A`（默认）| 正标量

*自 R2024b 起*

在反向恢复事件之前流过二极管的正向电流，模块使用该电流来测量恢复损耗。

#### 依赖关系

要启用此参数：

- 将 **Switching device** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 选择 **Model thermal effects parameter** 参数。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics`。
- 将 **Reverse recovery loss model** 设置为 `Fixed loss`。
- 选择 **Scale reverse recovery loss with current and voltage** 参数。

### **Turn-off voltage when measuring recovery loss, Vrec** — 测量恢复损耗时的关断电压 `10` `V`（默认）| 正标量

*自 R2024b 起*

反向恢复事件之后二极管两端的电压，模块使用该电压来测量恢复损耗。

#### 依赖关系

要启用此参数：

- 将 **Switching device** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 选择 **Model thermal effects parameter** 参数。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics`。
- 从以下选项中选择一项：

  - 将 **Reverse recovery loss model** 设置为 `Fixed loss` 并选择 **Scale reverse recovery loss with current and voltage** 参数。
  - 将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Filter time constant for voltage and current values** — 电压和电流值的滤波时间常数 `1 / 1000 / 100` `s`（默认）| 正标量

*自 R2024b 起*

模块用于计算反向恢复损耗的电压和电流值的滤波时间常数。将此参数设置为小于最快开关周期的值。

#### 依赖关系

要启用此参数：

- 将 **Switching device** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 选择 **Model thermal effects parameter** 参数。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics`。
- 从以下选项中选择一项：

  - 将 **Reverse recovery loss model** 设置为 `Fixed loss` 并选择 **Scale reverse recovery loss with current and voltage** 参数。
  - 将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Reverse recovery loss table, Erec(Tj, If)** — 反向恢复损耗 `zeros(2, 3)` `J`（默认）| 非负标量向量

*自 R2024b 起*

作为开关事件之前正向电流 *If* 以及二极管进入关断状态后的最终关断电压的函数的耗散能量。

#### 依赖关系

要启用此参数：

- 将 **Switching device** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 选择 **Model thermal effects parameter** 参数。
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
- 选择 **Model thermal effects parameter** 参数。
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
- 选择 **Model thermal effects parameter** 参数。
- 将 **Integral protection diode** 设置为 `Diode with no dynamics`。
- 将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`。

### **Junction capacitance** — 结电容 `50` `nF`（默认）| 标量

二极管结电容。

#### 依赖关系

请参阅保护二极管参数依赖关系表。

### **Peak reverse current, iRM** — 峰值反向电流 `-235` `A`（默认）| 负标量

由外部测试电路测得的峰值反向电流。

#### 依赖关系

请参阅保护二极管参数依赖关系表。

### **Initial forward current when measuring iRM** — 测量 iRM 时的初始正向电流 `300` `A`（默认）| 正标量

测量峰值反向电流时的初始正向电流。

#### 依赖关系

请参阅保护二极管参数依赖关系表。

### **Rate of change of current when measuring iRM** — 测量 iRM 时的电流变化率 `-50` `A/us`（默认）| 标量

测量峰值反向电流时的电流变化率。

#### 依赖关系

请参阅保护二极管参数依赖关系表。

### **Reverse recovery time parameterization** — 恢复时间模型 `Specify stretch factor`（默认）| `Specify reverse recovery time directly` | `Specify reverse recovery charge`

用于参数化恢复时间的模型。当您选择 `Specify stretch factor` 或 `Specify reverse recovery charge` 时，可以指定一个值，模块使用该值来推导反向恢复时间。有关这些选项的详细信息，请参阅模块如何计算 TM 和 Tau。

#### 依赖关系

请参阅保护二极管参数依赖关系表。

### **Reverse recovery time stretch factor** — 反向恢复时间拉伸因子 `3`（默认）| 大于 `1` 的标量

模块用于计算反向恢复时间的拉伸因子。指定拉伸因子比指定反向恢复电荷更容易参数化反向恢复时间。拉伸因子的值越大，反向恢复电流消散所需的时间就越长。

#### 依赖关系

请参阅保护二极管参数依赖关系表。

### **Reverse recovery time, trr** — 反向恢复时间 `15` `us`（默认）| 标量

电流初始降为零（二极管关断时）与电流降至峰值反向电流的 10% 以下之间的时间间隔。

**Reverse recovery time, trr** 参数的值必须大于 **Peak reverse current, iRM** 参数的值除以 **Rate of change of current when measuring iRM** 参数的值。

#### 依赖关系

请参阅 Protection Diodes Parameter Dependencies 表。

### **Reverse recovery charge, Qrr** — 反向恢复电荷 `1500` `s*uA`（默认）| 标量

模块用于计算反向恢复时间的反向恢复电荷。如果您的二极管器件数据手册指定了反向恢复电荷的值而不是反向恢复时间的值，请使用此参数。

反向恢复电荷是二极管关断时继续耗散的总电荷。该值必须小于 −i2RM2a，其中：

- *iRM* 是为 **Peak reverse current, iRM** 指定的值。
- *a* 是为 **Rate of change of current when measuring iRM** 指定的值。

#### 依赖关系

请参阅 Protection Diodes Parameter Dependencies 表。

### 缓冲器

要启用这些参数，请将 **Fidelity level** 设置为 `Detailed model - switching devices`，并将 **Switching device** 设置为以下选项之一：

- `Ideal Semiconductor Switch`
- `GTO`
- `IGBT`
- `MOSFET`
- `Thyristor`

### **Snubber** — 缓冲器模型 `None`（默认）| `RC snubber`

开关器件缓冲器。

### **Snubber resistance** — 电阻 `0.1` `Ohm`（默认）| 标量

开关器件缓冲器的电阻。

#### 依赖关系

要启用此参数，请将 **Snubber** 设置为 `RC Snubber`。

### **Snubber capacitance** — 电容 `1e-7`（默认）| `F` | 标量

开关器件缓冲器的电容。

#### 依赖关系

要启用此参数，请将 **Snubber** 设置为 `RC Snubber`。

### 热端口

要启用这些参数：

- 在 **Main** 设置中，将 **Fidelity level** 参数设置为 `Detailed model - switching devices`。
- 在 **Switching Devices** 设置中，将 **Switching device** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 在 **Switching Devices** 设置中，选择 **Model thermal effects** 参数。

有关使用热端口和 **Thermal Port** 参数的更多信息，请参阅 Simulating Thermal Effects in Semiconductors。

### **Thermal network** — 热网络建模选项 `External`（默认）| `Specify junction and case thermal parameters` | `Cauer model` | `Cauer model parameterized with Foster coefficients`

*自 R2024b 起*

用于对模块的热网络进行建模的选项。

### **Thermal mass parameterization** — 热质量参数化选项 `By thermal time constants`（默认）| `By thermal mass`

*自 R2024b 起*

用于对热质量进行参数化的选项：

- `By thermal time constants` — 根据热时间常数对热质量进行参数化。
- `By thermal mass` — 直接指定热质量值。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Specify junction and case thermal parameters`、`Cauer model` 或 `Cauer model parameterized with Foster coefficients`。

### **Junction case and case-ambient (or case-heatsink) thermal resistances, [R\_JC R\_CA]** — 结-壳和壳-环境（或壳-散热器）热阻 `[.08, .5]` `K/W`（默认）| 正值向量

*自 R2024b 起*

由两个 Conductive Heat Transfer 模块表示的两个热阻值的行向量 [ *R\_JC* *R\_CA* ]。第一个值 *R\_JC* 是结与壳之间的热阻。第二个值 *R\_CA* 是端口 **H** 与器件壳之间的热阻。

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

### **Thermal resistances, [R1 R2 … Rn]** — 热阻 `[.08,.1,.5]` `K/W` | `[.08,.14,.22,.16]` `K/W` | 正值向量

*自 R2024b 起*

由热网络中使用的 Cauer 元件表示的 *n* 个热阻值的行向量。

如果将 **Thermal network** 设置为 `Cauer model`，默认值为 `[.08,.1,.5]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，默认值为 `[.08,.14,.22,.16]`。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`。

### **Thermal masses, [M1 M2 … Mn]** — 热质量 `[.01,.1,.5]` `J/K` | `[.001,.005,.05,.5]` `J/K` | 正值向量

*自 R2024b 起*

*n* 个热质量值的行向量，其中 *n* 是热网络中 Cauer 元件的数量。

如果将 **Thermal network** 设置为 `Cauer model`，默认值为 `[.01,.1,.5]`。如果将 **Thermal network** 设置为 `Cauer model parameterized with Foster coefficients`，默认值为 `[.001,.005,.05,.5]`。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model` 或 `Cauer model parameterized with Foster coefficients`，并将 **Thermal mass parameterization** 设置为 `By thermal mass`。

### **Thermal masses initial temperatures, [T1 T2 … Tn]** — 热质量初始温度 `[25, 25, 25]` `degC`（默认）| 正值向量

*自 R2024b 起*

与模型中每个热容两端温差相对应的温度值行向量。

#### 依赖关系

要启用此参数，请将 **Thermal network** 设置为 `Cauer model`。

### **热时间常数，[t1 t2 … tn]** — 热时间常数 `[.001,.1,.2]` `s` | `[7e-05, .0007, .01, .08]` `s` | 正值向量

*自 R2024b 起*

由 *n* 个热时间常数值组成的行向量，其中
*n* 是热网络中 Cauer 元件的数量。该向量的长度必须与
**热阻，[R1 R2 … Rn]** 的长度一致。使用此参数化方式时，模块将热质量计算为
`Mi =
ti/Ri`，
其中 `Mi`、
`ti` 和
`Ri` 分别是第
i 个 Cauer 元件（如果将
**热网络** 设置为 `Cauer
模型`）或 Foster 元件（如果将 **热网络**
设置为 `使用 Foster 系数参数化的 Cauer
模型`）的热质量、热时间和热阻。

如果将 **热网络** 设置为 `Cauer
模型`，默认值为
`[.001,.1,.2]`。如果将 **热网络**
设置为 `使用 Foster 系数参数化的 Cauer
模型`，默认值为
`[7e-05, .0007, .01, .08]`。

#### 依赖关系

要启用此参数，请将 **热网络**
设置为 `Cauer 模型` 或 `使用 Foster
系数参数化的 Cauer 模型`，并将
**热质量参数化** 设置为
`按热时间常数`。

### **初始节点温度，[T1 T2 ... Tn]** — 初始节点温度 `[25, 25, 25, 25]` `degC`（默认）| 正值向量

*自 R2024b 起*

从结开始每个节点的温度值组成的行向量。

#### 依赖关系

要启用此参数，请将 **热网络**
设置为 `使用 Foster 系数参数化的 Cauer
模型`。

### **结热质量** — 结的热质量 `0.01` `J/K`（默认）| 正标量

*自 R2024b 起*

结的热质量。

#### 依赖关系

要启用此参数，请将 **热网络**
设置为 `外部`。
## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2024b：使用热端口对热效应建模

您现在可以使用热端口对产生的热量和设备温度的影响进行建模。当您暴露热端口时，Four-Quadrant Chopper 模块会对开关器件的导通损耗以及开通和关断损耗进行建模。如果您启用热端口并将 **集成保护二极管** 参数设置为 `无动态特性的二极管`，该模块还会对保护二极管的反向恢复损耗进行建模。

### R2024a：使用等效模型提高仿真速度

您现在可以从两个保真度级别中选择变流器模型。等效模型选项不对单个开关器件进行建模，但会返回等效结果。如果您需要开关器件动态特性的详细结果，请使用详细模型选项。否则，请使用等效模型以获得更快的仿真速度。要进行实时仿真，请使用等效模型。要验证结果，请使用详细模型和变步长求解器。

要使用详细模型，请将 **保真度级别** 参数设置为 `详细模型 - 开关器件`。要使用等效模型，请将 **保真度级别** 参数设置为 `等效模型 - PWM 控制`。

在 R2024a 之前，您只能使用详细模型。

## 描述

控制器驱动的四象限 DC-DC 斩波器

Four-Quadrant Chopper 模块表示用于将固定直流输入转换为可变直流输出的四象限受控斩波器。该模块包含两个桥臂。每个桥臂有两个开关器件。

您可以从两个保真度级别中选择变流器模型。等效模型选项不对单个开关器件进行建模，但会返回等效结果。如果您需要开关器件动态特性的详细结果，请使用详细模型选项。否则，请使用等效模型以获得更快的仿真速度。要进行实时仿真，请使用等效模型。要验证结果，请使用详细模型和变步长求解器。要使用详细模型，请将 **保真度级别** 参数设置为 `详细模型 - 开关器件`。要使用等效模型，请将 **保真度级别** 参数设置为 `等效模型 - PWM 控制`。

如果您选择详细模型，每个组件都是相同的开关器件，您可以通过设置 **开关器件** 参数来指定。您可以指定的开关器件是 **Simscape** > **Electrical** > **Semiconductors & Converters** 库中模块的实现：

- GTO — 门极关断晶闸管。有关该器件的 I-V 特性信息，请参阅 GTO。
- Ideal semiconductor switch — 有关该器件的 I-V 特性信息，请参阅 Ideal Semiconductor Switch。
- IGBT — 绝缘栅双极晶体管。有关该器件的 I-V 特性信息，请参阅 IGBT (Ideal, Switching)。
- MOSFET — N 沟道金属氧化物半导体场效应晶体管。有关该器件的 I-V 特性信息，请参阅 MOSFET (Ideal, Switching)。
- Thyristor — 有关该器件的 I-V 特性信息，请参阅 Thyristor (Piecewise Linear)。
- Averaged Switch — 带反并联二极管的半导体开关。控制信号端口 **G** 接受区间 [0,1] 内的值。当 **G** 等于 `0` 或 `1` 时，平均开关分别完全断开或完全闭合。该开关的行为类似于带反并联二极管的 Ideal Semiconductor Switch 模块。当 **G** 介于 0 和 1 之间时，平均开关部分断开。您可以在指定周期内对脉宽调制 (PWM) 信号进行平均。然后您可以对模型进行欠采样，并使用调制波形代替 PWM 信号。

图中显示了该模块的等效电路和工作原理。

要将等效模型用作整流器，请将 PWM 信号的所有元素设置为零。该模型表现为二极管整流器。

### 保护

该模块为每个开关器件包含一个集成保护二极管。集成二极管通过为反向电流提供导通路径来保护半导体器件。当半导体器件突然切断负载的电压供应时，感性负载可能产生高反向电压尖峰。

要配置内部保护二极管模块，请使用 **保护二极管** 参数。下表显示了如何根据您的目标设置 **模型动态特性** 参数。

| 目标 | | 要选择的值 | 集成保护二极管 |
| --- | --- | --- | --- |
| 不包含保护。 | | `None` | 无 |
| 包含保护。 | 优先考虑仿真速度。 | `无动态特性的二极管` | Diode 模块 |
| 优先考虑模型保真度，精确指定反向模式电荷动态特性。 | | `具有电荷动态特性的二极管` | Diode 模块的动态模型 |

**注意**

如果将 **开关器件** 参数设置为 `Averaged Switch`，该模块会自动对无动态特性的保护二极管进行建模，并且 **模型动态特性** 参数不可见。

您还可以为每个开关器件包含缓冲电路。缓冲电路包含串联连接的电阻和电容。它们保护开关器件免受感性负载在器件切断负载的电压供应时产生的高电压的影响。缓冲电路还可以防止开关器件开通时出现过大的电流变化率。

要为每个开关器件包含并配置缓冲电路，请使用 **缓冲器** 参数。

### 热效应建模

*自 R2024b 起*

您可以暴露热端口，以对产生的热量和设备温度的影响进行建模。要暴露热端口：

- 在 **Main** 设置中，将 **Fidelity level** 参数设置为 `Detailed model - switching devices`。
- 在 **Switching Devices** 设置中，将 **Switching device** 参数设置为以下选项之一：

  - `GTO`
  - `IGBT`
  - `MOSFET`
  - `Thyristor`
- 在 **Switching Devices** 设置中，选中 **Model thermal effects** 参数。

有关使用热端口和 **Thermal Port** 参数的详细信息，请参阅 Simulating Thermal Effects in Semiconductors。

当您暴露热端口时，Four-Quadrant Chopper 模块会对开关器件的导通损耗以及开通和关断损耗进行建模。该模块使用与以下模块相同的方法来计算这些损耗，这些模块的 **On-state behavior and switching losses** 参数设置为 `Specify constant values`：

- GTO
- IGBT (Ideal, Switching)
- MOSFET (Ideal, Switching)
- Thyristor (Piecewise Linear)

有关 Four-Quadrant Chopper 模块如何计算这些损耗的详细信息，请参阅与您为 **Switching device** 参数所选选项相匹配的模块文档。

如果您启用热端口并将 **Integral protection diode** 参数设置为 `Diode with no dynamics`，则该模块还会对保护二极管的反向恢复损耗进行建模。该模块使用与 Diode 模块相同的方法来计算这些损耗，该模块的 **Fidelity level** 参数设置为 `Ideal switching`，且 **Diode model** 参数设置为 `Piecewise linear`。

在理想开关情况下，该模块不使用基于物理的电荷模型。该模块将电荷在反向恢复期间产生的损耗表示为瞬时损耗。

该模块通过将结温升高一个等于反向恢复损耗除以结处总热质量的值来施加反向恢复损耗。

如果您将 **Reverse recovery loss model** 参数设置为 `Tabulated loss`，则 **Reverse recovery loss table, Erec(Tj, If)** 参数的值指定了耗散能量，它是结温和开关事件前正向电流的函数。断态电压相对于 **Turn-off voltage when measuring recovery loss, Vrec** 参数值对损耗进行线性缩放。该表格使用电流和电压的延迟值。要使用查找表中接近瞬时值的值，请将 **Filter time constant for voltage and current values** 参数设置为低于最快开关周期的值。

如果您将 **Reverse recovery loss model** 参数设置为 `Fixed loss`，则 **Reverse recovery loss** 参数的值指定了每次关断事件期间耗散的能量。如果您选中 **Scale reverse recovery loss with current and voltage** 参数，则该模块会按通态电流和断态电压对该损耗值进行线性缩放。要使用接近瞬时值的缩放值，请将 **Filter time constant for voltage and current values** 设置为低于最快开关周期的值。

### 门极控制

要将 Simulink® 门极控制电压信号连接到内部开关器件的门极端口：

1. 使用 Simulink-PS Converter 模块转换每个电压信号。
2. 使用 Four-Pulse Gate Multiplexer 模块将转换后的门极信号多路复用为单个向量。
3. 将该向量信号连接到 **G** 端口。

### 用于 FPGA 部署的平均开关中的分段常数近似

如果您将 **Switching device** 参数设置为 `Averaged switch`，并且您的模型使用分区求解器，则该模块会产生非线性分区，因为平均模式方程包含模式 *Gsat*，它们是输入 **G** 的函数。为了使这些方程与硬件描述语言 (HDL) 代码生成兼容，从而适用于 FPGA 部署，请将 **Integer for piecewise constant approximation of gate input (0 for disabled)** 参数设置为大于 `0` 的值。该模块随后会将 *Gsat* 模式视为具有固定范围的分段常数整数。这将先前非线性的分区转变为线性时变分区。

范围 `[0,K]` 内的整数值（其中 *K* 是 **Integer for piecewise constant approximation of gate input (0 for disabled)** 的值）现在与范围 `[0,1]` 内的每个实值模式相关联。该模块通过将原始模式除以 K 将其归一化回范围 `[0,1]` 来计算分段常数模式：

uI=(floor(u⋅K))u^=uIK
