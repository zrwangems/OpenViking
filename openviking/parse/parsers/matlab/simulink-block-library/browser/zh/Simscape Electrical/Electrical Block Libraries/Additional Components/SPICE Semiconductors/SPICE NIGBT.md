---
type: simulink-block
title: 'SPICE NIGBT'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Additional Components / SPICE Semiconductors'
documentation_page: 'spicenigbt'
documentation_source_path: 'ref/spicenigbt.html'
language: zh-CN
chinese_source: worker-translation
---

# SPICE NIGBT

## 端口

### 守恒

### **gx** — 栅极端子电气

与 IGBT 栅极端子关联的电气守恒端口。

### **cx** — 集电极端子电气

与 IGBT 集电极端子关联的电气守恒端口。

### **ex** — 发射极端子电气

与 IGBT 发射极端子关联的电气守恒端口。

## 参数

### 尺寸

### **栅漏交叠面积，AGD** — 栅漏交叠面积 `5.0e-6` `m^2`（默认）| 正标量

栅漏交叠面积。该值必须大于 `0`。

### **器件面积，AREA** — 器件面积 `1.0e-5` `m^2`（默认）| 正标量

器件面积。该值必须大于 `0`。

### **并联器件数，SCALE** — 并联器件数 `1`（默认）| 正整数

模块表示的并联晶体管数。该值必须是大于 `0` 的整数。

### 通用

### **电子迁移率，MUN** — 电子迁移率 `1.5e3` `cm^2/s/V`（默认）| 标量

电子的迁移率。

### **空穴迁移率，MUP** — 空穴迁移率 `4.5e2` `cm^2/s/V`（默认）| 标量

空穴的迁移率。

### **基区掺杂，NB** — 基区掺杂 `2e14` `1/cm^3`（默认）| 标量

基区的掺杂。

### MOSFET

### **三极管区因子，KF** — 三极管区因子 `1`（默认）

三极管区的因子。

### **MOS 跨导，KP** — MOS 跨导 `0.38` `A/V^2`（默认）| 标量

漏极电流对栅极电压的导数。该值必须大于或等于 `0`

### **阈值电压，VT** — 阈值电压 `4.7` `V`（默认）| 标量

阈值电压。

### **横向场因子，THETA** — 横向场因子 `0.02` `1/V`（默认）| 标量

横向场因子。

### BJT

### **双极复合寿命，TAU** — 双极复合寿命 `7.1e-6` `s`（默认）| 标量

双极复合寿命。

### **冶金基区宽度，WB** — 冶金基区宽度 `9.0e-5` `m`（默认）| 标量

冶金基区的宽度。

### **发射极饱和电流密度，JSNE** — 发射极饱和电流密度 `6.5e-13` `A/cm^2`（默认）| 标量

发射极饱和电流的密度。

### **雪崩均匀性因子，BVF** — 雪崩均匀性因子 `1`（默认）| 标量

雪崩均匀性因子。

### **雪崩倍增指数，BVN** — 雪崩倍增指数 `4`（默认）| 标量

雪崩倍增指数。

### 电容

### **单位面积栅源电容，CGS** — 单位面积栅源电容 `1.24e-8` `F/cm^2`（默认）| 标量

单位面积栅源电容。

### **单位面积栅漏氧化层电容，COXD** — 单位面积栅漏氧化层电容 `3.5e-8` `F/cm^2`（默认）| 标量

单位面积栅漏氧化层电容。

### **栅漏交叠耗尽阈值，VTD** — 栅漏交叠耗尽阈值 `1e-3` `V`（默认）| 标量

栅漏交叠耗尽阈值。

### **指定初始条件** — 是否指定初始条件 `No`（默认）| `Yes`

是否指定初始条件。

### **初始条件电压 ICVGE** — 初始条件电压 ICVGE `0` `V`（默认）| 标量

初始条件电压 ICVGE。

#### 依赖关系

要启用此参数，请将 **指定初始条件** 设置为 `Yes`。

