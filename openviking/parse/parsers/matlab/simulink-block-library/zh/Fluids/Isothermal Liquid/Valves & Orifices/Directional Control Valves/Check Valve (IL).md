---
type: simulink-block
title: 'Check Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: 'checkvalveil'
documentation_source_path: 'ref/checkvalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# Check Valve (IL)

## 端口

### 守恒端口

### **A** — 液体端口 等温液体

阀的入口点。

### **B** — 液体端口 等温液体

阀的出口点。

## 参数

### 参数

### **Opening parameterization** — 计算阀开度的方法 `Linear - Area vs. pressure`（默认）| `Tabulated data - Area vs. pressure` | `Tabulated data - Volumetric flow rate vs. pressure`

计算阀开度的方法。

- `Linear - Area vs. pressure`：阀开度面积与阀压力成线性对应关系。
- `Tabulated data - Area vs. pressure`：阀质量流量由面积值相对于压差的表格确定。
- `Tabulated data - Volumetric flow rate vs. pressure`：阀质量流量由体积流量值相对于压差的表格确定。

### **Opening pressure specification** — 用于阀控制的压差 `Pressure differential`（默认）| `Pressure at port A`

指定控制压差。`Pressure differential` 选项指端口 **A** 和 **B** 之间的压力差。`Pressure at port A` 选项指端口 **A** 与大气压之间的压力差。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Cracking pressure differential** — 阈值压力 `0.01 MPa`（默认）| 正标量

触发阀操作的阈值压力。当控制压力为端口 **A** 和 **B** 之间的压差时，此为设定压力。

#### 依赖关系

要启用此参数，请将 **Opening pressure specification** 设置为 `Pressure differential`，并将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Cracking pressure (gauge)** — 阈值压力 `0.1 MPa`（默认）| 正标量

当控制压力为端口 **A** 与大气压之间的压差时，触发阀操作的表压阈值。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`，并将 **Opening pressure specification** 设置为 `Pressure at port A`。

### **Maximum opening pressure differential** — 阀压差最大值 `0.1 MPa`（默认）| 正标量

最大阀压差。此参数为压力提供上限，以使系统压力保持在实际范围内。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`，并将 **Opening pressure specification** 设置为 `Pressure differential`。

### **Maximum opening pressure (gauge)** — 阀压力最大值 `0.2 MPa`（默认）| 正标量

