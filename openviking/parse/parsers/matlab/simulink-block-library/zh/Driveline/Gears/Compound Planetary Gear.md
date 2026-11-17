---
type: simulink-block
title: 'Compound Planetary Gear'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears'
documentation_page: 'compoundplanetarygear'
documentation_source_path: 'ref/compoundplanetarygear.html'
language: zh-CN
chinese_source: worker-translation
---

# Compound Planetary Gear

## 端口
```yaml
ports:
- name: C
  summary: 行星齿轮架旋转机械
  direction: unspecified
- name: R
  summary: 齿圈旋转机械
  direction: unspecified
- name: S
  summary: 太阳轮旋转机械
  direction: unspecified
- name: H
  summary: 热流热
  direction: unspecified
```

### 守恒

### **C** — 行星齿轮架旋转机械

与行星齿轮架关联的旋转机械守恒端口。

### **R** — 齿圈旋转机械

与齿圈关联的旋转机械守恒端口。

### **S** — 太阳轮旋转机械

与太阳轮关联的旋转机械守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。热流通过改变齿轮温度影响动力传输效率。

#### 依赖关系

要启用此端口，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。
## 参数
```yaml
parameters:
- name: Ring (R) to planet (P) teeth ratio (NR/NP)
  summary: 齿圈与行星轮旋转比 2（默认）| 大于 1 的标量
  group: 主要
- name: Planet (P) to sun (S) teeth ratio (NP/NS)
  summary: 行星轮与太阳轮旋转比 1（默认）| 正标量
  group: 主要
- name: Friction model
  summary: 摩擦模型 No meshing losses - Suitable for HIL simulation（默认）| Constant efficiency | Temperature-dependent efficiency
  group: 啮合损失
- name: Sun-planet and ring-planet ordinary efficiencies
  summary: 扭矩传递效率 [.96 .98]（默认）| 向量
  group: 啮合损失
- name: Temperature
  summary: 温度 [280, 300, 320] K（默认）| 向量
  group: 啮合损失
- name: Sun-planet efficiency
  summary: 太阳轮-行星轮效率 [.95, .9, .85]（默认）| 向量 | rot
  group: 啮合损失
- name: Ring-planet efficiency
  summary: 齿圈-行星轮效率 [.95 .9 .85]（默认）| 向量
  group: 啮合损失
- name: Sun-carrier and planet-carrier power thresholds
  summary: 太阳轮-行星架和行星轮-行星架齿轮联轴器的最低效率功率阈值 [.001, .001] W（默认）| 向量
  group: 啮合损失
- name: Sun-carrier and planet-carrier viscous friction coefficients
  summary: 齿轮粘性摩擦 [0 0] N*m/(rad/s)（默认）| 向量
  group: 粘性损失
- name: Inertia
  summary: 惯量选项 off（默认）| on
  group: 惯量
- name: Sun gear inertia
  summary: 太阳轮惯量 0.001 kg*m^2（默认）| 正标量
  group: 惯量
- name: Ring gear inertia
  summary: 齿圈惯量 0.001 kg*m^2（默认）| 正标量
  group: 惯量
- name: Carrier gear inertia
  summary: 行星架惯量 0.001 kg*m^2（默认）| 正标量
  group: 惯量
- name: Carrier gear radius
  summary: 行星架半径 0.01 m（默认）| 正标量
  group: 惯量
- name: Planet gear spin inertia
  summary: 行星轮自旋惯量 0.001 kg*m^2（默认）| 正标量
  group: 惯量
- name: Planet gear mass
  summary: 行星轮质量 0.001 kg*m^2（默认）| 正标量
  group: 惯量
- name: Thermal mass
  summary: 热质量 50 J/K（默认）| 标量
  group: 热端口
- name: Initial temperature
  summary: 初始温度 300 K（默认）| 标量
  group: 热端口
```

### 主要

### **Ring (R) to planet (P) teeth ratio (NR/NP)** — 齿圈与行星轮旋转比 `2`（默认）| 大于 `1` 的标量

齿圈与行星轮旋转的固定比值 *gRP*，定义为齿圈齿数除以行星轮齿数。此齿轮比必须严格大于 `1`。

