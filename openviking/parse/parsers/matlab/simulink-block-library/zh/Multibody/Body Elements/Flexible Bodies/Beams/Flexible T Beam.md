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
```yaml
ports:
- name: A
  summary: 连接框架 frame
  direction: unspecified
- name: B
  summary: 连接框架 frame
  direction: unspecified
- name: R
  summary: 参考框架 frame
  direction: unspecified
```

### 框架

### **A** — 连接框架 frame

用于在模型中连接该梁的框架。在未变形构型中，该框架位于相对于局部参考坐标系原点沿 -*z* 方向梁长度一半处。

### **B** — 连接框架 frame

用于在模型中连接该梁的框架。在未变形构型中，该框架位于相对于局部参考坐标系原点沿 +*z* 方向梁长度一半处。

### **R** — 参考框架 frame

虚拟未变形体的参考框架，表示柔性体的整体刚体运动。**R** 框架在物理上并不附着于柔性体。

**R** 端口不得与任何施加力和力矩或具有惯性的模块刚性连接。
## 参数
```yaml
parameters:
- name: End-to-End Height
  summary: 从翼缘顶面到腹板底端的距离 1 m（默认）| 正标量
  group: 几何
- name: Web Thickness
  summary: 腹板两面之间的距离 0.1 m（默认）| 正标量
  group: 几何
- name: Flange Width
  summary: 翼缘两端之间的距离 0.5 m（默认）| 正标量
  group: 几何
- name: Flange Thickness
  summary: 翼缘两面之间的距离 0.1 m（默认）| 正标量
  group: 几何
- name: Length
  summary: 梁的拉伸长度 10 m（默认）| 正标量
  group: 几何
- name: Type
  summary: 用于指定刚度和惯性属性的方法 Calculate from Geometry（默认）| Custom
  group: 刚度和惯性
- name: Density
  summary: 材料单位体积质量 2700 kg/m^3（默认）| 正标量
  group: 刚度和惯性
- name: Specify
  summary: 用于参数化梁的弹性属性 Young's Modulus and Poisson's Ratio（默认）| Young's and Shear Modulus
  group: 刚度和惯性
- name: Young's Modulus
  summary: 轴向应力与轴向应变之比 70 GPa（默认）| 正标量
  group: 刚度和惯性
- name: Poisson's Ratio
  summary: 横向应变与纵向应变之比 0.33（默认）| 范围 [0, 0.5) 内的标量
  group: 刚度和惯性
- name: Shear Modulus
  summary: 剪应力与工程剪应变之比 26 GPa（默认）| 正标量
  group: 刚度和惯性
- name: Derived Values
  summary: 质量和刚度截面特性的计算值 按钮
  group: 刚度和惯性
- name: Geometric Centroid
  summary: 梁横截面的形心 [0 0] m（默认）| 2×1 数组
  group: 刚度和惯性
- name: Bending Centroid
  summary: 中性轴与横截面的交点 [0 0] m（默认）| 2×1 数组
  group: 刚度和惯性
- name: Shear Center
  summary: 梁的剪切中心 [0 0] m（默认）| 2×1 数组
  group: 刚度和惯性
- name: Axial Rigidity
  summary: 抵抗轴向变形 1 Pa*m^2（默认）| 标量
  group: 刚度和惯性
- name: Flexural Rigidity
  summary: 抵抗弯曲变形 [1 1] Pa*m^4（默认）| 2×1 数组
  group: 刚度和惯性
- name: Cross Flexural Rigidity
  summary: 抵抗因绕 y 轴弯矩引起的绕 x 轴弯曲变形 0 Pa*m^4（默认）| 标量
  group: 刚度和惯性
- name: Torsional Rigidity
  summary: 抵抗扭转 1 Pa*m^4（默认）| 标量
  group: 刚度和惯性
- name: Center of Mass
  summary: 质心 [0 0] m（默认）| 2×1 数组
  group: 刚度和惯性
- name: Mass Per Unit Length
  summary: 单位长度质量 1 kg/m（默认）| 标量
  group: 刚度和惯性
- name: Mass Moment of Inertia Density
  summary: 抵抗绕 x 和 y 轴的旋转 [1 1] kg*m（默认）| 2×1 数组
  group: 刚度和惯性
- name: Mass Product of Inertia Density
  summary: 抵抗因绕 y 轴力矩引起的绕 x 轴旋转 0 kg*m（默认）| 标量
  group: 刚度和惯性
- name: Type
  summary: 阻尼方法类型 Proportional（默认）| Uniform Modal | None
  group: Damping
- name: Mass Coefficient
  summary: 质量矩阵系数 0 1/s（默认）| 非负标量
  group: Damping
- name: Stiffness Coefficient
  summary: 刚度矩阵系数 0.001 s（默认）| 非负标量
  group: Damping
- name: Damping Ratio
  summary: 均匀模态阻尼方法的阻尼比 0.01（默认）| 无量纲非负标量
  group: Damping
- name: Number of Elements
  summary: 梁有限元数量 1（默认）| 正整数
  group: 离散化
- name: Type
  summary: 参考条件类型 Linearized Mean Axes（默认）| Body-Fixed
  group: 参考条件
- name: Frame
  summary: 用于体固定参考条件的连接坐标系 坐标系名称
  group: 参考条件
- name: Show Port R
  summary: 显示参考坐标系端口 关闭（默认）| 开启
  group: 参考条件
- name: Reduction
  summary: 用于对柔性体建模的方法 None（默认）| Modally Reduced
  group: 保真度
- name: Number of Retained Modes
  summary: 保留模态数 1（默认）| 非负整数
  group: 保真度
- name: Type
  summary: 用于梁可视化显示的图形 From Geometry（默认）| None
  group: 图形
- name: Visual Properties
  summary: 颜色和不透明度的参数化方式 Simple（默认）| Advanced
  group: 图形
- name: Color
  summary: 漫反射光的颜色 [0.5 0.5 0.5]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量
  group: 图形
- name: Opacity
  summary: 图形不透明度 1.0（默认）| 取值范围为 0 到 1 的标量
  group: 图形
- name: Diffuse Color
  summary: 漫反射光的颜色 [0.5 0.5 0.5]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量
  group: 图形
- name: Specular Color
  summary: 由于镜面反射产生的光的颜色 [0.5 0.5 0.5 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量
  group: 图形
- name: Ambient Color
  summary: 环境光的颜色 [0.15 0.15 0.15 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量
  group: 图形
- name: Emissive Color
  summary: 自发光颜色 [0.0 0.0 0.0 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量
  group: 图形
- name: Shininess
  summary: 高光锐度 75（默认）| 取值约束为 0–128 的标量
  group: 图形
- name: Show Port A
  summary: 显示端口 A 以连接到其他模块 on（默认）| off
  group: Frames
- name: Show Port B
  summary: 显示端口 B 以连接到其他模块 on（默认）| off
  group: Frames
- name: New Frame
  summary: 创建自定义坐标系以连接到其他模块按钮
  group: Frames
- name: FrameN
  summary: 编辑或删除现有自定义坐标系坐标系名称
  group: Frames
```

