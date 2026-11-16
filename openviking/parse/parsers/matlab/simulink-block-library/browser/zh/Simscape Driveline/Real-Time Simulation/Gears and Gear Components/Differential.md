---
type: simulink-block
title: 'Differential'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Gears / Gear Assemblies'
documentation_page: 'differential'
documentation_source_path: 'ref/differential.html'
language: zh-CN
chinese_source: worker-translation
---

# Differential

## 端口

### 守恒

### **D** — Driveshaft rotational mechanical

与纵向传动轴关联的旋转机械守恒端口。

### **S1** — Sun gear 1 rotational mechanical

与太阳轮 1 关联的旋转守恒端口。

### **S2** — Sun gear 2 rotational mechanical

与太阳轮 2 关联的旋转守恒端口。

### **H** — Heat flow thermal

与热流关联的热守恒端口。热流通过改变齿轮温度影响动力传输效率。

#### 依赖关系

要启用此端口，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

## 参数

### 主要

### **Crown gear located** — Crown gear location `To the right of centerline` (default) | `To the left of centerline`

锥冠状齿轮相对于齿轮组中心线的位置。

### **Carrier (C) to driveshaft (D) teeth ratio (NC/ND)** — Carrier to driveshaft gear rotation ratio `4` (default) | positive scalar

固定比 *gD*，即行星架齿轮与纵向传动轴齿轮旋转之比，定义为行星架齿轮齿数除以传动轴齿轮齿数。此齿轮比必须严格大于 `0`。

### 啮合损失

### **Friction model** — Friction model `No meshing losses - Suitable for HIL simulation` (default) | `Constant efficiency` | `Temperature-dependent efficiency`

该模块的摩擦模型：

- `No meshing losses - Suitable for HIL simulation`
  — 齿轮啮合是理想的。
- `Constant efficiency` — 齿轮副之间的扭矩传递会因恒定效率 *η* 而降低，其中 0 < *η* ≤ 1。
- `Temperature-dependent efficiency` — 齿轮副之间的扭矩传递由基于温度的表查找定义。

### **Sun-sun and carrier-driveshaft ordinary efficiencies** — Torque transfer efficiencies `[.85, .92]` (default) | vector

扭矩传递效率向量 [*ηSS*, *ηCD*]，分别表示从主动太阳轮到从动太阳轮以及从行星架到纵向传动轴的效率。向量元素必须在范围 (0,1] 内。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`。

### **Temperature** — Temperature `[280, 300, 320]` `K` (default) | vector

用于构造一维温度-效率查找表的温度向量。向量元素必须从左到右递增。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Sun-sun efficiency** — Driving sun gear to driven sun gear torque transfer efficiency `[.95, .9, .85]` (default) | vector

描述从主动太阳轮到从动太阳轮功率流的输出输入功率比向量，*ηSS*。该模块使用这些值构造一维温度-效率查找表。

每个元素是与 **Temperature** 向量中某个温度对应的效率。向量长度必须等于 **Temperature** 向量的长度。向量中的每个元素必须在范围 (0,1] 内。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Carrier-driveshaft efficiency** — Carrier to driveshaft gear torque transfer efficiency `[.95, .9, .85]` (default) | vector

描述从行星架到传动轴功率流的输出输入功率比向量，*ηCD*。该模块使用这些值构造一维温度-效率查找表。

每个元素是与 **Temperature** 向量中某个温度对应的效率。向量长度必须等于 **Temperature** 向量的长度。向量中的每个元素必须在范围 (0,1] 内。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Sun-carrier and driveshaft-casing power thresholds** — Minimum efficiency power threshold for the sun-carrier and driveshaft-casing gear couplings `[0.001, 0.001]` `W` (default) | vector

功率阈值向量 *pth*，分别用于太阳轮-行星架和纵向传动轴-壳体 [*pS*, *pD*]。高于这些值时，应用完整效率损失。低于这些值时，双曲正切函数会平滑效率因子。

当您将 **Friction model** 设置为 `Constant efficiency` 时，模块在没有功率传输时将效率损失降为零。当您将 **Friction model** 设置为 `Temperature-dependent efficiency` 时，模块会在静止时的零值与功率阈值处温度-效率查找表提供的值之间平滑效率因子。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency` 或 `Temperature-dependent efficiency`。

### 粘性损失

### **Sun-carrier and driveshaft-casing viscous friction coefficients** — Viscous friction coefficients `[0, 0]` `N*m/(rad/s)` (default) | vector

粘性摩擦系数向量 [*μS* *μD* ]，分别用于太阳轮到行星架齿轮以及纵向传动轴到壳体齿轮的运动。

### 惯性

### **Inertia** — Inertia option `off` (default) | `on`

是否在模块中包含惯性效应。

### **Sun gear inertia** — Sun gear inertia `0.001` `kg*m^2` (default) | positive scalar

太阳轮惯性。

#### 依赖关系

要启用此参数，请选择 **Inertia**。

### **Sun gear radius** — Sun gear radius `0.01` `m` (default) | positive scalar

太阳轮半径。

#### 依赖关系

要启用此参数，请选择 **Inertia**。

### **Carrier inertia** — Carrier gear inertia `0.001` `kg*m^2` (default) | positive scalar

