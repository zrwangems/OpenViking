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

将彩色图像或视频帧指定为 *M*×*N*×3 矩阵 RGB、Intensity 或 YCbCr 4:2:2 信号。*M* 和 *N* 分别是每幅图像中的行数和列数。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Write** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **File color format** 参数设置为 `RGB`，并将 **Image signal** 参数设置为 `One multidimensional signal`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **R** — 图像或视频帧矩阵的红色分量

将图像或视频帧的红色分量指定为 *M*×*N* 矩阵。*M* 和 *N* 分别是图像中的行数和列数。

**R**、**G** 或 **B** 端口的输入必须具有相同的维度。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Write** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **File color format** 参数设置为 `RGB`，并将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **G** — 图像或视频帧矩阵的绿色分量

将图像或视频帧的绿色分量指定为 *M*×*N* 矩阵。*M* 和 *N* 分别是图像中的行数和列数。

**R**、**G** 或 **B** 端口的输入必须具有相同的维度。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Write** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **File color format** 参数设置为 `RGB`，并将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **B** — 图像或视频帧矩阵的蓝色分量

将图像或视频帧的蓝色分量指定为 *M*×*N* 矩阵。*M* 和 *N* 分别是图像中的行数和列数。

**R**、**G** 或 **B** 端口的输入必须具有相同的维度。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Write** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **File color format** 参数设置为 `RGB`，并将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Y** — 图像或视频帧矩阵的亮度分量

将图像或视频帧的亮度分量指定为 *M*×*N* 矩阵。*M* 和 *N* 分别是图像中的行数和列数。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Write** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **File color format** 参数设置为 `YCbCr 4:2:2`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Cb** — 图像或视频帧矩阵的蓝色差色度分量

将图像或视频帧的蓝色差色度分量指定为 *M*×*N*/2 矩阵。*M* 和 *N* 是输入图像中的行数和列数。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Write** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **File color format** 参数设置为 `YCbCr 4:2:2`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Cr** — 图像或视频帧矩阵的红色差色度分量

将图像或视频帧的红色差色度分量指定为 *M*×*N*/2 矩阵。*M* 和 *N* 是每幅输入图像中的行数和列数。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Write** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **File color format** 参数设置为 `YCbCr 4:2:2`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Audio** — 音频信号向量 | 矩阵

将音频信号指定为 *M* 元素向量或 *M*×*N* 矩阵。*M* 是每个通道中的采样数，*N* 是通道数。

#### 依赖关系

要启用此端口，请将 **File name** 参数设置为包含音频数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Write** 参数设置为 `Audio only` 或 `Video and audio`。

**数据类型：** `single` | `double` | `int16` | `int32` | `uint8`

## 参数

### **File name** — 文件名 `output.wav`（默认） | 字符向量

指定多媒体文件的名称。模块将文件保存到当前文件夹中。要指定不同的文件或位置，请点击 **Save As** 按钮。

### **File type** — 多媒体文件的文件类型 `WAV`（默认） | `AVI``MJ2000` | `WMA` | `WMV` | `MPEG4` | `FLAC` | `MP3` | `OGG` | `OPUS`

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

### **Write** — 多媒体类型 `Audio only`（默认） | `Video and audio` | `Video only`

指定模块是将视频帧、音频采样还是两者都写入多媒体文件。您可以选择 `Video and audio`、`Video only` 或 `Audio only`。

#### 依赖关系

要启用此参数，请将 **File type** 设置为 `AVI`、`MPEG4` 或 `OGG`。

### **Audio Quality (0-100)** — 音频文件的质量 `75`（默认） | [0 100] 范围内的整数

将可变比特率压缩的质量设置指定为 [0,100] 范围内的标量，其中 0 表示较低质量和较高压缩，100 表示较高质量和较低压缩。默认值为 `75`。

可变比特率 (VBR) 编解码器根据信号的感知复杂度和您在 **Audio Quality (0-100)** 参数中指定的值，为每个编码帧选择合适的比特率。

#### 依赖关系

要启用此参数，请将 **File type** 设置为 `OGG`、`OPUS` 或 `MP3`。

### **Audio Bit Rate (kb/s)** — 音频压缩器 `128`（默认） | `64` | `96` | `160` | `192` | `256` | `320`

将压缩音频文件的比特率以千比特每秒 (kb/s) 指定为 64、96、128、160、192、256 或 320。默认值为 128。

在 Windows 系统上，可以将比特率设置为 192、160、128 或 96。

通常，比特率值越大，感知音频质量越高。

#### 依赖关系

要启用此参数，请将 **File type** 设置为 `MPEG4`，并将 **Write** 设置为 `Audio only`。

### **Audio compressor** — 音频压缩器 `None (uncompressed)`（默认） | 字符向量

选择用于压缩音频数据的压缩算法类型。此压缩可减小多媒体文件的大小。选择 `None (uncompressed)` 可将未压缩的音频数据保存到多媒体文件。

**注意**

此参数列表中提供的其他项是您系统上安装的音频压缩算法。有关特定音频压缩器的信息，请参阅该压缩器的文档。

#### 依赖关系

要启用此参数，请将 **Write** 设置为 `Video and audio` 或 `Audio only`。

