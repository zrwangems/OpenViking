---
type: simulink-block
title: 'Pressure Reducing Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Valves & Orifices / Pressure Control Valves'
documentation_page: 'pressurereducingvalvetl'
documentation_source_path: 'ref/pressurereducingvalvetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure Reducing Valve (TL)

## 端口

### 输入

### **Ps** — 设定压力信号，Pa physical signal

受控阀门操作的压力阈值，单位为 Pa。

#### 依赖关系

要启用此端口，请将 **Set pressure control** 设置为 `Controlled`。

### 守恒

### **A** — 液体端口 thermal liquid

与阀门入口 A 关联的 thermal liquid 守恒端口。

### **B** — 液体端口 thermal liquid

与阀门入口 B 关联的 thermal liquid 守恒端口。

## 参数

### 参数

### **Opening parameterization** — 开度参数化 `Linear - Area vs. pressure`（默认） | `Tabulated data - Area vs. pressure` | `Tabulated data - Volumetric flow rate vs. pressure`

阀门开度的建模方法。当您将此参数设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure` 时，模块将开度面积与控制压力关联。当您将此参数设置为 `Tabulated data - Volumetric flow rate vs. pressure` 时，模块采用减压阀的参考流量与压差曲线。

### **Set pressure control** — 阀门操作方式 `Constant`（默认） | `Controlled`

阀门操作方式。当您将此参数设置为 `Constant` 时，阀门在固定压力调节范围内线性关闭，或根据您提供的表列压力和开度面积数据关闭。当您将此参数设置为 `Controlled` 时，阀门根据端口 **Ps** 处的可变设定压力信号在固定压力调节范围内关闭。

### **Set pressure (gauge)** — 阀门开始关闭时的表压 `0.1` `MPa`（默认） | positive scalar

阀门开始关闭时的压力。在阀门的整个压力调节范围内，开度面积保持可变。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`。

### **Pressure regulation range** — 阀门压力范围 `0.01` `MPa`（默认） | positive scalar

阀门开度面积变化的压力区间。该区间从 **Set pressure (gauge)** 参数的值开始。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Maximum opening area** — 全开位置的开度面积 `1e-4` `m^2`（默认） | positive scalar

当阀门处于压力调节范围下限时，由于密封不完善，阀门在全开位置的开度面积。模块使用此参数在整个压力调节范围内缩放阀门开度。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Leakage area** — 完全关闭位置时的间隙面积 `1e-10` `m^2`（默认） | positive scalar

阀门处于完全关闭位置时所有间隙的总和。模块将更小的数值饱和为此值。此参数通过保持流量连续性来帮助提高数值稳定性。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Pressure at port B (gauge) vector** — 用于表列面积参数化的表压值向量 `[0.2 : 0.2 : 1.2]` `MPa`（默认） | 1-by-*n* vector

用于阀门开度面积表列面积参数化的表压值向量。向量元素必须与 **Opening area vector** 参数中的元素一一对应。这些元素必须为正且按升序排列。模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated data - Area vs. pressure`。

### **Opening area vector** — 用于表列面积参数化的阀门开度面积 `[1e-05, 8e-06, 6e-06, 4e-06, 2e-06, 1e-10]` `m^2`（默认） | 1-by-*n* vector

用于阀门开度面积表列面积参数化的阀门开度面积向量。向量元素必须与 **Pressure at Port B (gauge) vector** 参数中的元素一一对应。这些元素必须为正且按升序排列。模块在数据点之间使用线性插值。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated data - Area vs. pressure`。

### **Reference pressure at port A (gauge)** — 端口 A 处的参考压力 `1.5` `MPa`（默认） | positive scalar

端口 **A** 处的恒定压力，构成参考曲线的基础。此值通常对应于阀门的最大工作压力。在仿真期间，端口 **A** 处的压力可以是任意值。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### **Reference pressure at port B (gauge) vector** — 端口 B 处的参考压力 `[1.2, 1, .8, .6, .4, .2]` `MPa`（默认） | 1-by-*n* vector

参考曲线中端口 **B** 处的单调递减压力值向量，随阀门开度面积变化。第一个元素是参考最大压力，即阀门完全关闭时的压力。最后一个元素是参考设定压力。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### **Reference volumetric flow rate vector** — 参考体积流量 `[1e-09, 1.8e-05, 6.6e-05, .00013, .0002, .00028]` `m^3/s`（默认） | 1-by-*n* vector

通过阀门的单调递增参考流量向量。模块使用此曲线为变化的阀门面积生成流量系数。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### **Cross-sectional area at ports A and B** — 守恒端口处的面积 `0.01` `m^2`（默认） | positive scalar

