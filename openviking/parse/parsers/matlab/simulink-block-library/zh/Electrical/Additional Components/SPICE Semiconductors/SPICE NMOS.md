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

### 守恒

### **gx** — 栅极端子电气

与晶体管栅极端子关联的电气守恒端口。

### **dx** — 漏极端子电气

与晶体管漏极端子关联的电气守恒端口。

### **sx** — 源极端子电气

与晶体管源极端子关联的电气守恒端口。

### **bx** — 体端子电气

与晶体管体端子关联的电气守恒端口。

## 参数

### 模型选择

### **MOS 模型** — 漏极电流模型 `Level 1 MOS`（默认）| `Level 3 MOS`

MOSFET 漏极电流模型选项：

- `Level 1 MOS` — 使用 Level 1 漏极电流模型。这是默认选项。
- `Level 3 MOS` — 使用 Level 3 漏极电流模型。

#### 依赖关系

您为 **MOS 模型** 选择的设置会影响 **直流电流** 和 **工艺** 设置中某些参数的可见性。

### 尺寸

### **器件面积因子，AREA** — 器件面积 `1.0`（默认）| 正标量

用于缩放的晶体管面积因子。该值必须大于 `0`。

### **并联器件数，SCALE** — 并联器件数 `1`（默认）| 正整数

模块所表示的并联 MOS 实例数。该参数会乘以输出电流和器件电荷。该值必须大于 `0`。

### **沟道长度，LENGTH** — 源极到漏极沟道长度 `1e-4` `m`（默认）| 正标量

源极和漏极之间沟道的长度。

### **沟道宽度，WIDTH** — 源极到漏极沟道宽度 `1e-4` `m`（默认）| 正标量

源极和漏极之间沟道的宽度。

### **漏极面积，AD** — 漏极面积 `0` `m^2`（默认）| 非负标量

晶体管漏极扩散区的面积。该值必须大于或等于 `0`。

### **源极面积，AS** — 源极面积 `0` `m^2`（默认）| 非负标量

晶体管源极扩散区的面积。该值必须大于或等于 `0`。

### **漏极周长，PD** — 漏极周长 `0` `m`（默认）| 非负标量

晶体管漏极扩散区的周长。该值必须大于或等于 `0`。

### **源极周长，PS** — 源极周长 `0` `m`（默认）| 非负标量

晶体管源极扩散区的周长。该值必须大于或等于 `0`。

### 电阻

### **漏极方块数，NRD** — 漏极扩散电阻方块数 `0`（默认）| 非负标量

构成晶体管漏极扩散区的电阻方块数。该值必须大于或等于 `0`。仅当您未指定 **漏极电阻，RD** 和 **源极电阻，RS** 参数值中的一个或两个时，模块才使用此参数值，如参数计算中所述。

### **源极方块数，NRS** — 晶体管源极扩散电阻方块数 `1`（默认）| 非负标量

构成晶体管源极扩散区的电阻方块数。该值必须大于或等于 `0`。仅当您未指定 **漏极电阻，RD** 和 **源极电阻，RS** 参数值中的一个或两个时，模块才使用此参数值，如参数计算中所述。

### **漏极电阻，RD** — 串联电阻 `0` `Ohm`（默认）| 非负标量

晶体管漏极电阻。该值必须大于或等于 `0`。

### **源极电阻，RS** — 串联电阻 `0` `Ohm`（默认）| 非负标量

晶体管源极电阻。该值必须大于或等于 `0`。

### **薄层电阻，RSH** — 每方块电阻 `0` `Ohm`（默认）| 非负标量

晶体管源极和漏极的每方块电阻。请查看参数计算，以了解模块何时使用此参数。该值必须大于或等于 `0`。

### 直流电流

### **阈值电压，VTO** — 阈值电压 `0` `V`（默认）| 标量

当超过该栅源电压时，晶体管会产生非零漏极电流。如果为此参数赋值为 `NaN`，则模块会根据指定的 **氧化层厚度，TOX** 和 **衬底掺杂，NSUB** 参数值计算该值。有关此计算的详细信息，请参阅温度依赖性。

### **跨导，KP** — 跨导 `2e-5` `A/V^2`（默认）| 非负标量

漏极电流关于栅极电压的导数。该值必须大于或等于 `0`。如果为此参数赋值为 `NaN`，则模块会根据指定的 **氧化层厚度，TOX** 和 **衬底掺杂，NSUB** 参数值计算该值。有关此计算的详细信息，请根据 **MOS 模型** 参数的所选值，酌情参阅 Level 1 漏极电流模型或 Level 3 漏极电流模型。

### **体阈值，GAMMA** — 体阈值 `0` `V^0.50000`（默认）| 非负标量

体效应参数，它将阈值电压 VTH 与体偏置 VBS 关联起来，如 Level 1 漏极电流模型和 Level 3 漏极电流模型中所述。该值必须大于或等于 `0`。如果为此参数赋值为 `NaN`，则模块会根据指定的 **氧化层厚度，TOX** 和 **衬底掺杂，NSUB** 参数值计算该值。有关此计算的详细信息，请根据 **MOS 模型** 参数的所选值，酌情参阅 Level 1 漏极电流模型或 Level 3 漏极电流模型。

### **表面电势，PHI** — 表面电势 `0.6` `V`（默认）| 非负标量

当表面电子浓度等于本征浓度且器件在耗尽与反型条件之间过渡时电压的两倍。该值必须大于或等于 `0`。如果为此参数赋值为 `NaN`，则模块会根据指定的 **氧化层厚度，TOX** 和 **衬底掺杂，NSUB** 参数值计算该值。有关此计算的详细信息，请根据 **MOS 模型** 参数的所选值，酌情参阅 Level 1 漏极电流模型或 Level 3 漏极电流模型。

### **沟道调制，LAMBDA** — 沟道长度调制 `0` `1/V`（默认）| 标量

沟道长度调制。

#### 依赖关系

仅当您在 **模型选择** 设置中为 **MOS 模型** 参数选择 `Level 1 MOS` 时，此参数才可见。

### **体饱和电流，IS** — 体饱和电流大小 `1e-14` `A`（默认）| 非负标量

在非常大的反向偏置水平下，结渐近趋近的电流大小。该值必须大于或等于 `0`。

### **发射系数，N** — 发射系数 `1`（默认）| 非负标量

晶体管发射系数或理想因子。该值必须大于 `0`。

### **体结饱和电流密度，JS** — 体结饱和电流密度 `0` `A/m^2`（默认）| 非负标量

在非常大的反向偏置水平下，结渐近趋近的单位面积电流大小。该值必须大于或等于 `0`。

### **宽度对阈值的影响，DELTA** — 宽度因子 `0`（默认）| 标量

控制晶体管宽度对阈值电压影响的因子。

#### 依赖关系

仅当您在 **模型选择** 设置中为 **MOS 模型** 参数选择 `Level 3 MOS` 时，此参数才可见。

