---
type: simulink-block
title: 'Counterbalance Valve (IL)'
family: 'hydro'
product_id: 'hydro'
product_name: 'Fluids'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Valves & Orifices / Pressure Control Valves'
documentation_page: 'counterbalancevalveil'
documentation_source_path: 'ref/counterbalancevalveil.html'
language: zh-CN
chinese_source: worker-translation
---

# Counterbalance Valve (IL)

## 端口
```yaml
ports:
- name: L
  summary: 液体端口，等温液体
  direction: conserving
- name: B
  summary: 液体端口，等温液体
  direction: conserving
- name: P
  summary: 压力端口，等温液体
  direction: conserving
```

### 守恒端口

### **L** — 液体端口，等温液体

与负载相关联的等温液体守恒端口。

### **B** — 液体端口，等温液体

与阀的背压相关联的等温液体守恒端口。

### **P** — 压力端口，等温液体

先导压力端口。
## 参数
```yaml
parameters:
- name: Opening parameterization
  summary: 开启参数化 Linear - Area vs. pressure（默认）| Tabulated data - Area vs. pressure | Tabulated data - Volumetric flow rate
    vs. pressure
  group: 模型参数化
- name: Set pressure differential
  summary: 初始弹簧压缩压力 5 MPa（默认）| 非负标量
  group: 模型参数化
- name: Pressure differential vector
  summary: '溢流级压降值 5 : 0.2 : 6 MPa（默认）| 1×*n* 向量'
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
  summary: 溢流级最大开启面积 1e-4 m^2（默认）| 正标量
  group: 模型参数化
- name: Leakage area
  summary: 阀处于完全关闭位置时的间隙面积 1e-10 m^2（默认）| 正标量
  group: 模型参数化
- name: Pilot ratio
  summary: 先导面积比 3（默认）| 正标量
  group: 模型参数化
- name: Back pressure ratio
  summary: 背压面积比 4（默认）| 正标量
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
- name: Opening area vector
  summary: 溢流级开启面积 [1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001] m^2（默认）| 1×*n* 向量
  group: 模型参数化
- name: Opening dynamics
  summary: 是否引入由节流孔开启引起的流量滞后 off（默认）| on
  group: 模型参数化
- name: Opening time constant
  summary: 节流孔开启时间常数 0.1 s（默认）| 正标量
  group: 模型参数化
- name: Cracking pressure differential
  summary: 单向阀操作的设定压力 0.01 MPa（默认）| 正标量
  group: 单向阀
- name: Maximum opening pressure differential
  summary: 阀内最大压力 0.1 MPa（默认）| 正标量
  group: 单向阀
- name: Maximum opening area
  summary: 最大开启面积 1e-4 m^2（默认）| 正标量
  group: 单向阀
- name: Pressure differential vector
  summary: '单向阀操作的压差 [0.01 : 0.01 : 0.1] MPa（默认）| 1×*n* 向量'
  group: 单向阀
- name: Opening area vector
  summary: 单向级开启面积 [1e-10, 1e-05, 2e-05, 3e-05, 4e-05, 5e-05, 6e-05, 7.5e-05, 8.5e-05, .0001] m^2（默认）| 1×*n* 向量
  group: 单向阀
- name: Volumetric flow rate vector
  summary: 单向级体积流量 [.000358, .045, .11, .191, .284, .39, .505, .63, .764, .905] .* 1e-3 m^3/s（默认）| 1×*n* 向量
  group: 单向阀
```

### 模型参数化

### **Opening parameterization** — 开启参数化 `Linear - Area vs. pressure`（默认）| `Tabulated data - Area vs. pressure` | `Tabulated data - Volumetric flow rate vs. pressure`

阀开启的建模方法。当您选择 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure` 时，模块将开启面积与控制压力相关联。当您选择 `Tabulated data - Volumetric flow rate vs. pressure` 时，模块采用平衡阀的溢流级和单向级的参考流量与压差曲线，其中背压端口和先导端口的压力对应于溢流级参考曲线中的 1 atm。

### **Set pressure differential** — 初始弹簧压缩压力 `5` `MPa`（默认）| 非负标量

提升溢流级所需的压差。使用此参数调整数据表中提供的设定压力。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Volumetric flow rate vs. pressure`。

