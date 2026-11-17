---
type: simulink-block
title: 'Counterbalance Valve (TL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Thermal Liquid / Valves & Orifices / Pressure Control Valves'
documentation_page: 'counterbalancevalvetl'
documentation_source_path: 'ref/counterbalancevalvetl.html'
language: zh-CN
chinese_source: worker-translation
---

# Counterbalance Valve (TL)

## 端口
```yaml
ports:
- name: L
  summary: 流体负载热液体
  direction: conserving
- name: B
  summary: 背压热液体
  direction: conserving
- name: P
  summary: 先导压力端口热液体
  direction: conserving
```

### 守恒端口

### **L** — 流体负载热液体

与负载相关联的热液体守恒端口。

### **B** — 背压热液体

与阀门背压相关联的热液体守恒端口。

### **P** — 先导压力端口热液体

与先导压力端口相关联的热液体守恒端口。
## 参数
```yaml
parameters:
- name: Opening parameterization
  summary: 开度参数化 Linear - Area vs. pressure（默认）| Tabulated data - Area vs. pressure | Tabulated data - Volumetric flow rate
    vs. pressure
  group: 模型参数化
- name: Set pressure differential
  summary: 初始弹簧压缩压力 5 MPa（默认）| 非负标量
  group: 模型参数化
- name: Pressure differential vector
  summary: '溢流级压降值 5 : 0.2 : 6 MPa（默认）| 1×*n* 向量'
  group: 模型参数化
- name: Opening area vector
  summary: 溢流级开度面积 [1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2（默认）| 1×*n* 向量
  group: 模型参数化
- name: Reference pressure differential vector
  summary: '溢流级压降 5 : 0.2 : 6 MPa（默认）| 向量'
  group: 模型参数化
- name: Reference volumetric flow rate vector
  summary: 通过溢流级的流量 [6.4e-09, .0013, .0027, .0041, .0055, .007] m^3/s（默认）| 向量
  group: 模型参数化
- name: Maximum opening pressure differential
  summary: 溢流阀最大压力 6 MPa（默认）| 正标量
  group: 模型参数化
- name: Maximum opening area
  summary: 溢流级最大开度面积 1e-4 m^2（默认）| 正标量
  group: 模型参数化
- name: Leakage area
  summary: 阀门完全关闭位置时的间隙面积 1e-10 m^2（默认）| 正标量
  group: 模型参数化
- name: Pilot ratio
  summary: 先导面积比 3（默认）| 正标量
  group: 模型参数化
- name: Back pressure ratio
  summary: 背压面积比 4（默认）| 正标量
  group: 模型参数化
- name: Cross-sectional area at ports A and B
  summary: 阀门入口或出口面积 0.01 m^2（默认）| 正标量
  group: 模型参数化
- name: Discharge coefficient
  summary: 流量系数 0.64（默认）| 正标量
  group: 模型参数化
- name: Critical Reynolds number
  summary: 层流的上限雷诺数 150（默认）| 正标量
  group: 模型参数化
- name: Smoothing factor
  summary: 数值平滑因子 0.01（默认）| 正标量
  group: 模型参数化
- name: Opening dynamics
  summary: 是否引入节流孔开启导致的流量滞后 off（默认）| on
  group: 模型参数化
- name: Opening time constant
  summary: 节流孔开启时间常数 0.1 s（默认）| 正标量
  group: 模型参数化
- name: Cracking pressure differential
  summary: 单向阀操作的设定压力 0.01 MPa（默认）| 正标量
  group: 单向阀
- name: Maximum opening pressure differential
  summary: 阀门中的最大压力 0.1 MPa（默认）| 正标量
  group: 单向阀
- name: Maximum opening area
  summary: 最大开度面积 1e-4 m^2（默认）| 正标量
  group: 单向阀
- name: Pressure differential vector
  summary: '单向阀操作的压差 [0.01 : 0.01 : 0.1] MPa（默认）| 1×*n* 向量'
  group: 单向阀
- name: Opening area vector
  summary: 单向阀级开启面积 [1e-10, 1e-05, 2e-05, 3e-05, 4e-05, 5e-05, 6e-05, 7.5e-05, 8.5e-05, .0001] m^2（默认）| 1×*n* 向量
  group: 单向阀
- name: Volumetric flow rate vector
  summary: 单向阀级体积流量 [.000358, .045, .11, .191, .284, .39, .505, .63, .764, .905] .* 1e-3 m^3/s（默认）| 1×*n* 向量
  group: 单向阀
```

### 模型参数化

