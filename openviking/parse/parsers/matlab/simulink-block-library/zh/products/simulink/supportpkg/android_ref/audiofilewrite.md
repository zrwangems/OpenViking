---
type: simulink-block
title: 'Audio File Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Audio and Video'
documentation_page: 'audiofilewrite'
documentation_source_path: 'supportpkg/android_ref/audiofilewrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Audio File Write

## 端口

### 输入

### **Port1** — 音频数据 *M*×*N* 矩阵

该模块发出一个 *M*×*N* 矩阵的数据，其中 *M* 是每帧的样本数，*N* 是通道数。

**数据类型：** `int16`

### **Port2** — 控制 `Input port`（默认）| `Block dialog`

录制音频数据可以由输入端口控制，也可以通过对话框指定。

**数据类型：** `int16`

## 参数

### **文件名** — 开发计算机上的音频文件名 `audiowrite`（默认）

如果文件位置未出现在您的 MATLAB® 路径中，请点击 **浏览** 以指定完整路径。如果该文件位置确实出现在您的 MATLAB 路径中，则仅输入文件名。

### **文件类型** — 音频数据类型 `wav`（默认）| `m4a`

Audio File Write 模块将单声道或立体声音频数据写入 `wav` 或 `m4a`。音频文件的输入可以为 `0` 或 `1`。

### **音频采样频率(Hz)** — 音频数据每帧的样本数 `44100`（默认）| 正整数

音频采样频率必须为正整数值。较大的帧大小可能导致音频输入延迟。请确保音频采样频率与输入采样频率匹配，以避免输出中出现任何问题。

### **录制控制** — 控制音频数据的录制 `Input control`（默认）| `Block dialog`

录制音频数据可以由输入端口控制，也可以通过对话框指定。在 `Input control` 模式下，控制输入只能接受 `0`、`1` 和 `2` 作为输入。`0` 是停止录制，`1` 是开始录制，`2` 是暂停录制。

### **最大录制时间** — 设置音频数据的录制时间 `60`（默认）| 正整数

录制时间必须为正整数值。当 **录制控制** 设置为 `Block dialog` 时，此参数启用。

### **比特率(kpbs)** — 每秒千比特数 `128`（默认）| 正整数

比特率必须为正整数值。当 **文件类型** 设置为 `m4a` 时，此参数启用。

## 所属库

Simulink Support Package for Android Devices / Audio & Video

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2019b 中引入**

## 描述

将音频帧写入音频文件

Audio File Write 模块将单声道或立体声音频数据写入 `wav` 或 `m4a` 文件。该模块接受音频数据作为 *M*×*N* 矩阵，其中 *M* 是每帧的样本数，*N* 是通道数。

音频数据由一个或多个通道组成。`mono` 音频源文件只有一个通道，`stereo` 音频源文件有两个通道。
