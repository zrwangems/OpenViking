---
type: simulink-block
title: '2-D Maximum'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: '2dmaximum'
documentation_source_path: 'ref/2dmaximum.html'
language: zh-CN
chinese_source: worker-translation
---

# 2-D Maximum

## 端口

### 输入

### **In** — 输入数组 向量 | 矩阵 | *N-D*- 数组

输入数组，指定为向量、矩阵或 *N-D*- 数组。除非选择 **Enable ROI processing** 参数或将 **Mode** 参数设置为 `Running`，否则此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持：** Yes

### **Rst** — 复位端口 标量

复位端口，指定为标量。此端口指定导致模块重置运行最大值的事件。**Rst** 输入的采样时间必须为正整数，并且是输入采样时间的倍数。

#### 依赖关系

要启用此端口，请将 **Mode** 参数设置为 `Running`，并将 **Reset port** 参数设置为 `Rising edge`、`Falling edge`、`Either edge` 或 `Non-zero sample`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **ROI** — 感兴趣区域 四元素向量 | *m*-by-4 矩阵 | *M*-by-*N* 矩阵

感兴趣区域 (ROI)，指定为四元素向量、*m*-by-4 矩阵或 *M*-by-*N* 矩阵。此端口的输入值取决于 **ROI type** 参数。

**注意**

仅当输入为矩阵时，才能使用 `ROI` 端口。

#### 依赖关系

要启用此端口，请将 **Find the maximum value over** 参数设置为 `Entire input`，并选择 **Enable ROI processing** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Label** — 标签矩阵 非负整数矩阵

标签矩阵，指定为非负整数矩阵。标签矩阵表示图像中的对象。标签为 0 的像素是背景。标签为 1 的像素构成一个对象；标签为 2 的像素构成第二个对象；依此类推。标签矩阵的大小必须与 2-D 输入的大小相同。

#### 依赖关系

要启用此端口，请选择 **Enable ROI processing** 参数，并将 **ROI type** 参数设置为 `Label matrix`。

**数据类型：** `uint8` | `uint16` | `uint32`

### **Label Numbers** — ROI 的标签值 *M* 元素向量

ROI 的标签值，指定为 *M* 元素向量。*M* 的值可以小于或等于标签矩阵中标记的对象数量。

#### 依赖关系

要启用此端口，请选择 **Enable ROI processing** 参数，并将 **ROI type** 参数设置为 `Label matrix`。

**数据类型：** `uint8` | `uint16` | `uint32`
### 输出

### **Val** — 输出最大值 标量 | 向量 | 矩阵 | *N-D*-数组

输出最大值，以标量、向量、矩阵或 *N-D*-数组形式返回。返回的最大值的大小取决于输入的大小以及 **Find the maximum value over** 参数的设置。

如果 **Mode** 设置为 `Running`，则此端口未命名。

#### 计算输入数组的最大值

**Mode** 参数设置为 `Value and Index` 或 `Value`。在这种情况下，可以沿输入的任意指定维度或整个输入计算最大值。输出最大值为：

- 如果输入为任意大小且 **Find the maximum value over** 参数设置为 `Entire input`，则为标量。
- 如果输入为矩阵且 **Find the maximum value over** 参数设置为 `Each row`、`Each column` 和 `Specified dimension` 中的任意一个，则为向量。在这种情况下，`Specified dimension` 的 **Dimension** 值可以是 1 或 2。
- 如果输入为 *N*-D 数组，**Find the maximum value over** 参数设置为 `Specified dimension`，且 **Dimension** 值为 *N*，则为 (*N-1*)-D 数组。
- 如果输入为 *N*-D 数组，**Find the maximum value over** 参数设置为 `Each row`、`Each column` 和 `Specified dimension` 中的任意一个，则为带一个单一维度的 *N*-D 数组。

  **示例：** 对于大小为 *M*-by-*N*-by-*P* 的 3-D 输入数组，返回输出的维度为：

  - 如果将 **Find the maximum value over** 参数设置为 `Entire row`，则为 1-by-*N*-by-*P*。
  - 如果将 **Find the maximum value over** 参数设置为 `Entire column`，则为 *M*-by-1-by-*P*。
  - 如果将 **Find the maximum value over** 参数设置为 `Specified dimension` 且 **Dimension** 值为 3，则为 *M*-by-*N*。

