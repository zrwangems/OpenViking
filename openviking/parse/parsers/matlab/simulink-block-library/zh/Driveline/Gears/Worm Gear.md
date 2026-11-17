---
type: simulink-block
title: 'Worm Gear'
family: 'gears'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears'
documentation_page: 'wormgear'
documentation_source_path: 'ref/wormgear.html'
language: zh-CN
chinese_source: worker-translation
---

# Worm Gear

## 端口

### 守恒

### **W** — 蜗杆机械旋转

表示蜗杆力矩和角速度的旋转守恒端口。

### **G** — 齿轮机械旋转

表示齿轮力矩和角速度的旋转守恒端口。

### **H** — 可选传热端口 机械平移

用于热建模的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Friction model** 设置为以下任一值：

- `Temperature-dependent
  efficiency`
- `Temperature and load-dependent
  efficiency`

.

## 参数

### 主要

### **Gear ratio** — 角速度之比 `25`（默认） | 大于 1 的正标量

齿轮比或传动比
*RWG*，由蜗杆角速度与齿轮角速度之比确定。

### **Worm thread type** — 旋转方向 `Right-hand`（默认） | `Left-hand`

选择与正蜗杆旋转对应的齿轮旋转方向。如果选择 `Left-hand`，蜗杆沿通常指定的正方向旋转将导致齿轮沿负方向旋转。

### 啮合损失

### **Friction model** — 齿轮摩擦模型 `No meshing losses — Suitable for HIL simulation`（默认） | `Constant efficiency` | `Temperature-dependent efficiency`

- `No meshing losses — Suitable for HIL
  simulation` — 齿轮啮合是理想的。
- `Constant efficiency` — 蜗杆与齿轮之间的力矩传递因摩擦而减小。
- `Temperature-dependent
  efficiency` — 力矩传递由用户提供的蜗杆-齿轮效率、齿轮-蜗杆效率和温度数据确定。

### **Friction parametrization** — 齿轮螺纹非理想啮合引起的摩擦损失 `Friction coefficient and geometrical parameters`（默认） | `Efficiencies`

- `Friction coefficient and geometrical
  parameters` — 摩擦由表面之间的接触摩擦确定。
- `Efficiencies` — 摩擦由恒定效率 0 < *η* < 1 确定。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`。

### **Normal pressure angle** — 螺纹压力角 `17.5` deg（默认） | 正标量

法向平面中的螺纹压力角 *α*。该值必须大于零且小于 90 度。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`，并将 **Friction parameterization** 设置为 `Friction coefficient and geometrical parameters`。

### **Lead angle** — 螺纹螺旋角 `20` deg（默认） | 正标量

螺纹螺旋角 *λ* =
arctan[*L*/(*π**d*)]，其中：

- *L* 是蜗杆导程。
- *d* 是蜗杆分度圆直径。

该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`，并将 **Friction parameterization** 设置为 `Friction coefficient and geometrical parameters`。

### **Friction coefficient** — 螺纹摩擦系数 `0.08`（默认） | 正标量

螺纹中法向摩擦的无量纲系数。该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`，并将 **Friction parameterization** 设置为 `Friction coefficient and geometrical parameters`。

### **Worm-gear efficiency** — 从蜗杆到齿轮的效率 `0.74`（默认） | (0,1] 范围内的正标量

从蜗杆到齿轮的功率传递效率 *η*WG。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`，并将 **Friction parameterization** 设置为 `Efficiencies`。

### **Gear-worm efficiency** — 从齿轮到蜗杆的效率 `0.65`（默认） | (0,1] 范围内的正标量

从齿轮到蜗杆的功率传递效率 *η*GW。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`，并将 **Friction parameterization** 设置为 `Efficiencies`。

### **Temperature** — 用于效率表格参数化的数组 `[280 300 320]` K（默认） | 向量

用于构造一维温度-效率查找表的温度数组。数组值必须从左到右递增。温度数组的大小必须与 **Worm-gear efficiency** 和 **Gear-worm efficiency** 数组相同。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Worm-gear efficiency** — 蜗杆到齿轮效率数组 `[0.75 0.7 0.65]`（默认） | 向量

以蜗杆为驱动件（即功率从蜗杆流向齿轮）时的部件效率数组。数组值是在 **Temperature** 数组中各温度下的效率。两个数组的大小必须相同。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Gear-worm efficiency** — 齿轮到蜗杆效率数组 `[0.5 0.45 0.4]`（默认） | 向量

以齿轮为驱动件（即功率从齿轮流向蜗杆）时的部件效率数组。数组值是在 **Temperature** 数组中各温度下的效率。两个数组的大小必须相同。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Power threshold** — 应用数值平滑的功率下限 `0.001` W（默认） | 正标量

功率阈值，高于该值时完整的效率因子生效。双曲正切函数在静止时的零与当前效率设定点之间平滑效率因子。

### 黏性损失

### **Viscous friction coefficients at worm (W) and gear (G)** — 流体动摩擦系数 `[0 0]` N\*m/(rad/s)（默认） | 正二元素向量

黏性摩擦系数向量
[*μ*W
*μ*G]，分别对应蜗杆和齿轮。

### 热端口

### **Thermal mass** — 热质量 `50` `J/K`（默认） | 正标量

使组件温度改变一度所需的热能。热质量越大，组件越难以发生温度变化。

### **Initial temperature** — 初始温度 `300` `K`（默认） | 正标量

仿真开始时的组件温度。初始温度会根据您指定的效率向量改变组件效率，从而影响起始啮合损失或摩擦损失。

