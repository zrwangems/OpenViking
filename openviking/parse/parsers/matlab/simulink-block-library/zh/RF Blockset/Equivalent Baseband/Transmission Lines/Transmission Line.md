---
type: simulink-block
title: 'Transmission Line'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'transmissionline'
documentation_source_path: 'ref/transmissionline.html'
language: zh-CN
chinese_source: worker-translation
---

# Transmission Line

## 端口

R2025b 中未记录。

## 参数

### 主要

### **Model type** — 传输线模型 `Delay-based and lossless`（默认） | `Delay-based and lossy` | `Lumped parameter L-section` | `Lumped parameter Pi-section` | `Coaxial` | `Coplanar waveguide` | `Microstrip` | `Stripline` | `Two-wire` | `Parallel-plate` | `Equation-based` | `RLCG` | ...

传输线模型的类型，指定为下列之一。

| 传输线类型 | 描述 |
| --- | --- |
| `Delay-based and lossless` | 对具有延迟但无损耗的传输线建模。  基于延迟的传输线 |
| `Delay-based and lossy` – | 对具有延迟和损耗的传输线建模。    基于延迟的有损传输线 |
| `Lumped parameter L-section` | 使用 RLGC L 形节对传输线建模。    R,L,G.C 连接为 L 形节。 |
| `Lumped parameter Pi-section` | 使用 RLGC pi 形节对传输线建模。    R,L,G.C 连接为 Pi 形节。 |
| `Coaxial` | 将传输线建模为同轴传输线。同轴传输线的横截面如下图所示。其物理特性包括内导体半径 *a* 和外导体半径 *b*。    同轴传输线层：内导体、介质、外导体 |
| `Coplanar waveguide` | 将传输线建模为共面波导。共面波导传输线的横截面如下图所示。其物理特性包括导体宽度 *w*、导体厚度 *t*、槽宽度 *s*、基板高度 *d* 和相对介电常数 *ε*。  有和无导体背地平面的共面波导横截面 |
| `Microstrip` | 将传输线建模为标准、嵌入式、倒置式或悬置式微带传输线。标准、嵌入式、倒置式和悬置式微带传输线的横截面如下所示。此类传输线的物理特性包括微带宽度 *w*、微带厚度 *t*、介质厚度 *d* 和相对介电常数 *ε*。    标准、嵌入式、倒置式和悬置式微带传输线的横截面 |
| `Stripline` | 将传输线建模为带状线传输线。带状线传输线的横截面如下图所示。其物理特性包括条带宽度 *w*、条带厚度 *t*、介质厚度 *h* 和相对介电常数 *ε*。    带状线传输线 |
| `Two-wire` | 将传输线建模为双线传输线。双线传输线的横截面如下图所示。其物理特性包括导线半径 *a*、导线中心之间的间隔或物理距离 *S*，以及导线的相对介电常数和相对磁导率。    双线传输线的横截面 |
| `Parallel plate` | 将传输线建模为平行板传输线。平行板传输线的横截面如下图所示。其物理特性包括板宽度 *w* 和板间距 *d*。    平行板传输线的横截面 |
| `Equation based` | 将传输线建模为基于方程的传输线。该传输线可以是有损或无损耗的，被视为二端口线性网络。  基于方程的传输线 |
| `RLCG` | 将传输线建模为 RLCG 传输线。该线路由其频率相关的电阻、电感、电容和电导定义。该传输线可以是有损或无损耗的，被视为二端口线性网络。    RLGC 传输线的横截面 |

### **Transmission delay** — 传输线中的延迟 `4.7e-9 s`（默认） | real scalar | `s` | `ms` | `us` | `ns`

传输线中的延迟，指定为以
`s`、`ms`、
`us` 或 `ns` 表示的 real scalar。

#### 依赖项

要启用此参数，请选择以下之一：

- `Delay-based and lossless`，在
  **Model type** 中。
- `Delay-based and lossy`，在
  **Model type** 中。

### **Characteristic impedance** — 传输线的阻抗 `50 ohm`（默认） | real scalar | `Ohm` | `kOhm` | `MOhm` | `GOhm`

传输线的阻抗，指定为以
`Ohm`、`kOhm`、
`MOhm` 或
`GOhm` 表示的 real scalar。

#### 依赖项

要启用此参数，请选择以下之一：

- `Delay-based and lossless`、
  `Delay-based and lossy` 或
  `Equation-based`，在
  **Model type** 中。
