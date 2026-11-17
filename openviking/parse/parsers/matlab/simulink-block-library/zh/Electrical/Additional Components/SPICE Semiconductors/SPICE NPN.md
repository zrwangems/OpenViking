---
type: simulink-block
title: 'SPICE NPN'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Semiconductors'
documentation_page: 'spicenpn'
documentation_source_path: 'ref/spicenpn.html'
language: zh-CN
chinese_source: worker-translation
---

# SPICE NPN

## 端口

### 守恒

### **bx** — 基极端子电气

与晶体管基极端子关联的电气守恒端口。

### **cx** — 集电极端子电气

与晶体管集电极端子关联的电气守恒端口。

### **ex** — 发射极端子电气

与晶体管发射极端子关联的电气守恒端口。

### **sx** — 衬底端子电气

与晶体管衬底端子关联的电气守恒端口。

## 参数

### 主要

### **Device area, AREA** — 器件面积 `1.0` `m^2`（默认）| 正标量

器件面积。该值必须大于 `0`。

### **Number of parallel devices, SCALE** — 并联器件数 `1`（默认）| 正标量

模块所表示的并联晶体管数量。该值必须大于 `0`。

### 正向增益

### **Transport saturation current, IS** — 饱和电流幅值 `1e-16` `A/m^2`（默认）| 正标量

晶体管饱和时的电流幅值。该值必须大于 `0`。

### **Forward beta, BF** — 理想最大正向 beta `100`（默认）| 正标量

理想最大正向 beta。该值必须大于 `0`。

### **Forward emission coefficient, NF** — 正向发射系数 `1`（默认）| 正标量

正向发射系数或理想因子。该值必须大于 `0`。

### **Forward Early voltage, VAF** — 正向 Early 电压 `Inf` `V`（默认）| 非负标量

正向 Early 电压。该值必须大于或等于 `0`。

### **Forward knee current, IKF** — 正向 beta 大电流滚降电流 `Inf` `A/m^2`（默认）| 非负标量

发生正向 beta 大电流滚降时的电流值。该值必须大于或等于 `0`。

### **B-E leakage current, ISE** — 基极-发射极漏电流 `0` `A/m^2`（默认）| 非负标量

基极-发射极漏电流。该值必须大于或等于 `0`。

### **B-E emission coefficient, NE** — 基极-发射极发射系数 `1.5`（默认）| 正标量

基极-发射极发射系数或理想因子。该值必须大于 `0`。

### 反向增益

### **Reverse beta, BR** — 理想最大反向 beta `1`（默认）| 正标量

理想最大反向 beta。该值必须大于 `0`。

### **Reverse emission coefficient, NR** — 反向发射系数 `1`（默认）| 正标量

反向发射系数或理想因子。该值必须大于 `0`。

### **Reverse Early voltage, VAR** — 反向 Early 电压 `Inf` `V`（默认）| 非负标量

反向 Early 电压。该值必须大于或等于 `0`。

### **Reverse knee current, IKR** — 反向 beta 大电流滚降电流 `Inf` `A/m^2`（默认）| 非负标量

发生反向 beta 大电流滚降时的电流值。该值必须大于或等于 `0`。

### **B-C leakage current, ISC** — 基极-集电极漏电流 `0` `A/m^2`（默认）| 非负标量

基极-集电极漏电流。该值必须大于或等于 `0`。

### **B-C emission coefficient, NC** — 基极-集电极发射系数 `2`（默认）| 正标量

基极-集电极发射系数或理想因子。该值必须大于 `0`。

### 电阻

### **Zero-bias base resistance, RB** — 基极电阻 `1` `m^2*Ohm`（默认）| 非负标量

基极的最大电阻。该值必须大于或等于 `0`。

### **Half base resistance cur, IRB** — 基极电阻半零偏压降电流 `Inf` `A/m^2`（默认）| 非负标量

基极电阻降至其零偏压值一半时的基极电流。该值必须大于或等于 `0`。如果不希望将基极电阻随基极电流的变化建模，请使用默认值 `Inf`。

### **Minimum base resistance, RBM** — 最小基极电阻 `0` `m^2*Ohm`（默认）| 标量 < *RB*

基极的最小电阻。该值必须小于或等于 **Zero-bias base resistance, RB** 参数值。

