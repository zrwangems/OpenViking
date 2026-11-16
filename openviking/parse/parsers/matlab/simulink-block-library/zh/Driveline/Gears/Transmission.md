---
type: simulink-block
title: 'Transmission'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Gears'
documentation_page: 'transmission'
documentation_source_path: 'ref/transmission.html'
language: zh-CN
chinese_source: worker-translation
---

# Transmission

## 端口

### 输入

### **G** — 挡位选择物理信号

与挡位选择关联的物理输入信号。输入中 `0` 表示空挡，`-1` 表示倒挡，而 **Forward gear ratios** 参数中的值表示前进挡。该模块将信号饱和到 `-1` 至 **Forward gear ratios** 参数长度之间。

### 守恒

### **B** — 基座接口机械旋转

与基座接口关联的机械旋转守恒端口。

### **F** — 从动接口机械旋转

与从动接口关联的机械旋转守恒端口。

### **H** — 热流热

与热流关联的热守恒端口。

#### 依赖项

要启用此端口，请将 **Thermal port** 设置为 `Model`。

## 参数

### 齿轮

### **Forward gear ratios** — Transmission 前进挡传动比 `[2.3, 1.6, 1.2, 1, .8, .6]`（默认）| 正数向量

有序的变速器传动比向量。该模块使用向量中每个元素的位置将该元素分配给给定输入信号。您可以参数化任意数量的传动比。

### **Reverse gear ratio** — Transmission 倒挡传动比 `-3`（默认）| 负标量

倒挡传动比。

#### 依赖项

要启用此参数，请将 **Friction model** 设置为 `Gear-dependent efficiency`。

### **Friction model** — 摩擦模型 `No meshing losses - Suitable for HIL simulation`（默认）| `Constant efficiency` | `Gear-dependent efficiency`

该模块的摩擦模型：

- `No meshing losses - Suitable for HIL simulation` — 齿轮啮合理想。
- `Constant efficiency` — 该模块根据 **Efficiency** 参数降低所有齿轮副之间的扭矩传递。
- `Gear-dependent efficiency` — 该模块根据 **Efficiency vector** 参数定义齿轮副之间的扭矩传递。

### **Efficiency** — 齿轮效率 `0.95`（默认）| 正标量

该模块应用于所有传动比的效率。

#### 依赖项

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency`。

### **Efficiency vector** — 前进挡相关效率 `[.95, .95, .95, .95, .95, .95]`（默认）| 正元素向量

挡位相关效率，其中每个元素对应于 **Forward gear ratios** 参数中的一个传动比。

#### 依赖项

要启用此参数，请将 **Friction model** 设置为 `Gear-dependent efficiency`。

### **Reverse efficiency** — 倒挡效率 `0.90`（默认）| 正标量

该模块应用于倒挡的效率。

### **Follower power threshold** — 模块应用完全效率损失的功率点 `0.001` `W`（默认）| 正标量

该模块向从动件应用完全效率时的绝对功率。

#### 依赖项

要启用此参数，请将 **Friction model** 设置为 `Constant efficiency` 或 `Gear-dependent efficiency`。

### **Stiffness at base (B)** — 基座弹簧刚度系数 `3e5` `N*m/rad`（默认）| 正标量

在基座处测得的变速器角柔度的倒数。

### **Damping at base (B)** — 基座阻尼系数 `3e4` `N*m*s/rad`（默认）| 正标量

在基座处测得的变速器角柔度阻尼的倒数。

### **Initial input torque at base (B)** — 基座启动扭矩 `0` `N*m`（默认）| 标量

仿真开始时施加在基座轴上的扭矩。

### **Viscous friction coefficients at base (B) and follower (F)** — 基座和从动件粘性摩擦向量 `[0, 0]` `N*m/(rad/s)`（默认）| 非负元素向量

分别施加在基座轴和从动轴上的粘性阻尼系数向量。

### 离合器

### **Kinetic friction torque** — 动摩擦扭矩阈值 `1000` `N*m`（默认）| 非负标量

维持离合器片之间相对运动所需的最小扭矩阈值。

### **Static friction torque** — 静摩擦扭矩阈值 `2000` `N*m`（默认）| 正标量

导致离合器片之间相对运动所需的最小扭矩阈值。

### **Shift model** — 包含有限换挡时间的选项 `Instantaneous`（默认）| `Finite shift time`

该模块是瞬时完成换挡，还是在挡位之间过渡到空挡并持续有限时间。

### **Shift time** — 传动比之间处于空挡的时间 `100` `ms`（默认）| 正标量

完成换挡的时间。在此期间变速器保持空挡。

#### 依赖项

要启用此参数，请将 **Shift model** 设置为 `Finite shift time`

### **Clutch velocity tolerance** — 运动边界条件 `0.001` `rad/s`（默认）| 非负标量

离合器最小角速度。

### **Initial State** — 仿真开始时离合器状态 `Unlocked`（默认）| `Locked`

以离合器未锁定或锁定状态开始仿真的选项。

### 热端口

### **Thermal port** — 公开热端口的选项 `Omit`（默认）| `Model`

是否公开热端口及相关参数。

### **Thermal mass** — 热质量 `100` `kJ/K`（默认）| 正标量

使组件温度变化一个温度单位所需的热能。热质量越大，组件越不易发生温度变化。

#### 依赖项

要启用此参数，请将 **Thermal port** 设置为 `Model`。

### **Initial temperature** — 仿真开始时的温度 `300` `K`（默认）| 正标量

对热流和温度变化建模时的初始变速器温度。

#### 依赖项

要启用此参数，请将 **Thermal port** 设置为 `Model`。

## 所属库

Simscape / Driveline / Gears

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022a 中引入**

## 描述

用于系统级传动系建模的抽象变速器

Transmission 模块表示用于系统级传动系模型的抽象变速器。该模块接受传动比命令作为物理信号输入到端口 **G**，其中 `0` 表示空挡，`-1` 表示倒挡，而 **Forward gear ratios** 参数中的值表示前进挡。此向量的长度对应于前进挡数量。该模块将输入值舍入为整数。该变速器是非顺序式的，允许您在任意两个传动比之间切换，而无需在中间传动比处停止。若要使该模块表现得像顺序式变速器，您必须按顺序指定每个传动比。

Transmission 模块是两个模块的复合体。该模块使用 Variable Ratio Transmission 模块的子组件实现来仿真变速器传动比动态，并使用 Logic-Controlled Clutch 模块仿真抽象离合器动态。要了解更多信息，请参阅 About Composite Components。

### 热模型

您可以通过启用可选热端口来对热流和温度变化的影响进行建模。要启用该端口，请将 **Thermal port** 设置为 `Model`。
