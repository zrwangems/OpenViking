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

输出图像或视频，以 *M*-by-*N*-by-*T* 数组或 *M*-by-*N*-by-*C*-by-*T* 数组形式返回。如果输出是 3 维数组，则第三维是视频中的帧数。如果输出是 4 维数组，则第三维是颜色通道数，第四维是视频中的帧数。

**注意**

如果从 MATLAB 工作区导入大小为 *M*-by-*N*-by-3 数组的 RGB 图像，该模块会将第三维视为帧数，并将该图像作为具有 3 个相同帧的灰度视频进行处理。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **R** — 输入视频的红色分量 3 维数组

输入视频的红色分量，以 3 维数组形式返回。第三维是输入视频中的帧数。

**注意**

可以使用 **Output port labels** 参数更改端口标签。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **G** — 输入视频的绿色分量 3 维数组

输入视频的绿色分量，以 3 维数组形式返回。第三维是输入视频中的帧数。

**注意**

可以使用 **Output port labels** 参数更改端口标签。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### **B** — 输入视频的蓝色分量 3 维数组

输入视频的蓝色分量，以 3 维数组形式返回。第三维是输入视频中的帧数。

**注意**

可以使用 **Output port labels** 参数更改端口标签。

#### 依赖关系

要启用此端口，请将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

## 参数

### **Signal** — 要读取的视频 `rand(32,32,3,5)`（默认）| *M*-by-*N*-by-*T* 数组 | *M*-by-*N*-by-*C*-by-*T* 数组 | MATLAB 工作区变量

指定要从工作区读取的视频。此参数的值可以是 3 维数值数组、4 维数值数组或 MATLAB 工作区变量。

要从 MATLAB 工作区导入 AVI 文件，请使用以下过程。

1. 使用 `VideoReader` 函数读取文件。

   ```
   mov = VideoReader('filename.avi')
   ```
2. 指定工作区变量，在本例中为 *mov*，作为 **Signal** 参数的值。如果 AVI 文件具有关联的颜色图，则它必须满足以下条件。

   - 颜色图必须为空或具有 256 个值。
   - 数据必须表示灰度图像。
   - 像素值的数据类型必须为 `uint8`。

### **Sample time** — 输出视频的采样周期 `1`（默认）| `-1` | 正标量

此参数将输出视频的采样周期指定为正标量或 `-1`。当设置为 `-1` 时，该模块从 Simulink 模型继承采样时间。

### **Form output after final value by** — 最终视频帧之后模块输出的形式 `Setting to zero`（默认）| `Holding final value` | `Cyclic repetition`

指定在模块生成最终视频帧之后，仿真持续期间的模块输出。

- `Setting to zero` — 生成零值输出。
- `Holding final value` — 重复最终帧。
- `Cyclic repetition` — 从头开始重复视频。

### **Image signal** — 视频信号的输出模式 `One multidimensional signal`（默认）| `Separate color signals`

指定模块返回彩色视频的格式。

- `One multidimensional signal` — 在单个 4 维数组中返回视频的所有颜色通道。第三维是视频中的颜色通道数。
- `Separate color signals` — 将视频的每个颜色通道作为单独的 3 维数组返回。此设置会在模块上启用与视频中颜色通道数相等的多个输出端口。每个端口返回单个颜色通道。

### **Output port labels** — 输出端口名称 `R|G|B`（默认）| 以竖线分隔的文本标签

命名输出端口。使用竖线字符 | 作为分隔符。

**示例：** Red|Green|Blue

#### 依赖关系

要启用此参数，请将 **Image signal** 参数设置为 `Separate color signals`。

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

**在 R2006a 之前推出**

## 描述

从 MATLAB 工作区导入视频

Video From Workspace 模块从 MATLAB® 工作区导入视频。模块的输出取决于工作区中视频的格式。

- 如果视频由 *M*-by-*N*-by-*T* 数组表示，则该模块输出灰度视频。*M* 和 *N* 是每个视频帧中的行数和列数，*T* 是视频中的帧数。
- 如果视频由 *M*-by-*N*-by-*C*-by-*T* 数组表示，则该模块输出彩色视频。*M* 和 *N* 是每个视频帧中的行数和列数，*C* 是颜色通道数，*T* 是视频中的帧数。

**注意**

- 如果从包含此模块的模型生成代码，则编译代码需要较长时间，因为 Simulink® Coder™ 会将所有视频数据放入 `.c` 文件中。要缩短代码生成时间，请将视频数据转换为 From Multimedia File 或 Read Binary File 模块支持的格式。
- Video From Workspace 模块还支持 `fi` 对象。有关 `fi` 对象的详细信息，请参阅 `fi` (Fixed-Point Designer)。
