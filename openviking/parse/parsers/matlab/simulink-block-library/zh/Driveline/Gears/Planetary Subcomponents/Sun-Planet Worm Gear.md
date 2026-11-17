---
type: simulink-block
title: 'Sun-Planet Worm Gear'
family: 'gears'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears / Planetary Subcomponents'
documentation_page: 'sunplanetwormgear'
documentation_source_path: 'ref/sunplanetwormgear.html'
language: zh-CN
chinese_source: worker-translation
---

# Sun-Planet Worm Gear

## 端口

### 守恒

### **C** — 行星齿轮架旋转机械

与行星齿轮架关联的旋转机械守恒端口。

### **W** — 蜗杆旋转机械

与蜗杆关联的旋转机械守恒端口。

### **S** — 太阳轮旋转机械

与太阳轮关联的旋转机械守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。热流通过改变齿轮温度影响功率传输效率。

#### 依赖关系

要启用此端口，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

## 参数

### 主要

### **齿轮比** — 齿轮比 `25` (默认) | positive scalar

齿轮或传动比，*RWG*，表示蜗杆角速度除以太阳轮角速度。此齿轮比必须严格为正。

### **蜗杆螺纹类型** — 螺纹旋转方向 `Right-hand` (默认) | `Left-hand`

正蜗杆旋转的方向。如果选择 `Left-hand`，正蜗杆旋转会导致负齿轮旋转。

### 啮合损失

该表显示了为 **摩擦模型** 选择的选项如何影响 **啮合损失** 选项卡中其他参数的可见性。

**啮合损失参数依赖关系**

| 啮合损失设置参数和值 | | | | | |
| --- | --- | --- | --- | --- | --- |
| **摩擦模型** | | | | | |
| `No meshing losses - Suitable for HIL simulation` | | `Constant efficiency` | | `Temperature-dependent efficiency` | |
| **摩擦参数化** | | **温度** | |
| `Friction coefficient and geometrical parameters` | `Efficiencies` |
| **法向压力角** | **蜗杆-齿轮效率** | **蜗杆-齿轮效率** | |
| **导程角** | **齿轮-蜗杆效率** | **齿轮-蜗杆效率** | |
| **摩擦系数** |
| **功率阈值** | **功率阈值** | **功率阈值** | |

### **摩擦模型** — 摩擦模型 `No meshing losses - Suitable for HIL simulation` (默认) | `Constant efficiency` | `Temperature-dependent efficiency`

模块的摩擦模型：

- `No meshing losses - Suitable for HIL simulation` — 齿轮啮合是理想的。
- `Constant efficiency` — 齿轮轮对之间的扭矩传递由恒定效率 *η* 降低，使得 0 < *η* ≤ 1。
- `Temperature-dependent efficiency` — 齿轮轮对之间的扭矩传递由基于温度的表查找定义。

### **摩擦参数化** — 摩擦参数化方法 `Friction coefficient and geometrical parameters` (默认) | `Efficiencies`

齿轮螺纹之间摩擦的表征：

- `Friction coefficient and geometrical parameters` — 摩擦由几何表面接触摩擦确定。
- `Efficiencies` — 摩擦由恒定效率确定，其中 0 < *η* < 1。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Constant efficiency`。

### **法向压力角** — 螺纹压力角 `17.5` `deg` (默认) | scalar

法向平面中的螺纹压力角，*α*。该值必须大于零且小于 90 度。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Constant efficiency`，并将 **摩擦参数化** 设置为 `Friction coefficient and geometrical parameters`。

### **导程角** — 螺纹螺旋角 `20` `deg` (默认) | positive scalar

螺纹螺旋角，其中 *λ* = arctan[*L*/(*π**d*)]。*L* 是蜗杆导程，*d* 是蜗杆节圆直径。此值必须大于零。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Constant efficiency`，并将 **摩擦参数化** 设置为 `Friction coefficient and geometrical parameters`。

### **摩擦系数** — 螺纹摩擦 `0.08` (默认) | positive scalar

螺纹中法向摩擦的无量纲系数。必须大于零。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Constant efficiency`，并将 **摩擦参数化** 设置为 `Friction coefficient and geometrical parameters`。

### **温度** — 温度 `[280, 300, 320]` `K` (默认) | vector

用于构造一维温度-效率查找表的温度向量。向量元素必须从左到右递增。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

### **蜗杆-齿轮效率** — 从蜗杆传递到太阳轮的扭矩传递效率 `[.75, .65, .6]` 或 `0.74` (默认) | vector or scalar

