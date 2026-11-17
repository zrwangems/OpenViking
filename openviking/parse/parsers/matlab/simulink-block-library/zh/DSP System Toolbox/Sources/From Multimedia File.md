---
type: simulink-block
title: 'From Multimedia File'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
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

彩色图像或视频帧，以 *M*×*N*×*P* 数组形式返回。*M* 和 *N* 分别是每幅图像的行数和列数。*P* 是每幅图像中的颜色通道数。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Multimedia outputs** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **Output color format** 参数设置为 `RGB`，并将 **Image signal** 参数设置为 `One multidimensional signal`。
- 如果 **Output color format** 参数设置为 `RGB` 且 **Image signal** 参数设置为 `Simulink image signal`，则此端口命名为 **Simulink Image**。

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

**R**、**G** 或 **B** 端口的输出必须具有相同的维度。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Multimedia outputs** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **Output color format** 参数设置为 `RGB`，并将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **G** — 图像或视频帧的绿色分量矩阵

图像或视频帧的绿色分量，以 *M*×*N* 矩阵形式返回。*M* 和 *N* 分别是图像的行数和列数。

**R**、**G** 或 **B** 端口的输出必须具有相同的维度。

#### 依赖关系

要启用此端口：

- 将 **File name** 参数设置为包含视频或图像数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Multimedia outputs** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **Output color format** 参数设置为 `RGB`，并将 **Image signal** 参数设置为 `Separate color signals`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **B** — 图像或视频帧的蓝色分量矩阵

图像或视频帧的蓝色分量，以 *M*×*N* 矩阵形式返回。*M* 和 *N* 分别是图像的行数和列数。

**R**、**G** 或 **B** 端口的输出必须具有相同的维度。

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

### 主选项卡

### **File name** — 多媒体文件名称 `speech_dft.mp3`（默认）| 字符向量

指定模块要读取的多媒体文件的名称。模块会确定文件类型（音频和视频、仅音频或仅视频）并提供相关参数。

如果文件位置不在 MATLAB 路径上，请使用 **Browse** 按钮指定完整路径。如果文件位置在 MATLAB 路径上，则只需输入文件名。

在 Windows 平台上，此参数支持指向 MMS（Microsoft Media Server）流的 URL。

### **Inherit sample time from file** — 从文件继承采样时间 on（默认）| off

指定模块是从多媒体文件继承采样时间还是使用指定的采样时间。选中此参数时，模块从输入多媒体文件继承采样时间。清除此参数时，模块使用在 **Desired sample time** 参数中指定的采样时间。

**提示**

当您不知道多媒体文件的预期采样率时，请选中此参数。

### **Desired sample time** — 模块采样时间 `1/30`（默认）| 实正标量

指定模块采样时间。

#### 依赖关系

要启用此参数，请清除 **Inherit sample time from file** 参数。

### **Number of times to play file** — 播放多媒体文件的次数 `inf`（默认）| 正整数

指定播放输入多媒体文件的次数。默认值 `inf` 指定模块重复播放多媒体文件，直到仿真停止时间。

### **Read range** — 音频采样范围 `[1 Inf]`（默认）| 二元素向量

以 [*StartSample* *EndSample*] 形式的二元素行向量指定要读取的采样范围，其中 *StartSample* 是开始读取文件的采样，*EndSample* 是停止读取文件的采样。

#### 依赖关系

要启用此参数，请将 **File name** 参数设置为包含音频数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Multimedia outputs** 参数设置为 `Audio only`。

### **Output end-of-file indicator** — 文件结束指示符 off（默认）| on

使用此参数确定输出是否为多媒体文件中的最后一个视频帧或音频采样。选中此参数时，模块上会出现一个标记为 **EOF** 的 `Boolean` 输出端口。当模块输出最后一个视频帧或音频采样时，**EOF** 端口的输出默认为 1。否则，**EOF** 端口的输出默认为 0。

### **Multimedia outputs** — 媒体类型 `Audio only`（默认）| `Video and audio` | `Video only`

指定从同时包含视频和音频数据的文件中读取的媒体类型。

#### 依赖关系

要启用此参数，请将 **File name** 参数设置为同时包含音频和视频数据的多媒体文件的名称。

