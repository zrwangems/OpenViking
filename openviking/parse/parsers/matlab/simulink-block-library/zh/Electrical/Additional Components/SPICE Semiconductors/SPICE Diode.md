---
type: simulink-block
title: 'SPICE Diode'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Semiconductors'
documentation_page: 'spicediode'
documentation_source_path: 'ref/spicediode.html'
language: zh-CN
chinese_source: worker-translation
---

# SPICE Diode

## 端口
```yaml
ports:
- name: +
  summary: 正电压电气端口
  direction: conserving
- name: '-'
  summary: 负电压电气端口
  direction: conserving
```

### 守恒端口

### **+** — 正电压电气端口

与正电压相关联的电气守恒端口。

### **-** — 负电压电气端口

与负电压相关联的电气守恒端口。
## 参数
```yaml
parameters:
- name: Device area, AREA
  summary: 器件面积 1.0 m^2（默认）| 正标量
  group: 主要
- name: Number of parallel devices, SCALE
  summary: 并联器件数 1（默认）| 正标量
  group: 主要
- name: Saturation current, IS
  summary: 饱和电流 1e-14 A/m^2（默认）| 非负标量
  group: 主要
- name: High-injection knee current, IKF
  summary: 高注入拐点电流 Inf A/m^2（默认）| 标量
  group: 主要
- name: Recombination current parameter, ISR
  summary: 复合电流 0 A/m^2（默认）| 标量
  group: 主要
- name: Emission coefficient, N
  summary: 发射系数 1（默认）| 正标量
  group: 主要
- name: Emission coefficient for ISR, NR
  summary: ISR 的发射系数 2（默认）| 正标量
  group: 主要
- name: Grading coefficient, M
  summary: 梯度系数 0.5（默认）| 0 < *M* < 0.9 | 标量
  group: 主要
- name: Junction potential, VJ
  summary: 结电势 1 V（默认）| *VJ* > 0.01 | 标量
  group: 主要
- name: Ohmic resistance, RS
  summary: 串联电阻 0.01 m^2*Ohm（默认）| 非负标量
  group: 主要
- name: Model junction capacitance
  summary: 结电容模型 No（默认）| Yes
  group: 结电容
- name: Zero-bias junction capacitance, CJO
  summary: 零偏结电容 0 F/m^2（默认）| 非负标量
  group: 结电容
- name: Capacitance coefficient, FC
  summary: 电容系数 0.5（默认）| 0 ≤ *FC* < 0.95 | 标量
  group: 结电容
- name: Transit time, TT
  summary: 渡越时间 0 s（默认）| 非负标量
  group: 结电容
- name: Specify initial condition
  summary: 初始条件模型 No（默认）| Yes
  group: 结电容
- name: Initial condition voltage, V0
  summary: 初始电压 0 V（默认）| 标量
  group: 结电容
- name: Model reverse breakdown
  summary: 反向击穿模型 No（默认）| Yes
  group: 反向击穿
- name: Reverse breakdown voltage, BV
  summary: 反向击穿阈值电压 Inf V（默认）| 非负标量
  group: 反向击穿
- name: Reverse breakdown current, IBV
  summary: 反向击穿电流 1e-10 A/m^2（默认）| 正标量
  group: 反向击穿
- name: Low-level reverse breakdown knee current, IBVL
  summary: 低电平反向击穿拐点电流 0 A/m^2（默认）| 正标量
  group: 反向击穿
- name: Reverse breakdown ideality factor, NBV
  summary: 反向击穿理想因子 1（默认）| 正标量
  group: 反向击穿
- name: Low-level reverse breakdown ideality factor, NBVL
  summary: 低电平反向击穿理想因子 1（默认）| 正标量
  group: 反向击穿
- name: Model temperature dependence using
  summary: 温度依赖模型 Device temperature（默认）| Fixed temperature
  group: 温度
- name: Saturation current temperature exponent, XTI
  summary: 饱和电流温度指数 3.0（默认）| 正标量
  group: 温度
- name: Activation energy, EG
  summary: 激活能 1.11 eV（默认）| *EG* *≥* 0.1 | 标量
  group: 温度
- name: IKF temperature coefficient (linear), TIKF
  summary: IKF 的温度系数 0 1/K（默认）| 正标量
  group: 温度
- name: RS temperature coefficient (linear), TRS1
  summary: RS 的温度系数 0 1/K（默认）| 正标量
  group: 温度
- name: RS temperature coefficient (quadratic), TRS2
  summary: RS 的温度系数 0 1/K^2（默认）| 正标量
  group: 温度
- name: BV temperature coefficient (linear), TBV1
  summary: BV 的温度系数 0 1/K（默认）| 正标量
  group: 温度
- name: BV temperature coefficient (quadratic), TBV2
  summary: BV 的温度系数 0 1/K^2（默认）| 正标量
  group: 温度
- name: Fixed circuit temperature, TFIXED
  summary: 固定电路温度 300.15 K（默认）| 正标量
  group: 温度
- name: Parameter extraction temperature, TMEAS
  summary: 参数提取温度 300.15 K（默认）| 正标量
  group: 温度
- name: Offset local circuit temperature, TOFFSET
  summary: 局部电路温度偏移 0 K（默认）| 标量
  group: 温度
```

