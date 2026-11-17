---
type: simulink-block
title: 'Harmonic Drive'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears'
documentation_page: 'harmonicdrive'
documentation_source_path: 'ref/harmonicdrive.html'
language: zh-CN
chinese_source: worker-translation
---

# Harmonic Drive

## 端口

### 守恒端口

### **B** — 基座轴机械旋转

与基座轴和应变波发生器关联的机械旋转守恒端口。

当您选择 **Ring gear rotation** 时，此端口对应于 Planetary Gear 模块的端口 **S**。

### **F** — 从动轴机械旋转

与从动轴和柔性花键关联的机械旋转守恒端口。

当您选择 **Ring gear rotation** 时，此端口对应于 Planetary Gear 模块的端口 **R**。

### **C** — 圆形花键机械旋转

与圆形花键关联的机械旋转守恒端口。

此端口对应于 Planetary Gear 模块的端口 **C**。

#### 依赖关系

要启用此端口，请选择 **Ring gear rotation**。

### **H** — 传热热端口

与传热关联的热守恒端口。

#### 依赖关系

要启用此端口，请将 **Friction model** 设置为 `Temperature-dependent efficiency` 或 `Temperature and load-dependent efficiency`。

## 参数

### 主要

### **Ring gear rotation** — 模拟齿圈运动的选项 `off`（默认）| `on`

模拟齿圈旋转的选项。选择此参数将启用端口 **R**。

### **Number of teeth on elliptical gear** — 椭圆齿轮齿数 `100`（默认）| 正标量

从椭圆齿轮周边向外突出的齿的总数。此参数的值应略小于圆形齿圈上的齿数。默认相差两个齿是常见的。两个齿轮齿数的比值定义了基座轴和从动轴的相对角速度。

### **Number of teeth on circular gear** — 圆形齿轮齿数 `102`（默认）| 正标量

从圆形齿圈周边向内突出的齿数。此参数的值应略大于椭圆齿轮上的齿数。默认相差两个齿是常见的。两个齿轮齿数的比值定义了基座轴和从动轴的相对角速度。

### 啮合损耗

### **Friction model** — 齿轮摩擦模型 `No meshing losses - Suitable for HIL simulation`（默认）| `Constant efficiency` | `Load-dependent efficiency` | `Temperature-dependent efficiency` | `Temperature and load-dependent efficiency`

包含摩擦啮合损耗的选项：

- `No meshing losses - Suitable for HIL simulation` — 模块忽略啮合损耗。
- `Constant efficiency` — 您指定一个在整个仿真过程中保持恒定的组件效率。
- `Load-dependent efficiency` — 模块通过可变效率因子降低扭矩传递。该因子落在 0 < *η* < 1 的范围内，并随扭矩负载变化。
- `Temperature-dependent efficiency` — 模块根据端口 **H** 的输入确定扭矩传递效率。该因子落在 0 < *η* ≤ 1 的范围内，且与负载无关。
- `Temperature and load-dependent efficiency` — 模块通过取决于温度和负载的可变效率因子降低扭矩传递。该因子落在 0 < *η* < 1 的范围内，并随扭矩负载变化。

#### 依赖关系

要启用此参数，请清除 **Ring gear rotation**。

### **Efficiency** — 扭矩传递效率 `0.95`（默认）| (0, 1] 范围内的正标量

基座轴和从动轴之间的扭矩传递效率（*η*）。此参数与啮合功率损耗成反比。

#### 依赖关系

要启用此参数，请清除 **Ring gear rotation** 并将 **Friction model** 设置为 `Constant efficiency`。

### **Follower power threshold** — 应用完整效率因子的功率阈值 `0.001` `W`（默认）| 正标量

从动轴功率的绝对值，超过该值时完整效率因子生效。双曲正切函数将效率因子从静止时的零平滑过渡到功率阈值处的完整效率值。

作为指导原则，功率阈值应低于仿真期间预期的传输功率。较高的值可能导致模块低估效率损耗。然而，非常低的值可能会增加仿真的计算成本。

#### 依赖关系

要启用此参数，请清除 **Ring gear rotation** 并将 **Friction model** 设置为 `Constant efficiency`。