### 几何

### **End-to-End Height** — 从翼缘顶面到腹板底端的距离 1 `m`（默认）| 正标量

从翼缘顶面到腹板底端的距离。`End-to-End Height` 也称为梁高。

**注意**

**End-to-End Height** 必须大于 **Flange Thickness**。

### **Web Thickness** — 腹板两面之间的距离 0.1 `m`（默认）| 正标量

腹板两面之间的距离。

**注意**

**Web Thickness** 必须小于 **Flange Width**。

### **Flange Width** — 翼缘两端之间的距离 0.5 `m`（默认）| 正标量

翼缘两端之间的距离。

### **Flange Thickness** — 翼缘两面之间的距离 0.1 `m`（默认）| 正标量

翼缘两面之间的距离。

### **Length** — 梁的拉伸长度 10 `m`（默认）| 正标量

梁的拉伸长度。该梁通过将指定横截面沿局部参考坐标系的 *z* 轴拉伸来建模。拉伸关于 *xy* 平面对称，梁的一半沿 *z* 轴负方向拉伸，另一半沿正方向拉伸。

### 刚度和惯性

### **Type** — 用于指定刚度和惯性属性的方法 `Calculate from Geometry`（默认）| `Custom`

用于指定刚度和惯性属性的方法，指定为 `Calculate from Geometry` 或 `Custom`。

