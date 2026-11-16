---
type: simulink-block
title: 'Flexible T Beam'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Body Elements / Flexible Bodies / Beams'
documentation_page: 'flexibletbeam'
documentation_source_path: 'ref/flexibletbeam.html'
language: zh-CN
chinese_source: worker-translation
---

# Flexible T Beam

## 端口

### 坐标系

### **A** — 连接坐标系 frame

用于在模型中连接梁的坐标系。在未变形配置中，该坐标系位于相对于局部参考坐标系原点的 -*z* 方向上、梁长度的一半处。

### **B** — 连接坐标系 frame

用于在模型中连接梁的坐标系。在未变形配置中，该坐标系位于相对于局部参考坐标系原点的 +*z* 方向上、梁长度的一半处。

### **R** — 参考坐标系 frame

表示柔性体整体刚体运动的虚拟未变形体的参考坐标系。**R** 坐标系并不物理连接到柔性体。

**R** 端口不得与任何施加力和力矩或具有惯性的模块刚性连接。

## 参数

### 几何

### **End-to-End Height** — 从法兰顶面到腹板底端的距离 1 `m` (default) | positive scalar

从法兰顶面到腹板底端的距离。`End-to-End Height` 也称为梁深度。

**注意**

**End-to-End Height** 必须大于 **Flange Thickness**。

### **Web Thickness** — 腹板两个面之间的距离 0.1 `m` (default) | positive scalar

腹板两个面之间的距离。

**注意**

**Web Thickness** 必须小于 **Flange Width**。

### **Flange Width** — 法兰两端之间的距离 0.5 `m` (default) | positive scalar

法兰两端之间的距离。

### **Flange Thickness** — 法兰两个面之间的距离 0.1 `m` (default) | positive scalar

法兰两个面之间的距离。

### **Length** — 梁的拉伸长度 10 `m` (default) | positive scalar

梁的拉伸长度。梁通过沿局部参考坐标系的 *z* 轴拉伸指定的横截面来建模。拉伸关于 *xy* 平面对称，梁的一半沿 *z* 轴负方向拉伸，另一半沿正方向拉伸。

### 刚度和惯性

### **Type** — 用于指定刚度和惯性属性的方法 `Calculate from Geometry` (default) | `Custom`

用于指定刚度和惯性属性的方法，指定为 `Calculate from Geometry` 或 `Custom`。当将该参数设置为 `Calculate from Geometry` 时，模块根据指定的密度、杨氏模量和泊松比或剪切模量计算刚度和惯性属性。将参数设置为 `Custom` 可手动指定刚度和惯性属性。

### **Density** — 材料单位体积的质量 2700 `kg/m^3` (default) | positive scalar

材料单位体积的质量——此处假定在梁内均匀分布。默认值对应于铝。

#### 依赖项

要启用此参数，请在**刚度和惯性**部分将 **Type** 参数设置为 `Calculate from Geometry`。

### **Specify** — 用于参数化梁的弹性属性 `Young's Modulus and Poisson's Ratio` (default) | `Young's and Shear Modulus`

用于参数化梁的弹性属性。这些属性通常可从材料数据库中获得。

#### 依赖项

要启用此参数，请在**刚度和惯性**部分将 **Type** 参数设置为 `Calculate from Geometry`。

### **Young's Modulus** — 轴向应力与轴向应变之比 70 `GPa` (default) | positive scalar

梁的杨氏弹性模量。其值越大，对弯曲和轴向变形的抵抗越强。默认值对应于铝。

#### 依赖项

要启用此参数，请在**刚度和惯性**部分将 **Type** 参数设置为 `Calculate from Geometry`。

### **Poisson's Ratio** — 横向应变与纵向应变之比 0.33 (default) | scalar in the range [0, 0.5)

梁的泊松比。指定值必须大于或等于 `0` 且小于 `0.5`。默认值对应于铝。

#### 依赖项