### **Opening parameterization** — 开度参数化 `Linear - Area vs. pressure`（默认）| `Tabulated data - Area vs. pressure` | `Tabulated data - Volumetric flow rate vs. pressure`

阀门开度的建模方法。当选择 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure` 时，模块将开度面积与控制压力相关联。当选择 `Tabulated data - Volumetric flow rate vs. pressure` 时，模块采用平衡阀的溢流级和单向级的参考流量与压差曲线，其中背压端口和先导端口的压力对应于溢流级参考曲线中的 1 atm。

### **Set pressure differential** — 初始弹簧压缩压力 `5` `MPa`（默认）| 非负标量

提升溢流级的压差。使用此参数调整数据手册提供的设定压力。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Volumetric flow rate vs. pressure`。

### **Pressure differential vector** — 溢流级压降值 `5 : 0.2 : 6` `MPa`（默认）| 1×*n* 向量

溢流级的压差向量。向量元素必须与 **Opening area vector** 参数中的元素一一对应。必须以升序输入元素。此向量定义了控制阀门开启和关闭的控制压力。向量中的第一个元素定义了设定压力，即溢流级刚开始开启时的控制压力。最后一个元素定义了阀门完全开启时的控制压力。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated data - Area vs. pressure`。

### **Opening area vector** — 溢流级开度面积 `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001]` `m^2`（默认）| 1×*n* 向量

溢流级开度面积的向量。向量元素必须与 **Pressure differential vector** 参数中的元素一一对应。按升序列出元素。所有元素必须大于 0。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated data - Area vs. pressure`。

### **Reference pressure differential vector** — 溢流级压降 `5 : 0.2 : 6` `MPa`（默认）| 向量

溢流级压降的向量。向量元素必须与 **Reference volumetric flow rate vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### **Reference volumetric flow rate vector** — 通过溢流级的流量 `[6.4e-09, .0013, .0027, .0041, .0055, .007]` `m^3/s`（默认）| 向量

通过溢流级的流量的向量。向量元素必须与 **Reference pressure differential vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### **Maximum opening pressure differential** — 溢流阀最大压力 `6` `MPa`（默认）| 正标量

溢流阀最大压力。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Maximum opening area** — 溢流级最大开度面积 `1e-4` `m^2`（默认）| 正标量

溢流级节流孔的最大开度面积。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Leakage area** — 阀门完全关闭位置时的间隙面积 `1e-10` `m^2`（默认）| 正标量

阀门处于完全关闭位置时所有间隙的总和。任何小于此值的面积都会饱和到指定的泄漏面积。此值通过保持流动的连续性来增强数值稳定性。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Pilot ratio** — 先导面积比 `3`（默认）| 正标量

先导压力作用面积与负载压力作用面积之比。

### **Back pressure ratio** — 背压面积比 `4`（默认）| 正标量

背压压力作用面积与负载压力作用面积之比。

### **Cross-sectional area at ports A and B** — 阀门入口或出口面积 `0.01` `m^2`（默认）| 正标量

入口和出口端口 **A** 和 **B** 处的横截面积。模块在确定通过阀门的质量流量的压力-流量方程中使用此面积。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

考虑理论流动中排放损失的修正系数。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过阀门的层流的上限雷诺数。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 正标量

连续平滑因子，在阀门接近开启或接近关闭位置时为流量响应引入逐渐变化的层。将此值设置为小于 1 的非零值以提高这些工况下仿真的稳定性。

### **Opening dynamics** — 是否引入节流孔开启导致的流量滞后 `off`（默认）| `on`

是否考虑阀门开启对流体系统的瞬态效应。选择 **Opening dynamics** 通过引入压力响应的一阶滞后来近似开启条件。

当选择此参数时，这些动态特性适用于溢流级而非平衡阀的单向级。

### **Opening time constant** — 节流孔开启时间常数 `0.1` `s`（默认）| 正标量

描述流体在阀门从一个位置开启或关闭到另一个位置时达到稳态条件所需时间的常数。此参数影响建模的开启动态特性。

#### 依赖关系

要启用此参数，请选择 **Opening dynamics**。

### 单向阀

### **Cracking pressure differential** — 单向阀操作的设定压力 `0.01` `MPa`（默认）| 正标量

提升单向阀的压差。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Maximum opening pressure differential** — 阀门中的最大压力 `0.1` `MPa`（默认）| 正标量

阀门最大压力。此参数限制阀门出口处的压力，以在仿真期间保持物理值。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Maximum opening area** — 最大开度面积 `1e-4` `m^2`（默认）| 正标量