- `Lumped parameter L-section`
  或 `Lumped parameter
  Pi-section`，在 **Model
  type** 中，并且 `By characterisitc
  impedance and capacitance`，在
  **Parameterization** 中。

### **Resistance per unit length** — 传输线的单位长度电阻 `0.3 Ohm/m`（默认） | positive scalar | `Ohm/m` | `kOhm/m` | `MOhm/m` | `GOhm/m`

传输线的单位长度电阻，指定为以
`Ohm/m`、
`kOhm/m`、
`MOhm/m` 或
`GOhm/m` 表示的 positive scalar。

#### 依赖项

要启用此参数，请选择以下之一：

- `Delay-based and lossy` 或
  `RLCG`，在 **Model
  type** 中。
- `Lumped parameter L-section`
  或 `Lumped parameter
  Pi-section`，在 **Model
  type** 中，并且 `By characterisitc
  impedance and capacitance`，在
  **Parameterization** 中。

### **Number of segments** — 传输线中的段数 `10`（默认） | positive scalar

传输线中的段数，指定为 positive
scalar。

#### 依赖项

要启用此参数，请选择以下之一：

- `Delay-based and lossy`，在
  **Model type** 中。
- `Lumped parameter L-section`
  或 `Lumped parameter
  Pi-section`，在 **Model
  type** 中，并且 `By characterisitc
  impedance and capacitance` 或 `By
  inductance and capacitance`，在
  **Parameterization** 中。

### **Parameterization** — 用于对传输线中的段进行建模的参数类型 `By characterisitc impedance and capacitance`（默认） | `By inductance and capacitance`

用于对传输线中的段进行建模的参数类型，指定为
`By characterisitc impedance and capacitance` 或
`By inductance and capacitance`。

#### 依赖项

要启用此参数，请在 **Model type** 中选择 `Lumped parameter L-section` 或 `Lumped parameter Pi-section`。

### **Capacitance per unit length** — 传输线的单位长度电容 `94e-12 F/m`（默认） | positive scalar

传输线的单位长度电容，指定为以
`F/m`、
`mF/m`、`uF/m`、
`nF/m` 或
`pF/m` 表示的 positive scalar。

#### 依赖项

要启用此参数，请在 **Model type** 中选择 `Lumped parameter L-section`、`Lumped parameter Pi-section` 或 `RLCG`。

### **Conductance per unit length** — 传输线的单位长度电导 `5e-6 S/m`（默认） | positive scalar | `S/m` | `mS/m` | `uS/m` | `nS/m`

传输线的单位长度电导，指定为以
`S/m`、
`mS/m`、`uS/m` 或
`nS/m` 表示的 positive scalar。

#### 依赖项

要启用此参数，请在 **Model type** 中选择 `Lumped parameter L-section`、`Lumped parameter Pi-section` 或 `RLCG`。

### **Inductance per unit length** — 传输线的单位长度电感 `235e-9 H/m`（默认） | positive scalar | `H/m` | `mH/m` | `uH/m` | `nH/m`

传输线的单位长度电感，指定为以
`H/m`、
`mH/m`、`uH/m` 或
`nH/m` 表示的 positive scalar。

#### 依赖项

要启用此参数，请选择以下之一：

- `Lumped parameter L-section`
  或 `Lumped parameter
  Pi-section`，在 **Model
  type** 中，并且 `By inductance and
  capacitance`，在
  **Parameterization** 中。
- `RLCG`，在 **Model
  type** 中

### **Outer radius** — 同轴传输线的外半径 `2.57 mm`（默认） | positive scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

同轴传输线的外半径，指定为以
`m`、`cm`、
`mm`、`um`、
`in` 或
`ft` 表示的 positive scalar。

#### 依赖项

要启用此参数，请在 **Model type** 中选择 `Coaxial`。

### **Inner radius** — 同轴传输线的内半径 `2.57 mm`（默认） | positive scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

同轴传输线的内半径，指定为以
`m`、`cm`、
`mm`、`um`、
`in` 或
`ft` 表示的 positive scalar。

#### 依赖项

要启用此参数，请在 **Model type** 中选择 `Coaxial`。

### **Conductor width** — 导体的物理宽度 `0.6 mm`（默认） | positive scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

导体的物理宽度，指定为以
`m`、`cm`、
`mm`、`um`、
`in` 或
`ft` 表示的 positive scalar。

