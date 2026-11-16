---
type: simulink-block
title: 'Flexible Angle Beam'
family: 'sm'
product_id: 'sm'
product_name: 'Simscape Multibody'
documentation_release: R2025b
official_category: 'Multibody Modeling / Bodies / Beam Elements'
documentation_page: 'flexibleanglebeam'
documentation_source_path: 'ref/flexibleanglebeam.html'
language: zh-CN
chinese_source: worker-translation
---

# Flexible Angle Beam

## 端口

### Frame

### **A** — 连接坐标系 frame

用于在模型中连接梁的坐标系。在未变形配置中，该坐标系相对于局部参考坐标系的原点，位于沿 -*z* 方向的梁长度一半处。

### **B** — 连接坐标系 frame

用于在模型中连接梁的坐标系。在未变形配置中，该坐标系相对于局部参考坐标系的原点，位于沿 +*z* 方向的梁长度一半处。

### **R** — 参考坐标系 frame

表示柔性体整体刚体运动的虚拟未变形体的参考坐标系。**R** 坐标系并未物理连接到柔性体。

**R** 端口不得与任何施加力/力矩或具有惯性的模块刚性连接。

## 参数

### 几何

### **End-to-End Width** — 水平肢两端之间的距离 1 `m`（默认） | positive scalar

水平肢两端之间的距离。

**注意**

**End-to-End Width** 必须大于 **Vertical Leg Thickness**。

### **End-to-End Height** — 垂直肢两端之间的距离 1 `m`（默认） | positive scalar

垂直肢两端之间的距离。

**注意**

**End-to-End Height** 必须大于 **Horizontal Leg Thickness**。

### **Horizontal Leg Thickness** — 水平肢两个面之间的距离 0.1 `m`（默认） | positive scalar

水平肢两个面之间的距离。

### **Vertical Leg Thickness** — 垂直肢两个面之间的距离 0.1 `m`（默认） | positive scalar

垂直肢两个面之间的距离。

### **Length** — 梁的挤出长度 10 `m`（默认） | positive scalar

梁的挤出长度。梁通过沿局部参考坐标系的 *z* 轴挤出指定横截面来建模。挤出关于 *xy* 平面对称，梁的一半沿 *z* 轴负方向挤出，另一半沿正方向挤出。

### 刚度和惯性

### **Type** — 用于指定刚度和惯性属性的方法 `Calculate from Geometry`（默认） | `Custom`

用于指定刚度和惯性属性的方法，指定为 `Calculate from Geometry` 或 `Custom`。

当将参数设置为 `Calculate from Geometry` 时，模块根据指定的密度、杨氏模量以及泊松比或剪切模量计算刚度和惯性属性。将参数设置为 `Custom` 以手动指定刚度和惯性属性。

### **Density** — 材料的单位体积质量 2700 `kg/m^3`（默认） | positive scalar

材料的单位体积质量——此处假设在梁中均匀分布。默认值对应于铝。

#### 依赖关系

要启用此参数，在 **刚度和惯性** 部分下，将 **Type** 参数设置为 `Calculate from Geometry`。

### **Specify** — 用于参数化梁的弹性属性 `Young's Modulus and Poisson's Ratio`（默认） | `Young's and Shear Modulus`

用于参数化梁的弹性属性。这些属性通常可从材料数据库中获得。

#### 依赖关系

要启用此参数，在 **刚度和惯性** 部分下，将 **Type** 参数设置为 `Calculate from Geometry`。

### **Young's Modulus** — 轴向应力与轴向应变之比 70 `GPa`（默认） | positive scalar

梁的杨氏弹性模量。其值越大，对弯曲和轴向变形的抵抗越强。默认值对应于铝。

#### 依赖关系

要启用此参数，在 **刚度和惯性** 部分下，将 **Type** 参数设置为 `Calculate from Geometry`。

### **Poisson's Ratio** — 横向应变与纵向应变之比 0.33（默认） | scalar in the range [0, 0.5)

