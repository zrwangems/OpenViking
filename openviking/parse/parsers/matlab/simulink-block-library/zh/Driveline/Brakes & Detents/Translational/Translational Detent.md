---
type: simulink-block
title: 'Translational Detent'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Brakes & Detents / Translational'
documentation_page: 'translationaldetent'
documentation_source_path: 'ref/translationaldetent.html'
language: zh-CN
chinese_source: worker-translation
---

# Translational Detent

## 端口

### 守恒端口

### **C** — 壳体机械平移

与壳体关联的机械平移守恒端口。

### **R** — 杆机械平移

与滑块或杆关联的机械平移守恒端口。

## 参数

### 定位器特性

### **Parameterization** — 定位器特性参数 `By peak force and notch width`（默认）| `By table lookup` | `By geometry`

定位器特性指定方式。

- `By peak force and notch width` — 通过峰值剪切力和凹口宽度指定定位器特性。
- `By table lookup` — 基于滑块与壳体之间的相对位移，通过一维查表定义定位器特性。
- `By geometry` — 通过球-凹口几何结构和动力学定义定位器特性。

### **Peak force** — 最大定位器剪切力 `10` `N`（默认）| 正标量

定位器内部产生的峰值剪切力。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By peak force and notch width`。

### **Notch width** — 剪切力区域 `30` `mm`（默认）| 正标量

剪切力产生的区域宽度。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By peak force and notch width`。

### **Relative displacement vector** — 位移查找向量 `[-15 -12.3 -7.6 -1.1 1.1 7.6 12.3 15]` `mm` | 向量

与 **Force vector** 参数中的值对应的输入相对位移向量。此向量的大小必须与 **Force vector** 参数相同。位移必须按递增顺序指定。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By table lookup`。

### **Force vector** — 力查找向量 `[0, 0, -8.365, -5.87, 5.87, 8.365, 0, 0]` `N`（默认）| 向量

与 **Relative displacement vector** 参数对应的剪切力输入值向量。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By table lookup`。

### **Interpolation method** — 查表断点值之间的插值方法 `Smooth`（默认）| `Linear`

查找表断点插值。该模块使用 `tablelookup` 函数，通过数组数据将输入值映射到输出值来建模非线性。

- `Linear` — 选择此选项可获得最低的计算成本。
- `Smooth` — 选择此选项可生成具有连续一阶导数的连续曲线。

有关详细信息，请参阅 `tablelookup`。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By table lookup`。

### **Ball diameter** — 球-凹口几何结构的球直径测量值 `12` `mm`（默认）| 正标量

球的横截面直径。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By geometry`。

### **Notch angle** — 球-凹口几何结构的凹口角度测量值 `120` `deg`（默认）| 正标量

凹口的全角。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By geometry`。

### **Notch depth** — 球-凹口几何结构的凹口深度测量值 `4.5` `mm`（默认）| 非负标量

滑块中凹口的深度。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By geometry`。

### **Preload force** — 球-凹口几何结构的弹簧预紧力测量值 `15` `N`（默认）| 非负标量

用于预紧定位器弹簧的力。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By geometry`。

### **Spring stiffness** — 球-凹口几何结构的弹簧刚度测量值 `3000` `N/m`（默认）| 非负标量

定位器弹簧的刚度。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By geometry`。

### **Shear reversal region** — 球-凹口几何结构的剪切反向区域长度测量值 `0.1` `mm`（默认）| 非负标量

凹口面之间的区域宽度。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By geometry`。

### **Initial relative position** — 起始位置 `0` `mm`（默认）| 标量

仿真开始时滑块与壳体的相对位移。

### 摩擦

### **Viscous friction coefficient** — 比例粘性摩擦 `0.1` `N/(m/s)`（默认）| 非负标量

球-凹口接触的粘性摩擦系数。

### **Friction to peak force ratio** — 动摩擦比 `0.01`（默认）| 正标量

用于计算动摩擦的比率。动摩擦为该比率乘以峰值剪切力。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By peak force and notch width` 或 `By table lookup`。

### **Kinetic friction coefficient** — 比例动摩擦 `0.1`（默认）| 正标量

球-凹口接触的动摩擦系数。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `By geometry`。

### **Friction velocity threshold** — 与峰值动摩擦相关的速度 `0.05` `m/s`（默认）| 正标量

定位器中达到峰值动摩擦所需的相对速度。

## 所属库

Simscape / Driveline / Brakes & Detents / Translational

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011b 中引入**

## 描述

双侧弹簧加载平移定位器

Translational Detent 模块表示具有球和锥形凹口的双侧弹簧加载平移定位器。定位器滑块在定位器壳体上水平滑动。这种相互作用产生水平剪切力。滑块内部是锥形凹口，定位器壳体包含垂直弹簧。定位器球位于弹簧和锥形凹口之间。该模型还包括滑块与壳体之间的粘性阻尼和动摩擦。

下图展示了球凹口定位器的几何结构。

平移定位器尺寸示意图

其中，

- *b* 是凹口深度。
- *r* 是球半径。
- *α* 是凹口半角。

根据您对模块进行参数化的方式，剪切力模型由几何和弹簧参数定义，由峰值力和凹口宽度定义，或由指定相对位移与力关系的查表定义。

### 平移定位器参数化

当您将 **Parameterization** 设置为 `By peak force and notch width` 时，模块确保力-相对位移曲线在定位器区域内提供连续的力和力导数。峰值力位于定位器中心和定位器边缘之间的中点，如下图所示。

定位器力分布图

当您将 **Parameterization** 设置为 `By geometry` 时，模块使用四个区域来定义剪切力。下图显示了这些区域。

平移定位器区域示意图。区域为 1、2、3、4、3、2、1，其中区域 4 在原点处从负到正穿过 y 轴。下表中有更多信息。

由于球是球形的且凹口是对称的，水平力与位移的函数关于原点对称。

下表描述了每个区域的球位置、接触角和剪切力贡献。

| 区域 | 球位置和接触角 | 剪切力 |
| --- | --- | --- |
| 1 | 球在锥形凹口外部。接触角为垂直方向。 | 仅粘性阻尼和动摩擦。无弹簧贡献。 |
| 2 | 球进入凹口并与凹口角接触。接触角从垂直方向旋转。 | 弹簧、粘性阻尼和动摩擦贡献。在从区域 2 过渡到区域 3 时达到峰值。 |
| 3 | 球沿凹口面滑动。接触角恒定。 | 力随着弹簧伸展而减小，直到达到弹簧预紧力。 |
| 4 | 球从一个面移动到另一个面。接触角切换方向。 | 力切换方向。剪切反向区域宽度控制此切换的平滑程度。 |

当您将 **Parameterization** 设置为 `By table lookup` 时，您可以创建将剪切力与相对位移关联的任意函数。如果创建此类函数，请考虑以下最佳实践。

**能量守恒**

为确保定位器守恒能量，力-相对位移曲线的积分必须为零。

**仿真性能**

避免力-相对位移函数中的不连续性。最重要的要求是具有非零宽度的剪切反向区域，类似于几何参数化中的区域 4。

### 假设和限制

- 该模块不考虑惯性。请从外部向 **R** 和 **C** 端口添加质量。
- 当您将 **Parameterization** 设置为 `By peak force and notch width` 或 `By table lookup` 时，动摩擦与定位器法向力无关。
