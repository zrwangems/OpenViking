---
type: simulink-block
title: 'Belt Pulley'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives'
documentation_page: 'beltpulley'
documentation_source_path: 'ref/beltpulley.html'
language: zh-CN
chinese_source: worker-translation
---

# Belt Pulley

## 端口
```yaml
ports:
- name: S
  summary: 带轮轴角速度 机械旋转
  direction: conserving
- name: A
  summary: 皮带端 A 线速度 机械平移
  direction: conserving
- name: B
  summary: 皮带端 B 线速度 机械平移
  direction: conserving
- name: C
  summary: 带轮中心线速度 机械平移
  direction: conserving
```

### 守恒端口

### **S** — 带轮轴角速度 机械旋转

与带轮轴角速度相关联的机械旋转守恒端口。

### **A** — 皮带端 A 线速度 机械平移

与皮带端 A 线速度相关联的机械平移守恒端口。

### **B** — 皮带端 B 线速度 机械平移

与皮带端 B 线速度相关联的机械平移守恒端口。

### **C** — 带轮中心线速度 机械平移

与带轮平移相关联的机械平移守恒端口。带轮在平面内沿带轮包角的角平分线方向移动。当相对速度为正时，带轮中心发生移动。

#### 依赖关系

要启用此端口，请选中 **Pulley translation**。
## 参数
```yaml
parameters:
- name: Belt type
  summary: 皮带参数化 Ideal - No slip（默认）| Flat belt | V-belt
  group: 皮带
- name: V-belt sheave angle
  summary: 带轮槽角 30 deg（默认）| 正标量
  group: 皮带
- name: Number of V-belts
  summary: 皮带数量 1（默认）| 正整数标量
  group: 皮带
- name: Centrifugal force
  summary: 离心力选项 Do not model centrifugal force - Suitable for HIL simulation（默认）| Model centrifugal force
  group: 皮带
- name: Belt mass per unit length
  summary: 单位长度质量 0.6 kg/m（默认）| 正标量
  group: 皮带
- name: Belt direction
  summary: 皮带端的初始相对运动方向 Ends move in opposite direction（默认）| Ends move in same direction
  group: 皮带
- name: Maximum tension
  summary: 张力阈值选项 No maximum tension（默认）| Specify maximum tension
  group: 皮带
- name: Belt maximum tension
  summary: 最大张力阈值 1e5 N（默认）| 正标量
  group: 皮带
- name: Tension warning
  summary: 松弛阈值报告 Do not check tension（默认）| Warn if leading end loses tension
  group: 皮带
- name: Pulley translation
  summary: 允许线性运动的选项 off（默认）| on
  group: 带轮
- name: Pulley radius
  summary: 带轮半径 .15 m（默认）| 正标量
  group: 带轮
- name: Bearing viscous friction coefficient
  summary: 轴承粘性摩擦 0.001 N*m/(rad/s)（默认）| 标量
  group: 带轮
- name: Inertia
  summary: 转动惯量 No inertia（默认）| Specify inertia and initial velocity
  group: 带轮
- name: Pulley inertia
  summary: 带轮惯量 0.01 kg*m^2（默认）| 正标量
  group: 带轮
- name: Pulley initial rotational velocity
  summary: 带轮初始角速度 0 rad/s（默认）| 标量
  group: 带轮
- name: Pulley mass
  summary: 带轮质量 0.01 kg（默认）| 正标量
  group: 带轮
- name: Pulley initial translational velocity
  summary: 带轮初始角速度 0 m/s（默认）| 标量
  group: 带轮
- name: Friction model
  summary: 摩擦方法选择 Modal（默认）| Continuous
  group: 接触
- name: Initial state
  summary: 带轮初始状态 Unlocked（默认）| Locked
  group: 接触
- name: Static friction coefficient
  summary: 静摩擦系数 0.5（默认）| 正标量
  group: 接触
- name: Kinetic friction coefficient
  summary: 动摩擦系数 0.42（默认）| 正标量
  group: 接触
- name: Contact friction coefficient
  summary: 接触摩擦系数 0.5（默认）| 正标量
  group: 接触
- name: Wrap angle
  summary: 皮带与带轮接触角 180 deg（默认）| 正标量
  group: 接触
- name: Velocity threshold
  summary: 速度阈值 0.001 m/s（默认）| 正标量
  group: 接触
- name: Force threshold
  summary: 力阈值 0.01 N（默认）| 正标量
  group: 接触
```

### 皮带

### **Belt type** — 皮带参数化 `Ideal - No slip`（默认）| `Flat belt` | `V-belt`

皮带类型选择。皮带类型影响打滑条件。

