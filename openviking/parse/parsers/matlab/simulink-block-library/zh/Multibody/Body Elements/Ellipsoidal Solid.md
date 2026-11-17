---
type: simulink-block
title: 'Ellipsoidal Solid'
family: 'body-elements'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Body Elements'
documentation_page: 'ellipsoidalsolid'
documentation_source_path: 'ref/ellipsoidalsolid.html'
language: zh-CN
chinese_source: worker-translation
---

# Ellipsoidal Solid

## 端口

### 坐标系

### **R** — 参考坐标系 frame

实体的局部参考坐标系。该坐标系相对于实体几何固定。将此端口连接到坐标系实体——端口、线或连接点——以确定参考坐标系在模型中的放置。有关详细信息，请参阅 Working with Frames。

### 几何

### **G** — 几何 geometry

表示实体的几何。将此端口连接到 Spatial Contact Force 模块以对实体上的接触建模。

#### 依赖关系

要启用此端口，请在 **Geometry** 下展开 **Export**，然后选择 **Entire Geometry**。

## 参数

### 几何

### **Radii** — 沿 *x*、*y* 和 *z* 半主轴方向的椭球半径 `[1 1 2] m`（默认） | 具有长度单位的标量

沿实体参考坐标系的 *x*、*y* 和 *z* 轴的椭球半径。如果所有半径相等，椭球变为球体。

### **Entire Geometry** — 导出模块的真实几何 `off`（默认） | `on`

选择 **Entire Geometry** 可导出 Ellipsoidal Solid 模块的真实几何，该几何可用于其他模块，例如 Spatial Contact Force 模块。

#### 依赖关系

要启用此选项，请在 **Export** 下选择 **Entire Geometry**。

### 惯性

### **Type** — 要使用的惯性参数化 `Calculate from Geometry`（默认） | `Point Mass` | `Custom`

要使用的惯性参数化。选择 `Point Mass` 以对具有可忽略转动惯量的集中质量建模。选择 `Custom` 以对具有指定惯性矩和惯性积的分布质量建模。默认设置 `Calculate from Geometry` 使模块能够根据实体几何以及指定的质量或质量密度自动计算转动惯量属性。

### **Based on** — 作为惯性计算基础的参数 `Density`（默认） | `Mass`

在惯性计算中使用的参数。模块根据实体几何和所选参数获得惯性张量。如果已知材料属性，请使用 `Density`。如果已知实体总质量，请使用 `Mass`。

### **Density** — 材料单位体积质量 `1000 kg/m^3`（默认）

材料单位体积质量。质量密度可取正值或负值。指定负质量密度以对实体中的空隙或空腔效应建模。

### **Mass** — 实体元素的总质量 `1 kg`（默认） | 具有质量单位的标量

要赋予实体元素的总质量。此参数可为正值或负值。使用负值可捕捉复合体（由多个实体和惯性组成）中的空隙或空腔效应，并注意确保该物体的质量总体上为正。

### **Custom: Center of Mass** — 质心坐标 `[0 0 0] m`（默认） | 具有长度单位的三元素向量

相对于模块参考坐标系的质心 [x y z] 坐标。仅在均匀引力场中，质心与重心重合。

### **Custom: Moments of Inertia** — 惯性张量的对角元素 `[1 1 1] kg*m^2`（默认） | 具有质量\*长度^2 单位的三元素向量

具有 [Ixx Iyy Izz] 惯性矩的三元素向量，相对于原点位于质心且轴平行于模块参考坐标系的坐标系指定。惯性矩是惯性张量的对角元素

(IxxIyyIzz),

其中：

- Ixx=∫m(y2+z2) dm
- Iyy=∫m(x2+z2) dm
- Izz=∫m(x2+y2) dm

### **Custom: Products of Inertia** — 惯性张量的非对角元素 `[0 0 0] kg*m^2`（默认） | 具有质量\*长度^2 单位的三元素向量

