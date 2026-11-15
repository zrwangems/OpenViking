---
type: simulink-block
title: 'ALSA Audio Capture'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Audio and Video'
documentation_page: 'alsaaudiocapture'
documentation_source_path: 'supportpkg/raspberrypi_ref/alsaaudiocapture.html'
language: zh-CN
chinese_source: official
---

# ALSA Audio Capture

## 端口

### 输出

### **Port\_1** — 音频数据 *N*×*C* 矩阵

该模块以 *N*×*C* 矩阵形式输出音频数据，其中 *N* 是每个通道的采样数，*C* 是音频支持的通道数。分别在**每帧采样数(N)** 和**通道数(C)** 参数中指定 *N* 和 *C* 的值。

例如，对于每个通道有三个采样的立体声音频源文件，该模块将音频数据组织成一个 3×2 矩阵。

输出矩阵的数据类型是在**设备位深**参数中指定的类型。

**数据类型:** `int8` | `int16` | `int32`

## 参数

### **设备名称** — ALSA 音频输入设备 `'hw:1,0'` (默认) | 任何连接的 ALSA 音频输入设备

指定连接到硬件的 ALSA 音频输入设备，模块从该设备读取音频数据。

您可以从连接到硬件的任意 ALSA 音频输入设备接收音频。要获取连接到硬件的音频输入设备列表，请使用 `listAudioDevices` 函数，如 List Available ALSA Audio Input Devices 中所述。

### **设备位深** — 音频数据类型 **16 位整数** (默认) | **8 位整数** | **32 位整数**

在执行模数转换之前，音频数据转换为在此参数中指定的数据类型。

### **通道数量(C)** — 支持的通道数量 `2` (默认) | 任意正整数

要计算音频输入设备支持的通道数，请使用 `listAudioDevices` 函数，如 List Available ALSA Audio Input Devices 中所述。

### **音频采样频率(Hz)** — 音频采样率 `44100` (默认) | 任意正整数

指定音频输入设备用于读取音频数据的采样率，以 Hz 为单位。**音频采样频率(Hz)** 参数中列出的采样率取决于音频输入设备。要计算音频输入设备支持的采样率，请使用 `listAudioDevices` 函数，如List Available ALSA Audio Input Devices 中所述。

### **每帧采样数(N)** — 每个音频通道的采样数 `4410` (默认) | 任意正整数

此参数指定模块输出的输出矩阵行数。输出矩阵的维度为 *N*×*C*，其中 *N* 是每个通道的采样数，*C* 是通道数。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Audio and Video

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

R2025b 官方文档未提供。

## 版本历史

**在 R2013a 中推出**

## 描述

使用 ALSA 从声卡捕获音频

ALSA Audio Capture 模块从连接到硬件的音频输入设备读取音频数据。该模块使用高级 Linux 声音架构 (ALSA) 驱动框架来读取音频数据。

该模块以 *N*×*C* 矩阵形式输出音频数据，其中 *N* 是每个音频通道的采样数，*C* 是音频设备支持的通道数。分别在**每帧采样数(N)** 和**通道数(C)** 参数中指定 *N* 和 *C* 的值。

**注意**

要将 ALSA Audio Capture 模块用于支持两个以上声道的音频设备，您必须有 Audio Toolbox™ 许可证。

在 Simulink® 模型中，您可以将 ALSA Audio Capture 模块设置为 Raspberry Pi® 硬件的调度器中断源。有关详细信息，请参阅Scheduler options。

### 算法

假设有一个 Simulink 模型，它包括一个 ALSA Audio Capture 模块和一个 ALSA Audio Playback 模块。在每个采样时间，ALSA Audio Capture 从连接到硬件音频输入连接器的麦克风读取立体声音频数据。该模块以 3×2 矩阵形式输出数据。ALSA Audio Playback 模块接受该音频矩阵，并将音频发送到连接到硬件音频输出插孔的耳机。

ALSA Audio Capture 模块根据每个音频通道的采样数 (*N*) 和采样频率 (*F*s) 确定采样时间 (*T*s)。

*T*s = *N* / *F*s

例如，如果 *N* 是 4410 个采样，而 *F*s 是 44,100 Hz，则模块采样时间是 4410/44,100 = 0.1 秒。

*N* 是在**通道数(C)** 参数中指定的每个音频通道的采样数。*F*s 是在**音频采样频率(Hz)** 参数中指定的音频数据的采样频率。
