---
type: simulink-block
title: 'Simple Gear'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears'
documentation_page: 'simplegear'
documentation_source_path: 'ref/simplegear.html'
language: zh-CN
chinese_source: worker-translation
---

# Simple Gear

## 端口

### 守恒端口

### **B** — 基座旋转机械

与基座轴关联的旋转机械守恒端口。

### **F** — 从动旋转机械

与从动轴关联的旋转机械守恒端口。

### **H** — 热流

与热流关联的热守恒端口。热流影响齿轮温度，从而影响动力传输效率。

#### 依赖关系

要启用此端口，请将 **Friction model** 设置为以下之一：

- `Temperature-dependent
  efficiency`
- `Temperature and load-dependent
  efficiency`

## 参数

### 参数依赖关系表

下表显示了某些 **Meshing Losses** 参数和 **Faults** 参数的可见性如何取决于热模型以及您为其他参数选择的选项。

| 默认模型 — 对于非热模型，热端口 **H** 不可见。 | | | | | | 热模型 — 对于热模型，热端口 **H** 可见。 | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 啮合损耗 | | | | | | 啮合损耗 | |
| 摩擦模型 — 选择 `No meshing losses - Suitable for HIL simulation`、`Constant efficiency` 或 `Load-dependent efficiency` | | | | | | 摩擦模型 — 选择 `Temperature-dependent efficiency` 或 `Temperature and load-dependent efficiency` | |
| **无啮合损失 - 适用于 HIL 仿真** | **恒定效率** | | | **负载相关效率** | | **温度相关效率** | **温度和负载相关效率** |
| Efficiency | | | Input shaft torque at no load | | Temperature | Temperature |
| Follower power threshold | | | Nominal output torque | | Efficiency | Load at base gear |
|  | | | Efficiency at nominal output torque | | Follower power threshold | Efficiency matrix |
|  | | | Follower angular velocity threshold | | Follower angular velocity threshold |

### 主要

### **Follower (F) to base (B) teeth ratio (NF/NB)** — 齿轮比 `2`（默认）| 正标量

从动轴与基座轴的固定比 *gFB*。齿轮比必须严格为正。

### **Output shaft rotates** — 轴旋转方向 `In opposite direction to input shaft`（默认）| `In same direction as input shaft`

从动（输出）驱动轴相对于基座（输入）驱动轴的运动方向。

### 啮合损耗

啮合损耗参数取决于热模型。有关更多信息，请参阅参数依赖关系表。

### **Friction model** — 默认摩擦模型 `No meshing losses - Suitable for HIL simulation`（默认）| `Constant efficiency` | `Load-dependent efficiency` | `Temperature-dependent efficiency` | `Temperature and load-dependent efficiency`

用于估算啮合功率损耗的各种精度级别的摩擦模型。

- `No meshing losses - Suitable for HIL
  simulation` — 忽略齿轮齿之间的摩擦。啮合是理想的。
- `Constant efficiency` —
  通过恒定效率因子减少扭矩传递。该因子在 0 < *η* ≤ 1 范围内，且与负载无关。
- `Load-dependent efficiency`
  — 通过可变效率因子减少扭矩传递。该因子在 0 < *η* <
  1 范围内，且随扭矩负载变化。
- `Temperature-dependent
  efficiency` — 通过取决于温度但不考虑齿轮负载的恒定效率因子减少扭矩传递。该因子在 0 < *η* ≤ 1 范围内，且与负载无关。扭矩传递由用户提供的齿轮效率和温度数据确定。
- `Temperature and load-dependent
  efficiency` — 通过取决于温度和负载的可变效率因子减少扭矩传递。该因子在 0 < *η* <
  1 范围内，且随扭矩负载变化。扭矩传递效率由用户提供的齿轮负载和温度数据确定。

### **Efficiency** — 扭矩传递效率，*η* `0.8`（默认）| `0`≤ *η* < `1`

基座轴与从动轴之间的扭矩传递效率 *η*。效率与啮合功率损耗成反比。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`。

有关更多信息，请参阅参数依赖关系表。

### **Follower power threshold** — 效率因子功率基准 `0.001` `W`（默认）| 正标量

从动轴功率的绝对值，高于此值时完整效率因子生效。低于此值时，双曲正切函数将效率因子平滑至 1，在无功率传输时将效率损耗降至 0。

作为指导原则，功率阈值应低于仿真期间预期的传输功率。较高的值可能导致模块低估效率损耗。非常低的值往往会增加仿真的计算成本。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`。

