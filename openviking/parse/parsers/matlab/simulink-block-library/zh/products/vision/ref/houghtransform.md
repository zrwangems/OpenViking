---
type: simulink-block
title: 'Hough Transform'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Filters, Transforms, and Enhancements'
documentation_page: 'houghtransform'
documentation_source_path: 'ref/houghtransform.html'
language: zh-CN
chinese_source: worker-translation
---

# Hough Transform

## 端口

### 输入

### **BW** — 二值图像矩阵

二值图像，指定为 `Boolean` 值的矩阵。

**数据类型：** `Boolean`
### 输出

### **Hough** — 参数空间矩阵矩阵

参数空间矩阵，返回为数值矩阵。参数空间矩阵中的值位于 (*rho, theta*) 空间。

**数据类型：** `single` | `double` | `fixed point`

### **Theta** — Theta 值向量

Theta 值，返回为数值向量。每个元素表示对应直线的旋转角度，以 radians 为单位。

#### 依赖项

要启用此端口，您必须选择 **输出 theta 和 rho 值** 参数。

**数据类型：** `single` | `double` | `fixed point`

### **Rho** — Rho 值向量

Rho 值，返回为数值向量。每个元素表示对应直线距图像左上点的距离。

#### 依赖项

要启用此端口，您必须选择 **输出 theta 和 rho 值** 参数。

**数据类型：** `single` | `double` | `fixed point`

## 参数

### 主要

### **Theta 分辨率 (radians)** — Theta 分辨率 `pi/180`（默认） | 正标量

指定 Hough 变换 bin 沿 *theta* 轴的间距。此值必须小于 `pi/2`。

### **Rho 分辨率 (pixels)** — Rho 分辨率 `1`（默认） | 正标量

指定 Hough 变换 bin 沿 *rho* 轴的间距。

### **输出 theta 和 rho 值** — 启用 Theta 和 Rho 输出端口 `off`（默认） | `on`

选择此参数可启用 **Theta** 和 **Rho** 输出端口。模块在这些端口分别输出 *theta* 轴和 *rho* 轴向量。

### **输出数据类型** — 输出数据类型 `double`（默认） | `single` | `Specify via Fixed-point tab`

指定输出信号的数据类型。如果选择 `double` 或 `single`，所有输出均为指定的数据类型。如果选择 `Specify via Fixed-point tab`，您可以在 **数据类型** 选项卡中指定每个输出的字长。

### 数据类型

有关定点模块参数的详细信息，请参阅为模块指定定点属性 (DSP System Toolbox)。

### **锁定数据类型设置以防止定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认） | `on`

选择此参数可防止定点工具覆盖您在此模块中指定的数据类型。有关详细信息，请参阅锁定输出数据类型设置 (Fixed-Point Designer)。

## 所属库

Computer Vision Toolbox / Transforms

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `doublea` | `fixed point` | `integer` | `singlea` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a 此数据类型在输出端口受支持。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

在图像中查找直线

使用 Hough Transform 模块在图像中查找直线。该模块输出 Hough 空间矩阵，并可选地输出 *rho* 轴和 *theta* 轴向量。矩阵中的峰值表示输入图像中的潜在直线。您可以使用 Hough Transform 模块的输出，通过 Hough Lines 模块在图像中查找直线。或者，您也可以使用自定义算法，通过定位 Hough 空间矩阵中的峰值来识别潜在直线。
