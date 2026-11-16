---
type: simulink-block
title: 'Sun-Planet'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears / Planetary Subcomponents'
documentation_page: 'sunplanet'
documentation_source_path: 'ref/sunplanet.html'
language: zh-CN
chinese_source: worker-translation
---

# Sun-Planet

## 端口

### 守恒

### **C** — 行星齿轮架旋转机械

与行星齿轮架相关联的旋转守恒端口。

### **P** — 行星齿轮旋转机械

与行星齿轮相关联的旋转守恒端口。

### **S** — 太阳轮旋转机械

与太阳轮相关联的旋转守恒端口。

### **H** — 热流（热）

与热流相关联的热守恒端口。热流通过改变齿轮温度来影响功率传输效率。

#### 依赖关系

要启用此端口，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

## 参数

### 主要

### **行星轮 (P) 与太阳轮 (S) 齿数比 (NP/NS)** — 行星轮-太阳轮齿轮比 `2` (默认) | 正标量

行星齿轮半径与太阳轮齿轮半径之比 *gPS*。

### 啮合损失

### **摩擦模型** — 摩擦模型 `No meshing losses - Suitable for HIL simulation` (默认) | `Constant efficiency` | `Temperature-dependent efficiency`

模块的摩擦模型：

- `No meshing losses - Suitable for HIL simulation`
  — 齿轮啮合是理想的。
- `Constant efficiency` — 齿轮轮对之间的扭矩传递由一个恒定效率 *η* 降低，
  满足 0 < *η* ≤ 1。
- `Temperature-dependent efficiency` — 齿轮轮对之间的扭矩传递由基于温度的表查找定义。

### **普通效率** — 效率 `0.98` (默认) | 标量 | `0` < *ηSP* ≤ `1`

太阳轮-行星轮齿轮轮对啮合的扭矩传递效率 *ηSP*。该值必须大于 `0` 且小于或等于 `1`。

#### 依赖关系

当 **摩擦模型** 参数设置为 `Constant efficiency` 时，会显示此参数。

### **温度** — 温度 `[280, 300, 320]` `K` (默认) | 向量

用于构造一维温度-效率查找表的温度向量。向量元素必须从左到右递增。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

### **效率** — 齿轮效率 `[.95, .9, .85]` (默认) | 数组 | `0` < *ηSP* ≤ `1`

机械效率数组，即输出功率与输入功率之比，用于从齿圈到行星齿轮的功率流，*ηRP*。该模块使用这些值构造一维温度-效率查找表。

每个元素都是一个效率，它与 **温度** 向量中的一个温度相关联。该向量的长度必须等于 **温度** 向量的长度。向量中的每个元素必须在范围 (0,1] 内。

#### 依赖关系

当 **摩擦模型** 参数设置为 `Temperature-dependent efficiency` 时，会显示此参数。

### **太阳轮-行星架功率阈值** — 功率阈值 `0.001` `W` (默认) | 标量

功率阈值 *pth*，高于该值时全效率生效。低于此值时，双曲正切函数会平滑效率因子。对于无热损失的模型，当没有功率传输时，该函数将效率损失降至零。对于考虑热损失的模型，该函数在静止时的零与功率阈值处由温度-效率查找表提供的值之间平滑效率因子。

#### 依赖关系

当 **摩擦模型** 参数设置为 `Constant efficiency` 或 `Temperature-dependent efficiency` 时，会显示此参数。

### 粘性损失

### **太阳轮-行星架粘性摩擦系数** — 粘性摩擦 `0` `N*m/(rad/s)` (默认)

太阳轮-行星架齿轮运动的粘性摩擦系数 *μS*。

### 热端口

当在 **啮合损失** 设置中将 **摩擦模型** 参数设置为 `Temperature-dependent efficiency` 时，这些设置可见。

### **热质量** — 热质量 `50` `J/K` (默认) | 标量

将组件温度改变一个温度单位所需的热能。热质量越大，组件对温度变化的抵抗越强。

#### 依赖关系

要启用此参数，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

## 所属库

Simscape / Driveline / Gears / Planetary Subcomponents

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

## 描述

由行星架、行星轮和太阳轮组成的行星齿轮组，具有可调齿轮比和摩擦损失

Sun-Planet 齿轮模块表示一组行星架、行星轮和太阳轮。行星轮连接到行星架，并相对于行星架旋转。行星轮和太阳轮以您指定的固定齿轮比共转，并且相对于行星架方向相同。太阳轮-行星轮齿轮和齿圈-行星轮齿轮是行星齿轮组的基本元件。有关模型详细信息，请参见方程。

### 热模型

您可以通过启用可选热端口来对热流和温度变化的影响进行建模。要启用该端口，请将 **摩擦模型** 设置为 `Temperature-dependent efficiency`。

### 方程

**理想齿轮约束和齿轮比**

Sun-Planet 对三个连接的轴施加一个运动学约束和一个几何约束：

rCωC=rSωS+rPωP

行星轮-太阳轮齿轮比为

gPS=rP/rS=NP/NS

其中 *N* 是每个齿轮上的齿数。就这一比率而言，关键运动学约束为：

ωS= –gPSωP+ (1 +gPS)ωC

三个自由度简化为两个独立自由度。齿轮对为 (1, 2) = (*S*, *P*)。

扭矩传递为：

gPSτS+τP–τloss= 0

在理想情况下，没有扭矩损失，即 *τloss* = 0。

**非理想齿轮约束和损失**

在非理想情况下，*τloss* ≠ 0。有关详细信息，请参见带损失的齿轮建模。

### 变量

在仿真前，使用 **变量** 设置来设置模块变量的优先级和初始目标值。有关详细信息，请参见设置模块变量的优先级和初始目标。