要启用此参数，请在**刚度和惯性**部分将 **Type** 参数设置为 `Calculate from Geometry`，并将 **Specify** 参数设置为 **Young's Modulus and Poisson's Ratio**。

### **Shear Modulus** — 剪应力与工程剪应变之比 26 `GPa` (default) | positive scalar

梁的剪切模量（或刚性模量）。其值越大，对扭转变形的抵抗越强。默认值对应于铝。

#### 依赖项

要启用此参数，请在**刚度和惯性**部分将 **Type** 参数设置为 `Calculate from Geometry`，并将 **Specify** 参数设置为 **Young's and Shear Modulus**。

### **Derived Values** — 质量和刚度截面属性的计算值按钮

梁的质量和刚度截面属性的计算值。单击 **Update** 以计算并显示这些值。

给出的属性包括 **质心** 和 **剪切中心**。质心是轴向力使梁伸长（或缩短）而不发生弯曲的点。剪切中心是横向力必须通过该点才能使梁弯曲而不发生扭转的点。

刚度截面属性计算如下：

- **轴向刚度**：*E**A*
- **弯曲刚度**：[*E**I*x,
  *E**I*y]
- **交叉弯曲刚度**：*E**I*xy
- **扭转刚度**：*G**J*

质量截面属性计算如下：

- **单位长度质量**：*ρ**A*
- **质量惯性矩密度**：[*ρ**I*x, *ρ**I*y]
- **质量惯性积密度**：*ρ**I*xy
- **极质量惯性矩密度**：*ρ**I*p

方程参数包括：

- *A* — 横截面积
- *ρ* — 密度
- *E* — 杨氏模量
- *G* — 剪切模量
- *J* — 扭转常数（通过求解 Saint-Venant 翘曲偏微分方程获得）

其余参数是梁的相关面积矩。这些矩是相对于形心坐标系的轴计算的——该坐标系与局部参考坐标系对齐，但其原点位于形心。面积矩为：

- *I*x,
  *I*y — 形心二次面积矩：
  [Ix,Iy]=[∫A(y−yc)2dA,∫A(x−xc)2dA],
- *I*xy — 形心面积积：
  Ixy=∫A(x−xc)(y−yc)dA,
- *I*p — 形心极面积矩：
  IP=Ix+Iy,

其中 *x*c 和 *y*c 是形心的坐标。

### **Geometric Centroid** — 梁横截面的形心 [0 0] `m` (default) | 2-by-1 array

梁横截面的形心，指定为 2×1 数组。该数组指定形心相对于梁参考坐标系的 *x* 和 *y* 坐标。

#### 依赖项

要启用此参数，请在**刚度和惯性**部分将 **Type** 设置为 `Custom`。

### **Bending Centroid** — 中性轴与横截面的交点 [0 0] `m` (default) | 2-by-1 array

中性轴与横截面的交点，指定为 2×1 数组。该数组指定形心相对于梁参考坐标系的 *x* 和 *y* 坐标。

#### 依赖项

要启用此参数，请在**刚度和惯性**部分将 **Type** 设置为 `Custom`。

### **Shear Center** — 梁剪切中心 [0 0] `m` (default) | 2-by-1 array

梁剪切中心，指定为 2×1 数组。该数组指定该点相对于梁参考坐标系的 *x* 和 *y* 坐标。

#### 依赖项

要启用此参数，请在**刚度和惯性**部分将 **Type** 设置为 `Custom`。

### **Axial Rigidity** — 对轴向变形的抵抗 1 `Pa*m^2` (default) | scalar

对沿梁纵向变形的抵抗，指定为标量。此参数指定刚度矩阵的 Sb 元素。

#### 依赖项

要启用此参数，请在**刚度和惯性**部分将 **Type** 设置为 `Custom`。

### **Flexural Rigidity** — 对弯曲变形的抵抗 [1 1] `Pa*m^4` (default) | 2-by-1 array

