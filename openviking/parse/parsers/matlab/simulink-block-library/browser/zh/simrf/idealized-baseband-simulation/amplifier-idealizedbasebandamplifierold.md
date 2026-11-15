---
type: simulink-block
title: 'Amplifier'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Idealized Baseband Simulation'
documentation_page: 'idealizedbasebandamplifierold'
documentation_source_path: 'ref/idealizedbasebandamplifierold.html'
language: zh-CN
chinese_source: worker-translation
---

# Amplifier

## 端口

在 R2025b 中未记录。

## 参数

### **Method** — 用于对非线性建模的方法 `Linear`（默认） | `Cubic polynomial` | `Hyperbolic tangent` | `Saleh model` | `Ghorbani model` | `Rapp model`

用于对放大器非线性建模的方法，指定为以下之一：

- `Linear`
- `Cubic polynomial`
- `Hyperbolic tangent`
- `Saleh model`
- `Ghorbani model`
- `Rapp model`

**可调：** Yes

### **Linear gain (dB)** — 输出函数的线性增益 `0`（默认） | real scalar

Amplifier 模块输出函数的线性增益，指定为 real scalar，以 decibels 为单位。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Linear`、`Cubic polynomial`、`Hyperbolic tangent` 或 `Rapp model`。

### **IIP3 (dBm)** — 三阶输入功率截点 `30`（默认） | real positive number

cubic polynomial 和 hyperbolic tangent 放大器模型的三阶输入功率截点，指定为 real positive number，以 dBm 为单位。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Cubic polynomial` 或 `Hyperbolic tangent`。

### **AM/PM conversion (degrees per dB)** — AM/PM conversion `10`（默认） | scalar

cubic polynomial 和 hyperbolic tangent 放大器模型的 AM/PM conversion，指定为 scalar，单位为 degrees per decibel。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Cubic polynomial` 或 `Hyperbolic tangent`。

### **Lower input power limit for AM/PM conversion (dBm)** — AM/PM conversion 随输入功率值线性缩放时的最小输入功率 `10`（默认） | scalar

AM/PM conversion 随输入功率值线性缩放时的最小输入功率，指定为 scalar。低于此值时，由 AM/PM conversion 引起的相移为零。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Cubic polynomial` 或 `Hyperbolic tangent`。

### **Upper input power limit for AM/PM conversion (dBm)** — AM/PM conversion 随输入功率值线性缩放时的最大输入功率 `inf`（默认） | positive scalar

AM/PM conversion 随输入功率值线性缩放时的最大输入功率，指定为 positive scalar。高于此值时，由 AM/PM conversion 引起的相移为常量。该最大偏移量的值由下式给出：

(AM/PM conversion)⋅(upper input power limit−lower input power limit),

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Cubic polynomial` 或 `Hyperbolic tangent`。

**可调：** Yes

### **Input scaling (dB)** — 对输入信号电平进行缩放的数值 `0`（默认） | scalar

用于 Saleh 和 Ghorbani 放大器模型、对输入信号电平进行缩放的数值，指定为 scalar，以 decibels 为单位。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Saleh model` 或 `Ghorbani model`。

### **Output scaling (dB)** — 对输出信号电平进行缩放的数值 `0`（默认） | scalar

用于 Saleh 和 Ghorbani 放大器模型、对输出信号电平进行缩放的数值，指定为 scalar，以 decibels 为单位。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Saleh model` 或 `Ghorbani model`。

### **AM/AM parameters [alpha beta]** — Saleh 放大器模型的 AM/AM 参数 `[2.1587 1.1517]`（默认） | vector

Saleh 放大器模型的 AM/AM 参数，指定为 vector。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Saleh model`。

### **AM/PM parameters [alpha beta]** — Saleh 放大器模型的 AM/AM 参数 `[4.0033 9.1040]`（默认） | vector

Saleh 放大器模型的 AM/AM 参数，指定为 vector。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Saleh model`。

### **AM/AM parameters [x1 x2 x3 x4]** — Ghorbani 的 AM/AM 参数 `[8.1081 1.5413 6.5202 -0.0718]`（默认） | vector

Ghorbani 放大器模型的 AM/AM 参数，指定为 vector。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Ghorbani model`。

### **AM/PM parameters [y1 y2 y3 y4]** — Ghorbani 的 AM/PM 参数 `[4.6645 2.0965 10.88 -0.003]`（默认） | vector

Ghorbani 放大器模型的 AM/PM 参数，指定为 vector。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Ghorbani model`。

### **Smoothness factor** — 幅度平滑因子 `0.5`（默认） | positive scalar

Rapp 放大器模型的幅度平滑因子，指定为 positive scalar。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Rapp model`。

### **Output saturation level** — 输出饱和电平 `1`（默认） | real positive number

Rapp 放大器模型的输出饱和电平，指定为 real positive number。用于指定输出饱和电平的 scalar。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Method** 设置为 `Rapp model`。

### **Specification method** — 噪声类型 `Noise factor`（默认） | `Noise temperature` | `Noise figure`

噪声类型，指定为 `Noise temperature`、`Noise figure` 和 `Noise factor`。

**可调：** Yes

### **Noise temperature (K)** — 用于对放大器噪声建模的噪声温度 `290`（默认） | nonnegative real number

用于对放大器噪声建模的噪声温度，指定为 nonnegative real number，单位为 kelvin。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Specification method** 设置为 `Noise temperature`。

### **Noise figure (dB)** — 用于对放大器噪声建模的噪声系数 `3.01`（默认） | nonnegative real number

用于对放大器噪声建模的噪声系数，指定为 nonnegative real number，以 decibels 为单位。将 `Noise figure` 设置为 `0` decibels 表示无噪声系统。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **Specification method** 设置为 `Noise figure`。

### **Noise factor** — 用于对放大器噪声建模的噪声因子 `2`（默认） | positive integer scalar greater than or equal to 1

用于相对于噪声温度对放大器噪声建模的噪声因子，指定为 positive integer scalar greater than or equal to 1。

要启用此参数，请将 **Specification method** 设置为 `Noise factor`。

**可调：** Yes

### **Initial seed** — 随机数生成器的种子 `67987`（默认） | nonnegative integer less than 232

随机数生成器的种子，指定为 nonnegative integer less than 232。使用此值初始化模块用于生成噪声的随机数生成器。

## 所属库

在 R2025b 中未记录。

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2006a 之前引入**

## 描述

带噪声放大器的复基带模型

Amplifier 模块生成带热噪声的放大器的复基带模型。
此模块提供六种对非线性建模的方法和三种指定噪声的方法。

**注意**

此模块假定标称阻抗为 1 ohm。
