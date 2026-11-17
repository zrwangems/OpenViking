---
type: simulink-block
title: 'Pressure Relief Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Valves & Orifices / Pressure Control Valves'
documentation_page: 'pressurereliefvalvetl'
documentation_source_path: 'ref/pressurereliefvalvetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure Relief Valve (TL)

## 端口

### 输入

### **Ps** — 设定压力信号，Pa 物理信号

用于受控阀操作的设定压差，单位为 Pa。

#### 依赖

要启用此端口，请将 **Set pressure control** 设置为 `Controlled`。
### 守恒

### **A** — 液体端口 热液体

与阀入口 A 关联的热液体守恒端口。

### **B** — 液体端口 热液体

与阀入口 B 关联的热液体守恒端口。

## 参数

### 参数

### **Set pressure control** — 阀操作方法 `Constant`（默认）| `Controlled`

阀操作方法。`Constant` 阀在固定的压力调节范围内线性开启，或根据您提供的表格化压力和开口面积数据开启。`Controlled` 阀根据端口 **Ps** 处的可变设定压力信号在固定的压力调节范围内开启。

#### 依赖

要启用此参数，请将 **Set pressure control** 设置为 `Constant`。

### **Opening parameterization** — 恒定阀开启或关闭的建模方法 `Linear - Area vs. pressure`（默认）| `Tabulated data - Area vs. pressure` | `Tabulated data - Volumetric flow rate vs. pressure`

阀开启或关闭的建模方法。您可以线性地参数化阀的开启，或使用将面积与压差关联的值表。

#### 依赖

要启用此参数，请将 **Set pressure control** 设置为 `Constant`。

### **Pressure control specification** — 评估压力的方法 `Pressure at port A`（默认）| `Pressure differential`

阀控制压力的指定方法。当您将此参数设置为 `Pressure at port A` 时，模块仅使用端口 **A** 处的压力来确定流量何时超过 **Set pressure (gauge)** 参数的值。当您将此参数设置为 `Pressure differential` 时，模块使用 **Set pressure differential** 参数的值来确定从端口 **A** 到端口 **B** 的压差是否超过范围。

#### 依赖

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **Set pressure (gauge)** — 开启机构触发时的表压 `0.1` `MPa`（默认）| 正标量

开启机构触发时的压力。在阀的整个压力调节范围内，开口面积保持可变。

#### 依赖

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，并且满足以下任一条件：

- **Pressure control specification** 设置为 `Pressure at port A`，且 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。
- **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### **Set pressure differential** — 最小开启压差 `0` `MPa`（默认）| 非负标量

打开阀所需的端口 **A** 和 **B** 之间的最小压差。高于此值的压差会使阀逐渐打开，直至达到完全开启状态。

#### 依赖

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，**Pressure control specification** 设置为 `Pressure differential`，并将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Pressure regulation range** — 阀压力范围 `0.15` `MPa`（默认）| 正标量

阀的工作范围。阀在设定压力值处开始开启，并在 *pmax* 处完全开启，*pmax* 是压力调节范围的终点，其中 *pmax = pset + prange*。

#### 依赖

要启用此参数，请设置以下任一条件：

- **Set pressure control** 设置为 `Controlled`。
- **Set pressure control** 设置为 `Constant`，且 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Maximum opening area** — 完全开启位置的开口面积 `1e-4` `m^2`（默认）| 正标量

当阀处于压力调节范围上限时，由于密封不完美，阀在完全开启位置的开口面积。

#### 依赖

要启用此参数，请设置以下任一条件：

- **Set pressure control** 设置为 `Controlled`。
- **Set pressure control** 设置为 `Constant`，且 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Leakage area** — 完全关闭位置的间隙面积 `1e-10` `m^2`（默认）| 正标量

阀处于完全关闭位置时所有间隙的总和。模块将较小的数值饱和到此值。此参数通过保持流量的连续性来帮助提高数值稳定性。

#### 依赖

要启用此参数，请设置以下任一条件：

- **Set pressure control** 设置为 `Controlled`。
- **Set pressure control** 设置为 `Constant`，且 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Pressure differential vector** — 表格化参数化的压差值 `[0.2 : 0.2 : 1.2]` MPa（默认）| 1×*n* 向量

用于阀开口面积表格化参数化的压差值向量。向量元素必须与 **Opening area vector** 参数中的元素一一对应。元素必须按升序排列，且必须大于 0。模块在表格数据点之间采用线性插值。

此参数的第一个元素是阀的压力设定值，即阀开始开启的压力。最后一个元素是最大压力，即阀完全开启的压力。两者之差即为阀的压力调节范围。

#### 依赖

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，并且满足以下任一条件：

