---
type: simulink-block
title: 'Pressure-Reducing 3-Way Valve (IL)'
family: 'isothermal-liquid'
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

### 守恒

### **A** — 液体端口（等温液体）

阀门的液体出口端口。

### **P** — 液体端口（等温液体）

阀门的液体入口端口。

### **T** — 液体端口（等温液体）

阀门的液体泄压端口。

### 输入

### **Ps** — 受控压差物理信号

用于受控阀门操作的变信号设定压力。

#### 依赖关系

要启用此端口，请将 **Set pressure control** 设置为 `Controlled`。

## 参数

### 参数

### **Set pressure control** — 阀门操作方式 `Constant`（默认） | `Controlled`

阀门操作方式。`Constant` 阀在固定的压力调节范围和压力过渡范围内线性开启或关闭，或根据您提供的表列压力和开度面积数据开启或关闭。`Controlled` 阀根据端口 **Ps** 处的可变设定压力信号，在固定的压力调节范围和压力过渡范围内开启或关闭。所选设置同时适用于减压阀和泄压阀操作。

### **Opening parameterization** — 开度参数化类型 `Linear`（默认） | `Tabulated`

对阀门开启或关闭进行建模的方法。阀门开度可以线性参数化，即将开度面积与提供的压力范围关联起来；也可以通过您提供的数值表参数化，即将阀门开度面积与压差数据关联起来。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`。

### **Set pressure differential for reducing valve** — 端口 P 处阀门关闭的设定压力 `0.6` MPa（默认） | scalar

端口 **T** 与端口 **A** 之间的压差。当超过此设定压差时，端口 **P** 处的阀开始关闭。关闭过程按 **Opening parameterization** 中的定义进行线性参数化或查表参数化。

### **Pressure regulation range** — 阀门工作压力范围 `3e-2` MPa（默认） | scalar

减压阀的工作压力范围。压力调节范围位于 **Set pressure differential** 与阀门最大工作压力之间。在 **Pressure regulation range** 结束时，减压阀关闭，并且 **Pressure transition range** 开始。

#### 依赖关系

要启用此参数，请设置

- **Set pressure control** 为 `Controlled`，或
- **Set pressure control** 为 `Constant`，并将 **Opening parameterization** 设置为 `Linear`。

### **Pressure transition range** — 端口 P 和 T 关闭时阀门所处的压力范围 `2e-2` MPa（默认） | scalar

三通阀的压力范围。此参数定义压力范围，该范围从 **Pressure regulation range** 结束时开始；在此范围内，端口 **P** 和 **T** 均关闭。低于此范围时，端口 **P** 处的减压阀打开允许流动；高于此范围时，端口 **T** 处的泄压阀打开。

#### 依赖关系

要启用此参数，请设置以下任一情况：

- **Set pressure control** 为 `Controlled`
- **Set pressure control** 为 `Constant` 且 **Opening parameterization** 为 `Linear`

### **Maximum opening area** — 端口最大开度面积 `1e-4` m^2（默认） | positive scalar

阀门（**P**-**A** 或 **A**-**T**）在全开位置时的横截面积。

#### 依赖关系

要启用此参数，请设置以下任一情况：

- **Set pressure control** 为 `Controlled`
- **Set pressure control** 为 `Constant` 且 **Opening parameterization** 为 `Linear`

### **Leakage area** — 完全关闭位置时的间隙面积 `1e-10` m^2（默认） | positive scalar

阀门处于完全关闭位置时所有间隙之和。任何小于此值的面积都会饱和到指定的泄漏面积。这通过保持流量连续性来提高数值稳定性。

#### 依赖关系

要启用此参数，请设置以下任一情况：

- **Set pressure control** 为 `Controlled`
- **Set pressure control** 为 `Constant` 且 **Opening parameterization** 为 `Linear`

### **Pressure differential vector for reducing valve** — 减压阀表格参数化的压差值 `0.6 : 0.02 : 0.7` MPa（默认） | 1-by-*n* vector

用于开度面积表格参数化的压差值向量。向量元素与 **Opening area vector reducing valve** 参数中的值一一对应。压差向量值按升序列出，并且其元素数量必须与 **Opening area vector reducing valve** 参数相同。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Tabulated`。

### **Opening area vector reducing valve** — 减压阀表格参数化的阀门开度面积向量 `[1e-05, 8e-06, 6e-06, 4e-06, 2e-06, 1e-10]`m^2（默认） | 1-by-*n* vector