### **最大载流子漂移速度，VMAX** — 最大漂移速度 `0` `m/s`（默认）| 标量

载流子的最大漂移速度。

#### 依赖关系

仅当您在 **模型选择** 设置中为 **MOS 模型** 参数选择 `Level 3 MOS` 时，此参数才可见。

### **快表面态密度，NFS** — 快表面态密度 `0` `1/cm^2`（默认）| 标量

快表面态密度会针对由栅极电压引起的迁移率降低来调整漏极电流。

#### 依赖关系

仅当您在 **模型选择** 设置中为 **MOS 模型** 参数选择 `Level 3 MOS` 时，此参数才可见。

### **Vds 相关阈值电压，ETA** — 漏源电压阈值 `0`（默认）| 标量

控制在漏极电流计算中漏极电压如何影响迁移率的系数。

#### 依赖关系

仅当您在 **模型选择** 设置中为 **MOS 模型** 参数选择 `Level 3 MOS` 时，此参数才可见。

### **Vgs 对迁移率的依赖性，THETA** — 迁移率依赖系数 `0` `1/V`（默认）| 标量

控制在漏极电流计算中栅极电压如何影响迁移率的系数。

#### 依赖关系

仅当您在 **模型选择** 设置中为 **MOS 模型** 参数选择 `Level 3 MOS` 时，此参数才可见。

### **迁移率调制，KAPPA** — 迁移率调制系数 `0.2`（默认）| 标量

Level 3 MOS 模型的沟道长度调制系数。

#### 依赖关系

仅当您在 **模型选择** 设置中为 **MOS 模型** 参数选择 `Level 3 MOS` 时，此参数才可见。

### C-V

### **栅极电容建模 (CGS, CGD, CGB)** — 栅极电容模型 `No intrinsic capacitance`（默认）| `Meyer gate capacitances` | `Charge conservation capacitances`

对栅极电容建模的选项：

- `No intrinsic capacitance` — 不在模型中包含栅极电容。
- `Meyer gate capacitances` —
- `Charge conservation capacitances` —

### **栅极重叠电容建模 (CGSO, CGDO, CGBO)** — 栅极重叠模型 `No`（默认）| `Yes`

对栅极重叠电容建模的选项：

- `No` — 不在模型中包含栅极重叠电容。
- `Yes` — 指定栅源、栅漏和栅体电容。

#### 依赖关系

选择 `Yes` 会显示相关参数。

### **栅源重叠电容，CGSO** — 栅源重叠电容 `0` `F/m`（默认）| 标量 | `0` 或 ≥ `1e-18`

由于源极横向扩散产生的栅源电容。该值必须等于 `0` 或大于或等于 *Cmin*。*Cmin* 是内置模型常量，其值为 `1e-18`。

#### 依赖关系

仅当您为 **栅极重叠电容建模 (CGSO, CGDO, CGBO)** 参数选择 `Yes` 时，此参数才可见。

### **栅漏重叠电容，CGDO** — 栅漏重叠电容 `0` `F/m`（默认）| 标量 | `0` 或 ≥ `1e-18`

由于漏极横向扩散产生的栅漏电容。该值必须等于 `0` 或大于或等于 *Cmin*。*Cmin* 是内置模型常量，其值为 `1e-18`。

#### 依赖关系

仅当您为 **栅极重叠电容建模 (CGSO, CGDO, CGBO)** 参数选择 `Yes` 时，此参数才可见。

### **栅体重叠电容，CGBO** — 栅体重叠电容 `0` `F/m`（默认）| 标量 | `0` 或 ≥ `1e-18`

由于栅极延伸到沟道宽度之外产生的栅体电容。该值必须等于 `0` 或大于或等于 *Cmin*。*Cmin* 是内置模型常量，其值为 `1e-18`。

#### 依赖关系

仅当您为 **栅极重叠电容建模 (CGSO, CGDO, CGBO)** 参数选择 `Yes` 时，此参数才可见。

### **结电容建模 (CBD, CBS)** — 结电容模型 `No`（默认）| `Yes`

对结电容建模的选项：

- `No` — 不在模型中包含结电容。
- `Yes` — 指定零偏结电容、结电势、梯度系数、正向偏置耗尽和电容系数。

#### 依赖关系

选择 `Yes` 会显示相关参数。

### **零偏 BD 电容，CBD** — 零偏结电容 `0` `F`（默认）| `0` 或 ≥ `1e-18`

体与漏极之间的电容。该值必须等于 `0` 或大于或等于 *Cmin*。*Cmin* 是内置模型常量，其值为 `1e-18`。

#### 依赖关系

仅当您为 **结电容建模 (CBD, CBS)** 参数选择 `Yes` 时，此参数才可见。

### **零偏 BS 电容，CBS** — 零偏体源电容 `0` `F`（默认）| 标量 | `0` 或 ≥ `1e-18`

体与源极之间的电容。该值必须等于 `0` 或大于或等于 *Cmin*。*Cmin* 是内置模型常量，其值为 `1e-18`。

#### 依赖关系

仅当您为 **结电容建模 (CBD, CBS)** 参数选择 `Yes` 时，此参数才可见。

### **体结电势，PB** — 体结电势 `0.8` `V`（默认）| 标量 | `0` 或 ≥ `0.01`

体结两端的电势。仅当您为 **结电容建模 (CBD, CBS)** 参数选择 `Yes` 时，此参数才可见。该值必须等于 `0` 或大于或等于 *VJmin*。*VJmin* 是内置模型常量，其值为 `0.01`。

#### 依赖关系

仅当您为 **结电容建模 (CBD, CBS)** 参数选择 `Yes` 时，此参数才可见。

### **每面积底部结电容，CJ** — 每结面积零偏体结底部电容 `0` `F/m^2`（默认）| 标量 | `0` 或 ≥ `1e-18`

每结面积的零偏体结底部电容。该值必须等于 `0` 或大于或等于 *Cmin*。*Cmin* 是内置模型常量，其值为 `1e-18`。

#### 依赖关系

仅当您为 **结电容建模 (CBD, CBS)** 参数选择 `Yes` 时，此参数才可见。

### **底部梯度系数，MJ** — 底部梯度系数 `0.5`（默认）| 标量 | 0 或 < 0.9

晶体管底部梯度系数。该值必须等于 `0` 或小于 *MGmax*。*MGmax* 是内置模型常量，其值为 `0.9`。

#### 依赖关系

仅当您为 **结电容建模 (CBD, CBS)** 参数选择 `Yes` 时，此参数才可见。

### **侧结电容/结周长面积，CJSW** — 每结周长零偏体结侧壁电容 `0` `F/m`（默认）| 标量 | `0` 或 ≥ `1e-18`

每结周长的零偏体结侧壁电容。该值必须等于 `0` 或大于或等于 *Cmin*。*Cmin* 是内置模型常量，其值为 `1e-18`。

