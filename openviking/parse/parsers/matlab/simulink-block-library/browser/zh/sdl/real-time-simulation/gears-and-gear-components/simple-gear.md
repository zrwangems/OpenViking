---
type: simulink-block
title: 'Simple Gear'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Gears / Gear Assemblies'
documentation_page: 'simplegear'
documentation_source_path: 'ref/simplegear.html'
language: zh-CN
chinese_source: worker-translation
---

# Simple Gear

## 端口

### 守恒

### **B** — 基座旋转机械

与基座轴关联的机械旋转守恒端口。

### **F** — 从动旋转机械

与从动轴关联的机械旋转守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。热流影响齿轮温度，因此影响动力传输效率。

#### 依赖关系

要启用此端口，请将 **摩擦模型** 设置为以下任一值：

- `Temperature-dependent
  efficiency`
- `Temperature and load-dependent
  efficiency`

## 参数

### 参数依赖关系表

该表显示了某些 **啮合损耗** 参数和 **故障** 参数的可见性如何取决于热模型以及为其他参数选择的选项。

| 默认模型 — 对于非热模型，热端口 **H** 不可见。 | | | | | | 热模型 — 对于热模型，热端口 **H** 可见。 | |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 啮合损耗 | | | | | | 啮合损耗 | |
| 摩擦模型 — 选择 `No meshing losses - Suitable for HIL simulation`、`Constant efficiency` 或 `Load-dependent efficiency` | | | | | | 摩擦模型 — 选择 `Temperature-dependent efficiency` 或 `Temperature and load-dependent efficiency` | |
| **No meshing losses - Suitable for HIL simulation** | **Constant efficiency** | | | **Load-dependent efficiency** | | **Temperature-dependent efficiency** | **Temperature and load-dependent efficiency** |
| 效率 | | | | 空载输入轴扭矩 | | 温度 | 温度 |
| 从动功率阈值 | | | | 额定输出扭矩 | | 效率 | 基座齿轮负载 |
|  | | | | 额定输出扭矩下的效率 | | 从动功率阈值 | 效率矩阵 |
|  | | | | 从动角速度阈值 | | 从动角速度阈值 |

### 主要

### **从动齿轮 (F) 与基座齿轮 (B) 齿数比 (NF/NB)** — 齿轮比 `2`（默认） | 正标量

从动轴与基座轴的固定比 *gFB*。齿轮比必须严格为正。

### **输出轴旋转** — 轴旋转方向 `In opposite direction to input shaft`（默认） | `In same direction as input shaft`

从动（输出）驱动轴相对于基座（输入）驱动轴的运动方向。

### 啮合损耗

啮合损耗参数取决于热模型。有关详细信息，请参阅参数依赖关系表。

### **摩擦模型** — 默认摩擦模型 `No meshing losses - Suitable for HIL simulation`（默认） | `Constant efficiency` | `Load-dependent efficiency` | `Temperature-dependent efficiency` | `Temperature and load-dependent efficiency`

用于估计啮合引起的功率损耗的各种精度级别的摩擦模型。

- `No meshing losses - Suitable for HIL simulation` — 忽略齿轮齿之间的摩擦。啮合是理想的。
- `Constant efficiency` — 通过恒定效率因子降低扭矩传递。该因子位于 0 < *η* ≤ 1 范围内，且与负载无关。
- `Load-dependent efficiency` — 通过可变效率因子降低扭矩传递。该因子位于 0 < *η* < 1 范围内，并随扭矩负载变化。
- `Temperature-dependent efficiency` — 通过依赖于温度但不考虑齿轮负载的恒定效率因子降低扭矩传递。该因子位于 0 < *η* ≤ 1 范围内，且与负载无关。扭矩传递由用户提供的齿轮效率和温度数据确定。
- `Temperature and load-dependent efficiency` — 通过依赖于温度和负载的可变效率因子降低扭矩传递。该因子位于 0 < *η* < 1 范围内，并随扭矩负载变化。扭矩传递效率由用户提供的齿轮负载和温度数据确定。

### **效率** — 扭矩传递效率，*η* `0.8`（默认） | `0`≤ *η* < `1`

基座轴和从动轴之间的扭矩传递效率 *η*。效率与啮合功率损耗成反比。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Constant efficiency`。

有关详细信息，请参阅参数依赖关系表。

### **从动功率阈值** — 效率因子功率基准 `0.001` `W`（默认） | 正标量

从动轴功率的绝对值，高于该值时完整效率因子生效。低于该值时，双曲正切函数将效率因子平滑到 1，从而在未传输功率时将效率损耗降至 0。

作为指导原则，功率阈值应低于仿真期间预期的传输功率。较高的值可能导致模块低估效率损耗。非常低的值往往会提高仿真的计算成本。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Constant efficiency`。