用于开度面积表格参数化的开度面积值向量。向量元素必须与 **Pressure differential vector for reducing valve** 参数中的值一一对应。面积按降序列出。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Tabulated`。

### **Pressure differential vector for relief valve** — 泄压阀表格参数化的压差值 `0.68 : 0.02 : 0.78` MPa（默认） | 1-by-*n* vector

用于开度面积表格参数化的压差值向量。向量元素与 **Opening area vector relief valve** 参数中的值一一对应。压差向量值按升序列出，并且其元素数量必须与 **Opening area vector relief valve** 参数相同。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Tabulated`。

### **Opening area vector for relief valve** — 泄压阀表格参数化的阀门开度面积 `[1e-10, 2e-06, 4e-06, 6e-06, 8e-06, 1e-05]`m^2（默认） | 1-by-*n* vector

用于开度面积表格参数化的开度面积值向量。向量元素必须与 **Pressure differential vector for relief valve** 参数中的值一一对应。面积按升序列出。在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Tabulated`。

### **Cross-sectional area at ports A, P & T.** — 守恒端口处的孔口面积 `inf` m^2（默认） | positive scalar

入口和出口端口 **A**、**P** 和 **T** 处的横截面积。此面积用于压力-流量方程，以确定通过孔口的质量流量。

### **Discharge coefficient** — 流量系数 `0.64`（默认） | positive scalar

用于考虑理论流动中排放损失的修正因子。Simscape™ Fluids™ 中阀门的默认流量系数为 0.64。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认） | positive scalar

通过阀门的层流的上限雷诺数。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认） | positive scalar in the range of [0,1]

连续平滑因子，当阀门处于接近打开或接近关闭位置时，为流量响应引入一层渐变变化。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear`。

### **Pressure recovery** — 是否考虑面积扩张中的压力升高 `off`（默认） | `on`

考虑流体从较小横截面积区域流向较大横截面积区域时的压力升高。清除 **Pressure recovery** 复选框时，不会捕获此压力升高。

### **Opening dynamics** — 是否引入由孔口开启引起的流量滞后 `off`（默认） | `on`

考虑阀门开启对流体系统的瞬态效应。选择 **Opening dynamics** 会通过在流量响应中引入一阶滞后来近似开启条件。**Opening time constant** 也会影响建模的开启动态。

### **Reducing valve initial opening area** — 仿真开始时端口 P 处的开启面积 `1e-4` m^2（默认） | positive scalar

动态开启时端口 **P** 处的初始横截面积。此值用于计算下一时间步 **P** 和 **A** 之间动态开启的瞬时开度面积。

#### 依赖关系

要启用此参数，请选择 **Opening dynamics**。

### **Relief valve initial opening area** — 仿真开始时端口 T 处的开启面积 `1e-10` m^2（默认） | positive scalar

动态开启时端口 **T** 处的初始开度横截面积。此值用于计算下一时间步 **A** 和 **T** 之间动态开启的瞬时开度面积。

#### 依赖关系

要启用此参数，请选择 **Opening dynamics**。

### **Opening time constant** — 阀门开启时间常数 `0.1` s（默认） | positive scalar

表示阀门从一个位置开启或关闭到另一位置时，流体达到稳态所需时间的常数。此参数会影响建模的开启动态。

#### 依赖关系

要启用此参数，请选择 **Opening dynamics**。

### 故障

### **Pressure-Reducing 3-Way Valve Area fault** — 用于对阀面积故障建模的选项 `Add fault`

用于在模块中对阀面积故障建模的选项。要添加故障，请点击 **Add fault** 超链接。发生故障时，通常由开度参数化设置的阀面积将根据 **Opening area when faulted** 参数中指定的值进行设置。

### **Valve areas when faulted** — 故障时的阀门特性 `Reducing valve closed and relief valve open`（默认） | `Reducing valve open and relief valve closed` | `Maintain last value`

故障阀门类型。您可以选择阀门在打开、关闭或触发故障时的面积处卡住。

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

Pressure-Reducing 3-Way Valve (IL) 是泄压阀和减压阀的组合。它通过限制端口 **P** 的流入面积并将流量从端口 **T** 排出，来保持阀门出口（端口 **A**）处的压力。

### 阀门功能

该模块通过将端口 **A** 和端口 **T** 之间的压差与一组压力阈值范围进行比较来控制阀门操作。当 **A** 和 **T** 之间的压差 *Pcontrol* 超过 *Pset,reducing* 时，端口 **P** 开始关闭。当 *Pcontrol* 介于 *Pset,reducing*+*Preg* 与 *Pset,reducing*+*Preg*+*Ptransition* 之间时，模块处于过渡范围，且端口 **P** 和 **T** 处的两个阀均关闭。当 *Pcontrol* 超过压力过渡范围 *Pset,relief* 时，其中 Pset,relief=Pset,reducing+Preg+Ptransition，端口 **T** 开始打开。

