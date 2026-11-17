---
type: simulink-block
title: 'SPICE NMOS'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Semiconductors'
documentation_page: 'spicenmos'
documentation_source_path: 'ref/spicenmos.html'
language: zh-CN
chinese_source: worker-translation
---

# SPICE NMOS

## 端口

### 守恒端口

### **gx** — 栅极端子电气端口

与晶体管栅极端子关联的电气守恒端口。

### **dx** — 漏极端子电气端口

与晶体管漏极端子关联的电气守恒端口。

### **sx** — 源极端子电气端口

与晶体管源极端子关联的电气守恒端口。

### **bx** — 体极端子电气端口

与晶体管体极端子关联的电气守恒端口。

## 参数

### 模型选择

### **MOS model** — 漏极电流模型 `Level 1 MOS`（默认）| `Level 3 MOS`

MOSFET 漏极电流模型选项：

- `Level 1 MOS` — 使用 Level 1 漏极电流模型。这是默认选项。
- `Level 3 MOS` — 使用 Level 3 漏极电流模型。

#### 依赖关系

为 **MOS model** 选择的设置会影响 **DC Currents** 和 **Process** 设置中某些参数的可见性。

### 尺寸

### **Device area factor, AREA** — 器件面积 `1.0`（默认）| 正标量

用于缩放的晶体管面积因子。该值必须大于 `0`。

### **Number of parallel devices, SCALE** — 并联器件数 `1`（默认）| 正整数

该模块所代表的并联 MOS 实例数。此参数会乘以输出电流和器件电荷。该值必须大于 `0`。

### **Length of channel, LENGTH** — 源到漏沟道长度 `1e-4` `m`（默认）| 正标量

源极与漏极之间的沟道长度。

### **Width of channel, WIDTH** — 源到漏沟道宽度 `1e-4` `m`（默认）| 正标量

源极与漏极之间的沟道宽度。

### **Area of drain, AD** — 漏极面积 `0` `m^2`（默认）| 非负标量

晶体管漏极扩散区面积。该值必须大于或等于 `0`。

### **Area of source, AS** — 源极面积 `0` `m^2`（默认）| 非负标量

晶体管源极扩散区面积。该值必须大于或等于 `0`。

### **Perimeter of drain, PD** — 漏极周长 `0` `m`（默认）| 非负标量

晶体管漏极扩散区周长。该值必须大于或等于 `0`。

### **Perimeter of source, PS** — 源极周长 `0` `m`（默认）| 非负标量

晶体管源极扩散区周长。该值必须大于或等于 `0`。

### 电阻

### **Number of drain squares, NRD** — 漏极扩散电阻方数 `0`（默认）| 非负标量

构成晶体管漏极扩散区的电阻方数。该值必须大于或等于 `0`。仅当您未指定 **Drain resistance, RD** 和 **Source resistance, RS** 参数值中的一个或两个时，该模块才会使用此参数值，如参数计算中所述。

### **Number of source squares, NRS** — 晶体管源极扩散电阻方数 `1`（默认）| 非负标量

构成晶体管源极扩散区的电阻方数。该值必须大于或等于 `0`。仅当您未指定 **Drain resistance, RD** 和 **Source resistance, RS** 参数值中的一个或两个时，该模块才会使用此参数值，如参数计算中所述。

### **Drain resistance, RD** — 串联电阻 `0` `Ohm`（默认）| 非负标量

晶体管漏极电阻。该值必须大于或等于 `0`。

### **Source resistance, RS** — 串联电阻 `0` `Ohm`（默认）| 非负标量

晶体管源极电阻。该值必须大于或等于 `0`。

### **Sheet resistance, RSH** — 每方电阻 `0` `Ohm`（默认）| 非负标量

晶体管源极和漏极的每方电阻。请查看参数计算以了解该模块何时使用此参数。该值必须大于或等于 `0`。

### 直流电流

### **Threshold voltage, VTO** — 阈值电压 `0` `V`（默认）| 标量

晶体管产生非零漏极电流时的栅源电压。如果将此参数赋值为 `NaN`，该模块将根据 **Oxide thickness, TOX** 和 **Substrate doping, NSUB** 参数的指定值计算该值。有关此计算的更多信息，请参阅温度依赖性。

### **Transconductance, KP** — 跨导 `2e-5` `A/V^2`（默认）| 非负标量

漏极电流对栅极电压的导数。该值必须大于或等于 `0`。如果将此参数赋值为 `NaN`，该模块将根据 **Oxide thickness, TOX** 和 **Substrate doping, NSUB** 参数的指定值计算该值。有关此计算的更多信息，请根据 **MOS model** 参数的选定值参阅 Level 1 漏极电流模型或 Level 3 漏极电流模型。

### **Bulk threshold, GAMMA** — 体阈值 `0` `V^0.50000`（默认）| 非负标量

体效应参数，它将阈值电压 VTH 与体偏置 VBS 关联起来，如 Level 1 漏极电流模型和 Level 3 漏极电流模型中所述。该值必须大于或等于 `0`。如果将此参数赋值为 `NaN`，该模块将根据 **Oxide thickness, TOX** 和 **Substrate doping, NSUB** 参数的指定值计算该值。有关此计算的更多信息，请根据 **MOS model** 参数的选定值参阅 Level 1 漏极电流模型或 Level 3 漏极电流模型。

### **Surface potential, PHI** — 表面电势 `0.6` `V`（默认）| 非负标量

表面电子浓度等于本征浓度且器件在耗尽与反型条件之间过渡时的电压的两倍。该值必须大于或等于 `0`。如果将此参数赋值为 `NaN`，该模块将根据 **Oxide thickness, TOX** 和 **Substrate doping, NSUB** 参数的指定值计算该值。有关此计算的更多信息，请根据 **MOS model** 参数的选定值参阅 Level 1 漏极电流模型或 Level 3 漏极电流模型。

### **Channel modulation, LAMBDA** — 沟道长度调制 `0` `1/V`（默认）| 标量

沟道长度调制。

#### 依赖关系

仅当您在 **Model Selection** 设置中为 **MOS model** 参数选择 `Level 1 MOS` 时，此参数才可见。

### **Bulk saturation current, IS** — 体饱和电流幅值 `1e-14` `A`（默认）| 非负标量

在非常大的反向偏置水平下，结渐近趋近的电流幅值。该值必须大于或等于 `0`。

### **Emission coefficient, N** — 发射系数 `1`（默认）| 非负标量

晶体管发射系数或理想因子。该值必须大于 `0`。

### **Bulk jct sat current density, JS** — 体结饱和电流密度 `0` `A/m^2`（默认）| 非负标量

在非常大的反向偏置水平下，结每单位面积渐近趋近的电流幅值。该值必须大于或等于 `0`。

### **Width effect on threshold, DELTA** — 宽度因子 `0`（默认）| 标量

控制晶体管宽度对阈值电压影响的因子。

#### 依赖关系

仅当您在 **Model Selection** 设置中为 **MOS model** 参数选择 `Level 3 MOS` 时，此参数才可见。

### **Max carrier drift velocity, VMAX** — 最大漂移速度 `0` `m/s`（默认）| 标量

载流子的最大漂移速度。

#### 依赖关系

