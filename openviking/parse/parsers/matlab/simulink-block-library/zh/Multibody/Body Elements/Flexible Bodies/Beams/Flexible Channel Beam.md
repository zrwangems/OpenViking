---
type: simulink-block
title: 'Flexible Channel Beam'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Body Elements / Flexible Bodies / Beams'
documentation_page: 'flexiblechannelbeam'
documentation_source_path: 'ref/flexiblechannelbeam.html'
language: zh-CN
chinese_source: worker-translation
---

# Flexible Channel Beam

## 端口

### 坐标系

### **A** — 连接坐标系 frame

用于在模型中连接梁的坐标系。在未变形配置中，该坐标系相对于局部参考坐标系的原点位于 -*z* 方向上半梁长度处。

### **B** — 连接坐标系 frame

用于在模型中连接梁的坐标系。在未变形配置中，该坐标系相对于局部参考坐标系的原点位于 +*z* 方向上半梁长度处。

### **R** — 参考坐标系 frame

虚拟未变形体的参考坐标系，其表示柔性体的整体刚体运动。**R** 坐标系不物理连接于柔性体。

**R** 端口不得与任何施加力和力矩或具有惯性的模块刚性连接。

## 参数

### 几何

### **End-to-End Height** — 法兰外表面之间的距离 1 `m` (默认) | positive scalar

两个法兰外表面之间的距离。`End-to-End Height` 也称为梁深度。

**注意**

`End-to-End Height` 必须大于两个法兰厚度之和。

### **Web Thickness** — 腹板两表面之间的距离 0.1 `m` (默认) | positive scalar

腹板两个表面之间的距离。

**注意**

`Web Thickness` 必须小于翼缘的宽度。

### **Top Flange Width** — 上翼缘两端之间的距离 0.5 `m` (默认) | positive scalar

上翼缘两端之间的距离。

### **Top Flange Thickness** — 上翼缘两表面之间的距离 0.1 `m` (默认) | positive scalar

上翼缘两个表面之间的距离。

### **Bottom Flange Width** — 下翼缘两端之间的距离 0.5 `m` (默认) | positive scalar

下翼缘两端之间的距离。

### **Bottom Flange Thickness** — 下翼缘两表面之间的距离 0.1 `m` (默认) | positive scalar

下翼缘两个表面之间的距离。

### **Length** — 梁的挤出长度 10 `m` (默认) | positive scalar

梁的挤出长度。梁通过沿局部参考坐标系的 *z* 轴挤出指定横截面来建模。挤出关于 *xy* 平面对称，梁的一半沿 *z* 轴负方向挤出，另一半沿正方向挤出。

### 刚度和惯性

### **Type** — 用于指定刚度和惯性属性的方法 `Calculate from Geometry` (默认) | `Custom`

用于指定刚度和惯性属性的方法，指定为 `Calculate from Geometry` 或 `Custom`。

当将该参数设置为 `Calculate from Geometry` 时，模块根据指定的密度、Young's modulus 和 Poisson's ratio 或 shear modulus 计算刚度和惯性属性。将参数设置为 `Custom` 可手动指定刚度和惯性属性。

### **Density** — 材料单位体积质量 2700 `kg/m^3` (默认) | positive scalar

材料单位体积质量——此处假设在梁内均匀分布。默认值对应于铝。

#### 依赖项

要启用此参数，请在 **Stiffness and Inertia** 部分将 **Type** 参数设置为 `Calculate from Geometry`。

### **Specify** — 用于对梁进行参数化的弹性属性 `Young's Modulus and Poisson's Ratio` (默认) | `Young's and Shear Modulus`

用于对梁进行参数化的弹性属性。这些属性通常可从材料数据库中获得。

#### 依赖项

要启用此参数，请在 **Stiffness and Inertia** 部分将 **Type** 参数设置为 `Calculate from Geometry`。

### **Young's Modulus** — 轴向应力与轴向应变之比 70 `GPa` (默认) | positive scalar

梁的杨氏弹性模量。其值越大，抗弯曲和轴向变形的能力越强。默认值对应于铝。

#### 依赖项

要启用此参数，请在 **Stiffness and Inertia** 部分将 **Type** 参数设置为 `Calculate from Geometry`。

### **Poisson's Ratio** — 横向应变与纵向应变之比 0.33 (默认) | scalar in the range [0, 0.5)

梁的泊松比。指定值必须大于或等于 `0` 且小于 `0.5`。默认值对应于铝。

#### 依赖项

