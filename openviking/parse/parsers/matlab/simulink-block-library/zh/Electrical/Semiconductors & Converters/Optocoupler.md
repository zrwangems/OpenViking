---
type: simulink-block
title: 'Optocoupler'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'optocoupler'
documentation_source_path: 'ref/optocoupler.html'
language: zh-CN
chinese_source: worker-translation
---

# Optocoupler

## 端口
```yaml
ports:
- name: +
  summary: 正极端子电气
  direction: conserving
- name: '-'
  summary: 负极端子电气
  direction: conserving
- name: C
  summary: 晶体管集电极端子电气
  direction: conserving
- name: E
  summary: 晶体管发射极端子电气
  direction: conserving
- name: H
  summary: 热端口热
  direction: conserving
```

### 守恒端口

### **+** — 正极端子电气

与二极管正极端子关联的电气守恒端口

### **-** — 负极端子电气

与二极管负极端子关联的电气守恒端口

### **C** — 晶体管集电极端子电气

与晶体管集电极端子关联的电气守恒端口

### **E** — 晶体管发射极端子电气

与晶体管发射极端子关联的电气守恒端口

### **H** — 热端口热

热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show
thermal port`。
## 参数
```yaml
parameters:
- name: Modeling option
  summary: 是否启用热端口 No thermal port（默认）| Show thermal port
  group: ''
- name: Current transfer ratio
  summary: 电流传输比 0.2（默认）
  group: 主
- name: Diode parameterization
  summary: 模型参数化 Use I-V curve data points（默认）| Use parameters IS and N
  group: 主
- name: Currents [I1 I2]
  summary: 两个点处的电流值向量 [.001, .015] A（默认）
  group: 主
- name: Voltages [V1 V2]
  summary: 两个点处的电压值向量 [.9, 1.05] V（默认）
  group: 主
- name: Ohmic resistance, RS
  summary: 欧姆电阻 0.1 Ohm（默认）
  group: 主
- name: Saturation current, IS
  summary: 饱和电流 1e-10 A（默认）
  group: 主
- name: Measurement temperature
  summary: 测量温度 25 °C（默认）
  group: 主
- name: Emission coefficient, N
  summary: 二极管发射系数 2（默认）
  group: 主
- name: Capacitance
  summary: 二极管结电容建模 Fixed or zero junction capacitance（默认）| Use C-V curve data points | Use parameters CJ0, VJ, M & FC
  group: 结电容
- name: Junction capacitance
  summary: 二极管结电容 5 pF（默认）
  group: 结电容
- name: Zero-bias junction capacitance, CJ0
  summary: 零偏结电容 5 pF（默认）
  group: 结电容
- name: Junction potential, VJ
  summary: 结电势 1 V（默认）
  group: 结电容
- name: Grading coefficient, M
  summary: 梯度系数 0.5（默认）
  group: 结电容
- name: Reverse bias voltages [VR1 VR2 VR3]
  summary: 反向偏置电压向量 [.1, 10, 100] V（默认）
  group: 结电容
- name: Corresponding capacitances [C1 C2 C3]
  summary: 对应电容向量 [3.5, 1, .4] pF（默认）
  group: 结电容
- name: Capacitance coefficient, FC
  summary: 拟合电容系数 0.5（默认）
  group: 结电容
- name: Parameterization
  summary: 温度依赖性参数化 None — Simulate at parameter measurement temperature（默认）| Use an I-V data point at second measurement
    temperature T2 | Specify saturation current at second measurement temperature T2 | Specify the energy gap EG
  group: 温度依赖性
- name: Current I1 at second measurement temperature
  summary: 第二测量温度下的电流 I1 0.029 A（默认）
  group: 温度依赖性
- name: Voltage V1 at second measurement temperature
  summary: 第二测量温度下的电压 V1 1.05 V（默认）
  group: 温度依赖性
- name: Saturation current, IS, at second measurement temperature
  summary: 第二测量温度下的饱和电流 IS 1.8e-8 A（默认）
  group: 温度依赖性
- name: Second measurement temperature
  summary: 第二测量温度 125 °C（默认）
  group: 温度依赖性
