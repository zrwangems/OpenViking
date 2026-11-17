---
type: simulink-block
title: 'Warp'
family: 'geometric-transformations'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Geometric Transformations'
documentation_page: 'warp'
documentation_source_path: 'ref/warp.html'
language: zh-CN
chinese_source: worker-translation
---

# Warp

## 端口

### 输入

### **Image** — 输入图像矩阵 | 3-D 数值数组

输入图像，指定为以下值之一：

- 矩阵 — 用于大小为
  *M*-by-*N* 的强度图像。
- 3-D 数值数组 — 用于大小为
  *M*-by-*N*-by-3 的真彩色图像。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **TForm** — 变换矩阵 3-by-2 矩阵 | 3-by-3 矩阵

变换矩阵，指定为以下值之一：

- 3-by-2 矩阵 — 用于仿射变换。
- 3-by-3 矩阵 — 用于投影变换。

有关变换的详细信息，请参阅算法。

#### 依赖项

要启用此输入端口，请将 **Transformation matrix
source** 参数值设置为 `Input port`。

**数据类型：** `double` | `single`

### **ROI** — 感兴趣区域 4 元素向量

感兴趣区域，指定为以下形式的 4 元素向量
[*xs*
*ys*
*width*
*height*]。*xs* 和
*ys* 分别是 ROI 左上角的 *x* 和
*y* 坐标。

如果指定 `ROI` 输入，则
`Warp` 模块仅对指定区域应用变换，并在输出处返回变换后的区域。

#### 依赖项

要启用此输入端口，请选择 **Enable ROI input port**
参数。
### 输出

### **Image** — 变换后的图像矩阵 | 3-D 数值数组

变换后的图像，返回为以下值之一：

- 矩阵 — 如果输入是大小为
  *P*-by-*Q1* 的强度图像。
- 3-D 数值数组 — 如果输入是大小为
  *P*-by-*Q*-by-3 的真彩色图像。

输出变换后图像的数据类型与输入图像相同。输出变换后图像的大小要么与输入图像相同，要么等于为 **Output image position vector [x y
width height]** 参数设置的值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Err\_roi** — 变换后 ROI 在图像区域之外的指示符 `0` | `1`

变换后 ROI 在图像区域之外的指示符，返回为
`0` 或 `1`。

**数据类型：** `Boolean`

## 参数

### **Transformation matrix for source** — 用于传递变换矩阵的来源 `Input port` (默认) | `Custom`

用于传递变换矩阵的来源，指定为 `Input
port` 或 `Custom`。如果选择
`Custom`，则可以使用随此选择出现的 **Transformation matrix** 参数输入变换矩阵
系数。

### **Transformation matrix** — 变换矩阵的值 3-by-2 矩阵 | 3-by-3 矩阵

变换矩阵的值，指定为用于仿射变换的 3-by-2 矩阵或用于投影变换的 3-by-3 矩阵。

#### 依赖项

要启用此参数，请将 **Transformation matrix for
source** 参数值设置为 `Custom`。

### **Interpolation method** — 用于对变换后的像素值进行插值的方法 `Bilinear` (默认) | `Nearest neighbor` | `Bicubic`

用于对变换后的像素值进行插值的方法，指定为 `Nearest
neighbor`、`Bilinear` 或
`Bicubic`。

如果选择 `Nearest neighbor`，该模块将使用附近像素的值作为新像素值。如果选择
`Bilinear`，则新像素值是四个最近像素值的加权平均值。如果选择 `Bicubic`，则新
像素值是十六个最近像素值的加权平均值。

该模块考虑的像素数会影响计算的复杂度。
因此，`Nearest neighbor` 插值在计算上最高效。但是，由于该方法的精度与
所考虑的像素数成正比，`Bicubic` 方法最准确。有关插值方法的信息，请参阅
更多信息部分。

### **Background fill value** — 变换后图像中背景像素的强度值 `0` (默认) | scalar | 3-element vector

变换后图像中背景像素的强度值，指定为以下值之一：

- 标量 — 如果输入图像是灰度图像。
- 3 元素向量 — 如果输入图像是真彩色图像。该向量采用 [*r*
  *g*
  *b*] 形式，用于指定背景像素的红色 (*r*)、绿色
  (*g*) 和蓝色 (*b*) 颜色通道值。

默认填充值为 `0`，并将背景
颜色设置为黑色。

### **Output image position source** — 用于传递输出图像大小的来源 `Same as input image` (默认) | `Custom`

用于传递输出图像大小值的来源，指定为
`Same as input image` 或 `Custom`。

- 如果选择 `Same as input image`，则输出
  变换后图像的大小与输入图像的大小相同。
- 如果选择 `Custom`，则必须指定一个边界
  框，以便仅输出位于该边界框内的图像区域。此
  选择会启用 **Output image position vector [x y width
  height]** 参数，您可以使用该参数指定边界框
  值。

### **Output image position vector [x y width height]** — 输出图像的大小 [`1` `1` `512` `512`] (默认) | 4-element vector

输出图像的大小，指定为以下形式的四元素向量
[*x*
*y*
*width*
*height*]。指定此参数时，
`Warp` 模块会创建一个具有指定宽度和
高度值的边界框。输出图像的大小设置为边界框的大小，并
将包含位于边界框内的变换后图像区域。如果输出图像的大小
大于边界框内变换后图像区域的大小，则输出图像中多余像素的强度值将设置
为 **Background fill value** 参数指定的值。

输出图像位置向量图示

*x* 和 *y* 是空间
坐标，用于定义边界框左上角相对于
输入图像的位置。

#### 依赖项

要启用此参数，请将 **Output image position
source** 参数值设置为 `Custom`。

### **Enable ROI input port** — 输入 ROI off (默认) | on

选择此参数可启用 `ROI` 输入端口，并指定
要变换的 ROI。

### **Enable output port indicating if any part of ROI is outside input image** — 如果变换后的 ROI 在指定图像大小之外则输出 off (默认) | on

选择此参数可启用 `Err_roi` 输出端口。

#### 依赖项

要启用此参数，请选择 **Enable ROI input port**
参数。

### **Simulate using** — 模块仿真方法 `Interpreted Execution` (默认) | `Code Generation`

模块仿真方法，指定为 `Interpreted Execution` 或
`Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望
模块作为编译代码运行，请选择 `Code Generation`。有关更多
信息，请参阅 Choosing a Simulation Mode (Simulink)。

## 所属库

Computer Vision Toolbox / Geometric Transformations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015b 中引入**

## 描述

应用投影变换或仿射变换

Warp 模块通过应用投影变换或仿射变换来变换图像。您可以通过定义矩形感兴趣区域 (ROI) 来变换整个图像或
图像的一个区域。