有关详细信息，请参阅参数依赖关系表。

### **空载输入轴扭矩** — 空载扭矩 `0.1` `N*m`（默认） | 正标量

在空载模式下，即传递到输出轴的扭矩等于零时，作用于输入轴的净扭矩 *τidle*。对于非零值，空载模式下的功率输入因啮合损耗而完全耗散。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Load-dependent efficiency`。

有关详细信息，请参阅参数依赖关系表。

### **额定输出扭矩** — 额定扭矩 `5` `N*m`（默认） | 正标量

用于对负载相关效率进行归一化的输出扭矩 *τ*F。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Load-dependent efficiency`。

有关详细信息，请参阅参数依赖关系表。

### **额定输出扭矩下的效率** — 额定效率，*η* `0.8`（默认） | `0` ≤ *η* < `1` | 标量

额定输出扭矩下的扭矩传递效率 *η*。较大的效率值对应于输入轴和输出轴之间更大的扭矩传递。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Load-dependent efficiency`。

有关详细信息，请参阅参数依赖关系表。

### **从动角速度阈值** — 效率因子角速度基准 `0.01` `rad/s`（默认） | 正标量

从动轴角速度的绝对值，高于该值时完整效率因子生效，*ωF*。低于该值时，双曲正切函数将效率因子平滑到 1，从而在静止时将效率损耗降至零。

作为指导原则，角速度阈值应低于仿真期间预期的角速度。较高的值可能导致模块低估效率损耗。非常低的值往往会提高仿真的计算成本。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Load-dependent efficiency`。

有关详细信息，请参阅参数依赖关系表。

### **温度** — 温度 `[280, 300, 320]` `K`（默认） | 正数组

用于构造效率查找表的温度数组。数组值必须从左到右递增。在温度相关模型中，温度数组必须与效率数组大小相同。在温度和负载相关模型中，该数组必须与效率矩阵的单行大小相同。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为以下任一值：

- `Temperature-dependent
  efficiency`
- `Temperature and load-dependent
  efficiency`

有关详细信息，请参阅参数依赖关系表。

### **效率** — 效率，*η* `[.95, .9, .85]`（默认） | `0` ≤ *η* < `1` | 数组

用于为温度相关效率模型构造一维温度-效率查找表的效率数组。数组值是在 **温度** 数组中的温度下的效率。元素数量必须与 **温度** 数组中的元素数量相同。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Temperature-dependent
efficiency`。

有关详细信息，请参阅参数依赖关系表。

### **从动功率阈值** — 效率因子功率基准 `0.001` `W`（默认） | 正数组

从动轴功率的绝对值，高于该值时完整效率因子生效，*pF*。低于该值时，双曲正切函数将效率因子平滑到 1，从而在未传输功率时将效率损耗降至 0。

作为指导原则，功率阈值应低于仿真期间预期的传输功率。较高的值可能导致模块低估效率损耗。非常低的值往往会提高仿真的计算成本。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Temperature-dependent
efficiency`。

有关详细信息，请参阅参数依赖关系表。

### **基座齿轮负载** — 基座齿轮负载 `[1, 5, 10]` `N*m`（默认） | 正数组

用于为温度和负载相关效率模型构造二维温度-负载效率查找表的基座齿轮负载数组。数组值必须从左到右递增。负载数组必须与效率矩阵的单列大小相同。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Temperature and load-dependent
efficiency`。

有关详细信息，请参阅参数依赖关系表。

### **效率矩阵** — 效率 `[.85, .8, .75; .95, .9, .85; .85, .8, .7]`（默认） | 元素为正值且位于 [0,1) 范围内的数值数组

用于构造二维温度-负载效率查找表的组件效率矩阵。矩阵元素是在 **温度** 数组给定的温度下以及 **基座齿轮负载** 数组给定的负载下的效率。

行数必须与 **温度** 数组中的元素数量相同。列数必须与 **基座齿轮负载** 数组中的元素数量相同。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Temperature and load-dependent
efficiency`。

有关详细信息，请参阅参数依赖关系表。

### **从动角速度阈值** — 效率因子角速度基准 `0.01` `rad/s`（默认） | 正标量

从动轴角速度的绝对值，高于该值时完整效率因子生效，*ωF*。低于该值时，双曲正切函数将效率因子平滑到 1，从而在静止时将效率损耗降至零。

