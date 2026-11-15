---
type: simulink-block
title: 'P-Channel LDMOS FET'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Semiconductors and Converters / Semiconductors'
documentation_page: 'pchannelldmosfet'
documentation_source_path: 'ref/pchannelldmosfet.html'
language: zh-CN
chinese_source: worker-translation
---

# P-Channel LDMOS FET

## 端口

### 守恒

### **G** — 栅极端子电气

与晶体管栅极端子关联的电气守恒端口。

### **D** — 漏极端子电气

与晶体管漏极端子关联的电气守恒端口。

### **S** — 源极端子电气

与晶体管源极端子关联的电气守恒端口。

### **H** — 热端口 thermal

热守恒端口。

#### 依赖关系

要启用此端口，请将 **Modeling option** 设置为 `Show thermal port`。

## 参数

### **Modeling option** — 是否启用热端口 `No thermal port`（默认） | `Show thermal port`

是否启用模块的热端口，并对生成的热量和器件温度的影响进行建模。

### 主要

### **Gain, [channel drift\_region]** — 增益 `[11.6, .01]` `A/V2`（默认）

MOSFET 各区域的增益 *β*。参数值是一个二元素向量，第一个元素对应沟道，第二个元素对应漂移区。此参数主要定义 *ID*–*VDS* 特性上的线性工作区。两个元素的值都必须大于 0。

### **Flatband voltage, [channel drift\_region]** — 平带电压 `[-1.05, -0.1]` `V`（默认）

平带电压 *VFB* 定义为了在硅表面实现平带条件而必须施加的栅极偏置。参数值是一个二元素向量，第一个元素对应沟道，第二个元素对应漂移区。你还可以使用此参数来因材料功函数差异以及俘获的界面电荷或氧化物电荷而任意移动阈值电压。不过在实践中，通常建议先使用 **Body factor, [channel drift\_region]** 和 **Surface potential at strong inversion, [channel drift\_region]** 参数来修改阈值电压，而仅使用此参数进行微调。

对于短路源-体连接，沟道区的阈值电压近似为

−VT=VFB+2ϕB+2ϕT+γ2ϕB+2ϕT

其中 2*ϕB* 是强反型时的表面势，*γ* 是体因子，二者都针对沟道区。

### **Body factor, [channel drift\_region]** — 体因子 `[3.4, 2.5]` `V1/2`（默认）

表面势方程中的体因子 *γ*。参数值是一个二元素向量，第一个元素对应沟道，第二个元素对应漂移区。

对于沟道区，体因子为

γ=2qεSiNDCox

有关此方程的详细信息，请参阅 N-Channel MOSFET 模块参考页。漂移区方程类似，不同之处在于 *ND* 被掺杂浓度 *NA* 替换。沟道区的参数值主要影响阈值电压。对于漂移区，此参数主要影响电荷模型，并且还对通过漂移区的体电流的夹断行为有较小影响。

### **Surface potential at strong inversion, [channel drift\_region]** — 强反型时的表面势 `[0.95, 0.95]` `V`（默认）

表面势方程中的 2*ϕB* 项。参数值是一个二元素向量，第一个元素对应沟道，第二个元素对应漂移区。

沟道区的参数值也主要影响阈值电压。对于漂移区，此参数仅影响电荷模型。

### **Velocity saturation factor, [channel drift\_region]** — 速度饱和因子 `[0.0, 0.1]` `1/V`（默认）

漏极电流方程中的速度饱和 *θsat*。在良好拟合线性工作会导致饱和电流过高的情况下，请使用此参数。通过增大此参数值，可以降低饱和电流。参数值是一个二元素向量，第一个元素对应沟道，第二个元素对应漂移区。默认值为 `[0.0, 0.1]` 1/V，这意味着默认情况下沟道区的速度饱和处于 off 状态。

### **Drift region surface scattering factor** — 漂移区表面散射因子 `0` `1/V`（默认）

漏极电流方程中的表面散射因子 *θsurf*。此参数仅适用于漂移区，用于考虑由于垂直电场而在积累层中发生的散射。

### **Channel-length modulation factor** — 沟道长度调制因子 `0`（默认）

*GΔL* 方程中对数项的乘数因子 α。有关此方程的详细信息，请参阅 N-Channel MOSFET 模块参考页。此参数描述沟道长度调制的开始。对于在饱和区表现出正电导的器件特性，请增大参数值以拟合此行为。此参数仅适用于沟道区。默认值为 `0`，这意味着默认情况下沟道长度调制处于 off 状态。

### **Channel-length modulation voltage** — 沟道长度调制电压 `5e-2` `V`（默认）

