---
type: simulink-block
title: 'General Flexible Plate'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Body Elements / Flexible Bodies / Plates and Shells'
documentation_page: 'generalflexibleplate'
documentation_source_path: 'ref/generalflexibleplate.html'
language: zh-CN
chinese_source: worker-translation
---

# General Flexible Plate

## 端口
```yaml
ports:
- name: FN
  summary: 自定义坐标系坐标系
  direction: unspecified
- name: R
  summary: 参考坐标系坐标系
  direction: unspecified
```

### 坐标系

### **FN** — 自定义坐标系坐标系

自定义的刚体附着坐标系。使用 New Frame 参数指定该端口的名称。如果未指定自定义坐标系的名称，模块会将坐标系命名为 **FN**，其中 `N` 是标识编号。

#### 依赖关系

要启用自定义坐标系端口，请点击 **New Frame** 创建一个坐标系。

### **R** — 参考坐标系坐标系

虚拟未变形体的参考坐标系，表示柔性体的整体刚体运动。**R** 坐标系在物理上并不附着于柔性体。

**R** 端口不得与任何施加力和力矩或具有惯性的模块刚性连接。
## 参数
```yaml
parameters:
- name: Midsurface
  summary: 板中面的坐标 [1 1; -1 1; -1 -1; 1 -1] m | *N*×2 矩阵 | *M*×1 或 1×*M* 元胞数组，包含 *N*×2 矩阵
  group: 几何
- name: Thickness
  summary: 板厚度 0.1 m（默认）| 正标量
  group: 几何
- name: Density
  summary: 材料单位体积质量 2700 kg/m^3（默认）| 正标量
  group: 刚度和惯性
- name: Specify
  summary: 用于参数化板的弹性属性 Young's Modulus and Poisson's Ratio（默认）| Young's and Shear Modulus
  group: 刚度和惯性
- name: Young's Modulus
  summary: 轴向应力与轴向应变之比 70 GPa（默认）| 正标量
  group: 刚度和惯性
- name: Poisson's Ratio
  summary: 横向应变与法向应变之比 0.33（默认）| 范围 [0, 0.5) 内的标量
  group: 刚度和惯性
- name: Shear Modulus
  summary: 剪应力与工程剪应变之比 26 GPa（默认）| 正标量
  group: 刚度和惯性
- name: Type
  summary: 阻尼方法的类型 Proportional（默认）| Uniform Modal | None
  group: 阻尼
- name: Mass Coefficient
  summary: 质量矩阵的系数 0 1/s（默认）| 非负标量
  group: 阻尼
- name: Stiffness Coefficient
  summary: 刚度矩阵的系数 0.001 s（默认）| 非负标量
  group: 阻尼
- name: Damping Ratio
  summary: 均匀模态阻尼方法的阻尼比 0.01（默认）| 无量纲非负标量
  group: 阻尼
- name: Type
  summary: 参考条件的类型 Linearized Mean Axes（默认）| Body-Fixed
  group: 参考条件
- name: Frame
  summary: 用于体固定参考条件的连接坐标系 坐标系名称
  group: 参考条件
- name: Show Port R
  summary: 显示参考坐标系端口 off（默认）| on
  group: 参考条件
- name: Reduction
  summary: 用于对柔性体建模的方法 None（默认）| Modally Reduced
  group: 保真度
- name: Number of Retained Modes
  summary: 保留模态 1（默认）| 非负整数
  group: 保真度
- name: Type
  summary: 用于平板可视化显示的图形 From Geometry（默认）| None
  group: Graphic
- name: Visual Properties
  summary: 颜色和不透明度的参数化 Simple（默认）| Advanced
  group: Graphic
- name: Color
  summary: 漫反射产生的光颜色 [0.5 0.5 0.5]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量
  group: Graphic
- name: Opacity
  summary: 图形不透明度 1.0（默认）| 0 到 1 范围内的标量
  group: Graphic
- name: Diffuse Color
  summary: 图形颜色 [0.5 0.5 0.5]（默认）| 三元素向量 | 三元素向量
  group: Graphic
- name: Specular Color
  summary: 镜面反射产生的光颜色 [0.5 0.5 0.5 1.0]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量
  group: Graphic
- name: Ambient Color
  summary: 环境光颜色 [0.15 0.15 0.15 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量
  group: Graphic
- name: Emissive Color
  summary: 自发光颜色 [0.0 0.0 0.0 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量
  group: Graphic
- name: Shininess
  summary: 高光锐度 75（默认）| 取值约束为 0–128 的标量
  group: Graphic
- name: New Frame
  summary: 创建自定义坐标系以连接到其他模块按钮
  group: Frames
- name: FrameN
  summary: 编辑或删除现有自定义坐标系坐标系名称
  group: Frames
```