### **初始条件电压 ICVCE** — 初始条件电压 ICVCE `0` `V`（默认）| 标量

初始条件电压 ICVCE。

#### 依赖关系

要启用此参数，请将 **指定初始条件** 设置为 `Yes`。

### 温度

### **使用以下方式建模温度依赖性** — 温度依赖性模型 `Device temperature`（默认）| `Fixed temperature`

用于对晶体管温度依赖性建模的选项：

- `Device temperature` — 使用器件温度对温度依赖性建模。
- `Fixed temperature` — 使用与电路温度无关的温度对温度依赖性建模。

有关详细信息，请参阅温度依赖性。

### **固定电路温度，TFIXED** — 固定电路温度 `300.15` `K`（默认）| 正标量

晶体管仿真温度。该值必须大于 `0` `K`。

#### 依赖关系

要启用此参数，请将 **使用以下方式建模温度依赖性** 设置为 `Fixed temperature`。

### **参数提取温度，TMEAS** — 参数提取温度 `300.15` `K`（默认）| 正标量

测量晶体管参数时的温度。该值必须大于 `0` `K`。

### **本地电路温度偏移，TOFFSET** — 本地电路温度偏移 `0` `K`（默认）| 标量

晶体管温度与电路温度的差值。

#### 依赖关系

要启用此参数，请将 **使用以下方式建模温度依赖性** 设置为 `Device temperature`。

## 所属库

Simscape / Electrical / Additional Components / SPICE Semiconductors

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

SPICE 兼容的 N 沟道绝缘栅双极型晶体管

SPICE NIGBT 模块对 SPICE n 型绝缘栅双极型晶体管 (IGBT) 建模。

SPICE（Simulation Program with Integrated Circuit Emphasis）是一种电子电路仿真工具。您可以使用 Environment Parameters 模块和 Additional Components 库中的 SPICE 兼容模块，将某些 SPICE 子电路转换为等效的 Simscape™ Electrical™ 模型。有关详细信息，请参阅 `subcircuit2ssc`。

下图显示了 SPICE NIGBT 模块的等效电路：

### 方程

SPICE NIGBT 模块方程中的变量包括：

- 通过为 SPICE NIGBT 模块指定参数定义的变量。
- 温度 *T*，默认值为 `300.15` `K`。您可以通过为 SPICE NIGBT 模块指定参数，或同时为 SPICE NIGBT 模块和 Environment Parameters 模块指定参数来使用不同的值。有关详细信息，请参阅晶体管温度。

**MOSFET 沟道电流**

下表显示了定义 MOSFET 沟道电流 *Imos* 与栅源电压 *Vgs* 之间关系的方程。

| 适用的 *Vgs* 值范围 | 对应的 *Imos* 方程 |
| --- | --- |
| Vgs<VT | Imos=GMIN\*Vds\*SCALE |
| Vds≤Vgs−VTKF | Imos=SCALE\*(KF\*KP[(Vgs−VT)Vds−KF\*Vds22]1+THETA\*(Vgs−VT)+GMIN\*Vds) |
| Vds>(Vgs−VT)KF | Imos=SCALE\*(KP(Vgs−VT)22[1+THETA\*(Vgs−VT)]+GMIN\*Vds) |

在这些方程中：

- *Vds* 是漏源电压。
- *VT* 是阈值电压。
- *KF* 是三极管区因子。
- *KP* 是 MOSFET 跨导。
- *THETA* 是横向场因子。

**双极稳态集电极电流**

下表显示了定义稳态集电极电流 *Icss* 与发射极-基极电容 *Qeb* 之间关系的方程。

| 适用的 *Qeb* 值范围 | 对应的 *Icss* 方程 |
| --- | --- |
| Qeb<0 | Icss=0 |
| Qeb≥0 | Icss=[(11+b)IT+(b1+b)(4DpW2)Qeb]\*SCALE |

在这些方程中：

