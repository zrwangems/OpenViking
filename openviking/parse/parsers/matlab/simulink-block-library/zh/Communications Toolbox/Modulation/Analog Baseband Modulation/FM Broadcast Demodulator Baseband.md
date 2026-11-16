---
type: simulink-block
title: 'FM Broadcast Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Analog Baseband Modulation'
documentation_page: 'fmbroadcastdemodulatorbaseband'
documentation_source_path: 'ref/fmbroadcastdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# FM Broadcast Demodulator Baseband

## 端口

### 输入

### **In** — FM 调制的基带音频信号列向量

FM 调制的基带音频信号，指定为列向量。有关信号长度限制的信息，请参阅限制。

**数据类型：** `double` | `single`
**复数支持：** 是

### 输出

### **Out** — RDS（或 RBDS）信号 *N* 元素列向量 | 2×*N* 矩阵

RDS（或 RBDS）信号，返回为与输入信号具有相同数据类型的列向量。

- 对于单声道信号的 *N* 元素列向量 — *N* 是音频信号中的样本数。如果未选择 **立体声音频**，则输出为列向量。
- 对于立体声信号的 2×*N* 矩阵 — *N* 是每个声道的音频信号中的样本数。如果选择 **立体声音频**，则输出有两个声道，并且模块在去加重滤波后执行立体声解码。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

### **采样率 (Hz)** — 输出信号采样率 `240e3` | 正标量

输出信号采样率，以 Hz 为单位，指定为正标量。采样率必须大于频率偏移的两倍。具体而言，**采样率 (Hz)**
> `2` × **频率偏移 (Hz)**。

### **频率偏移 (Hz)** — 输出信号频率的峰值偏移 `75e3` | 正标量

调制器输出信号频率的峰值偏移，以 Hz 为单位，指定为正实数标量。频率偏移必须小于采样率的一半。

系统带宽等于频率偏移与消息带宽之和的两倍。FM 广播标准在美国规定值为 75 kHz，在欧洲为 50 kHz。

### **去加重滤波器时间常数 (s)** — 去加重低通滤波器时间常数 `7.5e-05` (默认) | 正标量

去加重低通滤波器时间常数，以秒为单位，指定为正标量。FM 广播标准在美国规定值为 75 μs，在欧洲为 50 μs。

### **输出音频采样率 (Hz)** — 输出音频采样率 `48000` (默认) | 正标量

将输出音频采样率以 Hz 为单位指定为正标量。

### **播放音频设备** — 使用默认音频设备播放声音 `on` (默认) | `off`

选中此复选框以从默认音频设备播放声音。

### **缓冲区大小（采样点）** — 缓冲区大小 `4096` (默认) | 正标量

指定模块用于与音频设备通信的缓冲区大小（以采样点为单位），指定为正整数标量。

#### 依赖项

要启用此参数，请选择 **播放音频设备**。

### **立体声音频** — 启用立体声解调的选项 `off` (默认) | `on`

选中此复选框以启用立体声音频信号的解调。

- 如果未选择 **立体声音频** 复选框，则假定音频信号为单声道。
- 如果选择 **立体声音频** 复选框，则模块除了解调基带 (*L*+*R*) 外，还会解调 38 KHz 频带处的立体声音频 (*L*–*R*)。

有关详细信息，请参阅多路复用立体声和 RDS（或 RBDS）FM 信号。

### **RDS/RBDS 解调** — 启用 RDS（或 RBDS）波形解调的选项 `off` (默认) | `on`

选中此复选框以从输入复基带 FM 信号中解调 RBDS 信号。有关详细信息，请参阅多路复用立体声和 RDS（或 RBDS）FM 信号。

### **每个 RDS/RBDS 符号的采样点数** — 每个 RDS/RBDS 符号输出的采样点数 `10` (默认) | 正整数

每个 RDS/RBDS 符号输出的采样点数，指定为正整数。RDS（或 RBDS）广播数据的采样率为 1187.5 Hz。RDS（或 RBDS）采样率为 (**每个 RDS/RBDS 符号的采样点数** × `1187.5`) Hz。

#### 依赖项

要启用此参数，请选择 **RDS/RBDS 解调**。

### **RDS/RBDS Costas 环** — 启用 Costas 环的选项 `off` (默认) | `on`

指定模块是否使用 Costas 环来恢复 RBDS 信号的相位。对于未将 `57` kHz RBDS 信号与 `19` kHz 导频音的三次谐波锁相的无线电台，请选中此复选框。

#### 依赖项

要启用此参数，请选择 **RDS/RBDS 解调**。

### **仿真方式** — 要运行的仿真类型 `Code generation` (默认) | `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 通过使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度快于 `Interpreted execution` 选项。
- `Interpreted execution` — 通过使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但后续仿真的速度慢于 `Code generation` 选项。在此模式下，可以调试模块的源代码。

有关详细信息，请参阅解释执行与代码生成 (Simulink)。

## 所属库

Communications Toolbox / Modulation / Analog Baseband Modulation

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2015a 中引入**

## 描述

解调广播 FM 调制信号

FM Broadcast Demodulator Baseband 模块将广播 FM 信号解调为立体声或单声道音频信号，以及可选的 RDS（或 RBDS）信号。有关详细信息，请参阅算法。

此图标显示启用了所有端口的模块。显示可选输入端口的 FM Broadcast Demodulator Baseband 模块
