---
type: simulink-block
title: 'Resolver'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Sensors and Transducers / Encoders and Transducers'
documentation_page: 'resolver'
documentation_source_path: 'ref/resolver.html'
language: zh-CN
chinese_source: worker-translation
---

# Resolver

## 端口

### 守恒

### **p1** — 初级绕组正极端子 电气

与初级绕组正极端子关联的电气守恒端口。

### **p2** — 初级绕组负极端子 电气

与初级绕组负极端子关联的电气守恒端口。

### **R** — Resolver 转子 机械旋转

连接到转子的机械旋转守恒端口。

### **C** — Resolver 外壳 机械旋转

连接到 Resolver 外壳的机械旋转守恒端口。

### **x1** — 次级绕组 *x* 正极端子 电气

与次级绕组 *x* 正极端子关联的电气守恒端口。

### **x2** — 次级绕组 *x* 负极端子 电气

与次级绕组 *x* 负极端子关联的电气守恒端口。

### **y1** — 次级绕组 *y* 正极端子 电气

与次级绕组 *y* 正极端子关联的电气守恒端口。

### **y2** — 次级绕组 *y* 负极端子 电气

与次级绕组 *y* 负极端子关联的电气守恒端口。

## 参数

### **Parameterization** — Resolver 参数化 `Specify transformation ratio and omit dynamics`（默认） | `Specify transformation ratio and measured impedances` | `Specify equation parameters directly`

选择以下方法之一进行模块参数化：

- `Specify transformation ratio and omit
  dynamics` — 仅提供变比、极对数和初始转子角度的值。此模型忽略变压器电感项，并且仅当传感器由正弦波驱动时才有效。这些方程基于两个理想变压器的叠加，二者均具有取决于转子角度的耦合系数。有关更多信息，请参阅省略动态时的方程。
- `Specify transformation ratio and measured
  impedances` — 提供额外值以确定变压器电感项，以对电压幅度损失和相位差建模。此模型对任何输入波形均有效。这些方程基于两个互感器的叠加，二者均具有取决于转子角度的耦合系数。有关更多信息，请参阅包含动态时的方程。
- `Specify equation parameters
  directly` — 对动态建模，但提供转子和定子电感以及峰值耦合系数的值，而不是变比和测得阻抗。有关更多信息，请参阅包含动态时的方程。此模型对任何输入波形均有效。

### **Transformation ratio** — 峰值输出电压与输入电压之比 `0.5`（默认） | 正数

在假设由电阻和电感引起的次级电压降可忽略的情况下，峰值输出电压与峰值输入电压之比。

#### 依赖项

要启用此参数，请将 **Parameterization** 参数设置为 `Specify transformation ratio and omit
dynamics` 或 `Specify transformation ratio
and measured impedances`。如果您为 **Parameterization** 参数选择 `Specify transformation ratio and measured
impedances`，则变比会考虑由初级绕组电阻引起的电压降。

### **Rotor resistance** — 初级电阻 `70` `Ohm`（默认） | 正数

转子欧姆电阻。此电阻也称为初级电阻。

#### 依赖项

要启用此参数，请将 **Parameterization** 参数设置为 `Specify transformation ratio and measured
impedances` 或 `Specify equation parameters
directly`。

### **Stator resistance** — 次级电阻 `180` `Ohm`（默认） | 正数

定子欧姆电阻。此电阻也称为次级电阻。假设两个次级具有相同的电阻。

#### 依赖项

要启用此参数，请将 **Parameterization** 参数设置为 `Specify transformation ratio and measured
impedances` 或 `Specify equation parameters
directly`。

### **Rotor reactance** — 初级电抗 `100` `Ohm`（默认） | 正数

当次级绕组开路时的转子电抗。此电抗也称为初级电抗。

#### 依赖项

要启用此参数，请将 **Parameterization** 参数设置为 `Specify transformation ratio and measured
impedances`。

### **Stator reactance** — 次级电抗 `300` `Ohm`（默认） | 正数

