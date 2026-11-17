---
type: simulink-block
title: 'From Multimedia File'
family: 'vision'
product_id: 'vision'
product_name: 'Computer Vision Toolbox'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'frommultimediafile'
documentation_source_path: 'ref/frommultimediafile.html'
language: zh-CN
chinese_source: worker-translation
---

# From Multimedia File

## 端口

### 输出

### **Image** — 彩色图像或视频帧数组

彩色图像或视频帧，以 *M*×*N*×*P* 数组形式返回。
*M* 和 *N* 分别是每幅图像的行数和列数。*P* 是每幅图像中的颜色通道数。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Multimedia outputs** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **Output color format** 参数设置为 `RGB`，并将 **Image signal** 参数设置为 `One multidimensional signal`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Simulink.ImageType`

### **I** — 灰度图像或视频帧矩阵

灰度图像或视频帧，以 *M*×*N* 矩阵形式返回。*M* 和 *N* 分别是灰度图像的行数和列数。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Multimedia outputs** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **Output color format** 参数设置为 `Intensity`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **R** — 图像或视频帧的红色分量矩阵

图像或视频帧的红色分量，以 *M*×*N* 矩阵形式返回。*M* 和 *N* 分别是图像的行数和列数。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Multimedia outputs** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **Output color format** 参数设置为 `RGB`，并将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **G** — 图像或视频帧的绿色分量矩阵

图像或视频帧的绿色分量，以 *M*×*N* 矩阵形式返回。*M* 和 *N* 分别是图像的行数和列数。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Multimedia outputs** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **Output color format** 参数设置为 `RGB`，并将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **B** — 图像或视频帧的蓝色分量矩阵

图像或视频帧的蓝色分量，以 *M*×*N* 矩阵形式返回。*M* 和 *N* 分别是图像的行数和列数。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Multimedia outputs** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **Output color format** 参数设置为 `RGB`，并将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Y** — 图像或视频帧的亮度分量矩阵

图像或视频帧的亮度分量，以 *M*×*N* 矩阵形式返回。*M* 和 *N* 分别是图像的行数和列数。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Multimedia outputs** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **Output color format** 参数设置为 `YCbCr 4:2:2`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Cb** — 图像或视频帧的蓝色差色度分量矩阵

图像或视频帧的蓝色差色度分量，以 *M*×*N*/2 矩阵形式返回。*M* 和 *N* 分别是输入图像的行数和列数。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Multimedia outputs** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **Output color format** 参数设置为 `YCbCr 4:2:2`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Cr** — 图像或视频帧的红色差色度分量矩阵

图像或视频帧的红色差色度分量，以 *M*×*N*/2 矩阵形式返回。*M* 和 *N* 分别是每幅输入图像的行数和列数。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Multimedia outputs** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **Output color format** 参数设置为 `YCbCr 4:2:2`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Audio** — 音频信号向量 | 矩阵

音频信号，以 *M* 元素向量或 *M*×*N* 矩阵形式返回。*M* 是每个通道中的采样数，*N* 是通道数。

#### 依赖关系

要启用此端口，请将 **File name** 参数设置为包含音频数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Multimedia outputs** 参数设置为 `Audio only` 或 `Video and audio`。

**数据类型：** `single` | `double` | `int16` | `uint8`

### **EOF** — 文件结束指示符标量

文件结束指示符，针对每个视频帧或音频采样以逻辑标量形式返回。当模块输出文件中的最后一个视频帧或音频采样时，文件结束指示符为 `1`，否则为 `0`。

#### 依赖关系

要启用此端口，请选中 **Output end-of-file indicator** 参数。

**数据类型：** `Boolean`

## 参数

### **Main**

### **File name** — 多媒体文件名称 `vipmen.avi`（默认）| 字符向量

指定模块要读取的多媒体文件的名称。如果文件不在 MATLAB® 路径上，请选择 **Browse** 并导航到该文件，或指定完整的文件路径。

在 Microsoft®
Windows® 平台上，此参数支持指向 Microsoft Media Server (MMS) 流的 URL。

### **Inherit sample time from file** — 从文件继承采样时间 `on`（默认）| `off`

指定模块是从多媒体文件继承采样时间，还是使用指定的采样时间。选中此参数时，模块从输入多媒体文件继承采样时间。

**提示**

当您不知道多媒体文件的预期采样率时，请选中此参数。

### **Desired sample time** — 模块采样时间 `1/30`（默认）| 实正标量

指定模块的采样时间。

#### 依赖关系

要启用此参数，请清除 **Inherit sample time from file** 参数。

### **Number of times to play file** — 播放多媒体文件的次数 `inf`（默认）| 实正整数

指定播放输入多媒体文件的次数。默认值 `inf` 指定模块重复播放多媒体文件，直到仿真停止时间。

### **Output end-of-file indicator** — 文件结束指示符 `off`（默认）| `on`

选中此参数以启用 **EOF** 端口，该端口指示输出帧或采样是否为多媒体文件中的最后一个视频帧或音频采样。

### **Multimedia outputs** — 媒体类型 `Video only`（默认）| `Audio only` | `Video and audio`

指定从同时包含视频和音频数据的文件中读取的媒体类型。

#### 依赖关系

要启用此参数，请将 **File name** 参数设置为同时包含音频和视频数据的多媒体文件的名称。

### **Output color format** — 视频颜色格式 `RGB`（默认）| `Intensity` | `YCbCr 4:2:2`

指定输入视频数据的输出颜色格式。模块支持 `RGB`、`Intensity` 和 `YCbCr 4:2:2` 颜色格式。

#### 依赖关系

要启用此参数，请将 **File name** 参数设置为包含视频数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Multimedia outputs** 参数设置为 `Video only` 或 `Video and audio`。

### **Image signal** — RGB 视频的输出端口配置 `One multidimensional signal`（默认）| `Separate color signals` | `Simulink image signal`

指定模块如何输出 RGB 彩色视频。如果选择 `One multidimensional signal`，模块仅使用 **Image** 端口输出视频数据。如果选择 `Separate color signals`，模块使用三个独立的颜色通道输出视频数据，分别通过 **R**、**G** 和 **B** 端口。如果选择 `Simulink image signal`，模块以 `Simulink.ImageType` 数据类型输出视频。

#### 依赖关系

要启用此参数：

- 将 **File name** 参数设置为包含视频数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Multimedia outputs** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **Output color format** 参数设置为 `RGB`。

### **Read range** — 音频采样范围 `[1 Inf]`（默认）| 二元素行向量

指定从输入文件中读取的音频采样范围，以 `[StartSample EndSample]` 形式的二元素行向量表示。`StartSample` 是模块从音频文件中读取的第一个采样，`EndSample` 是模块从音频文件中读取的最后一个采样。`StartSample` 必须大于或等于 `1`。`EndSample` 必须大于 `StartSample`。

#### 依赖关系

要启用此参数，请将 **File name** 参数设置为包含音频数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Multimedia outputs** 参数设置为 `Audio only`。

### **Samples per audio channel** — 每个音频通道的采样数 `1024`（默认）| 实正整数

指定每个音频通道的采样数。

#### 依赖关系

要启用此参数，请将 **File name** 参数设置为包含音频数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Multimedia outputs** 参数设置为 `Audio only`。

### **Data Types**

### **Video output data type** — 视频输出数据类型 `single`（默认）| `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `Inherit from file`

