---
type: simulink-block
title: 'Belt Pulley'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Driveline Modeling / Power Transmission Using Pulley Networks'
documentation_page: 'beltpulley'
documentation_source_path: 'ref/beltpulley.html'
language: zh-CN
chinese_source: worker-translation
---

# Belt Pulley

## 端口

### 守恒

### **S** — 带轮轴角速度 机械旋转

与带轮轴角速度关联的机械旋转守恒端口。

### **A** — 传动带端 A 线速度 机械平移

与传动带端 A 线速度关联的机械平移守恒端口。

### **B** — 传动带端 B 线速度 机械平移

与传动带端 B 线速度关联的机械平移守恒端口。

### **C** — 带轮中心线速度 机械平移

与带轮平移关联的机械平移守恒端口。带轮在平面内并沿带轮包角的平分线移动。当相对速度为正时，带轮中心移动。

#### 依赖项

要启用此端口，请选择 **带轮平移**。

## 参数

### 传动带

### **传动带类型** — 传动带参数化 `Ideal - No slip`（默认） | `Flat belt` | `V-belt`

传动带类型选择。传动带类型影响打滑条件。

- `Ideal - No slip` — 参数化一个理想传动带，其相对于带轮不打滑。
- `Flat belt` — 参数化一个具有矩形横截面的传动带。
- `V-belt` — 参数化一个具有 V 形横截面的传动带。

### **V 带轮槽角** — 槽角 `30` `deg`（默认） | positive scalar

V 带的槽角。

#### 依赖项

要启用此参数，请将 **传动带类型** 设置为 `V-belt`。

### **V 带数量** — 传动带数量 `1`（默认） | positive scalar integer

V 带的数量。

该模块将非整数值四舍五入到最接近的整数。增加传动带数量会增加单位长度有效质量以及最大允许张力。

#### 依赖项

要启用此参数，请将 **传动带类型** 设置为 `V-belt`。

### **离心力** — 离心力选项 `Do not model centrifugal force - Suitable for HIL simulation`（默认） | `Model centrifugal force`

包含离心力效应的选项。如果将此参数设置为 `Model centrifugal force`，离心力会饱和到每个传动带端上的力值的大约 90%。

#### 依赖项

要启用此参数，请将 **传动带类型** 设置为 `Flat belt` 或 `V-belt`。

### **传动带单位长度质量** — 单位长度质量 `0.6` `kg/m`（默认） | positive scalar

以线密度表示的离心力贡献，线密度表示为质量每单位长度。

#### 依赖项

要启用此参数，请将 **传动带类型** 设置为 `Flat belt` 或 `V-belt`，并将 **离心力** 设置为 `Model centrifugal force`。

### **传动带方向** — 传动带端的初始相对运动方向 `Ends move in opposite direction`（默认） | `Ends move in same direction`

一个传动带端相对于另一个传动带端的平移运动相对方向。

### **最大张力** — 张力阈值选项 `No maximum tension`（默认） | `Specify maximum tension`

指定最大张力的选项。如果选择 `Specify maximum tension`，并且传动带任一端上的张力达到或超过为 **传动带最大张力** 参数指定的值，则仿真停止并生成断言错误。

### **传动带最大张力** — 最大张力阈值 `1e5` `N`（默认） | positive scalar

每个传动带的最大允许张力。当传动带任一端上的张力达到或超过此值时，仿真停止并生成断言错误。

#### 依赖项

要启用此参数，请将 **最大张力** 设置为 `Specify maximum tension`。

### **张力警告** — 松弛阈值报告 `Do not check tension`（默认） | `Warn if leading end loses tension`

当传动带任一端处的张力降至零以下时，该模块是否生成警告。

**注意**

当将 Belt Pulley 模块与 Rope 模块组合成环路时，请将 Belt Pulley 模块的 **张力警告** 参数设置为 `Do not check tension`，并将 Rope 模块的 **张力警告** 参数设置为 `Warn if rope loses tension`。

### 带轮

### **带轮平移** — 允许线性运动的选项 `off`（默认） | `on`

是否允许带轮平移。选择此参数会启用端口 **C**。

### **带轮半径** — 带轮半径 `.15` `m`（默认） | positive scalar

带轮的半径。

### **轴承粘性摩擦系数** — 轴承粘性摩擦 `0.001` `N*m/(rad/s)`（默认） | scalar

与支撑带轮轴的轴承相关的粘性摩擦。

### **惯性** — 转动惯量 `No inertia`（默认） | `Specify inertia and initial velocity`

使用初始速度参数化转动惯量的选项。

### **带轮转动惯量** — 带轮转动惯量 `0.01` `kg*m^2`（默认） | positive scalar

带轮的转动惯量。

#### 依赖项

要启用此参数，请将 **惯性** 设置为 `Specify inertia and initial velocity`。

### **带轮初始角速度** — 初始带轮角速度 `0` `rad/s`（默认） | scalar

带轮的初始角速度。

#### 依赖项

要启用此参数，请将 **惯性** 设置为 `Specify inertia and initial velocity`。

