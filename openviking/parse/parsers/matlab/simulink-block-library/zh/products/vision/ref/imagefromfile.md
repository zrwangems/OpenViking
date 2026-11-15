---
type: simulink-block
title: 'Image From File'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Video Loading, Saving, and Display'
documentation_page: 'imagefromfile'
documentation_source_path: 'ref/imagefromfile.html'
language: zh-CN
chinese_source: worker-translation
---

# Image From File

## 端口

### 输出

### **Image** — 输出图像矩阵 | 三维数组

输出图像，以矩阵或三维数组形式返回。如果读取的图像是二值图像或灰度图像，则输出为 *M*×*N* 矩阵。如果读取的图像是彩色图像，则输出为 *M*×*N*×3 数组。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `One multidimensional signal`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **R** — 图像矩阵的红色分量

图像的红色分量，以 *M*×*N* 矩阵形式返回。如果输入是彩色图像，则模块返回此输出。如果 **Image signal** 参数设置为 Separate color signals 且输入图像是灰度图像，则模块仅返回此端口。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **G** — 图像矩阵的绿色分量

图像的绿色分量，以 *M*×*N* 矩阵形式返回。仅当输入是彩色图像时，模块才返回此输出。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **B** — 图像矩阵的蓝色分量

图像的蓝色分量，以 *M*×*N* 矩阵形式返回。仅当输入是彩色图像时，模块才返回此输出。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

## 参数

### **File name** — 输入图像 `peppers.png`（默认）| 文件名

指定包含要读取图像的文件名。如果文件不在 MATLAB® 路径上，请点击 **Browse** 并导航到该文件。有关支持的文件格式列表，请参阅 MATLAB 文档中的 `imread` 函数参考页。

**注意**

**File name** 参数支持 URL 路径。

### **Sample time** — 模块执行的采样时间 `inf`（默认）| `Positive scalar` | `Vector`

指定模块执行的采样时间。向量长度必须为 2，表示 [Period, Offset] 值，其中 offset 应小于 period 且非负。给定默认值 inf，对于灰度和二值图像，模块输出一个矩阵。对于输入的灰度图像或彩色图像，输出分别是三维或四维数组。

添加维度的值等于 floor((*Tsim*/*Ts*)+1)。

*Tsim* 是仿真时间，*Ts* 是模块执行的采样时间。例如，如果输入图像是 256×256 矩阵，仿真时间为 10 sec，采样时间设置为 0.5 sec，则输出为 256×256×21 数组。

### **Image signal** — 模块返回的信号 `One multidimensional signal`（默认）| `Separate color signals`

指定模块如何返回从文件读取的图像。

- `One multidimensional signal` — 模块有一个输出端口，返回整个图像。
- `Separate color signals` — 模块有三个输出端口，每个颜色通道一个，返回图像的各个颜色通道。

### **Output port labels** — 输出端口标签 `R|G|B`（默认）| 端口名称

指定输出端口的标签。每个标签可以是任意值。使用竖线字符 | 作为所有输出端口名称之间的分隔符。

#### 依赖关系

要启用此参数，请将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型**

### **Output data type** — 输出图像的数据类型：inherit from input image（默认）| double | single | int8 | uint8 | int16 | uint16 | int32 | uint32 | boolean | fixed-point | user-defined | inherit via back propagation

指定输出图像的数据类型。如果输入图像的数据类型与 **Output data type** 参数的所选值不同，则模块会缩放像素值、为像素值添加偏移量以使其处于新数据类型的动态范围内，或同时执行这两种操作。双精度和单精度浮点像素值必须位于区间 [0 1] 内。

### **Signed** — 有符号定点数据类型 `on`（默认）| `off`

如果输入图像数据类型是有符号定点，请选择此参数。

#### 依赖关系

要启用此参数，请将 **Output data type** 参数设置为 `Fixed-point`。

### **Word length** — 定点数据类型中的位数 16（默认）| 正标量

指定定点输出数据类型的字长（以位为单位）。该值应小于 32。

#### 依赖关系

要启用此参数，请将 **Output data type** 参数设置为 `Fixed-point`。

### **Set fraction length in output to** — 定点数据类型的缩放因子 `User-defined`（默认）| `Best precision`

将定点输出的缩放因子指定为以下选项之一。

- `Best precision` — 输出会自动缩放，使输出信号具有可能的最佳精度。
- 选择 `User-defined` — 在 **Fraction length** 参数中指定输出缩放。

#### 依赖关系

要启用此参数，请将 **Output data type** 参数设置为 `Fixed-point`。

### **Fractional length** — 小数位数 `15`（默认）| 标量

指定小数点右侧的位数。

#### 依赖关系

要启用此端口，请将 **Output data type** 参数设置为 `Fixed-point`，并将 **Set fraction length in output** 参数设置为 `User-defined`。

### **User-defined data type** — 用户定义定点数据类型 `uint(8)`（默认）| `User-defined fixed-point data type`

指定任何内置或定点数据类型。可以使用 `fixdt` (Simulink) 函数指定定点数据类型。

#### 依赖关系

要启用此参数，请将 **Output data type** 参数设置为 `User-defined`。

## 所属库

Computer Vision Toolbox / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**R2006a 之前引入**

## 描述

从文件位置读取图像

Image From File 模块从指定的文件位置读取图像，并将其导入 Simulink® 工作区。输入文件可以包含二值图像、灰度图像或彩色图像。
