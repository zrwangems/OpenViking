---
type: simulink-block
title: 'Pressure Relief Valve (IL)'
family: 'isothermal-liquid'
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

### 守恒

### **A** — 液体端口 等温液体

阀门的入口或出口点。

### **B** — 液体端口 等温液体

阀门的入口或出口点。
### 输入

### **Ps** — 设定压力信号 物理信号

用于受控阀门操作的变信号设定压力。

#### 依赖关系

要启用此端口，请将 **Set pressure control** 设置为 `Controlled`。

## 参数

### 参数

### **Set pressure control** — 阀门操作方式 `Constant` (default) | `Controlled`

阀门操作方式。`Constant` 阀门在固定压力调节范围内线性开启，或根据您提供的表格式压力和开口面积数据开启。`Controlled` 阀门根据端口 **Ps** 处的可变设定压力信号在固定压力调节范围内开启。

### **Opening parameterization** — 对阀门恒定开启或关闭建模的方法 `Linear - Area vs. pressure` (default) | `Tabulated data - Area vs. pressure` | `Tabulated data - Volumetric flow rate vs. pressure`

对阀门开启或关闭建模的方法。阀门开度可以线性参数化，也可以通过将面积与压差关联的值表参数化。

### **Opening pressure specification** — 用于阀门控制的压差 `Pressure differential` (default) | `Pressure at port A`

用于阀门控制的压差。选择 `Pressure differential` 会将端口 **A** 和 **B** 之间的压差设置为压力控制的触发条件。选择 `Pressure at port A` 会将端口 **A** 处的表压，或端口 **A** 处压力与大气压力之差，设置为压力控制的触发条件。

### **Set pressure (gauge)** — 阈值压力 `0.1` MPa (default) | positive scalar

当 **Pressure control specification** 相对于端口 **A** 时，超过此表压将触发阀门操作。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，并将 **Pressure control specification** 设置为 `Pressure at port A`。

### **Set pressure differential** — 阈值压力 `0` MPa (default) | positive scalar

超过此压力将触发阀门操作。当 **Pressure control specification** 相对于端口 **A** 和 **B** 之间的压差时，这是设定压力。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，并将 **Pressure control specification** 设置为 `Pressure differential`。

### **Pressure regulation range** — 阀门操作压力范围 `0.1 MPa` (default) | positive scalar

阀门操作范围。阀门在设定压力值处开始开启，并在 *pmax*（压力调节范围的终点）处完全开启，其中 *pmax = pset + prange*。

#### 依赖关系

要启用此参数，请设置

- **Set pressure control** 为 `Controlled`
- **Set pressure control** 为 `Constant`，并将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`

### **Maximum opening area** — 完全开启阀门的面积 `1e-4` m^2 (default) | positive scalar

阀门完全打开位置时的横截面积。

#### 依赖关系

要启用此参数，请设置以下任一项：

- **Set pressure control** 为 `Controlled`
- **Set pressure control** 为 `Constant`，并将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`

### **Leakage area** — 完全关闭位置时的阀门间隙面积 `1e-10` m^2 (default) | positive scalar

阀门处于完全关闭位置时所有间隙的总和。任何小于此值的面积都保持为指定的泄漏面积。这通过保持流动连续性来帮助提高数值稳定性。

#### 依赖关系

要启用此参数，请设置以下任一项：

- **Set pressure control** 为 `Controlled`。
- **Set pressure control** 为 `Constant`，并将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`

### **Opening pressure (gauge) vector** — 用于表格化参数化的压差值 `[0.2 : 0.2 : 1.2]` MPa (default) | 1-by-*n* vector

用于阀门开口面积表格化参数化的压差值向量。向量元素必须与 **Opening area vector** 参数中的元素一一对应。元素按升序排列，且必须大于 0。表数据点之间采用线性插值。

此参数的第一个元素是阀门的压力设定值，此时阀门开始开启。最后一个元素是最大压力，此时阀门完全开启。两者之差是阀门的压力调节范围。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，将 **Opening parameterization** 设置为 `Tabulated data - Area vs. pressure`，并将 **Opening pressure specification** 设置为 `Pressure differential`。

### **Pressure differential vector** — 用于表格化参数化的压差值 `[0.2 : 0.2 : 1.2]` MPa (default) | 1-by-*n* vector

用于阀门开口面积表格化参数化的压差值向量。向量元素必须与 **Opening area vector** 参数中的元素一一对应。元素按升序排列，且必须大于 0。表数据点之间采用线性插值。

此参数的第一个元素是阀门的压力设定值，此时阀门开始开启。最后一个元素是最大压力，此时阀门完全开启。两者之差是阀门的压力调节范围。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，并设置

- **Opening parameterization** 为 `Tabulated data - Volumetric flow rate vs. pressure`，或
- **Opening parameterization** 为 `Tabulated data - Area vs. pressure`，并将 **Opening pressure specification** 设置为 `Pressure differential`。

### **Volumetric flow rate vector** — 用于表格数据参数化的体积流量向量 `[1e-09, 3.6e-05, 8.9e-05, .00015, .00023, .00031]` (default) | 1-by-*n* vector

用于阀门开度表格化参数化的体积流量值向量。此向量必须与 **Pressure drop vector** 参数的元素数量相同。向量元素必须按升序排列。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### **Opening area vector** — 用于表格化参数化的阀门开口面积 `[1e-10, 2e-06, 4e-06, 6e-06, 8e-06, 1e-05]`m^2 (default) | 1-by-*n* vector

用于阀门开口面积表格化参数化的阀门开口面积向量。向量元素必须与 **Pressure differential vector** 参数中的元素一一对应。元素按升序排列，且必须大于 0。表数据点之间采用线性插值。

#### 依赖关系

要启用此参数，请将 **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Tabulated data - Area vs. pressure`。

