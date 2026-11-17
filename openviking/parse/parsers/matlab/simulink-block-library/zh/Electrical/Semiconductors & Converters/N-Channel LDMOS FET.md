---
type: simulink-block
title: 'N-Channel LDMOS FET'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Semiconductors & Converters'
documentation_page: 'nchannelldmosfet'
documentation_source_path: 'ref/nchannelldmosfet.html'
language: zh-CN
chinese_source: worker-translation
---

# N-Channel LDMOS FET

## 端口

### 守恒端口

### **G** — 栅极端子电气

与晶体管栅极端子关联的电气守恒端口。

### **D** — 漏极端子电气

与晶体管漏极端子关联的电气守恒端口。

### **S** — 源极端子电气

与晶体管源极端子关联的电气守恒端口。

### **H** — 热端口热

热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认）| `Show thermal port`

是否启用模块的热端口，并对产生的热量和设备温度的影响进行建模。

### 主

### **Gain, [channel drift\_region]** — 增益 `[11.6, .01]` `A/V`（默认）| 正向量

MOSFET 各区域的增益 *β*。该参数值为一个二元素向量，第一个元素对应沟道，第二个元素对应漂移区。该参数主要定义 *I*D–*VDS* 特性上的线性工作区。

### **Flatband voltage, [channel drift\_region]** — 平带电压 `[-1.05, -.1]` `V`（默认）

平带电压 *VFB* 定义了为在硅表面实现平带条件而必须施加的栅极偏压。该参数值为一个二元素向量，第一个元素对应沟道，第二个元素对应漂移区。默认值为 `[-1.05, -0.1]` V。您也可以使用此参数来任意偏移由材料功函数差异以及界面陷阱电荷或氧化层电荷引起的阈值电压。但在实践中，通常建议首先通过 **Body factor** 和 **Surface potential at strong inversion** 参数来修改阈值电压，仅使用此参数进行微调。

对于源-体短接连接，沟道区的阈值电压近似为

VT=VFB+2ϕB+2ϕT+γ2ϕB+2ϕT

其中 2*ϕB* 是强反型时的表面电位，*γ* 是体因子，二者均为沟道区的值。

### **Body factor, [channel drift\_region]** — 体因子 `[3.4, 2.5]` `V1/2`（默认）

表面电位方程中的体因子 *γ*。该参数值为一个二元素向量，第一个元素对应沟道，第二个元素对应漂移区。

对于沟道区，体因子为

γ=2qεSiNACox

有关此方程的详细信息，请参阅 N-Channel MOSFET 模块参考页。漂移区方程类似，只是将 *NA* 替换为掺杂密度 *N*D。沟道区参数值主要影响阈值电压。对于漂移区，该参数主要影响电荷模型，同时对通过漂移区的体电流的夹断行为也有较小影响。

### **Surface potential at strong inversion, [channel drift\_region]** — 强反型时的表面电位 `[.95, .95]` `V`（默认）

表面电位方程中的 2*ϕB* 项。该参数值为一个二元素向量，第一个元素对应沟道，第二个元素对应漂移区。

沟道区参数值也主要影响阈值电压。对于漂移区，该参数仅影响电荷模型。

### **Velocity saturation factor, [channel drift\_region]** — 速度饱和因子 `[0, .1]` `1/V`（默认）

漏极电流方程中的速度饱和 *θ*sat。在良好拟合线性工作区导致饱和电流过高的情况下，请使用此参数。通过增大此参数值，可以降低饱和电流。该参数值为一个二元素向量，第一个元素对应沟道，第二个元素对应漂移区。默认值为 `[0.0, 0.1]` 1/V，这意味着默认情况下沟道区的速度饱和处于关闭状态。

### **Drift region surface scattering factor** — 漂移区表面散射因子 `0` `V`（默认）

漏极电流方程中的表面散射因子 *θsurf*。此参数仅适用于漂移区，用于考虑由垂直电场引起的积累层中的散射。

### **Channel-length modulation factor** — 沟道长度调制因子 `0`（默认）

*GΔL* 方程中对数项的乘数因子 α。有关此方程的详细信息，请参阅 N-Channel MOSFET 模块参考页。此参数描述沟道长度调制的起始。对于在饱和区表现出正电导的器件特性，请增大参数值以拟合此行为。此参数仅适用于沟道区。默认值为 `0`，这意味着默认情况下沟道长度调制处于关闭状态。

