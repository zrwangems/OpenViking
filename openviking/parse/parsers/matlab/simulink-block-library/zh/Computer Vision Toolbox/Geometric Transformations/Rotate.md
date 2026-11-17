---
type: simulink-block
title: 'Rotate'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Geometric Transformations'
documentation_page: 'rotate'
documentation_source_path: 'ref/rotate.html'
language: zh-CN
chinese_source: worker-translation
---

# Rotate

## 端口

### 输入

### **Image** — 要旋转的图像 矩阵 | 数组

要旋转的图像，对于灰度图像指定为二维数值矩阵，对于彩色图像指定为三维数值数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **Angle** — 旋转角度 标量

旋转角度，指定为数值标量，以弧度为单位。

如果 **Image** 端口的输入数据类型为 `single`、`double` 或 `fixed point`，则 **Angle** 端口的输入必须为相同的数据类型。

如果 **Image** 端口的输入为有符号或无符号整数数据类型，则 **Angle** 端口的输入必须为有符号整数数据类型。

#### 依赖关系

要启用此端口，请将 **Rotation angle source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
### 输出

### **Output** — 旋转后的图像 矩阵 | 数组

旋转后的图像，如果输入图像为灰度图像则返回二维数值矩阵，如果输入图像为彩色图像则返回三维数值数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

## 参数

### 主要

### **Output size** — 旋转后图像的大小 `Expanded to fit rotated input image`（默认）| `Same as input image`

将旋转后图像的大小指定为以下选项之一。

- `Expanded to fit rotated input image` - 模块输出扩展后的矩阵或数组，以包含所有值。
- `Same as input image` - 模块输出与输入图像大小相同的矩阵或数组，其中包含旋转后图像的中间部分。这可能导致模块裁剪旋转后图像的边缘。

使用 **Background fill value** 参数指定旋转后图像外部像素的颜色或强度值。

### **Rotation angle source** — 旋转角度来源 `Specify via dialog`（默认）| `Input port`

将旋转角度的来源指定为以下选项之一。

- `Specify via dialog` - 使用 **Angle (radians)** 参数指定旋转角度。
- `Input port` - 使用 **Angle** 端口指定旋转角度。模块在每个时间步使用此端口的输入作为旋转角度。

### **Angle (radians)** — 旋转角度 `pi/6`（默认）| 数值标量

以弧度为单位指定旋转角度。

当旋转角度为 `pi/2` 的倍数时，模块使用更高效的算法。如果 **Angle (radians)** 参数的指定值在 `pi/2` 的倍数的 `1e-5` 弧度范围内，则模块在执行旋转之前将角度值舍入到该 `pi/2` 的倍数。

#### 依赖关系

要启用此参数，请将 **Rotation angle source** 参数设置为 `Specify via dialog`。

### **Maximum angle (enter pi radians to accommodate all positive and negative angles)** — 最大旋转角度 `pi`（默认）| 小于或等于 `pi` 的非负标量

将输入图像的最大旋转角度指定为范围 [`0`, `pi`] 内的标量值，以弧度为单位。模块确定在 `0` 和指定最大角度之间哪个角度需要最大的输出大小，并相应地设置输出端口的维度。

#### 依赖关系

要启用此参数，请指定以下参数值。

- **Output size** — `Expanded to fit rotated input image`
- **Rotation angle source** — `Input port`

### **Display rotated image in** — 输出图像中的位置 `Top-left corner`（默认）| `Center`

指定旋转后图像在输出图像中的位置。如果选择 `Top-left corner`，模块将旋转后图像定位为其角与输出图像的顶部和左侧接触。如果选择 `Center`，输出图像将旋转后图像显示在其中心。

#### 依赖关系

要启用此参数，请将 **Rotation angle source** 参数设置为 `Input port`。

### **Sine value computation method** — 正弦值计算方法 `Table lookup`（默认）| `Trigonometric function`

指定正弦值计算方法。如果选择 `Trigonometric function`，模块在仿真期间计算图像旋转所需的正弦和余弦值。

如果选择 `Table lookup`，模块在仿真开始之前计算并存储图像旋转所需的三角函数值。对于此方法，模块需要额外的内存。

### **Background fill value** — 背景填充值 数值标量 | 三元素数值向量

为图像外部的像素指定一个值。

如果输入图像为灰度图像，**Background fill value** 的值必须为数值标量。对于灰度图像，默认值为 `0`。如果输入图像为彩色图像，**Background fill value** 的值必须为三元素数值向量。对于彩色图像，默认值为 `[0 0 0]`。

### **Interpolation method** — 插值方法 `Bilinear`（默认）| `Nearest neighbor` | `Bicubic`

从以下选项中指定模块用于旋转图像的插值方法。

- `Nearest neighbor` - 模块使用一个邻近像素的值作为新像素值。
- `Bilinear` - 新像素值是 4 个最近像素值的加权平均值。
- `Bicubic` - 新像素值是 16 个最近像素值的加权平均值。

模块考虑的像素数量影响计算的复杂度。因此，`Nearest neighbor` 插值的计算效率最高。然而，由于该方法的精度与所考虑的像素数量成正比，`Bicubic` 方法最为精确。

### 数据类型

有关通用定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

### **Angle values** — 角度值的定点参数 `Same word length as input`（默认）| `Specify word length` | `Binary point scaling`

选择如何指定角度值的字长和小数长度。

#### 依赖关系

要启用此参数，请将 **Rotation angle source** 参数设置为 `Specify via dialog`。

### **Lock data type settings against change by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在此模块中指定的数据类型。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

## 所属库

Computer Vision Toolbox / Geometric Transformations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

按指定角度旋转图像

使用 Rotate 模块按以弧度为单位指定的角度旋转灰度或彩色图像。