梁的泊松比。指定值必须大于或等于 `0` 且小于 `0.5`。默认值对应于铝。

#### 依赖关系

要启用此参数，在 **刚度和惯性** 部分下，将 **Type** 参数设置为 `Calculate from Geometry`，并将 **Specify** 参数设置为 **Young's Modulus and Poisson's Ratio**。

### **Shear Modulus** — 剪切应力与工程剪切应变之比 26 `GPa`（默认） | positive scalar

梁的剪切模量（或刚性模量）。其值越大，对扭转变形的抵抗越强。默认值对应于铝。

#### 依赖关系

要启用此参数，在 **刚度和惯性** 部分下，将 **Type** 参数设置为 `Calculate from Geometry`，并将 **Specify** 参数设置为 **Young's and Shear Modulus**。

### **Derived Values** — 质量和刚度截面属性的计算值 按钮

梁的质量和刚度截面属性的计算值。单击 **Update** 以计算并显示这些值。

给出的属性包括 **Centroid** 和 **Shear Center**。质心是轴向力拉伸（或压缩）梁而不产生弯曲的点。剪切中心是横向力必须通过该点才能弯曲梁而不产生扭转的点。

刚度截面属性计算如下：

- **Axial Rigidity**: *E**A*
- **Flexural Rigidity**: [*E**I*x,
  *E**I*y]
- **Cross Flexural Rigidity**: *E**I*xy
- **Torsional Rigidity**: *G**J*

质量截面属性计算如下：

- **Mass per Unit Length**: *ρ**A*
- **Mass Moment of Inertia Density**: [*ρ**I*x,
  *ρ**I*y]
- **Mass Product of Inertia Density**: *ρ**I*xy
- **Polar Mass Moment of Inertia Density**: *ρ**I*p

方程参数包括：

- *A* — 横截面积
- *ρ* — 密度
- *E* — 杨氏模量
- *G* — 剪切模量
- *J* — 扭转常数（由 Saint-Venant 翘曲偏微分方程的解获得）

其余参数是梁的相关面积矩。这些矩是围绕形心坐标系的轴计算的——该坐标系与局部参考坐标系对齐，但其原点位于形心。面积矩为：

- *I*x,
  *I*y — 形心二次面积矩：

  [Ix,Iy]=[∫A(y−yc)2dA,∫A(x−xc)2dA],
- *I*xy — 形心惯性积：

  Ixy=∫A(x−xc)(y−yc)dA,
- *I*p — 形心极惯性矩：

  IP=Ix+Iy,

其中 *x*c 和 *y*c 是形心的坐标。

### **Geometric Centroid** — 梁横截面的形心 [0 0] `m`（默认） | 2-by-1 array

梁横截面的形心，指定为 2-by-1 array。该数组指定形心相对于梁参考坐标系的 *x* 和 *y* 坐标。

#### 依赖关系

要启用此参数，在 **刚度和惯性** 部分中，将 **Type** 设置为 `Custom`。

### **Bending Centroid** — 中性轴与横截面的交点 [0 0] `m`（默认） | 2-by-1 array

中性轴与横截面的交点，指定为 2-by-1 array。该数组指定形心相对于梁参考坐标系的 *x* 和 *y* 坐标。

#### 依赖关系

要启用此参数，在 **刚度和惯性** 部分中，将 **Type** 设置为 `Custom`。

### **Shear Center** — 梁的剪切中心 [0 0] `m`（默认） | 2-by-1 array

梁的剪切中心，指定为 2-by-1 array。该数组指定该点相对于梁参考坐标系的 *x* 和 *y* 坐标。

#### 依赖关系

要启用此参数，在 **刚度和惯性** 部分中，将 **Type** 设置为 `Custom`。

### **Axial Rigidity** — 抗轴向变形 1 `Pa*m^2`（默认） | scalar

抵抗沿梁纵向方向变形的能力，指定为标量。此参数指定刚度矩阵的 Sb 元素。

