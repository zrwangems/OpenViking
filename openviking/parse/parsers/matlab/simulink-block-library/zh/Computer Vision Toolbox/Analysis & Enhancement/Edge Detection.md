---
type: simulink-block
title: 'Edge Detection'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Analysis & Enhancement'
documentation_page: 'edgedetection'
documentation_source_path: 'ref/edgedetection.html'
language: zh-CN
chinese_source: worker-translation
---

# Edge Detection

## 端口

### 输入

### **I** — 输入图像矩阵

输入图像，指定为强度值矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

**注意**

Canny 方法不支持 8-bit、16-bit 或 32-bit 有符号定点整数，也不支持 8-bit、16-bit 或 32-bit 无符号整数。

### **Th** — 阈值标量 | 向量

指定阈值作为标量或双元素向量，以从梯度中检测边缘。此值的数据类型必须与输入图像数据类型匹配。对于 Canny 边缘检测方法，阈值必须是范围 [0 1] 内的双元素向量。对于其他方法，阈值为标量。

#### 依赖项

要启用此端口：

- 将 **Method** 参数设置为 `Canny`。或者，将 **Method** 参数设置为 `Sobel`、`Prewitt` 或 `Roberts`，并且还将 **Output type** 参数设置为 `Binary image` 或 `Binary image and gradient components`。
- 选择 **User-defined threshold**。
- 将 **Threshold source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

**注意**

Canny 方法不支持 8-bit、16-bit 或 32-bit 有符号定点整数，也不支持 8-bit、16-bit 或 32-bit 无符号整数。
### 输出

### **Edge** — 边缘检测矩阵

边缘检测，返回为二值图像。值为 `1` 的像素表示边缘像素。

#### 依赖项

当将 **Method** 参数设置为 `Canny` 时，此端口始终启用。要为 `Sobel`、`Prewitt` 或 `Roberts` 方法启用此端口，请将 **Output type** 参数设置为 `Binary image` 或 `Binary image and gradient components`。

**数据类型：** `Boolean`

### **Gv** — 对垂直边缘的梯度响应矩阵

对垂直边缘的梯度响应矩阵。

#### 依赖项

要启用此端口，请设置以下参数：

- **Method** — `Sobel` 或 `Prewitt`
- **Output type** — `Gradient components` 或 `Binary image and gradient components`

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Gh** — 对水平边缘的梯度响应矩阵

对水平边缘的梯度响应矩阵。

#### 依赖项

要启用此端口，请设置以下参数：

- **Method** — `Sobel` 或 `Prewitt`
- **Output type** — `Gradient components` 或 `Binary image and gradient components`

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **G45** — 对 45 degrees 边缘的梯度响应矩阵

对 45 degrees 边缘的梯度响应矩阵。

#### 依赖项

要启用此端口，请设置以下参数：

- **Method** — `Roberts`
- **Output type** — `Gradient components` 或 `Binary image and gradient components`

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **G135** — 对 135 degrees 边缘的梯度响应矩阵

对 135 degrees 边缘的梯度响应矩阵。

#### 依赖项

要启用此端口，请设置以下参数：

- **Method** — `Roberts`
- **Output type** — `Gradient components` 或 `Binary image and gradient components`

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

**主要**

### **Method** — 边缘检测方法 `Sobel`（默认） | `Prewitt` | `Roberts` | `Canny`

指定在输入图像中检测边缘的方法。您可以选择 `Sobel`、`Prewitt`、`Roberts` 或 `Canny`。

### **Output Type** — 输出图像类型 `Binary image`（默认） | `Gradient components` | `Binary image and gradient components`

从以下选项之一指定输出图像类型：

- `Binary image` — 模块在 **Edge** 端口输出布尔矩阵。标记为 `1` 的矩阵元素表示边缘像素。
- `Gradient components` — 模块输出梯度分量。对于 `Sobel` 和 `Prewitt` 方法，梯度分量分别对应于 **Gh** 和 **Gv** 端口处的水平和垂直边缘响应。对于 `Roberts` 方法，梯度分量分别对应于 **G45** 和 **G135** 端口处的 45 degree 和 135 degree 边缘响应。
- `Binary image and gradient components` — 模块输出二值图像和图像的梯度分量两者。

#### 依赖项

要启用此参数，请将 **Method** 参数设置为 `Sobel`、`Prewitt` 或 `Roberts`。

### **User-defined threshold** — 用户定义阈值 off（默认） | on

通过对话框或 **Th** 端口指定所需的阈值。

#### 依赖项

当将 **Method** 参数设置为 `Canny` 时，此参数始终启用。要为 `Sobel`、`Prewitt` 或 `Roberts` 方法启用此参数，请将 **Output type** 参数设置为 `Binary image` 或 `Binary image and gradient components`。

