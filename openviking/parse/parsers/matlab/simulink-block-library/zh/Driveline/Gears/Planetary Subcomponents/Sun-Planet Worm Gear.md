---
type: simulink-block
title: 'Sun-Planet Worm Gear'
family: 'sdl'
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
```yaml
ports:
- name: C
  summary: 行星轮架旋转机械
  direction: conserving
- name: W
  summary: 蜗轮旋转机械
  direction: conserving
- name: S
  summary: 太阳轮旋转机械
  direction: conserving
- name: H
  summary: 热流热
  direction: conserving
```

### 守恒端口

### **C** — 行星轮架旋转机械

与行星轮架关联的旋转机械守恒端口。

### **W** — 蜗轮旋转机械

与蜗轮关联的旋转机械守恒端口。

### **S** — 太阳轮旋转机械

与太阳轮关联的旋转机械守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。热流通过改变齿轮温度影响动力传输效率。

#### 依赖关系

要启用此端口，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。
## 参数
```yaml
parameters:
- name: Gear ratio
  summary: 齿轮比 25（默认）| 正标量
  group: 主要
- name: Worm thread type
  summary: 螺纹旋转方向 Right-hand（默认）| Left-hand
  group: 主要
- name: Friction model
  summary: 摩擦模型 No meshing losses - Suitable for HIL simulation（默认）| Constant efficiency | Temperature-dependent efficiency
  group: 啮合损失
- name: Friction parameterization
  summary: 摩擦参数化方法 Friction coefficient and geometrical parameters（默认）| Efficiencies
  group: 啮合损失
- name: Normal pressure angle
  summary: 螺纹压力角 17.5 deg（默认）| 标量
  group: 啮合损失
- name: Lead angle
  summary: 螺纹螺旋角 20 deg（默认）| 正标量
  group: 啮合损失
- name: Friction coefficient
  summary: 螺纹摩擦 0.08（默认）| 正标量
  group: 啮合损失
- name: Temperature
  summary: 温度 [280, 300, 320] K（默认）| 向量
  group: 啮合损失
- name: Worm-gear efficiency
  summary: 从蜗轮到太阳轮的扭矩传递效率 [.75, .65, .6] 或 0.74（默认）| 向量或标量
  group: 啮合损失
- name: Gear-worm efficiency
  summary: 从太阳轮到蜗轮的扭矩传递效率 [.5, .45, .4] 或 0.65（默认）| 向量或标量
  group: 啮合损失
- name: Power threshold
  summary: 最小效率功率阈值 0.001 W（默认）| 标量
  group: 啮合损失
- name: Worm-carrier and sun-carrier viscous friction coefficients
  summary: 齿轮粘性摩擦 [0, 0] N*m/(rad/s)（默认）| 向量
  group: 粘性损失
- name: Thermal mass
  summary: 热质量 50 J/K（默认）| 标量
  group: 热端口
```

### 主要

### **Gear ratio** — 齿轮比 `25`（默认）| 正标量

齿轮或传动比，*RWG*，表示蜗轮角速度除以太阳轮角速度。该齿轮比必须严格为正。

### **Worm thread type** — 螺纹旋转方向 `Right-hand`（默认）| `Left-hand`

蜗轮正向旋转的方向。如果选择 `Left-hand`，蜗轮正向旋转将导致齿轮负向旋转。

### 啮合损失

下表显示了为 **Friction model** 选择的选项如何影响 **Meshing Losses** 选项卡中其他参数的可见性。

**啮合损失参数依赖关系**

| 啮合损失设置参数和值 | | | | | |
| --- | --- | --- | --- | --- | --- |
| **Friction Model** | | | | | |
| `No meshing losses - Suitable for HIL simulation` | | `Constant efficiency` | | `Temperature-dependent efficiency` | |
| **Friction parameterization** | | **Temperature** | |
| `Friction coefficient and geometrical parameters` | `Efficiencies` |
| **Normal pressure angle** | **Worm-gear efficiency** | **Worm-gear efficiency** | |
| **Lead angle** | **Gear-worm efficiency** | **Gear-worm efficiency** | |
| **Friction coefficient** |
| **Power threshold** | **Power threshold** | **Power threshold** | |

### **Friction model** — 摩擦模型 `No meshing losses - Suitable for HIL simulation`（默认）| `Constant efficiency` | `Temperature-dependent efficiency`

模块的摩擦模型：

- `No meshing losses - Suitable for HIL simulation` — 齿轮啮合为理想状态。
- `Constant efficiency` — 齿轮副之间的扭矩传递由恒定效率 *η* 降低，其中 0 < *η* ≤ 1。
- `Temperature-dependent efficiency` — 齿轮副之间的扭矩传递由基于温度的查表定义。

### **Friction parameterization** — 摩擦参数化方法 `Friction coefficient and geometrical parameters`（默认）| `Efficiencies`

齿轮螺纹之间摩擦的表征：

