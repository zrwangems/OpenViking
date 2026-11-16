---
type: simulink-block
title: 'Revolved Solid'
family: 'sm'
product_id: 'sm'
product_name: 'Simscape Multibody'
documentation_release: R2025b
official_category: 'Multibody Modeling / Bodies / Body Elements'
documentation_page: 'revolvedsolid'
documentation_source_path: 'ref/revolvedsolid.html'
language: zh-CN
chinese_source: worker-translation
---

# Revolved Solid

## 端口

### 坐标系

### **R** — 参考坐标系 frame

实体的局部参考坐标系。此坐标系相对于实体几何固定。将此端口连接到 frame 实体——端口、线或结点——以解析参考坐标系在模型中的放置。有关详细信息，请参阅 Working with Frames。
### 几何

### **CH** — 凸包表示 geometry

表示实体几何的凸包。将此端口连接到 Spatial Contact Force 模块以对凸包上的接触建模。

#### 依赖关系

要启用此端口，请在 **Geometry** 下展开 **Export** 并选择 **Convex Hull**。

## 参数

### 几何

### **Revolution: Cross-section** — 在 XZ 平面上指定的截面坐标 `[1 1; 1 -1; 2 -1; 2 1] m`（默认）| 单位为长度的两列矩阵

截面形状指定为 [x,z] 坐标矩阵，每一行对应截面轮廓上的一个点。指定的坐标必须定义闭合回路，且不得有自相交线段。

坐标的排列必须使得从一个点到下一个点时，实体区域始终位于左侧。该模块将指定的截面形状绕参考坐标系 z 轴旋转，以获得旋转实体。

### **Revolution: Extent of Revolution** — 完整或部分旋转的选择 `Full`（默认）| `Custom`

要使用的旋转扫掠类型。使用默认设置 `Full`，以最大 360 度旋转截面形状。选择 `Custom`，以较小角度旋转截面形状。

### **Revolution: Revolution Angle** — 部分旋转的扫掠角度 `180`（默认）| 正标量

与旋转相关联的旋转扫掠的角度。

### **Convex Hull** — 生成真实几何的凸包表示 `off`（默认）| `on`

选择 **Convex Hull** 以生成真实几何的凸包表示。通过连接 Spatial Contact Force 模块，此凸包可用于接触。

#### 依赖关系

要启用此选项，请在 **Export** 下选择 **Convex Hull**。

### 惯性

### **Type** — 要使用的惯性参数化 `Calculate from Geometry`（默认）| `Point Mass` | `Custom`

要使用的惯性参数化。选择 `Point Mass` 以对旋转惯性可忽略的集中质量建模。选择 `Custom` 以使用指定的惯性矩和惯性积对分布质量建模。默认设置 `Calculate from Geometry` 允许模块根据实体几何以及指定的质量或质量密度自动计算旋转惯性属性。

### **Based on** — 惯性计算所依据的参数 `Density`（默认）| `Mass`

要在惯性计算中使用的参数。模块根据实体几何和所选参数获得惯性张量。如果已知材料属性，请使用 `Density`。如果已知实体总质量，请使用 `Mass`。

### **Density** — 材料的单位体积质量 `1000 kg/m^3`（默认）

材料的单位体积质量。质量密度可取正值或负值。指定负质量密度以对实体中的空隙或空腔效应建模。

### **Mass** — 实体单元的总质量 `1 kg`（默认）| 单位为质量的标量

要赋予实体单元的总质量。此参数可为正值或负值。使用负值以捕获复合体（由多个实体和惯性组成）中的空隙或空腔效应，并小心确保该体的质量总体上为正值。

### **Custom: Center of Mass** — 质心坐标 `[0 0 0] m`（默认）| 单位为长度的三元素向量

质心相对于模块参考坐标系的 [x y z] 坐标。仅在均匀引力场中，质心与重心重合。

### **Custom: Moments of Inertia** — 惯性张量的对角元素 `[1 1 1] kg*m^2`（默认）| 单位为 mass\*length^2 的三元素向量

