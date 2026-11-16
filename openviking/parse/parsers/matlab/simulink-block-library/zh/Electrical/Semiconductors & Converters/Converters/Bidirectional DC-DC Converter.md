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

### 守恒

### **G** — 开关器件门极控制 electrical | vector

与开关器件门极端子相关的电气守恒端口。

**数据类型：** `double`

### **1+** — 正直流电压 1 electrical | scalar

与第一个直流电压的正端子相关的电气守恒端口。

**数据类型：** `double`

### **1-** — 负直流电压 1 electrical | scalar

与第一个直流电压的负端子相关的电气守恒端口。

**数据类型：** `double`

### **2+** — 正直流电压 2 electrical | scalar

与第二个直流电压的正端子相关的电气守恒端口。

**数据类型：** `double`

### **2-** — 负直流电压 2 electrical | scalar

与第二个直流电压的负端子相关的电气守恒端口。

**数据类型：** `double`

## 参数

### **建模选项** — 变换器模型 `Nonisolated converter`（默认）| `Isolated converter` | `Dual Active Bridge converter`

是要对具有两个开关器件的非隔离变换器、具有六个开关器件的隔离变换器，还是具有八个开关器件的双有源桥变换器进行建模。

### 主要

### **保真度级别** — 保真度级别 `Detailed model - switching devices`（默认）| `Equivalent model - PWM-controlled`

*自 R2024a 起*

模型的保真度级别。

要优先考虑仿真精度，或要获取各个开关器件的结果，请将此参数设置为 `Detailed model - switching devices`。

要优先考虑仿真速度，请将此参数设置为 `Equivalent model - PWM-controlled`。

#### 依赖项

要启用此参数，请将 **建模选项** 设置为 `Nonisolated converter` 或 `Dual Active Bridge converter`。

### 开关器件

这些表格显示了当使用详细模型选项时，**开关器件** 参数的可见性如何取决于您选择的变换器模型和开关器件。要了解如何阅读该表格，请参阅参数依赖关系。

**非隔离变换器开关器件参数依赖关系**

| 参数和选项 | | | | | |
| --- | --- | --- | --- | --- | --- |
| **开关器件** | | | | | |
| *`Ideal Semiconductor Switch`* | *`GTO`* | *`IGBT`* | *`MOSFET`* | *`Thyristor`* | *`Averaged Switch`* |
| 导通状态电阻 | 正向电压 | 正向电压 | 漏源导通电阻 | 正向电压 | 导通状态电阻 |
| 关断状态电导 | 导通状态电阻 | 导通状态电阻 | 关断状态电导 | 导通状态电阻 |
| 阈值电压 | 关断状态电导 | 关断状态电导 | 阈值电压 | 关断状态电导 |
| 门极触发电压, Vgt | 阈值电压 | 门极触发电压, Vgt | 用于门极输入分段常数近似的整数（0 表示禁用） |
| 门极关断电压, Vgt\_off | 门极关断电压, Vgt\_off |
| 保持电流 | 保持电流 |

**注意**

要启用这些参数，请将 **建模选项** 设置为 `Nonisolated converter`，并将 **保真度级别** 设置为 `Detailed model - switching devices`。

**隔离变换器和双有源桥变换器开关器件参数依赖关系**

| 参数和选项 | | | | | |
| --- | --- | --- | --- | --- | --- |
| **开关器件 HV** | | | | | |
| *`Ideal Semiconductor Switch`* | *`GTO`* | *`IGBT`* | *`MOSFET`* | *`Thyristor`* | *`Averaged Switch`* |
| 导通状态电阻 HV | 正向电压 HV | 正向电压 HV | 漏源导通电阻 HV | 正向电压 HV | 导通状态电阻 HV |
| 关断状态电导 HV | 导通状态电阻 HV | 导通状态电阻 HV | 关断状态电导 HV | 导通状态电阻 HV |
| 阈值电压 HV | 关断状态电导 HV | 关断状态电导 HV | 阈值电压 HV | 关断状态电导 HV |
| 门极触发电压 HV, Vgt\_hv | 阈值电压 HV | 门极触发电压 HV, Vgt\_hv | 用于门极输入分段常数近似的整数（0 表示禁用） |
| 门极关断电压 HV, Vgt\_off\_hv | 门极关断电压 HV, Vgt\_off\_hv |
| 保持电流 HV | 保持电流 HV |
| **开关器件 LV** | | | | | |
| *`Ideal Semiconductor Switch`* | *`GTO`* | *`IGBT`* | *`MOSFET`* | *`Thyristor`* | *`Averaged Switch`* |
| 导通状态电阻 LV | 正向电压 LV | 正向电压 LV | 漏源导通电阻 LV | 正向电压 LV | 导通状态电阻 LV |
| 关断状态电导 LV | 导通状态电阻 LV | 导通状态电阻 LV | 关断状态电导 LV | 导通状态电阻 LV |
| 阈值电压 LV | 关断状态电导 LV | 关断状态电导 LV | 阈值电压 LV | 关断状态电导 LV |
| 门极触发电压 LV, Vgt | 阈值电压 LV | 门极触发电压 LV, Vgt | 用于门极输入分段常数近似的整数（0 表示禁用） |
| 门极关断电压 LV, Vgt\_off\_lv | 门极关断电压 LV, Vgt\_off\_lv |
| 保持电流 LV | 保持电流 LV |