- `Friction coefficient and geometrical parameters` — 摩擦由几何表面接触摩擦确定。
- `Efficiencies` — 摩擦由恒定效率确定，其中 0 < *η* < 1。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`。

### **Normal pressure angle** — 螺纹压力角 `17.5` `deg`（默认）| 标量

法平面中的螺纹压力角 *α*。该值必须大于零且小于 90 度。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`，并将 **Friction parameterization** 设置为 `Friction coefficient and geometrical parameters`。

### **Lead angle** — 螺纹螺旋角 `20` `deg`（默认）| 正标量

螺纹螺旋角，其中 *λ* = arctan[*L*/(*π**d*)]。*L* 为蜗杆导程，*d* 为蜗杆节圆直径。该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`，并将 **Friction parameterization** 设置为 `Friction coefficient and geometrical parameters`。

### **Friction coefficient** — 螺纹摩擦 `0.08`（默认）| 正标量

螺纹中法向摩擦的无量纲系数。必须大于零。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`，并将 **Friction parameterization** 设置为 `Friction coefficient and geometrical parameters`。

### **Temperature** — 温度 `[280, 300, 320]` `K`（默认）| 向量

用于构建一维温度-效率查找表的温度向量。向量元素必须从左到右递增。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Worm-gear efficiency** — 从蜗轮到太阳轮的扭矩传递效率 `[.75, .65, .6]` 或 `0.74`（默认）| 向量或标量

描述从蜗轮到太阳轮功率流的输出-输入功率比向量，*ηWG*。当将 **Friction model** 设置为 `Constant efficiency` 时，将该值指定为标量。当将 **Friction model** 设置为 `Temperature-dependent efficiency` 时，将该值指定为向量。模块使用向量值构建一维温度-效率查找表。

每个元素是与 **Temperature** 向量中某个温度对应的效率。向量长度必须等于 **Temperature** 向量的长度。向量中的每个元素必须在 (0,1] 范围内。

#### 依赖关系

要启用此参数，请设置以下任一情况：

- **Friction model** 设置为 `Constant efficiency`，**Friction parameterization** 设置为 `Efficiencies` — 在这种情况下，将该值指定为标量。
- **Friction model** 设置为 `Temperature-dependent efficiency` — 在这种情况下，将该值指定为向量。

### **Gear-worm efficiency** — 从太阳轮到蜗轮的扭矩传递效率 `[.5, .45, .4]` 或 `0.65`（默认）| 向量或标量

描述从太阳轮到蜗轮功率流的输出-输入功率比向量，*ηGW*。当将 **Friction model** 设置为 `Constant efficiency` 时，将该值指定为标量。当将 **Friction model** 设置为 `Temperature-dependent efficiency` 时，将该值指定为向量。模块使用向量值构建一维温度-效率查找表。

每个元素是与 **Temperature** 向量中某个温度对应的效率。向量长度必须等于 **Temperature** 向量的长度。向量中的每个元素必须在 (0,1] 范围内。

#### 依赖关系

要启用此参数，请设置以下任一情况：

- **Friction model** 设置为 `Constant efficiency`，**Friction parameterization** 设置为 `Efficiencies` — 在这种情况下，将该值指定为标量。
- **Friction model** 设置为 `Temperature-dependent efficiency` — 在这种情况下，将该值指定为向量。

### **Power threshold** — 最小效率功率阈值 `0.001` `W`（默认）| 标量

功率阈值 *pth*，高于该值时全效率生效。低于该值时，双曲正切函数对效率因子进行平滑处理。

