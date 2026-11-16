---
type: simulink-block
title: 'FromOpenCV'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Code Generation, GPU, and Third-Party Support / OpenCV Interface for Simulink'
documentation_page: 'fromopencv'
documentation_source_path: 'ref/fromopencv.html'
language: zh-CN
chinese_source: worker-translation
---

# FromOpenCV

## 端口

### 输入

### **Port\_1** — 第一个输入信号 标量 | 向量 | 矩阵 | simulink bus | simulink image

FromOpenCV 模块的输入信号。该输入可以具有不同的数据类型。每个输入数据类型决定该模块的输出数据类型。有关详细信息，请参阅映射输入和输出数据类型。

**数据类型：** `OpenCV types`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵 | simulink bus | simulink image

FromOpenCV 模块的输出信号。

**数据类型：** `Converted Simulink types`

## 参数

### **DataType** — FromOpenCV 模块的输入信号的数据类型 `input data type`（默认）

指定 FromOpenCV 模块的输入数据类型。该表列出了 FromOpenCV 模块的输入数据类型与输出数据类型的一对一映射。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataType` |
| **类型：** character vector |
| **值：** input data type |
| **默认值：** `'Point2i'` |

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

将 OpenCV 数据类型转换为 Simulink 数据类型

FromOpenCV 模块将 Simulink® OpenCV 数据类型转换为 Simulink 数据类型。
