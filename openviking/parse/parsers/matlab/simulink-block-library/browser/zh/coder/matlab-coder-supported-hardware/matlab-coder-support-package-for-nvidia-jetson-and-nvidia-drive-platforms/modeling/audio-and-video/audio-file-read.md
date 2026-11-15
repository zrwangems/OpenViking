---
type: simulink-block
title: 'Audio File Read'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Audio and Video'
documentation_page: 'audiofileread'
documentation_source_path: 'nvidia/ref/audiofileread.html'
language: zh-CN
chinese_source: worker-translation
---

# Audio File Read

## 端口

### 输出

### **Port\_1** — 音频数据 *N*×*C* 矩阵

模块将音频数据输出为 *N*×*C* 矩阵，其中 *N* 是每个通道的采样数，*C* 是音频支持的通道数。

例如，对于立体声音频源文件，当 **每个音频通道的采样数(N)** 参数设置为 `3` 时，模块将音频数据组织为 3×2 矩阵，这表示包含每个通道三个采样的 2 通道信号。

模块图显示来自 Audio File Read 模块的数据布局

使用 **每个音频通道的采样数(N)** 参数指定 *N*。当使用 **文件名** 参数浏览音频文件时，所选音频文件支持的通道数 *C* 会显示在模块上。

当音频播放次数超过 **播放文件的次数** 参数指定的值时，**Port\_1** 端口在每个采样时间输出 `0`。例如，如果将 **播放文件的次数** 参数设置为 `3`，则在音频文件播放三次后，**Port\_1** 端口输出零。

**数据类型：** `int16`

### **EOF** — 音频文件结束指示 `0` | `1`

当模块输出最后一个音频采样时，该端口输出 `1`。否则，该端口输出 `0`。

#### 依赖关系

要启用该端口，请选择 **输出音频结束指示** 参数。

**数据类型：** `Boolean`

## 参数

### **文件名** — 音频文件的名称 `guitartune.wav` (默认)

如果文件的位置未出现在您的 MATLAB® 路径上，请点击 **浏览** 以指定完整路径。如果此文件的位置确实出现在您的 MATLAB 路径上，则仅输入文件名。

#### 编程使用

|  |
| --- |
| **模块参数：** `FileName` |
| **类型：** character vector |
| **值：** 有效的音频文件名 |
| **默认值：** `'guitartune.wav'` |

### **播放文件的次数** — 播放音频文件的次数 `inf` (默认) | 大于 0 的整数值

输入 `inf` 可播放文件，直到停止仿真。

#### 编程使用

|  |
| --- |
| **模块参数：** `PlayCount` |
| **类型：** character vector |
| **值：** 正整数 |
| **默认值：** `'Inf'` |

### **输出音频结束指示** — 确定输出是否为音频文件中的最后一个音频采样 `off` (默认) | `on`

当模块输出最后一个音频采样时，`EOF` 端口输出 `1`。否则，该端口输出 `0`。

#### 编程使用

|  |
| --- |
| **模块参数：** `OutputEOFIndicator` |
| **类型：** character vector |
| **值：** `'off'` | `'on'` |
| **默认值：** `'off'` |

### **每个音频通道的采样数(N)** — 每个音频通道的采样数 `4410` (默认) | 大于 0 的整数值

此参数指定模块输出的输出矩阵的行数。输出矩阵的维度为 *N*×*C*，其中 *N* 是每个通道的采样数，*C* 是通道数。

#### 编程使用

|  |
| --- |
| **模块参数：** `SamplesPerFrame` |
| **类型：** character vector |
| **值：** 正整数 |
| **默认值：** `'4410'` |

## 所属库

NVIDIA Jetson and NVIDIA DRIVE / Audio and Video

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2021a 中引入**

## 描述

从音频文件读取音频帧

Audio File Read 模块复制音频源文件并将音频数据输出到您的模型中。音频数据可以按 **播放文件的次数** 参数指定的次数循环播放。音频数据可以包含一个或多个通道 *C*。单声道音频源文件只有一个通道，立体声音频源文件有两个通道。音频数据从模块输出为 *N* 个连续的音频数据采样。

### 算法

Audio File Read 模块根据所选音频文件的每个音频通道的采样数 (*N*) 和采样频率 (*F*s) 确定采样时间 (*T*s)。

*T*s = *N* / *F*s

例如，如果 *N* 为 4410 个采样，*F*s 为 44,100 Hz，则模块采样时间为 4410/44,100 = 0.1 seconds。

*N* 是您在 **每个音频通道的采样数(N)** 参数中指定的值。当您使用 **文件名** 参数浏览文件时，所选音频文件的 *F*s 会自动显示在模块上。
