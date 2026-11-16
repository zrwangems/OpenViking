---
type: simulink-block
title: 'Loudness Meter'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Measurements'
documentation_page: 'loudnessmeter'
documentation_source_path: 'ref/loudnessmeter.html'
language: zh-CN
chinese_source: worker-translation
---

# Loudness Meter

## 端口

### 输入

### **Port\_1** — 输入信号矩阵 | 一维向量

- Matrix input –– 输入的每一列都被视为独立通道。如果使用默认 **Channel weights**，请按以下顺序指定输入通道：[Left, Right, Center, Left surround, Right surround]。
- 1-D vector input –– 输入被视为单通道。

**数据类型：** `single` | `double`

### 输出

### **M** — 瞬时响度测量列向量

该模块输出一个列向量，其数据类型和行数与输入信号相同。

**数据类型：** `single` | `double`

### **S** — 短期响度测量列向量

该模块输出一个列向量，其数据类型和行数与输入信号相同。

**数据类型：** `single` | `double`

### **TP** — 真峰值实数标量

该模块输出一个实数标量，其数据类型与输入信号相同。

#### 依赖关系

要启用此端口，请选择 **Output true-peak value** 参数。

**数据类型：** `single` | `double`

## 参数

如果参数列为可调，则可以在仿真期间更改其值。

### **Channel weights** — 应用于每个输入通道的线性加权 `[1, 1, 1, 1.41, 1.41]`（默认）| 非负行向量

行向量的元素数量必须等于或大于输入通道的数量。向量中的多余值将被忽略。

默认通道权重遵循 ITU-R BS.1170-4 标准。要使用默认通道权重，请将 Loudness Meter 模块的输入指定为一个矩阵，其列按以下顺序对应于通道：[Left, Right, Center, Left surround, Right surround]。

最佳做法是按以下顺序指定通道权重：[Left, Right, Center, Left surround, Right surround]。

**可调：** Yes

### **Use relative scale for loudness measurements** — 指定模块输出相对于目标电平的响度测量 off（默认）| on

- On — 响度测量相对于 **Target loudness level (LUFS)** 指定的值。模块的输出以响度单位 (LU) 返回。
- Off — 响度测量是绝对的，并以满量程响度单位 (LUFS) 返回。

**可调：** No

### **Target loudness level (LUFS)** — 相对响度测量的参考电平 `–23`（默认）| 实数标量

例如，如果 **Target loudness level (LUFS)** 为 –23，则 –24 LUFS 的响度值报告为 –1 LU。

**可调：** Yes

#### 依赖关系

要启用此参数，请选择 **Use relative scale for loudness measurements** 参数。

### **Output true-peak value** — 为真峰值添加输出端口 off（默认）| on

选择此参数时，模块会添加一个额外的输出端口 **TP**。**TP** 端口输出输入帧的真峰值。

**可调：** No

### **Inherit sample rate from input** — 指定输入采样率的来源 on（默认）| off

选择此参数时，模块从输入信号继承其采样率。清除此参数时，请在 **Input sample rate (Hz)** 中指定采样率。

**可调：** No

### **Input sample rate (Hz)** — 输入的采样率 `44100`（默认）| 标量

**可调：** Yes

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate from input** 参数。

### **Simulate using** — 指定要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码将在后续仿真中重用。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。
- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但仿真速度比 `Code generation` 慢。在此模式下，可以调试模块的源代码。

**可调：** No

## 所属库

Audio Toolbox / Measurements

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **零交叉检测** | `no` |

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2016b 中引入**

## 描述

符合标准的响度测量

Loudness Meter 模块基于 EBU R 128 和 ITU-R BS.1770-4 标准测量音频信号的响度和真峰值。
