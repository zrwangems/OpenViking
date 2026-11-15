---
type: simulink-block
title: 'I2S Audio Out'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Multimedia Peripherals'
documentation_page: 'i2saudioout'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/i2saudioout.html'
language: zh-CN
chinese_source: worker-translation
---

# I2S Audio Out

## 端口

### 输入

### **Port\_1** — 包含已处理音频采样的端口 `Scalar`

包含要发送到音频设备的已处理音频采样的输入端口。

**数据类型：** `int16` | `int32`

## 参数

### **I2S 模块** — 选择 I2S 音频输出模块 `I2S2`（默认） | `I2S1` | `I2S1`

选择 I2S 音频输出模块。

### **信号格式** — 选择音频输出信号格式 `16 bits`（默认） | `24 bits` | `32 bits`

选择 I2S 音频输出信号格式，以 bits 为单位。

### **音频采样频率（以 kHz 为单位）** — `16`（默认） | `8` | `22.5` | `32` | `44.1` | `48` | `96`

选择音频采样率。已处理音频采样发送到音频设备时所使用的采样率。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

将已处理音频采样发送到音频设备

I2S Audio Out 模块将数据流发送到音频输出连接器。该模块将已处理音频数据写入 STM32F4xx 基板上与处理器连接的音频设备。您可以按不同帧大小，以不同速率（例如 16kHz、32kHz 等）发送音频采样。

输入端口接受用于 **Stereo** 的 [Nx2] 格式的 `int16` 或 `int32` 音频帧。

您只能在此模块上播放立体声 [Nx2] 音频帧。

**注意**

您不能在此模块上播放 [1x1] 音频采样，因为该帧至少需要两个采样。

### 使用双缓冲发送已处理音频采样

Audio Out 模块使用双缓冲机制将数据发送到音频设备。

使用双缓冲时，一个缓冲区由 DMA 使用，以将音频帧从处理器传输到音频设备；而另一个缓冲区用于从您的音频算法接收已处理音频帧。这样做有助于在将数据发送到音频设备时防止覆盖缓冲区。

当您发送长度为 `N samples` 的音频帧时，该模块会创建两个长度为 `N` samples 的缓冲区。

下面描述 Audio Out 模块中的双缓冲机制。

- 在第一次迭代中，当已处理音频信号从 ‘Audio out buffer1’ 发送到音频设备时，会用来自音频处理算法的音频信号填充 ‘Audio out buffer0’。

  在第一次迭代中，‘Audio out buffer1’ 不包含音频采样。因此，来自 Audio Out 模块的音频采样会延迟一个音频帧。如果您的模型包含 Mic In 和 Audio Out 模块，则会有两个音频帧的时间延迟，因为 Mic In 模块也使用相同的双缓冲技术。
- 在 DMA 完成从 ‘Audio out buffer1’ 发送已处理数据后，会生成中断。
- 在第二次迭代中，当已处理音频信号从 Audio out buffer0 发送到音频设备时，会用来自音频处理算法的音频数据填充 ‘Audio out buffer1’。
