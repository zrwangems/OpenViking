---
type: simulink-block
title: 'ALSA Audio Capture'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / BeagleBone Black / Modeling'
documentation_page: 'alsaaudiocapture'
documentation_source_path: 'beaglebone/ref/alsaaudiocapture.html'
language: zh-CN
chinese_source: worker-translation
---

# ALSA Audio Capture

## 端口

### 输出

### **Port\_1** — 音频数据 *N*×*C* 矩阵

该模块将音频数据输出为 *N*×*C* 矩阵，其中 *N* 是每个通道的样本数，*C* 是音频支持的通道数。分别在 **Samples per frame (N)** 和 **Number of channels (C)** 参数中指定 *N* 和 *C* 的值。

例如，对于每个通道有三个样本的立体声音频源文件，该模块将音频数据组织为 3×2 矩阵。

输出矩阵的数据类型为 **Device Bit depth** 参数中指定的类型。

**数据类型：** `int8` | `int16` | `int32`

## 参数

### **Device name** — ALSA 音频输入设备 `'plughw:0,0'` (default) | 任何已连接的 ALSA 音频输入设备

指定连接到硬件的 ALSA 音频输入设备，该模块从该设备读取音频数据。

此值来自位于 BeagleBone® Black 硬件上的 ALSA 配置文件，`/usr/share/alsa/alsa.conf`。

### **Audio sampling frequency (Hz)** — 音频采样率 `44100` (default) | 正整数

指定音频输入设备用于读取音频数据的采样率，单位为 Hz。**Audio sampling frequency (Hz)** 参数中列出的采样率取决于音频输入设备。

### **Frame size (N)** — 每个音频通道的样本数 `4410` (default) | 正整数

此参数指定模块输出的输出矩阵的行数。输出矩阵的维度为 *N*×*C*，其中 *N* 是每个通道的样本数，*C* 是通道数。

## 所属库

Embedded Coder Support Package for BeagleBone Black Hardware

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2014b 中引入**

## 描述

使用 ALSA 从声卡捕获音频

ALSA Audio Capture 模块从连接到硬件的音频输入设备读取音频数据。该模块使用 Advanced Linux Sound Architecture (ALSA) 驱动程序框架读取音频数据。

该模块将音频数据输出为 *N*×*C* 矩阵，其中 *N* 是每个音频通道的样本数，*C* 是音频设备支持的通道数。分别在 **Samples per frame (N)** 和 **Number of channels (C)** 参数中指定 *N* 和 *C* 的值。

**注意**

要将 ALSA Audio Capture 模块与支持两个以上通道的音频设备一起使用，您必须具有 Audio Toolbox™ 许可证。

### 算法

考虑一个 Simulink® 模型，其中包含 ALSA Audio Capture 模块和 ALSA Audio Playback 模块。在每个采样时间，ALSA Audio Capture 从连接到硬件音频输入连接器的麦克风读取立体声音频数据。该模块将数据输出为 3×2 矩阵。ALSA Audio Playback 模块接受该音频矩阵，并将音频发送到连接到硬件音频输出插孔的耳机。

ALSA Audio Capture 模块根据每个音频通道的样本数 (*N*) 和采样频率 (*F*s) 确定采样时间 (*T*s)。

*T*s = *N* / *F*s

例如，如果 *N* 为 4410 个样本，*F*s 为 44,100 Hz，则模块采样时间为 4410/44,100 = 0.1 seconds。

*N* 是在 **Number of channels (C)** 参数中指定的每个音频通道的样本数。*F*s 是在 **Audio sampling frequency (Hz)** 参数中指定的音频数据采样频率。
