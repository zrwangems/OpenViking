---
type: simulink-block
title: 'Color Space Conversion'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Color Space Formatting and Conversions'
documentation_page: 'colorspaceconversion'
documentation_source_path: 'ref/colorspaceconversion.html'
language: zh-CN
chinese_source: worker-translation
---

# Color Space Conversion

## 端口

### 输入

### **Port\_1** — 输入图像数组

输入图像，指定为 *M*-by-*N*-by-*C* 数组，其中 *C* 是输入图像中的颜色通道数。

**Data Types:** `single` | `double` | `uint8`

### **R'** — 图像矩阵的红色分量

图像的红色分量，指定为 *M*-by-*N* 矩阵。

**注意**

到 **R'**、**G'** 和 **B'** 端口的输入必须具有相同的维度和数据类型。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为以下选项之一：

- `R'G'B' to Y'CbCr`
- `R'G'B' to intensity`
- `R'G'B' to HSV`
- `sR'G'B' to XYZ`
- `sR'G'B' to L*a*b*`

**Data Types:** `single` | `double` | `uint8`

### **G'** — 图像矩阵的绿色分量

图像的绿色分量，指定为 *M*-by-*N* 矩阵。

**注意**

到 **R'**、**G'** 和 **B'** 端口的输入必须具有相同的维度和数据类型。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为以下选项之一：

- `R'G'B' to Y'CbCr`
- `R'G'B' to intensity`
- `R'G'B' to HSV`
- `sR'G'B' to XYZ`
- `sR'G'B' to L*a*b*`

**Data Types:** `single` | `double` | `uint8`

### **B'** — 图像矩阵的蓝色分量

图像的蓝色分量，指定为 *M*-by-*N* 矩阵。

**注意**

到 **R'**、**G'** 和 **B'** 端口的输入必须具有相同的维度和数据类型。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为以下选项之一：

- `R'G'B' to Y'CbCr`
- `R'G'B' to intensity`
- `R'G'B' to HSV`
- `sR'G'B' to XYZ`
- `sR'G'B' to L*a*b*`

**Data Types:** `single` | `double` | `uint8`

### **Y'** — 图像矩阵的 Luma 分量

图像的 Luma 分量，指定为 *M*-by-*N* 矩阵。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `Y'CbCr to R'G'B'`。

**Data Types:** `single` | `double` | `uint8`

### **Cb** — 图像矩阵的蓝色差色度分量

图像的蓝色差色度分量，指定为 *M*-by-*D* 矩阵，其中 *D* 是图像宽度的一半。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `Y'CbCr to R'G'B'`。

**Data Types:** `single` | `double` | `uint8`

### **Cr** — 图像矩阵的红色差色度分量

图像的红色差色度分量，指定为 *M*-by-*D* 矩阵，其中 *D* 是图像宽度的一半。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `Y'CbCr to R'G'B'`。

**Data Types:** `single` | `double` | `uint8`

### **H** — 图像矩阵的色调分量

图像的色调分量，指定为 *M*-by-*N* 矩阵。

**注意**

到 **H**、**S** 和 **V** 端口的输入必须具有相同的维度和数据类型。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `HSV to R'G'B'`。

**Data Types:** `single` | `double`

### **S** — 图像矩阵的饱和度分量

图像的饱和度分量，指定为 *M*-by-*N* 矩阵。

**注意**

到 **H**、**S** 和 **V** 端口的输入必须具有相同的维度和数据类型。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `HSV to R'G'B'`。

**Data Types:** `single` | `double`

### **V** — 图像矩阵的亮度分量

图像的亮度分量，指定为 *M*-by-*N* 矩阵。

**注意**

到 **H**、**S** 和 **V** 端口的输入必须具有相同的维度和数据类型。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `HSV to R'G'B'`。

**Data Types:** `single` | `double`

### **X** — 图像矩阵的 X 分量

图像的 X 分量，指定为 *M*-by-*N* 矩阵。

**注意**

到 **X**、**Y** 和 **Z** 端口的输入必须具有相同的维度和数据类型。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `XYZ to sR'G'B'`。

**Data Types:** `single` | `double`

### **Y** — 图像矩阵的 Y 分量

图像的 Y 分量，指定为 *M*-by-*N* 矩阵。

**注意**

到 **X**、**Y** 和 **Z** 端口的输入必须具有相同的维度和数据类型。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `XYZ to sR'G'B'`。

**Data Types:** `single` | `double`

### **Z** — 图像矩阵的 Z 分量

图像的 Z 分量，指定为 *M*-by-*N* 矩阵。