#### 计算输入序列的最大值

当将 **Mode** 参数设置为 `Running` 时，模块计算相对于输入序列中每个样本的最大值。输出与输入大小相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **Idx** — 输入数组中最大值的索引 标量 | 向量 | 矩阵 | *N-D*-数组

输入数组中最大值的索引，以标量、向量、矩阵或 *N-D*-数组形式返回。返回索引的大小取决于输入的大小以及 **Find the maximum value over** 参数的设置。

要启用此端口，请将 **Mode** 参数设置为 `Value and Index` 或 `Index`。输出返回的索引为：

- 如果输入为 N 元素向量且 **Find the maximum value over** 参数设置为 `Entire input`，则为标量。
- 如果输入为矩阵且 **Find the maximum value over** 参数设置为 `Entire input`、`Each row`、`Each column` 和 `Specified dimension` 中的任意一个，则为向量。在这种情况下，`Specified dimension` 的 **Dimension** 值可以是 1 或 2。
- 如果输入为 *N*-D 数组，**Find the maximum value over** 参数设置为 `Specified dimension`，且 **Dimension** 值为 *N*，则为 (*N-1*)-D 数组。
- 如果输入为 *N*-D 数组，则为带一个单一维度的 *N*-D 数组。在这种情况下，**Find the maximum value over** 参数设置为 `Each row`、`Each column` 或 `Specified dimension`。在这种情况下，`Specified dimension` 的 **Dimension** 值为小于 *N* 的整数。

  **示例：** 对于大小为 *M*-by-*N*-by-*P* 的 3-D 输入数组，返回输出的维度为：

  - 如果将 **Find the maximum value over** 参数设置为 `Entire row`，则为 1-by-*N*-by-*P*。
  - 如果将 **Find the maximum value over** 参数设置为 `Entire column`，则为 *M*-by-1-by-*P*。
  - 如果将 **Find the maximum value over** 参数设置为 `Specified dimension` 且 **Dimension** 值为 3，则为 *M*-by-*N*。

**注意**

当最大值出现多次时，计算得到的索引对应于第一次出现。例如，在输入向量 `[3 2 1 2 3]` 中，最大值为 3，最大值的基于一的索引为 `1`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **Flag** — ROI 的验证 0 | 1

ROI 的验证，返回为 0 或 1。输出值表示输入中指定的所有 ROI 是否都位于图像边界内。输出值取决于 **Output** 和 **ROI Type** 参数的值。

|  |  |  |  |
| --- | --- | --- | --- |
| **ROI Type** | **Output** | **Output from Flag port** | **描述** |
| - `Rectangles` - `Lines` | `Individual statistics for each ROI` | 0 | ROI 完全位于输入图像之外。 |
| 1 | ROI 完全或部分位于输入图像内。 |
| `Single statistic for all ROIs` | 0 | ROI 完全位于输入图像之外。 |
| 1 | ROI 完全或部分位于输入图像内。 |
| `Label matrix` | `Individual statistics for each ROI` | 0 | 标签编号不在标签矩阵中。 |
| 1 | 标签编号在标签矩阵中。 |
| `Single statistic for all ROIs` | 0 | 所有标签编号都不在标签矩阵中。 |
| 1 | 至少有一个标签编号在标签矩阵中。 |

**注意**

如果 ROI 部分位于图像之外，则模块仅针对位于图像边界内的 ROI 部分计算方差值。

#### 依赖关系

要启用此端口，请选择 **Output flag indicating if ROI is within image bounds** 参数，并将 **ROI type** 参数的值设置为 `Rectangle`、`Lines` 或 `Label Matrix`。

## 参数

**主选项卡**

### **Mode** — 输出模式 `Value and Index` (default) | `Value` | `Index` | `Running`

指定模块要返回的输出类型。选择输出模式为：