- `Ideal - No slip` — 参数化相对于带轮不打滑的理想皮带。
- `Flat belt` — 参数化具有矩形横截面的皮带。
- `V-belt`— 参数化具有 V 形横截面的皮带。

### **V-belt sheave angle** — 带轮槽角 `30` `deg`（默认）| 正标量

V 形皮带的带轮槽角。

#### 依赖关系

要启用此参数，请将 **Belt type** 设置为 `V-belt`。

### **Number of V-belts** — 皮带数量 `1`（默认）| 正整数标量

V 形皮带的数量。

该模块将非整数值舍入为最接近的整数。增加皮带数量会增加单位长度的有效质量和最大允许张力。

#### 依赖关系

要启用此参数，请将 **Belt type** 设置为 `V-belt`。

### **Centrifugal force** — 离心力选项 `Do not model centrifugal force - Suitable for HIL simulation`（默认）| `Model centrifugal force`

包含离心力效应的选项。如果将此参数设置为 `Model centrifugal force`，离心力将饱和至每个皮带端所受力的约 90%。

#### 依赖关系

要启用此参数，请将 **Belt type** 设置为 `Flat belt` 或 `V-belt`。

### **Belt mass per unit length** — 单位长度质量 `0.6` `kg/m`（默认）| 正标量

以线密度表示的离心力贡献，表示为单位长度的质量。

#### 依赖关系

要启用此参数，请将 **Belt type** 设置为 `Flat belt` 或 `V-belt`，并将 **Centrifugal force** 设置为 `Model centrifugal force`。

### **Belt direction** — 皮带端的初始相对运动方向 `Ends move in opposite direction`（默认）| `Ends move in same direction`

一个皮带端相对于另一个皮带端的平移运动相对方向。

### **Maximum tension** — 张力阈值选项 `No maximum tension`（默认）| `Specify maximum tension`

指定最大张力的选项。如果选择 `Specify maximum tension`，且皮带任一端上的皮带张力达到或超过为 **Belt maximum tension** 参数指定的值，仿真将停止并生成断言错误。

### **Belt maximum tension** — 最大张力阈值 `1e5` `N`（默认）| 正标量

每条皮带的最大允许张力。当皮带任一端上的张力达到或超过此值时，仿真将停止并生成断言错误。

#### 依赖关系

要启用此参数，请将 **Maximum tension** 设置为 `Specify maximum tension`。

### **Tension warning** — 松弛阈值报告 `Do not check tension`（默认）| `Warn if leading end loses tension`

当皮带任一端上的张力降至零以下时，该模块是否生成警告。

**注意**

当将 Belt Pulley 模块与 Rope 模块组合形成环路时，请将 Belt Pulley 模块的 **Tension warning** 参数设置为 `Do not check tension`，并将 Rope 模块的 **Tension warning** 参数设置为 `Warn if rope loses tension`。

### 带轮

### **Pulley translation** — 允许线性运动的选项 `off`（默认）| `on`

是否允许带轮平移。选择此参数将启用端口 **C**。

### **Pulley radius** — 带轮半径 `.15` `m`（默认）| 正标量

带轮的半径。

### **Bearing viscous friction coefficient** — 轴承粘性摩擦 `0.001` `N*m/(rad/s)`（默认）| 标量

与支撑带轮轴的轴承相关联的粘性摩擦。

### **Inertia** — 转动惯量 `No inertia`（默认）| `Specify inertia and initial velocity`

使用初始速度参数化转动惯量的选项。

### **Pulley inertia** — 带轮惯量 `0.01` `kg*m^2`（默认）| 正标量

带轮的转动惯量。

#### 依赖关系

要启用此参数，请将 **Inertia** 设置为 `Specify inertia and initial velocity`。

### **Pulley initial rotational velocity** — 带轮初始角速度 `0` `rad/s`（默认）| 标量

带轮的初始角速度。

#### 依赖关系

要启用此参数，请将 **Inertia** 设置为 `Specify inertia and initial velocity`。

### **Pulley mass** — 带轮质量 `0.01` `kg`（默认）| 正标量

用于惯量计算的带轮质量。

#### 依赖关系

要启用此参数，

- 选中 **Pulley translation**
- 将 **Inertia** 设置为 `Specify inertia and initial velocity`

### **Pulley initial translational velocity** — 带轮初始角速度 `0` `m/s`（默认）| 标量

带轮的初始平移速度。

#### 依赖关系

要启用此参数，

- 选中 **Pulley translation**
- 将 **Inertia** 设置为 `Specify inertia and initial velocity`

### 接触

要启用这些设置，请将 **Belt type** 设置为 `Flat belt` 或 `V-belt`。