### **Audio data type** — 音频数据类型 `16-bit integer`（默认） | `Determine from input data type` | `8-bit integer` | `24-bit integer` | `32-bit integer` | `32-bit float` | `64-bit float`

选择音频数据类型。**Audio data type** 参数仅可用于未压缩的 wave 文件。

#### 依赖关系

要启用此参数，请将 **Audio compressor** 设置为 `None (uncompressed)`。

### **Video compressor** — 视频压缩器 `None (uncompressed)`（默认） | 字符向量

选择用于压缩视频数据的压缩算法类型。此压缩可减小多媒体文件的大小。选择 `None (uncompressed)` 可将未压缩的视频数据保存到多媒体文件。

**注意**

此参数列表中提供的其他项是您系统上安装的视频压缩算法。有关特定视频压缩器的信息，请参阅该压缩器的文档。

#### 依赖关系

要启用此参数，请将 **Write** 设置为 `Video and audio` 或 `Video only`。

### **Compression Factor (>1)** — 大于 1 的压缩因子) 10（默认） | 大于 1 的整数

将压缩因子指定为大于 `1` 的整数。此参数的默认值为 `10`。

#### 依赖关系

要启用此参数，请将 **File type** 设置为 `MJ2000`，并将 **Video compressor** 设置为 `Lossy`。

### **File color format** — 文件颜色格式 `RGB`（默认） | `YCbCr 4:2:2`

选择文件中存储的数据的颜色格式。您可以选择 `RGB` 或 `YCbCr 4:2:2`。

#### 依赖关系

要启用此参数，请将 **Write** 设置为 `Video and audio` 或 `Video only`。

### **Image signal** — 图像信号 `Separate color signals`（默认） | `One multidimensional signal`

指定模块如何接受彩色视频信号。如果选择 `One multidimensional signal`，则模块在一个端口接受 *M*×*N*×*P* 彩色视频信号，其中 *P* 是颜色平面数。如果选择 `Separate color signals`，模块上会出现其他端口。每个端口接受 RGB 视频流的一个 *M*×*N* 平面。

#### 依赖关系

要启用此参数，请将 **Write** 设置为 `Video and audio` 或 `Video only`。

### **Video Quality (0-100)** — 视频质量 `75`（默认） | [0 100] 范围内的整数

将视频质量指定为 [`0 100`] 范围内的整数。此参数的默认值为 `75`。

#### 依赖关系

要启用此参数，请将 **File type** 设置为 `MPEG4`，并将 **Write** 设置为 `Video only`。

## 所属库

Audio System Toolbox / Sinks DSP System Toolbox / Sinks

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

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 仅限主机计算机。不包括 Simulink Desktop Real-Time 代码生成。
- 从此模块生成的可执行文件依赖 MATLAB 附带的预构建动态库文件（`.dll` 文件）。使用 `packNGo` 函数将此模块生成的代码及所有相关文件打包到一个压缩 zip 文件中。使用此 zip 文件，您可以在未安装 MATLAB 的另一开发环境中重定位、解包并重建项目。有关详细信息，请参阅如何在 MATLAB 外部运行生成的可执行文件。

## 版本历史

**在 R2006a 之前引入**

### R2024a：新增 **Audio Quality (0-100)** 和 **Audio Bit Rate (kb/s)** 参数

现在，您可以针对以下压缩音频文件扩展名，在 To Multimedia File 模块中指定音频质量和音频比特率：

- `OGG`、`OPUS`、`MP3` –– 音频质量
- `MPEG4` –– 音频比特率

### R2023b：支持写入 MP3 文件

To Multimedia File 模块支持写入 MP3 文件（`.mp3`）。

### R2022b：支持 OPUS 音频文件格式

To Multimedia File 模块支持 OPUS 文件格式（`.opus`）。

## 描述

将视频帧和音频采样流式传输到多媒体文件

To Multimedia File 模块将视频帧、音频采样或两者写入多媒体（`.avi`、`.wav`、`.wma`、`.mp4`、`.ogg`、`.flac`、`.wmv`）文件。

您可以通过选择压缩算法来压缩视频帧或音频采样。您可以连接任意数量的输入端口。因此，您可以控制多媒体文件接收的视频和/或音频的类型。

**注意**

此模块支持为具有可用文件 I/O 的平台生成代码。不能将此模块与 Simulink® Desktop Real-Time™ 软件一起使用，因为该产品不支持文件 I/O。

此模块在具有 Windows Media® Player 软件版本 11 或更高版本的平台上性能最佳。在 Linux® 和 Mac 平台上，此模块仅支持未压缩的 RGB24 AVI 文件。

Windows® 7 UAC（用户账户控制）可能需要管理员权限才能编码 `WMV` 和 `WMA` 文件。

此模块生成的代码依赖预构建库文件。您可以在 MATLAB® 环境之外运行或重新部署此代码，但这样做时请务必考虑这些额外库文件。`packNGo` 函数创建一个 zip 文件，其中包含运行或重建此代码所需的所有部分。有关详细信息，请参阅 `packNGo` (Simulink Coder)。

要运行从包含此模块的模型生成的可执行文件，您可能需要将预编译共享库文件添加到系统路径。有关详细信息，请参阅了解 DSP System Toolbox 中的 C 代码生成。