#### 依赖关系

仅当您为 **结电容建模 (CBD, CBS)** 参数选择 `Yes` 时，此参数才可见。

### **侧壁梯度系数，MJSW** — 侧壁梯度系数 `0.5`（默认）| 标量 | 0 < *MJSW* < 0.9

晶体管侧壁梯度系数。该值必须等于 `0` 或小于 *MGmax*。*MGmax* 是内置模型常量，其值为 `0.9`。

#### 依赖关系

仅当您为 **结电容建模 (CBD, CBS)** 参数选择 `Yes` 时，此参数才可见。

### **电容系数，FC** — 电容系数 `0.5`（默认）| 0 或 ≤ 0.95 | 标量

用于量化耗尽电容随施加电压降低的拟合系数。该值必须等于 `0` 或小于或等于 *FCmax*。*FCmax* 是内置模型常量，其值为 `0.95`。

#### 依赖关系

仅当您为 **结电容建模 (CBD, CBS)** 参数选择 `Yes` 时，此参数才可见。

### **指定初始条件** — 初始条件模型 `No`（默认）| `Yes`

用于指定初始条件的选项：

- `No` — 不为模型指定初始条件。
- `Yes` — 指定初始晶体管电压。

  **注意**

  模块将初始晶体管电压施加在结电容两端，而不是端口两端。

#### 依赖项

要启用此参数，请设置以下任一项：

- 将 **栅极电容建模 (CGS, CGD, CGB)** 设置为 `No intrinsic capacitance`，并将 **栅极交叠电容建模 (CGSO, CGDO, CGBO)** 和 **结电容建模 (CBD, CBS)** 中的任一或两者设置为 `Yes`。
- 将 **栅极电容建模 (CGS, CGD, CGB)** 设置为 `Meyer gate capacitances` 或 `Charge conservation capacitances`。

### **初始条件电压, ICVDS** — 初始电压 `0` `V`（默认） | scalar

仿真开始时的漏-源电压。

#### 依赖项

仅当您为 **指定初始条件** 参数选择 `Yes` 时，此参数才可见。

### **初始条件电压, ICVGS** — 初始电压 `0` `V`（默认） | scalar

仿真开始时的栅-源电压。

#### 依赖项

仅当您为 **指定初始条件** 参数选择 `Yes` 时，此参数才可见。

### **初始条件电压, ICVBS** — 初始电压 `0` `V`（默认） | scalar

仿真开始时的体-源电压。

#### 依赖项

仅当您为 **指定初始条件** 参数选择 `Yes` 时，此参数才可见。

### 工艺

### **氧化层厚度, TOX** — 栅氧化层厚度 `1e-7` `m`（默认） | nonegative scalar

栅氧化层的厚度。该值必须大于或等于 `0`。

### **横向扩散, LD** — 横向扩散长度 `0` `m`（默认） | scalar

横向扩散长度。

### **表面迁移率, U0** — 零偏表面迁移率系数 `600` `cm^2/s/V`（默认）

零偏表面迁移率系数。

### **衬底掺杂, NSUB** — 衬底掺杂 `NaN` `1/cm^3`（默认） | scalar ≥ `1.45e10`

衬底掺杂。该值必须大于或等于 `1.45e10`（本征硅的载流子浓度）。

### **栅类型, TPG** — 栅类型 `Opposite of substrate (1)`（默认） | `Same as substrate (-1)` | `Aluminum (0)`

MOSFET 栅材料（与衬底相比）：

- `Opposite of substrate` — 栅材料与衬底相反。这意味着在器件方程中 TPG = 1。这是默认选项。
- `Same as substrate` — 栅材料与衬底相同。这意味着在器件方程中 TPG = –1。
- `Aluminum` — 栅材料为铝。这意味着在器件方程中 TPG = 0。

### **表面态密度, NSS** — 表面态密度 `NaN` `1/cm^2`（默认） | scalar

表面态密度。

### **结深, XJ** — 结深 `0``m`（默认）

结深。

#### 依赖项

仅当您在 **模型选择** 设置中为 **MOS 模型** 参数选择 `Level 3 MOS` 时，此参数才可见。

### 温度

### **使用以下方式建模温度依赖性** — 温度依赖性模型 `Device temperature`（默认） | `Fixed temperature`

选择以下选项之一来建模晶体管温度依赖性：

- `Device temperature` — 使用器件温度来建模温度依赖性。
- `Fixed temperature` — 使用独立于电路温度的温度来建模温度依赖性。

有关详细信息，请参阅温度依赖性。

#### 依赖项

选择 `Device temperature` 会显示 **本地电路温度偏移, TOFFSET** 参数。选择 `Fixed temperature` 会显示 **固定电路温度, TFIXED** 参数。

### **固定电路温度, TFIXED** — 固定电路温度 `300.15` `K`（默认） | positive scalar

晶体管仿真温度。该值必须大于 `0` `K`。

#### 依赖项

仅当您为 **使用以下方式建模温度依赖性** 参数选择 `Fixed temperature` 时，此参数才可见。

### **参数提取温度, TMEAS** — 参数提取温度 `300.15` `K`（默认） | positive scalar

测量晶体管参数时的温度。该值必须大于 `0` `K`。

### **本地电路温度偏移, TOFFSET** — 本地电路温度偏移 `0` `K`（默认） | scalar

晶体管温度与电路温度之间的差值。

#### 依赖项

仅当您为 **使用以下方式建模温度依赖性** 参数选择 `Device temperature` 时，此参数才可见。

## 所属库

Simscape / Electrical / Additional Components / SPICE Semiconductors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2009a 中引入**

## 描述

SPICE 兼容 N 沟道 MOSFET

SPICE NMOS 模块表示一个 SPICE 兼容的负沟道（N 沟道）金属氧化物半导体 (MOS) 场效应晶体管 (FET)。如果栅-源电压增加，则沟道电导增加。如果栅-源电压减小，则沟道电导减小。

SPICE（Simulation Program with Integrated Circuit Emphasis）是一种用于电子电路的仿真工具。您可以使用 Environment Parameters 模块以及 Additional Components 库中的 SPICE 兼容模块，将一些 SPICE 子电路转换为等效的 Simscape™ Electrical™ 模型。有关详细信息，请参阅 `subcircuit2ssc`。

### 方程变量

SPICE NMOS 模块方程的变量包括：

- 通过为 SPICE NMOS 模块指定参数来定义的变量。某些参数的可见性取决于您为其他参数设置的值。有关详细信息，请参阅参数。
- 几何调整变量，这些变量取决于您使用 SPICE NMOS 模块参数指定的若干值。有关详细信息，请参阅几何调整变量。
- 温度 *T*，默认值为 `300.15` `K`。您可以通过为 SPICE NMOS 模块指定参数，或同时为 SPICE NMOS 模块和 Environment Parameters 模块指定参数来使用不同的值。有关详细信息，请参阅晶体管温度。
- 最小电导 *GMIN*，默认值为 `1e-12` `1/Ohm`。您可以通过为 Environment Parameters 模块指定参数来使用不同的值。有关详细信息，请参阅最小导通。
- 热电压 *Vtn*。有关详细信息，请参阅热电压。

