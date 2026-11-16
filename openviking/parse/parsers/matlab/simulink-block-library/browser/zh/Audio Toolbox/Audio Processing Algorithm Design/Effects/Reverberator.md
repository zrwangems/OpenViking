---
type: simulink-block
title: 'Reverberator'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Audio Processing Algorithm Design / Effects'
documentation_page: 'reverberator'
documentation_source_path: 'ref/reverberator.html'
language: zh-CN
chinese_source: worker-translation
---

# Reverberator

## 端口

### 输入

### **x** — 输入信号矩阵 | 一维向量

- 矩阵输入 –– 输入的每一列视为独立通道。
- 一维向量输入 –– 输入视为单通道。

除非指定其他输入端口，否则此端口未命名。

**数据类型：** `single` | `double`

### **Delay** — 混响预延迟 (s)，范围 [0,1] 内的标量

#### 依赖项

要启用此端口，请为 Pre-delay (s) 参数选择 **Specify from input port**。

**数据类型：** `single` | `double`

### **HighCut** — 低通滤波器截止频率，范围 [0, (Sample Rate)/2] 内的正标量

#### 依赖项

要启用此端口，请为 Highcut frequency (Hz) 参数选择 **Specify from input port**。

**数据类型：** `single` | `double`

### **Diffusion** — 混响尾音密度，范围 [0,1] 内的标量

#### 依赖项

要启用此端口，请为 Diffusion 参数选择 **Specify from input port**。

**数据类型：** `single` | `double`

### **Decay** — 混响尾音衰减因子，范围 [0,1] 内的标量

#### 依赖项

要启用此端口，请为 Decay factor 参数选择 **Specify from input port**。

**数据类型：** `single` | `double`

### **Damping** — 高频阻尼，范围 [0,1] 内的标量

#### 依赖项

要启用此端口，请为 High frequency damping 参数选择 **Specify from input port**。

**数据类型：** `single` | `double`

### **WetDry** — 湿（混响）信号与干（原始）信号之比，范围 [0,1] 内的标量

#### 依赖项

要启用此端口，请为 Wet/dry mix 参数选择 **Specify from input port**。

**数据类型：** `single` | `double`

### 输出

### **Port\_1** — 输出信号矩阵

Reverberator 模块将混响后的信号输出为两列矩阵。

**数据类型：** `single` | `double`

## 参数

如果某个参数被列为可调，则可以在仿真期间更改其值。

### **Pre-delay (s)** — 混响预延迟 `0`（默认）| 范围 [0, 1] 内的标量

*混响预延迟* 是听到直达声与第一次早期反射之间的时间。**Pre-delay (s)** 的值与所建模房间的大小成正比。

要从输入端口指定 **Pre-delay (s)**，请为该参数选择 **Specify from input port**。

**可调：** Yes

### **Highcut frequency (Hz)** — 低通滤波器截止频率 `20000`（默认）| 范围 [0, (Sample Rate)/2] 内的标量

*低通滤波器截止频率* 是混响器结构前端的单极点低通滤波器的 –3 dB 截止频率。它防止对输入的高频分量应用混响。

要从输入端口指定 **Highcut frequency (Hz)**，请为该参数选择 **Specify from input port**。

**可调：** Yes

### **Diffusion** — 混响尾音密度 `0.50`（默认）| 范围 [0, 1] 内的标量

**Diffusion** 与混响尾音密度增加的速率成正比。增大 **Diffusion** 会使反射更紧密，从而使声音更厚实。减小 **Diffusion** 会产生更离散的回声。

要从输入端口指定 **Diffusion**，请为该参数选择 **Specify from input port**。

**可调：** Yes

### **Decay factor** — 混响尾音衰减因子 `0.50`（默认）| 范围 [0, 1] 内的标量

**Decay factor** 与反射能量耗尽所需的时间成反比。要对大房间建模，请使用长混响尾音（低衰减因子）。要对小房间建模，请使用短混响尾音（高衰减因子）。

要从输入端口指定 **Decay factor**，请为该参数选择 **Specify from input port**。

**可调：** Yes

### **High frequency damping** — 高频阻尼 `0.0005`（默认）| 范围 [0, 1] 内的标量

**High frequency damping** 与混响输出中高频的衰减成正比。将 **High frequency damping** 设置为较大值会使高频反射比低频反射衰减得更快。

要从输入端口指定 **High frequency damping**，请为该参数选择 **Specify from input port**。

**可调：** Yes

### **Wet/dry mix** — 湿（混响）信号与干（原始）信号之比 `0.3`（默认）| 范围 [0, 1] 内的标量

*Wet/dry mix* 是 Reverberator 模块输出的湿（混响）信号与干（原始）信号之比。

要从输入端口指定 **Wet/dry mix**，请为该参数选择 **Specify from input port**。

**可调：** Yes

### **Inherit sample rate from input** — 指定输入采样率的来源 on（默认）| off

选中此参数时，模块从输入信号继承其采样率。清除此参数时，在 **Input sample rate (Hz)** 中指定采样率。

### **Input sample rate (Hz)** — 输入采样率 `44100`（默认）| 正标量

**可调：** Yes

#### 依赖项

要启用此参数，请清除 **Inherit sample rate from input** 参数。

### **Simulate using** — 指定要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

- `Interpreted execution` – 使用 MATLAB® 解释器对模型进行仿真。此选项可减少启动时间，并且仿真速度与 `Code generation` 相当。在此模式下，您可以调试模块的源代码。
- `Code generation` – 使用生成的 C 代码对模型进行仿真。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，后续仿真会重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。

## 所属库

Audio Toolbox / Effects

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016a 中引入**

## 描述

向音频信号添加混响

Reverberator 模块向单声道或立体声音频信号添加混响。您可以调整 Reverberator 模块的参数，以模拟不同的声学环境。