*GΔL* 方程中的电压 *Vp*。有关此方程的详细信息，请参阅 N-Channel MOSFET 模块参考页。此参数控制沟道长度调制开始变得活跃时的漏极电压。此参数仅适用于沟道区。

### **Linear-to-saturation transition coefficient** — 线性到饱和过渡系数 `8`（默认）

此参数控制 MOSFET 从线性区过渡到饱和区的平滑程度，尤其是在启用速度饱和时。通常可以将此参数保留为其默认值，但你可以使用它来微调 *ID*–*VDS* 特性的拐点。此参数同时适用于沟道区和漂移区。此参数值的预期范围在 2 到 8 之间。

### **Measurement temperature** — 测量温度 `25` `degC`（默认）

测量模块参数时的温度 *Tm1*。如果 **温度依赖性** 选项卡上的 **Device simulation temperature** 参数与此值不同，则器件参数将根据仿真温度和参考温度从其定义值进行缩放。有关详细信息，请参阅温度依赖性。

### 欧姆电阻

### **Source ohmic resistance** — 源极欧姆电阻 `1e-4` `Ohm`（默认） | nonnegative scalar

晶体管源极电阻，即与源极接触关联的串联电阻。该值必须大于或等于 `0`。

### **Drain ohmic resistance** — 漏极欧姆电阻 `0.07` `Ohm`（默认） | nonnegative scalar

晶体管漏极电阻，即与漏极接触以及漂移区的 LOCOS 部分关联的串联电阻，后者不受所施加栅极电压的显著影响。该值必须大于或等于 `0`。

### **Gate ohmic resistance** — 栅极欧姆电阻 `8.4` `Ohm`（默认） | nonnegative scalar

晶体管栅极电阻，即与栅极接触关联的串联电阻。该值必须大于或等于 `0`。

### **Drift region low-bias resistance for gated region** — 栅控区域的漂移区低偏置电阻 `0.1` `Ohm`（默认） | nonnegative scalar

漏极电流方程中的电阻 *RD*。它表示在顶部和底部界面没有耗尽时漂移区体区部分的电阻。该值必须大于或等于 `0`。

### **Drift region depletion layer thickness factor** — 漂移区耗尽层厚度因子 `0.2`（默认）

漏极电流方程中的参数 *λD*。它是零偏置时垂直深度 *y1* 和 *y2* 的比值，其中 *y1* 表示空间电荷区，*y2* 表示漂移区的未耗尽部分。有关图示，请参阅 N-Channel LDMOS FET 模块参考页。

### 电容

### **Oxide capacitance, [channel drift\_region]** — 氧化层电容 `[1600.0, 1000.0]` `pF`（默认）

平行板栅-沟道电容和栅-漂移区电容。参数值是一个二元素向量，第一个元素对应沟道，第二个元素对应漂移区。

### **Gate-source overlap capacitance** — 栅-源交叠电容 `15` `pF`（默认）

与栅电极和源极阱交叠关联的固定线性电容。

### **Gate-drain overlap capacitance** — 栅-漏交叠电容 `15` `pF`（默认）

与栅电极和漏极阱交叠关联的固定线性电容。

### 体二极管

### **Reverse saturation current** — 反向饱和电流 `1e-13` `A`（默认）

体二极管方程中由 *Is* 符号表示的电流。

### **Built-in voltage** — 内建电压 `0.6` `V`（默认）

二极管的内建电压，在体二极管方程中由 *Vbi* 符号表示。

### **Ideality factor** — 理想因子 `1`（默认）

体二极管方程中由 *n* 符号表示的因子。

### **Zero-bias junction capacitance** — 零偏结电容 `1800` `pF`（默认）

仅由体二极管引起的、零偏置时漏极与体接触之间的电容。它在体二极管方程中由 *Cj0* 符号表示。

### **Transit time** — 渡越时间 `50` `ns`（默认）

体二极管方程中由 *τ* 符号表示的时间。

### 温度依赖性

### **Parameterization** — 温度依赖性参数化 `None — Simulate at parameter measurement temperature`（默认） | `Model temperature dependence`

选择以下温度依赖性参数化方法之一：

- `None — Simulate at parameter measurement temperature` — 不对温度依赖性建模。这是默认方法。
- `Model temperature dependence` — 对温度相关效应建模。为器件仿真温度 *Ts* 以及其他模块参数的温度缩放系数提供值。

### **Device simulation temperature** — 器件仿真温度 `25` `degC`（默认）

