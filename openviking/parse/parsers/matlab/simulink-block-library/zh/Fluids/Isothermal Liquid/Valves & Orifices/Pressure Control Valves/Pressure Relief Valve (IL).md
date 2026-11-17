---
type: simulink-block
title: 'Pressure Relief Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Pressure Control Valves'
documentation_page: 'pressurereliefvalveil'
documentation_source_path: 'ref/pressurereliefvalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# Pressure Relief Valve (IL)

## 端口

### 守恒端口

### **A** — 液体端口，等温液体

阀门的入口或出口点。

### **B** — 液体端口，等温液体

阀门的入口或出口点。
### 输入

### **Ps** — 设定压力信号，物理信号

用于受控阀门操作的变信号设定压力。

#### 依赖关系

要启用此端口，请将 **Set pressure control** 设置为
`Controlled`。

## 参数

### 参数

### **Set pressure control** — 阀门操作方法 `Constant`（默认）| `Controlled`

阀门操作方法。`Constant` 阀门在固定的压力调节范围内线性开启，或根据您提供的表格式压力和开度面积数据开启。`Controlled` 阀门根据端口 **Ps** 处的可变设定压力信号在固定的压力调节范围内开启。

### **Opening parameterization** — 恒定阀门开启或关闭的建模方法 `Linear - Area vs. pressure`（默认）| `Tabulated data - Area vs. pressure` | `Tabulated data - Volumetric flow rate vs. pressure`

阀门开启或关闭的建模方法。阀门开度可以通过线性参数化，也可以通过将面积与压差关联的值表进行参数化。

### **Opening pressure specification** — 用于阀门控制的压差 `Pressure differential`（默认）| `Pressure at port A`

用于阀门控制的压差。选择 `Pressure differential` 将端口 **A** 和端口 **B** 之间的压力差设置为压力控制的触发条件。选择 `Pressure at port A` 将端口 **A** 处的表压（即端口 **A** 处压力与大气压力之差）设置为压力控制的触发条件。

### **Set pressure (gauge)** — 阈值压力 `0.1` MPa（默认）| 正标量

当 **Pressure control specification** 相对于端口 **A** 时，触发阀门操作的超过表压。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，并将 **Pressure control specification** 设置为 `Pressure at port A`。

### **Set pressure differential** — 阈值压力 `0` MPa（默认）| 正标量

触发阀门操作的超过压力。当 **Pressure control specification** 相对于端口 **A** 和 **B** 之间的压差时，此为设定压力。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，并将 **Pressure control specification** 设置为 `Pressure differential`。

### **Pressure regulation range** — 阀门工作压力范围 `0.1 MPa`（默认）| 正标量

阀门工作范围。阀门在设定压力值处开始开启，并在 *pmax* 处完全开启，*pmax* 是压力调节范围的终点，其中 *pmax = pset + prange*。

#### 依赖关系

要启用此参数，请设置

- **Set pressure control** 为 `Controlled`
- **Set pressure control** 为 `Constant` 且 **Opening parameterization** 为 `Linear - Area vs. pressure`

### **Maximum opening area** — 阀门完全开启时的面积 `1e-4` m^2（默认）| 正标量

阀门处于完全开启位置时的横截面积。

#### 依赖关系

要启用此参数，请设置以下任一：

- **Set pressure control** 为 `Controlled`
- **Set pressure control** 为 `Constant` 且 **Opening parameterization** 为 `Linear - Area vs. pressure`

### **Leakage area** — 完全关闭位置时的阀门间隙面积 `1e-10` m^2（默认）| 正标量

阀门处于完全关闭位置时所有间隙的总和。任何小于此值的面积都保持在指定的泄漏面积。这通过保持流量连续性来帮助数值稳定性。

#### 依赖关系

要启用此参数，请设置以下任一：

- **Set pressure control** 为 `Controlled`。
- **Set pressure control** 为 `Constant` 且 **Opening parameterization** 为 `Linear - Area vs. pressure`

### **Opening pressure (gauge) vector** — 用于表格参数化的压差值 `[0.2 : 0.2 : 1.2]` MPa（默认）| 1×*n* 向量

用于阀门开度面积表格参数化的压差值向量。向量元素必须与 **Opening area vector** 参数中的元素一一对应。元素按升序列出，且必须大于 0。表格数据点之间采用线性插值。

此参数的第一个元素是阀门的压力设定值，阀门在此处开始开启。最后一个元素是最大压力，阀门在此处完全开启。两者之差即为阀门的压力调节范围。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，**Opening parameterization** 设置为 `Tabulated data - Area vs. pressure`，并将 **Opening pressure specification** 设置为 `Pressure differential`。

