---
type: simulink-block
title: 'Audio File Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Audio and Video'
documentation_page: 'audiofileread'
documentation_source_path: 'supportpkg/raspberrypi_ref/audiofileread.html'
language: zh-CN
chinese_source: worker-translation
---

# Audio File Read

## 端口

### 输出

### **Port\_1** — 音频数据 *N*×*C* 矩阵

模块将音频数据输出为 *N*×*C* 矩阵，其中 *N* 是每个通道的样本数，*C* 是音频支持的通道数。

例如，对于立体声音频源文件，当 **每个音频通道的样本数(N)** 参数设置为 `3` 时，模块将音频数据组织为 3×2 矩阵，这表示一个 2 通道信号，每通道包含三个样本。

使用 **每个音频通道的样本数(N)** 参数指定 *N*。所选音频文件支持的通道数 *C* 会在您使用 **文件名** 参数浏览音频文件时显示在模块上。

当音频播放次数超过 **播放文件的次数** 参数指定的值时，**Port\_1** 端口会在每个采样时间输出 `0`。例如，如果您将 **播放文件的次数** 参数设置为 `3`，则 **Port\_1** 端口会在音频文件播放三次后输出零。

**数据类型：** `int16`

### **EOF** — 音频文件结束指示符 `0` | `1`

当最后一个音频样本从模块输出时，该端口输出 `1`。否则，该端口输出 `0`。

#### 依赖关系

要启用该端口，请选择 **输出音频结束指示符** 参数。

**数据类型：** `Boolean`

## 参数

### **文件名** — 音频文件的名称 `guitartune.wav`（默认）

如果该文件的位置未出现在您的 MATLAB® 路径上，请点击 **浏览** 以指定完整路径。如果该文件的位置确实出现在您的 MATLAB 路径上，则只需输入文件名。

### **播放文件的次数** — 播放音频文件的次数 `inf`（默认）| 任何大于 0 的整数值

输入 `inf` 可播放文件，直到您停止仿真。

### **输出音频结束指示符** — 确定输出是否为音频文件中的最后一个音频样本 `off`（默认）| `on`

当最后一个音频样本从模块输出时，`EOF` 端口输出 `1`。否则，该端口输出 `0`。

### **每个音频通道的样本数(N)** — 每个音频通道的样本数 `4410`（默认）| 任何大于 0 的整数值

此参数指定模块输出的输出矩阵的行数。输出矩阵的维度为 *N*×*C*，其中 *N* 是每个通道的样本数，*C* 是通道数。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Audio and Video

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2017b 中引入**

## 描述

从音频文件读取音频帧

Audio File Read 模块复制音频源文件，并将音频数据输出到您的模型中。音频数据可以循环播放多次，具体由 **播放文件的次数** 参数指定。音频数据可以由一个或多个通道（*C*）组成。单声道音频源文件只有一个通道，立体声音频源文件有两个通道。音频数据以 *N* 个连续音频样本的形式从模块输出。

### 算法

Audio File Read 模块根据所选音频文件的每个音频通道的样本数 (*N*) 和采样频率 (*F*s) 确定采样时间 (*T*s)。

*T*s = *N* / *F*s

例如，如果 *N* 为 4410 个样本，*F*s 为 44,100 Hz，则模块采样时间为 4410/44,100 = 0.1 seconds。

*N* 是您在 **每个音频通道的样本数(N)** 参数中指定的值。当您使用 **文件名** 参数浏览文件时，所选音频文件的 *F*s 会自动显示在模块上。
