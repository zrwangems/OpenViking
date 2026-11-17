---
type: simulink-block
title: 'Check Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Valves & Orifices / Directional Control Valves'
documentation_page: 'checkvalvetl'
documentation_source_path: 'ref/checkvalvetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Check Valve (TL)

## 端口
```yaml
ports:
- name: A
  summary: 阀门入口热液体
  direction: conserving
- name: B
  summary: 阀门出口热液体
  direction: conserving
```

### 守恒端口

### **A** — 阀门入口热液体

与阀门入口关联的热液体守恒端口。

### **B** — 阀门出口热液体

与阀门出口关联的热液体守恒端口。
## 参数
```yaml
parameters:
- name: Opening parameterization
  summary: 计算阀门开度的方法 Linear - Area vs. pressure（默认）| Tabulated data - Area vs. pressure | Tabulated data - Volumetric flow
    rate vs. pressure
  group: 参数
- name: Opening pressure specification
  summary: 用于阀门控制的压差 Pressure differential（默认）| Pressure at port A
  group: 参数
- name: Cracking pressure differential
  summary: 阈值压力 0.01 MPa（默认）| 正标量
  group: 参数
- name: Cracking pressure (gauge)
  summary: 阈值压力 0.1 MPa（默认）| 正标量
  group: 参数
- name: Maximum opening pressure differential
  summary: 阀门最大压差 0.02 MPa（默认）| 正标量
  group: 参数
- name: Maximum opening pressure (gauge)
  summary: 阀门最大压力 0.2 MPa（默认）| 正标量
  group: 参数
- name: Maximum opening area
  summary: 阀门完全打开时的面积 1e-4 m^2（默认）| 正标量
  group: 参数
- name: Leakage area
  summary: 阀门完全关闭位置时的间隙面积 1e-10 m^2（默认）| 正标量
  group: 参数
- name: Pressure differential vector
  summary: '用于表格参数化的压差值 [0.01 : 0.01 : 0.1] MPa（默认）| 1×*n* 向量'
  group: 参数
- name: Opening area vector
  summary: 用于表格参数化的阀门开度面积 [1e-10, 1e-05, 2e-05, 3e-05, 4e-05, 5e-05, 6e-05, 7.5e-05, 8.5e-05, .0001] m^2（默认）| 1×*n* 向量
  group: 参数
- name: Cross-sectional area at ports A and B
  summary: 阀门入口或出口处的面积 0.01 m^2（默认）| 正标量
  group: 参数
- name: Discharge coefficient
  summary: 流量系数 0.64（默认）| 正标量
  group: 参数
- name: Critical Reynolds number
  summary: 层流的上限雷诺数 150（默认）| 正标量
  group: 参数
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认）| 正标量
  group: 参数
- name: Pressure recovery
  summary: 是否考虑面积扩大时的压力增加 off（默认）| on
  group: 参数
- name: Opening dynamics
  summary: 是否考虑阀门打开时的流动响应 off（默认）| on
  group: 参数
- name: Opening time constant
  summary: 阀门打开时间常数 0.1 s（默认）| 正标量
  group: 参数
- name: Volumetric flow rate vector
  summary: 用于表格数据参数化的体积流量向量 [.000358, .045, .11, .191, .284, .39, .505, .63, .764, .905] .* 1e-3 m^3/s（默认）| 1×*n* 向量
  group: 参数
- name: Check Valve Area fault
  summary: 用于对阀门面积故障建模的选项 Add fault
  group: 故障
- name: Opening area when faulted
  summary: 故障时的阀门面积 Closed（默认）| Open | Maintain at last value
  group: 故障
```

### 参数

### **Opening parameterization** — 计算阀门开度的方法 `Linear - Area vs. pressure`（默认）| `Tabulated data - Area vs. pressure` | `Tabulated data - Volumetric flow rate vs. pressure`

计算阀门开度的方法。

- `Linear - Area vs. pressure`：阀门开度面积与阀门压力呈线性对应关系。
- `Tabulated data - Area vs. pressure`：模块根据面积值相对于压差的表格确定阀门质量流量。
- `Tabulated data - Volumetric flow rate vs. pressure`：模块根据体积流量值相对于压差的表格确定阀门质量流量。

### **Opening pressure specification** — 用于阀门控制的压差 `Pressure differential`（默认）| `Pressure at port A`

用于阀门控制的压差。选择 `Pressure differential` 选项以测量端口 **A** 和 **B** 之间的压力差。选择 `Pressure at port A` 选项以测量端口 **A** 与大气压之间的压力差。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Cracking pressure differential** — 阈值压力 `0.01 MPa`（默认）| 正标量

