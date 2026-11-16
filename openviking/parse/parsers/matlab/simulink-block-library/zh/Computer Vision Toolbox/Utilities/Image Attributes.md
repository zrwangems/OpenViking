---
type: simulink-block
title: 'Image Attributes'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'imageattributes'
documentation_source_path: 'ref/imageattributes.html'
language: zh-CN
chinese_source: worker-translation
---

# Image Attributes

## 端口

### 输入

### **Port\_1** — Input signal `Simulink.ImageType`

输入到 Image Attributes 模块的输入信号。该输入是 Simulink 图像数据类型。

**数据类型：** `Simulink.ImageType`
### 输出

### **rows** — 图像数据中的行数（标量）

图像数据中的行数，以正整数形式返回。

**数据类型：** `uint32`

### **columns** — 图像数据中的列数（标量）

图像数据中的列数，以正整数形式返回。

**数据类型：** `uint32`

### **channels** — 数组中每个像素的颜色通道数或样本数（标量）

数组中每个像素的颜色通道数或样本数，以 `1`、`3` 或 `4` 形式返回。通道数对应于图像数据的颜色格式中的颜色通道数。以下是受支持颜色格式的 `Channels` 值：

| 颜色格式 | 通道数 |
| --- | --- |
| `Grayscale` | `1` |
| `RGB` | `3` |
| `BGR` | `3` |
| `BGRA` | `4` |

**数据类型：** `uint32`

### **class** — 底层图像数据的数据类型 string

底层图像数据的数据类型，返回为以下值之一：

- `'uint8'`
- `'int8'`
- `'uint16'`
- `'int16'`
- `'uint32'`
- `'int32'`
- `'single'`
- `'double'`
- `'boolean'`

**数据类型：** `string`

### **color** — 底层图像数据的颜色格式 string

底层图像数据的颜色格式，返回为 `'RGB'`、`'Grayscale'`、`'BGR'` 或 `'BGRA'`。颜色格式决定图像中像素的每个颜色通道表示的内容。

**数据类型：** `string`

### **layout** — 图像数据的数组布局 string

图像中矩阵数据的内存排列，返回为 `'ColumnMajor'` 或 `'RowMajor'`。

**数据类型：** `string`

## 参数

在 R2025b 中未记录。

## 所属库

Computer Vision Toolbox / Utilities

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `integer` | `string` | `image` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |
| **零交叉检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

支持 C++ 代码生成。

## 版本历史

**在 R2022b 中引入**

## 描述

输出 Simulink 图像信号的属性

Image Attributes 模块以数值数据形式输出 Simulink 图像信号的属性。可使用 Image Attributes 模块来：

- 为调试目的显示图像属性。
- 在图像处理算法的控制流或数据流中使用图像属性。