### **Input shaft torque at no load** — 空载时输入轴上的净扭矩 `0.1` `N*m`（默认）| 正标量

空载模式下作用在输入轴上的净扭矩（*τ*idle），例如当传递到输出轴的扭矩等于零时。对于非零值，空载模式下的输入功率由于啮合损耗而完全耗散。

#### 依赖关系

要启用此参数，请清除 **Ring gear rotation** 并将 **Friction model** 设置为 `Load-dependent efficiency`。

### **Nominal output torque** — 效率归一化时的扭矩值 `5` `N*m`（默认）| 正标量

用于归一化负载相关效率的输出扭矩（*τ*F）。

#### 依赖关系

要启用此参数，请清除 **Ring gear rotation** 并将 **Friction model** 设置为 `Load-dependent efficiency`。

### **Efficiency at nominal output torque** — 传递效率 `0.95`（默认）| (0,1] 范围内的正标量

额定输出扭矩下的扭矩传递效率（*η*）。较大的效率值对应于输入轴和输出轴之间更大的扭矩传递。

#### 依赖关系

要启用此参数，请清除 **Ring gear rotation** 并将 **Friction model** 设置为 `Load-dependent efficiency`。

### **Follower angular velocity threshold** — 应用完整效率因子的角速度阈值 `0.01` `rad/s`（默认）| 正标量

从动轴角速度的绝对值，超过该值时完整效率因子生效（*ω*F）。低于此值时，双曲正切函数将效率因子平滑过渡到一，在静止时将效率损耗降低到零。

作为指导原则，角速度阈值应低于仿真期间预期的角速度。较高的值可能导致模块低估效率损耗。然而，非常低的值可能会增加仿真的计算成本。

#### 依赖关系

要启用此参数，请清除 **Ring gear rotation** 并将 **Friction model** 设置为 `Load-dependent efficiency`。

### **Temperature** — 用于效率表格参数化的温度数组 `[280 300 320]` `K`（默认）| 向量

用于构建效率查找表的温度数组。数组值必须从左到右递增。在温度相关模型中，温度数组的大小必须与效率数组相同。该数组的大小必须与 **Efficiency** 数组相同。

#### 依赖关系

要启用此参数，请清除 **Ring gear rotation** 并将 **Friction model** 设置为以下之一：

- `Temperature-dependent efficiency`
- `Temperature and load-dependent efficiency`

### **Efficiency** — 齿轮效率数组 `[0.95 0.9 0.85]`（默认）| 向量

用于为温度相关效率模型构建一维温度-效率查找表的效率数组。数组元素是 **Temperature** 数组中各温度对应的效率。两个数组的大小必须相同。

#### 依赖关系

要启用此参数，请清除 **Ring gear rotation** 并将 **Friction model** 设置为以下之一：

- `Temperature-dependent efficiency`
- `Temperature and load-dependent efficiency`

### **Follower power threshold** — 应用数值平滑的功率阈值 `0.001` `W`（默认）| 正标量

从动轴功率的绝对值，超过该值时完整效率因子生效。双曲正切函数在静止时的零与功率阈值处温度-效率查找表提供的值之间平滑效率因子。

#### 依赖关系

要启用此参数，请清除 **Ring gear rotation** 并将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Load at elliptical gear** — 用于效率表格参数化的椭圆齿轮负载 `[1 5 10]` `N*m`（默认）| 数值数组

用于为温度和负载相关效率模型构建二维温度-负载-效率查找表的椭圆齿轮负载数组。数组值必须从左到右递增。负载数组的大小必须与效率矩阵的单列大小相同。

#### 依赖关系

要启用此参数，请清除 **Ring gear rotation** 并将 **Friction model** 设置为 `Temperature and load-dependent efficiency`。

### **Efficiency matrix** — 用于效率表格参数化的效率数组 `[ 0.85 0.8 0.75; 0.95 0.9 0.85; 0.85 0.8 0.7 ]`（默认）| 数值数组

用于构建二维温度-负载-效率查找表的组件效率矩阵。矩阵元素是 **Temperature** 数组中各温度和 **Load at elliptical gear** 数组中各负载对应的效率。

行数必须与 **Temperature** 数组中的元素数相同。列数必须与 **Load at elliptical gear** 数组中的元素数相同。