### 几何

### **Midsurface** — 板中面的坐标 [1 1; -1 1; -1 -1; 1 -1] `m` | *N*×2 矩阵 | *M*×1 或 1×*M* 元胞数组，包含 *N*×2 矩阵

用于在局部 *xy* 平面上指定板中面边界的坐标。您可以通过以下方式指定中面：

- 使用 *N*×2 的 *xy* 坐标矩阵指定中面。每一行给出中面边界上一点的 [*x*,*y*] 坐标。这些点按指定顺序连接形成闭合折线。为确保折线闭合，模块会在最后一个点和第一个点之间插入一条线段。
- 使用 *M*×1 或 1×*M* 的元胞数组，包含 *N*×2 的 *xy* 坐标矩阵，以指定带孔的中面。数组中的第一个元素表示外边界，后续元素指定孔边界。

**注意**

确保任意两个边界不相交、不重叠、不接触。

此外，每个单独的边界必须满足：

- 无重复顶点
- 无自相交
- 至少三个非共线点

### **Thickness** — 板厚度 0.1 `m`（默认）| 正标量

板的厚度。模块通过沿板的局部 *z* 轴拉伸指定的中面来对板进行建模。拉伸关于板的局部 *xy* 平面对称。为使板理论适用，厚度应远小于中面的整体尺寸。

### 刚度和惯性

### **Density** — 材料单位体积质量 2700 `kg/m^3`（默认）| 正标量

材料单位体积质量。默认值对应于铝。

### **Specify** — 用于参数化板的弹性属性 `Young's Modulus and Poisson's Ratio`（默认）| `Young's and Shear Modulus`

用于参数化板的弹性属性。您可以指定 `Young's Modulus and Poisson's Ratio` 或 `Young's and Shear Modulus`。这些属性通常可在材料数据库中找到。

### **Young's Modulus** — 轴向应力与轴向应变之比 70 `GPa`（默认）| 正标量

板的弹性杨氏模量。该参数值越大，对弯曲和面内法向变形的抵抗能力越强。默认值对应于铝。

### **Poisson's Ratio** — 横向应变与法向应变之比 0.33（默认）| 范围 [0, 0.5) 内的标量

板的泊松比。指定值必须大于或等于 0 且小于 0.5。默认值对应于铝。

#### 依赖关系

要启用此参数，请将 **Specify** 设置为 `Young's Modulus and Poisson's Ratio`。

### **Shear Modulus** — 剪应力与工程剪应变之比 26 `GPa`（默认）| 正标量

板的剪切模量，也称为刚性模量。值越大，对剪切和扭转的抵抗能力越强。默认值对应于铝。

#### 依赖关系

要启用此参数，请将 **Specify** 设置为 `Young's and Shear Modulus`。

### 阻尼

### **Type** — 阻尼方法的类型 `Proportional`（默认）| `Uniform Modal` | `None`

平板的阻尼方法：

- 选择 `None` 以对无阻尼平板建模。
- 选择 `Proportional` 以应用比例（或 Rayleigh）阻尼方法。该方法将阻尼矩阵 [*C*] 定义为质量矩阵 [*M*] 和刚度矩阵 [*K*] 的线性组合：

  [C]=α[M]+β[K]，

  其中 *α* 和 *β* 为标量系数。
- 选择 `Uniform Modal` 以应用均匀模态阻尼方法。该方法对平板的所有振动模态应用单一阻尼比。该值越大，振动衰减越快。

  所选的参考条件会影响阻尼比适用的模态类型。有关参考条件的详细信息，请参阅参考条件。当对柔性体使用模态缩减时，仅保留模态的一个子集。有关模态缩减的详细信息，请参阅减少柔性体的自由度。

### **Mass Coefficient** — 质量矩阵的系数 0 `1/s`（默认）| 非负标量

质量矩阵的系数 *α*。该参数定义与质量矩阵 [*M*] 成比例的阻尼。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Proportional`。

### **Stiffness Coefficient** — 刚度矩阵的系数 0.001 `s`（默认）| 非负标量

刚度矩阵的系数 *β*。该参数定义与刚度矩阵 [*K*] 成比例的阻尼。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Proportional`。

### **Damping Ratio** — 均匀模态阻尼方法的阻尼比 0.01（默认）| 无量纲非负标量