当将该参数设置为 `Calculate from Geometry` 时，模块根据指定的密度、杨氏模量和泊松比或剪切模量计算刚度和惯性属性。将该参数设置为 `Custom` 以手动指定刚度和惯性属性。

### **Density** — 材料单位体积质量 2700 `kg/m^3`（默认）| 正标量

材料单位体积质量——此处假定在梁内均匀分布。默认值对应于铝。

#### 依赖关系

要启用此参数，请在 **Stiffness and Inertia** 部分下，将 **Type** 参数设置为 `Calculate from Geometry`。

### **Specify** — 用于参数化梁的弹性属性 `Young's Modulus and Poisson's Ratio`（默认）| `Young's and Shear Modulus`

用于参数化梁的弹性属性。这些属性通常可从材料数据库中获得。

#### 依赖关系

要启用此参数，请在 **Stiffness and Inertia** 部分下，将 **Type** 参数设置为 `Calculate from Geometry`。

### **Young's Modulus** — 轴向应力与轴向应变之比 70 `GPa`（默认）| 正标量

梁的杨氏弹性模量。其值越大，对弯曲和轴向变形的抵抗能力越强。默认值对应于铝。

#### 依赖关系

要启用此参数，请在 **Stiffness and Inertia** 部分下，将 **Type** 参数设置为 `Calculate from Geometry`。

### **Poisson's Ratio** — 横向应变与纵向应变之比 0.33（默认）| 范围 [0, 0.5) 内的标量

梁的泊松比。指定的值必须大于或等于 `0` 且小于 `0.5`。默认值对应于铝。

#### 依赖关系

要启用此参数，请在 **Stiffness and Inertia** 部分下，将 **Type** 参数设置为 `Calculate from Geometry`，并将 **Specify** 参数设置为 **Young's Modulus and Poisson's Ratio**。

### **Shear Modulus** — 剪应力与工程剪应变之比 26 `GPa`（默认）| 正标量

梁的剪切模量（或刚性模量）。其值越大，抵抗扭转变形的能力越强。默认值对应于铝。

#### 依赖关系

要启用此参数，请在 **Stiffness and Inertia** 部分下，将 **Type** 参数设置为 `Calculate from Geometry`，并将 **Specify** 参数设置为 **Young's and Shear Modulus**。

### **Derived Values** — 质量和刚度截面特性的计算值 按钮

梁的质量和刚度截面特性的计算值。点击 **Update** 以计算并显示这些值。

给出的特性包括 **Centroid** 和 **Shear Center**。形心是轴向力使梁伸长（或缩短）而不发生弯曲的点。剪切中心是横向力必须通过以使梁弯曲而不发生扭转的点。

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
- *E* — 杨氏模量
- *G* — 剪切模量
- *J* — 扭转常数（由 Saint-Venant 翘曲偏微分方程的解获得）

其余参数是梁的相关面积矩。这些是围绕形心坐标系的轴计算的——该坐标系与局部参考坐标系对齐，但其原点位于形心。面积矩为：

- *I*x, *I*y — 形心二次面积矩：

  [Ix,Iy]=[∫A(y−yc)2dA,∫A(x−xc)2dA],
