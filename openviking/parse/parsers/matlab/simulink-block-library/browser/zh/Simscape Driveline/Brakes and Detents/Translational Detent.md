---
type: simulink-block
title: 'Translational Detent'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Brakes and Detents'
documentation_page: 'translationaldetent'
documentation_source_path: 'ref/translationaldetent.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Detent

## 端口

### 守恒

### **C** — 壳体机械平移

与壳体关联的机械平移守恒端口。

### **R** — 杆机械平移

与滑块或杆关联的机械平移守恒端口。

## 参数

### 定位器特性

### **Parameterization** — 定位器特性参数 `By peak force and notch width` (default) | `By table lookup` | `By geometry`

定位器特性规格。

- `By peak force and notch width` —
  通过峰值剪切力和凹槽宽度指定定位器特性。
- `By table lookup` — 基于滑块和壳体之间的相对位移，通过一维查表定义定位器特性。
- `By geometry` — 通过球-凹槽几何和动力学定义定位器特性。

### **Peak force** — 最大定位器剪切力 `10` `N` (default) | positive scalar

定位器内部产生的峰值剪切力。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By peak force and notch width`。

### **Notch width** — 剪切力区域 `30` `mm` (default) | positive scalar

产生剪切力的区域宽度。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By peak force and notch width`。

### **Relative displacement vector** — 位移查找向量 `[-15 -12.3 -7.6 -1.1 1.1 7.6 12.3 15]` `mm` | vector

与 **Force vector** 参数中的值对应的输入相对位移向量。此向量的大小必须与 **Force vector** 参数相同。必须以递增顺序指定位移。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By table lookup`。

### **Force vector** — 力查找向量 `[0, 0, -8.365, -5.87, 5.87, 8.365, 0, 0]` `N` (default) | vector

与 **Relative displacement vector** 参数对应的剪切力输入值向量。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By table lookup`。

### **Interpolation method** — 用于查表的断点值之间的插值方法 `Smooth` (default) | `Linear`

查表断点插值。该模块使用 `tablelookup` 函数，通过数组数据将输入值映射到输出值来对非线性进行建模。

- `Linear` — 选择此选项以实现最低计算成本。
- `Smooth` — 选择此选项以生成具有连续一阶导数的连续曲线。

有关更多信息，请参阅 `tablelookup`。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By table lookup`。

### **Ball diameter** — 球-凹槽几何的球直径测量 `12` `mm` (default) | positive scalar

球的横截面直径。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By geometry`。

### **Notch angle** — 球-凹槽几何的凹槽角度测量 `120` `deg` (default) | positive scalar

凹槽的全角度。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By geometry`。

### **Notch depth** — 球-凹槽几何的凹槽深度测量 `4.5` `mm` (default) | nonnegative scalar

滑块中凹槽的深度。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By geometry`。

### **Preload force** — 球-凹槽几何的弹簧预载荷力测量 `15` `N` (default) | nonnegative scalar

用于预加载定位器弹簧的力。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By geometry`。

### **Spring stiffness** — 球-凹槽几何的弹簧刚度测量 `3000` `N/m` (default) | nonnegative scalar

定位器弹簧的刚度。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By geometry`。

### **Shear reversal region** — 球-凹槽几何的剪切反向区域长度测量 `0.1` `mm` (default) | nonnegative scalar

凹槽面之间的区域宽度。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By geometry`。

### **Initial relative position** — 起始位置 `0` `mm` (default) | scalar

仿真开始时滑块和壳体的相对位移。

### 摩擦

### **Viscous friction coefficient** — 比例粘性摩擦 `0.1` `N/(m/s)` (default) | nonnegative scalar

球-凹槽接触的粘性摩擦系数。

### **Friction to peak force ratio** — 动摩擦比 `0.01` (default) | positive scalar

用于计算动摩擦的比率。动摩擦为此比率乘以峰值剪切力。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By peak force and notch width` 或 `By table lookup`。

### **Kinetic friction coefficient** — 比例动摩擦 `0.1` (default) | positive scalar

球-凹槽接触的动摩擦系数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By geometry`。

### **Friction velocity threshold** — 与峰值动摩擦相关的速度 `0.05` `m/s` (default) | positive scalar

定位器中达到峰值动摩擦所需的相对速度。

## 所属库

Simscape / Driveline / Brakes & Detents / Translational

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011b 中引入**

## 描述

双面、弹簧加载的平移定位器

Translational Detent 模块表示一个带球和锥形凹槽的双面、弹簧加载的平移定位器。定位器滑块在定位器壳体上水平滑动。这种相互作用产生水平剪切力。滑块内部是锥形凹槽，定位器壳体包含一个竖直弹簧。定位器球位于弹簧和锥形凹槽之间。模型还包括滑块和壳体之间的粘性阻尼和动摩擦。

该图展示了球-凹槽定位器的几何结构。

平移定位器尺寸标注图

其中，

- *b* 是凹槽深度。
- *r* 是球半径。
- *α* 是凹槽半角。

根据您对模块进行参数化的方式，剪切力模型由几何和弹簧参数、峰值力和凹槽宽度，或由指定相对位移与力关系的查表来定义。

### Translational Detent 参数化

当您将 **Parameterization** 设置为 `By peak force and notch width` 时，该模块确保力-相对位移曲线在定位器区域上提供连续的力和力导数。如图所示，峰值力位于定位器中心和定位器边缘之间的中点。

定位器力分布图

当您将 **Parameterization** 设置为 `By geometry` 时，该模块使用四个区域来定义剪切力。图中显示了这些区域。

平移定位器区域图。区域为 1、2、3、4、3、2、1，其中区域 4 在原点处从负到正穿过 y 轴。下表提供了更多信息。

由于球是球形的且凹槽是对称的，水平力与位移的函数关于原点对称。

该表描述了每个区域的球位置、接触角和剪切力贡献。

| 区域 | 球位置和接触角 | 剪切力 |
| --- | --- | --- |
| 1 | 球在锥形凹槽外部。接触角为竖直。 | 仅粘性阻尼和动摩擦。无弹簧贡献。 |
| 2 | 球进入凹槽并与凹槽角接触。接触角从竖直方向旋转。 | 弹簧、粘性阻尼和动摩擦贡献。在从区域 2 过渡到区域 3 时达到峰值。 |
| 3 | 球沿凹槽面滑动。接触角恒定。 | 力随着弹簧伸展而减小，直到达到弹簧预载荷力。 |
| 4 | 球从一个面移动到另一个面。接触角切换方向。 | 力切换方向。剪切反向区域宽度控制此切换的平滑程度。 |

当您将 **Parameterization** 设置为 `By table lookup` 时，可以创建将剪切力与相对位移关联的任意函数。如果创建此类函数，请考虑以下最佳实践。

**能量守恒**

为确保定位器守恒能量，力-相对位移曲线的积分必须为零。

**仿真性能**

避免力-相对位移函数中出现不连续。最重要的要求是具有非零宽度的剪切反向区域，类似于几何参数化中的区域 4。

### 假设和限制

- 该模块不考虑惯性。需在 **R** 和 **C** 端口外部添加质量。
- 当您将 **Parameterization** 设置为 `By peak force and notch width` 或 `By table lookup` 时，动摩擦与定位器法向力无关。
