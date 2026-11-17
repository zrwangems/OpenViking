---
type: simulink-block
title: 'Resolver'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sensors & Transducers'
documentation_page: 'resolver'
documentation_source_path: 'ref/resolver.html'
language: zh-CN
chinese_source: worker-translation
---

# Resolver

## 端口

### 守恒端口

### **p1** — 初级绕组正极端子电气

与初级绕组正极端子关联的电气守恒端口。

### **p2** — 初级绕组负极端子电气

与初级绕组负极端子关联的电气守恒端口。

### **R** — 旋转变压器转子机械旋转

连接到转子的机械旋转守恒端口。

### **C** — 旋转变压器壳体机械旋转

连接到旋转变压器壳体的机械旋转守恒端口。

### **x1** — 次级绕组 *x* 正极端子电气

与次级绕组 *x* 正极端子关联的电气守恒端口。

### **x2** — 次级绕组 *x* 负极端子电气

与次级绕组 *x* 负极端子关联的电气守恒端口。

### **y1** — 次级绕组 *y* 正极端子电气

与次级绕组 *y* 正极端子关联的电气守恒端口。

### **y2** — 次级绕组 *y* 负极端子电气

与次级绕组 *y* 负极端子关联的电气守恒端口。

## 参数

### **Parameterization** — 旋转变压器参数化 `Specify transformation ratio and omit dynamics`（默认）| `Specify transformation ratio and measured impedances` | `Specify equation parameters directly`

选择以下方法之一进行模块参数化：

- `Specify transformation ratio and omit dynamics` — 仅提供变压比、极对数和初始转子角的值。此模型忽略变压器电感项，仅在传感器由正弦波驱动时有效。方程基于两个理想变压器的叠加，两者的耦合系数均取决于转子角。有关详细信息，请参阅忽略动态时的方程。
- `Specify transformation ratio and measured impedances` — 提供额外值以确定变压器电感项，从而对电压幅值损失和相位差进行建模。此模型对任何输入波形均有效。方程基于两个互感器的叠加，两者的耦合系数均取决于转子角。有关详细信息，请参阅包含动态时的方程。
- `Specify equation parameters directly` — 对动态进行建模，但提供转子和定子电感以及峰值耦合系数的值，而非变压比和测量阻抗。有关详细信息，请参阅包含动态时的方程。此模型对任何输入波形均有效。

### **Transformation ratio** — 峰值输出电压与输入电压之比 `0.5`（默认）| 正数

假设由于电阻和电感导致的次级电压降可忽略不计时，峰值输出电压与峰值输入电压之比。

#### 依赖关系

要启用此参数，请将 **Parameterization** 参数设置为 `Specify transformation ratio and omit dynamics` 或 `Specify transformation ratio and measured impedances`。如果为 **Parameterization** 参数选择 `Specify transformation ratio and measured impedances`，则变压比会考虑由初级绕组电阻导致的电压降。

### **Rotor resistance** — 初级电阻 `70` `Ohm`（默认）| 正数

转子欧姆电阻。此电阻也称为初级电阻。

#### 依赖关系

要启用此参数，请将 **Parameterization** 参数设置为 `Specify transformation ratio and measured impedances` 或 `Specify equation parameters directly`。

### **Stator resistance** — 次级电阻 `180` `Ohm`（默认）| 正数

定子欧姆电阻。此电阻也称为次级电阻。假设两个次级绕组具有相同的电阻。

#### 依赖关系

要启用此参数，请将 **Parameterization** 参数设置为 `Specify transformation ratio and measured impedances` 或 `Specify equation parameters directly`。

### **Rotor reactance** — 初级电抗 `100` `Ohm`（默认）| 正数

次级绕组开路时的转子电抗。此电抗也称为初级电抗。

#### 依赖关系

要启用此参数，请将 **Parameterization** 参数设置为 `Specify transformation ratio and measured impedances`。

### **Stator reactance** — 次级电抗 `300` `Ohm`（默认）| 正数

初级绕组开路时的定子电抗。此电抗也称为次级电抗。

#### 依赖关系

要启用此参数，请将 **Parameterization** 参数设置为 `Specify transformation ratio and measured impedances`。

### **Frequency at which reactances and transformation ratio are specified** — 正弦源频率 `10` `kHz`（默认）| 正数

测量电抗时所用正弦源的频率。

#### 依赖关系

要启用此参数，请将 **Parameterization** 参数设置为 `Specify transformation ratio and measured impedances`。

