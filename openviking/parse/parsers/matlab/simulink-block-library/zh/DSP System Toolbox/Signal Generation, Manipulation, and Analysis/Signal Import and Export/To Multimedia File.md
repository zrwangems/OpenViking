---
type: simulink-block
title: 'To Multimedia File'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Signal Import and Export'
documentation_page: 'tomultimediafile'
documentation_source_path: 'ref/tomultimediafile.html'
language: zh-CN
chinese_source: worker-translation
---

# To Multimedia File

## 端口

### 输入

### **Image** — 彩色图像或视频帧数组

将颜色图像或视频帧指定为 *M*×*N*×3 矩阵形式的 RGB、Intensity 或 YCbCr 4:2:2 信号。*M* 和 *N* 分别是每幅图像的行数和列数。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定文件同时包含音频和视频数据，请将 **Write** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **File color format** 参数设置为 `RGB`，并将 **Image signal** 参数设置为 `One multidimensional signal`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **R** — 图像或视频帧矩阵的红色分量

将图像或视频帧的红色分量指定为 *M*×*N* 矩阵。*M* 和 *N* 分别是图像的行数和列数。

**R**、**G** 或 **B** 端口的输入必须具有相同的维度。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定文件同时包含音频和视频数据，请将 **Write** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **File color format** 参数设置为 `RGB`，并将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **G** — 图像或视频帧矩阵的绿色分量

将图像或视频帧的绿色分量指定为 *M*×*N* 矩阵。*M* 和 *N* 分别是图像的行数和列数。

**R**、**G** 或 **B** 端口的输入必须具有相同的维度。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定文件同时包含音频和视频数据，请将 **Write** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **File color format** 参数设置为 `RGB`，并将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **B** — 图像或视频帧矩阵的蓝色分量

将图像或视频帧的蓝色分量指定为 *M*×*N* 矩阵。*M* 和 *N* 分别是图像的行数和列数。

**R**、**G** 或 **B** 端口的输入必须具有相同的维度。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定文件同时包含音频和视频数据，请将 **Write** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **File color format** 参数设置为 `RGB`，并将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Y** — 图像或视频帧矩阵的亮度分量

将图像或视频帧的亮度分量指定为 *M*×*N* 矩阵。*M* 和 *N* 分别是图像的行数和列数。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定文件同时包含音频和视频数据，请将 **Write** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **File color format** 参数设置为 `YCbCr 4:2:2`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Cb** — 图像或视频帧矩阵的蓝色差色度分量

将图像或视频帧的蓝色差色度分量指定为 *M*×*N*/2 矩阵。*M* 和 *N* 分别是输入图像的行数和列数。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定文件同时包含音频和视频数据，请将 **Write** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **File color format** 参数设置为 `YCbCr 4:2:2`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Cr** — 图像或视频帧矩阵的红色差色度分量

将图像或视频帧的红色差色度分量指定为 *M*×*N*/2 矩阵。*M* 和 *N* 分别是每个输入图像的行数和列数。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定文件同时包含音频和视频数据，请将 **Write** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **File color format** 参数设置为 `YCbCr 4:2:2`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Audio** — 音频信号向量 | 矩阵

将音频信号指定为包含 *M* 个元素的向量或 *M*×*N* 矩阵。*M* 是每个通道中的样本数，*N* 是通道数。

#### 依赖关系

要启用此端口，请将 **File name** 参数设置为包含音频数据的多媒体文件的名称。如果指定文件同时包含音频和视频数据，请将 **Write** 参数设置为 `Audio only` 或 `Video and audio`。

**数据类型：** `single` | `double` | `int16` | `int32` | `uint8`

## 参数

### **File name** — 文件名 `output.wav`（默认值）| character vector

指定多媒体文件的名称。模块将文件保存在当前文件夹中。要指定其他文件或位置，请点击 **Save As** 按钮。

### **File type** — 多媒体文件的文件类型 `WAV`（默认值）| `AVI` | `MJ2000` | `WMA` | `WMV` | `MPEG4` | `FLAC` | `MP3` | `OGG` | `OPUS`

