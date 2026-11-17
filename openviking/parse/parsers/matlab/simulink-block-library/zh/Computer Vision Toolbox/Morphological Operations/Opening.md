---
type: simulink-block
title: 'Opening'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Morphological Operations'
documentation_page: 'opening'
documentation_source_path: 'ref/opening.html'
language: zh-CN
chinese_source: worker-translation
---

# Opening

## 端口

### 输入

### **I** — 输入图像矩阵

将输入图像指定为强度值矩阵。除非将 **Neighborhood or structuring element source** 参数设置为 `Input port`，否则此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **Nhood** — 邻域值向量 | 矩阵

将表示结构元素的邻域值指定为由 `1` 和 `0` 组成的向量或矩阵，或使用 `strel` 函数指定。

#### 依赖关系

要启用此端口，请将 **Neighborhood or structuring element source** 参数设置为 `Input port`。

**数据类型：** `Boolean`
### 输出

### **Port\_1** — 开运算后的图像矩阵

开运算后的图像以强度值矩阵形式返回。开运算后图像的大小和数据类型与输入图像相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

## 参数

### **Neighborhood or structuring element source** — 邻域或结构元素的来源 `Specify via dialog`（默认）| `Input port`

将邻域或结构元素的来源指定为以下选项之一：

- `Specify via dialog` — 使用 **Neighborhood or structuring element** 参数指定邻域或结构元素。
- `Input port` — 使用 **Nhood** 输入端口指定表示结构元素的邻域值。

### **Neighborhood or structuring element** — 邻域或结构元素 `strel('disk',5)`（默认）| 向量 | 矩阵

将邻域或结构元素指定为由 `1` 和 `0` 组成的向量或矩阵、一个 `strel` 对象或一个 `strel` 对象数组。当将此值指定为 `strel` 对象数组时，该模块会依次将每个对象应用于整个图像。

如果结构元素可分解为更小的元素，则该模块由于使用了更高效的算法而以更高的速度执行。

#### 依赖关系

要启用此参数，请将 **Neighborhood or structuring element source** 参数设置为 `Specify via dialog`。

## 所属库

Computer Vision Toolbox / Morphological Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前推出**

## 描述

对二值图像或强度图像执行形态学开运算

Opening 模块使用预定义的邻域或结构元素对强度图像或二值图像执行腐蚀操作，然后执行膨胀操作。

要定义该模块应用于图像的结构元素，请使用 **Neighborhood or structuring element** 参数。通过输入由 `1` 和 `0` 组成的向量或矩阵，或使用 `strel` 函数来指定此元素。

下面分别是输入图像和开运算后的输出图像。

此模块仅使用二维平坦结构元素。