有关更多信息，请参阅参数依赖关系表。

### **Input shaft torque at no load** — 空载扭矩 `0.1` `N*m`（默认）| 正标量

在怠速模式下，即当传递到输出轴的扭矩等于零时，作用在输入轴上的净扭矩 *τidle*。对于非零值，怠速模式下的功率输入因啮合损耗而完全耗散。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Load-dependent efficiency`。

有关更多信息，请参阅参数依赖关系表。

### **Nominal output torque** — 额定扭矩 `5` `N*m`（默认）| 正标量

用于归一化负载相关效率的输出扭矩 *τ*F。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Load-dependent efficiency`。

有关更多信息，请参阅参数依赖关系表。

### **Efficiency at nominal output torque** — 额定效率，*η* `0.8`（默认）| `0` ≤ *η* < `1` | 标量

额定输出扭矩下的扭矩传递效率 *η*。较大的效率值对应于输入轴和输出轴之间更大的扭矩传递。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Load-dependent efficiency`。

有关更多信息，请参阅参数依赖关系表。

### **Follower angular velocity threshold** — 效率因子角速度基准 `0.01` `rad/s`（默认）| 正标量

从动轴角速度的绝对值，高于此值时完整效率因子 *ωF* 生效。低于此值时，双曲正切函数将效率因子平滑至 1，在静止时将效率损耗降至零。

作为指导原则，角速度阈值应低于仿真期间预期的角速度。较高的值可能导致模块低估效率损耗。非常低的值往往会增加仿真的计算成本。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Load-dependent efficiency`。

有关更多信息，请参阅参数依赖关系表。

### **Temperature** — 温度 `[280, 300, 320]` `K`（默认）| 正数组

用于构建效率查找表的温度数组。数组值必须从左到右递增。在温度相关模型中，温度数组必须与效率数组大小相同。在温度和负载相关模型中，该数组必须与效率矩阵的单行大小相同。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为以下之一：

- `Temperature-dependent
  efficiency`
- `Temperature and load-dependent
  efficiency`

有关更多信息，请参阅参数依赖关系表。

### **Efficiency** — 效率，*η* `[.95, .9, .85]`（默认）| `0` ≤ *η* < `1` | 数组

用于为温度相关效率模型构建一维温度-效率查找表的效率数组。数组值是 **Temperature** 数组中各温度对应的效率。元素数量必须与 **Temperature** 数组中的元素数量相同。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent
efficiency`。

有关更多信息，请参阅参数依赖关系表。

### **Follower power threshold** — 效率因子功率基准 `0.001` `W`（默认）| 正数组

从动轴功率的绝对值，高于此值时完整效率因子 *pF* 生效。低于此值时，双曲正切函数将效率因子平滑至 1，在无功率传输时将效率损耗降至 0。

作为指导原则，功率阈值应低于仿真期间预期的传输功率。较高的值可能导致模块低估效率损耗。非常低的值往往会增加仿真的计算成本。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent
efficiency`。

有关更多信息，请参阅参数依赖关系表。

### **Load at base gear** — 基座齿轮负载 `[1, 5, 10]` `N*m`（默认）| 正数组

用于为温度和负载相关效率模型构建二维温度-负载-效率查找表的基座齿轮负载数组。数组值必须从左到右递增。负载数组必须与效率矩阵的单列大小相同。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature and load-dependent
efficiency`。

有关更多信息，请参阅参数依赖关系表。

### **Efficiency matrix** — 效率 `[.85, .8, .75; .95, .9, .85; .85, .8, .7]`（默认）| 元素为正且范围在 [0,1) 内的数值数组

用于构建二维温度-负载-效率查找表的组件效率矩阵。矩阵元素是 **Temperature** 数组给出的温度和 **Load at base gear** 数组给出的负载下的效率。

行数必须与 **Temperature** 数组中的元素数量相同。列数必须与 **Load at base gear** 数组中的元素数量相同。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature and load-dependent
efficiency`。

有关更多信息，请参阅参数依赖关系表。

### **Follower angular velocity threshold** — 效率因子角速度基准 `0.01` `rad/s`（默认）| 正标量

从动轴角速度的绝对值，高于此值时完整效率因子 *ωF* 生效。低于此值时，双曲正切函数将效率因子平滑至 1，在静止时将效率损耗降至零。

