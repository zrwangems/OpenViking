---
type: simulink-block
title: 'ALSA Audio Playback'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Audio and Video'
documentation_page: 'alsaaudioplayback'
documentation_source_path: 'nvidia/ref/alsaaudioplayback.html'
language: zh-CN
chinese_source: worker-translation
---

# ALSA Audio Playback

## 端口

### 输入

### **Port\_1** — 音频数据 *N*×*C* 矩阵

该模块接受一个 *N*×*C* 矩阵，其中 *N* 是每通道采样数，*C* 是音频支持的通道数。该模块根据输入信号确定这些值。

**数据类型：** `int8` | `int16` | `int32`

## 参数

### **设备名称** — ALSA 音频输出设备 `'hw:0,0'` (默认) | 有效的 ALSA 音频输出设备

指定连接到模块向其发送数据的硬件的 ALSA 音频输出设备。默认值 `'hw:0,0'` 指定模块将音频发送到硬件的默认音频插孔。

您可以将音频发送到连接到硬件的 ALSA 音频输出设备。要获取连接到硬件的音频输出设备列表，请使用 `listAudioDevices` 函数，如“列出可用的 ALSA 音频输出设备”中所述。

#### 程序化使用

|  |
| --- |
| **模块参数：** `deviceStr` |
| **类型：** character vector |
| **值：** `valid name`| |
| **默认值：**  `'hw:0,0'` |

### **音频采样频率 (Hz)** — 音频采样率 `44100` (默认) | positive integer

指定音频设备用于播放音频的采样率，单位为 Hz。**音频采样频率 (Hz)** 的范围取决于所连接的 ALSA 音频输出设备。要查找音频输出设备支持的采样率范围，请使用 `listAudioDevices` 函数，如“列出可用的 ALSA 音频输出设备”中所述。但是，如果您指定的采样频率不受设备支持，请在 **设备名称** 中将 ALSA 音频输出设备设置为 `'plughw:0,0'`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `sampleRateEnum` |
| **类型：** character vector |
| **值：** positive integer |
| **默认值：**  `'44100'` |

## 所属库

NVIDIA Jetson and NVIDIA DRIVE / Audio and Video

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2021a 中引入**

## 描述

使用 ALSA 将音频发送到声卡进行播放

ALSA Audio Playback 模块将音频数据发送到连接到 NVIDIA® 硬件的音频输出设备，例如扬声器或耳机。该模块使用 Advanced Linux Sound Architecture (ALSA) 驱动程序框架发送音频数据。

该模块接受一个 *N*×*C* 矩阵，其中 *N* 是每通道采样数，*C* 是音频支持的通道数。该模块根据输入信号确定这些值。

**注意**

要将 ALSA Audio Playback 模块与支持两个以上通道的音频设备一起使用，您必须拥有 Audio Toolbox™ 许可证。