仅当您在 **Model Selection** 设置中为 **MOS model** 参数选择 `Level 3 MOS` 时，此参数才可见。

### **Fast surface state density, NFS** — 快表面态密度 `0` `1/cm^2`（默认）| 标量

快表面态密度根据栅极电压引起的迁移率降低来调整漏极电流。

#### 依赖关系

仅当您在 **Model Selection** 设置中为 **MOS model** 参数选择 `Level 3 MOS` 时，此参数才可见。

### **Vds dependence threshold volt, ETA** — 漏源电压阈值 `0`（默认）| 标量

控制漏极电压如何影响漏极电流计算中迁移率的系数。

#### 依赖关系

仅当您在 **Model Selection** 设置中为 **MOS model** 参数选择 `Level 3 MOS` 时，此参数才可见。

### **Vgs dependence on mobility, THETA** — 迁移率依赖系数 `0` `1/V`（默认）| 标量

控制栅极电压如何影响漏极电流计算中迁移率的系数。

#### 依赖关系

仅当您在 **Model Selection** 设置中为 **MOS model** 参数选择 `Level 3 MOS` 时，此参数才可见。

### **Mobility modulation, KAPPA** — 迁移率调制系数 `0.2`（默认）| 标量

Level 3 MOS 模型的沟道长度调制系数。

#### 依赖关系

仅当您在 **Model Selection** 设置中为 **MOS model** 参数选择 `Level 3 MOS` 时，此参数才可见。

### C-V

### **Model gate capacitance (CGS, CGD, CGB)** — 栅极电容模型 `No intrinsic capacitance`（默认）| `Meyer gate capacitances` | `Charge conservation capacitances`

栅极电容建模选项：

- `No intrinsic capacitance` — 不在模型中包含栅极电容。
- `Meyer gate capacitances` —
- `Charge conservation capacitances` —

### **Model gate overlap capacitance (CGSO, CGDO, CGBO)** — 栅极重叠模型 `No`（默认）| `Yes`

栅极重叠电容建模选项：

- `No` — 不在模型中包含栅极重叠电容。
- `Yes` — 指定栅源、栅漏和栅体电容。

#### 依赖关系

选择 `Yes` 会显示相关参数。

### **G-S overlap capacitance, CGSO** — 栅源重叠电容 `0` `F/m`（默认）| 标量 | `0` 或 ≥ `1e-18`

由于源极横向扩散产生的栅源电容。该值必须等于 `0` 或大于或等于 *Cmin*。*Cmin* 是内置模型常数，其值为 `1e-18`。

#### 依赖关系

仅当您为 **Model gate overlap capacitance (CGSO, CGDO, CGBO)** 参数选择 `Yes` 时，此参数才可见。

### **G-D overlap capacitance, CGDO** — 栅漏重叠电容 `0` `F/m`（默认）| 标量 | `0` 或 ≥ `1e-18`

由于漏极横向扩散产生的栅漏电容。该值必须等于 `0` 或大于或等于 *Cmin*。*Cmin* 是内置模型常数，其值为 `1e-18`。

#### 依赖关系

仅当您为 **Model gate overlap capacitance (CGSO, CGDO, CGBO)** 参数选择 `Yes` 时，此参数才可见。

### **G-B overlap capacitance, CGBO** — 栅体重叠电容 `0` `F/m`（默认）| 标量 | `0` 或 ≥ `1e-18`

由于栅极延伸超出沟道宽度产生的栅体电容。该值必须等于 `0` 或大于或等于 *Cmin*。*Cmin* 是内置模型常数，其值为 `1e-18`。

#### 依赖关系

仅当您为 **Model gate overlap capacitance (CGSO, CGDO, CGBO)** 参数选择 `Yes` 时，此参数才可见。

### **Model junction capacitance (CBD, CBS)** — 结电容模型 `No`（默认）| `Yes`

结电容建模选项：

- `No` — 不在模型中包含结电容。
- `Yes` — 指定零偏结电容、结电势、梯度系数、正向偏置耗尽和电容系数。

#### 依赖关系

选择 `Yes` 会显示相关参数。

### **Zero-bias BD capacitance, CBD** — 零偏结电容 `0` `F`（默认）| `0` 或 ≥ `1e-18`

体极与漏极之间的电容。该值必须等于 `0` 或大于或等于 *Cmin*。*Cmin* 是内置模型常数，其值为 `1e-18`。

#### 依赖关系

仅当您为 **Model junction capacitance (CBD, CBS)** 参数选择 `Yes` 时，此参数才可见。

### **Zero-bias BS capacitance, CBS** — 零偏体源电容 `0` `F`（默认）| 标量 | `0` 或 ≥ `1e-18`

体极与源极之间的电容。该值必须等于 `0` 或大于或等于 *Cmin*。*Cmin* 是内置模型常数，其值为 `1e-18`。

#### 依赖关系

仅当您为 **Model junction capacitance (CBD, CBS)** 参数选择 `Yes` 时，此参数才可见。

### **Bulk junction potential, PB** — 体结电势 `0.8` `V`（默认）| 标量 | `0` 或 ≥ `0.01`

体结两端的电势。仅当您为 **Model junction capacitance (CBD, CBS)** 参数选择 `Yes` 时，此参数才可见。该值必须等于 `0` 或大于或等于 *VJmin*。*VJmin* 是内置模型常数，其值为 `0.01`。

#### 依赖关系

仅当您为 **Model junction capacitance (CBD, CBS)** 参数选择 `Yes` 时，此参数才可见。

### **Bottom junction cap per area, CJ** — 每结面积的零偏体结底部电容 `0` `F/m^2`（默认）| 标量 | `0` 或 ≥ `1e-18`

每结面积的零偏体结底部电容。该值必须等于 `0` 或大于或等于 *Cmin*。*Cmin* 是内置模型常数，其值为 `1e-18`。

#### 依赖关系

仅当您为 **Model junction capacitance (CBD, CBS)** 参数选择 `Yes` 时，此参数才可见。

### **Bottom grading coefficient, MJ** — 底部梯度系数 `0.5`（默认）| 标量 | 0 或 < 0.9

晶体管底部梯度系数。该值必须等于 `0` 或小于 *MGmax*。*MGmax* 是内置模型常数，其值为 `0.9`。

#### 依赖关系

仅当您为 **Model junction capacitance (CBD, CBS)** 参数选择 `Yes` 时，此参数才可见。

### **Side jct cap/area of jct perimeter, CJSW** — 每结周长的零偏体结侧壁电容 `0` `F/m`（默认）| 标量 | `0` 或 ≥ `1e-18`

每结周长的零偏体结侧壁电容。该值必须等于 `0` 或大于或等于 *Cmin*。*Cmin* 是内置模型常数，其值为 `1e-18`。

#### 依赖关系

仅当您为 **Model junction capacitance (CBD, CBS)** 参数选择 `Yes` 时，此参数才可见。

### **Side grading coefficient, MJSW** — 侧壁梯度系数 `0.5`（默认）| 标量 | 0 < *MJSW* < 0.9

晶体管侧壁梯度系数。该值必须等于 `0` 或小于 *MGmax*。*MGmax* 是内置模型常数，其值为 `0.9`。

#### 依赖关系

仅当您为 **Model junction capacitance (CBD, CBS)** 参数选择 `Yes` 时，此参数才可见。