**几何调整变量**

SPICE N 沟道 MOSFET 模型方程中的若干变量考虑该模块所表示器件的几何结构。这些几何调整变量取决于您通过指定 SPICE NMOS 模块参数所定义的变量。几何调整变量取决于以下变量：

- *AREA* — 器件面积
- *SCALE* — 并联连接的器件数
- 关联的未调整变量

该表包含几何调整变量及其定义方程。

| 变量 | 描述 | 方程 |
| --- | --- | --- |
| *KPd* | 几何调整跨导 | KPd=KP\*AREA\*SCALE |
| *ISd* | 几何调整体饱和电流 | ISd=IS\*AREA\*SCALE |
| *JSd* | 几何调整体结饱和电流密度 | JSd=JS\*AREA\*SCALE |
| *CBDd* | 几何调整零偏体-漏电容 | CBDd=CBD\*AREA\*SCALE |
| *CBSd* | 几何调整零偏体-源电容 | CBSd=CBS\*AREA\*SCALE |
| *CGSOd* | 几何调整栅-源交叠电容 | CGSOd=CGSO\*AREA\*SCALE |
| *CGDOd* | 几何调整栅-漏交叠电容 | CGDOd=CGDO\*AREA\*SCALE |
| *CGBOd* | 几何调整栅-体交叠电容 | CGBOd=CGBO\*AREA\*SCALE |
| *CJ* | 几何调整每结面积的底部电容 | CJd=CJ\*AREA\*SCALE |
| *CJSW* | 几何调整每结周长的侧壁电容 | CJSWd=CJSW\*AREA\*SCALE |
| *RDd* | 几何调整漏电阻 | RDd=RDAREA\*SCALE |
| *RSd* | 几何调整源电阻 | RSd=RSAREA\*SCALE |
| *RSHd* | 几何调整薄层电阻 | RSHd=RSHAREA\*SCALE |

**晶体管温度**

定义晶体管温度 *T* 有两种不同选项：

- `Fixed temperature` — 当 SPICE NMOS 模块的 **温度** 设置中的 **使用以下方式建模温度依赖性** 参数设置为 `Fixed temperature` 时，该模块使用独立于电路温度的温度。对于此模型，该模块将 *T* 设置为等于 *TFIXED*。
- `Device temperature` — 当 SPICE NMOS 模块的 **温度** 设置中的 **使用以下方式建模温度依赖性** 参数设置为 `Device temperature` 时，该模块使用取决于电路温度的温度。对于此模型，该模块将温度定义为

  T=TC+TOFFSET

  其中：

  - *TC* 是电路温度。

    如果电路中没有 Environment Parameters 模块，则 *TC* 等于 300.15 K。

    如果电路中有一个 Environment Parameters 模块，则 *TC* 等于您在 Environment Parameters 模块的 **SPICE** 设置中为 **温度** 参数指定的值。**温度** 参数的默认值为 `300.15` `K`。
  - *TOFFSET* 是本地电路温度偏移。

**最小导通**

最小电导 *GMIN* 的默认值为 `1e–12` `1/Ohm`。要指定其他值：

1. 如果电路中尚无 Environment Parameters 模块，请添加一个。
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

这些表展示了 SPICE NMOS 模块如何根据您指定的值确定其部分参数。

**漏电阻**

| 参数值 | | | 几何调整晶体管漏电阻 |
| --- | --- | --- | --- |
| **漏电阻, RD** | **薄层电阻, RSH** | **漏区方块数, NRD** |
| `NaN` | `NaN` | `NaN` | 0 |
| `NaN` | *RSH* | `NaN` | 0 |
| `NaN` | `NaN` | *NRD* | 0 |
| *RD* | `NaN` 或 *RSH* | `NaN` 或 *NRD* | *RDd* |
| `NaN` | *RSH* | *NRD* | *RSHd*\**NRD* |

**源电阻**

| 参数值 | | | 几何调整晶体管源电阻 |
| --- | --- | --- | --- |
| **源电阻, RS** | **薄层电阻, RSH** | **源区方块数, NRS** |
| `NaN` | `NaN` | `NaN` | 0 |
| `NaN` | *RSH* | `NaN` | 0 |
| `NaN` | `NaN` | *NRS* | 0 |
| *RS* | `NaN` 或 *RSH* | `NaN` 或 *NRS* | *RSd* |
| `NaN` | *RSH* | *NRS* | *RSHd*\**NRS* |

**跨导和表面迁移率**

| 参数值 | | | 几何调整跨导（level 1），单位 A/V2 | 几何调整跨导（level 3），单位 A/V2 | 表面迁移率（level 3），单位 cm2/s/V |
| --- | --- | --- | --- | --- | --- |
| **氧化层厚度, TOX** | **表面迁移率, U0** | **跨导, KP** |
| `NaN` | `NaN` | `NaN` | `2e-5`（默认值） | `2e-5`（默认值） | `600`（默认值） |
| `NaN` | `NaN` | `KP` | `KPd` | `KPd` | `600` |
| `NaN` | `U0` | `NaN` | `2e-5` | *UO*\**EPXox*/`1e-7` | `U0` |
| `NaN` | `U0` | `KP` | `KPd` | `KPd` | `U0` |
| *TOX* | `NaN` | `NaN` | `600`\**EPXox*/*TOX* | `600`\**EPXox*/*TOX* | `600` |
| *TOX* | `NaN` | `KP` | `KPd` | `KPd` | `600` |
| *TOX* | `U0` | `NaN` | *UO*\**EPXox*/*TOX* | *UO*\**EPXox*/*TOX* | `U0` |
| *TOX* | `U0` | `KP` | `KPd` | `KPd` | `U0` |

**氧化层厚度和阈值电压**

| 参数值 | | | | 表面电势, PHI (level 1), 单位 V | 阈值电压, VTO (level 1), 单位 V | 表面电势, PHI (level 3), 单位 V | 阈值电压, VTO (level 3), 单位 V |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **氧化层厚度, TOX** | **衬底掺杂, NSUB** | **表面电势, PHI** | **阈值电压, VTO** |
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

### 体-源二极管模型

该表显示了定义体-源电流 *Ibs* 与体-源电压 *Vbs* 之间关系的方程。在适用的情况下，模型参数首先会针对温度进行调整。有关详细信息，请参阅温度依赖性。

| *Vbs* 值的适用范围 | 对应的 *Ibs* 方程 |
| --- | --- |
| Vbs>80\*Vtn | Ibs=ISbs\*((VbsVtn−79)e80−1)+Vbs\*Gmin |
| 80Vtn≥Vbs | Ibs=ISbs\*(eVbs/Vtn−1)+Vbs\*Gmin |