### **Planet (P) to sun (S) teeth ratio (NP/NS)** — 行星轮与太阳轮旋转比 `1`（默认）| 正标量

行星轮与太阳轮旋转的固定比值 *gPS*，定义为行星轮齿数除以太阳轮齿数。此齿轮比必须严格大于 `0`。

### 啮合损失

### **Friction model** — 摩擦模型 `No meshing losses - Suitable for HIL simulation`（默认）| `Constant efficiency` | `Temperature-dependent efficiency`

模块的摩擦模型：

- `No meshing losses - Suitable for HIL simulation` — 齿轮啮合为理想状态。
- `Constant efficiency` — 齿轮对之间的扭矩传递按恒定效率 *η* 降低，其中 0 < *η* ≤ 1。
- `Temperature-dependent efficiency` — 齿轮对之间的扭矩传递由基于温度的查表定义。

### **Sun-planet and ring-planet ordinary efficiencies** — 扭矩传递效率 `[.96 .98]`（默认）| 向量

太阳轮-行星轮和齿圈-行星架齿轮对啮合的扭矩传递效率向量 [*ηSP* *ηRP*]。向量元素必须在区间 (0,1] 内。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`。

### **Temperature** — 温度 `[280, 300, 320]` `K`（默认）| 向量

用于构建一维温度-效率查找表的温度向量。向量元素必须从左到右递增。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Sun-planet efficiency** — 太阳轮-行星轮效率 `[.95, .9, .85]`（默认）| 向量 | rot

描述从太阳轮到行星轮功率流的输出-输入功率比向量 *ηSP*。模块使用这些值构建一维温度-效率查找表。

每个元素是与 **Temperature** 向量中某个温度对应的效率。向量长度必须等于 **Temperature** 向量的长度。向量中每个元素必须在范围 (0,1] 内。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Ring-planet efficiency** — 齿圈-行星轮效率 `[.95 .9 .85]`（默认）| 向量

组件效率向量 *ηRP*——输出功率与输入功率之比，模块使用这些值构建一维温度-效率查找表。

每个元素是与 **Temperature** 向量中某个温度对应的效率。向量长度必须等于 **Temperature** 向量的长度。向量中每个元素必须在范围 (0,1] 内。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Sun-carrier and planet-carrier power thresholds** — 太阳轮-行星架和行星轮-行星架齿轮联轴器的最低效率功率阈值 `[.001, .001]` `W`（默认）| 向量

功率阈值向量，超过该阈值时应用完整效率因子。按太阳轮-行星架、行星轮-行星架的顺序输入阈值。低于这些值时，双曲正切函数对效率因子进行平滑处理。

当您将 **Friction model** 设置为 `Constant efficiency` 时，模块在无功率传输时将效率损失降至零。当您将 **Friction model** 设置为 `Temperature-dependent efficiency` 时，模块在功率阈值处对静止时为零与温度-效率查找表提供的值之间的效率因子进行平滑处理。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency` 或 `Temperature-dependent efficiency`。

### 粘性损失

### **Sun-carrier and planet-carrier viscous friction coefficients** — 齿轮粘性摩擦 `[0 0]` `N*m/(rad/s)`（默认）| 向量

太阳轮-行星架和行星轮-行星架齿轮运动的粘性摩擦系数向量 [*μS* *μP*]。

### 惯量

### **Inertia** — 惯量选项 `off`（默认）| `on`

是否在模块中包含惯量效应。

### **Sun gear inertia** — 太阳轮惯量 `0.001` `kg*m^2`（默认）| 正标量

太阳轮惯量。

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

### **Carrier gear radius** — 行星架半径 `0.01` `m`（默认）| 正标量

行星架半径。

#### 依赖关系

要启用此参数，请选中 **Inertia**。

### **Planet gear spin inertia** — 行星轮自旋惯量 `0.001` `kg*m^2`（默认）| 正标量

行星轮绕自身轴线的惯量。

#### 依赖关系

要启用此参数，请选中 **Inertia**。

