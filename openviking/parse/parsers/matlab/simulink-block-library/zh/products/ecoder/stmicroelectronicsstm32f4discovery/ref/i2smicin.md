---
type: simulink-block
title: 'I2S Mic In'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Multimedia Peripherals'
documentation_page: 'i2smicin'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/i2smicin.html'
language: zh-CN
chinese_source: worker-translation
---

# I2S Mic In

## 端口

### 输出

### **Port\_1** — 包含来自 MEMS 麦克风的音频样本的输出端口 `Scalar`

该输出端口包含来自基于 STM32F4xx 的板上的 MEMS 麦克风的音频样本。

**数据类型：** `int16` | `int32`

## 参数

### **I2S Module** — 选择 I2S Mic In 模块 `I2S2` (默认) | `I2S1` | `I2S1`

选择 I2S Mic In 模块。

### **Enable PDM audio frame to PCM audio frame conversion** — 启用 PDM 到 PCM 音频帧的转换 `off` (默认) | `on`

选择启用 PDM 音频帧到 PCM 音频帧的转换。

### **Signal format** — 选择音频输出信号格式 `16 bits` (默认) | `24 bits` | `32 bits`

选择 I2S Mic In 信号格式（以位为单位）。

### **Number of channels** — 选择音频输出的通道数 `Stereo` (默认) | `Mono`

- `Stereo` - 选择立体声以使用 2 个不同的音频通道进行录制和播放。
- `Mono` - 选择单声道以使用单个音频通道进行录制和播放。

#### 依赖项

要将参数 **Number of channels** 设置为 `Mono`，请启用 **Enable PDM audio frame to PCM audio frame conversion** 参数。当选择 `Stereo` 时，禁用 **Enable PDM audio frame to PCM audio frame conversion** 参数。

### **Audio sample frequency (in kHz)** — `16` (默认) | `8` | `22.5` | `32` | `44.1` | `48` | `96`

选择音频采样率。它是从 MEMS 麦克风读取音频信号的采样频率。

### **Audio frame size** — 基于采样率的音频信号帧大小 `16` (默认)

音频信号帧大小基于您选择的采样率。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F2xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F3xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32G4xx Based Boards

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023a 中引入**

## 描述

从基于 STM32F4xx 的板上可用的 MEMS 麦克风读取音频样本

I2S Mic In 模块读取从基于 STM32F4xx 的板上可用的 MEMS 麦克风（MP45DT02，ST MEMS 音频传感器，全向数字麦克风）收集的音频样本。MEMS 麦克风产生脉冲密度调制 (PDM) 信号。

该模块输出 `int16` 或 `int32` 的脉冲编码调制音频帧，其大小由模块掩码中的 **Frame size (samples)** 字段指定。

模块采样率计算为：Sample frequency/ Frame size。

例如，当采样频率为 48 kHz 且帧大小为 96 个样本时，Mic in 模块的采样时间等于 2 ms (96/48000)。Mic in 模块允许的最小采样率为 1ms。

**注意**

- 由于 Mic In 模块始终输出 1ms 的 int16 PCM 音频帧数据，**Frame Size** 和 **Sample Time** 中的值基于您选择的 **Sample Rate** 计算。这些参数中的值仅用于显示目的。您无法编辑这些值。
- STM32CubeMX 项目中的 PDM 滤波器选项仅适用于基于 STM32F4xx 和 STM32F7xx 的板。

### PDM 处理

脉冲密度调制 (PDM) 使用脉冲的密度来表示信号。PDM 中脉冲的相对密度对应于模拟信号幅度。在 PDM 位流中，‘1’ 对应于正极性脉冲，‘0’ 对应于负极性脉冲。PDM 使用单个位来传送音频。

PDM 处理的一些优点包括：
- 概念和执行简单
- 以数字形式进行低成本音频传输
- 具有良好设计的高效系统
- 低噪声和较少信号干扰

### 使用双缓冲读取音频数据

Mic In 模块使用双缓冲从 MEMS 麦克风读取音频数据。

使用双缓冲时，一个缓冲区由 DMA 用于从 MEMS 麦克风读取音频 PDM 信号，而另一个缓冲区用于将音频帧发送到音频处理算法。这有助于防止在音频算法使用缓冲区时将其覆盖。

以下描述 Mic In 模块中的双缓冲机制。

- 在第一次迭代中，当 ‘Mic in buffer1’ 发送用于音频处理的数据时，DMA 填充 ‘Mic in buffer0’。

  在第一次迭代中，‘Mic in buffer1’ 不包含音频样本。因此，来自 Mic In 模块的音频样本会延迟一个音频帧。
- 在 DMA 完成填充 Mic in buffer0 后，会触发一个中断。
- 在第二次迭代中，当 ‘Mic in buffer0’ 发送用于音频处理的数据，并且 DMA 填充 ‘Mic in buffer1’。
