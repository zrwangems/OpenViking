---
type: simulink-block
title: 'SPICE PJFET'
family: 'additional-components'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Semiconductors'
documentation_page: 'spicepjfet'
documentation_source_path: 'ref/spicepjfet.html'
language: zh-CN
chinese_source: worker-translation
---

# SPICE PJFET

## 端口

### 守恒

### **gx** — 栅极端子电气

与晶体管栅极端子相关联的电气守恒端口。

### **dx** — 漏极端子电气

与晶体管漏极端子相关联的电气守恒端口。

### **sx** — 源极端子电气

与晶体管源极端子相关联的电气守恒端口。

## 参数

### 主要

### **器件面积, AREA** — 器件面积 `1.0` `m^2`（默认值） | 正标量

晶体管面积。值必须大于 `0`。

### **并联器件数, SCALE** — 并联器件数 `1`（默认值） | 正整数

该模块表示的并联晶体管数量。值必须是大于 `0` 的整数。

### **阈值电压, VTO** — 阈值电压 `-2` `V`（默认值） | 标量

源-栅电压高于该值时，晶体管产生非零漏极电流。

### **跨导, BETA** — 沟道调制 `1e-4` `A/m^2/V^2`（默认值） | 非负标量

漏极电流对栅极电压的导数。值必须大于或等于 `0`。

### **沟道调制, LAMBDA** — 沟道调制 `0` `1/V`（默认值） | 标量

沟道调制。

### **饱和电流, IS** — 饱和电流 `1e-14` `A/m^2`（默认值） | 非负标量

对于非常大的反向偏置水平，栅极电流方程渐近趋近的电流大小。值必须大于或等于 `0`。

### **漏极电阻, RD** — 串联电阻 `0.01` `m^2*Ohm`（默认值） | 非负标量

晶体管漏极电阻。值必须大于或等于 `0`。

### **源极电阻, RS** — 串联电阻 `0.0001` `m^2*Ohm`（默认值） | 非负标量

晶体管源极电阻。值必须大于或等于 `0`。

### **发射系数, N** — 发射系数 `1`（默认值） | 正标量

晶体管发射系数或理想因子。值必须大于 `0`。

### 结电容

### **结电容建模** — 结电容模型 `No`（默认值） | `Yes`

用于对结电容建模的选项：

- `No` — 不要在模型中包含结电容。
- `Yes` — 指定零偏结电容、结电势、梯度系数、正向偏置耗尽电容系数和渡越时间。

#### 依赖关系

选择 `Yes` 会显示相关参数。

### **零偏 GS 电容, CGS** — 零偏结电容 `0` `F/m^2`（默认值） | 非负标量

放置在栅极和源极之间的电容值。值必须大于或等于 `0`。

#### 依赖关系

仅当为 **结电容建模** 参数选择 `Yes` 时，此参数才可见。

### **零偏 GD 电容, CGD** — 零偏结电容 `0` `F/m^2`（默认值） | 非负标量

放置在栅极和漏极之间的电容值。值必须大于或等于 `0`。

#### 依赖关系

仅当为 **结电容建模** 参数选择 `Yes` 时，此参数才可见。

### **结电势, VJ** — 结电势 `1` `V`（默认值） | *VJ* > 0.01 | 标量

结电势, *VJ*。值必须大于 `0.01` `V`。

#### 依赖关系

仅当为 **结电容建模** 参数选择 `Yes` 时，此参数才可见。

### **梯度系数, M** — 梯度系数 `0.5`（默认值） | 0 < *M* < 0.9 | 标量

梯度系数, *M*。值必须大于 `0` 且小于 `0.9`。

#### 依赖关系

仅当为 **结电容建模** 参数选择 `Yes` 时，此参数才可见。

### **电容系数, FC** — 电容系数 `0.5`（默认值） | 0 ≤ *FC* < 0.95 | 标量

拟合系数 *FC*，用于量化耗尽电容随所施加电压的降低。值必须大于或等于 `0` 且小于 `0.95`。

#### 依赖关系

仅当为 **结电容建模** 参数选择 `Yes` 时，此参数才可见。

### **指定初始条件** — 初始条件模型 `No`（默认值） | `Yes`

用于指定初始条件的选项：

- `No` — 不要为模型指定初始条件。
- `Yes` — 指定晶体管初始电压。

  **注意**

  SPICE PJFET 模块将初始晶体管电压施加在结电容两端，而不是端口两端。