其中：

- *ISbs* 是体饱和电流，满足：如果：

  - JSd≠0 且 AS≠0，ISbs=JSd\*AS。

    其中：

    - *JSd* 是几何调整体结饱和电流密度。
    - *AS* 是源面积。
  - 如果 JSd=0 或 AS=0，ISbs=ISd，其中 *ISd* 是几何调整体饱和电流。
- *Vtn* 是热电压。有关详细信息，请参阅热电压。
- *Gmin* 是最小电导。有关详细信息，请参阅最小导通。

### 体-漏二极管模型

该表显示了定义体-漏电流 *Ibd* 与体-漏电压 *Vbd* 之间关系的方程。在适用的情况下，模型参数首先会针对温度进行调整。有关详细信息，请参阅温度依赖性。

| *Vbd* 值的适用范围 | 对应的 *Ibd* 方程 |
| --- | --- |
| Vbd>80\*Vtn | Ibd=ISbd\*((VbdVtn−79)e80−1)+Vbd\*Gmin |
| 80Vtn≥Vbd | Ibd=ISbd\*(eVbd/Vtn−1)+Vbd\*Gmin |

其中：

- *ISbd* 是体漏电流，满足：

  - 如果 JSd≠0 且 AD≠0，ISbd=JSd\*AD。

    其中：

    - *JSd* 是几何调整体结饱和电流密度。
    - *AD* 是漏面积。
  - 如果 JSd=0 或 AD=0，ISbd=ISd，其中 *ISd* 是几何调整体饱和电流。
- *Vtn* 是热电压。有关详细信息，请参阅热电压。
- *Gmin* 是最小电导。有关详细信息，请参阅最小导通。

### Level 1 漏极电流模型

此表显示了正常模式（*Vds* ≥ 0）下漏极电流 *Id* 与漏极-源极电压 *Vds* 之间的关系。在适用情况下，模型参数首先根据温度进行调整。

**正常模式**

| *Vgs* 和 *Vds* 值的适用范围 | 对应的 *Id* 方程 |
| --- | --- |
| Vgs-Von≤0 | Id=0 |
| 0<Vgs-Von≤Vds | Id=BETA\*(Vgs−Von)2(1+LAMBDA\*Vds)2 |
| 0<Vds<Vgs-Von | Id=BETA\*Vds((Vgs-Von)-Vds2)(1+LAMBDA\*Vds) |

其中：

- *Von* 取决于
  *Vbs* 和
  *PHI*。

  | *Vbs* 和 *PHI* 值的适用关系 | 对应的 *Von* 方程 |
  | --- | --- |
  | Vbs≤0 | Von=MTYPE\*VBI+GAMMAPHI−Vbs |
  | 0<Vbs≤2\*PHI | Von=MTYPE\*VBI+GAMMA(PHI−Vbs2PHI) |
  | Vbs>2\*PHI | Von=MTYPE\*VBI |
- *MTYPE* 为 1。
- *BETA* 为 BETA=(KPd\*WIDTH)/(LENGTH−2\*LD)
- *KP* 为：

  - 如果此参数具有数值，则为 **Transconductance, KP**。
  - 如果 **Transconductance, KP** 为 `NaN`，并且您同时为 **Oxide thickness, TOX** 和 **Substrate doping, NSUB** 参数指定值，则为 U0\*3.9\*ε0/TOX。
- *WIDTH* 是沟道宽度。
- *LENGTH* 是沟道长度。
- *LD* 是横向扩散。
- *VBI* 是模块在计算中使用的内建电压值。该值是温度的函数。有关详细定义，请参见温度依赖性。
- *PHI* 为：

  - 如果此参数具有数值，则为 **Surface potential, PHI**。
  - 如果 **Surface potential, PHI** 为 `NaN`，并且您同时为 **Oxide thickness, TOX** 和 **Substrate doping, NSUB** 参数指定值，则为 2\*kTmeas/q\*log(NSUB/ni)。
- *LAMBDA* 是沟道调制。
- *GAMMA* 为：

  - 如果此参数具有数值，则为 **Bulk threshold, GAMMA**。
  - 如果 **Bulk threshold, GAMMA** 为 `NaN`，并且您同时为 **Oxide thickness, TOX** 和 **Substrate doping, NSUB** 参数指定值，则为 TOX\*2\*11.7\*ε0\*q\*NSUB/(3.9\*ε0)。
- *ε0* 是自由空间介电常数，8.854214871e-12 F/m。
- *ni* 是本征硅的载流子浓度，1.45e10 cm-3。

此表显示了反向模式（*Vds* < 0）下漏极电流 *Id* 与漏极-源极电压 *Vds* 之间的关系。在适用情况下，模型参数首先根据温度进行调整。

**反向模式**

| *Vgd* 和 *Vds* 值的适用范围 | 对应的 *Id* 方程 |
| --- | --- |
| Vgd-Von≤0 | Id=0 |
| 0<Vgd-Von≤−Vds | Id=−BETA(Vgd−Von)2(1−LAMBDA\*Vds)/2 |
| 0<−Vds<Vgd−Von | Id=BETA\*Vds((Vgd-Von)+Vds/2)(1−LAMBDA\*Vds) |

*Von* 取决于
*Vbd* 和
*PHI*。

| *Vbs* 和 *PHI* 值的适用关系 | 对应的 *Von* 方程 |
| --- | --- |
| Vbd≤0 | Von=MTYPE\*VBI+GAMMAPHI−Vbd |
| 0<Vbd≤2\*PHI | Von=MTYPE\*VBI+GAMMA(PHI−Vbs2PHI) |
| Vbd>2\*PHI | Von=MTYPE\*PHI |

### Level 3 漏极电流模型

在根据温度调整适用模型参数之后，该模块为正常模式（Vds≥0）下的漏极电流 *Ids* 提供以下模型。

IDS=IDS0\*ScaleVMAX\*ScaleLChan\*ScaleINV

其中：

- *IDS0* 是基本漏极电流模型。
- *ScaleVMAX* 是速度饱和缩放。
- *ScaleLChan* 是沟道长度调制缩放。
- *ScaleINV* 是弱反型缩放。

该模块对反向模式（Vds<0）下的漏极电流使用相同模型，并进行以下替换：

Vbs≡Vbs−Vds

Vgs≡Vgs−Vds

Vds≡−Vds

**基本漏极电流模型**

漏极电流 *Ids* 与漏极-源极电压 *Vds* 之间的关系为

IDS0=BETA\*Fgate\*(VGSX−VTH−1+FB2\*VDSX)\*VDSX

其中：

- *BETA* 按 Level 1 漏极电流模型所述计算。
- *FGATE* 计算如下

  Fgate=11+THETA\*(Vgsx−VTH)

  其中：

  - *THETA* 对迁移率与栅极-源极电压的依赖关系建模。
  - Vgsx=max(VGS,Von)