作为指导原则，角速度阈值应低于仿真期间预期的角速度。较高的值可能导致模块低估效率损耗。非常低的值往往会增加仿真的计算成本。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature and load-dependent
efficiency`。

有关更多信息，请参阅参数依赖关系表。

### 齿隙

### **Enable backlash** — 齿隙选项 `off`（默认）| `on`

是否启用齿隙。

### **Hard stop model** — 硬限位过渡行为 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认）| ...

硬限位模型的刚度和回弹选项。您可以从以下选项中选择：

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at bounds,
  undamped rebound`
- `Full stiffness and damping applied at bounds,
  damped rebound`
- `Based on coefficient of
  restitution`

有关更多信息，请参阅 Translational Hard
Stop。

#### 依赖关系

要启用此参数，请选中 **Enable
backlash**。

### **Linear backlash** — 平移齿隙距离 `1e-3` `mm`（默认）| 正标量

齿轮齿在啮合齿之间可以移动的平移距离。

#### 依赖关系

要启用此参数，请选中 **Enable
backlash**。

### **Base (B) gear radius** — 基座齿轮节圆半径 `0.1` `m`（默认）| 正标量

基座齿轮从中心到齿轮齿上啮合点的距离。

#### 依赖关系

要启用此参数，请选中 **Enable
backlash**。

### **Transition region** — 硬限位效应渐变区域 `1e-4` `mm`（默认）| 正标量

模块逐渐施加刚度和阻尼效应的距离。当您将 **Hard stop model** 设置为 `Stiffness and damping applied smoothly through
transition region, damped rebound` 时，模块在硬限位接近全刚度时平滑过渡刚度和阻尼的起始。

#### 依赖关系

要启用此参数，请选中 **Enable
backlash** 并将 **Hard stop model** 设置为 `Stiffness and damping applied smoothly through
transition region, damped rebound`。

### **Linear stiffness** — 抗平移变形阻力 `1e6` `N/m`（默认）| 正标量

齿轮碰撞的有效平移弹簧刚度。

#### 依赖关系

要启用此参数，请选中 **Enable
backlash** 并将 **Hard stop model** 设置为以下选项之一：

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **Linear damping** — 耗散平移能量的趋势 `1e3` `N/(m/s)`（默认）| 正标量

齿轮碰撞的有效平移阻尼。

#### 依赖关系

要启用此参数，请选中 **Enable
backlash** 并将 **Hard stop model** 设置为以下选项之一：

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **Coefficient of restitution** — 碰撞能量损失系数 `0.7`（默认）| 正标量

碰撞期间平移动能的损失。值 `0` 表示非弹性碰撞，值 `1` 表示完全弹性碰撞，即齿轮保留所有动能。默认值 `0` 等效于在齿轮接触时模拟齿轮扭矩，并在齿轮改变方向且齿移动齿隙距离时移除扭矩。

#### 依赖关系

要启用此参数，请选中 **Enable
backlash** 并将 **Hard stop model** 设置为 `Based on coefficient of
restitution`。

### **Static contact speed threshold** — 碰撞前齿轮齿之间的阈值相对速度 `0.001` `m/s`（默认）| 非负标量

齿轮齿与啮合齿锁定的速度阈值 *vtol*。当 *|vTooth| <
vtol* 时，模块设置 *vTooth = 0*。

#### 依赖关系

要启用此参数，请选中 **Enable
backlash** 并将 **Hard stop model** 设置为 `Based on coefficient of
restitution`。

### **Static contact release force threshold** — 从接触模式过渡到自由模式所需的阈值力 `0.001` `N`（默认）| 正标量

将齿轮从静态接触模式释放所需的最小力。

#### 依赖关系

要启用此参数，请选中 **Enable
backlash** 并将 **Hard stop model** 设置为 `Based on coefficient of
restitution`。

### 粘性损耗

### **Viscous friction coefficients at base (B) and follower (F)** — 粘性摩擦系数 `[0, 0]` `N*m/(rad/s)`（默认）| 正数组

包含基座轴和从动轴处生效的粘性摩擦系数的双元素数组。要忽略粘性损耗，请使用默认设置 `[0, 0]`。

### 故障

要启用 **故障** 选项卡，请将 **摩擦模型** 设置为

- `恒定效率`
- `负载相关效率`
- `温度相关效率`
- `温度和负载相关效率`

要修改故障，请创建一个故障，然后在模块对话框中点击 **打开故障属性**。在属性检查器中，点击 **故障行为** 链接以打开故障。