### **Emitter resistance, RE** — 发射极电阻 `1e-4` `m^2*Ohm`（默认）| 非负标量

发射极的电阻。该值必须大于或等于 `0`。

### **Collector resistance, RC** — 集电极电阻 `0.01` `m^2*Ohm`（默认）| 非负标量

集电极的电阻。该值必须大于或等于 `0`。

### 电容

### **Model junction capacitance** — 结电容模型 `No`（默认）| `Yes`

用于对结电容建模的选项：

- `No` — 不在模型中包含结电容。这是默认选项。
- `Yes` — 在模型中包含结电容。

#### 依赖关系

为 **Model junction capacitance** 参数选择 `Yes` 会显示其他 **Capacitance** 参数以及以下电容结设置：

- **B-E Capacitance** — 基极-发射极参数
- **B-C Capacitance** — 基极-集电极参数
- **C-S Capacitance** — 集电极-衬底参数

### **Capacitance coefficient, FC** — 电容系数 `0.5`（默认）| 0 ≤ *FC* < 0.95 | 标量

拟合系数 *FC*，用于量化耗尽电容随施加电压的减小。该值必须大于或等于 `0` 且小于 `0.95`。

#### 依赖关系

仅当为 **Model junction capacitance** 参数选择 `Yes` 时，此参数才可见。

### **Specify initial condition** — 初始条件模型 `No`（默认）| `Yes`

用于指定初始条件的选项：

- `No` — 不为模型指定初始条件。这是默认选项。
- `Yes` — 指定晶体管初始条件。

  **注意**

  模块将初始晶体管电压施加在结电容两端，而不是施加在端口两端。

#### 依赖关系

仅当为 **Model junction capacitance** 参数选择 `Yes` 时，此参数才可见。

为 **Specify initial condition** 参数选择 `Yes` 会显示相关参数。

### **Initial condition voltage ICVBE** — 初始基极-发射极电压 `0` `V`（默认）| 标量

仿真开始时的基极-发射极电压。

#### 依赖关系

仅当为 **Model junction capacitance** 参数选择 `Yes` 且为 **Specify initial condition** 参数选择 `Yes` 时，此参数才可见。

### **Initial condition voltage ICVCE** — 初始基极-集电极电压 `0` `V`（默认）| 标量

仿真开始时的基极-集电极电压。

#### 依赖关系

仅当为 **Model junction capacitance** 参数选择 `Yes` 且为 **Specify initial condition** 参数选择 `Yes` 时，此参数才可见。

### B-E 电容

如果在 **Capacitance** 设置中为 **Model junction capacitance** 参数选择 `Yes`，则会显示这些设置。

### **B-E depletion capacitance, CJE** — 基极-发射极结耗尽电容 `0` `F/m^2`（默认）| 非负标量

基极-发射极结两端的耗尽电容。该值必须大于或等于 `0`。

#### 依赖关系

仅当为 **Model junction capacitance** 参数选择 `Yes` 时，此参数才可见。

### **B-E built-in potential, VJE** — 基极-发射极结电势 `0.75` `V`（默认）| 标量 | 0.01 ≤ *VJE*

基极-发射极结电势。该值必须大于或等于 `0.01`。

#### 依赖关系

仅当为 **Model junction capacitance** 参数选择 `Yes` 时，此参数才可见。

### **B-E exponential factor, MJE** — 基极-发射极结梯度系数 `0.33`（默认）| 标量 | 0 ≤ *MJC* ≤ 0.9

基极-发射极结的梯度系数。该值必须大于或等于 `0` 且小于或等于 `0.9`。

#### 依赖关系

仅当为 **Model junction capacitance** 参数选择 `Yes` 时，此参数才可见。

### **Forward transit time, TF** — 少数载流子渡越时间 `0` `s`（默认）| 非负标量

当基极-发射极结正向偏置时，引起扩散电容的少数载流子的渡越时间。该值必须大于或等于 `0`。

#### 依赖关系

仅当为 **Model junction capacitance** 参数选择 `Yes` 时，此参数才可见。

### **Coefficient of TF, XTF** — 基极-发射极渡越时间偏置依赖系数 `0`（默认）| 非负标量