- name: Energy gap parameterization
  summary: 能隙参数化 Use nominal value for silicon (EG=1.11eV)（默认）| Use nominal value for 4H-SiC silicon carbide (EG=3.23eV) |
    Use nominal value for 6H-SiC silicon carbide (EG=3.00eV) | Use nominal value for germanium (EG=0.67eV) | Use nominal value
    for gallium arsenide (EG=1.43eV) | Use nominal value for selenium (EG=1.74eV) | Use nominal value for Schottky barrier
    diodes (EG=0.69eV) | Specify a custom value
  group: 温度依赖性
- name: Energy gap, EG
  summary: 能隙 1.11 eV（默认）
  group: 温度依赖性
- name: Saturation current temperature exponent parameterization
  summary: 饱和电流温度指数参数化 Use nominal value for pn-junction diode (XTI=3)（默认）| Use nominal value for Schottky barrier diode (XTI=2)
    | Specify a custom value
  group: 温度依赖性
- name: Saturation current temperature exponent, XTI
  summary: 饱和电流温度指数 3（默认）
  group: 温度依赖性
- name: Device simulation temperature
  summary: 器件仿真温度 25 °C（默认）
  group: 温度依赖性
```

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口并对生成的热量和器件温度的影响进行建模。

### 主

### **Current transfer ratio** — 电流传输比 `0.2`（默认）

从晶体管集电极结流向发射极结的输出电流等于电流传输比与流过发光二极管的电流的乘积。

### **Diode parameterization** — 模型参数化 `Use I-V curve data points`（默认）| `Use parameters IS and N`

选择以下模型参数化方法之一：

- `Use I-V curve data points` — 指定二极管 I-V 曲线上两个点的测量数据。
- `Use parameters IS and N` — 指定饱和电流和发射系数。

### **Currents [I1 I2]** — 两个点处的电流值向量 `[.001, .015]` `A`（默认）

模块用于计算 *IS* 和 *N* 的二极管 I-V 曲线上两个点处的电流值向量。

#### 依赖关系

仅当为 **Diode parameterization** 参数选择 `Use I-V curve data
points` 时，此参数才可见。

### **Voltages [V1 V2]** — 两个点处的电压值向量 `[.9, 1.05]` `V`（默认）

模块用于计算 *IS* 和 *N* 的二极管 I-V 曲线上两个点处的电压值向量。

#### 依赖关系

仅当为 **Diode parameterization** 参数选择 `Use I-V curve data
points` 时，此参数才可见。

### **Ohmic resistance, RS** — 欧姆电阻 `0.1` `Ohm`（默认）

串联二极管连接电阻。

### **Saturation current, IS** — 饱和电流 `1e-10` `A`（默认）

理想二极管方程在非常大的反向偏置水平下渐近逼近的电流大小。

#### 依赖关系

仅当为 **Diode parameterization** 参数选择 `Use parameters IS and
N` 时，此参数才可见。

### **Measurement temperature** — 测量温度 `25` `°C`（默认）

测量 IS 或 I-V 曲线时的温度。默认值为 `25` °C。

### **Emission coefficient, N** — 二极管发射系数 `2`（默认）

二极管发射系数或理想因子。

#### 依赖关系

仅当为 **Diode parameterization** 参数选择 `Use parameters IS and
N` 时，此参数才可见。

### 结电容

### **Capacitance** — 二极管结电容建模 `Fixed or zero junction capacitance`（默认）| `Use C-V curve data points` | `Use parameters CJ0, VJ, M & FC`

选择以下二极管结电容建模选项之一：

- `Fixed or zero junction capacitance` — 将结电容建模为固定值。
- `Use C-V curve data points` — 指定二极管 C-V 曲线上三个点的测量数据。
- `Use parameters CJ0, VJ, M & FC` — 指定零偏结电容、结电势、梯度系数和正向偏置耗尽电容系数。

### **Junction capacitance** — 二极管结电容 `5` `pF`（默认）

固定结电容值。

#### 依赖关系

仅当为 **Capacitance** 参数选择 `Fixed or zero junction
capacitance` 时，此参数才可见。

### **Zero-bias junction capacitance, CJ0** — 零偏结电容 `5` `pF`（默认）

与指数二极管项并联放置的电容值。

#### 依赖关系

仅当为 **Capacitance** 参数选择 `Use parameters CJ0, VJ, M
& FC` 时，此参数才可见。

### **Junction potential, VJ** — 结电势 `1` `V`（默认）

结电势。

#### 依赖关系

仅当为 **Capacitance** 参数选择 `Use parameters CJ0, VJ, M
& FC` 时，此参数才可见。

### **Grading coefficient, M** — 梯度系数 `0.5`（默认）

量化结梯度的系数。

#### 依赖关系

仅当为 **Capacitance** 参数选择 `Use parameters CJ0, VJ, M
& FC` 时，此参数才可见。

### **Reverse bias voltages [VR1 VR2 VR3]** — 反向偏置电压向量 `[.1, 10, 100]` `V`（默认）

模块用于计算 *CJ0*、*VJ* 和 *M* 的二极管 C-V 曲线上三个点处的反向偏置电压值向量。

#### 依赖关系

仅当为 **Capacitance** 参数选择 `Use C-V curve data
points` 时，此参数才可见。

### **Corresponding capacitances [C1 C2 C3]** — 对应电容向量 `[3.5, 1, .4]` `pF`（默认）

模块用于计算 *CJ0*、*VJ* 和 *M* 的二极管 C-V 曲线上三个点处的电容值向量。

#### 依赖关系

仅当为 **Capacitance** 参数选择 `Use C-V curve data
points` 时，此参数才可见。

### **Capacitance coefficient, FC** — 拟合电容系数 `0.5`（默认）

量化耗尽电容随施加电压降低的拟合系数。

#### 依赖关系

仅当为 **Capacitance** 参数选择 `Use C-V curve data
points` 或 `Use parameters CJ0, VJ, M & FC` 时，此参数才可见。

### 温度依赖性

### **Parameterization** — 温度依赖性参数化 `None — Simulate at parameter measurement temperature`（默认）| `Use an I-V data point at second measurement temperature T2` | `Specify saturation current at second measurement temperature T2` | `Specify the energy gap EG`

选择以下温度依赖性参数化方法之一：

- `None — Simulate at parameter measurement temperature`
  — 不对温度依赖性建模，或者模型在测量温度 *T*m1（由 **Main** 选项卡上的 **Measurement temperature** 参数指定）下仿真。这是默认方法。
- `Use an I-V data point at second measurement temperature T2`
  — 如果选择此选项，则指定第二测量温度 *T*m2 以及该温度下的电流和电压值。模型使用这些值以及第一测量温度 *T*m1 下的参数值来计算能隙值。
- `Specify saturation current at second measurement temperature
  T2` — 如果选择此选项，则指定第二测量温度 *T*m2 以及该温度下的饱和电流值。模型使用这些值以及第一测量温度 *T*m1 下的参数值来计算能隙值。
- `Specify the energy gap EG` — 直接指定能隙值。

### **Current I1 at second measurement temperature** — 第二测量温度下的电流 I1 `0.029` `A`（默认）

指定在第二测量温度下电压为 *V1* 时的二极管电流 *I1* 值。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Use an I-V data point at
second measurement temperature T2` 时，此参数才可见。

