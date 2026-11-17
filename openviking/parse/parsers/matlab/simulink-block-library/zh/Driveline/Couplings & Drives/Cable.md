---
type: simulink-block
title: 'Cable'
family: 'couplings-drives'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives'
documentation_page: 'cable'
documentation_source_path: 'ref/cable.html'
language: zh-CN
chinese_source: worker-translation
---

# Cable

## 端口

### 输入

### **L** — 长度物理信号

与缆索段两端瞬时接触点之间的长度关联的物理信号输入端口。

#### 依赖关系

要启用此端口，请选择 **Model variable rest length**。

### 守恒

### **B** — Cable 机械平动的基座接触位置

与缆索段的基座瞬时接触位置关联的机械平动守恒端口。

### **F** — Cable 机械平动的从动接触位置

与缆索段的从动瞬时接触位置关联的机械平动守恒端口。

## 参数

### **Model variable rest length** — 可变静止长度选项 `off`（默认）| `on`

是否对可变静止长度建模。可变长度会影响刚度和阻尼。选择 **Model mass** 时，可变长度会影响缆索的质量。选择 **Model gravity** 时，可变长度会影响重力作用于缆索的力。

### **Minimum rest length** — 最小静止长度 `0.01` `m`（默认）| positive scalar

缆索的最小静止长度。仿真可变静止长度时，**Minimum rest length** 参数值表示缆索长度的下界。模块会平滑地过渡到该值并离开该值，并对低于该值的输入进行饱和处理。

#### 依赖关系

要启用此参数，请选择 **Model variable rest length**。

### **Stretch parameterization** — 常量或表格参数化 `Constant stiffness and damping`（默认）| `Tabulated stiffness and damping`

是否使用常量或表格化的刚度和阻尼值对缆索进行参数化。

### **Rigidity** — 缆索刚性 `1000` `N`（默认）| positive scalar

缆索段的有效刚性。当缆索拉伸运动纯为纵向时，此参数值等效于轴向刚度。

#### 依赖关系

要启用此参数，请选择 **Model variable rest length**，并将 **Stretch parameterization** 设置为 `Constant stiffness and damping`。

### **Stiffness** — 抗变形能力 `1000` `N/m`（默认）| positive scalar

缆索段的有效平动弹簧刚度。

#### 依赖关系

要启用此参数，请清除 **Model variable rest length**，并将 **Stretch parameterization** 设置为 `Constant stiffness and damping`。

### **Damping** — 耗散能量的趋势 `100` `N/(m/s)`（默认）| positive scalar

缆索段的有效平动阻尼。当选择 **Model slack** 参数且 xs<0 时，模块忽略阻尼。

#### 依赖关系

要启用此参数，请将 **Stretch parameterization** 设置为 `Constant stiffness and damping`。

### **Stretch vector** — 拉伸位移 `[.1, .2, .5, 1]` `m`（默认）| vector

缆索上给定点的拉伸位移。该向量长度必须至少为二，并且必须严格递增。模块根据缆索速度确定位移。

#### 依赖关系

要启用此参数，请清除 **Model variable rest length**，并将 **Stretch parameterization** 设置为 `Tabulated stiffness and damping`。

### **Stiffness vector** — 表格化能量耗散 `[500, 520, 540, 540]` `N/m`（默认）| vector of nonnegative values

给定拉伸位移下的缆索刚度。此参数中的元素与 **Stretch vector** 参数一一对应。

#### 依赖关系

要启用此参数，请清除 **Model variable rest length**，并将 **Stretch parameterization** 设置为 `Tabulated stiffness and damping`。

### **Damping vector** — 表格化阻尼 `[50, 60, 80, 80]` `N*s/m`（默认）| vector of nonnegative values

给定拉伸位移下的缆索阻尼。此参数中的元素与 **Stretch vector** 参数一一对应。

#### 依赖关系

要启用此参数，请清除 **Model variable rest length**，并将 **Stretch parameterization** 设置为 `Tabulated stiffness and damping`。

### **Rest length vector, Lr** — 表格化静止长度 `[.25, .5, 1]` `m`（默认）| vector of length *M*

静止长度值的向量，*LRest*。

#### 依赖关系