负载管路中单向阀的最大开度面积。在内部，此单向阀与溢流级并联。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为 `Linear - Area vs. pressure`。

### **Pressure differential vector** — 单向阀操作的压差 `[0.01 : 0.01 : 0.1]` `MPa`（默认）| 1×*n* 向量

单向阀级的压差向量。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为
`Tabulated data - Area vs. pressure` 或
`Tabulated data - Volumetric flow rate vs.
pressure`。

### **Opening area vector** — 单向阀级开启面积 `[1e-10, 1e-05, 2e-05, 3e-05, 4e-05, 5e-05, 6e-05, 7.5e-05, 8.5e-05, .0001]` `m^2`（默认）| 1×*n* 向量

单向阀级的开启面积向量。向量元素必须与 **Pressure differential
vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为
`Tabulated data - Area vs. pressure`。

### **Volumetric flow rate vector** — 单向阀级体积流量 `[.000358, .045, .11, .191, .284, .39, .505, .63, .764, .905] .* 1e-3` `m^3/s`（默认）| 1×*n* 向量

单向阀级的体积流量向量。此向量的元素必须与 **Pressure differential
vector** 参数中的元素对应。

#### 依赖关系

要启用此参数，请将 **Opening parameterization** 设置为
`Tabulated data - Volumetric flow rate vs.
pressure`。
## 所属库

Simscape / Fluids / Thermal Liquid / Valves & Orifices / Pressure Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

热液体网络中的平衡阀

Counterbalance Valve (TL) 模块表示热液体网络中的平衡压力控制阀。平衡阀常用于高压事件频繁发生的应用中，或需要以生产速度进行高压控制操作的任务中。这些应用包括过载液压或下放悬挂负载等任务。该阀在弹簧、端口 **B** 处的背压以及端口 **L** 处的负载压力之间的力平衡下工作，并响应先导管路压力的变化。当先导压力超过背压时，阀开始打开。

端口 **B** 和 **P** 之间或端口 **L** 和 **P** 之间没有流量。

下图显示了典型平衡阀的剖视图。

### 阀开启

该模块平衡平衡阀的力，使得

ppilotApilot+ploadAload=pbackAback+Fset+kspringxspool，

其中：

- *ppilot* 是端口 **P** 处的压力。
- *pload* 是端口 **L** 处的压力。
- *pback* 是端口 **B** 处的压力。
- *Fset* 是由于弹簧产生的累积力。
- *kspring* 是弹簧常数。
- *xspool* 是溢流级滑阀体的线性位置。该位置相对于未加压的安装位置。

该模块根据 **Pilot ratio** 参数 *Rpilot* 设置压力作用面积 *Apilot*、*Aload* 和 *Aback*，使得

Rpilot=ApilotAload，

并根据 **Back pressure ratio** 参数 *Rback* 设置，使得

Rback=AbackAload。

平衡阀的典型比值为 4:1 或 3:1。

预设力 *Fspring* 表示端口 **B** 处的弹簧预紧力和弹簧力的组合。该力是 *pset*（即 **Set pressure differential** 参数）的函数，使得

Fset=psetAload。

下图显示了 Counterbalance Valve with Test Harness 示例中的示意图，其中压力端口通过作用在具有不同面积的表面上控制阀。箭头显示了由于压力或弹簧力作用在溢流级本体上的力方向。灰色部分表示一个单一的实心体，当溢流级打开时向右移动。当单向阀打开时，它向左移动。

平衡阀示意图，其中负载压力和先导压力向右作用，背压和弹簧向左作用。

### 开启参数化

您可以使用线性数据或表格数据对模块进行参数化。模块的止回阀部分与 Check Valve (IL) 模块的操作完全相同。

**线性参数化**

当您将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 时，模块计算阀开启面积，使得

Avalve=p^(Amax−Aleak)+Aleak。

模块计算归一化控制压力 p^，如下

p^=(pload+ppilotRpilot−pbackRback)−pset(pmax−pset)，

其中 *pmax* 是 **Maximum opening pressure differential** 参数。

归一化止回阀压力为

p^=pcontrol−pcrackingpmax−pcracking，

其中：

- *pcracking* 是 **Cracking pressure differential** 参数。
- *pmax* 是 **Check valve** 部分中的 **Maximum opening pressure differential** 参数。

当阀在线性参数化中处于接近开启或接近关闭位置时，您可以通过调整 **Smoothing factor** 参数来保持仿真中的数值鲁棒性。如果 **Smoothing factor** 参数非零，模块会在 *pcracking* 和 *pmax* 之间平滑地饱和控制压力。有关详细信息，请参阅数值平滑。

