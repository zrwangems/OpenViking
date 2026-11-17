---
type: simulink-block
title: 'Simple Gear with Variable Efficiency'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears'
documentation_page: 'simplegearwithvariableefficiency'
documentation_source_path: 'ref/simplegearwithvariableefficiency.html'
language: zh-CN
chinese_source: worker-translation
---

# Simple Gear with Variable Efficiency

## 端口

### 输入

### **E** — 啮合效率物理信号

与齿轮啮合效率关联的物理信号输入端口。该模块接受范围在 (0,1] 内的效率值。
### 守恒

### **B** — 基座旋转机械

与基座轴关联的机械旋转守恒端口。

### **F** — 从动旋转机械

与从动轴关联的机械旋转守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。热流影响齿轮温度，因此影响动力传输效率。

#### 依赖关系

要启用此端口，请将 **Thermal port** 设置为
`Model`。

## 参数

### 主要

### **Follower (F) to base (B) teeth ratio (NF/NB)** — 齿轮比 `2`（默认）| 正标量

齿轮比。这是从动齿轮齿数与基座齿轮齿数之比，NF/NB。该比值必须为正。

### **Output shaft rotates** — 轴旋转方向 `In opposite direction to input shaft`（默认）| `In same direction as input shaft`

轴之间的相对旋转。这是输出轴相对于输入轴的旋转方向。您可以选择相同或相反的旋转方向。

### 啮合损失

### **Minimum efficiency** — 最小效率 `0.01`（默认）| 范围在 (0,1] 内的正标量

齿轮允许的最小效率值。效率是输出轴与输入轴之间的功率比。物理信号输入保持在低于最小效率或高于 1 的值。该值必须为正。

### **Follower power threshold** — 低于此功率时应用数值平滑 `0.001` W（默认）| 正标量

从动轴功率高于此值时，完整效率因子生效。双曲正切函数在静止时的零与效率设定点之间平滑效率因子。

### 粘性损失

### **Viscous friction coefficients at base (B) and follower (F)** — 流体动力摩擦系数 `[0 0]` `N*m/(rad/s)`（默认）| 正二元素向量

包含基座轴和从动轴上生效的粘性摩擦系数的二元素数组。默认数组对应零粘性损失。

### 热端口

### **Thermal port** — 是否对热效应建模 `Omit`（默认）| `Model`

是否对热效应建模并启用端口 **H** 以实现温度相关性能。

### **Thermal mass** — 热质量 `50` J/K（默认）| 正标量

使组件温度变化一度所需的热能。热质量越大，组件对温度变化的抵抗能力越强。

#### 依赖关系

要启用此参数，请将
**Thermal port** 设置为
`Model`。

### **Initial temperature** — 初始温度 `300` K（默认）| 正标量

仿真开始时组件的温度。初始温度根据您指定的效率向量改变组件效率，影响起始啮合或摩擦损失。

#### 依赖关系

要启用此参数，请将
**Thermal port** 设置为
`Model`。

## 所属库

Simscape / Driveline / Gears

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

具有平行轴旋转和可变啮合效率的齿轮组

Simple Gear with Variable Efficiency 模块表示具有可变啮合效率的简单齿轮系。该齿轮系以指定比率在平行配置的基座轴和从动轴之间传输扭矩。轴旋转可以以相同或相反方向发生。齿轮损失是可选的。它们包括啮合损失和粘性轴承损失。要指定可变啮合效率，该模块包含一个物理信号端口，您可以使用它输入一般时变信号。惯量和柔量效应被忽略。

### 简单齿轮模型

**理想齿轮约束和齿轮比**

Simple Gear 对两个连接的轴施加一个运动学约束：

|  |  |
| --- | --- |
| *r*F*ω*F = *r*B*ωB*. | **(1)** |

从动-基座齿轮比
*g*FB =
*r*F/*r*B
=
*N*F/*N*B。
*N* 是每个齿轮上的齿数。两个自由度缩减为一个独立自由度。

扭矩传递为：

|  |  |
| --- | --- |
| *g*FB*τ*B + *τ*F – *τ*loss = 0, | **(2)** |

在理想情况下 *τ*loss
= 0。

### 非理想齿轮约束和损失

在非理想情况下，*τ*loss
≠ 0。关于非理想齿轮建模的一般考虑，请参见 Model Gears with Losses。

### 热模型

您可以通过启用可选热端口来对热流和温度变化的影响建模。要启用该端口，请将 **Friction model** 设置为 `Temperature-dependent
efficiency`。

### 变量

使用 **Variables** 设置来在仿真前设置模块变量的优先级和初始目标值。有关更多信息，请参见 Set Priority and Initial Target for Block Variables。