要启用此参数，请在 **Stiffness and Inertia** 部分将 **Type** 参数设置为 `Calculate from Geometry`，并将 **Specify** 参数设置为 **Young's Modulus and Poisson's Ratio**。

### **Shear Modulus** — 剪应力与工程剪应变之比 26 `GPa` (默认) | positive scalar

梁的剪切模量（或刚性模量）。其值越大，抗扭转变形的能力越强。默认值对应于铝。

#### 依赖项

要启用此参数，请在 **Stiffness and Inertia** 部分将 **Type** 参数设置为 `Calculate from Geometry`，并将 **Specify** 参数设置为 **Young's and Shear Modulus**。

### **Derived Values** — 梁的质量和刚度截面特性的计算值 button

梁的质量和刚度截面特性的计算值。单击 **Update** 可计算并显示这些值。

给出的属性包括 **Centroid** 和 **Shear Center**。质心是轴向力使梁伸长（或缩短）而不产生弯曲的点。剪切中心是横向力必须通过以使梁弯曲而不扭转的点。

刚度截面特性计算如下：

- **Axial Rigidity**：*E**A*
- **Flexural Rigidity**：[*E**I*x, *E**I*y]
- **Cross Flexural Rigidity**：*E**I*xy
- **Torsional Rigidity**：*G**J*

质量截面特性计算如下：

- **Mass per Unit Length**：*ρ**A*
- **Mass Moment of Inertia Density**：[*ρ**I*x, *ρ**I*y]
- **Mass Product of Inertia Density**：*ρ**I*xy
- **Polar Mass Moment of Inertia Density**：*ρ**I*p

方程参数包括：

- *A* — 横截面积
- *ρ* — 密度
- *E* — Young's modulus
- *G* — Shear modulus
- *J* — 扭转常数（由 Saint-Venant 翘曲偏微分方程的解得到）

其余参数是梁的相关面积矩。这些面积矩围绕形心坐标系的轴计算——该坐标系与局部参考坐标系对齐，但其原点位于形心。面积矩为：

- *I*x, *I*y — 形心惯性矩：

  [Ix,Iy]=[∫A(y−yc)2dA,∫A(x−xc)2dA],
- *I*xy — 形心惯性积：

  Ixy=∫A(x−xc)(y−yc)dA,
- *I*p — 形心极惯性矩：

  IP=Ix+Iy,

其中 *x*c 和 *y*c 是形心的坐标。

### **Geometric Centroid** — 梁横截面的形心 [0 0] `m` (默认) | 2-by-1 array

梁横截面的形心，指定为 2-by-1 array。该数组指定形心相对于梁参考坐标系的 *x* 和 *y* 坐标。

#### 依赖项

要启用此参数，请在 **Stiffness and Inertia** 部分将 **Type** 设置为 `Custom`。

### **Bending Centroid** — 中性轴与横截面的交点 [0 0] `m` (默认) | 2-by-1 array

中性轴与横截面的交点，指定为 2-by-1 array。该数组指定形心相对于梁参考坐标系的 *x* 和 *y* 坐标。

#### 依赖项

要启用此参数，请在 **Stiffness and Inertia** 部分将 **Type** 设置为 `Custom`。

### **Shear Center** — 梁的剪切中心 [0 0] `m` (默认) | 2-by-1 array

梁的剪切中心，指定为 2-by-1 array。该数组指定该点相对于梁参考坐标系的 *x* 和 *y* 坐标。

#### 依赖项

要启用此参数，请在 **Stiffness and Inertia** 部分将 **Type** 设置为 `Custom`。

### **Axial Rigidity** — 抗轴向变形能力 1 `Pa*m^2` (默认) | scalar

抵抗沿梁纵向变形的能力，指定为 scalar。此参数指定刚度矩阵的 Sb 元素。

#### 依赖项

要启用此参数，请在 **Stiffness and Inertia** 部分将 **Type** 设置为 `Custom`。

### **Flexural Rigidity** — 抗弯曲变形能力 [1 1] `Pa*m^4` (默认) | 2-by-1 array

抵抗弯曲变形的能力，指定为 2-by-1 array。该数组指定刚度矩阵的 Hxb 和 Hyb 元素。

#### 依赖项

要启用此参数，请在 **Stiffness and Inertia** 部分将 **Type** 设置为 `Custom`。

### **Cross Flexural Rigidity** — 抵抗由绕 y 轴的弯矩引起的绕 x 轴弯曲变形 0 `Pa*m^4` (默认) | scalar

抵抗由绕 *y* 轴的弯矩引起的绕 *x* 轴弯曲变形，指定为 scalar。此参数指定刚度矩阵的 Hxyb 元素。