将多媒体文件的类型指定为以下选项之一：

- `WAV`
- `AVI`
- `MJ2000`
- `WMA`
- `WMV`
- `MPEG4`
- `FLAC`
- `MP3`
- `OGG`
- `OPUS`

### **Write** — 多媒体类型 `Audio only`（默认值）| `Video and audio` | `Video only`

指定模块是向多媒体文件写入视频帧、音频样本，还是二者都写入。可以选择 `Video and audio`、`Video only` 或 `Audio only`。

#### 依赖关系

要启用此参数，请将 **File type** 设置为 `AVI`、`MPEG4` 或 `OGG`。

### **Audio Quality (0-100)** — 音频文件的质量 `75`（默认值）| 范围 [0 100] 内的整数

将可变比特率压缩的质量设置指定为范围 [0,100] 内的标量，其中 0 表示质量较低、压缩程度较高，100 表示质量较高、压缩程度较低。默认值为 `75`。

可变比特率 (VBR) 编解码器会根据信号的感知复杂度和您在 **Audio Quality (0-100)** 参数中指定的值，为每个编码帧选择适当的比特率。

#### 依赖关系

要启用此参数，请将 **File type** 设置为 `OGG`、`OPUS` 或 `MP3`。

### **Audio Bit Rate (kb/s)** — 音频压缩器 `128`（默认值）| `64` | `96` | `160` | `192` | `256` | `320`

以千比特每秒 (kb/s) 为单位，将压缩音频文件的比特率指定为 64、96、128、160、192、256 或 320。默认值为 128。

在 Windows 系统上，您可以将比特率设置为 192、160、128 或 96。

通常，比特率值越大，感知的音频质量越高。

#### 依赖关系

要启用此参数，请将 **File type** 设置为 `MPEG4`，并将 **Write** 设置为 `Audio only`。

### **Audio compressor** — 音频压缩器 `None (uncompressed)`（默认值）| character vector

选择用于压缩音频数据的压缩算法类型。这种压缩可减小多媒体文件的大小。选择 `None (uncompressed)` 可将未压缩的音频数据保存到多媒体文件中。

**注意**

此参数列表中可用的其他项是系统上安装的音频压缩算法。有关特定音频压缩器的信息，请参阅该压缩器的文档。

#### 依赖关系

要启用此参数，请将 **Write** 设置为 `Video and audio` 或 `Audio only`。

### **Audio data type** — 音频数据类型 `16-bit integer`（默认值）| `Determine from input data type` | `8-bit integer` | `24-bit integer` | `32-bit integer` | `32-bit float` | `64-bit float`

选择音频数据类型。只有对于未压缩的 wave 文件，才能使用 **Audio data type** 参数。

#### 依赖关系

要启用此参数，请将 **Audio compressor** 设置为 `None (uncompressed)`。

### **Video compressor** — 视频压缩器 `None (uncompressed)`（默认值）| character vector

选择用于压缩视频数据的压缩算法类型。这种压缩可减小多媒体文件的大小。选择 `None (uncompressed)` 可将未压缩的视频数据保存到多媒体文件中。

**注意**

此参数列表中可用的其他项是系统上安装的视频压缩算法。有关特定视频压缩器的信息，请参阅该压缩器的文档。

#### 依赖关系

要启用此参数，请将 **Write** 设置为 `Video and audio` 或 `Video only`。

### **Compression Factor (>1)** — 大于 1 的压缩因子 `10`（默认值）| 大于 1 的整数

将压缩因子指定为大于 `1` 的整数。此参数的默认值为 `10`。

#### 依赖关系

要启用此参数，请将 **File type** 设置为 `MJ2000`，并将 **Video compressor** 设置为 `Lossy`。

### **File color format** — 文件颜色格式 `RGB`（默认值）| `YCbCr 4:2:2`

选择存储在文件中的数据的颜色格式。可以选择 `RGB` 或 `YCbCr 4:2:2`。

#### 依赖关系

