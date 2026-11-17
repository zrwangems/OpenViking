---
type: simulink-block
title: 'Warp'
family: 'vision'
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

### **Image** — 输入图像 矩阵 | 三维数值数组

输入图像，指定为以下值之一：

- 矩阵 — 用于大小为
  *M*×*N* 的灰度图像。
- 三维数值数组 — 用于大小为
  *M*×*N*×3 的真彩色图像。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **TForm** — 变换矩阵 3×2 矩阵 | 3×3 矩阵

变换矩阵，指定为以下值之一：

- 3×2 矩阵 — 用于仿射变换。
- 3×3 矩阵 — 用于投影变换。

有关变换的详细信息，请参阅算法。

#### 依赖关系

要启用此输入端口，请将 **Transformation matrix
source** 参数值设置为 `Input port`。

**数据类型：** `double` | `single`

### **ROI** — 感兴趣区域 四元素向量

感兴趣区域，指定为形式为
[*xs*
*ys*
*width*
*height*] 的四元素向量。*xs* 和
*ys* 分别是 ROI 左上角的 *x* 和
*y* 坐标。

如果指定 `ROI` 输入，`Warp` 模块仅对指定的区域应用变换，并在输出端返回变换后的区域。

#### 依赖关系

要启用此输入端口，请选中 **Enable ROI input port**
参数。
### 输出

### **Image** — 变换后的图像 矩阵 | 三维数值数组

变换后的图像，返回为以下值之一：

- 矩阵 — 如果输入是大小为
  *P*×*Q1* 的灰度图像。
- 三维数值数组 — 如果输入是大小为
  *P*×*Q*×3 的真彩色图像。

输出变换图像的数据类型与输入图像的数据类型相同。输出变换图像的大小可以与输入图像相同，也可以等于 **Output image position vector [x y
width height]** 参数设置的值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Err\_roi** — 变换后的 ROI 是否在图像区域外的指示符 `0` | `1`

变换后的 ROI 是否在图像区域外的指示符，返回为
`0` 或 `1`。

**数据类型：** `Boolean`

## 参数

### **Transformation matrix for source** — 传递变换矩阵的来源 `Input port`（默认）| `Custom`

传递变换矩阵的来源，指定为 `Input
port` 或 `Custom`。如果选择
`Custom`，可以使用随该选择出现的 **Transformation matrix** 参数输入变换矩阵系数。

### **Transformation matrix** — 变换矩阵的值 3×2 矩阵 | 3×3 矩阵

变换矩阵的值，指定为用于仿射变换的 3×2 矩阵或用于投影变换的 3×3 矩阵。

#### 依赖关系

要启用此参数，请将 **Transformation matrix for
source** 参数值设置为 `Custom`。

### **Interpolation method** — 插值变换后像素值的方法 `Bilinear`（默认）| `Nearest neighbor` | `Bicubic`

插值变换后像素值的方法，指定为 `Nearest
neighbor`、`Bilinear` 或
`Bicubic`。

如果选择 `Nearest neighbor`，模块使用附近像素的值作为新像素值。如果选择
`Bilinear`，新像素值是四个最近像素值的加权平均值。如果选择 `Bicubic`，新像素值是十六个最近像素值的加权平均值。

模块考虑的像素数量会影响计算的复杂度。因此，`Nearest neighbor` 插值在计算上最高效。然而，由于该方法的精度与所考虑的像素数量成正比，`Bicubic` 方法最精确。有关插值方法的信息，请参阅详细信息部分。

### **Background fill value** — 变换后图像中背景像素的强度值 `0`（默认）| 标量 | 三元素向量

变换后图像中背景像素的强度值，指定为以下值之一：

- 标量 — 如果输入图像是灰度图像。
- 三元素向量 — 如果输入图像是真彩色图像。该向量形式为 [*r*
  *g*
  *b*]，指定背景像素的红色（*r*）、绿色
  （*g*）和蓝色（*b*）通道值。

默认填充值为 `0`，将背景颜色设置为黑色。

### **Output image position source** — 传递输出图像大小的来源 `Same as input image`（默认）| `Custom`

传递输出图像大小值的来源，指定为
`Same as input image` 或 `Custom`。

- 如果选择 `Same as input image`，输出变换图像的大小与输入图像的大小相同。
- 如果选择 `Custom`，必须指定一个边界框，以仅输出位于边界框内的图像区域。此选择会启用 **Output image position vector [x y width
  height]** 参数，可用于指定边界框值。

### **Output image position vector [x y width height]** — 输出图像的大小 [`1` `1` `512` `512`]（默认）| 四元素向量

输出图像的大小，指定为形式为
[*x*
*y*
*width*
*height*] 的四元素向量。指定此参数时，`Warp` 模块会创建具有指定宽度和高度值的边界框。输出图像的大小设置为边界框的大小，并将包含位于边界框内的变换图像区域。如果输出图像的大小大于边界框内变换图像区域的大小，则输出图像中多余像素的强度值将设置为 **Background fill value** 参数指定的值。

输出图像位置向量示意图

*x* 和 *y* 是定义边界框左上角相对于输入图像位置的空间坐标。

#### 依赖关系

要启用此参数，请将 **Output image position
source** 参数值设置为 `Custom`。

### **Enable ROI input port** — 输入 ROI 关闭（默认）| 打开

选中此参数以启用 `ROI` 输入端口，并指定要变换的 ROI。

### **Enable output port indicating if any part of ROI is outside input image** — 变换后的 ROI 是否在指定图像大小之外的输出 关闭（默认）| 打开

选中此参数以启用 `Err_roi` 输出端口。

#### 依赖关系

要启用此参数，请选中 **Enable ROI input port**
参数。

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真方法，指定为 `Interpreted Execution` 或
`Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

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

应用投影或仿射变换

Warp 模块通过应用投影或仿射变换来变换图像。可以通过定义矩形感兴趣区域（ROI）来变换整个图像或图像的一个区域。
