---
type: simulink-block
title: 'ToOpenCV'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Code Generation, GPU, and Third-Party Support / OpenCV Interface for Simulink'
documentation_page: 'toopencv'
documentation_source_path: 'ref/toopencv.html'
language: zh-CN
chinese_source: worker-translation
---

# ToOpenCV

## 端口

### 输入

### **Port\_1** — 输入信号 scalar | vector | matrix | simulink bus | simulink image

ToOpenCV 模块的输入信号。输入可以具有不同的数据类型。每个输入数据类型决定模块的输出数据类型。

**数据类型：** `uint8` | `uint16` | `int8` | `int16` | `int32` | `single` | `double` | `Simulink.ImageType` | `CV_DMATCH_BUS` | `CV_RECT_BUS` | `CV_ROTATEDRECT_BUS` | `CV_TERMCRITERIA_BUS` | `CV_SIZE_BUS` | `CV_RANGE_BUS` | `CV_POINT2I_BUS` | `CV_POINT2F_BUS` | `CV_POINT2D_BUS` | `CV_POINT3I_BUS` | `CV_POINT3F_BUS` | `CV_POINT3D_BUS`
### 输出

### **Port\_1** — 输出信号 scalar | vector | matrix | simulink bus | simulink image

ToOpenCV 模块的输出信号。输出信号支持 OpenCV 类型。有关详细信息，请参阅 Mapping Input and Output Data Types。

**数据类型：** `OpenCV types`

## 参数

### **DataType** — ToOpenCV 模块输入信号的数据类型 `input data type`（默认）

指定 ToOpenCV 模块的输入数据类型。表中列出了 ToOpenCV 模块输入与输出数据类型的一一映射。

#### 编程使用

|  |
| --- |
| **模块参数：** `DataType` |
| **类型：** character vector |
| **值：** 输入数据类型 |
| **默认：** `'Point2i'` |

## 所属库

Computer Vision Toolbox Interface for OpenCV in Simulink

## 模块特性

|  |  |
| --- | --- |
| **数据类型** |  |
| **直接馈通** | `Yes` |
| **多维信号** | `Yes` |
| **可变大小信号** | `No` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

支持 C++ 代码生成。

## 版本历史

**在 R2020a 中引入**

## 描述

将 Simulink 数据类型转换为 OpenCV 数据类型

ToOpenCV 模块将 Simulink® 数据类型转换为 Simulink OpenCV 数据类型。
