---
type: simulink-block
title: 'Audio File Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Android Devices / Modeling / Audio and Video'
documentation_page: 'audiofileread'
documentation_source_path: 'supportpkg/android_ref/audiofileread.html'
language: zh-CN
chinese_source: worker-translation
---

# Audio File Read

## 端口

### 输出

### **Port1** — 音频数据 *M*×*N* 矩阵

该模块输出一个 *M*×*N* 矩阵形式的数据，其中 *M* 是通道数，*N* 是帧大小。要指定 *N*，请使用 **Frame size** 参数。

**数据类型：** `int16`

## 参数

### **File name** — 开发计算机上音频文件的名称 `guitartune.wav`（默认）

如果文件的位置未出现在您的 MATLAB® 路径上，请点击 **Browse** 以指定完整路径。如果此文件的位置出现在您的 MATLAB 路径上，则仅输入文件名。

### **Frame size** — 每帧音频数据的 samples 数量 `1024`（默认）| 正整数

帧大小必须为正整数值。较大的帧大小可能会导致音频输出延迟。

## 所属库

Simulink Support Package for Android Devices / Audio & Video

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2017a 中引入**

## 描述

将计算机中的音频文件添加到移动应用

Audio File Read 模块将音频源文件复制到您的模型中，并将音频数据输出到模型中。该模块以 *M*×*N* 矩阵形式输出音频数据，其中 *M* 是通道数，*N* 是音频数据的帧大小。

音频数据由一个或多个通道组成。`mono` 音频源文件只有一个通道，`stereo` 音频源文件有两个通道。音频数据从模块输出为帧，这些帧由 `M` 个连续的音频数据 samples 组成。

### 算法

Audio File Read 模块的采样时间由所选音频文件的数据帧大小和音频频率自动确定。

*采样时间* = *帧大小* / *音频频率*

例如，如果 *音频频率* 为 44,100 Hz，且 *帧大小* 为 4410 samples，则模块采样时间为 4410 / 44,100 = 0.1 seconds。

要选择音频源文件，请使用 **File name** 参数。所选文件的音频频率会显示在模块上。

**注意**

为保持音频质量，在连接到 Audio File Read 模块的模块中，将采样时间设置为 inherited。
