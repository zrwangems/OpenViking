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

### 守恒

### **L** — 液体端口等温液体

与负载关联的等温液体守恒端口。

### **B** — 液体端口等温液体

与阀的背压关联的等温液体守恒端口。

### **P** — 压力端口等温液体

先导压力端口。

## 参数

### 模型参数化

### **Opening parameterization** — 开启参数化 `Linear - Area vs. pressure`（默认） | `Tabulated data - Area vs. pressure` | `Tabulated data - Volumetric flow rate vs. pressure`

对阀开启进行建模的方法。当您选择 `Linear - Area vs. pressure` 或 `Tabulated data - Area vs. pressure` 时，模块将开启面积与控制压力关联。当您选择 `Tabulated data - Volumetric flow rate vs. pressure` 时，模块采用平衡阀泄压级和单向阀级的参考流量与压差曲线，其中在泄压级的参考曲线中，背压端口和先导端口处的压力对应于 1 atm。

### **Set pressure differential** — 初始弹簧压缩压力 `5` `MPa`（默认） | nonnegative scalar

使泄压级抬起的压差。使用此参数调整数据表中提供的设定压力。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Linear - Area vs. pressure` 或 `Tabulated data - Volumetric flow rate vs. pressure`。

### **Pressure differential vector** — 泄压级压降值 `5 : 0.2 : 6` `MPa`（默认） | 1-by-*n* vector

泄压级压差值的向量。向量元素必须与 **Opening area vector** 参数中的元素一一对应。必须按升序输入元素。此向量定义控制阀开启和关闭的控制压力。向量中的第一个元素定义设定压力，即泄压级刚开始开启时的控制压力。最后一个元素定义阀完全开启时的控制压力。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Tabulated data - Area vs. pressure`。

### **Reference pressure differential vector** — 泄压级两端的压降 `5 : 0.2 : 6` `MPa`（默认） | vector

泄压级两端的压降向量。向量元素必须与 **Reference volumetric flow rate vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### **Reference volumetric flow rate vector** — 通过泄压级的流量 `[6.4e-09, .0013, .0027, .0041, .0055, .007]` `m^3/s`（默认） | vector

通过泄压级的流量向量。向量元素必须与 **Reference pressure differential vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。

### **Maximum opening pressure differential** — 最大泄压阀压力 `6` `MPa`（默认） | positive scalar

最大泄压阀压力。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Linear - Area vs. pressure`。

### **Maximum opening area** — 泄压级最大开启面积 `1e-4` `m^2`（默认） | positive scalar

泄压级节流孔的最大开启面积。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Linear - Area vs. pressure`。

### **Leakage area** — 阀处于完全关闭位置时的间隙面积 `1e-10` `m^2`（默认） | positive scalar

当阀处于完全关闭位置时所有间隙的总和。任何小于此值的面积都会被饱和到指定的泄漏面积。该值通过保持流量连续性来提高数值稳定性。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Linear - Area vs. pressure`。

### **Pilot ratio** — 先导面积比 `3`（默认） | positive scalar

先导压力作用面积与负载压力作用面积之比。

### **Back pressure ratio** — 背压面积比 `4`（默认） | positive scalar

背压压力作用面积与负载压力作用面积之比。

### **Discharge coefficient** — 流量系数 `0.64`（默认） | positive scalar

用于考虑理论流量中排放损失的修正系数。

### **Critical Reynolds number** — 层流的上限雷诺数 `150`（默认） | positive scalar

通过阀的层流的上限雷诺数。

### **Smoothing factor** — 数值平滑因子 `0.01`（默认） | positive scalar

连续平滑因子，当阀处于接近开启或接近关闭位置时，为流量响应引入一层渐变变化。将此值设置为小于 1 的非零值，以提高这些工况下仿真的稳定性。

### **Opening area vector** — 泄压级开启面积 `[1e-10, 2e-05, 4e-05, 6e-05, 8e-05, .0001]` `m^2`（默认） | 1-by-*n* vector

泄压级开启面积的向量。向量元素必须与 **Pressure differential vector** 参数中的元素一一对应。按升序列出元素。所有元素必须大于 0。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Tabulated data - Area vs. pressure`。

### **Opening dynamics** — 是否引入由节流口开启引起的流量滞后 `off`（默认） | `on`

是否考虑因开启阀而对流体系统产生的瞬态效应。选择 **Opening dynamics** 会通过在压力响应中引入一阶滞后来近似开启条件。**Opening time constant** 参数也会影响建模的开启动态。

启用后，这些动态适用于平衡阀的泄压级，而不适用于单向阀级。

### **Opening time constant** — 节流口开启时间常数 `0.1` `s`（默认） | positive scalar

当阀从一个位置开启或关闭到另一个位置时，流体达到稳态条件所需时间的常数。此参数影响建模的开启动态。

#### 依赖关系

要启用此参数，请选择 **Opening dynamics**。

### 单向阀