**注意**

到 **X**、**Y** 和 **Z** 端口的输入必须具有相同的维度和数据类型。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `XYZ to sR'G'B'`。

**Data Types:** `single` | `double`

### **L\*** — 图像矩阵的明度分量

图像的明度分量，指定为 *M*-by-*N* 矩阵。

**注意**

到 **L\***、**a\*** 和 **b\*** 端口的输入必须具有相同的维度和数据类型。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `L*a*b* to sR'G'B'`。

**Data Types:** `single` | `double`

### **a\*** — 图像 *M*-by-*N* 矩阵的红绿分量

图像的红绿分量，指定为 *M*-by-*N* 矩阵。

**注意**

到 **L\***、**a\*** 和 **b\*** 端口的输入必须具有相同的维度和数据类型。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `L*a*b* to sR'G'B'`。

**Data Types:** `single` | `double`

### **b\*** — 图像 *M*-by-*N* 矩阵的黄蓝分量

图像的黄蓝分量，指定为 *M*-by-*N* 矩阵。

**注意**

到 **L\***、**a\*** 和 **b\*** 端口的输入必须具有相同的维度和数据类型。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `L*a*b* to sR'G'B'`。

**Data Types:** `single` | `double`

### 输出

### **Port\_1** — 输出图像数组

输出图像，返回为 *M*-by-*N*-by-*P* 数组，其中 *P* 是输出图像中的颜色通道数。对于 Y'CbCr 输出，Y 分量的值范围不同于 Cb 和 Cr 分量。

- 如果输入是 `uint8`，则 Y'CbCr 是 `uint8`。`Y'` 的范围为 `[16, 235]`，`Cb` 和 `Cr` 的范围为 `[16, 240]`。
- 如果输入是 `double`，则 `Y'CbCr` 是 `double`。`Y'` 的范围为 `[16/255, 235/255]`，`Cb` 和 `Cr` 的范围为 `[16/255, 240/255]`。

**Data Types:** `single` | `double` | `int8` | `uint8`

### **R'** — 图像矩阵的红色分量

图像的红色分量，返回为 *M*-by-*N* 矩阵。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为以下选项之一：

- `Y'CbCr to R'G'B'`
- `HSV to R'G'B'`
- `XYZ to sR'G'B'`
- `L*a*b* to sR'G'B'`

.

**Data Types:** `single` | `double` | `int8` | `uint8`

### **G'** — 图像矩阵的绿色分量

图像的绿色分量，返回为 *M*-by-*N* 矩阵。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为以下选项之一：

- `Y'CbCr to R'G'B'`
- `HSV to R'G'B'`
- `XYZ to sR'G'B'`
- `L*a*b* to sR'G'B'`

**Data Types:** `single` | `double` | `int8` | `uint8`

### **B'** — 图像矩阵的蓝色分量

图像的蓝色分量，返回为 *M*-by-*N* 矩阵。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为以下选项之一：

- `Y'CbCr to R'G'B'`
- `HSV to R'G'B'`
- `XYZ to sR'G'B'`
- `L*a*b* to sR'G'B'`

.

**Data Types:** `single` | `double` | `int8` | `uint8`

### **Y'** — 图像矩阵的 Luma 分量

图像的 Luma 分量，返回为 *M*-by-*N* 矩阵。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `R'G'B' to Y'CbCr`。

**Data Types:** `single` | `double` | `int8` | `uint8`

### **Cb** — 图像矩阵的蓝色差色度分量

图像的蓝色差色度分量，返回为 *M*-by-*N* 矩阵。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `R'G'B' to Y'CbCr`。

**Data Types:** `single` | `double` | `int8` | `uint8`

### **Cr** — 图像矩阵的红色差色度分量

图像的红色差色度分量，返回为 *M*-by-*N* 矩阵。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `R'G'B' to Y'CbCr`。

**Data Types:** `single` | `double` | `int8` | `uint8`

### **I'** — 强度图像矩阵

强度图像，返回为 *M*-by-*N* 矩阵。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `R'G'B' to intensity`。

**Data Types:** `single` | `double` | `int8` | `uint8`

### **H** — 图像矩阵的色调分量

图像的色调分量，返回为 *M*-by-*N* 矩阵。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `R'G'B' to HSV`。

**Data Types:** `single` | `double`

### **S** — 图像矩阵的饱和度分量

图像的饱和度分量，返回为 *M*-by-*N* 矩阵。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `R'G'B' to HSV`。

**Data Types:** `single` | `double`

### **V** — 图像矩阵的亮度分量

