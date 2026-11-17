---
type: simulink-block
title: '2-D Minimum'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: '2dminimum'
documentation_source_path: 'ref/2dminimum.html'
language: zh-CN
chinese_source: worker-translation
---

# 2-D Minimum

## 端口

### 输入

### **In** — 输入数组 标量 | 向量 | 矩阵 | *N* 维数组

输入数组，指定为向量、矩阵或 *N* 维数组。

#### 依赖

仅当您选择 **Enable ROI processing** 参数或将 **Mode** 参数设置为 `Running` 时，该端口才会被命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是

### **Rst** — 重置运行最小值 标量

重置运行最小值，指定为标量。该端口指定导致模块重置运行最小值的事件。**Rst** 输入的采样时间必须为正整数，且为模块输入采样时间的倍数。

#### 依赖

要启用此端口，请将 **Mode** 参数设置为 `Running`，并将 **Reset port** 参数设置为 `Rising edge`、`Falling edge`、`Either edge` 或 `Non-zero sample`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **ROI** — 感兴趣区域 四元素向量 | *m*×4 矩阵 | *M*×*N* 矩阵

感兴趣区域 (ROI)，指定为四元素向量、*m*×4 矩阵或 *M*×*N* 矩阵。该端口根据 **ROI type** 参数的设置接受不同的输入值。

**注意**

- 仅当 **In** 端口的输入为二维图像时，才能使用 **ROI** 端口。
- 如果 **Mode** 参数设置为 `Running`，则不能使用 **ROI** 端口。

#### 依赖

要启用此端口，请将 **Find the minimum value over** 参数设置为 `Entire input`，并选择 **Enable ROI processing** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **Label** — 标签矩阵 非负整数矩阵

标签矩阵，指定为非负整数矩阵。标签矩阵表示二维图像中的对象。标记为 `0` 的像素为背景。标记为 `1` 的像素构成第一个对象，标记为 `2` 的像素构成第二个对象，依此类推。标签矩阵的大小必须与二维输入图像的大小相同。

#### 依赖

要启用此端口，请选择 **Enable ROI processing** 参数，并将 **ROI type** 参数设置为 `Label matrix`。

**注意**

如果 **Mode** 参数设置为 `Running`，则不能启用 **Label** 端口。

**数据类型：** `uint8` | `uint16` | `uint32`

### **Label Numbers** — ROI 的标签值 *M* 元素向量

ROI 的标签值，指定为 *M* 元素向量。这表示标签矩阵中对应数字的对象名称。*M* 必须小于或等于标签矩阵中的对象数量。

#### 依赖

要启用此端口，请选择 **Enable ROI processing** 参数，并将 **ROI type** 参数设置为 `Label matrix`。

**注意**

如果 **Mode** 参数设置为 **Running**，则不能启用 `Label Numbers` 端口。

**数据类型：** `uint8` | `uint16` | `uint32`
### 输出

### **Val** — 输入的最小值 标量 | 向量 | 矩阵 | *N* 维数组

输入的最小值，以标量、向量、矩阵或 *N* 维数组形式返回。此输出的大小取决于输入的大小以及 **Mode** 和 **Find the minimum value over** 参数的设置。

**注意**

如果 **Mode** 参数设置为 `Running`，则该端口未命名。如果 **Mode** 参数设置为 `Index`，则该端口不显示。

#### 计算输入数组的最小值

将 **Mode** 参数设置为 `Value and Index` 或 `Value`。模块沿输入的指定维度或跨整个输入计算最小值。输出最小值的大小取决于输入的大小以及 **Find the Minimum value over** 参数的设置。

- 标量 — 输入为任意大小，且 **Find the minimum value over** 参数设置为 `Entire input`。
- 向量 — 输入为矩阵，且 **Find the minimum value over** 参数设置为 `Each row`、`Each column` 或 `Specified dimension`。如果选择 `Specified dimension`，则 **Dimension** 参数的值必须为 `1` 或 `2`。
- (*N*–1) 维数组 — 输入为 *N* 维数组，**Find the minimum value over** 参数设置为 `Specified dimension`，且 **Dimension** 参数的值为 *N*。
- 具有一个单一维度的 *N* 维数组 — 输入为 *N* 维数组，且 **Find the minimum value over** 参数设置为 `Each row`、`Each column` 或 `Specified dimension`。如果选择 `Specified dimension`，则 **Dimension** 参数的值必须为小于 *N* 的整数。

  **示例：** 对于大小为 *M*×*N*×*P* 的三维输入数组，返回输出的维度为：

  - 1×*N*×*P*，如果将 **Find the minimum value over** 参数设置为 `Entire row`。
  - *M*×1×*P*，如果将 **Find the minimum value over** 参数设置为 `Entire column`。
  - *M*×*N*，如果将 **Find the minimum value over** 参数设置为 `Specified dimension`，并将 **Dimension** 参数设置为 `3`。