### **Friction model** — 摩擦方法选择 `Modal`（默认）| `Continuous`

参数化连续摩擦或模态摩擦的选项。

#### 依赖关系

要启用此参数，请清除 **Pulley translation**。

### **Initial state** — 带轮初始状态 `Unlocked`（默认）| `Locked`

以带轮锁定或解锁状态初始化仿真的选项。

#### 依赖关系

要启用此参数，

- 清除 **Pulley translation**
- 将 **Friction model** 设置为 `Modal`

### **Static friction coefficient** — 静摩擦系数 `0.5`（默认）| 正标量

保持静态接触时的皮带摩擦。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Modal`。

### **Kinetic friction coefficient** — 动摩擦系数 `0.42`（默认）| 正标量

打滑时的皮带摩擦。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Modal`。

### **Contact friction coefficient** — 接触摩擦系数 `0.5`（默认）| 正标量

皮带与带轮表面之间的库仑摩擦系数。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Continuous`。

### **Wrap angle** — 皮带与带轮接触角 `180` `deg`（默认）| 正标量

皮带与带轮之间的径向接触角。

### **Velocity threshold** — 速度阈值 `0.001` `m/s`（默认）| 正标量

接触中达到峰值动摩擦所需的相对速度。摩擦速度阈值通过确保速度方向改变时力连续，从而提高仿真的数值稳定性。

### **Force threshold** — 力阈值 `0.01` `N`（默认）| 正标量

接触中达到峰值动摩擦所需的相对力。

#### 依赖关系

要启用此参数，请将 **Belt type** 设置为 `Flat belt` 或 `V-belt`。
## 所属库

Simscape / Driveline / Couplings & Drives

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2012a 中引入**

### 枚举更新

**Pulley translation** 参数现在使用复选框。在以前的版本中，此参数使用下拉菜单。

## 描述

带摩擦皮带缠绕在带轮圆周上的动力传输元件

Belt Pulley 模块表示一个缠绕有柔性理想皮带、平皮带或 V 形皮带的带轮。当将 **Belt type** 设置为 `Ideal - No slip` 时，皮带相对于带轮表面不打滑。您可以选择启用带轮线性平移。

该模块考虑柔性皮带与带轮表面之间的摩擦。当负载超过摩擦力时，张紧器打滑。该模块考虑柔性皮带中的离心载荷、带轮惯量和轴承摩擦。

皮带端可以沿相同方向或相反方向移动。

该模块方程关联皮带分支之间或与带轮之间的动力传输。主动分支和从动分支使用相同的计算。如果没有足够的张力，摩擦力不足以在带轮和皮带之间传输动力。

当皮带两端均处于张力状态时，您的模型是有效的。您可以选择在 Simulink® Diagnostic Viewer 中当领先皮带端失去张力时显示警告。在组装模型时，通过向至少一个皮带端添加质量或添加类似 Cable 模块的张紧器，确保在整个仿真过程中保持张力。使用 Variable Viewer 确保连接到皮带的任何弹簧均处于张力状态。有关构建张紧器的更多详细信息，请参阅 Best Practices for Modeling Pulley Networks。

您可以将 **Friction model** 设置为 `Modal`，以使用带轮的模态参数化。选择模态参数化以获得更好的数值鲁棒性。要启用此参数，请清除 **Pulley translation** 参数。

Belt Pulley 模块使用 Fundamental Friction Clutch 模块的复合实现来产生模态参数化的条件。

### 方程

对于 **Friction model** 参数的任一设置，模块方程均涉及以下量：

- *β* 是皮带方向符号。当将 **Belt direction** 设置为 `Ends move in same direction` 时，*β* = 1。否则，*β* = -1。
- *Vrel* 是皮带与带轮周边之间的相对速度。当 **Belt type** 为 `Ideal - No slip` 时，*Vrel* = 0。
- *VA* 是分支 A 的线速度。
- *VB* 是分支 B 的线速度。
- *VC* 是带轮在其中心处的线速度。当清除 **Pulley translation** 时，该模块将此值约束为 0。
- *ωS* 是带轮接触表面的角速度。
- *R* 是带轮的半径。
- *Fcentrifugal* 是皮带的离心力。
- *FC* 是通过带轮质心的力。当为 **Inertia** 指定值时，*FC* 包括带轮质量加速度产生的力。
- *ρ* 是皮带线密度。
- *Ffr* 是带轮与皮带之间的摩擦力。
- *FA* 是沿分支 A 作用的力。
- *FB* 是沿分支 B 作用的力。
- *θ* 是接触包角。
- *τS* 是带轮转矩。

带轮与皮带之间的运动学约束为：

−βVA=VC−RωS−βVrel

VB=VC+RωS+βVrel

当将 **Belt type** 设置为 `V-belt` 或 `Flat belt`，并将 **Centrifugal force** 设置为 `Model centrifugal force` 时，离心力为：

Fcentrifugal=ρ(VB−VC)2.

当选中 **Pulley translation** 时，力平衡方程为：

FC=(βFA−FB−Fcentrifugal,smooth,sat)⋅sin(θ2).

为计算 *Fcentrifugal,smooth,sat*，该模块

- 使用 *Fthr* 对 *Fcentrifugal* 进行平滑。您可以通过提高 *Fthr* 来增加平滑，通过降低 *Fthr* 来减少平滑。
- 对高于 *βFA-FB* 的值进行饱和。

符号约定使得当 **Belt direction** 为 `Ends move in opposite direction` 时，端口 **S** 中的正旋转导致端口 **A** 的负平移和端口 **B** 的正平移。

要启用 **Friction model** 参数，请将 **Belt type** 设置为 `Flat belt` 或 `V-belt`，并清除 **Pulley translation**。

**连续摩擦**

当将 **Friction model** 设置为 `Continuous` 时，模块方程涉及以下量：

- *μ* 是 **Contact friction coefficient** 参数。
- *μsmoothed* 是摩擦系数的瞬时值。
- *Vthr* 是 **Velocity threshold** 参数。
- *b* 是轴承的粘性阻尼。
- *Fthr* 是 **Force threshold** 参数。

瞬时摩擦系数是相对速度的函数，使得

μsmoothed=μsheavetanh(4VrelVthr),

其中双曲正切函数通过确保 *Vrel* 过零时的输出平滑连续来保持数值鲁棒性。

对于 V 形皮带，该模块使用带轮槽角推导接触摩擦值：

μsheave=μsin(ϕ2),

其中：

- *μsheave* 是有效摩擦系数。
- *Φ* 是带轮槽角。

对于平皮带，*μsheave* = *μ*。

摩擦速度阈值控制摩擦系数从零变化到稳态最大值的区域宽度。摩擦速度阈值指定双曲正切等于 `0.999` 时的速度。该值越小，*μ* 的变化越陡峭。

该模块确定摩擦对皮带端力的影响为：

−βFA−Fcentrifugal=(FB−Fcentrifugal)e−μsmoothedθ,

其形式遵循欧拉-埃特尔魏因方程（也称为绞盘方程）。作用在带轮上的转矩为

τS=(−βFA−FB)Rσ+ωSb,

其中当将 **Belt type** 设置为 `Ideal - No slip` 时，*σ* = 1。否则，

σ=tanh(4VrelVthr)tanh(FBFthr).

**模态摩擦**

对于 V 形皮带，该模块使用带轮槽角推导静摩擦和动摩擦值：

μStatic,sheave=μStaticsin(ϕ2)μKinetic,sheave=μKineticsin(ϕ2)

其中：

- *μStatic* 是 **Static friction coefficient** 参数。
- *μStatic,sheave* 是有效静摩擦系数。
- *μKinetic* 是 **Kinetic friction coefficient** 参数。
- *μKinetic,sheave* 是有效动摩擦系数。
- *Φ* 是带轮槽角。

对于平皮带，*μStatic,sheave* = *μStatic*，*μKinetic,sheave* = *μKinetic*。

当将 **Friction model** 设置为 `Modal` 时，该模块计算打滑前的最大静摩擦力为

FFriction,Static,Max=(FDrive−FCentrifugal)⋅(1−e−μStatic,sheaveθ),

其中 *FFriction,Static,Max* 是静摩擦产生的最大力幅值，*FDrive* 是在带轮力幅值最大端感受到的张力产生的力。与 *Fcentrifugal* 一样，该模块使用 *Fthr* 对 *FDrive* 进行平滑。要增加或减少对 *FDrive* 的平滑，请提高或降低 **Force threshold** 参数的值。

该模块将 *FFriction,Static,Max* 平滑饱和为大于或等于 0，即

FFriction,Static,Max,Smooth=0.5(FFriction,Static,Max+FFriction,Static,Max2+(RFthr)2).

在打滑期间，

FFriction,Slip=μKinetic,sheaveμStatic,sheaveFFriction,Static,Max,

其中 *μKinetic,sheave* 是动摩擦系数。该模块使用以下方程求解转矩平衡

τS=ωSb+RFFriction,

以及

RβFA+RFB=−RFFriction,

其中 Simscape™ 将 *RFFriction* 记录为 `fundamental_clutch.torque`。
