---
type: simulink-block
title: '2-D Mean'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: '2dmean'
documentation_source_path: 'ref/2dmean.html'
language: zh-CN
chinese_source: worker-translation
---

# 2-D Mean

## 端口
```yaml
ports:
- name: I
  summary: 输入数组 向量 | 矩阵 | *N* 维数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: Rst
  summary: 重置运行均值 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: ROI
  summary: 感兴趣区域 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Label
  summary: 标签矩阵 矩阵
  direction: input
  data_types: uint8 | uint16 | uint32
- name: Label Numbers
  summary: ROI 的标签值 向量
  direction: input
  data_types: uint8 | uint16 | uint32
- name: Out
  summary: 输入的均值 标量 | 向量 | 矩阵 | *N* 维数组
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: Flag
  summary: ROI 验证 标量 | 向量
  direction: output
  data_types: Boolean
```

### 输入

### **I** — 输入数组 向量 | 矩阵 | *N* 维数组

输入数组，指定为向量、矩阵或 *N* 维数组。除非您选中 **Enable ROI processing** 参数，或者选中 **Running mean** 参数并将 **Reset port** 参数设置为 `None` 以外的值，否则此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`
**复数支持：** 是

### **Rst** — 重置运行均值 标量

重置运行均值，指定为标量。此端口指定导致模块重置运行均值的事件。**Rst** 输入的采样时间必须为正整数，并且是模块采样时间的倍数。

#### 依赖关系

要启用此端口，请选中 **Running mean** 参数，并将 **Reset port** 参数设置为以下选项之一：

- `Rising edge`
- `Falling edge`
- `Either edge`
- `Non-zero sample`

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **ROI** — 感兴趣区域 向量 | 矩阵

感兴趣区域 (ROI)，指定为四元素向量、*m*×4 矩阵或 *M*×*N* 矩阵。此端口接受的输入值取决于 **ROI type** 参数的设置。

**注意**

该模块仅对二维输入图像支持 **ROI** 端口。

#### 依赖关系

要启用此端口，请选中 **Enable ROI processing** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Label** — 标签矩阵 矩阵

标签矩阵，指定为非负整数矩阵。标签矩阵基于逐像素表示二维图像中的对象。标记为 `0` 的像素表示背景，标记为 `1` 的像素构成第一个对象，标记为 `2` 的像素构成第二个对象，依此类推。标签矩阵的大小必须与二维输入图像的大小相同。

#### 依赖关系

要启用此端口，请选中 **Enable ROI processing** 参数，并将 **ROI type** 参数设置为 `Label matrix`。

**数据类型：** `uint8` | `uint16` | `uint32`

### **Label Numbers** — ROI 的标签值 向量

ROI 的标签值，指定为 *M* 元素向量。使用此向量指定模块为其计算统计量的对象。向量的每个元素必须对应于标签矩阵中的一个已标记对象。*M* 必须小于或等于标签矩阵中的对象数。

#### 依赖关系

要启用此端口，请选中 **Enable ROI processing** 参数，并将 **ROI type** 参数设置为 `Label matrix`。

**数据类型：** `uint8` | `uint16` | `uint32`
### 输出

### **Out** — 输入的均值 标量 | 向量 | 矩阵 | *N* 维数组

输入的均值，以标量、向量、矩阵或 *N* 维数组形式返回。此输出的大小取决于输入的大小和模块的参数设置。除非您选中 **Output flag indicating if ROI is within image bounds** 或 **Output flag indicating if input label numbers are valid** 参数，否则此端口未命名。

#### 计算输入数组的均值

该模块沿输入的指定维度或跨整个输入计算均值。该模块返回的输出为：

- 标量 — 输入为任意大小，且 **Find the mean value over** 参数设置为 `Entire input`。
- 向量 — 输入为矩阵，且 **Find the mean value over** 参数设置为 `Each row`、`Each column` 或 `Specified dimension`。如果选择 `Specified dimension`，则 **Dimension** 参数的值必须为 `1` 或 `2`。
- (*N*–1) 维数组 — 输入为 *N* 维数组，**Find the mean value over** 参数设置为 `Specified dimension`，且 **Dimension** 参数的值为 *N*。
- 具有一个单一维度的 *N* 维数组 — 输入为 *N* 维数组，且 **Find the mean value over** 参数设置为 `Each row`、`Each column` 或 `Specified dimension`。如果选择 `Specified dimension`，则 **Dimension** 参数的值必须是小于 *N* 的整数。

  **示例：** 对于大小为 *M*×*N*×*P* 的三维输入数组，返回输出的维度为：

  - 如果将 **Find the mean value over** 参数设置为 `Entire row`，则为 1×*N*×*P* 数组。
  - 如果将 **Find the mean value over** 参数设置为 `Entire column`，则为 *M*×1×*P* 数组。
  - 如果将 **Find the mean value over** 参数设置为 `Specified dimension`，并将 **Dimension** 参数设置为 `3`，则为 *M*×*N* 矩阵。

#### 计算输入序列的均值

选中 **Running mean** 参数。该模块在整个序列中查找输入每个元素的均值，并将它们合并为单个数组。输出的大小与输入相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **Flag** — ROI 验证 标量 | 向量

ROI 验证，以逻辑值的标量或向量形式返回。如果 **ROI type** 参数设置为 `Rectangles` 或 `Lines`，则输出表示指定的 ROI 是完全还是部分位于输入图像内。如果 **ROI type** 参数设置为 `Label matrix`，则输出表示 **Label Numbers** 输入中指定的标签编号是否存在于输入标签矩阵中。此输出的大小取决于 **Output** 参数设置为 `Individual statistics for each ROI` 还是 `Single statistic for all ROIs`。

|  |  |  |
| --- | --- | --- |
| **ROI type** | `Individual statistics for each ROI` | `Single statistic for all ROIs` |
| `Rectangles` 或 `Lines` | 该端口返回 *M* 元素逻辑值向量，其中 *M* 是在 **ROI** 端口指定的区域数。当 ROI 完全或部分位于输入图像内时，向量的对应元素为 `1`。当 ROI 完全位于输入图像外时，向量的对应元素为 `0`。 | 该端口返回逻辑标量。当所有 ROI 完全位于输入图像外时，标量为 `0`。否则，标量为 `1`。 |
| `Label matrix` | 该端口返回 *M* 元素逻辑值向量，其中 *M* 是在 **Label Numbers** 端口指定的输入中的元素数。当指定的标签编号存在于标签矩阵中时，向量的对应元素为 `1`，不存在时为 `0`。 | 该端口返回逻辑标量。当 **Label Numbers** 端口指定的向量的所有元素都不存在于标签矩阵中时，标量为 `0`。否则，标量为 `1`。 |

**注意**

如果 ROI 部分位于图像外，则该模块仅计算位于图像边界内的 ROI 部分的均值。

#### 依赖关系

要启用此端口，请将 **ROI type** 参数设置为 `Rectangles`、`Lines` 或 `Label matrix`。对于 `Rectangles` 或 `Lines`，请选中 **Output flag indicating if ROI is within image bounds** 参数。对于 Label matrix，请选中 **Output flag indicating if input label numbers are valid** 参数。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Running mean
  summary: 运行均值 off（默认）| on
  group: ''
- name: Reset port
  summary: 重置事件 None（默认）| Rising edge | Falling edge | Either edge | Non-zero sample
  group: ''
- name: Find the mean value over
  summary: 计算均值所沿的维度 Entire input（默认）| Each row | Each column | Specified dimension
  group: ''
- name: Dimension
  summary: 自定义维度 1（默认）| 正标量
  group: ''
- name: Enable ROI processing
  summary: 在 ROI 内计算均值 off（默认）| on
  group: ''
- name: ROI type
  summary: ROI 类型 Rectangles（默认）| Lines | Label matrix | Binary mask
  group: ''
- name: ROI portion to process
  summary: 要计算均值的 ROI 部分 Entire ROI（默认）| ROI perimeter
  group: ''
- name: Output
  summary: 计算 ROI 的单独均值或通用均值 Individual statistics for each ROI（默认）| Single statistic for all ROIs
  group: ''
- name: Output flag indicating if ROI is within image bounds
  summary: 启用标志输出端口 off（默认）| on
  group: ''
- name: Output flag indicating if input label numbers are valid
  summary: 启用标志输出端口 off（默认）| on
  group: ''
- name: Lock data type settings against change by the fixed-point tools
  summary: 防止定点工具覆盖数据类型 off（默认）| on
  group: ''
```

