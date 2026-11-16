---
type: simulink-block
title: 'Planet-Planet'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Gears / Planetary Gear Subcomponents'
documentation_page: 'planetplanet'
documentation_source_path: 'ref/planetplanet.html'
language: zh-CN
chinese_source: worker-translation
---

# Planet-Planet

## 端口

### 守恒

### **C** — 行星轮行星架旋转机械

与行星轮行星架关联的旋转机械守恒端口。

### **Po** — 外行星轮旋转机械

与外行星轮关联的旋转机械守恒端口。

### **Pi** — 内行星轮旋转机械

与内行星轮关联的旋转机械守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。热流通过改变齿轮温度影响功率传输效率。

#### 依赖关系

要启用此端口，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

## 参数

### 主要

### **外行星轮 (Po) 到内行星轮 (Pi) 齿数比 (NPo/NPi)** — 外行星轮与内行星轮旋转比 `2`（默认） | positive scalar

比率 *goi*，即外行星轮旋转与内行星轮旋转之比，由外行星轮齿数除以内行星轮齿数定义。该齿轮比必须严格为正。

### 啮合损失

### **摩擦模型** — 摩擦模型 `No meshing losses - Suitable for HIL simulation`（默认） | `Constant efficiency` | `Temperature-dependent efficiency`

模块的摩擦模型：

- `No meshing losses - Suitable for HIL simulation`
  — 齿轮啮合为理想情况。
- `Constant efficiency` — 齿轮轮对之间的扭矩传递按恒定效率 *η* 降低，使得 0 < *η* ≤ 1。
- `Temperature-dependent efficiency` — 齿轮轮对之间的扭矩传递由基于温度的表查找定义。

### **普通效率** — 扭矩传递效率 `0.98`（默认） | scalar

外行星轮与内行星轮轮对啮合的扭矩传递效率 *ηPP*。该值必须在范围 (0,1] 内。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Constant efficiency`。

### **温度** — 温度 `[280, 300, 320]` `K`（默认） | vector

用于构造一维温度-效率查找表的温度向量。向量元素必须从左到右递增。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

### **效率** — 齿轮效率 `[.95, .9, .85]`（默认） | vector

描述从外行星轮到内行星轮功率流的输出/输入功率比向量，*ηPP*。该模块使用这些值构造一维温度-效率查找表。

每个元素是一个效率，与 **温度** 向量中的某个温度对应。该向量的长度必须等于 **温度** 向量的长度。向量中的每个元素必须在范围 (0,1] 内。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

### **内行星轮-行星架功率阈值** — 内行星轮-行星架齿轮耦合的最小效率功率阈值 `0.001` `W`（默认） | scalar

功率阈值 *pth*，高于该值时全效率生效。低于该值时，双曲正切函数会平滑效率因子。

当您将 **摩擦模型** 设置为 `Constant efficiency` 时，该模块在未传输功率时将效率损失降低为零。当您将 **摩擦模型** 设置为 `Temperature-dependent efficiency` 时，该模块会在静止时的零与功率阈值处由温度-效率查找表提供的值之间平滑效率因子。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Constant efficiency` 或 `Temperature-dependent efficiency`。

### 粘性损失

### **内行星轮-行星架粘性摩擦系数** — 齿轮粘性摩擦 `0` `N*m/(rad/s)`（默认） | scalar

内行星轮-行星架齿轮运动的粘性摩擦系数 *μPi*。

### 热端口

要启用此参数，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

### **热质量** — 热质量 `50` `J/K`（默认） | scalar

将组件温度改变一个温度单位所需的热能。热质量越大，组件越难以发生温度变化。

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

具有可调齿轮比和摩擦损失的行星架、内行星轮和外行星轮行星齿轮组

Planet-Planet 齿轮模块表示一个行星架和两个内-外行星轮齿轮对。两个行星轮都连接到行星架并相对于行星架旋转。行星轮以您指定的固定齿轮比同向旋转。有关模型详细信息，请参阅方程。

### 热模型

您可以通过启用可选热端口来对热流和温度变化的影响进行建模。要启用该端口，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

### 方程

**理想齿轮约束与齿轮比**

Planet-Planet 模块对三个连接轴施加一个运动学约束和一个几何约束：

rCωC=rPoωPo+rPiωPi

rC=rPo+rPi

外行星轮到内行星轮的齿轮比为

goi=rPo/rPi=NPo/NPi,

其中 *N* 是每个齿轮的齿数。就这个比率而言，关键运动学约束为

(1 +goi)ωC=ωPi+goiωPo.

三个自由度减少为两个独立自由度。齿轮对为 (1, 2) = (*Pi*,*Po*)。

扭矩传递为

goiτPi+τPo–τloss= 0.

在无扭矩损失的理想情况下，*τloss* = 0。

**非理想齿轮约束与损失**

在非理想情况下，*τloss* ≠ 0。有关详细信息，请参阅 Model Gears with Losses。

### 变量

在仿真前，使用 **变量** 设置为模块变量设置优先级和初始目标值。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

### 假设与限制

- 假设齿轮惯量可忽略不计。
- 齿轮被视为刚性组件。
- 库仑摩擦会减慢仿真速度。有关详细信息，请参阅 Adjust Model Fidelity。
