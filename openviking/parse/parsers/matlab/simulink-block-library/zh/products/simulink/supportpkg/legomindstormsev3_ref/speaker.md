---
type: simulink-block
title: 'Speaker'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / LEGO MINDSTORMS EV3 Hardware / Modeling / Control Blocks'
documentation_page: 'speaker'
documentation_source_path: 'supportpkg/legomindstormsev3_ref/speaker.html'
language: zh-CN
chinese_source: worker-translation
---

# Speaker

## 端口

### 输入

### **Freq** — 音调频率整数

该模块将 EV3 扬声器发出的音调频率作为输入。扬声器可以产生大约从 `32` 到 `13000` Hz 的可听声音。要停止播放音调，请向此模块输入 `0`。

#### 依赖项

- 要启用此端口，请将 **Input mode** 设置为 `Frequency and volume` 或 `Frequency only`。

**数据类型：** `uint32`

### **Vol** — 音调音量整数

该模块将 EV3 扬声器发出的音调音量作为输入。扬声器音量范围为 `0` 到 `100`（最低到最高）。要停止播放音调，请向此模块输入 `0`。

#### 依赖项

- 要启用此端口，请将 **Input mode** 设置为 `Frequency and volume` 或 `Volume only`。

**数据类型：** `uint32`

## 参数

### **Input mode** — 接受音调频率或音量 `Frequency and volume`（默认） | `Frequency only` | `Volume only`

从这些参数中选择以接受音调的频率、音量或两者。

- `Frequency and volume` — 接受音调的频率和音量两者作为模块输入。
- `Frequency only` — 仅接受音调音量作为模块输入。
- `Volume only` — 仅接受音调频率作为模块输入。

### **Volume (0 - 100)** — 音调音量 `50`（默认） | `0` 到 `100` 之间的正整数

设置 EV3 扬声器发出的音调音量。

#### 依赖项

- 要启用此参数，请将 **Input mode** 设置为 `Frequency only`。

### **Frequency (Hz)** — 音调频率 `100`（默认） | `32` 到 `13000` 之间的正整数

输入 EV3 扬声器发出的音调频率。

#### 依赖项

- 要启用此参数，请将 **Input mode** 设置为 `Volume only`。

### **Duration (ms)** — 音调持续时间 `100`（默认） | 正整数

设置从 EV3 扬声器播放连续音调或间歇音调（蜂鸣声）的持续时间。如果此值等于或大于源模块的采样时间，则扬声器发出连续音调。如果此值短于源模块的采样时间，则扬声器在每个采样周期发出间歇音调。例如，如果源模块的采样时间为 0.1 seconds，而扬声器持续时间为 100 milliseconds (0.1 seconds)，则扬声器播放连续音调。如果将扬声器持续时间更改为 50 milliseconds，则扬声器每 0.1 seconds 发出一次蜂鸣声。

## 所属库

Simulink Support Package for LEGO MINDSTORMS EV3 Hardware

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2012a 中引入**

## 描述

从 EV3 扬声器播放曲调

使用 Speaker 模块从 EV3 主机的扬声器播放音调。要播放音调，请将扬声器音量和频率设置为可听见的值。

此模块会转换其接收值的数据类型。您无需转换输入信号的数据类型。

在没有硬件的仿真期间，此模块输出零。请参阅 Block Produces Zeros or Does Nothing in Simulation。
