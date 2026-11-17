---
type: simulink-block
title: 'Demosaic'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Conversions'
documentation_page: 'demosaic'
documentation_source_path: 'ref/demosaic.html'
language: zh-CN
chinese_source: worker-translation
---

# Demosaic

## 端口

### 输入

### **I** — 待去马赛克的图像 矩阵

待去马赛克的图像，指定为二维数值矩阵。矩阵的大小要求取决于 **Interpolation algorithm** 参数的值。

- 如果 **Interpolation algorithm** 的值为 `Bilinear`，则矩阵必须具有三行或更多行以及三列或更多列。
- 如果 **Interpolation algorithm** 的值为 `Gradient-corrected linear`，则矩阵必须具有五行或更多行以及五列或更多列。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **R** — 处理后图像的红色通道 矩阵

处理后图像的红色通道，返回为与 **I** 具有相同大小和数据类型的二维数值矩阵。

#### 依赖

要启用此端口，请将 **Output image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **G** — 处理后图像的绿色通道 矩阵

处理后图像的绿色通道，返回为与 **I** 具有相同大小和数据类型的二维数值矩阵。

#### 依赖

要启用此端口，请将 **Output image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **B** — 处理后图像的蓝色通道 矩阵

处理后图像的蓝色通道，返回为与 **I** 具有相同大小和数据类型的二维数值矩阵。

#### 依赖

要启用此端口，请将 **Output image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Image** — 多维处理后图像 矩阵

多维处理后图像，返回为与 **I** 具有相同数据类型的三维数值矩阵。如果输入图像 **I** 的维度为 *M*×*N*，则 **Image** 的维度为 *M*×*N*×*P*，其中 *P* 是颜色通道数。

#### 依赖

要启用此端口，请将 **Output image signal** 参数指定为 `One multidimensional signal`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### 主

### **Interpolation algorithm** — 插值算法 `Bilinear`（默认）| `Gradient-corrected linear`

指定模块用于计算缺失颜色信息的算法。如果选择 `Bilinear`，模块对缺失颜色值的相邻像素值进行空间平均以计算其颜色信息。

如果选择 `Gradient-corrected linear`，模块使用 Weiner 方法最小化插值中的均方误差。此方法在图像中对象的边缘处表现良好。两种方法在图像边界处均使用对称填充。有关详细信息，请参阅 Image Pad 模块参考页。

### **Sensor alignment** — R、G、B 像素对齐方式 `RGGB`（默认）| `GRBG` | `GBRG` | `BGGR`

指定输入图像的对齐方式。选择与图像左上角 2×2 像素块对应的 R、G 和 B 像素序列。按从左到右、从上到下的顺序指定序列。例如，对于此图像，您应选择 `BGGR`。

Bayer 格式的 4×4 图像示意图，每个像素标记为 R、G 或 B。

### **Output image signal** — 输出图像的维度 `One multidimensional signal`（默认）| `Separate color signals`

指定如何输出 RGB 图像。给定 *M*×*N* 输入图像，此参数以下列方式影响此模块的输出。

- `One multidimensional image` — 模块具有单个端口 Image，输出 *M*×*N*×*P* RGB 图像，其中 *P* 是颜色通道数。
- `Separate color signals` — 模块具有三个端口 R、G 和 B，每个端口输出 RGB 图像的一个 *M*×*N* 颜色通道。

### 数据类型

有关定点模块参数的详细信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

### **Lock data type settings against change by the fixed-point tools** — 防止定点工具覆盖数据类型 `off`（默认）| `on`

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

Demosaic 模块接收 Bayer 格式的图像并输出 RGB 图像。该模块使用梯度校正线性插值算法或双线性插值算法执行此操作。下图展示了 Bayer 格式的 4×4 图像，每个像素标记为 R、G 或 B。

Bayer 格式的 4×4 图像示意图，每个像素标记为 R、G 或 B。