端口 **A** 和 **B** 处的面积，模块在确定通过阀门的质量流量的压力-流量方程中使用该面积。

### **Discharge coefficient** — 流量系数 `0.64`（默认） | positive scalar

修正因子，模块用它来考虑理论流量中的排放损失。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认） | positive scalar

通过阀门的层流的上限雷诺数。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认） | positive scalar，范围 [0,1]

连续平滑因子，在阀门接近打开或接近关闭位置时，为流量响应引入一层渐变。将此值设置为小于 1 的非零值，可提高这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Pressure recovery** — 在面积扩张期间包含压力增加的选项 `off`（默认） | `on`

是否捕获当流体从较小横截面积区域流向较大横截面积区域时的压力增加。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **Opening dynamics** — 包含对阀门打开的流量响应的选项 `off`（默认） | `on`

是否近似阀门打开对流体系统的瞬态影响。选择 **Opening dynamics** 会通过在流量响应中引入一阶滞后来近似打开条件。

### **Opening time constant** — 阀门打开时间常数 `0.1` `s`（默认） | positive scalar

用于计算开度动态中滞后的时间常数。

#### 依赖关系

要启用此参数，请选择 **Opening dynamics**。

### 止回阀

### **Enable check valve** — 止回阀选项 `off`（默认） | `on`

模块是否模拟内部止回阀。

### **Cracking pressure differential** — 止回阀操作的设定压力 `0.1` `MPa`（默认） | positive scalar

使止回阀开启的压差。

#### 依赖关系

要启用此参数，请选择 **Enable check valve**，并将 **Valve parameterization** 设置为 `Linear - Area vs. pressure`。

### **Maximum opening pressure differential** — 阀门中的最大压力 `0.2` `MPa`（默认） | positive scalar

止回阀完全关闭时的压差。

#### 依赖关系

要启用此参数，请选择 **Enable check valve**，并将 **Valve parameterization** 设置为 `Linear - Area vs. pressure`。

### **Maximum opening area** — 最大打开面积 `1e-4` `m^2`（默认） | positive scalar

负载管路中止回阀的最大打开面积。在内部，止回阀与减压级并联。

#### 依赖关系

要启用此参数，请选择 **Enable check valve**，并将 **Valve parameterization** 设置为 `Linear - Area vs. pressure`。

### **Pressure differential vector** — 止回阀操作的压差 `[0.01 : 0.01 : 1]` `MPa`（默认） | 1-by-*n* vector

止回阀级的压差向量。模块将止回阀压差计算为端口 **B** 处压力相对于端口 **A** 处压力。

#### 依赖关系

要启用此参数，请选择 **Enable check valve**，并将 **Valve parameterization** 设置为 `Tabulated data - Area vs. pressure` 或 `Tabulated data - Volumetric flow rate vs. pressure`。

### **Opening area vector** — 止回阀级开度面积 `[1e-10, 1e-05, 2e-05, 3e-05, 4e-05, 5e-05, 6e-05, 7.5e-05, 8.5e-05, .0001]` `m^2`（默认） | 1-by-*n* vector

止回阀级的开度面积向量。向量元素必须与 **Pressure differential vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请选择 **Enable check valve**，并将 **Valve parameterization** 设置为 `Tabulated data - Area vs. pressure`。

### **Volumetric flow rate vector** — 止回阀级体积流量 `[.000358, .045, .11, .191, .284, .39, .505, .63, .764, .905] .* 1e-3` `m^3/s`（默认） | 1-by-*n* vector

止回阀级的体积流量向量。此向量的元素必须与 **Pressure differential vector** 参数中的元素对应。

#### 依赖关系

要启用此参数，请选择 **Enable check valve**，并将 **Valve parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### 故障

### **Pressure-Reducing Valve Area fault** — 用于对减压阀故障建模的选项 `Add fault`

用于启用减压阀故障参数的选项。要添加故障，请单击 **Add fault** 超链接。发生故障时，模块将开度面积设置为 **Reducing valve opening when faulted** 参数指定的位置。

### **Reducing valve opening when faulted** — 减压阀故障位置 `Closed`（默认） | `Open` | `Maintain last value`

故障时的减压阀位置。您可以选择阀门在打开、关闭或保持原位时发生故障。

#### 依赖关系

要启用此参数，请通过单击 **Pressure-Reducing Valve Area fault** 参数的 **Add fault** 超链接来为模块启用故障。

### **Check Valve Area fault** — 用于对止回阀故障建模的选项 `Add fault`

用于启用止回阀故障参数的选项。要添加故障，请单击 **Add fault** 超链接。发生故障时，模块将开度面积设置为 **Check valve opening when faulted** 参数指定的位置。