三元素向量，其中包含相对于一个坐标系的 [Ixx Iyy Izz] 惯性矩，该坐标系的原点位于质心，且各轴平行于模块参考坐标系。惯性矩是惯性张量的对角元素

(IxxIyyIzz),

其中：

- Ixx=∫m(y2+z2) dm
- Iyy=∫m(x2+z2) dm
- Izz=∫m(x2+y2) dm

### **Custom: Products of Inertia** — 惯性张量的非对角元素 `[0 0 0] kg*m^2`（默认）| 单位为 mass\*length^2 的三元素向量

三元素向量，其中包含相对于一个坐标系的 [Iyz Izx Ixy] 惯性积，该坐标系的原点位于质心，且各轴平行于模块参考坐标系。惯性积是惯性张量的非对角元素

(IxyIzxIxyIyzIzxIyz),

其中：

- Iyz=−∫myz dm
- Izx=−∫mzx dm
- Ixy=−∫mxy dm

### **Calculate from Geometry: Derived Values** — 显示计算出的质量属性值 按钮

显示计算出的实体质量属性值——质量、质心、惯性矩和惯性积。单击 **Update** 按钮以计算并显示实体的质量属性。在对模块参数进行任何更改后，单击此按钮以确保显示的值仍然是最新的。

质心在实体的局部参考坐标系中解析。惯性矩和惯性积各自在惯性解析坐标系中解析——该坐标系的各轴平行于参考坐标系的各轴，但原点与实体质心重合。

#### 依赖关系

当 **Inertia** > **Type** 模块参数设置为 `Calculate from Geometry` 时，计算和显示质量属性的选项处于活动状态。

### 图形

### **Type** — 用于可视化的图形 `From Geometry`（默认）| `Marker` | `None`

实体的视觉表示类型，指定为 `From Geometry`、`Marker` 或 `None`。将参数设置为 `From Geometry` 以显示实体的视觉表示。将参数设置为 `Marker` 以将实体表示为标记。将参数设置为 `None` 以在模型可视化中隐藏实体。

### **Visual Properties** — 颜色和不透明度的参数化 `Simple`（默认）| `Advanced`

用于指定视觉属性的参数化。选择 `Simple` 以指定 **Diffuse Color** 和 **Opacity**。选择 `Advanced` 以指定更多视觉属性，例如 **Specular Color**、**Ambient Color**、**Emissive Color** 和 **Shininess**。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `From Geometry` 或 `Marker`。

### **Shape** — 用于表示实体的标记形状 `Sphere`（默认）| `Cube` | `Frame`

用于可视化实体的标记形状。标记的运动反映实体自身的运动。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Marker`。

### **Size** — 标记的宽度，以像素为单位 10 `pixels`（默认）| 标量

标记的宽度，以像素为单位。此宽度不随缩放级别缩放。请注意，标记的表观大小部分取决于屏幕分辨率，分辨率越高，每单位长度包含的像素越多，因此产生的图标越小。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Marker`。

### **Color** — 漫反射光的颜色 [0.5 0.5 0.5]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

直接白光下图形的颜色，指定为 0–1 尺度上的 [R G B] 或 [R G B A] 向量。可选的第四个元素 (A) 指定颜色不透明度，尺度为 0–1。省略不透明度元素等效于指定值 1。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Simple`

### **Opacity** — 图形不透明度 1.0（默认）| 0 到 1 范围内的标量

图形不透明度，指定为 0 到 1 范围内的标量。标量 0 对应完全透明，标量 1 对应完全不透明。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Simple`

### **Diffuse Color** — 漫反射光的颜色 [0.5 0.5 0.5]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

由于漫反射产生的光色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

漫反射颜色反映渲染实体的主颜色，并提供阴影，使渲染对象具有三维外观。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

### **Specular Color** — 镜面反射光的颜色 [0.5 0.5 0.5 1.0]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

由于镜面反射产生的光色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。此参数更改镜面高光的颜色，镜面高光是由于光源的光反射而在渲染实体上形成的亮斑。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

### **Ambient Color** — 环境光的颜色 [0.15 0.15 0.15 1.0]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

环境光的颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

