---
type: simulink-block
title: 'Pressure-Reducing 3-Way Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Pressure Control Valves'
documentation_page: 'pressurereducing3wayvalveil'
documentation_source_path: 'ref/pressurereducing3wayvalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure-Reducing 3-Way Valve (IL)

## 端口

### 守恒端口

### **A** — 液体端口，等温液体

阀的液体出口端口。

### **P** — 液体端口，等温液体

阀的液体入口端口。

### **T** — 液体端口，等温液体

阀的液体泄放端口。
### 输入

### **Ps** — 受控压差物理信号

用于受控阀操作的变压设定压力信号。

#### 依赖关系

要启用此端口，请将 **Set pressure control** 设置为 `Controlled`。

## 参数

### 参数

### **Set pressure control** — 阀操作方式 `Constant`（默认）| `Controlled`

阀操作方式。`Constant` 阀在固定的压力调节范围和压力过渡范围内线性开启或关闭，或者根据您提供的表格化压力和开口面积数据开启或关闭。`Controlled` 阀根据端口 **Ps** 处的可变设定压力信号，在固定的压力调节和压力过渡范围内开启或关闭。所选设置同时适用于减压阀和泄压阀操作。

### **Opening parameterization** — 开口参数化类型 `Linear`（默认）| `Tabulated`

对阀开启或关闭进行建模的方法。阀开口可以线性参数化，即将开口面积与所提供的压力范围相关联，也可以通过您提供的将阀开口面积与压差数据相关联的值表进行参数化。

#### 依赖关系

要启用此端口，请将 **Set pressure control** 设置为 `Constant`。

### **Set pressure differential for reducing valve** — 端口 P 处阀关闭的设定压力 `0.6` MPa（默认）| 标量

端口 **T** 和端口 **A** 之间的压差。当超过此设定压差时，端口 **P** 处的阀开始关闭。关闭过程按照 **Opening parameterization** 中的定义进行线性参数化或通过查找表参数化。

### **Pressure regulation range** — 阀工作压力范围 `3e-2` MPa（默认）| 标量

减压阀的工作压力范围。压力调节范围介于 **Set pressure differential** 和阀最大工作压力之间。在 **Pressure regulation range** 结束时，减压阀关闭，**Pressure transition range** 开始。

#### 依赖关系

要启用此参数，请设置

- **Set pressure control** 为 `Controlled`，或
- **Set pressure control** 为 `Constant` 且 **Opening parameterization** 为 `Linear`。

### **Pressure transition range** — 端口 P 和 T 均关闭时阀的压力范围 `2e-2` MPa（默认）| 标量

三通阀的压力范围。此参数定义了从 **Pressure regulation range** 结束时开始的压力范围，在该范围内端口 **P** 和 **T** 均关闭。低于此范围时，端口 **P** 处的减压阀打开以允许流动；高于此范围时，端口 **T** 处的泄压阀打开。

#### 依赖关系

要启用此参数，请设置以下任一：

- **Set pressure control** 为 `Controlled`
- **Set pressure control** 为 `Constant` 且 **Opening parameterization** 为 `Linear`

### **Maximum opening area** — 端口最大开口面积 `1e-4` m^2（默认）| 正标量

阀（**P**-**A** 或 **A**-**T**）在全开位置时的横截面积。

#### 依赖关系

要启用此参数，请设置以下任一：

- **Set pressure control** 为 `Controlled`
- **Set pressure control** 为 `Constant` 且 **Opening parameterization** 为 `Linear`

### **Leakage area** — 全关位置时的间隙面积 `1e-10` m^2（默认）| 正标量

阀处于全关位置时所有间隙的总和。任何小于此值的面积都会被饱和到指定的泄漏面积。这通过保持流动的连续性来帮助提高数值稳定性。

#### 依赖关系

要启用此参数，请设置以下任一：

- **Set pressure control** 为 `Controlled`
- **Set pressure control** 为 `Constant` 且 **Opening parameterization** 为 `Linear`

### **Pressure differential vector for reducing valve** — 减压阀表格化参数化的压差值 `0.6 : 0.02 : 0.7` MPa（默认）| 1×*n* 向量

用于开口面积表格化参数化的压差值向量。向量元素与 **Opening area vector reducing valve** 参数中的值一一对应。压差向量值按升序列出，且元素数量必须与 **Opening area vector reducing valve** 参数相同。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Tabulated`。

### **Opening area vector reducing valve** — 减压阀表格化参数化的阀开口面积向量 `[1e-05, 8e-06, 6e-06, 4e-06, 2e-06, 1e-10]`m^2（默认）| 1×*n* 向量

用于开口面积表格化参数化的开口面积值向量。向量元素必须与 **Pressure differential vector for reducing valve** 参数中的值一一对应。面积按降序列出。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Tabulated`。