渡越时间对基极-发射极偏置依赖性的系数，该依赖性会在基极-发射极结两端产生电荷。该值必须大于或等于 `0`。如果不希望对渡越时间的基极-发射极偏置效应建模，请使用默认值 `0`。

#### 依赖关系

仅当为 **Model junction capacitance** 参数选择 `Yes` 时，此参数才可见。

### **VBC dependence of TF, VTF** — 基极-集电极渡越时间偏置依赖系数 `Inf` `V`（默认）| 非负标量

渡越时间对基极-集电极偏置依赖性的系数。该值必须大于或等于 `0`。

#### 依赖关系

仅当为 **Model junction capacitance** 参数选择 `Yes` 时，此参数才可见。

### **Coefficient of TF, ITF** — 集电极电流渡越时间依赖系数 `0` `A/m^2`（默认）| 非负标量

渡越时间对集电极电流依赖性的系数。该值必须大于或等于 `0`。如果不希望对渡越时间的集电极电流效应建模，请使用默认值 `0`。

#### 依赖关系

仅当为 **Model junction capacitance** 参数选择 `Yes` 时，此参数才可见。

### B-C 电容

如果在 **Capacitance** 设置中为 **Model junction capacitance** 参数选择 `Yes`，则会显示这些设置。

### **B-C depletion capacitance, CJC** — 基极-集电极结耗尽电容 `0` `F/m^2`（默认）| 正标量

基极-集电极结两端的耗尽电容。该值必须大于 `0`。

#### 依赖关系

仅当为 **Model junction capacitance** 参数选择 `Yes` 时，此参数才可见。

### **B-C built-in potential, VJC** — 基极-集电极结电势 `0.75` `V`（默认）| 标量 | 0.01 ≤ *VJC*

基极-集电极结电势。该值必须大于或等于 `0.01` `V`。

#### 依赖关系

仅当为 **Model junction capacitance** 参数选择 `Yes` 时，此参数才可见。

### **B-C exponential factor, MJC** — 基极-集电极结梯度系数 `0.33`（默认）| 0 ≤ *MJC* ≤ 0.9

基极-集电极结的梯度系数。该值必须大于或等于 `0` 且小于或等于 `0.9`。

#### 依赖关系

仅当为 **Model junction capacitance** 参数选择 `Yes` 时，此参数才可见。

### **B-C capacitance fraction, XCJC** — 基极-集电极耗尽电容分数 `1`（默认）| 标量 | 0 ≤ *XCJC* ≤ 1

连接在内部基极和内部集电极之间的基极-集电极耗尽电容的分数。其余的基极-集电极耗尽电容连接在外部基极和内部集电极之间。该值必须大于或等于 `0` 且小于或等于 `1`。

#### 依赖关系

仅当为 **Model junction capacitance** 参数选择 `Yes` 时，此参数才可见。

### **Reverse transit time, TR** — 少数载流子渡越时间 `0` `s`（默认）| 非负标量

当基极-集电极结正向偏置时，引起扩散电容的少数载流子的渡越时间。该值必须大于或等于 `0`。

#### 依赖关系

仅当为 **Model junction capacitance** 参数选择 `Yes` 时，此参数才可见。

### C-S 电容

如果在 **Capacitance** 设置中为 **Model junction capacitance** 参数选择 `Yes`，则会显示这些设置。

### **C-S junction capacitance, CJS** — 集电极-衬底结电容 `0``F/m^2`（默认）| 非负标量

集电极-衬底结电容。该值必须大于或等于 `0`。

#### 依赖关系

仅当为 **Model junction capacitance** 参数选择 `Yes` 时，此参数才可见。

### **Substrate built-in potential, VJS** — 衬底电势 `0.75` `V`（默认）| 标量 | 0.01 ≤ *VJC*

衬底的电势。该值必须大于或等于 `0.01` `V`。

#### 依赖关系

仅当为 **Model junction capacitance** 参数选择 `Yes` 时，此参数才可见。

### **Substrate exponential factor, MJS** — 集电极-衬底结梯度系数 `0`（默认）| 标量 | 0 ≤ *MJS* ≤ 0.9

集电极-衬底结的梯度系数。该值必须大于或等于 `0` 且小于或等于 `0.9`。