对弯曲变形的抵抗，指定为 2×1 数组。该数组指定刚度矩阵的 Hxb 和 Hyb 元素。

#### 依赖项

要启用此参数，请在**刚度和惯性**部分将 **Type** 设置为 `Custom`。

### **Cross Flexural Rigidity** — 对绕 *x* 轴的弯曲变形的抵抗，该变形由绕 *y* 轴的弯矩引起 0 `Pa*m^4` (default) | scalar

对绕 *x* 轴的弯曲变形的抵抗，该变形由绕 *y* 轴的弯矩引起，指定为标量。此参数指定刚度矩阵的 Hxyb 元素。

#### 依赖项

要启用此参数，请在**刚度和惯性**部分将 **Type** 设置为 `Custom`。

### **Torsional Rigidity** — 对扭转的抵抗 1 `Pa*m^4` (default) | scalar

对绕梁纵轴扭转的抵抗，指定为标量。此参数指定刚度矩阵的 Hzb 元素。

#### 依赖项

要启用此参数，请在**刚度和惯性**部分将 **Type** 设置为 `Custom`。

### **Center of Mass** — 质心 [0 0] `m` (default) | 2-by-1 array

质心，指定为 2×1 数组。该数组指定该点相对于梁参考坐标系的 *x* 和 *y* 坐标。

#### 依赖项

要启用此参数，请在**刚度和惯性**部分将 **Type** 设置为 `Custom`。

### **Mass Per Unit Length** — 单位长度质量 1 `kg/m` (default) | scalar

单位长度质量，指定为标量。此参数指定质量矩阵的 mc 元素。

#### 依赖项

要启用此参数，请在**刚度和惯性**部分将 **Type** 设置为 `Custom`。

### **Mass Moment of Inertia Density** — 对绕 `x` 和 `y` 轴旋转的抵抗 [1 1] `kg*m` (default) | 2-by-1 array

对绕 `x` 和 `y` 轴旋转的抵抗，指定为 2×1 数组。该数组指定质量矩阵的 ixc 和 iyc 元素。

#### 依赖项

要启用此参数，请在**刚度和惯性**部分将 **Type** 设置为 `Custom`。

### **Mass Product of Inertia Density** — 对由绕 `y` 轴的力矩引起的绕 `x` 轴旋转的抵抗 0 `kg*m` (default) | scalar

对由绕 `y` 轴的力矩引起的绕 `x` 轴旋转的抵抗，指定为标量。此参数指定质量矩阵的 ixyc 元素。

#### 依赖项

要启用此参数，请在**刚度和惯性**部分将 **Type** 设置为 `Custom`。

### 阻尼

### **Type** — 阻尼方法的类型 `Proportional` (default) | `Uniform Modal` | `None`

要应用于梁的阻尼方法：

- 选择 `None` 可对无阻尼梁建模。
- 选择 `Proportional` 可应用比例（或 Rayleigh）阻尼方法。此方法将阻尼矩阵 [*C*] 定义为质量矩阵 [*M*] 和刚度矩阵 [*K*] 的线性组合：

  [C]=α[M]+β[K],

  其中 *α* 和 *β* 是标量系数。
- 选择 `Uniform Modal` 可应用均匀模态阻尼方法。此方法对梁的所有振动模式应用单一阻尼比。该值越大，振动衰减越快。

  所选的参考条件会影响阻尼比所适用的模式类型。有关参考条件的详细信息，请参阅参考条件。当对柔性体使用模态降阶时，仅保留模式的一个子集。有关模态降阶的详细信息，请参阅 Reduce the Degrees of Freedom for a Flexible Body。

### **Mass Coefficient** — 质量矩阵的系数 0 `1/s` (default) | nonnegative scalar

质量矩阵的系数 *α*。此参数定义与质量矩阵 [*M*] 成比例的阻尼。

#### 依赖项

