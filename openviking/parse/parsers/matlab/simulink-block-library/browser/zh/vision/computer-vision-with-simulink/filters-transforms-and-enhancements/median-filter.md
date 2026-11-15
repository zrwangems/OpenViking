---
type: simulink-block
title: 'Median Filter'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Filters, Transforms, and Enhancements'
documentation_page: 'medianfilter'
documentation_source_path: 'ref/medianfilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Median Filter

## 端口

### 输入

### **I** — 输入图像矩阵

输入图像，指定为 *M*×*N* 矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`

### **PVal** — 填充值标量

填充值，指定为标量。该模块将此值用于添加到输入图像的行或列的每个元素。

#### 依赖关系

要启用此端口：

- 将 **输出大小** 参数设置为 `Same as input port I`。
- 将 **填充选项** 参数设置为 `Constant`。
- 将 **填充值来源** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Port\_1** — 输出图像矩阵

输出图像，以矩阵形式返回。中值滤波后的输出图像的维度由 **输出大小** 参数指定。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

## 参数

### **邻域大小** — 邻域窗口大小 `[3 3]`（默认）| 正整数 | 二元素正整数向量

指定该模块计算中值所依据的邻域的窗口大小。如果指定为标量，则此值创建一个具有指定行数和列数的正方形邻域。如果指定为向量，则第一个元素是邻域中的行数，第二个元素是邻域中的列数。

### **输出大小** — 输出大小调整方法 `Same as input port I`（默认）| `Valid`

将输出大小调整方法指定为以下选项之一。

- `Same as input port I` — 该模块使用填充计算边界像素，从而计算整个图像的邻域中值。输出图像与输入图像具有相同的维度。选择此选项将启用 **填充选项** 参数。
- `Valid` — 该模块在邻域完全位于输入图像内且无需填充的位置计算中值。对于大小为 *M*×*N* 的输入图像和大小为 *X*×*Y* 的邻域，输出图像的维度为 (`M`–`X`+1)×(`N`–`Y`+1)。

### **填充选项** — 填充方法 `Symmetric`（默认）| `Constant` | `Replicate` | `Circular`

使用以下方法之一填充图像：

- `Constant` — 使用常量值填充图像。选择此选项将启用 **填充值来源** 参数。有关详细信息，请参阅使用常量值填充。
- `Replicate` — 通过重复输入图像的边界值填充图像。有关详细信息，请参阅通过重复边界值填充。
- `Symmetric` — 使用输入数据的镜像填充图像。有关详细信息，请参阅使用镜像填充。
- `Circular` — 使用输入图像中元素的循环重复填充图像。有关详细信息，请参阅使用元素循环重复填充。

#### 依赖关系

要启用此参数，请将 **输出大小** 参数设置为 `Same as input port I`。

### **填充值来源** — 常量填充值的来源 `Specify via dialog`（默认）| `Input port`

将填充来源指定为 `Specify via dialog` 或 `Input port`。

- `Specify via dialog` — 使用 **填充值** 参数指定填充值。
- `Input port` — 使用 **PVal** 输入端口指定填充值。

#### 依赖关系

要启用此参数，请将 **输出大小** 参数设置为 `Same as input port I`，并将 **填充选项** 参数设置为 `Constant`。

### **填充值** — 填充值 `0`（默认）| 标量

指定用于填充图像的标量值。

#### 依赖关系

要启用此端口：

- 将 **输出大小** 参数设置为 `Same as input port I`。
- 将 **填充选项** 参数设置为 `Constant`。
- 将 **填充值来源** 参数设置为 `Specify via dialog`。

## 所属库

Computer Vision Toolbox / Analysis & Enhancement Computer Vision Toolbox / Filtering

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

执行二维中值滤波

Median Filter 模块对输入图像的每个像素应用中值滤波器。对于每个 *M*×*N* 邻域，该滤波器用邻域的中值替换中心值。如果邻域具有中心元素，则该模块用中值替换中心像素，如下图所示。

如果邻域没有精确的中心，则该模块偏向邻域的左上角。在此图中，中值已放置在邻域中心相交的四个像素的左上像素中。

该模块对输入图像的边缘进行填充以进行滤波。这会导致图像两侧 *M/2* 个像素范围内以及顶部或底部 *N/2* 个像素范围内的像素出现失真。

中值对极端值不如均值敏感。因此，Median Filter 可有效去除图像中的椒盐噪声，而不会显著降低图像的清晰度。