- 如果您为 **Fast surface state density, NFS** 参数指定非零值，则模块使用以下方程计算 *Von*：

  Von=VTH+xnVT

  否则，

  Von=VTH
- 模块按如下方式计算 *xn*：

  xn=1+q\*NFSCOX+(GAMMA\*Fs\*Vbulk+Fn\*VbulkWIDTH)2\*Vbulk
- 模块按如下方式计算 *Vbulk*：

  - 如果

    VBS≤0，

    Vbulk=PHI−VBS.
  - 否则，模块按如下方式计算 *Vbulk*：

    Vbulk=PHI(1+VBS2\*PHI)2
- 热电压，使得

  VT=kTq
- 模块使用以下方程计算 *VTH*：

  VTH=VBI−8.15e−22\*ETACOX\*(LENGTH−2\*LD)3\*VDS​​​​​​​​​​            +GAMMA\*Fs\*Vbulk+Fn\*Vbulk

  有关模块如何计算 *VBI* 的信息，请参见温度依赖性。
- *ETA* 是 **Vds dependence threshold volt, ETA**。
- COX=εoxTOX,

  其中 *εox* 是氧化层介电常数，*TOX* 是 **Oxide thickness, TOX**。
- 如果您为 **Junction depth, XJ** 参数指定非零值，并为 **Substrate doping, NSUB** 参数指定值，则模块使用以下方程计算 *Fs*：

  α=2εsiqNSUB

  XD=α

  wc=.0631353+.8013292\*XD\*VbulkXJ−.01110777\*(XD\*VbulkXJ)2+LDXJ

  Fs=1−(wc\*1−(XD\*VbulkXJ+XD\*Vbulk)2−LDXJ)

  其中 *εsi* 是硅的介电常数。

  否则，

  Fs=1
- 模块按如下方式计算 *FB*：

  FB=GAMMA\*Fs4\*Vbulk+Fn
- 模块按如下方式计算 *Fn*：

  Fn=DELTA\*π\*εsi2\*COX\*WIDTH
- *DELTA* 是阈值上的宽度效应。
- *VDSX* 是 *VDS* 与饱和电压 *Vdsat* 中的较小者。

  - 如果您为 **Max carrier drift velocity, VMAX** 参数指定正值，则模块使用以下方程计算 *Vdsat*：

    Vdsat=Vgsx−VTH1+FB+(LENGTH−2\*LD)\*VMAXUO\*Fgate             −(Vgsx−VTH1+FB)2+((LENGTH−2\*LD)\*VMAXUO\*Fgate)2

    否则，模块按如下方式计算 *Vdsat*：

    Vdsat=Vgsx−VTH1+FB

**速度饱和缩放**

如果您为 **Max carrier drift velocity, VMAX** 参数指定正值，则模块按如下方式计算 *ScaleVMAX*：

ScaleVMAX=11+UO\*Fgate(LENGTH−2\*LD)\*VMAX\*VDSX

否则，

ScaleVMAX=1

**沟道长度调制缩放**

如果模块满足以下所有条件，则模块缩放漏极电流以考虑沟道长度调制：

- VDS>Vdsat
- **Max carrier drift velocity, VMAX** 小于或等于零，或 *α* 非零。

模块使用以下方程缩放漏极电流：

ScaleLChan=11−Δl(LENGTH−2\*LD)

为计算 Δl，模块：

1. 计算中间值 Δl0。

   - 如果您为 **Max carrier drift velocity, VMAX** 参数指定正值，则模块将中间值 *gdsat* 计算为 1e-12 与以下方程结果中的较大者：

     IDS0\*(1−11+Scalegdsat\*VDSX)\*Scalegdsat

     其中：

     Scalegdsat=UO\*Fgate(LENGTH−2\*LD)\*VMAX

     然后，模块使用以下方程计算中间值 Δ*l0*：

     Δl0=(KA\*IDS2\*(LENGTH−2\*LD)\*gdsat)2+KA\*(VDS−Vdsat)            −KA\*IDS2\*(LENGTH−2\*LD)\*gdsat

     其中

     KA=KAPPA\*α.
   - 否则，模块使用以下方程将中间值 Δl0 计算为

     Δl=KA\*(VDS−Vdsat)
2. 模块检查穿通并计算 Δl。

   - 如果

     Δl0>(LENGTH−2\*LD)/2，

     则模块使用以下方程计算 Δl：

     Δl=(1−(LENGTH−2\*LD)4\*Δl0)\*(LENGTH−2\*LD)
   - 否则，

     Δl=Δl0.

**弱反型缩放**

如果 *VGS* 小于 *Von*，则模块使用以下方程计算 *ScaleINV*：

ScaleINV=eVgs−Vonxn\*VT

否则，

ScaleINV=1

### 结电荷模型

模块对结重叠电荷和体结电荷建模。

**结重叠电荷**

模块计算以下结重叠电荷：

- QGS=CGSOd\*WIDTH\*Vgs

  其中：

  - *QGS* 是栅极-源极重叠电荷。
  - *CGSOd* 是几何调整后的栅极-源极重叠电容。
  - *WIDTH* 是沟道宽度。
- QGD=CGDOd\*WIDTH\*Vgd

  其中：

  - *QGD* 是栅极-漏极重叠电荷。
  - *CGDOd* 是几何调整后的栅极-漏极重叠电容。
- QGB=CGBOd\*(LENGTH−2\*LD)\*Vgb

  其中：

  - *QGB* 是栅极-体重叠电荷。
  - *CGBOd* 是几何调整后的栅极-体重叠电容。
  - *LENGTH* 是沟道长度。
  - *LD* 是横向扩散。

**体结电荷**

此表显示了体-漏底部结电荷 *Qbottom* 与结电压 *Vbd* 之间的关系。在适用情况下，模型参数首先根据温度进行调整。

| *Vbd* 值的适用范围 | 对应的 *Qbottom* 方程 |
| --- | --- |
| Vbd<FC\*PB | Qbottom=CBDd\*PB\*(1-(1-VbdPB)1−MJ)1−MJ 如果 CBDd>0  Qbottom=CJd\*AD\*PB\*(1-(1-VbdPB)1−MJ)1−MJ 否则。 |
| Vbd≥FC\*PB | Qbottom=CBDd\*                       (F1+F3\*(Vbd-FC\*PB)+MJ\*(Vbd2-(FC\*PB)2)2\*PBF2) 如果 CBDd>0  Qbottom=CJd\*AD\*                       (F1+F3\*(Vbd-FC\*PB)+MJ\*(Vbd2-(FC\*PB)2)2\*PBF2) 否则。 |

其中：