#### 依赖关系

要启用此参数，在 **刚度和惯性** 部分中，将 **Type** 设置为 `Custom`。

### **Flexural Rigidity** — 抗弯曲变形 [1 1] `Pa*m^4`（默认） | 2-by-1 array

抵抗弯曲变形的能力，指定为 2-by-1 array。该数组指定刚度矩阵的 Hxb 和 Hyb 元素。

#### 依赖关系

要启用此参数，在 **刚度和惯性** 部分中，将 **Type** 设置为 `Custom`。

### **Cross Flexural Rigidity** — 响应绕 y 轴的弯矩而抵抗绕 x 轴的弯曲变形 0 `Pa*m^4`（默认） | scalar

抵抗响应于绕 *y* 轴的弯矩而绕 *x* 轴弯曲变形的能力，指定为标量。此参数指定刚度矩阵的 Hxyb 元素。

#### 依赖关系

要启用此参数，在 **刚度和惯性** 部分中，将 **Type** 设置为 `Custom`。

### **Torsional Rigidity** — 抗扭转 1 `Pa*m^4`（默认） | scalar

抵抗绕梁纵向轴扭转的能力，指定为标量。此参数指定刚度矩阵的 Hzb 元素。

#### 依赖关系

要启用此参数，在 **刚度和惯性** 部分中，将 **Type** 设置为 `Custom`。

### **Center of Mass** — 质心 [0 0] `m`（默认） | 2-by-1 array

质心，指定为 2-by-1 array。该数组指定该点相对于梁参考坐标系的 *x* 和 *y* 坐标。

#### 依赖关系

要启用此参数，在 **刚度和惯性** 部分中，将 **Type** 设置为 `Custom`。

### **Mass Per Unit Length** — 单位长度质量 1 `kg/m`（默认） | scalar

单位长度质量，指定为标量。此参数指定质量矩阵的 mc 元素。

#### 依赖关系

要启用此参数，在 **刚度和惯性** 部分中，将 **Type** 设置为 `Custom`。

### **Mass Moment of Inertia Density** — 抵抗绕 `x` 和 `y` 轴旋转 [1 1] `kg*m`（默认） | 2-by-1 array

抵抗绕 *x* 和 *y* 轴旋转的能力，指定为 2-by-1 array。该数组指定质量矩阵的 ixc 和 iyc 元素。

#### 依赖关系

要启用此参数，在 **刚度和惯性** 部分中，将 **Type** 设置为 `Custom`。

### **Mass Product of Inertia Density** — 由绕 `y` 轴的力矩引起的对绕 `x` 轴旋转的抵抗 0 `kg*m`（默认） | scalar

由绕 *y* 轴的力矩引起的对绕 *x* 轴旋转的抵抗，指定为标量。此参数指定质量矩阵的 ixyc 元素。

#### 依赖关系

要启用此参数，在 **刚度和惯性** 部分中，将 **Type** 设置为 `Custom`。

### 阻尼

### **Type** — 阻尼方法类型 `Proportional`（默认） | `Uniform Modal` | `None`

要应用于梁的阻尼方法：

- 选择 `None` 以对无阻尼梁建模。
- 选择 `Proportional` 以应用比例（或 Rayleigh）阻尼方法。此方法将阻尼矩阵 [*C*] 定义为质量矩阵 [*M*] 和刚度矩阵 [*K*] 的线性组合：

  [C]=α[M]+β[K],

  其中 *α* 和 *β* 是标量系数。
- 选择 `Uniform Modal` 以应用均匀模态阻尼方法。此方法对梁的所有振动模态应用单一阻尼比。值越大，振动衰减越快。

  所选择的参考条件会影响阻尼比适用的模态类型。有关参考条件的详细信息，请参见参考条件。当您对柔性体使用模态缩减时，仅保留部分模态。有关模态缩减的详细信息，请参见减少柔性体的自由度。