#### 计算输入序列的最小值

将 **Mode** 参数设置为 `Running`。模块查找给定序列中所有输入的最小值，并将其编译为单个数组。输出的大小与输入相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **Idx** — 输入中最小值的索引 标量 | 向量 | 矩阵 | *N* 维数组

输入数组中最小值的索引，以标量、向量、矩阵或 *N* 维数组形式返回。

要启用此端口，请将 **Mode** 参数设置为 `Value and Index` 或 `Index`。输出的大小取决于输入的大小以及 **Find the minimum value over** 参数的设置。

- 标量 — 输入为 *N* 元素向量，且 **Find the minimum value over** 参数设置为 `Entire input`。
- 向量 — 输入为矩阵，且 **Find the minimum value over** 参数设置为 `Entire input`、`Each row`、`Each column` 或 `Specified dimension`。如果选择 `Specified dimension`，则 **Dimension** 参数的值必须为 `1` 或 `2`。
- (*N*–1) 维数组 — 输入为 *N* 维数组，**Find the minimum value over** 参数设置为 `Specified dimension`，且 **Dimension** 参数的值为 *N*。
- 具有一个单一维度的 *N* 维数组 — 输入为 *N* 维数组，且 **Find the minimum value over** 参数设置为 `Each row`、`Each column` 或 `Specified dimension`。如果选择 `Specified dimension`，则 **Dimension** 参数的值必须为小于 *N* 的整数。

  **示例：** 对于大小为 *M*×*N*×*P* 的三维输入数组，返回输出的维度为：

  - 1×*N*×*P*，如果将 **Find the minimum value over** 参数设置为 `Entire row`。
  - *M*×1×*P*，如果将 **Find the minimum value over** 参数设置为 `Entire column`。
  - *M*×*N*，如果将 **Find the minimum value over** 参数设置为 `Specified dimension`，并将 **Dimension** 参数设置为 `3`。

**注意**

当最小值出现多次时，计算得到的索引对应于第一次出现的位置。例如，如果输入向量为 `[3 2 1 2 1]`，则最小值为 `1`，最小值的基于一的索引为 `3`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Flag** — ROI 验证 标量 | 向量

ROI 验证，以逻辑 `1` (`true`) 或 `0` (`false`) 的标量或向量形式返回。如果 **ROI type** 参数设置为 `Rectangles` 或 `Lines`，则输出表示指定的 ROI 是完全或部分位于输入图像内。如果 **ROI type** 参数设置为 `Label matrix`，则输出表示 **Label Numbers** 输入中指定的标签编号是否存在于输入标签矩阵中。

|  |  |  |
| --- | --- | --- |
| **ROI type** | **每个 ROI 的单独统计量** | **所有 ROI 的单一统计量** |
| `Rectangles` | 该端口返回一个 *m* 元素向量，其中 *m* 是 **ROI** 端口输入中 *m*×4 矩阵的行数。该向量的每个元素为 `1` 或 `0`，表示矩形 ROI 完全或部分位于输入图像内 (`1`) 或完全位于输入图像外 (`0`)。 | 该端口返回一个标量。该标量为 `1` 或 `0`，表示 **ROI** 输入中的任一矩形完全或部分位于输入图像内 (`1`) 或完全位于输入图像外 (`0`)。 |
| `Lines` | 该端口返回一个标量。该标量为 `1` 或 `0`，表示给予 **ROI** 端口的输入完全或部分位于输入图像内 (`1`) 或完全位于输入图像外 (`0`)。 | 该端口返回一个标量。该标量为 `1` 或 `0`，表示给予 **ROI** 端口的输入完全或部分位于输入图像内 (`1`) 或完全位于输入图像外 (`0`)。 |
| `Label matrix` | 该端口返回一个 *M* 元素向量，其中 *M* 是 **Label Numbers** 端口输入中的元素数量。该向量的每个元素为 `1` 或 `0`，表示 **Label Numbers** 输入中的关联标签存在于 (`1`) 或不存在于 (`0`) Label Matrix 输入中。 | 该端口返回一个标量。该标量为 `1` 或 `0`，表示 **Label Numbers** 输入中的任一标签存在于 (`1`) 或全部不存在于 (`0`) Label Matrix 输入中。 |

