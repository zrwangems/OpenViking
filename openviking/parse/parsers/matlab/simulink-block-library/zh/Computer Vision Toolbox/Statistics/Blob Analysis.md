---
type: simulink-block
title: 'Blob Analysis'
family: 'vision'
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
```yaml
ports:
- name: BW
  summary: 二值图像 向量 | 矩阵
  direction: input
  data_types: Boolean
- name: Area
  summary: 标记区域中的像素数 向量
  direction: output
  data_types: int32
- name: Centroid
  summary: 质心坐标 *M*×2 矩阵
  direction: output
  data_types: double | single | fixed point
- name: BBox
  summary: 边界框坐标 *M*×4 矩阵
  direction: output
```

### 输入

### **BW** — 二值图像 向量 | 矩阵

二值图像，指定为向量或矩阵

**数据类型：** `Boolean`
### 输出

### **Area** — 标记区域中的像素数 向量

标记区域中的像素数，以向量形式返回。

#### 依赖关系

要启用此端口，请选中 **Area** 参数。

**数据类型：** `int32`

### **Centroid** — 质心坐标 *M*×2 矩阵

由 *M* 个斑点的质心坐标构成的 *M*×2 矩阵。

各行表示每个区域的质心坐标，
*M* 表示斑点的数量。

例如，有两个斑点，其质心的行坐标和列坐标分别为 *x*1、
*y*1 和
*x*2、
*y*2。该模块输出：

[x1y1x2y2]

输出端口为 **Centroid**。

#### 依赖关系

要启用此端口，请选中 **Centroid** 参数。

**数据类型：** `double` | `single` | `fixed point`

### **BBox** — 边界框坐标 *M*×4 矩阵

边界框坐标，以 *M*×4 矩阵形式返回，该矩阵包含
*M* 个斑点的边界框。矩阵的每一行都将一个
边界框定义为四元素向量
[*x*,*y*,*width*,*height*]，
并采用像素坐标。各行表示每个边界框的坐标，其中
*M* 表示斑点的数量。

例如，有两个斑点，其中 *x* 和
*y* 定义边界框左上角的位置，
*w* 和 *h* 定义边界框的宽度和高度。该模块输出：

[x1y1w1h1x2y2w2h2]

输出端口为 **BBox**。

#### 依赖关系

要启用此端口，请选中 **Bounding Box**
参数。
## 参数
```yaml
parameters:
- name: Area
  summary: 标记区域中的像素数 向量
  group: ''
- name: Centroid
  summary: 质心坐标 *M*×2 矩阵
  group: ''
- name: BBox
  summary: 边界框坐标 *M*×4 矩阵
  group: ''
- name: Major axis length
  summary: 椭圆长轴的长度 off（默认） | on
  group: ''
- name: Minor axis length
  summary: 椭圆短轴的长度 off（默认） | on
  group: ''
- name: Orientation
  summary: 方向 off（默认）| on
  group: ''
- name: Eccentricity
  summary: 离心率 off（默认）| on
  group: ''
- name: Equivalent diameter squared
  summary: 等效直径平方 off（默认）| on
  group: ''
- name: Extent
  summary: 延展度 off（默认）| on
  group: ''
- name: Perimeter
  summary: 周长 off（默认）| on
  group: ''
- name: Statistics output data type
  summary: 输出数据类型 double（默认）| single | 通过 Data Types 选项卡指定
  group: ''
- name: 连通性
  summary: 标记区域数 8（默认） | 4
  group: ''
- name: 输出标签矩阵
  summary: 输出标签矩阵 off（默认） | on
  group: ''
- name: 最大团块数
  summary: 最大团块数 scalar
  group: ''
- name: 超过最大团块数时发出警告
  summary: 超过最大团块数时发出警告 on（默认） | off
  group: ''
- name: 输出实际斑点数
  summary: 斑点数 off (默认值) | on
  group: ''
- name: 以像素为单位指定最小斑点面积
  summary: 以像素为单位的最小斑点面积 0 (默认值) | 标量
  group: ''
- name: 以像素为单位指定最大斑点面积
  summary: 以像素为单位的最大斑点面积 intmax('uint32') (默认值) | 标量
  group: ''
- name: 排除接触图像边界的斑点
  summary: 排除接触图像边界的斑点 off (默认值) | on
  group: ''
- name: 将斑点统计信息作为可变大小信号输出
  summary: 将斑点统计信息作为可变大小信号输出 off (默认值) | on
  group: ''
- name: 填充输出中的空白
  summary: 填充输出中的空白 off (默认值) | on
  group: ''
- name: 填充值
  summary: 用于填充输出中空白位置的标量 -1（默认） | scalar | vector
  group: ''
```