### **Capacitance coefficient, FC** — 电容系数 `0.5`（默认）| 0 或 ≤ 0.95 | 标量

量化耗尽电容随施加电压降低的拟合系数。该值必须等于 `0` 或小于或等于 *FCmax*。*FCmax* 是内置模型常数，其值为 `0.95`。

#### 依赖关系

仅当您为 **Model junction capacitance (CBD, CBS)** 参数选择 `Yes` 时，此参数才可见。

### **Specify initial condition** — 初始条件模型 `No`（默认）| `Yes`

初始条件指定选项：

- `No` — 不为模型指定初始条件。
- `Yes` — 指定初始晶体管电压。

  **注意**

  该模块将初始晶体管电压施加在结电容两端，而不是施加在端口两端。

#### 依赖关系

要启用此参数，请设置以下任一项：

- 将 **Model gate capacitance (CGS, CGD, CGB)** 设置为 `No intrinsic capacitance`，并将 **Model gate overlap capacitance (CGSO, CGDO, CGBO)** 和 **Model junction capacitance (CBD, CBS)** 中的任一或两者设置为 `Yes`。
- 将 **Model gate capacitance (CGS, CGD, CGB)** 设置为 `Meyer gate capacitances` 或 `Charge conservation capacitances`。

### **Initial condition voltage, ICVDS** — 初始电压 `0` `V`（默认）| 标量

仿真开始时的漏源电压。

#### 依赖关系

此参数仅在将 **Specify initial condition** 参数选择为 `Yes` 时可见。

### **Initial condition voltage, ICVGS** — 初始电压 `0` `V`（默认）| 标量

仿真开始时的栅源电压。

#### 依赖关系

此参数仅在将 **Specify initial condition** 参数选择为 `Yes` 时可见。

### **Initial condition voltage, ICVBS** — 初始电压 `0` `V`（默认）| 标量

仿真开始时的体源电压。

#### 依赖关系

此参数仅在将 **Specify initial condition** 参数选择为 `Yes` 时可见。

### 工艺

### **Oxide thickness, TOX** — 栅氧化层厚度 `1e-7` `m`（默认）| 非负标量

栅氧化层的厚度。该值必须大于或等于 `0`。

### **Lateral diffusion, LD** — 横向扩散长度 `0` `m`（默认）| 标量

横向扩散长度。

### **Surface mobility, U0** — 零偏置表面迁移率系数 `600` `cm^2/s/V`（默认）

零偏置表面迁移率系数。

### **Substrate doping, NSUB** — 衬底掺杂 `NaN` `1/cm^3`（默认）| 标量 ≥ `1.45e10`

衬底掺杂。该值必须大于或等于 `1.45e10`（本征硅的载流子浓度）。

### **Gate type, TPG** — 栅极类型 `Opposite of substrate (1)`（默认）| `Same as substrate (-1)` | `Aluminum (0)`

MOSFET 栅极材料（相对于衬底）：

- `Opposite of substrate` — 栅极材料与衬底相反。这意味着在器件方程中 TPG = 1。这是默认选项。
- `Same as substrate` — 栅极材料与衬底相同。这意味着在器件方程中 TPG = –1。

- `Aluminum` — 栅极材料为铝。这意味着在器件方程中 TPG = 0。

### **Surface state density, NSS** — 表面态密度 `NaN` `1/cm^2`（默认）| 标量

表面态密度。

### **Junction depth, XJ** — 结深 `0``m`（默认）

结深。

#### 依赖关系

此参数仅在 **Model Selection** 设置中将 **MOS model** 参数选择为 `Level 3 MOS` 时可见。

### 温度

### **Model temperature dependence using** — 温度依赖性模型 `Device temperature`（默认）| `Fixed temperature`

选择以下选项之一来建模晶体管温度依赖性：

- `Device temperature` — 使用器件温度来建模温度依赖性。
- `Fixed temperature` — 使用独立于电路温度的温度来建模温度依赖性。

有关详细信息，请参阅温度依赖性。

#### 依赖关系

选择 `Device temperature` 会显示 **Offset local circuit temperature, TOFFSET** 参数。选择 `Fixed temperature` 会显示 **Fixed circuit temperature, TFIXED** 参数。

### **Fixed circuit temperature, TFIXED** — 固定电路温度 `300.15` `K`（默认）| 正标量

晶体管仿真温度。该值必须大于 `0` `K`。

#### 依赖关系

此参数仅在将 **Model temperature dependence using** 参数选择为 `Fixed temperature` 时可见。

### **Parameter extraction temperature, TMEAS** — 参数提取温度 `300.15` `K`（默认）| 正标量

测量晶体管参数时的温度。该值必须大于 `0` `K`。

### **Offset local circuit temperature, TOFFSET** — 局部电路温度偏移 `0` `K`（默认）| 标量

晶体管温度与电路温度之间的差值。

#### 依赖关系

此参数仅在将 **Model temperature dependence using** 参数选择为 `Device temperature` 时可见。

## 所属库

Simscape / Electrical / Additional Components / SPICE Semiconductors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中引入**

## 描述

SPICE 兼容的 N 沟道 MOSFET

SPICE NMOS 模块表示一个 SPICE 兼容的负沟道（N 沟道）金属氧化物半导体（MOS）场效应晶体管（FET）。如果栅源电压增加，沟道电导增加。如果栅源电压减小，沟道电导减小。

SPICE（Simulation Program with Integrated Circuit Emphasis）是一种电子电路仿真工具。您可以使用 Environment Parameters 模块和 Additional Components 库中的 SPICE 兼容模块，将一些 SPICE 子电路转换为等效的 Simscape™ Electrical™ 模型。有关详细信息，请参阅 `subcircuit2ssc`。

### 方程变量

SPICE NMOS 模块方程的变量包括：

- 通过为 SPICE NMOS 模块指定参数来定义的变量。某些参数的可见性取决于您为其他参数设置的值。有关详细信息，请参阅参数。
- 几何调整变量，取决于您使用 SPICE NMOS 模块参数指定的若干值。有关详细信息，请参阅几何调整变量。
- 温度 *T*，默认为 `300.15` `K`。您可以通过为 SPICE NMOS 模块指定参数，或同时为 SPICE NMOS 模块和 Environment Parameters 模块指定参数来使用不同的值。有关详细信息，请参阅晶体管温度。
- 最小电导 *GMIN*，默认为 `1e-12` `1/Ohm`。您可以通过为 Environment Parameters 模块指定参数来使用不同的值。有关详细信息，请参阅最小导通。
- 热电压 *Vtn*。有关详细信息，请参阅热电压。

**几何调整变量**

SPICE N 沟道 MOSFET 模型方程中的若干变量考虑了模块所表示器件的几何结构。这些几何调整变量取决于您通过指定 SPICE NMOS 模块参数来定义的变量。几何调整变量取决于以下变量：

- *AREA* — 器件面积
- *SCALE* — 并联连接的器件数量
- 相关的未调整变量

下表列出了几何调整变量及其定义方程。

