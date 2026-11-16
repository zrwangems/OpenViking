---
type: simulink-block
title: 'Audio Output'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / Multimedia'
documentation_page: 'audiooutput'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/audiooutput.html'
language: zh-CN
chinese_source: worker-translation
---

# Audio Output

## 端口

### 输入

### **Port\_1** — 包含以帧矩阵形式表示的 PCM 音频采样的输入端口

该模块接受 `[NxM]` 或 `[MxN]``int16` PCM 音频帧。`N` 是每帧的采样数。`M` 是信号中的音频通道数。

支持的最大音频通道数对于 STM32F746G 为 2，对于 STM32F769I 为 4。对于 STM32F746G，该模块支持单声道音频帧：(`[Nx1]` 或 `[1xN]`) 格式和立体声：(`[Nx2]` 或 `[2xN]`) 格式。对于 STM32F769I，该模块支持四声道音频帧：`[4xN]` 或 `[Nx4]`。`M` 和 `N` 的值由输入端口传入的音频帧确定。

该模块将 `N`×`2` 矩阵解释为具有 `2` 个独立通道且每通道 `N` 个采样的多通道信号。例如，该模块将一系列 `5`×`2` 矩阵解释为帧大小为 5 的双通道信号。

**数据类型：** `int16`

## 参数

### **Device** — 要将音频数据发送到的设备 `Headphone`（默认） | `Speaker` | `Both`

选择该模块向其发送音频数据的音频设备。

### **Sampling frequency (Hz)** — 将音频信号写入音频设备的采样频率 `8000` | `11025` | `16000` | `22050` | `32000` | `44100 (default for STM32F769I)` | `48000 (default for STM32F746G)` | `96000` | `192000(STM32F746G only)`

指定每秒写入你在 **Device** 参数中指定的音频设备的采样数。

### **Volume** — 输出端音频信号的响度 `90 (default for STM32F746G)` | `80 (default for STM32F769I)` | `integer between 0 and 100`

该模块对你在该参数中指定的值应用增益。增益计算如下：

(Volume\*63) /100

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

将处理后的音频采样发送到 STMicroelectronics STM32F746G/STM32F769I– Discovery 板上的音频设备

Audio Output 模块将处理后的音频数据写入连接到 STM32F746G/STM32F769I–Discovery™ 板上处理器的音频设备（耳机或扬声器）。

该模块接受 `int16` 脉冲编码调制 (PCM) 音频帧。对于 STM32F746G，这些帧是单声道：(`[1xN]` 或 `[Nx1]`) 或立体声：(`[2xN]` 或 `[Nx2]`) `int16` 矩阵。对于 STM32F769I，这些帧是四声道：`[4xN]` 或 `[Nx4]`。`N` 是来自输入信号的每帧采样数，`2` 和 `4` 是每帧的音频通道数。

你可以使用不同的采样频率以不同速率发送音频采样，例如 8 kHz、11 kHz、16 kHz、22 kHz、32 kHz、44 kHz、48 kHz、96 kHz 和 192 kHz（仅限 STM32F746G）。

使用此模块的参数，你可以指定要将音频发送到的设备。你还可以指定模块发出音频帧时的音量级别。

### 将音频写入耳机或扬声器

STM32F746G–Discovery 板将音频发送到连接到它的音频设备、耳机或扬声器，或两者。

来自 Audio Output 模块实例输入端口的 `int16` PCM 音频帧通过 ARM® Cortex® M7 处理器和 WM8994 编解码器流式传输。然后这些帧被发送到连接的音频设备。

ARM Cortex M7 处理器、WM8994 编解码器和音频设备之间的音频数据使用 I2S 线路传输。

**注意**

通过 ARM Cortex M7 处理器和 WM8994 编解码器流式传输的音频帧不进行任何转换。

### 使用双缓冲发送处理后的音频采样

Audio Output 模块使用双缓冲机制将数据发送到音频设备。

使用双缓冲时，DMA 使用一个缓冲区将音频帧从处理器传输到音频设备，同时另一个缓冲区接收来自你的音频算法的处理后音频帧。将数据发送到音频设备时，这样做有助于防止覆盖缓冲区。

当你发送长度为 `N` 个采样的音频帧时，该模块会创建两个长度为 `N` 个采样的缓冲区。

在 Audio Output 模块中使用双缓冲机制时：

- 在第一次迭代中，当处理后的音频信号从 Audio out buffer1 发送到音频设备时，Audio out buffer0 会填充来自音频处理算法的音频信号。

  在第一次迭代中，Audio out buffer1 不包含音频采样。因此，来自 Audio Output 模块的音频采样会延迟一个音频帧。如果你的模型有 Audio Input 和 Audio Output 模块，则会有两个音频帧的时间延迟。出现此延迟是因为 Audio Input 模块也使用相同的双缓冲技术。
- 在 DMA 完成从 Audio out buffer1 发送处理后的数据后，会生成一个中断。
- 在第二次迭代中，当处理后的音频信号从 Audio out buffer0 发送到音频设备时，Audio out buffer1 会填充来自音频处理算法的音频数据。