触发阀门操作的阈值压力。当控制压力为端口 **A** 和 **B** 之间的压差时，此值为设定压力。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`，并将 **Opening pressure specification** 设置为 `Pressure differential`。

### **Cracking pressure (gauge)** — 阈值压力 `0.1 MPa`（默认）| 正标量

当控制压力为端口 **A** 与大气压之间的压差时，触发阀门操作的表压阈值。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`，并将 **Opening pressure specification** 设置为 `Pressure at port A`。

### **Maximum opening pressure differential** — 阀门最大压差 `0.02 MPa`（默认）| 正标量

阀门最大压差。此参数为压力提供上限，以使系统压力保持在实际范围内。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`，并将 **Opening pressure specification** 设置为 `Pressure differential`。

### **Maximum opening pressure (gauge)** — 阀门最大压力 `0.2 MPa`（默认）| 正标量

阀门最大表压。此参数为压力提供上限，以使系统压力保持在实际范围内。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`，并将 **Opening pressure specification** 设置为 `Pressure at port A`。

### **Maximum opening area** — 阀门完全打开时的面积 `1e-4 m^2`（默认）| 正标量

阀门处于完全打开位置时的横截面积。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Leakage area** — 阀门完全关闭位置时的间隙面积 `1e-10 m^2`（默认）| 正标量

阀门处于完全关闭位置时所有间隙的总和。任何小于此值的面积都会饱和到指定的泄漏面积。此值通过保持流动的连续性来增强数值稳定性。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Pressure differential vector** — 用于表格参数化的压差值 `[0.01 : 0.01 : 0.1] MPa`（默认）| 1×*n* 向量

用于阀门开度面积表格参数化的压差值向量。向量元素必须与 **Opening area vector** 参数中的元素一一对应。元素按升序排列且必须大于 0。模块在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **Opening area vector** — 用于表格参数化的阀门开度面积 `[1e-10, 1e-05, 2e-05, 3e-05, 4e-05, 5e-05, 6e-05, 7.5e-05, 8.5e-05, .0001] m^2`（默认）| 1×*n* 向量

