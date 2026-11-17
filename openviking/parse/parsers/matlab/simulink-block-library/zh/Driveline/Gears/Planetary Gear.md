---
type: simulink-block
title: 'Planetary Gear'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears'
documentation_page: 'planetarygear'
documentation_source_path: 'ref/planetarygear.html'
language: zh-CN
chinese_source: worker-translation
---

# Planetary Gear

## 端口

### 守恒端口

### **C** — 行星齿轮架旋转机械

与行星齿轮架关联的旋转机械守恒端口。

### **R** — 齿圈旋转机械

与齿圈关联的旋转机械守恒端口。

### **S** — 太阳轮旋转机械

与太阳轮关联的旋转机械守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。热流通过改变齿轮温度影响功率传输效率。

#### 依赖关系

要启用此端口，请将 **Friction model** 设置为
`Temperature-dependent efficiency`。

## 参数

### 主要

### **Ring (R) to sun (S) teeth ratio (NR/NS)** — 齿圈与太阳轮的旋转比 `2`（默认）| 标量整数

齿圈与太阳轮旋转的固定比值 *gRS*，定义为齿圈齿数除以太阳轮齿数。齿轮比必须严格大于 `1`。

### 啮合损耗

### **Friction model** — 摩擦模型 `No meshing losses - Suitable for HIL simulation`（默认）| `Constant efficiency` | `Temperature-dependent efficiency`

模块的摩擦模型：

- `No meshing losses - Suitable for HIL simulation`
  — 齿轮啮合为理想状态。
- `Constant efficiency` — 齿轮对之间的扭矩传递按恒定效率
  *η* 降低，其中 0 < *η* ≤ 1。
- `Temperature-dependent efficiency` — 齿轮对之间的扭矩传递由基于温度的表查找定义。

### **Sun-planet and ring-planet ordinary efficiencies** — 从太阳轮到行星轮以及从齿圈到行星轮的扭矩传递效率 `[.96, .98]`（默认）| 向量

扭矩传递效率向量
[*ηSP*
*ηRP*]，分别对应太阳轮-行星轮和齿圈-行星架齿轮对的啮合。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Constant efficiency`。

### **Temperature** — 温度 `[280, 300, 320]` `K`（默认）| 向量

用于构建一维温度-效率查找表的温度向量。向量元素必须从左到右递增。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为
`Temperature-dependent efficiency`。

### **Wave generator flexspline efficiency** — 波发生器到柔轮的扭矩传递效率 `[.95, .9, .85]`（默认）| 向量

描述从波发生器齿轮到柔轮齿轮功率流的输出-输入功率比向量，
*ηSP*。模块使用这些值构建一维温度-效率查找表。

每个元素是与 **Temperature** 向量中某个温度对应的效率。
向量长度必须等于 **Temperature** 向量的长度。向量中每个元素必须在 (0,1] 范围内。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Temperature-dependent
efficiency`。

### **Ring-flexspline efficiency** — 从齿圈到柔轮的扭矩传递效率 `[.95, .9, .85]`（默认）| 向量

描述从齿圈到柔轮齿轮功率流的输出-输入功率比向量，
*ηRP*。模块使用这些值构建一维温度-效率查找表。

每个元素是与 **Temperature** 向量中某个温度对应的效率。
向量长度必须等于 **Temperature** 向量的长度。向量中每个元素必须在 (0,1] 范围内。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Temperature-dependent
efficiency`。

### **Sun-carrier and planet-carrier power thresholds** — 太阳轮-行星架和行星轮-行星架齿轮联轴器的最小效率功率阈值 `[.001, .001]` `W`（默认）| 向量

功率阈值向量，高于该阈值时应用完整效率因子。按太阳轮-行星架、行星轮-行星架的顺序输入阈值。低于这些值时，双曲正切函数对效率因子进行平滑处理。

当您将 **Friction model** 设置为
`Constant efficiency` 时，模块在无功率传输时将效率损耗降为零。当您将
**Friction model** 设置为
`Temperature-dependent efficiency` 时，模块在功率阈值处对效率因子进行平滑处理，使其在静止时为零与温度-效率查找表提供的值之间过渡。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Constant efficiency` 或
`Temperature-dependent
efficiency`。

### 粘性损耗

### **Sun-carrier and planet-carrier viscous friction coefficients** — 齿轮粘性摩擦 `[0, 0]` `N*m/(rad/s)`（默认）| 向量

粘性摩擦系数向量
[*μS*,
*μP*]，分别对应太阳轮-行星架和行星轮-行星架的齿轮运动。

### 惯量

