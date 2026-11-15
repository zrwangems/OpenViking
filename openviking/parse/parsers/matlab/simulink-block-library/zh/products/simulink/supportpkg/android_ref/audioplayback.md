---
type: simulink-block
title: 'Audio Playback'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Audio and Video'
documentation_page: 'audioplayback'
documentation_source_path: 'supportpkg/android_ref/audioplayback.html'
language: zh-CN
chinese_source: worker-translation
---

# Audio Playback

## 端口

### 输入

### **Port\_1** — 音频样本数值矩阵

该模块输入音频样本，指定为 *N*×2 数值矩阵。这里，*N* 是每帧的音频样本数，矩阵的列分别表示左音频通道和右音频通道。

**数据类型：** `int16`

## 参数

### **音频采样频率 (Hz)** — 设备扬声器的采样率 `44100` (默认) | `8000` | `11025` | `16000` | `22050` | `24000` | `32000` | `48000`

指定设备扬声器的音频采样频率。

## 所属库

Simulink Support Package for Android Devices / Audio & Video

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2014a 中引入**

## 描述

在设备扬声器上播放音频

使用 Audio Playback 模块在设备扬声器上播放音频样本。

**注意**

在与硬件未连接的仿真期间，此模块不执行任何操作。有关详细信息，请参阅“模块在仿真中产生零值或不执行任何操作”。