## 所属库

Simscape / Driveline / Gears

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

## 描述

具有可调齿轮比和摩擦损失的蜗轮蜗杆传动

该模块表示一个旋转齿轮，其约束两个相连的传动系轴——蜗杆 (W) 和齿轮 (G)——以您指定的固定比例一起旋转。您可以选择齿轮沿正方向还是负方向旋转。右旋为正方向。如果蜗杆螺纹为右旋，*ω*W 和 *ω*G 符号相同。如果蜗杆螺纹为左旋，*ω*W 和 *ω*G 符号相反。

### 热模型

您可以通过启用可选热端口来建模热流和温度变化的影响。要启用该端口，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### 模型变量

|  |  |
| --- | --- |
| *R*WG | 齿轮比 |
| *ω*W | 蜗杆角速度 |
| *ω*G | 齿轮角速度 |
| *α* | 法向压力角 |
| *λ* | 蜗杆导程角 |
| *L* | 蜗杆导程 |
| *d* | 蜗杆分度圆直径 |
| *τ*G | 齿轮力矩 |
| *τ*W | 蜗杆上的力矩 |
| *τ*loss | 由于啮合摩擦引起的力矩损失。该损失取决于装置效率和功率流向。为避免 *ω*G = 0 处摩擦力矩突变，摩擦力矩通过双曲函数引入。 |
| *τ*fr | *ω*G → ∞ 时摩擦力矩的稳态值。 |
| *k* | 摩擦系数 |
| *ηWG* | 从蜗杆到齿轮的力矩传递效率 |
| *ηGW* | 从齿轮到蜗杆的力矩传递效率 |
| *p*th | 功率阈值 |
| [*μ*W *μ*G] | 蜗杆和齿轮的黏性摩擦系数向量 |

### 理想齿轮约束与齿轮比

蜗轮蜗杆传动对两个相连轴施加一个运动学约束：

|  |  |
| --- | --- |
| *ω*W = *R*WG*ω*G. | **(1)** |

两个自由度缩减为一个独立自由度。正向传递齿轮对约定为 (1,2) = (W,G)。

力矩传递为：

|  |  |
| --- | --- |
| *R*WG*τ*W – *τ*G – *τ*loss = 0, | **(2)** |

其中在理想情况下 *τ*loss = 0。

### 非理想齿轮约束

在非理想情况下，*τ*loss ≠ 0。有关非理想齿轮建模的一般考虑，请参阅 Model Gears with Losses。

**几何表面接触摩擦**

在接触摩擦情况下，*η*WG 和 *η*GW 由以下因素确定：

- 蜗杆-齿轮螺纹几何形状，由导程角 *λ* 和法向压力角 *α* 指定。
- 表面接触摩擦系数 *k*。

|  |  |
| --- | --- |
| *η*WG = (cos*α* – *k*·tan*λ*)/(cos*α* + *k*/tan*λ*) | **(3)** |

|  |  |
| --- | --- |
| *η*GW = (cos*α* – *k*/tan*λ*)/(cos*α* + *k*·tan*λ*) | **(4)** |

**恒定效率**

在恒定摩擦情况下，您指定 *η*WG 和 *η*GW，与几何细节无关。

**自锁与负效率**

*η*GW 有两个不同区间，取决于导程角 *λ*，二者由 *自锁点* 分隔，在该点 *η*GW = 0 且 cos*α* = *k*/tan*λ*。

- 在 *逆向驱动工况* 中，*η*GW > 0，作用在螺母上的力可以使丝杠旋转。
- 在 *自锁工况* 中，*η*GW < 0，必须对丝杠施加外部力矩才能释放原本锁定的机构。*η*GW 越负，释放机构所需的力矩越大。

*η*WG 按惯例为正。

### 啮合效率

蜗杆与齿轮之间啮合的效率 *η* 仅在传输功率大于功率阈值时完全生效。

如果功率小于该阈值，实际效率会在零速度时自动正则化为单位值。

您可以将啮合损失摩擦模型设置为：

- `No meshing losses - suitable for HIL
  simulation`。
- `Constant efficiency`，这是 R2020b 之前模块版本的默认摩擦设置。
- `Temperature-dependent efficiency`，该模型根据用户提供的查找表对在 `Constant efficiency` 设置中计算的基础轴效率的可变性进行建模。温度相关设置会启用一个热守恒端口 **H**。该端口接收进入模块的热流，并根据齿轮 **Thermal mass** 将其转换为模块温度。

### 黏性摩擦力

黏性摩擦系数 *μ*W 控制蜗杆因润滑的非理想齿轮螺纹和黏性轴承损失而承受的黏性摩擦力矩。蜗杆传动系轴上的黏性摩擦力矩为 –*μ*W*ω*W。*ω*W 是蜗杆相对于其安装座的角速度。

黏性摩擦系数 *μ*G 控制齿轮主要因黏性轴承损失而承受的黏性摩擦力矩。齿轮传动系轴上的黏性摩擦力矩为 –*μ*G*ω*G。*ω*G 是齿轮相对于其安装座的角速度。

### 硬件在环仿真

为获得实时仿真的最佳性能，请在 **Meshing Losses** 选项卡上将 **Friction model** 设置为 `No meshing losses - Suitable for HIL simulation`。

### 变量

使用 **Variables** 设置在仿真前为模块变量设置优先级和初始目标值。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

### 限制

- 假设齿轮惯量可忽略。
- 齿轮被视为刚性组件。
- 库仑摩擦会减慢仿真速度。有关详细信息，请参阅 Adjust Model Fidelity。