#### 依赖关系

仅当为 **Model junction capacitance** 参数选择 `Yes` 时，此参数才可见。

### 温度

### **Model temperature dependence using** — 温度依赖模型 `Device temperature`（默认）| `Fixed temperature`

选择以下选项之一来对晶体管温度依赖性建模：

- `Device temperature` — 使用器件温度对温度依赖性建模。
- `Fixed temperature` — 使用与电路温度无关的温度对温度依赖性建模。

有关详细信息，请参阅 Transistor Temperature。

#### 依赖关系

选择 `Device temperature` 会显示 **Offset local circuit temperature, TOFFSET** 参数。选择 `Fixed temperature` 会显示 **Fixed circuit temperature, TFIXED** 参数。

### **Beta temperature exponent, XTB** — 正向和反向 beta 温度指数 `0`（默认）| 非负标量

用于对基极电流温度依赖性建模的正向和反向 beta 温度指数。该值必须大于或等于 `0`。

### **Energy gap, EG** — 能隙 `1.11` `eV`（默认）| *EG* ≥ 0.1 | 标量

影响饱和电流随温度升高而增大的能隙。该值必须大于或等于 `0.1`。

### **Temperature exponent for IS, XTI** — 饱和电流指数增长阶数 `3`（默认）| 非负标量

饱和电流随温度升高而指数增长的阶数。该值必须大于或等于 `0`。

### **Offset local circuit temperature, TOFFSET** — 局部电路温度偏移 `0` `K`（默认）| 标量

晶体管温度与电路温度之间的差值。

#### 依赖关系

仅当为 **Model temperature dependence using** 参数选择 `Device temperature` 时，此参数才可见。

### **Fixed circuit temperature, TFIXED** — 固定电路温度 `300.15` `K`（默认）| 正标量

晶体管仿真温度。该值必须大于 `0` `K`。

#### 依赖关系

仅当为 **Model temperature dependence using** 参数选择 `Fixed temperature` 时，此参数才可见。

### **Parameter extraction temperature, TMEAS** — 参数提取温度 `300.15` `K`（默认）| 正标量

测量晶体管参数时的温度。该值必须大于 `0` `K`。

## 所属库

Simscape / Electrical / Additional Components / SPICE Semiconductors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2008a 中引入**

## 描述

SPICE 兼容的 Gummel-Poon NPN 晶体管

SPICE NPN 模块表示一个 SPICE 兼容的四端 Gummel-Poon NPN 双极结型晶体管。一个电容器将衬底端口 **sx** 连接到晶体管基极 **bx**。因此，当 **C-S 结电容，CJS** 参数使用默认值 `0`，并将衬底端口连接到任何其他端口（包括发射极端口 **ex** 或集电极端口 **cx**）时，该器件等效于一个三端晶体管。

SPICE，即集成电路重点仿真程序（Simulation Program with Integrated Circuit Emphasis），是一种电子电路仿真工具。您可以使用 Environment Parameters 模块和 Additional Components 库中的 SPICE 兼容模块，将一些 SPICE 子电路转换为等效的 Simscape™ Electrical™ 模型。有关更多信息，请参阅 `subcircuit2ssc`。

### 方程

SPICE NPN 模块方程中的变量包括：

- 通过为 SPICE NPN 模块指定参数来定义的变量。某些参数的可见性取决于您为其他参数设置的值。有关更多信息，请参阅参数。
- 几何调整变量，取决于您通过 SPICE NPN 模块参数指定的若干值。有关更多信息，请参阅几何调整变量。
- 温度 *T*，默认为 `300.15` `K`。您可以通过为 SPICE NPN 模块指定参数，或同时为 SPICE NPN 模块和 Environment Parameters 模块指定参数来使用不同的值。有关更多信息，请参阅晶体管温度。
- 温度相关变量。有关更多信息，请参阅温度依赖性。
- 最小电导 *GMIN*，默认为 `1e–12` `1/Ohm`。您可以通过为 Environment Parameters 模块指定参数来使用不同的值。有关更多信息，请参阅最小导通。

**几何调整变量**

SPICE NPN 双极结型晶体管模型方程中的若干变量考虑了模块所表示器件的几何结构。这些几何调整变量取决于您通过指定 SPICE NPN 模块参数来定义的变量。几何调整变量取决于以下变量：