要启用此参数，请将 **Type** 设置为 `Proportional`。

### **Stiffness Coefficient** — 刚度矩阵的系数 0.001 `s` (default) | nonnegative scalar

刚度矩阵的系数 *β*。此参数定义与刚度矩阵 [*K*] 成比例的阻尼。

#### 依赖项

要启用此参数，请将 **Type** 设置为 `Proportional`。

### **Damping Ratio** — 均匀模态阻尼方法的阻尼比 0.01 (default) | unitless nonnegative scalar

应用于均匀模态阻尼模型中所有梁振动模式的阻尼比 *ζ*。该值越大，梁振动衰减越快。

当 *ζ* = 0 时，梁无阻尼。如果施加到梁上的边界条件与所选参考条件完全匹配，则 *ζ* < 1 会产生欠阻尼模态衰减，*ζ* = 1 对应于临界阻尼，*ζ* > 1 会产生过阻尼耗散。当边界条件和参考条件不匹配时，所选阻尼比的效果会变化。有关参考条件的详细信息，请参阅参考条件。

#### 依赖项

要启用此参数，请将 **Type** 设置为 `Uniform Modal`。

### 离散化

### **Number of Elements** — 梁有限元数量 1 (default) | positive integer

梁模型中的有限元数量。增加单元数量总能提高仿真精度。但实际上，当单元数量很多时，精度的提高会变得可以忽略。此外，更多的单元会增加计算成本并降低仿真速度。

### 参考条件

### **Type** — 参考条件类型 `Linearized Mean Axes` (default) | `Body-Fixed`

指定要应用的参考条件类型。有关详细信息，请参阅参考条件。

- `Linearized Mean Axes`：参考体坐标系跟随瞬时质心，柔性体表现出无约束的变形振动模式。
- `Body-Fixed`：选择固连于体的坐标系作为参考体坐标系。柔性体的变形表现出自由振动模态形状，在参考体坐标系位置处的平移和旋转变形为零。

### **Frame** — 用于 body-fixed 参考条件的连接坐标系名称

输入用作参考体坐标系的连接坐标系的名称。坐标系名称区分大小写。确保所选坐标系作为端口暴露在模块上。不能使用 **R** 坐标系，它是虚拟未变形体的参考坐标系。

#### 依赖项

要启用此参数，请将 **Type** 设置为 `Body-Fixed`。

### **Show Port R** — 显示参考坐标系端口 off (default) | on

选择此项可暴露 **R** 端口，该端口表示虚拟未变形体的参考坐标系。请注意，**R** 坐标系并不物理连接到柔性体。

**R** 端口不得与任何施加力和力矩或具有惯性的模块刚性连接。

### 保真度

### **Reduction** — 对柔性体建模的方法 `None` (default) | `Modally Reduced`

用于对柔性体建模的方法，指定为 `None` 或 `Modally Reduced`。将参数设置为 `None` 可使用有限元法生成的完整节点弹性坐标，或将参数设置为 `Modally Reduced` 可使用模态变换方法减少体的弹性坐标。对于这两种设置，模块都使用浮动参考系公式 [1-2] 将体与其弹性变形耦合。

### **Number of Retained Modes** — 保留模式 1 (default) | nonnegative integer

保留模式，指定为范围 [0, *n*] 内的整数，其中 *n* 是体的弹性自由度数量。如果将数量设置为 0，则柔性体被视为刚体。

#### 依赖项

要启用此参数，请将 **Reduction** 设置为 `Modally Reduced`。

### 图形

### **Type** — 用于梁可视化的图形 `From Geometry`（默认） | `None`

梁的视觉表示类型，指定为 `From Geometry` 或 `None`。将参数设置为 `From Geometry` 可显示梁的视觉表示。将参数设置为 `None` 可在模型可视化中隐藏梁。

### **Visual Properties** — 颜色和不透明度的参数化方式 `Simple`（默认） | `Advanced`