### **Cracking pressure differential** — 单向阀操作的设定压力 `0.01` `MPa`（默认） | positive scalar

使单向阀抬起的压差。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Linear - Area vs. pressure`。

### **Maximum opening pressure differential** — 阀内最大压力 `0.1` `MPa`（默认） | positive scalar

最大阀压力。此参数限制阀出口处的压力，以在仿真期间保持物理值。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Linear - Area vs. pressure`。

### **Maximum opening area** — 最大开启面积 `1e-4` `m^2`（默认） | positive scalar

负载管路中单向阀的最大开启面积。在内部，该单向阀与泄压级并联。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Linear - Area vs. pressure`。

### **Pressure differential vector** — 单向阀操作的压差 `[0.01 : 0.01 : 0.1]` `MPa`（默认） | 1-by-*n* vector

单向阀级的压差向量。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Tabulated data - Area vs. pressure` 或 `Tabulated data - Volumetric flow rate vs. pressure`。

### **Opening area vector** — 单向阀级开启面积 `[1e-10, 1e-05, 2e-05, 3e-05, 4e-05, 5e-05, 6e-05, 7.5e-05, 8.5e-05, .0001]` `m^2`（默认） | 1-by-*n* vector

单向阀级的开启面积向量。向量元素必须与 **Pressure differential vector** 参数中的元素一一对应。

#### 依赖关系

要启用此参数，请将 **Valve parameterization** 设置为 `Tabulated data - Area vs. pressure`。

### **Volumetric flow rate vector** — 单向阀级体积流量 `[.000358, .045, .11, .191, .284, .39, .505, .63, .764, .905] .* 1e-3` `m^3/s`（默认） | 1-by-*n* vector

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

### R2022b：Opening parameterization 选项包括体积流量

您可以将 **Opening parameterization** 设置为 `Tabulated data - Volumetric flow rate vs. pressure`。此选择启用以下新参数：

- **Set pressure differential**
- **Reference pressure differential vector**
- **Reference volumetric flow rate vector**
- **Volumetric flow rate vector**

为提高清晰度：

- `Linear` 选项已重命名为 `Linear - Area vs. pressure`。
- `Tabulated` 选项已重命名为 `Tabulated data - Area vs. pressure`

### R2022b：访问预参数化模块选项

现在可以从可用的预参数化选项中进行选择。可用的制造商为 Rexroth Bosch Group 和 Sun Hydraulics。

## 描述

等温液体系统中的高压调节阀

Counterbalance Valve (IL) 模块表示等温液体网络中的平衡压力控制阀。平衡阀常用于高压事件常见的应用，或任务需要在生产速度下进行高压受控操作时。这包括液压过载或下放悬吊负载等任务。该阀在弹簧、端口 **B** 处的背压和端口 **L** 处的负载压力之间的力平衡下工作。该阀响应先导管路压力的变化。当先导压力超过背压时，阀开始开启。

端口 **B** 与 **P** 之间或端口 **L** 与 **P** 之间没有流量。

此图显示了典型的平衡阀剖视图。

### 阀开启

模块平衡平衡阀的力，使得

ppilotApilot+ploadAload=pbackAback+Fset+kspringxspool,

其中：

- *ppilot* 是端口 **P** 处的压力。
- *pload* 是端口 **L** 处的压力。
- *pback* 是端口 **B** 处的压力。
- *Fset* 是由于弹簧而累积的力。
- *kspring* 是弹簧常数。
- *xspool* 是泄压级阀芯体的线性位置。此位置相对于未加压安装位置。

模块根据 **Pilot ratio** 参数 *Rpilot* 设置压力作用面积 *Apilot*、*Aload* 和 *Aback*，使得

Rpilot=ApilotAload,

以及根据 **Back pressure ratio** 参数 *Rback*，使得

Rback=AbackAload.

对于平衡阀，4:1 或 3:1 的比例是典型值。

预设力 *Fspring* 表示弹簧预紧力与端口 **B** 处的弹簧力的合力。该力是 **Set pressure differential** 参数 *pset* 的函数，使得

Fset=psetAload.

此图显示了 Counterbalance Valve with Test Harness 示例中的示意图，其中压力端口通过作用在具有不同面积的表面上控制该阀。箭头表示由于压力或弹簧力作用在泄压级阀体上的力的方向。灰色部分表示一个单一实体，当泄压级开启时向右移动。单向阀开启时向左移动。

平衡阀示意图，其中负载压力和先导压力向右作用，背压和弹簧向左作用。

### 开口参数化

该模块接受线性或表格化参数化。该模块的单向阀部分与 Check Valve (IL) 模块的操作完全相同。

**线性参数化**

当您将 **开口参数化** 设置为 `Linear - Area vs. pressure` 时，该模块计算阀开口面积，使得

Avalve=p^(Amax−Aleak)+Aleak.

该模块计算归一化控制压力 p^，如下

p^=(pload+ppilotRpilot−pbackRback)−pset(pmax−pset),

其中 *pmax* 是 **最大开启压差** 参数。

