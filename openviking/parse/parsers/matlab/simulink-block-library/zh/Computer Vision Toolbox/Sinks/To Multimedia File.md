---
type: simulink-block
title: 'To Multimedia File'
family: 'sinks'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'tomultimediafile'
documentation_source_path: 'ref/tomultimediafile.html'
language: zh-CN
chinese_source: worker-translation
---

# To Multimedia File

## 端口

### 输入

### **Image** — 输入图像帧矩阵 | 数组

将输入图像帧指定为矩阵或数组。要将强度图像帧写入多媒体文件，请将其指定为 *M*×*N* 矩阵。对于彩色图像帧，请将其指定为 *M*×*N*×3 数组。

#### 依赖关系

要启用此端口：

- 将 **File type** 参数设置为 `AVI`、`MJ-2000`、`WMV` 或 `MPEG4`。
- 如果 **File type** 参数值不是 `MJ-2000`，则将 **Write** 参数设置为 `Video and audio` 或 `Video only`。
- 如果 **File type** 参数值是 `AVI` 或 `MPEG4`，则将 **File color format** 参数设置为 `RGB`。
- 将 **Image signal** 参数设置为 `One multidimensional signal`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **R** — 图像矩阵的红色分量

将输入图像帧的红色分量指定为 *M*×*N* 矩阵。

#### 依赖关系

要启用此端口：

- 将 **File type** 参数设置为 `AVI`、`MJ-2000`、`WMV` 或 `MPEG4`。
- 如果 **File type** 参数值不是 `MJ-2000`，则将 **Write** 参数设置为 `Video and audio` 或 `Video only`。
- 如果 **File type** 参数值是 `AVI` 或 `MPEG4`，则将 **File color format** 参数设置为 `RGB`。
- 将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **G** — 图像矩阵的绿色分量

将输入图像帧的绿色分量指定为 *M*×*N* 矩阵。

#### 依赖关系

要启用此端口：

- 将 **File type** 参数设置为 `AVI`、`MJ-2000`、`WMV` 或 `MPEG4`。
- 如果 **File type** 参数值不是 `MJ-2000`，则将 **Write** 参数设置为 `Video and audio` 或 `Video only`。
- 如果 **File type** 参数值是 `AVI` 或 `MPEG4`，则将 **File color format** 参数设置为 `RGB`。
- 将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **B** — 图像矩阵的蓝色分量

将输入图像帧的蓝色分量指定为 *M*×*N* 矩阵。

#### 依赖关系

要启用此端口：

- 将 **File type** 参数设置为 `AVI`、`MJ-2000`、`WMV` 或 `MPEG4`。
- 如果 **File type** 参数值不是 `MJ-2000`，则将 **Write** 参数设置为 `Video and audio` 或 `Video only`。
- 如果 **File type** 参数值是 `AVI` 或 `MPEG4`，则将 **File color format** 参数设置为 `RGB`。
- 将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Y** — 图像矩阵的亮度分量

将输入图像帧的亮度分量指定为 *M*×*N* 矩阵。

#### 依赖关系

要启用此端口：

- 将 **File type** 参数设置为 `AVI` 或 `MPEG4`。
- 将 **Write** 参数设置为 `Video and audio` 或 `Video only`。
- 将 **File color format** 参数设置为 `YCbCr 4:2:2`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Cb** — 图像矩阵的蓝色差色度分量

将输入图像的蓝色差色度分量指定为 *M*×*N*/2 矩阵。

#### 依赖关系

要启用此端口：

- 将 **File type** 参数设置为 `AVI` 或 `MPEG4`。
- 将 **Write** 参数设置为 `Video and audio` 或 `Video only`。
- 将 **File color format** 参数设置为 `YCbCr 4:2:2`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Cr** — 图像矩阵的红色差色度分量

将输入图像的红色差色度分量指定为 *M*×*N*/2 矩阵。

#### 依赖关系

要启用此端口：

- 将 **File type** 参数设置为 `AVI` 或 `MPEG4`。
- 将 **Write** 参数设置为 `Video and audio` 或 `Video only`。
- 将 **File color format** 参数设置为 `YCbCr 4:2:2`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Audio** — 输入音频信号向量 | 矩阵

