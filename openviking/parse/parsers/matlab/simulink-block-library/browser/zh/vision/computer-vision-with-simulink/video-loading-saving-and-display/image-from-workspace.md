---
type: simulink-block
title: 'Image From Workspace'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Computer Vision with Simulink / Video Loading, Saving, and Display'
documentation_page: 'imagefromworkspace'
documentation_source_path: 'ref/imagefromworkspace.html'
language: zh-CN
chinese_source: worker-translation
---

# Image From Workspace

## 端口

### 输出

### **Image** — 输出图像矩阵 | 三维数组

输出图像，以矩阵或三维数组形式返回。如果导入的图像是二值或灰度图像，则输出是大小为 *M*-by-*N* 的矩阵。如果导入的图像是彩色图像，则输出是大小为 *M*-by-*N*-by-3 的三维数组。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `One multidimensional signal`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **R** — 图像矩阵的红色分量

图像的红色分量，以 *M*-by-*N* 矩阵形式返回。如果输入是彩色图像，则该模块返回此输出。如果 **Image signal** 参数设置为 `Separate color signals`，且输入图像是二值或灰度图像，则该模块仅返回此端口

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **G** — 图像矩阵的绿色分量

图像的绿色分量，以 *M*-by-*N* 矩阵形式返回。仅当输入是彩色图像时，该模块才返回此输出。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **B** — 图像矩阵的蓝色分量

图像的蓝色分量，以 *M*-by-*N* 矩阵形式返回。仅当输入是彩色图像时，该模块才返回此输出。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

## 参数

**主**

### **Value** — 要导入的图像 `rand(100,100,3)` (默认) | 向量 | 矩阵 | 三维数组 | `MATLAB workspace variable` | `MATLAB function`

将图像指定为向量、矩阵、三维数组、函数或 MATLAB 工作区变量。**Value** 参数可以为：

- 向量 — 赋予 **Value** 参数的值可以是行向量或列向量
- 三维数值数组 — 赋予 **Value** 参数的值可以是三维数组，使用 MATLAB 函数生成
- MATLAB 工作区变量 — 赋予 **Value** 参数的值可以是变量名称，即 MATLAB 工作区变量
- MATLAB 函数 — 赋予 **Value** 参数的值可以是具有指定输入参数的 MATLAB 函数，用于生成数值数组

### **Sample time** — 模块执行的采样时间 `inf` (默认) | `positive scalar` | `Vector`

此参数指定模块执行的采样时间。向量长度必须为 2，表示 [Period, Offset] 值，其中 offset 应小于 period 且非负。给定默认值 inf，该模块为灰度和二值图像输出矩阵。如果输入图像分别为灰度或彩色图像，则输出分别为三维或四维。

添加维度的值等于 *floor*((*Tsim*/*Ts*)+1)

*Tsim* 是仿真时间，*Ts* 是模块执行的采样时间。例如，如果输入图像是 256-by-256 矩阵，仿真时间为 10 sec，采样时间设置为 0.5 sec，则输出为 256-by-256-by-21 数组。

### **Image signal** — 模块返回的信号 `One multidimensional signal` (默认) | `Separate color signals`

指定模块如何返回从 MATLAB 工作区读取的图像。

- `One multidimensional signal`— 该模块有一个输出端口 **Image**，返回整个图像。
- `Separate color signals` — 该模块为每个颜色通道有一个输出端口。每个端口返回图像的一个颜色通道。

### **Output port labels** — 输出端口标签 `R|G|B` (默认) | 端口名称

指定输出端口的标签。每个标签可以是任意值。使用竖线字符 | 作为分隔符来命名所有输出端口。

#### 依赖关系

要启用此参数，请将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型**

### **Output data type** — 输出图像的数据类型 `Inherit from Value` (默认) | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean` | `Fixed-point` | `User-defined` | `Inherit via back propagation` | ...

指定输出图像的数据类型。如果 **Value** 参数中指定的导入图像的数据类型与 **Output data type** 参数的值不同，则该模块会缩放像素值、向像素值添加偏移量以使其处于新数据类型的动态范围内，或同时执行这两项操作。双精度和单精度浮点像素值必须在 [0, 1] 范围内。

### **Signed** — 有符号定点数据类型 `on` (默认) | `off`

如果输入图像数据类型为有符号定点，请选择此参数。

#### 依赖关系

要启用此参数，请将 **Output data type** 参数设置为 `Fixed-point`。

### **Word length** — 定点数据类型中的位数 `16` (默认) | 正标量

指定定点输出数据类型的字长（以位为单位）。该值应小于 32。

#### 依赖关系

要启用此参数，请将 **Output data type** 参数设置为 `Fixed-point`。

### **Set fraction length in output to** — 定点的缩放因子 `User-defined` (默认) | `Best precision`

通过以下两种方法之一指定定点输出的缩放因子：

- `Best precision`— 输出自动缩放，以使输出信号具有最佳可能精度。
- `User-defined` — 在 **Fraction length** 参数中指定输出缩放。

#### 依赖关系

要启用此参数，请将 **Output data type** 参数设置为 `Fixed-point`。

### **Fractional length** — 小数位数 `15` (默认) | `scalar`

指定小数点右侧的位数。

#### 依赖关系

要启用此参数，请将 **Output data type** 参数设置为 `Fixed-point`，并将 **Set fraction length in output** 参数设置为 `User-defined`。

### **User-defined data type** — 用户定义定点数据类型 `sfix(16)` (默认) | `user-defined fixed-point data type`

指定任何内置或定点数据类型。您可以使用 `fixdt` (Simulink) 函数指定定点数据类型。

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

### R2022b：`Image From Workspace` 模块默认值更改

此版本将 Image From Workspace 模块的默认值更改为 `rand(100,100,3)`。以前，默认值为 `checker_board`。

## 描述

从 MATLAB 工作区导入图像

Image From Workspace 模块将图像从存储在 MATLAB® 工作区的矩阵、三维数组、MATLAB 函数或变量导入到 Simulink® 工作区。
