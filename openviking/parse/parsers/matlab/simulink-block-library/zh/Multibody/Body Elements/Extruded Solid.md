---
type: simulink-block
title: 'Extruded Solid'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Body Elements'
documentation_page: 'extrudedsolid'
documentation_source_path: 'ref/extrudedsolid.html'
language: zh-CN
chinese_source: worker-translation
---

# Extruded Solid

## 端口

### Frame

### **R** — 参考坐标系 frame

实体的局部参考坐标系。该坐标系相对于实体几何固定。将此端口连接到坐标系实体——端口、线或结点——以确定参考坐标系在模型中的放置位置。有关详细信息，请参阅 Working with Frames。
### Geometry

### **G** — 几何 geometry

表示实体的几何。将此端口连接到 Spatial Contact Force 模块以对实体上的接触进行建模。

#### 依赖关系

要启用此端口，请在 **Geometry** 下展开 **Export** 并选择 **Entire Geometry**。

## 参数

### Geometry

### **Extrusion Type** — 要使用的形状参数化 `Regular`（默认）| `General`

要使用的形状参数化。选择 `Regular` 或 `General`。

- `Regular` — 对正多边形横截面进行平移扫掠，几何中心与参考坐标系原点重合，挤出轴与参考坐标系 z 轴重合。
- `General` — 对一般横截面进行平移扫掠，几何中心与横截面 XY 平面上的 [0 0] 坐标重合，挤出轴与参考坐标系 z 轴重合。

### **Regular Extrusion: Number of Sides** — 挤出横截面的边数 `3`（默认）| 带长度单位的标量

挤出横截面的边数。根据定义，横截面是正多边形——即各边长度相等的多边形。指定的数值必须大于二。

### **Regular Extrusion: Outer Radius** — 挤出横截面内切圆的半径 `1 m`（默认）| 带长度单位的标量

完全内切挤出横截面的圆的半径。根据定义，横截面是正多边形——即各边长度相等的多边形。

### **Regular Extrusion: Length** — 挤出的扫掠长度 `1 m`（默认）| 带长度单位的标量

对指定挤出横截面进行扫掠的长度。挤出轴是实体参考坐标系的 *z* 轴。横截面在正方向和负方向上以相等的量进行扫掠。

### **General Extrusion: Cross-section** — 在 XY 平面上指定的横截面坐标 `[1 1; -1 1; -1 -1; 1 -1]`（默认）| 带长度单位的二列矩阵

横截面形状，指定为 [x,y] 坐标矩阵，每一行对应横截面轮廓上的一个点。指定的坐标必须定义一个没有自相交线段的闭合环路。

坐标的排列必须使得从一个点到下一个点时，实体区域始终位于左侧。该模块沿 z 轴挤出指定的横截面形状以获得挤出实体。

### **General Extrusion: Length** — 挤出的扫掠长度 `1 m`（默认）| 带长度单位的标量

对指定挤出横截面进行扫掠的长度。挤出轴是实体参考坐标系的 *z* 轴。横截面在正方向和负方向上以相等的量进行扫掠。

### **Entire Geometry** — 导出模块的真实几何 `off`（默认）| `on`

选择 **Entire Geometry** 以导出 Extruded Solid 模块的真实几何，该几何可用于其他模块，例如 Spatial Contact Force 模块。

#### 依赖关系

要启用此选项，请将 **Extrusion Type** 设置为 `Regular`，并在 **Export** 下选择 **Entire Geometry**。

### **Convex Hull** — 生成真实几何的凸包表示 `off`（默认）| `on`

选择 **Convex Hull** 以生成真实几何的凸包表示。该凸包可通过连接 Spatial Contact Force 模块用于接触。

#### 依赖关系

要启用此选项，请将 **Extrusion Type** 设置为 `General`，并在 **Export** 下选择 **Convex Hull**。

### Inertia

### **Type** — 要使用的惯性参数化方式 `Calculate from Geometry`（默认）| `Point Mass` | `Custom`

要使用的惯性参数化方式。选择 `Point
Mass` 可将集中质量建模为可忽略转动惯量的形式。选择 `Custom` 可对具有指定惯性矩和惯性积的分布质量建模。默认设置 `Calculate from Geometry`
使该模块能够根据实体几何以及指定的质量或质量
密度自动计算转动惯性
属性。

### **Based on** — 惯性计算所基于的参数 `Density`（默认）| `Mass`

用于惯性计算的参数。该模块根据实体几何和所选参数
获得惯性
张量。如果已知材料属性，请使用
`Density`。如果已知实体总质量，请使用 `Mass`。

### **Density** — 材料单位体积质量 `1000 kg/m^3`（默认）

材料单位体积质量。质量密度可以取
正值或负值。指定负质量密度可对实体中的空腔或孔洞
效应建模。