### **Cross-sectional area at ports A and B** — 阀门入口或出口处的面积 `inf` m^2 (default) | positive scalar

入口和出口端口 **A** 和 **B** 处的横截面积。这些面积用于压力-流量方程，以确定通过阀门的质量流量。

### **Discharge coefficient** — 流量系数 `0.64` (default) | positive scalar

用于计入理论流动中排放损失的修正因子。Simscape™ Fluids™ 中阀门的默认流量系数为 0.64。

### **Critical Reynolds number** — 层流的上限雷诺数 `150` (default) | positive scalar

通过阀门的层流的雷诺数上限。

### **Smoothing factor** — 数值平滑因子 `0.01` (default) | positive scalar

连续平滑因子，当阀门处于接近开启或接近关闭位置时，为流量响应引入一层渐变变化。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Pressure recovery** — 是否考虑面积扩大中的压力升高 `off` (default) | `on`

用于考虑流体从较小横截面积区域流向较大横截面积区域时的压力升高。清除 **Pressure recovery** 复选框时，不会捕获此压力升高。

### **Opening dynamics** — 是否考虑流量对阀门开启的响应 `off` (default) | `on`

是否考虑因阀门开启而对流体系统造成的瞬态影响。选择 **Opening dynamics** 会通过在流量响应中引入一阶滞后来近似开启条件。**Opening time constant** 也会影响建模的开启动态。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`。

### **Opening time constant** — 阀门开启时间常数 `0.1` s (default) | positive scalar

用于捕获阀门从一个位置开启或关闭到另一位置时流体达到稳态所需时间的常数。此参数会影响建模的开启动态。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure`，并选择 **Opening dynamics**。

### 故障

### **Pressure Relief Valve Area fault** — 对开口面积故障建模的选项 `Add fault`

用于在模块中对阀门面积故障建模的选项。要添加故障，请单击 **Add fault** 超链接。发生故障时，通常由开口参数化设置的阀门面积将根据 **Opening area when faulted** 参数中指定的值设置。

### **Opening area when faulted** — 故障阀门特性 `Closed` (default) | `Open` | `Maintain last value`

故障阀门类型。您可以选择阀门在开启、关闭或故障触发时的面积处卡住。

#### 依赖关系

要启用此参数，请单击 **Add fault** 超链接。

## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Pressure Control Valves

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2024a：使用 Simscape 故障接口对故障建模

Pressure Relief Valve (IL) 模块现在支持 Simscape 故障接口。要了解更多信息，请参阅 Simscape 故障简介。

### R2022b：访问预参数化模块选项

模块支持预参数化选项。供应商包括 Daikin、Kawasaki Heavy Industries、Parker 和 Yuken。

## 描述

等温液体网络中的泄压阀

Pressure Relief Valve (IL) 模块表示等温液体网络中的泄压阀。当压力小于指定值时，阀门保持关闭。当达到或超过此压力时，阀门开启。该设定压力要么是阀门两端（端口 **A** 和 **B** 之间）的阈值压差，要么是端口 **A** 与大气压力之间的阈值压差。有关基于流体系统中其他元件的压力控制，请参阅 Pressure Compensator Valve (IL) 模块。

### 压力控制

对于线性预参数化，控制阀门开口面积的归一化压力 p^ 取决于 **Set pressure control** 参数的值。

当您将 **Set pressure control** 设置为 `Constant`，并将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 时，归一化压力为