#### 依赖项

要启用此参数，请在 **Stiffness and Inertia** 部分将 **Type** 设置为 `Custom`。

### **Torsional Rigidity** — 抗扭转能力 1 `Pa*m^4` (默认) | scalar

抵抗绕梁纵轴扭转的能力，指定为 scalar。此参数指定刚度矩阵的 Hzb 元素。

#### 依赖项

要启用此参数，请在 **Stiffness and Inertia** 部分将 **Type** 设置为 `Custom`。

### **Center of Mass** — 质心 [0 0] `m` (默认) | 2-by-1 array

质心，指定为 2-by-1 array。该数组指定该点相对于梁参考坐标系的 *x* 和 *y* 坐标。

#### 依赖项

要启用此参数，请在 **Stiffness and Inertia** 部分将 **Type** 设置为 `Custom`。

### **Mass Per Unit Length** — 单位长度质量 1 `kg/m` (默认) | scalar

单位长度质量，指定为 scalar。此参数指定质量矩阵的 mc 元素。

#### 依赖项

要启用此参数，请在 **Stiffness and Inertia** 部分将 **Type** 设置为 `Custom`。

### **Mass Moment of Inertia Density** — 抵抗绕 `x` 和 `y` 轴旋转的能力 [1 1] `kg*m` (默认) | 2-by-1 array

抵抗绕 *x* 和 *y* 轴旋转的能力，指定为 2-by-1 array。该数组指定质量矩阵的 ixc 和 iyc 元素。

#### 依赖项

要启用此参数，请在 **Stiffness and Inertia** 部分将 **Type** 设置为 `Custom`。

### **Mass Product of Inertia Density** — 抵抗由绕 `y` 轴的力矩引起的绕 `x` 轴旋转的能力 0 `kg*m` (默认) | scalar

抵抗由绕 *y* 轴的力矩引起的绕 *x* 轴旋转的能力，指定为 scalar。此参数指定质量矩阵的 ixyc 元素。

#### 依赖项

要启用此参数，请在 **Stiffness and Inertia** 部分将 **Type** 设置为 `Custom`。

### 阻尼

### **Type** — 阻尼方法类型 `Proportional` (默认) | `Uniform Modal` | `None`

要应用于梁的阻尼方法：

- 选择 `None` 可对无阻尼梁建模。
- 选择 `Proportional` 可应用比例（或 Rayleigh）阻尼方法。此方法将阻尼矩阵 [*C*] 定义为质量矩阵 [*M*] 和刚度矩阵 [*K*] 的线性组合：

  [C]=α[M]+β[K],

  其中 *α* 和 *β* 是标量系数。
- 选择 `Uniform Modal` 可应用均匀模态阻尼方法。此方法对梁的所有振动模态应用单一阻尼比。该值越大，振动衰减越快。

  所选参考条件会影响阻尼比适用的模态类型。有关参考条件的详细信息，请参见参考条件。对柔性体使用模态缩减时，仅保留模态的子集。有关模态缩减的详细信息，请参阅 Reduce the Degrees of Freedom for a Flexible Body。

### **Mass Coefficient** — 质量矩阵系数 0 `1/s` (默认) | nonnegative scalar

质量矩阵的系数 *α*。此参数定义与质量矩阵 [*M*] 成比例的阻尼。

#### 依赖项

要启用此参数，请将 **Type** 设置为 `Proportional`。

### **Stiffness Coefficient** — 刚度矩阵系数 0.001 `s` (默认) | nonnegative scalar

刚度矩阵的系数 *β*。此参数定义与刚度矩阵 [*K*] 成比例的阻尼。

#### 依赖项

要启用此参数，请将 **Type** 设置为 `Proportional`。

### **Damping Ratio** — 均匀模态阻尼方法的阻尼比 0.01 (默认) | unitless nonnegative scalar

均匀模态阻尼模型中应用于所有梁振动模态的阻尼比 *ζ*。该值越大，梁振动衰减越快。

当 *ζ* = 0 时，梁无阻尼。如果施加到梁上的边界条件与所选参考条件完全匹配，则 *ζ* < 1 产生欠阻尼模态衰减，*ζ* = 1 对应于临界阻尼，*ζ* > 1 产生过阻尼耗散。当边界条件和参考条件不匹配时，所选阻尼比的效果会有所不同。有关参考条件的详细信息，请参见参考条件。

#### 依赖项

要启用此参数，请将 **Type** 设置为 `Uniform Modal`。

### 离散化

### **Number of Elements** — 梁有限元数量 1 (默认) | positive integer

