---
type: simulink-block
title: 'Compositing'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Text & Graphics'
documentation_page: 'compositing'
documentation_source_path: 'ref/compositing.html'
language: zh-CN
chinese_source: worker-translation
---

# Compositing

## 端口

### 输入

### **Image1** — 输入图像一 矩阵 | 数组

输入图像一，指定为 *M*×*N* 矩阵或 *M*×*N*×*P* 数组。如果输入为 *M*×*N*×*P* 数组，则 *P* 是图像中的颜色通道数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **Image2** — 输入图像二 矩阵 | 数组

输入图像二，指定为 *M*×*N* 矩阵或 *M*×*N*×*P* 数组。如果输入为 *M*×*N*×*P* 数组，则 *P* 是图像中的颜色通道数。

#### 依赖

要启用此端口，请将 **Operation** 参数设置为 `Blend` 或 `Binary mask`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **Mask** — 二值掩膜 标量 | 矩阵

二值掩膜，指定为标量或矩阵。此掩膜根据 **Operation** 参数的值，确定该模块将 **Image1** 的哪些像素用 **Image2** 的像素值覆盖或高亮显示。

- `Binary mask` — 该模块将 **Image1** 中由掩膜指示的像素值用 **Image2** 的对应像素值覆盖。您可以将 **Mask** 指定为标量 `0` 或 `1`（该模块将其用于 **Image2** 的所有像素），或指定为与 **Image2** 大小相同的二值矩阵。
- `Highlight selected pixels` — 该模块高亮显示 **Image1** 中由掩膜指示的像素。

#### 依赖

要启用此端口：

- 如果要用另一幅图像的像素值覆盖一幅图像的像素值，请将 **Operation** 参数设置为 `Binary mask`，并将 **Mask source** 参数设置为 `Input port`。
- 如果要高亮显示图像中选定的像素，请将 **Operation** 参数设置为 `Highlight selected pixels`。

**数据类型：** `single` | `double` | `Boolean`

### **Factor** — 不透明度因子 标量 | 矩阵

不透明度因子，指定为标量或矩阵。如果指定为标量，则该值是 **Image2** 的每个像素与 **Image1** 的每个对应像素组合的比例。如果指定为矩阵，则其维度必须与 **Image2** 的维度匹配。每个不透明度因子必须在 [0, 1] 范围内。

#### 依赖

要启用此端口，请将 **Operation** 参数设置为 `Blend`，并将 **Opacity factor(s) source** 参数设置为 `Input port`。

**数据类型：** `single` | `double`

### **Location** — 位置索引 向量

位置索引，指定为二元素向量。第一个元素表示 **Image2** 左上角相对于 **Image1** 左上角的行位置，第二个元素表示列位置。如果 **Image2** 左上角的位置使得其任何像素将渲染到 **Image1** 边界之外，则该模块将 **Image2** 裁剪到 **Image1** 的最后一行或最后一列。

**注意**

当 **Image1** 输入具有定点或布尔数据类型时，**Location** 输入必须具有内置整数数据类型。

#### 依赖

要启用此端口，请将 **Location source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **Port\_1** — 输出图像 矩阵

输出图像，返回为 *M*×*N* 矩阵或 *M*×*N*×*P* 数组。如果输出为 *M*×*N*×*P* 数组，则 *P* 是图像中的颜色通道数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### 主要

### **Operation** — 指定操作 `Blend`（默认） | `Binary mask` | `Highlight selected pixels`

选择该模块要执行的图像操作。

- `Blend` — 使用指定的不透明度因子，将 **Image1** 的像素值与 **Image2** 的像素值线性组合。
- `Binary mask` — 用二值掩膜指定的 **Image2** 的值覆盖 **Image1** 的像素值。
- `Highlight selected pixels` — 高亮显示二值掩膜指示的 **Image1** 的像素。高亮操作将最高强度或颜色值分配给 **Image1** 中与二值掩膜逻辑 1 的像素对应的像素。

### **Opacity factor(s) source** — 不透明度因子的来源 `Specify via dialog`（默认） | `Input port`

指定不透明度因子的来源。如果将此参数设置为 `Input port`，则启用 **Factor** 输入端口。

#### 依赖

要启用此参数，请将 **Operation** 参数设置为 `Blend`。

### **Opacity factor(s)** — 不透明度因子 `0.75`（默认） | 标量 | 矩阵

定义 **Image2** 的每个像素与 **Image1** 的每个对应像素组合的比例。当您将不透明度因子指定为矩阵时，其维度必须与 **Image2** 的维度匹配。如果将其指定为标量，则该模块将该值用作 **Image2** 所有像素的不透明度因子。不透明度因子必须在 [0, 1] 范围内。

#### 依赖

要启用此参数，请将 **Operation** 参数设置为 `Blend`，并将 **Opacity factor(s) source** 参数设置为 `Specify via dialog`。

### **Location source** — 叠加位置的来源 `Specify via dialog`（默认） | `Input port`

选择叠加位置的来源。如果将此参数设置为 `Input port`，则启用 **Location** 输入端口。

### **Location [x y]** — 叠加位置索引 `[1 1]`（默认） | 二元素向量

将 **Image2** 左上角相对于 **Image1** 左上角的行和列位置指定为二元素向量。如果 **Image2** 左上角的位置使得其任何像素将渲染到 **Image1** 边界之外，则该模块将 **Image2** 裁剪到 **Image1** 的最后一行或最后一列。

#### 依赖

要启用此参数，请将 **Location source** 参数设置为 `Specify via dialog`。

### **Mask source** — 掩膜的来源 `Specify via dialog`（默认） | `Input port`

选择二值掩膜的来源。如果将此参数设置为 `Input port`，则启用 **Mask** 输入端口。

#### 依赖

要启用此参数，请将 **Operation** 参数设置为 `Binary mask`。

### **Mask** — 二值掩膜 `0`（默认） | `1` | 矩阵

二值掩膜，指定为标量或矩阵，定义该模块将 **Image1** 的哪些像素用 **Image2** 的对应像素值覆盖或高亮显示。您指定 `0` 或 `1`（该模块将其用于 **Image2** 中的所有像素），或指定为与 **Image2** 大小相同的二值矩阵。

#### 依赖

要启用此参数，请将 **Operation** 参数设置为 `Binary mask`，并将 **Mask source** 参数设置为 `Specify via dialog`。

### 数据类型

有关定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

## 所属库

Computer Vision Toolbox / Text & Graphics

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

组合两幅图像或将掩膜应用于图像

Compositing 模块组合两幅图像、将一幅图像叠加到另一幅图像上，或高亮显示图像中选定的像素。当组合两幅图像时，该模块使用以下方程，其中输出图像 *O* 是两幅图像 I1 和 I2 的线性组合：

O(i,j)=(1−X)∗I1(i,j)+X∗I2(i,j)。

不透明度因子 *X* 在组合图像之前对每个像素进行缩放，其中 0≤X≤1。

当将一幅图像叠加到另一幅图像上，或高亮显示输入图像中选定的像素时，该模块使用二值掩膜来指定要覆盖或高亮显示哪些像素。

**注意**

此模块支持二值图像、强度图像和彩色图像。