### **齿轮故障** — 对齿轮故障建模的选项 `添加故障`

是否对模块中的故障建模。当您触发故障时，模块将 **故障效率** 参数的值应用于 **故障角度范围** 参数中指定的齿轮范围。要添加故障，请点击 **添加故障** 超链接。

#### 依赖关系

要启用此参数，请将 **啮合损耗** 设置为：

- `恒定效率`
- `负载相关效率`
- `温度相关效率`
- `温度和负载相关效率`

### **故障效率** — 故障效率 `0.05`（默认）| [0,1] 范围内的标量

故障触发时的效率。

#### 依赖关系

要启用此参数，请通过点击 **添加故障** 超链接为模块启用故障。

### **故障角度范围** — 故障角度范围 `pi / 12` `rad`（默认）| 非负标量

故障效率的旋转角度范围。对于 `2π rad` 的倍数，模块在整个旋转过程中应用 **故障效率** 参数的值。

#### 依赖关系

要启用此参数，请通过点击 **添加故障** 超链接为模块启用故障。

### 热端口

### **热质量** — 热质量 `50` `J/K`（默认）| 正标量

使组件温度变化一度所需的热能。热质量越大，组件对温度变化的抵抗力越强。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为以下之一：

- `温度相关效率`
- `温度和负载相关效率`

### **初始温度** — 温度 `300` `K`（默认）| 正标量

仿真开始时的温度。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为以下之一：

- `温度相关效率`
- `温度和负载相关效率`

## 所属库

Simscape / Driveline / Gears

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

### R2024a：使用 Simscape 故障接口对故障建模

Simple Gear 模块现在支持 Simscape 故障接口。要了解更多信息，请参阅 Introduction to Simscape Faults。

### R2023a：间隙更新

由于 Translational Hard Stop 模块的更新，Simple Gear 模块在建模间隙时提供了新选项。以前，该模块使用 **间隙模型** 下拉参数。现在，您可以在选择 **启用间隙** 时启用间隙。

更新后的 **硬止点模型** 参数提供了与 Translational Hard Stop 模块相同的选项。参数名称与 Translational Hard Stop 模块中引入的新选项保持一致。

## 描述

具有可调齿轮比、摩擦损耗和触发故障的基轮和从动轮简单齿轮

Simple Gear 模块表示一个齿轮箱，它将基齿轮 *B* 和从动齿轮 *F* 的连接传动轴约束为以您指定的固定比率同转。您可以选择从动轴与基轴旋转方向相同还是相反。如果它们沿相同方向旋转，从动齿轮的角速度 *ωF* 和基齿轮的角速度 *ωB* 具有相同的符号。如果它们沿相反方向旋转，*ωF* 和 *ωB* 具有相反的符号。您可以轻松添加和移除间隙、故障和热效应。

### 理想齿轮约束和齿轮比

Simple Gear 模块对两个连接轴施加的运动学约束为

rFωF=rBωB

其中：

- *rF* 是从动齿轮的半径。
- *ωF* 是从动齿轮的角速度。
- *rB* 是基齿轮的半径。
- *ωB* 是基齿轮的角速度。

从动齿轮与基齿轮的齿轮比为

gFB=rFrB=NFNB

其中：

- *NB* 是基齿轮的齿数。
- *NBF* 是从动齿轮的齿数。

将两个自由度缩减为一个独立自由度，得到扭矩传递方程

gFBτB+τF−τloss=0

其中：

- *τB* 是输入扭矩。
- *τF* 是输出扭矩。
- *τloss* 是由于摩擦引起的扭矩损耗。

对于理想情况，τloss=0。

### 非理想齿轮约束和损耗

在非理想情况下，τloss≠0。关于非理想齿轮建模的一般考虑，请参阅 Model Gears with Losses。

在非理想齿轮对 (B,F) 中，角速度、齿轮半径和齿轮齿数约束保持不变。但传递的扭矩和功率因以下因素而减少：

- 齿轮 *B* 和 *F* 上齿面之间的库仑摩擦，由效率 *η* 表征
- 驱动轴与轴承的粘性耦合，由粘性摩擦系数 *μ* 参数化

**恒定效率**

在恒定效率情况下，*η* 是常数，与负载或传递的功率无关。

**负载相关效率**

在负载相关效率情况下，*η* 取决于负载或通过齿轮传递的功率。对于任一功率流，

