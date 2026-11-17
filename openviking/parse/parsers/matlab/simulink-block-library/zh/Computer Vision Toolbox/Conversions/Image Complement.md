---
type: simulink-block
title: 'Image Complement'
family: 'conversions'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Conversions'
documentation_page: 'imagecomplement'
documentation_source_path: 'ref/imagecomplement.html'
language: zh-CN
chinese_source: worker-translation
---

# Image Complement

## 端口

### 输入

### **Port\_1** — 输入图像矩阵

将输入图像指定为强度值矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`
### 输出

### **Port\_1** — 输出图像矩阵

二值或强度输入图像的补值以强度值矩阵形式返回。输出图像的大小和数据类型与输入图像相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean`

## 参数

在 R2025b 中未记录。

## 所属库

Computer Vision Toolbox / Conversions

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

计算二值图像或强度图像中像素值的补值

Image Complement 模块计算二值图像或强度图像的补值。

对于二值图像，该模块将等于 `0` 的像素值替换为 `1`，将等于 `1` 的像素值替换为 `0`。在输出图像中，黑色和白色反转。对于强度图像，该模块从输入数据类型可表示的最大值中减去每个像素值，并输出差值。在输出图像中，暗区变亮，亮区变暗。

例如，假设输入像素值由 *x*(i) 给出，输出像素值由 *y*(i) 给出。如果输入的数据类型为 boolean、double 或 single，则该模块输出 *y*(i) = 1.0-*x*(i)。如果输入为 8 位无符号整数，则该模块输出 *y*(i) = 255-*x*(i)。