- *AREA* — 器件面积
- *SCALE* — 并联连接的器件数量
- 相关的未调整变量

下表列出了几何调整变量及其定义方程。

| 变量 | 描述 | 方程 |
| --- | --- | --- |
| *ISd* | 几何调整传输饱和电流 | ISd=IS\*AREA\*SCALE |
| *IKFd* | 几何调整正向拐点电流 | IKFd=IKF\*AREA\*SCALE |
| *ISd* | 几何调整基极-发射极漏电流 | ISEd=ISE\*AREA\*SCALE |
| *IKRd* | 几何调整反向拐点电流 | IKRd=IKR\*AREA\*SCALE |
| *ISCd* | 几何调整基极-集电极漏电流 | ISCd=ISC\*AREA\*SCALE |
| *IRBd* | 几何调整半基极电阻电流 | IRBd=IRB\*AREA\*SCALE |
| *CJEd* | 几何调整基极-发射极耗尽电容 | CJEd=CJE\*AREA\*SCALE |
| *ITFd* | 几何调整正向渡越时间系数 | ITFd=ITF\*AREA\*SCALE |
| *CJCd* | 几何调整基极-集电极耗尽电容 | CJCd=CJC\*AREA\*SCALE |
| *CJSd* | 几何调整集电极-衬底结电容 | CJSd=CJS\*AREA\*SCALE |
| *RBd* | 几何调整零偏基极电阻 | RBd=RBAREA\*SCALE |
| *RBMd* | 几何调整最小基极电阻 | RBMd=RBMAREA\*SCALE |
| *REd* | 几何调整发射极电阻 | REd=REAREA\*SCALE |
| *RCd* | 几何调整集电极电阻 | RCd=RCAREA\*SCALE |

**晶体管温度**

您可以使用以下选项来定义晶体管温度 *T*：

- 固定温度 — 当 SPICE NPN 模块 **Temperature** 设置中的 **Model temperature dependence using** 参数设置为 `Fixed temperature` 时，模块使用独立于电路温度的温度。对于此模型，模块将 *T* 设置为等于 *TFIXED*。
- 器件温度 — 当 SPICE NPN 模块 **Temperature** 设置中的 **Model temperature dependence using** 参数设置为 `Device temperature` 时，模块使用取决于电路温度的温度。对于此模型，模块将温度定义为

  T=TC+TOFFSET

  其中：

  - *TC* 是电路温度。

    如果电路中没有 Environment Parameters 模块，则 *TC* 等于 300.15 K。

    如果电路中有 Environment Parameters 模块，则 *TC* 等于您在 Environment Parameters 模块 **SPICE** 设置中为 **Temperature** 参数指定的值。**Temperature** 参数的默认值为 `300.15` `K`。
  - *TOFFSET* 是偏移局部电路温度。

**最小导通**

最小电导 *GMIN* 的默认值为 `1e–12` `1/Ohm`。要指定不同的值：

1. 如果电路中没有 Environment Parameters 模块，请添加一个。
2. 在 Environment Parameters 模块的 **SPICE** 设置中，为 **GMIN** 参数指定所需的 *GMIN* 值。

**电流-电压和基极电荷模型**

晶体管的电流-电压关系和基极电荷关系通过基极-发射极和基极-集电极结电流、端子电流和基极电荷模型来描述。在适用的情况下，模型参数首先根据温度进行调整。

**基极-发射极和基极-集电极结电流**

基极-发射极结电流取决于基极-发射极电压 *VBE*，使得：

- 当 VBE>80\*VTF 时：

  Ibef = ISd\*((VBEVTF-79)\*e80 - 1)+Gmin\*VBE

  Ibee = ISEd\*((VBE-80\*VTF+VTE)\*e(80\*VTF/VTE)VTE - 1)
- 当 VBE≤80\*VTF 时：

  Ibef = ISd\*(e(VBE/VTF)-1)+ Gmin\*VBE

  Ibee = ISEd\*(e(VBE/VTE)-1)

基极-集电极结电流取决于基极-集电极电压 *VBC*，使得：

