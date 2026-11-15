---
type: simulink-block
title: 'FM Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Analog Baseband Modulation'
documentation_page: 'fmdemodulatorbaseband'
documentation_source_path: 'ref/fmdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# FM Demodulator Baseband

## 端口

### 输入

### **In** — 输入数据信号 `scalar` | `vector` | `matrix`

输入信号，指定为实数标量、向量或矩阵。

**数据类型：** `double` | `single`
### 输出

### **Out** — 输出数据信号 `scalar` | `vector` | `matrix`

输出信号，返回为实数标量、向量或矩阵。此端口上的数据具有与输入信号相同的数据类型和大小。

**数据类型：** `double` | `single`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条中的 **仿真** 选项卡上的 **准备** 库中，选择 **属性检查器**。

### **Frequency deviation (Hz)** — 解调器的频率偏移 `75e3` (默认) | `positive scalar`

解调器的频率偏移，以 Hz 为单位，指定为正标量。系统带宽等于频率偏移与消息带宽之和的两倍。

### **Simulate using** — 要运行的仿真类型 `Code generation` (默认) | `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 通过使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度快于 `Interpreted execution` 选项。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但后续仿真的速度慢于 `Code generation` 选项。在此模式下，您可以调试模块的源代码。

有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。

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

使用 FM 方法解调

FM Demodulator Baseband 模块对复输入信号进行解调，并返回实输出信号。
