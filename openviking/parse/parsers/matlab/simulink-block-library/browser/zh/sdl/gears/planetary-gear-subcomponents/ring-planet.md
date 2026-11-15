---
type: simulink-block
title: 'Ring-Planet'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Gears / Planetary Gear Subcomponents'
documentation_page: 'ringplanet'
documentation_source_path: 'ref/ringplanet.html'
language: zh-CN
chinese_source: worker-translation
---

# Ring-Planet

## 端口

### 守恒

### **C** — 行星架旋转机械

与行星架关联的旋转机械守恒端口。

### **R** — 齿圈旋转机械

与齿圈关联的旋转机械守恒端口。

### **P** — 行星齿轮旋转机械

与行星齿轮关联的旋转机械守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。热流通过改变齿轮温度来影响动力传输效率。

#### 依赖关系

要启用此端口，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

## 参数

### 主要

### **齿圈 (R) 到行星轮 (P) 齿数比 (NR/NP)** — 齿圈到行星齿轮旋转比 `2` (默认) | 大于 1 的标量

比值 *gRP*，即齿圈旋转与行星齿轮旋转之比，定义为齿圈齿数除以行星齿轮齿数。该齿轮比必须严格大于 1。

### 啮合损失

### **摩擦模型** — 摩擦模型 `No meshing losses - Suitable for HIL simulation` (默认) | `Constant efficiency` | `Temperature-dependent efficiency`

模块的摩擦模型：

- `No meshing losses - Suitable for HIL simulation` — 齿轮啮合是理想的。
- `Constant efficiency` — 齿轮轮对之间的扭矩传递由恒定效率 *η* 降低，使得 0 < *η* ≤ 1。
- `Temperature-dependent efficiency` — 齿轮轮对之间的扭矩传递由基于温度的查表定义。

### **普通效率** — 扭矩传递效率 `0.98` (默认) | 标量

用于外侧和内侧行星齿轮轮对啮合的扭矩传递效率 *ηRP*。此值必须在范围 (0,1] 内。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Constant efficiency`。

### **温度** — 温度 `[280, 300, 320]` `K` (默认) | 向量

用于构造一维温度-效率查找表的温度向量。向量元素必须从左到右递增。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

### **效率** — 齿轮效率 `[.95, .9, .85]` (默认) | 向量

描述从齿圈到行星齿轮功率流的输出与输入功率比向量 *ηRP*。模块使用这些值构造一维温度-效率查找表。

每个元素是与 **温度** 向量中某个温度相关的效率。向量的长度必须等于 **温度** 向量的长度。向量中的每个元素必须在范围 (0,1] 内。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

### **行星架功率阈值** — 行星架齿轮耦合的最小效率功率阈值 `0.001` `W` (默认) | 标量

功率阈值 *pth*，高于该值时全效率生效。低于该值时，双曲正切函数会平滑效率因子。

当您将 **摩擦模型** 设置为 `Constant efficiency` 时，模块在未传输功率时将效率损失降至零。当您将 **摩擦模型** 设置为 `Temperature-dependent efficiency` 时，模块在功率阈值处将效率因子在静止时的零与温度-效率查找表提供的值之间进行平滑。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Constant efficiency` 或 `Temperature-dependent efficiency`。

### 黏性损失

### **行星架黏性摩擦系数** — 齿轮黏性摩擦 `0` `N*m/(rad/s)` (默认) | 标量

用于行星架齿轮运动的黏性摩擦系数 *μP*。

### 热端口

要启用此参数，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

### **热质量** — 热质量 `50` `J/K` (默认) | 标量

将组件温度变化一个温度单位所需的热能。热质量越大，组件越难以发生温度变化。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

## 所属库

Simscape / Driveline / Gears / Planetary Subcomponents

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

## 描述

具有可调齿轮比和摩擦损失的行星架、行星轮和齿圈行星齿轮组

Ring-Planet 模块表示一个行星架、一个齿圈和一组行星齿轮。行星齿轮连接到行星架并相对于行星架旋转。行星齿轮和齿圈以您指定的固定齿轮比共同旋转。齿圈-行星轮和太阳轮-行星轮齿轮是行星齿轮组的基本元素。有关模型详细信息，请参阅方程。

### 热模型

您可以通过启用可选热端口来建模热流和温度变化的影响。要启用该端口，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

### 方程

**理想齿轮约束和齿轮比**

Ring-Planet 模块对三个相连轴施加一个运动学约束和一个几何约束：

rRωR=rCωC+rPωP

rR=rC+rP

齿圈-行星轮齿轮比为

gRP=rR/rP=NR/NP,

其中 *N* 是每个齿轮的齿数。就这个比值而言，关键运动学约束为

gRPωR=ωP+ (gRP– 1)ωC.

三个自由度减少为两个独立自由度。齿轮对为 (1, 2) = (*P*, *R*)。

**警告**

齿圈-行星轮齿轮比 *gRP* 必须严格大于 1。

扭矩传递为：

gRPτP+τR–τloss= 0.

在无扭矩损失的理想情况下，*τloss* = 0。

**非理想齿轮约束和损失**

在非理想情况下，*τloss* ≠ 0。有关详细信息，请参阅对带损失的齿轮建模。

### 变量

使用 **变量** 设置可在仿真前设置模块变量的优先级和初始目标值。有关详细信息，请参阅为模块变量设置优先级和初始目标。

### 假设和限制

- 假设齿轮惯性可忽略不计。
- 齿轮被视为刚性组件。
- 库仑摩擦会减慢仿真速度。有关详细信息，请参阅调整模型保真度。