用于指定视觉属性的参数化方式。选择 `Simple` 可指定 **Color** 和 **Opacity**。选择 `Advanced` 可指定更多视觉属性，例如 **Specular Color**、**Ambient Color**、**Emissive Color** 和 **Shininess**。

#### 依赖项

要启用此参数，请将 **Type** 设置为 `From Geometry`。

### **Color** — 漫反射产生的光的颜色 [0.5 0.5 0.5]（默认） | 值在 0 到 1 范围内的 3-by-1 或 1-by-3 向量 | 值在 0 到 1 范围内的 4-by-1 或 1-by-4 向量

直接白光下图形的颜色，指定为 0–1 范围内的 [R G B] 或 [R G B A] 向量。可选的第四个元素 (A) 指定 0–1 范围内的颜色不透明度。省略不透明度元素等效于指定值 1。

#### 依赖项

要启用此参数，请设置：

1. 将 **Type** 设置为 `From Geometry`
2. 将 **Visual Properties** 设置为 `Simple`

### **Opacity** — 图形不透明度 1.0（默认） | 0 到 1 范围内的标量

图形不透明度，指定为 0 到 1 范围内的标量。标量 0 表示完全透明，标量 1 表示完全不透明。

#### 依赖项

要启用此参数，请设置：

1. 将 **Type** 设置为 `From Geometry`
2. 将 **Visual Properties** 设置为 `Simple`

### **Diffuse Color** — 漫反射产生的光的颜色 [0.5 0.5 0.5]（默认） | 值在 0 到 1 范围内的 3-by-1 或 1-by-3 向量 | 值在 0 到 1 范围内的 4-by-1 或 1-by-4 向量

漫反射产生的光的颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

漫反射颜色反映所渲染梁的主要颜色，并提供阴影，使所渲染对象呈现三维外观。

#### 依赖项

要启用此参数，请设置：

1. 将 **Type** 设置为 `From Geometry`
2. 将 **Visual Properties** 设置为 `Advanced`

### **Specular Color** — 镜面反射产生的光的颜色 [0.5 0.5 0.5 1.0]（默认） | 值在 0 到 1 范围内的 3-by-1 或 1-by-3 向量 | 值在 0 到 1 范围内的 4-by-1 或 1-by-4 向量

镜面反射产生的光的颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。此参数更改镜面高光的颜色，镜面高光是由于光源的光反射而在所渲染梁上形成的亮斑。

#### 依赖项

要启用此参数，请设置：

1. 将 **Type** 设置为 `From Geometry`
2. 将 **Visual Properties** 设置为 `Advanced`

### **Ambient Color** — 环境光的颜色 [0.15 0.15 0.15 1.0]（默认） | 值在 0 到 1 范围内的 3-by-1 或 1-by-3 向量 | 值在 0 到 1 范围内的 4-by-1 或 1-by-4 向量

环境光的颜色，指定为值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

环境光指的是并非直接来自光源的一般照明水平。环境光是已经反射并再次反射多次，以至于不再来自任何特定方向的光。您可以调整此参数来更改所渲染梁的阴影颜色。

#### 依赖项

要启用此参数，请设置：

1. 将 **Type** 设置为 `From Geometry`
2. 将 **Visual Properties** 设置为 `Advanced`

### **Emissive Color** — 自发光颜色 [0.0 0.0 0.0 1.0]（默认） | 值在 0 到 1 范围内的 3-by-1 或 1-by-3 向量

由于自发光产生的颜色，指定为 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

发射颜色是不来自任何外部来源的颜色，因此看起来是由梁自身发出的。当梁具有发射颜色时，即使没有外部光源，也可以看到该梁。

#### 依赖项

要启用此参数，请设置：

1. 将 **Type** 设置为 `From Geometry`
2. 将 **Visual Properties** 设置为 `Advanced`

