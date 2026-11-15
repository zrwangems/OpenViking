---
type: simulink-block
title: 'File Solid'
family: 'sm'
product_id: 'sm'
product_name: 'Simscape Multibody'
documentation_release: R2025b
official_category: 'Multibody Modeling / Bodies / Body Elements'
documentation_page: 'filesolid'
documentation_source_path: 'ref/filesolid.html'
language: zh-CN
chinese_source: worker-translation
---

# File Solid

## 端口

### 坐标系

### **R** — 局部参考坐标系 frame

导入实体的局部参考坐标系。此坐标系相对于实体固定。将此坐标系连接到另一个模块，以指定实体的位置和方向。

### 几何

### **CH** — 凸包表示 geometry

表示实体几何的凸包。将此端口连接到 Spatial Contact Force 模块，以在凸包上对接触进行建模。

#### 依赖关系

要启用此端口，请在 **Geometry** 下展开 **Export**，然后选择 **Convex Hull**。

## 参数

### 几何

### **File Name** — CAD 文件名或 CAD 文件路径 character vector

CAD 文件名或 CAD 文件路径，指定为 character vector。如果文件名或路径不包含文件扩展名，模块假定文件类型为 STEP。模块支持多种格式的 CAD 文件。有关支持的 CAD 文件格式列表，请参阅 Supported Software and File Formats。

根据 CAD 文件的位置，使用以下方法之一来指定 **File Name**。

| **Location** | Methods |
| --- | --- |
| File is in the current working folder or on the MATLAB® path | 在文本框中输入文件名。 **示例：** `myShape.STEP` |
| File is in a folder that is neither the current folder nor on the MATLAB path | - 输入 CAD 文件的相对路径，即相对于当前文件夹的路径。 **示例：** `Geometries/myShape.STEP, or   ../Geometries/myShape.STEP` - 单击 Browsing for CAD file 按钮，然后浏览到 CAD 文件。 - 输入 CAD 文件的完整路径。 **示例：** `C:/Users/Model/Geometries/myShape.STEP` |

**提示**

- 在跨多个平台使用该模块或与他人共享模型时，请考虑使用文件名或相对路径。
- 正斜杠 (/) 在任何平台上都是有效的分隔符。反斜杠 (\) 仅在 Microsoft Windows 平台上有效。

### **Unit Type** — 实体几何单位的来源 `From File` (默认) | `Custom`

实体几何单位的来源。选择 `From File` 以使用导入文件中指定的单位。选择 `Custom` 以指定自己的单位。

### **Unit** — 导入文件中指定几何坐标所用的长度单位 `m` (默认) | `cm` | `mm` | `km` | `in` | `ft`

用于解释几何文件中定义的几何的长度单位。更改单位会改变导入几何的比例。

### **Convex Hull** — 生成真实几何的凸包表示 `off` (默认) | `on`

选择 **Convex Hull** 以生成真实几何的凸包表示。选择此参数会启用端口 **CH**。

### 惯性

### **Type** — 要使用的惯性参数化 `Calculate from Geometry` (默认) | `Point Mass` | `Custom`

要使用的惯性参数化。选择 `Point Mass` 以对转动惯性可忽略的集中质量进行建模。选择 `Custom` 以对具有指定惯性矩和惯性积的分布质量进行建模。默认设置 `Calculate from Geometry` 使模块能够根据实体几何以及密度或质量自动计算转动惯性属性。

### **Based on** — 惯性计算中要使用的参数 `Density from File` (默认) | `Custom Density` | `Custom Mass`

惯性计算中要使用的参数。模块根据实体几何和所选参数计算惯性张量。

- `Density from File`：模块根据从 CAD 文件获取的密度计算物体的惯性。请注意，只有某些 CAD 格式包含密度数据。
- `Custom Density`：模块根据对话框中指定的密度计算物体的惯性。
- `Custom Mass`：模块根据对话框中指定的质量计算物体的惯性。

### **Density** — 材料单位体积质量 `1000 kg/m^3` (默认)

材料单位体积的质量。质量密度可以取正值或负值。指定负质量密度以对实体中的空隙或空腔效应进行建模。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Type** 设置为 `Calculate from Geometry`
2. 将 **Based on** 设置为 `Custom Density`

### **Mass** — 实体元素的总质量 `1 kg` (默认) | 带质量单位的标量

要赋予实体元素的总质量。此参数可以为正值或负值。使用负值可捕获复合体（由多个实体和惯性组成）中空隙或空腔的效应，但要注意确保物体总质量整体上为正。

### **Center of Mass** — 质心坐标 `[0 0 0] m` (默认) | 带长度单位的三元素向量