### **Pressure differential vector** — 溢流级压降值 `5 : 0.2 : 6` `MPa`（默认）| 1×*n* 向量

溢流级的压差向量。向量元素必须与 **Opening area vector** 参数中的元素一一对应。必须以升序输入元素。此向量定义了控制阀开启和关闭的控制压力。向量中的第一个元素定义了设定压力，即溢流级刚开始开启时的控制压力。最后一个元素定义了阀完全开启时的控制压力。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Tabulated data - Area vs. pressure`。

### **Reference pressure differential vector** — 溢流级压降 `5 : 0.2 : 6` `MPa`（默认）| 向量

溢流级的压降向量。向量元素必须与 **Reference volumetric flow rate vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### **Reference volumetric flow rate vector** — 通过溢流级的流量 `[6.4e-09, .0013, .0027, .0041, .0055, .007]` `m^3/s`（默认）| 向量

通过溢流级的流量向量。向量元素必须与 **Reference pressure differential vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### **Maximum opening pressure differential** — 溢流阀最大压力 `6` `MPa`（默认）| 正标量

溢流阀的最大压力。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Linear - Area vs. pressure`。

### **Maximum opening area** — 溢流级最大开启面积 `1e-4` `m^2`（默认）| 正标量

溢流级节流孔的最大开启面积。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Linear - Area vs. pressure`。

### **Leakage area** — 阀处于完全关闭位置时的间隙面积 `1e-10` `m^2`（默认）| 正标量

阀处于完全关闭位置时所有间隙的总和。任何小于此值的面积都会被饱和到指定的泄漏面积。此值通过保持流动的连续性来增强数值稳定性。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Linear - Area vs. pressure`。

### **Pilot ratio** — 先导面积比 `3`（默认）| 正标量

先导压力作用面积与负载压力作用面积之比。

### **Back pressure ratio** — 背压面积比 `4`（默认）| 正标量

背压压力作用面积与负载压力作用面积之比。

### **Discharge coefficient** — 流量系数 `0.64`（默认）| 正标量

用于修正理论流量中排放损失的修正系数。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认）| 正标量

通过阀的层流的上限雷诺数。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认）| 正标量

连续平滑因子，在阀接近开启或接近关闭位置时为流量响应引入逐渐变化的层。将此值设置为小于 1 的非零值可提高这些工况下仿真的稳定性。

### **Opening area vector** — 溢流级开启面积 `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001]` `m^2`（默认）| 1×*n* 向量

溢流级开启面积的向量。向量元素必须与 **Pressure differential vector** 参数中的元素一一对应。按升序列出元素。所有元素必须大于 0。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Tabulated data - Area vs. pressure`。

### **Opening dynamics** — 是否引入由节流孔开启引起的流量滞后 `off`（默认）| `on`

是否考虑因阀开启而对流体系统产生的瞬态效应。选择 **Opening dynamics** 通过引入压力响应的一阶滞后来近似开启条件。**Opening time constant** 参数也会影响所建模的开启动态特性。

启用时，这些动态特性适用于平衡阀的溢流级，而不适用于单向级。

### **Opening time constant** — 节流孔开启时间常数 `0.1` `s`（默认）| 正标量

描述流体在阀从一个位置开启或关闭到另一个位置时达到稳态条件所需时间的常数。此参数影响所建模的开启动态特性。

#### 依赖关系

要启用此参数，请选择 **Opening dynamics**。

### 单向阀

### **Cracking pressure differential** — 单向阀操作的设定压力 `0.01` `MPa`（默认）| 正标量

提升单向阀所需的压差。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Linear - Area vs. pressure`。

### **Maximum opening pressure differential** — 阀内最大压力 `0.1` `MPa`（默认）| 正标量

阀的最大压力。此参数限制阀出口处的压力，以在仿真期间保持物理值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Linear - Area vs. pressure`。

### **Maximum opening area** — 最大开启面积 `1e-4` `m^2`（默认）| 正标量

负载管路中单向阀的最大开启面积。在内部，此单向阀与溢流级并联。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Linear - Area vs. pressure`。

