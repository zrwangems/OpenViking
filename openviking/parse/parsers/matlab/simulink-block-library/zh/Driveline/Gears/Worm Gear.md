---
type: simulink-block
title: 'Worm Gear'
family: 'sdl'
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

### 守恒端口

### **W** — 蜗杆机械旋转

表示蜗杆扭矩和角速度的旋转守恒端口。

### **G** — 齿轮机械旋转

表示齿轮扭矩和角速度的旋转守恒端口。

### **H** — 可选热传递端口机械平移

用于热建模的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Friction model** 设置为以下之一：

- `Temperature-dependent
  efficiency`
- `Temperature and load-dependent
  efficiency`

。

## 参数

### 主要

### **Gear ratio** — 角速度之比 `25`（默认）| 大于 1 的正标量

齿轮或传动比
*RWG*，定义为蜗杆角速度与齿轮角速度之比。

### **Worm thread type** — 旋转方向 `Right-hand`（默认）| `Left-hand`

选择与正蜗杆旋转相对应的齿轮旋转方向。如果选择 `Left-hand`，
蜗杆沿通常指定的正方向旋转将导致齿轮沿负方向旋转。

### 啮合损耗

### **Friction model** — 齿轮摩擦模型 `No meshing losses — Suitable for HIL simulation`（默认）| `Constant efficiency` | `Temperature-dependent efficiency`

- `No meshing losses — Suitable for HIL
  simulation` — 齿轮啮合为
  理想状态。
- `Constant efficiency` —
  蜗杆与齿轮之间的扭矩传递因摩擦而减小。
- `Temperature-dependent
  efficiency` — 扭矩传递
  由用户提供的蜗杆-齿轮效率、齿轮-蜗杆效率和温度数据确定。

### **Friction parametrization** — 齿轮螺纹非理想啮合引起的摩擦损耗 `Friction coefficient and geometrical parameters`（默认）| `Efficiencies`

- `Friction coefficient and geometrical
  parameters` — 摩擦由
  表面之间的接触摩擦确定。
- `Efficiencies` — 摩擦由
  常数效率 0 < *η* < 1 确定。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Constant efficiency`。

### **Normal pressure angle** — 螺纹压力角 `17.5` deg（默认）| 正标量

法平面内的螺纹压力角 *α*。该值
必须大于零且小于 90 度。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Constant efficiency`，并将
**Friction parameterization** 设置为
`Friction coefficient and geometrical
parameters`。

### **Lead angle** — 螺纹螺旋角 `20` deg（默认）| 正标量

螺纹螺旋角 *λ* =
arctan[*L*/(*π**d*)]，其中：

- *L* 是蜗杆导程。
- *d* 是蜗杆分度圆直径。

该值必须大于零。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Constant efficiency`，并将
**Friction parameterization** 设置为
`Friction coefficient and geometrical
parameters`。

### **Friction coefficient** — 螺纹摩擦系数 `0.08`（默认）| 正标量

螺纹中法向摩擦的无量纲系数。该值
必须大于零。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Constant efficiency`，并将
**Friction parameterization** 设置为
`Friction coefficient and geometrical
parameters`。

### **Worm-gear efficiency** — 从蜗杆到齿轮的效率 `0.74`（默认）| 范围 (0,1] 内的正标量

从蜗杆到齿轮的功率传递效率 *η*WG。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Constant efficiency`，并将
**Friction parameterization** 设置为
`Efficiencies`。

### **Gear-worm efficiency** — 从齿轮到蜗杆的效率 `0.65`（默认）| 范围 (0,1] 内的正标量

从齿轮到蜗杆的功率传递效率 *η*GW。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Constant efficiency`，并将
**Friction parameterization** 设置为
`Efficiencies`。

### **Temperature** — 用于效率表格化参数化的数组 `[280 300 320]` K（默认）| 向量

用于构建一维温度-效率查找表的温度数组。数组值必须从左到右递增。温度数组必须与 **Worm-gear
efficiency** 和 **Gear-worm efficiency**
数组大小相同。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Temperature-dependent
efficiency`。

### **Worm-gear efficiency** — 蜗杆到齿轮效率数组 `[0.75 0.7 0.65]`（默认）| 向量

以蜗杆为主动件的组件效率数组——
即功率从蜗杆流向齿轮。数组值为
**Temperature** 数组中各温度下的效率。两个数组必须
大小相同。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Temperature-dependent
efficiency`。

### **Gear-worm efficiency** — 齿轮到蜗杆效率数组 `[0.5 0.45 0.4]`（默认）| 向量