#### 依赖项

要启用此参数，请在 **Model type** 中选择 `Coplanar waveguide`。

### **Slot width** — 槽的物理宽度 `0.2 mm`（默认） | positive scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

槽的物理宽度，指定为以
`m`、`cm`、
`mm`、`um`、
`in` 或
`ft` 表示的 positive scalar。

#### 依赖项

要启用此参数，请在 **Model type** 中选择 `Coplanar waveguide`。

### **Conductor backed** — 无限底部导体 `off`（默认） | `on`

选择此参数可向共面波导传输线添加无限底部导体。

#### 依赖项

要启用此参数，请将 **Model type** 设置为 `Coplanar waveguide`。

### **Structure** — 微带传输线的类型 `Standard`（默认） | `Embedded` | `Inverted` | `Suspended`

微带传输线的类型，指定为 Standard、Embedded、Inverted 或 Suspended。

#### 依赖项

要启用此参数，请将 **Model type** 设置为 `Microstrip`。

### **Strip Width** — 微带传输线的宽度 `0.6 mm`（默认） | positive scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

微带传输线的宽度，指定为以
`m`、`cm`、
`mm`、`um`、
`in` 或
`ft` 表示的 positive scalar。

#### 依赖项

要启用此参数，请将 **Model type** 设置为`Microstrip`。

### **Strip thickness** — 导体的物理厚度 `5 um`（默认） | nonnegative scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

导体的物理厚度，指定为以
`m`、`cm`、
`mm`、`um`、
`in` 或
`ft` 表示的 nonnegative scalar。

#### 依赖项

要启用此参数，请在 **Model type** 中选择 `Coplanar waveguide` 或 `Microstrip`。

### **Strip Height** — 微带传输线的条带高度 `0.635 mm`（默认） | positive scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

倒置、悬置或嵌入微带传输线的条带高度，指定为以
`m`、`cm`、
`mm`、`um`、
`in` 或
`ft` 表示的 positive scalar。

#### 依赖项

要启用此参数，请在 **Model type** 中选择 `Microstrip`，并在 **Structure** 中选择 `Inverted`、`Suspended` 或 `Embedded`。

### **Wire radius** — 双线传输线的导线半径 `0.67 mm`（默认） | positive scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

双线传输线的导线半径，指定为以
`m`、
`cm`、`mm`、
`um`、`in` 或
`ft` 表示的 positive scalar。

#### 依赖项

要启用此参数，请在 **Model type** 中选择 `Two-wire`。

### **Wire separation** — 双线传输线的导线之间的物理距离 `1.62 mm`（默认） | positive scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

双线传输线的导线之间的物理距离，指定为以
`m`、`cm`、
`mm`、`um`、
`in` 或
`ft` 表示的 positive scalar。

#### 依赖项

要启用此参数，请在 **Model type** 中选择 `Two-wire`。

### **Plate width** — 平行板传输线的宽度 `5 mm`（默认） | positive scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

平行板传输线的宽度，指定为以
`m`、`cm`、
`mm`、`um`、
`in` 或
`ft` 表示的 positive scalar。

#### 依赖项

要启用此参数，请在 **Model type** 中选择 `Parallel-plate`。

### **Plate separation** — 分隔板的介质厚度 `1 mm`（默认） | positive scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

分隔板的介质厚度，指定为以
`m`、
`cm`、`mm`、
`um`、`in` 或
`ft` 表示的 positive scalar。

#### 依赖项

要启用此参数，请在 **Model type** 中选择 `Parallel-plate`。

### **Phase velocity (m/s)** — 传输线上均匀平面波的传播速度 `299792458`（默认） | positive scalar

传输线上均匀平面波的传播速度，指定为以 meters per second 表示的 positive scalar。

#### 依赖项

要启用此参数，请在 **Model type** 中选择 `Equation-based`。

### **Loss (dB/m)** — 信号沿传输线传播时的强度降低 `0`（默认） | positive scalar

信号沿传输线传播时的强度降低，指定为以 meters per second 表示的 positive scalar。

#### 依赖项

要启用此参数，请在 **Model type** 中选择 `Equation-based`。

### **Frequency** — 建模频率 `1e9 Hz`（默认） | positive scalar | `Hz` | `kHz` | `MHz` | `GHz`