| 变量 | 描述 | 方程 |
| --- | --- | --- |
| *KPd* | 几何调整跨导 | KPd=KP\*AREA\*SCALE |
| *ISd* | 几何调整体饱和电流 | ISd=IS\*AREA\*SCALE |
| *JSd* | 几何调整体结饱和电流密度 | JSd=JS\*AREA\*SCALE |
| *CBDd* | 几何调整零偏置体漏电容 | CBDd=CBD\*AREA\*SCALE |
| *CBSd* | 几何调整零偏置体源电容 | CBSd=CBS\*AREA\*SCALE |
| *CGSOd* | 几何调整栅源重叠电容 | CGSOd=CGSO\*AREA\*SCALE |
| *CGDOd* | 几何调整栅漏重叠电容 | CGDOd=CGDO\*AREA\*SCALE |
| *CGBOd* | 几何调整栅体重叠电容 | CGBOd=CGBO\*AREA\*SCALE |
| *CJ* | 几何调整每结面积底部电容 | CJd=CJ\*AREA\*SCALE |
| *CJSW* | 几何调整每结周长侧壁电容 | CJSWd=CJSW\*AREA\*SCALE |
| *RDd* | 几何调整漏电阻 | RDd=RDAREA\*SCALE |
| *RSd* | 几何调整源电阻 | RSd=RSAREA\*SCALE |
| *RSHd* | 几何调整薄层电阻 | RSHd=RSHAREA\*SCALE |

**晶体管温度**

定义晶体管温度 *T* 有两种不同的选项：

- 固定温度 — 当 SPICE NMOS 模块的 **Temperature** 设置中的 **Model temperature dependence using** 参数设置为 `Fixed temperature` 时，模块使用独立于电路温度的温度。对于此模型，模块将 *T* 设置为等于 *TFIXED*。
- 器件温度 — 当 SPICE NMOS 模块的 **Temperature** 设置中的 **Model temperature dependence using** 参数设置为 `Device temperature` 时，模块使用取决于电路温度的温度。对于此模型，模块将温度定义为

  T=TC+TOFFSET

  其中：

  - *TC* 是电路温度。

    如果电路中没有 Environment Parameters 模块，则 *TC* 等于 300.15 K。

    如果电路中有 Environment Parameters 模块，则 *TC* 等于您在 Environment Parameters 模块的 **SPICE** 设置中为 **Temperature** 参数指定的值。**Temperature** 参数的默认值为 `300.15` `K`。
  - *TOFFSET* 是局部电路温度偏移。

**最小导通**

最小电导 *GMIN* 的默认值为 `1e–12` `1/Ohm`。要指定不同的值：

1. 如果电路中还没有 Environment Parameters 模块，请添加一个。
2. 在 Environment Parameters 模块的 **SPICE** 设置中，为 **GMIN** 参数指定所需的 *GMIN* 值。

**热电压**

*Vtn* 是热电压，定义为

Vtn=Nk\*Tq

其中：

- *N* 是发射系数。
- *T* 是晶体管温度。有关详细信息，请参阅晶体管温度。
- *k* 是玻尔兹曼常数。
- *q* 是电子的基本电荷。

### 参数计算

下表显示了 SPICE NMOS 模块如何根据您指定的值确定其某些参数。

**漏电阻**

| 参数值 | | | 几何调整晶体管漏电阻 |
| --- | --- | --- | --- |
| **Drain resistance, RD** | **Sheet resistance, RSH** | **Number of drain squares, NRD** |
| `NaN` | `NaN` | `NaN` | 0 |
| `NaN` | *RSH* | `NaN` | 0 |
| `NaN` | `NaN` | *NRD* | 0 |
| *RD* | `NaN` 或 *RSH* | `NaN` 或 *NRD* | *RDd* |
| `NaN` | *RSH* | *NRD* | *RSHd*\**NRD* |

**源电阻**

| 参数值 | | | 几何调整晶体管源电阻 |
| --- | --- | --- | --- |
| **Source resistance, RS** | **Sheet resistance, RSH** | **Number of source squares, NRS** |
| `NaN` | `NaN` | `NaN` | 0 |
| `NaN` | *RSH* | `NaN` | 0 |
| `NaN` | `NaN` | *NRS* | 0 |
| *RS* | `NaN` 或 *RSH* | `NaN` 或 *NRS* | *RSd* |
| `NaN` | *RSH* | *NRS* | *RSHd*\**NRS* |

**跨导和表面迁移率**

| 参数值 | | | 几何调整跨导（level 1），单位 A/V2 | 几何调整跨导（level 3），单位 A/V2 | 表面迁移率（level 3），单位 cm2/s/V |
| --- | --- | --- | --- | --- | --- |
| **Oxide thickness, TOX** | **Surface mobility, U0** | **Transconductance, KP** |
| `NaN` | `NaN` | `NaN` | `2e-5`（默认值） | `2e-5`（默认值） | `600`（默认值） |
| `NaN` | `NaN` | `KP` | `KPd` | `KPd` | `600` |
| `NaN` | `U0` | `NaN` | `2e-5` | *UO*\**EPXox*/`1e-7` | `U0` |
| `NaN` | `U0` | `KP` | `KPd` | `KPd` | `U0` |
| *TOX* | `NaN` | `NaN` | `600`\**EPXox*/*TOX* | `600`\**EPXox*/*TOX* | `600` |
| *TOX* | `NaN` | `KP` | `KPd` | `KPd` | `600` |
| *TOX* | `U0` | `NaN` | *UO*\**EPXox*/*TOX* | *UO*\**EPXox*/*TOX* | `U0` |
| *TOX* | `U0` | `KP` | `KPd` | `KPd` | `U0` |

**氧化层厚度和阈值电压**

| 参数值 | | | | 表面电势 PHI（level 1），单位 V | 阈值电压 VTO（level 1），单位 V | 表面电势 PHI（level 3），单位 V | 阈值电压 VTO（level 3），单位 V |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Oxide thickness, TOX** | **Substrate doping, NSUB** | **Surface potential, PHI** | **Threshold voltage, VTO** |
| `NaN` | `NaN` | `NaN` | `NaN` | `0.6`（默认值） | 0（默认值） | `0.6`（默认值） | 0（默认值） |
| `NaN` | `NaN` | `NaN` | `VTO` | `0.6` | `VTO` | `0.6` | `VTO` |
| `NaN` | `NaN` | `PHI` | `NaN` | `PHI` | 0 | `PHI` | 0 |
| `NaN` | `NaN` | `PHI` | `VTO` | `PHI` | `VTO` | `PHI` | `VTO` |
| `NaN` | `NSUB` | `NaN` | `NaN` | `0.6` | 0 | `PHI (1e-7, NSUB)` | `VTO (1e-7, NSUB)` |
| `NaN` | `NSUB` | `NaN` | `VTO` | `0.6` | `VTO` | `PHI (1e-7, NSUB)` | `VTO` |
| `NaN` | `NSUB` | `PHI` | `NaN` | `PHI` | 0 | `PHI` | `VTO (1e-7, NSUB)` |
| `NaN` | `NSUB` | `PHI` | `VTO` | `PHI` | `VTO` | `PHI` | `VTO` |
| `TOX` | `NaN` | `NaN` | `NaN` | `0.6` | 0 | `0.6` | 0 |
| `TOX` | `NaN` | `NaN` | `VTO` | `0.6` | `VTO` | `0.6` | `VTO` |
| `TOX` | `NaN` | `PHI` | `NaN` | `PHI` | 0 | `PHI` | 0 |
| `TOX` | `NaN` | `PHI` | `VTO` | `PHI` | `VTO` | `PHI` | `VTO` |
| `TOX` | `NSUB` | `NaN` | `NaN` | `PHI (NSUB, TOX)` | `VTO (NSUB, TOX)` | `PHI (NSUB, TOX)` | `VTO (NSUB, TOX)` |
| `TOX` | `NSUB` | `NaN` | `VTO` | `PHI (NSUB, TOX)` | `VTO` | `PHI (NSUB, TOX)` | `VTO` |
| `TOX` | `NSUB` | `PHI` | `NaN` | `PHI` | `VTO (NSUB, TOX)` | `PHI` | `VTO (NSUB, TOX)` |
| `TOX` | `NSUB` | `PHI` | `VTO` | `PHI` | `VTO` | `PHI` | `VTO` |

