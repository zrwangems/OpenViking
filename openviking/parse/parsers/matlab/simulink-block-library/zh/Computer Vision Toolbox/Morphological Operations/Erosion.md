---
type: simulink-block
title: 'Erosion'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Morphological Operations'
documentation_page: 'erosion'
documentation_source_path: 'ref/erosion.html'
language: zh-CN
chinese_source: worker-translation
---

# Erosion

## 端口
```yaml
ports:
- name: I
  summary: 输入图像矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
- name: Nhood
  summary: 邻域值向量 | 矩阵
  direction: input
  data_types: Boolean
- name: Port_1
  summary: 腐蚀后的图像矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
```

### 输入

### **I** — 输入图像矩阵

将输入图像指定为二值或灰度值矩阵。在将 **Neighborhood or structuring element source** 参数设置为 `Input port` 之前，此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **Nhood** — 邻域值向量 | 矩阵

将表示结构元素的邻域值指定为由 `1` 和 `0` 组成的向量或矩阵。

#### 依赖关系

要启用此端口，请将 **Neighborhood or structuring element source** 参数设置为 `Input port`。

**数据类型：** `Boolean`
### 输出

### **Port\_1** — 腐蚀后的图像矩阵

腐蚀后的图像，以矩阵形式返回。输出图像的大小和数据类型与输入图像相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: Neighborhood or structuring element source
  summary: 邻域或结构元素的来源 Specify via dialog（默认）| Input port
  group: ''
- name: Neighborhood or structuring element
  summary: 邻域或结构元素 strel('square',4)（默认）
  group: ''
```

### **Neighborhood or structuring element source** — 邻域或结构元素的来源 `Specify via dialog`（默认）| `Input port`

将邻域或结构元素的来源指定为以下选项之一：

- `Specify via dialog` — 使用 **Neighborhood or structuring element** 参数指定邻域或结构元素。
- `Input port` — 使用 **Nhood** 输入端口指定表示结构元素的邻域值。

### **Neighborhood or structuring element** — 邻域或结构元素 `strel('square',4)`（默认）

将邻域或结构元素指定为由 `1` 和 `0` 组成的向量或矩阵、一个 `strel` 对象，或一个 `strel` 对象数组。当指定 `strel` 对象数组时，该模块会依次将每个对象应用于整个图像。

如果结构元素可分解为更小的元素，由于算法更高效，模块的执行速度会提高。

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

**在 R2006a 之前引入**

## 描述

在二值或灰度图像中查找局部最小值

Erosion 模块在图像上滑动邻域或结构元素，查找局部最小值，并根据这些最小值创建输出矩阵。如果邻域或结构元素具有中心元素，该模块将最小值放置在该处，如下图所示。

三乘三网格，中心方格上标有“X”，表示局部最小值。

如果邻域或结构元素没有精确的中心，该模块会偏向中心元素的左上方，并将最小值放置在该处，如下图所示。

四乘四网格，第二行第二列的方格上标有“X”，表示局部最小值。

此模块仅使用平坦结构元素。