当初级绕组开路时的定子电抗。此电抗也称为次级电抗。

#### 依赖项

要启用此参数，请将 **Parameterization** 参数设置为 `Specify transformation ratio and measured
impedances`。

### **Frequency at which reactances and transformation ratio are specified** — 正弦电源频率 `10` `kHz`（默认） | 正数

测量电抗时所用正弦电源的频率。

#### 依赖项

要启用此参数，请将 **Parameterization** 参数设置为 `Specify transformation ratio and measured
impedances`。

### **Rotor inductance** — 初级电抗 `0.0016` `H`（默认） | 正数

转子或初级电感，*L*p。

#### 依赖项

要启用此参数，请将 **Parameterization** 参数设置为 `Specify equation parameters
directly`。

### **Stator inductance** — 次级电抗 `0.0048` `H`（默认） | 正数

定子或次级电感，*L*s。

#### 依赖项

要启用此参数，请将 **Parameterization** 参数设置为 `Specify equation parameters
directly`。

### **Peak coefficient of coupling** — 最大耦合系数 `0.35`（默认） | 0 到 1 之间（不含）的数

初级绕组与次级绕组之间的峰值耦合系数。

#### 依赖项

要启用此参数，请将 **Parameterization** 参数设置为 `Specify equation parameters
directly`。

### **Number of pole pairs** — 转子极对数 `1`（默认） | 正数

转子上的极对数。

## 所属库

Simscape / Electrical / Sensors & Transducers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ Code Generation
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2017b 中引入**

## 描述

测量旋转角度的旋转变压器

Resolver 模块对通用旋转变压器建模，该旋转变压器通过电磁耦合测量信号的电气相位角。该旋转变压器由旋转变压器组成，该旋转变压器将施加到初级绕组的交流电压耦合到两个次级绕组。这些次级绕组在物理上彼此成 90 度方向。随着转子角度变化，初级与两个次级绕组之间的相对耦合也随之变化。在 Resolver 模块模型中，第一个次级绕组的方向使得当转子位于零度时发生峰值耦合，因此第二个次级绕组在转子位于零度时具有最小耦合。

不失一般性，假设初级电路与转子电路之间的变压器为理想变压器，变比为 1:1。这导致转子电流和电压等效于初级电流和电压。

定义模块方程时有两个选项：

- 通过忽略变压器电感项来省略动态。仅当传感器由正弦波驱动时，此模型才有效，因为初级侧的任何 DC 分量都会传递到输出侧。
- 包含电感项，从而捕获电压幅度损失和相位差。此模型对任何输入波形均有效。在此选项中，您可以直接指定电感和峰值耦合系数，也可以指定变比和测得阻抗，在这种情况下，模块使用这些值来确定电感项。

### 省略动态时的方程

这些方程基于两个理想变压器的叠加，二者均具有取决于转子角度的耦合系数。这两个理想变压器共用初级绕组。有关对理想变压器建模的更多信息，请参阅 Simscape Ideal Transformer 模块参考页。方程为：

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
- *R* 是变比。
- *N* 是极对数。
- *Θ* 是转子角度。

### 包含动态时的方程

这些方程基于两个互感器的叠加，二者均具有取决于转子角度的耦合系数。这两个互感器共用初级绕组。有关对互感器建模的更多信息，请参阅 Simscape Mutual Inductor 模块参考页。方程为：

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
- *Θ* 是转子角度。

假设两个次级绕组之间的耦合为零。

数据表通常不会给出耦合系数和电感参数，而是给出变比 R 和测得阻抗。如果您为 **Parameterization** 参数选择 `Specify transformation ratio and measured impedances`，则您提供的值将用于确定方程系数的值，如上所定义。

### 变量

要在仿真前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关更多信息，请参阅 Set Priority and Initial Target for Block Variables。

使用标称值指定模型中变量的预期量级。基于标称值使用系统缩放可提高仿真鲁棒性。标称值可以来自不同来源。其中一个来源是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关更多信息，请参阅 System Scaling by Nominal Values。