### **Pressure differential vector** — 单向阀操作的压差 `[0.01 : 0.01 : 0.1]` `MPa`（默认）| 1×*n* 向量

单向阀级的压差向量。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Tabulated data - Area vs. pressure` 或 `Tabulated data - Volumetric flow rate vs. pressure`。

### **Opening area vector** — 单向级开启面积 `[1e-10, 1e-05, 2e-05, 3e-05, 4e-05, 5e-05, 6e-05, 7.5e-05, 8.5e-05, .0001]` `m^2`（默认）| 1×*n* 向量

单向阀级的开启面积向量。向量元素必须与 **Pressure differential vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Tabulated data - Area vs. pressure`。

### **Volumetric flow rate vector** — 单向级体积流量 `[.000358, .045, .11, .191, .284, .39, .505, .63, .764, .905] .* 1e-3` `m^3/s`（默认）| 1×*n* 向量

单向阀级的体积流量向量。此向量的元素必须与 **Pressure differential vector** 参数中的元素对应。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。
## 所属库

Simscape / Fluids / Isothermal Liquid / Valves & Orifices / Pressure Control Valves

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

### R2022b：开启参数化选项包括体积流量

您可以将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。此选项启用以下新参数：

- **Set pressure differential**
- **Reference pressure differential vector**
- **Reference volumetric flow rate vector**
- **Volumetric flow rate vector**

为提高清晰度：

- `Linear` 选项已重命名为 `Linear - Area vs. pressure`。
- `Tabulated` 选项已重命名为 `Tabulated data - Area vs. pressure`

### R2022b：访问预参数化模块选项

您现在可以从可用的预参数化选项中进行选择。可用的制造商为 Rexroth Bosch Group 和 Sun Hydraulics。

## 描述

等温液体系统中的高压调节阀

Counterbalance Valve (IL) 模块表示等温液体网络中的平衡压力控制阀。平衡阀常用于高压事件频繁发生的应用中，或需要以生产速度进行高压控制操作的任务中。这包括过载液压或下放悬挂负载等任务。该阀在弹簧、端口 **B** 处的背压和端口 **L** 处的负载压力之间的力平衡下工作。该阀响应先导管路压力的变化。当先导压力超过背压时，阀开始开启。

端口 **B** 和 **P** 之间或端口 **L** 和 **P** 之间没有流动。

下图显示了典型的平衡阀剖视图。

### 阀开启

模块平衡平衡阀的力，使得

ppilotApilot+ploadAload=pbackAback+Fset+kspringxspool，

其中：

- *ppilot* 是端口 **P** 处的压力。
- *pload* 是端口 **L** 处的压力。
- *pback* 是端口 **B** 处的压力。
- *Fset* 是由于弹簧产生的累积力。
- *kspring* 是弹簧常数。
- *xspool* 是溢流级阀芯体的线性位置。此位置相对于未加压的安装位置。

模块根据 **Pilot ratio** 参数 *Rpilot* 设置压力作用面积 *Apilot*、*Aload* 和 *Aback*，使得

Rpilot=ApilotAload，

并根据 **Back pressure ratio** 参数 *Rback* 设置

Rback=AbackAload。

平衡阀的典型比值为 4:1 或 3:1。

预设力 *Fspring* 表示组合的弹簧预紧力和端口 **B** 处的弹簧力。此力是 *pset*（即 **Set pressure differential** 参数）的函数，使得

Fset=psetAload。

下图显示了 Counterbalance Valve with Test Harness 示例中的示意图，其中压力端口通过作用于具有不同面积的表面来控制阀。箭头显示了由于压力或弹簧力作用在溢流级阀体上的力方向。灰色部分表示一个单一的实心体，当溢流级开启时向右移动。单向阀开启时向左移动。

平衡阀示意图，其中负载压力和先导压力向右作用，背压和弹簧向左作用。

### 开启参数化

该模块接受线性或表格化参数化。模块中的单向阀部分与 Check Valve (IL) 模块的运行方式完全相同。

**线性参数化**

当您将 **Opening parameterization** 设置为 `Linear - Area vs. pressure` 时，模块计算阀口开启面积，使得