#### 依赖关系

要启用此参数，请清除 **Ring gear rotation** 并将 **Friction model** 设置为 `Temperature and load-dependent efficiency`。

### **Follower angular velocity threshold** — 应用数值平滑的角速度阈值 `0.01` `rad/s`（默认）| 正标量

从动轴角速度的绝对值，超过该值时完整效率因子生效。低于此值时，双曲正切函数将效率因子平滑过渡到一，在静止时将效率损耗降低到零。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为 `Temperature and load-dependent efficiency`。

### **Friction model** — 摩擦模型 `No meshing losses - Suitable for HIL simulation`（默认）| `Constant efficiency` | `Temperature-dependent efficiency`

模块的摩擦模型：

- `No meshing losses - Suitable for HIL simulation` — 齿轮啮合是理想的。
- `Constant efficiency` — 齿轮对之间的扭矩传递通过恒定效率 *η* 降低，使得 0 < *η* ≤ 1。
- `Temperature-dependent efficiency` — 齿轮对之间的扭矩传递由基于温度的查表定义。

#### 依赖关系

要启用此参数，请选择 **Ring gear rotation**。

### **Sun-planet and ring-planet ordinary efficiencies** — 扭矩传递效率向量 `[.96, .98]`（默认）| 向量

扭矩传递效率向量，其中第一个元素表示应变波发生器与椭圆齿轮之间的关系，第二个元素表示椭圆齿轮与圆形齿圈之间的关系。

#### 依赖关系

要启用此参数，请选择 **Ring gear rotation** 并将 **Friction model** 设置为 `Constant efficiency`。

### **Temperature** — 温度 `[280, 300, 320]` `K`（默认）| 向量

用于构建一维温度-效率查找表的温度向量。向量元素必须从左到右递增。

#### 依赖关系

要启用此参数，请选择 **Ring gear rotation** 并将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Sun-planet efficiency** — 太阳轮到行星轮的扭矩传递效率 `[.95, .9, .85]`（默认）| 向量

描述从应变波发生器到椭圆齿轮的功率流的输出-输入功率比向量。模块使用这些值构建一维温度-效率查找表。

每个元素是与 **Temperature** 向量中某个温度对应的效率。向量的长度必须等于 **Temperature** 向量的长度。向量中的每个元素必须在 (0,1] 范围内。

#### 依赖关系

要启用此参数，请选择 **Ring gear rotation** 并将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Ring-planet efficiency** — 齿圈到行星轮的扭矩传递效率 `[.95, .9, .85]`（默认）| 向量

描述从椭圆齿轮到柔性齿轮的功率流的输出-输入功率比向量。模块使用这些值构建一维温度-效率查找表。

每个元素是与 **Temperature** 向量中某个温度对应的效率。向量的长度必须等于 **Temperature** 向量的长度。向量中的每个元素必须在 (0,1] 范围内。

#### 依赖关系

要启用此参数，请选择 **Ring gear rotation** 并将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### **Sun-carrier and planet-carrier power thresholds** — 太阳轮-行星架和行星轮-行星架齿轮耦合的最小效率功率阈值 `[.001, .001]` `W`（默认）| 向量

完整效率因子生效的功率阈值向量。按应变波发生器-圆形齿轮、椭圆齿轮-圆形齿轮的顺序输入阈值。低于这些值时，双曲正切函数对效率因子进行平滑处理。

当您将 **Friction model** 设置为 `Constant efficiency` 时，模块在没有功率传输时将效率损耗降低到零。当您将 **Friction model** 设置为 `Temperature-dependent efficiency` 时，模块在静止时的零与功率阈值处温度-效率查找表提供的值之间平滑效率因子。

#### 依赖关系

要启用此参数，请选择 **Ring gear rotation** 并将 **Friction model** 设置为 `Constant efficiency` 或 `Temperature-dependent efficiency`。

### 粘性损耗

### **Viscous friction coefficients at base (B) and follower (F)** — 流体动力摩擦系数 `[0 0]` `N*m/(rad/s)`（默认）| 正二元素向量

包含基座轴和从动轴处生效的粘性摩擦系数的二元素数组。默认数组对应于零粘性损耗。

### 惯性

