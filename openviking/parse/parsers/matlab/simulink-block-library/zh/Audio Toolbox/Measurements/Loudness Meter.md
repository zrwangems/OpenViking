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
```yaml
ports:
- name: Port_1
  summary: 输入信号矩阵 | 一维向量
  direction: input
  data_types: single | double
- name: M
  summary: 瞬时响度测量列向量
  direction: output
  data_types: single | double
- name: S
  summary: 短时响度测量列向量
  direction: output
  data_types: single | double
- name: TP
  summary: 真峰值实数标量
  direction: output
  data_types: single | double
```

### 输入

### **Port\_1** — 输入信号矩阵 | 一维向量

- 矩阵输入 –– 输入的每一列被视为一个独立声道。如果使用默认的**声道权重**，请按以下顺序指定输入声道：[Left, Right, Center, Left surround, Right surround]。
- 一维向量输入 –– 输入被视为单声道。

**数据类型：** `single` | `double`
### 输出

### **M** — 瞬时响度测量列向量

该模块输出一个列向量，其数据类型和行数与输入信号相同。

**数据类型：** `single` | `double`

### **S** — 短时响度测量列向量

该模块输出一个列向量，其数据类型和行数与输入信号相同。

**数据类型：** `single` | `double`

### **TP** — 真峰值实数标量

该模块输出一个实数标量，其数据类型与输入信号相同。

#### 依赖关系

要启用此端口，请选择**输出真峰值**参数。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Channel weights
  summary: 应用于每个输入声道的线性加权 [1, 1, 1, 1.41, 1.41]（默认）| 非负行向量
  group: ''
- name: Use relative scale for loudness measurements
  summary: 指定模块输出相对于目标级别的响度测量值 off（默认）| on
  group: ''
- name: Target loudness level (LUFS)
  summary: 相对响度测量的参考级别 –23（默认）| 实数标量
  group: ''
- name: Output true-peak value
  summary: 添加真峰值输出端口 off（默认）| on
  group: ''
- name: Inherit sample rate from input
  summary: 指定输入采样率的来源 on（默认）| off
  group: ''
- name: Input sample rate (Hz)
  summary: 输入采样率 44100（默认）| 标量
  group: ''
- name: Simulate using
  summary: 指定要运行的仿真类型 Code generation（默认）| Interpreted execution
  group: ''
```

如果参数被列为可调，则可以在仿真期间更改其值。

### **Channel weights** — 应用于每个输入声道的线性加权 `[1, 1, 1, 1.41, 1.41]`（默认）| 非负行向量

行向量的元素个数必须等于或大于输入声道数。向量中多余的值将被忽略。

默认声道权重遵循 ITU-R BS.1170-4 标准。要使用默认声道权重，请将 Loudness Meter 模块的输入指定为一个矩阵，其列按以下顺序对应声道：[Left, Right, Center, Left surround, Right surround]。

最佳实践是按以下顺序指定声道权重：[Left, Right, Center, Left surround, Right surround]。

**可调：** 是

### **Use relative scale for loudness measurements** — 指定模块输出相对于目标级别的响度测量值 off（默认）| on

- On — 响度测量值相对于**Target loudness level (LUFS)**指定的值。模块的输出以响度单位（LU）返回。
- Off — 响度测量值为绝对值，以满刻度响度单位（LUFS）返回。

**可调：** 否

### **Target loudness level (LUFS)** — 相对响度测量的参考级别 `–23`（默认）| 实数标量

例如，如果**Target loudness level (LUFS)**为 –23，则 –24 LUFS 的响度值报告为 –1 LU。

**可调：** 是

#### 依赖关系

要启用此参数，请选择**Use relative scale for loudness measurements**参数。

### **Output true-peak value** — 添加真峰值输出端口 off（默认）| on

选择此参数时，模块会添加一个额外的输出端口 **TP**。**TP** 端口输出输入帧的真峰值。

**可调：** 否

### **Inherit sample rate from input** — 指定输入采样率的来源 on（默认）| off

选择此参数时，模块从输入信号继承采样率。清除此参数时，需在**Input sample rate (Hz)**中指定采样率。

**可调：** 否

### **Input sample rate (Hz)** — 输入采样率 `44100`（默认）| 标量

**可调：** 是

#### 依赖关系

要启用此参数，请清除**Inherit sample rate from input**参数。

### **Simulate using** — 指定要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，后续仿真将重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。
- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项缩短了启动时间，但仿真速度比 `Code generation` 慢。在此模式下，可以调试模块的源代码。

**可调：** 否
## 所属库

Audio Toolbox / Measurements

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

**在 R2016b 中引入**

## 描述

符合标准的响度测量

Loudness Meter 模块基于 EBU R 128 和 ITU-R BS.1770-4 标准测量音频信号的响度和真峰值。