环境光指并非直接来自光源的一般照明水平。环境光由已被反射和再反射很多次、因而不再来自任何特定方向的光组成。您可以调整此参数以更改渲染实体的阴影颜色。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

### **Emissive Color** — 自发光颜色 [0.0 0.0 0.0 1.0]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量

由于自发光产生的颜色，指定为 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

发射颜色是不来自任何外部源的颜色，因此看起来是由实体自身发射的。当实体具有发射颜色时，即使没有外部光源，也可以看到该实体。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

### **Shininess** — 高光锐度 75（默认）| 值限制在 0–128 的标量

镜面光反射的锐度，指定为 0–128 尺度上的标量数值。增大 shininess 值可获得更小但更锐利的高光。减小该值可获得更大但更平滑的高光。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

### 坐标系

### **Show Port R** — 显示用于连接到其他模块的参考坐标系端口 on（默认）| off

选择以公开 **R** 端口。

### **New Frame** — 创建用于连接到其他模块的自定义坐标系 按钮

单击 Create 按钮 Create 以打开用于创建新的体附着坐标系的窗格。在此窗格中，可以指定坐标系的名称、原点和方向。

- 要命名自定义坐标系，请单击 **Frame Name** 参数的文本字段。该名称标识实体模块上的对应端口以及 Multibody Explorer 树视图窗格中的对应项。
- 要选择自定义坐标系的 **Frame Origin**，请使用以下方法之一：

  - **At Reference Frame Origin**：使新坐标系原点与实体参考坐标系的原点重合。
  - **At Center of Mass**：使新坐标系原点与实体质心重合。
  - **Based on Geometric Feature**：使新坐标系原点与所选特征的中心重合。有效特征包括曲面、线和点。从可视化窗格中选择特征，然后单击 **Use Selected Feature** 以确认原点位置。原点位置的名称出现在此选项下方的字段中。
- 要定义自定义坐标系的方向，请在 **Frame Axes** 部分下，选择自定义坐标系的 **Primary Axis** 和 **Secondary Axis**，然后指定它们的方向。

  使用以下方法选择用于指定主轴和次轴方向的向量。主轴平行于所选向量，并将其余两个轴约束到其法平面。次轴平行于所选向量在法平面上的投影。

  - **Along Reference Frame Axis**：选择实体参考坐标系的一个轴。
  - **Along Principal Inertia Axis**：选择实体的主惯性轴的一个轴。
  - **Based on Geometric Feature**：选择与实体所选几何特征相关联的向量。有效特征包括曲面和线。对应向量在可视化窗格中由白色箭头指示。您可以从可视化窗格中选择特征，然后单击 **Use Selected Feature** 以确认选择。所选特征的名称出现在此选项下方的字段中。

### **FrameN** — 编辑或删除现有自定义坐标系 frame 名称

您已创建的坐标系。`N` 是每个自定义坐标系的唯一标识编号。

- 单击文本字段以编辑现有自定义坐标系的名称。

- 单击 Edit 按钮 Edit 以编辑自定义坐标系的其他方面，例如原点和轴。
- 单击 Delete 按钮 Delete 以删除自定义坐标系。

#### 依赖关系

要启用此参数，请通过单击 **New Frame** 创建坐标系。

## 所属库

Simscape / Multibody / Body Elements

## 模块特性

R2025b 中未记载。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

具有几何、惯量和颜色的旋转实体单元

Revolved Solid 模块是一般横截面的旋转扫掠，其几何中心与横截面 XZ 平面上的 [0 0] 坐标重合，并且其旋转轴与参考坐标系 z 轴重合。

Revolved Solid 模块向附加坐标系添加一个具有几何、惯量和颜色的实体单元。该实体单元可以是简单刚体，也可以是复合刚体的一部分——复合刚体是一组刚性连接的实体，通常通过刚体变换在空间上分隔。将 Revolved Solid 和其他实体模块与 Rigid Transform 模块组合，以对复合刚体建模。

参考坐标系编码实体的位置和方向。在默认配置中，该模块仅提供参考坐标系。坐标系创建界面提供基于实体几何特征定义附加坐标系的方法。通过在 **Frames** 可展开区域中选择 Create 按钮来访问此界面。