### **Inertia** — 惯量选项 `off`（默认）| `on`

是否在模块中包含惯量效应。

### **Sun gear inertia** — 太阳轮惯量 `0.001` `kg*m^2`（默认）| 正标量

太阳轮惯量。

#### 依赖关系

要启用此参数，请选中
**Inertia**。

### **Ring gear inertia** — 齿圈惯量 `0.001` `kg*m^2`（默认）| 正标量

齿圈惯量。

#### 依赖关系

要启用此参数，请选中
**Inertia**。

### **Carrier gear inertia** — 行星架惯量 `0.001` `kg*m^2`（默认）| 正标量

行星架惯量。

#### 依赖关系

要启用此参数，请选中
**Inertia**。

### **Carrier gear radius** — 行星架半径 `0.01` `m`（默认）| 正标量

行星架半径。

#### 依赖关系

要启用此参数，请选中
**Inertia**。

### **Planet gear spin inertia** — 行星轮自旋惯量 `0.001` `kg*m^2`（默认）| 正标量

行星轮绕其自身轴线的惯量。

#### 依赖关系

要启用此参数，请选中
**Inertia**。

### **Planet gear mass** — 行星轮质量 `0.001` `kg`（默认）| 正标量

行星轮质量。

#### 依赖关系

要启用此参数，请选中
**Inertia**。

### 热端口

要启用这些设置，请将 **Friction model** 设置为
`Temperature-dependent efficiency`。

### **Thermal mass** — 热质量 `50` `J/K`（默认）| 标量

使组件温度变化一个温度单位所需的热能。热质量越大，组件对温度变化的抵抗能力越强。

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

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

### R2025a：枚举更新

**Inertia** 参数现在使用复选框。此参数在之前的版本中使用下拉菜单。

### R2024b：惯量更新

您现在可以指定所有齿轮子组件的惯量，包括太阳轮、齿圈和行星架齿轮。您现在还可以在行星轮惯量行为中包含行星轮进动的影响。

## 描述

带太阳轮、行星轮和齿圈的齿轮系

Planetary Gear 模块对带太阳轮、行星轮和齿圈的齿轮系进行建模。行星齿轮在传动系统中很常见，它们能在紧凑的几何结构中提供高齿轮比。连接到驱动轴的行星架固定行星轮。端口 **C**、**R** 和 **S**
分别代表连接到行星齿轮架、齿圈和太阳轮的轴。

该模块基于 Sun-Planet 和 Ring-Planet
Simscape™
Driveline™ 模块将行星齿轮建模为结构组件。图中显示了该结构组件的模块图。

为提高齿轮模型的保真度，您可以指定齿轮惯量、啮合损耗和粘性损耗等属性。默认情况下，齿轮惯量和粘性损耗假定为可忽略不计。

### 热模型

您可以通过启用可选热端口来对热流和温度变化的影响进行建模。要启用该端口，请将 **Friction model** 设置为 `Temperature-dependent
efficiency`。

### 方程

**理想齿轮约束和齿轮比**

Planetary Gear 模块施加两个运动学约束和两个几何约束，

rCωC=rSωS+rPωP

rRωR=rCωC+rPωP

rC=rS+rP

rR=rC+rP

其中：

- *rC* 是行星架齿轮的半径。
- *ωC* 是行星架齿轮的角速度。
- *rS* 是太阳轮的半径。
- *ωS* 是太阳轮的角速度。
- *rP* 是行星轮的半径。
- *ωp* 是行星轮的角速度。
- *rR* 是齿圈的半径。

齿圈-太阳轮齿轮比为

gRS=rR/rS=NR/NS，

其中 *N* 是每个齿轮的齿数。

根据该比值，关键运动学约束为：

(1 + gRS)ωC = ωS + gRSωR。

四个自由度简化为两个独立自由度。齿轮对为 (1, 2) = (*S*, *P*) 和
(*P*, *R*)。

**警告**

齿轮比 *g*RS 必须严格大于一。

扭矩传递为

gRSτS + τR– τloss= 0，

其中：

- *τS* 是太阳轮的扭矩传递。
- *τR* 是齿圈的扭矩传递。
- *τloss* 是扭矩传递损耗。

在无扭矩损耗的理想情况下，*τloss* = 0。

**非理想齿轮约束和损耗**

在非理想情况下，*τloss* ≠ 0。有关详细信息，请参阅 Model Gears with Losses。

### 假设和限制

- 齿轮惯量假定为可忽略不计。
- 齿轮被视为刚性组件。
- 库仑摩擦会减慢仿真速度。有关详细信息，请参阅 Adjust Model Fidelity。