以齿轮为主动件的组件效率数组——
即功率从齿轮流向蜗杆。数组值为
**Temperature** 数组中各温度下的效率。两个数组必须
大小相同。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Temperature-dependent
efficiency`。

### **Power threshold** — 低于此功率时应用数值平滑 `0.001` W（默认）| 正标量

高于此功率阈值时，完整效率因子生效。双曲正切函数在静止时的零值与当前效率设定点之间对效率因子进行平滑。

### 粘性损耗

### **Viscous friction coefficients at worm (W) and gear (G)** — 流体动力摩擦系数 `[0 0]` N\*m/(rad/s)（默认）| 正二元向量

粘性摩擦系数向量
[*μ*W
*μ*G]，分别对应蜗杆和齿轮。

### 热端口

### **Thermal mass** — 热质量 `50` `J/K`（默认）| 正标量

使组件温度变化一度所需的热能。热质量越大，组件对温度变化的抵抗能力越强。

### **Initial temperature** — 初始温度 `300` `K`（默认）| 正标量

仿真开始时组件的温度。初始温度根据您指定的效率向量改变组件效率，从而影响起始啮合或摩擦损耗。

## 所属库

Simscape / Driveline / Gears

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

## 描述

具有可调齿轮比和摩擦损耗的蜗轮蜗杆

该模块表示一个旋转齿轮，它将两个相连的传动系轴——蜗杆 (W) 和齿轮 (G)——约束为以您指定的固定比率一起旋转。您可以选择齿轮沿正方向还是负方向旋转。右旋为正方向。如果蜗杆螺纹为右旋，
*ω*W 和
*ω*G 具有相同的符号。如果蜗杆螺纹
为左旋，*ω*W 和
*ω*G 具有相反的符号。

### 热模型

您可以通过启用可选热端口来建模
热流和温度变化的影响。要启用
该端口，请将 **Friction model** 设置为 `Temperature-dependent
efficiency`。

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
| *τ*G | 齿轮扭矩 |
| *τ*W | 蜗杆上的扭矩 |
| *τ*loss | 啮合摩擦引起的扭矩损失。该损失取决于装置效率和功率流向。为避免在 *ω*G = 0 处摩擦力矩的突变，摩擦力矩通过双曲函数引入。 |
| *τ*fr | *ω*G → ∞ 时摩擦力矩的稳态值。 |
| *k* | 摩擦系数 |
| *ηWG* | 从蜗杆到齿轮的扭矩传递效率 |
| *ηGW* | 从齿轮到蜗杆的扭矩传递效率 |
| *p*th | 功率阈值 |
| [*μ*W *μ*G] | 蜗杆和齿轮的粘性摩擦系数向量 |

### 理想齿轮约束和齿轮比

蜗轮蜗杆对两个相连轴施加一个运动学约束：

|  |  |
| --- | --- |
| *ω*W = *R*WG*ω*G。 | **(1)** |

两个自由度被缩减为一个独立自由度。正向传递齿轮对约定为 (1,2) = (W,G)。

扭矩传递为：

|  |  |
| --- | --- |
| *R*WG*τ*W – *τ*G – *τ*loss = 0， | **(2)** |

在理想情况下 *τ*loss = 0。

### 非理想齿轮约束

在非理想情况下，*τ*loss ≠ 0。关于非理想齿轮建模的一般考虑，请参见 Model Gears with Losses。

**几何表面接触摩擦**

在接触摩擦情况下，*η*WG
和 *η*GW 由以下因素确定：

- 蜗杆-齿轮螺纹几何形状，由导程角
  *λ* 和法向压力角
  *α* 指定。
- 表面接触摩擦系数 *k*。

|  |  |
| --- | --- |
| *η*WG = (cos*α* – *k*·tan*λ*)/(cos*α* + *k*/tan*λ*) | **(3)** |

|  |  |
| --- | --- |
| *η*GW = (cos*α* – *k*/tan*λ*)/(cos*α* + *k*·tan*λ*) | **(4)** |

**常数效率**

在常数摩擦情况下，您指定
*η*WG 和
*η*GW，与几何
细节无关。

**自锁和负效率**

*η*GW 有两种不同的状态，
取决于导程角 *λ*，由
*自锁点*分隔，在该点 *η*GW = 0 且 cos*α* =
*k*/tan*λ*。

- 在 *超越状态* 中，*η*GW >
  0，作用在螺母上的力可以旋转
  丝杠。
- 在 *自锁状态* 中，*η*GW <
  0，必须对丝杠施加外部扭矩
  才能释放原本锁定的机构。*η*GW
  越负，释放机构所需的扭矩
  越大。

*η*WG 通常
为正。

### 啮合效率

蜗杆与齿轮之间啮合的效率 *η* 仅在传递功率大于功率阈值时才完全
生效。

如果功率小于阈值，实际效率在零速度时自动
正则化为 1。

您可以将啮合损耗摩擦模型设置为：

- `No meshing losses - suitable for HIL
  simulation`。
- `Constant efficiency`，这是 R2020b 之前模块版本的默认
  摩擦设置。
- `Temperature-dependent efficiency`，它
  根据用户提供的查找表对
  `Constant efficiency` 设置中计算的基础轴效率的
  变化进行建模。温度依赖性设置
  启用一个热守恒端口 **H**。该端口
  接收进入模块的热流，并根据齿轮 **Thermal
  mass** 将其转换为
  模块温度。

### 粘性摩擦力

粘性摩擦系数 *μ*W
控制蜗杆因润滑的非理想齿轮螺纹和粘性轴承损耗而承受的粘性摩擦力矩。蜗杆传动系轴上的
粘性摩擦力矩为
–*μ*W*ω*W。
*ω*W 是蜗杆
相对于其安装座的角速度。

粘性摩擦系数 *μ*G
控制齿轮主要因粘性轴承损耗而承受的粘性摩擦力矩。齿轮传动系轴上的
粘性摩擦力矩为
–*μ*G*ω*G。
*ω*G 是齿轮
相对于其安装座的角速度。

### 硬件在环仿真

为获得实时仿真的最佳性能，请在 **Meshing Losses** 选项卡上将 **Friction
model** 设置为 `No meshing losses - Suitable for HIL
simulation`。

### 变量

使用 **Variables** 设置在仿真前为模块变量设置优先级和初始目标
值。有关详细信息，请参见 Set Priority and Initial Target for Block Variables。

### 限制

- 假设齿轮惯量可忽略不计。
- 齿轮被视为刚性组件。
- 库仑摩擦会减慢仿真速度。有关详细信息，请参见 Adjust Model Fidelity。