### **Pressure differential vector** — 用于表格参数化的压差值 `[0.2 : 0.2 : 1.2]` MPa（默认）| 1×*n* 向量

用于阀门开度面积表格参数化的压差值向量。向量元素必须与 **Opening area vector** 参数中的元素一一对应。元素按升序列出，且必须大于 0。表格数据点之间采用线性插值。

此参数的第一个元素是阀门的压力设定值，阀门在此处开始开启。最后一个元素是最大压力，阀门在此处完全开启。两者之差即为阀门的压力调节范围。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，并设置

- **Opening parameterization** 为 `Tabulated data - Volumetric flow rate vs. pressure`，或
- **Opening parameterization** 为 `Tabulated data - Area vs. pressure` 且 **Opening pressure specification** 为 `Pressure differential`。

### **Volumetric flow rate vector** — 用于表格数据参数化的体积流量向量 `[1e-09, 3.6e-05, 8.9e-05, .00015, .00023, .00031]`（默认）| 1×*n* 向量

用于阀门开度表格参数化的体积流量值向量。此向量必须与 **Pressure drop vector** 参数具有相同数量的元素。向量元素必须按升序列出。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### **Opening area vector** — 用于表格参数化的阀门开度面积 `[1e-10, 2e-06, 4e-06, 6e-06, 8e-06, 1e-05]`m^2（默认）| 1×*n* 向量

用于阀门开度面积表格参数化的阀门开度面积向量。向量元素必须与 **Pressure differential vector** 参数中的元素一一对应。元素按升序列出，且必须大于 0。表格数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Tabulated data - Area vs. pressure`。

### **Cross-sectional area at ports A and B** — 阀门入口或出口处的面积 `inf` m^2（默认）| 正标量

入口和出口端口 **A** 和 **B** 处的横截面积。这些面积用于确定通过阀门的质量流量的压力-流量方程中。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

考虑理论流动中排放损失的修正因子。Simscape™ Fluids™ 中阀门的默认流量系数为 0.64。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过阀门的层流的上限雷诺数。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 正标量

连续平滑因子，当阀门处于接近开启或接近关闭位置时，为流量响应引入一层渐变变化。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Pressure recovery** — 是否考虑面积扩大时的压力升高 `off`（默认）| `on`

当流体从较小横截面积区域流向较大横截面积区域时，考虑压力升高。当您清除 **Pressure recovery** 复选框时，不会捕获此压力升高。

### **Opening dynamics** — 是否考虑阀门开启的流量响应 `off`（默认）| `on`

是否考虑阀门开启对流体系统造成的瞬态效应。选择 **Opening dynamics** 会通过在流量响应中引入一阶滞后来近似开启条件。**Opening time constant** 也会影响所建模的开启动态。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **Opening time constant** — 阀门开启时间常数 `0.1` s（默认）| 正标量

当阀门从一个位置开启或关闭到另一个位置时，流体达到稳态所需时间的常数。此参数影响所建模的开启动态。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`，并选择 **Opening dynamics**。

### 故障

### **Pressure Relief Valve Area fault** — 用于对开启面积故障建模的选项 `Add fault`

用于在模块中对阀门面积故障建模的选项。要添加故障，请点击 **Add fault** 超链接。发生故障时，通常由开启参数化设置的阀门面积将根据 **Opening area when faulted** 参数中指定的值进行设置。

### **Opening area when faulted** — 故障时的阀门特性 `Closed`（默认）| `Open` | `Maintain last value`

故障时的阀门类型。您可以选择阀门在开启、关闭或故障触发时面积处卡滞。

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

Pressure Relief Valve (IL) 模块现在支持 Simscape 故障接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

### R2022b：访问预参数化模块选项

该模块支持预参数化选项。供应商包括 Daikin、Kawasaki Heavy Industries、Parker 和 Yuken。

## 描述

等温液体网络中的减压阀

Pressure Relief Valve (IL) 模块表示等温液体网络中的减压阀。当压力低于指定值时，阀门保持关闭。当达到或超过此压力时，阀门开启。此设定压力要么是阀门上端口 **A** 和 **B** 之间的阈值压差，要么是端口 **A** 与大气压力之间的阈值压差。要基于流体系统中的其他元件进行压力控制，请参阅 Pressure Compensator Valve (IL) 模块。

### 压力控制

对于线性预参数化，控制阀门开启面积的归一化压力 p^ 取决于 **Set pressure control** 参数的值。