其中 `PHI (NSUB, TOX)`、`PHI (1e-7, NSUB)`、`VTO (NSUB, TOX)` 和 `VTO (1e-7, NSUB)` 使用以下方程获得：

PHI=2kTqln(NSUBni)

GAMMA=2qεsiNSUBCox

VFB=φMS−qNSSCoxVTO=VFB+PHI+GAMMA\*PHI.

### 体源二极管模型

下表显示了定义体源电流 *Ibs* 与体源电压 *Vbs* 之间关系的方程。在适用的情况下，模型参数首先进行温度调整。有关详细信息，请参阅温度依赖性。

| *Vbs* 值的适用范围 | 对应的 *Ibs* 方程 |
| --- | --- |
| Vbs>80\*Vtn | Ibs=ISbs\*((VbsVtn−79)e80−1)+Vbs\*Gmin |
| 80Vtn≥Vbs | Ibs=ISbs\*(eVbs/Vtn−1)+Vbs\*Gmin |

其中：

- *ISbs* 是体饱和电流，使得，如果：

  - JSd≠0 且 AS≠0，则 ISbs=JSd\*AS。

    其中：

    - *JSd* 是几何调整体结饱和电流密度。
    - *AS* 是源面积。
  - 如果 JSd=0 或 AS=0，则 ISbs=ISd，其中 *ISd* 是几何调整体饱和电流。
- *Vtn* 是热电压。有关详细信息，请参阅热电压。
- *Gmin* 是最小电导。有关详细信息，请参阅最小导通。

### 体漏二极管模型

下表显示了定义体漏电流 *Ibd* 与体漏电压 *Vbd* 之间关系的方程。在适用的情况下，模型参数首先进行温度调整。有关详细信息，请参阅温度依赖性。

| *Vbd* 值的适用范围 | 对应的 *Ibd* 方程 |
| --- | --- |
| Vbd>80\*Vtn | Ibd=ISbd\*((VbdVtn−79)e80−1)+Vbd\*Gmin |
| 80Vtn≥Vbd | Ibd=ISbd\*(eVbd/Vtn−1)+Vbd\*Gmin |

其中：

- *ISbd* 是体漏电流，使得：

  - 如果 JSd≠0 且 AD≠0，则 ISbd=JSd\*AD。

    其中：

    - *JSd* 是几何调整体结饱和电流密度。
    - *AD* 是漏面积。
  - 如果 JSd=0 或 AD=0，则 ISbd=ISd，其中 *ISd* 是几何调整体饱和电流。
- *Vtn* 是热电压。有关详细信息，请参阅热电压。
- *Gmin* 是最小电导。有关详细信息，请参阅最小导通。

### Level 1 漏极电流模型

此表显示了正常模式（*Vds* ≥ 0）下漏极电流 *Id* 与漏源电压 *Vds* 之间的关系。在适用的情况下，模型参数首先根据温度进行调整。

**正常模式**

| *Vgs* 和 *Vds* 值的适用范围 | 对应的 *Id* 方程 |
| --- | --- |
| Vgs-Von≤0 | Id=0 |
| 0<Vgs-Von≤Vds | Id=BETA\*(Vgs−Von)2(1+LAMBDA\*Vds)2 |
| 0<Vds<Vgs-Von | Id=BETA\*Vds((Vgs-Von)-Vds2)(1+LAMBDA\*Vds) |

其中：

- *Von* 取决于 *Vbs* 和 *PHI*。

  | *Vbs* 和 *PHI* 值的适用关系 | 对应的 *Von* 方程 |
  | --- | --- |
  | Vbs≤0 | Von=MTYPE\*VBI+GAMMAPHI−Vbs |
  | 0<Vbs≤2\*PHI | Von=MTYPE\*VBI+GAMMA(PHI−Vbs2PHI) |
  | Vbs>2\*PHI | Von=MTYPE\*VBI |
- *MTYPE* 为 1。
- *BETA* 为 BETA=(KPd\*WIDTH)/(LENGTH−2\*LD)
- *KP* 为：

  - **Transconductance, KP**，如果此参数具有数值。
  - U0\*3.9\*ε0/TOX，如果 **Transconductance, KP** 为 `NaN` 且您为 **Oxide thickness, TOX** 和 **Substrate doping, NSUB** 参数都指定了值。
- *WIDTH* 为沟道宽度。
- *LENGTH* 为沟道长度。
- *LD* 为横向扩散。
- *VBI* 是模块在计算中使用的内建电压值。该值是温度的函数。详细定义请参见温度依赖性。
- *PHI* 为：

  - **Surface potential, PHI**，如果此参数具有数值。
  - 2\*kTmeas/q\*log(NSUB/ni)，如果 **Surface potential, PHI** 为 `NaN` 且您为 **Oxide thickness, TOX** 和 **Substrate doping, NSUB** 参数都指定了值。
- *LAMBDA* 为沟道调制。
- *GAMMA* 为：

  - **Bulk threshold, GAMMA**，如果此参数具有数值。
  - TOX\*2\*11.7\*ε0\*q\*NSUB/(3.9\*ε0)，如果 **Bulk threshold, GAMMA** 为 `NaN` 且您为 **Oxide thickness, TOX** 和 **Substrate doping, NSUB** 参数都指定了值。
- *ε0* 为自由空间的介电常数，8.854214871e-12 F/m。
- *ni* 为本征硅的载流子浓度，1.45e10 cm-3。

此表显示了反向模式（*Vds* < 0）下漏极电流 *Id* 与漏源电压 *Vds* 之间的关系。在适用的情况下，模型参数首先根据温度进行调整。

**反向模式**

| *Vgd* 和 *Vds* 值的适用范围 | 对应的 *Id* 方程 |
| --- | --- |
| Vgd-Von≤0 | Id=0 |
| 0<Vgd-Von≤−Vds | Id=−BETA(Vgd−Von)2(1−LAMBDA\*Vds)/2 |
| 0<−Vds<Vgd−Von | Id=BETA\*Vds((Vgd-Von)+Vds/2)(1−LAMBDA\*Vds) |

*Von* 取决于 *Vbd* 和 *PHI*。