### **Channel-length modulation voltage** — 沟道长度调制电压 `5e-2` `V`（默认）

*GΔL* 方程中的电压 *Vp*。有关此方程的详细信息，请参阅 N-Channel MOSFET 模块参考页。此参数控制沟道长度调制开始生效时的漏极电压。此参数仅适用于沟道区。

### **Linear-to-saturation transition coefficient** — 线性到饱和过渡系数 `8`（默认）

此参数控制 MOSFET 从线性区过渡到饱和区的平滑程度，特别是在启用速度饱和时。此参数通常可以保留默认值，但您可以使用它来微调 *ID*–*VDS* 特性的拐点。此参数同时适用于沟道区和漂移区。此参数值的预期范围在 2 到 8 之间。

### **Measurement temperature** — 测量温度 `25` `degC`（默认）

测量模块参数时的温度 *Tm1*。如果 **Temperature Dependence** 选项卡上的 **Device simulation temperature** 参数与此值不同，则器件参数将根据仿真温度和参考温度从其定义值进行缩放。有关详细信息，请参阅温度依赖性。

### 欧姆电阻

### **Source ohmic resistance** — 源极欧姆电阻 `1e-4` `Ohm`（默认）| 非负标量

晶体管源极电阻，即与源极接触关联的串联电阻。

### **Drain ohmic resistance** — 漏极欧姆电阻 `0.07` `Ohm`（默认）| 非负标量

晶体管漏极电阻，即与漏极接触以及漂移区 LOCOS 部分关联的串联电阻，该部分受所施加栅极电压的影响不大。

### **Gate ohmic resistance** — 栅极欧姆电阻 `8.4` `Ohm`（默认）| 非负标量

晶体管栅极电阻，即与栅极接触关联的串联电阻。

### **Drift region low-bias resistance for gated region** — 栅控区漂移区低偏压电阻 `0.1` `Ohm`（默认）| 非负标量

漏极电流方程中的电阻 *RD*。它表示在顶部和底部界面均无耗尽的情况下漂移区体部分的电阻。

### **Drift region depletion layer thickness factor** — 漂移区耗尽层厚度因子 `0.2`（默认）

漏极电流方程中的参数 *λD*。它是在零偏压时垂直深度 *y1* 与 *y2* 的比值，其中 *y1* 表示空间电荷区，*y2* 表示漂移区未耗尽的部分。

### 电容

### **Oxide capacitance, [channel drift\_region]** — 氧化层电容 `[1600, 1000]` `pF`（默认）

平行板栅极-沟道和栅极-漂移区电容。该参数值为一个二元素向量，第一个元素对应沟道，第二个元素对应漂移区。

### **Gate-source overlap capacitance** — 栅源交叠电容 `15` `pF`（默认）

与栅电极和源极阱交叠关联的固定线性电容。

### **Gate-drain overlap capacitance** — 栅漏交叠电容 `15` `pF`（默认）

与栅电极和漏极阱交叠关联的固定线性电容。

### 体二极管

### **Reverse saturation current** — 反向饱和电流 `1e-13` `A`（默认）

体二极管方程中用 *Is* 符号表示的电流。

### **Built-in voltage** — 内建电压 `0.6` `V`（默认）

二极管的内建电压，在体二极管方程中用 *Vbi* 符号表示。

### **Ideality factor** — 理想因子 `1`（默认）

体二极管方程中用 *n* 符号表示的因子。

### **Zero-bias junction capacitance** — 零偏压结电容 `1800` `pF`（默认）

仅由体二极管引起的、零偏压时漏极与体接触之间的电容。在体二极管方程中用 *Cj0* 符号表示。

### **Transit time** — 渡越时间 `50e-9` `s`（默认）

体二极管方程中用 *τ* 符号表示的时间。

### 温度依赖性

### **Parameterization** — 温度依赖性参数化 `None — Simulate at parameter measurement temperature`（默认）| `Model temperature dependence`

选择以下温度依赖性参数化方法之一：

- `None — Simulate at parameter
  measurement temperature` —
  不对温度依赖性建模。这是默认方法。