梁模型中的有限元数量。增加单元数量总能提高仿真精度。但实际上，当单元很多时，精度提升在某个点后会变得可以忽略。此外，较多的单元会增加计算成本并降低仿真速度。

### 参考条件

### **Type** — 参考条件类型 `Linearized Mean Axes` (默认) | `Body-Fixed`

指定要应用的参考条件类型。有关详细信息，请参见参考条件。

- `Linearized Mean Axes`：参考体坐标系跟随瞬时质心，柔性体表现出无约束的变形振动模态。
- `Body-Fixed`：选择固连于体的坐标系作为参考体坐标系。柔性体的变形表现出自由振动模态振型，在参考体坐标系位置处具有零平移和旋转变形。

### **Frame** — 用于 body-fixed 参考条件的连接坐标系 frame name

输入要用作参考体坐标系的连接坐标系的名称。坐标系名称区分大小写。确保所选坐标系作为端口暴露在模块上。不能使用 **R** 坐标系，它是虚拟未变形体的参考坐标系。

#### 依赖项

要启用此参数，请将 **Type** 设置为 `Body-Fixed`。

### **Show Port R** — 显示参考坐标系端口 off (默认) | on

选择此项可暴露 **R** 端口，它表示虚拟未变形体的参考坐标系。请注意，**R** 坐标系不物理连接于柔性体。

**R** 端口不得与任何施加力和力矩或具有惯性的模块刚性连接。

### 保真度

### **Reduction** — 对柔性体建模的方法 `None` (默认) | `Modally Reduced`

用于对柔性体建模的方法，指定为 `None` 或 `Modally Reduced`。将参数设置为 `None` 可使用有限元方法生成的完整节点弹性坐标，或将参数设置为 `Modally Reduced` 可使用模态变换方法缩减体的弹性坐标。对于这两种设置，模块都使用浮动参考坐标系公式 [1-2] 将体与其弹性变形耦合。

### **Number of Retained Modes** — 保留模态 1 (默认) | nonnegative integer

保留模态，指定为范围 [0, *n*] 中的整数，其中
*n* 是体的弹性自由度数量。如果将数字设置为 0，则柔性体被视为刚体。

#### 依赖项

要启用此参数，请将 **Reduction** 设置为 `Modally Reduced`。

### 图形

### **Type** — 用于梁可视化的图形 `From Geometry` (默认) | `None`

梁的可视表示类型，指定为 `From Geometry` 或 `None`。将参数设置为 `From Geometry` 可显示梁的可视表示。将参数设置为 `None` 可在模型可视化中隐藏梁。

### **Visual Properties** — 颜色和不透明度的参数化选项 `Simple` (默认) | `Advanced`

用于指定可视属性的参数化选项。选择 `Simple` 可指定 **Color** 和 **Opacity**。选择 `Advanced` 可指定更多可视属性，例如 **Specular Color**、**Ambient Color**、**Emissive Color** 和 **Shininess**。

#### 依赖项

要启用此参数，请将 **Type** 设置为 `From Geometry`。

### **Color** — 漫反射产生的光颜色 [0.5 0.5 0.5] (默认) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

直接白光下图形的颜色，指定为 0–1 范围内的 [R G B] 或 [R G B A] 向量。可选的第四个元素 (A) 指定 0–1 范围内的颜色不透明度。省略不透明度元素等效于指定值 1。

#### 依赖项

要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Simple`

### **Opacity** — 图形不透明度 1.0 (默认) | scalar in the range of 0 to 1

图形不透明度，指定为 0 到 1 范围内的标量。标量 0 对应于完全透明，标量 1 对应于完全不透明。

#### 依赖项

要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Simple`

### **Diffuse Color** — 漫反射产生的光颜色 [0.5 0.5 0.5] (默认) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

漫反射产生的光颜色，指定为取值范围 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

漫反射颜色反映渲染梁的主要颜色，并提供阴影，使渲染对象具有三维外观。

#### 依赖项

要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Advanced`

### **Specular Color** — 镜面反射产生的光颜色 [0.5 0.5 0.5 1.0] (默认) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

镜面反射产生的光颜色，指定为取值范围 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。此参数更改镜面高光的颜色，镜面高光是由于光源的光反射而在渲染梁上出现的亮点。

#### 依赖项

要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Advanced`

### **Ambient Color** — 环境光颜色 [0.15 0.15 0.15 1.0] (默认) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1 | 4-by-1 or 1-by-4 vector with values in the range of 0 to 1

环境光颜色，指定为取值范围 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

