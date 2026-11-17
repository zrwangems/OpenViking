---
type: simulink-block
title: 'Dilation'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Morphological Operations'
documentation_page: 'dilation'
documentation_source_path: 'ref/dilation.html'
language: zh-CN
chinese_source: worker-translation
---

# Dilation

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
  summary: 膨胀后的图像矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean | fixed point
```

### 输入

### **I** — 输入图像矩阵

将输入图像指定为强度值矩阵。除非将**邻域或结构元素来源**参数设置为 `Input port`，否则此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **Nhood** — 邻域值向量 | 矩阵

将表示结构元素的邻域值指定为由 `1` 和 `0` 组成的向量或矩阵，或使用 `strel` 函数指定。

#### 依赖关系

要启用此端口，请将**邻域或结构元素来源**参数设置为 `Input port`。

**数据类型：** `Boolean`
### 输出

### **Port\_1** — 膨胀后的图像矩阵

该模块将膨胀后的图像作为强度值矩阵返回。输出图像的大小和数据类型与输入图像相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`
## 参数
```yaml
parameters:
- name: 邻域或结构元素来源
  summary: 邻域或结构元素的来源 Specify via dialog（默认）| Input port
  group: ''
- name: 邻域或结构元素
  summary: 邻域或结构元素 [1 1; 1 1]（默认）| 向量 | 矩阵
  group: ''
```

### **邻域或结构元素来源** — 邻域或结构元素的来源 `Specify via dialog`（默认）| `Input port`

将邻域或结构元素的来源指定为以下选项之一：

- `Specify via dialog` — 使用**邻域或结构元素**参数指定邻域或结构元素。
- `Input port` — 使用 **Nhood** 输入端口指定表示结构元素的邻域值。

### **邻域或结构元素** — 邻域或结构元素 `[1 1; 1 1]`（默认）| 向量 | 矩阵

将邻域或结构元素指定为由 `1` 和 `0` 组成的向量或矩阵、一个 `strel` 对象或一个 `strel` 对象数组。当指定 `strel` 对象数组时，该模块会依次将每个对象应用于整个图像。

如果结构元素可分解为更小的元素，该模块将使用一种更高效的算法，从而可以更快地执行。

#### 依赖关系

要启用此参数，请将**邻域或结构元素来源**参数设置为 `Specify via dialog`。
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

通过查找局部最大值对二值图像或强度图像进行膨胀

Dilation 模块对强度图像或二值图像执行形态学膨胀，并输出膨胀后的图像。

要定义该模块应用于图像的结构元素，请使用**邻域或结构元素**参数。

该模块仅使用二维平坦结构元素。