### **带轮质量** — 带轮质量 `0.01` `kg`（默认） | positive scalar

用于转动惯量计算的带轮质量。

#### 依赖项

要启用此参数，

- 选择 **带轮平移**
- 将 **惯性** 设置为 `Specify inertia and initial velocity`

### **带轮初始平移速度** — 初始带轮平移速度 `0` `m/s`（默认） | scalar

带轮的初始平移速度。

#### 依赖项

要启用此参数，

- 选择 **带轮平移**
- 将 **惯性** 设置为 `Specify inertia and initial velocity`

### 接触

要启用这些设置，请将 **传动带类型** 设置为 `Flat belt` 或 `V-belt`。

### **摩擦模型** — 摩擦方法选择 `Modal`（默认） | `Continuous`

参数化连续摩擦或模态摩擦的选项。

#### 依赖项

要启用此参数，请清除 **带轮平移**。

### **初始状态** — 带轮初始状态 `Unlocked`（默认） | `Locked`

使用带轮锁定或未锁定初始化仿真的选项。

#### 依赖项

要启用此参数，

- 清除 **带轮平移**
- 将 **摩擦模型** 设置为 `Modal`

### **静摩擦系数** — 静摩擦系数 `0.5`（默认） | positive scalar

保持静态接触时的传动带摩擦。

#### 依赖项

要启用此参数，请将 **摩擦模型** 设置为 `Modal`。

### **动摩擦系数** — 动摩擦系数 `0.42`（默认） | positive scalar

打滑时的传动带摩擦。

#### 依赖项

要启用此参数，请将 **摩擦模型** 设置为 `Modal`。

### **接触摩擦系数** — 接触摩擦系数 `0.5`（默认） | positive scalar

传动带与带轮表面之间的库仑摩擦系数。

#### 依赖项

要启用此参数，请将 **摩擦模型** 设置为 `Continuous`。

### **包角** — 传动带与带轮接触角 `180` `deg`（默认） | positive scalar

传动带与带轮之间的径向接触角。

### **速度阈值** — 速度阈值 `0.001` `m/s`（默认） | positive scalar

接触中达到峰值动摩擦所需的相对速度。摩擦速度阈值通过确保速度方向改变时力连续来提高仿真的数值稳定性。

### **力阈值** — 力阈值 `0.01` `N`（默认） | positive scalar

接触中达到峰值动摩擦所需的相对力。

#### 依赖项

要启用此参数，请将 **传动带类型** 设置为 `Flat belt` 或 `V-belt`。

## 所属库

Simscape / Driveline / Couplings & Drives

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2012a 中引入**

### 枚举更新

**带轮平移** 参数现在使用复选框。在以前的版本中，此参数使用下拉列表。

## 描述

绕在带轮圆周上的摩擦传动带动力传输元件

Belt Pulley 模块表示一个缠绕在柔性理想、平型或 V 形传动带中的带轮。当将 **传动带类型** 设置为 `Ideal - No slip` 时，传动带相对于带轮表面不打滑。您可以选择启用带轮线性平移。

该模块考虑柔性传动带与带轮表面之间的摩擦。当负载超过摩擦力时，张紧器打滑。该模块考虑柔性传动带中的离心载荷、带轮转动惯量和轴承摩擦。

传动带端可以沿相同方向或相反方向移动。

该模块方程将传动带分支之间的动力传输或与带轮之间的动力传输关联起来。主动分支和从动分支使用相同的计算。如果没有足够的张力，摩擦力不足以在带轮与传动带之间传输动力。

当传动带两端均处于张力状态时，您的模型有效。您可以选择当传动带前端失去张力时在 Simulink® Diagnostic Viewer 中显示警告。在组装模型时，请通过向至少一个传动带端添加质量或通过添加诸如 Cable 模块之类的张紧器，确保在整个仿真过程中保持张力。使用 Variable Viewer 确保连接到传动带的任何弹簧均处于张力状态。有关构建张紧器的更多详细信息，请参阅 Best Practices for Modeling Pulley Networks。

您可以将 **摩擦模型** 设置为 `Modal`，以使用带轮的模态参数化。选择模态参数化以获得更高的数值稳健性。要启用此参数，请清除 **带轮平移** 参数。

Belt Pulley 模块使用 Fundamental Friction Clutch 模块的复合实现来生成模态参数化的条件。

### 方程

对于 **摩擦模型** 参数的任一设置，模块方程均涉及以下量：

- *β* 是传动带方向符号。当将 **传动带方向** 设置为 `Ends move in same direction` 时，*β* = 1。否则，*β* = -1。
- *Vrel* 是传动带与带轮周边之间的相对速度。当 **传动带类型** 为 `Ideal - No slip` 时，*Vrel* = 0。
- *VA* 是分支 A 的线速度。
- *VB* 是分支 B 的线速度。
- *VC* 是带轮在其中心处的线速度。当清除 **带轮平移** 时，模块将此值约束为 0。
- *ωS* 是带轮接触表面的角速度。
- *R* 是带轮的半径。
- *Fcentrifugal* 是传动带的离心力。
- *FC* 是作用通过带轮质心的力。当为 **惯性** 指定值时，*FC* 包括带轮质量加速度引起的力。
- *ρ* 是传动带线密度。
- *Ffr* 是带轮与传动带之间的摩擦力。
- *FA* 是沿分支 A 作用的力。
- *FB* 是沿分支 B 作用的力。
- *θ* 是接触包角。
- *τS* 是带轮转矩。

