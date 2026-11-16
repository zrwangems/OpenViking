---
type: simulink-block
title: '2-D Standard Deviation'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Statistics'
documentation_page: '2dstandarddeviation'
documentation_source_path: 'ref/2dstandarddeviation.html'
language: zh-CN
chinese_source: worker-translation
---

# 2-D Standard Deviation

## 端口

### 输入

### **In** — 输入数组 向量 | 矩阵 | *N-D* 数组

输入数组，指定为向量、矩阵或 *N-D* 数组。在选择 **启用 ROI 处理** 参数之前，此端口未命名。

**数据类型：** `single` | `double`

### **Rst** — 复位端口 标量

复位端口，指定为标量。此端口指定导致模块重置运行标准差的事件。**Rst** 输入的采样时间必须是正整数，并且是输入采样时间的倍数。

#### 依赖关系

要启用此端口，请选择 **运行标准差** 参数，并将 **复位端口** 参数设置为 `Rising edge`、`Falling edge`、`Either edge` 或 `Non-zero sample`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **ROI** — 感兴趣区域 四元素向量 | *m*×4 矩阵 | *M*×*N* 矩阵

感兴趣区域 (ROI)，指定为四元素向量、*m*×4 矩阵或 *M*×*N* 矩阵。此端口的输入值取决于 **ROI 类型** 参数。

**注意**

仅当输入为 2-D 图像时，才能使用 `ROI` 端口。

#### 依赖关系

要启用此端口，请将 **计算标准差的范围** 参数设置为 `Entire input`，并选择 **启用 ROI 处理** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **Label** — 标签矩阵 非负整数矩阵

标签矩阵，指定为非负整数矩阵。标签矩阵表示图像中的对象。标记为 0 的像素是背景。标记为 1 的像素组成一个对象；标记为 2 的像素组成第二个对象；依此类推。标签矩阵的大小必须与 2-D 输入的大小相同。

#### 依赖关系

要启用此端口，请选择 **启用 ROI 处理** 参数，并将 **ROI 类型** 参数设置为 `Label matrix`。

**数据类型：** `uint8` | `uint16` | `uint32`

### **Label Numbers** — ROI 的标签值 *M* 元素向量

ROI 的标签值，指定为 *M* 元素向量。*M* 的值可以小于或等于标签矩阵中标记的对象数。

#### 依赖关系

要启用此端口，请选择 **启用 ROI 处理** 参数，并将 **ROI 类型** 参数设置为 `Label matrix`。

**数据类型：** `uint8` | `uint16` | `uint32`

### 输出

### **Out** — 计算出的输出标准差 标量 | 向量 | 矩阵 | *N-D* 数组

计算出的输出标准差，返回为标量、向量、矩阵或 *N-D* 数组。返回的输出标准差的大小取决于输入的大小，以及 **运行标准差** 和 **计算标准差的范围** 参数的设置。

在选择 **输出标志，指示 ROI 是否在图像边界内** 且 **ROI 类型** 参数设置为 `Rectangles`、`Lines` 或 `Label matrix` 之前，此端口未命名。

#### 如果清除了 **运行标准差**

您可以沿输入的任意指定维度或整个输入计算标准差。输出为：

- 如果输入为任意大小，且 **计算标准差的范围** 参数设置为 `Entire input`，则为标量。
- 如果输入为矩阵，且 **计算标准差的范围** 参数设置为 `Each row`、`Each column` 和 `Specified dimension` 中的任意一个，则为向量。在这种情况下，`Specified dimension` 的 **维度** 值可以是 1 或 2。
- 如果输入为 3-D 数组，且 **计算标准差的范围** 参数设置为 `Specified dimension`，并且 **维度** 值为 3，则为矩阵。
- 如果输入为 *N-D* 数组，且 **计算标准差的范围** 参数设置为除 `Entire input` 以外的选项，则为 *N-D* 数组。

  如果沿输入的 *N* 维计算标准差，则返回的输出为 *(N-1)-D* 数组。在这种情况下，`Specified dimension` 的 **维度** 值设置为 *N*。

  **示例：** 对于大小为 *M*×*N*×*P* 的 3-D 输入数组，返回输出的维度为：

  - 如果将 **计算标准差的范围** 参数设置为 `Entire row`，则为 1×*N*×*P*。
  - 如果将 **计算标准差的范围** 参数设置为 `Entire column`，则为 *M*×1×*P*。
  - 如果将 **计算标准差的范围** 参数设置为 `Specified dimension`，并将 **维度** 值设置为 3，则为 *M*×*N*。