### **Mass Coefficient** — 质量矩阵系数 0 `1/s`（默认） | nonnegative scalar

质量矩阵的系数 *α*。此参数定义与质量矩阵 [*M*] 成比例的阻尼。

#### 依赖关系

要启用此参数，将 **Type** 设置为 `Proportional`。

### **Stiffness Coefficient** — 刚度矩阵系数 0.001 `s`（默认） | nonnegative scalar

刚度矩阵的系数 *β*。此参数定义与刚度矩阵 [*K*] 成比例的阻尼。

#### 依赖关系

要启用此参数，将 **Type** 设置为 `Proportional`。

### **Damping Ratio** — 均匀模态阻尼方法的阻尼比 0.01（默认） | unitless nonnegative scalar

在均匀模态阻尼模型中应用于所有梁振动模态的阻尼比 *ζ*。值越大，梁振动衰减越快。

当 *ζ* = 0 时，梁无阻尼。如果施加到梁的边界条件与所选参考条件完全匹配，则 *ζ* < 1 产生欠阻尼模态衰减，*ζ* = 1 对应临界阻尼，*ζ* > 1 产生过阻尼耗散。当边界条件与参考条件不匹配时，所选阻尼比的效果会变化。有关参考条件的详细信息，请参见参考条件。

#### 依赖关系

要启用此参数，将 **Type** 设置为 `Uniform Modal`。

### 离散化

### **Number of Elements** — 梁有限单元的数量 1（默认） | positive integer

梁模型中的有限单元数量。增加单元数量始终会提高仿真精度。但实际上，在某个点之后，当单元很多时，精度的提高可以忽略不计。此外，更多单元会增加计算成本并降低仿真速度。

### 参考条件

### **Type** — 参考条件类型 `Linearized Mean Axes`（默认） | `Body-Fixed`

指定要应用的参考条件类型。有关详细信息，请参见参考条件。

- `Linearized Mean Axes`：参考的体坐标系跟随瞬时质心，柔性体表现出不受约束的变形振动模态。
- `Body-Fixed`：选择固连于体的坐标系作为参考的体坐标系。柔性体的变形表现出自由振动模态形状，在参考体坐标系位置处具有零平移和旋转变形。

### **Frame** — 用于 body-fixed 参考条件的连接坐标系 frame name

输入要用作参考体坐标系的连接坐标系名称。该坐标系名称区分大小写。确保所选的坐标系在模块上作为端口暴露。不能使用 **R** 坐标系，它是虚拟未变形体的参考坐标系。

#### 依赖关系

要启用此参数，将 **Type** 设置为 `Body-Fixed`。

### **Show Port R** — 显示参考坐标系端口 off（默认） | on

选择以显示 **R** 端口，该端口表示虚拟未变形体的参考坐标系。请注意，**R** 坐标系并未物理连接到柔性体。

**R** 端口不得与任何施加力/力矩或具有惯性的模块刚性连接。

### 保真度

### **Reduction** — 对柔性体建模的方法 `None`（默认） | `Modally Reduced`

用于对柔性体建模的方法，指定为 `None` 或 `Modally Reduced`。将参数设置为 `None` 以使用有限元方法生成的完整节点弹性坐标，或将参数设置为 `Modally Reduced` 以使用模态变换方法缩减体的弹性坐标。对于这两种设置，模块都使用浮动参考系公式 [1-2] 将体与其弹性变形耦合。

### **Number of Retained Modes** — 保留的模态 1（默认） | nonnegative integer

保留的模态，指定为范围 [0, *n*] 内的整数，其中 *n* 是体的弹性自由度数量。如果将数字设置为 0，则柔性体被视为刚体。

#### 依赖关系

要启用此参数，将 **Reduction** 设置为 `Modally Reduced`。

### 图形

### **Type** — 用于梁可视化的图形 `From Geometry`（默认） | `None`

梁的视觉表示类型，指定为 `From Geometry` 或 `None`。将参数设置为 `From Geometry` 可显示梁的视觉表示。将参数设置为 `None` 可在模型可视化中隐藏梁。