应用于平板所有振动模态的阻尼比 *ζ*。该值越大，振动衰减越快。如果施加到平板上的边界条件与所选参考条件完全匹配，则 *ζ* < 1 产生欠阻尼模态衰减，而 *ζ* > 1 产生过阻尼耗散。当边界条件与参考条件不匹配时，所选阻尼比的效果会有所不同。有关参考条件的详细信息，请参阅参考条件。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Uniform Modal`。

**数据类型：** `double`

### 参考条件

### **Type** — 参考条件的类型 `Linearized Mean Axes`（默认）| `Body-Fixed`

指定要应用的参考条件的类型。有关详细信息，请参阅参考条件。

- `Linearized Mean Axes`：参考的体坐标系跟随瞬时质心，柔性体表现出无约束的变形振动模态。
- `Body-Fixed`：选择一个体附着坐标系作为参考的体坐标系。柔性体的变形表现出自由振动模态振型，在参考体坐标系位置处的平移和旋转变形为零。

### **Frame** — 用于体固定参考条件的连接坐标系 坐标系名称

输入用作参考体坐标系的连接坐标系的名称。坐标系名称区分大小写。确保所选坐标系作为端口暴露在模块上。不能使用 **R** 坐标系，它是虚拟未变形体的参考坐标系。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Body-Fixed`。

### **Show Port R** — 显示参考坐标系端口 off（默认）| on

选择以暴露 **R** 端口，它表示虚拟未变形体的参考坐标系。请注意，**R** 坐标系并非物理上附着于柔性体。

**R** 端口不得与任何施加力和力矩或具有惯性的模块刚性连接。

### 保真度

### **Reduction** — 用于对柔性体建模的方法 `None`（默认）| `Modally Reduced`

用于对柔性体建模的方法，指定为
`None` 或 `Modally Reduced`。将
该参数设置为 `None` 以使用有限元法生成的完整节点弹性坐标，或将该参数设置为 `Modally
Reduced` 以使用模态变换方法缩减体的弹性
坐标。对于这两种设置，该模块都使用浮动参考系
公式 [5-6] 将体与其弹性变形耦合。

### **Number of Retained Modes** — 保留模态 1（默认）| 非负整数

保留模态，指定为范围 [0, *n*] 内的整数，其中
*n* 是体的弹性自由度数量。如果
将该数值设置为 0，则柔性体被视为刚体。

#### 依赖关系

要启用此参数，请将 **Reduction** 设置为
`Modally Reduced`。

### Graphic

### **Type** — 用于平板可视化显示的图形 `From Geometry`（默认）| `None`

平板的可视表示类型，指定为 `From
Geometry` 或 `None`。将该参数设置为
`From Geometry` 以显示平板的可视表示。
将该参数设置为 `None` 以在模型可视化中隐藏平板。

### **Visual Properties** — 颜色和不透明度的参数化 `Simple`（默认）| `Advanced`

用于指定视觉属性的参数化。选择
`Simple` 以指定颜色和不透明度。选择
`Advanced` 以指定更多视觉属性，例如
**Specular Color**、**Ambient Color**、**Emissive
Color** 和 **Shininess**。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `From
Geometry`。

### **Color** — 漫反射产生的光颜色 [0.5 0.5 0.5]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

图形在直接白光下的颜色，指定为 0–1 范围内的 [R G B] 或 [R G B A]
向量。可选的第四个元素 (A) 指定 0–1 范围内的颜色不透明度。省略不透明度元素等效于指定值
1。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From
   Geometry`
2. **Visual Properties** 为
   `Simple`

### **Opacity** — 图形不透明度 1.0（默认）| 0 到 1 范围内的标量

图形不透明度，指定为 0 到 1 范围内的标量。标量为 0
对应于完全透明，标量为 1 对应于完全
不透明。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From
   Geometry`
2. **Visual Properties** 为
   `Simple`

### **Diffuse Color** — 图形颜色 [0.5 0.5 0.5]（默认）| 三元素向量 | 三元素向量

图形在直接白光下的颜色，指定为 0–1 范围内的 [R G B] 或 [R G B A]
向量。可选的第四个元素指定 0–1 范围内的颜色不透明度。省略不透明度元素等效于指定值
1。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为
   `Advanced`

### **Specular Color** — 镜面反射产生的光颜色 [0.5 0.5 0.5 1.0]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