#### 依赖关系

要启用此参数，请选择 **Enable check valve**。

### **Check valve opening when faulted** — 故障阀门特性 `Closed`（默认） | `Open` | `Maintain last value`

故障时的止回阀位置。您可以选择阀门在打开、关闭或保持原位时发生故障。

#### 依赖关系

要启用此参数，请选择 **Enable check valve**，并通过单击 **Check Valve Area fault** 参数的 **Add fault** 超链接来为模块启用故障。

## 所属库

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Pressure Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2024b：使用 Simscape 故障界面对故障建模

Pressure Reducing Valve (TL) 模块现在支持 Simscape 故障界面。要了解更多信息，请参阅 Introduction to Simscape Faults。

### R2024b：新的阀门控制选项

将 **Set pressure control** 设置为 `Controlled`，以使用端口 **Ps** 处的信号控制模块设定压力。选择 **Enable check valve** 以对在流动反向期间功能与 Check Valve (TL) 模块相同的止回阀建模。

### R2023a：新的参数化选项

使用 **Opening parameterization** 参数选择模块参数化：`Linear - Area vs. pressure`、`Tabulated data - Area vs. pressure` 或 `Tabulated data - Volumetric flow rate vs. pressure`。

## 描述

热液体网络中的减压阀

Pressure Reducing Valve (TL) 模块表示一个在热液体网络中降低下游压力的阀门。当端口 **B** 处的压力小于指定压力时，阀门保持打开。当端口 **B** 处的压力达到或超过该压力时，阀门关闭。模块基于设定压力与端口 **B** 处压力之间的差值运行。模块包含一个止回阀部分，在流动反向期间其功能与 Check Valve (TL) 模块相同。

### 压力控制

模块在设定压力与最大压力之间调节压力。当您将 **Set pressure control** 设置为：

- `Controlled` — 您可以将压力信号连接到端口 **Ps**。当端口 **B** 处的压力大于参考设定压力 *Pset* 且低于 *Pmax* 时，模块调节压力。端口 **B** 处的压力充当此阀门的控制压力 *Pcontrol*。

  *Pmax* 是 *Pset* 与压力调节范围之和。
- `Constant` — **Set pressure (gauge)** 参数定义恒定设定压力。

当 **Opening parameterization** 为 `Linear - Area vs. pressure` 时，归一化压力 p^ 控制阀门开度面积。归一化压力为

p^=pcontrol-psetpmax-pset,

其中：

- *pcontrol* 是控制压力，*pB ̶ pAtm*，其中 *pAtm* 是大气压力。
- *pset* 是阀门设定压力

  pset=pset,gauge+pAtm,

  其中 *Pset,gauge* 是 **Set pressure (gauge)** 参数的值。
- *pmax* 是最大压力，*pmax = pset + prange*，其中 *prange* 是 **Pressure regulation range** 参数的值。

### 开度参数化

质量流量取决于 **Opening parameterization** 参数的值。

**面积-压力参数化**

当您将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure` 时，质量流量为

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4,

其中：

- *Cd* 是 **Discharge coefficient** 参数的值。
- *Avalve* 是瞬时阀门开启面积。
- *Aport* 是 **Cross-sectional area at ports A and B** 参数的值。
- ρ¯ 是平均流体密度。
- *Δp* 是阀门压差 *pA* – *pB*。

临界压差 *Δpcrit* 是与 **Critical Reynolds number** *Recrit* 相关的压差，即层流和湍流之间的流态转变点：

Δpcrit=π8Avalveρ¯(μRecritCd)2,

其中 *μ* 是热液体的动力粘度。

压力损失 *PRloss* 描述了由于面积减小而导致的阀门压力降低。该模块计算 *PRloss* 如下：

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport.

压力恢复描述了由于面积增加而导致的阀门正压力变化。当您清除 **Pressure recovery** 复选框时，模块将 *PRloss* 设置为 1。

当您将 **Opening parameterization** 参数设置为 `Linear - Area vs. pressure` 时，模块计算开启面积如下：

Avalve=p^(Aleak−Amax)+Amax,

其中 *Aleak* 是 **Leakage Area** 参数的值，*Amax* 是 **Maximum opening area** 参数的值。

此图显示了模块如何使用线性参数化控制开启面积。

使用线性参数化时，常开阀的端口 X 和 Y 之间的压差与开启面积的关系

当阀门在线性参数化中处于接近打开或接近关闭位置时，您可以通过调整 **Smoothing factor** 参数来保持仿真中的数值鲁棒性。如果 **Smoothing factor** 参数非零，模块将在 *pset* 和 *pmax* 之间平滑地饱和控制压力。有关详细信息，请参阅 Numerical Smoothing。

当您将 **Opening parameterization** 设置为 `Tabulated data - Area vs. pressure` 时，模块计算开启面积如下：

Avalve=tablelookup(pcontrol,TLU,ref,ATLU,pcontrol,interpolation=linear,extrapolation=nearest),

其中：

- *pcontrol,TLU,ref* = *pTLU* + *poffset*。
- *pTLU* 是 **Pressure differential vector** 参数。
- *poffset* 是一个内部压力偏移，当 *pcontrol,TLU,ref* = *pset* 时，使阀门开始关闭。
- *ATLU* 是 **Opening area vector** 参数。

此图显示了当 **Opening parameterization** 为 `Tabulated data - Area vs. pressure` 时，模块如何控制开启面积。

使用表格参数化时，常开阀的端口 X 和 Y 之间的压差与开启面积的关系

**体积流量-压力参数化**

当您将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure` 时，阀门根据用户提供的端口 **A** 和 **B** 之间的体积流量和压差的表格数据打开。