### 主要

### **Device area, AREA** — 器件面积 `1.0` `m^2`（默认）| 正标量

二极管面积。该值必须大于 `0`。

### **Number of parallel devices, SCALE** — 并联器件数 `1`（默认）| 正标量

该模块所表示的并联二极管数量。该值必须大于 `0`。

### **Saturation current, IS** — 饱和电流 `1e-14` `A/m^2`（默认）| 非负标量

理想二极管方程在非常大的反向偏置水平下渐近逼近的电流幅值。该值必须大于或等于 `0`。

### **High-injection knee current, IKF** — 高注入拐点电流 `Inf` `A/m^2`（默认）| 标量

正向 beta 大电流滚降发生时的电流值。该值必须大于或等于 `0`。

### **Recombination current parameter, ISR** — 复合电流 `0` `A/m^2`（默认）| 标量

由结内电子和空穴复合过程产生的电流幅值。

### **Emission coefficient, N** — 发射系数 `1`（默认）| 正标量

二极管发射系数或理想因子。该值必须大于 `0`。

### **Emission coefficient for ISR, NR** — ISR 的发射系数 `2`（默认）| 正标量

复合电流的二极管发射系数。该值必须大于 `0`。

### **Grading coefficient, M** — 梯度系数 `0.5`（默认）| 0 < *M* < 0.9 | 标量

梯度系数 *M*。该值必须大于 `0` 且小于 `0.9`。

#### 依赖关系

仅当 **Model junction capacitance** 参数选择 `Yes` 时，此参数才可见。

### **Junction potential, VJ** — 结电势 `1` `V`（默认）| *VJ* > 0.01 | 标量

结电势 *VJ*。该值必须大于 `0.01` `V`。

#### 依赖关系

仅当 **Model junction capacitance** 参数选择 `Yes` 时，此参数才可见。

### **Ohmic resistance, RS** — 串联电阻 `0.01` `m^2*Ohm`（默认）| 非负标量

串联二极管连接电阻。该值必须大于或等于 `0`。

### 结电容

### **Model junction capacitance** — 结电容模型 `No`（默认）| `Yes`

结电容建模选项：

- `No` — 不在模型中包含结电容。
- `Yes` — 指定零偏结电容、结电势、梯度系数、正向偏置耗尽电容系数和渡越时间。

### **Zero-bias junction capacitance, CJO** — 零偏结电容 `0` `F/m^2`（默认）| 非负标量

与指数二极管项并联的电容值。该值必须大于或等于 `0`。