| *Vbs* 和 *PHI* 值的适用关系 | 对应的 *Von* 方程 |
| --- | --- |
| Vbd≤0 | Von=MTYPE\*VBI+GAMMAPHI−Vbd |
| 0<Vbd≤2\*PHI | Von=MTYPE\*VBI+GAMMA(PHI−Vbs2PHI) |
| Vbd>2\*PHI | Von=MTYPE\*PHI |

### Level 3 漏极电流模型

模块在根据温度调整适用的模型参数后，为正常模式（Vds≥0）下的漏极电流 *Ids* 提供以下模型。

IDS=IDS0\*ScaleVMAX\*ScaleLChan\*ScaleINV

其中：

- *IDS0* 为基本漏极电流模型。
- *ScaleVMAX* 为速度饱和缩放。
- *ScaleLChan* 为沟道长度调制缩放。
- *ScaleINV* 为弱反型缩放。

模块对反向模式（Vds<0）下的漏极电流使用相同的模型，并进行以下替换：

Vbs≡Vbs−Vds

Vgs≡Vgs−Vds

Vds≡−Vds

**基本漏极电流模型**

漏极电流 *Ids* 与漏源电压 *Vds* 之间的关系为

IDS0=BETA\*Fgate\*(VGSX−VTH−1+FB2\*VDSX)\*VDSX

其中：

- *BETA* 的计算方式如 Level 1 漏极电流模型中所述。
- *FGATE* 的计算方式为

  Fgate=11+THETA\*(Vgsx−VTH)

  其中：

  - *THETA* 建模了迁移率对栅源电压的依赖性。
  - Vgsx=max(VGS,Von)
- 如果您为 **Fast surface state density, NFS** 参数指定了非零值，模块使用以下方程计算 *Von*：

  Von=VTH+xnVT

  否则，

  Von=VTH
- 模块计算 *xn* 如下

  xn=1+q\*NFSCOX+(GAMMA\*Fs\*Vbulk+Fn\*VbulkWIDTH)2\*Vbulk
- 模块计算 *Vbulk* 如下：

  - 如果

    VBS≤0，

    Vbulk=PHI−VBS。
  - 否则，模块计算 *Vbulk* 如下

    Vbulk=PHI(1+VBS2\*PHI)2
- 热电压使得

  VT=kTq
- 模块使用以下方程计算 *VTH*：

  VTH=VBI−8.15e−22\*ETACOX\*(LENGTH−2\*LD)3\*VDS​​​​​​​​​​            +GAMMA\*Fs\*Vbulk+Fn\*Vbulk

  有关模块如何计算 *VBI* 的信息，请参见温度依赖性。
- *ETA* 为 **Vds dependence threshold volt, ETA**。
- COX=εoxTOX，

  其中 *εox* 为氧化物的介电常数，*TOX* 为 **Oxide thickness, TOX**。
- 如果您为 **Junction depth, XJ** 参数指定了非零值并为 **Substrate doping, NSUB** 参数指定了值，模块使用以下方程计算 *Fs*：

  α=2εsiqNSUB

  XD=α

  wc=.0631353+.8013292\*XD\*VbulkXJ−.01110777\*(XD\*VbulkXJ)2+LDXJ

  Fs=1−(wc\*1−(XD\*VbulkXJ+XD\*Vbulk)2−LDXJ)

  其中 *εsi* 为硅的介电常数。

  否则，

  Fs=1
- 模块计算 *FB* 如下

  FB=GAMMA\*Fs4\*Vbulk+Fn
- 模块计算 *Fn* 如下

  Fn=DELTA\*π\*εsi2\*COX\*WIDTH
- *DELTA* 为阈值处的宽度效应。
- *VDSX* 为 *VDS* 与饱和电压 *Vdsat* 中的较小者。

  - 如果您为 **Max carrier drift velocity, VMAX** 参数指定了正值，模块使用以下方程计算 *Vdsat*：

    Vdsat=Vgsx−VTH1+FB+(LENGTH−2\*LD)\*VMAXUO\*Fgate             −(Vgsx−VTH1+FB)2+((LENGTH−2\*LD)\*VMAXUO\*Fgate)2

    否则，模块计算 *Vdsat* 如下

    Vdsat=Vgsx−VTH1+FB

**速度饱和缩放**

如果您为 **Max carrier drift velocity, VMAX** 参数指定了正值，模块计算 *ScaleVMAX* 如下

ScaleVMAX=11+UO\*Fgate(LENGTH−2\*LD)\*VMAX\*VDSX

否则，

ScaleVMAX=1

**沟道长度调制缩放**

如果模块满足以下所有条件，模块会缩放漏极电流以考虑沟道长度调制：

- VDS>Vdsat
- **Max carrier drift velocity, VMAX** 小于或等于零，或者 *α* 非零。

模块使用以下方程缩放漏极电流：

ScaleLChan=11−Δl(LENGTH−2\*LD)

为计算 Δl，模块：

1. 计算中间值 Δl0。

   - 如果您为 **Max carrier drift velocity, VMAX** 参数指定了正值，模块将中间值 *gdsat* 计算为 1e-12 与以下方程结果中的较大者：

     IDS0\*(1−11+Scalegdsat\*VDSX)\*Scalegdsat

     其中：

     Scalegdsat=UO\*Fgate(LENGTH−2\*LD)\*VMAX

     然后，模块使用以下方程计算中间值 Δ*l0*：

     Δl0=(KA\*IDS2\*(LENGTH−2\*LD)\*gdsat)2+KA\*(VDS−Vdsat)            −KA\*IDS2\*(LENGTH−2\*LD)\*gdsat

     其中

     KA=KAPPA\*α。
   - 否则，模块使用以下方程计算中间值 Δl0

     Δl=KA\*(VDS−Vdsat)
2. 模块检查穿通并计算 Δl。

   - 如果

     Δl0>(LENGTH−2\*LD)/2，

     模块使用以下方程计算 Δl：

     Δl=(1−(LENGTH−2\*LD)4\*Δl0)\*(LENGTH−2\*LD)
   - 否则，

     Δl=Δl0。

**弱反型缩放**

如果 *VGS* 小于 *Von*，模块使用以下方程计算 *ScaleINV*：

ScaleINV=eVgs−Vonxn\*VT

否则，

ScaleINV=1

### 结电荷模型

模块对结重叠电荷和体结电荷进行建模。

**结重叠电荷**

模块计算以下结重叠电荷：

- QGS=CGSOd\*WIDTH\*Vgs

  其中：

  - *QGS* 为栅源重叠电荷。
  - *CGSOd* 为几何调整后的栅源重叠电容。
  - *WIDTH* 为沟道宽度。
- QGD=CGDOd\*WIDTH\*Vgd

  其中：

  - *QGD* 为栅漏重叠电荷。
  - *CGDOd* 为几何调整后的栅漏重叠电容。
- QGB=CGBOd\*(LENGTH−2\*LD)\*Vgb

  其中：

  - *QGB* 为栅体重叠电荷。
  - *CGBOd* 为几何调整后的栅体重叠电容。
  - *LENGTH* 为沟道长度。
  - *LD* 为横向扩散。

**体结电荷**

此表显示了体漏底部结电荷 *Qbottom* 与结电压 *Vbd* 之间的关系。在适用的情况下，模型参数首先根据温度进行调整。