- *PB* 是体结电势。
- *FC* 是电容系数。
- *CBDd* 是几何调整后的零偏置体-漏电容。
- *CJd* 是几何调整后的每结面积底部电容。
- *AD* 是漏极面积。
- *MJ* 是底部梯度系数。
- F1=PB\*(1-(1-FC)1−MJ)1−MJ
- F2=(1-FC)1+MJ
- F3=1-FC\*(1+MJ)

为计算体-源底部结电荷，模块替换上表中的变量。模块替换：

- 用 *Vbs* 替换 *Vbd*
- 用 *AS* 替换 *AD*
- 用 *CBSd* 替换 *CBDd*

此表显示了体-漏侧壁结电荷 *Qsidewall* 与结电压 *Vbd* 之间的关系。在适用情况下，模型参数首先根据温度进行调整。

| *Vbd* 值的适用范围 | 对应的 *Qsidewall* 方程 |
| --- | --- |
| Vbd<FC\*PB | Qsidewall=CJSWd\*PD\*PB\*(1-(1-VbdPB)1−MGSW)1−MGSW |
| Vbd≥FC\*PB | Qsidewall=CJSWd\*PD\*                      (F1+F3\*(Vbd-FC\*PB)+MGSW\*(Vbd2-(FC\*PB)2)2\*PBF2) |

其中：

- *CJSWd* 是几何调整后的每结周长侧壁电容。
- *PD* 是漏极周长。
- *MGSW* 是侧壁梯度系数。
- F1=PB\*(1-(1-FC)1−MJSW)1−MJSW
- F2=(1-FC)1+MJSW
- F3=1-FC\*(1+MJSW)

为计算体-源侧壁结电荷和侧壁结电压，模块替换上表中的变量。模块替换：

- 用 *Vbs* 替换 *Vbd*
- 用 *PS* 替换 *PD*

### 电容模型

SPICE NMOS 模块允许您以三种不同方式对晶体管电容模型建模：

- 无本征电容模型
- Meyer 栅极电容模型
- 电荷守恒电容模型

**Meyer 栅极电容模型**

此表显示了晶体管工作区与栅极-体、栅极-漏极和栅极-源极电容之间的关系。

| 工作区 | 栅极-体 *Cgb*、栅极-漏极 *Cgd* 和栅极-源极 *Cgs* 方程 | |
| --- | --- | --- |
| 积累区，Vgb<VFB | Cgb=CoxtCgd=0Cgs=0 | |
| 耗尽区，Vgs<VTH | Cgb=Coxt1+4GAMMA2\*(Vgb−VFB)Cgd=0Cgs=0 | |
| 饱和区，Vgs−VTH<Vds | 如果 Vds<Vsatmin 则： | 如果 Vds≥Vsatmin 则： |
| | Cgb=0Cgd=23(Coxt−Cgb)(1−(Vsatmin)2(2Vsatmin−Vds)2)Cgs=23(Coxt−Cgb)(1−(Vsatmin−Vds)2(2Vsatmin−Vds)2) | Cgb=0Cgd=0Cgs=23(Coxt−Cgb) |
| 线性区，Vgs−VTH>Vds | Cgb=0Cgd=23(Coxt−Cgb)\*(1−(Vgs−VTH)2(2\*(Vgs−VTH)−Vds)2)Cgs=23(Coxt−Cgb)\*(1−(Vgs−VTH−Vds)2(2\*(Vgs−VTH)−Vds)2) | |

其中：

- Coxt=WIDTH\*(LENGTH−2\*LD)\*COX\*AREA\*SCALE
- VFB=VBI\*MTYPE−PHI 是平带电压。
- *Vsatmin* 是最小饱和电压。它是一个预定义参数，等于 `1` `V`。

这些方程在耗尽区和积累区之间连续，而在耗尽区和反型区之间不连续。其他 SPICE 工具在反型区和耗尽区之间应用平滑函数。

Cgb=WIDTH\*LENGTH\*COX(1+4GAMMA2\*(VTH−Vbs−VFB))m\*smoothingsmoothing=1(1+4GAMMA2\*(Vgs−VTH))m

其中 *m* 是预定义平滑常数。

**电荷守恒电容模型**

此表显示了晶体管工作区与 level 1 MOS 的栅极、体、沟道、漏极和源极电荷之间的关系。

| 工作区 | Level-1 电荷方程 |
| --- | --- |
| 积累区，Vgb<VFB | Qg=Coxt\*(Vgb−VFB)Qb=−Coxt\*(Vgb−VFB)Qc=0Qd=0Qs=Qc−Qd |
| 耗尽区，Vgs<VTH | Qg=−0.5\*Coxt\*GAMMA2\*(1−1+4GAMMA2\*(Vgb−VFB))Qb=0.5\*Coxt\*GAMMA2\*(1−1+4GAMMA2\*(Vgb−VFB))Qc=0Qd=0Qs=Qc−Qd |
| 饱和区，Vgs−VTH<Vds | Qg=Coxt\*(Vgs−VFB−PHI−Vgs−VTH3)Qb=−Coxt\*(VTH−VFB−PHI)Qc=−Coxt\*(Vgs−VTH−Vgs−VTH3)Qd=0Qs=Qc−Qd |
| 线性区，Vgs−VTH>Vds | Qg=Coxt\*(Vgs−VFB−PHI−Vds2+Vds212(Vgs−VTH−0.5Vds))Qb=−Coxt\*(VTH−VFB−PHI)Qc=−Coxt\*(Vgs−VTH−Vds2+Vds212(Vgs−VTH−0.5Vds))Qd=−Coxt\*(Vgs−VTH2−3Vds4+Vds28(Vgs−VTH−0.5Vds))Qs=Qc−Qd |

其中：

- Qc=−(Qg+Qb)=Qd+Qs 是沟道中的电荷。
  *Qc* 需要在 *Qd* 和 *Qs* 之间分配。

其中：

- *Qg* 是栅极电荷。
- *Qb* 是体电荷。
- *Qd* 是漏极电荷。
- *Qs* 是源极电荷。
- Qc=−(Qg+Qb)=Qd+Qs 是沟道中的电荷。
  *Qc* 需要在 *Qd* 和 *Qs* 之间分配。

此表显示了晶体管工作区与 level-3 MOS 的栅极、体、沟道、漏极和源极电荷之间的关系。