#### 依赖关系

仅当为 **结电容建模** 参数选择 `Yes` 时，此参数才可见。

为此参数选择 `Yes` 会显示 **初始条件电压, ICVDS** 和 **初始条件电压, ICVGS** 参数。

### **初始条件电压, ICVDS** — 初始电压 `0` `V`（默认值） | 标量

仿真开始时的漏-源电压。

#### 依赖关系

仅当为 **结电容建模** 参数选择 `Yes`，且为 **指定初始条件** 参数选择 `Yes` 时，此参数才可见。

### **初始条件电压, ICVGS** — 初始电压 `0` `V`（默认值） | 标量

仿真开始时的栅-源电压。

#### 依赖关系

仅当为 **结电容建模** 参数选择 `Yes`，且为 **指定初始条件** 参数选择 `Yes` 时，此参数才可见。

### 温度

### **使用以下方式对温度依赖性建模** — 温度依赖性模型 `Device temperature`（默认值） | `Fixed temperature`

选择以下选项之一来对晶体管温度依赖性建模：

- `Device temperature` — 使用器件温度对温度依赖性建模。
- `Fixed temperature` — 使用与电路温度无关的温度对温度依赖性建模。

有关详细信息，请参阅晶体管温度。

#### 依赖关系

选择 `Device temperature` 会显示 **本地电路温度偏移, TOFFSET** 参数。选择 `Fixed temperature` 会显示 **固定电路温度, TFIXED** 参数。

### **饱和电流温度指数, XTI** — 饱和电流温度指数 `0`（默认值） | 正标量

饱和电流随温度升高而呈指数增加的阶数。值必须大于 `0`。

### **激活能, EG** — 激活能 `1.11` `eV`（默认值） | *EG* *≥* 0.1 | 标量

晶体管激活能。值必须大于或等于 `0.1`。

### **固定电路温度, TFIXED** — 固定电路温度 `300.15` `K`（默认值） | 正标量

晶体管仿真温度。值必须大于 `0`。

#### 依赖关系

仅当为 **使用以下方式对温度依赖性建模** 参数选择 `Fixed temperature` 时，此参数才可见。

### **参数提取温度, TMEAS** — 参数提取温度 `300.15` `K`（默认值） | 正标量

测量晶体管参数时的温度。值必须大于 `0`。

### **本地电路温度偏移, TOFFSET** — 本地电路温度偏移 `0` `K`（默认值） | 标量

晶体管温度与电路温度之差。

#### 依赖关系

仅当为 **使用以下方式对温度依赖性建模** 参数选择 `Device temperature` 时，此参数才可见。

## 所属库

Simscape / Electrical / Additional Components / SPICE Semiconductors

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

与 SPICE 兼容的 P 沟道 JFET

SPICE PJFET 模块表示与 SPICE 兼容的 P 沟道结型场效应晶体管 (PJFET)。如果施加到栅极端口 **gx** 的电压大于施加到源极端口 **sx** 的电压，则源极端口和漏极端口 **dx** 之间的电流会减小。

SPICE（Simulation Program with Integrated Circuit Emphasis）是用于电子电路的仿真工具。您可以使用 Environment Parameters 模块以及 Additional Components 库中与 SPICE 兼容的模块，将一些 SPICE 子电路转换为等效的 Simscape™ Electrical™ 模型。有关详细信息，请参阅 `subcircuit2ssc`。

### 方程

SPICE PJFET block 方程的变量包括：

- 通过为 SPICE PJFET block 指定参数来定义的变量。某些参数的可见性取决于你为其他参数设置的值。有关更多信息，请参见参数。
- 几何调整变量，它们取决于你使用 SPICE PJFET block 的参数指定的若干值。有关更多信息，请参见几何调整变量。
- 温度 *T*，默认值为 `300.15` `K`。你可以通过为 SPICE PJFET block 指定参数，或通过同时为 SPICE PJFET block 和 Environment Parameters block 指定参数，来使用不同值。有关更多信息，请参见晶体管温度。
- 温度相关变量。有关更多信息，请参见温度依赖性。
- 最小电导 *GMIN*，默认值为 `1e-12` `1/Ohm`。你可以通过为 Environment Parameters block 指定参数，来使用不同值。有关更多信息，请参见最小导通。

**几何调整变量**