要启用此参数，请选择 **Model variable rest length**，并将 **Stretch parameterization** 设置为 `Tabulated stiffness and damping`。

### **Stretch per rest length vector, s/Lr** — 表格化每静止长度拉伸 `[.01, .02, .1, .25]`（默认）| vector of length *N*

给定静止长度的拉伸值向量，*s/LRest*。各元素与 **Rest length vector, Lr** 参数一一对应。

#### 依赖关系

要启用此参数，请选择 **Model variable rest length**，并将 **Stretch parameterization** 设置为 `Tabulated stiffness and damping`。

### **Stiffness table (Lr, s/Lr)** — 表格化刚度 `[500, 600, 600, 500; 250, 300, 300, 250; 125, 150, 150, 125]` `N/m`（默认）| *M*x*N* matrix

给定静止长度 *LRest* 和拉伸 *s/LRest* 的刚度值表。

#### 依赖关系

要启用此参数，请选择 **Model variable rest length**，并将 **Stretch parameterization** 设置为 `Tabulated stiffness and damping`。

### **Damping table (Lr, s/Lr)** — 表格化阻尼 `[50, 60, 60, 50; 50, 60, 60, 50; 50, 60, 60, 50]` `N*s/m`（默认）| *M*x*N* matrix

给定静止长度 *LRest* 和拉伸 *s/LRest* 的阻尼值表。

#### 依赖关系

要启用此参数，请选择 **Model variable rest length**，并将 **Stretch parameterization** 设置为 `Tabulated stiffness and damping`。

### **Model slack** — 松弛参数化选项 `off`（默认）| `on`

是否对松弛建模。当缆索不受张力时，模块不传递弹簧力。选择此参数后，Cable 模块等效于一个 **Upper bound** 设置为 `0` 且 **Lower bound** 设置为 `-inf` 的 Translational Hard Stop 模块。有关详细信息，请参阅 Translational Hard Stop。

### **Slack model** — 松弛过渡行为 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| `Full stiffness and damping applied at bounds, undamped rebound` | ...

松弛模型的刚度和回弹选项。松弛模型等效于 Translational Hard Stop 模块。可从以下选项中选择：

- `Stiffness and damping applied smoothly through transition region, damped rebound`
- `Full stiffness and damping applied at bounds, undamped rebound`
- `Full stiffness and damping applied at bounds, damped rebound`

#### 依赖关系

要启用此参数，请选择 **Model slack**。

### **Linear density** — 线密度 `0.2` `kg/m`（默认）| positive scalar

缆索段的线密度，*μ*。

#### 依赖关系

要启用此参数，请选择 **Model variable rest length**，并选择 **Model mass** 或 **Model slack**。

### **Transition region** — 部分松弛效应区域 `0.1` `mm`（默认）| positive scalar