建模频率，指定为以
`Hz`、`kHz`、
`MHz` 或
`GHz` 表示的 positive scalar 或 vector。

#### 依赖项

要启用此参数，请在 **Model type** 中选择 `Equation-based` 或 `RLCG`。

### **Interpolation method** — 用于在建模频率处计算值的插值方法 `Linear`（默认） | `Spline` | `Cubic`

用于在建模频率处计算值的插值方法，指定为 `Linear`、`Spline` 或 `Cubic`。

#### 依赖项

要启用此参数，请在 **Model type** 中选择 `Equation-based` 或 `RLCG`。

### **Conductivity of conductor** — 导体的电导率 `inf`（默认） | scalar | `S/m` | `mS/m` | `uS/m` | `nS/m`

导体的电导率，指定为以
`S/m`、`mS/m`、
`uS/m` 或
`nS/m` 表示的 scalar。

#### 依赖项

要启用此参数，请在 **Model type** 中选择 `Coaxial`、`Coplanar waveguide`、`Microstrip`、`Two-wire` 或 `Parallel-plate`。

### **Dielectric Thickness** — 导体所在介质的厚度 `0.635 mm`（默认） | positive scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

导体所在介质的厚度，指定为以
`m`、`cm`、
`mm`、`um`、
`in` 或
`ft` 表示的 positive scalar。

共面波导以及标准、嵌入、倒置和悬置微带传输线的介质厚度默认值列于下表中。

| 模型类型 | 结构 | 默认介质厚度（mm） |
| --- | --- | --- |
| `Coplanar waveguide` | N.A. | `0.635` |
| `Microstrip` | `Standard` and `Inverted` | `0.635` |
| `'Suspended'` | `0.3175` |
| `'Embedded'` | `1.37` |

#### 依赖项

要启用此参数，请将 **Model type** 设置为 `Microstrip` 或 `Coplanar waveguide`。

### **Relative permeability of dielectric** — 介质的相对磁导率 `1`（默认） | scalar

介质的相对磁导率，指定为 scalar。

#### 依赖项

要启用此参数，请将 **Model type** 设置为 `Coaxial`、`Two-wire` 或 `Parallel-plate`。

### **Relative permittivity of dielectric** — 介质的相对介电常数 `2.2`（默认） | scalar

介质的相对介电常数，指定为 scalar。

#### 依赖项

要启用此参数，请将 **Model type** 设置为 `Coaxial`、`Coplanar waveguide`、`Microstrip`、`Two-wire` 或 `Parallel-plate`。

### **Loss tangent of dielectric** — 介质的损耗角正切 `0`（默认） | scalar

介质的损耗角正切，指定为 scalar。

#### 依赖项

要启用此参数，请将 **Model type** 设置为 `Coaxial`、`Coplanar waveguide`、`Microstrip`、`Two-wire` 或 `Parallel-plate`。

### **Line length** — 传输线的物理长度 `1 cm`（默认） | positive scalar | `m` | `cm` | `mm` | `um` | `in` | `ft`

传输线的物理长度或 *l*，指定为以 `m`、
`cm`、`mm`、
`um`、`in` 或
`ft` 表示的 positive scalar。

#### 依赖项

要启用此参数，请选择以下项之一：

- `Delay-based and lossy`、
  `Coaxial`、
  `Coplanar waveguide`、
  `Microstrip`，或
  `Two-wire`、
  `Parallel-plate`、
  `Equation-based`，或
  `RLCG` 在 **Model type** 中。
- `Lumped parameter L-section`
  或 `Lumped parameter Pi-section` 在 **Model type** 中，以及 `By characterisitc impedance and capacitance` 或 `By inductance and capacitance` 在 **Parameterization** 中。

### **Stub mode** — 短截线类型 `Not a stub`（默认）| `Shunt` | `Series`

短截线类型，指定为 `Not a stub`、`Shunt` 或 `Series`。请参见 Parameter Calculations for Transmission Line with Stub。

#### 依赖项

要启用此参数，请在 **Model type** 中选择
`Coaxial`、`Coplanar waveguide`、`Microstrip`、`Two-wire`、
`Parallel-plate`、
`Equation-based` 或
`RLCG`。

### **Termination of stub** — 短截线的终接类型 `Open`（默认）| `Short`

短截线的终接类型，指定为
`Open` 或
`Short`。

#### 依赖项

要启用此参数，请在 **Stub mode** 中选择 `Series`
或 `Shunt`。

