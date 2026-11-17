---
type: simulink-block
title: 'Octave Filter'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Filters'
documentation_page: 'octavefilter'
documentation_source_path: 'ref/octavefilter.html'
language: zh-CN
chinese_source: worker-translation
---

# Octave Filter

## 端口

### 输入

### **x** — 输入信号矩阵 | 一维向量

- 矩阵输入 –– 输入的每一列被视为一个独立通道。
- 一维向量输入 –– 输入被视为单通道。

除非您指定额外的输入端口，否则此端口未命名。

**数据类型：** `single` | `double`

### **CF** — 中心频率 (Hz) 标量，范围 `3` 到 `22,000`（含）

#### 依赖关系

要启用此端口，请为 Center frequency (Hz) 参数选择 **Specify from input port**。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 输出信号矩阵

Octave Filter 模块输出的信号与输入信号具有相同的数据类型。输出的大小取决于输入的大小：

- 矩阵输入 –– 模块输出与输入信号大小和数据类型相同的矩阵。
- 一维向量输入 –– 模块输出 *N*×1 矩阵（列向量），其中 *N* 是一维向量中的元素个数。

**数据类型：** `single` | `double`

## 参数

如果参数被列为可调，则您可以在仿真期间更改其值。

### **Filter order** — 倍频程滤波器阶数 `6`（默认）| 偶数整数

**可调：** 否

### **Center frequency (Hz)** — 倍频程滤波器中心频率 `1000`（默认）| 范围 `3` 到 `22,000`（含）内的标量

- 最大中心频率是使上频带边缘等于奈奎斯特频率 *Fs*/2 的值。高于此值的频率将被饱和。
- 最小中心频率是使下频带边缘等于 1 Hz 的值。低于此值的频率将被量化为 1 Hz。

要从输入端口指定 **Center frequency (Hz)**，请为该参数选择 **Specify from input port**。

**可调：** 是

### **Bandwidth** — 以倍频程为单位的滤波器带宽 `1 octave`（默认）| `2/3 octave` | `1/2 octave` | `1/3 octave` | `1/6 octave` | `1/12 octave` | `1/24 octave` | `1/48 octave`

**可调：** 是

### **Oversample the input by 2 for this filter** — 过采样开关 off（默认）| on

- off –– Octave Filter 模块以输入采样率运行。
- on –– Octave Filter 模块以输入采样率的两倍运行。过采样可最小化双线性变换引入的频率畸变效应。FIR 半带插值器在倍频程滤波之前实现过采样。半带抽取器在倍频程滤波之后将采样率降回输入采样率。

**可调：** 否

### **Inherit sample rate from input** — 指定输入采样率的来源 off（默认）| on

当您选择此参数时，模块从输入信号继承其采样率。当您清除此参数时，您在 **Input sample rate (Hz)** 中指定采样率。

**可调：** 否

### **Input sample rate (Hz)** — 输入采样率 `44100`（默认）| 标量

**可调：** 是

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate from input** 参数。

### **Simulate using** — 指定要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

- `Code generation` –– 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不更改，C 代码将在后续仿真中重复使用。此选项需要额外的启动时间，但后续仿真的速度与 `Interpreted execution` 相当。
- `Interpreted execution` –– 使用 MATLAB® 解释器仿真模型。此选项缩短了启动时间，但仿真速度比 `Code generation` 慢。在此模式下，您可以调试模块的源代码。

**可调：** 否

### **Mask for attenuation limits** — 为滤波器响应可视化创建掩膜 `No mask`（默认）| `Class 0` | `Class 1` | `Class 2`

掩膜衰减限值在 ANSI S1.11-2004 标准中定义。

- 如果掩膜为绿色，则设计符合要求。
- 如果掩膜为红色，则设计不符合要求。

**可调：** 是

### **Visualize filter response** — 打开绘图以可视化幅值响应和合规掩膜 按钮

使用 2048 点 FFT 计算幅值响应。

**可调：** 是

### **Variable name** — 导出的滤波器的变量名 `myFilt`（默认）| 有效变量名

基础工作区中用于在导出时包含滤波器的变量名。该名称必须是有效的 MATLAB 变量名。

### **Overwrite variable if it already exists** — 如果变量已存在则覆盖 `on`（默认）| `off`

当您选择此参数时，如果 **Variable name** 参数指定的变量已存在于基础工作区中，导出滤波器将覆盖该变量。如果您不选择此参数且指定的变量已存在于工作区中，导出滤波器将创建一个新变量，在变量名后附加下划线和数字。例如，如果变量名为 `var` 且它已存在，则导出的变量将命名为 `var_1`。

### **Export filter to workspace** — 将滤波器导出到工作区 按钮

将滤波器导出到基础工作区中由 **Variable name** 参数指定的变量中。

#### 提示

- 如果您启用了 **Inherit sample rate from input** 参数且模型未运行，则无法导出滤波器。
- 如果您从输入端口指定滤波器特性，则无法导出滤波器。

## 所属库

Audio Toolbox / Filters

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

倍频程带和分数倍频程带滤波器

Octave Filter 模块在每个输入通道上独立执行倍频程带或分数倍频程带滤波。倍频程带是最高频率为最低频率两倍的频带。倍频程带和分数倍频程带滤波器通常用于模拟人类感知响度的方式。在对数刻度上查看时，倍频程滤波器最易于理解，对数刻度模拟了人耳对频谱的加权方式。