归一化单向阀压力为

p^=pcontrol−pcrackingpmax−pcracking,

其中：

- *pcracking* 是 **开启压差** 参数。
- *pmax* 是单向阀 **最大开启压差** 参数。

当阀在 **线性参数化** 中处于接近开启或接近关闭位置时，您可以通过调整 **平滑因子** 参数来保持仿真中的数值稳健性。如果 **平滑因子** 参数非零，则该模块在 *pcracking* 和 *pmax* 之间对控制压力进行平滑饱和处理。有关详细信息，请参阅数值平滑。

**表格化面积参数化**

当您将 **开口参数化** 设置为 `Tabulated data - Area vs. pressure` 时，该模块使用与线性参数化相同的方程，但使用表格数据。表格数据表示相对于给定控制压力的面积，其中 *Pcontrol* = *pload* + *pPilotRPilot* - *pBackRBack*。**压差向量** 参数的第一个元素是设定压力，即当溢流级开始开启时的控制压力。最后一个元素定义阀完全开启时的控制压力。

**表格化流量参数化**

当您将 **开口参数化** 设置为 `Tabulated data - Volumetric flow rate vs. pressure` 时，体积流量方程引用以下量：

- ρ¯valve 是溢流级流动的仿真平均密度。
- *K* 是通过溢流级的流量系数。
- *Δpvalve* 是流动期间溢流级的压降。
- *Δpcrit* 是流动期间溢流级的临界压降。
- *pcontrol* 是仿真控制压力。
- *pcontrol,TLU,Ref* 是内部推导的变化控制压力查找表。
- *pset* 是设定压差。
- *Recrit* 是 **临界雷诺数** 参数。
- *Cd* 是 **流量系数** 参数。
- *ν* 是运动粘度。
- *KTLU,Ref* 是内部推导的流量系数变化查找表，该流量系数是阀面积的函数。
- V˙TLU,Ref 是参考体积流量向量。
- *ppilot,Ref*、*pback,Ref*、*pload,Ref* 分别是用户提供的 **参考体积流量向量** 参数对应的先导压力、背压和负载压力。

该模块计算溢流级的质量流量，使得

m˙valve=ρ¯valveKΔpvalve(Δpvalve2+Δpcrit2)1/4,

其中：

Δpvalve=pload−pbackΔpcrit=π2ρ¯valve8Cd(Recritυ)K=tablelookup(pcontrol,TLU,Ref,KTLU,Ref,pcontrol,interpolation = linear, extrapolation = nearest)

液体从 load 端口流向 back 端口。该模块在按如下方式计算 *KTLU,Ref* 后，将 *K* 外推到最近点：

KTLU,Ref=V˙TLU,RefΔpvalve,TLU,ref,

其中 *Δpvalve,TLU,ref* = *pload,Ref* - *pback,Ref*。该模块按如下方式计算控制压力

pcontrol=Rpilotppilot+pload−Rbackpback

以及参考控制向量

pcontrol,TLU,Ref=Rpilotppilot,Ref+pload,Ref−Rbackpback,Ref+poffset,

其中：

ppilot,Ref=1 atmpback,Ref=1 atmpload,Ref=pback,Ref+Δpvalve,TLU,Ref

该模块内部推导 *Δpflow,Ref*，即指定参考曲线中流体流动的压降。该模块内部按如下方式计算 *poffset*：

poffset=pset−Rpilotppilot,Ref−pload,Ref(1)+Rbackpback,Ref.

该表显示了该模块如何根据 **开口面积** 参数设置来控制溢流级和单向阀级的开口面积。

| 开口参数化 | 溢流级 | 单向阀级 |
| --- | --- | --- |
| `Linear - Area vs. pressure` |  |  |
| `Tabulated - Area vs. pressure` |  |  |
| `Tabulated - Volumetric flow rate vs. pressure` |  |  |

### 预定义参数化

您可以使用预参数化的制造数据填充该模块，从而对特定供应商组件进行建模。

要加载预定义参数化：

1. 在模块对话框中，在 **选定部件** 旁边，单击模块对话框设置中 **选定部件** 旁边的 "<单击以选择>" 超链接。
2. 将打开 **模块参数化管理器** 窗口。从菜单中选择一个部件，然后单击 **全部应用**。您可以使用 **制造商** 下拉菜单缩小选择范围。
3. 您可以关闭 **模块参数化管理器** 菜单。该模块现在具有您指定的参数化。
4. 您可以在模块参数化管理器窗口中，通过选择一个部件并查看 **比较选定部件与模块** 部分中的数据，将当前参数设置与特定供应商组件进行比较。

**注意**

预定义模块参数化使用可用数据源提供参数值。该模块对缺失数据采用工程判断和简化假设。因此，预计仿真行为与实际物理行为之间会有一些偏差。为确保准确性，请根据实验数据验证仿真行为，并根据需要细化组件模型。

要了解更多信息，请参阅预参数化组件列表。