**主**

### **Running mean** — 运行均值 `off`（默认）| `on`

选中此参数可在一段时间内跨输入序列计算运行均值。

### **Reset port** — 重置事件 `None`（默认）| `Rising edge` | `Falling edge` | `Either edge` | `Non-zero sample`

指定模块检测为重置事件的内容。当 **Rst** 端口发生重置事件时，模块重置运行均值。重置采样时间必须为正整数，并且是输入采样时间的倍数。

将重置事件指定为以下选项之一。

- `None` — 禁用 **Rst** 端口。
- `Rising edge` — 当 **Rst** 输入执行以下操作之一时触发重置事件。

  - 从负值上升到正值或零
  - 从零上升到正值，其中该上升不是从负值上升到零的延续

    上升沿示意图
- `Falling edge` — 当 **Rst** 输入执行以下操作之一时触发重置事件。

  - 从正值下降到负值或零
  - 从零下降到负值，其中该下降不是从正值下降到零的延续

    下降沿示意图

- `Either edge` — 当 **Rst** 输入为上升沿或下降沿时触发重置事件。
- `Non-zero sample` — 在对应于非零 **Rst** 输入的每个采样时间触发重置事件。

  **注意**

  在 Simulink® 多任务模式下运行仿真时，重置信号有一个采样延迟。在这种情况下，当模块检测到重置事件时，在模块应用重置之前，**Rst** 端口处存在一个采样延迟。