具有 [Iyz Izx Ixy] 惯性积的三元素向量，相对于原点位于质心且轴平行于模块参考坐标系的坐标系指定。惯性积是惯性张量的非对角元素

(IxyIzxIxyIyzIzxIyz),

其中：

- Iyz=−∫myz dm
- Izx=−∫mzx dm
- Ixy=−∫mxy dm

### **Calculate from Geometry: Derived Values** — 显示计算得到的质量属性值 按钮

显示实体的质量属性计算值——质量、质心、惯性矩和惯性积。单击 **Update** 按钮以计算并显示实体的质量属性。在对模块参数进行任何更改后单击此按钮，以确保显示的值仍然是最新值。

质心在实体的局部参考坐标系中解析。惯性矩和惯性积分别在惯性解析坐标系中解析——该坐标系的轴平行于参考坐标系的轴，但原点与实体质心重合。

#### 依赖关系

当 **Inertia** > **Type** 模块参数设置为 `Calculate from Geometry` 时，计算并显示质量属性的选项处于活动状态。

### 图形

### **Type** — 用于可视化的图形 `From Geometry`（默认） | `Marker` | `None`

实体的视觉表示类型，指定为 `From Geometry`、`Marker` 或 `None`。将参数设置为 `From Geometry` 以显示实体的视觉表示。将参数设置为 `Marker` 以将实体表示为标记。将参数设置为 `None` 以在模型可视化中隐藏实体。

### **Visual Properties** — 颜色和不透明度的参数化 `Simple`（默认） | `Advanced`

用于指定视觉属性的参数化。选择 `Simple` 以指定 **Diffuse Color** 和 **Opacity**。选择 `Advanced` 以指定更多视觉属性，例如 **Specular Color**、**Ambient Color**、**Emissive Color** 和 **Shininess**。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `From Geometry` 或 `Marker`。

### **Shape** — 用于表示实体的标记形状 `Sphere`（默认） | `Cube` | `Frame`

用于可视化实体的标记形状。标记的运动反映实体自身的运动。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Marker`。

### **Size** — 标记宽度（以像素为单位） 10 `pixels`（默认） | 标量

标记宽度（以像素为单位）。此宽度不随缩放级别缩放。请注意，标记的表观大小部分取决于屏幕分辨率，分辨率越高，每单位长度包含的像素越多，因此产生的图标越小。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Marker`。

### **Color** — 漫反射产生的光的颜色 [0.5 0.5 0.5]（默认） | 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量

直接白光下图形的颜色，指定为 0–1 范围内的 [R G B] 或 [R G B A] 向量。可选的第四个元素 (A) 指定 0–1 范围内的颜色不透明度。省略不透明度元素等效于指定值 1。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Simple`

### **Opacity** — 图形不透明度 1.0（默认） | 0 到 1 范围内的标量

图形不透明度，指定为 0 到 1 范围内的标量。标量 0 对应完全透明，标量 1 对应完全不透明。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Simple`

### **Diffuse Color** — 漫反射产生的光的颜色 [0.5 0.5 0.5]（默认） | 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量

漫反射产生的光的颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

漫射颜色反映渲染实体的主色，并提供阴影，使渲染对象呈现三维外观。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

### **Specular Color** — 镜面反射产生的光的颜色 [0.5 0.5 0.5 1.0]（默认） | 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量

镜面反射产生的光的颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。此参数更改镜面高光的颜色，镜面高光是由于光源的光反射而在渲染实体上出现的亮点。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

### **Ambient Color** — 环境光的颜色 [0.15 0.15 0.15 1.0]（默认） | 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量

环境光的颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

环境光是指并非直接来自光源的一般照明水平。环境光由已被反射和再反射许多次、以至于不再来自任何特定方向的光组成。您可以调整此参数以更改渲染实体的阴影颜色。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

### **Emissive Color** — 自发光颜色 [0.0 0.0 0.0 1.0]（默认） | 取值范围为 0 到 1 的 3×1 或 1×3 向量