当您将 **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 时，归一化压力为

p^=pcontrol-psetpmax-pset，

其中：

- *pcontrol* 是控制压力。当您将 **Opening pressure specification** 设置为 `Pressure differential` 时，控制压力为 *pA ̶ pB*。当您将 **Opening pressure specification** 设置为 `Pressure at port A` 时，控制压力为端口 **A** 处压力与大气压力之间的差值。
- *pset* 是设定压力。当 **Opening pressure specification** 为 `Pressure differential` 时，*pset* 是 **Set pressure differential** 参数的值。当 **Opening pressure specification** 为 `Pressure at port A` 时，*pset* 是 **Set pressure (gauge)** 参数的值。
- *pmax* 是压力调节范围的最大值，*pmax = pset + prange*，其中 *prange* 是 **Pressure regulation range** 参数的值。

当您将 **Set pressure control** 设置为 `Controlled` 时，归一化压力为

p^=pcontrol-pspmax-ps，

其中：

- *ps* 是端口 **Ps** 处信号的值。
- *pmax = ps + prange*，其中 *prange* 是 **Pressure regulation range** 参数的值。
- *pcontrol* 是端口 **A** 和 **B** 之间的压差，*pA ̶ pB*。

### 开度参数化

质量流量取决于 **设定压力控制** 和 **开度参数化** 参数的值。

**面积 vs. 压力参数化**