#### 依赖关系

要启用此参数，请选中 **Running mean** 参数。

### **Find the mean value over** — 计算均值所沿的维度 `Entire input`（默认）| `Each row` | `Each column` | `Specified dimension`

指定模块沿其计算均值的输入维度。

- `Entire input` — 在整个输入上计算均值。
- `Each row` — 在每一行上计算均值。
- `Each column` — 在每一列上计算均值。
- `Specified dimension`— 在 **Dimension** 参数指定的维度上计算均值。

  - 如果 **Dimension** 参数设置为 `1`，则输出与选择 `Each column` 时相同。
  - 如果 **Dimension** 参数设置为 `2`，则输出与选择 `Each row` 时相同。

#### 依赖关系

要启用此参数，请清除 **Running mean** 参数。

### **Dimension** — 自定义维度 `1`（默认）| 正标量

指定模块在其上计算均值的输入数组的维度（从 1 开始的值）。此参数的值不得超过输入数组中的维度数。

#### 依赖关系

要启用此参数，请将 **Find the mean value over** 参数设置为 `Specified dimension`。

### **Enable ROI processing** — 在 ROI 内计算均值 `off`（默认）| `on`

选中以在图像中指定的 ROI 内计算均值。

#### 依赖关系

要启用此参数，请将 **Find the mean value over** 参数设置为 `Entire input`。

### **ROI type** — ROI 类型 `Rectangles`（默认）| `Lines` | `Label matrix` | `Binary mask`

指定表示图像中要计算均值的区域的 ROI 格式。ROI 类型可以是矩形、线、标签矩阵或二值掩膜。