要启用此参数，请将 **Write** 设置为 `Video and audio` 或 `Video only`。

### **Image signal** — 图像信号 `Separate color signals`（默认值）| `One multidimensional signal`

指定模块如何接受彩色视频信号。如果选择 `One multidimensional signal`，模块将在一个端口上接受 *M*×*N*×*P* 彩色视频信号，其中 *P* 是颜色平面的数量。如果选择 `Separate color signals`，模块上会显示其他端口。每个端口接受 RGB 视频流的一个 *M*×*N* 平面。

#### 依赖关系

要启用此参数，请将 **Write** 设置为 `Video and audio` 或 `Video only`。

### **Video Quality (0-100)** — 视频质量 `75`（默认值）| 范围 [0 100] 内的整数

将视频质量指定为范围 [`0 100`] 内的整数。此参数的默认值为 `75`。

#### 依赖关系

要启用此参数，请将 **File type** 设置为 `MPEG4`，并将 **Write** 设置为 `Video only`。

## 所属库

Audio System Toolbox / Sinks  
DSP System Toolbox / Sinks

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `integera` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |
|  |  |
| --- | --- |
| a 支持 16 位和 32 位有符号整数以及 8 位无符号整数。 | |

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 仅限主机计算机。不包括 Simulink Desktop Real-Time 代码生成。
- 此模块生成的可执行文件依赖于 MATLAB 附带的预构建动态库文件（`.dll` 文件）。使用 `packNGo` 函数将此模块生成的代码和所有相关文件打包到一个压缩的 zip 文件中。使用此 zip 文件，您可以在未安装 MATLAB 的其他开发环境中重新定位、解压缩并重新构建项目。有关详细信息，请参阅“如何在 MATLAB 外部运行生成的可执行文件”。

## 版本历史

**在 R2006a 之前推出**

### R2024a：新增 **Audio Quality (0-100)** 和 **Audio Bit Rate (kb/s)** 参数

现在，对于以下压缩音频文件扩展名，您可以在 To Multimedia File 模块中指定音频质量和音频比特率：

- `OGG`、`OPUS`、`MP3` —— 音频质量
- `MPEG4` —— 音频比特率

### R2023b：支持写入 MP3 文件

To Multimedia File 模块支持写入 MP3 文件（`.mp3`）。

### R2022b：支持 OPUS 音频文件格式

To Multimedia File 模块支持 OPUS 文件格式（`.opus`）。

## 描述

将视频帧和音频样本流式传输到多媒体文件

To Multimedia File 模块将视频帧、音频样本或二者写入多媒体文件（`.avi`、`.wav`、`.wma`、`.mp4`、`.ogg`、`.flac`、`.wmv`）。

您可以通过选择压缩算法来压缩视频帧或音频样本。您可以根据需要连接任意数量的输入端口。因此，您可以控制多媒体文件接收的视频和/或音频类型。

**注意**

此模块支持在具有可用文件 I/O 的平台上进行代码生成。您不能将此模块与 Simulink® Desktop Real-Time™ 软件结合使用，因为该产品不支持文件 I/O。

此模块在安装有 Windows Media® Player 软件版本 11 或更高版本的平台上运行效果最佳。在 Linux® 和 Mac 平台上，此模块仅支持未压缩的 RGB24 AVI 文件。

Windows® 7 UAC（User Account Control，用户帐户控制）可能要求具备管理员权限才能编码 `WMV` 和 `WMA` 文件。

此模块生成的代码依赖于预构建的库文件。您可以在 MATLAB® 环境之外运行此代码或重新部署它，但在此过程中务必考虑这些额外的库文件。`packNGo` 函数会创建一个 zip 文件，其中包含运行或重新构建此代码所需的所有内容。有关详细信息，请参阅 `packNGo` (Simulink Coder)。

要运行由包含此模块的模型生成的可执行文件，您可能需要将预编译的共享库文件添加到系统路径中。有关详细信息，请参阅“了解 DSP System Toolbox 中的 C 代码生成”。
