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
```yaml
ports:
- name: C
  summary: 行星齿轮架旋转机械
  direction: conserving
- name: R
  summary: 齿圈旋转机械
  direction: conserving
- name: SL
  summary: 大太阳轮旋转机械
  direction: conserving
- name: SS
  summary: 小太阳轮旋转机械
  direction: conserving
- name: H
  summary: 热流热
  direction: conserving
```

### 守恒端口

### **C** — 行星齿轮架旋转机械

与行星齿轮架关联的旋转机械守恒端口。

### **R** — 齿圈旋转机械

与齿圈关联的旋转机械守恒端口。

### **SL** — 大太阳轮旋转机械

与大太阳轮关联的旋转机械守恒端口。

### **SS** — 小太阳轮旋转机械

与小太阳轮关联的旋转机械守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。热流通过改变齿轮温度影响功率传输效率。

#### 依赖关系

要启用此端口，请将 **Friction model** 设置为
`Temperature-dependent efficiency`。
## 参数
```yaml
parameters:
- name: Ring (R) to large sun (SL) teeth ratio (NR/NSL)
  summary: 齿圈与大太阳轮旋转比 2（默认）| 正标量
  group: 主要
- name: Ring (R) to small sun (SS) teeth ratio (NR/NSS)
  summary: 齿圈与小太阳轮旋转比 3（默认）| 大于 (NR/NSL) 的正标量
  group: 主要
- name: Friction model
  summary: 摩擦模型 No meshing losses - Suitable for HIL simulation（默认）| Constant efficiency | Temperature-dependent efficiency
  group: 啮合损失
- name: Large sun-planet, small sun-planet, ring-planet and planet-planet ordinary efficiencies
  summary: 扭矩传递效率 [.98, .98, .98, .99]（默认）| 向量
  group: 啮合损失
- name: Temperature
  summary: 温度 [280, 300, 320] K（默认）| 向量
  group: 啮合损失
- name: Large sun-planet efficiency
  summary: 从大太阳轮到行星轮的扭矩传递效率 [.95, .9, .85]（默认）| 向量
  group: 啮合损失
- name: Small sun-planet efficiency
  summary: 从小太阳轮到行星轮的扭矩传递效率 [.95, .9, .85]（默认）| 向量
  group: 啮合损失
- name: Ring-planet efficiency
  summary: 从齿圈到行星轮的扭矩传递效率 [.95, .9, .85]（默认）| 向量
  group: 啮合损失
- name: Planet-planet efficiency
  summary: 行星轮-行星轮效率 [.95, .9, .85]（默认）| 向量
  group: 啮合损失
- name: Large sun-carrier, small sun-carrier, large sun planet-carrier and small sun planet-carrier power thresholds
  summary: 大太阳轮-行星架、小太阳轮-行星架、大太阳轮行星轮-行星架和小太阳轮行星轮-行星架齿轮联轴器的最小效率功率阈值 [.001, .001, .001, .001] W（默认）| 向量
  group: 啮合损失
- name: Large sun-carrier, small sun-carrier, large sun planet-carrier and small sun planet-carrier viscous friction coefficients
  summary: 齿轮粘性摩擦 [0, 0, 0, 0] N*m/(rad/s)（默认）| 向量
  group: 粘性损失
- name: Inertia
  summary: 惯量选项 off（默认）| on
  group: 惯量
- name: Small sun gear inertia
  summary: 小太阳轮惯量 0.001 kg*m^2（默认）| 正标量
  group: 惯量
- name: Large sun gear inertia
  summary: 大太阳轮惯量 0.001 kg*m^2（默认）| 正标量
  group: 惯量
- name: Ring gear inertia
  summary: 齿圈惯量 0.001 kg*m^2（默认）| 正标量
  group: 惯量
- name: Carrier gear inertia
  summary: 行星架惯量 0.001 kg*m^2（默认）| 正标量
  group: 惯量
- name: Carrier gear inner radius
  summary: 行星架内半径 0.01 m（默认）| 正标量
  group: 惯量
- name: Carrier gear outer radius
  summary: 行星架外半径 0.02 m（默认）| 正标量
  group: 惯量
- name: Inner planet gear spin inertia
  summary: 内行星轮自旋惯量 0.001 kg*m^2（默认）| 正标量
  group: 惯量
- name: Inner planet gear mass
  summary: 内行星轮质量 0.001 kg（默认）| 正标量
  group: 惯量
- name: Outer planet gear inertia
  summary: 外行星轮惯量 0.001 kg*m^2（默认）| 正标量
  group: 惯量
- name: Outer planet gear mass
  summary: 外行星轮质量 0.001 kg（默认）| 正标量
  group: 惯量
- name: Thermal mass
  summary: 热质量 50 J/K（默认）| 标量
  group: 热端口
- name: Initial temperature
  summary: 初始温度 300 K（默认）| 标量
  group: 热端口
```

### 主要

### **Ring (R) to large sun (SL) teeth ratio (NR/NSL)** — 齿圈与大太阳轮旋转比 `2`（默认）| 正标量

齿圈与太阳轮旋转比 *gRLS*，定义为齿圈齿数除以大太阳轮齿数。

