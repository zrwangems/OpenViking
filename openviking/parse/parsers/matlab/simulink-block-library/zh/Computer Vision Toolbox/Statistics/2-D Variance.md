---
type: simulink-block
title: '2-D Variance'
family: 'statistics'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: '2dvariance'
documentation_source_path: 'ref/2dvariance.html'
language: zh-CN
chinese_source: worker-translation
---

# 2-D Variance

## 端口

### 输入

### **In** — 输入数组 向量 | 矩阵 | 数组

输入数组，指定为向量、矩阵或 *N-D* 数组。在选择 **Enable ROI processing** 参数之前，此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是

### **Rst** — 复位端口 标量

复位端口，指定为标量。此端口指定导致模块复位运行方差的事件。**Rst** 输入的采样时间必须是正整数，并且是输入采样时间的倍数。

#### 依赖关系

要启用此端口，请选择 **Running variance** 参数，并将 **Reset port** 参数设置为 `Rising edge`、`Falling edge`、`Either edge` 或 `Non-zero sample`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **ROI** — 感兴趣区域 向量 | 矩阵

感兴趣区域 (ROI)，指定为四元素向量、*m*-by-4 矩阵或 *M*-by-*N* 矩阵。此端口的输入值取决于 **ROI type** 参数。

**注意**

仅当输入为 2-D 图像时，才能使用 `ROI` 端口。

#### 依赖关系

要启用此端口，请将 **Find the variance value over** 参数设置为 `Entire input`，并选择 **Enable ROI processing** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **Label** — 标签矩阵 矩阵

标签矩阵，指定为非负整数矩阵。标签矩阵表示图像中的对象。标记为 0 的像素是背景。标记为 1 的像素构成一个对象；标记为 2 的像素构成第二个对象；依此类推。标签矩阵的大小必须与 2-D 输入的大小相同。

#### 依赖关系

要启用此端口，请选择 **Enable ROI processing** 参数，并将 **ROI type** 参数设置为 `Label matrix`。

**数据类型：** `uint8` | `uint16` | `uint32`

### **Label Numbers** — ROI 的标签值 向量

ROI 的标签值，指定为 *M* 元素向量。*M* 的值可以小于或等于标签矩阵中已标记的对象数量。

#### 依赖关系

要启用此端口，请选择 **Enable ROI processing** 参数，并将 **ROI type** 参数设置为 `Label matrix`。

**数据类型：** `uint8` | `uint16` | `uint32`
### 输出

### **Out** — 计算得到的输出方差 标量 | 向量 | 矩阵 | *N-D* 数组

计算得到的输出方差，返回为标量、向量、矩阵或 *N-D* 数组。返回的输出方差大小取决于输入大小，以及 **Running variance** 和 **Find the variance value over** 参数的设置。

在选择 **Output flag indicating if ROI is within image bounds** 并将 **ROI type** 参数设置为 `Rectangles`、`Lines` 或 `Label matrix` 之前，此端口未命名。

#### 如果清除了 **Running variance**

可以沿输入的任意指定维度或整个输入计算方差。输出为：

- 如果输入为任意大小，且 **Find the variance value over** 参数设置为 `Entire input`，则为标量。
- 如果输入为矩阵，且 **Find the variance value over** 参数设置为 `Each row`、`Each column` 和 `Specified dimension` 中的任意一个，则为向量。在这种情况下，`Specified dimension` 的 **Dimension** 值可以为 1 或 2。
- 如果输入为 3-D 数组，且 **Find the variance value over** 参数设置为 `Specified dimension`，并且 **Dimension** 值为 3，则为矩阵。
- 如果输入为 *N-D* 数组，且 **Find the variance value over** 参数设置为除 `Entire input` 以外的选项，则为 *N-D* 数组。

  如果沿输入的 *N* 维计算方差，则返回的输出为 *(N-1)-D* 数组。在这种情况下，`Specified dimension` 的 **Dimension** 值设置为 *N*。

  **示例：** 对于大小为 *M*-by-*N*-by-*P* 的 3-D 输入数组，返回输出的维度为：

  - 如果将 **Find the variance value over** 参数设置为 `Entire row`，则为 1-by-*N*-by-*P*。
  - 如果将 **Find the variance value over** 参数设置为 `Entire column`，则为 *M*-by-1-by-*P*。
  - 如果将 **Find the variance value over** 参数设置为 `Specified dimension`，并将 **Dimension** 值设置为 3，则为 *M*-by-*N*。