p^=pcontrol-psetpmax-pset,

其中：

- *pcontrol* 是控制压力。当您将 **Opening pressure specification** 设置为 `Pressure differential` 时，控制压力为 *pA ̶ pB*。当您将 **Opening pressure specification** 设置为 `Pressure at port A` 时，控制压力为端口 **A** 处压力与大气压力之差。
- *pset* 是设定压力。当 **Opening pressure specification** 为 `Pressure differential` 时，*pset* 是 **Set pressure differential** 参数的值。当 **Opening pressure specification** 为 `Pressure at port A` 时，*pset* 是 **Set pressure (gauge)** 参数的值。
- *pmax* 是压力调节范围的最大值，*pmax = pset + prange*，其中 *prange* 是 **Pressure regulation range** 参数的值。

当您将 **Set pressure control** 设置为 `Controlled` 时，归一化压力为

p^=pcontrol-pspmax-ps,

其中：

- *ps* 是端口 **Ps** 处信号的值。
- *pmax = ps + prange*，其中 *prange* 是 **Pressure regulation range** 参数的值。
- *pcontrol* 是端口 **A** 和 **B** 之间的压差，*pA ̶ pB*。

### 开启参数化

质量流量取决于 **Set pressure control** 和 **Opening parameterization** 参数的值。

**面积 vs. 压力参数化**

当您将 **Set pressure control** 设置为 `Controlled`，或设置为 `Constant` 并将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure` 时，质量流量为

m˙=CdAvalve2ρ¯PRloss(1−(AvalveAport)2)Δp[Δp2+Δpcrit2]1/4,

其中：

- *Cd* 是 **Discharge coefficient** 的值。
- *Avalve* 是瞬时阀开启面积。
- *Aport* 是 **Cross-sectional area at ports A and B** 的值。
- ρ¯ 是平均流体密度。
- *Δp* 是阀压差 *pA* – *pB*。

临界压差 *Δpcrit* 是与 **Critical Reynolds number** 相关联的压差，*Recrit* 是层流与湍流之间的流态转捩点：

Δpcrit=πρ¯8Avalve(νRecritCd)2.

*Pressure loss* 描述由于面积减小而导致阀内压力降低。*PR*loss 计算如下：

PRloss=1−(AvalveAport)2(1−Cd2)−CdAvalveAport1−(AvalveAport)2(1−Cd2)+CdAvalveAport.

*Pressure recovery* 是由于面积增加而导致阀内压力正向变化。如果您不希望捕捉此压力增加，请清除 **Pressure recovery** 复选框。在这种情况下，*PR*loss 为 1。

当您将 **Set pressure control** 设置为 `Controlled`，或设置为 `Constant` 并将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 时，开启面积为

Avalve=p^(Amax−Aleak)+Aleak,

其中：

- *Aleak* 是 **Leakage area** 参数的值。
- *Amax* 是 **Maximum opening area** 参数的值。

当阀在线性参数化中处于接近开启或接近关闭位置时，您可以通过调整 **Smoothing factor** 参数来维持仿真中的数值稳健性。如果 **Smoothing factor** 参数非零，模块会在 *pset* 和 *pmax* 之间平滑饱和控制压力。有关详细信息，请参阅 Numerical Smoothing。

当您将 **Set pressure control** 设置为 `Constant` 并将 **Opening parameterization** 设置为 `Tabulated data - Area vs. pressure` 时，模块根据 **Pressure control specification** 参数的值，从 **Opening area vector** 参数中相对于 **Pressure differential vector** 或 **Opening pressure (gauge) vector** 参数插值 *Avalve*。当 smoothing factor 非零时，模块还使用平滑后的归一化压力，采用线性插值和最近外推法。

**体积流量 vs. 压力参数化**

当您将 **Set pressure control** 设置为 `Constant` 并将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure` 时，阀根据用户提供的端口 **A** 和 **B** 之间的体积流量与压差的表格数据开启。

质量流量为

m˙=ρ¯KΔp(Δp2+Δpcrit2)1/4,

其中：

- ρ¯ 是平均流体密度。
- Δp=pA−pB.
- Δpcrit=π2ρ¯8CdK(Recritv)2, 其中 *Cd* 是流量系数，*Recrit* 是临界雷诺数，*ν* 是运动黏度。在此参数化中，*Cd* 和 *Recrit* 分别固定为 `0.64` 和 `150`。

当模块在表格数据的限值内运行时，

K=tablelookup(ΔpTLU,KTLU,Δp,interpolation=linear,extrapolation=nearest),

其中：