仿真器件时的温度 *Ts*。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Model temperature dependence` 时，此参数才可见。

### **Gain temperature exponent, [channel drift\_region]** — 增益温度指数 `[1.3, 1.3]`（默认）

参数值是一个二元素向量，第一个元素对应沟道，第二个元素对应漂移区。在沟道区和漂移区中，均假定 MOSFET 增益 *β* 随温度按指数规律缩放，*β* = *βm1* (*Tm1*/*Ts*)^*ηβ*。*βm1* 是沟道或漂移区增益的值，由 **主要** 选项卡中的 **Gain, [channel drift\_region]** 参数指定。*ηβ* 是 **Gain temperature exponent, [channel drift\_region]** 参数中的对应元素。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Model temperature dependence` 时，此参数才可见。

### **Flatband voltage temperature coefficient, [channel drift\_region]** — 平带电压温度系数 `[0.0005, 0.0005]` `V/K`（默认）

参数值是一个二元素向量，第一个元素对应沟道，第二个元素对应漂移区。假定平带电压 *VFB* 随温度线性缩放，*VFB* = *VFBm1* + (*Ts* – *Tm1*)*ST,VFB*。*VFBm1* 是沟道或漂移区平带电压的值，由 **主要** 选项卡中的 **Flatband voltage, [channel drift\_region]** 参数指定。*ST,VFB* 是 **Flatband voltage temperature coefficient, [channel drift\_region]** 参数中的对应元素。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Model temperature dependence` 时，此参数才可见。

### **Surface potential at strong inversion temperature coefficient** — 强反型表面势温度系数 `-8.5e-4` `V/K`（默认）

假定强反型时的表面势 2*ϕB* 随温度线性缩放，*2ϕB* = 2*ϕBm1* + (*Ts* – *Tm1*)*ST,ϕB*。2*ϕBm1* 是 **主要** 选项卡中 **Surface potential at strong inversion** 参数的值，*ST,ϕB* 是 **Surface potential at strong inversion temperature coefficient**。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Model temperature dependence` 时，此参数才可见。

### **Velocity saturation temperature exponent, [channel drift\_region]** — 速度饱和温度指数 `[1.04, 1.04]`（默认）