τCoul=gFBτidle+kτF

其中：

- *τCoul* 是库仑摩擦相关扭矩。
- *k* 是比例常数。
- *τidle* 是空载模式下作用在输入轴上的净扭矩。

效率 *η* 以标准的前述形式与 *τCoul* 相关，但变为负载相关：

η=τFgFBτidle+(k+1)τF

### 间隙

您可以在模型中纳入间隙的影响。*间隙* 是齿轮齿与配合齿轮齿之间的多余空间。增加间隙可以补偿降低的制造公差，并允许润滑剂在齿轮中自由运动以防止卡滞。然而，过大的间隙可能导致系统组件过早磨损，并可能影响依赖齿轮位置的测量。该模块使用 Translational Hard Stop 模块的实现，在启动和反转时应用间隙。

当您选择 **启用间隙** 时，模块将齿轮旋转与线性间隙关联为：

vTooth=rBωB−βrFωF，

其中：

- *vTooth* 是齿轮齿的相对线速度。
- *rB* 是 **基齿轮 (B) 半径** 参数。
- *rF* 是从动齿轮半径，其中 *rF = NF/NB·**rB*，**从动齿轮 (F) 与基齿轮 (B) 齿数比 (NF/NB)** 参数表示 *NF/NB*。
- *ωB* 和 *ωF* 分别是基齿轮和从动齿轮的角速度。
- *β* 是齿轮方向符号。当您将：

  - **输出轴旋转** 设置为 `与输入轴方向相同`，*β = 1*。
  - **输出轴旋转** 设置为 `与输入轴方向相反`，*β = -1*。

模块将啮合齿轮齿视为位置 *xTooth*，相对于线性间隙 *Backlash*，其中 *-1/2·Backlash < xTooth < 1/2·Backlash*。*Backlash* 等同于 **线性间隙** 参数。**间隙位置** 变量的初始值等同于 *xTooth* 的初始位置。

当您将 **硬止点模型** 设置为 `基于恢复系数` 时，硬止点可以将 **恢复系数** 参数 *coeffrest* 的非零值纳入动量平衡方程。在碰撞期间，

coeffrest=vBacklash,t−vBacklash,t+，

其中 *t-* 和 *t+* 分别是碰撞前和碰撞后的时刻。模块断言 *coeffrest* 在 [0, 1] 范围内。有关更多信息，请参阅 State Reset Modeling。Simscape™ 将齿轮的模式状态记录为中间量 **M**。

| 状态 | 值 |
| --- | --- |
| *M = 0* | 脱离 |
| *M = 1* | 正向啮合，*xtooth = 1/2·Backlash* |
| *M = -1* | 反向啮合，*xtooth = -1/2·Backlash* |
| *M = 2* | 正向啮合与正向脱离之间的瞬时模式转换 |
| *M = -2* | 反向啮合与反向脱离之间的瞬时模式转换 |
| *M = 3* | 瞬时冲击模式 |

硬止点模拟边界处的静态接触。当发生碰撞且 *|vTooth| < vtol* 时，齿轮锁定。一旦齿轮锁定，*vTooth* = 0。一旦 *fTooth* > *fTol*，齿轮解锁，其中

- *fTol* 是 **静态接触释放力阈值** 参数。
- *vtol* 是 **静态接触速度阈值** 参数。
- *fTooth* 是齿轮齿之间的啮合力，使得 *fTooth* = *TB/rB* = *TF/rF*。

### 故障

要在 Simple Gear 模块中对故障建模，请在 **故障** 部分中，点击您要建模的故障旁边的 **添加故障** 超链接。有关故障建模的更多信息，请参阅 Fault Behavior Modeling and Fault Triggering。

当您触发故障时，模块将 **故障效率** 参数的值应用于 **故障角度范围** 参数中指定的齿轮范围。

### 热模型

您可以通过启用可选热端口来对热流和温度变化的影响建模。要启用该端口，请将 **摩擦模型** 设置为 `温度相关效率`。

此外，您可以通过将 **摩擦模型** 设置为 `温度和负载相关效率` 来选择对随负载和温度变化的效率建模。选择热变体：

- 暴露端口 **H**，热域中的守恒端口。
- 启用 **热质量** 参数，允许您指定组件抵抗温度变化的能力。
- 启用 **初始温度** 参数，允许您设置初始温度。

### 变量

使用 **变量** 设置在仿真前为模块变量设置优先级和初始目标值。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。
