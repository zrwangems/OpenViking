---
type: simulink-block
title: 'ALSA Audio Playback'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / BeagleBone Black / Modeling'
documentation_page: 'alsaaudioplayback'
documentation_source_path: 'beaglebone/ref/alsaaudioplayback.html'
language: zh-CN
chinese_source: worker-translation
---

# ALSA Audio Playback

## 端口

### 输入

### **Port\_1** — 音频数据 *N*×*C* 矩阵

该模块接受一个 *N*×*C* 矩阵，其中 *N* 是每个通道的样本数，*C* 是音频支持的通道数。该模块根据输入信号确定这些值。

**数据类型：** `int8` | `int16` | `int32`

## 参数

### **设备名称** — ALSA 音频输入设备 `'plughw:0,0'`（默认） | 任何已连接的 ALSA 音频输入设备

指定连接到硬件的 ALSA 音频输入设备，该模块从该设备读取音频数据。

此值来自位于 BeagleBone® Black 硬件上的 ALSA 配置文件 `/usr/share/alsa/alsa.conf`。

### **音频采样频率 (Hz)** — 音频采样率 `44100`（默认） | 正整数

指定音频输入设备用于读取音频数据的采样率，以 Hz 为单位。**音频采样频率 (Hz)** 参数中列出的采样率取决于音频输入设备。

### **队列持续时间 (seconds)** — 音频缓冲区 `1.0`（默认） | 正标量

输入该模块缓冲的音频量。值越高，音频越平滑，但代价是延迟增加。

## 所属库

Embedded Coder Support Package for BeagleBone Black Hardware

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

使用 ALSA 向声卡发送音频以进行播放

ALSA Audio Playback 模块将音频数据发送到连接到硬件的音频输出设备，例如扬声器或耳机。该模块使用高级 Linux 声音架构 (ALSA) 驱动程序框架发送音频数据。

该模块接受一个 *N*×*C* 矩阵，其中 *N* 是每个通道的样本数，*C* 是音频支持的通道数。该模块根据输入信号确定这些值。

**注意**

要将 ALSA Audio Playback 模块与支持两个以上通道的音频设备一起使用，必须具有 Audio Toolbox™ 许可证。

### 算法

考虑一个 Simulink® 模型，其中包含一个 ALSA Audio Capture 模块和一个 ALSA Audio Playback 模块。ALSA Audio Capture 从连接到硬件音频输入连接器的麦克风读取立体声音频数据。该模块输出数据为 3×2 矩阵。在每个采样时间，ALSA Audio Playback 模块接受该音频矩阵，并将音频发送到连接到硬件音频输出插孔的耳机。

ALSA Audio Playback 模块根据每个音频通道的样本数 (*N*) 和采样频率 (*F*s) 确定采样时间 (*T*s)。

*T*s = *N* / *F*s

例如，如果 *N* 为 4410 个样本，*F*s 为 44,100 Hz，则模块采样时间为 4410/44,100 = 0.1 seconds。

*N* 是每个音频通道的样本数。该模块根据输入数据确定 *N* 的值。*F*s 是在 **音频采样频率 (Hz)** 参数中指定的输入数据采样频率。