- **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。
- **Opening parameterization** 设置为 `Tabulated data - Area vs. pressure`，且 **Pressure control specification** 设置为 `Pressure differential`。

### **Opening pressure (gauge) vector** — 表格化面积参数化的压差值 `[0.2 : 0.2 : 1.2]` MPa（默认）| 1×*n* 向量

用于阀开口面积表格化面积参数化的压差值向量。向量元素必须与 **Opening area vector** 参数中的元素一一对应。元素必须按升序排列，且必须大于 0。模块在表格数据点之间采用线性插值。

此参数的第一个元素是阀的压力设定值，即阀开始开启的压力。最后一个元素是最大压力，即阀完全开启的压力。两者之差即为阀的压力调节范围。

#### 依赖

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，**Opening parameterization** 设置为 `Tabulated data - Area vs. pressure`，并将 **Pressure control specification** 设置为 `Pressure at port A`。

### **Opening area vector** — 表格化面积参数化的阀开口面积 `[1e-10, 2e-06, 4e-06, 6e-06, 8e-06, 1e-05]`m^2（默认）| 1×*n* 向量

用于阀开口面积表格化面积参数化的阀开口面积向量。向量元素必须与 **Pressure differential vector** 参数中的元素一一对应。元素必须按升序排列，且必须大于 0。模块在表格数据点之间采用线性插值。

#### 依赖

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Tabulated data - Area vs. pressure`。

### **Volumetric flow rate vector** — 用于表格数据参数化的体积流量向量 `[1e-09, 3.6e-05, 8.9e-05, .00015, .00023, .00031]`m^3/s（默认）| 1×*n* 向量

用于阀门开度表格参数化的体积流量值向量。此向量必须与 **Pressure drop vector** 参数具有相同数量的元素。向量元素必须按升序排列。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### **Cross-sectional area at ports A and B** — 守恒端口处的面积 `0.01` `m^2`（默认）| 正标量

端口 **A** 和 **B** 处的面积，模块在用于确定通过阀门的质量流量的压力-流量方程中使用该面积。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

模块用于修正理论流动中排放损失的修正系数。

#### 依赖关系

要启用此参数，请设置以下任一选项：

- **Set pressure control** 设置为 `Controlled`。
- **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过阀门的层流的上限雷诺数。

#### 依赖关系

要启用此参数，请设置以下任一选项：

- **Set pressure control** 设置为 `Controlled`。
- **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 范围 [0,1] 内的正标量

连续平滑因子，在阀门接近打开或接近关闭位置时，为流量响应引入一层渐变变化。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

平滑因子为 0 对应于在设定压力和最大面积压力处不连续的线性函数。平滑因子为 1 对应于在整个函数域内连续变化的非线性函数。

平滑因子介于 0 和 1 之间对应于在设定压力和最大面积压力处具有平滑非线性过渡的连续函数。

#### 依赖关系

要启用此参数，请设置以下任一选项：

- **Set pressure control** 设置为 `Controlled`。
- **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Pressure recovery** — 是否考虑面积扩张中的压力增加 `off`（默认）| `on`

是否考虑当流体从较小横截面积区域流向较大横截面积区域时的压力增加。要捕获压力增加，请选择此参数。

#### 依赖关系

要启用此参数，请设置以下任一选项：

- **Set pressure control** 设置为 `Controlled`。
- **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **Opening dynamics** — 是否考虑阀门开启的流量响应 `off`（默认）| `on`

是否考虑阀门开启对流体系统造成的瞬态效应。选择此参数通过在流量响应中引入一阶滞后来近似开启条件。

### **Opening time constant** — 阀门开启时间常数 `0.1` s（默认）| 正标量

用于计算开启动态滞后的时间常数。

#### 依赖关系

要启用此参数，请选择 **Opening dynamics**。

### 故障

### **Pressure Relief Valve Area fault** — 用于对开启面积故障建模的选项 `Add fault`

用于在模块中对阀门面积故障建模的选项。要添加故障，请点击 **Add fault** 超链接。当故障发生时，通常由开启参数化设置的阀门面积将根据 **Opening area when faulted** 参数中指定的值进行设置。

### **Opening area when faulted** — 故障时的阀门特性 `Closed`（默认）| `Open` | `Maintain last value`

故障时的阀门类型。您可以选择阀门在打开、关闭或故障触发时的面积处卡滞。

#### 依赖关系

要启用此参数，请点击 **Add fault** 超链接。

## 所属库

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Pressure Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

### R2024b：使用 Simscape 故障接口对故障建模

Pressure Relief Valve (TL) 模块现在支持 Simscape 故障接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

### R2024b：对受控泄压阀建模

将 **Set pressure control** 设置为 `Controlled`，以通过端口 **Ps** 处的信号控制模块设定压力。

### R2023a：新的参数化选项

使用 **Opening parameterization** 参数选择模块参数化：`Linear - Area vs. pressure`、`Tabulated data - Area vs. pressure` 或 `Tabulated data - Volumetric flow rate vs. pressure`。

## 描述

热液体网络中的泄压阀

Pressure Relief Valve (TL) 模块表示一个在热液体网络中释放过剩压力的阀门。当压力低于指定值时，阀门保持关闭。当达到或超过此压力时，阀门打开。此设定压力可以是阀门上端口 **A** 和 **B** 之间的阈值压差，也可以是端口 **A** 与大气压力之间的阈值压差。高于设定压力的控制压力会使阀门逐渐打开，从而允许流体网络释放过剩压力。

### 压力控制

当 **Opening parameterization** 为 `Linear - Area vs. pressure` 时，归一化压力 p^ 控制阀门开启面积。归一化压力为

p^=pcontrol-psetpmax-pset,

其中：

- *pcontrol* 是控制压力，取决于 **Pressure control specification** 参数的值。

  当您将 **Pressure control specification** 设置为 `Pressure differential` 时，控制压力为 *pA ̶ pB*。

  当您将 **Pressure control specification** 设置为 `Pressure at port A` 时，控制压力为端口 **A** 处压力与大气压力之间的差值。
- *pset* 是设定压力，取决于 **Pressure control specification** 参数的值。

  当您将 **Pressure control specification** 设置为 `Pressure differential` 时，*pset* 是 **Set pressure differential** 参数的值。

  当您将 **Set pressure specification** 设置为 `Pressure at port A` 时，*pset* 是 **Set pressure (gauge)** 参数的值。
- *pmax* 是最大压力，*pmax = pset + prange*，其中 *prange* 是 **Pressure regulation range** 参数的值。

### 开度参数化

质量流量取决于 **Opening parameterization** 参数的值。

**面积 vs. 压力参数化**

当您将 **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure` 时，质量流量为

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4,