| *Vbd* 值的适用范围 | 对应的 *Qbottom* 方程 |
| --- | --- |
| Vbd<FC\*PB | Qbottom=CBDd\*PB\*(1-(1-VbdPB)1−MJ)1−MJ 如果 CBDd>0  Qbottom=CJd\*AD\*PB\*(1-(1-VbdPB)1−MJ)1−MJ 否则。 |
| Vbd≥FC\*PB | Qbottom=CBDd\*                       (F1+F3\*(Vbd-FC\*PB)+MJ\*(Vbd2-(FC\*PB)2)2\*PBF2) 如果 CBDd>0  Qbottom=CJd\*AD\*                       (F1+F3\*(Vbd-FC\*PB)+MJ\*(Vbd2-(FC\*PB)2)2\*PBF2) 否则。 |

其中：

- *PB* 为体结电势。
- *FC* 为电容系数。
- *CBDd* 为几何调整后的零偏置体漏电容。
- *CJd* 为几何调整后的每结面积底部电容。
- *AD* 为漏极面积。
- *MJ* 为底部梯度系数。
- F1=PB\*(1-(1-FC)1−MJ)1−MJ
- F2=(1-FC)1+MJ
- F3=1-FC\*(1+MJ)

为计算体源底部结电荷，模块在前表中的方程中替换变量。模块替换：

- *Vbs* 替换 *Vbd*
- *AS* 替换 *AD*
- *CBSd* 替换 *CBDd*

此表显示了体漏侧壁结电荷 *Qsidewall* 与结电压 *Vbd* 之间的关系。在适用的情况下，模型参数首先根据温度进行调整。

| *Vbd* 值的适用范围 | 对应的 *Qsidewall* 方程 |
| --- | --- |
| Vbd<FC\*PB | Qsidewall=CJSWd\*PD\*PB\*(1-(1-VbdPB)1−MGSW)1−MGSW |
| Vbd≥FC\*PB | Qsidewall=CJSWd\*PD\*                      (F1+F3\*(Vbd-FC\*PB)+MGSW\*(Vbd2-(FC\*PB)2)2\*PBF2) |

其中：

- *CJSWd* 为几何调整后的每结周长侧壁电容。
- *PD* 为漏极周长。
- *MGSW* 为侧壁梯度系数。
- F1=PB\*(1-(1-FC)1−MJSW)1−MJSW
- F2=(1-FC)1+MJSW
- F3=1-FC\*(1+MJSW)

为计算体源侧壁结电荷和侧壁结电压，模块在前表中的方程中替换变量。模块替换：

- *Vbs* 替换 *Vbd*
- *PS* 替换 *PD*

### 电容模型

SPICE NMOS 模块允许您以三种不同方式对晶体管电容模型进行建模：

- 无本征电容模型
- Meyer 栅极电容模型
- 电荷守恒电容模型

**Meyer 栅极电容模型**

此表显示了晶体管的工作区与栅体、栅漏和栅源电容之间的关系。

| 工作区 | 栅体 *Cgb*、栅漏 *Cgd* 和栅源 *Cgs* 方程 | |
| --- | --- | --- |
| 积累区，Vgb<VFB | Cgb=CoxtCgd=0Cgs=0 | |
| 耗尽区，Vgs<VTH | Cgb=Coxt1+4GAMMA2\*(Vgb−VFB)Cgd=0Cgs=0 | |
| 饱和区，Vgs−VTH<Vds | 如果 Vds<Vsatmin 则： | 如果 Vds≥Vsatmin 则： |
| Cgb=0Cgd=23(Coxt−Cgb)(1−(Vsatmin)2(2Vsatmin−Vds)2)Cgs=23(Coxt−Cgb)(1−(Vsatmin−Vds)2(2Vsatmin−Vds)2) | Cgb=0Cgd=0Cgs=23(Coxt−Cgb) |
| 线性区，Vgs−VTH>Vds | Cgb=0Cgd=23(Coxt−Cgb)\*(1−(Vgs−VTH)2(2\*(Vgs−VTH)−Vds)2)Cgs=23(Coxt−Cgb)\*(1−(Vgs−VTH−Vds)2(2\*(Vgs−VTH)−Vds)2) | |

其中：

- Coxt=WIDTH\*(LENGTH−2\*LD)\*COX\*AREA\*SCALE
- VFB=VBI\*MTYPE−PHI 为平带电压。
- *Vsatmin* 为最小饱和电压。它是一个预定义参数，等于 `1` `V`。

这些方程在耗尽区和积累区之间是连续的，在耗尽区和反型区之间是不连续的。其他 SPICE 工具在反型区和耗尽区之间应用平滑函数。

Cgb=WIDTH\*LENGTH\*COX(1+4GAMMA2\*(VTH−Vbs−VFB))m\*smoothingsmoothing=1(1+4GAMMA2\*(Vgs−VTH))m

其中 *m* 为预定义平滑常数。

**电荷守恒电容模型**

此表显示了 level 1 MOS 的晶体管工作区与栅极、体、沟道、漏极和源极电荷之间的关系。

| 工作区 | Level-1 电荷方程 |
| --- | --- |
| 积累区，Vgb<VFB | Qg=Coxt\*(Vgb−VFB)Qb=−Coxt\*(Vgb−VFB)Qc=0Qd=0Qs=Qc−Qd |
| 耗尽区，Vgs<VTH | Qg=−0.5\*Coxt\*GAMMA2\*(1−1+4GAMMA2\*(Vgb−VFB))Qb=0.5\*Coxt\*GAMMA2\*(1−1+4GAMMA2\*(Vgb−VFB))Qc=0Qd=0Qs=Qc−Qd |
| 饱和区，Vgs−VTH<Vds | Qg=Coxt\*(Vgs−VFB−PHI−Vgs−VTH3)Qb=−Coxt\*(VTH−VFB−PHI)Qc=−Coxt\*(Vgs−VTH−Vgs−VTH3)Qd=0Qs=Qc−Qd |
| 线性区，Vgs−VTH>Vds | Qg=Coxt\*(Vgs−VFB−PHI−Vds2+Vds212(Vgs−VTH−0.5Vds))Qb=−Coxt\*(VTH−VFB−PHI)Qc=−Coxt\*(Vgs−VTH−Vds2+Vds212(Vgs−VTH−0.5Vds))Qd=−Coxt\*(Vgs−VTH2−3Vds4+Vds28(Vgs−VTH−0.5Vds))Qs=Qc−Qd |

其中：

- Qc=−(Qg+Qb)=Qd+Qs 为沟道中的电荷。*Qc* 需要在 *Qd* 和 *Qs* 之间分配。

其中：

- *Qg* 为栅极电荷。
- *Qb* 为体电荷。
- *Qd* 为漏极电荷。
- *Qs* 为源极电荷。
- Qc=−(Qg+Qb)=Qd+Qs 为沟道中的电荷。*Qc* 需要在 *Qd* 和 *Qs* 之间分配。

此表显示了 level-3 MOS 的晶体管工作区与栅极、体、沟道、漏极和源极电荷之间的关系。

