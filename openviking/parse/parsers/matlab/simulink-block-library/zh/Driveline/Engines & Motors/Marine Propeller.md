---
type: simulink-block
title: 'Marine Propeller'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Engines & Motors'
documentation_page: 'marinepropeller'
documentation_source_path: 'ref/marinepropeller.html'
language: zh-CN
chinese_source: worker-translation
---

# Marine Propeller

## 端口

### 输入

### **Va** — 进速，m/s 物理信号

与通过螺旋桨的流速相关联的物理信号输入端口。

#### 依赖

要启用此端口，请将 **Translational connections** 设置为 `Physical signals`。

### **PR** — 叶距直径比，无量纲物理信号

与给定螺旋桨直径的叶片螺距相关联的物理信号输入端口。

#### 依赖

要启用此端口，请将 **Blade pitch type** 设置为 `Controlled`。

### **Rho** — 可变密度，kg/m^3 物理信号

与流体密度相关联的物理信号输入端口，单位为 kg/m3。

#### 依赖

要启用此端口，请将 **Fluid density specification** 设置为 `Variable`。

### **w** — 螺旋桨转速，rad/s 物理信号

与螺旋桨转速相关联的物理信号端口，单位为 rad/s。

#### 依赖

要启用此端口，请将 **Rotational connections** 设置为 `Physical signals`。
### 输出

### **Th** — 螺旋桨推力，N 物理信号

与螺旋桨产生的推力相关联的物理信号输出端口，单位为 N。

#### 依赖

要启用此端口，请将 **Translational connections** 设置为 `Physical signals`。

### **E** — 效率，无量纲物理信号

与螺旋桨效率相关联的物理信号输出端口。效率信号是进速比绝对值的函数。

#### 依赖

要启用此端口，请选中 **Efficiency sensor**。

### **Q** — 螺旋桨阻力矩，N\*m 物理信号

与螺旋桨阻力矩相关联的物理信号端口，单位为 N\*m。

#### 依赖

要启用此端口，请将 **Rotational connections** 设置为 `Physical signals`。
### 守恒

### **R1** — 杆接口 机械旋转

与杆接口相关联的机械旋转守恒端口。

#### 依赖

要启用此端口，请将 **Rotational connections** 设置为 `Conserving`。

### **R2** — 船舶速度和推力 机械平移

与船舶速度和推力相关联的机械平移守恒端口。

#### 依赖

要启用此端口，请将 **Translational connections** 设置为 `Conserving`。

### **C2** — 参考水流 机械平移

与螺旋桨所抵抗的水流运动相关联的机械平移守恒端口。

#### 依赖

要启用此端口，请将 **Translational connections** 设置为 `Conserving`。

## 参数

### 螺旋桨

### **Parameterization** — 螺旋桨参数化 `Constant coefficients`（默认）| `Polynomial fit` | `Tabulated data for advance ratio` | `Tabulated data for advance angle`

通过常数、多项式或表格化的推力和扭矩系数来参数化螺旋桨的选项。从以下设置中选择：

- `Constant coefficients` — 使用相对于进速比的常数推力和扭矩系数。
- `Polynomial fit` — 使用多项式系数来参数化进速比。
- `Tabulated data for advance ratio` — 使用表格化进速比数据来参数化进速比。
- `Tabulated data for advance angle` — 使用相对于叶片半径 70% 处相对进速的推力和扭矩系数。

要了解更多信息，请参阅 Parameterizations。

### **Propeller direction** — 正推力方向 `Negative rotational velocity generates positive thrust for positive thrust coefficients`（默认）| `Positive rotational velocity generates positive thrust for positive thrust coefficients`

对于正推力系数，负转速还是正转速产生正推力。

### **Propeller diameter** — 螺旋桨直径 `0.2` `m`（默认）| 正标量

螺旋桨的直径。

### **Thrust coefficient, kT** — 推力系数 `0.25`（默认）| 正标量

使用常数系数时的无量纲常数推力系数。

#### 依赖

要启用此参数，请将 **Parameterization** 设置为 `Constant coefficients`。

