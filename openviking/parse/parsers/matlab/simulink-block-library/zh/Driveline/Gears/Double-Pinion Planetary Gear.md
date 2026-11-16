---
type: simulink-block
title: 'Double-Pinion Planetary Gear'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears'
documentation_page: 'doublepinionplanetarygear'
documentation_source_path: 'ref/doublepinionplanetarygear.html'
language: zh-CN
chinese_source: worker-translation
---

# Double-Pinion Planetary Gear

## 端口

### 守恒

### **C** — 行星齿轮架旋转机械

与行星齿轮架关联的旋转机械守恒端口。

### **R** — 齿圈旋转机械

与齿圈关联的旋转机械守恒端口。

### **S** — 太阳轮旋转机械

与太阳轮关联的旋转机械守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。热流通过改变齿轮温度影响功率传输效率。

#### 依赖关系

要启用此端口，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

## 参数

### 主要

### **Ring (R) to sun (S) teeth ratio (NR/NS)** — 齿圈与太阳轮旋转比 `2`（默认）| 正标量

由行星轮齿数除以太阳轮齿数定义的齿圈旋转与太阳轮旋转的固定比。

### **Outer planet (Po) to inner planet (Pi) teeth ratio (NPo/NPi)** — 外行星轮与内行星轮旋转比 `1`（默认）| 正标量

由行星轮齿数除以太阳轮齿数定义的外行星轮旋转与内行星轮旋转的固定比。

### 啮合损耗

### **Friction model** — 摩擦模型 `No meshing losses - Suitable for HIL simulation`（默认）| `Constant efficiency` | `Temperature-dependent efficiency`

该模块的摩擦模型：

- `No meshing losses - Suitable for HIL simulation`
  — 齿轮啮合是理想的。
- `Constant efficiency` — 齿轮轮对之间的转矩传递按恒定效率
  *η* 降低，使得 0 < *η* ≤ 1。
- `Temperature-dependent efficiency` — 齿轮轮对之间的转矩传递由基于温度的查表定义。

### **Sun-planet, ring-planet and planet-planet ordinary efficiencies** — 转矩传递效率 `[.98, .98, .99]`（默认）| 向量

转矩传递效率向量
[*ηSP*,
*ηRP*,
*ηRPP*]，分别用于太阳轮-行星轮、齿圈-行星轮和行星轮-行星轮齿轮对啮合。向量元素必须位于区间 (0,1] 内。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Constant efficiency`。

### **Temperature** — 温度 `[280, 300, 320]` `K`（默认）| 向量

用于构建一维温度-效率查找表的温度向量。向量元素必须从左到右递增。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为
`Temperature-dependent efficiency`。

### **Sun-planet efficiency** — 从太阳轮到内行星轮的转矩传递效率 `[.75, .65, .6]`（默认）| 向量

描述从太阳轮流向内行星轮的功率流的输出功率与输入功率之比向量，
*ηSP*。该模块使用这些值构建一维温度-效率查找表。

每个元素是与 **Temperature** 向量中某个温度关联的效率。
向量长度必须等于 **Temperature** 向量的长度。向量中的每个元素
必须在范围 (0,1] 内。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Temperature-dependent
efficiency`。

### **Ring-planet efficiency** — 从齿圈到外行星轮的转矩传递效率 `[.5, .45, .4]`（默认）| 向量

描述从齿圈流向外行星轮的功率流的输出功率与输入功率之比向量，
*ηRP*。该模块使用这些值构建一维温度-效率查找表。

每个元素是与 **Temperature** 向量中某个温度关联的效率。
向量长度必须等于 **Temperature** 向量的长度。向量中的每个元素
必须在范围 (0,1] 内。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Temperature-dependent
efficiency`。

### **Planet-planet efficiency** — 从内行星轮到外行星轮的转矩传递效率 `[.5, .45, .4]`（默认）| 向量

描述从内行星轮流向外部行星轮的功率流的输出功率与输入功率之比向量，
*ηPP*。该模块使用这些值构建一维温度-效率查找表。

每个元素是与 **Temperature** 向量中某个温度关联的效率。
向量长度必须等于 **Temperature** 向量的长度。向量中的每个元素
必须在范围 (0,1] 内。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Temperature-dependent
efficiency`。

### **Sun-carrier, ring-carrier, and planet-carrier power thresholds** — 太阳轮-行星架、齿圈-行星架和行星轮-行星架齿轮联轴器的最小效率功率阈值 `[.001, .001, .001]` `W`（默认）| 向量

功率阈值向量；高于该阈值时应用完整效率因子。按太阳轮-行星架、齿圈-行星架、
行星轮-行星架的顺序输入阈值。

当将 **Friction model** 设置为
`Constant efficiency` 时，该模块在未传输功率时将
效率损耗降低到零。当将 **Friction model** 设置为
`Temperature-dependent efficiency` 时，该模块在
静止时的零值与功率阈值下温度-效率查找表提供的值之间平滑效率因子。

功率阈值应低于仿真期间预期传输的功率。较高的值可能导致模块
低估效率损耗。非常低的值可能提高计算成本。

#### 依赖关系

要启用该参数，请将 **Friction model**
设置为 `Constant efficiency` 或
`Temperature-dependent
efficiency`。

### 粘性损耗

### **Sun-carrier, ring-carrier, and planet-carrier viscous friction coefficients** — 齿轮粘性摩擦 `[0, 0, 0]` `N*m/(rad/s)`（默认）| 向量

粘性摩擦系数向量
[*μS*
*μR*
*μP*]，分别用于太阳轮-行星架、
齿圈-行星架和行星轮-行星架齿轮运动。