- b=MUNMUP 是双极迁移率比。
- Dp=KBTq\*MUP 是空穴扩散系数。
- W=WB−Wbcj 是准中性基区宽度，其中：

  - *WB* 是冶金基区宽度。
  - Wbcj=2εsiVbc+Vbiq\*NB 是基极-集电极耗尽宽度。
  - *Vbc* 是基极-集电极电压。
  - *Vbi* 是内建电压，等于 `0.6` `V`

**双极稳态基极电流**

下表显示了定义稳态基极电流 *Ibss* 与发射极-基极电容 *Qeb* 之间关系的方程。

| 适用的 *Qeb* 值范围 | 对应的 *Ibss* 方程 |
| --- | --- |
| Qeb<0 | Ibss=0 |
| Qeb≥0 | Ibss=QebTAU+(QebQB)2(4\*NB2ni2)JSNE\*AREA\*SCALE |

在这些方程中：

- *TAU* 是双极复合寿命。
- *JSNE* 是发射极饱和电流密度。
- *ni* 是本征载流子浓度。在 `300` `K` 时，它等于 `1.45*1010` `1/cm3`。
- QB=qWNB\*AREA 是背景可动载流子基极电荷，其中：

  - *NB* 是基区掺杂。
  - *AREA* 是器件面积。

**双极发射极-基极电压**

下表显示了定义发射极-基极电压 *Veb* 与发射极-基极电容 *Qeb* 之间关系的方程。

| 适用的 *Qeb* 值范围 | 对应的 *Veb* 方程 |
| --- | --- |
| Qeb<0 | Veb=Vebj |
| Qbi>Qeb≥0 | Vebmin=min(Vebj,Vebd) |
| Qeb>Qbi | Veb=Vebd |

在这些方程中：

- Vebj=Vbi−(Qeb−Qbi)22qNBεsiA2 是发射极-基极耗尽电压。
- *Vbi* 是内建电压。
- Qbi=AREA\*2εsiqNB\*Vbi 是发射极-基极结内建电压。
- Vebd=kTqln[(P0ni2+1NB)(NB+P0)]−DCμnclnP0+NBNB 是发射极-基极扩散电压。

**阳极电流**

阳极电流由以下方程得到：

IT=VaeRb\*SCALE,

其中：

- *Vae* 是施加的阳极-发射极电压。
- *Rb* 是电导调制基极电阻。

下表显示了定义电导调制基极电阻 *Rb* 与发射极-基极电容 *Qeb* 之间关系的方程。

| 适用的 *Qeb* 值范围 | 对应的 *Rb* 方程 |
| --- | --- |
| Qeb<0 | Rb=Wq\*MUN\*AREA\*NB |
| Qeb≥0 | Rb=Wq\*μeff\*AREA\*neff |

在这些方程中：

- *μeff* 是有效载流子迁移率。
- *neff* 是有效基区掺杂浓度。
- *MUN* 是电子迁移率。

*μeff* 和 *neff* 由以下方程得到：

μnc=1(1μn+1μc)μpc=1(1μp+1μc)μeff=μnc+μpcQeb(Qeb+QB)Dc=2kTqμncμpcμnc+μpcL=Dc\*TAUP0=Qq\*AREA\*LtanhW2Lneff=W2LNB2+P02csch(WL)arctanh[NB2+P02csch(WL)tanh(W2L)NB+P0csch(WL)tanh(W2L)]δ¯p=P0sinh(W2L)sinh(WL)

其中：

- *μnc* 是电子载流子散射迁移率。
- *μpc* 是空穴载流子散射迁移率。
- *Dc* 是载流子-载流子散射扩散率。
- *L* 是双极扩散长度。
- *P0* 是基区发射极端的载流子浓度。
- δp¯ 是基区中的平均载流子浓度。

**雪崩倍增电流**

雪崩倍增电流由以下方程得到：

Imult=(M−1)(Imos+Icss+Iccer)+M\*Igen,

其中：