- 当 VBC>80\*VTR 时：

  Ibcr = ISd\*((VBCVTR-79)\*e80 - 1)+Gmin\*VBC

  Ibcc = ISCd\*((VBC-80\*VTR+VTC)\*e(80\*VTR/VTC)VTC - 1)
- 当 VBC≤80\*VTR 时：

  Ibcr = ISCd\*(e(VBC/VTR)−1)+Gmin\*VBC

  Ibcc = ISCd\*(e(VBC/VTC)-1)

其中：

- *VBE* 是基极-发射极电压。
- *VBC* 是基极-集电极电压。
- *VTE* 是发射极热电压，使得 VTE=NE\*k\*T/q。
- *VTC* 是集电极热电压，使得 VTC=NC\*k\*T/q。
- *VTF* 是正向热电压，使得 VTF=NF\*k\*T/q。
- *VTR* 是反向热电压，使得 VTR=NR\*k\*T/q。
- *ISCd* 是几何调整基极-集电极漏电流。
- *ISEd* 是几何调整基极-发射极漏电流。
- *NE* 是基极-发射极发射系数。
- *NC* 是基极-集电极发射系数。
- *NF* 是正向发射系数。
- *NR* 是反向发射系数。
- *q* 是电子的基本电荷。
- *k* 是玻尔兹曼常数。
- *T* 是晶体管温度。有关更多信息，请参阅晶体管温度。
- *Gmin* 是最小电导。有关更多信息，请参阅最小导通。

**端子电流**

端子电流计算如下：

IB = (IbefBF+Ibee+IbcrBR+Ibcc)

IC = (Ibef-Ibcrqb-IbcrBR-Ibcc)

其中：

- *IB* 是基极端子电流。
- *IC* 是集电极端子电流。
- *BF* 是正向 beta。
- *BR* 是反向 beta。

**基极电荷模型**

基极电荷 *qb* 使用以下方程计算：

qb=q12(1+0.5((1+4q2 - eps)2 + eps2 + 1+4q2-eps)+eps)

q1=(1−VBCVAF−VBEVAR)−1

q2= IbefIKFd+IbcrIKRd

其中：

- *qb* 是基极电荷。
- *VAF* 是正向厄利电压。
- *VAR* 是反向厄利电压。
- *IKFd* 是几何调整正向拐点电流。
- *IKRd* 是几何调整反向拐点电流。
- *eps* 是 1e-4。

**基极电阻模型**

您可以使用以下选项来建模基极电阻 *rbb*：

- 如果 **Half base resistance cur, IRB** 参数使用默认值无穷大，则模块将基极电阻计算为

  rbb = RBMd+RBd-RBMdqb

  其中：

  - *rbb* 是基极电阻。
  - *RBMd* 是几何调整最小基极电阻。
  - *RBd* 是几何调整零偏基极电阻。
- 如果为 **Half base resistance cur, IRB** 参数指定有限值，则模块将基极电阻计算为

  rbb = RBMd+3\*(RBd-RBMd)\*(tan z -zz\*tan2z)

  其中

  z=1+144IB/(π2IRBd)−1(24/π2)(IB/IRBd)

**渡越电荷调制模型**

如果您为 **Coefficient of TF, XTF** 参数指定非零值，则模块通过缩放正向渡越时间来建模渡越电荷调制，如下所示

TFmod=TF\*[1+XTF\*eVBC/(1.44VTF)(IBEIBE+ITFd)2]qb

其中 *ITFd* 是几何调整正向渡越时间系数。

**结电荷模型**

模块允许您对结电荷进行建模。基极-集电极电荷 *Qbc* 和基极-发射极电荷 *Qbe* 取决于一个中间值 *Qdep*。在适用的情况下，模型参数首先根据温度进行调整。

- 对于内部基极-发射极结

  Qbe=TFmod\*Ibe+Qdep
- 对于内部基极-集电极结

  Qbc=TR\*Ibc+XCJC\*Qdep
- 对于外部基极-集电极结

  Qbextc=(1−XCJC)\*Qdep

*Qdep* 取决于结电压 *Vjct*（基极-发射极结为 *VBE*，基极-集电极结为 *VBC*），如下所示。

