---
type: simulink-block
title: 'Video From Workspace'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'videofromworkspace'
documentation_source_path: 'ref/videofromworkspace.html'
language: zh-CN
chinese_source: worker-translation
---

# Video From Workspace

## 端口

### 输出

### **Image** — 输出图像或视频 *M*-by-*N*-by-*T* 数组 | *M*-by-*N*-by-*C*-by-*T* 数组

输出图像或视频，返回为
*M*-by-*N*-by-*T* 数组或
*M*-by-*N*-by-*C*-by-*T*
数组。如果输出是三维数组，则第三个维度是视频中的帧数。如果输出是四维数组，则第三个维度是颜色通道数，第四个维度是视频中的帧数。

**注意**

如果从 MATLAB 工作区导入大小为 *M*-by-*N*-by-3 数组的 RGB 图像，则该模块会将第三个维度视为帧数，并将该图像作为具有 3 个相同帧的灰度视频进行处理。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **R** — 输入视频的红色分量三维数组

输入视频的红色分量，返回为三维数组。第三个维度是输入视频中的帧数。

**注意**

可以使用 **输出端口标签** 参数更改端口标签。

#### 依赖关系

要启用此端口，请将 **图像信号**  参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **G** — 输入视频的绿色分量三维数组

输入视频的绿色分量，返回为三维数组。第三个维度是输入视频中的帧数。

**注意**

可以使用 **输出端口标签** 参数更改端口标签。

#### 依赖关系

要启用此端口，请将 **图像信号**  参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **B** — 输入视频的蓝色分量三维数组

输入视频的蓝色分量，返回为三维数组。第三个维度是输入视频中的帧数。

**注意**

可以使用 **输出端口标签** 参数更改端口标签。

#### 依赖关系

要启用此端口，请将 **图像信号**  参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

## 参数

### **信号** — 要读取的视频 `rand(32,32,3,5)` (默认) | *M*-by-*N*-by-*T* 数组 | *M*-by-*N*-by-*C*-by-*T* 数组 | MATLAB 工作区变量

指定要从工作区读取的视频。此参数的值可以是三维数值数组、四维数值数组或 MATLAB 工作区变量。

要从 MATLAB 工作区导入 AVI 文件，请使用以下过程。

1. 使用 `VideoReader` 函数读取文件。

   ```
   mov = VideoReader('filename.avi')
   ```
2. 指定工作区变量，在此例中为 *mov*，作为 **信号** 参数的值。如果 AVI 文件具有关联的 colormap，则它必须满足以下条件。

   - colormap 必须为空或具有 256 个值。
   - 数据必须表示灰度图像。
   - 像素值的数据类型必须为 `uint8`。

### **采样时间** — 输出视频的采样周期 `1` (默认) | `-1` | 正标量

此参数将输出视频的采样周期指定为正标量或 `-1`。设置为 `-1` 时，该模块从 Simulink 模型继承采样时间。

### **最终值后的输出形成方式** — 最终视频帧之后的模块输出形式 `Setting to zero` (默认) | `Holding final value` | `Cyclic repetition`

指定该模块生成最终视频帧之后，在仿真期间的模块输出。

- `Setting to zero` — 生成零值输出。
- `Holding final value` — 重复最终帧。
- `Cyclic repetition` — 从头开始重复视频。

### **图像信号** — 视频信号的输出模式 `One multidimensional signal` (默认) | `Separate color signals`

指定该模块返回彩色视频的格式。

- `One multidimensional signal` — 在单个四维数组中返回视频的所有颜色通道。第三个维度是视频中的颜色通道数。
- `Separate color signals` — 将视频的每个颜色通道作为单独的三维数组返回。此设置将在该模块上启用与视频中颜色通道数相等的多个输出端口。每个端口返回单个颜色通道。

### **输出端口标签** — 输出端口名称 `R|G|B` (默认) | 由竖线分隔的文本标签

为输出端口命名。使用竖线字符 | 作为分隔符。

**示例：** Red|Green|Blue

#### 依赖关系

要启用此参数，请将 **图像信号**  参数设置为 `Separate color signals`。

## 所属库

Computer Vision Toolbox / Sources

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

从 MATLAB 工作区导入视频

Video From Workspace 模块从 MATLAB® 工作区导入视频。该模块的输出取决于工作区中视频的格式。

- 如果视频由
  *M*-by-*N*-by-*T* 数组表示，则该模块
  输出灰度视频。*M* 和 *N* 是每个视频帧中的
  行数和列数，*T* 是视频中的
  帧数。
- 如果视频由
  *M*-by-*N*-by-*C*-by-*T*
  数组表示，则该模块输出彩色视频。*M* 和 *N*
  是每个视频帧中的行数和列数，*C* 是
  颜色通道数，*T* 是视频中的
  帧数。

**注意**

- 如果从包含此模块的模型生成代码，则编译代码会耗时较长，因为 Simulink®
  Coder™ 会将所有视频数据放入 `.c` 文件中。为
  缩短代码生成时间，请将视频数据转换为
  From Multimedia File 或 Read Binary File 模块支持的格式。
- Video From Workspace 模块还支持 `fi`
  对象。有关 `fi` 对象的详细信息，请参阅 `fi` (Fixed-Point Designer)。