环境光是指并非直接来自光源的一般照明水平。环境光是已经反射和重新反射许多次，以至于不再来自任何特定方向的光。您可以调整此参数以更改渲染梁的阴影颜色。

#### 依赖项

要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Advanced`

### **Emissive Color** — 自发光颜色 [0.0 0.0 0.0 1.0] (默认) | 3-by-1 or 1-by-3 vector with values in the range of 0 to 1

自发光产生的颜色，指定为取值范围 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

发射颜色是不来自任何外部来源的颜色，因此看起来是由梁本身发射的。当梁具有自发光颜色时，即使没有外部光源，也可以看到该梁。

#### 依赖项

要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Advanced`

### **Shininess** — 高光锐度 75 (默认) | scalar with value constrained to 0–128

镜面光反射的锐度，指定为 0–128 范围内的标量数值。
增大 shininess 值可获得更小但更锐利的高光。减小该值可获得更大但更平滑的高光。

#### 依赖项

要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Advanced`

### 坐标系

### **Show Port A** — 显示用于连接到其他模块的端口 A on (默认) | off

选择以显示 **A** 端口。

### **Show Port B** — 显示用于连接到其他模块的端口 B on (默认) | off

选择以显示 **B** 端口。

### **New Frame** — 创建用于连接到其他模块的自定义坐标系 按钮

单击 Create 按钮 Create 以打开一个窗格，用于创建新的
体附着坐标系。在此窗格中，可以为该坐标系指定名称、原点和
方向。

- 若要为自定义坐标系命名，请单击
  **Frame Name** 参数的文本字段。该名称标识
  梁模块上以及 Multibody Explorer 的树视图窗格
  中的对应端口。
- 若要为自定义坐标系选择 **Frame Origin**，请使用以下方法之一：

  - **At Reference Frame Origin**：使
    新坐标系原点与未变形梁的参考坐标系原点
    重合。
  - **Based on Geometric Feature**：使
    新坐标系原点与所选未变形几何特征的中心
    重合。有效特征包括曲面、线和点。从可视化窗格中
    选择一个特征，然后单击 **Use Selected Feature** 以确认
    原点的位置。原点位置的名称将出现在
    此选项下方的字段中。
- 若要定义自定义坐标系的方向，请在
  **Frame Axes** 部分下，选择
  **Primary Axis** 和 **Secondary Axis**
  自定义坐标系，然后指定其
  方向。

  使用以下方法选择用于指定主轴和次轴
  方向的向量。主轴平行于所选向量，并
  将其余两个轴约束到其法平面。次轴平行于
  所选向量在法平面上的投影。

  - **Along Reference Frame Axis**：
    选择未变形梁的参考坐标系的一个轴。
  - **Based on Geometric Feature**：
    选择与未变形梁的所选几何特征
    关联的向量。有效特征包括
    曲面和线。对应向量在可视化窗格中
    由白色箭头指示。可以从可视化窗格中选择一个特征，然后
    单击 **Use Selected Feature** 以确认选择。所选特征
    的名称将出现在此选项下方的字段中。

### **FrameN** — 编辑或删除现有自定义坐标系 坐标系名称

已创建的坐标系。`N` 是每个自定义坐标系的唯一标识
编号。

- 单击文本字段以编辑现有自定义
  坐标系的名称。

- 单击 Edit 按钮 Edit 以编辑自定义
  坐标系的其他方面，例如原点和轴。
- 单击 Delete 按钮 Delete 以删除自定义
  坐标系。

#### 依赖项

要启用此参数，请通过单击 **New Frame** 创建坐标系。

## 所属库

Simscape / Multibody / Body Elements / Flexible Bodies / Beams

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

用于变形的具有弹性特性的通道梁

Flexible Channel Beam 模块对具有
C 形横截面的细长梁（也称为 C-beam）进行建模。C-beam 由两个称为翼缘的水平
组件组成，这两个组件通过一个称为
腹板的垂直组件连接。C-beam 可以具有小的线性变形。这些变形包括拉伸、
弯曲和扭转。该模块根据您指定的几何和材料属性计算梁的横截面属性，例如
轴向刚度、抗弯刚度和抗扭刚度。

C-beam 的几何形状是其横截面的拉伸。梁横截面
定义在 *xy* 平面中，并沿 *z* 轴拉伸。要定义横截面，可以在模块对话框的 **Geometry** 部分中指定其尺寸。该图
显示了 C-beam 及其横截面。梁的参考坐标系位于
腹板的形心处。

有关对柔性梁建模的详细信息，请参阅 Overview of Flexible Beams。