- *I*xy — 形心面积惯性积：

  Ixy=∫A(x−xc)(y−yc)dA,
- *I*p — 形心极惯性矩：

  IP=Ix+Iy,

其中 *x*c 和 *y*c 是形心的坐标。

### **Geometric Centroid** — 梁横截面的形心 [0 0] `m`（默认）| 2×1 数组

梁横截面的形心，指定为 2×1 数组。该数组指定形心相对于梁参考坐标系的 *x* 和 *y* 坐标。

#### 依赖关系

要启用此参数，请在 **Stiffness and Inertia** 部分中，将 **Type** 设置为 `Custom`。

### **Bending Centroid** — 中性轴与横截面的交点 [0 0] `m`（默认）| 2×1 数组

中性轴与横截面的交点，指定为 2×1 数组。该数组指定形心相对于梁参考坐标系的 *x* 和 *y* 坐标。

#### 依赖关系

要启用此参数，请在 **Stiffness and Inertia** 部分中，将 **Type** 设置为 `Custom`。

### **Shear Center** — 梁的剪切中心 [0 0] `m`（默认）| 2×1 数组

梁的剪切中心，指定为 2×1 数组。该数组指定该点相对于梁参考坐标系的 *x* 和 *y* 坐标。

#### 依赖关系

要启用此参数，请在 **Stiffness and Inertia** 部分中，将 **Type** 设置为 `Custom`。

### **Axial Rigidity** — 抵抗轴向变形 1 `Pa*m^2`（默认）| 标量

抵抗沿梁纵向方向的变形，指定为标量。此参数指定刚度矩阵的 Sb 元素。

#### 依赖

要启用此参数，请在 **Stiffness and Inertia** 部分中，将 **Type** 设置为 `Custom`。

### **Flexural Rigidity** — 抵抗弯曲变形 [1 1] `Pa*m^4`（默认）| 2×1 数组

抵抗弯曲变形，指定为 2×1 数组。该数组指定刚度矩阵的 Hxb 和 Hyb 元素。

#### 依赖

要启用此参数，请在 **Stiffness and Inertia** 部分中，将 **Type** 设置为 `Custom`。

### **Cross Flexural Rigidity** — 抵抗因绕 y 轴弯矩引起的绕 x 轴弯曲变形 0 `Pa*m^4`（默认）| 标量

抵抗因绕 *y* 轴弯矩引起的绕 *x* 轴弯曲变形，指定为标量。此参数指定刚度矩阵的 Hxyb 元素。

#### 依赖

要启用此参数，请在 **Stiffness and Inertia** 部分中，将 **Type** 设置为 `Custom`。

### **Torsional Rigidity** — 抵抗扭转 1 `Pa*m^4`（默认）| 标量

抵抗绕梁纵向轴的扭转，指定为标量。
此参数指定刚度矩阵的 Hzb 元素。

#### 依赖

要启用此参数，请在 **Stiffness and Inertia** 部分中，将 **Type** 设置为 `Custom`。

### **Center of Mass** — 质心 [0 0] `m`（默认）| 2×1 数组

质心，指定为 2×1 数组。该数组指定该点相对于梁参考坐标系的
*x* 和 *y* 坐标。

#### 依赖

要启用此参数，请在 **Stiffness and
Inertia** 部分中，将 **Type** 设置为
`Custom`。

### **Mass Per Unit Length** — 单位长度质量 1 `kg/m`（默认）| 标量

单位长度质量，指定为标量。此参数指定质量矩阵的 mc 元素。

#### 依赖

要启用此参数，请在 **Stiffness and Inertia** 部分中，将 **Type** 设置为 `Custom`。

### **Mass Moment of Inertia Density** — 抵抗绕 `x` 和 `y` 轴的旋转 [1 1] `kg*m`（默认）| 2×1 数组