#### 依赖关系

要启用此参数，请将 **Model junction capacitance** 设置为 `Yes`。

### **Capacitance coefficient, FC** — 电容系数 `0.5`（默认）| 0 ≤ *FC* < 0.95 | 标量

拟合系数 *FC*，用于量化耗尽电容随外加电压的减小。该值必须大于或等于 `0` 且小于 `0.95`。

#### 依赖关系

要启用此参数，请将 **Model junction capacitance** 设置为 `Yes`。

### **Transit time, TT** — 渡越时间 `0` `s`（默认）| 非负标量

引起扩散电容的载流子的渡越时间 *TT*。该值必须大于或等于 `0`。

#### 依赖关系

要启用此参数，请将 **Model junction capacitance** 设置为 `Yes`。

### **Specify initial condition** — 初始条件模型 `No`（默认）| `Yes`

初始条件指定选项：

- `No` — 不为模型指定初始条件。
- `Yes` — 指定初始二极管电压。

  **注意**

  SPICE Diode 模块将初始二极管电压施加在结电容两端，而不是施加在端口两端。

#### 依赖关系

要启用此参数，请将 **Model junction capacitance** 设置为 `Yes`。

### **Initial condition voltage, V0** — 初始电压 `0` `V`（默认）| 标量

仿真开始时的二极管电压。

**注意**

该模块将初始条件施加在二极管结两端，因此仅当包含电荷存储时（即 **Zero-bias junction capacitance, CJO** 和 **Transit time, TT** 参数中有一个或两个大于零时），初始条件才有效。

#### 依赖关系

要启用此参数，请将 **Model junction capacitance** 和 **Specify initial condition** 设置为 `Yes`。

### 反向击穿

### **Model reverse breakdown** — 反向击穿模型 `No`（默认）| `Yes`

反向击穿建模选项：

- `No` — 不对反向击穿建模。
- `Yes` — 在二极管 I-V 关系中引入第二个指数项，从而对超过击穿电压时电导的快速增加进行建模。

### **Reverse breakdown voltage, BV** — 反向击穿阈值电压 `Inf` `V`（默认）| 非负标量

如果电压降至该值以下，模块将对二极管击穿时发生的电导快速增加进行建模。该值必须大于或等于 `0`。

#### 依赖关系

要启用此参数，请将 **Model reverse breakdown** 设置为 `Yes`。

### **Reverse breakdown current, IBV** — 反向击穿电流 `1e-10` `A/m^2`（默认）| 正标量

与 **Reverse breakdown voltage, BV** 参数所指定电压对应的二极管电流。该值必须大于 `0`。

#### 依赖关系

要启用此参数，请将 **Model reverse breakdown** 设置为 `Yes`。

### **Low-level reverse breakdown knee current, IBVL** — 低电平反向击穿拐点电流 `0` `A/m^2`（默认）| 正标量

低电平反向击穿拐点电流。

#### 依赖关系

要启用此参数，请将 **Model reverse breakdown** 设置为 `Yes`。

### **Reverse breakdown ideality factor, NBV** — 反向击穿理想因子 `1`（默认）| 正标量

**Reverse breakdown voltage, BV** 的理想因子。

#### 依赖关系

要启用此参数，请将 **Model reverse breakdown** 设置为 `Yes`。

### **Low-level reverse breakdown ideality factor, NBVL** — 低电平反向击穿理想因子 `1`（默认）| 正标量

**Low-level reverse breakdown knee current, IBVL** 的理想因子。

#### 依赖关系

要启用此参数，请将 **Model reverse breakdown** 设置为 `Yes`。

### 温度

### **Model temperature dependence using** — 温度依赖模型 `Device temperature`（默认）| `Fixed temperature`

选择以下选项之一来对二极管温度依赖性建模：

- `Device temperature` — 使用器件温度对温度依赖性建模。
- `Fixed temperature` — 使用独立于电路温度的温度对温度依赖性建模。