**注意**

如果 ROI 部分位于图像外，模块仅计算位于图像边界内的 ROI 部分的统计值。

#### 依赖

要启用此端口，请选择 **Output flag indicating if ROI is within image bounds** 参数，并将 **ROI type** 参数的值设置为 `Rectangle` 或 `Lines`，或者选择 **Output flag indicating if input label numbers are valid** 参数，并将 **ROI type** 参数的值设置为 `Label matrix`。

## 参数

**主**

### **Mode** — 输出模式 `Value and Index`（默认）| `Value` | `Index` | `Running`

将模块的输出模式指定为以下选项之一。

- `Value and Index` — 同时返回给定输入中的最小值及其对应的索引。
- `Value` — 仅返回最小值。
- `Index` — 仅返回给定输入中最小值的索引。
- `Running` — 跟踪一系列输入中的最小值。

### **Index Base** — 第一个元素的索引 `One`（默认）| `Zero`

指定输入数组中第一个元素的索引。

- `One` 表示基于一的编号。每个维度的索引值范围为 1 到 *m*，其中 *m* 是该维度的长度。例如，矩阵中第一个元素的索引为 (`1,1`)。
- `Zero` 表示基于零的编号。每个维度的索引值范围为 0 到 *m*–1，其中 *m* 是该维度的长度。例如，矩阵中第一个元素的索引为 (`0,0`)。

### **Find the minimum value over** — 计算最小值的维度 `Entire input`（默认）| `Each row` | `Each column` | `Specified dimension`

指定模块沿其计算最小值的输入维度。

- `Entire input` — 在整个输入上计算最小值。
- `Each row` — 在每一行上计算最小值。
- `Each column` — 在每一列上计算最小值。
- `Specified dimension` — 在 **Dimension** 参数指定的维度上计算最小值。

  - 如果 **Dimension** 参数设置为 `1`，则输出与选择 `Each column` 时相同。
  - 如果 **Dimension** 参数设置为 `2`，则输出与选择 `Each row` 时相同。

#### 依赖

要启用此参数，请将 **Mode** 参数设置为 `Value and Index`、`Value` 或 `Index`。

### **Dimension** — 自定义维度 `1`（默认）| 正标量

将模块沿其计算最小值的输入数组维度指定为基于一的值。此参数的值必须大于零且小于或等于输入数组的维度数。

#### 依赖

要启用此参数，请将 **Find the minimum value over** 参数设置为 `Specified dimension`。

### **Reset port** — 重置事件 `None`（默认）| `Rising edge` | `Falling edge` | `Either edge` | `Non-zero sample`

指定模块检测为重置事件的内容。当在 **Rst** 端口检测到重置事件时，模块重置运行最小值。重置采样时间必须为正整数，且为输入采样时间的倍数。

将重置事件指定为以下选项之一。

- `None` — 禁用 **Rst** 端口。
- `Rising edge` — 当 **Rst** 输入执行以下操作之一时触发重置事件。

  - 从负值上升到正值或零
  - 从零上升到正值，其中该上升不是从负值上升到零的延续
- `Falling edge` — 当 **Rst** 输入执行以下操作之一时触发重置事件。

  - 从正值下降到负值或零
  - 从零下降到负值，其中该下降不是从正值下降到零的延续

- `Either edge` — 当 **Rst** 输入为 `Rising edge` 或 `Falling edge` 时触发重置事件。
- `Non-zero sample` — 在每个采样时间触发重置事件，其中 **Rst** 输入不为零。

  **注意**

  在 Simulink® 多任务模式下运行仿真时，重置信号有一个采样延迟。在这种情况下，当模块检测到重置事件时，在模块应用重置之前，在 **Rst** 端口速率下存在一个采样延迟。

#### 依赖

要启用此参数，请将 **Mode** 参数设置为 `Running`。

### **Enable ROI processing** — 计算 ROI 内的最小值 `off`（默认）| `on`

选择以计算图像中 ROI 内的最小值。

**注意**

完整的 ROI 处理仅在您拥有 Computer Vision Toolbox™ 许可证时可用。如果您没有 Computer Vision Toolbox 许可证，仍然可以使用 ROI 处理，但 **ROI type** 参数仅限于 `Rectangles`。

#### 依赖