- `Model temperature dependence`
  — 对温度相关效应建模。为器件仿真温度
  *Ts* 以及
  其他模块参数的温度缩放系数提供值。

### **Device simulation temperature** — 器件仿真温度 `25` `degC`（默认）

仿真器件时的温度 *Ts*

### **Gain temperature exponent, [channel drift\_region]** — 增益温度指数 `[1.3, 1.3]`（默认）

该参数值为一个二元素向量，第一个元素对应沟道，第二个元素对应漂移区。在沟道区和漂移区中，均假定 MOSFET 增益 *β* 随温度 *β* = *βm1* (*Tm1*/*T*s)^*ηβ* 呈指数缩放。*βm1* 是沟道或漂移区增益的值，由 **Main** 选项卡中的 **Gain, [channel drift\_region]** 参数指定。*η*β 是 **Gain temperature exponent, [channel drift\_region]** 参数的对应元素。

### **Flatband voltage temperature coefficient, [channel drift\_region]** — 平带电压温度系数 `[.0005, .0005]` `V/K`（默认）

该参数值为一个二元素向量，第一个元素对应沟道，第二个元素对应漂移区。假定平带电压 *V*FB 随温度线性缩放，*V*FB = *V*FBm1 + (*Ts* – *Tm1*)*S*T,VFB。*VFBm1* 是沟道或漂移区平带电压的值，由 **Main** 选项卡中的 **Flatband voltage, [channel drift\_region]** 参数指定。*ST,VFB* 是 **Flatband voltage temperature coefficient, [channel drift\_region]** 参数的对应元素。

### **Surface potential at strong inversion temperature coefficient** — 表面电位 `-8.5e-4` `V/K`（默认）

假定强反型时的表面电位 2*ϕB* 随温度线性缩放，*2ϕB* = 2*ϕBm1* + (*Ts* – *Tm1*)*ST,ϕB*。2*ϕBm1* 是 **Main** 选项卡中 **Surface potential at strong inversion** 参数的值，*ST,ϕB* 是 **Surface potential at strong inversion temperature coefficient**。

### **Velocity saturation temperature exponent, [channel drift\_region]** — 速度饱和温度指数 `[1.04, 1.04]`（默认）

该参数值为一个二元素向量，第一个元素对应沟道，第二个元素对应漂移区。假定速度饱和 *θsat* 随温度呈指数缩放，*θsat* = *θsat,m1* (*Tm1*/*Ts*)^*ηθ*。*θsat,m1* 是沟道或漂移区速度饱和因子的值，由 **Main** 选项卡中的 **Velocity saturation factor, [channel drift\_region]** 参数指定。*η*θ 是 **Velocity saturation temperature exponent, [channel drift\_region]** 参数的对应元素。

### **Ohmic resistance temperature exponent** — 欧姆电阻温度指数 `0.95`（默认）

假定串联电阻对应于半导体电阻。因此，它们随温度升高呈指数下降。*Ri* = *Ri,m1* (*T*/*T*s)^*ηR*，其中 *i* 分别为 *Sm1*、*D* 或 *G*，对应源极、漏极或栅极串联电阻。*Ri,m1* 是 **Ohmic Resistance** 选项卡中对应串联电阻参数的值，*ηR* 是 **Ohmic resistance temperature exponent**。

### **Drift region low-bias resistance temperature exponent for gated portion** — 栅控部分漂移区低偏压电阻温度指数 `0.95`（默认）

电阻 *R*D，即漂移区体部分的低偏压电阻，其缩放方式与其他串联电阻类似。为此电阻单独设置温度指数值提供了额外的自由度。

### **Body diode reverse saturation current temperature exponent** — 体二极管反向饱和电流温度指数 `3`（默认）

假定体二极管的反向饱和电流与本征载流子浓度的平方成正比，*ni* = *NC* exp(–*EG*/2*kB**T*)。*NC* 是温度相关的有效态密度，*EG* 是半导体材料的温度相关带隙。为避免引入另一个温度缩放参数，模块忽略带隙的温度依赖性，并对所有器件类型使用硅在 300K 时的带隙（1.12eV）。因此，温度缩放后的反向饱和电流由下式给出