### **Resistive torque coefficient, kQ** — 扭矩系数 `0.05`（默认）| 正标量

使用常数系数时的无量纲阻力矩系数。

#### 依赖

要启用此参数，请将 **Parameterization** 设置为 `Constant coefficients`。

### **Blade pitch type** — 恒定或可控叶片螺距 `Constant`（默认）| `Controlled`

要建模的叶片类型。选择 `Constant` 表示恒定螺距的叶片，或选择 `Controlled` 表示使用 **PR** 端口指定的可变螺距叶片。

#### 依赖

要启用此参数，请将 **Parameterization** 设置为 `Polynomial fit`、`Tabulated data for advance ratio` 或 `Tabulated 提前角的数据`。

### **kT polynomial coefficients (pN...p0)** — 推力系数多项式系数 `[.063, -.19, -.25, .37]`（默认）| 向量

无量纲多项式推力系数向量。按降序指定元素。该模块使用这些系数生成查找表。有关详细信息，请参阅 Using Lookup Tables in Equations。

#### 依赖

要启用此参数，请设置：

- **Parameterization** 为 `Polynomial fit`
- **Blade pitch type** 为 `Constant`

### **kQ polynomial coefficients (pN...p0)** — 扭矩系数多项式系数 `[.0043, -.021, -.03, .05]`（默认）| 向量

无量纲多项式推力系数向量。按降序指定元素。该模块使用这些系数生成查找表。有关详细信息，请参阅 Using Lookup Tables in Equations。

#### 依赖

要启用此参数，请设置：

- **Parameterization** 为 `Polynomial fit`
- **Blade pitch type** 为 `Constant`

### **Pitch-diameter ratio vector, P/D** — 推力和扭矩系数的叶距直径比值 `[-.5, .5, .7, .9, 1.1, 1.4]`（默认）| 向量

叶片螺距与直径的比值。每个元素在 **Table of kT polynomial coefficients (P/D, pN...p0)** 和 **Table of kQ polynomial coefficients (P/D, pN...p0)** 参数中都有对应的行。

#### 依赖

要启用此参数，请设置：

- **Parameterization** 为 `Polynomial fit`、`Tabulated data for advance ratio` 或 `Tabulated data for advance angle`
- **Blade pitch type** 为 `Controlled`

### **Table of kT polynomial coefficients (P/D, pN...p0)** — 可控螺距螺旋桨的多项式推力系数 `[.04, -.1, -.24, .12; .118, -.24, -.24, .19; .082, -.21, -.25, .28; .063, -.19, -.25, .37; .055, -.17, -.25, .45; .064, -.21, -.19, .55]`（默认）| 矩阵

给定 *P/D* 比值的多项式推力系数向量表。

#### 依赖

要启用此参数，请设置：

- **Parameterization** 为 `Tabulated data for advance ratio`
- **Blade pitch type** 为 `Controlled`

### **Table of kQ polynomial coefficients (P/D, pN...p0)** — 可控螺距螺旋桨的多项式扭矩系数 `[.02, -.06, -.02, .02; .04, -.034, -.016, .018; .0076, -.02, -.023, .031; .0043, -.021, -.03, .05; .0047, -.024, -.036, .073; .0045, -.025, -.044, .11]`（默认）| 矩阵

给定 *P/D* 比值的多项式扭矩系数向量表。

#### 依赖

要启用此参数，请设置：

- **Parameterization** 为 `Tabulated data for advance ratio`
- **Blade pitch type** 为 `Controlled`

### **Advance ratio vector, J** — 表格化推力和扭矩系数的进速比范围 `[0, .3, .5, .7, .9, 1.2, 1.5]`（默认）| 向量

表格化进速比。每个元素在 **Thrust coefficient vector, kT(J)** 和 **Resistive torque coefficient vector, kQ(J)** 参数中都有对应的元素，或在 **Thrust coefficients table, kT(P/D, J)** 和 **Resistive torque coefficients table, kQ(P/D, J)** 参数中都有对应的列。

#### 依赖

要启用此参数，请将 **Parameterization** 设置为 `Tabulated data for advance ratio`。

