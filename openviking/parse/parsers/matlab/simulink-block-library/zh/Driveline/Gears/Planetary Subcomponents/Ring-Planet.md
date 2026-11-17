---
type: simulink-block
title: 'Ring-Planet'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears / Planetary Subcomponents'
documentation_page: 'ringplanet'
documentation_source_path: 'ref/ringplanet.html'
language: zh-CN
chinese_source: worker-translation
---

# Ring-Planet

## 端口

### 守恒端口

### **C** — 行星齿轮架旋转机械

与行星齿轮架关联的旋转机械守恒端口。

### **R** — 齿圈旋转机械

与齿圈关联的旋转机械守恒端口。

### **P** — 行星齿轮旋转机械

与行星齿轮关联的旋转机械守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。热流通过改变齿轮温度影响功率传输效率。

#### 依赖关系

要启用此端口，请将 **Friction model** 设置为
`Temperature-dependent efficiency`。

## 参数

### 主要

### **Ring (R) to planet (P) teeth ratio (NR/NP)** — 齿圈与行星齿轮旋转比 `2`（默认）| 大于 1 的标量

齿圈与行星齿轮旋转的比值 *gRP*，定义为齿圈齿数除以行星齿轮齿数。此齿轮比必须严格大于 1。

### 啮合损失

### **Friction model** — 摩擦模型 `No meshing losses - Suitable for HIL simulation`（默认）| `Constant efficiency` | `Temperature-dependent efficiency`

模块的摩擦模型：

- `No meshing losses - Suitable for HIL simulation`
  — 齿轮啮合为理想状态。
- `Constant efficiency` — 齿轮对之间的扭矩传递按恒定效率
  *η* 降低，其中 0 < *η* ≤ 1。
- `Temperature-dependent efficiency` — 齿轮对之间的扭矩传递由基于温度的表查找定义。

### **Ordinary efficiency** — 扭矩传递效率 `0.98`（默认）| 标量

外行星齿轮和内行星齿轮对啮合的扭矩传递效率
*ηRP*。此值必须在范围
(0,1] 内。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Constant efficiency`。

### **Temperature** — 温度 `[280, 300, 320]` `K`（默认）| 向量

用于构建一维温度-效率查找表的温度向量。
向量元素必须从左到右递增。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为
`Temperature-dependent efficiency`。

### **Efficiency** — 齿轮效率 `[.95, .9, .85]`（默认）| 向量

描述从齿圈到行星齿轮功率流的输出与输入功率比向量
*ηRP*。模块使用
这些值构建一维温度-效率查找表。

每个元素是与 **Temperature** 向量中某个温度对应的效率。向量长度
必须等于 **Temperature**
向量的长度。向量中每个元素必须在范围 (0,1] 内。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Temperature-dependent
efficiency`。

### **Planet-carrier power threshold** — 行星-行星架齿轮耦合的最小效率功率阈值 `0.001` `W`（默认）| 标量

功率阈值 *pth*，高于此值时全效率生效。低于此值时，双曲正切函数对效率因子进行平滑处理。

当您将 **Friction model** 设置为
`Constant efficiency` 时，模块在无功率传输时将效率损失降至零。当您将
**Friction model** 设置为
`Temperature-dependent efficiency` 时，模块在功率阈值处对静止时为零与温度-效率查找表提供的值之间的效率因子进行平滑处理。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Constant efficiency` 或
`Temperature-dependent
efficiency`。

### 粘性损失

### **Planet-carrier viscous friction coefficient** — 齿轮粘性摩擦 `0` `N*m/(rad/s)`（默认）| 标量

行星-行星架齿轮运动的粘性摩擦系数
*μP*。

### 热端口

要启用此参数，请将 **Friction model** 设置为
`Temperature-dependent efficiency`。

### **Thermal mass** — 热质量 `50` `J/K`（默认）| 标量

将组件温度改变一个温度单位所需的热能。热质量越大，组件对温度变化的抵抗能力越强。

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

具有可调齿轮比和摩擦损失的行星架、行星齿轮和齿圈的行星齿轮组

Ring-Planet 模块表示一个行星架、一个齿圈和一组行星齿轮。行星齿轮连接到行星架并相对于行星架旋转。行星齿轮和齿圈以您指定的固定齿轮比同向旋转。齿圈-行星齿轮和太阳轮-行星齿轮是行星齿轮组的基本元件。有关模型详细信息，请参阅方程。

### 热模型

您可以通过启用可选热端口来建模热流和温度变化的影响。要启用
该端口，请将 **Friction model** 设置为 `Temperature-dependent
efficiency`。

### 方程

**理想齿轮约束和齿轮比**

Ring-Planet 模块对三个连接轴施加一个运动学约束和一个几何约束：

rRωR=rCωC+rPωP

rR=rC+rP

齿圈-行星齿轮比为

gRP=rR/rP=NR/NP，

其中 *N* 是每个齿轮上的齿数。根据此比值，关键运动学约束为

gRPωR=ωP+ (gRP– 1)ωC。

三个自由度简化为两个独立自由度。齿轮对为 (1, 2) = (*P*, *R*)。

**警告**

齿圈-行星齿轮比 *gRP*
必须严格大于 1。

扭矩传递为：

gRPτP+τR–τloss= 0。

在无扭矩损失的理想情况下，*τloss* = 0。

**非理想齿轮约束和损失**

在非理想情况下，*τloss* ≠ 0。有关更多信息，请参阅 Model Gears with Losses。

### 变量

使用 **Variables** 设置可在仿真前设置模块变量的优先级和初始目标
值。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。

### 假设和限制

- 假设齿轮惯量可忽略不计。
- 齿轮被视为刚性组件。
- 库仑摩擦会减慢仿真速度。有关更多信息，请参阅 Adjust Model Fidelity。