### 惯性

### **Inertia** — 惯性选项 `off`（默认）| `on`

是否在模块中包含惯性的影响。

### **Sun gear inertia** — 太阳轮惯量 `0.001` `kg*m^2`（默认）| 正标量

太阳轮惯量。

#### 依赖关系

要启用此参数，请选择
**Inertia**。

### **Sun gear radius** — 太阳轮半径 `0.01` `m`（默认）| 正标量

太阳轮半径。

#### 依赖关系

要启用此参数，请选择
**Inertia**。

### **Ring gear inertia** — 齿圈惯量 `0.001` `kg*m^2`（默认）| 正标量

齿圈惯量。

#### 依赖关系

要启用此参数，请选择
**Inertia**。

### **Carrier gear inertia** — 行星架齿轮惯量 `0.001` `kg*m^2`（默认）| 正标量

行星架齿轮惯量。

#### 依赖关系

要启用此参数，请选择
**Inertia**。

### **Inner planet gear spin inertia** — 内行星轮自旋惯量 `0.001` `kg*m^2`（默认）| 正标量

内行星轮绕其自身轴线的惯量。

#### 依赖关系

要启用此参数，请选择
**Inertia**。

### **Inner planet gear mass** — 内行星轮质量 `0.001` `kg`（默认）| 正标量

内行星轮的质量。

#### 依赖关系

要启用此参数，请选择
**Inertia**。

### **Inner planet gear radius** — 内行星轮半径 `0.01` `m`（默认）| 正标量

内行星轮的半径。

#### 依赖关系

要启用此参数，请选择
**Inertia**。

### **Outer planet gear spin inertia** — 外行星轮自旋惯量 `0.001` `kg*m^2`（默认）| 正标量

外行星轮绕其自身轴线的惯量。

#### 依赖关系

要启用此参数，请选择
**Inertia**。

### **Outer planet gear mass** — 内行星轮质量 `0.001` `kg`（默认）| 正标量

外行星轮的质量。

#### 依赖关系

要启用此参数，请选择
**Inertia**。

### **Outer planet gear radius** — 内行星轮半径 `0.02` `m`（默认）| 正标量

外行星轮的半径。

#### 依赖关系

要启用此参数，请选择
**Inertia**。

### 热端口

要启用这些设置，请将 **Friction model** 设置为
`Temperature-dependent efficiency`。

### **Thermal mass** — 热质量 `50` `J/K`（默认）| 标量

使组件温度改变一个温度单位所需的热能。热质量越大，组件对温度变化的抵抗能力越强。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为
`Temperature-dependent
efficiency`。

### **Initial temperature** — 初始温度 `300` `K`（默认）| 标量

仿真开始时的模块温度。初始温度根据各自的效率向量设置初始组件效率。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为
`Temperature-dependent efficiency`。

## 所属库

Simscape / Driveline / Gears

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

### R2025a：枚举更新

**Inertia** 参数现在使用复选框。此参数在以前的版本中使用下拉菜单。

### R2024b：惯性更新

现在可以指定所有齿轮子组件（包括太阳轮、齿圈和行星架）的惯性。现在还可以在行星惯性行为中包含行星进动的影响。

## 描述

具有两组啮合行星齿轮组的行星齿轮系

Double-Pinion Planetary Gear 模块表示一种在太阳轮和齿圈之间具有两组
啮合行星齿轮组的行星齿轮系。单个行星架将两组行星齿轮组保持在距太阳轮中心线
不同半径处，同时允许各个齿轮彼此相对旋转。该齿轮模型包含由于啮合轮齿之间的
摩擦以及旋转齿轮轴的粘性阻尼引起的功率损耗。

在结构上，双行星轮行星齿轮类似于不带第二个大太阳轮的 Ravigneaux 齿轮。
内行星轮与太阳轮啮合，外行星轮与齿圈啮合。由于包含两组行星齿轮组，
双行星轮行星齿轮会反转齿圈和太阳轮的相对旋转方向。

啮合齿轮对的齿数比确定该对中两个齿轮的相对角速度。在 Double-Pinion Planetary Gear
模块中，可以指定齿圈与太阳轮之间以及外行星轮与内行星轮之间的齿轮齿数比。
几何约束确定其余齿数比——齿圈与外行星轮之间以及内行星轮与太阳轮之间的齿数比。
这将齿圈半径约束为太阳轮半径与内、外行星轮直径之和。

rr=rs+2⋅rpi+2⋅rpo,

其中：

- *rr* 是齿圈半径。
- *rs* 是太阳轮半径。
- *rpi* 是内行星轮半径。
- *rpo* 是外行星轮半径。

齿圈与外行星轮的齿数比是

rrrpo=2⋅rrrs(rrrs−1)⋅(rporpi+1)rporpi.

内行星轮与太阳轮的齿数比是

rpirs=(rrrs−1)2(rporpi+1).

Double-Pinion Planetary Gear 模块是一个复合组件。它包含三个底层模块——Ring-Planet、Planet-Planet 和 Sun-Planet——按图中所示连接。每个模块通过一个旋转守恒端口连接到单独的驱动轴。

### 热模型

通过启用可选热端口，可以建模热流和温度变化的影响。要启用该端口，请将
**Friction model** 设置为 `Temperature-dependent
efficiency`。

### 假设和限制

- 假设齿轮惯性可忽略。
- 齿轮被视为刚性组件。
- 库仑摩擦会减慢仿真速度。有关详细信息，请参阅 Adjust Model Fidelity。