### **Thrust coefficient vector, kT(J)** — 给定进速比的表格化推力系数值 `[.37, .28, .21, .12, .033, -.098, -.23]`（默认）| 向量

作为进速比函数的表格化推力系数值。

#### 依赖

要启用此参数，请设置：

- **Parameterization** 为 `Tabulated data for advance ratio`
- **Blade pitch type** 为 `Constant`

### **Resistive torque coefficient vector, kQ(J)** — 给定进速比的表格化扭矩系数值 `[.049, .039, .03, .02, .0096, -.0093, -.028]`（默认）| 向量

作为进速比函数的表格化扭矩系数值。

#### 依赖

要启用此参数，请设置：

- **Parameterization** 为 `Tabulated data for advance ratio`
- **Blade pitch type** 为 `Constant`

### **Thrust coefficient table, kT(P/D, J)** — 给定叶距直径比和进速比的表格化推力系数值 `[.12, .04, -.02, -.083, -.15, -.24, -.33;`（默认）| 矩阵 | ...

作为叶距直径比和进速比函数的表格化推力系数值。列对应于 **Advance ratio vector, J** 参数中的元素，行对应于 **Pitch-diameter ratio vector, P/D** 参数中的元素。

默认值为 `[.12, .04, -.02, -.083, -.15, -.24, -.33; .19, .1, .029, -.047, -.12, -.23, -.35; .28, .19, .12, .032, -.054, -.18, -.31; .37, .28, .21, .12, .033, -.098, -.23; .45, .36, .29, .21, .13, -.0057, -.16; .54, .47, .41, .33, .25, .13, .0029]`。

#### 依赖

要启用此参数，请设置：

- **Parameterization** 为 `Tabulated data for advance ratio`
- **Blade pitch type** 为 `Controlled`

### **Resistive torque coefficient table, kQ(P/D, J)** — 给定叶距直径比和进速比的表格化扭矩系数值 `[.02, .0091, -.0025, -.017, -.032, -.056, -.078;`（默认）| 矩阵 | ...

作为叶距直径比和进速比函数的表格化扭矩系数值。列对应于 **Advance ratio vector, J** 参数中的元素，行对应于 **Pitch-diameter ratio vector, P/D** 参数中的元素。

默认值为 `[.02, .0091, -.0025, -.017, -.032, -.056, -.078; .017, .011, .006, .0009, -.0041, -.012, -.019; .03, .022, .015, .0074, -.0008, -.013, -.026; .049, .039, .03, .02, .0096, -.0093, -.028; .072, .06, .05, .038, .025, .0042, -.015; .11, .097, .085, .071, .057, .033, .0065]`。

#### 依赖

要启用此参数，请设置：

- **Parameterization** 为 `Tabulated data for advance ratio`
- **Blade pitch type** 为 `Controlled`

### **Advance angle vector, β** — 递增进速角 `linspace(0, 360, 10)` `deg`（默认）| 长度为 *N* 的向量

表格化进速角。使用单调递增向量，其中元素在 [0, 360] 度范围内。在仿真期间，螺旋桨进速角可以在 [0, 360) 度范围内，其中模块将角度包裹在 0 到 360 度之间。

当您将 **Extrapolation method** 设置为 `Linear` 或 `Nearest` 时：

- 如果第一个元素不是 0，则当 *β* 小于第一个元素时，模块基于第一个或前两个元素进行外插。
- 如果最后一个元素不等于 360 度，则当 *β* 大于最后一个元素时，模块基于最后一个或最后两个元素进行外插。

#### 依赖

要启用此参数，请将 **Parameterization** 设置为 `Tabulated 提前角的数据`。

### **Thrust coefficient vector, Ct(β)** — 给定进速角的表格化推力系数 `0.2 * sind(linspace(0, 360, 10) - 200)`（默认）| 长度为 *N* 的向量

作为进速角函数的表格化推力系数。该系数取决于叶片半径 70% 处的叶片相对进速。此向量中的元素必须与 **Advance angle vector, β** 参数一一对应。

#### 依赖

要启用此参数，请将 **Parameterization** 设置为 `Tabulated data for advance angle`，并将 **Blade pitch type** 设置为 `Constant`。

