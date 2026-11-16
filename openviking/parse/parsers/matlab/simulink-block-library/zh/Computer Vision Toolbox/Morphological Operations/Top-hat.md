---
type: simulink-block
title: 'Top-hat'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Morphological Operations'
documentation_page: 'tophat'
documentation_source_path: 'ref/tophat.html'
language: zh-CN
chinese_source: worker-translation
---

# Top-hat

## 端口

### 输入

### **I** — 输入图像矩阵

将输入图像指定为强度值矩阵。除非将 **邻域或结构元素来源** 参数设置为 `Input port`，否则此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **Nhood** — 邻域值向量 | 矩阵

将表示结构元素的邻域值指定为由 `1` 和 `0` 组成的向量或矩阵，或使用 `strel` 函数指定。

#### 依赖项

要启用此端口，请将 **邻域或结构元素来源** 参数设置为 `Input port`。

**数据类型：** `Boolean`
### 输出

### **Port\_1** — 滤波后图像矩阵

返回的顶帽滤波后图像是强度值矩阵。滤波后图像的大小和数据类型与输入图像相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

## 参数

### **输入图像类型** — 输入图像的类型 `Intensity`（默认） | `Binary`

将图像类型指定为以下选项之一：

- `Intensity` — 如果输入图像是强度图像，请选择此选项。
- `Binary` — 如果输入图像是二值图像，请选择此选项。

### **邻域或结构元素来源** — 邻域或结构元素的来源 `Specify via dialog`（默认） | `Input port`

将邻域或结构元素的来源指定为以下选项之一：

- `Specify via dialog` — 使用 **邻域或结构元素** 参数指定邻域或结构元素。
- `Input port` — 使用 **Nhood** 输入端口指定表示结构元素的邻域值。

### **邻域或结构元素** — 邻域或结构元素 `strel('square',4)`（默认） | 向量 | 矩阵

将邻域或结构元素指定为由 `1` 和 `0` 组成的向量或矩阵、`strel` 对象或 `strel` 对象数组。当将此值指定为 `strel` 对象数组时，模块会依次将每个对象应用于整个图像。

如果结构元素可分解为更小的元素，则由于使用更高效的算法，模块执行速度会更高。

#### 依赖项

要启用此参数，请将 **邻域或结构元素来源** 参数设置为 `Specify via dialog`。

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

**在 R2006a 之前引入**

## 描述

对强度图像或二值图像执行形态学顶帽滤波

Top-hat 模块使用预定义的邻域或结构元素对强度图像或二值图像执行顶帽滤波。顶帽滤波等效于从输入图像本身中减去对输入图像执行形态学开运算的结果。

要定义模块应用于图像的结构元素，请使用 **邻域或结构元素** 参数。通过输入由 `1` 和 `0` 组成的向量或矩阵，或使用 `strel` 函数来指定此元素。

此模块仅使用二维平坦结构元素。