用于阀门开度面积表格参数化的阀门开度面积向量。向量元素必须与 **Pressure differential vector** 参数中的元素一一对应。元素按升序排列且必须大于 0。模块在表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated data - Area vs. pressure`。

### **Cross-sectional area at ports A and B** — 阀门入口或出口处的面积 `0.01 m^2`（默认）| 正标量

入口和出口端口 **A** 和 **B** 处的横截面积。模块在确定通过阀门质量流量的压力-流量方程中使用这些面积。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

用于修正理论流动中排放损失的修正因子。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过阀门的层流的上限雷诺数。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 正标量

连续平滑因子，当阀门处于接近打开或接近关闭位置时，为流动响应引入一层渐变。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Pressure recovery** — 是否考虑面积扩大时的压力增加 `off`（默认）| `on`

是否考虑流体从较小横截面积区域流向较大横截面积区域时的压力增加。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Opening dynamics** — 是否考虑阀门打开时的流动响应 `off`（默认）| `on`

是否考虑因打开阀门而对流体系统产生的瞬态效应。选择 **Opening dynamics** 通过在流动响应中引入一阶滞后来近似打开条件。**Opening time constant** 也会影响所建模的打开动态特性。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Opening time constant** — 阀门打开时间常数 `0.1 s`（默认）| 正标量

表示阀门从一个位置打开或关闭到另一个位置时流体达到稳态所需时间的常数。此参数影响所建模的打开动态特性。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 并选中 **Opening dynamics**。

### **Volumetric flow rate vector** — 用于表格数据参数化的体积流量向量 `[.000358, .045, .11, .191, .284, .39, .505, .63, .764, .905] .* 1e-3 m^3/s`（默认）| 1×*n* 向量

用于阀门开度表格参数化的体积流量值向量。此向量的元素数量必须与 **Pressure drop vector** 参数相同。向量元素必须按升序排列。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### 故障

### **Check Valve Area fault** — 用于对阀门面积故障建模的选项 `Add fault`

用于在模块中对阀门面积故障建模的选项。要添加故障，请点击 **Add fault** 超链接。当故障发生时，模块将使用 **Opening area when faulted** 参数中指定的值作为阀门面积。

### **Opening area when faulted** — 故障时的阀门面积 `Closed`（默认）| `Open` | `Maintain at last value`

模块发生故障时使用的面积。您可以选择阀门卡死在完全关闭或完全打开位置，或卡死在触发故障时的工况。当 **Opening parameterization** 为 `Linear - Area vs. pressure` 时，此参数设置面积；当 **Opening parameterization** 为 `Tabulated data` 时，此参数设置质量流量。

#### 依赖关系

要启用此参数，请通过点击 **Add fault** 超链接为模块启用故障。
## 所属库

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Directional Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2024b：使用表格数据对模块进行参数化

将 **Opening parameterization** 设置为 `Tabulated data - Area vs. pressure` 或 `Tabulated data - Volumetric flow rate vs. pressure`，以使用表格数据对模块进行参数化。

要保持与之前版本相同的行为，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### R2024b：使用 Simscape 故障接口对故障建模

Check Valve (TL) 模块现在支持 Simscape 故障接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

## 描述

热液体网络中的止回阀

Check Valve (TL) 模块在热液体域中对止回阀进行建模。止回阀是一种比例阀，当其端口之间的压差降至称为*开启压力*的阈值以下时关闭。止回阀常用于防回流装置，例如公共供水网络中使用的装置，其中水管下游的受污染水不得回流至上游。该模块不假定特定的阀门关闭机制，如球式、盘式或隔膜式。允许的流动方向始终为从端口 **A** 到端口 **B**。

当阀门两端的压降升至指定的开启压力以上时，阀门开启。当压降达到模块中指定的最大值时，阀门完全打开，其开启面积不再随压力增加。通过阀门的流量永远不会真正为零，因为当压力降至开启压力以下时，仍会保留一个小泄漏面积。

### 面积与压力参数化

您可以使用线性或表格化的面积和压力数据对模块进行参数化。

**线性面积与压力参数化**

当 **Opening parameterization** 为 `Linear - Area vs. pressure` 时，阀门开启面积与开启压差呈线性关系。阀门控制有两种选项：

- 当 **Opening pressure differential** 为 `Pressure differential` 时，控制压力为端口 **A** 和 **B** 之间的压差。当 *P*control 达到或超过 **Cracking pressure differential** 参数的值时，阀门开始开启。
- 当 **Opening pressure differential** 为 `Pressure at port A` 时，控制压力为端口 **A** 与大气压之间的压差。当 *P*control 达到或超过 **Cracking pressure (gauge)** 参数的值时，阀门开始开启。

阀门面积的线性参数化为

Avalve=p^(Amax−Aleak)+Aleak，

其中归一化压力 p^ 为

p^=pcontrol−pcrackingpmax−pcracking。

当阀门处于接近打开或接近关闭位置时，您可以通过调整 **Smoothing factor** 参数来保持仿真中的数值鲁棒性。如果 **Smoothing factor** 参数非零，模块将在 *pcracking* 和 *pmax* 之间平滑地饱和控制压力。有关更多信息，请参阅 Numerical Smoothing。

**表格数据面积与压力参数化**

当您将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure` 时，模块根据 **Opening area vector** 参数与 **Pressure differential vector** 参数的曲线，对仿真压差线性插值 *Avalve*。

对于表格数据以及线性面积与压力参数化，通过阀门的质量流量为

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4，

其中：

- *Cd* 是 **Discharge coefficient** 参数的值。
- *Avalve* 是瞬时阀门开启面积。
- *Aport* 是 **Cross-sectional area at ports A and B** 参数的值。
- ρ¯ 是平均流体密度。
- *Δp* 是阀门压差 *pA* – *pB*。

临界压差 *Δpcrit* 是与 **Critical Reynolds number** 参数 *Recrit* 相关的压差，即层流与湍流之间的流态转变点：

Δpcrit=πρ¯8Avalve(νRecritCd)2。

压力损失是由于面积减小而导致的阀门压力降低。*PRloss* 为

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport。

压力恢复是由于面积增加而导致的阀门正压力变化。如果您不希望捕捉此压力增加，请清除 **Pressure recovery** 复选框。在这种情况下，*PRloss* 为 1。

### 表格化体积流量参数化

当 **Opening parameterization** 为 `Tabulated data - Volumetric flow rate vs. pressure` 时，阀门根据用户提供的端口 **A** 和 **B** 之间体积流量与压差的表格数据开启。

质量流量为

m˙=ρ¯KΔp(Δp2+Δpcrit2)1/4，

其中：

- ρ¯ 是平均流体密度。
- Δp=pA−pB。
- Δpcrit=π2ρ¯8CdK(Recritv)2，其中 *Cd* 是排放系数，*Recrit* 是临界雷诺数，*ν* 是运动粘度。在此参数化中，*Cd* 和 *Recrit* 分别固定为 `0.64` 和 `150`。

当模块在表格数据的范围内运行时，