### **Voltage V1 at second measurement temperature** — 第二测量温度下的电压 V1 `1.05` `V`（默认）

指定在第二测量温度下电流为 *I1* 时的二极管电压 *V1* 值。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Use an I-V data point at
second measurement temperature T2` 时，此参数才可见。

### **Saturation current, IS, at second measurement temperature** — 第二测量温度下的饱和电流 IS `1.8e-8` `A`（默认）

指定第二测量温度下的饱和电流 *IS* 值。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Specify saturation current
at second measurement temperature T2` 时，此参数才可见。

### **Second measurement temperature** — 第二测量温度 `125` `°C`（默认）

指定第二测量温度的值。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Use an I-V data point at
second measurement temperature T2` 或 `Specify saturation current
at second measurement temperature T2` 时，此参数才可见。

### **Energy gap parameterization** — 能隙参数化 `Use nominal value for silicon (EG=1.11eV)`（默认）| `Use nominal value for 4H-SiC silicon carbide (EG=3.23eV)` | `Use nominal value for 6H-SiC silicon carbide (EG=3.00eV)` | `Use nominal value for germanium (EG=0.67eV)` | `Use nominal value for gallium arsenide (EG=1.43eV)` | `Use nominal value for selenium (EG=1.74eV)` | `Use nominal value for Schottky barrier diodes (EG=0.69eV)` | `Specify a custom value`

从预定选项列表中选择能隙值，或指定自定义值：

- `Use nominal value for silicon (EG=1.11eV)` — 这是默认值。
- `Use nominal value for 4H-SiC silicon carbide (EG=3.23eV)`
- `Use nominal value for 6H-SiC silicon carbide (EG=3.00eV)`
- `Use nominal value for germanium (EG=0.67eV)`
- `Use nominal value for gallium arsenide (EG=1.43eV)`
- `Use nominal value for selenium (EG=1.74eV)`
- `Use nominal value for Schottky barrier diodes (EG=0.69eV)`
- `Specify a custom value` — 如果选择此选项，对话框中会出现 **Energy gap, EG** 参数，以便您为 *EG* 指定自定义值。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Specify the energy gap
EG` 时，此参数才可见。