### **Torque coefficient vector, Cq(β)** — 给定进速角的表格化扭矩系数 `0.015 * sind(linspace(0, 360, 10) - 200)`（默认）| 长度为 *N* 的向量

作为进速角函数的表格化阻力矩系数。该系数基于叶片半径 70% 处的叶片相对进速。此向量中的元素必须与 **Advance angle vector, β** 参数一一对应。

#### 依赖

要启用此参数，请将 **Parameterization** 设置为 `Tabulated data for advance angle`，并将 **Blade pitch type** 设置为 `Constant`。

### **Thrust coefficient table, Ct(P/D, β)** — 给定叶距直径比和进速角的表格化推力系数 `[0.15 * sind(linspace(0, 360, 10) - 200); 0.20 * sind(linspace(0, 360, 10) - 200);`（默认）| *M*×*N* 矩阵

作为叶距直径比和进速角函数的表格化推力系数。默认值为 `[0.15 * sind(linspace(0, 360, 10) - 200); 0.20 * sind(linspace(0, 360, 10) - 200); 0.25 * sind(linspace(0, 360, 10) - 200); 0.30 * sind(linspace(0, 360, 10) - 200); 0.35 * sind(linspace(0, 360, 10) - 200); 0.40 * sind(linspace(0, 360, 10) - 200)]`。

#### 依赖

要启用此参数，请将 **Parameterization** 设置为 `Tabulated data for advance angle`，并将 **Blade pitch type** 设置为 `Controlled`。

### **Torque coefficient table, Cq(P/D, β)** — 给定叶距直径比和进速角的表格化扭矩系数 `[0.010 * sind(linspace(0, 360, 10) - 200); 0.015 * sind(linspace(0, 360, 10) - 200);`（默认）| *M*×*N* 矩阵 | ...

作为叶距直径比和进速角函数的表格化扭矩系数。默认值为 `[0.010 * sind(linspace(0, 360, 10) - 200); 0.015 * sind(linspace(0, 360, 10) - 200); 0.020 * sind(linspace(0, 360, 10) - 200); 0.025 * sind(linspace(0, 360, 10) - 200); 0.030 * sind(linspace(0, 360, 10) - 200); 0.035 * sind(linspace(0, 360, 10) - 200)]`。

#### 依赖

要启用此参数，请将 **Parameterization** 设置为 `Tabulated data for advance angle`，并将 **Blade pitch type** 设置为 `Controlled`。

### **Interpolation method** — 断点值之间的插值方法 `Linear`（默认）| `Smooth`

用于查找表断点插值的方法。该模块使用 `tablelookup` 函数，通过使用数组数据将输入值映射到输出值来对非线性进行建模：

- `Linear` — 选择此选项可获得最低的计算成本。
- `Smooth` — 选择此选项可生成具有连续一阶导数的连续曲线。

有关详细信息，请参阅 `tablelookup`。

#### 依赖

要启用此参数，请将 **Parameterization** 设置为 `Tabulated data for advance ratio` 或 `Tabulated 提前角的数据`。

### **Extrapolation method** — 处理超出断点数据集范围的输入值的方法 `Linear`（默认）| `Nearest` | `Error`

用于查找表断点外插的方法。此方法确定当输入值超出参数列表中指定的范围时的输出值。该模块使用 `tablelookup` 函数，通过使用数组数据将输入值映射到输出值来对非线性进行建模：

- `Linear` — 选择此选项可生成在外插区域以及与插值区域边界处具有连续一阶导数的曲线。
- `Nearest` — 选择此选项可生成不高于数据中最高点或低于数据中最低点的外插。
- `Error` — 当您希望数据在表范围内时，选择此选项可避免外插。如果输入信号超出表的范围，仿真将停止并生成错误。

#### 依赖关系

要启用此参数，请将 **Parameterization** 设置为 `Tabulated
data for advance ratio` 或 `Tabulated
提前角的数据`。

### 环境与动力学

### **Fluid density specification** — 流体密度选择 `Constant`（默认）| `Variable`

用于指定恒定或可变流体密度的选项。