### **Threshold source** — 阈值来源 `Input port`（默认） | `Specify via dialog`

从以下选项之一选择用于输入阈值的来源：

- `Input port` — 使用 **Th** 端口指定阈值。此值的数据类型必须与输入图像数据类型匹配。
- `Specify via dialog` — 在对话框中输入所需的阈值。

#### 依赖项

要启用此参数：

- 将 **Method** 参数设置为 `Canny`。或者将 **Method** 参数设置为 `Sobel`、`Prewitt` 或 `Roberts`，并且还将 **Output type** 参数设置为 `Binary image` 或 `Binary image and gradient components`。
- 选择 **User-defined threshold**。

### **Threshold** — 阈值 20（默认） | 标量

指定在输入数据范围内的阈值。此阈值适用于 Sobel、Prewitt 和 Roberts 边缘检测方法。

#### 依赖项

要启用此参数，请设置以下模块参数：

- **Method** — `Sobel`、`Prewitt` 或 `Roberts`
- **Output type** — `Binary image` 或 `Binary image and gradient components`
- **User-defined threshold** — `On`。
- **Threshold source** — `Specify via dialog`

### **Threshold, [Low High]** — Canny 边缘检测的阈值 [0.25 0.60]（默认） | 向量

将 Canny 边缘检测的阈值指定为范围 [0 1] 内的双元素向量。该向量的元素分别指定弱边缘和强边缘的低阈值和高阈值。

#### 依赖项

要启用此参数，请设置以下模块参数：

- **Method** — `Canny`
- **User-defined threshold** — `On`。
- **Threshold source** — `Specify via dialog`

### **Threshold scale factor:(used to automatically calculate threshold value)** — 阈值缩放因子 `4`（默认） | 标量

指定用于自动计算阈值值的阈值缩放因子。模块使用梯度幅值平方图像的均值计算自动阈值，并将此参数的值与自动阈值相乘，以确定新的阈值。

#### 依赖项

要启用此参数，请设置以下模块参数：

- **Method** — `Sobel`、`Prewitt` 或 `Roberts`
- **Output type** — `Binary image` 或 `Binary image and gradient components`
- **User-defined threshold** — `Off`

### **Edge Thinning** — 边缘细化 `off`（默认） | `on`

选择此参数以减少输出图像中边缘的厚度。此选项需要额外的处理时间和内存资源。

**提示**

当清除 **Edge thinning** 复选框并使用 **Threshold** 参数指定阈值时，此模块在内存使用和处理时间方面最高效。

#### 依赖项

要启用此参数，请设置以下模块参数：

- **Method** — `Sobel`、`Prewitt` 或 `Roberts`
- **Output type** — `Binary image` 或 `Binary image and gradient components`

### **Approximate percentage of weak edge and nonedge pixels (used to automatically calculate threshold values)** — 弱边缘和非边缘像素的近似百分比 70（默认） | 标量

指定弱边缘和非边缘图像像素的近似百分比。模块使用此值计算自动阈值。

#### 依赖项

要启用此参数，请设置以下模块参数：

- **Method** — `Canny`
- **User-defined threshold** — `Off`

### **Standard deviation of Gaussian filter** — 高斯滤波器的标准差 1（默认） | 标量

指定用于 Canny 边缘检测算法的高斯滤波器的标准差。

#### 依赖项

要启用此参数，请将 **Method** 参数设置为 `Canny`。

**数据类型**

有关定点模块参数的信息，请参阅 Specify Fixed-Point Attributes for Blocks (DSP System Toolbox)。

## 所属库

Computer Vision Toolbox / Analysis & Enhancement

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

当您选中 **Normalized output** 复选框时，模块输入不能为定点。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用 Sobel、Prewitt、Roberts 或 Canny 方法查找图像中对象的边缘。

Edge Detection 模块查找输入图像中对象的边缘。该模块支持四种方法：Sobel、Prewitt、Roberts 和 Canny。前三种方法通过近似图像的梯度幅值来查找边缘。模块将输入矩阵分别与 Sobel、Prewitt 或 Roberts 核进行卷积，并输出所得图像的梯度分量。此外，模块通过对梯度幅值进行阈值处理，输出边缘检测的二值图像。

Canny 方法使用高斯滤波器的导数计算输入图像的梯度。然后通过查找梯度的局部极大值来查找边缘。此方法使用两个阈值检测强边缘和弱边缘。仅当弱边缘连接到强边缘时，弱边缘才属于输出的一部分。对于此方法，模块输出边缘检测的二值图像。