| 工作区 | Level-3 电荷方程 |
| --- | --- |
| 积累区，Vgb<VFB | Qg=Coxt\*(Vgb−VFB)−SF1+SF2Qb=−Coxt\*(Vgb−VFB)−SF1+SF2Qc=0Qd=0Qs=Qc−Qd |
| 耗尽区，Vgs<VTH | Qg=−0.5\*Coxt\*GAMMA2\*(1−1+4GAMMA2\*(Vgb−VFB))−SF1+SF2Qb=0.5\*Coxt\*GAMMA2\*(1−1+4GAMMA2\*(Vgb−VFB))+SF1−SF2Qc=0Qd=0Qs=Qc−Qd |
| 饱和区，Vgs−VTH<Vds | Qg=Coxt\*(Vgs−VFB−PHI+ETA\*Vdsat−Vdsat2+1+FB12\*Fi\*Vdsat2)Qb=−Coxt\*(VTH−VFB−PHI+ETA\*Vdsat−Fb2\*Vds−FB\*(1+FB)12\*Fi\*Vdsat2)Qc=−Coxt\*(Vgs−VTH−1+FB2\*Vdsat+(1+FB)212\*Fi\*Vdsat2)Qd=0Qs=Qc−Qd |
| 线性区，Vgs−VTH>Vds | Qg=Coxt\*(Vgs−VFB−PHI+ETA\*Vds−Vds2+1+FB12\*Fi\*Vds2)Qb=−Coxt\*(VTH−VFB−PHI+ETA\*Vds+FB2\*Vds−FB\*(1+FB)12\*Fi\*Vds2)Qc=−Coxt\*(Vgs−VTH−1+FB2\*Vds+(1+FB)212\*Fi\*Vds2)Qd=−Coxt\*(Vgs−VTH2−3(1+FB)2\*Vds+(1+FB)28\*Fi\*Vds2)Qs=Qc−Qd |

其中：

- *Vdsat* 为饱和电压
- *FB* 为体效应系数
- *ETA* 为漏源电压阈值系数
- Fi=Vgs−VTH−1+FB2\*Vds
- SF1=−0.5\*Coxt\*GAMMA2\*(1−(1+4GAMMA2\*2(VTH−Vbs−VFB))0.5) 和 SF2=Coxt\*(VTH−VFB−PHI) 为耗尽区和积累区之间的平滑因子，有助于收敛。

### 温度依赖性

跨导作为晶体管温度的函数为

KP(T)=KPd(TTmeas)3/2

其中：

- *KPd* 是经几何调整的跨导。
- *T* 是晶体管温度。有关详细信息，请参阅晶体管温度。
- *Tmeas* 是参数提取温度。

表面势作为晶体管温度的函数为

PHI(T)=TTmeas(PHI+kTmeasq(log(Tmeas300.15)3+qk(1.115300.15−EGTmeasTmeas)))                          −kTq(log(T300.15)3+qk(1.115300.15−EGTT))

其中：

- *PHI* 是表面势。
- *k* 是玻尔兹曼常数。
- *q* 是电子上的基本电荷，1.6021918e-19 C。
- *EG* 是激活能，使得：

  - EGTmeas=1.16eV-(7.02e-4\*Tmeas2)/(Tmeas+1108)
  - EGT=1.16eV-(7.02e-4\*T2)/(T+1108)

内建电压作为晶体管温度的函数为

VBI(T)=VTO+MTYPE\*(PHI(T)−PHI2−GAMMAPHI)                               +EGTmeas−EGT2

其中：

- *VBI* 是内建电压。
- *VTO* 是阈值电压。
  *VTO* 取决于你在 **DC currents** 设置中为 **Threshold voltage, VTO** 参数指定的值。如果你指定数值，则 *VTO* 按该值计算。如果你指定非数值（`NAN`），并且在 **Process** 设置中为 **Oxide thickness, TOX** 和 **Substrate doping, NSUB** 参数都指定了数值，则 *VTO* 按 Φ−3.25+EGTmeas/2+MTYPE\*PHI/2−NSS\*q\*TOX/(3.9\*ε0)+MTYPE\*(GAMMA\*PHI+PHI) 计算，其中：

  - *Φ* 取决于栅极类型，你通过 **Gate type, TPG** 参数指定该类型。如果你指定 `Aluminum (0)`，则 Φ=3.2。否则，Φ=3.25+EGTmeas/2−MTYPE\*TPG\*EGTmeas/2，其中：

    - *MTYPE* 是晶体管类型。对于 N 沟道 MOSFET，*MTYPE* = 1。
    - *TPG* 表示栅极类型，并且还取决于你在 **Process** 设置中为 **Gate type, TPG** 参数指定的选项。如果你指定

      - `Opposite of substrate (1)` — *TPG* = 1
      - `Same as substrate (-1)` — *TPG* = -1
  - *NSS* 是表面态密度。
  - *TOX* 是氧化层厚度。
  - *ε0* 是真空介电常数。
  - *GAMMA* 是体阈值。*GAMMA* 取决于你在 **DC currents** 设置中为 **Bulk threshold, GAMMA** 参数指定的值。如果你指定数值，则 *GAMMA* 按该值计算。如果你指定非数值（`NAN`），并且在 **Process** 设置中为 **Oxide thickness, TOX** 和 **Substrate doping, NSUB** 参数都指定了数值，则 *VTO* 按 TOX\*2\*11.7\*ε0\*q\*NSUB/(3.9\*ε0) 计算，其中 *NSUB* 是衬底掺杂。

体饱和电流作为晶体管温度的函数为

IS(T)=ISd\*e−qEGTND\*kT + qEGTmeasND\*kTmeas

其中：

- *ISd* 是经几何调整的体饱和电流。
- *ND* 是发射系数。

体结饱和电流密度作为晶体管温度的函数为

JS(T)=JSd\*e−qEGTND\*kT + qEGTmeasND\*kTmeas

其中 *JSd* 是经几何调整的体结饱和电流密度。

体结电势作为晶体管温度的函数为

PB(T)=PB+kTmeasq(log(Tmeas300.15)3+qk(1.115300.15−EGTmeasT))TmeasT                         −kTq(log(T300.15)3+qk(1.115300.15−EGTT))

其中 *PB* 是体结电势。

体-漏结电容作为晶体管温度的函数为

CBD(T)=CBDdpbo+MJ\*(4\*104\*(T−300.15)\*pbo−(PB(T)−pbo))pbo+MJ\*(4\*104\*(Tmeas−300.15)\*pbo−(PB−pbo))

其中：

- *CBDd* 是经几何调整的零偏置体-漏电容。
- *MJ* 是底部梯度系数。
- pbo=PB+kTmeasq(log(Tmeas300.15)3+qk(1.115300.15−EGTmeasT))Tmeas300.15

该模块使用 *CBD(T)* 方程来计算：

- 体-源结电容，方法是将 *CBSd*（经几何调整的零偏置体-源电容）代入 *CBDd*。
- 底部结电容，方法是将 *CJd*（经几何调整的每结面积底部电容）代入 *CBDd*。

侧壁结电容 *CJSW* 与晶体管温度 *T* 之间的关系为

CJSW(T)=CJSWdpbo+MJSW\*(4\*104\*(T−300.15)\*pbo−(PB(T)−pbo))pbo+MJSW\*(4\*104\*(Tmeas−300.15)\*pbo−(PB−pbo))

其中：

- *CJSWd* 是经侧壁几何调整的每结周长侧壁电容。
- *MJSW* 是侧壁梯度系数。