镜面反射产生的光颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A]
向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。此参数会更改镜面高光的颜色，镜面高光是由于光源的光反射而在渲染梁上形成的亮点。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From
   Geometry`
2. **Visual Properties** 为
   `Advanced`

### **Ambient Color** — 环境光颜色 [0.15 0.15 0.15 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量

环境光的颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值为 1。

环境光指的是并非直接来自光源的一般照明水平。环境光由经过多次反射和再反射、以至于不再来自任何特定方向的光组成。您可以调整此参数以更改所渲染波束的阴影颜色。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From
   Geometry`
2. **Visual Properties** 为
   `Advanced`

### **Emissive Color** — 自发光颜色 [0.0 0.0 0.0 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量

由于自发光而产生的颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值为 1。

发射颜色是不来自任何外部光源的颜色，因此看起来是由波束自身发射的。当波束具有发射颜色时，即使没有外部光源，也可以看到该波束。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From
   Geometry`
2. **Visual Properties** 为
   `Advanced`

### **Shininess** — 高光锐度 75（默认）| 取值约束为 0–128 的标量

镜面光反射的锐度，指定为 0–128 范围内的标量数值。增大 shininess 值可获得更小但更锐利的高光。减小该值可获得更大但更平滑的高光。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From
   Geometry`
2. **Visual Properties** 为
   `Advanced`

### Frames

### **New Frame** — 创建自定义坐标系以连接到其他模块按钮

单击创建按钮 Create 打开一个用于创建新的体附着坐标系的窗格。在此窗格中，您可以指定坐标系的名称、原点和方向。

- 要命名自定义坐标系，请在 **Frame Name** 参数中输入名称。该名称用于标识模块上的端口以及 Multibody Explorer 树视图窗格中的端口。
- 在 **Frame Origin** 部分中选择坐标系原点：

  - **At Reference Frame Origin**：使新坐标系原点与未变形板的参考坐标系原点重合。
  - **Based on Geometric Feature**：使新坐标系原点与所选未变形几何特征的中心重合。有效特征包括曲面、线和点。从可视化窗格中选择一个特征，然后单击 **Use Selected Feature** 按钮以确认原点的位置。原点位置的名称将显示在此选项下方的字段中。
- 要定义自定义坐标系的方向，请在 **Frame Axes** 部分下选择自定义坐标系的 **Primary Axis** 和 **Secondary Axis**，然后指定它们的方向。

  使用以下方法选择用于指定主轴和次轴方向的向量。主轴平行于所选向量，并将其余两个轴约束到其法平面内。次轴平行于所选向量在法平面上的投影。

  - **Along Reference Frame Axis**：选择未变形板的参考坐标系的轴。
  - **Based on Geometric Feature**：选择与未变形板的所选几何特征相关联的向量。有效特征包括曲面和线。相应的向量在可视化窗格中用白色箭头指示。您可以从可视化窗格中选择一个特征，然后单击 **Use Selected Feature** 按钮以确认选择。所选特征的名称将显示在此选项下方的字段中。

### **FrameN** — 编辑或删除现有自定义坐标系坐标系名称

您创建的坐标系。使用 New Frame 参数指定端口的名称。如果未指定自定义坐标系的名称，模块会将坐标系命名为 **FN**，其中 `N` 是标识编号。

- 单击文本字段以编辑现有自定义坐标系的名称。

- 单击编辑按钮 Edit 以编辑自定义坐标系的其他方面，例如原点和轴。
- 单击删除按钮 Delete 以删除自定义坐标系。

#### 依赖关系

要启用此参数，请单击 **New Frame** 创建一个坐标系。
## 所属库

Simscape / Multibody / Body Elements / Flexible Bodies / Plates and Shells

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

用于变形的弹性薄板

通用柔性板模块对能够发生弹性变形（包括拉伸、弯曲和剪切效应）的薄而扁平结构进行建模。该模块应用剪切变形 Mindlin 板理论 [1][2][3]，并使用有限元方法 [4] 进行求解。您可以使用此模块对薄而扁平的结构进行建模，例如连杆和卫星太阳能帆板。

通用柔性板

要指定板的几何形状，请使用 **Midsurface** 和 **Thickness** 参数。板的中面位于 *xy* 平面内，厚度沿 *z* 轴方向。厚度必须远小于板的宽度和长度，并且板关于中面对称。有关更多详细信息，请参阅 Geometry 部分。

该模块对由均质、各向同性且线弹性材料制成的柔性板进行建模。您可以在 **Stiffness and Inertia** 部分中指定板的密度、杨氏模量和泊松比或剪切模量。此外，该模块支持两种阻尼方法以控制建模性能。要向板添加自定义坐标系，请在 **Frames** 部分中指定参数。