### **Ground and hide negative terminals** — 将 RF 电路端子接地 `on`（默认）| `off`

选择此参数可在内部将负端子接地并隐藏。要暴露负端子，请清除此参数。通过暴露这些端子，您可以将它们连接到模型的其他部分。

默认情况下，此选项处于选中状态。

### 建模

### **Modeling Options** — 对 S 参数建模的选项 `Frequency domain`（默认）| `Time domain`

对 S 参数建模的选项，指定为：

- `Frequency domain` – 独立计算每个载波频率的基带冲激响应。此技术基于卷积。可以选择指定冲激响应的持续时间。有关详细信息，请参阅 Compare Time and Frequency Domain Simulation Options for S-parameters。
- `Time domain` – 计算可近似整个数据范围的分析有理模型。

对于 Amplifier、Antenna 和 S-Parameters 模块，默认值为 `Time domain`。对于 Transmission Line 模块，默认值为 `Frequency domain`。

### **Automatically estimate impulse response duration** — 自动计算冲激响应持续时间 `off`（默认）| `on`

选择 **Automatically estimate impulse response duration** 可自动计算冲激响应持续时间。清除该选择可指定冲激响应持续时间。

#### 依赖项

要启用此参数，请在 **Modeling options** 中选择 `Frequency domain`。

### **Impulse response duration** — 手动指定冲激响应持续时间 `0 s`（默认）| 正标量 | `s` | `ms` | `us` | `ns`

手动指定冲激响应持续时间，指定为以 `s`、`ms`、`us` 或 `ns` 为单位的正标量。

#### 依赖项

要启用此参数，请清除 **Automatically estimate impulse response duration**。

### **Fitting options** — 用于 rationalfit 的拟合选项 `Share all poles`（默认）| `Share poles by columns` | `Fit individually`

用于 rationalfit 的拟合选项，指定为 `Share all poles`、`Share poles by columns` 或 `Fit individually`。

对于 Amplifier 模块，默认值为 `Fit individually`。对于 S-parameters 模块和 Transmission Line 模块，默认值为 `Share all poles`。

#### 依赖项

要启用此参数，请在 **Modeling options** 中选择 `Time domain`。

### **Relative error desired (dB)** — 有理拟合输出中可接受的相对误差 `-40`（默认）| 实标量

有理拟合输出中可接受的相对误差，指定为以分贝为单位的实标量。

#### 依赖项

要启用此参数，请在 **Modeling options** 中选择 `Time domain`。

### **Rational fitting results** — rationalfit 计算的值，只读（默认）

显示 **Number of independent fits**、**Number of required poles** 和 **Relative error achieved (dB)** 的值。

使用 `Time domain` 建模时，`Visualization` 选项卡中的 **Plot** 会绘制 `Data Source` 中定义的数据以及 `rationalfit` 函数中的值。

#### 依赖项

要启用此参数，请在 **Modeling options** 中选择 `Time domain`。

**注意**

对于除 `Delay-based and lossless`、`Delay-based and lossy`、`Lumped parameter L-section` 和 `Lumped parameter pi-section` 之外的所有传输线类型，Modeling 选项卡均启用。

## 所属库

RF Blockset / Circuit Envelope / Elements

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2012a 中引入**

### R2024b：`Time domain (rationalfit)` 参数已重命名

Transmission Line 模块中 **Modeling options** 参数内的 `Time domain (rationalfit)` 参数值已重命名为 `Time domain`。

当打开在 R2024b 之前创建且包含 Transmission Line 模块的模型时，参数名显示为 `Time domain`。

### R2022a：三个模块参数已重命名

Transmission Line 模块中的 **Substrate height**、**Relative permittivity constant** 和 **Relative permeability constant** 参数已分别重命名为 **Dielectric thickness**、**Relative permittivity of dielectric** 和 **Relative permeability of dielectric**。

当打开在 R2022a 之前创建且包含 Transmission Line 模块的模型时，软件会用新参数名替换旧参数名。

### R2022a：对传输线建模

使用 Transmission Line 模块对以下项建模：

- 嵌入式、倒置式和悬置式微带传输线
- 导体背衬共面波导传输线
- 带状线传输线

## 描述

对传输线建模

使用 Transmission Line 模块对基于延迟的、集总和分布传输线进行建模。Mask 对话框选项会自动更改以适配所选的模型类型。