当将 **Friction model** 设置为 `Constant efficiency` 时，模块在无功率传输时将效率损失降为零。当将 **Friction model** 设置为 `Temperature-dependent efficiency` 时，该函数在静止时为零与功率阈值处温度-效率查找表提供的值之间对效率因子进行平滑处理。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency` 或 `Temperature-dependent efficiency`。

### 粘性损失

### **Worm-carrier and sun-carrier viscous friction coefficients** — 齿轮粘性摩擦 `[0, 0]` `N*m/(rad/s)`（默认）| 向量

粘性摩擦系数向量 [*μWC* *μSC*]，分别对应蜗轮-轮架和太阳轮-轮架轴。

### 热端口

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Thermal mass** — 热质量 `50` `J/K`（默认）| 标量

将组件温度改变一个温度单位所需的热能。热质量越大，组件对温度变化的抵抗力越强。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。
## 所属库

Simscape / Driveline / Gears / Planetary Subcomponents

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

## 描述

由轮架、蜗轮行星轮和太阳轮组成的行星齿轮组，具有可调齿轮比、蜗杆螺纹类型和摩擦损失

Sun-Planet Worm Gear 模块表示由轮架、太阳轮和行星轮构成的两自由度行星齿轮。按类型划分，太阳轮和行星轮是交叉斜齿圆柱齿轮，布置为蜗杆传动，其中行星轮为蜗杆。此类传动用于 Torsen® T-1 差速器。在传递动力时，太阳轮可由蜗杆（行星）轮独立旋转驱动，也可由轮架驱动，或由两者共同驱动。

您指定一个固定齿轮比，表示蜗杆角速度除以太阳轮角速度。通过将蜗杆螺纹类型设置为左旋或右旋来控制方向。右旋蜗杆正向旋转导致太阳轮正向旋转。太阳轮和轮架的正方向相同。

### 热模型

您可以通过启用可选热端口来建模热流和温度变化的影响。要启用该端口，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### 方程

**变量**

方程变量为：

|  |  |
| --- | --- |
| *RWG* | 齿轮比，表示蜗杆角速度除以太阳轮角速度：右旋蜗杆该比值为正，左旋蜗杆为负 |
| *ωS* | 太阳轮角速度 |
| *ωP* | 蜗轮角速度 |
| *ωC* | 轮架角速度 |
| *ωSC* | 太阳轮相对于轮架的角速度 |
| *α* | 法向压力角 |
| *λ* | 蜗杆导程角 |
| *L* | 蜗杆导程 |
| *d* | 蜗杆节圆直径 |
| *τS* | 施加到太阳轮轴的扭矩 |
| *τP* | 施加到行星轮轴的扭矩 |
| *τC* | 施加到轮架轴的扭矩 |
| *τ* | 啮合摩擦产生的扭矩：损失取决于装置效率和功率流方向。为避免在 *ωS* = 0 处摩擦力矩的突变，摩擦力矩通过双曲函数引入。 |
| *τinstfr* | 用于模拟摩擦损失的摩擦力矩瞬时值 |
| *τfr* | 稳态摩擦扭矩 |
| *k* | 摩擦系数 |
| *ηWG* | 蜗轮到齿轮功率传递效率 |
| *ηGW* | 齿轮到蜗杆功率传递效率 |
| *pth* | 功率阈值 |
| *μSC* | 太阳轮-轮架界面的粘性摩擦系数 |
| *μWC* | 蜗轮-轮架界面的粘性摩擦系数 |

**理想齿轮约束和齿轮比**

Sun-Planet Worm Gear 模块对三个连接轴施加一个运动学约束：

ωS=ωPRWG+ωC。

该齿轮具有两个独立自由度。齿轮副为 (1,2) = (*S*,*P*)。

扭矩传递为：

RWGτP+τS–τloss= 0

τC= –τS

在无扭矩损失的理想情况下，*τloss* = 0。

**非理想齿轮约束**

在非理想情况下，*τloss* ≠ 0。有关详细信息，请参阅 Model Gears with Losses。

在非理想齿轮中，角速度和几何约束不变，但传递的扭矩和功率因以下因素而降低：

- 蜗杆-太阳轮啮合产生的库仑摩擦，由摩擦系数 *k* 或恒定效率 [*ηWG*, *ηGW*] 表征
- 驱动轴与轴承的粘性耦合，由粘性摩擦系数 *μSC* 和 *μWC* 参数化

由于该传动包含蜗轮，正向和反向功率传递的效率不同。下表显示了功率传递所有组合的效率值。

|  |  |  |  |
| --- | --- | --- | --- |
| **驱动轴** | **从动轴** | | |
| **行星轮** | **太阳轮** | **轮架** |
| **行星轮** | 不适用 | *ηWG* | *ηWG* |
| **太阳轮** | *ηGW* | 不适用 | 无损失 |
| **轮架** | *ηGW* | 无损失 | 不适用 |

**几何表面接触摩擦**

当将 **Friction model** 设置为 `Constant efficiency` 并将 **Friction parameterization** 保持为 `Friction coefficient and geometrical parameters` 时，模型考虑几何表面接触摩擦。在这种情况下，*ηWG* 和 *ηGW* 取决于：

- 蜗轮螺纹几何形状，由导程角 *λ* 和法向压力角 *α* 指定。
- 表面接触摩擦系数 *k*。

ηWG= (cosα–k·tanλ)(cosα+ktanλ)

ηGW= (cosα–ktanλ)(cosα+k·tanα)

**恒定效率**

当将 **Friction model** 设置为 `Constant efficiency` 并将 **Friction parameterization** 设置为 `Efficiencies` 时，或者当将 **Friction model** 设置为 `Temperature-dependent efficiency` 时，模型将效率视为常数。在这种情况下，您独立于几何细节指定 *ηWG* 和 *ηGW*。

**自锁和负效率**

您可以通过使效率为负来启用自锁行为。除非对蜗杆施加一定扭矩以释放传动链，否则功率无法从太阳轮传递到蜗杆或从轮架传递到蜗杆。在这种情况下，效率的绝对值指定传动链释放的比率。传动链导程角越小，反向效率越小。

**啮合效率**

蜗轮和行星轮之间啮合的效率 *η* 仅在传递功率大于功率阈值时完全生效。

如果功率小于阈值，实际效率在零速度时自动正则化为 1。

**粘性摩擦力**

蜗轮-轮架和太阳轮-轮架轴承的粘性摩擦系数控制轮架从润滑的非理想齿轮螺纹所经历的粘性摩擦力矩。有关详细信息，请参阅 Nonideal Gear Constraints。

### 变量

使用 **Variables** 设置可在仿真前设置模块变量的优先级和初始目标值。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

### 假设和限制

- 假设齿轮惯量可忽略不计。
- 齿轮视为刚性组件。
- 库仑摩擦会减慢仿真速度。有关详细信息，请参阅 Adjust Model Fidelity。