- `Value and Index`，返回给定输入中的最大值以及对应索引。
- `Value`，仅返回计算出的最大值。
- `Index`，仅返回给定输入中最大值的索引。
- `Running`，返回输入序列中的最大值。

### **Index Base** — 索引起点 `One` (default) | `Zero`

指定输入数组中第一个元素的索引。选择索引起点为：

- `One`，用于基于一的编号。N-D 输入数组中元素的索引值范围设置为 (1, N)。例如，矩阵中第一个元素的索引值设置为 (1,1)。
- `Zero`，用于基于零的编号。N-D 输入数组中元素的索引值范围设置为 (0, N-1)。例如，矩阵中第一个元素的索引值设置为 (0,0)。

### **Find the maximum value over** — 计算最大值所沿的维度 `Entire input` (default) | `Each row` | `Each column` | `Specified dimension`

指定模块沿其计算最大值的输入维度。

- `Entire input` — 在整个输入上计算最大值。
- `Each row` — 在每一行上计算最大值。
- `Each column` — 在每一列上计算最大值。
- `Specified dimension`— 在 **Dimension** 参数指定的维度上计算最大值。

  - 如果 **Dimension** 为 1，则输出与选择 `Each column` 时相同。
  - 如果 **Dimension** 为 2，则输出与选择 `Each row` 时相同。

#### 依赖关系

要启用此参数，请将 **Mode** 参数设置为 `Value and Index`、`Value` 或 `Index`。

### **Dimension** — 自定义维度 1 (default) | 标量

将计算最大值所沿的输入数组维度指定为基于一的值。此参数的值必须大于 0，且小于或等于输入数组中的维度数。

#### 依赖关系

要启用此参数，请将 **Find the maximum value over** 参数设置为 `Specified dimension`。

### **Reset port** — 复位事件 `None` (default) | `Rising edge` | `Falling edge` | `Either edge` | `Non-zero sample`

指定模块何时检测复位事件。当在可选的 **Rst** 端口检测到复位事件时，模块重置运行模式。复位采样时间必须为正整数，并且是输入采样时间的倍数。

将复位事件指定为：

- `None`，禁用 **Rst** 端口。
- `Rising edge`，当 **Rst** 输入执行以下操作之一时触发复位事件：

  - 从负值上升到正值或零
  - 从零上升到正值，其中该上升不是从负值上升到零的延续
- `Falling edge`，当 **Rst** 输入执行以下操作之一时触发复位事件：

  - 从正值下降到负值或零
  - 从零下降到负值，其中该下降不是从正值下降到零的延续

- `Either edge`，当 **Rst** 输入为 `Rising edge` 或 `Falling edge` 时触发复位事件。
- `Non-zero sample`，当 **Rst** 输入不为零时，在每个采样时间触发复位事件。

  **注意**

  在 Simulink® 多任务模式下运行仿真时，复位信号具有一个样本的延迟。因此，当模块检测到复位事件时，在模块应用复位之前，复位端口速率下会有一个样本的延迟。

#### 依赖关系

要启用此参数，请将 **Mode** 参数设置为 `Running`。

**ROI 处理**

### **Enable ROI processing** — 计算特定区域内的最大值 off (default) | on

选择此项可计算图像中特定 ROI 内的最大值。

**注意**

完整的 ROI 处理仅在拥有 Computer Vision Toolbox™ 许可证时可用。如果没有 Computer Vision Toolbox 许可证，仍可使用 ROI 处理，但 **ROI type** 仅限于 `Rectangles`。

#### 依赖关系

要启用此参数，请将 **Find the maximum value over** 参数设置为 `Entire input`。

### **ROI type** — ROI 类型 `Rectangles` (default) | `Lines` | `Label matrix` | `Binary mask`

指定表示图像中区域的 ROI 类型，模块在这些区域上计算方差。ROI 类型可以是矩形、线条、标签矩阵或二值掩码。