### **Pressure differential vector for relief valve** — 泄压阀表格化参数化的压差值 `0.68 : 0.02 : 0.78` MPa（默认）| 1×*n* 向量

用于开口面积表格化参数化的压差值向量。向量元素与 **Opening area vector relief valve** 参数中的值一一对应。压差向量值按升序列出，且元素数量必须与 **Opening area vector relief valve** 参数相同。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Tabulated`。

### **Opening area vector for relief valve** — 泄压阀表格化参数化的阀开口面积 `[1e-10, 2e-06, 4e-06, 6e-06, 8e-06, 1e-05]`m^2（默认）| 1×*n* 向量

用于开口面积表格化参数化的开口面积值向量。向量元素必须与 **Pressure differential vector for relief valve** 参数中的值一一对应。面积按升序列出。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Tabulated`。

### **Cross-sectional area at ports A, P & T.** — 守恒端口处的孔口面积 `inf` m^2（默认）| 正标量

入口和出口端口 **A**、**P** 和 **T** 处的横截面积。此面积用于确定通过孔口的质量流量的压力-流量方程。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

用于修正理论流动中排放损失的修正因子。Simscape™ Fluids™ 中阀的默认流量系数为 0.64。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过阀的层流的上限雷诺数。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| [0,1] 范围内的正标量