[*x* *y* *z*] 质心相对于模块参考坐标系的坐标。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Custom`。

### **Moments of Inertia** — 惯性张量的对角元素 `[1 1 1] kg*m^2` (默认) | 带质量\*长度^2 单位的三元素向量

三元素向量，包含相对于原点位于质心且各轴平行于模块参考坐标系的坐标系的 [*Ixx* *Iyy* *Izz*] 惯性矩。惯性矩是惯性张量

(IxxIyyIzz)

的对角元素，

其中：

- Ixx=∫m(y2+z2) dm
- Iyy=∫m(x2+z2) dm
- Izz=∫m(x2+y2) dm

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Custom`。

### **Products of Inertia** — 惯性张量的非对角元素 `[0 0 0] kg*m^2` (默认) | 带质量\*长度^2 单位的三元素向量

三元素向量，包含相对于原点位于质心且各轴平行于模块参考坐标系的坐标系的 [*Iyz* *Izx* *Ixy*] 惯性积。惯性积是惯性张量

(IxyIzxIxyIyzIzxIyz)

的非对角元素，

其中：

- Iyz=−∫myz dm
- Izx=−∫mzx dm
- Ixy=−∫mxy dm

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Custom`。

### **Derived Values** — 显示计算得到的惯性属性值按钮

显示计算得到的实体惯性属性值——质量、质心、惯性矩和惯性积。单击 **Update** 按钮以计算并显示实体的属性。在对模块参数进行任何更改后，请单击此按钮，以确保显示的值仍然是最新值。

质心在实体的局部参考坐标系中分解。惯性矩和惯性积分别在惯性分解坐标系中分解——该坐标系的轴平行于参考坐标系的轴，但原点与实体质心重合。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Calculate from Geometry`。

### 图形

### **Type** — 用于可视化的图形 `From Geometry` (默认) | `Marker` | `None`

实体视觉表示的类型，指定为 `From Geometry`、`Marker` 或 `None`。将参数设置为 `From Geometry` 以显示实体的视觉表示。将参数设置为 `Marker` 以将实体表示为标记。将参数设置为 `None` 以在模型可视化中隐藏实体。

### **Visual Properties** — 颜色和不透明度的参数化 `Simple` (默认) | `Advanced`

用于指定视觉属性的参数化。选择 `Simple` 以指定 **Diffuse Color** 和 **Opacity**。选择 `Advanced` 以指定更多视觉属性，例如 **Specular Color**、**Ambient Color**、**Emissive Color** 和 **Shininess**。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `From Geometry` 或 `Marker`。

### **Shape** — 用于表示实体的标记形状 `Sphere` (默认) | `Cube` | `Frame`

