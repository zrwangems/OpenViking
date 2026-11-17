---
type: simulink-block
title: 'Bidirectional DC-DC Converter'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters / Converters'
documentation_page: 'bidirectionaldcdcconverter'
documentation_source_path: 'ref/bidirectionaldcdcconverter.html'
language: zh-CN
chinese_source: worker-translation
---

# Bidirectional DC-DC Converter

## 端口

### 守恒端口

### **G** — 开关器件栅极控制 electrical | vector

与开关器件栅极端子关联的电气守恒端口。

**数据类型：** `double`

### **1+** — 正直流电压 1 electrical | scalar

与第一个直流电压正极端子关联的电气守恒端口。

**数据类型：** `double`

### **1-** — 负直流电压 1 electrical | scalar

与第一个直流电压负极端子关联的电气守恒端口。

**数据类型：** `double`

### **2+** — 正直流电压 2 electrical | scalar

与第二个直流电压正极端子关联的电气守恒端口。

**数据类型：** `double`

### **2-** — 负直流电压 2 electrical | scalar

与第二个直流电压负极端子关联的电气守恒端口。

**数据类型：** `double`

## 参数

### **Modeling option** — 变换器模型 `Nonisolated converter`（默认）| `Isolated converter` | `Dual Active Bridge converter`

选择建模为非隔离变换器（含两个开关器件）、隔离变换器（含六个开关器件），还是双有源桥变换器（含八个开关器件）。

### 主要

### **Fidelity level** — 保真度级别 `Detailed model - switching devices`（默认）| `Equivalent model - PWM-controlled`

*自 R2024a 起*

模型的保真度级别。

若优先考虑仿真精度，或需要获取各个开关器件的结果，请将此参数设置为 `Detailed model - switching devices`。

若优先考虑仿真速度，请将此参数设置为 `Equivalent model - PWM-controlled`。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Nonisolated converter` 或 `Dual Active Bridge converter`。

### 开关器件

以下表格展示了当使用详细模型选项时，**Switching Devices** 参数的可见性如何取决于所选的变换器模型和开关器件。要了解如何阅读该表格，请参阅参数依赖关系。

**非隔离变换器开关器件参数依赖关系**

| 参数和选项 | | | | | |
| --- | --- | --- | --- | --- | --- |
| **Switching device** | | | | | |
| *`Ideal Semiconductor Switch`* | *`GTO`* | *`IGBT`* | *`MOSFET`* | *`Thyristor`* | *`Averaged Switch`* |
| On-state resistance | Forward voltage | Forward voltage | Drain-source on resistance | Forward voltage | On-state resistance |
| Off-state conductance | On-state resistance | On-state resistance | Off-state conductance | On-state resistance |
| Threshold voltage | Off-state conductance | Off-state conductance | Threshold voltage | Off-state conductance |
| 门极触发电压，Vgt | 阈值电压 | 门极触发电压，Vgt | 用于门极输入分段常数近似的整数（0 表示禁用） |
| Gate turn-off voltage, Vgt\_off | Gate turn-off voltage, Vgt\_off |
| Holding current | Holding current |

**注意**

要启用这些参数，请将 **Modeling option** 设置为 `Nonisolated converter`，并将 **Fidelity level** 设置为 `Detailed model - switching devices`。

**隔离变换器和双有源桥变换器开关器件参数依赖关系**

| 参数和选项 | | | | | |
| --- | --- | --- | --- | --- | --- |
| **Switching device HV** | | | | | |
| *`Ideal Semiconductor Switch`* | *`GTO`* | *`IGBT`* | *`MOSFET`* | *`Thyristor`* | *`Averaged Switch`* |
| On-state resistance HV | Forward voltage HV | Forward voltage HV | Drain-source on resistance HV | Forward voltage HV | On-state resistance HV |
| Off-state conductance HV | On-state resistance HV | On-state resistance HV | Off-state conductance HV | On-state resistance HV |
| Threshold voltage HV | Off-state conductance HV | Off-state conductance HV | Threshold voltage HV | Off-state conductance HV |
| 门极触发电压 HV，Vgt\_hv | 阈值电压 HV | 门极触发电压 HV，Vgt\_hv | 用于门极输入分段常数近似的整数（0 表示禁用） |
| Gate turn-off voltage HV, Vgt\_off\_hv | Gate turn-off voltage HV, Vgt\_off\_hv |
| Holding current HV | Holding current HV |
| **Switching device LV** | | | | | |
| *`Ideal Semiconductor Switch`* | *`GTO`* | *`IGBT`* | *`MOSFET`* | *`Thyristor`* | *`Averaged Switch`* |
| On-state resistance LV | Forward voltage LV | Forward voltage LV | Drain-source on resistance LV | Forward voltage LV | On-state resistance LV |
| Off-state conductance LV | On-state resistance LV | On-state resistance LV | Off-state conductance LV | On-state resistance LV |
| Threshold voltage LV | Off-state conductance LV | Off-state conductance LV | Threshold voltage LV | Off-state conductance LV |
| 门极触发电压 LV，Vgt | 阈值电压 LV | 门极触发电压 LV，Vgt | 用于门极输入分段常数近似的整数（0 表示禁用） |
| Gate turn-off voltage LV, Vgt\_off\_lv | Gate turn-off voltage LV, Vgt\_off\_lv |
| Holding current LV | Holding current LV |

**注意**

要启用这些参数，请选择以下选项之一：

- 将 **Modeling option** 设置为 `Isolated converter`。
- 将 **Modeling option** 设置为 `Dual Active Bridge converter`，并将 **Fidelity level** 设置为 `Detailed model - switching devices`。

### **Switching device** — 开关类型 `Ideal Semiconductor Switch`（默认）| `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