有关详细信息，请参阅 Diode Temperature。

### **Saturation current temperature exponent, XTI** — 饱和电流温度指数 `3.0`（默认）| 正标量

饱和电流随温度升高的指数增长阶数。该值必须大于 `0`。

### **Activation energy, EG** — 激活能 `1.11` `eV`（默认）| *EG* *≥* 0.1 | 标量

二极管激活能。该值必须大于或等于 `0.1` `eV`。

### **IKF temperature coefficient (linear), TIKF** — IKF 的温度系数 `0` `1/K`（默认）| 正标量

**High-injection knee current, IKF** 的线性温度系数。

### **RS temperature coefficient (linear), TRS1** — RS 的温度系数 `0` `1/K`（默认）| 正标量

**Ohmic resistance, RS** 的线性温度系数。

### **RS temperature coefficient (quadratic), TRS2** — RS 的温度系数 `0` `1/K^2`（默认）| 正标量

**Ohmic resistance, RS** 的二次温度系数。

### **BV temperature coefficient (linear), TBV1** — BV 的温度系数 `0` `1/K`（默认）| 正标量

**Breakdown voltage, BV** 的线性温度系数。

### **BV temperature coefficient (quadratic), TBV2** — BV 的温度系数 `0` `1/K^2`（默认）| 正标量

**Breakdown voltage, BV** 的二次温度系数。

### **Fixed circuit temperature, TFIXED** — 固定电路温度 `300.15` `K`（默认）| 正标量

二极管仿真温度。该值必须大于 `0` `K`。

#### 依赖关系

要启用此参数，请将 **Model temperature dependence using** 设置为 `Fixed temperature`。

### **Parameter extraction temperature, TMEAS** — 参数提取温度 `300.15` `K`（默认）| 正标量

测量二极管参数时的温度。该值必须大于 `0` `K`。

### **Offset local circuit temperature, TOFFSET** — 局部电路温度偏移 `0` `K`（默认）| 标量

二极管温度与电路温度之间的差值。

#### 依赖关系

要启用此参数，请将 **Model temperature dependence using** 设置为 `Device temperature`。
## 所属库

Simscape / Electrical / Additional Components / SPICE Semiconductors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

SPICE 兼容二极管

SPICE Diode 模块表示一个 SPICE 兼容二极管。

SPICE（Simulation Program with Integrated Circuit Emphasis）是一种电子电路仿真工具。您可以使用 Environment Parameters 模块和 Additional Components 库中的 SPICE 兼容模块，将一些 SPICE 子电路转换为等效的 Simscape™ Electrical™ 模型。有关详细信息，请参阅 `subcircuit2ssc`。

### 方程

SPICE 二极管模块方程的变量包括：

- 通过为 SPICE 二极管模块指定参数来定义的变量。某些参数的可见性取决于为其他参数设置的值。有关详细信息，请参阅参数。
- 几何调整变量，取决于使用 SPICE 二极管模块参数指定的多个值。有关详细信息，请参阅几何调整变量。
- 温度 *T*，默认值为 `300.15` `K`。您可以通过为 SPICE 二极管模块指定参数，或通过同时为 SPICE 二极管模块和 Environment Parameters 模块指定参数来使用不同的值。有关详细信息，请参阅二极管温度。
- 温度相关变量。有关详细信息，请参阅温度依赖性。
- 最小电导 *GMIN*，默认值为 `1e–12` `1/Ohm`。您可以通过为 Environment Parameters 模块指定参数来使用不同的值。有关详细信息，请参阅最小导通。
- 热电压 *Vt*。有关详细信息，请参阅热电压。

**几何调整变量**

SPICE 二极管模型方程中的若干变量考虑了模块所代表器件的几何结构。这些几何调整变量取决于通过指定 SPICE 二极管模块参数定义的变量。几何调整变量取决于以下变量：