用于可视化实体的标记的形状。标记的运动反映实体本身的运动。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Marker`。

### **Size** — 标记宽度（以像素为单位）10 `pixels` (默认) | 标量

标记的宽度（以像素为单位）。此宽度不随缩放级别缩放。请注意，标记的视觉大小部分取决于屏幕分辨率，分辨率越高，单位长度内像素越多，因此生成的图标越小。

#### 依赖关系

要启用此参数，请将 **Type** 设置为 `Marker`。

### **Color** — 漫反射光的颜色 [0.5 0.5 0.5] (默认) | 3×1 或 1×3 向量，取值范围为 0 到 1 | 4×1 或 1×4 向量，取值范围为 0 到 1

图形在直接白光下的颜色，指定为 0–1 范围内的 [R G B] 或 [R G B A] 向量。可选的第四个元素 (A) 指定 0–1 范围内的颜色不透明度。省略不透明度元素等效于指定值 1。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Type** 设置为 `From Geometry` 或 `Marker`
2. 将 **Visual Properties** 设置为 `Simple`

### **Opacity** — 图形不透明度 1.0 (默认) | 取值范围为 0 到 1 的标量

图形不透明度，指定为取值范围为 0 到 1 的标量。标量 0 对应完全透明，标量 1 对应完全不透明。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Type** 设置为 `From Geometry` 或 `Marker`
2. 将 **Visual Properties** 设置为 `Simple`

### **Diffuse Color** — 漫反射光的颜色 [0.5 0.5 0.5] (默认) | 3×1 或 1×3 向量，取值范围为 0 到 1 | 4×1 或 1×4 向量，取值范围为 0 到 1

漫反射光的颜色，指定为取值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

漫反射颜色反映渲染实体的主色，并提供明暗效果，使渲染对象具有三维外观。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Type** 设置为 `From Geometry` 或 `Marker`
2. 将 **Visual Properties** 设置为 `Advanced`

### **Specular Color** — 镜面反射光的颜色 [0.5 0.5 0.5 1.0] (默认) | 3×1 或 1×3 向量，取值范围为 0 到 1 | 4×1 或 1×4 向量，取值范围为 0 到 1

镜面反射光的颜色，指定为取值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。此参数更改镜面高光的颜色，镜面高光是由于光源的光反射而在渲染实体上出现的亮点。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Type** 设置为 `From Geometry` 或 `Marker`
2. 将 **Visual Properties** 设置为 `Advanced`

### **Ambient Color** — 环境光的颜色 [0.15 0.15 0.15 1.0] (默认) | 3×1 或 1×3 向量，取值范围为 0 到 1 | 4×1 或 1×4 向量，取值范围为 0 到 1

环境光的颜色，指定为取值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

环境光是指并非直接来自光源的一般照明水平。环境光由经过多次反射和再反射、不再来自任何特定方向的光组成。您可以调整此参数以更改渲染实体的阴影颜色。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Type** 设置为 `From Geometry` 或 `Marker`
2. 将 **Visual Properties** 设置为 `Advanced`

### **Emissive Color** — 自发光颜色 [0.0 0.0 0.0 1.0] (默认) | 3×1 或 1×3 向量，取值范围为 0 到 1

自发光产生的颜色，指定为取值在 0 到 1 范围内的 [R,G,B] 或 [R,G,B,A] 向量。该向量可以是行向量或列向量。可选的第四个元素指定颜色不透明度。省略不透明度元素等效于指定值 1。

发射颜色是不来自任何外部源的颜色，因此看起来是由实体自身发出的。当实体具有自发光颜色时，即使没有外部光源，也可以看到该实体。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Type** 设置为 `From Geometry` 或 `Marker`
2. 将 **Visual Properties** 设置为 `Advanced`

### **Shininess** — 高光锐度 75 (默认) | 取值限制为 0–128 的标量

镜面光反射的锐度，指定为 0–128 范围内的标量数值。增大 shininess 值可获得更小但更锐利的高光。减小该值可获得更大但更平滑的高光。

#### 依赖关系

要启用此参数，请设置：

1. 将 **Type** 设置为 `From Geometry` 或 `Marker`
2. 将 **Visual Properties** 设置为 `Advanced`

### 坐标系

### **Show Port R** — 显示用于连接到其他模块的参考坐标系端口 on (默认) | off

选择以公开 **R** 端口。

### **New Frame** — 创建用于连接到其他模块的自定义坐标系按钮

单击 Create 按钮 Create 以打开一个窗格，用于创建新的附着于实体的坐标系。在此窗格中，可以指定坐标系的名称、原点和方向。

- 要命名自定义坐标系，请单击 **Frame Name** 参数的文本字段。该名称标识实体模块上以及 Multibody Explorer 的 **Model Tree** 窗格中的对应端口。
- 要选择自定义坐标系的 **Frame Origin**，请使用以下方法之一：

  - **At Reference Frame Origin**：使新坐标系原点与实体的参考坐标系原点重合。
  - **At Center of Mass**：使新坐标系原点与实体的质心重合。
  - **Based on Geometric Feature**：使新坐标系原点与所选特征的中心重合。有效特征包括曲面、线和点。从可视化窗格中选择一个特征，然后单击 **Use Selected Feature** 以确认原点的位置。原点位置的名称会出现在此选项下方的字段中。
- 要定义自定义坐标系的方向，请在 **Frame Axes** 部分下，选择自定义坐标系的 **Primary Axis** 和 **Secondary Axis**，然后指定它们的方向。

  使用以下方法选择用于指定主轴和次轴方向的向量。主轴平行于所选向量，并将其余两个轴约束到其法平面。次轴平行于所选向量在法平面上的投影。

  - **Along Reference Frame Axis**：选择实体参考坐标系的一个轴。
  - **Along Principal Inertia Axis**：选择实体的主惯性轴的一个轴。
  - **Based on Geometric Feature**：选择与实体所选几何特征关联的向量。有效特征包括曲面和线。对应的向量在可视化窗格中由白色箭头指示。您可以从可视化窗格中选择一个特征，然后单击 **Use Selected Feature** 以确认选择。所选特征的名称会出现在此选项下方的字段中。

### **FrameN** — 编辑或删除现有自定义坐标系名称

您已创建的坐标系。`N` 是每个自定义坐标系的唯一标识编号。

- 点击文本字段以编辑现有自定义坐标系的名称。

- 点击 Edit 按钮 Edit 以编辑自定义坐标系的其他方面，例如原点和轴。
- 点击 Delete 按钮 Delete 以删除自定义坐标系。

#### 依赖项

要启用此参数，请点击 **New Frame** 创建坐标系。

## 所属库

Simscape / Multibody / Body Elements

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

### R2023b: 导入装配体

现在，您可以从各种 CAD 格式将装配体导入到 File Solid 模块。File Solid 模块使用 CAD 文件中的默认姿态将导入的装配体表示为一个刚体。该模块忽略所有约束，并假定整个几何体具有一个密度。如果所有零件的密度相同，该模块可以从 CAD 文件获取密度。如果装配体文件没有密度或具有多个密度，则必须显式指定该装配体的惯性属性。

## 描述

属性派生自 CAD 文件的实体

File Solid 模块对具有从 CAD 文件派生的几何、惯性、颜色和参考坐标系的实体进行建模。您可以为导入的实体手动指定惯性和颜色。File Solid 模块可以使用各种 CAD 格式对实体进行建模。

### 支持的软件和文件格式

| CAD | 支持的版本 |
| --- | --- |
| ACIS | 最高 2020 |
| Autodesk® Inventor | 最高 2022 |
| CATIA V4 | 最高 4.2.5 |
| CATIA V5 | 最高 V5-6 R2021 |
| CATIA V6 | 最高 V5-6 R2019(R29) |
| Creo-Pro/E | Pro/Engineer 19.0 到 Creo 8.0 |
| IGES | 5.1、5.2 和 5.3 |
| JT | 最高 v10.5 |
| NX | V11.0 到 NX 18.0，NX 到 NX12，NX 1847 系列到 NX 1980 系列 |
| OBJ | 所有版本 |
| Parasolid | 最高 v33 |
| PRC | 所有版本 |
| Rhino3D | 4 到 7 |
| Solid Edge | V19 - 20、ST - ST10、2021 |
| SolidWorks® | 97 到 2021 |
| STEP | AP 203 E1/E2、AP 214 和 AP 242 |
| STL | 所有版本 |
| U3D | ECMA-363 |

**注意**

该模块无法读取 CAD 工程图，因为它们不包含实体所需的数据。

### 导入零件

File Solid 模块将导入的零件表示为一个刚体。该模块可以从 CAD 文件读取惯性和颜色数据。或者，您可以为导入的零件显式指定这些属性。有关详细信息，请参阅 Inertia 和 Graphic。

File Solid 模块使用惯性坐标系（其原点与质心重合，且轴平行于参考坐标系的轴）来计算导入实体的惯性。计算惯性矩和惯性积所使用的坐标系因 CAD 软件而异。有关如何指定惯性的详细信息，请参阅 Specifying Custom Inertias。

**计算惯性**

如果该模块根据导入实体的几何计算惯性，您可以在模块对话框中查看计算值。展开 **Inertia** 下的 **Derived Values** 节点，然后点击 **Update**。如果几何、密度或质量发生变化，请点击 **Update** 按钮再次计算惯性。所有计算值均采用 SI 单位。

**坐标系**

导入的实体通过坐标系连接。默认情况下，导入的实体具有由端口 **R** 表示的参考坐标系。CAD 文件指定参考坐标系的位置。

如果您需要在实体的不同部分建立连接，或者需要在实体上建立多个连接，可以在实体上创建其他坐标系。每个坐标系都会向该模块添加一个新的坐标系端口。有关创建自定义坐标系的详细信息，请参阅 Frames。

### 导入装配体

File Solid 模块使用 CAD 文件中指定的默认姿态将导入的装配体表示为一个刚体。该模块忽略 CAD 文件中的所有约束，并假定整个装配体具有一个密度。

如果您在 **Inertia** 下将 **Type** 指定为 `Calculate From Geometry`，并将 **Based On** 指定为 `Density`，则 File Solid 模块可以从 CAD 文件读取密度数据。为确保该模块成功读取密度，CAD 文件必须具有整个装配体的密度，并且所有零件的密度要么具有相同值，要么未指定。否则，仿真将返回错误。

您可以手动指定导入装配体的密度、质量或惯性属性。该过程与单个零件的过程相同。有关详细信息，请参阅 Specifying Custom Inertias。

您可以导入其中的零件由不同建模方法表示的装配体，例如分面模型、多边形模型和 BRep 模型。但是，只能对由 BRep 模型表示的零件创建坐标系，因为它们具有必要的边界图元，例如点、边和面。

### 导出几何

File Solid 模块可以在 Simscape Multibody 环境中生成导入 CAD 文件的凸包几何表示。您可以将导出的几何用于空间接触。

如图所示，凸包几何是真实几何的近似。该模块基于其真实几何计算物理属性，例如质量和惯性。

实体真实几何及其对应凸包的图示