### **Fluid density** — 恒定流体密度值 `1000` `kg/m^3`（默认）| 正标量

恒定流体密度值。

#### 依赖关系

要启用此参数，请将 **Fluid density
specification** 设置为
`Constant`。

### **Rotational connections** — 旋转运动输入选项 `Physical signals`（默认）| `Conserving`

是将螺旋桨旋转速度和阻力拖曳力矩分别作为物理信号输入和输出进行仿真，还是作为旋转连接进行仿真。此设置决定图标中轮毂的颜色，该颜色指示模块处于旋转守恒域还是物理信号域。

### **Translational connections** — 平移运动输入选项 `Conserving`（默认）| `Physical signals`

是将前进速度和螺旋桨推力分别作为物理信号输入和输出进行仿真，还是作为平移连接进行仿真。此设置决定图标中叶片的颜色，该颜色指示模块处于平移守恒域还是物理信号域。当您选择 `Conserving` 时，恒定伴流分数会相对于船舶速度降低前进速度。

### **Wake fraction** — 伴流调整后的船舶速度百分比 `0.2`（默认）| 非负标量

相对于前进速度的船舶速度折减量。对于敞水情况，请使用值 `0`。

#### 依赖关系

要启用此参数，请将 **Translational
connections** 设置为
`Conserving`。

### **Model inertia** — 惯性选项 `off`（默认）| `on`

是否仿真由转子运动引起的惯性。该模块在端口 **R1** 处施加旋转惯性，在端口 **R2** 处施加平移惯性。

#### 依赖关系

要启用此参数，请将 **Rotational
connections** 或 **Translational
connections** 设置为 conserving。

### **Propeller inertia** — 螺旋桨惯性 `0.1` `kg*m^2`（默认）| 正标量

螺旋桨组件的惯性。该模块在端口 **R1** 处施加该惯性。

#### 依赖关系

要启用此参数，请将 **Rotational
connections** 设置为 conserving 并选择 **Model
inertia**。

### **Propeller mass** — 螺旋桨质量 `10` `kg`（默认）| 正标量

螺旋桨组件的质量。该模块在端口 **R2** 处施加平移惯性。

#### 依赖关系

要启用此参数，请将 **Translational
connections** 设置为 conserving 并选择 **Model
inertia**。

### 高级

### **Efficiency sensor** — 运行效率输出选项 `off`（默认）| `on`

是否启用效率端口 **E**，该端口输出正值效率信号。

### **Rotational speed threshold** — 转速平滑点 `0.001` `Hz`（默认）| 正标量

饱和阈值，
*nThr*，超过该值后，
模块会施加平滑直至饱和点。

### **Saturation threshold for nondimensional coefficients** — 无量纲系数平滑点 `0.001`（默认）| 正标量

饱和阈值，
*kThr*，在该值处模块
对无量纲系数施加平滑。

### **Check if operating beyond normal propeller operation** — 运行边界容差 `Warning`（默认）| `None` | `Error`

当螺旋桨超出运行参数时，是生成警告还是错误。该模块检查螺旋桨是否在第一象限内运行。如果
*Va* 或
*n(t)* 不为正值，则螺旋桨会生成带有相应符号的推力
和力矩系数，并根据参数设置生成警告
或错误。当您提高 **Rotational speed threshold** 参数的值时，
触发会变得不那么敏感。

当您将 **Parameterization** 设置为
`Polynomial fit` 时，当螺旋桨超出
*kT* 参数的第一个正根时，模块会生成
警告或错误。

该模块使用关于第一象限的对称或
非对称行为来近似水动力学。

#### 依赖关系

要启用此参数，请将
**Parameterization** 设置为 `Polynomial
fit` 或 `Tabulated data for advance
ratio`。

## 所属库

Simscape / Driveline / Engines & Motors

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

### R2023a：端口和参数更新

端口 **C1** 不再需要，并已被移除。

**Propeller direction** 参数是新增的。

### R2023a：新增惯性选项

要对惯性建模，请选择 **Model inertia**，并将
**Rotational connections** 或 **Translational
connections** 设置为 `Conserving`，以分别启用
**Propeller inertia** 或 **Propeller
mass** 参数。

