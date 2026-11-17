---
type: simulink-block
title: 'Fundamental Friction Clutch'
family: 'clutches'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Clutches / Fundamental Components'
documentation_page: 'fundamentalfrictionclutch'
documentation_source_path: 'ref/fundamentalfrictionclutch.html'
language: zh-CN
chinese_source: worker-translation
---

# Fundamental Friction Clutch

## 端口

### 输入

### **tK** — 动摩擦扭矩，N\*m physical signal

用于动摩擦扭矩的 physical signal 输入端口。

### **t+** — 静摩擦扭矩上限，N\*m physical signal

用于静摩擦扭矩上限的 physical signal 输入端口。

### **t-** — 静摩擦扭矩下限，N\*m physical signal

用于静摩擦扭矩下限的 physical signal 输入端口。

### 输出

### **S** — 离合器滑移速度，rad/sec physical signal

用于离合器滑移速度的 physical signal 输出端口。

### **M** — 离合器状态 physical signal

用于离合器状态的 physical signal 输出端口。

### 守恒

### **B** — 旋转速度，rad/sec mechanical rotational

与主动轴关联的旋转守恒端口。

### **F** — 旋转速度，rad/sec mechanical rotational

与从动轴关联的旋转守恒端口。

### **H** — 热流 thermal

与热流关联的热守恒端口。热端口允许您对模块与所连接网络之间的热流建模。有关详细信息，请参阅 Model Thermal Losses in Driveline Components。

#### 依赖关系

要启用这些设置，将 **Thermal Port** 设置为 `Model`。

## 参数

### **Directionality** — 允许的板间滑移方向 `Bidirectional` (默认) | `Unidirectional`

离合器允许其摩擦片之间的滑移方向。双向离合器允许正和负滑移速度。单向离合器仅允许正滑移速度。

单向离合器等效于与单向离合器并联的摩擦离合器，该单向离合器仅在滑移速度变为正时分离。要对在负方向滑移的单向离合器建模，请反转主动和从动端口连接。

### **Thermal port** — 热模型 `Omit` (默认) | `Model`

用于热流和温度变化的模型：

- `Omit` — 忽略热动态。
- `Model` — 包括热动态。

### **Thermal mass** — 对温度变化的阻力 `50` `kJ/K` (默认) | scalar

使组件温度变化一个热单位所需的热能。热质量越大，组件对温度变化的阻力越大。

#### 依赖关系

要启用此参数，将 **Thermal Port** 设置为 `Model`。

### **Clutch velocity tolerance** — 滑移速度阈值 `0.001` `rad/s` (默认) | scalar

离合器可锁止时的滑移速度下限。如果在降至离合器速度容差以下后，动摩擦扭矩非零且传递扭矩位于静摩擦扭矩限值之间，则离合器锁止。

### **Initial state** — 初始离合器状态 `Unlocked` (默认) | `Locked`

仿真开始时的离合器状态。离合器可以处于两种状态之一：locked 和 unlocked。锁止的离合器约束主动轴和从动轴以相同速度旋转，即作为一个整体。未锁止的离合器允许两个轴以不同速度旋转，从而导致离合器片之间滑移。

以未锁止状态开始仿真的离合器没有运动方向。出于此原因，在检查未锁止状态有效后，模块根据传动系动态自动确定适当的运动方向。根据运动方向，离合器随后转换为 unlocked-reverse 或 unlocked-forward 状态。

## 所属库

Simscape / Driveline / Clutches / Fundamental Components

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

## 描述

以动摩擦扭矩和静摩擦限值扭矩作为输入的摩擦离合器

Fundamental Friction Clutch 模块表示一种通过摩擦传递旋转动力的机构。离合器包含两组摩擦片，每组刚性连接至一个传动轴，接触时接合。一旦接触，摩擦片会受到摩擦扭矩，使动力能够在传动轴之间流动。

离合器可以是双向或单向的。双向离合器可以在正方向和负方向滑移。单向离合器只能在正方向滑移。如果从动轴比主动轴旋转得快，则滑移方向为正；如果旋转得慢，则为负。模块将滑移速度定义为差值

ω=ωF−ωB,

其中：

- *ω* 是滑移速度。
- *ωF* 是从动传动轴的角速度。
- *ωB* 是主动传动轴的角速度。

### 离合器状态

离合器可以处于三种状态：

- Locked — 实际离合器状态，其中摩擦片作为一个整体旋转。锁止的离合器具有一个旋转自由度。它不因摩擦而经历功率损失。
- Unlocked — 实际离合器状态，其中摩擦片彼此滑移。未锁止的离合器具有两个旋转自由度。它经历的功率损失等于滑移速度与动摩擦扭矩的乘积。
- Wait — 虚拟离合器状态，在测试锁止和未锁止时保持前一状态的运动。离合器的自由度和功率损失取决于前一离合器状态。

示意图显示了离合器锁止和未锁止的条件。通常，如果离合器传递的扭矩位于其静摩擦扭矩限值之间，并且滑移速度的幅值小于其速度容差，则离合器锁止。否则离合器未锁止。

在示意图中：

- *τ* 是离合器片之间传递的扭矩。
- *τS*-
  和
  *τ*S+
  是静摩擦扭矩限值。
- *τK* 是离合器片之间的动摩擦扭矩。
- *ωTol* 是离合器的滑移速度容差。
- *ω* 是离合器片之间的滑移速度。

该模块通过 physical signal 端口 **M** 使用值 -1、0 和 +1 标识离合器状态。下表总结了状态与输出值之间的对应关系。

| 状态 | 值 |
| --- | --- |
| Unlocked Forward or Wait Forward | +1 |
| Unlocked Reverse or Wait Reverse | -1 |
| Locked or Unlocked Initial State | 0 |

### 状态转换

在仿真开始时，离合器处于两种状态之一 — locked 或 initial unlocked。initial unlocked 状态的独特之处在于它没有运动方向。离合器保持此状态，直到离合器滑移速度变为非零。然后，根据示意图，离合器转换到适当状态，unlocked reverse 或 unlocked forward。

在仿真期间，离合器测试各种动态条件，以确定适当的状态转换（如果有）。示意图显示可能的转换、其动态条件以及结果状态。如果离合器是单向的，则示意图简化为右半部分。该图显示单向离合器的转换。

该图显示双向离合器的转换。

### 热模型

启用热端口后，Fundamental Friction Clutch 模块仿真热流和相对于耗散功率量产生的热量的影响。要仿真热流，必须将该端口连接到另一个已启用热端口的模块。许多 Simscape™ Driveline™ 模块具有热建模选项。当支持热建模的参数可用时，它显示为向量，其长度对应于 **Temperature** 的长度。有关详细信息，请参阅 Model Thermal Losses in Driveline Components。

要启用热端口，将 **Thermal Port** 设置为 `Model`。启用热端口还会启用以下设置：

- **参数** > **Thermal Mass**
- **变量** > **Temperature**

### 变量

在仿真前，使用 **变量** 设置为模块变量设置优先级和初始目标值。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

**依赖关系**

要启用这些设置，将 **Thermal port** 设置为 `Model`。