带轮与传动带之间的运动学约束为：

−βVA=VC−RωS−βVrel

VB=VC+RωS+βVrel

当将 **传动带类型** 设置为 `V-belt` 或 `Flat belt`，并将 **离心力** 设置为 `Model centrifugal force` 时，离心力为：

Fcentrifugal=ρ(VB−VC)2.

当选择 **带轮平移** 时，力平衡方程为：

FC=(βFA−FB−Fcentrifugal,smooth,sat)⋅sin(θ2).

要计算 *Fcentrifugal,smooth,sat*，该模块

- 使用 *Fthr* 平滑 *Fcentrifugal*。您可以通过提高 *Fthr* 来增加平滑，通过降低 *Fthr* 来减少平滑。
- 将高于 *βFA-FB* 的值饱和。

符号约定使得当 **传动带方向** 为 `Ends move in opposite direction` 时，端口 **S** 中的正旋转导致端口 **A** 的负平移和端口 **B** 的正平移。

要启用 **摩擦模型** 参数，请将 **传动带类型** 设置为 `Flat belt` 或 `V-belt`，并清除 **带轮平移**。

**连续摩擦**

当将 **摩擦模型** 设置为 `Continuous` 时，模块方程涉及以下量：

- *μ* 是 **接触摩擦系数** 参数。
- *μsmoothed* 是摩擦系数的瞬时值。
- *Vthr* 是 **速度阈值** 参数。
- *b* 是轴承的粘性阻尼。
- *Fthr* 是 **力阈值** 参数。

瞬时摩擦系数是相对速度的函数，使得

μsmoothed=μsheavetanh(4VrelVthr),

其中双曲正切函数通过确保 *Vrel* 零交叉时输出平滑且连续来保持数值稳健性。

对于 V 带，模块使用槽角推导接触摩擦值：

μsheave=μsin(ϕ2),

其中：

- *μsheave* 是有效摩擦系数。
- *Φ* 是槽角。

对于平带，*μsheave* = *μ*。

摩擦速度阈值控制摩擦系数从零变化到稳态最大值的区域宽度。摩擦速度阈值指定双曲正切等于 `0.999` 时的速度。该值越小，*μ* 的变化越陡。

模块确定摩擦对传动带端处力的影响为：

−βFA−Fcentrifugal=(FB−Fcentrifugal)e−μsmoothedθ,

其遵循 capstan 方程（也称为 Euler-Eytelwein 方程）的形式。作用在带轮上的转矩为

τS=(−βFA−FB)Rσ+ωSb,

其中当将 **传动带类型** 设置为 `Ideal - No slip` 时，*σ* = 1。否则，

σ=tanh(4VrelVthr)tanh(FBFthr).

**模态摩擦**

对于 V 带，模块使用槽角推导静摩擦和动摩擦值：

μStatic,sheave=μStaticsin(ϕ2)μKinetic,sheave=μKineticsin(ϕ2)

其中：

- *μStatic* 是 **静摩擦系数** 参数。
- *μStatic,sheave* 是有效静摩擦系数。
- *μKinetic* 是 **动摩擦系数** 参数。
- *μKinetic,sheave* 是有效动摩擦系数。
- *Φ* 是槽角。

对于平带，*μStatic,sheave* = *μStatic*，且 *μKinetic,sheave* = *μKinetic*。

当将 **摩擦模型** 设置为 `Modal` 时，模块在打滑前计算最大静摩擦力为

FFriction,Static,Max=(FDrive−FCentrifugal)⋅(1−e−μStatic,sheaveθ),

其中 *FFriction,Static,Max* 是静摩擦产生的最大力幅值，*FDrive* 是在力幅值最大的带轮端处感受到的由张力产生的力。与 *Fcentrifugal* 一样，模块使用 *Fthr* 平滑 *FDrive*。要增加或减少 *FDrive* 上的平滑，请提高或降低 **力阈值** 参数的值。

模块平滑地将 *FFriction,Static,Max* 饱和为大于或等于 0，如下：

FFriction,Static,Max,Smooth=0.5(FFriction,Static,Max+FFriction,Static,Max2+(RFthr)2).

在打滑期间，

FFriction,Slip=μKinetic,sheaveμStatic,sheaveFFriction,Static,Max,

其中 *μKinetic,sheave* 是动摩擦系数。模块使用以下方程求解转矩平衡：

τS=ωSb+RFFriction,

以及

RβFA+RFB=−RFFriction,

其中 Simscape™ 将 *RFFriction* 记录为 `fundamental_clutch.torque`。