指定输出视频帧的数据类型。

#### 依赖关系

要启用此参数，请将 **File name** 参数设置为包含视频数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Multimedia outputs** 参数设置为 `Video only` 或 `Video and audio`。

### **Audio output data type** — 音频输出数据类型 `int16`（默认）| `double` | `single` | `uint8`

指定输出音频采样的数据类型。

#### 依赖关系

要启用此参数，请将 **File name** 参数设置为包含音频数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Multimedia outputs** 参数设置为 `Audio only` 或 `Video and audio`。

## 所属库

Computer Vision Toolbox / Sources

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
- 从此模块生成的可执行文件依赖于 MATLAB 附带的预构建动态库文件（`.dll` 文件）。使用 `packNGo` (Simulink Coder) 函数将从此模块生成的代码及所有相关文件打包到一个压缩的 ZIP 文件中。使用此 ZIP 文件，您可以在未安装 MATLAB 的另一个开发环境中重新定位、解包并重新构建您的项目。

## 版本历史

**在 R2006a 之前推出**

## 描述

从多媒体文件中读取视频帧和音频采样

From Multimedia File 模块从多媒体文件中读取视频帧、音频采样或两者。该模块将受支持文件格式的文件中的数据导入到 Simulink® 模型中。有关受支持文件格式的详细信息，请参阅 Supported Platforms and File Formats。

此模块使您能够从系统或通过网络连接读取 WMA 或 WMV 流。类似地，To Multimedia File 模块使您能够将 WMA 或 WMV 流写入系统或通过网络连接写入。如果您的系统没有支持某种文件格式所需的编解码器，则必须将该格式的文件重新编码为 Computer Vision Toolbox™ 支持的文件格式。

如果您拥有 Simulink
Coder™ 许可证，则可以从包含此模块的模型生成代码。要运行生成的可执行文件，您可能需要将预编译的共享库文件添加到系统路径中。有关详细信息，请参阅 Simulink Shared Library Dependencies 和 Accelerating Simulink Models。

**注意**

此模块支持为具有文件 I/O 可用的主机生成代码。您不能将此模块与 Simulink
Desktop Real-Time™ 软件一起使用，因为该产品不支持文件 I/O。