- Igen=SCALETAUqniAREA2εsiVbcqNB 是集电极-基极热生成电流。
- *Icss* 是稳态集电极电流。
- *Imos* 是 MOSFET 沟道电流。
- *Iccer* 是集电极-发射极再分布电流。

以下方程定义基极-集电极电压 *Vbc* 与雪崩倍增因子 *M* 之间的关系：

M=11−(VbcBVcbo)BVN,

其中：

- BVcbo=BVF\*5.34e13\*NB−0.75 是开基极集电极-发射极击穿电压。
- *BVF* 是雪崩均匀性因子。
- *BVN* 是雪崩倍增指数。

**电容模型**

栅源电容由以下方程得到：

Qgs=CGS\*Vgs\*SCALE.

漏源电容由以下方程得到：

Qds=q(AREA−AGD)\*NB\*Wdsj\*SCALE,

其中 *Wdsj = Wbcj* 是漏源耗尽宽度。

下表显示了定义栅漏电容 *Qdg* 与漏栅电压 *Vdg* 之间关系的方程

| 适用的 *Vdg* 值范围 | 对应的 *Qdg* 方程 |
| --- | --- |
| Vdg+VTD≤0 | Qdg=Cgdo\*Vdg\*SCALE |
| Vdg+VTD>0 | Qdg=[qNBεsiAGDCOXD(COXD\*Wdgjεsilog(1+COXD\*Wdgjεsi))−Cgdo\*VTD]\*SCALE |

在这些方程中：

- Cgdo=COXD\*AGD 是栅漏交叠氧化层电容。
- *Vdg* 是漏栅电压。
- *εsi* 是硅的介电常数。
- Wdgj=2εsi(Vdg+VTD)qNB 是栅漏交叠耗尽宽度。
- *VTD* 是 **栅漏交叠耗尽阈值，VTD**。
- *COXD* 是 **单位面积栅漏氧化层电容，COXD**。
- *AGD* 是 **栅漏交叠面积，AGD**。
- *NB* 是 **基区掺杂，NB**。

以下方程显示集电极-发射极再分布电流 *Iccer* 与集电极-发射极再分布电容 *Ccer* 之间的关系：

Iccer=Ccer\*dVecdt\*SCALE,

其中 *Vec* 是发射极-集电极电压。

下表显示了定义集电极-发射极再分布电容 *Ccer* 与发射极-基极电容 *Qeb* 之间关系的方程。

| 适用的 *Qeb* 值范围 | 对应的 *Ccer* 方程 |
| --- | --- |
| Qeb>0 | Ccer=QebCbcj3QB+Cmin\*AREA |
| Qeb≤0 | Ccer=CminAREA |

在这些方程中：

- *Cbcj* 是基极-集电极耗尽电容。
- QB=qWNB\*AREA 是背景可动载流子基极电荷。

隐式发射极-基极电容器电流由以下方程得到：

Iqeb=dQebdt\*SCALE.

**晶体管温度**

您可以使用以下选项来定义晶体管温度 *T*：

- Fixed temperature — 当 SPICE NIGBT 模块的 **温度** 设置中的 **使用以下方式建模温度依赖性** 参数设置为 `Fixed temperature` 时，模块使用与电路温度无关的温度。对于此模型，模块将 *T* 设置为等于 *TFIXED*。
- Device temperature — 当 SPICE NIGBT 模块的 **温度** 设置中的 **使用以下方式建模温度依赖性** 参数设置为 `Device temperature` 时，模块使用取决于电路温度的温度。对于此模型，模块将温度定义为

  T=TC+TOFFSET

  其中：

  - *TC* 是电路温度。

    如果电路中没有 Environment Parameters 模块，则 *TC* 等于 300.15 K。

    如果电路中有 Environment Parameters 模块，则 *TC* 等于您在 Environment Parameters 模块的 **SPICE** 设置中为 **Temperature** 参数指定的值。**Temperature** 参数的默认值为 `300.15` `K`。
  - *TOFFSET* 是本地电路温度偏移。
