---
type: simulink-block
title: 'Reduced Order Flexible Solid'
family: 'sm'
product_id: 'sm'
product_name: 'Multibody'
documentation_release: R2025b
official_category: 'Body Elements / Flexible Bodies'
documentation_page: 'reducedorderflexiblesolid'
documentation_source_path: 'ref/reducedorderflexiblesolid.html'
language: zh-CN
chinese_source: worker-translation
---

# Reduced Order Flexible Solid

## 端口

### Frame

### **F1, F2, ..., F*`n`*** — Frames frame

将柔性体连接到模型的坐标系。每个接口坐标系对应于降阶模型中的一个边界节点。这些坐标系允许您将柔性体连接到其他 Simscape™ Multibody™ 元素，例如关节、约束、力和传感器。不要求所有坐标系端口都连接。

### **R** — Reference frame frame

虚拟未变形体的参考坐标系，表示柔性体的整体刚体运动。**R** 坐标系在物理上不附着于柔性体。

**R** 端口不得与施加力和力矩或具有惯性的任何模块刚性连接。

## 参数

### Unit System

### **单位制** — 长度、质量和时间的标准或自定义单位 `SI (m, kg, s)`（默认）| `CGS (cm, g, s)` | `English (ft, slug, s)` | `Custom`

用于表示长度、质量、时间以及所有模块参数中使用的其他派生测量单位的单位制。角度测量始终以弧度为单位。

| Unit System | Base Units | | | Selected Derived Units | | |
| --- | --- | --- | --- | --- | --- | --- |
| Length | Mass | Time | Force | Stress and Pressure | Density |
| `SI` | m | kg | s | N = kg·m/s2 | Pa = kg/(m·s2) | kg/m3 |
| `CGS` | cm | g | s | dyn = g·cm/s2 | Ba = g/(cm·s2) | g/cm3 |
| `English` | ft | slug | s | lbf = slug·ft/s2 | slug/(ft·s2) | slug/ft3 |

要分别指定长度、质量和时间的单位，请选择 `Custom`。例如，假设您指定一个自定义单位制，长度使用 `mm`，质量使用 `t`，时间使用 `s`。派生单位包括力的单位 N = t·mm/s2，应力和压力的单位 MPa = t/(mm·s2)，以及密度的单位 t/mm3。

**Note**

指定的单位必须与导入的数据一致。例如，当使用 Flexible Body Model Builder 应用生成的 ROM 数据时，必须将 **Unit System** 参数设置为 `SI (m, kg, s)`，因为生成的 ROM 数据使用 SI 单位。

### **长度单位** — 长度的度量单位 `m`（默认）| `cm` | `mm` | `km` | `in` | `ft` | `yd` | `mi`

用于表示长度的测量单位。

#### 依赖关系

要启用此参数，请将 **Unit System** 设置为 `Custom`。

### **质量单位** — 质量的度量单位 `kg`（默认）| `g` | `t` | `lbm` | `slug`

用于表示质量的测量单位。

#### 依赖关系

要启用此参数，请将 **Unit System** 设置为 `Custom`。

### **时间单位** — 时间的度量单位 s（默认）| `ms` | `min` | `hr`

用于表示时间的测量单位。

#### 依赖关系

要启用此参数，请将 **Unit System** 设置为 `Custom`。

### Interface Frames

### **帧数** — 帧端口数量 `1`（默认）| 正整数

接口坐标系端口的数量，指定为正整数。此数量必须与 ROM 数据中定义的边界节点数量匹配。该参数不支持变量或表达式。

### **Origins** — Cartesian coordinates of interface frame origins `[0 0 0]` (default) | *n*-by-*3* matrix

所有接口坐标系原点的笛卡尔坐标，指定为 *n*×*3* 矩阵。矩阵的每一行代表一个坐标系原点。所有坐标必须相对于公共参考坐标系。降阶模型中的每个边界节点必须在模块上具有对应的接口坐标系。

### **Orientations** — Orientations of interface frames `[1 0 0 0]` (default) | *n*-by-*4* matrix of unit quaternions

接口坐标系的姿态，指定为 *n*×*4* 的单位四元数矩阵，其中 *n* 是接口坐标系的数量。

### Reduced Order Matrices

### **Stiffness Matrix** — 降阶模型的刚度矩阵 `[]`（默认）| *r*×*r* 矩阵