#### 如果选择了 **运行标准差**

当选择 **运行标准差** 参数时，模块计算输入中每个样本相对于所有先前样本的标准差。输出的大小与输入相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **Flag** — ROI 验证 0 | 1

ROI 验证，返回为 0 或 1。输出值表示输入处指定的所有 ROI 是否都位于图像边界内。输出值取决于 **输出** 和 **ROI 类型** 参数的值。

|  |  |  |  |
| --- | --- | --- | --- |
| **ROI 类型** | **输出** | **Flag 端口输出** | **描述** |
| - `Rectangles` - `Lines` | `Individual statistics for each ROI` | 0 | ROI 完全位于输入图像之外。 |
| 1 | ROI 完全或部分位于输入图像内。 |
| `Single statistic for all ROIs` | 0 | ROI 完全位于输入图像之外。 |
| 1 | ROI 完全或部分位于输入图像内。 |
| `Label matrix` | `Individual statistics for each ROI` | 0 | 标签号不在标签矩阵中。 |
| 1 | 标签号在标签矩阵中。 |
| `Single statistic for all ROIs` | 0 | 标签号都不在标签矩阵中。 |
| 1 | 至少有一个标签号在标签矩阵中。 |

**注意**

如果 ROI 部分位于图像之外，模块仅计算位于图像边界内的 ROI 部分的标准差值。

#### 依赖关系

要启用此端口，请选择 **输出标志，指示 ROI 是否在图像边界内** 参数，并将 **ROI 类型** 参数的值设置为 `Rectangle`、`Lines` 或 `Label Matrix`。

## 参数

**主选项卡**

### **运行标准差** — 跟踪运行标准差 off (默认) | on

选择以跟踪模块连续输入的标准差。在此模式下，模块将每个元素视为一个通道。

### **复位端口** — 复位事件 `None` (默认) | `Rising edge` | `Falling edge` | `Either edge` | `Non-zero sample`

指定模块何时检测到复位事件。当在可选的 **Rst** 端口检测到复位事件时，模块会重置运行标准差。复位采样时间必须是正整数，并且是输入采样时间的倍数。

将复位事件指定为：

- `None` 以禁用 **Rst** 端口。
- `Rising edge`：当 **Rst** 输入执行以下操作之一时触发复位事件：

  - 从负值上升到正值或零
  - 从零上升到正值，其中该上升不是从负值上升到零的延续
- `Falling edge`：当 **Rst** 输入执行以下操作之一时触发复位事件：

  - 从正值下降到负值或零
  - 从零下降到负值，其中该下降不是从正值下降到零的延续

- `Either edge`：当 **Rst** 输入为 `Rising edge` 或 `Falling edge` 时触发复位事件。
- `Non-zero sample`：在每个采样时间，当 **Rst** 输入不为零时触发复位事件。

  **注意**

  在 Simulink® 多任务模式下运行仿真时，复位信号有一个采样延迟。因此，当模块检测到复位事件时，在模块应用复位之前，复位端口速率处有一个采样延迟。

#### 依赖关系

要启用此参数，请选择 **运行标准差** 参数。

### **计算标准差的范围** — 计算标准差的维度 `Entire input` (默认) | `Each row` | `Each column` | `Specified dimension`

指定模块沿其计算标准差的输入维度。

- `Entire input` — 在整个输入上计算标准差。
- `Each row` — 在每一行上计算标准差。
- `Each column` — 在每一列上计算标准差。
- `Specified dimension` — 在 **维度** 参数指定的维度上计算标准差。默认情况下，**维度** 参数设置为 1，输出与选择 `Each column` 时相同。

#### 依赖关系

要启用此参数，请清除 **运行标准差** 参数。

### **维度** — 自定义维度 1 (默认)

将计算标准差的输入数组维度指定为从 1 开始的值。此参数的值设置为 1..

#### 依赖关系

要启用此参数，请将 **计算标准差的范围** 参数设置为 `Specified dimension`。

**ROI 处理**

### **启用 ROI 处理** — 计算特定区域内的标准差 off (默认) | on

选择以计算图像中特定 ROI 内的标准差。

**注意**

完整的 ROI 处理仅在您拥有 Computer Vision Toolbox™ 许可证时可用。如果您没有 Computer Vision Toolbox 许可证，仍然可以使用 ROI 处理，但 **ROI 类型** 仅限于 `Rectangles`。

#### 依赖关系

