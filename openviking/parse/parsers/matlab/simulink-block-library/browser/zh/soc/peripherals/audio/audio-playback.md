---
type: simulink-block
title: 'Audio Playback'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Audio'
documentation_page: 'audioplayback'
documentation_source_path: 'ref/audioplayback.html'
language: zh-CN
chinese_source: worker-translation
---

# Audio Playback

## 端口

### 输入

### **data** — 音频数据帧 *M* 元素向量 | *M*×*C* 矩阵

要发送到音频播放设备的音频数据帧，对于单通道音频，指定为
*M* 元素；对于多通道音频，指定为
*M*×*C* 矩阵。
*C* 由 **Number of
channels** 参数指定。

**数据类型：** `int8` | `int16` | `int32`
### 输出

### **msg** — 来自音频捕获接口的数据消息 标量

此端口将包含音频数据的数据消息输出到连接的 Audio Playback
Interface 模块。有关消息的更多信息，请参阅消息。

**数据类型：** `SoCData`

## 参数

### **Number of channels** — 通道数 `2`（默认） | 正标量

指定每个音频数据采样中的音频通道数 *C*。

## 所属库

SoC Blockset / Processor I/O

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

- 要自动为您的设计生成 C 代码，
  并在 SoC 设备上执行，请使用 SoC Builder 工具。
  有关为 SoC 设计生成代码的更多信息，请参阅使用 SoC Builder 生成 SoC 设计。
- 要为您的 SoC 模型生成并执行 C 代码，此模块需要 Embedded Coder® 和 SoC Blockset™ Support Package for Embedded Linux® Devices。
- 要使用此模块，您必须将 **Hardware Board** 设置为
  `Embedded Linux Board`。然后，您可以按照说明
  配置该板。有关更多信息，请参阅创建 Embedded Linux 设备配置。

当部署到受支持的硬件板时，此模块使用 V4L2 驱动框架
从视频捕获设备（例如摄像头）捕获图像。要指定视频捕获
设备和事件触发器，请使用 Hardware Mapping 工具。有关
V4L2 驱动框架的更多信息，请参阅 Video4Linux。

## 版本历史

**在 R2021a 中引入**

## 描述

将音频样本从算法播放到输出音频设备

Audio Playback 模块模拟硬件板上将音频播放到音频输出（例如扬声器）的驱动程序代码的行为。此模块的输出必须连接到 Audio Playback
Interface 模块，该模块模拟硬件板上的物理音频设备。将此模块放在任务内，并连接到算法，以便在任务每次执行时输出一帧音频样本。有关任务的更多信息，请参阅定时器驱动任务和事件驱动任务。