**注意**

要启用这些参数，请选择以下选项之一：

- 将 **建模选项** 设置为 `Isolated converter`。
- 将 **建模选项** 设置为 `Dual Active Bridge converter`，并将 **保真度级别** 设置为 `Detailed model - switching devices`。

### **开关器件** — 开关类型 `Ideal Semiconductor Switch`（默认）| `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

非隔离变换器模型的开关器件类型。

#### 依赖项

请参阅非隔离变换器开关器件参数依赖关系表。

### **正向电压** — 电压 `0.8` `V`（默认）| scalar

对于不同的开关器件类型，**正向电压** 取为：

- GTO — 使器件 I-V 特性的梯度为 1/*Ron* 所需的阳极和阴极块端口之间的最小电压，其中 *Ron* 是 **导通状态电阻** 的值
- IGBT — 使二极管 i-v 特性的梯度为 1/*Ron* 所需的集电极和发射极块端口之间的最小电压，其中 *Ron* 是 **导通状态电阻** 的值
- Thyristor — 器件导通所需的最小电压

#### 依赖项

请参阅非隔离变换器开关器件参数依赖关系表。

### **导通状态电阻** — 电阻 `0.001` `Ohm`（默认）| scalar

对于不同的开关器件类型，**导通状态电阻** 取为：

- GTO — 高于正向电压时电压对电流的变化率
- Ideal semiconductor switch — 器件开启时的阳极-阴极电阻
- IGBT — 器件开启时的集电极-发射极电阻
- Thyristor — 器件开启时的阳极-阴极电阻
- Averaged switch — 器件开启时的阳极-阴极电阻

#### 依赖项

请参阅非隔离变换器开关器件参数依赖关系表。

### **漏源导通电阻** — 电阻 `0.001` `Ohm`（默认）| scalar

漏极和源极之间的电阻，该电阻还取决于门极到源极电压。

#### 依赖项

请参阅非隔离变换器开关器件参数依赖关系表。

### **关断状态电导** — 电导 `1e-5` `1/Ohm`（默认）| scalar

器件关断时的电导。该值必须小于 1/*R*，其中 *R* 是 **导通状态电阻** 的值。

对于不同的开关器件类型，**导通状态电阻** 取为：

- GTO — 阳极-阴极电导
- Ideal semiconductor switch — 阳极-阴极电导
- IGBT — 集电极-发射极电导
- MOSFET — 漏源电导
- Thyristor — 阳极-阴极电导

#### 依赖项

请参阅非隔离变换器开关器件参数依赖关系表。

### **阈值电压** — 电压阈值 `6` `V`（默认）| scalar

门极电压阈值。当门极电压高于此值时，器件开启。对于不同的开关器件类型，相关的器件电压为：

- Ideal semiconductor switch — 门极-阴极电压
- IGBT — 门极-发射极电压
- MOSFET — 门极-源极电压

#### 依赖项

请参阅非隔离变换器开关器件参数依赖关系表。

### **门极触发电压, Vgt** — 电压阈值 `1` `V`（默认）| scalar

门极-阴极电压阈值。当门极-阴极电压高于此值时，器件开启。

#### 依赖项

请参阅非隔离变换器开关器件参数依赖关系表。

### **门极关断电压, Vgt\_off** — 电压阈值 `-1` `V`（默认）| scalar

门极-阴极电压阈值。当门极-阴极电压低于此值时，器件关断。

#### 依赖项

请参阅非隔离变换器开关器件参数依赖关系表。

### **保持电流** — 电流阈值 `1` `A`（默认）| scalar

门极电流阈值。当电流高于此值时，即使门极-阴极电压降至门极触发电压以下，器件仍保持开启。

#### 依赖项

请参阅非隔离变换器开关器件参数依赖关系表。

### **开关器件 HV** — 开关 `Ideal Semiconductor Switch`（默认）| `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

隔离变换器模型高压侧的开关器件类型。

#### 依赖项

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **正向电压 HV** — 电压 `0.8` `Ohm`（默认）| scalar

对于不同的开关器件类型，**正向电压 HV** 取为：

- GTO — 使器件 I-V 特性的梯度为 1/*Ron* 所需的阳极和阴极块端口之间的最小电压，其中 *Ron* 是 **导通状态电阻** 的值
- IGBT — 使二极管 i-v 特性的梯度为 1/*Ron* 所需的集电极和发射极块端口之间的最小电压，其中 *Ron* 是 **导通状态电阻** 的值
- Thyristor — 器件导通所需的最小电压

#### 依赖项

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **漏源导通电阻 HV** — 电阻 `0.001` `Ohm`（默认）| scalar

漏极和源极之间的电阻，该电阻还取决于门极到源极电压。

#### 依赖项

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **导通状态电阻 HV** — 电阻 `0.001` `Ohm`（默认）| scalar

对于不同的开关器件类型，**导通状态电阻 HV** 取为：

- GTO — 高于正向电压时电压对电流的变化率
- Ideal semiconductor switch — 器件开启时的阳极-阴极电阻
- IGBT — 器件开启时的集电极-发射极电阻
- Thyristor — 器件开启时的阳极-阴极电阻
- Averaged switch — 器件开启时的阳极-阴极电阻

#### 依赖项

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **关断状态电导 HV** — 电导 `1e-5` `1/Ohm`（默认）| scalar

器件关断时的电导。该值必须小于 1/*R*，其中 *R* 是 **导通状态电阻 HV** 的值。

对于不同的开关器件类型，**导通状态电阻 HV** 取为：

- GTO — 阳极-阴极电导
- Ideal semiconductor switch — 阳极-阴极电导
- IGBT — 集电极-发射极电导
- MOSFET — 漏源电导
- Thyristor — 阳极-阴极电导

#### 依赖项

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **阈值电压 HV** — 电压阈值 `6` `V`（默认）| scalar

门极电压阈值。当门极电压高于此值时，器件开启。对于不同的开关器件类型，相关的器件电压为：

- Ideal semiconductor switch — 门极-阴极电压
- IGBT — 门极-发射极电压
- MOSFET — 门极-源极电压

#### 依赖项

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **门极触发电压 HV, Vgt\_hv** — 电压阈值 `1` `V`（默认）| scalar

门极-阴极电压阈值。当门极-阴极电压高于此值时，器件开启。

#### 依赖项

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **门极关断电压 HV, Vgt\_off\_hv** — 电压阈值 `-1` `V`（默认）| scalar

门极-阴极电压阈值。当门极-阴极电压低于此值时，器件关断。

#### 依赖项

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **保持电流 HV** — 电流阈值 `1` `A`（默认）| scalar

门极电流阈值。当电流高于此值时，即使门极-阴极电压降至门极触发电压以下，器件仍保持开启。

#### 依赖项

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **开关器件 LV** — 开关 `Ideal Semiconductor Switch`（默认）| `GTO` | `IGBT` | `MOSFET` | `Thyristor` | `Averaged Switch`

隔离变换器模型低压侧的开关器件类型。

#### 依赖项

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **正向电压 LV** — 电压 `0.8` `Ohm`（默认）| scalar

对于不同的开关器件类型，**正向电压 LV** 取为：

- GTO — 使器件 I-V 特性的梯度为 1/*Ron* 所需的阳极和阴极块端口之间的最小电压，其中 *Ron* 是 **导通状态电阻** 的值
- IGBT — 使二极管 i-v 特性的梯度为 1/*Ron* 所需的集电极和发射极块端口之间的最小电压，其中 *Ron* 是 **导通状态电阻** 的值
- Thyristor — 器件导通所需的最小电压

#### 依赖项

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **漏源导通电阻 LV** — 电阻 `0.001` `Ohm`（默认）| scalar

漏极和源极之间的电阻，该电阻还取决于门极到源极电压。

#### 依赖项

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **导通状态电阻 LV** — 电阻 `0.001` `Ohm`（默认）| scalar

对于不同的开关器件类型，**导通状态电阻 LV** 取为：

- GTO — 高于正向电压时电压对电流的变化率
- Ideal semiconductor switch — 器件开启时的阳极-阴极电阻
- IGBT — 器件开启时的集电极-发射极电阻
- Thyristor — 器件开启时的阳极-阴极电阻
- Averaged switch — 器件开启时的阳极-阴极电阻

#### 依赖项

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **关断状态电导 LV** — 电导 `1e-5` `1/Ohm`（默认）| scalar

器件关断时的电导。该值必须小于 1/*R*，其中 *R* 是 **导通状态电阻 LV** 的值。

对于不同的开关器件类型，**导通状态电阻 LV** 取为：

- GTO — 阳极-阴极电导
- Ideal semiconductor switch — 阳极-阴极电导
- IGBT — 集电极-发射极电导
- MOSFET — 漏源电导
- Thyristor — 阳极-阴极电导

#### 依赖项

请参阅隔离变换器和双有源桥变换器开关器件参数依赖关系表。

### **阈值电压 LV** — 电压阈值 `6` `V`（默认）| scalar

栅极电压阈值。当栅极电压高于此值时，器件导通。对于不同的开关器件类型，关注的器件电压为：

- Ideal semiconductor switch — 栅-阴极电压
- IGBT — 栅-发射极电压
- MOSFET — 栅-源极电压

#### 依赖关系

请参阅 Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies 表。

### **栅极触发电压 LV, Vgt\_lv** — 电压阈值 `1` `V`（默认）| scalar

栅-阴极电压阈值。当栅-阴极电压高于此值时，器件导通。

#### 依赖关系

请参阅 Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies 表。

### **栅极关断电压 LV, Vgt\_off\_lv** — 电压阈值 `-1` `V`（默认）| scalar

栅-阴极电压阈值。当栅-阴极电压低于此值时，器件关断。

#### 依赖关系

请参阅 Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies 表。

### **维持电流 LV** — 电流阈值 `1` `A`（默认）| scalar

栅极电流阈值。当电流高于此值时，即使栅-阴极电压降至栅极触发电压以下，器件仍保持导通。

#### 依赖关系

请参阅 Isolated Converter and Dual Active Bridge Converter Switching Devices Parameter Dependencies 表。

### **用于门极输入分段常数逼近的整数（0 表示禁用）** — FPGA 部署的整数模式 `0`（默认）| nonnegative scalar

用于对 FPGA 部署的门极输入执行分段常数逼近的整数。

#### 依赖关系

要启用此参数，请将 **开关器件** 设置为 `Averaged Switch`。

### 保护二极管

要启用这些参数，请选择以下选项之一：

- 将 **建模选项** 设置为 `Nonisolated
  converter` 或 `Dual Active Bridge
  converter`，并将 **保真度级别** 设置为
  `Detailed model - switching
  devices`。
- 将 **建模选项** 设置为 `Isolated
  converter`。

**保护二极管** 参数的可见性取决于如何配置 **模型动态** 和
**反向恢复时间参数化** 参数。要了解如何阅读此表，请参阅参数依赖关系。

**保护二极管参数依赖关系**

| 参数和选项 | | | |
| --- | --- | --- | --- |
| **模型动态** | | | |
| *Diode with no dynamics* | *Diode with charge dynamics* | | |
| 正向电压 | 正向电压 | | |
| 导通电阻 | 导通电阻 | | |
| 断态电导 | 断态电导 | | |
| 结电容 | | |
| 峰值反向电流, iRM | | |
| 测量 iRM 时的初始正向电流 | | |
| 测量 iRM 时的电流变化率 | | |
| **反向恢复时间参数化** | | |
| *`Specify stretch factor`* | *`Specify reverse recovery time directly`* | *`Specify reverse recovery charge`* |
| 反向恢复时间拉伸因子 | 反向恢复时间, trr | 反向恢复电荷, Qrr |

**注意**

如果将 **开关器件** 参数设置为
`Averaged Switch`，则模块对保护二极管进行无动态建模，并且 **模型动态**
参数不可见。

### **模型动态** — 二极管模型 `Diode with no dynamics`（默认）| `Diode with charge dynamics`

Bidirectional DC-DC Converter 模块用于每个开关器件的保护二极管的模型。选择以下选项之一：

- `None` — Bidirectional DC-DC Converter 不对保护二极管建模。
- `Diode with no dynamics` — Bidirectional DC-DC Converter 模块使用与无动态 Diode 模块相同的方程对保护二极管建模。选择此选项可优先考虑仿真速度。
- `Diode with charge dynamics` — Bidirectional DC-DC Converter 模块使用与有电荷动态 Diode 模块相同的方程对保护二极管建模。选择此选项可优先考虑详细仿真结果。

#### 依赖关系

请参阅保护二极管参数依赖关系表。

### **正向电压** — 电压 `0.8` `V`（默认）| scalar

使二极管 I-V 特性的斜率为 1/*Ron* 所需的跨正负模块端口的最小电压，其中 *Ron* 是 **导通电阻** 参数的值。

### **导通电阻** — 导通电阻 `0.001` `Ohm`（默认）| scalar

高于 **正向电压** 参数值时的电压随电流的变化率。

### **断态电导** — 电导 `1e-5` `1/Ohm`（默认）| scalar

反向偏置二极管的电导。

### **结电容** — 结电容 `50` `nF`（默认）| scalar

二极管结电容。

#### 依赖关系

请参阅保护二极管参数依赖关系表。

### **峰值反向电流, iRM** — 峰值反向电流 `-235` `A`（默认）| negative scalar

由外部测试电路测得的峰值反向电流。

#### 依赖关系

请参阅保护二极管参数依赖关系表。

### **测量 iRM 时的初始正向电流** — 测量 iRM 时的初始正向电流 `300` `A`（默认）| positive scalar

测量峰值反向电流时的初始正向电流。

#### 依赖关系

请参阅保护二极管参数依赖关系表。

### **测量 iRM 时的电流变化率** — 电流变化率 `-50` `A/us`（默认）| scalar

测量峰值反向电流时的电流变化率。

#### 依赖关系

请参阅保护二极管参数依赖关系表。

### **反向恢复时间参数化** — 恢复时间模型 `Specify stretch factor`（默认）| `Specify reverse recovery time directly` | `Specify reverse recovery charge`

用于参数化恢复时间的模型。当您选择
`Specify stretch factor` 或
`Specify reverse recovery charge` 时，可以指定一个值，模块使用该值推导反向恢复时间。
有关这些选项的详细信息，请参阅 How the Block Calculates TM and Tau。

#### 依赖关系

请参阅保护二极管参数依赖关系表。

### **反向恢复时间拉伸因子** — 反向恢复时间拉伸因子 `3`（默认）| scalar greater than `1`

模块用于计算反向恢复时间的拉伸因子。指定拉伸因子比指定反向恢复电荷更容易参数化反向恢复时间。拉伸因子的值越大，反向恢复电流消散所需的时间越长。

#### 依赖关系

请参阅保护二极管参数依赖关系表。

### **反向恢复时间, trr** — 反向恢复时间 `15` `us`（默认）| scalar

电流初始降为零（二极管关断时）与电流降至峰值反向电流的 10% 以下之间的时间间隔。

**反向恢复时间, trr** 参数的值必须大于 **峰值反向电流, iRM** 参数的值除以 **测量 iRM 时的电流变化率** 参数的值。

#### 依赖关系

请参阅保护二极管参数依赖关系表。

### **反向恢复电荷, Qrr** — 反向恢复电荷 `1500` `s*uA`（默认）| scalar

模块用于计算反向恢复时间的反向恢复电荷。如果您的二极管器件数据手册指定了反向恢复电荷的值而不是反向恢复时间的值，请使用此参数。

反向恢复电荷是二极管关断时继续耗散的总电荷。该值必须小于 −i2RM2a，

其中：

- *iRM* 是为 **峰值反向电流, iRM** 指定的值。
- *a* 是为 **测量 iRM 时的电流变化率** 指定的值。

#### 依赖关系

请参阅保护二极管参数依赖关系表。

### 变压器

### **变压器一次绕组自感, L1** — 变压器一次绕组自感 `0.03` `H`（默认）| positive scalar

变压器一次绕组的自感。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Isolated converter` 或 `Dual Active Bridge converter`。

### **变压器二次绕组自感, L2** — 变压器二次绕组自感 `0.03` `H`（默认）| positive scalar

变压器二次绕组的自感。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Isolated converter` 或 `Dual Active Bridge converter`。

### **变压器耦合系数** — 耦合系数 `0.9`（默认）| positive scalar greater than zero and less than 1

定义变压器的互感。

#### 依赖关系

要启用此参数，请将 **建模选项** 设置为 `Isolated converter` 或 `Dual Active Bridge converter`。

### LC 参数

### **电感, L** — 电感 `1e-6` `H`（默认）| positive scalar

转换器电感。如果将 **建模选项** 参数设置为 `Isolated converter`，则两个电感相同。

### **电感串联电阻** — 电感串联电阻 `0` `Ohm`（默认）| zero or positive scalar

电感的串联电阻。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将 **建模选项** 设置为
  `Isolated
  converter`。
- 将 **建模选项** 设置为
  `Nonisolated converter` 或
  `Dual Active Bridge
  converter`，并将 **保真度级别** 设置为 `Detailed model -
  switching devices`。

### **电容, C1** — 电容 `1e-7` `F`（默认）| positive scalar

第一个直流端子的电容。

### **电容, C2** — 电容 `1e-7` `F`（默认）| positive scalar

第二个直流端子的电容。

### **C1 有效串联电阻** — 电阻 `1e-6` `Ohm`（默认）| zero or positive scalar

电容 *C1* 的串联电阻。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将 **建模选项** 设置为
  `Isolated
  converter`。
- 将 **建模选项** 设置为
  `Nonisolated converter` 或
  `Dual Active Bridge
  converter`，并将 **保真度级别** 设置为 `Detailed model -
  switching devices`。

### **C2 有效串联电阻** — 电阻 `1e-6` `Ohm`（默认）| zero or positive scalar

电容 *C2* 的串联电阻。

#### 依赖关系

要启用此参数，请选择以下选项之一：

- 将 **建模选项** 设置为
  `Isolated
  converter`。
- 将 **建模选项** 设置为
  `Nonisolated converter` 或
  `Dual Active Bridge
  converter`，并将 **保真度级别** 设置为 `Detailed model -
  switching devices`。

### 缓冲器

要启用这些参数，请将 **开关器件** 设置为以下选项之一：

- `Ideal Semiconductor Switch`
- `GTO`
- `IGBT`
- `MOSFET`
- `Thyristor`

此表总结了 **缓冲器** 参数依赖关系。要了解如何阅读此表，请参阅参数依赖关系。

**缓冲器参数依赖关系**

| 缓冲器参数依赖关系 | | | | | |
| --- | --- | --- | --- | --- | --- |
| **建模选项** | | | | | |
| *`Nonisolated Converter`* | | *`Isolated Converter`* | | *`Dual Active Bridge converter`* | |
| **缓冲器** | | **HV 缓冲器** | | **HV 缓冲器** | |
| *`None`* | *`RC Snubber`* | **`None`** | *`RC Snubber`* | **`None`** | *`RC Snubber`* |
| 缓冲电阻 | HV 缓冲电阻 | HV 缓冲电阻 |
| 缓冲电容 | HV 缓冲电容 | HV 缓冲电容 |
| **LV 缓冲器** | | **LV 缓冲器** | |
| *`None`* | *`RC Snubber`* | *`None`* | *`RC Snubber`* |
| LV 缓冲电阻 | LV 缓冲电阻 |
| LV 缓冲电容 | LV 缓冲电容 |

### **缓冲器** — 缓冲器模型 `None`（默认）| `RC snubber`

每个开关器件的缓冲器。

#### 依赖关系

请参阅缓冲器参数依赖关系表。

### **缓冲电阻** — 电阻 `0.1` `Ohm`（默认）| scalar

缓冲器的电阻。

#### 依赖关系

请参阅缓冲器参数依赖关系表。

### **缓冲电容** — 电容 `1e-7` `F`（默认）| scalar

缓冲器的电容。

#### 依赖关系

请参阅缓冲器参数依赖关系表。

### **HV 缓冲器** — 缓冲器模型 `None`（默认）| `RC snubber`

每个开关器件的 HV 缓冲器。

#### 依赖关系

请参阅缓冲器参数依赖关系表。

### **HV 缓冲电阻** — 电阻 `0.1` `Ohm`（默认）| scalar

高压缓冲器的电阻。

#### 依赖关系

请参阅缓冲器参数依赖关系表。

### **HV 缓冲电容** — 电容 `1e-7` `F`（默认）| scalar

高压缓冲器的电容。

#### 依赖关系

请参阅缓冲器参数依赖关系表。

### **LV 缓冲器** — 缓冲器模型 `None`（默认）| `RC snubber`

每个开关器件的 LV 缓冲器。

#### 依赖关系

请参阅缓冲器参数依赖关系表。

### **LV 缓冲电阻** — 电阻 `0.1` `Ohm`（默认）| scalar

低压缓冲器的电阻。

#### 依赖关系

请参阅缓冲器参数依赖关系表。

### **LV 缓冲电容** — 电容 `1e-7` `F`（默认）| scalar

低压缓冲器的电容。

#### 依赖关系

请参阅缓冲器参数依赖关系表。

## 所属库

Simscape / Electrical / Semiconductors & Converters / Converters

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018a 中引入**

### R2024a: 使用等效模型提高仿真速度

如果您对非隔离转换器或双有源桥转换器建模，现在可以从转换器模型的两种保真度级别中进行选择。等效模型选项不对单个开关器件建模，而是返回等效结果。如果您需要开关器件动态的详细结果，请使用详细模型选项。否则，请使用等效模型以加快仿真速度。要进行实时仿真，请使用等效模型。要验证结果，请使用带可变步长求解器的详细模型。

要使用详细模型，请将 **保真度级别** 参数设置为 `Detailed model - switching devices`。要使用等效模型，请将 **保真度级别** 参数设置为 `Equivalent model - PWM-controlled`。

在 R2024a 之前，只能使用详细模型。

## 描述

由控制器驱动的双向 DC-DC 升压和降压电压调节器

Bidirectional DC-DC Converter 模块表示一种变换器，其由所连接的控制器和门极信号发生器驱动，将 DC 电压从变换器任一侧升压或降压到另一侧。双向 DC-DC 变换器可用于在能量存储和使用之间切换，例如在电动汽车中。

Bidirectional DC-DC Converter 模块允许您对具有两个开关器件的非隔离变换器、具有六个开关器件的隔离变换器或具有八个开关器件的双有源桥变换器进行建模。

如果您对非隔离变换器或双有源桥变换器建模，则可以为变换器模型选择两个保真度级别之一。等效模型选项不会对各个开关器件建模，但会返回等效结果。如果您需要开关器件动态的详细结果，请使用详细模型选项。否则，为了更快仿真，请使用等效模型。要进行实时仿真，请使用等效模型。要验证结果，请将详细模型与可变步长求解器一起使用。要使用详细模型，请将 **Fidelity level** 参数设置为 `Detailed model - switching devices`。要使用等效模型，请将 **Fidelity level** 参数设置为 `Equivalent model - PWM-controlled`。

如果您对隔离变换器建模，则只能使用详细模型。**Fidelity level** 参数不可见。

如果您选择详细模型，则每个组件都是相同的开关器件，您可以通过设置 **Switching device** 参数来指定该器件。您可以指定的开关器件是 **Simscape** > **Electrical** > **Semiconductors & Converters** 库中模块的实现：

- GTO — 门极可关断晶闸管。有关该器件的 I-V 特性信息，请参阅 GTO。
- Ideal semiconductor switch — 有关该器件的 I-V 特性信息，请参阅 Ideal Semiconductor Switch。
- IGBT — 绝缘栅双极型晶体管。有关该器件的 I-V 特性信息，请参阅 IGBT (Ideal, Switching)。
- MOSFET — N 沟道金属氧化物半导体场效应晶体管。有关该器件的 I-V 特性信息，请参阅 MOSFET (Ideal, Switching)。
- Thyristor — 有关该器件的 I-V 特性信息，请参阅 Thyristor (Piecewise Linear)。
- Averaged Switch — 带有反并联二极管的半导体开关。控制信号端口 **G** 接受区间 [0,1] 中的值。当 **G** 等于 `0` 或 `1` 时，Averaged Switch 分别完全断开或完全闭合。该开关的行为类似于带有反并联二极管的 Ideal Semiconductor Switch 模块。当 **G** 在 0 和 1 之间时，Averaged Switch 部分断开。您可以在指定周期内对脉冲宽度调制 (PWM) 信号求平均。然后，您可以对模型进行欠采样，并使用调制波形代替 PWM 信号。

**注意**

如果您将 **Switching device** 参数设置为 `Averaged Switch`，则模块会自动对无动态的保护二极管建模，并且 **Model dynamics** 参数不可见。

### 模型

您可以对三种不同类型的双向 DC-DC 变换器进行建模。要访问不同选项，双击模块，并将 **Modeling option** 参数设置为以下之一：

- `Nonisolated converter` — 无电气隔离屏障的双向 DC-DC 变换器。此变换器包含一个电感、两个电容和两个开关，且这些开关为同一器件类型。
- `Isolated converter` — 带电气隔离屏障的双向 DC-DC 变换器。此变换器包含四个额外开关，它们构成一个全桥。全桥位于变换器的输入或高压 (HV) 侧。另外两个开关位于变换器的输出或低压 (LV) 侧。您可以为 HV 和 LV 开关器件选择不同的半导体类型。例如，您可以为 HV 开关器件使用 GTO，为 LV 开关器件使用 IGBT。为了在输入和输出电压之间提供隔离，模型使用高频变压器。
- `Dual Active Bridge converter` — 此双向 DC-DC 变换器包含两个全桥。左侧桥是变换器的输入或高压 (HV) 侧。右侧桥是变换器的输出或低压 (LV) 侧。您可以为 HV 和 LV 开关器件选择不同的半导体类型。例如，您可以为 HV 开关器件使用 GTO，为 LV 开关器件使用 IGBT。为了在输入和输出电压之间提供隔离，模型使用高频变压器。要使用等效模型并将变压器两侧中的任意一侧用作整流器，请将该侧对应的 PWM 信号元素设置为零。变压器的该侧表现为二极管整流器。

### 保护

该模块为每个开关器件包含一个集成保护二极管。集成二极管通过为反向电流提供导通路径来保护半导体器件。当半导体器件突然关断对负载的电压供应时，感性负载可能产生高反向电压尖峰。

要配置内部保护二极管模块，请使用 **Protection Diode** 参数。此表显示如何根据您的目标设置 **Model dynamics** 参数。

| 目标 | 要选择的值 | 集成保护二极管 |
| --- | --- | --- |
| 优先考虑仿真速度。 | `Diode with no dynamics` | Diode 模块 |
| 优先考虑模型保真度，通过精确指定反向模式电荷动态。 | `Diode with charge dynamics` | Diode 模块的动态模型 |

您还可以为每个开关器件包含一个缓冲电路。缓冲电路包含一个串联连接的电阻和电容。它们保护开关器件免受感性负载在器件关断对负载的电压供应时产生的高电压影响。缓冲电路还防止开关器件导通时出现过大的电流变化率。

要为每个开关器件包含并配置缓冲电路，请使用 **Snubbers** 参数。

### 门极控制

要将 Simulink® 门极控制电压信号连接到开关器件的门极端口：

1. 使用 Simulink-PS Converter 模块转换每个电压信号。
2. 将转换后的门极信号多路复用为单个向量。

   - 对于非隔离变换器模型，使用 Two-Pulse Gate Multiplexer 模块。
   - 对于隔离变换器模型，使用 Six-Pulse Gate Multiplexer 模块。
   - 对于双有源桥变换器模型，使用 Eight-Pulse Gate Multiplexer 模块。
3. 将向量信号连接到 **G** 端口。

### Averaged Switch 中用于 FPGA 部署的分段常数近似

如果您将 **Switching device** 参数设置为 `Averaged switch`，并且您的模型使用分区求解器，则此模块会产生非线性分区，因为平均模式方程包含模式 *Gsat*，该模式是输入 **G** 的函数。为使这些方程与硬件描述语言 (HDL) 代码生成兼容，并因此适用于 FPGA 部署，请将 **Integer for piecewise constant approximation of gate input (0 for disabled)** 参数设置为大于 `0` 的值。然后，此模块将 *Gsat* 模式视为具有固定范围的分段常数整数。这将先前非线性分区转换为线性时变分区。

现在，范围 `[0,K]` 中的整数值（其中 *K* 是 **Integer for piecewise constant approximation of gate input (0 for disabled)** 的值）与范围 `[0,1]` 中的每个实数值模式相关联。该模块通过将原始模式除以 K 来计算分段常数模式，以将其归一化回范围 `[0,1]`：

uI=(floor(u⋅K))u^=uIK

### 假设

源阻抗或非零等效串联电阻 (ESR) 连接到 Bidirectional DC-DC Converter 模块的左侧。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种在模型中指定变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。您可以使用不同来源指定标称值，包括模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
