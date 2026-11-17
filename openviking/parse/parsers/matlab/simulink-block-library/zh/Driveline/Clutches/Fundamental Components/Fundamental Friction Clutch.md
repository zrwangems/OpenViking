---
type: simulink-block
title: 'Fundamental Friction Clutch'
family: 'sdl'
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
```yaml
ports:
- name: tK
  summary: 动摩擦力矩，N\*m 物理信号
  direction: input
- name: t+
  summary: 静摩擦力矩上限，N\*m 物理信号
  direction: input
- name: t-
  summary: 静摩擦力矩下限，N\*m 物理信号
  direction: input
- name: S
  summary: 离合器滑移速度，rad/sec 物理信号
  direction: output
- name: M
  summary: 离合器状态 物理信号
  direction: output
- name: B
  summary: 旋转速度，rad/sec 机械旋转
  direction: output
- name: F
  summary: 旋转速度，rad/sec 机械旋转
  direction: output
- name: H
  summary: 热流 热
  direction: output
```

### 输入

### **tK** — 动摩擦力矩，N\*m 物理信号

动摩擦力矩的物理信号输入端口。

### **t+** — 静摩擦力矩上限，N\*m 物理信号

静摩擦力矩上限的物理信号输入端口。

### **t-** — 静摩擦力矩下限，N\*m 物理信号

静摩擦力矩下限的物理信号输入端口。
### 输出

### **S** — 离合器滑移速度，rad/sec 物理信号

离合器滑移速度的物理信号输出端口。

### **M** — 离合器状态 物理信号

离合器状态的物理信号输出端口。
### 守恒

### **B** — 旋转速度，rad/sec 机械旋转

与主动轴关联的旋转守恒端口。

### **F** — 旋转速度，rad/sec 机械旋转

与从动轴关联的旋转守恒端口。

### **H** — 热流 热

与热流关联的热守恒端口。热端口允许您对模块与所连接网络之间的热流进行建模。有关详细信息，请参阅 Model Thermal Losses in Driveline Components。

#### 依赖关系

要启用这些设置，请将 **Thermal Port** 设置为 `Model`。
## 参数
```yaml
parameters:
- name: Directionality
  summary: 允许的板间滑移方向 Bidirectional（默认）| Unidirectional
  group: ''
- name: Thermal port
  summary: 热模型 Omit（默认）| Model
  group: ''
- name: Thermal mass
  summary: 对温度变化的阻力 50 kJ/K（默认）| 标量
  group: ''
- name: Clutch velocity tolerance
  summary: 滑移速度阈值 0.001 rad/s（默认）| 标量
  group: ''
- name: Initial state
  summary: 初始离合器状态 Unlocked（默认）| Locked
  group: ''
```

### **Directionality** — 允许的板间滑移方向 `Bidirectional`（默认）| `Unidirectional`

离合器允许其板间发生的滑移方向。双向离合器允许正滑移速度和负滑移速度。单向离合器仅允许正滑移速度。

单向离合器等效于一个摩擦离合器与一个单向离合器并联，后者仅在滑移速度变为正值时脱开。要对负方向滑移的单向离合器进行建模，请反转主动端口和从动端口的连接。

### **Thermal port** — 热模型 `Omit`（默认）| `Model`

热流和温度变化的模型：

- `Omit` — 忽略热动态。
- `Model` — 包含热动态。

### **Thermal mass** — 对温度变化的阻力 `50` `kJ/K`（默认）| 标量

使组件温度变化一个热单位所需的热能。热质量越大，组件对温度变化的阻力越大。

#### 依赖关系

要启用此参数，请将 **Thermal Port** 设置为 `Model`。

### **Clutch velocity tolerance** — 滑移速度阈值 `0.001` `rad/s`（默认）| 标量

低于该滑移速度时离合器可以锁止。如果在降至离合器速度容差以下后，动摩擦力矩非零且传递力矩处于静摩擦力矩限值之间，则离合器锁止。

### **Initial state** — 初始离合器状态 `Unlocked`（默认）| `Locked`

仿真开始时的离合器状态。离合器可以处于两种状态之一：锁止和未锁止。锁止的离合器约束主动轴和从动轴以相同速度旋转，即作为一个整体旋转。未锁止的离合器允许两个轴以不同速度旋转，从而导致离合器板之间发生滑移。