将输入音频信号指定为向量或矩阵。当指定为矩阵时，模块将每一列视为独立通道。

#### 依赖关系

要启用此端口：

- 将 **File type** 参数设置为 `AVI`、`WAV`、`WMA`、`MPEG4`、`FLAC` 或 `OGG`。
- 如果 **File type** 参数值是 `AVI`、`WMV` 或 `MPEG4`，则将 **Write** 参数设置为 `Video and audio` 或 `Audio only`。

**数据类型：** `single` | `double` | `int16` | `int32` | `uint8`

## 参数

### **File name** — 多媒体文件名 `output.avi`（默认）| character vector

指定模块写入的多媒体文件的名称。模块会根据指定的 **File type** 参数自动追加文件扩展名。如果指定的文件名（包括文件扩展名）已存在，模块会用新的输入数据覆盖现有文件中的数据。

默认情况下，模块将文件保存在当前工作目录中。要指定不同的文件位置，请点击 **Save As...** 按钮。

### **File type** — 多媒体文件类型 `AVI`（默认）| `WAV` | `MJ2000` | `WMA` | `WMV` | `MPEG4` | `FLAC` | `OGG`

指定要写入的多媒体文件类型。模块支持 `AVI`、`WAV`、`MJ2000`、`WMA`、`WMV`、`MPEG4`、`FLAC` 和 `OGG` 文件格式。

### **Write** — 媒体类型 `Video only`（默认）| `Audio only` | `Video and audio`

指定要写入的媒体类型。根据 **File type** 参数的值，可以选择 `Video only`、`Audio only` 或 `Video and audio`。

|  |  |
| --- | --- |
| **文件类型** | **支持的媒体类型** |
| `AVI` | - `Video only` - `Audio only` - `Video and audio` |
| `WMV` | - `Video only` - `Video and audio` |
| `MPEG4` | - `Video only` - `Audio only` |

#### 依赖关系

要启用此参数，请将 **File type** 参数设置为 `AVI`、`WMV` 或 `MPEG4`。

### **Video compressor** — 视频压缩算法 `None (uncompressed)`（默认）| `DV Video Encoder` | `MJPEG Compressor` | `Lossy` | `Lossless`

指定用于减小输出文件大小的视频压缩算法。可用选项取决于 **File type** 参数的值。

- `AVI` — 选择 `DV Video Encoder` 或 `MJPEG Compressor` 算法。如果不希望减小文件大小，请选择 `None (uncompressed)`。
- `MJ2000` — 选择 `Lossy` 或 `Lossless` 算法。

**注意**

此参数的选项是系统上安装的视频压缩算法。有关特定视频压缩器的信息，请参阅该压缩器的文档。

#### 依赖关系

要启用此参数，请将 **File type** 参数设置为 `MJ2000` 或 `AVI`。对于 `AVI` 文件类型，请将 **Write** 参数设置为 `Video only` 或 `Video and audio`。

### **Compression Factor (>1)** — 压缩因子 `10`（默认）| 大于 `1` 的整数

将压缩因子指定为大于 `1` 的整数。

#### 依赖关系

要启用此参数，请将 **File type** 参数设置为 `MJ2000`，并将 **Video compressor** 参数设置为 `Lossy`。

### **Video Quality (0-100)** — 视频质量 `75`（默认）| [0, 100] 范围内的整数

将视频质量指定为 [0, 100] 范围内的整数。

#### 依赖关系

要启用此参数，请将 **File type** 参数设置为 `MPEG4`，并将 **Write** 参数设置为 `Video only`。

### **File color format** — 输出视频的颜色格式 `RGB`（默认）| `YCbCr 4:2:2`

指定输出文件的视频颜色格式。模块支持 `RGB` 和 `YCbCr 4:2:2` 颜色格式。

#### 依赖关系

要启用此参数，请将 **File type** 参数设置为 `AVI` 或 `MPEG4`。