连续平滑因子，当阀处于接近开启或接近关闭位置时，为流量响应引入一层渐变。将此值设置为小于 1 的非零值可提高这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear`。

### **Pressure recovery** — 是否考虑面积扩大时的压力升高 `off`（默认）| `on`

考虑流体从较小横截面积区域流向较大横截面积区域时的压力升高。当您清除 **Pressure recovery** 复选框时，不会捕获此压力升高。

### **Opening dynamics** — 是否引入由孔口开启引起的流动滞后 `off`（默认）| `on`

考虑由阀开启引起的流体系统瞬态效应。选择 **Opening dynamics** 通过引入流量响应的一阶滞后来近似开启条件。**Opening time constant** 也会影响所建模的开启动态特性。

### **Reducing valve initial opening area** — 仿真开始时端口 P 处的开口面积 `1e-4` m^2（默认）| 正标量

动态开启时端口 **P** 处的初始横截面积。此值用于计算下一时间步 **P** 和 **A** 之间动态开启的瞬时开口面积。

#### 依赖关系

要启用此参数，请选择 **Opening dynamics**。

### **Relief valve initial opening area** — 仿真开始时端口 T 处的开口面积 `1e-10` m^2（默认）| 正标量

动态开启时端口 **T** 处的初始开口横截面积。此值用于计算下一时间步 **A** 和 **T** 之间动态开启的瞬时开口面积。

#### 依赖关系

要启用此参数，请选择 **Opening dynamics**。

### **Opening time constant** — 阀开启时间常数 `0.1` s（默认）| 正标量

捕获阀从一个位置开启或关闭到另一位置时流体达到稳态所需时间的常数。此参数影响所建模的开启动态特性。

#### 依赖关系

要启用此参数，请选择 **Opening dynamics**。

### 故障

### **Pressure-Reducing 3-Way Valve Area fault** — 对阀面积故障建模的选项 `Add fault`

对模块中的阀面积故障建模的选项。要添加故障，请点击 **Add fault** 超链接。发生故障时，通常由开口参数化设置的阀面积将根据 **Opening area when faulted** 参数中指定的值进行设置。

### **Valve areas when faulted** — 故障时的阀特性 `Reducing valve closed and relief valve open`（默认）| `Reducing valve open and relief valve closed` | `Maintain last value`

故障阀类型。您可以选择阀在开启、关闭时卡滞，或在触发故障时保持当时的面积。

#### 依赖关系

要启用此参数，请点击 **Add fault** 超链接。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Pressure Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a：使用 Simscape 故障接口对故障建模

Pressure-Reducing 3-Way Valve (IL) 模块现在支持 Simscape 故障接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

## 描述

等温液体系统中的组合式泄压阀和减压阀

Pressure-Reducing 3-Way Valve (IL) 是泄压阀和减压阀的组合。它通过限制端口 **P** 处的流入面积并将流量从端口 **T** 排出，来维持阀出口端口 **A** 处的压力。

### 阀功能

该模块通过将端口 **A** 和端口 **T** 之间的压力差与一组压力阈值范围进行比较来控制阀操作。当 **A** 和 **T** 之间的压力差 *Pcontrol* 超过 *Pset,reducing* 时，端口 **P** 开始关闭。当 *Pcontrol* 介于 *Pset,reducing*+*Preg* 和 *Pset,reducing*+*Preg*+*Ptransition* 之间时，模块处于过渡范围，端口 **P** 和 **T** 处的两个阀均关闭。当 *Pcontrol* 超过压力过渡范围 *Pset,relief* 时，其中 Pset,relief=Pset,reducing+Preg+Ptransition，端口 **T** 开始打开。

要模拟相对于另一系统元件的压力泄放或压力降低，请参阅 Pressure Compensator Valve (IL)。要模拟阀出口与大气之间的压力降低，请参阅 Pressure-Reducing Valve (IL)。要模拟相对于阀或阀出口与大气压力之间的压力泄放，请参阅 Pressure Relief Valve (IL)。

### 压力控制

当 *Pcontrol*（即 *PA* – *PT*）超过阈值压力 *Pset,reducing* 时，端口 **P** 处的阀开始关闭。当压力超过过渡范围时，或当 *Pcontrol* > *Pset,relief* 时，端口 **T** 处的阀开始打开。阀的关闭和开启均以两种方式进行参数化：

- 当 **Set pressure control** 为 `Controlled` 时，模块使用端口 **Ps** 处的压力信号来控制阀。在此设置中，*Preg* 是 **Pressure regulation range** 参数的值，*Ptransition* 是 **Pressure transition range** 参数的值。当 *Pcontrol* 大于 *Pset,reducing*（即端口 **Ps** 处信号的值）时，减压阀开始关闭。当 *Pcontrol* 大于 *Pset,relief* 且低于 *Pmax,relief* 时，触发泄压阀响应，即端口 **T** 开始打开。*Pmax,relief* 是 **Pressure regulation range** 参数的值与 *Pset,relief* 之和。
- 当 **Set Pressure control** 为 `Constant` 时，端口 **P** 处的阀关闭由线性或表格化参数化连续调节。类似地，端口 **T** 处的泄压阀开启通过线性或查表进行参数化。减压阀（实线）和泄压阀（虚线）的线性参数化示例如下所示。

  如果您将 **Opening parameterization** 设置为 `Linear`，则 *Pset,reducing* 是 **Set pressure differential for reducing valve** 参数的值，*Preg* 是 **Pressure regulation range** 参数的值，*Ptransition* 是 **Pressure transition range** 参数的值。*Pmax,relief* 是 **Pressure regulation range** 参数的值与 *Pset,relief* 之和。

  如果您将 **Opening parameterization** 设置为 `Tabulated`，则 *Pset,reducing* 和 *Pmax,reducing* 分别是 **Pressure differential vector for reducing valve** 的第一个和最后一个参数，*Pset,relief* 和 *Pmax,relief* 分别是 **Pressure differential vector for relief valve** 的第一个和最后一个参数。减压阀和泄压阀的表格化参数化示例如下所示。

### 质量流量方程

通过阀门的动量守恒：

m˙A+m˙reducing+m˙relief=0。

通过阀门的质量流量计算如下：

m˙reducing=CdAPA2ρ¯PRloss,reducing(1−(APAAport)2)Δpreducing[Δpreducing2+Δpcrit,reducing2]1/4，

m˙relief=CdAAT2ρ¯PRloss,relief(1−(AATAport)2)Δprelief[Δprelief2+Δpcrit,relief2]1/4，

其中：

- *Cd* 是 **Discharge coefficient** 参数的值。
- *A* 是端口 **A** 与 **P** 之间或 **A** 与 **T** 之间的瞬时阀门开口面积，由下标指示。
- *A*port 是 **Cross-sectional area at ports A, P & T** 参数的值。
- ρ¯ 是平均流体密度。
- *Δp* 是阀门压差，*pA* – *pB*。

临界压差 *Δpcrit* 是与 **Critical Reynolds number** *Recrit* 相关的压差，即层流与湍流之间的流态转变点，对应于阀门的减压分量或泄压分量，

Δpcrit=πρ¯8A(νRecritCd)2，

其中 *A* 是 *APA* 或 *AAT*，分别对应于阀门的减压分量或泄压分量。

*Pressure loss* 描述由于面积减小而导致的阀门压力降低。*PRloss* 为

PRloss=1−(AAport)2(1−Cd2)−CdAAport1−(AAport)2(1−Cd2)+CdAAport。

*Pressure recovery* 描述由于面积增大而导致的阀门正压力变化。如果您不希望捕获此压力增加，请清除 **Pressure recovery** 复选框。在这种情况下，*PRloss* 为 1。

当 **Set Pressure control** 为 `Constant` 时，模块通过使用减压阀（**P** 到 **A**）或泄压阀（**A** 到 **T**）的开口参数化以及阀门开口动态来计算开口面积 *A*。

### 打开和关闭参数化

当您将 **Opening parameterization** 设置为 `Linear` 时，减压阀的阀门面积为

Avalve=p^reducing(Aleak−Amax)+Amax，

泄压阀的阀门面积为

Avalve=p^relief(Amax−Aleak)+Aleak。

归一化压力 p^ 为

p^=pcontrol−psetpmax−pset，

其中设定压力和最大压力分别是相应的减压阀或泄压阀设置。

当阀门在线性参数化中处于接近打开或接近关闭位置时，您可以通过调整 **Smoothing factor** 参数来保持仿真中的数值鲁棒性。如果 **Smoothing factor** 参数非零，模块会在 *pset* 和 *pmax* 之间平滑地饱和控制压力。有关详细信息，请参阅 Numerical Smoothing。

当您将 **Opening parameterization** 设置为 `Tabulated` 时，*A*leak,PA 和 *A*max,PA 分别是 **Opening area vector reducing valve** 参数的第一个和最后一个元素，*A*leak,AT 和 *A*max,AT 分别是 **Opening area vector for relief valve** 参数的第一个和最后一个元素。模块计算开口面积为

Avalve=tablelookup(pcontrol,TLU,ref,ATLU,pcontrol,interpolation=linear,extrapolation=nearest)。

对于减压阀，模块使用查表方法计算开口面积，其中：

- *pcontrol* 是控制压力，即端口 **A** 和 **T** 之间的压差。
- *pcontrol,TLU,ref* = *pTLU* + *poffset*。
- *pTLU* 是 **Pressure differential vector for reducing valve** 参数。
- *poffset* 是内部压力偏移，使阀门在 *pcontrol,TLU,ref* = *pset,reducing* 时开始关闭。
- *ATLU* 是 **Opening area vector reducing valve** 参数。

对于泄压阀，模块使用查表方法计算开口面积，其中：

- *pcontrol* 是端口 **A** 和 **T** 之间的压差。
- *pcontrol,TLU,ref* = *pTLU* + *poffset*。
- *pTLU* 是 **Pressure differential vector for relief valve** 参数。
- *poffset* 是内部压力偏移，使阀门在 *pcontrol,TLU,ref* = *pset,releif* 时开始打开。
- *ATLU* 是 **Opening area vector for relief valve** 参数。

### 开口动态

如果对 **Opening dynamics** 进行建模，则会在阀门开口的流量响应中引入滞后。*A*valve 变为动态打开或关闭面积 *A*dyn；否则，*A*valve 是稳态开口面积。该面积特定于阀门的减压和泄压分量，分别为 *A*PA 或 *A*AT。动态开口面积的瞬时变化基于 **Opening time constant** *τ* 计算：

p˙dyn=pcontrol−pdynτ。

默认情况下，不对 **Opening dynamics** 进行建模。

### 故障

要对故障进行建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault** 超链接。使用故障参数指定故障属性。有关故障建模的详细信息，请参阅 Introduction to Simscape Faults。

**Valve areas when faulted** 参数有三个故障选项：

- `Reducing valve closed and relief valve open` — 减压阀冻结在其最小值，泄压阀冻结在其最大值，具体取决于 **Opening parameterization**：

  - 当 **Opening parameterization** 设置为 `Linear` 时，减压阀面积冻结在 **Leakage area** 参数的值，泄压阀面积冻结在 **Maximum opening area** 参数的值。
  - 当 **Opening parameterization** 设置为 `Tabulated` 时，减压阀面积冻结在 **Opening area vector** 参数的第一个元素的值，泄压阀面积冻结在 **Opening area vector** 参数的最后一个元素的值。
- `Reducing valve open and relief valve closed` — 减压阀冻结在其最大值，泄压阀冻结在其最小值，具体取决于 **Opening parameterization**：

  - 当 **Opening parameterization** 设置为 `Linear` 时，减压阀面积冻结在 **Maximum opening area** 参数的值，泄压阀冻结在 **Leakage area** 参数的值。
  - 当 **Orifice parameterization** 设置为 `Tabulated` 时，减压阀面积冻结在 **Opening area vector** 参数的最后一个元素的值，泄压阀面积冻结在 **Opening area vector** 参数的第一个元素的值。
- `Maintain last value` — 减压阀和泄压阀面积在触发时冻结在开口面积。

由于阀门面积极值处的数值平滑，模块使用的最小面积大于 **Leakage area** 参数的值，最大面积小于 **Maximum orifice area** 参数的值，与 **Smoothing factor** 值成比例。

故障触发后，阀门在仿真的剩余时间内保持在故障面积。

### 假设和限制

阀门与流体之间的摩擦、流体对阀门部件的液压力以及流体惯性的影响均被忽略。