要模拟相对于另一系统元件的泄压或减压，请参阅 Pressure Compensator Valve (IL)。要模拟阀门出口与大气之间的减压，请参阅 Pressure-Reducing Valve (IL)。要模拟相对于阀门的泄压，或阀门出口与大气压力之间的泄压，请参阅 Pressure Relief Valve (IL)。

### 压力控制

当 *Pcontrol*（即 *PA* – *PT*）超过阈值压力 *Pset,reducing* 时，端口 **P** 处的阀开始关闭。当压力超过过渡范围，或当 *Pcontrol* > *Pset,relief* 时，端口 **T** 处的阀开始打开。阀门关闭和打开均以两种方式参数化：

- 当 **Set pressure control** 为 `Controlled` 时，模块使用端口 **Ps** 处的压力信号控制阀门。在此设置下，*Preg* 是 **Pressure regulation range** 参数的值，*Ptransition* 是 **Pressure transition range** 参数的值。当 *Pcontrol* 大于 *Pset,reducing*（即端口 **Ps** 处信号的值）时，减压阀开始关闭。当 *Pcontrol* 大于 *Pset,relief* 且低于 *Pmax,relief* 时，触发泄压阀响应，即端口 **T** 开始打开。*Pmax,relief* 是 **Pressure regulation range** 参数的值与 *Pset,relief* 之和。
- 当 **Set Pressure control** 为 `Constant` 时，端口 **P** 处的阀门关闭由线性或表格参数化连续调节。类似地，端口 **T** 处的泄压阀打开通过线性或查表参数化。下面显示了减压阀（实线）和泄压阀（虚线）的线性参数化示例。

  如果将 **Opening parameterization** 设置为 `Linear`，则 *Pset,reducing* 是 **Set pressure differential for reducing valve** 参数的值，*Preg* 是 **Pressure regulation range** 参数的值，*Ptransition* 是 **Pressure transition range** 参数的值。*Pmax,relief* 是 **Pressure regulation range** 参数的值与 *Pset,relief* 之和。

  如果将 **Opening parameterization** 设置为 `Tabulated`，则 *Pset,reducing* 和 *Pmax,reducing* 分别是 **Pressure differential vector for reducing valve** 的第一个和最后一个参数，*Pset,relief* 和 *Pmax,relief* 分别是 **Pressure differential vector for relief valve** 的第一个和最后一个参数。下面显示了减压阀和泄压阀两者的表格参数化示例。

### 质量流量方程

通过阀门的动量守恒：

m˙A+m˙reducing+m˙relief=0.

通过阀门的质量流量计算如下：

m˙reducing=CdAPA2ρ¯PRloss,reducing(1−(APAAport)2)Δpreducing[Δpreducing2+Δpcrit,reducing2]1/4,

m˙relief=CdAAT2ρ¯PRloss,relief(1−(AATAport)2)Δprelief[Δprelief2+Δpcrit,relief2]1/4,

其中：

- *Cd* 是 **Discharge coefficient** 参数的值。
- *A* 是端口 **A** 和 **P** 或 **A** 和 **T** 之间的瞬时阀门开启面积，如下标所示。
- *A*port 是 **Cross-sectional area at ports A, P & T** 参数的值。
- ρ¯ 是平均流体密度。
- *Δp* 是阀门压差，*pA* – *pB*。

临界压差 *Δpcrit* 是与 **Critical Reynolds number**、*Recrit* 相关的压差，即层流和湍流之间的流态转变点，它对应于阀门的减压或溢流组件，

Δpcrit=πρ¯8A(νRecritCd)2,

其中 *A* 是 *APA* 或 *AAT*，分别对应于阀门的减压或溢流组件。

*压力损失* 描述由于面积减小导致的阀门压力降低。*PRloss* 为

PRloss=1−(AAport)2(1−Cd2)−CdAAport1−(AAport)2(1−Cd2)+CdAAport.

*压力恢复* 描述由于面积增加导致的阀门正压力变化。如果不希望捕获该压力增加，请清除 **Pressure recovery** 复选框。在这种情况下，*PRloss* 为 1。

当 **Set Pressure control** 为 `Constant` 时，该模块使用减压阀（**P** 到 **A**）或溢流阀（**A** 到 **T**）的开启参数化以及阀门开启动态来计算开启面积 *A*。

### 开启和关闭参数化

当将 **Opening parameterization** 设置为 `Linear` 时，减压阀的阀门面积为