要启用此参数，请将 **Find the minimum value over** 参数设置为 `Entire input`。

### **ROI type** — ROI 的格式 `Rectangles`（默认）| `Lines` | `Label matrix` | `Binary mask`

指定表示图像中区域的 ROI 格式，用于在其上计算最小值。ROI 的类型可以是矩形、线、标签矩阵或二值掩膜。

|  |  |  |
| --- | --- | --- |
| **ROI type** | **输入到 ROI 端口的内容** | **描述** |
| `Rectangles` | - 四元素行向量    [*x y width   height*] - *m*×4 矩阵：  [x1y1width1height1x2y2width2height2⋮⋮⋮⋮xMyMwidthMheightM]  ，其中 *m* 是矩形 ROI 的数量。矩阵的每一行对应一个不同的矩形。 | - *x* 和 *y* 是矩形左上角的从 1 开始的坐标。 - *width* 和 *height* 是矩形的宽度和高度，以像素为单位。*width* 和 *height* 的值必须大于零。 |
| `Lines` | - 四元素行向量    [*x*1   *y*1   *x*2   *y*2] - *m*×4 矩阵    [x11y11x12y12x21y21x22y22⋮⋮⋮⋮xM1yM1xM2yM2]  ，其中 *m* 是线的数量。矩阵的每一行对应一条不同的线。 | - *x*1 和 *y*1 是线起点的坐标。 - *x*2 和 *y*2 是线终点的坐标。 |
| `Label matrix` | *M*×*N* 矩阵 | 与输入图像大小相同的矩阵。该矩阵包含表示图像中不同对象的标签值。标记为 `0` 的像素是背景。标记为 `1` 的像素构成一个对象，标记为 `2` 的像素构成第二个对象，依此类推。 |
| `Binary mask` | *M*×*N* 矩阵 | 与输入图像大小相同的矩阵。二值掩膜将图像像素分类为属于感兴趣区域或背景。二值掩膜值为 `1` 表示对应的图像像素属于 ROI。二值掩膜值为 `0` 表示对应的图像像素是背景的一部分。 |

#### 依赖关系

要启用此参数，请将 **Find the minimum value over** 参数设置为 `Entire input`，并选中 **Enable ROI processing** 参数。

### **ROI portion to process** — 计算最小值的 ROI 部分 `Entire ROI`（默认）| `ROI perimeter`

指定模块计算二维最小值的 ROI 部分。

- `Entire ROI` — 模块计算整个矩形 ROI 区域上的最小值。
- `ROI perimeter` — 模块沿矩形 ROI 的周长计算最小值。

#### 依赖关系

要启用此参数，请选中 **Enable ROI processing** 参数，并将 **ROI type** 参数设置为 `Rectangles`。

### **Output** — 为 ROI 计算单个或统一的最小值 `Individual statistics for each ROI`（默认）| `Single statistic for all ROIs`

指定是为每个 ROI 单独计算二维最小值，还是跨所有 ROI 计算。

- 如果选择 `Individual statistics for each ROI`，模块输出一个最小值向量，每个元素代表一个 ROI。输出向量的大小等于 ROI 的数量。
- 如果选择 `Single statistic for all ROIs`，模块输出一个标量值。该标量值是所有指定 ROI 中的最小值。

#### 依赖关系

要启用此参数，请选中 **Enable ROI processing** 参数，并将 **ROI type** 参数设置为 `Rectangles`、`Lines` 或 `Label matrix`。

### **Output flag indicating if ROI is within image bounds** — 启用 Flag 端口 `off`（默认）| `on`

选中以启用 Flag 输出端口。

**注意**

当 **ROI type** 参数设置为 `Label matrix` 时，此参数的名称变为 **Output flag indicating if input label numbers are valid**。

#### 依赖关系

要启用此参数，请选中 **Enable ROI processing** 参数，并将 **ROI type** 参数设置为 `Rectangles` 或 `Lines`。

**数据类型**

有关定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

### **Lock data type settings against change by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选中此参数可防止定点工具覆盖您在此模块中指定的数据类型。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

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

**在 R2006a 之前引入**

## 描述

查找输入或输入序列中的最小值

二维最小值模块识别输入中最小元素的值，并可选地识别其位置。输入可以是向量、矩阵或 *N* 维数组。该模块沿输入的指定维度或跨整个输入识别最小值。当 **Mode** 参数设置为 `Running` 时，它还会跟踪一段时间内输入序列中的最小值。
