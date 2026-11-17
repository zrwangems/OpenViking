---
type: simulink-block
title: 'General Variable Mass'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Body Elements / Variable Mass'
documentation_page: 'generalvariablemass'
documentation_source_path: 'ref/generalvariablemass.html'
language: zh-CN
chinese_source: worker-translation
---

# General Variable Mass

## 端口

### 输入

### **m** — 以质量单位标量形式指定的质量物理信号

时变质量的输入端口。

#### 依赖

当 **Inertia** > **Mass** 参数设置为 `Time-Varying` 时，此端口启用。

### **com** — 以长度单位 3×1 或 1×3 向量形式指定的质心物理信号

时变质心坐标的输入端口。相对于模块参考坐标系，按 `[x y z]` 顺序指定坐标。

#### 依赖

当 **Inertia** > **Center of Mass** 参数设置为 `Time-Varying` 时，此端口启用。

### **I** — 以质量 × 长度^2 单位的 3×3 矩阵形式指定的惯性物理信号

时变惯性张量的输入端口。按 `[Ixx Ixy I xz; Iyx Iyy Iyz; Izx Izy Izz]` 顺序指定张量元素。这些元素相对于原点位于质心且坐标轴与参考坐标系对齐的坐标系定义。关于惯性矩和惯性积的定义，请参见 **Inertia tensor** 参数说明。

#### 依赖

当 **Inertia** > **Type** 参数设置为 `Custom` 时，此端口启用。

### 坐标系

### **R** — 参考坐标系坐标系

变质量元素的局部参考坐标系。将端口连接到坐标系线或另一个坐标系端口，以定义变质量元素的相对位置和方向。

## 参数

### 惯性

### **Type** — 点质量或分布质量的选择 `Custom`（默认）| `Point Mass`

点质量或分布质量的选择。选择 `Point Mass` 以建模无转动惯量的集中质量。选择 `Custom` 以建模具有指定惯性张量和质心的分布质量。

### **Mass** — 质量参数化 `Time-Varying`（默认）| `Constant`

固定质量或可变质量的选择。选择 `Time-Varying` 以通过物理信号输入端口 **m** 将质量指定为变量。选择 `Constant` 以将质量指定为常量参数。

### **Mass: Value** — 质量元素的总质量 `1 kg`（默认）| 以质量单位为单位的标量

质量元素的总质量。质量可以为正值或负值。指定负质量以建模复合体中空腔和空洞的总效应。当此参数激活时，质量为常量。

#### 依赖

当 **Mass** 参数设置为 `Constant` 时，此参数启用。

### **Center of Mass** — 质心参数化 `Time-Varying`（默认）| `Constant`

固定质心或可变质心的选择。选择 `Time-Varying` 以通过物理信号输入端口 **com** 将质心指定为变量。选择 `Constant` 以将质心指定为常量参数。

### **Center of Mass: Value** — 质心坐标 `[0 0 0] m`（默认）| 以长度单位为单位的三元素向量

质心相对于参考坐标系原点的 [*x* *y* *z*] 坐标。质心仅在均匀引力场中与重心重合。当此参数激活时，质心为常量。

#### 依赖

当 **Center of Mass** 参数设置为 `Constant` 时，此参数启用。

### **Inertia Matrix** — 惯性矩阵参数化 `Time-Varying`（默认）| `Constant`

可变惯性矩阵或固定惯性矩阵的选择。选择 `Time-Varying` 以通过物理信号输入端口 **I** 将惯性矩阵指定为变量。选择 `Constant` 以将惯性矩和惯性积分别指定为常量模块参数。

### **惯性矩阵：惯性矩** — 惯性矩阵的对角元素 `[1 1 1] kg * m^2`（默认）| 单位为质量\*长度^2 的三元素向量

按 [*I*xx
*I*yy
*I*zz] 顺序指定的可变质量元素的惯性矩。惯性矩
相对于原点位于质心且坐标轴与参考坐标系坐标轴平行的坐标系定义。
惯性矩是惯性张量的对角元素，

(IxxIyyIzz)，

其中：

- Ixx=∫m(y2+z2) dm
- Iyy=∫m(x2+z2) dm
- Izz=∫m(x2+y2) dm

#### 依赖关系

当 **Inertia
Matrix** 参数设置为
`Constant` 时，此参数启用。

### **惯性矩阵：惯性积** — 惯性矩阵的非对角元素 `[0 0 0] kg * m^2`（默认）| 单位为质量 \* 长度^2 的 3 元素数组

按 [*I*yz
*I*zx
*I*xy] 顺序指定的可变质量元素的惯性积。惯性积
相对于原点位于质心且坐标轴与参考坐标系坐标轴平行的坐标系定义。
惯性积是惯性矩阵的非对角元素，

(IxyIzxIxyIyzIzxIyz)，

其中：

- Iyz=−∫myz dm
- Izx=−∫mzx dm
- Ixy=−∫mxy dm

#### 依赖关系

当 **Inertia
Matrix** 参数设置为
`Constant` 时，此参数启用。

### 图形