自发光产生的颜色，指定为 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

发射颜色是不来自任何外部光源的颜色，因此看起来是由实体自身发出的。当实体具有发射颜色时，即使没有外部光源，也可以看到该实体。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

### **Shininess** — 高光锐度 75（默认） | 值约束在 0–128 范围内的标量

镜面光反射的锐度，指定为 0–128 范围内的标量数字。增大 shininess 值可获得更小但更锐利的高光。减小该值可获得更大但更平滑的高光。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry` 或 `Marker`
2. **Visual Properties** 为 `Advanced`

### 坐标系

### **Show Port R** — 显示用于连接到其他模块的参考坐标系端口 on（默认） | off

选择以显示 **R** 端口。

### **New Frame** — 创建用于连接到其他模块的自定义坐标系 按钮

单击 Create 按钮 Create 以打开用于创建新附着于实体的坐标系的窗格。在此窗格中，可以指定坐标系的名称、原点和方向。

- 要命名自定义坐标系，请单击 **Frame Name** 参数的文本字段。该名称标识实体模块上的对应端口以及 Multibody Explorer 树视图窗格中的对应端口。
- 要选择自定义坐标系的 **Frame Origin**，请使用以下方法之一：

  - **At Reference Frame Origin**：使新坐标系原点与实体参考坐标系的原点重合。
  - **At Center of Mass**：使新坐标系原点与实体的质心重合。
  - **Based on Geometric Feature**：使新坐标系原点与所选特征的中心重合。有效特征包括曲面、线和点。在可视化窗格中选择一个特征，然后单击 **Use Selected Feature** 以确认原点的位置。原点位置的名称显示在此选项下方的字段中。

- 要定义自定义坐标系的方向，请在 **Frame Axes** 部分下选择自定义坐标系的 **Primary Axis** 和 **Secondary Axis**，然后指定其方向。

  使用以下方法选择向量，以指定主轴和副轴的方向。主轴平行于所选向量，并将其余两个轴约束到其法平面。副轴平行于所选向量在法平面上的投影。

  - **Along Reference Frame Axis**：选择实体参考坐标系的轴。
  - **Along Principal Inertia Axis**：选择实体的主惯性轴的一个轴。
  - **Based on Geometric Feature**：选择与实体所选几何特征关联的向量。有效特征包括曲面和线。对应向量在可视化窗格中由白色箭头指示。您可以从可视化窗格中选择一个特征，然后单击 **Use Selected Feature** 以确认选择。所选特征的名称显示在此选项下方的字段中。

### **FrameN** — 编辑或删除现有自定义坐标系 frame name

您已创建的坐标系。`N` 是每个自定义坐标系的唯一标识编号。

- 单击文本字段以编辑现有自定义坐标系的名称。
- 单击 Edit 按钮 Edit 以编辑自定义坐标系的其他方面，例如原点和轴。
- 单击 Delete 按钮 Delete 以删除自定义坐标系。

#### 依赖关系

要启用此参数，请通过单击 **New Frame** 创建坐标系。

## 所属库

Simscape / Multibody / Body Elements

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

具有几何、惯性和颜色的实体椭球元素

Ellipsoidal Solid 模块是椭圆的三维扩展，其几何中心与参考坐标系原点重合，半主轴与参考坐标系的 x、y 和 z 轴重合。

Ellipsoidal Solid 模块向所附坐标系添加一个具有几何、惯性和颜色的实体元素。该实体元素可以是简单刚体，也可以是复合刚体的一部分——复合刚体是一组刚性连接的实体，通常通过刚性变换在空间上分离。将 Ellipsoidal Solid 和其他实体模块与 Rigid Transform 模块组合，以对复合刚体建模。

参考坐标系编码实体的位置和方向。在默认配置中，模块仅提供参考坐标系。坐标系创建界面提供基于实体几何特征定义其他坐标系的方法。您可以通过在 **Frames** 可展开区域中选择 Create 按钮 来访问此界面。