- *AREA* — 器件面积
- *SCALE* — 并联连接的器件数量
- 相关的未调整变量

下表包含几何调整变量及其定义方程。

| 变量 | 描述 | 方程 |
| --- | --- | --- |
| *CJOd* | 几何调整零偏结电容 | CJOd=CJO\*AREA\*SCALE |
| *IBVd* | 几何调整反向击穿电流 | IBVd=IBV\*AREA\*SCALE |
| *ISd* | 几何调整饱和电流 | ISd=IS\*AREA\*SCALE |
| *RSd* | 几何调整串联电阻 | RSd=RSAREA\*SCALE |

**二极管温度**

您可以使用以下选项来定义二极管温度 *T*：

- 固定温度 — 当 Spice Diode 模块的 **Temperature** 设置中的 **Model temperature dependence using** 参数设置为 `Fixed temperature` 时，模块使用独立于电路温度的温度。对于此模型，模块将 *T* 设置为等于 *TFIXED*。
- 器件温度 — 当 Spice Diode 模块的 **Temperature** 设置中的 **Model temperature dependence using** 参数设置为 `Device temperature` 时，模块使用取决于电路温度的温度。对于此模型，模块将温度定义为

  T=TC+TOFFSET

  其中：

  - *TC* 是电路温度。

    如果电路中没有 Environment Parameters 模块，则 *TC* 等于 300.15 K。

    如果电路中有 Environment Parameters 模块，则 *TC* 等于为 Environment Parameters 模块的 **Spice** 设置中的 **Temperature** 参数指定的值。**Temperature** 参数的默认值为 `300.15` `K`。
  - *TOFFSET* 是偏移局部电路温度。

**最小导通**

最小电导 *GMIN* 的默认值为 `1e–12` `1/Ohm`。要指定不同的值：

1. 如果二极管电路中没有 Environment Parameters 模块，请添加一个。
2. 在 Environment Parameters 模块的 **Spice** 设置中，为 **GMIN** 参数指定所需的 *GMIN* 值。

**热电压**

热电压 *Vt* 由以下方程定义

Vt=Nk\*Tq

其中：

- *N* 是发射系数。
- *T* 是二极管温度。有关详细信息，请参阅二极管温度。
- *k* 是玻尔兹曼常数。
- *q* 是电子的基本电荷。

**电流-电压方程**

这些方程定义了二极管电流 *Id* 与二极管电压 *Vd* 之间的关系。在适用的情况下，模型参数首先根据温度进行调整。有关详细信息，请参阅温度依赖性。

Id=AREA\*(Ifwd−Irev)

Ifwd=Inrm\*Kinj+Irec\*Kgen

Irev=Irevh+Irevl

Inrm=ISeVd/(N\*Vt)−1

Irec=ISReVd/(NR\*Vt)−1

Kinj=(IKFIKF+Inrm)0.5

Kgen=[(1−VdVJ)2+0.005]M2

Irevh=IBV\*e−Vd+BVNBV\*Vt

Irevl=IBVL\*e−Vd+BVNBVL\*Vt

其中：

- *Ifwd* 是正向电流。
- *Irev* 是反向电流。
- *Inrm* 是正常电流。
- *Irec* 是复合电流。
- *Kinj* 是高注入因子。
- *Kgen* 是产生因子。
- *Irevh* 是高电平击穿电流。
- *Irevl* 是低电平击穿电流。
- *Vt* 是热电压。有关详细信息，请参阅热电压。
- *IS* 是饱和电流。
- *ISR* 是复合电流。
- *IKF* 是正向拐点电流。
- *VJ* 是结电势。
- *N* 是发射系数。
- *NR* 是反向发射系数。
- *NBV* 是反向击穿发射系数。
- *NBVL* 是低电平反向击穿理想因子。
- *M* 是梯度系数。
- *BV* 是反向击穿电压。
- *IBV* 是反向击穿电流。
- *IBVL* 是低电平反向击穿拐点电流。