模块计算质量流量如下：

m˙=ρ¯V˙,

其中：

- V˙ 是体积流量。
- ρ¯ 是平均流体密度。

模块使用以下公式计算质量流量与压力之间的关系：

m˙=Kρ¯Δp,

其中

K=V˙|Δp|.

### 开度动态

当您选择 **Opening dynamics** 时，模块引入控制压力滞后，其中 *pcontrol* 变为动态控制压力 *pdyn*。动态开启面积的瞬时变化基于 **Opening time constant** 参数 *τ* 计算：

p˙dyn=pcontrol−pdynτ.

默认情况下，模块清除 **Opening dynamics** 复选框。

### 能量平衡

阀门中的能量守恒方程为

ϕA+ϕB=0,

其中：

- *ϕA* 是通过端口 **A** 进入阀门的能量流率。
- *ϕB* 是通过端口 **B** 进入阀门的能量流率。

### 故障

要对故障建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault** 超链接。使用故障参数指定故障属性。有关故障建模的详细信息，请参阅 Introduction to Simscape Faults。

对于减压阀和单向阀，有三种故障选项可用。对于 **Reducing valve opening when faulted** 和 **Check valve opening when faulted** 参数，您可以选择：

- `Closed` — 阀门关闭到其最小开启值，具体取决于 **Opening parameterization** 参数。当您将 **Opening parameterization** 设置为：
  - `Linear - Area vs. pressure` — 阀门面积减小到 **Leakage area** 参数的值。
  - `Tabulated data - Area vs. pressure` — 阀门面积减小到 **Opening area vector** 参数中最后一个元素的值。
  - `Tabulated data - Volumetric flow rate vs. pressure` — 流量系数减小到派生流量系数查找表 *KTLU,Ref* 中最后一个元素的值。
- `Open` — 阀门打开到其最大开启值，具体取决于 **Opening parameterization** 参数。当您将 **Opening parameterization** 设置为：
  - `Linear - Area vs. pressure` — 阀门面积打开到 **Maximum opening area** 的值。
  - `Tabulated data - Area vs. pressure` — 阀门面积打开到 **Opening area vector** 中第一个元素的值。
  - `Tabulated data - Volumetric flow rate vs. pressure` — 流量系数减小到派生流量系数查找表 *KTLU,Ref* 中第一个元素的值。
- `Maintain last value` — 阀门面积保持在触发发生时的阀门开启面积。

对于线性参数化，阀门面积极值处的数值平滑会导致应用的最小面积大于 **Leakage area** 参数，最大面积小于 **Maximum orifice area** 参数。

故障触发后，阀门在仿真的剩余时间内保持在故障面积。

### 预定义参数化

您可以使用预参数化的制造数据填充模块，这允许您对特定供应商组件进行建模。

要加载预定义参数化：

1. 在模块对话框中，在 **Selected part** 旁边，单击模块对话框设置中 **Selected part** 旁边的 "<click to select>" 超链接。
2. 将打开 Block Parameterization Manager 窗口。从菜单中选择一个部件，然后单击 **Apply all**。您可以使用 **Manufacturer** 下拉菜单缩小选择范围。
3. 您可以关闭 **Block Parameterization Manager** 菜单。模块现在具有您指定的参数化。
4. 您可以通过选择部件并在 **Compare selected part with block** 部分中查看数据，将当前参数设置与特定供应商组件在 Block Parameterization Manager 窗口中进行比较。

**注意**

预定义模块参数化使用可用的数据源来提供参数值。模块对缺失数据采用工程判断和简化假设。因此，预计仿真与实际物理行为之间会有一些偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化组件模型。

要了解更多信息，请参阅 List of Pre-Parameterized Components。