当您将 **设定压力控制** 设置为 `Controlled`，或设置为 `Constant` 且将 **开度参数化** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure` 时，质量流量为

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4,

其中：

- *Cd* 是 **流量系数** 的值。
- *Avalve* 是瞬时阀门开启面积。
- *Aport* 是 **端口 A 和 B 的横截面积** 的值。
- ρ¯ 是平均流体密度。
- *Δp* 是阀门压差 *pA* – *pB*。

临界压差 *Δpcrit* 是与 **临界雷诺数** *Recrit* 相关的压差，即层流与湍流之间的流态转变点：

Δpcrit=πρ¯8Avalve(νRecritCd)2.

*压力损失* 描述了由于面积减小而导致的阀门压力降低。*PR*loss 计算如下：

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport.

*压力恢复* 是由于面积增加而导致的阀门正压力变化。如果您不希望捕获此压力增加，请清除 **压力恢复** 复选框。在这种情况下，*PR*loss 为 1。

当您将 **设定压力控制** 设置为 `Controlled`，或设置为 `Constant` 且将 **开度参数化** 设置为 `Linear - Area vs. pressure` 时，开启面积为

Avalve=p^(Amax−Aleak)+Aleak,

其中：

- *Aleak* 是 **泄漏面积** 参数的值。
- *Amax* 是 **最大开启面积** 参数的值。

当阀门在线性参数化中处于接近开启或接近关闭位置时，您可以通过调整 **平滑因子** 参数来保持仿真中的数值鲁棒性。如果 **平滑因子** 参数非零，模块将在 *pset* 和 *pmax* 之间平滑地饱和控制压力。有关详细信息，请参阅数值平滑。

当您将 **设定压力控制** 设置为 `Constant` 且将 **开度参数化** 设置为 `Tabulated data - Area vs. pressure` 时，模块根据 **压力控制规格** 参数的值，从 **开启面积向量** 参数中相对于 **压差向量** 或 **开启压力（表压）向量** 参数插值 *Avalve*。当平滑因子非零时，模块还使用平滑、归一化的压力进行线性插值和最近邻外推。

**体积流量 vs. 压力参数化**

当您将 **设定压力控制** 设置为 `Constant` 且将 **开度参数化** 设置为 `Tabulated data - Volumetric flow rate vs. pressure` 时，阀门根据用户提供的端口 **A** 和 **B** 之间体积流量和压差的表格数据开启。

质量流量为

m˙=ρ¯KΔp(Δp2+Δpcrit2)1/4,

其中：

- ρ¯ 是平均流体密度。
- Δp=pA−pB。
- Δpcrit=π2ρ¯8CdK(Recritv)2，其中 *Cd* 是流量系数，*Recrit* 是临界雷诺数，*ν* 是运动粘度。在此参数化中，*Cd* 和 *Recrit* 分别固定为 `0.64` 和 `150`。

当模块在表格数据范围内运行时，

K=tablelookup(ΔpTLU,KTLU,Δp,interpolation=linear,extrapolation=nearest),

其中：

- *ΔpTLU* 是 **压降向量** 参数。
- KTLU=V˙TLUΔpTLU，其中 *V˙TLU* 是 **体积流量向量** 参数。

当仿真压力低于 **压降向量** 参数的第一个元素时，*K*`=`*KLeak*，

KLeak=V˙TLU(1)|ΔpTLU(1)|,

其中 *V˙TLU(1)* 是 **体积流量向量** 参数的第一个元素。

当仿真压力高于 **压降向量** 参数的最后一个元素时，*K*`=`*KMax*，

KMax=V˙TLU(end)|ΔpTLU(end)|,

其中 *V˙TLU(end)* 是 **体积流量向量** 参数的最后一个元素。

### 质量守恒

模块通过阀门守恒质量，使得

m˙A+m˙B=0.

其中 m˙ 是通过由 **A** 或 **B** 下标指示的端口进入阀门的质量流量。

### 开启动态特性

当您将 **开启动态特性** 设置为 `On` 时，模块引入控制压力滞后，并用动态控制压力 *pdyn* 替换 *pcontrol*。模块根据 **开启时间常数** 参数 *τ* 计算动态控制压力

p˙dyn=pcontrol−pdynτ.

默认情况下，模块清除 **开启动态特性** 复选框。

稳态动态特性由与阀门开启相同的参数化设定，并基于控制压力 *p*control。非零的 **平滑因子** 可以在节流孔处于接近关闭或接近开启位置时提供额外的数值稳定性。

### 故障

要对故障建模，请在 **故障** 部分中，单击要建模的故障旁边的 **添加故障** 超链接。使用故障参数指定故障属性。有关故障建模的详细信息，请参阅 Simscape 故障简介。

**故障时的开启面积** 参数有三个故障选项：

- `Closed` — 阀门冻结在其最小值，具体取决于 **开度参数化** 参数：

  - 当您将 **开度参数化** 设置为 `Linear - Area vs. pressure` 时，阀门面积冻结在 **泄漏面积** 参数处。
  - 当您将 **开度参数化** 设置为 `Tabulated data - Area vs. pressure` 时，阀门面积冻结在 **开启面积向量** 参数的第一个元素处。
- `Open` — 阀门冻结在其最大值，具体取决于 **开度参数化** 参数：

  - 当您将 **开度参数化** 设置为 `Linear - Area vs. pressure` 时，阀门面积冻结在 **最大开启面积** 参数处。
  - 当您将 **节流孔参数化** 设置为 `Tabulated data - Area vs. pressure` 时，阀门面积冻结在 **开启面积向量** 参数的最后一个元素处。
- `Maintain last value` — 阀门面积冻结在触发发生时的阀门开启面积处。

由于阀门面积极值处的数值平滑，模块使用的最小面积大于 **泄漏面积** 参数，最大值小于 **最大节流孔面积** 参数，其比例与 **平滑因子** 参数值成正比。

故障触发后，阀门在仿真的剩余时间内保持在故障面积处。

当您将 **开度参数化** 设置为 `Tabulated data - Volumetric flow rate vs. pressure` 时，故障选项由通过阀门的体积流量定义：

- `Closed` — 阀门停止在与 **体积流量向量** 参数和 **压降向量** 参数的第一个元素相关的质量流量处：

  m˙=KLeakρ¯Δp.
- `Open` — 阀门停止在与 **体积流量向量** 参数和 **压降向量** 参数的最后一个元素相关的质量流量处：

  m˙=KMaxρ¯Δp
- `Maintain at last value` — 阀门停止在触发发生时的质量流量和压差处：

  m˙=KLastρ¯Δp,

其中

KLast=|m˙|ρ¯|Δp|.

### 预定义参数化

您可以使用预先参数化的制造数据填充该模块，从而对特定供应商组件进行建模。

要加载预定义参数化：

1. 在模块对话框中，点击 **Selected part** 旁边的“<click to select>”超链接。
2. 将打开 Block Parameterization Manager 窗口。从菜单中选择一个部件，然后点击 **Apply all**。您可以使用 **Manufacturer** 下拉菜单缩小选择范围。
3. 您可以关闭 **Block Parameterization Manager** 菜单。该模块现在具有您指定的参数化。
4. 您可以通过在 Block Parameterization Manager 窗口中选择一个部件并查看 **Compare selected part with block** 部分中的数据，将当前参数设置与特定供应商组件进行比较。

**注意**

预定义模块参数化使用可用的数据源来提供参数值。该模块对缺失数据采用工程判断和简化假设进行替代。因此，仿真行为与实际物理行为之间可能会出现一些偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化您的组件模型。

要了解更多信息，请参阅预参数化组件列表。