作为指导原则，角速度阈值应低于仿真期间预期的角速度。较高的值可能导致模块低估效率损耗。非常低的值往往会提高仿真的计算成本。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Temperature and load-dependent
efficiency`。

有关详细信息，请参阅参数依赖关系表。

### 齿隙

### **启用齿隙** — 齿隙选项 `off`（默认） | `on`

是否启用齿隙。

### **硬停止模型** — 硬停止转换行为 `Stiffness and damping applied smoothly through transition region, damped rebound`（默认） | ...

硬停止模型的刚度和回弹选项。可以从以下选项中选择：

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at bounds,
  undamped rebound`
- `Full stiffness and damping applied at bounds,
  damped rebound`
- `Based on coefficient of
  restitution`

有关详细信息，请参阅 Translational Hard Stop。

#### 依赖关系

要启用此参数，请选择 **启用齿隙**。

### **线性齿隙** — 平移齿隙距离 `1e-3` `mm`（默认） | 正标量

齿轮齿在啮合齿之间可以移动的平移距离。

#### 依赖关系

要启用此参数，请选择 **启用齿隙**。

### **基座齿轮 (B) 半径** — 基座齿轮节圆半径 `0.1` `m`（默认） | 正标量

基座齿轮从中心到齿轮齿上啮合点的距离。

#### 依赖关系

要启用此参数，请选择 **启用齿隙**。

### **过渡区域** — 硬停止效果的渐变区域 `1e-4` `mm`（默认） | 正标量