来自 ROM 数据的刚度矩阵，指定为 *r*×*r* 矩阵。刚度矩阵是一个对称矩阵，用于描述柔性体的弹性特性。对于具有 *n* 个边界节点和 *m* 个动态变形模态的 ROM 数据集，刚度矩阵具有 *r* = 6*n* + *m* 行和列。

### **Mass Matrix** — 降阶模型的质量矩阵 `[]`（默认）| *r*×*r* 矩阵

来自 ROM 数据的质量矩阵，指定为 *r*×*r* 矩阵。质量矩阵是一个对称矩阵，用于描述柔性体的惯性特性。对于具有 *n* 个边界节点和 *m* 个动态变形模态的 ROM 数据集，质量矩阵具有 *r* = 6*n* + *m* 行和列。

### Damping

### **Type** — 阻尼方法类型 `Proportional`（默认）| `Uniform Modal` | `Damping Matrix` | `None`

要应用于柔性体的阻尼方法：

- 选择 `Proportional` 以应用比例（或 Rayleigh）阻尼方法。此方法将阻尼矩阵 [*C*] 定义为质量矩阵 [*M*] 和刚度矩阵 [*K*] 的线性组合：

  [C]=α[M]+β[K]，

  其中 *α* 和 *β* 是标量系数。
- 选择 `Uniform Modal` 以应用均匀模态阻尼方法。此方法对固体的所有振动模态应用单一阻尼比。该值越大，振动衰减越快。

  所选择的参考条件会影响阻尼比适用的模态类型。有关参考条件的详细信息，请参阅 Reference Conditions。当对柔性体使用模态降阶时，仅保留模态的一个子集。有关模态降阶的详细信息，请参阅 Reduce the Degrees of Freedom for a Flexible Body。
- 选择 `Damping Matrix` 以使用您通过刚度矩阵和质量矩阵计算得到的降阶阻尼矩阵。例如，您可以使用此选项为柔性体指定模态阻尼模型。
- 选择 `None` 以对无阻尼体进行建模。

### **Mass Coefficient** — 质量矩阵系数 0 `1/s`（默认）| 非负标量

质量矩阵的系数 *α*。此参数定义与质量矩阵 [*M*] 成比例的阻尼。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Proportional`。

### **Stiffness Coefficient** — 刚度矩阵系数 0.001 `s`（默认）| 非负标量

刚度矩阵的系数 *β*。此参数定义与刚度矩阵 [*K*] 成比例的阻尼。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Proportional`。

### **Damping Ratio** — 均匀模态阻尼方法的阻尼比 0.01（默认）| 无量纲非负标量

应用于柔性体所有振动模态的阻尼比 *ζ*。该值越大，振动衰减越快。

当 *ζ* = 0 时，物体无阻尼。如果施加到物体上的边界条件与所选择的参考条件完全匹配，则 *ζ* < 1 会产生欠阻尼模态衰减，*ζ* = 1 对应于临界阻尼，*ζ* > 1 会产生过阻尼耗散。当边界条件与参考条件不匹配时，所选阻尼比的效果会发生变化。有关参考条件的详细信息，请参阅 Reference Conditions。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Uniform Modal`。

**Data Types:** `double`

### **Damping Matrix** — 降阶阻尼矩阵 `[]`（默认）| *r*×*r* 矩阵

降阶阻尼矩阵，指定为 *r*×*r* 矩阵。阻尼矩阵是一个对称矩阵，用于描述柔性体的阻尼特性。在具有 *n* 个边界节点和 *m* 个动态变形模态的柔性体中，阻尼矩阵具有 *r* = 6*n* + *m* 行和列。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Damping Matrix`。

### Reference Conditions

### **Type** — 参考条件类型 `Linearized Mean Axes`（默认）| `Body-Fixed`

指定要应用的参考条件类型。有关详细信息，请参阅参考条件。

- `Linearized Mean Axes`：参考的体坐标系跟随瞬时质心，柔性体表现出无约束的变形振动模态。
- `Body-Fixed`：选择附着于体的坐标系作为参考体坐标系。柔性体的变形表现出自由振动模态振型，在参考体坐标系位置处的平移和旋转变形为零。

### **Frame** — 用于体固定参考条件的连接坐标系 坐标系名称

