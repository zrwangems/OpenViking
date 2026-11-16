---
type: simulink-block
title: 'Nonlinear Rotational Damper'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Couplings & Drives / Springs & Dampers'
documentation_page: 'nonlinearrotationaldamper'
documentation_source_path: 'ref/nonlinearrotationaldamper.html'
language: zh-CN
chinese_source: worker-translation
---

# Nonlinear Rotational Damper

## 端口

### 守恒

### **R** — 轴机械平动

与轴关联的机械平动守恒端口。

### **C** — 壳体机械平动

与壳体关联的机械平动守恒端口。

## 参数

### **Parameterization** — 用于参数化阻尼的选项 `By polynomial`（默认）| `By table lookup`

是按多项式还是按查表参数化阻尼。

### **Symmetry** — 用于参数化阻尼对称性的选项 `Symmetric`（默认）| `Two-sided`

是使用对称还是双侧查表参数化。

### **Vector of damping coefficients** — 多项式阻尼系数 `[.0001, 0, 1e-05, 0, 1e-06]` `N*m*s/rad`（默认）| 长度为 5 的向量

阻尼系数。物理单位应用于第一个元素。

### **Vector of positive rotation damping coefficients** — 正旋转多项式阻尼系数 `[.0001, 0, 1e-05, 0, 1e-06]` `N*m*s/rad`（默认）| 长度为 5 的向量

正旋转阻尼系数。物理单位应用于第一个元素。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By polynomial`，并将 **Symmetry** 设置为 `Two-sided`。

### **Vector of negative rotation damping coefficients** — 负旋转多项式阻尼系数 `[.001, -1e-05, .0001, 0, 0]` `N*m*s/rad`（默认）| 长度为 5 的向量

负旋转阻尼系数。物理单位应用于第一个元素。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By polynomial`，并将 **Symmetry** 设置为 `Two-sided`。

### **Angular velocity vector** — 角速度 `[-1, -.5, -.3, -.1, .1, .3, .5, 1]` `rad/s`（默认）| 向量

角速度。向量需要基于插值方法的最小元素数。当将 **Interpolation method** 设置为：

- `Linear`，最小值为 2。
- `Smooth`，最小值为 3。

元素与 **Torque vector** 参数一一对应。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By table lookup`。

### **Torque vector** — 阻尼转矩 `[-.0001, -4e-05, -2e-05, -5e-06, 5e-06, 2e-05, 4e-05, .0001]` `N*m`（默认）

给定角速度下的阻尼转矩。向量需要基于插值方法的最小元素数。当将 **Interpolation method** 设置为：

- `Linear`，最小值为 2。
- `Smooth`，最小值为 3。

元素与 **Angular velocity vector** 参数一一对应。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By table lookup`。

### **Interpolation method** — 断点值之间的插值方法 `Linear`（默认）| `Smooth`

用于查找表断点插值的方法。该模块使用 `tablelookup` 函数，通过使用数组数据将输入值映射到输出值来对非线性进行建模：

- `Linear` — 选择此选项以获得最低计算成本。
- `Smooth` — 选择此选项以生成具有连续一阶导数的连续曲线。

有关详细信息，请参阅 `tablelookup`。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By table lookup`。

### **Extrapolation method** — 处理超出断点数据集范围的输入值的方法 `Linear`（默认）| `Nearest` | `Error`

用于查找表断点外推的方法。当输入值超出参数列表中指定的范围时，此方法确定输出值。该模块使用 `tablelookup` 函数，通过使用数组数据将输入值映射到输出值来对非线性进行建模：

- `Linear` — 选择此选项以在外推区域以及在与插值区域的边界处生成具有连续一阶导数的曲线。
- `Nearest` — 选择此选项以生成不会高于数据中最高点或低于数据中最低点的外推。
- `Error` — 当你希望数据位于表范围内时，选择此选项以避免外推。如果输入信号在表范围之外，仿真将停止并生成错误。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By table lookup`。

## 所属库

Simscape / Driveline / Couplings & Drives / Springs & Dampers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

旋转系统中的非线性阻尼器

Nonlinear Rotational Damper 模块表示一个非线性旋转阻尼器。多项式和查表参数化定义阻尼转矩与相对角速度之间的非线性关系。阻尼转矩可以关于零速度点对称或非对称。该模块在两个旋转守恒端口上施加大小相等、方向相反的阻尼转矩。

对称多项式参数化根据以下表达式定义正相对速度和负相对速度的阻尼转矩：

T=b1ω+sign(ω)⋅b2ω2+b3ω3+sign(ω)⋅b4ω4+b5ω5,

其中：

- *T* — 阻尼转矩
- *b1*, *b2*, ..., *b5* — 阻尼系数
- *ω* — 端口 **R** 和 **C** 之间的相对角速度，ω=ωR−ωC
- *ωR* — 与端口 **R** 关联的绝对角速度
- *ωC* — 与端口 **C** 关联的绝对角速度

为避免减慢仿真的零穿越，通过指定奇多项式（*b2*,*b4* = 0）来消除多项式表达式中的 sign 函数。

双侧多项式参数化根据以下表达式定义正相对速度和负相对速度的阻尼转矩：

T={b1pω+b2pω2+b3pω3+b4pω4+b5pω5,ω≥0b1nω+b2nω2+b3nω3+b4nω4+b5nω5,ω<0,

其中：

- *b1p*, *b2p*, ..., *b5p* — 正相对速度的阻尼系数
- *b1n*, *b2n*, ..., *b5n* — 负相对速度的阻尼系数

两种多项式参数化均使用五阶多项式表达式。要使用低阶多项式，请将不需要的高阶系数设置为零。要使用更高阶多项式，请拟合为低阶多项式或使用查表参数化。

查表参数化基于一组转矩和角速度向量定义阻尼转矩。如果未指定，该模块会自动在原点添加一个数据点，即零角速度与零转矩的交点。

### 假设与限制

该模块假定为粘性阻尼。阻尼力仅取决于速度。
