---
type: simulink-block
title: 'From Simulink Image'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'fromsimulinkimage'
documentation_source_path: 'ref/fromsimulinkimage.html'
language: zh-CN
chinese_source: worker-translation
---

# From Simulink Image

## 端口

### 输入

### **Port\_1** — 输入信号 `Simulink.ImageType`

From Simulink Image 模块的输入信号。输入是 Simulink 图像数据类型。

**数据类型：** `Simulink.ImageType`
### 输出

### **Port\_1** — 输出信号矩阵

From Simulink Image 模块的输出信号。输出是矩阵或数组，具体取决于输入的格式。

- *M*×*N* 矩阵 — 输入是 `Grayscale` 图像。*M* 和 *N* 是图像的高度和宽度，单位为 pixels。
- *M*×*N*×*C* 矩阵 — 输入是 `RGB` 或 `BGR` 图像。*M* 和 *N* 是图像的高度和宽度，单位为 pixels。*C* 是颜色通道数。

**数据类型：** `integer` | `single` | `double` | `Boolean`

## 参数

### **输出维度** — 模块输出信号的维度 `[480 640 3]`（默认）

指定输出图像信号的维度。表达式必须是形式为 `[Rows Columns Channels]` 的三元素数值行向量。

#### 编程使用

|  |
| --- |
| **模块参数：** `ImageSize` |
| **类型：** character vector |
| **值：** character vector |
| **默认值：** `[480 640 3]` |

## 所属库

Computer Vision Toolbox / Utilities

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` | `integer` | `Boolean` | `image` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

支持 C++ 代码生成。

## 版本历史

**在 R2022a 中引入**

## 描述

从 Simulink 图像解包数值矩阵

From Simulink Image 模块将 Simulink® 图像数据转换为矩阵数据。