|  |  |  |
| --- | --- | --- |
| **参数** | | **描述** |
| **ROI type** | **ROI 端口的输入** |
| `Rectangles` | - 四元素行向量    `[x y width   height]` - *m*-by-4 矩阵  [x1y1width1height1x2y2width2height2⋮⋮⋮⋮xMyMwidthMheightM]  ,  其中 *m* 是矩形数量。矩阵的每一行对应一个不同的矩形。 | - `x` 和 `y` 是矩形左上角的基于一的坐标。 - `width` 和 `height` 是矩形的宽度和高度，单位为 pixels。`width` 和 `height` 的值必须大于 0。 |
| `Lines` | - 四元素行向量    `[x1   y1 x2   y2]` - *m*-by-4 矩阵    [x11y11x12y12x21y21x22y22⋮⋮⋮⋮xM1yM1xM2yM2]  ,  其中 *m* 是线条数量。矩阵的每一行对应一条不同的线。 | - `x1` 和 `y1` 是线条起点的坐标。 - `x2` 和 `y2` 是线条终点的坐标。 |
| `Label matrix` | *M*-by-*N* 矩阵 | 与输入图像大小相同的矩阵。该矩阵包含表示图像中不同对象的标签值。标签为 0 的像素是背景。标签为 1 的像素构成一个对象；标签为 2 的像素构成第二个对象；依此类推。 |
| `Binary mask` | *M*-by-*N* 矩阵 | 与输入图像大小相同的矩阵。二值掩码将图像像素分类为属于感兴趣区域或背景。掩码像素值为 1 表示图像像素属于 ROI。掩码像素值为 0 表示图像像素是背景的一部分。 |

#### 依赖关系

要启用此参数，请将 **Find the maximum value over** 参数设置为 `Entire input`，并选择 **Enable ROI processing** 参数。

### **ROI portion to process** — 计算最大值所在的 ROI 部分 `Entire ROI` (default) | `ROI perimeter`

指定模块必须从中计算 2-D 最大值的 ROI 部分。ROI 部分可以是整个 ROI 或 ROI 周长。

#### 依赖关系

要启用此参数，请选择 **Enable ROI processing** 参数，并将 **ROI type** 参数设置为 `Rectangles`。

### **Output** — 计算单个 ROI 或整个 ROI 的最大值 `Individual statistics for each ROI` (default) | `Single statistic for all ROIs`

指定是为每个 ROI 单独计算 2-D 最大值，还是为整个 ROI 计算 2-D 最大值。

- 如果选择 `Individual statistics for each ROI`，模块输出最大值向量。输出向量的大小等于 ROI 数量。
- 如果选择 `Single statistic for all ROIs`，模块输出标量值。该标量值表示所有指定 ROI 的统计值。

#### 依赖关系

要启用此参数，请选择 **Enable ROI processing** 参数，并将 **ROI type** 参数设置为 `Rectangles`、`Lines` 或 `Label matrix`。

### **输出标志，指示 ROI 是否在图像边界内** — 启用 Flag 端口 off（默认） | on

选择此项可显示 **Flag** 端口。有关 **Flag** 端口输出的描述，请参阅 Flag。

#### 依赖关系

要启用此参数，请选择 **启用 ROI 处理** 参数，并将 **ROI 类型** 参数设置为 `Rectangles`、`Lines` 或 `Label matrix`。

**Data Types 选项卡**

有关定点模块参数的详细信息，请参阅为模块指定定点属性 (DSP System Toolbox)。

### **锁定数据类型设置，防止其被定点工具更改** — 防止定点工具覆盖数据类型 off（默认） | on

选择此参数可防止定点工具覆盖您在此模块中指定的数据类型。有关详细信息，请参阅锁定输出数据类型设置 (Fixed-Point Designer)。

## 所属库

Computer Vision Toolbox / Statistics

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011a 中引入**

## 描述

计算输入或输入序列的最大值

2-D Maximum 模块识别输入数组中最大元素的索引。输入可以是 1-D 向量、2-D 矩阵或 *N-D* 数组。该模块可以沿输入的指定维度或整个输入计算最大值。2-D Maximum 模块还可以在一段时间内跟踪输入序列中的最大值。