其中：

- *Cd* 是 **Discharge coefficient** 参数的值。
- *Avalve* 是瞬时阀门开口面积。
- *Aport* 是 **Cross-sectional area at ports A and B** 参数的值。
- ρ¯ 是平均流体密度。
- *Δp* 是阀门压差 *pA* – *pB*。

临界压差 *Δpcrit* 是与 **Critical Reynolds number** *Recrit* 相关的压差，即层流与湍流之间的流态转变点：

Δpcrit=π8Avalveρ¯(μRecritCd)2,

其中 *μ* 是热液体的动力粘度。

压力损失 *PRloss* 描述了由于面积减小而导致的阀门压力降低。该模块按如下方式计算 *PRloss*：

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport。

压力恢复描述了由于面积增大而导致的阀门正压力变化。当您清除 **Pressure recovery** 复选框时，该模块将 *PRloss* 设置为 1。

当您将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 时，该模块按如下方式计算开口面积：

Avalve=p^(Amax−Aleak)+Aleak,

其中 *Aleak* 是 **Leakage Area** 参数的值，*Amax* 是 **Maximum opening area** 参数的值。

下图显示了该模块如何使用线性参数化来控制开口面积。

使用线性参数化的常闭阀，端口 X 和 Y 之间的压差与开口面积的关系

当阀门在线性参数化中处于接近打开或接近关闭位置时，您可以通过调整 **Smoothing factor** 参数来保持仿真中的数值鲁棒性。如果 **Smoothing factor** 参数非零，该模块会在 *pset* 和 *pmax* 之间平滑地饱和控制压力。有关详细信息，请参阅数值平滑。

当您将 **Opening parameterization** 设置为 `Tabulated data - Area vs. pressure` 时，该模块按如下方式计算开口面积：

Avalve=tablelookup(pcontrol,TLU,ref,ATLU,pcontrol,interpolation=linear,extrapolation=nearest),

其中：

- *pcontrol,TLU,ref* = *pTLU* + *poffset*。
- *pTLU* 是 **Pressure differential vector** 或 **Opening pressure (gauge) vector** 参数，具体取决于 **Pressure control specification** 参数的值。
- *poffset* 是一个内部压力偏移量，使得当 *pcontrol,TLU,ref* = *pset* 时阀门开始关闭。
- *ATLU* 是 **Opening area vector** 参数。

下图显示了当 **Opening parameterization** 为 `Tabulated data - Area vs. pressure` 时，该模块如何控制开口面积。

使用表格参数化的常闭阀，端口 X 和 Y 之间的压差与开口面积的关系

**体积流量 vs. 压力参数化**

