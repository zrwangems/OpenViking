---
type: simulink-block
title: 'FM Broadcast Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Analog Baseband Modulation'
documentation_page: 'fmbroadcastmodulatorbaseband'
documentation_source_path: 'ref/fmbroadcastmodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# FM Broadcast Modulator Baseband

## 端口

### 输入

### **In1** — 音频信号 *N* 元素列向量 | 2×*N* 矩阵

音频信号，指定为以下选项之一。

- 用于单声道
  信号的 *N* 元素列向量 — 如果未选择 **Stereo
  audio**，则必须将音频信号指定为
  列向量。*N* 是音频信号中的
  采样数。
- 用于立体声信号的 2×*N* 矩阵 — 如果
  选择 **Stereo
  audio**，则音频信号必须有两个
  声道，并且模块在预加重滤波后执行立体声编码。*N* 是
  每个声道的音频信号中的采样数。

有关信号长度限制的信息，请参阅限制。

**数据类型：** `double` | `single`
**复数支持：** Yes

### **In2** — RDS（或 RBDS）信号 *N* 元素列向量 | 2×*N* 矩阵

RDS（或 RBDS）信号，指定为以下选项之一。

- 用于单声道
  信号的 *N* 元素列向量 — 如果未选择 **Stereo
  audio**，则必须将音频信号指定为
  列向量。*N* 是音频信号中的
  采样数。
- 用于立体声信号的 2×*N* 矩阵 — 如果
  选择 **Stereo
  audio**，则音频信号必须有两个
  声道，并且模块在预加重滤波后执行立体声编码。*N* 是
  每个声道的音频信号中的采样数。

有关信号长度限制的信息，请参阅限制。

**数据类型：** `double` | `single`
**复数支持：** Yes
### 输出

### **Out** — FM 调制基带信号列向量

FM 调制基带信号，返回为与输入信号具有相同数据类型的复数值列向量。此输出的长度为
`length`(`Input 1` × **Sample rate
(Hz)** / **Sample rate of audio
input signal (Hz)**)。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### **Sample rate (Hz)** — 输出信号采样率 `240e3` | 正标量

输出信号采样率，以 Hz 为单位，指定为正标量。采样率必须大于频率偏差的两倍。具体而言，**Sample rate** > 2×**Frequency Deviation**。

### **Frequency deviation (Hz)** — 调制器输出信号频率的峰值偏差 `75e3` | 正标量

调制器输出信号频率的峰值偏差，以 Hz 为单位，指定为正标量。频率偏差必须小于采样率的一半。

系统带宽等于频率偏差与消息带宽之和的两倍。FM 广播标准在美国规定值为 75 kHz，在欧洲为 50 kHz。

### **Pre-emphasis filter time constant (s)** — 预加重高通滤波器时间常数 `7.5e-05`（默认）| 正标量

预加重高通滤波器时间常数，以秒为单位，指定为正标量。FM 广播标准在美国规定值为 75 μs，在欧洲为 50 μs。

### **Sample rate of audio input signal (Hz)** — 输入音频信号的采样率 `48000`（默认）| 正标量

输入音频信号的采样率，以 Hz 为单位，指定为正标量。

### **Stereo audio** — 启用立体声调制的选项 `off`（默认）| `on`

如果输入信号是立体声音频信号，则选中此复选框。如果未选择，则假定音频信号为单声道。如果选中 **Stereo audio** 复选框，则模块除了基带 (*L*+*R*) 外，还在 38 kHz 频段调制立体声 (*L*–*R*)。有关详细信息，请参阅多路复用立体声和 RDS（或 RBDS）FM 信号。

### **RDS/RBDS modulation** — 启用 RDS（或 RBDS）波形调制的选项 `off`（默认）| `on`

选中此复选框以在 57 kHz 调制基带 RBDS 信号。有关详细信息，请参阅多路复用立体声和 RDS（或 RBDS）FM 信号。

### **Oversampling factor of RDS/RBDS input** — RDS（或 RBDS）输入信号的过采样因子 `10`（默认）| 正整数

RDS（或 RBDS）输入信号的过采样因子，指定为正整数。RDS（或 RBDS）广播数据的采样率为 1187.5 Hz。RDS（或 RBDS）信号采样率为（**Oversampling factor of RDS/RBDS input** × `1187.5`）Hz。

#### 依赖关系

要启用此参数，请选择 **RDS/RBDS modulation**。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 通过使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型发生变化，否则模型将在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度快于使用 `Interpreted execution` 选项时。
- `Interpreted execution` — 通过使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但后续仿真的速度慢于使用 `Code generation` 选项时。在此模式下，可以调试模块的源代码。

有关更多信息，请参阅解释执行与代码生成 (Simulink)。

## 所属库

Communications Toolbox / Modulation / Analog Baseband Modulation

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` \| `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015a 中引入**

## 描述

使用广播 FM 方法进行调制
FM Broadcast Modulator Baseband 模块创建用于广播 FM 信号的 FM 信道结构。有关更多详细信息，请参阅算法。
此图标显示启用了所有端口的模块。FM Broadcast Modulator Baseband 模块显示可选输入端口
