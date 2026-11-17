---
type: simulink-block
title: 'Audio Playback Interface'
family: 'peripherals'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Peripherals'
documentation_page: 'audioplaybackinterface'
documentation_source_path: 'ref/audioplaybackinterface.html'
language: zh-CN
chinese_source: worker-translation
---

# Audio Playback Interface

## 端口

### 输入

### **msg** — SoC message data vector

此端口接收来自连接的 Audio Playback 模块的包含音频数据的数据消息。

**数据类型：** `SoCData`
### 输出

### **data** — 音频数据帧 *M* 元素向量 | *M*×*C* 矩阵

当模块接收单个音频通道时，音频数据帧是来自仿真的硬件音频输出的 *M* 元素向量。**Samples per frame** 参数定义音频数据的样本数 *M*。当模块接收多个音频通道时，音频数据帧是 *M*×*C* 矩阵，其中 *C* 由 **Number of channels** 参数指定。

#### 依赖项

要启用此端口，请将 **Output** 参数设置为 `To output port`。

**数据类型：** `int8` | `int16` | `int32`

## 参数

### **Output** — 输出类型 `To terminator`（默认）| `To output port`

指定该模块是否充当终止器（类似于 Terminator 模块），还是向输出端口生成数据。

### **Number of channels** — 数据通道数 `2`（默认）| 正整数

指定发送到音频设备的音频通道数 *C*。此数值必须与 Audio Playback 模块中的 **Number of channels** 参数匹配。

### **Samples per frame** — 从音频设备读取的数据向量大小 `4410`（默认）| 正标量整数

指定音频数据的每帧样本数 *M*。

### **Sample time** — 以 seconds 为单位的采样时间 `-1`（默认）| 正标量

当清除 **Enable event-based execution** 参数时，输入供定时器驱动任务子系统使用的采样时间。

## 所属库

SoC Blockset / Peripherals

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要为您的设计自动生成 C 代码，并在 SoC 设备上执行，请使用 SoC Builder 工具。要为您的 SoC 模型生成并执行 C 代码，需要 Embedded Coder® 功能。有关为 SoC 设计生成代码的详细信息，请参阅 Use SoC Builder to Generate SoC Design。

Embedded Coder 不为该模块生成代码。在生成的代码中，高级 Linux 声音架构（ALSA）驱动框架在设备上执行音频输出。相关的 Audio Playback 模块表示 ALSA 驱动。有关 ALSA 驱动框架的详细信息，请参阅 Advanced Linux Sound Architecture 网站。

## 版本历史

**在 R2021a 中引入**

## 描述

在硬件板上仿真音频输出设备

Audio Playback Interface 模块仿真音频输出设备的行为。该模块以消息形式从连接的 Audio Playback 模块接收音频样本，后者仿真连接到您算法的音频驱动代码。
