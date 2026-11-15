---
type: simulink-block
title: 'Demosaic'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Color Space Formatting and Conversions'
documentation_page: 'demosaic'
documentation_source_path: 'ref/demosaic.html'
language: zh-CN
chinese_source: worker-translation
---

# Demosaic

## 端口

### 输入

### **I** — 要去马赛克的图像矩阵

要去马赛克的图像，指定为二维数值矩阵。矩阵的大小要求取决于 **插值算法** 参数的值。

- 如果 **插值算法** 的值为
  `Bilinear`，矩阵必须具有三行或更多行以及三列或更多列。
- 如果 **插值算法** 的值为
  `Gradient-corrected linear`，矩阵必须具有五行或更多行以及五列或更多列。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **R** — 处理后图像的红色通道矩阵

处理后图像的红色通道，返回为与 **I** 大小和数据类型相同的二维数值矩阵。

#### 依赖项

要启用此端口，请将 **输出图像信号** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **G** — 处理后图像的绿色通道矩阵

处理后图像的绿色通道，返回为与 **I** 大小和数据类型相同的二维数值矩阵。

#### 依赖项

要启用此端口，请将 **输出图像信号** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **B** — 处理后图像的蓝色通道矩阵

处理后图像的蓝色通道，返回为与 **I** 大小和数据类型相同的二维数值矩阵。

#### 依赖项

要启用此端口，请将 **输出图像信号** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Image** — 多维处理后图像矩阵

多维处理后图像，返回为与 **I** 数据类型相同的三维数值矩阵。如果输入图像 **I** 的维度为 *M*×*N*，则 **Image** 的维度为 *M*×*N*×*P*，其中 *P* 是颜色通道数。

#### 依赖项

要启用此端口，请将 **输出图像信号** 参数指定为 `One multidimensional signal`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### 主要

### **插值算法** — 插值算法 `Bilinear` (default) | `Gradient-corrected linear`

指定该模块用于计算缺失颜色信息的算法。如果选择 `Bilinear`，该模块会对缺失颜色值的相邻像素值进行空间平均，以计算其颜色信息。

如果选择 `Gradient-corrected linear`，该模块使用 Weiner 方法最小化插值中的均方误差。该方法在图像中对象的边缘处表现良好。两种方法都在图像边界处使用对称填充。有关详细信息，请参阅 Image Pad 模块参考页。

### **传感器对齐** — R,G,B 像素对齐 `RGGB` (default) | `GRBG` | `GBRG` | `BGGR`

指定输入图像的对齐方式。选择与图像左上角 2×2 像素块对应的 R、G 和 B 像素序列。按从左到右、从上到下的顺序指定该序列。例如，对于此图像，应选择 `BGGR`。

4×4 Bayer 格式图像的图示，其中每个像素标记为 R、G 或 B。

### **输出图像信号** — 输出图像的维度 `One multidimensional signal` (default) | `Separate color signals`

指定如何输出 RGB 图像。给定 *M*×*N* 输入图像，此参数通过以下方式影响该模块的输出。

- `One multidimensional image` — 该模块有一个端口 Image，输出 *M*×*N*×*P* RGB 图像，其中 *P* 是颜色通道数。
- `Separate color signals` — 该模块有三个端口 R、G 和 B，每个端口输出 RGB 图像的一个 *M*×*N* 颜色通道。

### 数据类型

有关定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

### **锁定数据类型设置以防定点工具更改** — 防止定点工具覆盖数据类型 `off` (default) | `on`

选择此参数可防止定点工具覆盖您在此模块中指定的数据类型。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

## 所属库

Computer Vision Toolbox / Conversions

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006b 中引入**

## 描述

对 Bayer 格式图像进行去马赛克

Demosaic 模块接受 Bayer 格式图像并输出 RGB 图像。该模块使用梯度校正线性插值算法或双线性插值算法执行此操作。下图展示了一个 4×4 Bayer 格式图像，其中每个像素标记为 R、G 或 B。

4×4 Bayer 格式图像的图示，其中每个像素标记为 R、G 或 B。