以未锁止状态开始仿真的离合器缺少运动方向。因此，在检查未锁止状态有效后，模块会根据传动系统动态自动确定适当的运动方向。然后，根据运动方向，离合器转换为未锁止反向或未锁止正向状态。
## 所属库

Simscape / Driveline / Clutches / Fundamental Components

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

## 描述

以动摩擦和静摩擦极限转矩为输入的摩擦离合器

基本摩擦离合器模块表示一种通过摩擦传递旋转动力的机构。该离合器包含两组摩擦片，每组摩擦片刚性连接到一个驱动轴上，通过接触实现接合。一旦接触，摩擦片会受到摩擦力矩的作用，使动力能够在驱动轴之间传递。

该离合器可以是双向的或单向的。双向离合器可以在正方向和负方向上打滑。单向离合器只能在正方向上打滑。如果从动轴转速快于主动轴，则打滑方向为正；如果转速较慢，则为负。该模块将打滑速度定义为差值

ω=ωF−ωB，

其中：

- *ω* 是打滑速度。
- *ωF* 是从动驱动轴的角速度。
- *ωB* 是主动驱动轴的角速度。

### 离合器状态

离合器可以处于三种状态：

- 锁定 — 实际离合器状态，摩擦片作为一个整体旋转。锁定的离合器具有一个旋转自由度。它不因摩擦而产生功率损耗。
- 解锁 — 实际离合器状态，摩擦片彼此之间发生打滑。解锁的离合器具有两个旋转自由度。它产生的功率损耗等于打滑速度与动摩擦力矩的乘积。
- 等待 — 虚拟离合器状态，在检测锁定和解锁的同时保持前一状态的运动。离合器的自由度和功率损耗取决于前一离合器状态。

示意图显示了离合器锁定和解锁的条件。如果离合器传递的转矩位于其静摩擦转矩极限之间，且打滑速度的大小小于其速度容差，则离合器通常处于锁定状态。否则离合器解锁。

在示意图中：

- *τ* 是离合器摩擦片之间传递的转矩。
- *τS*- 和 *τ*S+ 是静摩擦转矩极限。
- *τK* 是离合器摩擦片之间的动摩擦转矩。
- *ωTol* 是离合器的打滑速度容差。
- *ω* 是离合器摩擦片之间的打滑速度。

该模块通过物理信号端口 **M** 使用值 -1、0 和 +1 来标识离合器状态。下表总结了状态与输出值之间的对应关系。

| 状态 | 值 |
| --- | --- |
| 正向解锁或正向等待 | +1 |
| 反向解锁或反向等待 | -1 |
| 锁定或解锁初始状态 | 0 |

### 状态转换

在仿真开始时，离合器处于两种状态之一——锁定或初始解锁。初始解锁状态的独特之处在于它没有运动方向。离合器保持在此状态，直到离合器打滑速度变为非零。然后离合器根据示意图转换到适当的状态，即反向解锁或正向解锁。

在仿真过程中，离合器检测各种动态条件以确定适当的状​​态转换（如果有）。示意图显示了可能的转换、其动态条件以及结果状态。如果离合器是单向的，则示意图简化为右半部分。该图显示单向离合器的转换。

该图显示双向离合器的转换。

### 热模型

当您启用热端口时，基础摩擦离合器模块会模拟热流以及相对于耗散功率所产生的热量的影响。要模拟热流，您必须将该端口连接到另一个启用了热端口的模块。许多 Simscape™ Driveline™ 模块都具有热建模选项。当支持热建模的参数可用时，它会显示为一个向量，其长度对应于 **Temperature** 的长度。有关详细信息，请参阅 Model Thermal Losses in Driveline Components。

要启用热端口，请将 **Thermal Port** 设置为 `Model`。启用热端口还会启用以下设置：

- **Parameters** > **Thermal Mass**
- **Variables** > **Temperature**

### 变量

使用 **Variables** 设置可在仿真前设置模块变量的优先级和初始目标值。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

**依赖关系**

要启用这些设置，请将 **Thermal port** 设置为 `Model`。