抵抗绕 *x* 和
*y* 轴的旋转，指定为 2×1 数组。该数组
指定质量矩阵的 ixc 和 iyc 元素。

#### 依赖

要启用此参数，请在 **Stiffness and
Inertia** 部分中，将 **Type** 设置为
`Custom`。

### **Mass Product of Inertia Density** — 抵抗因绕 `y` 轴力矩引起的绕 `x` 轴旋转 0 `kg*m`（默认）| 标量

抵抗因绕 *y* 轴力矩引起的绕 *x* 轴旋转，指定为标量。此
参数指定质量矩阵的 ixyc 元素。

#### 依赖

要启用此参数，请在 **Stiffness and
Inertia** 部分中，将 **Type** 设置为
`Custom`。

### Damping

### **Type** — 阻尼方法类型 `Proportional`（默认）| `Uniform Modal` | `None`

要施加到梁上的阻尼方法：

- 选择 `None` 以对无阻尼梁进行建模。
- 选择 `Proportional` 以施加比例（或 Rayleigh）阻尼方法。此方法将阻尼矩阵
  [*C*] 定义为质量矩阵
  [*M*] 和刚度矩阵
  [*K*] 的线性组合：

  [C]=α[M]+β[K]，

  其中 *α* 和 *β* 是标量
  系数。
- 选择 `Uniform Modal` 以施加均匀模态
  阻尼方法。此方法对梁的所有振动
  模态施加单一阻尼比。该值越大，振动
  衰减越快。

  所选参考条件会影响阻尼比适用的模态
  类型。有关参考条件的详细信息，请参阅参考条件。当您
  对柔性体使用模态缩减时，仅会保留
  模态的一个子集。有关模态缩减的详细信息，请参阅减少柔性体的自由度。

### **Mass Coefficient** — 质量矩阵系数 0 `1/s`（默认）| 非负标量

质量矩阵的系数 *α*。此参数定义与质量矩阵 [*M*] 成比例的
阻尼。

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Proportional`。

### **Stiffness Coefficient** — 刚度矩阵系数 0.001 `s`（默认）| 非负标量

刚度矩阵的系数 *β*。此参数定义与刚度矩阵 [*K*] 成比例的
阻尼。

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Proportional`。

### **Damping Ratio** — 均匀模态阻尼方法的阻尼比 0.01（默认）| 无量纲非负标量

在均匀模态阻尼模型中施加到所有梁振动模态的
阻尼比 *ζ*。该值越大，梁振动
衰减越快。