非隔离变换器模型的开关器件类型。

#### 依赖关系

请参阅非隔离变换器开关器件参数依赖关系表。

### **Forward voltage** — 电压 `0.8` `V`（默认）| scalar

对于不同的开关器件类型，**Forward voltage** 的含义为：

- GTO — 为使器件 I-V 特性的斜率为 1/*Ron* 所需的阳极和阴极块端口之间的最小电压，其中 *Ron* 为 **On-state resistance** 的值
- IGBT — 为使二极管 i-v 特性的斜率为 1/*Ron* 所需的集电极和发射极块端口之间的最小电压，其中 *Ron* 为 **On-state resistance** 的值
- Thyristor — 器件导通所需的最小电压

#### 依赖关系

请参阅非隔离变换器开关器件参数依赖关系表。

### **On-state resistance** — 电阻 `0.001` `Ohm`（默认）| scalar

对于不同的开关器件类型，**On-state resistance** 的含义为：

- GTO — 正向电压以上电压对电流的变化率
- Ideal semiconductor switch — 器件导通时的阳极-阴极电阻
- IGBT — 器件导通时的集电极-发射极电阻
- Thyristor — 器件导通时的阳极-阴极电阻
- Averaged switch — 器件导通时的阳极-阴极电阻

#### 依赖关系

请参阅非隔离变换器开关器件参数依赖关系表。

### **Drain-source on resistance** — 电阻 `0.001` `Ohm`（默认）| scalar

漏极和源极之间的电阻，该电阻还取决于栅极-源极电压。

#### 依赖关系

请参阅非隔离变换器开关器件参数依赖关系表。

### **Off-state conductance** — 电导 `1e-5` `1/Ohm`（默认）| scalar

器件关断时的电导。该值必须小于 1/*R*，其中 *R* 为 **On-state resistance** 的值。

对于不同的开关器件类型，**On-state resistance** 的含义为：

- GTO — 阳极-阴极电导
- Ideal semiconductor switch — 阳极-阴极电导
- IGBT — 集电极-发射极电导
- MOSFET — 漏极-源极电导
- Thyristor — 阳极-阴极电导

#### 依赖关系

请参阅非隔离变换器开关器件参数依赖关系表。

### **Threshold voltage** — 电压阈值 `6` `V`（默认）| scalar

栅极电压阈值。当栅极电压高于此值时，器件导通。对于不同的开关器件类型，所关注的器件电压为：

- Ideal semiconductor switch — 栅极-阴极电压
- IGBT — 栅极-发射极电压
- MOSFET — 栅极-源极电压

#### 依赖关系

请参阅非隔离变换器开关器件参数依赖关系表。

### **Gate trigger voltage, Vgt** — 电压阈值 `1` `V`（默认）| scalar

栅极-阴极电压阈值。当栅极-阴极电压高于此值时，器件导通。

#### 依赖关系

请参阅非隔离变换器开关器件参数依赖关系表。

### **Gate turn-off voltage, Vgt\_off** — 电压阈值 `-1` `V`（默认）| scalar

栅极-阴极电压阈值。当栅极-阴极电压低于此值时，器件关断。

#### 依赖关系

请参阅非隔离变换器开关器件参数依赖关系表。

### **Holding current** — 电流阈值 `1` `A`（默认）| scalar

栅极电流阈值。当电流高于此值时，即使栅极-阴极电压降至栅极触发电压以下，器件仍保持导通。

#### 依赖关系

请参阅非隔离变换器开关器件参数依赖关系表。

### **Switching device HV** — 开关 `Ideal Semiconductor Switch`（默认）| `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

隔离变换器模型高压侧的开关器件类型。

#### 依赖关系

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **Forward voltage HV** — 电压 `0.8` `Ohm`（默认）| scalar

对于不同的开关器件类型，**Forward voltage HV** 的含义为：

- GTO — 为使器件 I-V 特性的斜率为 1/*Ron* 所需的阳极和阴极块端口之间的最小电压，其中 *Ron* 为 **On-state resistance** 的值
- IGBT — 为使二极管 i-v 特性的斜率为 1/*Ron* 所需的集电极和发射极块端口之间的最小电压，其中 *Ron* 为 **On-state resistance** 的值
- Thyristor — 器件导通所需的最小电压

#### 依赖关系

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **Drain-source on resistance HV** — 电阻 `0.001` `Ohm`（默认）| scalar

漏极和源极之间的电阻，该电阻还取决于栅极-源极电压。

#### 依赖关系

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **On-state resistance HV** — 电阻 `0.001` `Ohm`（默认）| scalar

对于不同的开关器件类型，**On-state resistance HV** 的含义为：

- GTO — 正向电压以上电压对电流的变化率
- Ideal semiconductor switch — 器件导通时的阳极-阴极电阻
- IGBT — 器件导通时的集电极-发射极电阻
- Thyristor — 器件导通时的阳极-阴极电阻
- Averaged switch — 器件导通时的阳极-阴极电阻

#### 依赖关系

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **Off-state conductance HV** — 电导 `1e-5` `1/Ohm`（默认）| scalar

器件关断时的电导。该值必须小于 1/*R*，其中 *R* 为 **On-state resistance HV** 的值。

对于不同的开关器件类型，**On-state resistance HV** 的含义为：

- GTO — 阳极-阴极电导
- Ideal semiconductor switch — 阳极-阴极电导
- IGBT — 集电极-发射极电导
- MOSFET — 漏极-源极电导
- Thyristor — 阳极-阴极电导

#### 依赖关系

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **Threshold voltage HV** — 电压阈值 `6` `V`（默认）| scalar

栅极电压阈值。当栅极电压高于此值时，器件导通。对于不同的开关器件类型，所关注的器件电压为：

- Ideal semiconductor switch — 栅极-阴极电压
- IGBT — 栅极-发射极电压
- MOSFET — 栅极-源极电压

#### 依赖关系

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **Gate trigger voltage HV, Vgt\_hv** — 电压阈值 `1` `V`（默认）| scalar

栅极-阴极电压阈值。当栅极-阴极电压高于此值时，器件导通。

#### 依赖关系

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **Gate turn-off voltage HV, Vgt\_off\_hv** — 电压阈值 `-1` `V`（默认）| scalar

栅极-阴极电压阈值。当栅极-阴极电压低于此值时，器件关断。

#### 依赖关系

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **Holding current HV** — 电流阈值 `1` `A`（默认）| scalar

栅极电流阈值。当电流高于此值时，即使栅极-阴极电压降至栅极触发电压以下，器件仍保持导通。

#### 依赖关系

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **Switching device LV** — 开关 `Ideal Semiconductor Switch`（默认）| `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

隔离变换器模型低压侧的开关器件类型。

#### 依赖关系

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **Forward voltage LV** — 电压 `0.8` `Ohm`（默认）| scalar

对于不同的开关器件类型，**Forward voltage LV** 的含义为：

- GTO — 为使器件 I-V 特性的斜率为 1/*Ron* 所需的阳极和阴极块端口之间的最小电压，其中 *Ron* 为 **On-state resistance** 的值
- IGBT — 为使二极管 i-v 特性的斜率为 1/*Ron* 所需的集电极和发射极块端口之间的最小电压，其中 *Ron* 为 **On-state resistance** 的值
- Thyristor — 器件导通所需的最小电压

#### 依赖关系

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **Drain-source on resistance LV** — 电阻 `0.001` `Ohm`（默认）| scalar

漏极和源极之间的电阻，该电阻还取决于栅极-源极电压。

#### 依赖关系

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **On-state resistance LV** — 电阻 `0.001` `Ohm`（默认）| scalar

对于不同的开关器件类型，**On-state resistance LV** 的含义为：

- GTO — 正向电压以上电压对电流的变化率
- Ideal semiconductor switch — 器件导通时的阳极-阴极电阻
- IGBT — 器件导通时的集电极-发射极电阻
- Thyristor — 器件导通时的阳极-阴极电阻
- Averaged switch — 器件导通时的阳极-阴极电阻

#### 依赖关系

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **Off-state conductance LV** — 电导 `1e-5` `1/Ohm`（默认）| scalar

器件关断时的电导。该值必须小于 1/*R*，其中 *R* 为 **On-state resistance LV** 的值。

对于不同的开关器件类型，**On-state resistance LV** 的含义为：

- GTO — 阳极-阴极电导
- Ideal semiconductor switch — 阳极-阴极电导
- IGBT — 集电极-发射极电导
- MOSFET — 漏极-源极电导
- Thyristor — 阳极-阴极电导

#### 依赖关系

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **Threshold voltage LV** — 电压阈值 `6` `V`（默认）| 标量

栅极电压阈值。当栅极电压高于此值时，器件导通。对于不同的开关器件类型，所关注的器件电压为：

- Ideal semiconductor switch — 栅极-阴极电压
- IGBT — 栅极-发射极电压
- MOSFET — 栅极-源极电压

#### 依赖关系

请参阅 Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies 表。

### **Gate trigger voltage LV, Vgt\_lv** — 电压阈值 `1` `V`（默认）| 标量

栅极-阴极电压阈值。当栅极-阴极电压高于此值时，器件导通。

#### 依赖关系

请参阅 Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies 表。

### **Gate turn-off voltage LV, Vgt\_off\_lv** — 电压阈值 `-1` `V`（默认）| 标量

栅极-阴极电压阈值。当栅极-阴极电压低于此值时，器件关断。

#### 依赖关系

请参阅 Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies 表。

### **Holding current LV** — 电流阈值 `1` `A`（默认）| 标量

栅极电流阈值。当电流高于此值时，即使栅极-阴极电压降至栅极触发电压以下，器件仍保持导通。

#### 依赖关系

请参阅 Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies 表。

### **Integer for piecewise constant approximation of gate input (0 for disabled)** — 用于 FPGA 部署的整数模式 `0`（默认）| 非负标量

用于对栅极输入进行分段常数近似以部署到 FPGA 的整数。

#### 依赖关系

要启用此参数，请将 **Switching device** 设置为 `Averaged Switch`。

### Protection Diode

要启用这些参数，请选择以下选项之一：

- 将 **Modeling Option** 设置为 `Nonisolated
  converter` 或 `Dual Active Bridge
  converter`，并将 **Fidelity level** 设置为
  `Detailed model - switching
  devices`。
- 将 **Modeling Option** 设置为 `Isolated
  converter`。

**Protection Diode** 参数的可见性取决于您如何配置 **Model dynamics** 和 **Reverse recovery time parameterization** 参数。要了解如何阅读此表，请参阅 Parameter Dependencies。

**Protection Diode Parameter Dependencies**

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

**注意**

如果将 **Switching device** 参数设置为 `Averaged Switch`，则该模块对保护二极管进行无动态建模，且 **Model dynamics** 参数不可见。

### **Model dynamics** — 二极管模型 `Diode with no dynamics`（默认）| `Diode with charge dynamics`

Bidirectional DC-DC Converter 模块用于每个开关器件的保护二极管的模型。请选择以下选项之一：

- `None` — Bidirectional DC-DC Converter 不对保护二极管建模。
- `Diode with no dynamics` — Bidirectional DC-DC Converter 模块使用与 Diode 模块（无动态）相同的方程对保护二极管建模。选择此选项可优先考虑仿真速度。
- `Diode with charge dynamics` — Bidirectional DC-DC Converter 模块使用与 Diode 模块（有电荷动态）相同的方程对保护二极管建模。选择此选项可优先考虑详细的仿真结果。

#### 依赖关系

请参阅 Protection Diode Parameter Dependencies 表。

### **Forward voltage** — 电压 `0.8` `V`（默认）| 标量

使二极管 I-V 特性梯度为 1/*Ron* 所需的跨模块正负端口的最小电压，其中 *Ron* 是 **On resistance** 参数的值。

### **On resistance** — 导通电阻 `0.001` `Ohm`（默认）| 标量

高于 **Forward voltage** 参数值时的电压随电流的变化率。

### **Off conductance** — 电导 `1e-5` `1/Ohm`（默认）| 标量

反向偏置二极管的电导。

### **Junction capacitance** — 结电容 `50` `nF`（默认）| 标量

二极管结电容。

#### 依赖关系

请参阅 Protection Diode Parameter Dependencies 表。

### **Peak reverse current, iRM** — 峰值反向电流 `-235` `A`（默认）| 负标量

由外部测试电路测得的峰值反向电流。

#### 依赖关系

请参阅 Protection Diode Parameter Dependencies 表。

### **Initial forward current when measuring iRM** — 测量 iRM 时的初始正向电流 `300` `A`（默认）| 正标量

测量峰值反向电流时的初始正向电流。

#### 依赖关系

请参阅 Protection Diode Parameter Dependencies 表。

### **Rate of change of current when measuring iRM** — 电流变化率 `-50` `A/us`（默认）| 标量

测量峰值反向电流时的电流变化率。

#### 依赖关系

请参阅 Protection Diode Parameter Dependencies 表。

### **Reverse recovery time parameterization** — 恢复时间模型 `Specify stretch factor`（默认）| `Specify reverse recovery time directly` | `Specify reverse recovery charge`

用于参数化恢复时间的模型。当您选择 `Specify stretch factor` 或 `Specify reverse recovery charge` 时，可以指定一个值，模块使用该值来推导反向恢复时间。有关这些选项的详细信息，请参阅 How the Block Calculates TM and Tau。

#### 依赖关系

请参阅 Protection Diode Parameter Dependencies 表。

### **Reverse recovery time stretch factor** — 反向恢复时间拉伸因子 `3`（默认）| 大于 `1` 的标量

模块用于计算反向恢复时间的拉伸因子。指定拉伸因子比指定反向恢复电荷更容易参数化反向恢复时间。拉伸因子的值越大，反向恢复电流消散所需的时间越长。

#### 依赖关系

请参阅 Protection Diode Parameter Dependencies 表。

### **Reverse recovery time, trr** — 反向恢复时间 `15` `us`（默认）| 标量

电流初始降至零（二极管关断时）与电流降至峰值反向电流的 10% 以下之间的时间间隔。

**Reverse recovery time, trr** 参数的值必须大于 **Peak reverse current, iRM** 参数的值除以 **Rate of change of current when measuring iRM** 参数的值。

#### 依赖关系

请参阅 Protection Diode Parameter Dependencies 表。

### **Reverse recovery charge, Qrr** — 反向恢复电荷 `1500` `s*uA`（默认）| 标量

模块用于计算反向恢复时间的反向恢复电荷。如果您的二极管器件数据手册指定了反向恢复电荷的值而非反向恢复时间的值，请使用此参数。

反向恢复电荷是二极管关断时继续消散的总电荷。该值必须小于 −i2RM2a，

其中：

- *iRM* 是为 **Peak reverse current, iRM** 指定的值。
- *a* 是为 **Rate of change of current when measuring iRM** 指定的值。

#### 依赖关系

请参阅 Protection Diode Parameter Dependencies 表。

### Transformer

### **Self inductance of transformer primary winding, L1** — 变压器初级绕组自感 `0.03` `H`（默认）| 正标量

变压器初级绕组的自感。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Isolated converter` 或 `Dual Active Bridge converter`。

### **Self inductance of transformer secondary winding, L2** — 变压器次级绕组自感 `0.03` `H`（默认）| 正标量

变压器次级绕组的自感。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Isolated converter` 或 `Dual Active Bridge converter`。

### **Transformer coefficient of coupling** — 耦合系数 `0.9`（默认）| 大于零且小于 1 的正标量

定义变压器的互感。

#### 依赖关系

要启用此参数，请将 **Modeling option** 设置为 `Isolated converter` 或 `Dual Active Bridge converter`。

### LC Parameters

### **Inductance, L** — 电感 `1e-6` `H`（默认）| 正标量

变换器电感。如果将 **Modeling option** 参数设置为 `Isolated converter`，则两个电感相同。

### **Inductor series resistance** — 电感串联电阻 `0` `Ohm`（默认）| 零或正标量

电感的串联电阻。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将 **Modeling Option** 设置为 `Isolated
  converter`。
- 将 **Modeling Option** 设置为 `Nonisolated converter` 或 `Dual Active Bridge
  converter`，并将 **Fidelity
  level** 设置为 `Detailed model -
  switching devices`。

### **Capacitance, C1** — 电容 `1e-7` `F`（默认）| 正标量

第一个直流端子的电容。

### **Capacitance, C2** — 电容 `1e-7` `F`（默认）| 正标量

第二个直流端子的电容。

### **C1 effective series resistance** — 电阻 `1e-6` `Ohm`（默认）| 零或正标量

电容 *C1* 的串联电阻。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将 **Modeling Option** 设置为 `Isolated
  converter`。
- 将 **Modeling Option** 设置为 `Nonisolated converter` 或 `Dual Active Bridge
  converter`，并将 **Fidelity
  level** 设置为 `Detailed model -
  switching devices`。

### **C2 effective series resistance** — 电阻 `1e-6` `Ohm`（默认）| 零或正标量

电容 *C2* 的串联电阻。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将 **Modeling Option** 设置为 `Isolated
  converter`。
- 将 **Modeling Option** 设置为 `Nonisolated converter` 或 `Dual Active Bridge
  converter`，并将 **Fidelity
  level** 设置为 `Detailed model -
  switching devices`。

### Snubbers

要启用这些参数，请将 **Switching device** 设置为以下选项之一：

- `Ideal Semiconductor Switch`
- `GTO`
- `IGBT`
- `MOSFET`
- `Thyristor`

此表总结了 **Snubbers** 参数依赖关系。要了解如何阅读此表，请参阅 Parameter Dependencies。

**Snubbers Parameter Dependencies**

| Snubbers Parameter Dependencies | | | | | |
| --- | --- | --- | --- | --- | --- |
| **Modeling option** | | | | | |
| *`Nonisolated Converter`* | | *`Isolated Converter`* | | *`Dual Active Bridge converter`* | |
| **Snubber** | | **Snubber HV** | | **Snubber HV** | |
| *`None`* | *`RC Snubber`* | **`None`** | *`RC Snubber`* | **`None`** | *`RC Snubber`* |
| Snubber resistance | Snubber resistance HV | Snubber resistance HV |
| Snubber capacitance | Snubber capacitance HV | Snubber capacitance HV |
| **Snubber LV** | | **Snubber LV** | |
| *`None`* | *`RC Snubber`* | *`None`* | *`RC Snubber`* |
| Snubber resistance LV | Snubber resistance LV |
| Snubber capacitance LV | Snubber capacitance LV |

### **Snubber** — 缓冲器模型 `None`（默认）| `RC snubber`

每个开关器件的缓冲器。

#### 依赖关系

请参阅 Snubbers Parameter Dependencies 表。

### **Snubber resistance** — 电阻 `0.1` `Ohm`（默认）| 标量

缓冲器的电阻。

#### 依赖关系

请参阅 Snubbers Parameter Dependencies 表。

### **Snubber capacitance** — 电容 `1e-7` `F`（默认）| 标量

缓冲器的电容。

#### 依赖关系

请参阅 Snubbers Parameter Dependencies 表。

### **Snubber HV** — 缓冲器模型 `None`（默认）| `RC snubber`

每个开关器件的高压缓冲器。

#### 依赖关系

请参阅 Snubbers Parameter Dependencies 表。

### **Snubber resistance HV** — 电阻 `0.1` `Ohm`（默认）| 标量

高压缓冲器的电阻。

#### 依赖关系

请参阅 Snubbers Parameter Dependencies 表。

### **Snubber capacitance HV** — 电容 `1e-7` `F`（默认）| 标量

高压缓冲器的电容。

#### 依赖关系

请参阅 Snubbers Parameter Dependencies 表。

### **Snubber LV** — 缓冲器模型 `None`（默认）| `RC snubber`

每个开关器件的低压缓冲器。

#### 依赖关系

请参阅 Snubbers Parameter Dependencies 表。

### **Snubber resistance LV** — 电阻 `0.1` `Ohm`（默认）| 标量

低压缓冲器的电阻。

#### 依赖关系

请参阅 Snubbers Parameter Dependencies 表。

### **Snubber capacitance LV** — 电容 `1e-7` `F`（默认）| 标量

低压缓冲器的电容。

#### 依赖关系

请参阅 Snubbers Parameter Dependencies 表。

## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2024a：使用等效模型提高仿真速度

如果您对非隔离变换器或双有源桥变换器建模，现在可以从两个保真度级别中选择变换器模型。等效模型选项不对单个开关器件建模，但返回等效结果。如果您需要开关器件动态的详细结果，请使用详细模型选项。否则，请使用等效模型以获得更快的仿真速度。要进行实时仿真，请使用等效模型。要验证结果，请使用详细模型配合变步长求解器。

要使用详细模型，请将 **Fidelity level** 参数设置为 `Detailed model - switching devices`。要使用等效模型，请将 **Fidelity level** 参数设置为 `Equivalent model - PWM-controlled`。

在 R2024a 之前，只能使用详细模型。

## 描述

由控制器驱动的双向 DC-DC 升压和降压电压调节器

Bidirectional DC-DC Converter 模块表示一个转换器，该转换器在附加控制器和门极信号发生器的驱动下，将 DC 电压从转换器的任一侧升压或降压到另一侧。双向 DC-DC 转换器可用于在能量存储和使用之间切换，例如在电动汽车中。

Bidirectional DC-DC Converter 模块允许您对具有两个开关器件的非隔离转换器、具有六个开关器件的隔离转换器或具有八个开关器件的双有源桥转换器进行建模。

如果您对非隔离转换器或双有源桥转换器进行建模，则可以从转换器模型的两种保真度级别中进行选择。等效模型选项不对单个开关器件进行建模，但会返回等效结果。如果您需要开关器件动态的详细结果，请使用详细模型选项。否则，请使用等效模型以加快仿真速度。要进行实时仿真，请使用等效模型。要验证结果，请使用详细模型和变步长求解器。要使用详细模型，请将 **Fidelity level** 参数设置为 `Detailed model - switching devices`。要使用等效模型，请将 **Fidelity level** 参数设置为 `Equivalent model - PWM-controlled`。

如果您对隔离转换器进行建模，则只能使用详细模型。**Fidelity level** 参数不可见。

如果您选择详细模型，则每个组件都是相同的开关器件，您可以通过设置 **Switching device** 参数来指定。您可以指定的开关器件是 **Simscape** > **Electrical** > **Semiconductors & Converters** 库中模块的实现：

- GTO — 门极关断晶闸管。有关该器件的 I-V 特性信息，请参见 GTO。
- Ideal semiconductor switch — 有关该器件的 I-V 特性信息，请参见 Ideal Semiconductor Switch。
- IGBT — 绝缘栅双极晶体管。有关该器件的 I-V 特性信息，请参见 IGBT (Ideal, Switching)。
- MOSFET — N 沟道金属氧化物半导体场效应晶体管。有关该器件的 I-V 特性信息，请参见 MOSFET (Ideal, Switching)。
- Thyristor — 有关该器件的 I-V 特性信息，请参见 Thyristor (Piecewise Linear)。
- Averaged Switch — 带反并联二极管的半导体开关。控制信号端口 **G** 接受区间 [0,1] 内的值。当 **G** 等于 `0` 或 `1` 时，平均开关分别完全打开或完全闭合。该开关的行为类似于带反并联二极管的 Ideal Semiconductor Switch 模块。当 **G** 介于 0 和 1 之间时，平均开关部分打开。您可以在指定周期内对脉宽调制 (PWM) 信号进行平均。然后，您可以对模型进行欠采样，并使用调制波形代替 PWM 信号。

**注意**

如果您将 **Switching device** 参数设置为 `Averaged Switch`，则该模块会自动对无动态的保护二极管进行建模，并且 **Model dynamics** 参数不可见。

### 模型

您可以对三种不同类型的双向 DC-DC 转换器进行建模。要访问不同的选项，请双击该模块并将 **Modeling option** 参数设置为以下之一：

- `Nonisolated converter` — 不带电气隔离栅的双向 DC-DC 转换器。该转换器包含一个电感、两个电容和两个相同器件类型的开关。
- `Isolated converter` — 带电气隔离栅的双向 DC-DC 转换器。该转换器包含四个附加开关，构成一个全桥。全桥位于转换器的输入或高压 (HV) 侧。另外两个开关位于转换器的输出或低压 (LV) 侧。您可以为 HV 和 LV 开关器件选择不同的半导体类型。例如，您可以为 HV 开关器件使用 GTO，为 LV 开关器件使用 IGBT。为了在输入和输出电压之间提供隔离，该模型使用高频变压器。
- `Dual Active Bridge converter` — 该双向 DC-DC 转换器包含两个全桥。左侧桥是转换器的输入或高压 (HV) 侧。右侧桥是转换器的输出或低压 (LV) 侧。您可以为 HV 和 LV 开关器件选择不同的半导体类型。例如，您可以为 HV 开关器件使用 GTO，为 LV 开关器件使用 IGBT。为了在输入和输出电压之间提供隔离，该模型使用高频变压器。要使用等效模型并将变压器的任一侧用作整流器，请将该侧对应的 PWM 信号元素设置为零。变压器的该侧表现为二极管整流器。

### 保护

该模块为每个开关器件包含一个集成保护二极管。集成二极管通过为反向电流提供导通路径来保护半导体器件。当半导体器件突然切断负载的电压供应时，感性负载可能会产生高反向电压尖峰。

要配置内部保护二极管模块，请使用 **Protection Diode** 参数。下表显示了如何根据您的目标设置 **Model dynamics** 参数。

| 目标 | 要选择的值 | 集成保护二极管 |
| --- | --- | --- |
| 优先考虑仿真速度。 | `Diode with no dynamics` | Diode 模块 |
| 通过精确指定反向模式电荷动态来优先考虑模型保真度。 | `Diode with charge dynamics` | Diode 模块的动态模型 |

您还可以为每个开关器件包含一个缓冲电路。缓冲电路包含一个串联的电阻和电容。它们保护开关器件免受感性负载在器件切断负载的电压供应时产生的高电压影响。缓冲电路还可以防止开关器件导通时出现过大的电流变化率。

要为每个开关器件包含并配置缓冲电路，请使用 **Snubbers** 参数。

### 门极控制

要将 Simulink® 门极控制电压信号连接到开关器件的门极端口：

1. 使用 Simulink-PS Converter 模块转换每个电压信号。
2. 将转换后的门极信号多路复用为单个向量。

   - 对于非隔离转换器模型，使用 Two-Pulse Gate Multiplexer 模块。
   - 对于隔离转换器模型，使用 Six-Pulse Gate Multiplexer 模块。
   - 对于双有源桥转换器模型，使用 Eight-Pulse Gate Multiplexer 模块。
3. 将向量信号连接到 **G** 端口。

### 用于 FPGA 部署的平均开关中的分段常数近似

如果您将 **Switching device** 参数设置为 `Averaged switch`，并且您的模型使用分区求解器，则该模块会产生非线性分区，因为平均模式方程包含模式 *Gsat*，它们是输入 **G** 的函数。为了使这些方程与硬件描述语言 (HDL) 代码生成兼容，从而支持 FPGA 部署，请将 **Integer for piecewise constant approximation of gate input (0 for disabled)** 参数设置为大于 `0` 的值。然后，该模块将 *Gsat* 模式视为具有固定范围的分段常数整数。这将先前非线性的分区转换为线性时变分区。

范围 `[0,K]` 内的一个整数值（其中 *K* 是 **Integer for piecewise constant approximation of gate input (0 for disabled)** 的值）现在与范围 `[0,1]` 内的每个实值模式相关联。该模块通过将原始模式除以 K 将其归一化回范围 `[0,1]` 来计算分段常数模式：

uI=(floor(u⋅K))u^=uIK

### 假设

源阻抗或非零等效串联电阻 (ESR) 连接到 Bidirectional DC-DC Converter 模块的左侧。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参见 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。您可以使用不同的来源指定标称值，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参见 System Scaling by Nominal Values。
