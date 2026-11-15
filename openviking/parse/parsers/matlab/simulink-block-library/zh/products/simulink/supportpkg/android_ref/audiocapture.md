---
type: simulink-block
title: 'Audio Capture'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Audio and Video'
documentation_page: 'audiocapture'
documentation_source_path: 'supportpkg/android_ref/audiocapture.html'
language: zh-CN
chinese_source: worker-translation
---

# Audio Capture

## 端口

### 输出

### **Port\_1** — 从设备麦克风捕获的音频样本数值矩阵

该模块输出从设备麦克风捕获的音频样本，返回为 *N*×2 数值矩阵。这里，*N* 是每帧的音频样本数。矩阵的列分别表示左音频声道和右音频声道。

**数据类型：** `int16`

## 参数

### **音频采样频率 (Hz)** — 设备麦克风的采样率 `44100` (默认) | `8000` | `11025` | `16000` | `22050` | `24000` | `32000` | `48000`

指定设备麦克风的采样率。

### **帧大小 (N)** — 每帧的音频样本数 `4410` (默认) | 非负标量

指定每帧的音频样本数。

## 所属库

Simulink Support Package for Android Devices / Audio & Video

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2014a 中引入**

## 描述

从设备麦克风捕获音频流

使用 Audio Capture 模块从设备麦克风捕获一个音频样本。该模块将左音频声道和右音频声道输出为 *N*×2 `int16` 矩阵。*N* 是每帧的音频样本数，矩阵的列分别表示左音频声道和右音频声道。**帧大小 (N)** 参数设置 *N* 的值。

该模块的采样时间由 **帧大小 (N)** 和 **音频采样频率 (Hz)** 参数值推导得出。例如，如果 **音频采样频率 (Hz)** 为 44100 Hz，**帧大小 (N)** 为 4410，则采样时间为 4410/44100 = 0.1s。

**注意**

在未连接硬件的情况下进行仿真时，此模块不执行任何操作。有关详细信息，请参阅模块在仿真中产生零或不执行任何操作。