行星齿轮架的转动惯量。

#### 依赖关系

要启用此参数，请选择 **Inertia**。

### **Planet gear spin inertia** — Planet gear spin inertia `0.001` `kg*m^2` (default) | positive scalar

行星齿轮绕其自身轴线的惯性。

#### 依赖关系

要启用此参数，请选择 **Inertia**。

### **Planet gear mass** — Planet gear mass `0.001` `kg*m^2` (default) | positive scalar

行星齿轮质量。

#### 依赖关系

要启用此参数，请选择 **Inertia**。

### 热端口

要启用这些设置，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Thermal mass** — Thermal mass `50` `J/K` (default) | scalar

使组件温度改变一个温度单位所需的热能。热质量越大，组件对温度变化越不敏感。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Initial temperature** — Initial temperature `300` `K` (default) | scalar

仿真开始时的模块温度。初始温度根据各自的效率向量设置初始组件效率。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

## 所属库

Simscape / Driveline / Gears

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## 版本历史

**Introduced in R2011a**

### R2025a: Enumeration Updates

**Inertia** 参数现在使用复选框。在以前的版本中，此参数使用下拉列表。

### R2024b: Inertia updates

现在，您可以指定所有齿轮子组件（包括太阳轮、齿圈和行星架齿轮）的惯性。现在，您还可以在行星齿轮惯性行为中包含行星进动的影响。

## 描述

Gear mechanism that allows driven shafts to spin at different speeds

Differential 模块表示一种允许从动轴以不同速度旋转的齿轮机构。差速器在汽车中很常见，它们使各个车轮在转弯时能够以不同速度旋转。端口 **D**、**S1** 和 **S2** 分别表示差速器的纵向传动轴和太阳轮轴。任一轴都可以驱动另外两个轴。

该模块将差速器机构建模为基于 Simple Gear 和 Sun-Planet Bevel Simscape™ Driveline™ 模块的结构组件。该图展示了 Differential 模块的等效框图。

为提高齿轮模型的保真度，请指定齿轮惯性、啮合损失和粘性损失等属性。默认情况下，齿轮惯性和粘性损失假定可忽略不计。该模块允许您指定齿轮行星架和内部行星齿轮的惯性。要对行星齿轮的惯性建模，请将 Simscape Inertia 模块连接到端口 **D**、**S1** 和 **S2**。

### 热建模

您可以通过启用可选热端口来对热流和温度变化的影响进行建模。要启用该端口，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### 方程

**Ideal Gear Constraints and Gear Ratios**

差速器对三个连接轴施加一个运动学约束，使得

ωS1−ωS2,

其中：

- *ωS1* 是太阳轮轴 1 的速度。
- *ωS2* 是太阳轮轴 2 的速度。

负值意味着差速器位于中心线左侧。三个自由度缩减为两个独立自由度。齿轮对为 (1,2) = (*S*, *S*) 和 (*C*, *D*)。*C* 是行星架。

横向运动之和是变换后的纵向运动。侧向运动之差 ωS1−ωS2 与纵向运动无关。横向轴的一般运动是这两个独立自由度的叠加，它们具有以下物理意义：

- 纵向自由度等效于两个横向轴以相同角速度 ωS1=ωS2 旋转，并且相对于纵向轴保持固定比。
- 差速自由度等效于保持纵向驱动轴锁定，ωD=0，其中 *ωD* 是驱动轴的速度，同时横向轴彼此以相反方向相对旋转，ωS1=−ωS2。

横向轴扭矩受纵向轴扭矩约束，使得净功率流之和为零：

ωS1τS1+ωS2τS2+ωDτD−Ploss=0,

其中：

- *τS1* 和 *τS2* 是沿横向轴的扭矩。
- *τD* 是纵向扭矩。
- *Ploss* 是功率损失。

当运动学约束和功率约束结合时，理想情况给出

gDτD=2(ωS1τS1+ωS2τS2)ωS1+ωS2,

其中 *gD* 是纵向传动轴的齿轮比。

**Ideal Fundamental Constraints**

有效的 Differential 模块约束由两个太阳轮-行星轮锥齿轮子约束组成。

- 第一个子约束是由于两个太阳轮-行星轮锥齿轮与行星架的耦合：

  ωS1−ωCωS2−ωC=−gSP2gSP1,

  其中 *gSP1* 和 *gSP2* 是太阳轮-行星轮齿轮的齿轮比。
- 第二个子约束是由于行星架与纵向传动轴的耦合：

  ωD=−gDωC.

底层太阳轮-行星轮锥齿轮的太阳轮-行星轮齿轮比，以太阳轮-行星轮齿轮的半径 *r* 表示，为：

gSP1=rS1rP1

gSP2=rS2rP2

Differential 模块实现为 gSP1=gSP2=1，使 *gD* 可自由调整。

**Nonideal Gear Constraints and Losses**

在非理想情况下，*τloss* ≠ 0。有关详细信息，请参阅 Model Gears with Losses。

### 假设和限制

- 假定齿轮是刚性的。
- 库仑摩擦会减慢仿真速度。有关详细信息，请参阅 Adjust Model Fidelity。