P 沟道结型场效应晶体管模型的方程中有若干变量会考虑该模块所表示器件的几何结构。这些几何调整变量取决于你通过指定 SPICE PJFET block 参数定义的变量。这些几何调整变量取决于以下变量：

- *AREA* — 器件面积
- *SCALE* — 并联连接的器件数
- 相关的未调整变量

下表包含几何调整变量及其定义方程。

| 变量 | 描述 | 方程 |
| --- | --- | --- |
| *BETAd* | 几何调整后的跨导 | BETAd=BETA\*AREA\*SCALE |
| *CGDd* | 几何调整后的零偏置栅极-漏极电容 | CGDd=CGD\*AREA\*SCALE |
| *CGSd* | 几何调整后的零偏置栅极-源极电容 | CGSd=CGS\*AREA\*SCALE |
| *ISd* | 几何调整后的饱和电流 | ISd=IS\*AREA\*SCALE |
| *RSd* | 几何调整后的源极电阻 | RSd=RSAREA\*SCALE |
| *RDd* | 几何调整后的漏极电阻 | RDd=RDAREA\*SCALE |

**晶体管温度**

你可以使用以下选项定义晶体管温度 *T*：

- 固定温度 — 当 SPICE PJFET block 的 **Temperature** 设置中的 **Model temperature dependence using** 参数设置为 `Fixed temperature` 时，该模块使用的温度与电路温度无关。对于此模型，该模块将 *T* 设置为等于 *TFIXED*。
- 器件温度 — 当 SPICE PJFET block 的 **Temperature** 设置中的 **Model temperature dependence using** 参数设置为 `Device temperature` 时，该模块使用的温度依赖于电路温度。对于此模型，该模块将温度定义为

  T=TC+TOFFSET

  其中：

  - *TC* 是电路温度。

    如果电路中没有 Environment Parameters block，则 *TC* 等于 300.15 K。

    如果电路中有 Environment Parameters block，则 *TC* 等于你为 Environment Parameters block 的 **SPICE** 设置中的 **Temperature** 参数指定的值。**Temperature** 参数的默认值为 `300.15` `K`。
  - *TOFFSET* 是局部电路温度偏移。

**最小导通**

最小电导 *GMIN* 的默认值为 `1e–12` `1/Ohm`。要指定不同值：

1. 如果晶体管电路中没有 Environment Parameters block，则添加一个。
2. 在 Environment Parameters block 的 **SPICE** 设置中，为 **GMIN** 参数指定所需的 *GMIN* 值。

**源极-栅极电流-电压模型**

下表显示了定义源极-栅极电流 *Isg* 与源极-栅极电压 *Vsg* 之间关系的方程。在适用情况下，首先针对温度调整模型参数。有关更多信息，请参见温度依赖性。

| *Vsg* 值的适用范围 | 对应的 *Isg* 方程 |
| --- | --- |
| Vsg>80\*Vt | Isg=ISd\*((VsgVt−79)e80−1)+Vsg\*Gmin |
| 80\*Vt≥Vsg | Isg=ISd\*(eVsg/Vt−1)+Vsg\*Gmin |

其中：

- *ISd* 是几何调整后的饱和电流。
- *Vt* 是热电压，满足 Vt=ND\*k\*T/q。
- *ND* 是发射系数。
- *q* 是电子的基本电荷。
- *k* 是玻尔兹曼常数。
- *T* 是晶体管温度。有关更多信息，请参见晶体管温度
- *GMIN* 是晶体管最小电导。有关更多信息，请参见最小导通

**漏极-栅极电流-电压模型**

下表显示了漏极-栅极电流 *Idg* 与漏极-栅极电压 *Vdg* 之间的关系。在适用情况下，首先针对温度调整模型参数。

| *Vdg* 值的适用范围 | 对应的 *Idg* 方程 |
| --- | --- |
| Vdg>80\*Vt | Idg=ISd\*((VdgVt−79)e80−1)+Vdg\*Gmin |
| 80\*Vt≥Vdg | Idg=ISd\*(eVdg/Vt−1)+Vdg\*Gmin |

**源极-漏极电流-电压模型**

下表显示了正常模式（*Vsd* ≥ 0）下源极-漏极电流 *Isd* 与源极-漏极电压 *Vsd* 之间的关系。在适用情况下，首先针对温度调整模型参数。

