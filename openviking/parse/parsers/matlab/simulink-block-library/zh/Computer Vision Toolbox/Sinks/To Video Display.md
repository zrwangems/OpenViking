---
type: simulink-block
title: 'To Video Display'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'tovideodisplay'
documentation_source_path: 'ref/tovideodisplay.html'
language: zh-CN
chinese_source: worker-translation
---

# To Video Display

## 端口

### 输入

### **Image** — 输入图像矩阵 | 数组

输入图像或视频，指定为 *M*×*N* 矩阵、*M*×*N*×*T* 数组或 *M*×*N*×*C*×*T* 数组。如果输入为 3-D 数组，则第三维是视频中的帧数。如果输入为 4-D 数组，则第三维是颜色通道数，第四维是视频中的帧数。

#### 依赖项

要启用此端口，请将 **Input Color Format** 参数设置为 `RGB`，并将 **Image signal** 设置为 `One multidimensional signal`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **R** — 图像矩阵的红色分量 | 数组

输入图像或视频的红色分量，指定为 *M*×*N* 矩阵或 *M*×*N*×*T* 数组。如果输入为 3-D 数组，则第三维是视频中的帧数。

**注意**

**R**、**G** 和 **B** 端口的输入必须具有相同的维度和数据类型。

#### 依赖项

要启用此端口，请将 **Input Color Format** 参数设置为 `RGB`，并将 **Image signal** 设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **G** — 图像矩阵的绿色分量 | 数组

输入图像或视频的绿色分量，指定为 *M*×*N* 矩阵或 *M*×*N*×*T* 数组。如果输入为 3-D 数组，则第三维是视频中的帧数。

**注意**

**R**、**G** 和 **B** 端口的输入必须具有相同的维度和数据类型。

#### 依赖项

要启用此端口，请将 **Input Color Format** 参数设置为 `RGB`，并将 **Image signal** 设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **B** — 图像矩阵的蓝色分量 | 数组

输入图像或视频的蓝色分量，指定为 *M*×*N* 矩阵或 *M*×*N*×*T* 数组。如果输入为 3-D 数组，则第三维是视频中的帧数。

**注意**

**R**、**G** 和 **B** 端口的输入必须具有相同的维度和数据类型。

#### 依赖项

要启用此端口，请将 **Input Color Format** 参数设置为 `RGB`，并将 **Image signal** 设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Y** — 图像矩阵的亮度分量 | 数组

输入图像或视频的亮度分量，指定为 *M*×*N* 矩阵或 *M*×*N*×*T* 数组。如果输入为 3-D 数组，则第三维是视频中的帧数。

#### 依赖项

要启用此端口，请将 **Input Color Format** 参数设置为 `YCbCr 4:2:2`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Cb** — 图像矩阵的蓝色差色度分量 | 数组

输入图像或视频的蓝色差色度分量，指定为 *M*×*N*/2 矩阵或 *M*×*N*/2×*T* 数组。如果输入为 3-D 数组，则第三维是视频中的帧数。

#### 依赖项

要启用此端口，请将 **Input Color Format** 参数设置为 `YCbCr 4:2:2`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Cr** — 图像矩阵的红色差色度分量 | 数组

输入图像或视频的红色差色度分量，指定为 *M*×*N*/2 矩阵或 *M*×*N*/2×*T* 数组。如果输入为 3-D 数组，则第三维是视频中的帧数。

#### 依赖项

要启用此端口，请将 **Input Color Format** 参数设置为 `YCbCr 4:2:2`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### 视图

### **Window size** — 显示窗口大小 `Normal`（默认）| `Full-screen (Esc to exit)` | `True size (1:1)`

以各种窗口大小显示视频流：

- `Normal` — 在仿真开始时修改显示大小。
- `Full-screen (Esc to exit)` — 在全屏窗口中显示视频流。要退出全屏视图，请按 **Esc**。
- `True size (1:1)` — 在仿真开始时，以一对一像素比例显示输入图像。

### **Open at Start of Simulation** — 在仿真开始时打开窗口 `on`（默认）| `off`

要设置 **Video Display** 窗口在仿真开始时自动打开并显示视频帧，请选中 **Open at Start of Simulation**。如果清除此参数，则该模块在运行时不被包含，仿真将以 Accelerator Mode (Simulink) 运行。

### 设置

### **Input Color Format** — 输入颜色格式 `RGB`（默认）| `YCbCr 4:2:2`

指定输入图像的颜色格式：

- `RGB` — 将输入色彩空间指定为 RGB。您可以使用 **Image signal** 参数选择将图像作为单个信号输入，还是作为各个颜色信号输入。
- `YCbCr 4:2:2`— 将输入色彩空间指定为 YCbCr。您必须将图像作为单独信号输入到三个输入端口 **Y**、**Cb** 和 **Cr**。

### **Image signal** — 配置输入端口 `One multidimensional signal`（默认）| `Separate color signals`

指定该模块将 RGB 颜色输入接受为单个信号，还是接受为每个颜色通道的单独信号。

- `One multidimensional signal` — 该模块通过一个端口将 RGB 输入接受为单个数组。
- `Separate color signals` — 该模块将 RGB 输入接受为三个单独的矩阵或数组，每个颜色通道一个，分别输入到 **R**、**G** 和 **B** 端口。

#### 依赖项

要启用此参数，请将 **Input Color Format** 参数设置为 `RGB`。

## 所属库

Computer Vision Toolbox / Sinks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `integer` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

**注意**

此模块支持为具有文件 I/O 可用的平台生成代码。您不能将此模块与 Simulink® Desktop Real-Time™ 软件一起使用，因为该产品不支持文件 I/O。

此模块生成的代码依赖于预构建库文件。您可以在 MATLAB® 环境之外运行此代码，或重新部署它，但这样做时请务必考虑这些额外的库文件。`packNGo` 函数会创建一个 ZIP 文件，其中包含运行或重新构建此代码所需的所有组件。有关详细信息，请参阅 `packNGo` (Simulink Coder)。

要了解 Simulink 模块的代码生成过程，请参阅 Simulink Coder。要运行从包含此模块的模型生成的可执行文件，您可能需要将预编译共享库文件添加到系统路径。有关详细信息，请参阅 Simulink 共享库依赖项和加速 Simulink 模型。

使用说明和限制：

- 仅限主机计算机。不包括 Simulink Desktop Real-Time 代码生成。
- 从此模块生成的可执行文件依赖于 MATLAB 附带的预构建动态库文件（`.dll` 文件）。使用 `packNGo` 函数将从此模块生成的代码及所有相关文件打包到一个压缩 ZIP 文件中。使用此 ZIP 文件，您可以在未安装 MATLAB 的另一个开发环境中重新定位、解包并重新构建您的项目。有关更多详细信息，请参阅代码生成、GPU 和第三方支持。

## 版本历史

**R2006a 之前引入**

## 描述

显示图像或视频帧

To Video Display 模块显示 RGB 或 YCbCr 格式的图像和视频帧。该模块创建的显示轻量且高性能，能够以高帧率显示高清视频。