当您将 **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure` 时，阀门根据用户提供的端口 **A** 和 **B** 之间体积流量和压差的表格数据打开。

该模块按如下方式计算质量流量：

m˙=ρ¯V˙,

其中：

- V˙ 是体积流量。
- ρ¯ 是平均流体密度。

该模块使用以下关系计算质量流量与压力之间的关系：

m˙=Kρ¯Δp,

其中

K=V˙|Δp|。

**受控压力调节**

当您将 **Set pressure control** 设置为 `Controlled` 时，控制压力是端口 **A** 和 **B** 之间的压差，并且没有使用表压的选项。归一化压力为

p^=pcontrol-pspmax-ps,

其中：

- *ps* 是端口 **Ps** 处信号的值。
- *pmax = ps + prange*，其中 *prange* 是 **Pressure regulation range** 参数的值。
- *pcontrol* 是端口 **A** 和 **B** 之间的压差，*pA ̶ pB*。

### 开度动态

当您将 **Opening dynamics** 设置为 `On` 时，该模块引入控制压力滞后，并用动态控制压力 *pdyn* 替换 *pcontrol*。该模块基于 **Opening time constant** 参数 *τ* 计算动态控制压力

p˙dyn=pcontrol−pdynτ。

默认情况下，该模块清除 **Opening dynamics** 复选框。

### 能量平衡

阀门中的能量守恒方程为

ϕA+ϕB=0,

其中：

- *ϕ*A 是通过端口 **A** 流入阀门的能量流率。
- *ϕ*B 是通过端口 **B** 流入阀门的能量流率。

### 故障

要对故障建模，请在 **Faults** 部分中，单击要建模的故障旁边的 **Add fault** 超链接。使用故障参数指定故障属性。有关故障建模的详细信息，请参阅 Simscape 故障简介。

**Opening area when faulted** 参数有三个故障选项：

- `Closed` — 阀门冻结在其最小值：

  - 当您将 **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 时，阀门面积冻结在 **Leakage area** 参数处。
  - 当您将 **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Tabulated data - Area vs. pressure` 时，阀门面积冻结在 **Opening area vector** 参数的第一个元素处。
  - 当您将 **Set pressure control** 设置为 `Controlled` 时，阀门面积冻结在 **Leakage area** 参数处。
- `Open` — 阀门冻结在其最大值：

  - 当您将 **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 时，阀门面积冻结在 **Maximum opening area** 参数处。
  - 当您将 **Set pressure control** 设置为 `Constant`，并将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. pressure` 时，阀门面积冻结在 **Opening area vector** 参数的最后一个元素处。
  - 当您将 **Set pressure control** 设置为 `Controlled` 时，阀门面积冻结在 **Maximum opening area** 参数处。
- `Maintain last value` — 阀门面积冻结在触发发生时的阀门开口面积处。

由于阀门面积极值处的数值平滑，该模块使用的最小面积大于 **Leakage area** 参数，最大面积小于 **Maximum orifice area** 参数，其比例与 **Smoothing factor** 参数值成正比。

故障触发后，阀门在仿真的剩余时间内保持在故障面积处。

当您将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure` 时，故障选项由通过阀门的体积流量定义：

- `Closed` — 阀门停止在与 **Volumetric flow rate vector** 参数和 **Pressure drop vector** 参数第一个元素相关的质量流量处：

  m˙=KLeakρ¯Δp。
- `Open` — 阀门停止在与 **Volumetric flow rate vector** 参数和 **Pressure drop vector** 参数最后一个元素相关的质量流量处：

  m˙=KMaxρ¯Δp
- `Maintain at last value` — 阀门停止在触发发生时的质量流量和压差处：

  m˙=KLastρ¯Δp,

其中

KLast=|m˙|ρ¯|Δp|。

### 预定义参数化

您可以使用预先参数化的制造数据填充该模块，从而对特定供应商组件进行建模。

要加载预定义参数化：

1. 在模块对话框中，点击 **Selected part** 旁边的“<click to select>”超链接。
2. 将打开 Block Parameterization Manager 窗口。从菜单中选择一个部件，然后点击 **Apply all**。您可以使用 **Manufacturer** 下拉菜单缩小选择范围。
3. 您可以关闭 **Block Parameterization Manager** 菜单。该模块现在具有您指定的参数化。
4. 您可以通过在 Block Parameterization Manager 窗口中选择一个部件并查看 **Compare selected part with block** 部分中的数据，将当前参数设置与特定供应商组件进行比较。

**注意**

预定义模块参数化使用可用的数据源来提供参数值。该模块用工程判断和简化假设替代缺失数据。因此，预计仿真行为与实际物理行为之间会存在一定偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化您的组件模型。

要了解更多信息，请参阅 List of Pre-Parameterized Components。