| *Vsg* 和 *Vdg* 值的适用范围 | 对应的 *Isd* 方程 |
| --- | --- |
| Vsg-Vto≤0 | Isd=0 |
| 0<Vsg-Vto≤Vsd | Isd=βd(Vsg−Vto)2(1+λVsd) |
| 0<Vsd<Vsg-Vto | Isd=βdVsd(2(Vsg-Vto)-Vsd)(1+λVsd) |

其中：

- *Vto* 是阈值电压。
- *βd* 是几何调整后的跨导。
- *λ* 是沟道调制。

下表显示了反向模式（*Vsd* < 0）下源极-漏极电流 *Isd* 与源极-漏极电压 *Vsd* 之间的关系。在适用情况下，首先针对温度调整模型参数。

| *Vsggs* 和 *Vdg* 值的适用范围 | 对应的 *Isd* 方程 |
| --- | --- |
| Vdg-Vto≤0 | Isd=0 |
| 0<Vdg-Vto≤−Vsd | Isd=−βd(Vdg−Vto)2(1−λVsd) |
| 0<−Vsd<Vdg-Vto | Isd=βdVsd(2(Vdg-Vto)+Vsd)(1−λVsd) |

**结电荷模型**

下表显示了源极-栅极电荷 *Qsg* 与源极-栅极电压 *Vsg* 之间的关系。在适用情况下，首先针对温度调整模型参数。

| *Vsg* 值的适用范围 | 对应的 *Qsg* 方程 |
| --- | --- |
| Vsg<FC\*VJ | Qsg=CGSd\*VJ\*(1-(1-VsgVJ)1−MG)1−MG |
| Vsg≥FC\*VJ | Qsg=CGSd\*(F1+F3\*(Vsg-FC\*VJ)+MG\*(Vsg2-(FC\*VJ)2)2\*VJF2) |

其中：

- *FC* 是电容系数。
- *VJ* 是结电势。
- *CGSd* 是零偏置栅极-源极电容。
- *MG* 是分级系数。
- F1=VJ\*(1-(1-FC)1−MG)1−MG
- F2=(1-FC)1+MG
- F3=1-FC\*(1+MG)

下表显示了漏极-栅极电荷 *Qdg* 与漏极-栅极电压 *Vdg* 之间的关系。在适用情况下，首先针对温度调整模型参数。

| *Vdg* 值的适用范围 | 对应的 *Qdg* 方程 |
| --- | --- |
| Vdg<FC\*VJ | Qdg=CGDd\*VJ\*(1-(1-VdgVJ)1−MG)1−MG |
| Vdg≥FC\*VJ | Qdg=CGDd\*(F1+F3\*(Vdg-FC\*VJ)+MG\*(Vdg2-(FC\*VJ)2)2\*VJF2) |

其中：

- *CGDd* 是几何调整后的零偏置栅极-漏极电容。

**温度依赖性**

该模块提供饱和电流 *IS* 与晶体管温度 *T* 之间的以下关系：

IS(T)=ISd\*(T/Tmeas)XTIND\*e(TTmeas−1)\*EGVt

其中：

- *ISd* 是几何调整后的饱和电流。
- *Tmeas* 是参数提取温度。
- *XTI* 是饱和电流温度指数。
- *EG* 是能隙。
- *Vt* 是热电压，满足 Vt=ND\*k\*T/q。
- *ND* 是发射系数。

结电势 *VJ* 与晶体管温度 *T* 之间的关系为

VJ(T)=VJ\*(TTmeas)-3\*k\*Tq\*log(TTmeas)-(TTmeas)\*EGTmeas+EGT

其中：

- *VJ* 是结电势。
- EGTmeas=1.16eV-(7.02e-4\*Tmeas2)/(Tmeas+1108)
- EGT=1.16eV-(7.02e-4\*T2)/(T+1108)

栅极-源极结电容 *CGS* 与晶体管温度 *T* 之间的关系：

CGS(T) = CGSd\*[1+MG\*(400e−6\*(T-Tmeas)-VJ(T)-VJVJ)]

其中：

- *CGSd* 是几何调整后的零偏置栅极-源极电容。

该模块使用 *CGS(T)* 方程，通过将 *CGSd* 替换为零偏置栅极-漏极电容 *CGDd*，来计算栅极-漏极结电容。

跨导 *β* 与晶体管温度 *T* 之间的关系为

β(T)=βd\*(TTmeas)

其中 *βd* 是几何调整后的跨导。