Is=Is,m1(TsTm1)ηIs⋅exp(EGkB⋅(1Tm1−1Ts)).

*Is,m1* 是 **Body Diode** 选项卡中 **Reverse saturation current** 参数的值，*kB* 是玻尔兹曼常数（8.617x10-5eV/K），*ηIs* 是 **Body diode reverse saturation current temperature exponent**。默认值为 `3`，因为硅的 *NC* 大致与 *T3/2* 成正比。您可以通过务实地选择 *ηIs* 来弥补忽略带隙温度依赖性的影响。

## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2019b：热网络 simlog 路径

从 R2019b 起，可以在内部或外部对此模块的热网络进行建模。

因此，与热网络对应的 simlog 路径已更改。如果您有以编程方式访问 simlog 的脚本，则必须手动更新它以反映这些更改。

## 描述

适用于高压的 N 沟道横向扩散金属氧化物半导体或垂直扩散金属氧化物半导体晶体管

N-Channel LDMOS FET 模块对适用于高压的 LDMOS（或 VDMOS）晶体管进行建模。该模型基于表面势，并包含由扩展漏极（漂移）区引起的效应：

- 与漂移区相关的非线性电容效应
- 漂移区中的表面散射和速度饱和
- 沟道区中的速度饱和和沟道长度调制
- 模型内部的电荷守恒，因此您可以将该模型用于电荷敏感仿真
- 本征体二极管
- 体二极管模型中的反向恢复
- 物理参数的温度缩放
- 对于具有暴露热端口的选项（请参阅热端口），动态自热

下图显示了该模型的物理结构：

沟道区位于 p+ 区中，从重掺杂 n 型源极阱延伸到 p+ 区的末端。漂移区是轻掺杂漏极扩展区。再往下是 p 型外延层，然后整个结构位于重掺杂 p 型衬底上。栅氧化层在整个沟道区以及部分漂移区上较薄。在漂移区更深处，栅氧化层在硅局部氧化（LOCOS）区中具有更大的厚度。

下图显示了该模型的等效电路。

该建模方法类似于 [1]。栅极接触与源极和漏极 n 阱的重叠被建模为集总线性电容。沟道（p+）区使用基于表面势的 MOSFET 模型进行建模。源极/体与漏极之间的 pn 结使用理想二极管进行建模，包括结电容和扩散电容。薄栅氧化层下方的漂移区根据表面势公式进行建模，其中包括：

- 半导体-氧化物界面处积累层产生的电流
- 漂移区更深处流向漏极的电子产生的电流

外延层与漂移区之间的空间电荷区通过对流经漂移区体区的电流的夹断效应来表示。漂移区的 LOCOS 部分被建模为集总串联电阻，并且还有串联电阻添加到源极和栅极接触。

有关沟道模型的详细描述，请参阅 N-Channel MOSFET 模块的基于表面势的模型。漂移区模型同样使用泊松方程从表面势推导而来。对于在渐变沟道近似下的 n 型半导体，定义方程为：

∂2ψ∂y2≈qNDεSi[−1−exp(−ψ−2ϕBϕT)+exp(ψ−VCBϕT)]

ϕT=kBTq

其中：

- *ψ* 是静电势。
- *q* 是电子电荷的幅值。
- *ND* 是漂移区的掺杂浓度。
- *ɛSi* 是半导体材料（例如硅）的介电常数。
- *ϕB* 是本征费米能级与漂移区深处费米能级之间的差值。
- *VCB* 是漂移区相对于体的准费米势。
- *ϕT* 是热电压。
- *kB* 是玻尔兹曼常数。
- *T* 是温度。

忽略直流电流模型中的反型，得到以下电流表达式：

ID=11+θsatVDK[flinRDVDK+β2⋅VGK2−VGD21+θsurf2(VGK+VGD)]

其中：