| 工作区 | Level-3 电荷方程 |
| --- | --- |
| 积累区，Vgb<VFB | Qg=Coxt\*(Vgb−VFB)−SF1+SF2Qb=−Coxt\*(Vgb−VFB)−SF1+SF2Qc=0Qd=0Qs=Qc−Qd |
| 耗尽区，Vgs<VTH | Qg=−0.5\*Coxt\*GAMMA2\*(1−1+4GAMMA2\*(Vgb−VFB))−SF1+SF2Qb=0.5\*Coxt\*GAMMA2\*(1−1+4GAMMA2\*(Vgb−VFB))+SF1−SF2Qc=0Qd=0Qs=Qc−Qd |
| 饱和区，Vgs−VTH<Vds | Qg=Coxt\*(Vgs−VFB−PHI+ETA\*Vdsat−Vdsat2+1+FB12\*Fi\*Vdsat2)Qb=−Coxt\*(VTH−VFB−PHI+ETA\*Vdsat−Fb2\*Vds−FB\*(1+FB)12\*Fi\*Vdsat2)Qc=−Coxt\*(Vgs−VTH−1+FB2\*Vdsat+(1+FB)212\*Fi\*Vdsat2)Qd=0Qs=Qc−Qd |
| 线性区，Vgs−VTH>Vds | Qg=Coxt\*(Vgs−VFB−PHI+ETA\*Vds−Vds2+1+FB12\*Fi\*Vds2)Qb=−Coxt\*(VTH−VFB−PHI+ETA\*Vds+FB2\*Vds−FB\*(1+FB)12\*Fi\*Vds2)Qc=−Coxt\*(Vgs−VTH−1+FB2\*Vds+(1+FB)212\*Fi\*Vds2)Qd=−Coxt\*(Vgs−VTH2−3(1+FB)2\*Vds+(1+FB)28\*Fi\*Vds2)Qs=Qc−Qd |

其中：

- *Vdsat* 是饱和电压
- *FB* 是体效应系数
- *ETA* 是漏极-源极电压阈值系数
- Fi=Vgs−VTH−1+FB2\*Vds
- SF1=−0.5\*Coxt\*GAMMA2\*(1−(1+4GAMMA2\*2(VTH−Vbs−VFB))0.5) 和 SF2=Coxt\*(VTH−VFB−PHI) 是耗尽区与积累区之间的平滑因子，有助于收敛。

### 温度依赖性

晶体管温度的函数跨导为

KP(T)=KPd(TTmeas)3/2

其中：

- *KPd* 是经几何调整的跨导。
- *T* 是晶体管温度。有关更多信息，请参阅晶体管温度。
- *Tmeas* 是参数提取温度。

作为晶体管温度函数的表面势为

PHI(T)=TTmeas(PHI+kTmeasq(log(Tmeas300.15)3+qk(1.115300.15−EGTmeasTmeas)))                          −kTq(log(T300.15)3+qk(1.115300.15−EGTT))

其中：

- *PHI* 是表面势。
- *k* 是玻尔兹曼常数。
- *q* 是电子上的基本电荷，1.6021918e-19 C。
- *EG* 是激活能，满足：

  - EGTmeas=1.16eV-(7.02e-4\*Tmeas2)/(Tmeas+1108)
  - EGT=1.16eV-(7.02e-4\*T2)/(T+1108)

作为晶体管温度函数的内建电压为

VBI(T)=VTO+MTYPE\*(PHI(T)−PHI2−GAMMAPHI)                               +EGTmeas−EGT2

其中：

- *VBI* 是内建电压。
- *VTO* 是阈值电压。*VTO* 取决于你在 **Threshold voltage, VTO** 参数中指定的值，该参数位于 **DC currents** 设置中。如果指定数值，*VTO* 将按该值计算。如果指定非数值 (`NAN`)，并且你为 **Process** 设置中的 **Oxide thickness, TOX** 和 **Substrate doping, NSUB** 两个参数都指定了数值，则 *VTO* 的计算方式为 Φ−3.25+EGTmeas/2+MTYPE\*PHI/2−NSS\*q\*TOX/(3.9\*ε0)+MTYPE\*(GAMMA\*PHI+PHI)，其中：

  - *Φ* 取决于栅极类型，你使用 **Gate type, TPG** 参数指定该类型。如果指定 `Aluminum (0)`，则 Φ=3.2。否则，Φ=3.25+EGTmeas/2−MTYPE\*TPG\*EGTmeas/2，其中：

    - *MTYPE* 是晶体管类型。对于 N 沟道 MOSFET，*MTYPE* = 1。
    - *TPG* 表示栅极类型，并且还取决于你为 **Process** 设置中的 **Gate type, TPG** 参数指定的选项。如果指定

      - `Opposite of substrate (1)` — *TPG* = 1
      - `Same as substrate (-1)` — *TPG* = -1
  - *NSS* 是表面态密度。
  - *TOX* 是氧化层厚度。
  - *ε0* 是真空介电常数。
  - *GAMMA* 是体阈值。*GAMMA* 取决于你为 **DC currents** 设置中的 **Bulk threshold, GAMMA** 参数指定的值。如果指定数值，*GAMMA* 将按该值计算。如果指定非数值 (`NAN`)，并且你为 **Process** 设置中的 **Oxide thickness, TOX** 和 **Substrate doping, NSUB** 两个参数都指定了数值，则 *VTO* 的计算方式为 TOX\*2\*11.7\*ε0\*q\*NSUB/(3.9\*ε0)，其中 *NSUB* 是衬底掺杂。

作为晶体管温度函数的体饱和电流为

IS(T)=ISd\*e−qEGTND\*kT + qEGTmeasND\*kTmeas

其中：

- *ISd* 是经几何调整的体饱和电流。
- *ND* 是发射系数。

作为晶体管温度函数的体结饱和电流密度为

JS(T)=JSd\*e−qEGTND\*kT + qEGTmeasND\*kTmeas

其中 *JSd* 是经几何调整的体结饱和电流密度。

作为晶体管温度函数的体结电势为

PB(T)=PB+kTmeasq(log(Tmeas300.15)3+qk(1.115300.15−EGTmeasT))TmeasT                         −kTq(log(T300.15)3+qk(1.115300.15−EGTT))

其中 *PB* 是体结电势。

作为晶体管温度函数的体-漏结电容为

CBD(T)=CBDdpbo+MJ\*(4\*104\*(T−300.15)\*pbo−(PB(T)−pbo))pbo+MJ\*(4\*104\*(Tmeas−300.15)\*pbo−(PB−pbo))

其中：

- *CBDd* 是经几何调整的零偏置体-漏电容。
- *MJ* 是底部梯度系数。
- pbo=PB+kTmeasq(log(Tmeas300.15)3+qk(1.115300.15−EGTmeasT))Tmeas300.15

该模块使用 *CBD(T)* 方程计算：

- 体-源结电容，通过将经几何调整的零偏置体-源电容 *CBSd* 替换 *CBDd*。
- 底部结电容，通过将经几何调整的每结面积底部电容 *CJd* 替换 *CBDd*。

侧壁结电容 *CJSW* 与晶体管温度 *T* 之间的关系为

CJSW(T)=CJSWdpbo+MJSW\*(4\*104\*(T−300.15)\*pbo−(PB(T)−pbo))pbo+MJSW\*(4\*104\*(Tmeas−300.15)\*pbo−(PB−pbo))

其中：

- *CJSWd* 是每结周长经侧边几何调整的侧壁电容。
- *MJSW* 是侧边梯度系数。