**主选项卡**

### **Area** — 标记区域中的像素数 向量

标记区域中的像素数，以向量形式返回。

#### 依赖关系

要启用此端口，请选中 **Area** 参数。

### **Centroid** — 质心坐标 *M*×2 矩阵

对应 *M* 个斑点的 *M*×2 矩阵。

各行表示每个区域的质心坐标，*M* 表示斑点数量。

例如，有两个斑点，其质心的行坐标和列坐标分别为 *x*1、*y*1 和 *x*2、*y*2。该模块输出：

[x1y1x2y2]

在 **Centroid** 端口输出。

#### 依赖项

要启用此端口，请选中 **Centroid** 参数。

### **BBox** — 边界框坐标 *M*×4 矩阵

边界框坐标，以 *M*×4 矩阵形式返回，其中包含 *M* 个斑点的边界框。矩阵的每一行都将一个边界框定义为采用像素坐标的四元素向量 [*x*,*y*,*width*,*height*]。各行表示每个边界框的坐标，其中 *M* 表示斑点数量。

例如，有两个斑点，*x* 和 *y* 定义边界框左上角的位置，*w* 和 *h* 定义边界框的宽度和高度。该模块输出

[x1y1w1h1x2y2w2h2]

在 **BBox** 端口输出。

#### 依赖项

要启用此端口，请选中 **Bounding Box** 参数。

### **Major axis length** — 椭圆长轴的长度 off（默认） | on

启用 **Major axis length** 端口。选中此复选框可输出一个满足以下条件的向量：

- 表示椭圆长轴的长度
- 与标记区域具有相同的归一化二阶中心矩

### **Minor axis length** — 椭圆短轴的长度 off（默认） | on

启用 **Minor axis length** 端口。选中此复选框可输出一个满足以下条件的向量：

- 表示椭圆短轴的长度
- 与标记区域具有相同的归一化二阶中心矩

### **Orientation** — 方向 off（默认）| on

启用 **Orientation** 端口。

选中此复选框可输出一个向量，该向量表示各椭圆长轴与 *x* 轴之间的夹角。角度值以 radians 为单位，取值范围为：−π/2 至 π/2（含端点）。

### **Eccentricity** — 离心率 off（默认）| on

启用 **Eccentricity** 端口。选中此复选框可输出一个向量，该向量表示与区域具有相同二阶矩的椭圆的离心率。

### **Equivalent diameter squared** — 等效直径平方 off（默认）| on

启用 **Equivalent diameter squared** 端口。选中此复选框可输出一个向量，该向量表示等效直径的平方。

### **Extent** — 延展度 off（默认）| on

启用 **Extent** 端口。选中此复选框可输出一个向量，该向量表示将各团块的面积除以其边界框面积所得到的结果。

### **Perimeter** — 周长 off（默认）| on

启用 **Perimeter** 端口。选中此复选框可输出一个 *N*×1 向量，其中包含每个团块的周长（以 pixels 为单位），*N* 为团块的数量。

### **Statistics output data type** — 输出数据类型 double（默认）| single | 通过 Data Types 选项卡指定

将输出的数据类型指定为 `double`、`single` 或 `Specify via Data Types tab`。

### **连通性** — 标记区域数 `8`（默认） | `4`

指定每个图像中标记区域的数量。

定义像素之间的连接方式。如果要连接位于上、下、左、右方向的像素，请选择 `4`。如果要将像素与位于其上、下、左、右及对角线方向的其他像素连接，请选择 `8`。有关此参数的更多信息，请参阅 Label 模块。

