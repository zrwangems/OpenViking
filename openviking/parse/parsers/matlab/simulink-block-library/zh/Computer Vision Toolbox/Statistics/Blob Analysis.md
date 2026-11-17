---
type: simulink-block
title: 'Blob Analysis'
family: 'statistics'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: 'blobanalysis'
documentation_source_path: 'ref/blobanalysis.html'
language: zh-CN
chinese_source: worker-translation
---

# Blob Analysis

## 端口

### 输入

### **BW** — 二值图像 向量 | 矩阵

二值图像，指定为向量或矩阵

**数据类型:** `Boolean`
### 输出

### **Area** — 已标记区域中的 pixels 数量 向量

已标记区域中的 pixels 数量，以向量形式返回。

#### 依赖关系

要启用此端口，请选择 **Area** 参数。

**数据类型:** `int32`

### **Centroid** — 质心坐标 *M*-by-2 矩阵

*M*-by-2 矩阵，包含 *M* 个 blob。

各行表示每个区域质心的坐标，*M* 表示 blob 数量。

例如，有两个 blob，其质心的行和列坐标分别为 *x*1、*y*1 和 *x*2、*y*2。该模块输出：

[x1y1x2y2]

在 **Centroid** 端口。

#### 依赖关系

要启用此端口，请选择 **Centroid** 参数。

**数据类型:** `double` | `single` | `fixed point`

### **BBox** — 边界框坐标 *M*-by-4 矩阵

边界框坐标，以 *M*-by-4 矩阵形式返回，其中包含 *M* 个 blob 的边界框。矩阵的每一行将一个边界框定义为四元素向量 [*x*,*y*,*width*,*height*]，采用 pixel 坐标。各行表示每个边界框的坐标，其中 *M* 表示 blob 数量。

例如，有两个 blob，其中 *x* 和 *y* 定义边界框左上角的位置，*w* 和 *h* 定义边界框的宽度和高度。该模块输出

[x1y1w1h1x2y2w2h2]

在 **BBox** 端口。

#### 依赖关系

要启用此端口，请选择 **Bounding Box** 参数。

## 参数

**Main 选项卡**

### **Area** — 已标记区域中的 pixels 数量 向量

已标记区域中的 pixels 数量，以向量形式返回。

#### 依赖关系

要启用此端口，请选择 **Area** 参数。

### **Centroid** — 质心坐标 *M*-by-2 矩阵

*M*-by-2 矩阵，包含 *M* 个 blob。

各行表示每个区域质心的坐标，*M* 表示 blob 数量。

例如，有两个 blob，其质心的行和列坐标分别为 *x*1、*y*1 和 *x*2、*y*2。该模块输出：

[x1y1x2y2]

在 **Centroid** 端口。

#### 依赖关系

要启用此端口，请选择 **Centroid** 参数。

### **BBox** — 边界框坐标 *M*-by-4 矩阵

边界框坐标，以 *M*-by-4 矩阵形式返回，其中包含 *M* 个 blob 的边界框。矩阵的每一行将一个边界框定义为四元素向量 [*x*,*y*,*width*,*height*]，采用 pixel 坐标。各行表示每个边界框的坐标，其中 *M* 表示 blob 数量。

例如，有两个 blob，其中 *x* 和 *y* 定义边界框左上角的位置，*w* 和 *h* 定义边界框的宽度和高度。该模块输出

[x1y1w1h1x2y2w2h2]

在 **BBox** 端口。

#### 依赖关系

要启用此端口，请选择 **Bounding Box** 参数。

### **Major axis length** — 椭圆的长轴长度 off（默认）| on

启用 **Major axis length** 端口。选中此复选框以输出一个向量，该向量

- 表示椭圆的长轴长度
- 具有与已标记区域相同的归一化二阶中心矩

### **Minor axis length** — 椭圆的短轴长度 off（默认）| on

启用 **Minor axis length** 端口。选中此复选框以输出一个向量，该向量

- 表示椭圆的短轴长度
- 具有与已标记区域相同的归一化二阶中心矩

### **Orientation** — Orientation off（默认）| on

启用 **Orientation** 端口。

选中此复选框以输出一个向量，该向量表示椭圆的长轴与 *x* 轴之间的角度。角度值以 radians 为单位，范围为：−π2 到 π2（含端点）。

### **Eccentricity** — Eccentricity off（默认）| on

启用 **Eccentricity** 端口。选中此复选框以输出一个向量，该向量表示与区域具有相同二阶矩的椭圆的偏心率。

### **Equivalent diameter squared** — Equivalent diameter squared off（默认）| on

启用 **Equivalent diameter squared** 端口。选中此复选框以输出一个向量，该向量表示等效直径的平方。

### **Extent** — Extent off（默认）| on

启用 **Extent** 端口。选中此复选框以输出一个向量，该向量表示将 blob 的面积除以其边界框面积的结果。

### **Perimeter** — 周长长度 off（默认）| on

启用 **Perimeter** 端口。选中此复选框以输出一个 *N*-by-1 向量，其中包含每个 blob 的周长长度，以 pixels 为单位，其中 *N* 是 blob 数量。