- *ID* 是漏极电流。
- *θsat* 是速度饱和。
- *Vij* 是节点 *i* 和 *j* 之间的电压差，其中下标 D 和 K 分别指漏极以及沟道与漂移区的结，下标 G 指栅极，并施加了由平带电压引起的修正。
- *flin*/*RD* 表示漂移区体区的电导，包括由于外延-漂移界面耗尽引起的夹断效应。
- *β* 是漂移区与薄栅氧化层之间界面处积累层的增益。
- *θsurf* 是考虑由垂直电场引起的积累层中散射的参数。

该方程描述了漂移区体区的夹断，

flin=1−λDVbi+VSB−VbiVbi

其中：

- *λD* 是表示零偏置时沿外延-漂移界面的空间电荷区 n 侧垂直深度除以零偏置时漂移区未耗尽部分的垂直深度的参数。

  在图中，顶部实线是半导体表面。下方实线是漂移区与外延层之间的结。虚线显示了漂移-外延界面周围空间电荷区的范围。*λD* 是零偏置时的 *y1*/*y2*。
- *Vbi* 是外延-漂移二极管的内建电压。
- *VSB* 是源-体电压，用作施加在外延-漂移二极管上的偏置的近似值。使用该电压代替 *VKB* 在数值上更稳定，并且是合理的，因为在晶体管导通状态下，大部分漏源电压降落在漂移区上。

电荷模型类似于基于表面势的 MOSFET 模型，并增加了用于考虑漂移区电荷的表达式。该模块使用 [1] 中描述的推导方程，其中包括漂移区中的反型和积累。

### 体二极管建模

该模块将体二极管建模为理想指数二极管，同时具有结电容和扩散电容：

Idio=Is[exp(−VDBnϕT)−1]

Cj=Cj01+VDBVbi

Cdiff=τIsnϕTexp(−VDBnϕT)

其中：

- *Idio* 是通过二极管的电流。
- *Is* 是反向饱和电流。
- *VDB* 是漏-体电压。
- *n* 是理想因子。
- *ϕT* 是热电压。
- *Cj* 是二极管的结电容。
- *Cj0* 是零偏置结电容。
- *Vbi* 是内建电压。
- *Cdiff* 是二极管的扩散电容。
- *τ* 是渡越时间。

这些电容通过显式计算电荷来定义，然后对电荷求导以给出上述电容表达式。该模块将电容性二极管电流计算为相关电荷的时间导数，类似于基于表面势的 MOSFET 模型中的计算。

### 温度依赖性建模

默认行为是不对温度依赖性进行建模，器件在您提供模块参数时所对应的温度下进行仿真。要在仿真期间对温度依赖性进行建模，请在 **Temperature Dependence** 选项卡上的 **Parameterization** 参数中选择 `Model temperature dependence`。

该模型包括温度对电容特性的影响，以及在仿真期间对晶体管静态行为温度依赖性的建模。

**Main** 选项卡上的 **Measurement temperature** 参数指定提取其他器件参数时的温度 *Tm1*。**Temperature Dependence** 参数提供仿真温度 *Ts* 以及其他器件参数的温度缩放系数。有关详细信息，请参阅 Temperature Dependence。

### 热端口

您可以暴露热端口，以对产生的热量和器件温度的影响进行建模。要暴露热端口，请将 **Modeling option** 参数设置为以下之一：

- `No thermal port` — 该模块不包含热端口，也不仿真器件中的热量产生。
- `Show thermal port` — 该模块包含一个热端口，允许您对传导损耗产生的热量进行建模。为了提高数值效率，热状态不影响模块的电气行为。

有关使用热端口以及 **Thermal Port** 参数的详细信息，请参阅 Simulating Thermal Effects in Semiconductors。

该模块的热选项包括动态自热。这使您可以仿真自热对器件电气特性的影响。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值来指定模型中变量的预期幅值。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。

### 绘制基本 I-V 特性

您可以在不构建完整模型的情况下绘制 N-Channel LDMOS FET 模块的基本 I-V 特性。使用这些图来探索参数选择对器件特性的影响。如果您根据数据手册对模块进行参数化，可以将图与数据手册进行比较，以检查您是否正确地对模块进行了参数化。如果您有一个完整可用的模型但不知道使用哪个制造器件，可以将图与数据手册进行比较以帮助您做出决定。

要启用此选项，请将 N-Channel LDMOS FET 模块的 **Modeling option** 参数设置为 `No thermal port`。要绘制基本特性，请右键单击该模块，然后从上下文菜单中选择 **Electrical** > **Basic characteristics**。有关 **Basic characteristics** 选项的详细信息，请参阅 Plot Basic I-V Characteristics of Semiconductor Blocks。
