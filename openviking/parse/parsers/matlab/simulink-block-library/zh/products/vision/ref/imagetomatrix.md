---
type: simulink-block
title: 'Image To Matrix'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Code Generation, GPU, and Third-Party Support / OpenCV Interface for Simulink'
documentation_page: 'imagetomatrix'
documentation_source_path: 'ref/imagetomatrix.html'
language: zh-CN
chinese_source: worker-translation
---

# Image To Matrix

## 端口

### 输入

### **Port\_1** — 输入信号 `Simulink.ImageType`

Image To Matrix 模块的输入信号。输入是 Simulink 图像数据类型。

**数据类型：** `Simulink.ImageType`
### 输出

### **Port\_1** — 输出信号矩阵

Image To Matrix 模块的输出信号。输出是矩阵或数组，具体取决于输入的格式。

- *M*×*N* 矩阵 — 输入是 `Grayscale` 图像。*M* 和 *N* 是图像的高度和宽度，以像素为单位。
- *M*×*N*×*C* 矩阵 — 输入是 `RGB` 或 `BGR` 图像。*M* 和 *N* 是图像的高度和宽度，以像素为单位。*C* 是颜色通道数。

**数据类型：** `uint8` | `uint16` | `int8` | `int16` | `single` | `double`

## 参数

### **Rows** — 图像数据中的行数 `'480'` (默认) | 正整数

将图像数据中的行数指定为正整数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Rows` |
| **类型：** `double` |
| **值：** 正整数 |
| **默认值：** `'480'` |

### **Columns** — 图像数据中的列数 `'640'` (默认) | 正整数

将图像数据中的列数指定为正整数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Columns` |
| **类型：** `double` |
| **值：** 正整数 |
| **默认值：** `'640'` |

### **Channels** — 每个像素的颜色通道数或样本数 `3` (默认) | `1`

将数组中每个像素的颜色通道数或样本数指定为 `1` 或 `3`。通道数必须与图像数据的颜色格式中的颜色通道数对应。以下是支持的色彩格式对应的 **Channels** 值：

| 色彩格式 | Channels |
| --- | --- |
| `Grayscale` | `1` |
| `RGB` | `3` |
| `BGR` | `3` |

#### 程序化使用

|  |
| --- |
| **模块参数：** `Channels` |
| **类型：** `double` |
| **值：** 正整数 |
| **默认值：** `'3'` |

## 所属库

Computer Vision Toolbox OpenCV Interface for Simulink

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` | `uint8` | `uint16` | `int8` | `int16` | `int32` | `image` |
| **直接馈通** | `Yes` |
| **多维信号** | `Yes` |
| **可变大小信号** | `No` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

支持 C++ 代码生成。

## 版本历史

**在 R2021b 中引入**

## 描述

将 Simulink 图像数据转换为矩阵数据

Image To Matrix 模块将 Simulink® 图像数据转换为矩阵数据。
