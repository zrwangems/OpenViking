---
type: simulink-block
title: 'Resize'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Feature Detection and Recognition'
documentation_page: 'resize'
documentation_source_path: 'ref/resize.html'
language: zh-CN
chinese_source: worker-translation
---

# Resize

## 端口

### 输入

### **Image** — 输入图像或视频矩阵 | 数组

输入图像或视频，指定为 *M*×*N* 矩阵、*M*×*N*×*T* 数组、*M*×*N*×*C* 数组或 *M*×*N*×*C*×*T* 数组。*T* 是视频或图像序列中的帧数，*C* 是颜色通道数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **ROI** — 感兴趣区域向量

感兴趣区域，指定为 `[x y width height]`，其中 `[x y]` 是该区域左上角的坐标。`width` 和 `height` 分别指定该区域的宽度和高度。

如果为 `ROI` 端口指定输入值，则 `Resize` 模块仅对输入图像中的指定区域应用变换。

#### 依赖关系

要启用此端口，请选择 **Enable ROI processing** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### 输出

### **Out** — 调整大小后的输出图像或视频矩阵 | 数组

调整大小后的输出图像或视频，返回为 *M*×*N* 矩阵、*M*×*N*×*T* 数组、*M*×*N*×*C* 数组或 *M*×*N*×*C*×*T* 数组。*T* 是视频或图像序列中的帧数，*C* 是颜色通道数。

调整大小后的输出图像的数据类型与输入图像相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Flag** — ROI 在图像区域外 `0` | `1`

ROI 在图像区域外，返回为 `0` 或 `1`。

下表描述 **Flag** 端口的输出。

| Flag 端口输出 | 描述 |
| --- | --- |
| `0` | ROI 完全位于输入图像内部。 |
| `1` | ROI 完全或部分位于输入图像外部。 |

#### 依赖关系

要启用此端口，请选择以下参数：

- **Enable ROI processing**
- **Output flag indicating if ROI is within image
  bounds**

**数据类型：** `Boolean`

## 参数

### **Specify** — 要调整大小的图像的方面 `Output size as a percentage of input size` (默认) | `Number of output columns and preserve aspect ratio` | `Number of output rows and preserve aspect ratio` | `Number of output rows and columns`

将输入图像中要考虑的变换方面指定为以下选项之一：

- `Output size as a percentage of input size` —
  变换输入图像尺寸，使输出图像尺寸为输入图像大小的指定百分比。使用 **Resize factor in
  percentage** 参数为整个图像指定百分比因子，或为输入图像的行和列分别指定独立的百分比因子。
- `Number of output columns and preserve aspect ratio`
  — 将输入图像的列维度变换为指定的输出列数。该模块计算输出行数，使输出图像与输入图像具有相同的宽高比。使用 **Number of output
  columns** 参数指定输出列数。
- `Number of output rows and preserve aspect ratio` —
  将输入图像的行维度变换为指定的输出行数。该模块计算输出列数，使输出图像与输入图像具有相同的宽高比。使用 **Number of output
  rows** 参数指定输出行数。
- `Number of output rows and columns` — 将输出图像大小变换为指定的行数和列数。使用 **Number of output rows and columns** 参数指定输出行数和列数。

  **注意**

  指定输出行数和列数可能会改变输出图像的宽高比。

### **Resize factor in percentage** — 用于输入图像变换的百分比因子 `[200 150]` (默认) | 标量 | 双元素向量

将应用于输入图像的百分比 resize factor 指定为以下选项之一：

- 标量 — 对输入图像的行和列应用相同的 resize factor。
- 双元素向量值 — 向量的第一个元素指定应用于图像行的百分比 resize factor，第二个元素指定应用于列的百分比 resize factor。

对于标量 **Resize factor in percentage** 值 *resize factor*，该模块使用以下方程计算输出图像的维度 `[Mout Nout]`：

变换后的输出图像尺寸

要调整输入图像的大小，请指定大于零的 resize factor 值。下表描述各种 resize factor 值对输入图像的影响。