要启用此参数，请将 **计算标准差的范围** 参数设置为 `Entire input`。

### **ROI 类型** — ROI 类型 `Rectangles` (默认) | `Lines` | `Label matrix` | `Binary mask`

指定表示图像中区域的 ROI 类型，模块在这些区域上计算标准差。ROI 类型可以是矩形、线、标签矩阵或二值掩膜。

|  |  |  |
| --- | --- | --- |
| **参数** | | **描述** |
| **ROI 类型** | **ROI 端口的输入** |
| `Rectangles` | - 四元素行向量    `[x y width   height]` - *m*×4 矩阵  [x1y1width1height1x2y2width2height2⋮⋮⋮⋮xMyMwidthMheightM]  ，其中 *m* 是矩形数量。矩阵的每一行对应不同的矩形。 | - `x` 和 `y` 是矩形左上角的从 1 开始的坐标。 - `width` 和 `height` 是矩形的宽度和高度，以像素为单位。`width` 和 `height` 的值必须大于 0。 |
| `Lines` | - 四元素行向量    `[x1   y1 x2   y2]` - *m*×4 矩阵    [x11y11x12y12x21y21x22y22⋮⋮⋮⋮xM1yM1xM2yM2]  ，其中 *m* 是线数量。矩阵的每一行对应不同的线。 | - `x1` 和 `y1` 是线的起点坐标。 - `x2` 和 `y2` 是线的终点坐标。 |
| `Label matrix` | *M*×*N* 矩阵 | 与输入图像大小相同的矩阵。该矩阵包含表示图像中不同对象的标签值。标记为 0 的像素是背景。标记为 1 的像素组成一个对象；标记为 2 的像素组成第二个对象；依此类推。 |
| `Binary mask` | *M*×*N* 矩阵 | 与输入图像大小相同的矩阵。二值掩膜将图像像素分类为属于感兴趣区域或背景。掩膜像素值为 1 表示图像像素属于 ROI。掩膜像素值为 0 表示图像像素是背景的一部分。 |

#### 依赖关系

要启用此参数，请选择 **启用 ROI 处理** 参数。

### **要处理的 ROI 部分** — 计算标准差的 ROI 部分 `Entire ROI` (默认) | `ROI perimeter`

指定模块要从中计算 2-D 标准差的 ROI 部分。ROI 部分可以是整个 ROI 或 ROI 周长。

#### 依赖关系

要启用此参数，请选择 **启用 ROI 处理** 参数，并将 **ROI 类型** 参数设置为 `Rectangles`。

### **输出** — 计算单个 ROI 或整个 ROI 的标准差 `Individual statistics for each ROI` (默认) | `Single statistic for all ROIs`

指定是为每个 ROI 单独计算 2-D 标准差，还是为整个 ROI 计算 2-D 标准差。

- 如果选择 `Individual statistics for each ROI`，模块会输出标准差值的向量。输出向量的大小等于 ROI 的数量。
- 如果选择 `Single statistic for all ROIs`，模块会输出标量值。该标量值表示所有指定 ROI 的统计值。

#### 依赖关系

要启用此参数，请选择 **启用 ROI 处理** 参数，并将 **ROI 类型** 参数设置为 `Rectangles`、`Lines` 或 `Label matrix`。

### **输出标志，指示 ROI 是否在图像边界内** — 启用 Flag 端口 off (默认) | on

选择以显示 **Flag** 端口。有关 **Flag** 端口输出的描述，请参阅 Flag。

#### 依赖关系

要启用此参数，请选择 **启用 ROI 处理** 参数，并将 **ROI 类型** 参数设置为 `Rectangles`、`Lines` 或 `Label matrix`。

**数据类型选项卡**

有关定点模块参数的详细信息，请参阅指定模块的定点属性 (DSP System Toolbox)。

### **锁定数据类型设置，防止定点工具更改** — 防止定点工具覆盖数据类型 off (默认) | on

选择此参数可防止定点工具覆盖您在此模块中指定的数据类型。有关详细信息，请参阅锁定输出数据类型设置 (Fixed-Point Designer)。

## 所属库

Computer Vision Toolbox / Statistics

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011b 中引入**

## 描述

计算输入或输入序列的标准差

2-D Standard Deviation 模块计算输入数组的标准差。输入可以是 1-D 向量、2-D 矩阵或 *N-D* 数组。该模块可以沿输入的指定维度或整个输入计算标准差。如果选择 **运行标准差** 参数，该模块还可以跟踪一段时间内输入序列的标准差。