#### 如果选中了 **Running variance**

选中 **Running variance** 参数时，该模块会计算输入中每个样本相对于所有先前样本的方差。输出与输入大小相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **Flag** — ROI 验证 `0` | `1`

ROI 验证，返回为 0 或 1。输出值表示输入处指定的所有 ROI 是否都位于图像边界内。输出值取决于 **Output** 和 **ROI Type** 参数的值。

|  |  |  |  |
| --- | --- | --- | --- |
| **ROI Type** | **Output** | **Flag 端口输出** | **描述** |
| - `Rectangles` - `Lines` | `Individual statistics for each ROI` | 0 | ROI 完全在输入图像外部。 |
| 1 | ROI 完全或部分位于输入图像内部。 |
| `Single statistic for all ROIs` | 0 | ROI 完全在输入图像外部。 |
| 1 | ROI 完全或部分位于输入图像内部。 |
| `Label matrix` | `Individual statistics for each ROI` | 0 | 标签编号不在标签矩阵中。 |
| 1 | 标签编号在标签矩阵中。 |
| `Single statistic for all ROIs` | 0 | 标签编号都不在标签矩阵中。 |
| 1 | 至少有一个标签编号在标签矩阵中。 |

**注意**

如果 ROI 部分在图像外部，则该模块仅对位于图像边界内的 ROI 部分计算方差值。

#### 依赖关系

要启用此端口，请选择 **Output flag indicating if ROI is within image bounds** 参数，并将 **ROI type** 参数的值设置为 `Rectangle`、`Lines` 或 `Label Matrix`。

## 参数

### 主要

### **Running variance** — 跟踪运行方差 `off` (默认) | `on`

选中此项可跟踪模块连续输入的方差。在此模式下，该模块将每个元素视为一个通道。

### **Reset port** — 复位事件 `None` (默认) | `Rising edge` | `Falling edge` | `Either edge` | `Non-zero sample`

指定模块何时检测复位事件。当在可选的 **Rst** 端口检测到复位事件时，该模块会复位运行方差。复位采样时间必须是正整数，并且是输入采样时间的倍数。

将复位事件指定为：

- `None` 以禁用 **Rst** 端口。
- `Rising edge` 以在 **Rst** 输入执行以下操作之一时触发复位事件：

  - 从负值上升到正值或零
  - 从零上升到正值，其中该上升不是从负值上升到零的延续
- `Falling edge` 以在 **Rst** 输入执行以下操作之一时触发复位事件：

  - 从正值下降到负值或零
  - 从零下降到负值，其中该下降不是从正值下降到零的延续

- `Either edge` 以在 **Rst** 输入为 `Rising edge` 或 `Falling edge` 时触发复位事件。
- `Non-zero sample` 以在每个采样时间，当 **Rst** 输入不为零时触发复位事件。

  **注意**

  在 Simulink® 多任务模式下运行仿真时，复位信号有一个采样延迟。因此，当该模块检测到复位事件时，在模块应用复位之前，复位端口速率处会有一个采样延迟。

#### 依赖关系

要启用此参数，请选择 **Running variance** 参数。

### **Find the variance value over** — 计算方差所沿的维度 `Entire input` (默认) | `Each row` | `Each column` | `Specified dimension`

指定该模块计算方差所沿的输入维度。

- `Entire input` — 在整个输入上计算方差。
- `Each row` — 在每一行上计算方差。
- `Each column` — 在每一列上计算方差。
- `Specified dimension` — 在 **Dimension** 参数中指定的维度上计算方差。

  - 如果 **Dimension** 为 1，则输出与选择 `Each column` 时相同。
  - 如果 **Dimension** 为 2，则输出与选择 `Each row` 时相同。

#### 依赖关系

要启用此参数，请清除 **Running variance** 参数。

### **Dimension** — 自定义维度 `1` (默认) | 标量

将计算方差的输入数组维度指定为从 1 开始的值。此参数的值必须大于 0 且小于或等于输入数组中的维度数。

#### 依赖关系

要启用此参数，请将 **Find the variance value over** 参数设置为 `Specified dimension`。

**ROI 处理**

### **Enable ROI processing** — 计算特定区域内的方差 `off` (默认) | `on`

选中此项可计算图像中特定 ROI 内的方差。

**注意**