Avalve=p^(Amax−Aleak)+Aleak。

模块计算归一化控制压力 p^ 为

p^=(pload+ppilotRpilot−pbackRback)−pset(pmax−pset)，

其中 *pmax* 是 **Maximum opening pressure differential** 参数。

归一化单向阀压力为

p^=pcontrol−pcrackingpmax−pcracking，

其中：

- *pcracking* 是 **Cracking pressure differential** 参数。
- *pmax* 是单向阀 **Maximum opening pressure differential** 参数。

当阀在线性参数化中处于接近开启或接近关闭位置时，您可以通过调整 **Smoothing factor** 参数来保持仿真中的数值鲁棒性。如果 **Smoothing factor** 参数非零，模块会在 *pcracking* 和 *pmax* 之间平滑地饱和控制压力。有关详细信息，请参阅 Numerical Smoothing。

**表格化面积参数化**

当您将 **Opening parameterization** 设置为 `Tabulated data - Area vs. pressure` 时，模块使用与线性参数化相同的方程，但使用表格化数据。表格化数据表示相对于给定控制压力的面积，其中 *Pcontrol* = *pload* + *pPilotRPilot* - *pBackRBack*。**Pressure differential vector** 参数的第一个元素是设定压力，即溢流级开始开启时的控制压力。最后一个元素定义阀完全开启时的控制压力。

**表格化流量参数化**

当您将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure` 时，体积流量方程涉及以下量：

- ρ¯valve 是溢流级流量的仿真平均密度。
- *K* 是通过溢流级的流量系数。
- *Δpvalve* 是流动期间溢流级两端的压降。
- *Δpcrit* 是流动期间溢流级两端的临界压降。
- *pcontrol* 是仿真控制压力。
- *pcontrol,TLU,Ref* 是内部推导的变化控制压力查找表。
- *pset* 是设定压力差。
- *Recrit* 是 **Critical Reynolds number** 参数。
- *Cd* 是 **Discharge coefficient** 参数。
- *ν* 是运动粘度。
- *KTLU,Ref* 是内部推导的变化流量系数查找表，作为阀面积的函数。
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

并计算参考控制向量为

pcontrol,TLU,Ref=Rpilotppilot,Ref+pload,Ref−Rbackpback,Ref+poffset，

其中：

ppilot,Ref=1 atmpback,Ref=1 atmpload,Ref=pback,Ref+Δpvalve,TLU,Ref

模块内部推导 *Δpflow,Ref*，即指定参考曲线中流体流动的压降。模块内部计算 *poffset* 为

poffset=pset−Rpilotppilot,Ref−pload,Ref(1)+Rbackpback,Ref。

该表显示了模块如何根据 **Opening area** 参数设置控制溢流级和单向阀级的开启面积。

| Opening parameterization | Relief stage | Check stage |
| --- | --- | --- |
| `Linear - Area vs. pressure` |  |  |
| `Tabulated - Area vs. pressure` |  |  |
| `Tabulated - Volumetric flow rate vs. pressure` |  |  |

### 预定义参数化

您可以使用预参数化的制造数据填充模块，这允许您对特定供应商组件进行建模。

要加载预定义参数化：

1. 在模块对话框中，在 **Selected part** 旁边，单击模块对话框设置中 **Selected part** 旁边的“<click to select>”超链接。
2. 将打开 Block Parameterization Manager 窗口。从菜单中选择一个部件，然后单击 **Apply all**。您可以使用 **Manufacturer** 下拉菜单缩小选择范围。
3. 您可以关闭 **Block Parameterization Manager** 菜单。模块现在具有您指定的参数化。
4. 您可以通过在 Block Parameterization Manager 窗口中选择一个部件并查看 **Compare selected part with block** 部分中的数据，将当前参数设置与特定供应商组件进行比较。

**注意**

预定义模块参数化使用可用的数据源来提供参数值。模块用工程判断和简化假设替代缺失数据。因此，预期仿真行为与实际物理行为之间会有一些偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化您的组件模型。

要了解更多信息，请参阅 List of Pre-Parameterized Components。