最大阀表压。此参数为压力提供上限，以使系统压力保持在实际范围内。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`，并将 **Opening pressure specification** 设置为 `Pressure at port A`。

### **Maximum opening area** — 阀完全打开时的面积 `1e-4 m^2`（默认）| 正标量

阀在完全打开位置时的横截面积。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Leakage area** — 完全关闭位置时的阀间隙面积 `1e-12 m^2`（默认）| 正标量

阀处于完全关闭位置时所有间隙的总和。任何小于此值的面积都会被饱和到指定的泄漏面积。这通过保持流动的连续性来帮助数值稳定性。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Pressure differential vector** — 表格参数化的压差值 `[0.01 : 0.01 : 0.1] MPa`（默认）| 1×*n* 向量

用于阀开度面积表格参数化的压差值向量。向量元素必须与 **Opening area vector** 参数中的元素一一对应。元素按升序列出，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请设置：

- **Set pressure control** 为 `Constant`。
- **Opening parameterization** 为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。
- **Opening pressure specification** 为 `Pressure differential`。

### **Opening area vector** — 表格参数化的阀开度面积 `[1e-10, 1e-05, 2e-05, 3e-05, 4e-05, 5e-05, 6e-05, 7.5e-05, 8.5e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀开度面积表格参数化的阀开度面积向量。向量元素必须与 **Pressure differential vector** 参数中的元素一一对应。元素按升序列出，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Tabulated data - Area vs. pressure`。

### **Cross-sectional area at ports A and B** — 阀入口或出口处的面积 `inf m^2`（默认）| 正标量

入口和出口端口 **A** 和 **B** 处的横截面积。这些面积用于确定通过阀的质量流量的压力-流量方程。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

用于修正理论流动中排放损失的修正因子。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过阀的层流的上限雷诺数。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 正标量

连续平滑因子，当阀处于接近打开或接近关闭位置时，为流动响应引入一层渐变。将此值设置为小于 1 的非零值，以提高在这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Pressure recovery** — 是否考虑面积扩大时的压力增加 `off`（默认）| `on`

是否考虑流体从较小横截面积区域流向较大横截面积区域时的压力增加。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Opening dynamics** — 是否考虑阀打开时的流动响应 `off`（默认）| `on`

是否考虑因打开阀而对流体系统产生的瞬态效应。选择 **Opening dynamics** 通过在流动响应中引入一阶滞后来近似打开条件。**Opening time constant** 也会影响建模的打开动态特性。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Opening time constant** — 阀打开时间常数 `0.1 s`（默认）| 正标量

当阀从一个位置打开或关闭到另一个位置时，流体达到稳态所需时间的常数。此参数影响建模的打开动态特性。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`，并选择 **Opening dynamics**。

### **Volumetric flow rate vector** — 表格数据参数化的体积流量向量 `[.000358, .045, .11, .191, .284, .39, .505, .63, .764, .905] .* 1e-3 m^3/s`（默认）| 1×*n* 向量

用于阀开度表格参数化的体积流量值向量。此向量必须与 **Pressure drop vector** 参数具有相同数量的元素。向量元素必须按升序列出。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### 故障

### **Check Valve Area fault** — 建模阀面积故障的选项 `Add fault`

用于在模块中建模阀面积故障的选项。要添加故障，请单击 **Add fault** 超链接。发生故障时，通常由打开参数化设置的阀面积将根据 **Opening area when faulted** 参数中指定的值进行设置。

### **Opening area when faulted** — 故障时的阀特性 `Closed`（默认）| `Open` | `Maintain at last value`

故障时的阀面积。您可以选择阀在完全关闭或完全打开位置卡住，或在触发故障时的条件下卡住。当 **Opening parameterization** 为 `Linear - Area vs. pressure` 时，此参数设置面积；当 **Opening parameterization** 为 `Tabulated data` 时，此参数设置质量流量。

#### 依赖关系

要启用此参数，请单击 **Add fault** 超链接。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2025a：生成数字数据表

通过使用模块对话框 **Description** 选项卡中的 **Generate datasheet** 超链接，生成包含性能数据和压降与体积流量曲线的数字数据表。该超链接会打开一个脚本，该脚本从您在模型中选择的 Check Valve (IL) 模块导入参数。您可以使用特性曲线来评估开启压力和泄漏流量。

### R2024a：使用 Simscape 故障接口建模故障

Check Valve (IL) 模块现在支持 Simscape™ 故障接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

## 描述

等温液体系统中的单向阀

Check Valve (IL) 模块表示一个单向阀，其从端口 **A** 到端口 **B** 为自由流动，从端口 **B** 到端口 **A** 为受限流动。当端口 **A** 处的压力或压差达到或超过设定压力阈值时，阀开始打开。

### 打开参数化

当 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 时，阀打开面积与开启压差成线性关系。

**开启压力**

阀控制有两种选项：

- 当 **Opening pressure differential** 设置为 `Pressure differential` 时，控制压力为端口 **A** 和 **B** 之间的压差。当 *P*control 达到或超过 **Cracking pressure differential** 时，阀开始打开。
- 当 **Opening pressure differential** 设置为 `Pressure at port A` 时，控制压力为端口 **A** 与大气压之间的压力差。当 *P*control 达到或超过 **Cracking pressure (gauge)** 时，阀开始打开。

**打开面积与压力**

阀面积的线性参数化为

Avalve=p^(Amax−Aleak)+Aleak，

其中归一化压力 p^ 为

p^=pcontrol−pcrackingpmax−pcracking。

当阀在线性参数化中处于接近打开或接近关闭位置时，您可以通过调整 **Smoothing factor** 参数来保持仿真的数值鲁棒性。如果 **Smoothing factor** 参数非零，模块将在 *pcracking* 和 *pmax* 之间平滑地饱和控制压力。有关更多信息，请参阅 Numerical Smoothing。

当您将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure` 时，*Avalve* 是 **Opening area vector** 参数与 **Pressure differential vector** 参数曲线在仿真压差下的线性插值。

**质量流量方程**

通过阀的质量守恒：

m˙A+m˙B=0。

通过阀的质量流量计算为：

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4，

其中：

- *C*d 是 **Discharge coefficient**。
- *A*valve 是瞬时阀打开面积。
- *A*port 是 **Cross-sectional area at ports A and B**。
- ρ¯ 是平均流体密度。
- *Δp* 是阀压差 *p*A – *p*B。

临界压差 *Δp*crit 是与 **Critical Reynolds number** *Re*crit（层流与湍流之间的流态转变点）相关的压差：

Δpcrit=πρ¯8Avalve(νRecritCd)2。

*Pressure loss* 描述由于面积减小而导致的阀中压力降低。*PR*loss 计算为：

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport。

*Pressure recovery* 描述由于面积增加而导致的阀中正压力变化。如果您不想捕获此压力增加，请清除 **Pressure recovery** 复选框。在这种情况下，*PR*loss 为 1。

### 表格体积流量参数化

当 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure` 时，阀根据用户提供的端口 **A** 和 **B** 之间体积流量和压差的表格数据打开。

质量流量为

m˙=ρ¯KΔp(Δp2+Δpcrit2)1/4，

其中：

- ρ¯ 是平均流体密度。
- Δp=pA−pB。
- Δpcrit=π2ρ¯8CdK(Recritv)2，其中 *Cd* 是流量系数，*Recrit* 是临界雷诺数，*ν* 是运动粘度。在此参数化中，*Cd* 和 *Recrit* 分别固定为 `0.64` 和 `150`。

当模块在表格数据范围内运行时，

K=tablelookup(ΔpTLU,KTLU,Δp,interpolation=linear,extrapolation=nearest)，

其中：

- *ΔpTLU* 是 **Pressure drop vector** 参数。
- KTLU=V˙TLUΔpTLU，其中 *V˙TLU* 是 **Volumetric flow rate vector** 参数。

当仿真压力低于 **Pressure drop vector** 参数的第一个元素时，*K*`=`*KLeak*，

KLeak=V˙TLU(1)|ΔpTLU(1)|，

其中 *V˙TLU(1)* 是 **Volumetric flow rate vector** 参数的第一个元素。

当仿真压力高于 **Pressure drop vector** 参数的最后一个元素时，*K*`=`*KMax*，

KMax=V˙TLU(end)|ΔpTLU(end)|，

其中 *V˙TLU(end)* 是 **Volumetric flow rate vector** 参数的最后一个元素。

### 打开动态特性

线性参数化支持阀打开和关闭动态特性。如果对打开动态特性进行建模，则会在建模控制压力的流动响应中引入滞后。*p*control 变为动态控制压力 *p*dyn；否则，*p*control 为稳态压力。动态控制压力的瞬时变化基于 **Opening time constant** *τ* 计算：

p˙dyn=pcontrol−pdynτ。

默认情况下，模块清除 **Opening dynamics** 复选框。

### 故障

要对故障建模，请在**故障**部分中，
单击要建模的故障旁边的**添加故障**超链接。使用
故障参数指定故障属性。有关故障建模的详细信息，
请参阅 Simscape 故障简介。

**发生故障时的开启面积**参数有三个选项：

- `Closed`
- `Open`
- `Maintain at last value`

故障触发后，阀门将在仿真的剩余时间内保持故障面积。

**线性参数化中的故障**

在线性参数化中，故障选项由阀门面积定义：

- `Closed` — 阀门面积冻结
  在**泄漏面积**。
- `Open` — 阀门面积冻结在
  **最大开启面积**。
- `Maintain at last value` — 当触发发生时，
  阀门冻结在开启面积。

**表格数据参数化中的故障**

在表格参数化中，故障选项由通过阀门的质量
流量定义：

- `Closed` — 阀门冻结在与**体积流量
  向量**和**压降
  向量**的第一个元素相关联的质量流量

  m˙=KLeakρ¯Δp。
- `Open` — 阀门冻结在与**体积流量
  向量**和**压降
  向量**的最后一个元素相关联的质量流量

  m˙=KMaxρ¯Δp
- `Maintain at last value` — 当触发发生时，阀门冻结在
  质量流量和压差

  m˙=KLastρ¯Δp，

其中

KLast=|m˙|ρ¯|Δp|。

### 生成数字数据表

*自 R2025a 起*

通过使用模块对话框的**描述**选项卡中的**生成
数据表**超链接，生成包含性能数据以及 Check Valve
(IL) 模块的压降与体积流量曲线的数字数据表。该数据表脚本会从
你在模型中选定的 Check Valve (IL) 模块导入参数。你可以使用特性曲线来帮助评估所选 Check Valve
(IL) 模块的开启压力和泄漏流量。要打开实时脚本：

1. 双击该模块以打开“模块参数”对话框。
2. 打开**描述**选项卡。
3. 单击**生成数据表**超链接。
4. 在模型中单击一个 Check Valve (IL) 模块。
5. 要生成数据表，请在实时脚本中单击
   **生成数据表**按钮。

### 预定义参数化

你可以使用预参数化的制造数据填充该模块，从而对
特定供应商组件进行建模。

要加载预定义参数化：

1. 在模块对话框中，在**选定部件**旁边，单击
   模块对话框设置中**选定部件**旁边的
   “<click to select>”超链接。
2. 将打开“模块参数化管理器”窗口。从菜单中选择一个部件
   并单击**全部应用**。你可以使用
   **制造商**下拉菜单缩小选择范围。
3. 你可以关闭**模块参数化管理器**菜单。
   该模块现在具有你指定的参数化。
4. 你可以通过在“模块参数化管理器”窗口中选择一个部件并查看
   **将选定部件与模块比较**
   部分中的数据，将当前参数设置与特定供应商组件进行比较。

**注意**

预定义模块参数化使用可用的数据源来提供参数
值。该模块会用工程判断和简化假设替代缺失数据。因此，预计仿真行为与实际物理
行为之间会有一些偏差。为确保准确性，请根据实验数据验证仿真行为，
并根据需要细化你的组件模型。

要了解更多信息，请参阅预参数化组件列表。