图像的亮度分量，返回为 *M*-by-*N* 矩阵。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `R'G'B' to HSV`。

**Data Types:** `single` | `double`

### **X** — 图像矩阵的 X 分量

图像的 X 分量，返回为 *M*-by-*N* 矩阵。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `sR'G'B' to XYZ`。

**Data Types:** `single` | `double`

### **Y** — 图像矩阵的 Y 分量

图像的 Y 分量，返回为 *M*-by-*N* 矩阵。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `sR'G'B' to XYZ`。

**Data Types:** `single` | `double`

### **Z** — 图像矩阵的 Z 分量

图像的 Z 分量，返回为 *M*-by-*N* 矩阵。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `sR'G'B' to XYZ`。

**Data Types:** `single` | `double`

### **L\*** — 图像矩阵的明度分量

图像的明度分量，返回为 *M*-by-*N* 矩阵。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `sR'G'B' to L*a*b*`。

**Data Types:** `single` | `double`

### **a\*** — 图像矩阵的红绿分量

图像的红绿分量，返回为 *M*-by-*N* 矩阵。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `sR'G'B' to L*a*b*`。

**Data Types:** `single` | `double`

### **b\*** — 图像矩阵的黄蓝分量

图像的黄蓝分量，返回为 *M*-by-*N* 矩阵。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`，并将 **Conversion** 参数设置为 `sR'G'B' to L*a*b*`。

**Data Types:** `single` | `double`

## 参数

### **Conversion** — 颜色空间转换 `R'G'B' to Y'CbCr`（默认） | `Y'CbCr to R'G'B'` | `R'G'B' to intensity` | ...

指定要将图像从哪种颜色空间转换到哪种颜色空间，使用以下选项：

- `R'G'B' to Y'CbCr`
- `Y'CbCr to R'G'B'`
- `R'G'B' to intensity`
- `B'G'R' to intensity`
- `B'G'R' to R'G'B'`
- `R'G'B' to B'G'R'`
- `R'G'B' to HSV`
- `HSV to R'G'B'`
- `sR'G'B' to XYZ`
- `XYZ to sR'G'B'`
- `sR'G'B' to L*a*b*`
- `L*a*b* to sR'G'B'`

**注意**

撇号表示信号经过 gamma 校正。

### **Use conversion specified by** — 颜色转换标准 `Rec. 601 (SDTV)`（默认） | `Rec. 709 (HDTV)`

指定在 R'G'B' 和 Y'CbCr 颜色空间之间转换图像时使用的颜色转换标准，为 `Rec. 601 (SDTV)` 或 `Rec. 709 (HDTV)`。

#### 依赖关系

要启用此参数，请将 **Conversion** 参数设置为 `R'G'B' to Y'CbCr` 或 `Y'CbCr to R'G'B'`。

### **Scanning standard** — 扫描标准 `1125/60/2:1`（默认） | `1250/50/2:1`

指定在 R'G'B' 和 Y'CbCr 颜色空间之间转换图像时使用的扫描标准，为 `1125/60/2:1` 或 `1250/50/2:1`。

#### 依赖关系

要启用此参数，请将 **Conversion** 参数设置为 `R'G'B' to Y'CbCr` 或 `Y'CbCr to R'G'B'`，并将 **Use conversion specified by** 参数设置为 `Rec. 709 (HDTV)`。

### **White point** — 白点 `D50`（默认） | `D55` | `D65`

指定在 sR'G'B' 和 L\*a\*b\* 颜色空间之间转换图像时使用的参考白点，为 `D50`、`D55` 或 `D65`。

#### 依赖关系

要启用此参数，请将 **Conversion** 参数设置为 `sR'G'B' to L*a*b*` 或 `L*a*b* to sR'G'B'`。

### **Image signal** — 图像信号输入 `One multidimensional signal`（默认） | `Separate color signals`

指定是将图像的颜色通道合并为一个信号，还是分别输入和输出它们。

- `One multidimensional signal` — 该模块将输入图像的所有颜色通道作为多维数组接受到一个输入端口，并从单个输出端口将转换后的图像作为单个矩阵或数组输出。
- `Separate color signals` — 该模块将输入图像的每个颜色通道接受到一个单独的输入端口，并从单独的输出端口输出转换后图像的每个颜色通道。

## 所属库

Computer Vision Toolbox / Conversions

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `integer` | `single` | `image` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换
使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

转换图像的颜色空间

Color Space Conversion 模块在颜色空间之间转换颜色信息。使用 **Conversion** 参数指定要在哪些颜色空间之间转换。