### **Inertia** — 包含惯性的选项 `off`（默认）| `on`

是否包含齿圈旋转产生的惯性。

#### 依赖关系

要启用此参数，请选择 **Ring gear rotation**。

### **Wave generator gear inertia** — 波发生器齿轮的惯性 `0.001` `kg*m^2`（默认）| 正标量

波发生器齿轮的惯性。

#### 依赖关系

要启用此参数，请选择 **Ring gear rotation** 和 **Inertia**。

### **Flexspline gear inertia** — 柔性花键齿轮的惯性 `0.0005` `kg*m^2`（默认）| 正标量

柔性花键齿轮的惯性。

#### 依赖关系

要启用此参数，请选择 **Ring gear rotation** 和 **Inertia**。

### **Ring gear inertia** — 齿圈惯性 `0.001` `kg*m^2`（默认）| 正标量

齿圈旋转产生的惯性。

#### 依赖关系

要启用此参数，请选择 **Ring gear rotation** 和 **Inertia**。

### 热端口

### **Thermal mass** — 热质量 `50` `J/K`（默认）| 正标量

将组件温度改变一度所需的热能。热质量越大，组件对温度变化的抵抗力越强。

### **Initial temperature** — 初始温度 `300` `K`（默认）| 正标量

仿真开始时组件的温度。初始温度根据您指定的效率向量改变组件效率，影响起始啮合或摩擦损耗。

## 所属库

Simscape / Driveline / Gears

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2014a 中引入**

### R2025a：枚举更新

**Ring gear rotation** 和 **Inertia** 参数现在使用复选框。这些参数在之前的版本中使用下拉菜单。

### R2024b：惯性更新

现在您可以指定所有齿轮子组件（包括太阳轮、齿圈和行星架）的惯性。您现在还可以在行星惯量行为中包含行星进动的影响。

## 描述

基于椭圆齿轮弹性变形的高传动比减速器

Harmonic Drive 模块表示一种紧凑的高传动比减速机构，包含三个关键组件：

- 应变波发生器
- 椭圆齿轮
- 圆形齿圈

谐波减速器在设计上具有无背隙和高减速比的特点。这对于需要精确齿轮定位的系统非常有利。基础轴带动应变波发生器旋转，应变波发生器呈椭圆形，其圆周上装有轴承。轴承允许应变波发生器在椭圆齿轮内旋转。椭圆齿轮是柔性的，应变波发生器的运动导致椭圆齿轮的顶点移动。椭圆的这种变形使椭圆齿轮的齿缓慢地沿圆形齿圈的齿爬行。齿圈的齿数多于椭圆齿轮，以允许这种运动。椭圆齿轮在齿圈内旋转的同时将扭矩传递到输出轴。

啮合同时在椭圆齿轮的两个顶点处发生。这种设计使啮合齿数加倍，从而提高了驱动系统的扭矩容量。

两个齿轮之间的内啮合导致椭圆齿轮轴线与椭圆应变波发生器反向旋转。

大减速比源于几乎相等的齿数。有效齿轮减速比为

r=nEnC−nE ，

其中：

- *r* 是齿轮减速比。
- *n*C 是圆形齿圈的齿数。
- *n*E 是椭圆齿轮的齿数。

Simple Gear 模块为该模块提供了基础。

### 齿圈旋转

您可以通过选中 **Ring gear rotation** 参数来启用圆形齿圈的旋转。该模块启用端口 **R**，允许您通过机械旋转输入信号控制齿圈的旋转运动。

**注意**

**Ring gear rotation** 参数决定了您如何参数化啮合损耗。

当您清除 **Ring gear rotation** 时，该模块使用 Simple Gear 模块实现来计算效率。在这种情况下，您以与 Simple Gear 模块相同的方式参数化啮合损耗。当您选中 **Ring gear rotation** 时，该模块通过实现 Planetary Gear 模块来计算效率。在这种情况下，您以与 Planetary Gear 模块相同的方式参数化啮合损耗。

### 热模型

您可以通过启用可选热端口来对热流和温度变化的影响进行建模。要启用该端口，请将 **Friction model** 设置为 `Temperature-dependent efficiency`。

### 变量

使用 **Variables** 设置在仿真前设置模块变量的优先级和初始目标值。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。
