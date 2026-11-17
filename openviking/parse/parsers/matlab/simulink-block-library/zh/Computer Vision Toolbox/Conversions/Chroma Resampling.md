---
type: simulink-block
title: 'Chroma Resampling'
family: 'conversions'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Conversions'
documentation_page: 'chromaresampling'
documentation_source_path: 'ref/chromaresampling.html'
language: zh-CN
chinese_source: worker-translation
---

# Chroma Resampling

## 端口

### 输入

### **Cb** — 图像矩阵的蓝色差色度分量

图像的蓝色差色度分量，指定为 *M*×*D* 矩阵。*D* 是图像宽度的一半。

**数据类型：** `single` | `double` | `uint8`

### **Cr** — 图像矩阵的红色差色度分量

图像的红色差色度分量，指定为 *M*×*D* 矩阵。*D* 是图像宽度的一半。

**数据类型：** `single` | `double` | `uint8`

### 输出

### **Cb** — 图像矩阵的蓝色差色度分量

图像的蓝色差色度分量，返回为 *M*×*P* 矩阵。*P* 是重采样图像宽度的一半。如果对输入图像进行下采样，*P* 小于 *D*。如果对输入图像进行上采样，*P* 大于 *D*。

**数据类型：** `single` | `double` | `int8` | `uint8`

### **Cr** — 图像矩阵的红色差色度分量

图像的红色差色度分量，返回为 *M*×*P* 矩阵。*P* 是重采样图像宽度的一半。如果对输入图像进行下采样，*P* 小于 *D*。如果对输入图像进行上采样，*P* 大于 *D*

**数据类型：** `single` | `double` | `int8` | `uint8`

## 参数

### **Resampling** — 色度重采样方法 `4:4:4 to 4:2:2`（默认） | `4:4:4 to 4:2:0 (MPEG1)` | `4:4:4 to 4:2:0 (MPEG2)` | ...

指定用于对图像色度分量进行下采样或上采样的重采样方法。

这些选项指定下采样操作：

- `4:4:4 to 4:2:2`
- `4:4:4 to 4:2:0 (MPEG1)`
- `4:4:4 to 4:2:0 (MPEG2)`
- `4:4:4 to 4:1:1`
- `4:2:2 to 4:2:0 (MPEG1)`
- `4:2:2 to 4:2:0 (MPEG2)`

这些选项指定上采样操作：

- `4:2:2 to 4:4:4`
- `4:2:0 (MPEG1) to 4:2:2`
- `4:2:0 (MPEG1) to 4:4:4`
- `4:2:0 (MPEG2) to 4:2:2`
- `4:2:0 (MPEG2) to 4:4:4`
- `4:1:1 to 4:4:4`

有关详细信息，请参阅色度重采样格式。

### **Antialiasing filter** — 色度下采样抗混叠滤波器 `Default`（默认） | `User-defined` | `None`

指定该模块用于防止混叠的低通滤波器。

- `Default` — 该模块使用内置低通滤波器。
- `User-defined` — 为该模块指定自定义滤波器系数。根据 Resampling 参数的值，此选项会启用 **Horizontal filter coefficients** 参数、**Vertical filter coefficients** 参数或同时启用两者。
- `None` — 该模块不对输入信号进行滤波。

#### 依赖关系

要启用此参数，请将 **Resampling** 参数设置为以下选项之一：

- `4:4:4 to 4:2:2`
- `4:4:4 to 4:2:0 (MPEG1)`
- `4:4:4 to 4:2:0 (MPEG2)`
- `4:4:4 to 4:1:1`
- `4:2:2 to 4:2:0 (MPEG1)`
- `4:2:2 to 4:2:0 (MPEG2)`

。

### **Horizontal filter coefficients** — 水平低通滤波器的系数 [0.2 0.6 0.2]（默认） | 行向量

将水平滤波器系数指定为要应用于输入信号的偶数个元素组成的向量。

#### 依赖关系

要启用此参数，必须：

- 将 **Resampling** 参数设置为以下选项之一：

  - `4:4:4 to 4:2:2`
  - `4:4:4 to 4:2:0 (MPEG1)`
  - `4:4:4 to 4:2:0 (MPEG2)`
  - `4:4:4 to 4:1:1`
- 将 **Antialiasing filter** 参数设置为 `User-defined`。

### **Vertical filter coefficients** — 垂直低通滤波器的系数 [0.5 0.5]（默认） | 行向量

将滤波器系数指定为要应用于输入信号的奇数个元素组成的向量。

#### 依赖关系

要启用此参数，必须：

- 将 **Resampling** 参数设置为以下选项之一：

  - `4:4:4 to 4:2:0 (MPEG1)`
  - `4:4:4 to 4:2:0 (MPEG2)`
  - `4:2:2 to 4:2:0 (MPEG1)`
  - `4:2:2 to 4:2:0 (MPEG2)`
- 将 **Antialiasing filter** 参数设置为 `User-defined`。

### **Interpolation** — 色度上采样插值方法 `linear`（默认） | `pixel replication`

指定该模块在上采样图像时使用线性插值还是像素复制插值来近似缺失的色度值。

- `linear` — 该模块使用线性插值计算缺失值。
- `pixel replication` — 该模块复制相邻像素的色度值，为上采样图像中的额外像素赋值。

#### 依赖关系

要启用此参数，请将 **Resampling** 参数设置为以下选项之一：

- `4:2:2 to 4:4:4`
- `4:2:0 (MPEG1) to 4:2:2`
- `4:2:0 (MPEG1) to 4:4:4`
- `4:2:0 (MPEG2) to 4:2:2`
- `4:2:0 (MPEG2) to 4:4:4`
- `4:1:1 to 4:4:4`

。

### **Input image is transposed (data order is row major)** — 按行读取数据 `off`（默认） | `on`

启用此参数以按行读取数据元素。

## 所属库

Computer Vision Toolbox / Conversions

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

对图像的色度分量进行下采样或上采样

Chroma Resampling 模块对输入图像的色度分量进行重采样。色度重采样包括以下操作：

- 下采样 — 降低信号传输或存储所需的带宽。可以通过对输入信号应用低通滤波器进行限带来防止混叠。
- 上采样 — 扩展信号的带宽。该模块执行插值以近似缺失的色度值。
