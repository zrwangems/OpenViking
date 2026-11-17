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

### 守恒端口

### **C** — 行星齿轮架旋转机械

与行星齿轮架关联的旋转守恒端口。

### **P** — 行星齿轮旋转机械

与行星齿轮关联的旋转守恒端口。

### **S** — 太阳齿轮旋转机械

与太阳齿轮关联的旋转守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。热流通过改变齿轮温度影响功率传输效率。

#### 依赖关系

要启用此端口，请将 **Friction model** 设置为
`Temperature-dependent efficiency`。

## 参数

### 主要

### **Planet (P) to sun (S) teeth ratio (NP/NS)** — 行星齿轮与太阳齿轮传动比 `2`（默认）| 正标量

行星齿轮半径与太阳齿轮半径之比 *gPS*。

### 啮合损失

### **Friction model** — 摩擦模型 `No meshing losses - Suitable for HIL simulation`（默认）| `Constant efficiency` | `Temperature-dependent efficiency`

模块的摩擦模型：

- `No meshing losses - Suitable for HIL simulation`
  — 齿轮啮合为理想状态。
- `Constant efficiency` — 齿轮副之间的扭矩传递按恒定效率
  *η* 降低，其中 0 < *η* ≤ 1。
- `Temperature-dependent efficiency` — 齿轮副之间的扭矩传递
  由基于温度的查表确定。

### **Ordinary efficiency** — 效率 `0.98`（默认）| 标量 | `0` < *ηSP* ≤ `1`

太阳轮-行星轮齿轮副啮合的扭矩传递效率
*ηSP*。该值必须大于 `0`
且小于或等于 `1`。

#### 依赖关系

当 **Friction
model** 参数设置为 `Constant
efficiency` 时，此参数可见。

### **Temperature** — 温度 `[280, 300, 320]` `K`（默认）| 向量

用于构建一维温度-效率查找表的温度向量。
向量元素必须从左到右递增。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为
`Temperature-dependent efficiency`。

### **Efficiency** — 齿轮效率 `[.95, .9, .85]`（默认）| 数组 | `0` < *ηSP* ≤ `1`

机械效率数组，即从齿圈到行星齿轮的功率流的输出功率与输入功率之比，
*ηRP*。模块使用
这些值构建一维温度-效率查找表。

每个元素是与 **Temperature** 向量中某个温度
对应的效率。
向量的长度必须等于
**Temperature** 向量的长度。向量中的每个元素
必须在 (0,1] 范围内。

#### 依赖关系

当 **Friction
model** 参数设置为
`Temperature-dependent
efficiency` 时，此参数可见。

### **Sun-carrier power threshold** — 功率阈值 `0.001` `W`（默认）| 标量

功率阈值 *pth*，高于该值时
全效率生效。低于该值时，双曲
正切函数对效率因子进行平滑处理。对于无
热损失的模型，当无功率传输时，该函数将效率损失降至零。对于考虑热损失的
模型，该函数在静止时为零与功率阈值处由温度-效率查找表提供的
值之间对效率因子进行平滑处理。

#### 依赖关系

当 **Friction
model** 参数设置为 `Constant
efficiency` 或 `Temperature-dependent
efficiency` 时，此参数可见。

### 粘性损失

### **Sun-carrier viscous friction coefficient** — 粘性摩擦 `0` `N*m/(rad/s)`（默认）

太阳轮-行星架齿轮运动的粘性摩擦系数
*μS*。

### 热端口

当在 **Meshing Losses**
设置中将 **Friction model** 参数设置为
`Temperature-dependent efficiency` 时，这些设置可见。

### **Thermal mass** — 热质量 `50` `J/K`（默认）| 标量

使组件温度变化一个温度单位所需的热能。热质量
越大，组件对温度
变化的抵抗能力越强。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为
`Temperature-dependent
efficiency`。

## 所属库

Simscape / Driveline / Gears / Planetary Subcomponents

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

## 描述

具有可调传动比和摩擦损失的由行星架、行星轮和太阳轮组成的行星齿轮组

Sun-Planet 齿轮模块表示一组行星架、
行星轮和太阳轮。行星轮连接到行星架并相对于行星架旋转。行星轮和太阳轮以您指定的固定传动比共转，并且相对于行星架
方向相同。太阳轮-行星轮和齿圈-行星轮齿轮是
行星齿轮组的基本元件。有关模型详细信息，请参阅方程。

### 热模型

您可以通过启用可选热端口来对热流和温度变化的影响进行建模。要启用
该端口，请将 **Friction model** 设置为 `Temperature-dependent
efficiency`。

### 方程

**理想齿轮约束和传动比**

Sun-Planet 对三个连接轴施加一个运动学约束和一个几何约束：

rCωC=rSωS+rPωP

行星轮-太阳轮传动比为

gPS=rP/rS=NP/NS

其中 *N* 是每个
齿轮上的齿数。根据该传动比，关键运动学约束为：

ωS= –gPSωP+ (1 +gPS)ωC

三个自由度简化为两个独立自由度。齿轮副为 (1, 2) = (*S*, *P*)。

扭矩传递为：

gPSτS+τP–τloss= 0

在理想情况下，没有扭矩损失，
即 *τloss* = 0。

**非理想齿轮约束和损失**

在非理想情况下，*τloss* ≠ 0。有关更多信息，请参阅 Model Gears with Losses。

### 变量

使用 **Variables** 设置在仿真前设置模块变量的优先级和初始目标
值。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。