仅当您拥有 Computer Vision Toolbox™ 许可证时，才可使用完整的 ROI 处理。如果您没有 Computer Vision Toolbox 许可证，仍可以使用 ROI 处理，但 **ROI type** 仅限于 `Rectangles`。

#### 依赖关系

要启用此参数，请将 **Find the variance value over** 参数设置为 `Entire input`。

### **ROI type** — ROI 类型 `Rectangles` (默认) | `Lines` | `Label matrix` | `Binary mask`

指定表示图像中区域的 ROI 类型，该模块在这些区域上计算方差。ROI 类型可以是矩形、线、标签矩阵或二值掩膜。

|  |  |  |
| --- | --- | --- |
| **参数** | | **描述** |
| **ROI type** | **ROI 端口的输入** |
| `Rectangles` | - 四元素行向量    `[x y width   height]` - *m*-by-4 矩阵  [x1y1width1height1x2y2width2height2⋮⋮⋮⋮xMyMwidthMheightM]  ，其中 *m* 是矩形数量。矩阵的每一行对应一个不同的矩形。 | - `x` 和 `y` 是矩形左上角从 1 开始的坐标。 - `width` 和 `height` 是矩形的宽度和高度，以像素为单位。`width` 和 `height` 的值必须大于 0。 |
| `Lines` | - 四元素行向量    `[x1   y1 x2   y2]` - *m*-by-4 矩阵    [x11y11x12y12x21y21x22y22⋮⋮⋮⋮xM1yM1xM2yM2]  ，其中 *m* 是线数量。矩阵的每一行对应一条不同的线。 | - `x1` 和 `y1` 是线起点的坐标。 - `x2` 和 `y2` 是线终点的坐标。 |
| `Label matrix` | *M*-by-*N* 矩阵 | 与输入图像大小相同的矩阵。该矩阵包含表示图像中不同对象的标签值。标记为 0 的像素是背景。标记为 1 的像素构成一个对象；标记为 2 的像素构成第二个对象；依此类推。 |
| `Binary mask` | *M*-by-*N* 矩阵 | 与输入图像大小相同的矩阵。二值掩膜将图像像素分类为属于感兴趣区域或背景。掩膜像素值为 1 表示图像像素属于 ROI。掩膜像素值为 0 表示图像像素是背景的一部分。 |

#### 依赖关系

要启用此参数，请选择 **Enable ROI processing** 参数。

### **ROI portion to process** — 要计算方差的 ROI 部分 `Entire ROI` (默认) | `ROI perimeter`

指定该模块要从中计算 2-D 方差的 ROI 部分。ROI 部分可以是整个 ROI 或 ROI 周长。

#### 依赖关系

要启用此参数，请选择 **Enable ROI processing** 参数，并将 **ROI type** 参数设置为 `Rectangles`。

### **Output** — 计算各个 ROI 或整个 ROI 的方差 `Individual statistics for each ROI` (默认) | `Single statistic for all ROIs`

指定是分别为每个 ROI 计算 2-D 方差，还是为整个 ROI 计算 2-D 方差。

- 如果选择 `Individual statistics for each ROI`，则该模块输出方差值向量。输出向量的大小等于 ROI 的数量。
- 如果选择 `Single statistic for all ROIs`，则该模块输出标量值。该标量值表示所有指定 ROI 的统计值。

#### 依赖关系

要启用此参数，请选择 **Enable ROI processing** 参数，并将 **ROI type** 参数设置为 `Rectangles`、`Lines` 或 `Label matrix`。

### **Output flag indicating if ROI is within image bounds** — 启用 Flag 端口 `off` (默认) | `on`

选中此项可显示 **Flag** 端口。有关 **Flag** 端口输出的说明，请参阅 Flag。

#### 依赖关系

要启用此参数，请选择 **Enable ROI processing** 参数，并将 **ROI type** 参数设置为 `Rectangles`、`Lines` 或 `Label matrix`。

### 数据类型

有关定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

### **Lock data type settings against change by the fixed-point tools** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选中此参数可防止定点工具覆盖您在此模块中指定的数据类型。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

## 所属库

Computer Vision Toolbox / Statistics

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算输入或输入序列的方差

2-D Variance 模块计算输入数组的无偏方差。输入可以是 1-D 向量、2-D 矩阵或 *N-D* 数组。该模块可以沿输入的指定维度或整个输入计算方差。如果选中 **Running variance** 参数，该模块还可以跟踪一段时间内输入序列的方差。
