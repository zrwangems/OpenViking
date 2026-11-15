---
type: simulink-block
title: 'ALSA Audio Playback'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Audio and Video'
documentation_page: 'alsaaudioplayback'
documentation_source_path: 'supportpkg/raspberrypi_ref/alsaaudioplayback.html'
language: zh-CN
chinese_source: worker-translation
---

# ALSA Audio Playback

## 端口

### 输入

### **Port\_1** — 音频数据 *N*×*C* 矩阵

该模块接受一个 *N*×*C* 矩阵，其中 *N* 是每通道样本数，*C* 是音频支持的通道数。该模块根据输入信号确定这些值。

**数据类型：** `int8` | `int16` | `int32`

## 参数

### **设备名称** — ALSA 音频输出设备 `'hw:0,0'`（默认）| 任何已连接的 ALSA 音频输出设备

指定连接到硬件的 ALSA 音频输出设备，模块将数据发送到该设备。默认值 `'hw:0,0'` 指定模块将音频发送到硬件的默认音频插孔。

您可以将音频发送到连接到硬件的任何 ALSA 音频输出设备。要获取连接到硬件的音频输出设备列表，请使用 `listAudioDevices` 函数，如“列出可用的 ALSA 音频输出设备”中所述。

### **音频采样频率 (Hz)** — 音频采样率 `44100`（默认）| 任何正整数

指定音频设备用于播放音频的采样率，以 Hz 为单位。**音频采样频率 (Hz)** 的范围取决于已连接的 ALSA 音频输出设备。要查找音频输出设备支持的采样率范围，请使用 `listAudioDevices` 函数，如“列出可用的 ALSA 音频输出设备”中所述。但是，如果指定的采样频率不受设备支持，请在 **设备名称** 中将 ALSA 音频输出设备设置为 `'plughw:0,0'`。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Audio and Video

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2013a 中引入**

## 描述

使用 ALSA 将音频发送到声卡进行播放

ALSA Audio Playback 模块将音频数据发送到连接到硬件的音频输出设备，例如扬声器或耳机。该模块使用高级 Linux 声音架构 (ALSA) 驱动程序框架发送音频数据。

该模块接受一个 *N*×*C* 矩阵，其中 *N* 是每通道样本数，*C* 是音频支持的通道数。该模块根据输入信号确定这些值。

**注意**

要将 ALSA Audio Playback 模块用于支持两个以上通道的音频设备，您必须拥有 Audio Toolbox™ 许可证。

在 Simulink® 模型中，您可以将 ALSA Audio Playback 模块设置为 Raspberry Pi® 硬件的调度器中断源。有关详细信息，请参阅调度器选项。

### 算法

假设有一个 Simulink 模型，其中包含一个 ALSA Audio Capture 模块和一个 ALSA Audio Playback 模块。ALSA Audio Capture 从连接到硬件音频输入连接器的麦克风读取立体声音频数据。该模块输出 3×2 矩阵形式的数据。在每个采样时间，ALSA Audio Playback 模块接收该音频矩阵，并将音频发送到连接到硬件音频输出插孔的耳机。

ALSA Audio Playback 模块根据每音频通道样本数 (*N*) 和采样频率 (*F*s) 确定采样时间 (*T*s)。

*T*s = *N* / *F*s

例如，如果 *N* 为 4410 个样本且 *F*s 为 44,100 Hz，则模块采样时间为 4410/44,100 = 0.1 seconds。

*N* 是每音频通道的样本数。模块根据输入数据确定 *N* 的值。*F*s 是在 **音频采样频率 (Hz)** 参数中指定的输入数据采样频率。