### **Statistics output data type** — 输出数据类型 double（默认）| single | specify via Data Types tab

将输出的数据类型指定为 `double`、`single` 或 `Specify via Data Types tab`。

### **Connectivity** — 已标记区域数量 `8`（默认）| `4`

指定每个图像中已标记区域的数量。

定义哪些 pixels 彼此连接。如果要连接位于顶部、底部、左侧和右侧的 pixels，请选择 `4`。如果要将 pixels 连接到顶部、底部、左侧、右侧以及对角线上的其他 pixels，请选择 `8`。有关此参数的更多信息，请参阅 Label 模块。

**Connectivity** 参数还会影响模块计算 blob 周长的方式。例如，此图说明了当您将 **Connectivity** 参数设置为 `4` 时，模块如何计算周长。

该模块计算每个 pixel 中心之间的距离（由黑点标记），并估计周长为 22。

下一幅图说明了当您将 **Connectivity** 参数设置为 `8` 时，模块如何计算 blob 的周长。

该模块围绕 blob 采用不同路径，并估计周长为 18+22。

### **Output label matrix** — 输出标签矩阵 off（默认）| on

启用 **Label** 端口。选中此复选框以输出标签矩阵。等于 `0` 的 pixels 表示背景。等于 `1` 的 pixels 表示第一个对象。等于 `2` 的 pixels 表示第二个对象，依此类推。

**Blob Properties 选项卡**

### **Maximum number of blobs** — 最大 blob 数量 标量

指定每个输入图像中已标记区域的最大数量。该模块使用此值预分配向量和矩阵，以确保它们足够长以容纳统计值。模块输出的最大 blob 数量取决于此参数的值和输入图像的大小。模块输出的 blob 数量可能会受到输入图像大小的限制。

### **Warn if maximum number of blobs is exceeded** — 如果超过最大 blob 数量则发出警告 on（默认）| off

选择此参数可在超过最大 blob 数量时发出警告。

### **Output actual number of blobs** — blob 数量 off（默认）| on

启用 **Count** 端口。选择此参数以输出一个标量值，该值表示每个图像中连通区域的实际数量。

### **Specify minimum blob area in pixels** — 最小 blob 面积，以 pixels 为单位 `0`（默认）| 标量

选择此参数以指定最小 blob 面积，以 pixels 为单位。如果 pixels 数量满足指定的最小大小，则标记该 blob。

**可调:** Yes

### **Specify maximum blob area in pixels** — 最大 blob 面积，以 pixels 为单位 intmax('uint32')（默认）| 标量

选择此参数以指定最大 blob 面积，以 pixels 为单位。如果 pixels 数量满足指定的最大大小，则标记该 blob。允许的最大值是 `uint32` 数据类型的最大值。

**可调:** Yes

### **Exclude blobs touching image border** — 排除接触图像边界的 blob off（默认）| on

指定此参数以排除包含至少一个边界 pixel 的已标记 blob。

### **Output blob statistics as a variable size signal** — 将 blob 统计信息输出为可变大小信号 off（默认）| on

指定此参数以将 blob 统计信息输出为可变大小信号。

### **Fill empty spaces in output** — 填充输出中的空白位置 off（默认）| on

指定此参数以使用您在 **Fill values** 参数中指定的值填充统计向量中的空白位置。

#### 依赖关系

要启用此参数，请清除 **Output blob statistics as a variable size signal** 参数。

### **Fill values** — 用于填充输出中空白位置的标量 `-1`（默认）| 标量 | 向量

指定一个标量值以填充统计向量中的所有空白位置。如果输入向量，则该向量的长度必须与所选统计信息的数量相同。模块使用每个向量元素填充不同的统计向量。如果空白位置不影响您的计算，可以清除 **Fill empty spaces in outputs** 参数。

#### 依赖关系

要启用此参数，请清除 **Output blob statistics as a variable size signal** 参数。

**Data Types 选项卡**

要启用 **Data Types** 选项卡上的选项，请在 **Main** 选项卡中，将 **Statistics output data type** 参数设置为 `Specify via Data Types tab`。有关定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

## 所属库

Computer Vision Toolbox / Statistics

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `doubleb` | `fixed pointbc` | `integerb` | `singleb` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a 当您将 FFT implementation 参数设置为 FFTW，或当变换长度不是 2 的幂时，生成的代码将仅限于 MATLAB 主机计算机。  b 此数据类型在输出端口支持。  c 定点数据类型在 Major Axis、Minor Axis、Orientation 和 Eccentricity 输出端口不受支持。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

已标记区域的统计信息

Blob Analysis 模块计算二值图像中已标记区域的统计信息。该模块返回诸如质心、边界框、标签矩阵和 blob 计数等量。Blob Analysis 模块支持输入和输出可变大小信号。您还可以使用来自 Simulink® 的 Selector (Simulink) 模块，根据 blob 的统计信息选择特定 blob。

有关 pixel 和空间坐标系定义的信息，请参阅 Image Coordinate Systems 和 Coordinate Systems。
