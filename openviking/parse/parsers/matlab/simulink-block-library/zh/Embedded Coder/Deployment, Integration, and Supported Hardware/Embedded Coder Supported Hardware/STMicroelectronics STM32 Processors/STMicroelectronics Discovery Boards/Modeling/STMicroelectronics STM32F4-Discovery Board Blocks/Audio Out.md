---
type: simulink-block
title: 'Audio Out'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F4-Discovery Board Blocks'
documentation_page: 'audioout'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/audioout.html'
language: zh-CN
chinese_source: worker-translation
---

# Audio Out

## 端口

### 输入

### **Port\_1** — 包含处理后音频样本标量的端口

输入端口，包含要发送到音频设备的处理后音频样本。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **采样率 (Hz)** — 48000（默认） | 8000 | 16000 | 22050 | 32000 | 44100 | 48000

选择采样率。这是处理后音频样本发送到音频设备时所使用的采样率。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4-Discovery

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

将处理后音频样本发送到音频设备

此模块将处理后的音频数据写入连接到 STM32F4–Discovery™ 板上的处理器的音频设备。您可以以不同速率（例如 16kHz、32kHz 等）和不同帧大小发送音频样本。

您可以在此模块上播放单声道（[1xN] 或 [Nx1]）或立体声 [Nx2] 音频帧。

在配置参数对话框中，在 Coder Target 下，可以选择 `“Audio Out” block DMA interrupt` 作为 **调度器中断源**。这可确保处理算法与 Audio out 模块中断同步。

选择此选项时，请确保以基础速率调度 Audio out 模块。

**注意**

不能在此模块上播放 [1x1] 音频样本，因为帧至少需要两个样本。

### 使用双缓冲发送处理后音频样本

Audio Out 模块使用双缓冲机制将数据发送到音频设备。

使用双缓冲时，一个缓冲区由 DMA 用于将音频帧从处理器传输到音频设备，而另一个缓冲区用于从您的音频算法接收处理后的音频帧。这样做有助于防止在将数据发送到音频设备时覆盖缓冲区。

当您发送长度为 `N samples` 的音频帧时，该模块会创建两个长度为 `N` 个样本的缓冲区。

下面描述 Audio Out 模块中的双缓冲机制。

- 在第一次迭代中，当处理后的音频信号从 ‘Audio out buffer1’ 发送到音频设备时，‘Audio out buffer0’ 会由来自音频处理算法的音频信号填充。

  在第一次迭代中，‘Audio out buffer1’ 不包含音频样本。因此，来自 Audio Out 模块的音频样本会延迟一个音频帧。如果您的模型包含 Mic In 和 Audio Out 模块，则会有两个音频帧的时间延迟，因为 Mic In 模块也使用相同的双缓冲技术。
- 在 DMA 完成从 ‘Audio out buffer1’ 发送处理后数据之后，会生成一个中断。
- 在第二次迭代中，当处理后的音频信号从 Audio out buffer0 发送到音频设备时，‘Audio out buffer1’ 会由来自音频处理算法的音频数据填充。