当 *ζ* = 0 时，梁无阻尼。如果施加到梁上的边界条件与所选参考条件
完全匹配，则 *ζ* < 1 会产生欠阻尼模态衰减，*ζ* = 1 对应临界阻尼，*ζ* > 1 会产生过阻尼耗散。当边界条件与
参考条件不匹配时，所选阻尼比的效果会发生变化。有关
参考条件的详细信息，请参阅参考条件。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Uniform
Modal`。

### 离散化

### **Number of Elements** — 梁有限元数量 1（默认）| 正整数

梁模型中的有限元数量。增加单元数量始终
会提高仿真精度。但在实际中，当单元很多时，精度的提升
在某个点之后可以忽略不计。此外，更多的
单元会增加计算成本并降低
仿真速度。

### 参考条件

### **Type** — 参考条件类型 `Linearized Mean Axes`（默认）| `Body-Fixed`

指定要施加的参考条件类型。有关详细信息，请参阅参考条件。

- `Linearized Mean Axes`：参考的体坐标系
  跟随瞬时质心，柔性
  体表现出无约束的变形振动模态。
- `Body-Fixed`：选择固连于体的坐标系作为
  参考的体坐标系。柔性体的变形
  表现出自由振动模态振型，并且在参考体坐标系
  位置处具有零平移和
  旋转变形。

### **Frame** — 用于体固定参考条件的连接坐标系 坐标系名称

输入要用作参考体坐标系的连接坐标系名称。
坐标系名称区分大小写。确保所选坐标系作为端口
暴露在模块上。您不能使用 **R** 坐标系，它是
虚拟未变形体的参考坐标系。

#### 依赖关系

要启用此参数，请将 **Type** 设置为
`Body-Fixed`。

### **Show Port R** — 显示参考坐标系端口 关闭（默认）| 开启

选择以公开 **R** 端口，该端口表示虚拟未变形体的参考坐标系。请注意，**R** 坐标系并非物理上附着于柔性体。

**R** 端口不得与任何施加力和力矩或具有惯性的模块刚性连接。

### 保真度

### **Reduction** — 用于对柔性体建模的方法 `None`（默认）| `Modally Reduced`

用于对柔性体建模的方法，指定为 `None` 或 `Modally Reduced`。将参数设置为 `None` 以使用由有限元方法生成的完整节点弹性坐标，或将参数设置为 `Modally Reduced` 以使用模态变换方法缩减体的弹性坐标。对于这两种设置，模块均使用浮动参考系公式 [1-2] 将体与其弹性变形耦合。

### **Number of Retained Modes** — 保留模态数 1（默认）| 非负整数

保留模态数，指定为范围 [0, *n*] 内的整数，其中 *n* 为体的弹性自由度数量。如果将数值设置为 0，则柔性体被视为刚体。

#### 依赖关系

要启用此参数，请将 **Reduction** 设置为 `Modally Reduced`。

### 图形

### **Type** — 用于梁可视化显示的图形 `From Geometry`（默认）| `None`

梁的视觉表示类型，指定为 `From Geometry` 或 `None`。将参数设置为 `From Geometry` 以显示梁的视觉表示。将参数设置为 `None` 以在模型可视化中隐藏梁。

### **Visual Properties** — 颜色和不透明度的参数化方式 `Simple`（默认）| `Advanced`

用于指定视觉属性的参数化方式。选择 `Simple` 以指定 **Color** 和 **Opacity**。选择 `Advanced` 以指定更多视觉属性，例如 **Specular Color**、**Ambient Color**、**Emissive Color** 和 **Shininess**。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `From Geometry`。

### **Color** — 漫反射光的颜色 [0.5 0.5 0.5]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量

在直接白光下图形的颜色，指定为 0–1 范围内的 [R G B] 或 [R G B A] 向量。可选的第四个元素 (A) 以 0–1 的比例指定颜色不透明度。省略不透明度元素等同于指定值为 1。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Simple`

### **Opacity** — 图形不透明度 1.0（默认）| 取值范围为 0 到 1 的标量

图形不透明度，指定为 0 到 1 范围内的标量。标量为 0 对应于完全透明，标量为 1 对应于完全不透明。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Simple`

### **Diffuse Color** — 漫反射光的颜色 [0.5 0.5 0.5]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量

漫反射光的颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等同于指定值为 1。

漫反射颜色反映所渲染梁的主色，并提供阴影，使渲染对象呈现三维外观。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Advanced`

### **Specular Color** — 由于镜面反射产生的光的颜色 [0.5 0.5 0.5 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量

由于镜面反射产生的光的颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值为 1。此参数会改变镜面高光的颜色，镜面高光是由于光源的光反射而在渲染光束上形成的亮点。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Advanced`

### **Ambient Color** — 环境光的颜色 [0.15 0.15 0.15 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量

环境光的颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值为 1。

环境光指的是并非直接来自光源的一般照明水平。环境光是已经反射并再次反射了很多次，以至于不再来自任何特定方向的光。您可以调整此参数来更改渲染光束的阴影颜色。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Advanced`

### **Emissive Color** — 自发光颜色 [0.0 0.0 0.0 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量

由于自发光产生的颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值为 1。