**连通性**参数还会影响模块计算团块周长的方式。例如，此图说明了将**连通性**参数设置为 `4` 时，模块如何计算周长。

该模块计算各像素中心（由黑点标记）之间的距离，并估计周长为 22。

下一图说明了将**连通性**参数设置为 `8` 时，模块如何计算团块的周长。

该模块沿团块周围采用不同的路径，并估计周长为 18+22。

### **输出标签矩阵** — 输出标签矩阵 off（默认） | on

启用 **Label** 端口。选中此复选框可输出标签矩阵。值为 `0` 的像素表示背景。值为 `1` 的像素表示第一个对象。值为 `2` 的像素表示第二个对象，依此类推。

**团块属性选项卡**

### **最大团块数** — 最大团块数 scalar

指定每个输入图像中标记区域的最大数量。模块使用该值预分配向量和矩阵，以确保其长度足以保存统计值。模块输出的团块最大数量同时取决于此参数的值和输入图像的大小。模块输出的团块数量可能受输入图像大小的限制。

### **超过最大团块数时发出警告** — 超过最大团块数时发出警告 on（默认） | off

选择此参数可在超过最大团块数时发出警告。

### **输出实际斑点数** — 斑点数 off (默认值) | on

启用 **Count** 端口。选中此参数可输出一个标量值，该值表示每幅图像中连接区域的实际数量。

### **以像素为单位指定最小斑点面积** — 以像素为单位的最小斑点面积 `0` (默认值) | 标量

选中此参数可指定以像素为单位的最小斑点面积。如果斑点的像素数符合指定的最小尺寸要求，则对该斑点进行标记。

**可调：** 是

### **以像素为单位指定最大斑点面积** — 以像素为单位的最大斑点面积 intmax('uint32') (默认值) | 标量

选中此参数可指定以像素为单位的最大斑点面积。如果斑点的像素数符合指定的最大尺寸要求，则对该斑点进行标记。最大允许值为 `uint32` 数据类型的最大值。

**可调：** 是

### **排除接触图像边界的斑点** — 排除接触图像边界的斑点 off (默认值) | on

选中此参数可排除包含至少一个边界像素的已标记斑点。

### **将斑点统计信息作为可变大小信号输出** — 将斑点统计信息作为可变大小信号输出 off (默认值) | on

选中此参数可将斑点统计信息作为可变大小信号输出。

### **填充输出中的空白** — 填充输出中的空白 off (默认值) | on

选中此参数可使用您在 **填充值** 参数中指定的值填充统计向量中的空位。

#### 依赖关系

要启用此参数，请取消选中 **将斑点统计信息作为可变大小信号输出** 参数。

### **填充值** — 用于填充输出中空白位置的标量 `-1`（默认） | scalar | vector

指定一个标量值，以填充统计向量中的所有空白位置。如果输入向量，则其长度必须与所选统计量的数量相同。模块使用向量的每个元素填充不同的统计向量。如果空白位置不影响计算，则可以取消选中 **填充输出中的空白** 参数。

#### 依赖关系

要启用此参数，请取消选中 **将 blob 统计量作为可变大小信号输出** 参数。

**数据类型选项卡**

要启用 **数据类型** 选项卡上的选项，请在 **主** 选项卡中，将 **统计量输出数据类型** 参数设置为 `Specify via Data Types tab`。有关定点模块参数的详细信息，请参阅为模块指定定点属性 (DSP System Toolbox)。
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
| a 当将 FFT 实现参数设置为 FFTW，或变换长度不是 2 的幂时，生成的代码将只能在 MATLAB 主机计算机上运行。  b 输出端口支持此数据类型。  c Major Axis、Minor Axis、Orientation 和 Eccentricity 输出端口不支持定点数据类型。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

标记区域的统计信息

Blob Analysis 模块计算二值图像中标记区域的统计信息。该模块返回质心、边界框、标签矩阵和斑点数量等统计量。Blob Analysis 模块支持可变大小的输入和输出信号。您还可以使用 Simulink® 中的 Selector (Simulink) 模块，根据斑点的统计信息选择特定斑点。

有关像素坐标系和空间坐标系定义的信息，请参阅图像坐标系和坐标系。