- *ΔpTLU* 是 **Pressure drop vector** 参数。
- KTLU=V˙TLUΔpTLU, 其中 *V˙TLU* 是 **Volumetric flow rate vector** 参数。

当仿真压力低于 **Pressure drop vector** 参数的第一个元素时，*K*`=`*KLeak*，

KLeak=V˙TLU(1)|ΔpTLU(1)|,

其中 *V˙TLU(1)* 是 **Volumetric flow rate vector** 参数的第一个元素。

当仿真压力升高到 **Pressure drop vector** 参数的最后一个元素以上时，*K*`=`*KMax*，

KMax=V˙TLU(end)|ΔpTLU(end)|,

其中 *V˙TLU(end)* 是 **Volumetric flow rate vector** 参数的最后一个元素。

### 质量守恒

模块通过阀守恒质量，使得

m˙A+m˙B=0.

其中 m˙ 是通过 **A** 或 **B** 下标所指示端口流入阀的质量流量。

### 开启动力学

当您将 **Opening dynamics** 设置为 `On` 时，模块会引入控制压力滞后，并用动态控制压力 *pdyn* 替换 *pcontrol*。模块基于 **Opening time constant** 参数 *τ* 计算动态控制压力

p˙dyn=pcontrol−pdynτ.

默认情况下，模块清除 **Opening dynamics** 复选框。

稳态动力学由与阀开启相同的参数化设置，并基于控制压力 *p*control。当节流孔处于接近关闭或接近开启位置时，非零 **Smoothing factor** 可以提供额外的数值稳定性。

### 故障

要对故障建模，请在 **Faults** 部分中，单击您要建模的故障旁边的 **Add fault** 超链接。使用故障参数指定故障属性。有关故障建模的详细信息，请参阅 Introduction to Simscape Faults。

**Opening area when faulted** 参数有三个故障选项：

- `Closed` — 阀冻结在其最小值，具体取决于 **Opening parameterization** 参数：

  - 当您将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 时，阀面积冻结在 **Leakage area** 参数处。
  - 当您将 **Opening parameterization** 设置为 `Tabulated data - Area vs. pressure` 时，阀面积冻结在 **Opening area vector** 参数的第一个元素处。
- `Open` — 阀冻结在其最大值，具体取决于 **Opening parameterization** 参数：

  - 当您将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 时，阀面积冻结在 **Maximum opening area** 参数处。
  - 当您将 **Orifice parameterization** 设置为 `Tabulated data - Area vs. pressure` 时，阀面积冻结在 **Opening area vector** 参数的最后一个元素处。
- `Maintain last value` — 触发发生时，阀面积冻结在阀开启面积。

由于阀面积极值处的数值平滑，模块使用的最小面积大于 **Leakage area** 参数，最大面积小于 **Maximum orifice area** 参数，其比例与 **Smoothing factor** 参数值成正比。

故障触发后，阀在仿真的剩余时间内保持故障面积不变。

当您将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure` 时，故障选项由通过阀的体积流量定义：

- `Closed` — 阀停止在与 **Volumetric flow rate vector** 参数和 **Pressure drop vector** 参数的第一个元素相关联的质量流量处：

  m˙=KLeakρ¯Δp.
- `Open` — 阀停止在与 **Volumetric flow rate vector** 参数和 **Pressure drop vector** 参数的最后一个元素相关联的质量流量处：

  m˙=KMaxρ¯Δp
- `Maintain at last value` — 触发发生时，阀停止在质量流量和压差处：

  m˙=KLastρ¯Δp,

其中

KLast=|m˙|ρ¯|Δp|.

### 预定义参数化

您可以使用预参数化制造数据填充该模块，从而对特定供应商组件进行建模。

要加载预定义参数化：

1. 在模块对话框中，在 **Selected part** 旁边，单击模块对话框设置中 **Selected part** 旁边的 "<click to select>" 超链接。
2. Block Parameterization Manager 窗口打开。从菜单中选择一个零件，然后单击 **Apply all**。您可以使用 **Manufacturer** 下拉菜单缩小选择范围。
3. 您可以关闭 **Block Parameterization Manager** 菜单。该模块现在具有您指定的参数化。
4. 您可以在 Block Parameterization Manager 窗口中选择一个零件，并查看 **Compare selected part with block** 部分中的数据，从而将当前参数设置与特定供应商组件进行比较。

**注意**

预定义模块参数化使用可用的数据源提供参数值。对于缺失数据，模块会以工程判断和简化假设替代。因此，仿真行为与实际物理行为之间预期会有一定偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化您的组件模型。

要了解更多信息，请参阅 List of Pre-Parameterized Components。