### **Rotor inductance** — 初级电抗 `0.0016` `H`（默认）| 正数

转子或初级电感，*L*p。

#### 依赖关系

要启用此参数，请将 **Parameterization** 参数设置为 `Specify equation parameters directly`。

### **Stator inductance** — 次级电抗 `0.0048` `H`（默认）| 正数

定子或次级电感，*L*s。

#### 依赖关系

要启用此参数，请将 **Parameterization** 参数设置为 `Specify equation parameters directly`。

### **Peak coefficient of coupling** — 最大耦合系数 `0.35`（默认）| 介于零和一之间（不含端点）的数

初级绕组与次级绕组之间的峰值耦合系数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 参数设置为 `Specify equation parameters directly`。

### **Number of pole pairs** — 转子极对数 `1`（默认）| 正数

转子上的极对数。

## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

测量旋转角度的旋转变压器

Resolver 模块对通用旋转变压器进行建模，它通过电磁耦合测量信号的电气相位角。旋转变压器由一个旋转变压器组成，它将施加到初级绕组的交流电压耦合到两个次级绕组。这些次级绕组在物理上彼此成 90 度方向排列。随着转子角的变化，初级绕组与两个次级绕组之间的相对耦合也会变化。在 Resolver 模块模型中，第一个次级绕组的排列方式使得当转子处于零度时发生峰值耦合，因此第二个次级绕组在转子处于零度时具有最小耦合。

在不失一般性的前提下，假设初级与转子电路之间的变压器为理想变压器，变比为 1:1。这导致转子电流和电压等同于初级电流和电压。

定义模块方程有两种选项：

- 通过忽略变压器电感项来省略动态。此模型仅在传感器由正弦波驱动时有效，因为初级侧的任何直流分量都会传递到输出侧。
- 包含电感项，从而捕获电压幅值损失和相位差。此模型对任何输入波形均有效。在此选项中，您可以直接指定电感和峰值耦合系数，也可以指定变压比和测量阻抗，在这种情况下，模块使用这些值来确定电感项。

### 忽略动态时的方程

方程基于两个理想变压器的叠加，两者的耦合系数均取决于转子角。这两个理想变压器具有共同的初级绕组。有关对理想变压器建模的详细信息，请参阅 Simscape™ Ideal Transformer 模块参考页。方程为：

*Kx* = *R* cos(
*N*
*Θ* )

*Ky* = *R* sin(
*N*
*Θ* )

*vx* =
*Kx*
*v*
p

*vy* =
*Ky*
*v*
p

*ip* = –
*Kx*
*ix* –
*Ky*
*iy*

其中：

- *vp* 和
  *ip* 分别是转子（或等效地，初级）电压和电流。
- *vx* 和
  *ix* 分别是第一个次级电压和电流。
- *vy* 和
  *iy* 分别是第二个次级电压和电流。
- *Kx* 是第一个次级绕组的耦合系数。
- *Ky* 是第二个次级绕组的耦合系数。
- *R* 是变压比。
- *N* 是极对数。
- *Θ* 是转子角。

### 包含动态时的方程

方程基于两个互感器的叠加，两者的耦合系数均取决于转子角。这两个互感器具有共同的初级绕组。有关对互感器建模的详细信息，请参阅 Simscape Mutual Inductor 模块参考页。方程为：

vp=Rpip+Lpdipdt+LpLsk(cos(Nθ)dixdt+sin(Nθ)diydt)

vx=Rsix+Lsdixdt+LpLskcos(Nθ)dipdt

vy=Rsiy+Lsdiydt+LpLsksin(Nθ)dipdt

其中：

- *vp* 和
  *ip* 分别是转子（或等效地，初级）电压和电流。
- *vx* 和
  *ix* 分别是第一个次级电压和电流。
- *vy* 和
  *iy* 分别是第二个次级电压和电流。
- *Rp* 是转子（或初级）电阻。
- *Lp* 是转子（或初级）电感。
- *Rs* 是定子（或次级）电阻。
- *Ls* 是定子（或次级）电感。
- *N* 是极对数。
- *k* 是耦合系数。
- *Θ* 是转子角。

假设两个次级绕组之间的耦合为零。

数据手册通常不会给出耦合系数和电感参数，而是给出变压比 R 和测量阻抗。如果为 **Parameterization** 参数选择 `Specify transformation ratio and measured impedances`，则您提供的值将用于确定如上定义的方程系数值。

### 变量

要在仿真前为模块变量设置优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值来指定模型中变量的预期幅值。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 System Scaling by Nominal Values。