### R2022b：名称变更

模块名称从 Propeller 更改为
Marine Propeller。

### R2022b：前进角支持

要独立参数化四个象限，请将
**Parameterization** 设置为 `Tabulated data for advance
angle`。此设置会启用以下参数：

- `Advance angle vector, β`
- `Thrust coefficient vector, Ct(β)`
- `Torque coefficient vector, Cq(β)`
- `Thrust coefficient table, Ct(P/D, β)`
- `Torque coefficient table, Cq(P/D, β)`

先前名为 `Tabulated coefficients` 的设置
现在为 `Tabulated data for advance ratio`。

## 描述

在海洋环境中将旋转转换为推力的螺旋桨

Marine Propeller 模块表示一个螺旋桨，它将旋转机械运动转换为
海洋应用中的推力。您可以将螺旋桨配置为固定叶片或可控叶片。您可以
使用常数、多项式或表格数据来参数化
螺旋桨，以表征推力和力矩系数。您可以提供表格化的前进速度数据，或者
提供表格化的前进角数据，以参数化所有四个运行象限。
允许负螺距或可反向运行的螺旋桨可能包含特定于
倒车方向的推力和力矩系数曲线，您也可以在模块中
指定这些曲线。

您还可以在模块中包含船体对螺旋桨的伴流效应。当您
指定恒定伴流分数或启用物理信号端口时，模块
会自动计算伴流效应。

您可以使用物理信号来控制叶片螺距。

以下术语有助于理解该模块：

- *伴流分数* 是船舶
  速度与前进速度之差与船舶
  速度的比值。
- *前进速度* 是流过
  螺旋桨的流速，*Va*。
- *前进比* 是流过
  螺旋桨的流速相对于螺旋桨叶尖角速度的比值。当您将
  **Parameterization** 设置为 `Polynomial
  fit` 或 `Tabulated data for advance
  ratio` 时，模块使用它来确定
  *kT* 和
  *kQ*。
- *前进角* 是
  螺旋桨运行条件在四象限图上的角位置。当您将
  **Parameterization** 设置为 `Tabulated data for
  advance ratio` 时，模块使用它来确定 *CT* 和
  *CQ*。
- *象限* 是
  螺旋桨运行条件的相对二维位置，其中垂直轴为
  *Va*，水平轴
  为 *ω*。
- *螺距* 是单次旋转的理想平移螺旋桨前进
  距离。
- *敞水* 是不存在
  船体效应时的情况。

模块方程引用以下量：

- *T* 是螺旋桨推力。
- *Q* 是螺旋桨力矩。
- *ρ* 是流体密度。您可以使用 **Density** 参数或
  **Rho** 端口指定流体
  密度。
- *P* 是螺距。
- *D* 是 **Propeller diameter**
  参数，其中一个表示
- *ω* 是端口
  **R** 处的螺旋桨角速度输入。有关在 Simscape™ 中使用角度单位的
  更多信息，请参阅 Angular Units。
- *n* 是螺旋桨角速度，以每秒转数表示，它一致地将力矩和推力
  无量纲化。模块定义 *ω = 2πn*。
- *nThr* 是 **Rotational
  speed threshold** 参数。
- *ε* 是 **Propeller direction**
  参数。
- *kT* 是相对于螺旋桨转速的推力
  系数。
- *kQ* 是相对于螺旋桨转速的阻力力矩
  系数。
- *pkT* 是多项式推力
  系数向量或二维矩阵。
- *pkQ* 是多项式阻力
  力矩系数向量或二维矩阵。
- *CT* 是相对于相对前进速度的推力
  系数。
- *CQ* 是相对于相对前进速度的力矩
  系数。
- *kThr* 是 **Saturation
  threshold for nondimensional coefficients** 参数。
- *J* 是前进比。
- *Va* 是前进速度。
  使用 **Va** 端口指定前进速度。
- *VR* 是在叶片半径 70% 处的叶片截面处的相对前进
  速度。
- *η* 是效率。
- *CT\**
  是基于 70% 叶片半径处叶片相对前进速度的推力
  系数。
