---
type: simulink-block
title: 'Ravigneaux Gear'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears'
documentation_page: 'ravigneauxgear'
documentation_source_path: 'ref/ravigneauxgear.html'
language: zh-CN
chinese_source: worker-translation
---

# Ravigneaux Gear

## 端口

### 守恒

### **C** — 行星齿轮架旋转机械

与行星齿轮架关联的旋转机械守恒端口。

### **R** — 齿圈旋转机械

与齿圈关联的旋转机械守恒端口。

### **SL** — 大太阳轮旋转机械

与大太阳轮关联的旋转机械守恒端口。

### **SS** — 小太阳轮旋转机械

与小太阳轮关联的旋转机械守恒端口。

### **H** — 热流

与热流关联的热守恒端口。热流通过改变齿轮温度来影响动力传输效率。

#### 依赖项

要启用此端口，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

## 参数

### 主要

### **Ring (R) to large sun (SL) teeth ratio (NR/NSL)** — 齿圈与大太阳轮旋转比 `2`（默认）| 正标量

齿圈旋转与大太阳轮旋转的比 *gRLS*，由齿圈齿数除以大太阳轮齿数定义。

### **Ring (R) to small sun (SS) teeth ratio (NR/NSS)** — 齿圈与小太阳轮旋转比 `3`（默认）| 大于 (NR/NSL) 的正标量

齿圈轮与小太阳轮旋转的比 *gRSS*，由齿圈齿数除以小太阳轮齿数定义。此齿轮比必须严格大于 **Ring (R) to large sun (SL) teeth ratio (NR/NSL)**。

### 啮合损失

### **Friction model** — 摩擦模型 `No meshing losses - Suitable for HIL simulation`（默认）| `Constant efficiency` | `Temperature-dependent efficiency`

模块的摩擦模型：

- `No meshing losses - Suitable for HIL simulation` — 齿轮啮合是理想的。
- `Constant efficiency` — 齿轮轮对之间的扭矩传递按恒定效率 *η* 降低，其中 0 < *η* ≤ 1。
- `Temperature-dependent efficiency` — 齿轮轮对之间的扭矩传递由基于温度的表查找定义。

### **Large sun-planet, small sun-planet, ring-planet and planet-planet ordinary efficiencies** — 扭矩传递效率 `[.98, .98, .98, .99]`（默认）| 向量

扭矩传递效率向量 [*ηLS*, *ηSS*, *ηRP*, *ηPP*]，分别对应大太阳轮-行星轮、小太阳轮-行星轮、齿圈-行星轮和行星轮-行星轮齿轮轮对啮合。向量元素必须在 (0,1] 范围内。