描述从蜗杆流向太阳轮的功率的输出-输入功率比向量，*ηWG*。当您将 **摩擦模型** 设置为 `Constant efficiency` 时，请将该值指定为 scalar。当您将 **摩擦模型** 设置为 `Temperature-dependent efficiency` 时，请将该值指定为 vector。模块使用向量值构造一维温度-效率查找表。

每个元素是与 **温度** 向量中的温度相关的效率。向量的长度必须等于 **温度** 向量的长度。向量中的每个元素必须在范围 (0,1] 内。

#### 依赖关系

要启用此参数，请设置以下任一：

- **摩擦模型** 为 `Constant efficiency`，且 **摩擦参数化** 为 `Efficiencies` — 在这种情况下，请将该值指定为 scalar。
- **摩擦模型** 为 `Temperature-dependent efficiency` — 在这种情况下，请将该值指定为 vector。

### **齿轮-蜗杆效率** — 从太阳轮传递到蜗杆的扭矩传递效率 `[.5, .45, .4]` 或 `0.65` (默认) | vector or scalar

描述从太阳轮流向蜗杆的功率的输出-输入功率比向量，*ηGW*。当您将 **摩擦模型** 设置为 `Constant efficiency` 时，请将该值指定为 scalar。当您将 **摩擦模型** 设置为 `Temperature-dependent efficiency` 时，请将该值指定为 vector。模块使用向量值构造一维温度-效率查找表。

每个元素是与 **温度** 向量中的温度相关的效率。向量的长度必须等于 **温度** 向量的长度。向量中的每个元素必须在范围 (0,1] 内。

#### 依赖关系

要启用此参数，请设置以下任一：

- **摩擦模型** 为 `Constant efficiency`，且 **摩擦参数化** 为 `Efficiencies` — 在这种情况下，请将该值指定为 scalar。
- **摩擦模型** 为 `Temperature-dependent efficiency` — 在这种情况下，请将该值指定为 vector。

### **功率阈值** — 最小效率功率阈值 `0.001` `W` (默认) | scalar

功率阈值，*pth*，高于该值时全效率生效。低于此值时，双曲正切函数会平滑效率因子。