|  |  |  |
| --- | --- | --- |
| **ROI type** | **ROI 端口的输入** | **描述** |
| `Rectangles` | - 四元素行向量    [*x y width   height*] - *M*×4 矩阵：  [x1y1width1height1x2y2width2height2⋮⋮⋮⋮xMyMwidthMheightM]  ，其中 *M* 是矩形 ROI 的数量。矩阵的每一行对应于不同的矩形。 | - *x* 和 *y* 是矩形左上角的从 1 开始的坐标。 - *width* 和 *height* 是矩形的宽度和高度（以像素为单位）。*width* 和 *height* 的值必须大于零。 |
| `Lines` | - 四元素行向量    [*x*1   *y*1   *x*2   *y*2] - *M*×4 矩阵：    [x11y11x12y12x21y21x22y22⋮⋮⋮⋮xM1yM1xM2yM2]    其中 *M* 是线性 ROI 的数量。矩阵的每一行对应于不同的线。 | - *x*1 和 *y*1 是线起点的坐标。 - *x*2 和 *y*2 是线终点的坐标。 |
| `Label matrix` | *M*×*N* 矩阵 | 与输入图像大小相同的矩阵。该矩阵包含表示图像中不同对象的标签值。标记为 `0` 的像素表示背景。标记为 `1` 的像素构成一个对象，标记为 `2` 的像素构成第二个对象，依此类推。 |
| `Binary mask` | *M*×*N* 矩阵 | 与输入图像大小相同的矩阵。二值掩膜将图像像素分类为属于感兴趣区域或背景。二值掩膜值为 `1` 表示对应的图像像素属于 ROI。二值掩膜值为 `0` 表示对应的图像像素是背景的一部分。 |

#### 依赖关系

要启用此参数，请选中 **Enable ROI processing** 参数。

### **ROI portion to process** — 要计算均值的 ROI 部分 `Entire ROI`（默认）| `ROI perimeter`

指定模块为其计算二维均值的 ROI 部分。

- `Entire ROI` — 该模块在矩形 ROI 的整个区域上计算均值。
- `ROI perimeter` — 该模块沿矩形 ROI 的周长计算均值。

#### 依赖关系

要启用此参数，请将 **ROI type** 参数设置为 `Rectangles`。

### **Output** — 计算 ROI 的单独均值或通用均值 `Individual statistics for each ROI`（默认）| `Single statistic for all ROIs`

指定是单独为每个 ROI 计算二维均值还是跨所有 ROI 计算二维均值。

- 要为每个 ROI 计算单独的均值，请将此参数设置为 `Individual statistics for each ROI`。该模块输出对应于不同 ROI 的均值向量。输出向量的长度等于 ROI 的数量。
- 要跨所有指定的 ROI 计算通用均值，请将此参数设置为 `Single statistic for all ROIs`。该模块输出表示所有指定 ROI 均值的标量。

#### 依赖关系

要启用此参数，请将 **ROI type** 参数设置为 `Rectangles`、`Lines` 或 `Label matrix`。

### **Output flag indicating if ROI is within image bounds** — 启用标志输出端口 `off`（默认）| `on`

选中以启用 Flag 输出端口。

#### 依赖关系

要启用此参数，请将 **ROI type** 参数设置为 `Rectangles` 或 `Lines`。

### **Output flag indicating if input label numbers are valid** — 启用标志输出端口 `off`（默认）| `on`

选中以启用 Flag 输出端口。

#### 依赖关系

要启用此参数，请将 **ROI type** 参数设置为 `Label matrix`。

**数据类型**

有关定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

### **Lock data type settings against change by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选中此参数可防止定点工具覆盖您在此模块中指定的数据类型。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

**注意**

浮点继承优先于此窗格上定义的数据类型设置。当输入为浮点时，模块忽略这些设置，所有内部数据类型均为浮点。
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

查找输入数组的二维均值

2-D Mean 模块计算输入的均值。它可以沿输入的指定维度或跨整个输入计算均值。该模块还可以在一段时间内计算输入序列中的运行均值。