参数值是一个二元素向量，第一个元素对应沟道，第二个元素对应漂移区。假定速度饱和 *θsat* 随温度按指数规律缩放，*θsat* = *θsat,m1* (*Tm1*/*Ts*)^*ηθ*。*θsat,m1* 是沟道或漂移区速度饱和因子的值，由 **主要** 选项卡中的 **Velocity saturation factor, [channel drift\_region]** 参数指定。*ηθ* 是 **Velocity saturation temperature exponent, [channel drift\_region]** 参数中的对应元素。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Model temperature dependence` 时，此参数才可见。

### **Ohmic resistance temperature exponent** — 欧姆电阻温度指数 `0.95`（默认）

假定串联电阻对应于半导体电阻。因此，它们随温度升高而按指数规律减小。*Ri* = *Ri,m1* (*Tm1*/*Ts*)^*ηR*，其中 *i* 为 S、D 或 G，分别对应源极、漏极或栅极串联电阻。*Ri,m1* 是 **欧姆电阻** 选项卡中相应串联电阻参数的值，*ηR* 是 **Ohmic resistance temperature exponent**。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Model temperature dependence` 时，此参数才可见。

### **Drift region low-bias resistance temperature exponent for gated portion** — 栅控部分的漂移区低偏置电阻温度指数 `0.95`（默认）

电阻 *RD*，即漂移区体区部分的低偏置电阻，其缩放方式与其他串联电阻类似。为此电阻单独提供一个温度指数值可增加一个自由度。

#### 依赖关系

仅当为 **Parameterization** 参数选择 `Model temperature dependence` 时，此参数才可见。

### **Body diode reverse saturation current temperature exponent** — 体二极管反向饱和电流温度指数 `3`（默认）

假定体二极管的反向饱和电流与本征载流子浓度 *ni* = *NC* exp(–*EG*/2*kB**T*) 的平方成正比。*NC* 是随温度变化的有效态密度，*EG* 是半导体材料随温度变化的带隙。为避免引入另一个温度缩放参数，模块忽略带隙的温度依赖性，并对所有器件类型使用硅在 300K 时的带隙（1.12eV）。因此，经过温度缩放的反向饱和电流由下式给出

Is=Is,m1(TsTm1)ηIs⋅exp(EGkB⋅(1Tm1−1Ts)).

*Is,m1* 是 **体二极管** 选项卡中 **Reverse saturation current** 参数的值，*kB* 是玻尔兹曼常数（8.617x10-5eV/K），*ηIs* 是 **Body diode reverse saturation current temperature exponent**。默认值为 `3`，因为硅的 *NC* 大致与 T3/2 成正比。你可以通过务实地选择 *ηIs* 来弥补忽略带隙温度依赖性所带来的影响。

#### 依赖项

仅当为 **Parameterization** 参数选择 `Model temperature dependence` 时，此参数才可见。

## 所属库

Simscape / Electrical / Semiconductors & Converters

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

### R2019b：热网络 simlog 路径

从 R2019b 起，可以在内部或外部对该模块的热网络进行建模。

因此，与热网络对应的 simlog 路径已更改。如果您的脚本以编程方式访问 simlog，则必须手动更新它以反映这些更改。

## 描述

适用于高电压的 P-Channel 横向扩散金属氧化物半导体或垂直扩散金属氧化物半导体晶体管

P-Channel LDMOS FET 模块对适用于高电压的 LDMOS（或 VDMOS）晶体管进行建模。该模型基于表面电势，并包括由扩展漏极（漂移）区引起的效应：

- 与漂移区相关的非线性电容效应
- 漂移区中的表面散射和速度饱和
- 沟道区中的速度饱和和沟道长度调制
- 模型内部的电荷守恒，因此可将该模型用于电荷敏感仿真
- 本征体二极管
- 体二极管模型中的反向恢复
- 物理参数的温度缩放
- 对于具有外露热端口的选项（请参见热端口），动态自热

有关物理背景和定义方程的信息，请参见 N-Channel LDMOS FET 模块参考页。LDMOS 模型的 p 型和 n 型版本均使用相同的底层代码，并采用适当的电压变换，以考虑不同的器件类型。

电荷模型与基于表面电势的 MOSFET 模型类似，并具有附加表达式以考虑漂移区中的电荷。该模块使用 [1] 中描述的推导方程，其中包括漂移区中的反型和积累。

### 对体二极管建模

该模块将体二极管建模为具有结电容和扩散电容的理想指数二极管：

Idio=Is[exp(−VBDnϕT)−1]

Cj=Cj01+VBDVbi

Cdiff=τIsnϕTexp(−VBDnϕT)

其中：

- *Idio* 是流过二极管的电流。
- *Is* 是反向饱和电流。
- *VBD* 是体-漏电压。
- *n* 是理想因子。
- *ϕT* 是热电压。
- *Cj* 是二极管的结电容。
- *Cj0* 是零偏结电容。
- *Vbi* 是内建电压。
- *Cdiff* 是二极管的扩散电容。
- *τ* 是渡越时间。

这些电容通过电荷的显式计算来定义，然后对这些电荷进行微分以得到上述电容表达式。该模块将电容性二极管电流计算为相关电荷的时间导数，类似于基于表面电势的 MOSFET 模型中的计算。

### 对温度依赖性建模

默认行为是不对温度依赖性进行建模，器件在您提供模块参数所对应的温度下进行仿真。要在仿真期间对温度依赖性进行建模，请在 **Temperature Dependence** 选项卡上的 **Parameterization** 参数中选择 `Model temperature dependence`。

该模型包括温度对电容特性的影响，并在仿真期间对晶体管静态行为的温度依赖性进行建模。

**Main** 选项卡上的 **Measurement temperature** 参数指定提取其他器件参数时的温度 *Tm1*。**Temperature Dependence** 选项卡提供仿真温度 *Ts* 以及其他器件参数的温度缩放系数。有关更多信息，请参见温度依赖性。

### 热端口

您可以外露热端口，以对生成的热量和器件温度的影响进行建模。要外露热端口，请将 **Modeling option** 参数设置为以下任一项：

- `No thermal port` — 该模块不包含热端口，也不仿真器件中的热量生成。
- `Show thermal port` — 该模块包含热端口，允许您对传导损耗生成的热量进行建模。为了提高数值效率，热状态不影响模块的电气行为。

有关使用热端口以及 **Thermal Port** 参数的更多信息，请参见 Simulating Thermal Effects in Semiconductors。

如果外露热端口，则该模块包括动态自热。这使您可以仿真自热对器件电气特性的影响。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关更多信息，请参见 Set Priority and Initial Target for Block Variables。

使用标称值指定模型中变量的预期量级。基于标称值使用系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关更多信息，请参见 System Scaling by Nominal Values。

### 绘制基本 I-V 特性

您可以在不构建完整模型的情况下绘制 P-Channel LDMOS FET 模块的基本 I-V 特性。使用这些图来探究参数选择对器件特性的影响。如果您从数据手册对模块进行参数化，则可以将图与数据手册进行比较，以检查您是否正确地对模块进行了参数化。如果您有一个完整的工作模型但不知道使用哪个制造商生产的部件，则可以将图与数据手册进行比较以帮助您做出决定。

要启用此选项，请将 P-Channel LDMOS FET 模块的 **Modeling option** 参数设置为 `No thermal port`。要绘制基本特性，请右键单击该模块，然后从上下文菜单中选择 **Electrical** > **Basic characteristics**。有关 **Basic characteristics** 选项的更多信息，请参见 Plot Basic I-V Characteristics of Semiconductor Blocks。