#### 依赖项

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`。

### **Temperature** — 温度 `[280, 300, 320]` `K`（默认）| 向量

用于构造一维温度-效率查找表的温度向量。向量元素必须从左到右递增。

#### 依赖项

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Large sun-planet efficiency** — 从大太阳轮至行星轮的扭矩传递效率 `[.95, .9, .85]`（默认）| 向量

描述从大太阳轮到行星轮的动力流的输出/输入功率比向量，*ηLSP*。模块使用这些值构造一维温度-效率查找表。

每个元素是一个效率，与 **Temperature** 向量中的温度相关。向量的长度必须等于 **Temperature** 向量的长度。向量中的每个元素必须在 (0,1] 范围内。

#### 依赖项

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Small sun-planet efficiency** — 从小太阳轮至行星轮的扭矩传递效率 `[.95, .9, .85]`（默认）| 向量

描述从小太阳轮到行星轮的动力流的输出/输入功率比向量，*ηSSP*。模块使用这些值构造一维温度-效率查找表。

每个元素是一个效率，与 **Temperature** 向量中的温度相关。向量的长度必须等于 **Temperature** 向量的长度。向量中的每个元素必须在 (0,1] 范围内。

#### 依赖项

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Ring-planet efficiency** — 从齿圈至行星轮的扭矩传递效率 `[.95, .9, .85]`（默认）| 向量

描述从齿圈到行星轮的动力流的输出/输入功率比向量，*ηRP*。模块使用这些值构造一维温度-效率查找表。

每个元素是一个效率，与 **Temperature** 向量中的温度相关。向量的长度必须等于 **Temperature** 向量的长度。向量中的每个元素必须在 (0,1] 范围内。

#### 依赖项

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Planet-planet efficiency** — 行星轮-行星轮效率 `[.95, .9, .85]`（默认）| 向量

描述从小太阳轮行星轮到大太阳轮行星轮的动力流的输出/输入功率比向量，*ηPP*。模块使用这些值构造一维温度-效率查找表。

每个元素是一个效率，与 **Temperature** 向量中的温度相关。向量的长度必须等于 **Temperature** 向量的长度。向量中的每个元素必须在 (0,1] 范围内。

#### 依赖项

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Large sun-carrier, small sun-carrier, large sun planet-carrier and small sun planet-carrier power thresholds** — 大太阳轮-行星架、小太阳轮-行星架、大太阳轮行星轮-行星架和小太阳轮行星轮-行星架齿轮耦合的最小效率功率阈值 `[.001, .001, .001, .001]` `W`（默认）| 向量

功率阈值向量，高于这些阈值时应用完整效率因子。按大太阳轮、小太阳轮、大太阳轮行星轮和小太阳轮行星轮的顺序输入阈值，均相对于齿轮架。低于这些值时，双曲正切函数会平滑效率因子。

当将 **Friction model** 设置为 `Constant efficiency` 时，模块在未传输功率时将效率损失降至零。当将 **Friction model** 设置为 `Temperature-dependent efficiency` 时，模块在静止时的零值与功率阈值处由温度-效率查找表提供的值之间平滑效率因子。

#### 依赖项

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### 粘性损失

### **Large sun-carrier, small sun-carrier, large sun planet-carrier and small sun planet-carrier viscous friction coefficients** — 齿轮粘性摩擦 `[0, 0, 0, 0]` `N*m/(rad/s)`（默认）| 向量

粘性摩擦系数向量 [*μLS*, *μSS*, *μLSP*, *μSSP*]，分别对应大太阳轮-行星架、小太阳轮-行星架、大太阳轮行星轮-行星架和小太阳轮行星轮-行星架的齿轮运动。

### 惯性

### **Inertia** — 惯性选项 `off`（默认）| `on`

是否在模块中包含惯性效应。

### **Small sun gear inertia** — 小太阳轮惯性 `0.001` `kg*m^2`（默认）| 正标量

小太阳轮惯性。

#### 依赖项

要启用此参数，请选择 **Inertia**。

### **Large sun gear inertia** — 大太阳轮惯性 `0.001` `kg*m^2`（默认）| 正标量

大太阳轮惯性。

#### 依赖项

要启用此参数，请选择 **Inertia**。

### **Ring gear inertia** — 齿圈惯性 `0.001` `kg*m^2`（默认）| 正标量

齿圈惯性。

#### 依赖项

要启用此参数，请选择 **Inertia**。

### **Carrier gear inertia** — 行星架齿轮惯性 `0.001` `kg*m^2`（默认）| 正标量

行星架齿轮惯性。

#### 依赖项

要启用此参数，请选择 **Inertia**。

### **Carrier gear inner radius** — 行星架齿轮内半径 `0.01` `m`（默认）| 正标量

行星架齿轮内半径。

#### 依赖项

要启用此参数，请选择 **Inertia**。

### **Carrier gear outer radius** — 行星架齿轮外半径 `0.02` `m`（默认）| 正标量

行星架齿轮外半径。

#### 依赖项

要启用此参数，请选择 **Inertia**。

### **Inner planet gear spin inertia** — 内行星轮自旋惯性 `0.001` `kg*m^2`（默认）| 正标量

内行星轮绕其自身轴线的惯性。

#### 依赖项

要启用此参数，请选择 **Inertia**。

### **Inner planet gear mass** — 内行星轮质量 `0.001` `kg`（默认）| 正标量

内行星轮的质量。

#### 依赖项

要启用此参数，请选择 **Inertia**。

### **Outer planet gear inertia** — 外行星轮惯性 `0.001` `kg*m^2`（默认）| 正标量

外行星轮的转动惯量。此值必须为正。

#### 依赖项

要启用此参数，请选择 **Inertia**。

### **Outer planet gear mass** — 外行星轮质量 `0.001` `kg`（默认）| 正标量

内行星轮的质量。

#### 依赖项

要启用此参数，请选择 **Inertia**。

### 热端口

要启用这些设置，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Thermal mass** — 热质量 `50` `J/K`（默认）| 标量

使组件温度改变一个温度单位所需的热能。热质量越大，组件越不易发生温度变化。

#### 依赖项

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Initial temperature** — 初始温度 `300` `K`（默认）| 标量

仿真开始时的模块温度。初始温度根据各自的效率向量设置初始组件效率。

#### 依赖项

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

## 所属库

Simscape / Driveline / Gears

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2011a 中引入**

### R2025a：枚举更新

**Inertia** 参数现在使用复选框。此参数在以前的版本中使用下拉列表。

### R2024b：惯性更新

现在可以指定所有齿轮子组件的惯性，包括太阳轮、齿圈和行星架齿轮。现在还可以在行星轮惯性行为中包含行星轮进动的影响。

## 描述

具有两个太阳轮和两组行星轮的行星齿轮

Ravigneaux Gear 模块表示具有双太阳轮和双行星轮组的行星齿轮系。两个太阳轮居中布置，并沿一条公共旋转轴线纵向分开。其中较小的齿轮与内行星轮组啮合，内行星轮组进而与外行星轮组啮合。外行星轮组的长度跨度为两个太阳轮之间的距离，同时与较大的太阳轮和齿圈啮合。

行星架将行星轮组固定在不同半径处。行星架与驱动轴刚性连接，可作为一个整体相对于太阳轮和齿圈旋转。每个转动副位于一个行星轮与行星架之间，使各齿轮能够绕其各自的纵向轴线旋转。

太阳轮、行星轮和齿圈的相对角速度由它们之间的运动学约束决定。有关详细信息，请参阅方程。

该模块将 Ravigneaux 齿轮建模为基于 Sun-Planet、Planet-Planet 和 Ring-Planet Simscape™ Driveline™ 模块的结构组件。图中显示了此结构组件的等效模块图。

为提高齿轮模型的保真度，可以指定齿轮惯性、啮合损失和粘性损失等属性。默认情况下，假设齿轮惯性和粘性损失可忽略不计。该模块允许指定内部行星轮的惯性。要对行星架、大太阳轮、小太阳轮和齿圈的惯性建模，请将 Simscape Inertia 模块连接到端口 **C**、**SL**、**SS** 和 **R**。

### 热模型

可以通过启用可选热端口来对热流和温度变化的影响建模。要启用该端口，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### 方程

**理想齿轮约束和齿轮比**

Ravigneaux Gear 模块对四个连接轴和两个内部轮（内行星轮和外行星轮）施加四个运动学约束和四个几何约束：

rCiωC=rSSωSS+rPiωPi

rCi=rSS+rPi

rCoωC=rSLωSL+rPoωPo

rCo=rSL+rPo

(rCo−rCi)ωC=rPiωPi+rPoωPo

rCo−rCi=rPo+rPi

rRωR=rCoωC+rPoωPo

rR=rCo+rPo

其中：

- *rCi* 是内行星架齿轮的半径。
- *ωC* 是行星架齿轮的角速度。
- *rSS* 是小太阳轮的半径。
- *ωSS* 是小太阳轮的角速度。
- *rPi* 是内行星轮的半径。
- *ωPi* 是内行星轮的角速度。
- *rCo* 是外行星架齿轮的半径。
- *rSL* 是大太阳轮的半径。
- *ωSL* 是大太阳轮的角速度。
- *rPo* 是外行星轮的半径。
- *ωPo* 是外行星轮的角速度。
- *ωR* 是齿圈的角速度。

齿圈与太阳轮的比为：

gRSS=rR/rSS=NR/NSS

gRSL=rR/rSL=NR/NSL

其中：

- *gRSS* 是齿圈与小太阳轮的比。
- *NR* 是齿圈中的齿数。
- *NSS* 是小太阳轮中的齿数。
- *gRSS* 是齿圈与大太阳轮的比。
- *NSL* 是大太阳轮中的齿数。

用这些齿轮比表示，关键运动学约束为：

(gRSS−1)ωC=gRSSωR−ωSS

(gRSL+1)ωC=gRSLωR+ωSL

六个自由度减少为两个独立自由度。齿轮对为 (1,2) = (*LS*,*P*)、(*SS*,*P*)、(*P*,*R*) 和 (*P*,*P*)。

**警告**

齿轮比 *gRSS* 必须严格大于齿轮比 *gRSL*。齿轮比 *gRSL* 必须严格大于 1。

扭矩传递为：

gRSSτSS+τR−τloss(SS,R)=0

gRSLτSL+τR−τloss(SL,R)=0

其中：

- *τSS* 是小太阳轮的扭矩传递。
- *τR* 是齿圈的扭矩传递。
- *τloss(SS,R)* 是小太阳轮与齿圈之间的扭矩传递损失。
- *τSL* 是大太阳轮的扭矩传递。
- *τloss(SL,R)* 是大太阳轮与齿圈之间的扭矩传递损失。

在无扭矩损失的理想情况下，*τloss* = 0。

**非理想齿轮约束和损失**

在非理想情况下，*τloss* ≠ 0。有关详细信息，请参阅 Model Gears with Losses。

### 假设和限制

- 假设齿轮是刚性的。
- 库仑摩擦会减慢仿真速度。有关详细信息，请参阅 Adjust Model Fidelity。