输入用作参考体坐标系的连接坐标系名称。坐标系名称区分大小写。确保所选坐标系在模块上暴露为端口。不能使用 **R** 坐标系，它是虚拟未变形体的参考坐标系。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Body-Fixed`。

### **Show Port R** — 显示参考坐标系端口 off（默认）| on

选择以暴露 **R** 端口，它表示虚拟未变形体的参考坐标系。请注意，**R** 坐标系在物理上并不附着于柔性体。

**R** 端口不得与任何施加力和力矩或具有惯性的模块刚性连接。

### Fidelity

### **Type** — 柔性体建模方法 `None`（默认）| `Modally Reduced`

用于对柔性体建模的方法，指定为 `None` 或 `Modally Reduced`。

- 如果选择 `None`，模块将对具有所有自由度的柔性体进行建模。
- 如果选择 `Modally Reduced`，模块将对柔性体的质量矩阵和刚度矩阵执行特征值分解。然后可以使用 **Number of Retained Modes** 参数指定仿真所需的柔性体法向模态。

### **Number of Retained Modes** — 保留的法向模态 1（默认）| 非负整数

保留的法向模态，指定为范围 [0, *n*] 内的整数，其中 *n* 等于柔性体的弹性自由度数量。

模块使用此参数指定仿真中保留多少个低频模态。如果将此参数设置为 `0`，柔性体将被视为刚体。数值越大，仿真速度越慢。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Modally Reduced`。

### Graphic

### **Type** — 柔性体的可视化表示 `None`（默认）| `Partitioned Geometry` | `Deformed Geometry`

柔性体的可视化表示，指定为 `None`、`Partitioned Geometry` 或 `Deformed Geometry`。

- 要隐藏体，请使用 `None`。
- 要使用由多个刚性部件组成的近似表示来显示变形体，请使用 `Partitioned Geometry`。在可视化中，模块根据接口坐标系将体分为多个部件，并将每个部件刚性附着到其对应的接口坐标系。
- 要显示体的重建变形形状，请使用 `Deformed Geometry`。模块使用提供的体三角剖分和恢复数据来重建三角剖分上顶点的弹性变形。

### **File Name** — CAD 文件名或 CAD 文件的路径字符向量

CAD 文件名或 CAD 文件的路径，指定为字符向量。如果文件名或路径不包含文件扩展名，模块假定文件类型为 STEP。该模块支持多种格式的 CAD 文件。有关支持的 CAD 文件格式列表，请参阅 Supported Software and File Formats。

根据 CAD 文件的位置，使用以下方法之一指定 **File Name**。

| **位置** | 方法 |
| --- | --- |
| 文件位于当前工作文件夹或 MATLAB® 路径上 | 在文本框中输入文件名。**示例：** `myShape.STEP` |
| 文件位于既不是当前文件夹也不在 MATLAB 路径上的文件夹中 | - 输入 CAD 文件的相对路径，即相对于当前文件夹的路径。**示例：** `Geometries/myShape.STEP, or ../Geometries/myShape.STEP` - 点击 Browsing for CAD file 按钮并浏览到 CAD 文件。- 输入 CAD 文件的完整路径。**示例：** `C:/Users/Model/Geometries/myShape.STEP` |

**提示**

- 在跨多个平台使用该模块或将模型分享给他人时，考虑使用文件名或相对路径。
- 正斜杠 (/) 在任何平台上都是有效的分隔符。反斜杠 (\\) 仅在 Microsoft Windows 平台上有效。

### **Unit Type** — 几何体长度单位的来源 `From File` (默认) | `From Unit System`

实体几何体单位的来源，指定为 `From File` 或 `From Unit System`。选择 `From File` 以使用导入文件中指定的单位。选择 `From Unit System` 以使用 **Unit System** 参数指定的单位。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Partitioned Geometry`。

### **Vertex Coordinates** — 三角剖分表示中顶点的坐标 `[]` (默认) | *nv*×*3* 矩阵

实体的三角剖分表示中顶点的坐标，指定为 *nv*×*3* 矩阵。*nv* 是顶点数，矩阵的每一行包含一个顶点的 *x*、*y* 和 *z* 坐标。坐标参考公共参考坐标系。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Deformed Geometry`。

### **Facet Vertex Indices** — 定义三角剖分表示中各面的顶点索引 `[]` (默认) | *nf*×*3* 矩阵

定义实体三角剖分表示中各面的顶点索引，指定为 *nf*×*3* 矩阵。*nf* 是面数，矩阵的每一行包含定义其对应面的三个顶点的索引。顶点的索引是该顶点在 **Vertex Coordinates** 参数矩阵中的行号。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Deformed Geometry`。

### **Reconstruction Matrix** — 用于可视化变形体的恢复数据 `[]` (默认) | *3nv*×*r* 矩阵

用于可视化变形体的恢复数据，指定为 *3nv*×*r* 矩阵。*nv* 是顶点数，*r* 是 ROM 数据中质量矩阵或刚度矩阵的列数。

Reduced Order Flexible Solid 模块使用重构矩阵来计算三角剖分表示中顶点的位移，以显示物体的变形形状。矩阵中每三行对应一个顶点的 *x*、*y* 和 *z* 位移。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Deformed Geometry`。

