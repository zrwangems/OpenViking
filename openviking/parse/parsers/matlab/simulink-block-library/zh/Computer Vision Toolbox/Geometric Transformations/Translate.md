---
type: simulink-block
title: 'Translate'
family: 'geometric-transformations'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Geometric Transformations'
documentation_page: 'translate'
documentation_source_path: 'ref/translate.html'
language: zh-CN
chinese_source: worker-translation
---

# Translate

## 端口

### 输入

### **Image** — 输入图像或视频矩阵 | 数组

输入图像或视频，指定为 *M*×*N* 矩阵、*M*×*N*×*T* 数组、*M*×*N*×*C* 数组或 *M*×*N*×*C*×*T* 数组。*T* 是视频或图像序列中的帧数，*C* 是颜色通道数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Offset** — 平移值向量

平移值，指定为形式为 `[vertical horizontal]` 的二元素向量。向量中的 `vertical` 值是沿垂直方向将图像向上或向下平移的像素数。`horizontal` 元素是沿水平方向将图像向左或向右平移的像素数。坐标轴原点位于输入图像的左上角。

- 要将图像向下平移，请为 `vertical` 元素指定正像素值。
- 要将图像向上平移，请为 `vertical` 元素指定负像素值。
- 要将图像向右平移，请为 `horizontal` 元素指定正像素值。
- 要将图像向左平移，请为 `horizontal` 元素指定负像素值。

#### 依赖关系

要启用此端口，请将 **偏移量来源** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### 输出

### **Output** — 平移后的图像或视频矩阵 | 数组

平移后的图像或视频，返回为 *P*×*Q* 矩阵、*P*×*Q*×*T* 数组、*P*×*Q*×*C* 数组或 *P*×*Q*×*C*×*T* 数组。*T* 是视频或图像序列中的帧数，*C* 是颜色通道数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **平移后的输出大小** — 平移后的图像大小 `Full` (default) | `Same as input image`

将平移后的图像大小指定为 `Full` 或 `Same as input image`。

- `Full` — 模块输出包含整个平移后图像的矩阵。
- `Same as input image` — 模块输出与输入图像大小相同的矩阵，其中包含平移后图像的一部分。

### **偏移量来源** — 平移值的来源 `Specify via dialog` (default) | `Input port`

将平移值的来源指定为以下选项之一：

- `Specify via dialog` — 使用 **偏移量** 参数指定平移值。
- `Input port` — 使用 **Offset** 端口指定平移值。

### **偏移量** — 平移值 `[1.5 2.3]` (default) | 二元素向量

将平移值指定为形式为 [`vertical horizontal`] 的二元素向量。向量中的 vertical 元素是沿垂直方向将图像向上或向下平移的像素数。horizontal 元素是沿水平方向将图像向左或向右平移的像素数。坐标轴原点位于输入图像的左上角。

- 要将图像向下平移，请为 `vertical` 元素指定正像素值。
- 要将图像向上平移，请为 `vertical` 元素指定负像素值。
- 要将图像向右平移，请为 `horizontal` 元素指定正像素值。
- 要将图像向左平移，请为 `horizontal` 元素指定负像素值。

#### 依赖关系

要启用此参数，请将 **偏移量来源** 参数设置为 `Specify via dialog`。

### **最大偏移量** — 平移值限制 `[8 10]` (default) | 二元素向量

将输入图像在垂直和水平方向上平移的最大像素数指定为形式为 [`vertical horizontal`] 的向量。当 **平移后的输出大小** 参数设置为 `Full` 且 **偏移量来源** 参数设置为 `Input port` 时，Translate 模块使用此参数确定平移后图像的大小。如果 **Offset** 端口的任一输入值大于 **最大偏移量** 参数的对应值，则 Translate 模块会将那个输入平移值减小到对应的最大平移值。

#### 依赖关系

要启用此参数，请将 **偏移量来源** 参数设置为 `Input port`。

### **背景填充值** — 平移后图像中背景的强度或颜色 `0` (default) | scalar | RGB triplet

将平移后图像背景的强度或颜色指定为标量强度值或 RGB 三元组。

### **插值方法** — 用于对平移后像素值进行插值的方法 `Bilinear` (default) | `Nearest neighbor` | `Bicubic`

将用于对平移后图像像素值进行插值的方法指定为以下选项之一：

- `Nearest neighbor` — Translate 模块使用最近像素的值作为插值像素。
- `Bilinear` — 插值像素值是 4 个最近像素值的加权平均值。
- `Bicubic` — 插值像素值是 16 个最近像素值的加权平均值。

模块为插值考虑的像素数会影响计算的复杂度和准确度。`Nearest neighbor` 插值使用的像素最少，计算效率最高且准确度最低；而 `Bicubic` 插值计算效率最低且准确度最高。有关插值方法和核的详细信息，请参阅“更多信息”部分以及 Create and Compare Resizing Interpolation Kernels 示例。

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

**R2006a 之前引入**

## 描述

平移图像或视频帧

Translate 模块根据二元素偏移量向量指定的垂直和水平方向上的像素数，对输入图像或视频帧进行平移。
