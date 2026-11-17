---
type: simulink-block
title: 'Planet-Planet'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears / Planetary Subcomponents'
documentation_page: 'planetplanet'
documentation_source_path: 'ref/planetplanet.html'
language: zh-CN
chinese_source: worker-translation
---

# Planet-Planet

## 端口

### 守恒端口

### **C** — 行星齿轮架旋转机械

与行星齿轮架相关联的旋转机械守恒端口。

### **Po** — 外行星齿轮旋转机械

与外行星齿轮相关联的旋转机械守恒端口。

### **Pi** — 内行星齿轮旋转机械

与内行星齿轮相关联的旋转机械守恒端口。

### **H** — 热流热

与热流相关联的热守恒端口。热流通过改变齿轮温度影响功率传输效率。

#### 依赖关系

要启用此端口，请将 **Friction model** 设置为
`Temperature-dependent efficiency`。

## 参数

### 主要

### **Outer planet (Po) to inner planet (Pi) teeth ratio (NPo/NPi)** — 外行星齿轮与内行星齿轮旋转比 `2`（默认）| 正标量

外行星齿轮与内行星齿轮旋转之比 *goi*，定义为外行星齿轮齿数除以内行星齿轮齿数。该齿轮比必须严格为正。

### 啮合损耗

### **Friction model** — 摩擦模型 `No meshing losses - Suitable for HIL simulation`（默认）| `Constant efficiency` | `Temperature-dependent efficiency`

模块的摩擦模型：

- `No meshing losses - Suitable for HIL simulation`
  — 齿轮啮合为理想情况。
- `Constant efficiency` — 齿轮副之间的扭矩传递按恒定效率
  *η* 降低，使得 0 < *η* ≤ 1。
- `Temperature-dependent efficiency` — 齿轮副之间的扭矩传递由基于温度的查表定义。

### **Ordinary efficiency** — 扭矩传递效率 `0.98`（默认）| 标量

外行星齿轮与内行星齿轮副啮合的扭矩传递效率
*ηPP*。该值必须在范围
(0,1] 内。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Constant efficiency`。

### **Temperature** — 温度 `[280, 300, 320]` `K`（默认）| 向量

用于构造一维温度-效率查找表的温度向量。
向量元素必须从左到右递增。

#### 依赖关系

要启用此参数，请将 **Friction model** 设置为
`Temperature-dependent efficiency`。

### **Efficiency** — 齿轮效率 `[.95, .9, .85]`（默认）| 向量

描述从外行星齿轮到内行星齿轮功率流的输出与输入功率比向量
*ηPP*。模块使用这些值构造一维温度-效率查找表。

每个元素是与 **Temperature** 向量中某个温度对应的效率。
向量长度必须等于
**Temperature** 向量的长度。向量中每个元素
必须在范围 (0,1] 内。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Temperature-dependent
efficiency`。

### **Inner planet-carrier power threshold** — 内行星-行星架齿轮耦合的最小效率功率阈值 `0.001` `W`（默认）| 标量

功率阈值 *pth*，高于该值时全效率生效。低于该值时，双曲正切函数对效率因子进行平滑处理。

当您将 **Friction model** 设置为
`Constant efficiency` 时，模块在无功率传输时将效率损耗降为零。当您将
**Friction model** 设置为
`Temperature-dependent efficiency` 时，模块在功率阈值处对效率因子进行平滑处理，使其在静止时为零与温度-效率查找表提供的值之间过渡。

#### 依赖关系

要启用此参数，请将 **Friction model**
设置为 `Constant efficiency` 或
`Temperature-dependent
efficiency`。

### 粘性损耗

### **Inner planet-carrier viscous friction coefficient** — 齿轮粘性摩擦 `0` `N*m/(rad/s)`（默认）| 标量

内行星-行星架齿轮运动的粘性摩擦系数
*μPi*。

### 热端口

要启用此参数，请将 **Friction model** 设置为
`Temperature-dependent efficiency`。

### **Thermal mass** — 热质量 `50` `J/K`（默认）| 标量

使组件温度变化一个温度单位所需的热能。热质量越大，组件对温度变化的抵抗能力越强。

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

由行星架、内行星轮和外行星轮组成的行星齿轮组，具有可调齿轮比和摩擦损耗

Planet-Planet 齿轮模块表示一个行星架和两对内外行星齿轮副。两个行星齿轮均连接到行星架并相对于行星架旋转。行星齿轮以您指定的固定齿轮比同向旋转。有关模型详细信息，请参见方程。

### 热模型

您可以通过启用可选热端口来建模热流和温度变化的影响。要启用该端口，请将 **Friction model** 设置为 `Temperature-dependent
efficiency`。

### 方程

**理想齿轮约束和齿轮比**

Planet-Planet 模块对三个连接轴施加一个运动学约束和一个几何约束：

rCωC=rPoωPo+rPiωPi

rC=rPo+rPi

外行星齿轮与内行星齿轮的齿轮比为

goi=rPo/rPi=NPo/NPi，

其中 *N* 是每个齿轮的齿数。用该比率表示，关键运动学约束为

(1 +goi)ωC=ωPi+goiωPo。

三个自由度缩减为两个独立自由度。齿轮副为 (1, 2) = (*Pi*,*Po*)。

扭矩传递为

goiτPi+τPo–τloss= 0。

在无扭矩损耗的理想情况下，*τloss* = 0。

**非理想齿轮约束和损耗**

在非理想情况下，*τloss* ≠ 0。有关更多信息，请参见 Model Gears with Losses。

### 变量

使用 **Variables** 设置可在仿真前设置模块变量的优先级和初始目标值。有关更多信息，请参见 Set Priority and Initial Target for Block Variables。

### 假设和限制

- 假设齿轮惯量可忽略不计。
- 齿轮被视为刚性组件。
- 库仑摩擦会减慢仿真速度。有关更多信息，请参见 Adjust Model Fidelity。