距完全压缩或完全伸展的距离，在此范围内会部分施加刚度和阻尼效应。当将 **Slack model** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound` 时，模块会在弹簧接近完全伸展或完全压缩时平滑过渡刚度和阻尼的开始。

#### 依赖关系

要启用此参数，请选择 **Model variable rest length**，或清除 **Model variable rest length** 并选择 **Model slack**，然后将 **Slack model** 设置为 `Stiffness and damping applied smoothly through transition region`。

### **Model mass** — 质量参数化选项 `Off`（默认）| `On`

是否对质量建模。选择 **Model mass** 时，模块会考虑其所代表的缆索段的质量。包含质量有助于初始化某些模型，但计算成本也可能更高。

#### 依赖关系

要启用此参数，请清除 **Model slack** 参数。

### **Mass** — 缆索段质量 `1` `kg`（默认）| positive scalar

模块所代表的缆索段的质量。模块将总质量的一半分配到缆索的每一端。

#### 依赖关系

要启用此参数，请清除 **Model variable rest length**，选择 **Model mass** 或 **Model slack**。

### **Model gravity** — 重力选项 `off`（默认）| `on`

是否对重力建模。

#### 依赖关系

要启用此参数，请选择 **Model mass** 或 **Model slack**。

### **Gravitational acceleration, g** — 重力加速度 `9.81` `m/s^2`（默认）| positive scalar

重力引起的加速度。可通过 **Angle of gravity relative to positive direction, θ** 参数指定正加速度的方向。

#### 依赖关系

要启用此参数，请选择 **Model mass** 或 **Model slack** 以及 **Model gravity**。

### **Angle of gravity relative to positive direction, θ** — 正重力角度 `0` `deg`（默认）| scalar

**Gravitational acceleration, g** 参数值为正时的角度，*θ*。值 `0` 表示向下加速度。

#### 依赖关系

要启用此参数，请选择 **Model mass** 或 **Model slack** 以及 **Model gravity**。

### **Warn if cable loses tension** — 失去张力警告选项 `off`（默认）| `on`

当缆索段不再处于张力状态时是否生成警告。使用此参数可识别系统是否出现松弛情况。

### **Error if cable exceeds maximum tension** — 最大张力错误选项 `off`（默认）| `on`

当缆索段超过 **Cable maximum tension** 参数值时是否生成错误。

### **Cable maximum tension** — 缆索段中允许的最大张力 `1e5` `N`（默认）| positive scalar

张力值错误目标。当缆索段中的张力超过此参数时，模块会生成错误。

#### 依赖关系

要启用此参数，请选择 **Error if cable exceeds maximum tension**。

## 所属库

Simscape / Driveline / Couplings & Drives

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

### R2024b: 可变静止长度

表示具有可变静止长度的连接。选择 **Model variable rest length** 时，模块会为移动滑轮应用生成更高精度的结果。

此外，你现在可以包含重力。要启用 **Model gravity** 参数，请选择 **Model mass** 参数。

### R2023b: 表格化刚度和阻尼

可以将新的 **Stretch parameterization** 参数设置为 `Tabulated`，以指定缆索行为的表格化数据。关联的 **Stretch vector**、**Stiffness vector** 和 **Damping vector** 参数也是新增的。这些参数已更新以支持模块增强：

| 旧参数 | 新参数 |
| --- | --- |
| **Rope model** | **Model slack** |
| **Maximum tension** | **Specify maximum tension** |
| **Tension warning** | **Warn if cable loses tension** |

### R2023b: 名称变更

Rope 模块已重命名为 Cable 模块。

## 描述

可实现张力传递的 Cable 连接

Cable 模块表示一个在两个接触点之间传递张力的元件。可以将该模块视为任意张力传递装置，以仿真多种情况，包括滑轮网络、缆索驱动和蛇形带。可以选择缆索在失去张力时是否出现松弛。该模块具有一个基座端口 **B** 和一个从动端口 **F**。当基座端口领先于从动端口时，缆索在张力下拉伸。

该模块仅考虑纵向平动运动以及施加在缆索端部的力。第一张图显示了并联的 Translational Spring 和 Translational Damper 模块，其在功能上等效于质量为零的 Cable 模块。第二张图显示了相同的弹簧和阻尼器模块，但在两侧各有一个额外的 Mass 模块，其在功能上等效于质量非零的 Cable 模块。

带有 in 端口和 out 端口的并联弹簧和阻尼器。带有 in 端口、out 端口以及两端质量的并联弹簧和阻尼器。

这些图仅适用于缆索处于张力状态时。

**提示**

在选择 **Model slack** 和 **Model mass** 参数之前，请确认模型按预期运行。通过在 **Simscape Results Viewer** 中查看每条缆索的张力图并查找意外的负值，验证 **B** 和 **F** 端口的朝向是否正确。

Cable 模块可以充当绳索、皮带、缆索或任何其他具有抗拉强度并在两个接触点之间传递张力的装置。接触点可以是滑轮、卷筒或理想源。可以使用 **Stretch parameterization** 参数控制该模块是充当常量连接还是表格化连接。

可以使用此模块对静止或移动滑轮网络建模。可以使用诸如 Ideal Translational Velocity Source 模块之类的源，或连接到 Ideal Force Source 模块的 Rope Drum 模块来驱动 Cable 模块。

为了获得更高的保真度或数值稳定性，可以选择对系统中的质量效应建模。选择 **Model mass** 时，模块会将总质量的一半分配到缆索的每一端。添加少量质量可以改善模型的初始化。还可以指定缆索的初始条件。如果选择仿真松弛，则当缆索处于松弛状态时，模块不施加刚度和阻尼。选择 **Model slack** 或 **Model mass** 会启用 **Model gravity** 参数。包含重力效应可提高重型缆索段的精度。

对于具有可变静止长度的缆索段，请使用 **Model variable rest length** 参数来提高移动滑轮应用的结果。该模块支持以下可变静止长度场景示例：

- 缆索的一端固定，另一端连接到移动滑轮。
- 缆索的两端各连接到一个移动滑轮。

选择 **Model variable rest length** 时，必须为模块使用正确的朝向。要了解更多信息，请参阅 Best Practices for Modeling Pulley Networks。

### 方程

模块方程涉及以下量：

- *F* 是张力，其中 F=FB=−FF。
- *xs* 是由拉伸引起的变形，通过 **Stretch** 变量指定。Simscape Results Explorer 将此量显示为 `s`。
- *K* 是弹簧刚度系数。当选择 **Model slack** 且 xs<0 时，K(xs)=0。
- *D* 是阻尼系数。
- *m* 是总质量，通过 **Mass** 参数指定。模块将总质量的一半分配到每一端。
- *xB* 是 base 节点的位置。
- *xF* 是 follower 节点的位置。
- *ẋs* 是拉伸速度。
- *LRest* 是缆绳段的静止长度。
- *Lmin* 是 **Minimum rest length** 参数。
- *μ* 是 **Linear density** 参数。

Cable 模块对端口 **B** 处外部载荷的响应为

FB(xs(t),t)=m2x¨B(t)+Dx˙s(t)+Kxs(t),

以及对端口 **F** 的响应为，

FF(xs(t),t)=m2x¨F(t)−Dx˙s(t)−Kxs(t),

其中 xs(t)=xB(t)−xF(t)。*D* 和 *V* 的定义取决于参数化。

- 当将 **Stretch parameterization** 设置为 `Constant stiffness and damping` 并清除 **Model variable rest length** 时，*D* 和 *K* 为常量。
- 当将 **Stretch parameterization** 设置为 `Constant stiffness and damping` 并选择 **Model variable rest length** 时，*D* 为常量，且 *K = EA/LRest*，其中 EA 是 **Rigidity** 参数的值。
- 当将 **Stretch parameterization** 设置为 `Tabulated stiffness and damping` 并清除 **Model variable rest length** 时，*D = TLU(xs)* 且 *K = TLU(xs)*。
- 当将 **Stretch parameterization** 设置为 `Tabulated stiffness and damping` 并选择 **Model variable rest length** 时，*D = TLU(xs, xs/LRest)* 且 *K = TLU(LRest, xs/LRest)*。

当选择 **Model slack** 且 *xs < 0* 时，模块将 *K* 的值覆盖为 `0`。

力作为时间和拉伸变形 *xs* 的函数而变化。*K* 和 *B* 是 *xs* 的函数，使得当没有松弛或未模拟松弛时，K(xs)=K。否则，当在 xs<0 发生松弛时，K(xs)=0。相同逻辑适用于 *B*。涉及质量的项仅当选择 **Model mass** 参数时适用。

当选择 **Model variable rest length** 时，会在端口 **L** 将长度作为输入。要输入静止长度，请使用 Translational Motion Sensor 模块确定缆绳段的运动。模块对静止长度进行饱和处理，使得

Lrest=max(L−xs,Lmin)

当选择 **Model variable rest length** 和 **Model mass** 时，模块使用 **Linear density** 参数的值确定缆绳段的质量，使得

m= μLRestfMass,B=m2v˙BfMass,F=m2v˙F

当选择 **Model variable rest length**、**Model mass** 和 **Model gravity** 时，模块对缆绳段每一端施加重力，使得

fGravity=mgcos(θ)fGravity,B=fGravity2fGravity,F=fGravity2

正的缆绳速度从端口 **B** 作用到端口 **F**。正的重力根据缆绳方向向下作用。重力根据 B 和 F 端口的方向作用于模块。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期量值的方法。使用基于标称值的系统缩放可提高仿真稳健性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。

### 限制

当选择 **Model mass** 和 **Model variable rest length** 参数时，模块使用准静态模型计算由质量引起的力。模块不考虑缆绳段质量的变化率。可以使用 Variable Mass 模块来包含变化质量对由质量引起的张力的影响。