当您将 **摩擦模型** 设置为 `Constant efficiency` 时，模块在无功率传输时将效率损失降为零。当您将 **摩擦模型** 设置为 `Temperature-dependent efficiency` 时，该函数在静止时为零与功率阈值处温度-效率查找表提供的值之间平滑效率因子。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Constant efficiency` 或 `Temperature-dependent efficiency`。

### 粘性损失

### **蜗杆-行星架和太阳轮-行星架粘性摩擦系数** — 齿轮粘性摩擦 `[0, 0]` `N*m/(rad/s)` (默认) | vector

分别用于蜗杆-行星架和太阳轮-行星架轴的粘性摩擦系数向量 [*μWC* *μSC*]。

### 热端口

要启用此参数，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

### **热质量** — 热质量 `50` `J/K` (默认) | scalar

使组件温度变化一个温度单位所需的热能。热质量越大，组件对温度变化的抵抗越强。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

## 所属库

Simscape / Driveline / Gears / Planetary Subcomponents

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

## 描述

具有可调齿轮比、蜗杆螺纹类型和摩擦损失的由行星架、蜗杆行星轮和太阳轮组成的行星齿轮组

Sun-Planet Worm Gear 模块表示一个二自由度行星齿轮，由行星架以及太阳轮和行星轮构成。按类型来说，太阳轮和行星轮是交叉斜齿轮，布置为蜗杆传动，其中行星轮是蜗杆。此类传动用于 Torsen® T-1 差速器。传输功率时，太阳轮可由蜗杆（行星）齿轮、行星架或两者独立旋转。

您指定一个固定齿轮比，它表示蜗杆角速度除以太阳轮角速度。您通过将蜗杆螺纹类型设置为 left-hand 或 right-hand 来控制方向。右旋蜗杆沿正方向旋转会使太阳轮沿正方向旋转。太阳轮和行星架的正方向相同。

### 热模型

您可以通过启用可选热端口来对热流和温度变化的影响进行建模。要启用该端口，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

### 方程

**变量**

方程变量为：

|  |  |
| --- | --- |
| *RWG* | 齿轮比，表示蜗杆角速度除以太阳轮角速度：对于右旋蜗杆该比值为正，对于左旋蜗杆为负 |
| *ωS* | 太阳轮角速度 |
| *ωP* | 蜗杆角速度 |
| *ωC* | 行星架角速度 |
| *ωSC* | 太阳轮相对于行星架的角速度 |
| *α* | 法向压力角 |
| *λ* | 蜗杆导程角 |
| *L* | 蜗杆导程 |
| *d* | 蜗杆节圆直径 |
| *τS* | 施加到太阳轮轴上的扭矩 |
| *τP* | 施加到行星轮轴上的扭矩 |
| *τC* | 施加到行星架轴上的扭矩 |
| *τ* | 啮合摩擦产生的扭矩：损失取决于装置效率和功率流向。为避免在 *ωS* = 0 处摩擦扭矩突变，摩擦扭矩通过双曲函数引入。 |
| *τinstfr* | 用于模拟摩擦损失的摩擦扭矩瞬时值 |
| *τfr* | 稳态下的摩擦扭矩 |
| *k* | 摩擦系数 |
| *ηWG* | 蜗杆到齿轮功率传递的效率 |
| *ηGW* | 齿轮到蜗杆功率传递的效率 |
| *pth* | 功率阈值 |
| *μSC* | 太阳轮-行星架界面的粘性摩擦系数 |
| *μWC* | 蜗杆-行星架界面的粘性摩擦系数 |

**理想齿轮约束和齿轮比**

Sun-Planet Worm Gear 模块对三个连接轴施加一个运动学约束：

ωS=ωPRWG+ωC.

该齿轮具有两个独立自由度。齿轮对为 (1,2) = (*S*,*P*)。

扭矩传递为：

RWGτP+τS–τloss= 0

τC= –τS

在无扭矩损失的理想情况下，*τloss* = 0。

**非理想齿轮约束**

在非理想情况下，*τloss* ≠ 0。有关详细信息，请参阅 Model Gears with Losses。

在非理想齿轮中，角速度和几何约束不变，但传递的扭矩和功率因以下因素而降低：

- 由蜗杆-太阳轮啮合引起的库仑摩擦，其特征由摩擦系数 *k* 或恒定效率 [*ηWG*, *ηGW*] 表示
- 传动轴与轴承的粘性耦合，由粘性摩擦系数 *μSC* 和 *μWC* 参数化

由于该传动包含蜗杆，直接和反向功率传递的效率不同。该表显示了功率传递所有组合的效率值。

|  |  |  |  |
| --- | --- | --- | --- |
| **主动轴** | **从动轴** | | |
| **行星轮** | **太阳轮** | **行星架** |
| **行星轮** | N/A | *ηWG* | *ηWG* |
| **太阳轮** | *ηGW* | N/A | 无损失 |
| **行星架** | *ηGW* | 无损失 | N/A |

**几何表面接触摩擦**

当您将 **摩擦模型** 设置为 `Constant efficiency`，并将 **摩擦参数化** 保持设置为 `Friction coefficient and geometrical parameters` 时，模型会考虑几何表面接触摩擦。在这种情况下，*ηWG* 和 *ηGW* 取决于：

- 蜗杆螺纹几何形状，由导程角 *λ* 和法向压力角 *α* 指定。
- 表面接触摩擦系数 *k*。

ηWG= (cosα–k·tanλ)(cosα+ktanλ)

ηGW= (cosα–ktanλ)(cosα+k·tanα)

**恒效率**

当您将 **摩擦模型** 设置为 `Constant efficiency`，并将 **摩擦参数化** 设置为 `Efficiencies` 时，或者当您将 **摩擦模型** 设置为 `Temperature-dependent efficiency` 时，模型将效率视为恒定。在这种情况下，您指定 *ηWG* 和 *ηGW* 时与几何细节无关。

**自锁和负效率**

您可以通过使效率为负来启用自锁行为。除非对蜗杆施加某些扭矩以释放轮系，否则功率无法从太阳轮传递到蜗杆，或从行星架传递到蜗杆。在这种情况下，效率的绝对值指定轮系释放的比率。轮系导程角越小，反向效率越小。

**啮合效率**

只有当传递的功率大于功率阈值时，蜗杆和行星轮之间啮合的效率 *η* 才完全生效。

如果功率小于阈值，则实际效率在零速度时自动正则化为单位值。

**粘性摩擦力**

蜗杆-行星架和太阳轮-行星架轴承的粘性摩擦系数控制行星架从润滑的非理想齿轮螺纹承受的粘性摩擦扭矩。有关详细信息，请参阅非理想齿轮约束。

### 变量

使用 **变量** 设置可在仿真前设置模块变量的优先级和初始目标值。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

### 假设和限制

- 假设齿轮惯量可忽略不计。
- 齿轮被视为刚性组件。
- 库仑摩擦会减慢仿真速度。有关详细信息，请参阅 Adjust Model Fidelity。