### **Samples per audio channel** — 每个音频通道的采样数 `1024`（默认）| 正整数

指定每个音频通道的采样数。此参数适用于包含音频的文件。

#### 依赖关系

要启用此参数，请将 **File name** 参数设置为包含音频数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Multimedia outputs** 参数设置为 `Audio only`。

### **Output color format** — 视频颜色格式 `RGB`（默认）| `Intensity` | `YCbCr 4:2:2`

指定输入视频数据的输出颜色格式。模块支持 `RGB`、`Intensity` 和 `YCbCr 4:2:2` 颜色格式。

如果选择 `RGB`，请使用 **Image signal** 参数指定如何输出颜色信号。

#### 依赖关系

要启用此参数，请将 **File name** 参数设置为包含视频数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Multimedia outputs** 参数设置为 `Video only` 或 `Video and audio`。

### **Image signal** — RGB 视频的输出端口配置 `One multidimensional signal`（默认）| `Separate color signals` | `Simulink image signal`

指定模块如何输出 RGB 彩色视频。如果选择：

- `One multidimensional signal` —— 模块通过 **Image** 端口输出 *M*×*N*×*P* 彩色视频信号，其中 *P* 是颜色平面数。
- `Separate color signals` —— 模块使用三个独立的颜色通道输出视频数据，分别通过 **R**、**G** 和 **B** 端口。每个端口输出 RGB 视频流的一个 *M*×*N* 平面。
- `Simulink image signal` —— 模块输出 `Simulink.ImageType` 数据类型的视频。

#### 依赖关系

要启用此参数：

- 将 **File name** 参数设置为包含视频数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Multimedia outputs** 参数设置为 `Video only` 或 `Video and audio`。
- 将 **Output color format** 参数设置为 `RGB`。

### 数据类型选项卡

### **Audio output data type** — 音频输出数据类型 `double`（默认）| `single` | `int16` | `uint8`

指定 **Audio** 端口输出的音频采样的数据类型。

#### 依赖关系

要启用此参数，请将 **File name** 参数设置为包含音频数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Multimedia outputs** 参数设置为 `Audio only` 或 `Video and audio`。

### **Video output data type** — 视频输出数据类型 `single`（默认）| `double` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `Inherit from file`

指定 **R**、**G**、**B** 或 **Image** 端口输出的视频帧的数据类型。

#### 依赖关系

要启用此参数，请将 **File name** 参数设置为包含视频数据的多媒体文件的名称。如果指定的文件同时包含音频和视频数据，请将 **Multimedia outputs** 参数设置为 `Video only` 或 `Video and audio`。

## 所属库

Audio Toolbox / Sources DSP System Toolbox / Sources

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
- 从此模块生成的可执行文件依赖于 MATLAB 附带的预构建动态库文件（`.dll` 文件）。使用 `packNGo` 函数将从此模块生成的代码及所有相关文件打包到一个压缩 ZIP 文件中。使用此 ZIP 文件，您可以在未安装 MATLAB 的另一个开发环境中重新定位、解包并重建您的项目。有关更多详细信息，请参阅 How To Run a Generated Executable Outside MATLAB。

## 版本历史

**在 R2006a 之前推出**

### R2022b：支持 OPUS 音频文件格式

From Multimedia File 模块支持 OPUS 文件格式（`.opus`）的音频文件。

## 描述

从多媒体文件流式传输

From Multimedia File 模块从多媒体文件中读取音频采样、视频帧或两者，并生成具有以下数据类型和幅度范围之一的信号。

| 输出数据类型 | 输出幅度范围 |
| --- | --- |
| `double` | ±1 |
| `single` | ±1 |
| `int16` | −32768 至 32767（−215 至 215 − 1） |
| `uint8` | 0 至 255 |

该模块将文件中的数据导入 Simulink® 模型。

**注意**

此模块支持在具有文件 I/O 的主机上进行代码生成。您不能将此模块与 Simulink Desktop Real-Time™ 软件一起使用，因为该产品不支持文件 I/O。此模块生成的代码依赖于预构建的库文件。有关更多详细信息，请参阅代码生成。
