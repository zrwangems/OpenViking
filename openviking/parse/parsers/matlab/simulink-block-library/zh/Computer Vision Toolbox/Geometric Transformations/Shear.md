---
type: simulink-block
title: 'Shear'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Geometric Transformations'
documentation_page: 'shear'
documentation_source_path: 'ref/shear.html'
language: zh-CN
chinese_source: worker-translation
---

# Shear

## 端口

### 输入

### **Image** — 输入图像或视频矩阵 | 数组

输入图像或视频，指定为 *M*×*N* 矩阵、*M*×*N*×*T* 数组、*M*×*N*×*C* 数组或 *M*×*N*×*C*×*T* 数组。*T* 是视频或图像序列中的帧数，*C* 是颜色通道数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **S** — 剪切值向量

剪切值，指定为形式为 `[first last]` 的二元素向量。

- 要水平剪切图像，模块使用指定到 **S** 端口的 `first` 和 `last` 值分别偏移第一行和最后一行的像素。
- 要垂直剪切图像，模块使用指定到 **S** 端口的 `first` 和 `last` 值分别偏移第一列和最后一列的像素。

#### 依赖关系

要启用此端口，请将 **Shear values source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **Output** — 变换后的图像或视频矩阵 | 数组

变换后的图像或视频，返回为 *P*×*Q* 矩阵、*P*×*Q*×*T* 数组、*P*×*Q*×*C* 数组或 *P*×*Q*×*C*×*T* 数组。*T* 是视频或图像序列中的帧数，*C* 是颜色通道数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **Shear direction** — 变换方向 `Horizontal`（默认）| `Vertical`

指定输入图像的剪切方向，为以下选项之一：

- `Horizontal` — 以线性变化的偏移量偏移输入图像的行。使用 **Row/column shear values [first last]** 参数指定第一行和最后一行的偏移量限制。
- `Vertical` — 以线性变化的偏移量偏移输入图像的列。使用 **Row/column shear values [first last]** 参数指定第一列和最后一列的偏移量限制。

水平和垂直剪切对输入图像变换效果的图示

### **Output size after shear** — 变换后的图像大小 `Full`（默认）| `Same as input image`

指定变换后图像的大小，为 `Full` 或 `Same as input image`。

- `Full` — 模块输出整个剪切后的图像。
- `Same as input image` — 模块输出与输入图像大小相同的矩阵。在这种情况下，输出图像包含剪切后图像的左上部分，受输入图像尺寸限制。

### **Shear values source** — 剪切值偏移量限制的来源 `Specify via dialog`（默认）| `Input port`

从以下选项中选择剪切值偏移量限制的来源：

- `Specify via dialog` — 使用 **Row/column shear values [first last]** 参数指定剪切值偏移量限制。
- `Input port` — 使用 **S** 端口指定剪切值偏移量限制。

### **Row/column shear values [first last]** — 剪切值偏移量限制 `[0 3]`（默认）| 二元素向量

将剪切值偏移量限制指定为形式为 [`first last`] 的二元素向量。`first` 和 `last` 值分别表示输入图像第一行和最后一行或第一列和最后一列要偏移的像素数。

例如，如果将 **Shear direction** 参数设置为 `Horizontal`，并将 **Row/column shear values [first last]** 参数值指定为 `[50 150]`，则模块将输入图像的顶行向右偏移 50 像素，将底行向右偏移 150 像素。要将某一行向左移动，请为 **Row/column shear values [first last]** 参数的对应元素指定负值。

类似地，如果将 **Shear direction** 参数设置为 `Vertical`，并将 **Row/column shear values [first last]** 参数值指定为 `[10 50]`，则模块将最左列向下偏移 10 像素，将最右列向下偏移 50 像素。要将某一列向上移动，请为 **Row/column shear values [first last]** 参数的对应元素指定负值。

#### 依赖关系

要启用此参数，请将 **Shear values source** 参数设置为 `Specify via dialog`。

### **Maximum shear value** — 最大行或列剪切量 `20`（默认）| 标量

指定输入图像任意行或列要剪切的最大像素数。Shear 模块使用此参数确定剪切后图像的大小。如果 **S** 端口的任何输入大于 **Maximum shear value** 参数的绝对值，则 Shear 模块将输入值减小到最大剪切值。

#### 依赖关系

要启用此参数，请将 **Shear values source** 参数设置为 `Input port`。

### **Background fill value** — 变换后图像中背景的强度值 `0`（默认）| 标量 | 三元素向量

将变换后图像背景的强度值指定为标量强度值或表示 RGB 三元组的三元素向量。

### **Interpolation method** — 插值变换后像素值的方法 `Bilinear`（默认）| `Nearest neighbor` | `Bicubic`

指定对剪切后图像的像素值进行插值的方法，为以下选项之一：

- `Nearest neighbor` — Shear 模块使用 1 个最近像素的值作为新像素值。
- `Bilinear` — 新像素值是 4 个最近像素值的加权平均值。
- `Bicubic` — 新像素值是 16 个最近像素值的加权平均值。

模块为插值考虑的像素数会影响计算的复杂度和精度。`Nearest neighbor` 插值使用的像素最少，计算效率最高但精度最低，而 `Bicubic` 插值计算效率最低但精度最高。有关插值方法和核的详细信息，请参阅“详细信息”部分以及 Create and Compare Resizing Interpolation Kernels 示例。

## 所属库

Computer Vision Toolbox / Geometric Transformations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

通过线性变化的偏移量偏移图像或视频帧的行或列

Shear 模块通过偏移行或列来变换输入图像或视频帧。该模块使用水平或垂直剪切来变换输入图像。

- 水平剪切通过从左到右或从右到左逐渐增加偏移量来线性偏移图像中的行。
- 垂直剪切通过从上到下或从下到上逐渐增加偏移量来线性偏移图像中的列。
