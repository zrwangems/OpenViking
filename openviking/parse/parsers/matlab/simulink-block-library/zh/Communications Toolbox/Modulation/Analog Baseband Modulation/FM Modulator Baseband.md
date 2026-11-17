---
type: simulink-block
title: 'FM Modulator Baseband'
family: 'modulation'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Analog Baseband Modulation'
documentation_page: 'fmmodulatorbaseband'
documentation_source_path: 'ref/fmmodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# FM Modulator Baseband

## 端口

### 输入

### **In** — 输入数据信号 `scalar` | `vector` | `matrix`

输入信号，指定为实数标量、向量或矩阵。

**数据类型：** `double` | `single`
### 输出

### **Out** — 输出数据信号 `scalar` | `vector` | `matrix`

输出信号，以实数标量、向量或矩阵返回。此端口上的数据与输入信号具有相同的数据类型和大小。

**数据类型：** `double` | `single`

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条上的 **仿真** 选项卡中，在 **准备** 库中，选择 **属性检查器**。

### **频率偏移 (Hz)** — 调制器的频率偏移 `75e3`（默认）| `positive scalar`

调制器的频率偏移，以 Hz 为单位，指定为正标量。系统带宽等于频率偏移与消息带宽之和的两倍。

### **仿真方式** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型发生变化，否则模型会为后续仿真重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比使用 `Interpreted execution` 选项更快。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但后续仿真的速度比使用 `Code generation` 选项更慢。在此模式下，可以调试模块的源代码。

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

使用 FM 方法进行调制

FM Modulator Baseband 模块对实数输入信号应用频率调制，并返回复数输出信号。