**表格面积参数化**

当您将 **Opening parameterization** 设置为 `Tabulated data - Area vs. pressure` 时，模块使用与线性参数化相同的方程，但使用表格数据。表格数据表示面积相对于给定控制压力的关系，其中 *Pcontrol* = *pload* + *pPilotRPilot* - *pBackRBack*。**Pressure differential vector** 参数的第一个元素是设定压力，即溢流级开始开启时的控制压力。最后一个元素定义阀完全开启时的控制压力。

**表格流量参数化**

当您将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure` 时，体积流量方程涉及以下量：

- ρ¯valve 是溢流级流的模拟平均密度。
- *K* 是通过溢流级的流量系数。
- *Δpvalve* 是流动期间溢流级的压降。
- *Δpcrit* 是流动期间溢流级的临界压降。
- *pcontrol* 是模拟控制压力。
- *pcontrol,TLU,Ref* 是内部推导的变化控制压力查找表。
- *pset* 是设定压力差。
- *Recrit* 是 **Critical Reynolds number** 参数。
- *Cd* 是 **Discharge coefficient** 参数。
- *ν* 是运动粘度。
- *KTLU,Ref* 是内部推导的变化流量系数作为阀面积函数的查找表。
- V˙TLU,Ref 是参考体积流量向量。
- *ppilot,Ref*、*pback,Ref*、*pload,Ref* 分别是用户提供的 **Reference volumetric flow rate vector** 参数的先导压力、背压和负载压力。

模块计算溢流级的质量流量，使得

m˙valve=ρ¯valveKΔpvalve(Δpvalve2+Δpcrit2)1/4，

其中：

Δpvalve=pload−pbackΔpcrit=π2ρ¯valve8Cd(Recritυ)K=tablelookup(pcontrol,TLU,Ref,KTLU,Ref,pcontrol,interpolation = linear, extrapolation = nearest)

液体从负载端口流向背压端口。模块在计算 *KTLU,Ref* 后将 *K* 外推到最近点，如下

KTLU,Ref=V˙TLU,RefΔpvalve,TLU,ref，

其中 *Δpvalve,TLU,ref* = *pload,Ref* - *pback,Ref*。模块计算控制压力为

pcontrol=Rpilotppilot+pload−Rbackpback

参考控制向量为

pcontrol,TLU,Ref=Rpilotppilot,Ref+pload,Ref−Rbackpback,Ref+poffset，

其中：

ppilot,Ref=1 atmpback,Ref=1 atmpload,Ref=pback,Ref+Δpvalve,TLU,Ref

模块内部推导 *Δpflow,Ref*，即指定参考曲线中流体流动的压降。模块内部计算 *poffset* 为

poffset=pset−Rpilotppilot,Ref−pload,Ref(1)+Rbackpback,Ref。

该表显示了模块如何根据 **Opening area** 参数设置控制溢流级和止回级的开启面积。

| Opening Parameterization Setting | Relief Stage | Check Stage |
| --- | --- | --- |
| `Linear - Area vs. pressure` |  |  |
| `Tabulated - Area vs. pressure` |  |  |
| `Tabulated - Volumetric flow rate vs. pressure` |  |  |

### 预定义参数化

您可以使用预参数化的制造数据填充模块，从而对特定供应商组件进行建模。

要加载预定义参数化：

1. 在模块对话框中，点击 **Selected part** 旁边的 "<click to select>" 超链接。
2. 打开 Block Parameterization Manager 窗口。从菜单中选择一个部件，然后点击 **Apply all**。您可以使用 **Manufacturer** 下拉菜单缩小选择范围。
3. 您可以关闭 **Block Parameterization Manager** 菜单。模块现在具有您指定的参数化。
4. 您可以通过在 Block Parameterization Manager 窗口中选择一个部件并查看 **Compare selected part with block** 部分中的数据，将当前参数设置与特定供应商组件进行比较。

**注意**

预定义模块参数化使用可用的数据源来提供参数值。模块用工程判断和简化假设替代缺失数据。因此，预期仿真行为与实际物理行为之间会有一些偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化您的组件模型。

要了解更多信息，请参阅预参数化组件列表。

### 假设和限制

- 模块仅在内部排油–外部先导、非通气配置下运行。
- 当您将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure` 时，模块使用体积流量相对于溢流级压降的值来生成参考曲线。模块假设先导端口和背压端口对大气压力开放。
