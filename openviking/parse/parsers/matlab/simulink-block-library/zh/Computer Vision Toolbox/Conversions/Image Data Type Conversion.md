---
type: simulink-block
title: 'Image Data Type Conversion'
family: 'conversions'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Conversions'
documentation_page: 'imagedatatypeconversion'
documentation_source_path: 'ref/imagedatatypeconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# Image Data Type Conversion

## 端口

### 输入

### **I** — 输入图像矩阵 | 数组

输入图像，指定为 *M*-by-*N* 矩阵或 *M*-by-*N*-by-*C* 数组，其中 *C* 是输入图像中的颜色通道数。

**数据类型：** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出图像矩阵 | 数组

输出图像，返回为 *M*-by-*N* 矩阵或 *M*-by-*N*-by-*C* 数组，其中 *C* 是输出图像中的颜色通道数。

**数据类型：** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixed point`

## 参数

### **Output data type** — 输出数据类型 `double` (默认) | `single` | `int8` | `uint8` | `int16` | `uint16` | `boolean` | `Fixed-point` | `Inherit via back propagation`

指定输出信号的数据类型。

### **Signed** — 有符号输出 `on` (默认) | `off`

将输出信号的定点数据类型指定为有符号。

#### 依赖关系

要启用此参数，请将 **Output data type** 参数设置为 `Fixed-point`。

### **Word length** — 字长 `16` (默认) | 标量

指定定点输出的字长。

#### 依赖关系

要启用此参数，请将 **Output data type** 参数设置为 `Fixed-point`。

### **Fraction length** — 小数长度 `0` (默认) | 标量

指定定点输出的小数长度。

#### 依赖关系

要启用此参数，请将 **Output data type** 参数设置为 `Fixed-point`。

## 所属库

Computer Vision Toolbox / Conversions

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed pointa` | `integera` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a 支持小于或等于 16 bits 的字长。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

将输入图像转换并缩放到指定的输出数据类型

Image Data Type Conversion 模块将输入图像的数据类型转换为指定的数据类型，并将像素值缩放到输出数据的动态范围。若要在数据类型之间进行转换而不进行缩放，请使用 Data Type Conversion (Simulink) 模块。

该模块的行为因图像的输入和输出数据类型而异。

- 在浮点数据类型之间转换时，模块将输入值强制转换为输出数据类型，并将低于或高于输出数据类型范围的值分别限幅为 `0` 或 `1`。
- 当转换为 `Boolean` 数据类型时，模块将 `0` 值映射为 `0` (`false`)，将所有其他值映射为 `1` (`true`)。
- 在所有其他数据类型之间，模块将输入数据类型的值强制转换并缩放到输出数据类型的动态范围。对于 double 和 single 精度的浮点数据类型，动态范围在 `0` 和 `1` 之间。对于定点数据类型，动态范围在该数据类型的最小和最大像素值之间。