Avalve=p^reducing(Aleak−Amax)+Amax,

而溢流阀的阀门面积为

Avalve=p^relief(Amax−Aleak)+Aleak.

归一化压力 p^ 为

p^=pcontrol−psetpmax−pset,

其中设定压力和最大压力分别是相应的减压阀或溢流阀设置。

在线性参数化中，当阀门处于接近开启或接近关闭位置时，可以通过调整 **Smoothing factor** 参数来保持仿真中的数值稳健性。如果 **Smoothing factor** 参数非零，该模块会在 *pset* 和 *pmax* 之间平滑地饱和控制压力。有关详细信息，请参阅数值平滑。

当将 **Opening parameterization** 设置为 `Tabulated` 时，*A*leak,PA 和 *A*max,PA 分别是 **Opening area vector reducing valve** 参数的第一个和最后一个元素，而 *A*leak,AT 和 *A*max,AT 分别是 **Opening area vector for relief valve** 参数的第一个和最后一个元素。该模块按如下方式计算开启面积：

Avalve=tablelookup(pcontrol,TLU,ref,ATLU,pcontrol,interpolation=linear,extrapolation=nearest).

对于减压阀，该模块使用表查找方法计算开启面积，其中：

- *pcontrol* 是控制压力，即端口 **A** 和 **T** 之间的压差。
- *pcontrol,TLU,ref* = *pTLU* + *poffset*。
- *pTLU* 是 **Pressure differential vector for reducing valve** 参数
- *poffset* 是一个内部压力偏移，当 *pcontrol,TLU,ref* = *pset,reducing* 时使阀门开始关闭。
- *ATLU* 是 **Opening area vector reducing valve** 参数。

对于溢流阀，该模块使用表查找方法计算开启面积，其中：

- *pcontrol* 是端口 **A** 和 **T** 之间的压差。
- *pcontrol,TLU,ref* = *pTLU* + *poffset*。
- *pTLU* 是 **Pressure differential vector for relief valve** 参数。
- *poffset* 是一个内部压力偏移，当 *pcontrol,TLU,ref* = *pset,releif* 时使阀门开始开启。
- *ATLU* 是 **Opening area vector for relief valve** 参数。

### 开启动态

如果对 **Opening dynamics** 进行建模，则会在流量对阀门开启的响应中引入滞后。*A*valve 变为动态开启或关闭面积 *A*dyn；否则，*A*valve 是稳态开启面积。该面积特定于阀门的减压和溢流组件，分别为 *A*PA 或 *A*AT。动态开启面积的瞬时变化基于 **Opening time constant**、*τ* 计算：

p˙dyn=pcontrol−pdynτ.

默认情况下，不对 **Opening dynamics** 进行建模。

### 故障

要对故障进行建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault** 超链接。使用故障参数指定故障属性。有关故障建模的详细信息，请参阅 Simscape 故障简介。

**Valve areas when faulted** 参数有三个故障选项：

- `Reducing valve closed and relief valve open`
  — 减压阀冻结在其最小值，溢流阀冻结在其最大值，具体取决于 **Opening parameterization**：

  - 当 **Opening parameterization** 设置为 `Linear` 时，减压阀面积冻结在 **Leakage area** 参数的值，溢流阀面积冻结在 **Maximum opening area** 参数的值。
  - 当 **Opening parameterization** 设置为 `Tabulated` 时，减压阀面积冻结在 **Opening area vector** 参数的第一个元素的值，溢流阀面积冻结在 **Opening area vector** 参数的最后一个元素的值。
- `Reducing valve open and relief valve closed`
  — 减压阀冻结在其最大值，溢流阀冻结在其最小值，具体取决于 **Opening parameterization**：

  - 当 **Opening parameterization** 设置为 `Linear` 时，减压阀面积冻结在 **Maximum opening area** 参数的值，溢流阀冻结在 **Leakage area** 参数的值。
  - 当 **Orifice parameterization** 设置为 `Tabulated` 时，减压阀面积冻结在 **Opening area vector** 参数的最后一个元素的值，溢流阀面积冻结在 **Opening area vector** 参数的第一个元素的值。
- `Maintain last value` — 减压阀和溢流阀面积冻结在触发发生时的开启面积。

由于阀门面积极值处的数值平滑，该模块使用的最小面积大于 **Leakage area** 参数的值，而最大面积小于 **Maximum orifice area** 参数的值，与 **Smoothing factor** 值成比例。

故障触发后，阀门在仿真的剩余时间内保持在故障面积。

### 假设和限制

忽略阀门与流体之间的摩擦、流体对阀门部件的液压力以及流体惯性效应。