发射颜色是不来自任何外部来源的颜色，因此看起来是由光束本身发射的。当光束具有发射颜色时，即使没有外部光源，也可以看到该光束。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Advanced`

### **Shininess** — 高光锐度 75（默认）| 取值约束为 0–128 的标量

镜面光反射的锐度，指定为 0–128 范围内的标量数值。
增大 shininess 值可获得更小但更锐利的高光。减小该值可获得更大但更平滑的高光。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `From Geometry`
2. **Visual Properties** 为 `Advanced`

### Frames

### **Show Port A** — 显示端口 A 以连接到其他模块 on（默认）| off

选择此项以公开 **A** 端口。

### **Show Port B** — 显示端口 B 以连接到其他模块 on（默认）| off

选择此项以公开 **B** 端口。

### **New Frame** — 创建自定义坐标系以连接到其他模块按钮

单击创建按钮 Create 以打开用于创建新的体附着坐标系的窗格。在此窗格中，您可以指定坐标系的名称、原点和方向。

- 要命名自定义坐标系，请单击 **Frame Name** 参数的文本字段。该名称标识梁模块上对应的端口以及 Multibody Explorer 树视图窗格中的对应端口。
- 要为自定义坐标系选择 **Frame Origin**，请使用以下方法之一：

  - **At Reference Frame Origin**：使新坐标系原点与未变形梁的参考坐标系原点重合。
  - **Based on Geometric Feature**：使新坐标系原点与所选未变形几何特征的中心重合。有效特征包括曲面、线和点。从可视化窗格中选择一个特征，然后单击 **Use Selected Feature** 以确认原点的位置。原点位置的名称将显示在此选项下方的字段中。
- 要定义自定义坐标系的方向，请在 **Frame Axes** 部分下，选择自定义坐标系的 **Primary Axis** 和 **Secondary Axis**，然后指定它们的方向。

  使用以下方法选择用于指定主轴和次轴方向的向量。主轴平行于所选向量，并将其余两个轴约束到其法平面内。次轴平行于所选向量在法平面上的投影。

  - **Along Reference Frame Axis**：选择未变形梁的参考坐标系的一个轴。
  - **Based on Geometric Feature**：选择与未变形梁的所选几何特征相关联的向量。有效特征包括曲面和线。对应的向量在可视化窗格中由白色箭头指示。您可以从可视化窗格中选择一个特征，然后单击 **Use Selected Feature** 以确认选择。所选特征的名称将显示在此选项下方的字段中。

### **FrameN** — 编辑或删除现有自定义坐标系坐标系名称

您已创建的坐标系。`N` 是每个自定义坐标系的唯一标识编号。

- 单击文本字段以编辑现有自定义坐标系的名称。

- 单击编辑按钮 Edit 以编辑自定义坐标系的其他方面，例如原点和轴。
- 单击删除按钮 Delete 以删除自定义坐标系。

#### 依赖关系

要启用此参数，请单击 **New Frame** 创建一个坐标系。
## 所属库

Simscape / Multibody / Body Elements / Flexible Bodies / Beams

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

具有弹性特性的 T 型梁，用于变形分析

Flexible T Beam 模块对具有 T 形横截面的细长梁（也称为 T 型梁）进行建模。T 型梁由一个水平组件（称为翼缘）和一个垂直组件（称为腹板）组成。T 型梁可以具有小的线性变形。这些变形包括拉伸、弯曲和扭转。该模块根据您指定的几何形状和材料属性计算梁的横截面特性，例如轴向刚度、抗弯刚度和抗扭刚度。

T 型梁的几何形状是其横截面的拉伸体。梁的横截面定义在 *xy* 平面内，沿 *z* 轴拉伸。要定义横截面，您可以在模块对话框的 **Geometry** 部分中指定其尺寸。该图显示了一个 T 型梁及其横截面。梁的参考坐标系位于腹板和翼缘中平面交线的中点处。

有关柔性梁建模的更多信息，请参阅 Overview of Flexible Beams。