- *CT,TLU\**
  是参考推力系数向量或二维矩阵。
- *C\*Q*
  是基于 70% 叶片半径处叶片相对前进速度的力矩
  系数。
- *C\*Q,TLU*
  是参考力矩系数向量或二维矩阵。
- *β* 是前进角。
- *βTLU* 是参考前进
  角。

### 参数化

螺旋桨性能取决于推力和阻力力矩系数。
**Parameterization** 参数为您提供不同的选项来
控制这些系数。螺旋桨输出取决于
螺旋桨运行的象限。模块将四个象限定义为：

- 第一象限：*+Va*，
  *+n*
- 第二象限：*+Va*，
  *-n*
- 第三象限：*-Va*，
  *-n*
- 第四象限：*-Va*，
  *+n*

该图显示了象限的可视化表示。

四象限图，其中前进速度为正 y 轴，前进旋转为正 x 轴。

当您将 **Parameterization** 设置为
`Constant coefficients` 时，您可以直接指定推力和
阻力力矩系数。否则，模块会根据 **Parameterization**
设置计算这些
系数。

**前进比**

当您将 **Parameterization** 设置为 `Polynomial
fit` 或 `Tabulated data for advance
ratio` 时，模块使用前进比 *J*。
模块使用基本推力和
力矩方程的数值平滑版本，使得

T=kTρD4nn2+nthr2Q=kQρD5nn2+nthr2

模块将前进比定义为

J=VaεnD(n2+nThr2)，

其中角速度阈值
*nThr* 对螺旋桨
转速 *n* 进行线性化以进行平滑。

当您将 **Parameterization** 设置为：

- `Polynomial fit` —
  *kT* 和
  *kQ* 根据您为多项式系数
  参数指定的值随时间变化。模块将 *J* 饱和在 0 和
  多项式第一个正根之间，并限制
  *kT* 和
  *kQ* 始终为
  正值。模块计算推力和力矩系数
  如下

  kT=∑j=1:NNpkT,jJjkQ=∑j=1:NNpkQ,jJj

  其中 *pkT*
  和 *pkQ* 表示
  多项式系数。
- `Tabulated data for advance ratio` — 您
  为给定的
  *J* 值或 *J* 和
  *P/D* 值指定
  *kT* 和
  *kQ* 的表格值，具体取决于 **Blade pitch
  type** 参数。

螺旋桨效率的基础是基本关系

η=PoweroutPowerin=TVA2πnQ=J2πkTkQ。

当 **Efficiency sensor** 开启，并且您将
**Parameterization** 设置为
`Constant` 时，模块计算平滑
效率如下

η=kTJ2+kThr22πkQ。

当 **Efficiency sensor** 开启，并且您
将 **Parameterization** 设置为 `Polynomial
fit` 或 `Tabulated data for advance
velocity` 时，模块计算平滑效率如下

η=kTJ2+kThr22πkQ2+(0.01·kThr)2。

**前进角**

当您将 **Parameterization** 设置为 `Tabulated
data for advance angle` 时，模块使用相对于相对前进角的推力和力矩
系数。模块将
前进角定义为

β=arctan(Va0.7πεnD)，

其中 *β* 是循环的。您必须确保
系数外推和循环回绕按预期发生。模块
将相对于相对前进速度的推力和力矩系数定义为

CT\*=T18ρVR2πD2CQ\*=Q18ρVR2πD3

其中 *VR* 是
叶片半径 70% 处叶片截面处的
相对前进速度，使得

VR2=VA2+(0.7Dπεn)2。

重新排列系数方程可得到模块
关于相对前进速度的推力和力矩方程：

T=CT\*18ρVR2D2Q=CQ\*18ρVR2D3

当您将 **Blade pitch** 设置为：

- `Constant` 时，模块计算
  推力和力矩系数如下

  CT\*=tablelookup(βTLU,CT,TLU\*,β,interpolation = interp\_method,extrapolation = extrap\_method)CQ\*=tablelookup(βTLU,CQ,TLU\*,β,interpolation = interp\_method,extrapolation = extrap\_method)