K=tablelookup(ΔpTLU,KTLU,Δp,interpolation=linear,extrapolation=nearest)，

其中：

- *ΔpTLU* 是 **Pressure drop vector** 参数。
- KTLU=V˙TLUΔpTLU，其中 *V˙TLU* 是 **Volumetric flow rate vector** 参数。

当仿真压力降至 **Pressure drop vector** 参数的第一个元素以下时，*K*`=`*KLeak*，

KLeak=V˙TLU(1)|ΔpTLU(1)|，

其中 *V˙TLU(1)* 是 **Volumetric flow rate vector** 参数的第一个元素。

当仿真压力升至 **Pressure drop vector** 参数的最后一个元素以上时，*K*`=`*KMax*，

KMax=V˙TLU(end)|ΔpTLU(end)|，

其中 *V˙TLU(end)* 是 **Volumetric flow rate vector** 参数的最后一个元素。

### 质量平衡

质量通过阀门守恒

m˙A+m˙B=0，

其中 m˙ 是端口 **A** 或 **B** 处的质量流量。

### Energy Balance

该阀是一个绝热组件。流体与阀壁之间不会发生热交换。流体通过阀时，既不对流体做功，也不由流体做功。在这些假设下，能量只能通过对流通过端口 **A** 和 **B** 进入和离开该阀。根据能量守恒原理，通过各端口的能量流之和必须始终等于零，

ϕA+ϕB=0,

其中 *ϕ* 是通过端口 **A** 或 **B** 进入该阀的能量流率。

### Opening Dynamics

当 **Opening parameterization** 为 `Linear- Area
vs. Pressure` 时，该模块可以对开启和关闭动态进行建模。如果对开启动态进行建模，该模块会为控制压力对应的流量响应引入滞后，并且 *pcontrol* 变为动态控制压力 *pdyn*。否则，*pcontrol* 为稳态压力。该模块基于 **Opening time constant** 参数 *τ* 计算动态控制压力的瞬时变化：

p˙dyn=pcontrol−pdynτ.

默认情况下，**Opening dynamics** 复选框处于清除状态。

### 故障

要对故障进行建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault** 超链接。使用故障参数指定故障属性。有关故障建模的更多信息，请参阅 Introduction to Simscape Faults。

**Opening area when faulted** 参数有三个选项：

- `Closed`
- `Open`
- `Maintain at last value`

故障触发后，该阀将在仿真剩余时间内保持故障面积。

**Faulting in the Linear Parameterization**

当 **Opening parameterization** 为 `Linear -
Area vs. pressure` 时，阀面积定义故障选项：

- `Closed` — 阀面积冻结为 **Leakage area** 参数的值。
- `Open` — 阀面积冻结为 **Maximum opening area** 参数的值。
- `Maintain at last value` — 触发发生时，阀冻结在开启面积。

**表格化数据参数化中的故障**

当 **Opening parameterization** 为 `Tabulated
data - Area vs. pressure` 或 `Tabulated data -
Volumetric flow rate vs. pressure` 时，通过该阀的质量流量定义故障选项：

- `Closed` — 阀冻结在与 **Volumetric flow rate vector** 参数和 **Pressure drop vector** 参数的首个元素相关联的质量流量

  m˙=KLeakρ¯Δp.
- `Open` — 阀冻结在与 **Volumetric flow rate vector** 和 **Pressure drop vector** 参数的最后一个元素相关联的质量流量

  m˙=KMaxρ¯Δp
- `Maintain at last value` — 触发发生时，阀冻结在质量流量和压差

  m˙=KLastρ¯Δp,

其中

KLast=|m˙|ρ¯|Δp|.

### Predefined Parameterization

您可以使用预参数化的制造数据填充该模块，从而对特定供应商组件进行建模。

要加载预定义参数化：

1. 在模块对话框中，单击模块对话框设置中 **Selected part** 旁边的 "<click to select>" 超链接。
2. 将打开 Block Parameterization Manager 窗口。从菜单中选择一个部件，然后单击 **Apply all**。您可以使用 **Manufacturer** 下拉菜单缩小选择范围。
3. 您可以关闭 **Block Parameterization Manager** 菜单。该模块现在具有您指定的参数化。
4. 您可以通过在 Block Parameterization Manager 窗口中选择一个部件，并查看 **Compare selected part with block** 部分中的数据，将当前参数设置与特定供应商组件进行比较。

**Note**

预定义模块参数化使用可用数据源提供参数值。该模块会用工程判断和简化假设替代缺失数据。因此，预计仿真行为与实际物理行为之间会有一些偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化您的组件模型。

要了解更多信息，请参阅 List of Pre-Parameterized Components。