### **Image signal** — RGB 视频的输入端口配置 `One multidimensional signal`（默认）| `Separate color signals`

指定模块如何接受 RGB 彩色视频输入。如果选择 `One multidimensional signal`，模块仅使用 **Image** 端口接受输入。如果选择 `Separate color signals`，模块使用三个单独的颜色通道（分别通过 **R**、**G** 和 **B** 端口）接受输入视频。

#### 依赖关系

要启用此参数：

- 将 **File type** 参数设置为 `AVI`、`MJ-2000`、`WMV` 或 `MPEG4`。
- 将 **Write** 参数设置为 `Video and audio` 或 `Video only`。
- 如果 **File type** 参数值是 `AVI` 或 `MPEG4`，则将 **File color format** 参数设置为 `RGB`。

### **Audio compressor** — 音频压缩算法 `None (uncompressed)`（默认）| `CCITT A-Law` | `CCITT u-Law` | `GSM 6.10` | `IMA ADPCM` | `Microsoft ADPCM` | `PCM`

指定用于减小输出文件大小的音频压缩算法。模块支持 `CCITT A-Law`、`CCITT u-Law`、`GSM 6.10`、`IMA ADPCM`、`Microsoft ADPCM` 和 `PCM` 算法。如果不希望减小文件大小，请选择 `None (uncompressed)`。

**注意**

此参数的选项是系统上安装的音频压缩算法。有关特定音频压缩器的信息，请参阅该压缩器的文档。

#### 依赖关系

要启用此参数，请使用以下任一选项：

- 将 **File type** 参数设置为 `AVI`，并将 **Write** 参数设置为 `Video and audio` 或 `Audio only`。
- 将 **File type** 参数设置为 `WAV`。

### **Audio data type** — 音频数据类型 `Determine from input data type`（默认）| `8-bit integer` | `16-bit integer` | `24-bit integer` | `32-bit integer` | `32-bit float` | `64-bit float`

指定输出文件的音频数据类型。

#### 依赖关系

要启用此参数，请使用以下任一选项：

- 将 **File type** 参数设置为 `WAV`，并将 **Audio compressor** 参数设置为 `None (uncompressed)`。
- 将 **File type** 参数设置为 `FLAC`。此文件类型仅支持 `8-bit integer`、`16-bit integer` 和 `24-bit integer` 数据类型。

## 所属库

Computer Vision Toolbox / Sinks

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

- 仅限主机。不包括 Simulink Desktop Real-Time 代码生成。
- 从此模块生成的可执行文件依赖于 MATLAB® 附带的预构建动态库文件（`.dll` 文件）。使用 `packNGo` (Simulink Coder) 函数将从此模块生成的代码及所有相关文件打包到压缩 ZIP 文件中。使用此 ZIP 文件，您可以在未安装 MATLAB 的另一个开发环境中重新定位、解压缩并重建项目。有关更多详细信息，请参阅代码生成、GPU 和第三方支持。

## 版本历史

**在 R2006a 之前引入**

## 描述

将视频帧和音频样本写入多媒体文件

To Multimedia File 模块将视频帧、音频样本或二者写入多媒体文件（`.avi`、`.wav`、`.mj2`、`.mp4` 或 `.m4v` 格式）。

您可以通过选择压缩算法来压缩视频帧或音频样本。除了多媒体文件接收的其他相关属性外，您还可以控制视频或音频的类型。

如果您拥有 Simulink® Coder™ 许可证，则可以从包含此模块的模型生成代码。要运行生成的可执行文件，您可能需要将预编译的共享库文件添加到系统路径中。有关详细信息，请参阅 Simulink Shared Library Dependencies 和 Accelerating Simulink Models。

**注意**

此模块支持为具有可用文件 I/O 的平台生成代码。您不能将此模块与 Simulink Desktop Real-Time™ 软件一起使用，因为该产品不支持文件 I/O。

此模块在装有 Windows Media® Player 软件版本 11 或更高版本的平台上性能最佳。在 Linux® 和 Mac 平台上，此模块仅支持未压缩的 RGB24 AVI 文件。