### **Visual Properties** — 颜色和不透明度的参数化设置 `From File`（默认）| `Advanced` | `Simple`

用于指定视觉属性的参数化设置。

- 选择 `From File` 以使用导入的 CAD 几何文件中的颜色数据。请注意，并非所有文件格式都允许颜色数据。在允许颜色数据的格式中，该数据通常是可选的。如果您的文件未指定颜色，则实体将以灰色渲染。
- 选择 `Simple` 以指定 **Color** 和 **Opacity**。
- 选择 `Advanced` 以指定更多视觉属性，例如 **Diffuse Color**、**Specular Color**、**Ambient Color**、**Emissive Color** 和 **Shininess**。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Partitioned Geometry`。

### **Color** — 漫反射产生的光线颜色 [0.5 0.5 0.5]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

在直接白光下图形的颜色，指定为 [R G B] 或 [R G B A] 向量，范围为 0–1。可选的第四个元素 (A) 指定颜色的不透明度，范围为 0–1。省略不透明度元素等同于指定值为 1。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Partitioned Geometry`。
2. **Visual Properties** 为 `Simple`。

### **Opacity** — 图形不透明度 1.0（默认）| 0 到 1 范围内的标量

图形不透明度，指定为 0 到 1 范围内的标量。标量为 0 对应完全透明，标量为 1 对应完全不透明。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Partitioned Geometry`。
2. **Visual Properties** 为 `Simple`。

### **Diffuse Color** — 漫反射产生的光线颜色 [0.5 0.5 0.5]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

漫反射产生的光线颜色，指定为 [R,G,B] 或 [R,G,B,A] 向量，值在 0 到 1 范围内。该向量可以是行向量或列向量。可选的第四个元素指定颜色的不透明度。省略不透明度元素等同于指定值为 1。

漫反射颜色反映渲染实体的主色，并提供着色效果，使渲染对象呈现三维外观。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Partitioned Geometry`。
2. **Visual Properties** 为 `Advanced`。

### **Specular Color** — 镜面反射产生的光线颜色 [0.5 0.5 0.5 1.0]（默认）| 值在 0 到 1 范围内的 3×1 或 1×3 向量 | 值在 0 到 1 范围内的 4×1 或 1×4 向量

镜面反射产生的光线颜色，指定为 [R,G,B] 或 [R,G,B,A] 向量，值在 0 到 1 范围内。该向量可以是行向量或列向量。可选的第四个元素指定颜色的不透明度。省略不透明度元素等同于指定值为 1。此参数改变镜面高光的颜色，即由于光源光线反射而在渲染实体上形成的亮点。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Partitioned Geometry`。
2. **Visual Properties** 为 `Advanced`。

### **Ambient Color** — 环境光颜色 [0.15 0.15 0.15 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量 | 取值范围为 0 到 1 的 4×1 或 1×4 向量

环境光的颜色，指定为 [R,G,B] 或 [R,G,B,A] 向量，取值范围为 0 到 1。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值为 1。

环境光是指并非直接来自光源的一般照明水平。环境光由经过多次反射和再反射、不再来自任何特定方向的光组成。您可以调整此参数以更改所渲染实体的阴影颜色。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Partitioned
   Geometry`。
2. **Visual Properties** 为
   `Advanced`。

### **Emissive Color** — 自发光颜色 [0.0 0.0 0.0 1.0]（默认）| 取值范围为 0 到 1 的 3×1 或 1×3 向量

由于自发光而产生的颜色，指定为取值范围为 0 到 1 的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值为 1。