### **Visual Properties** — 颜色和不透明度的参数化 `Simple`（默认） | `Advanced`

用于指定视觉属性的参数化。选择 `Simple` 可指定 **Color** 和 **Opacity**。选择 `Advanced` 可指定更多视觉属性，例如 **Specular Color**、**Ambient Color**、**Emissive Color** 和 **Shininess**。

#### 依赖关系

要使此参数可用，请将 **Type** 设置为 `From Geometry`。

### **Color** — 漫反射光颜色 [0.5 0.5 0.5]（默认） | 取值范围为 0 到 1 的 3-by-1 或 1-by-3 向量 | 取值范围为 0 到 1 的 4-by-1 或 1-by-4 向量

白光直射下图形的颜色，指定为 0–1 范围内的 [R G B] 或 [R G B A] 向量。可选的第四个元素 (A) 指定 0–1 范围内的颜色不透明度。省略不透明度元素等同于指定值 1。

#### 依赖关系

要使此参数可用，请设置：

1. 将 **Type** 设置为 `From Geometry`
2. 将 **Visual Properties** 设置为 `Simple`

### **Opacity** — 图形不透明度 1.0（默认） | 0 到 1 范围内的 scalar

图形不透明度，指定为 0 到 1 范围内的 scalar。scalar 0 对应完全透明，scalar 1 对应完全不透明。

#### 依赖关系

要使此参数可用，请设置：

1. 将 **Type** 设置为 `From Geometry`
2. 将 **Visual Properties** 设置为 `Simple`

### **Diffuse Color** — 漫反射光颜色 [0.5 0.5 0.5]（默认） | 取值范围为 0 到 1 的 3-by-1 或 1-by-3 向量 | 取值范围为 0 到 1 的 4-by-1 或 1-by-4 向量

漫反射光颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值 1。

漫反射颜色反映渲染梁的主要颜色，并提供阴影，使渲染对象具有三维外观。

#### 依赖关系

要使此参数可用，请设置：

1. 将 **Type** 设置为 `From Geometry`
2. 将 **Visual Properties** 设置为 `Advanced`

### **Specular Color** — 镜面反射光颜色 [0.5 0.5 0.5 1.0]（默认） | 取值范围为 0 到 1 的 3-by-1 或 1-by-3 向量 | 取值范围为 0 到 1 的 4-by-1 或 1-by-4 向量

镜面反射光颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值 1。此参数更改镜面高光的颜色，该高光是由于来自光源的光反射而在渲染梁上形成的亮斑。

#### 依赖关系

要使此参数可用，请设置：

1. 将 **Type** 设置为 `From Geometry`
2. 将 **Visual Properties** 设置为 `Advanced`

### **Ambient Color** — 环境光颜色 [0.15 0.15 0.15 1.0]（默认） | 取值范围为 0 到 1 的 3-by-1 或 1-by-3 向量 | 取值范围为 0 到 1 的 4-by-1 或 1-by-4 向量

环境光颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值 1。

环境光是指并非直接来自光源的一般照明水平。环境光是被反射和再反射多次，以致不再来自任何特定方向的光。您可以调整此参数以更改渲染梁的阴影颜色。

#### 依赖关系

要使此参数可用，请设置：

1. 将 **Type** 设置为 `From Geometry`
2. 将 **Visual Properties** 设置为 `Advanced`

### **Emissive Color** — 自发光颜色 [0.0 0.0 0.0 1.0]（默认） | 取值范围为 0 到 1 的 3-by-1 或 1-by-3 向量

因自发光产生的颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值 1。

发射颜色是不来自任何外部源的颜色，因此看起来是由梁本身发射的。当梁具有自发光颜色时，即使没有外部光源也可以看到梁。

#### 依赖关系

要使此参数可用，请设置：

1. 将 **Type** 设置为 `From Geometry`
2. 将 **Visual Properties** 设置为 `Advanced`