### **Mass** — 实体元素的总质量 `1 kg`（默认）| 带质量单位的标量

要赋予实体元素的总质量。此参数可以为正值或
负值。使用负值可捕捉复合
体（由多个实体和惯性组成）中的空腔或孔洞效应，同时注意确保
该物体的质量总体上为正。

### **Custom: Center of Mass** — 质心坐标 `[0 0 0] m`（默认）| 带长度单位的三元素向量

相对于模块参考坐标系的质心 [x y z] 坐标。仅在
均匀引力场中，质心才与重心
重合。

### **Custom: Moments of Inertia** — 惯性张量的对角元素 `[1 1 1] kg*m^2`（默认）| 带质量\*长度^2 单位的三元素向量

三元素向量，包含相对于某一坐标系指定的 [Ixx Iyy
Izz] 惯性矩，该坐标系原点位于质心，且各轴平行于模块参考坐标系。惯性
矩是惯性张量的对角元素

(IxxIyyIzz)，

其中：

- Ixx=∫m(y2+z2) dm
- Iyy=∫m(x2+z2) dm
- Izz=∫m(x2+y2) dm

### **Custom: Products of Inertia** — 惯性张量的非对角元素 `[0 0 0] kg*m^2`（默认）| 带质量\*长度^2 单位的三元素向量

三元素向量，包含相对于某一坐标系指定的 [Iyz Izx Ixy]
惯性积，该坐标系原点位于
质心，且各轴平行于模块参考坐标系。惯性
积是惯性张量的非对角元素

(IxyIzxIxyIyzIzxIyz)，

其中：

- Iyz=−∫myz dm
- Izx=−∫mzx dm
- Ixy=−∫mxy dm

### **Calculate from Geometry: Derived Values** — 显示计算得到的质量属性值 按钮

显示计算得到的实体质量属性值——质量、
质心、惯性矩和惯性积。单击
**Update** 按钮以计算并显示实体的质量
属性。在对模块参数进行任何更改后，请单击此按钮，以确保显示的值仍然
是最新的。

质心在实体的局部参考坐标系中表示。惯性矩和惯性积分别在
用于表示的惯性坐标系中表示——该坐标系的轴平行于参考坐标系的轴，但原点与实体质心
重合。

#### 依赖关系

当 **Inertia** > **Type** 模块参数设置为 `Calculate from
Geometry` 时，用于计算并显示质量属性的选项处于活动
状态。

### Graphic

### **Type** — 用于可视化的图形 `From Geometry`（默认）| `Marker` | `None`

实体的视觉表示类型，指定为 `From Geometry`、`Marker` 或 `None`。将参数设置为 `From Geometry` 以显示实体的视觉表示。将参数设置为 `Marker` 以将实体表示为标记。将参数设置为 `None` 以在模型可视化中隐藏实体。

### **Visual Properties** — 颜色和不透明度的参数化方式 `Simple`（默认）| `Advanced`

用于指定视觉属性的参数化方式。选择 `Simple` 以指定 **Diffuse Color** 和 **Opacity**。选择 `Advanced` 以指定更多视觉属性，例如 **Specular Color**、**Ambient Color**、**Emissive Color** 和 **Shininess**。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `From Geometry` 或 `Marker`。

### **Shape** — 用于表示实体的标记形状 `Sphere`（默认）| `Cube` | `Frame`

用于可视化实体的标记形状。标记的运动反映实体本身的运动。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Marker`。

### **Size** — 标记的宽度（以像素为单位） 10 `pixels`（默认）| 标量

标记的宽度（以像素为单位）。此宽度不随缩放级别缩放。请注意，标记的表观大小部分取决于屏幕分辨率，较高分辨率下每单位长度包含更多像素，因此会产生较小的图标。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Marker`。

### **Color** — 漫反射产生的光的颜色 [0.5 0.5 0.5]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

在直接白光下图形的颜色，指定为 0–1 范围内的 [R G B] 或 [R G B A] 向量。可选的第四个元素 (A) 指定 0–1 范围内的颜色不透明度。省略不透明度元素等同于指定值 1。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Simple`

### **Opacity** — 图形不透明度 1.0（默认）| 0 到 1 范围内的标量

图形不透明度，指定为 0 到 1 范围内的标量。标量为 0 对应于完全透明，标量为 1 对应于完全不透明。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Simple`

### **Diffuse Color** — 漫反射产生的光的颜色 [0.5 0.5 0.5]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

漫反射产生的光的颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值 1。

漫反射颜色反映渲染实体的主色，并提供使渲染对象呈现三维外观的着色。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

### **Specular Color** — 由于镜面反射产生的光的颜色 [0.5 0.5 0.5 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量