模块逐渐施加刚度和阻尼效果的距离。当您将 **硬停止模型** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound` 时，模块会在硬停止接近完全刚度时平滑过渡刚度和阻尼的起始。

#### 依赖关系

要启用此参数，请选择 **启用齿隙** 并将 **硬停止模型** 设置为 `Stiffness and damping applied smoothly through transition region, damped rebound`。

### **线性刚度** — 抗平移变形 `1e6` `N/m`（默认） | 正标量

齿轮碰撞的有效平移弹簧刚度。

#### 依赖关系

要启用此参数，请选择 **启用齿隙** 并将 **硬停止模型** 设置为以下选项之一：

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **线性阻尼** — 耗散平移能量的趋势 `1e3` `N/(m/s)`（默认） | 正标量

齿轮碰撞的有效平移阻尼。

#### 依赖关系

要启用此参数，请选择 **启用齿隙** 并将 **硬停止模型** 设置为以下选项之一：

- `Stiffness and damping applied smoothly
  through transition region, damped
  rebound`
- `Full stiffness and damping applied at
  bounds, undamped rebound`
- `Full stiffness and damping applied at
  bounds, damped rebound`

### **恢复系数** — 碰撞能量损失系数 `0.7`（默认） | 正标量

碰撞期间平移动能的损失。值 `0` 表示非弹性碰撞，值 `1` 表示完全弹性碰撞，其中齿轮保留所有动能。默认值 `0` 等效于在齿轮接触时模拟齿轮扭矩，并在齿轮改变方向且齿移动齿隙距离时移除扭矩。

#### 依赖关系

要启用此参数，请选择 **启用齿隙** 并将 **硬停止模型** 设置为 `Based on coefficient of
restitution`。

### **静接触速度阈值** — 碰撞前齿轮齿之间的相对速度阈值 `0.001` `m/s`（默认） | 非负标量

速度 *vtol*，低于该值时齿轮齿与啮合齿锁定。当 *|vTooth| < vtol* 时，模块设置 *vTooth = 0*。

#### 依赖关系

要启用此参数，请选择 **启用齿隙** 并将 **硬停止模型** 设置为 `Based on coefficient of
restitution`。

### **静接触释放力阈值** — 从接触模式转换到自由模式所需的阈值力 `0.001` `N`（默认） | 正标量

使齿轮从静接触模式释放所需的最小力。

#### 依赖关系

要启用此参数，请选择 **启用齿隙** 并将 **硬停止模型** 设置为 `Based on coefficient of
restitution`。

### 粘性损耗

### **基座 (B) 和从动 (F) 处的粘性摩擦系数** — 粘性摩擦系数 `[0, 0]` `N*m/(rad/s)`（默认） | 正数组

包含在基座轴和从动轴处生效的粘性摩擦系数的二元素数组。要忽略粘性损耗，请使用默认设置 `[0, 0]`。

### 故障

要启用 **Faults** 选项卡，请将 **Friction model** 设置为

- `Constant efficiency`
- `Load-dependent efficiency`
- `Temperature-dependent efficiency`
- `Temperature and load-dependent efficiency`

要修改故障，请创建故障，然后在模块对话框中点击 **Open fault properties**。在属性检查器中，点击 **Fault behavior** 链接以打开故障。

### **Gear fault** — 对齿轮故障建模的选项 `Add fault`

是否对模块中的故障建模。触发故障时，模块会将 **Faulted efficiency** 参数的值应用于 **Faulted angle range** 参数所指定的齿轮范围。要添加故障，请点击 **Add fault** 超链接。

#### 依赖关系

要启用此参数，请将 **Meshing Losses** 设置为：

- `Constant efficiency`
- `Load-dependent efficiency`
- `Temperature-dependent efficiency`
- `Temperature and load-dependent efficiency`

### **Faulted efficiency** — 故障效率 `0.05`（默认） | [0,1] 范围内的标量

故障触发时的效率。

#### 依赖关系

要启用此参数，请通过点击 **Add fault** 超链接为模块启用故障。

### **Faulted angle range** — 故障角度范围 `pi / 12` `rad`（默认） | 非负标量

故障效率的旋转角度范围。对于 `2π rad` 的整数倍，模块在整个旋转过程中都应用 **Faulted efficiency** 参数的值。

#### 依赖关系

要启用此参数，请通过点击 **Add fault** 超链接为模块启用故障。

### 热端口

### **Thermal mass** — 热质量 `50` `J/K`（默认） | 正标量

将组件温度改变一度所需的热能。热质量越大，组件抵抗温度变化的能力越强。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为以下之一：

- `Temperature-dependent efficiency`
- `Temperature and load-dependent efficiency`

### **Initial temperature** — 温度 `300` `K`（默认） | 正标量

仿真开始时的温度。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为以下之一：

- `Temperature-dependent efficiency`
- `Temperature and load-dependent efficiency`

## 所属库

Simscape / Driveline / Gears

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

### R2024a：使用 Simscape 故障接口对故障建模

Simple Gear 模块现在支持 Simscape 故障接口。要了解更多信息，请参阅 Simscape 故障简介。

### R2023a：齿隙更新

由于 Translational Hard Stop 模块的更新，Simple Gear 模块在对齿隙建模时提供了新选项。以前，该模块使用 **Backlash model** 下拉参数。现在，选择 **Enable backlash** 即可启用齿隙。

更新后的 **Hard stop model** 参数提供与 Translational Hard Stop 模块相同的选项。参数名称与 Translational Hard Stop 模块中引入的新选项保持一致。

## 描述

具有可调齿轮比、摩擦损耗和触发故障的基轮和从动轮简单齿轮

Simple Gear 模块表示一个齿轮箱，它将基齿轮 *B* 和从动齿轮 *F* 的连接传动系统轴约束为以您指定的固定比率一起旋转。您可以选择从动轴是与基轴同向旋转还是反向旋转。如果它们沿相同方向旋转，则从动轮的角速度 *ωF* 与基轮的角速度 *ωB* 符号相同。如果它们沿相反方向旋转，则 *ωF* 与 *ωB* 符号相反。您可以轻松添加和移除齿隙、故障和热效应。

### 理想齿轮约束与齿轮比

Simple Gear 模块对两个连接轴施加的运动学约束为

rFωF=rBωB

其中：

- *rF* 是从动齿轮的半径。
- *ωF* 是从动齿轮的角速度。
- *rB* 是基齿轮的半径。
- *ωB* 是基齿轮的角速度。

从动齿轮-基齿轮比为

gFB=rFrB=NFNB

其中：

- *NB* 是基齿轮的齿数。
- *NBF* 是从动齿轮的齿数。

将两个自由度减少为一个独立自由度可得到扭矩传递方程

gFBτB+τF−τloss=0

其中：

- *τB* 是输入扭矩。
- *τF* 是输出扭矩。
- *τloss* 是由摩擦引起的扭矩损失。

对于理想情况，τloss=0。

### 非理想齿轮约束与损耗

在非理想情况下，τloss≠0。有关非理想齿轮建模的一般注意事项，请参阅带损耗的齿轮建模。

在非理想齿轮对 (B,F) 中，角速度、齿轮半径和齿轮齿约束保持不变。但传递的扭矩和功率会因以下因素而降低：

- 齿轮 *B* 和 *F* 的齿面之间的库仑摩擦，由效率 *η* 表征
- 传动轴与轴承的粘性耦合，由粘性摩擦系数 *μ* 参数化

**Constant Efficiency**

在恒定效率情况下，*η* 是常数，与传递的负载或功率无关。

**Load-Dependent Efficiency**

在负载相关效率情况下，*η* 取决于通过齿轮传递的负载或功率。对于任一功率流方向，

τCoul=gFBτidle+kτF

其中：

- *τCoul* 是库仑摩擦相关扭矩。
- *k* 是比例常数。
- *τidle* 是空载模式下作用在输入轴上的净扭矩。

效率 *η* 与 *τCoul* 的关系采用上述标准形式，但会变得依赖于负载：

η=τFgFBτidle+(k+1)τF

### 齿隙

您可以在模型中纳入齿隙的影响。*Backlash* 是齿轮齿与配对齿轮齿之间的多余空间。增加齿隙可补偿降低的制造公差，并允许齿轮中的润滑剂自由运动以防止卡滞。但是，过大的齿隙会导致系统组件过早磨损，并可能影响依赖齿轮位置的测量。该模块使用 Translational Hard Stop 模块的实现，在启动和换向时应用齿隙。

当您选择 **Enable backlash** 时，模块将齿轮旋转与线性齿隙关联如下：

vTooth=rBωB−βrFωF,

其中：

- *vTooth* 是齿轮齿的相对线速度。
- *rB* 是 **Base (B) gear radius** 参数。
- *rF* 是从动齿轮半径，其中 *rF = NF/NB·rB*，并且 **Follower (F) to base (B) teeth ratio (NF/NB)** 参数表示 *NF/NB*。
- *ωB* 和 *ωF* 分别是基齿轮和从动齿轮的角速度。
- *β* 是齿轮方向符号。当您设置：

  - **Output shaft rotates** 为 `In same direction as input shaft` 时，*β = 1*。
  - **Output shaft rotates** 为 `In opposite direction as input shaft` 时，*β = -1*。

该模块将啮合齿轮齿视为相对于线性齿隙 *Backlash* 的位置 *xTooth*，其中 *-1/2·Backlash < xTooth < 1/2·Backlash*。*Backlash* 等效于 **Linear backlash** 参数。**Backlash position** 变量的初始值等效于 *xTooth* 的初始位置。

当您将 **Hard stop model** 设置为 `Based on coefficient of restitution` 时，硬停止可以将 **Coefficient of restitution** 参数 *coeffrest* 的非零值纳入动量平衡方程。在碰撞期间，

coeffrest=vBacklash,t−vBacklash,t+,

其中 *t-* 和 *t+* 分别是碰撞前和碰撞后的时刻。该模块断言 *coeffrest* 在范围 [0, 1] 内。有关更多信息，请参阅状态重置建模。Simscape™ 将齿轮的模式状态记录为中间量 **M**。

| 状态 | 值 |
| --- | --- |
| *M = 0* | 脱离 |
| *M = 1* | 正向啮合，*xtooth = 1/2·Backlash* |
| *M = -1* | 反向啮合，*xtooth = -1/2·Backlash* |
| *M = 2* | 正向啮合与正向脱离之间的瞬时模式转换 |
| *M = -2* | 反向啮合与反向脱离之间的瞬时模式转换 |
| *M = 3* | 瞬时冲击模式 |

硬停止在边界处模拟静态接触。当发生碰撞且 *|vTooth| < vtol* 时，齿轮锁止。一旦齿轮锁止，*vTooth* = 0。一旦 *fTooth* > *fTol*，齿轮解锁，其中

- *fTol* 是 **Static contact release force threshold** 参数。
- *vtol* 是 **Static contact speed threshold** 参数。
- *fTooth* 是齿轮齿之间的啮合力，使得 *fTooth* = *TB/rB* = *TF/rF*。

### 故障

要对 Simple Gear 模块中的故障建模，请在 **Faults** 部分中，点击要建模的故障旁边的 **Add fault** 超链接。有关故障建模的更多信息，请参阅故障行为建模和故障触发。

当您触发故障时，模块会将 **Faulted efficiency** 参数的值应用于 **Faulted angle range** 参数所指定的齿轮范围。

### 热模型

您可以通过启用可选热端口来对热流和温度变化的影响建模。要启用该端口，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

此外，您可以选择通过将 **Friction model** 设置为 `Temperature and load-dependent efficiency` 来对随负载和温度变化的效率建模。选择热变体会：

- 公开端口 **H**，这是热域中的守恒端口。
- 启用 **Thermal mass** 参数，该参数允许您指定组件抵抗温度变化的能力。
- 启用 **Initial Temperature** 参数，该参数允许您设置初始温度。

### 变量

使用 **Variables** 设置可在仿真前设置模块变量的优先级和初始目标值。有关更多信息，请参阅设置模块变量的优先级和初始目标。