### **Energy gap, EG** — 能隙 `1.11` `eV`（默认）

为能隙 *EG* 指定自定义值。

#### 依赖关系

仅当为 **Energy gap parameterization** 参数选择 `Specify a custom
value` 时，此参数才可见。

### **Saturation current temperature exponent parameterization** — 饱和电流温度指数参数化 `Use nominal value for pn-junction diode (XTI=3)`（默认）| `Use nominal value for Schottky barrier diode (XTI=2)` | `Specify a custom value`

选择以下选项之一来指定饱和电流温度指数值：

- `Use nominal value for pn-junction diode (XTI=3)` — 这是默认值。
- `Use nominal value for Schottky barrier diode (XTI=2)`
- `Specify a custom value` — 如果选择此选项，对话框中会出现 **Saturation current temperature exponent, XTI** 参数，以便您为 *XTI* 指定自定义值。

### **Saturation current temperature exponent, XTI** — 饱和电流温度指数 `3`（默认）

为饱和电流温度指数 *XTI* 指定自定义值。

#### 依赖关系

仅当为 **Saturation current temperature exponent
parameterization** 参数选择 `Specify a custom
value` 时，此参数才可见。

### **Device simulation temperature** — 器件仿真温度 `25` `°C`（默认）

指定器件仿真温度 *T*s 的值。
## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

光耦作为 LED、电流传感器和受控电流源的行为模型

此模块使用由以下组件组成的模型来表示光耦：

- 输入侧与电流传感器串联的指数发光二极管
- 输出侧的受控电流源

输出侧电流从集电极结流向发射极结。其值为 *CTR*·*Id*，其中 *CTR* 是 **Current transfer ratio** 参数值，*Id* 是二极管电流。

使用 Optocoupler 模块可以在不建立直接电气连接的情况下连接两个电路。这样做的常见原因是两个电路工作在不同的电压水平。

**注意**

每个电路必须有自己的 Electrical Reference 模块。

如果输出电路是光电晶体管，**Current transfer ratio** 参数的典型值为 0.1 到 0.5。如果输出级由达林顿对组成，参数值可能远高于此。**Current transfer ratio** 值也随发光二极管电流变化，但 Photodiode 模块未对此效应建模。

一些制造商提供光耦的最大数据速率。实际上，最大数据速率取决于以下因素：

- 光电二极管的电容和驱动电路的类型
- 光电晶体管的结构及其相关电容

Optocoupler 模块仅允许您定义发光二极管上的电容。您可以使用 **Junction capacitance** 参数在集电极和发射极连接之间添加自己的电容。

Optocoupler 模块允许您对底层二极管的温度依赖性建模。有关详细信息，请参阅 Diode 参考页。

### 热端口

您可以暴露热端口来对生成的热量和器件温度的影响进行建模。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 模块不包含热端口，也不仿真器件中的热量生成。
- `Show thermal port` — 模块包含热端口，允许您对传导损耗生成的热量进行建模。为了提高数值效率，热状态不影响模块的电气行为。

有关使用热端口以及 **Thermal Port** 参数的详细信息，请参阅 Simulating Thermal Effects in Semiconductors。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值来指定模型中变量的预期大小。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