发射颜色是不来自任何外部源的颜色，因此看起来是由实体本身发射的。当实体具有发射颜色时，即使没有外部光源，也可以看到该实体。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Partitioned
   Geometry`。
2. **Visual Properties** 为
   `Advanced`。

### **Shininess** — 所渲染实体的光泽度 75（默认）| 取值范围为 1 到 128 的标量

所渲染实体的光泽度，指定为取值范围为 0 到 128 的标量。此参数影响所渲染实体镜面反射的锐度。光泽度高的实体具有类似镜面的外观，光泽度低的实体具有更低光泽或缎面的外观。

#### 依赖关系

要启用此参数，请设置：

1. **Type** 为 `Partitioned
   Geometry`。
2. **Visual Properties** 为
   `Advanced`。

## 所属库

Simscape / Multibody / Body Elements / Flexible Bodies

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2019b 中引入**

## 描述

使用降阶模型数据创建柔性体

Reduced Order Flexible Solid 模块使用降阶模型 (ROM) 数据创建柔性体。

降阶模型是一种计算高效的模型，用于表征可具有线性弹性变形的柔性体属性。ROM 数据必须包括：

- 指定所有接口坐标系相对于公共参考坐标系的位置和方向的坐标和单位四元数。请参阅 Interface Frames。
- 描述柔性体弹性属性的对称刚度矩阵。请参阅 Stiffness Matrix。
- 描述柔性体惯性属性的对称质量矩阵。请参阅 Mass Matrix。

要生成 ROM 数据，您可以使用 Flexible Body Model Builder 应用程序或有限元分析工具，例如 Partial Differential Equation Toolbox™。通过使用该工具箱，您可以从实体的 CAD 几何开始，生成有限元网格，应用 Craig-Bampton 方法，并生成相应的 ROM 数据。有关详细信息，请参阅 Model an Excavator Dipper Arm as a Flexible Body。

### Common Reference Frame

提供给 Reduced Order Flexible Solid 模块的数据必须参考一个一致的公共参考坐标系。该参考坐标系定义了 *x*、*y* 和 *z* 方向，用于指定物体中所有点的相对位置。该坐标系还定义了与每个接口坐标系相关联的弹性自由度的方向。

### ROM 数据的要求

Reduced Order Flexible Solid 模块的 ROM 数据必须满足以下要求：

- ROM 数据必须至少有一个边界节点。每个边界节点确定一个接口坐标系的位置。
- 每个边界节点必须为降阶模型贡献六个自由度。节点 *i* 的自由度必须按以下顺序保留

  *Ui* =
  [*Txi*,
  *Tyi*,
  *Tzi*,
  *Rxi*,
  *Ryi*,
  *Rzi*]，

  其中：

  - *Txi*、*Tyi* 和 *Tzi* 是沿公共参考坐标系 *x*、*y* 和 *z* 方向的平移自由度。
  - *Rxi*、*Ryi* 和 *Rzi* 是绕公共参考坐标系 *x*、*y* 和 *z* 轴的旋转自由度。

降阶模型还可以包含额外的自由度 *D1*、*D2*、⋯、*Dm*，它们对应于保留的正则振动模态。对于具有 *n* 个边界节点和 *m* 个模态自由度的降阶模型，模型的自由度为：

*U*`reduced`**
= [*U1*,
*U2*, ⋯,
*Un*,
*D1*,
*D2*, ⋯,
*Dm*]。

自由度的数量 *N*`reduced`** 等于 6*n* + *m*，其中包括六个刚体自由度。弹性自由度的数量等于 *N*`reduced`** - 6。自由度的数量决定了刚度矩阵和质量矩阵的大小。对于这些矩阵，行和列的顺序必须与 *U*`reduced`** 的顺序相对应。

### 降低柔性体的自由度

您可以使用该模块进一步减少柔性体的自由度。柔性体的自由度越少，仿真速度越快。

例如，由 Craig-Bampton 方法生成的 ROM 数据集具有两个边界节点和 10 个固定界面正则模态，总共有 22 个自由度。如果使用该 ROM 数据，该模块会生成柔性体的内部表示，其具有六个刚体自由度和 16 个弹性自由度。要进一步减少弹性自由度的数量，您可以将 **Reduction** 设置为 `Modally Reduced`。如果将 **Number of Retained Modes** 指定为 `8`，则柔性体除六个刚体自由度外，还会保留八个最低频率的模态自由度。

### Damping

为了指定柔性体的阻尼特性，该模块有三种阻尼方法：比例阻尼、均匀模态阻尼和阻尼矩阵方法。有关更多信息，请参阅 Damping。

### Simulation Performance

柔性体会增加多体模型的数值刚度。为避免仿真问题，请使用刚性求解器，例如 `ode15s` 或 `ode23t`。

阻尼会显著影响仿真性能。例如，在对阻尼很小或没有阻尼的物体进行建模时，响应中不期望的高频模态会减慢仿真速度。在这种情况下，添加少量阻尼可以提高仿真速度，而不会显著影响模型的精度。