**结电荷模型**

下表显示了定义二极管电荷 *Qd* 与二极管电压 *Vd* 之间关系的方程。在适用的情况下，模型参数首先根据温度进行调整。有关详细信息，请参阅温度依赖性。

| *Vd* 范围 | *Qd* 方程 |
| --- | --- |
| Vd<FC\*VJ | Qd=TT\*AREA\*Ifwd+CJOd\*VJ\*1−(1−VdVJ)1−M1−M |
| Vd≥FC\*VJ | Qd=TT\*AREA\*Ifwd+          CJOd\*(F1+F3\*(Vd-FC\*VJ)+(M2\*VJ)\*(Vd2-(FC\*VJ)2)F2)​ |

其中：

- *FC* 是正向偏置耗尽电容系数。
- *VJ* 是结电势。
- *TT* 是渡越时间。
- *CJOd* 是几何调整零偏结电容。有关详细信息，请参阅几何调整变量。
- *M* 是梯度系数。
- F1=VJ\*(1-(1-FC)(1-M))/(1-M)
- F2=(1-FC)(1+M)
- F3=1-FC\*(1+M)

**温度依赖性**

几何调整饱和电流与二极管温度之间的关系为

ISd(T)=ISd\*(T/TMEAS)XTIN\*e(TTMEAS−1)\*EGN\*Vt

其中：

- *ISd* 是几何调整饱和电流。有关详细信息，请参阅几何调整变量。
- *T* 是二极管温度。有关详细信息，请参阅二极管温度。
- *TMEAS* 是参数提取温度。
- *XTI* 是饱和电流温度指数。
- *N* 是发射系数。
- *EG* 是激活能。
- *Vt* 是热电压。有关详细信息，请参阅热电压。

复合电流与二极管温度之间的关系为

ISR(T)=ISR\*(TTMEAS)XTINR\*e(TTMEAS−1)\*EGNR\*Vt

其中：

- *ISR* 是复合电流。
- *NR* 是反向发射系数。

正向拐点电流与二极管温度之间的关系为

IKF(T)=IKF\*[1+TIKF\*(T−TMEAS)]

其中：

- *IKF* 是正向拐点电流。
- *TIKF* 是线性 IKF 温度系数。

击穿电压与二极管温度之间的关系为

BV(T)=BV\*[1+TBV1\*(T−TMEAS)+TBV2\*(T−TMEAS)2]

其中：

- *BV* 是击穿电压。
- *TBV1* 是线性 BV 温度系数。
- *TBV2* 是二次 BV 温度系数。

欧姆电阻与二极管温度之间的关系为

RS(T)=RS\*[1+TRS1\*(T−TMEAS)+TRS2\*(T−TMEAS)2]

其中：

- *RS* 是欧姆电阻。
- *TRS1* 是线性 RS 温度系数。
- *TRS2* 是二次 RS 温度系数。

结电势与二极管温度之间的关系为

VJ(T)=VJ\*(TTMEAS)-3\*Vt\*ln(TTMEAS)-(TTMEAS)\*EGTMEAS+EGT

其中：

- *VJ* 是结电势。
- *EGTMEAS* 是测量二极管参数时温度对应的激活能。定义方程为 EGTMEAS=1.16eV-(7.02e-4\*TMEAS2)/(TMEAS+1108)。
- *EGT* 是二极管温度对应的激活能。定义方程为 EGT=1.16eV-(7.02e-4\*T2)/(T+1108)。

几何调整二极管零偏结电容与二极管温度之间的关系为

CJOd(T) = CJOd\*[1+M\*(400e−6\*(T-TMEAS)-VJ(T)-VJVJ)]

其中：

- *CJOd* 是几何调整零偏结电容。有关详细信息，请参阅几何调整变量。
- *M* 是梯度系数。
