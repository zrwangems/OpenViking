---
type: simulink-block
title: 'Matrix To Image'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Code Generation, GPU, and Third-Party Support / OpenCV Interface for Simulink'
documentation_page: 'matrixtoimage'
documentation_source_path: 'ref/matrixtoimage.html'
language: zh-CN
chinese_source: worker-translation
---

# Matrix To Image

## 端口

### 输入

### **Port\_1** — 输入信号矩阵

输入到 Matrix To Image 模块的输入信号。输入是数值矩阵。

**数据类型：** `uint8` | `uint16` | `int8` | `int16` | `single` | `double`
### 输出

### **Port\_1** — 输出信号 `Simulink.ImageType`

来自 Matrix To Image 模块的输出信号。输出是 `Simulink.ImageType` 数据类型的图像。

**数据类型：** `Simulink.ImageType`

## 参数

### **Rows** — 图像数据中的行数 `'480'`（默认） | 正整数

将图像数据中的行数指定为正整数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Rows` |
| **类型：** `double` |
| **值：** 正整数 |
| **默认值：** `'480'` |

### **Columns** — 图像数据中的列数 `'640'`（默认） | 正整数

将图像数据中的列数指定为正整数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Columns` |
| **类型：** `double` |
| **值：** 正整数 |
| **默认值：** `'640'` |

### **Channels** — 数组中每个像素的颜色通道数或样本数 `3`（默认） | `1`

将数组中每个像素的颜色通道数或样本数指定为 `1` 或 `3`。通道数必须与图像数据的颜色格式中的颜色通道数相对应。以下是支持的颜色格式对应的 **Channels** 值：

| Channels | Color Format |
| --- | --- |
| `1` | `Grayscale` |
| `3` | `RGB` |
| `3` | `BGR` |

#### 程序化使用

|  |
| --- |
| **模块参数：** `Columns` |
| **类型：** character vector |
| **值：** 正整数 |
| **默认值：** `'3'` |

### **Underlying Datatype** — 底层图像数据的数据类型 `'uint8'`（默认） | `'int8'` | `'uint16'` | `'int16'` | `'uint32'` | `'int32'` | `'single'` | `'double'` | `'logical'`

将底层图像数据的数据类型指定为以下选项之一：

- `'uint8'`
- `'int8'`
- `'uint16'`
- `'int16'`
- `'uint32'`
- `'int32'`
- `'single'`
- `'double'`
- `'logical'`

#### 程序化使用

|  |
| --- |
| **模块参数：** `ClassUnderlying` |
| **类型：** character vector |
| **值：** `'uint8'` | `'int8'` | `'uint16'` | `'int16'` | `'uint32'` | `'int32'` | `'single'` | `'double'` | `'logical'` |
| **默认值：** `'uint8'` |

### **Array Layout** — 图像中矩阵数据的内存排列 `'Column-major'`（默认） | `'Row-major'`

将图像中矩阵数据的内存排列指定为 `Column-major` 或 `Row-major`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Layout` |
| **类型：** character vector |
| **值：** `'Column-major'` | `'Row-major'` |
| **默认值：** `'Column-major'` |

### **Color Format** — 底层图像数据中像素的颜色格式 `'RGB'`（默认） | `'Grayscale'` | `'BGR'`

将底层图像数据中像素的每个颜色通道表示的内容指定为 `Grayscale`、`RGB` 或 `BGR`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ColorFormat` |
| **类型：** character vector |
| **值：** `'Grayscale'` | `'RGB'` | `'BGR'` |
| **默认值：** `'RGB'` |

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

将矩阵数据转换为 Simulink 图像数据

Matrix To Image 模块将矩阵数据转换为 Simulink® 图像数据。