由于镜面反射产生的光的颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值为 1。此参数会改变镜面高光的颜色，镜面高光是由于光源的光被反射而在渲染实体上形成的亮点。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或
   `Marker`
2. **Visual Properties** 为
   `Advanced`

### **Ambient Color** — 环境光的颜色 [0.15 0.15 0.15 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量

环境光的颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值为 1。

环境光是指并非直接来自光源的一般照明水平。环境光由已经被反射和再反射很多次、以至于不再来自任何特定方向的光组成。您可以调整此参数来改变渲染实体的阴影颜色。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或
   `Marker`
2. **Visual Properties** 为
   `Advanced`

### **Emissive Color** — 自发光颜色 [0.0 0.0 0.0 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量

由于自发光产生的颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值为 1。

发射颜色是不来自任何外部光源的颜色，因此看起来是由实体自身发出的。当实体具有发射颜色时，即使没有外部光源，也可以看到该实体。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或
   `Marker`
2. **Visual Properties** 为
   `Advanced`

### **Shininess** — 高光锐度 75（默认）| 取值约束为 0–128 的标量

镜面光反射的锐度，指定为 0–128 范围内的标量数值。增大 shininess 值可获得更小但更锐利的高光。减小该值可获得更大但更平滑的高光。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或
   `Marker`
2. **Visual Properties** 为
   `Advanced`

### Frames

### **Show Port R** — 显示用于连接到其他模块的参考坐标系端口 on（默认）| off

选择此项可显示 **R** 端口。

### **New Frame** — 创建用于连接到其他模块的自定义坐标系按钮

点击创建按钮创建以打开用于创建新的附着于实体的坐标系的窗格。在此窗格中，您可以指定坐标系的名称、原点和方向。

- 要命名自定义坐标系，请点击 **Frame Name** 参数的文本字段。该名称标识实体模块上以及 Multibody Explorer 树视图窗格中的对应端口。
- 要选择自定义坐标系的 **Frame Origin**，请使用以下方法之一：

  - **At Reference Frame Origin**：使新坐标系原点与实体参考坐标系的原点重合。
  - **At Center of Mass**：使新坐标系原点与实体的质心重合。
  - **Based on Geometric Feature**：使新坐标系原点与所选特征的中心重合。有效特征包括曲面、线和点。从可视化窗格中选择一个特征，然后点击 **Use Selected Feature** 以确认原点的位置。原点位置的名称将出现在此选项下方的字段中。
- 要定义自定义坐标系的方向，请在 **Frame Axes** 部分下，选择自定义坐标系的 **Primary Axis** 和 **Secondary Axis**，然后指定它们的方向。

  使用以下方法选择用于指定主轴和次轴方向的向量。主轴平行于所选向量，并将其余两个轴约束在其法平面内。次轴平行于所选向量在法平面上的投影。

  - **Along Reference Frame Axis**：选择实体参考坐标系的一个轴。
  - **Along Principal Inertia Axis**：选择实体主惯性轴的一个轴。
  - **Based on Geometric Feature**：选择与实体所选几何特征相关联的向量。有效特征包括曲面和线。对应的向量在可视化窗格中用白色箭头指示。您可以从可视化窗格中选择一个特征，然后点击 **Use Selected Feature** 以确认选择。所选特征的名称将出现在此选项下方的字段中。

### **FrameN** — 编辑或删除现有自定义坐标系坐标系名称

您已创建的坐标系。`N` 是每个自定义坐标系的唯一标识编号。

- 点击文本字段以编辑现有自定义坐标系的名称。

- 点击编辑按钮编辑以编辑自定义坐标系的其他方面，例如原点和轴。
- 点击删除按钮删除以删除自定义坐标系。

#### 依赖关系

要启用此参数，请通过点击 **New Frame** 创建一个坐标系。

## 所属库

Simscape / Multibody / Body Elements

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

具有几何、惯量和颜色的实体拉伸元件

Extruded Solid 模块向所附坐标系添加一个具有几何、惯量和颜色的实体元件。该实体元件可以是简单刚体，也可以是复合刚体的一部分——复合刚体是一组刚性连接的实体，通常通过刚性变换在空间上分隔。将 Extruded Solid 和其他实体模块与 Rigid Transform 模块组合，以对复合刚体进行建模。

参考坐标系编码实体的位置和方向。在默认配置中，该模块仅提供参考坐标系。坐标系创建界面提供了基于实体几何特征定义附加坐标系的方法。您可以通过在 **Frames** 可展开区域中选择创建按钮来访问此界面。

### 导出几何属性

Extruded Solid 模块可以从拉伸实体生成凸包几何表示。该几何数据可用于建模空间接触力。

如图所示，凸包几何是真实几何的近似。请注意，该模块基于其真实几何计算物理属性，例如质量和惯性。

**L 形实体**
