---
type: simulink-block
title: 'Nonlinear Translational Damper'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Couplings and Drives / Springs and Dampers'
documentation_page: 'nonlineartranslationaldamper'
documentation_source_path: 'ref/nonlineartranslationaldamper.html'
language: zh-CN
chinese_source: worker-translation
---

# Nonlinear Translational Damper

## 端口

### 守恒

### **R** — 轴机械平移

与轴关联的机械平移守恒端口。

### **C** — 壳体机械平移

与壳体关联的机械平移守恒端口。

## 参数

### **Parameterization** — 用于参数化阻尼的选项 `By polynomial`（默认）| `By table lookup`

是否通过多项式或查表对阻尼进行参数化。

### **Symmetry** — 用于参数化阻尼对称性的选项 `Symmetric`（默认）| `Two-sided`

是否使用对称或双侧查表参数化。

### **Vector of damping coefficients** — 多项式阻尼系数 `[10, 0, 1, 0, .1]` `N*s/m`（默认）| 长度为 5 的 vector

阻尼系数。物理单位适用于第一个元素。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By polynomial`，并将 **Symmetry** 设置为 `Symmetric`。

### **Vector of extension damping coefficients** — 多项式拉伸阻尼系数 `[10, 0, 1, 0, .1]` `N*s/m`（默认）| 长度为 5 的 vector

拉伸阻尼系数。物理单位适用于第一个元素。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By polynomial`，并将 **Symmetry** 设置为 `Two-sided`。

### **Vector of contraction damping coefficients** — 多项式压缩阻尼系数 `[100, -1, 10, 0, 0]` `N*s/m`（默认）| 长度为 5 的 vector

压缩阻尼系数。物理单位适用于第一个元素。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By polynomial`，并将 **Symmetry** 设置为 `Two-sided`。

### **Velocity vector** — 速度 `[-1, -.5, -.3, -.1, .1, .3, .5, 1]` `m/s`（默认）| vector

平移速度。该向量需要基于插值方法的最少元素数。当您将 **Interpolation method** 设置为：

- `Linear`，最小值为二。
- `Smooth`，最小值为三。

这些元素与 **Force vector** 参数一一对应。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By table lookup`。

### **Force vector** — 阻尼力 `[-100, -40, -20, -5, 5, 20, 40, 100]` `N`（默认）| vector

给定平移速度下的阻尼力。该向量需要基于插值方法的最少元素数。当您将 **Interpolation method** 设置为：

- `Linear`，最小值为二。
- `Smooth`，最小值为三。

这些元素与 **Velocity vector** 参数一一对应。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By table lookup`。

### **Interpolation method** — 在断点值之间插值的方法 `Linear`（默认）| `Smooth`

用于查找表断点插值的方法。该模块使用 `tablelookup` 函数，通过使用数组数据将输入值映射到输出值来对非线性进行建模：

- `Linear` — 选择此选项以获得最低的计算成本。
- `Smooth` — 选择此选项可生成具有连续一阶导数的连续曲线。

有关详细信息，请参阅 `tablelookup`。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By table lookup`。

### **Extrapolation method** — 处理超出断点数据集范围的输入值的方法 `Linear`（默认）| `Nearest` | `Error`

用于查找表断点外推的方法。当输入值超出参数列表中指定的范围时，此方法确定输出值。该模块使用 `tablelookup` 函数，通过使用数组数据将输入值映射到输出值来对非线性进行建模：

- `Linear` — 选择此选项可生成在外推区域中以及与插值区域的边界处具有连续一阶导数的曲线。
- `Nearest` — 选择此选项可生成不会高于数据中的最高点或低于数据中的最低点的外推。
- `Error` — 当您希望数据处于表范围内时，选择此选项可避免外推。如果输入信号超出表的范围，仿真将停止并生成错误。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By table lookup`。

## 所属库

Simscape / Driveline / Couplings & Drives / Springs & Dampers

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013a 中引入**

## 描述

平移系统中的非线性阻尼器

Nonlinear Translational Damper 模块表示一个非线性平移阻尼器。多项式参数化和查表参数化定义阻尼力与相对线速度之间的非线性关系。阻尼力可以关于零速度点对称或不对称。该模块在两个平移守恒端口上施加大小相等、方向相反的阻尼力。

对称多项式参数化根据以下表达式定义正相对速度和负相对速度的阻尼力：

F=b1v+sign(v)⋅b2v2+b3v3+sign(v)⋅b4v4+b5v5,

其中：

- *F* — 阻尼力
- *b1*,
  *b2*,...,
  *b5* — 阻尼系数
- *v* — 端口 **R** 和 **C** 之间的相对线速度，v=vR−vC
- *vR* — 与端口 **R** 关联的绝对线速度
- *vC* — 与端口 **C** 关联的绝对线速度

为避免减慢仿真的过零，通过指定奇多项式（*b2*,*b4* = 0）从多项式表达式中消除 sign 函数。

双侧多项式参数化根据以下表达式定义正相对速度和负相对速度的阻尼力：

F={b1ev+b2ev2+b3ev3+b4ev4+b5ev5,v≥0b1cv−b2cv2+b3cv3−b4cv4+b5cv5,v<0,

其中：

- *b1e*,
  *b2e*, ...,
  *b5e* — 正相对速度的阻尼系数
- *b1c*,
  *b2c*, ...,
  *b5c* — 负相对速度的阻尼系数

当端口 **R** 和 **C** 分开移动时，正相对速度对应于阻尼器拉伸。当端口 **R** 和 **C** 一起移动时，负相对速度对应于阻尼器压缩。

两种多项式参数化都使用五阶多项式表达式。要使用较低阶多项式，请将不需要的高阶系数设置为零。对于阶数大于五的多项式，请拟合为阶数小于或等于五的多项式，或使用查表参数化。

查表参数化基于一组速度向量和力向量定义阻尼力。如果向量中未包含原点，即零速度与零力的交点，该模块会自动添加一个数据点。

### 假设和限制

该模块假定黏性阻尼。阻尼力仅取决于速度。