| *Vjct* 值的适用范围 | 对应的 *Qdep* 方程 |
| --- | --- |
| Vjct<FC\*VJ | Qdep=Cjct\*VJ\*1-(1-Vjct/VJ)(1−MJ)1−MJ |
| Vjct≥FC\*VJ | Qdep=Cjct\*[F1+F3\*(Vjct-FC\*VJ)+MJ\*[Vjct2-(FC\*VJ)2]2\*VJF2] |

其中：

- *FC* 是电容系数。
- *VJ* 是：

  - 基极-发射极结的基极-发射极内建电势 *VJE*。
  - 基极-集电极结的基极-集电极内建电势 *VJC*。
- *MJ* 是：

  - 基极-发射极结的基极-发射极指数因子 *MJE*。
  - 基极-集电极结的基极-集电极指数因子 *MJC*。
- *Cjct* 是：

  - 基极-发射极结的几何调整基极-发射极耗尽电容 *CJEd*。
  - 基极-集电极结的几何调整基极-集电极耗尽电容 *CJCd*。
- F1=VJ\*(1-(1-FC)(1−MJ))/(1−MJ)
- F2=(1-FC)(1+MJ)
- F3=1-FC\*(1+MJ)

集电极-衬底电荷 *Qcs* 取决于集电极-衬底电压 *Vcs*。在适用的情况下，模型参数首先根据温度进行调整。

| *Vcs* 值的适用范围 | 对应的 *Qcs* 方程 |
| --- | --- |
| Vcs<0 | Qcs=CJSd\*VJS\*(1-(1-Vcs/VJS)(1−MJS)1−MJS) |
| Vcs≥0 | Qcs=CJSd\*(1+MJS\*Vcs/(2\*VJS))\*Vcs |

其中：

- *CJSd* 是几何调整集电极-衬底结电容。
- *VJS* 是衬底内建电势。
- *MJS* 是衬底指数因子。

**温度依赖性**

饱和电流 *ISd* 与晶体管温度 *T* 之间的关系为

IS(T)=ISd\*(T/Tmeas)XTI\*e(TTmeas−1)\*EGVt

其中：

- *ISd* 是几何调整传输饱和电流。
- *Tmeas* 是参数提取温度。
- *XTI* 是传输饱和电流温度指数。
- *EG* 是能隙。
- *Vt* = *kT/q*。

基极-发射极结电势 *VJE* 与晶体管温度 *T* 之间的关系为

VJE(T)=VJE\*(TTmeas)-3\*k\*Tq\*log(TTmeas)-(TTmeas)\*EGTmeas+EGT

其中：

- *VJE* 是基极-发射极内建电势。
- EGTmeas=1.16eV-(7.02e-4\*Tmeas2)/(Tmeas+1108)
- EGT=1.16eV-(7.02e-4\*T2)/(T+1108)

模块使用 *VJE(T)* 方程，通过将 *VJC*（基极-集电极内建电势）替换 *VJE* 来计算基极-集电极结电势。

基极-发射极结电容 *CJE* 与晶体管温度 *T* 之间的关系为

CJE(T) = CJEd\*[1+MJE\*(400e−6\*(T-Tmeas)-VJE(T)-VJEVJE)]

其中：

- *CJEd* 是几何调整基极-发射极耗尽电容。
- *MJE* 是基极-发射极指数因子。

模块使用 *CJE(T)* 方程，通过将 *CJCd*（几何调整基极-集电极耗尽电容）替换 *CJEd*，将 *MJC*（基极-集电极指数因子）替换 *MJE* 来计算基极-集电极结电容。

正向和反向 beta 与晶体管温度 *T* 之间的关系为

β(T)=β\*(TTmeas)XTB

其中：

- *β* 是正向 beta 或反向 beta。
- *XTB* 是 beta 温度指数。

基极-发射极漏电流 *ISE* 与晶体管温度 *T* 之间的关系为

ISE(T)=ISEd\*(TTmeas)-XTB \* (IS(T)ISd)1/NE

其中：

- *ISEd* 是几何调整基极-发射极漏电流。
- *NE* 是基极-发射极发射系数。

模块使用此方程，通过将 *ISCd*（几何调整基极-集电极漏电流）替换 *ISEd*，将 *NC*（基极-集电极发射系数）替换 *NE* 来计算基极-集电极漏电流。