| Resize factor 百分比 | 对图像的影响 |
| --- | --- |
| `0` < *resize factor* < `100` | `Resize` 模块缩小图像。 |
| *resize factor* = `100` | 图像大小不变。 |
| *resize factor* > `100` | `Resize` 模块放大图像。 |

resize factor 对变换输入图像影响的图示

#### 依赖关系

要启用此参数，请将 **Specify** 参数值设置为 `Output size as a percentage of input size`。

### **Number of output columns** — 输出图像中的列数 `25` (默认) | 标量

指定输出图像中的列数。

#### 依赖关系

要启用此参数，请将 **Specify** 参数值设置为 `Number of output columns and preserve aspect ratio`。

### **Number of output rows** — 输出图像中的行数 `25` (默认) | 标量

指定输出图像中的行数。

#### 依赖关系

要启用此参数，请将 **Specify** 参数值设置为 `Number of output rows and preserve aspect ratio`。

### **Number of output rows and columns** — 输出图像中的行数和列数 `[25 35]` (默认) | 双元素向量

将输出图像中的行数和列数指定为双元素向量。第一个元素指定输出图像中的行数，第二个元素指定列数。

#### 依赖关系

要启用此参数，请将 **Specify** 参数值设置为 `Number of output rows and columns`。

### **Interpolation method** — 插值方法 `Bilinear` (默认) | `Nearest neighbor` | `Bicubic` | `Lanczos2` | `Lanczos3`

将调整大小后的图像的像素值插值方法指定为以下选项之一：

- `Nearest neighbor` — `Resize` 模块使用 1 个最近像素的值作为新像素值。
- `Bilinear` — 新像素值是 4 个最近像素值的加权平均值。
- `Bicubic` — 新像素值是 16 个最近像素值的加权平均值。
- `Lanczos2` — 新像素值是 16 个最近像素值的加权平均值，使用 Lanczos-2 核计算。
- `Lanczos3` — 新像素值是 36 个最近像素值的加权平均值，使用 Lanczos-3 核计算。

模块为插值考虑的像素数会影响计算的复杂度和精度。`Nearest neighbor` 插值使用的像素最少，计算效率最高且精度最低，而使用 `Lanczos3` 核的插值计算效率最低且精度最高。有关插值方法和核的详细信息，请参阅更多信息部分和 Create and Compare Resizing Interpolation Kernels 示例。

### **Perform antialiasing when resize factor is between 0 and 100** — 缩小图像时防止混叠 `off` (默认) | `on`

选择此参数可在缩小输入图像之前对其进行低通滤波。当 **Resize factor in percentage** 参数的值介于 `0` 和 `100` 之间时，选择此参数可以防止输出图像中出现混叠。

### **Enable ROI processing** — 启用 ROI 输入 `off` (默认) | `on`

选择此参数可启用 **ROI** 输入端口，用于指定要在输入图像中调整大小的感兴趣区域。

#### 依赖关系

要启用此参数：

- 将 **Specify** 参数设置为 `Number of output rows and columns`。
- 将 **Interpolation method** 设置为以下选项之一：

  - `Nearest neighbor`
  - `Bilinear`
  - `Bicubic`
- 清除 **Perform antialiasing when resize factor is between 0 and 100** 参数。

### **Output flag indicating if ROI is within image bounds** — 启用用于指示指定 ROI 是否在输入图像区域外的标志 `off` (默认) | `on`

选择此参数可启用 **Flag** 端口，该端口指示指定的 ROI 值是否完全或部分超出输入图像维度的范围。

#### 依赖关系

要启用此参数，请选择 **Enable ROI processing** 参数。

## 所属库

Computer Vision Toolbox / Geometric Transformations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

放大或缩小整个图像或图像中的感兴趣区域

`Resize` 模块放大或缩小输入图像或图像中的感兴趣区域 (ROI)。该模块先沿行维度调整大小，再沿列维度调整大小，或反之。