- `Controlled` 时，模块计算
  推力和力矩系数如下

  CT\*=tablelookup(P/DTLU,βTLU,CT,TLU\*,P/D,β,interpolation = interp\_method,extrapolation = extrap\_method)CQ\*=tablelookup(P/DTLU,βTLU,CQ,TLU\*,P/D,β,interpolation = interp\_method,extrapolation = extrap\_method)

螺旋桨效率的基础是基本关系

η=PoweroutPowerin=TVA2πεnQ=VACT\*2πεnDCQ\*。

当 **Efficiency sensor** 开启时，模块
计算平滑效率如下

η=12πDVA2C\*2+(DπnThrKThr)2n2CQ\*2+(0.1nThrKThr)2。

**环境交互**

当您将 **Translational connections** 设置为
`Conserving` 时，模块使用恒定伴流
分数来关联船舶速度与前进速度。您使用 **R2** 和
**C2** 端口输入船舶的
推力和速度。模块计算前进速度
如下：

VA=V(1−w)，

其中：

- *V* 是船舶速度。您可以使用
  **R2** 和 **C2** 端口指定船舶相对于参考的速度，其中 *V* =
  *VR2*-*VC2*。
- *w* 是 **Wake fraction**
  参数。

当您将 **Translational connections** 设置为
`Physical connections` 时，您可以使用
**Va** 端口以物理信号形式提供前进速度。模块从
**Th** 端口输出螺旋桨推力作为物理信号。

**可控螺距**

当您将 **Blade pitch type** 设置为
`Controlled` 时，您可以在一定范围的螺距直径比 *P/D* 内参数化螺旋桨。您必须在 **Pitch-diameter
ratio vector, P/D** 参数中将 *P/D* 范围指定为向量，其中每个元素对应于
*kT* 和
*kQ* 矩阵中的一行。

### Inertia

您可以选择性地包含平移和旋转螺旋桨惯性。要模拟惯性，请将 **Rotational connections** 或 **Translational connections** 设置为 `Conserving`，并选择 **Model inertia**。当您选择 **Model inertia** 并将 **Rotational connections** 设置为 `Conserving` 时，在 **Initial Targets** 部分设置轴上的初始旋转速度或扭矩，或将代数链接变量设置为高优先级以初始化旋转惯性。当您选择 **Model inertia** 并将 **Translational connections** 设置为 `Conserving` 时，在 **Initial Targets** 部分设置初始平移速度或推力，或将代数链接变量设置为高优先级以初始化平移质量。

**Note**

对于旋转守恒连接，该模块记录 `Q`（气动扭矩）和 `Inertia.t`。

对于平移守恒连接，该模块记录 `thrust`（气动推力）和 `mass.f`。

您可以使用 Ideal Torque Sensor 或 Ideal Force Sensor 模块分别记录惯性与气动扭矩或力之和。

### 假设和限制

- 该模块将流体速度和螺旋桨旋转速度视为时间上的准稳态。流体均匀流过螺旋桨。
- 当您将 **Parameterization** 设置为 `Polynomial fit` 时，该模块假设螺旋桨扭矩和推力系数在第一象限内是对称的。
- 当您将 **Parameterization** 设置为 `Tabulated data for advance ratio` 时，该模块假设扭矩和推力系数在第一和第三象限以及第二和第四象限中相同。
- 当您将 **Parameterization** 设置为 `Tabulated data for advance angle` 时，该模块从 *Va* 中移除符号。要获得负推力和扭矩，您必须在 *CT* 和 *CQ* 的值中包含符号。

### 变量

要在仿真之前设置模块变量的优先级和初始目标值，请使用模块对话框或 Property Inspector 中的 **Initial Targets** 部分。有关详细信息，请参阅 Set Priority and Initial Target for Block Variables。

标称值提供了一种指定模型中变量预期幅值的方法。使用基于标称值的系统缩放可提高仿真鲁棒性。标称值可以来自不同来源，其中之一是模块对话框或 Property Inspector 中的 **Nominal Values** 部分。有关详细信息，请参阅 Modify Nominal Values for a Block Variable。
