---
type: simulink-block
title: 'Mic In'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F4-Discovery Board Blocks'
documentation_page: 'micin'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/micin.html'
language: zh-CN
chinese_source: worker-translation
---

# Mic In

## 端口

### 输出

### **Port\_1** — 包含来自 MEMS 麦克风的音频样本的标量输出端口

输出端口包含来自 STMicroelectronics® STM32F4–Discovery 板上的 MEMS 麦克风的音频样本。

**数据类型：** `int16`

## 参数

### **Sample rate (Hz)** — 读取音频信号的采样频率 48000 (default) | 8000 | 16000 | 22050 | 32000 | 44100 | 48000

选择采样率。它是从 MEMS 麦克风读取音频信号的采样频率。

### **Frame size (samples)** — 基于采样率的音频信号帧大小 48 (default) |

音频信号帧大小基于您选择的采样率。

### **Sample time** — 基于采样率的采样时间 48/48000 (default) |

模块采样时间基于您选择的采样率计算。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F4-Discovery

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2013b 中引入**

## 描述

从 STMicroelectronics STM32F4– Discovery 板上可用的 MEMS 麦克风读取音频样本

此模块读取从 MEMS 麦克风（MP45DT02，ST MEMS 音频传感器，全向数字麦克风）收集的音频样本，该麦克风在 STM32F4–Discovery™ 板上可用。MEMS 麦克风产生脉冲密度调制 (PDM) 信号。

模块输出发出 int16 脉冲编码调制音频帧，其大小在模块掩码的 **Frame size (samples)** 字段中指定。

模块采样率计算如下：采样频率/ Frame size。

例如，Mic In 模块在 48 kHz 采样频率和 96 个样本帧大小下的采样时间等于 2 ms（96/48000）。Mic In 模块允许的最小采样率为 1ms。

在 Configuration Parameters 对话框中，在 Coder Target 下，您可以选择 `“Mic In” block DMA interrupt` 作为 **Scheduler Interrupt Source**。这确保您的算法处理与 Mic In 模块中断同步。

选择此选项时，请确保您的模型基础速率与 Mic In 模块采样时间相同。

**注意**

由于 Mic In 模块始终输出 1ms 的 int16 PCM 音频帧数据，**Frame Size** 和 **Sample Time** 中的值基于您选择的 **Sample Rate** 计算。这些参数中的值仅用于显示目的。您不能编辑这些值。

### PDM 处理

脉冲密度调制 (PDM) 使用脉冲的密度来表示信号。PDM 中脉冲的相对密度对应于模拟信号幅度。在 PDM 比特流中，‘1’ 对应正极性脉冲，‘0’ 对应负极性脉冲。PDM 使用单比特传送音频。

PDM 处理的一些优势包括：

- 概念和执行简单
- 以数字形式进行低成本音频传输
- 设计良好时系统高效
- 低噪声和较少信号干扰

### 使用双缓冲读取音频数据

Mic In 模块使用双缓冲从 MEMS 麦克风读取音频数据。

使用双缓冲时，DMA 使用一个缓冲区从 MEMS 麦克风读取音频 PDM 信号，而另一个缓冲区用于将音频帧发送到音频处理算法。这有助于防止在音频算法使用缓冲区时将其覆盖。

以下描述 Mic In 模块中的双缓冲机制。

- 在第一次迭代中，当 ‘Mic in buffer1’ 发送数据以供音频处理时，DMA 填充 ‘Mic in buffer0’。

  在第一次迭代中，‘Mic in buffer1’ 不包含音频样本。因此，来自 Mic In 模块的音频样本会延迟一个音频帧。
- DMA 完成填充 Mic in buffer0 后，会触发一个中断。
- 在第二次迭代中，当 ‘Mic in buffer0’ 发送数据以供音频处理时，DMA 填充 ‘Mic in buffer1’。
