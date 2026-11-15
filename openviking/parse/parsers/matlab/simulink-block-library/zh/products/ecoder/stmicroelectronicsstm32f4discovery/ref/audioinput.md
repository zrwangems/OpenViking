---
type: simulink-block
title: 'Audio Input'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / System Core'
documentation_page: 'audioinput'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/audioinput.html'
language: zh-CN
chinese_source: worker-translation
---

# Audio Input

## 端口

### 输出

### **Port\_1** — 输出端口，包含帧矩阵形式的 PCM 音频采样

该模块发出 PCM 音频帧。对于 STM32F746G，输出帧为 `[Nx2]`
`int16` 矩阵。对于 STM32F769I，输出帧为
`[Nx2]` 或 `[Nx4]`
`int16` 矩阵。`N` 是在 **Samples per frame
(N)** 参数中指定的每帧采样数，`2` 是每帧的音频通道数。

该模块将
`N`-by-`2` 矩阵解释为具有 `2` 个独立通道和
每通道 `N` 个采样的多通道信号。例如，
如果将 **Samples per frame (N)** 指定为
`5`，则该模块将以下
`5`-by-`2` 矩阵序列解释为
帧大小为 5 的双通道信号。

**数据类型：** `int16`

## 参数

### **Device** — 从中获取音频的设备 `Microphone` (默认) | `LineIn`

选择该模块从中读取音频数据的设备。

### **Audio sampling frequency (Hz)** — 从音频设备读取音频信号的采样频率 `8000` | `11025` | `16000` | `22050` | `32000` | `44100 (default for STM32F769I)` | `48000 (default for STM32F746G)` | `96000` | `192000(STM32F746G only)`

指定每秒从 **Device** 参数中指定的音频设备读取的采样数。

### **Number of Channels** — 音频通道数（仅限 STM32F769I） `2` (默认) | `4`

如果 **Device** 为 Microphone，则可以选择 2 或 4 个音频通道。此参数对 Line In 不可用。

**注意**

要在 Audio Input 模块中使用四个麦克风，您必须拥有 Audio Toolbox™ 许可证。

### **Samples per frame (N)** — 输出端的每帧采样数 `48(default for STM32F746G)` | `1024(default for STM32F769I)` | `integer between 1 and 65535`

指定该模块发出的每帧采样数。

### **Volume** — 输出端音频信号的响度（仅限 STM32F746G） `90` (默认) | `integer between 0 and 100`

该模块对您在此参数中指定的值应用增益。
增益计算如下：

(Volume\*240)/100

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

从 STMicroelectronics STM32F746G/STM32F769I– Discovery 板上的音频设备读取音频采样

Audio Input 模块从连接到 STM32F746G/STM32F769I–Discovery™ 板上处理器的音频
设备（Microphone、Line In）读取音频采样。音频采样要么采用脉冲密度调制 (PDM)
格式，要么采用脉冲编码调制 (PCM) 格式。音频采样的格式取决于
该模块从中获取音频的设备。

该模块发出 PCM 音频帧。对于 STM32F746G，这些帧为
`[Nx2]`
`int16` 矩阵。对于 STM32F769I，这些帧对于 Line In 输入为
`[Nx2]`，对于 Microphone 输入为 `[Nx2]` 或
`[Nx4]`，具体取决于所选的通道数。`N` 是每帧采样数，
`2` 和 `4` 是每帧的音频通道数。

您可以以不同的速率读取音频采样，例如 8 kHz、11 kHz、16 kHz、22 kHz、
32 kHz、44 kHz、48 kHz、96 kHz 和 192 kHz（仅限 STM32F746G），并使用不同的帧
大小。

使用该模块的参数，您可以指定从中获取音频的设备。对于 STM32F746G，您还可以指定
该模块发出音频帧时的音量级别。

该模块的输出连接到音频设备，例如耳机或扬声器。

### 从 Microphone 或 LineIn 读取音频

STM32F746G/STM32F769I–Discovery 板从连接到该板的两个音频设备（双 MEMS
麦克风 (MP34DT01) 或 Line In）中的任一个获取音频。

STM32F746G–Discovery 板上的双 MEMS 麦克风 (MP34DT01) 输出 PDM 信号，然后该信号被发送到 WM8994 编解码器。
WM8994 编解码器将 PDM 信号转换为 16 位 PCM 格式，并将其发送到
ARM®
Cortex® M7 处理器。

STM32F769I–Discovery 板上的两个双 MEMS 麦克风输出 PDM 信号，然后这些信号被发送到用于 sigma delta 调制的数字滤波器
(DFSDM) 外设。DFSDM 外设将 PDM
信号转换为 16 位 PCM 格式，并将其发送到 ARM
Cortex M7 处理器。

LineIn 输出 PCM 信号。输出信号被发送到 WM8994 编解码器，然后
被发送到 ARM
Cortex M7 处理器。然后这些帧被发送到连接的音频
设备。

音频设备、WM8994 编解码器和 ARM
Cortex M7 处理器之间的音频数据使用 I2S 线路传输。

**注意**

来自 LineIn 的 16 位 PCM 音频帧（通过
WM8994 编解码器和 ARM
Cortex M7 处理器流式传输）不进行任何转换。

### 使用双缓冲读取音频数据

Audio Input 模块使用双缓冲机制从音频设备读取
音频数据。

使用双缓冲时，DMA 使用一个缓冲区从音频设备读取音频 PCM 信号，
而另一个缓冲区将音频帧发送到音频处理
算法。当音频算法使用缓冲区时，此机制有助于防止
缓冲区被覆盖。

在 Audio Input 模块中使用双缓冲机制时：

- 在第一次迭代中，当 Audio In buffer1 发送数据以进行
  音频处理时，DMA 填充 Audio In buffer0。

  在第一次迭代中，Audio In buffer1 不包含
  音频采样。因此，来自 Audio
  Input 模块的音频采样会延迟一个音频帧。
- 在 DMA 完成填充 Audio In buffer0 后，会触发一个中断。
- 在第二次迭代中，当 Audio In buffer0 发送数据以进行
  音频处理时，DMA 填充 Audio In buffer1。