### **Planet gear mass** — 行星轮质量 `0.001` `kg*m^2`（默认）| 正标量

行星轮质量。

#### 依赖关系

要启用此参数，请选中 **Inertia**。

### 热端口

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Thermal mass** — 热质量 `50` `J/K`（默认）| 标量

将组件温度改变一个温度单位所需的热能。热质量越大，组件对温度变化的抵抗能力越强。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Initial temperature** — 初始温度 `300` `K`（默认）| 标量

仿真开始时模块的温度。初始温度根据各自的效率向量设置初始组件效率。

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

您现在可以指定所有齿轮子组件的惯量，包括太阳轮、齿圈和行星架齿轮。您现在还可以在行星轮惯量行为中包含行星轮进动的影响。

## 描述

带阶梯行星轮组的行星齿轮系

Compound Planetary Gear 模块表示具有复合行星轮的行星齿轮系。每个复合行星轮是一对刚性连接且纵向排列的不同半径的齿轮。两个齿轮中的一个与中心位置的太阳轮啮合，另一个与外齿圈啮合。

**Compound Planetary Gear**

该模块基于 Simscape™ Driveline™ 的 Sun-Planet 和 Ring-Planet 模块，将复合行星齿轮建模为结构组件。图中展示了 Compound planetary gear 模块的等效框图。

为提高齿轮模型的保真度，可指定齿轮惯量、啮合损失和粘性损失等属性。默认情况下，假设齿轮惯量和粘性损失可忽略不计。该模块允许您指定内部行星轮的惯量。要对行星架、太阳轮和齿圈的惯量建模，请将 Simscape Inertia 模块连接到端口 **C**、**S** 和 **R**。

### 热模型

您可以通过启用可选热端口来对热流和温度变化的影响进行建模。要启用该端口，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### 方程

**理想齿轮约束和齿轮比**

Compound Planetary Gear 模块施加两个运动学约束和两个几何约束。

rCωC=rSωS+rP1ωP，

rRωR=rCωC+rP2ωP，

rC=rS+rP1，

rR=rC+rP2，

其中：

- *rC* 是行星架的半径。
- *ωC* 是行星架的角速度。
- *rS* 是太阳轮的半径。
- *ωS* 是太阳轮的角速度。
- *rP1* 是行星轮 1 的半径。
- *ωP* 是行星轮的角速度。
- *rP2* 是行星轮 2 的半径。
- *rR* 是齿圈的半径。

齿圈-行星轮和行星轮-太阳轮齿轮比为：

gRP=rR/rP2=NR/NP2

和

gPS=rP1/rS=NP1/NS，

其中：

- *gRP* 是齿圈-行星轮齿轮比。
- *NR* 是齿圈上的齿数。
- *NP2* 是行星轮 2 上的齿数。
- *gPS* 是行星轮-太阳轮齿轮比。
- *NP1* 是行星轮 1 上的齿数。
- *NS* 是太阳轮上的齿数。

就齿轮比而言，关键运动学约束为：

(1 + gRPgPS)ωC = ωS + gRPgPSωR。

四个自由度简化为两个独立自由度。齿轮对为 (1, 2) = (*P2*, *R*) 和 (*S*, *P1*)。

**警告**

齿轮比 *gRP* 必须严格大于一。

扭矩传递为：

gRPτP2 + τR– τloss(P2,R) = 0

和

gPSτS + τP1 – τloss(S,P1)=0，

其中：

- *τP2* 是行星轮 2 的扭矩传递。
- *τR* 是齿圈的扭矩传递。
- *τloss* 是扭矩传递损失。
- *τS* 是太阳轮的扭矩传递。
- *τP1* 是行星轮 1 的扭矩传递。

在无扭矩损失的理想情况下，*τloss* = 0。

**非理想齿轮约束和损失**

在非理想情况下，*τloss* ≠ 0。有关详细信息，请参阅 Model Gears with Losses。

### 假设和限制

- 假设齿轮惯量可忽略不计。
- 齿轮被视为刚性组件。
- 库仑摩擦会减慢仿真速度。有关详细信息，请参阅 Adjust Model Fidelity。
