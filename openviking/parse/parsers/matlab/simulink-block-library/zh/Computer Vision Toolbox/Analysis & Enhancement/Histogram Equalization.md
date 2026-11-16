---
type: simulink-block
title: 'Histogram Equalization'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Analysis & Enhancement'
documentation_page: 'histogramequalization'
documentation_source_path: 'ref/histogramequalization.html'
language: zh-CN
chinese_source: worker-translation
---

# Histogram Equalization

## 端口

### 输入

### **I** — 输入图像矩阵

输入图像，指定为强度值矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **Hist** — 整数目标直方图向量

输出图像的目标直方图，指定为整数向量。向量的每个元素表示对应 bin 的所需计数值。必须对输入向量进行归一化，使所有 bin 计数之和等于输入图像中的像素数。

当输入图像的数据类型为 `single` 或 `double` 时，**Hist** 端口输入必须为相同的数据类型。

#### 依赖关系

要启用此端口，请设置以下模块参数：

- **目标直方图**：
  `User-defined`
- **直方图来源**：`Input port`

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **Port\_1** — 输出图像矩阵

输出图像，返回为强度值矩阵。输出图像的数据类型与输入图像的数据类型相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

## 参数

### **目标直方图** — 所需直方图的类型 `Uniform`（默认）| `User-defined`

指定所需的直方图类型。

- `Uniform` — 该模块变换输入图像，使输出图像的直方图近似平坦。
- `User-defined` — 该模块变换输入图像，使输出图像的直方图近似匹配指定的直方图。

### **Bin 数** — 目标直方图的 bin 数 `64`（默认）| 大于一的整数

指定目标直方图的 bin 数。该模块将 bin 等间距分布。

#### 依赖关系

要启用此参数，请将 **目标直方图** 参数设置为 `Uniform`。

### **直方图来源** — 目标直方图的来源 `Specify via dialog`（默认）| `Input port`

将目标直方图的来源指定为 `Specify via dialog` 或 `Input port`。

- `Specify via dialog` — 使用 **直方图** 参数指定一个整数值向量，该向量表示目标直方图等间距 bin 的所需计数。
- `Input port` — 使用 **Hist** 输入端口指定目标直方图。

#### 依赖关系

要启用此参数，请将 **目标直方图** 参数设置为 `User-defined`。

**注意**

对使用所选 **直方图来源** 指定的输入向量进行归一化，使所有 bin 计数之和等于输入图像中的像素数。如果未对向量进行归一化，该模块不会显示错误。

### **直方图** — 目标直方图的 bin 计数 `ones(1,64)`（默认）| 整数向量

指定目标直方图每个 bin 的计数。bin 计数之和必须等于输入图像中的像素数。

#### 依赖关系

要启用此参数，请设置以下模块参数：

- **目标直方图**：
  `User-defined`
- **直方图来源**：`Specify via dialog`

## 所属库

Computer Vision Toolbox / Analysis & Enhancement

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用直方图均衡化增强图像对比度

Histogram Equalization 模块增强图像对比度。该模块变换图像中的强度值，使输出图像的直方图近似匹配指定的直方图。默认情况下，该模块变换输入图像，使输出图像的直方图接近平坦。