### **Shininess** — 高光锐度 75（默认） | 值限制在 0–128 范围内的标量

镜面光反射的锐度，指定为 0–128 范围内的标量数值。
增大 shininess 值可获得更小但更锐利的高光。减小该值可获得更大但更平滑的高光。

#### 依赖项

要启用此参数，请设置：

1. 将 **Type** 设置为 `From Geometry`
2. 将 **Visual Properties** 设置为 `Advanced`

### 坐标系

### **Show Port A** — 显示用于连接到其他模块的端口 A on（默认） | off

选择此项可公开 **A** 端口。

### **Show Port B** — 显示用于连接到其他模块的端口 B on（默认） | off

选择此项可公开 **B** 端口。

### **New Frame** — 创建用于连接到其他模块的自定义坐标系的按钮

单击 Create 按钮 Create 以打开用于创建新的实体附加坐标系的窗格。在此窗格中，可以指定该坐标系的名称、原点和方向。

- 要为自定义坐标系命名，请单击 **Frame Name** 参数的文本字段。该名称标识梁模块上的相应端口，以及 Multibody Explorer 的树视图窗格中的相应端口。
- 要为自定义坐标系选择 **Frame Origin**，请使用以下方法之一：

  - **At Reference Frame Origin**：使新坐标系原点与未变形梁的参考坐标系原点重合。
  - **Based on Geometric Feature**：使新坐标系原点与所选未变形几何特征的中心重合。有效特征包括曲面、线和点。从可视化窗格中选择一个特征，然后单击 **Use Selected Feature** 以确认原点的位置。原点位置的名称将显示在此选项下方的字段中。

- 要定义自定义坐标系的方向，请在 **Frame Axes** 部分下，选择自定义坐标系的 **Primary Axis** 和 **Secondary Axis**，然后指定它们的方向。

  使用以下方法选择用于指定主轴和副轴方向的向量。主轴平行于所选向量，并将其余两个轴约束到其法平面。副轴平行于所选向量在法平面上的投影。

  - **Along Reference Frame Axis**：选择未变形梁的参考坐标系的一个轴。
  - **Based on Geometric Feature**：选择与未变形梁的所选几何特征关联的向量。有效特征包括曲面和线。相应向量在可视化窗格中由白色箭头指示。您可以从可视化窗格中选择一个特征，然后单击 **Use Selected Feature** 以确认选择。所选特征的名称将显示在此选项下方的字段中。

### **FrameN** — 编辑或删除现有自定义坐标系名称

您已创建的坐标系。`N` 是每个自定义坐标系的唯一标识编号。

- 单击文本字段以编辑现有自定义坐标系的名称。
- 单击 Edit 按钮 Edit 以编辑自定义坐标系的其他方面，例如原点和轴。
- 单击 Delete 按钮 Delete 以删除自定义坐标系。

#### 依赖项

要启用此参数，请通过单击 **New Frame** 创建坐标系。

## 所属库

Simscape / Multibody / Body Elements / Flexible Bodies / Beams

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

具有用于变形的弹性特性的 T 形梁

Flexible T Beam 模块对具有 T 形横截面的细长梁（也称为 T 形梁）进行建模。T 形梁由一个水平部件（称为翼缘）和一个垂直部件（称为腹板）组成。T 形梁可以具有小的线性变形。这些变形包括拉伸、弯曲和扭转。该模块根据您指定的几何和材料属性计算梁的横截面特性，例如轴向刚度、弯曲刚度和扭转刚度。

T 形梁的几何形状是其横截面的拉伸。梁的横截面在 *xy* 平面中定义，并沿 *z* 轴拉伸。要定义横截面，您可以在模块对话框的 **Geometry** 部分中指定其尺寸。图中显示了 T 形梁及其横截面。梁的参考坐标系位于腹板和翼缘中平面的交线的中点处。

有关对柔性梁建模的详细信息，请参阅柔性梁概述。