### **Shininess** — 高光锐度 75（默认） | 值限制在 0–128 的 scalar

镜面光反射的锐度，指定为 0–128 范围内的 scalar 数字。增大 Shininess 值以获得更小但更锐利的高光。减小该值以获得更大但更平滑的高光。

#### 依赖关系

要使此参数可用，请设置：

1. 将 **Type** 设置为 `From Geometry`
2. 将 **Visual Properties** 设置为 `Advanced`

### 坐标系

### **Show Port A** — 用于连接到其他模块时显示端口 A on（默认） | off

选择以显示 **A** 端口。

### **Show Port B** — 用于连接到其他模块时显示端口 B on（默认） | off

选择以显示 **B** 端口。

### **New Frame** — 用于创建自定义坐标系以连接到其他模块的按钮

单击 Create 按钮 Create 以打开一个窗格，用于创建新的固连于体的坐标系。在该窗格中，您可以指定坐标系的名称、原点和方向。

- 要为自定义坐标系命名，请单击 **Frame Name** 参数的文本字段。该名称标识梁模块上的对应端口以及 Multibody Explorer 的树视图窗格中的对应项。
- 要为自定义坐标系选择 **Frame Origin**，请使用以下方法之一：

  - **At Reference Frame Origin**：使新坐标系原点与未变形梁的参考坐标系原点重合。
  - **Based on Geometric Feature**：使新坐标系原点与所选未变形几何特征的中心重合。有效特征包括曲面、线和点。从可视化窗格中选择一个特征，然后单击 **Use Selected Feature** 以确认原点的位置。原点位置的名称显示在此选项下方的字段中。
- 要定义自定义坐标系的方向，请在 **Frame Axes** 部分下，选择自定义坐标系的 **Primary Axis** 和 **Secondary Axis**，然后指定其方向。

  使用以下方法选择用于指定主轴和副轴方向的向量。主轴平行于所选向量，并将其余两个轴约束到其法平面。副轴平行于所选向量在法平面上的投影。

  - **Along Reference Frame Axis**：选择未变形梁的参考坐标系的一个轴。
  - **Based on Geometric Feature**：选择与未变形梁的所选几何特征关联的向量。有效特征包括曲面和线。对应向量在可视化窗格中由白色箭头指示。您可以从可视化窗格中选择一个特征，然后单击 **Use Selected Feature** 以确认选择。所选特征的名称显示在此选项下方的字段中。

### **FrameN** — 编辑或删除现有自定义坐标系的名称

您已创建的坐标系。`N` 是每个自定义坐标系的唯一标识编号。

- 单击文本字段以编辑现有自定义坐标系的名称。
- 单击 Edit 按钮 Edit 以编辑自定义坐标系的其他方面，例如原点和轴。
- 单击 Delete 按钮 Delete 以删除自定义坐标系。

#### 依赖关系

要使此参数可用，请通过单击 **New Frame** 创建坐标系。

## 所属库

Simscape / Multibody / Body Elements / Flexible Bodies / Beams

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

用于变形的具有弹性属性的角梁

Flexible Angle Beam 模块对具有 L 形横截面的细长梁（也称为 L 梁）进行建模。L 梁由一个水平分量和一个垂直分量组成，这两个分量称为梁腿。L 梁可以具有小的线性变形。这些变形包括拉伸、弯曲和扭转。该模块根据您指定的几何和材料属性计算梁的横截面特性，例如轴向刚度、抗弯刚度和抗扭刚度。

L 梁的几何形状是其横截面的拉伸。梁的横截面定义在 *xy* 平面中，并沿 *z* 轴拉伸。要定义横截面，您可以在模块对话框的 **Geometry** 部分中指定其尺寸。该图显示了 L 梁及其横截面。梁的参考坐标系位于两个梁腿中平面交线的中点。

有关对柔性梁建模的详细信息，请参阅 Overview of Flexible Beams。