### **Ring (R) to small sun (SS) teeth ratio (NR/NSS)** — 齿圈与小太阳轮旋转比 `3`（默认）| 大于 (NR/NSL) 的正标量

齿圈与小太阳轮旋转比 *gRSS*，定义为齿圈齿数除以小太阳轮齿数。此齿轮比必须严格大于 **Ring (R) to large sun (SL) teeth ratio (NR/NSL)**。

### 啮合损失

### **Friction model** — 摩擦模型 `No meshing losses - Suitable for HIL simulation`（默认）| `Constant efficiency` | `Temperature-dependent efficiency`

模块的摩擦模型：

- `No meshing losses - Suitable for HIL simulation`
  — 齿轮啮合为理想状态。
- `Constant efficiency` — 齿轮对之间的扭矩传递按恒定效率
  *η* 降低，其中 0 < *η* ≤ 1。
- `Temperature-dependent efficiency` — 齿轮对之间的扭矩传递由基于温度的表查找定义。

### **Large sun-planet, small sun-planet, ring-planet and planet-planet ordinary efficiencies** — 扭矩传递效率 `[.98, .98, .98, .99]`（默认）| 向量

扭矩传递效率向量
[*ηLS*,
*ηSS*,
*ηRP*,
*ηPP*]，分别对应大太阳轮-行星轮、小太阳轮-行星轮、齿圈-行星轮和行星轮-行星轮齿轮对啮合。向量元素必须在 (0,1] 范围内。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`。

### **Temperature** — 温度 `[280, 300, 320]` `K`（默认）| 向量

用于构建一维温度-效率查找表的温度向量。向量元素必须从左到右递增。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Large sun-planet efficiency** — 从大太阳轮到行星轮的扭矩传递效率 `[.95, .9, .85]`（默认）| 向量

描述从大太阳轮到行星轮功率流的输出-输入功率比向量，
*ηLSP*。模块使用这些值构建一维温度-效率查找表。

每个元素是与 **Temperature** 向量中某个温度对应的效率。向量长度必须等于 **Temperature** 向量的长度。向量中每个元素必须在 (0,1] 范围内。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Small sun-planet efficiency** — 从小太阳轮到行星轮的扭矩传递效率 `[.95, .9, .85]`（默认）| 向量

描述从小太阳轮到行星轮功率流的输出-输入功率比向量，
*ηSSP*。模块使用这些值构建一维温度-效率查找表。

每个元素是与 **Temperature** 向量中某个温度对应的效率。向量长度必须等于 **Temperature** 向量的长度。向量中每个元素必须在 (0,1] 范围内。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Ring-planet efficiency** — 从齿圈到行星轮的扭矩传递效率 `[.95, .9, .85]`（默认）| 向量

描述从齿圈到行星轮功率流的输出-输入功率比向量，
*ηRP*。模块使用这些值构建一维温度-效率查找表。

每个元素是与 **Temperature** 向量中某个温度对应的效率。向量长度必须等于 **Temperature** 向量的长度。向量中每个元素必须在 (0,1] 范围内。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Planet-planet efficiency** — 行星轮-行星轮效率 `[.95, .9, .85]`（默认）| 向量

描述从小太阳轮行星轮到大大阳轮行星轮功率流的输出-输入功率比向量，
*ηPP*。模块使用这些值构建一维温度-效率查找表。

每个元素是与 **Temperature** 向量中某个温度对应的效率。向量长度必须等于 **Temperature** 向量的长度。向量中每个元素必须在 (0,1] 范围内。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Large sun-carrier, small sun-carrier, large sun planet-carrier and small sun planet-carrier power thresholds** — 大太阳轮-行星架、小太阳轮-行星架、大太阳轮行星轮-行星架和小太阳轮行星轮-行星架齿轮联轴器的最小效率功率阈值 `[.001, .001, .001, .001]` `W`（默认）| 向量

功率阈值向量，高于此值时应用完整效率因子。按大太阳轮、小太阳轮、大太阳轮行星轮和小太阳轮行星轮的顺序输入阈值，均相对于齿轮架。低于这些值时，双曲正切函数对效率因子进行平滑处理。

当您将 **Friction model** 设置为 `Constant efficiency` 时，模块在无功率传输时将效率损失降至零。当您将 **Friction model** 设置为 `Temperature-dependent efficiency` 时，模块在静止时的零值与功率阈值处温度-效率查找表提供的值之间对效率因子进行平滑处理。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### 粘性损失

### **Large sun-carrier, small sun-carrier, large sun planet-carrier and small sun planet-carrier viscous friction coefficients** — 齿轮粘性摩擦 `[0, 0, 0, 0]` `N*m/(rad/s)`（默认）| 向量

粘性摩擦系数向量
[*μLS*,
*μSS*,
*μLSP*,
*μSSP*]，分别对应大太阳轮-行星架、小太阳轮-行星架、大太阳轮行星轮-行星架和小太阳轮行星轮-行星架齿轮运动。

### 惯量

### **Inertia** — 惯量选项 `off`（默认）| `on`

是否在模块中包含惯量效应。

### **Small sun gear inertia** — 小太阳轮惯量 `0.001` `kg*m^2`（默认）| 正标量

小太阳轮惯量。

#### 依赖关系

要启用此参数，请选中 **Inertia**。

### **Large sun gear inertia** — 大太阳轮惯量 `0.001` `kg*m^2`（默认）| 正标量

大太阳轮惯量。

#### 依赖关系

要启用此参数，请选中 **Inertia**。

### **Ring gear inertia** — 齿圈惯量 `0.001` `kg*m^2`（默认）| 正标量

齿圈惯量。

#### 依赖关系

要启用此参数，请选中 **Inertia**。

### **Carrier gear inertia** — 行星架惯量 `0.001` `kg*m^2`（默认）| 正标量

行星架惯量。

#### 依赖关系

要启用此参数，请选中 **Inertia**。

### **Carrier gear inner radius** — 行星架内半径 `0.01` `m`（默认）| 正标量

行星架内半径。

#### 依赖关系

要启用此参数，请选中 **Inertia**。

### **Carrier gear outer radius** — 行星架外半径 `0.02` `m`（默认）| 正标量

行星架外半径。

#### 依赖关系

要启用此参数，请选中 **Inertia**。

### **Inner planet gear spin inertia** — 内行星轮自旋惯量 `0.001` `kg*m^2`（默认）| 正标量

内行星轮绕自身轴线的惯量。

#### 依赖关系

要启用此参数，请选中 **Inertia**。

### **Inner planet gear mass** — 内行星轮质量 `0.001` `kg`（默认）| 正标量

内行星轮的质量。

#### 依赖关系

要启用此参数，请选中 **Inertia**。

### **Outer planet gear inertia** — 外行星轮惯量 `0.001` `kg*m^2`（默认）| 正标量

外行星轮的转动惯量。此值必须为正。

#### 依赖关系

要启用此参数，请选中 **Inertia**。

### **Outer planet gear mass** — 外行星轮质量 `0.001` `kg`（默认）| 正标量

内行星轮的质量。

#### 依赖关系

要启用此参数，请选中 **Inertia**。

### 热端口

要启用这些设置，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Thermal mass** — 热质量 `50` `J/K`（默认）| 标量

使组件温度变化一个温度单位所需的热能。热质量越大，组件对温度变化的抵抗力越强。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Initial temperature** — 初始温度 `300` `K`（默认）| 标量

仿真开始时的模块温度。初始温度根据各自的效率向量设置初始组件效率。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。
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

您现在可以指定所有齿轮子组件的惯量，包括太阳轮、齿圈和行星架。您现在还可以在行星轮惯量行为中包含行星轮进动的影响。

## 描述

带两个太阳轮和两组行星轮的行星齿轮

Ravigneaux Gear 模块表示具有双太阳轮和行星轮组的行星齿轮系。两个太阳轮位于中心，沿公共旋转轴线纵向分开。其中较小的齿轮与内行星轮组啮合，内行星轮组又与外星轮组啮合。外行星轮组的长度跨越两个太阳轮之间的距离，同时与大太阳轮和齿圈啮合。

行星架将行星轮组固定在不同半径处。行星架与驱动轴刚性连接，可相对于太阳轮和齿圈作为一个整体旋转。每个行星轮与行星架之间的转动副使齿轮能够绕各自的纵向轴线旋转。

太阳轮、行星轮和齿圈之间的相对角速度由它们之间的运动学约束决定。有关更多信息，请参阅方程。

该模块基于 Sun-Planet、Planet-Planet 和 Ring-Planet Simscape™ Driveline™ 模块将 Ravigneaux 齿轮建模为结构组件。图中显示了此结构组件的等效框图。

为提高齿轮模型的保真度，您可以指定齿轮惯量、啮合损失和粘性损失等属性。默认情况下，齿轮惯量和粘性损失假定可忽略不计。该模块允许您指定内行星轮的惯量。要对行星架、大太阳轮、小太阳轮和齿圈的惯量建模，请将 Simscape Inertia 模块连接到端口 **C**、**SL**、**SS** 和 **R**。

### 热模型

您可以通过启用可选热端口来建模热流和温度变化的影响。要启用该端口，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

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
- *NR* 是齿圈的齿数。
- *NSS* 是小太阳轮的齿数。
- *gRSS* 是齿圈与大太阳轮的比。
- *NSL* 是大太阳轮的齿数。

根据这些齿轮比，关键运动学约束为：

(gRSS−1)ωC=gRSSωR−ωSS

(gRSL+1)ωC=gRSLωR+ωSL

六个自由度简化为两个独立自由度。齿轮对为 (1,2) = (*LS*,*P*)、(*SS*,*P*)、(*P*,*R*) 和 (*P*,*P*)。

**警告**

齿轮比 *gRSS* 必须严格大于齿轮比 *gRSL*。齿轮比 *gRSL* 必须严格大于一。

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

在非理想情况下，*τloss* ≠ 0。有关更多信息，请参阅 Model Gears with Losses。

### 假设和限制

- 假定齿轮为刚性。
- 库仑摩擦会减慢仿真速度。有关更多信息，请参阅 Adjust Model Fidelity。