### **Type** — 模型可视化中使用的几何类型 `Equivalent Inertia Ellipsoid`（默认）| `Marker` | `None`

此可变质量的可视化设置，指定为
`Equivalent Inertia Ellipsoid`、
`Marker` 或
`None`。将参数设置为
`Equivalent Inertia Ellipsoid` 以将
可变质量表示为椭球体。将参数设置为
`Marker` 以将可变质量表示为
标记。将参数设置为 `None` 以在模型可视化中隐藏
可变质量。

### **Shape** — 用于表示可变质量的标记形状 `Sphere`（默认）| `Cube` | `Frame`

用于可视化可变质量的标记形状，
指定为 `Sphere`、
`Cube` 或
`Frame`。标记的运动反映
可变质量本身的运动。

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Marker`。

### **Size** — 标记的宽度（以像素为单位）10 `pixels`（默认）| 标量

标记的宽度（以像素为单位）。此宽度不随缩放
级别缩放。请注意，标记的表观大小部分取决于
屏幕分辨率，较高分辨率每单位长度包含更多像素，
因此会产生较小的图标。

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Marker`。

### **Visual Properties** — 颜色和不透明度的参数化 `Simple`（默认）| `Advanced`

用于指定视觉属性的参数化。选择
`Simple` 以指定 **Diffuse
Color** 和 **Opacity**。选择
`Advanced` 以指定更多视觉
属性，例如 **Specular Color**、
**Ambient Color**、**Emissive
Color** 和 **Shininess**。

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Equivalent Inertia Ellipsoid` 或
`Marker`。

### **Diffuse Color** — 漫反射产生的光颜色 [0.5 0.5 0.5]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

漫反射产生的光颜色，指定为值在 0 到 1 范围内的 [R,G,B]
或 [R,G,B,A] 向量。该向量可以是
行向量或列向量。可选的第四个元素指定
颜色不透明度。省略不透明度元素等效于指定
值为 1。

漫反射颜色反映图形的主色，并提供
阴影，使图形具有三维外观。

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`From Geometry` 或
`Marker`

### **Opacity** — 图形不透明度 1.0（默认）| 0 到 1 范围内的标量

图形不透明度，指定为 0 到 1 范围内的标量。标量 0 对应于完全透明，标量 1 对应于完全不透明。

#### 依赖项

要启用此参数，请设置：

1. **Type** 为 `Equivalent
   Inertia Ellipsoid` 或
   `Marker`
2. **Visual Properties** 为
   `Simple`

### **Specular Color** — 镜面反射光颜色 [0.5 0.5 0.5 1.0]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

镜面反射光颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。此参数改变镜面高光的颜色，镜面高光是由于光源的光反射而在图形上形成的亮点。

#### 依赖项

要启用此参数，请设置：

1. **Type** 为 `Equivalent
   Inertia Ellipsoid` 或
   `Marker`
2. **Visual Properties** 为
   `Advanced`

### **Ambient Color** — 环境光颜色 [0.15 0.15 0.15 1.0]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

环境光颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

环境光是指并非直接来自光源的一般照明水平。环境光由经过多次反射和再反射以至于不再来自任何特定方向的光组成。您可以调整此参数来改变图形的阴影颜色。

#### 依赖项

要启用此参数，请设置：

1. **Type** 为 `Equivalent
   Inertia Ellipsoid` 或
   `Marker`
2. **Visual Properties** 为
   `Advanced`

### **Emissive Color** — 自发光颜色 [0.0 0.0 0.0 1.0]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量

自发光颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

发射颜色是不来自任何外部光源的颜色，因此看起来是由图形自身发出的。当图形具有发射颜色时，即使没有外部光源，图形也可见。

#### 依赖项

要启用此参数，请设置：

1. **Type** 为 `Equivalent
   Inertia Ellipsoid` 或
   `Marker`
2. **Visual Properties** 为
   `Advanced`

### **Shininess** — 高光锐度 75（默认）| 值约束在 0–128 范围内的标量

镜面光反射的锐度，指定为 0–128 范围内的标量数值。增大 shininess 值可获得更小但更锐利的高光。减小该值可获得更大但更平滑的高光。

#### 依赖项

要启用此参数，请设置：

1. **Type** 为 `Equivalent
   Inertia Ellipsoid` 或
   `Marker`
2. **Visual Properties** 为
   `Advanced`

## 所属库

Simscape / Multibody / Body Elements / Variable Mass

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

具有可变惯性属性的质量单元

General Variable Mass 模块向所连接的坐标系添加一个具有恒定或时变惯性属性的质量单元。该质量单元可以是无转动惯量的质点，也可以是具有转动惯量的自定义质量。惯性属性包括质量、质心、惯性矩和惯性积。每个惯性属性都可以独立配置为恒定或时变。

质量单元的几何形状未指定。标记或等效惯性椭球在 Multibody Explorer 的可视化窗格中标识该质量单元。惯性椭球提供质量单元主惯性矩的图形表示。该模块包含一个选项，用于在 Multibody Explorer 可视化窗口中隐藏可变质量单元。
