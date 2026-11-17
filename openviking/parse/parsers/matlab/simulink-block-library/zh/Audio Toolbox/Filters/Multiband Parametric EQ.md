---
type: simulink-block
title: 'Multiband Parametric EQ'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Filters'
documentation_page: 'multibandparametriceq'
documentation_source_path: 'ref/multibandparametriceq.html'
language: zh-CN
chinese_source: worker-translation
---

# Multiband Parametric EQ

## 端口
```yaml
ports:
- name: Port_1
  summary: 均衡器音频输入 矩阵 | 向量
  direction: input
  data_types: single | double
- name: Port_1
  summary: 均衡器音频输出 矩阵
  direction: output
  data_types: single | double
```

### 输入

### **Port\_1** — 均衡器音频输入 矩阵 | 向量

均衡器的音频输入，指定为以下之一：

- 矩阵输入 —— 该模块将输入的每一列视为独立通道。
- 向量输入 —— 该模块将输入视为单通道。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 均衡器音频输出 矩阵

均衡器的音频输出，以矩阵形式返回。如果将输入指定为矩阵，则该模块返回与矩阵输入大小相同的输出。如果将输入指定为向量，则输出为 N×1 矩阵。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: EQ order
  summary: 各均衡器频段的阶数 2（默认）| 偶数正整数
  group: 主要
- name: Number of bands
  summary: 均衡器频段的数量 3（默认）| 范围 [1,10] 内的整数
  group: 主要
- name: Specify frequencies from input port
  summary: 从输入端口指定频率 off（默认）| on
  group: 主要
- name: Frequencies (Hz)
  summary: 均衡器频段的中心频率 [100,181,325]（默认）| 长度等于 Number of bands 的行向量
  group: 主要
- name: Specify peak gains from input port
  summary: 从输入端口指定峰值增益 off（默认）| on
  group: 主要
- name: Peak Gains (dB)
  summary: 峰值或陷波滤波器增益 [0,0,0]（默认）| 长度等于 Number of bands 的行向量
  group: 主要
- name: Specify quality factors from input port
  summary: 从输入端口指定品质因数 off（默认）| on
  group: 主要
- name: Quality factors
  summary: 均衡器频段的品质因数 [1.6,1.6,1.6]（默认）| 行向量
  group: 主要
- name: Inherit sample rate from input
  summary: 从输入端口指定采样率 off（默认）| on
  group: 主要
- name: Input sample rate (Hz)
  summary: 输入采样率 44100（默认）| 正标量
  group: 主要
- name: Visualize filter response
  summary: 可视化均衡器的幅值响应 按钮
  group: 主要
- name: Variable name
  summary: 导出滤波器的变量名 myFilt（默认）| 有效变量名
  group: 主要
- name: Overwrite variable if it already exists
  summary: 如果变量已存在则覆盖 on（默认）| off
  group: 主要
- name: Export filter to workspace
  summary: 将滤波器导出到工作区 按钮
  group: 主要
- name: Add low-shelf filter
  summary: 向均衡器添加低搁架滤波器 off（默认）| on
  group: 高级
- name: Specify low-shelf cutoff from input port
  summary: 从输入端口指定低搁架截止频率 off（默认）| on
  group: 高级
- name: Low-shelf cutoff frequency (Hz)
  summary: 低搁架截止频率 200（默认）| 标量
  group: 高级
- name: Specify low-shelf slope from input port
  summary: 指定低搁架斜率 off（默认）| on
  group: 高级
- name: Low-shelf filter slope
  summary: 低搁架斜率 1.5（默认）| 正标量
  group: 高级
- name: Specify low-shelf gain from input port
  summary: 从输入端口指定低搁架增益 off（默认）| on
  group: 高级
- name: Low-shelf filter gain (dB)
  summary: 低搁架增益 0（默认）| 实标量
  group: 高级
- name: Add high-shelf filter
  summary: 向均衡器添加高搁架滤波器 off（默认）| on
  group: 高级
- name: Specify high-shelf cutoff from input port
  summary: 从输入端口指定高搁架截止频率 off（默认）| on
  group: 高级
- name: High-shelf cutoff frequency (Hz)
  summary: 高搁架截止频率 15e3（默认）| 标量
  group: 高级
- name: Specify high-shelf slope from input port
  summary: 从输入端口指定高搁架斜率 off（默认）| on
  group: 高级
- name: High-shelf filter slope
  summary: 高搁架斜率 1.5（默认）| 正标量
  group: 高级
- name: Specify high-shelf gain from input port
  summary: 从输入端口指定高搁架增益 off（默认）| on
  group: 高级
- name: High-shelf filter gain (dB)
  summary: 高搁架增益 0（默认）| 实标量
  group: 高级
- name: Add lowpass filter
  summary: 向均衡器添加低通滤波器 off（默认）| on
  group: 高级
- name: Specify lowpass cutoff from input port
  summary: 从输入端口指定低通截止频率 off（默认）| on
  group: 高级
- name: Lowpass cutoff frequency (Hz)
  summary: 低通截止频率 18e3（默认）| 标量
  group: 高级
- name: Specify lowpass slope from input port
  summary: 从输入端口指定低通斜率 off（默认）| on
  group: 高级
- name: Lowpass filter slope
  summary: 低通斜率 12（默认）| 范围 [0:6:48] 内的实标量
  group: 高级
- name: Add highpass filter
  summary: 向均衡器添加高通滤波器 off（默认）| on
  group: 高级
- name: Specify highpass cutoff from input port
  summary: 从输入端口指定高通截止频率 off（默认）| on
  group: 高级
- name: Highpass cutoff frequency (Hz)
  summary: 高通截止频率 20（默认）| 非负实标量
  group: 高级
- name: Specify highpass slope from input port
  summary: 从输入端口指定高通斜率 off（默认）| on
  group: 高级
- name: Highpass filter slope
  summary: 高通斜率 30（默认）| 范围 [0:6:48] 内的实标量
  group: 高级
- name: Oversample
  summary: 过采样开关 off（默认）| on
  group: 高级
- name: Simulate using
  summary: 指定要运行的仿真类型 Code generation（默认）| Interpreted execution
  group: 高级
```

### 主要

### **EQ order** — 各均衡器频段的阶数 `2`（默认）| 偶数正整数

各均衡器频段的阶数，指定为偶数正整数。所有均衡器频段具有相同的阶数。

### **Number of bands** — 均衡器频段的数量 `3`（默认）| 范围 `[1,10]` 内的整数

均衡器频段的数量，指定为范围 `[1,10]` 内的整数。均衡器频段的数量不包括搁架滤波器、高通滤波器或低通滤波器。

### **Specify frequencies from input port** — 从输入端口指定频率 `off`（默认）| `on`

选择此参数以从输入端口指定频率。

### **Frequencies (Hz)** — 均衡器频段的中心频率 `[100,181,325]`（默认）| 长度等于 Number of bands 的行向量

均衡器频段的中心频率，以 Hz 为单位，指定为长度等于 **Number of bands** 的行向量。该向量由范围 `0` 到 **Input sample rate (Hz)**/2 内的实标量组成。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Specify input frequencies from input port** 设置为 `off`。

### **Specify peak gains from input port** — 从输入端口指定峰值增益 `off`（默认）| `on`

选择此参数以从输入端口指定峰值增益。

### **Peak Gains (dB)** — 峰值或陷波滤波器增益 `[0,0,0]`（默认）| 长度等于 Number of bands 的行向量

峰值或陷波滤波器增益，以 dB 为单位，指定为长度等于 **Number of bands** 的行向量。该向量由范围 `[–inf,20]` 内的实标量组成。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Specify peak gains from input port** 设置为 `off`。

### **Specify quality factors from input port** — 从输入端口指定品质因数 `off`（默认）| `on`

选择此参数以从输入端口指定品质因数。

### **Quality factors** — 均衡器频段的品质因数 `[1.6,1.6,1.6]`（默认）| 行向量

均衡器频段的品质因数，指定为长度等于 **Number of bands** 的行向量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Specify quality factor from input port** 设置为 `off`。

### **Inherit sample rate from input** — 从输入端口指定采样率 `off`（默认）| `on`

选择此参数以从输入端口指定采样率。

### **Input sample rate (Hz)** — 输入采样率 `44100`（默认）| 正标量

输入采样率，以 Hz 为单位，指定为正标量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Inherit sample rate from input port** 设置为 `off`。

### **Visualize filter response** — 可视化均衡器的幅值响应 按钮

此按钮在幅值 (dB) 对频率 (Hz) 的图中绘制低搁架、高搁架、高通（低切）和低通（高切）滤波器的滤波器响应。

**注意**

如果任何参数从输入端口指定，或采样率被继承，则该模块不支持滤波器可视化。

### **Variable name** — 导出滤波器的变量名 `myFilt`（默认）| 有效变量名

导出滤波器时，基础工作区中包含该滤波器的变量名称。该名称必须是有效的 MATLAB® 变量名。

### **Overwrite variable if it already exists** — 如果变量已存在则覆盖 `on`（默认）| `off`

选择此参数后，如果 **Variable name** 参数指定的变量已存在于基础工作区中，则导出滤波器会覆盖该变量。如果未选择此参数，且指定的变量已存在于工作区中，则导出滤波器会创建一个新变量，其名称在变量名后附加下划线和数字。例如，如果变量名为 `var` 且已存在，则导出的变量将命名为 `var_1`。

### **Export filter to workspace** — 将滤波器导出到工作区 按钮

将滤波器导出到基础工作区中由 **Variable name** 参数指定的变量中。

#### 提示

- 如果启用了 **Inherit sample rate from input** 参数且模型未运行，则无法导出滤波器。
- 如果从输入端口指定滤波器特性，则无法导出滤波器。

### 高级

### **Add low-shelf filter** — 向均衡器添加低搁架滤波器 `off`（默认）| `on`

选择此参数以向均衡器添加低搁架滤波器。

### **Specify low-shelf cutoff from input port** — 从输入端口指定低搁架截止频率 `off`（默认）| `on`

选择此参数以从输入端口指定低搁架滤波器的截止频率。

#### 依赖关系

要启用此参数，请将 **Add low-shelf filter** 设置为 `on`。

### **Low-shelf cutoff frequency (Hz)** — 低搁架截止频率 `200`（默认）| 标量

低搁架滤波器的截止频率，以 Hz 为单位，指定为大于或等于 `0` 的标量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Add low-shelf filter** 设置为 `on`，并将 **Specify low-shelf cutoff from input port** 设置为 `off`。

### **Specify low-shelf slope from input port** — 指定低搁架斜率 `off`（默认）| `on`

选择此参数以从输入端口指定低搁架斜率。

#### 依赖关系

要启用此参数，请将 **Add low-shelf filter** 设置为 `on`。

### **Low-shelf filter slope** — 低搁架斜率 `1.5`（默认）| 正标量

低搁架滤波器的斜率，指定为正标量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Add low-shelf filter** 设置为 `on`，并将 **Specify low-shelf slope from input port** 设置为 `off`。

### **Specify low-shelf gain from input port** — 从输入端口指定低搁架增益 `off`（默认）| `on`

选择此参数以从输入端口指定低搁架滤波器的增益。

#### 依赖关系

要启用此参数，请将 **Add low-shelf filter** 设置为 `on`。

### **Low-shelf filter gain (dB)** — 低搁架增益 `0`（默认）| 实标量

低搁架滤波器的增益，指定为实标量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Add low-shelf filter** 设置为 `on`，并将 **Specify low-shelf gain from input port** 设置为 `off`。

### **Add high-shelf filter** — 向均衡器添加高搁架滤波器 `off`（默认）| `on`

选择此参数以向均衡器添加高搁架滤波器。

### **Specify high-shelf cutoff from input port** — 从输入端口指定高搁架截止频率 `off`（默认）| `on`

选择此参数以从输入端口指定高搁架滤波器的截止频率。

#### 依赖关系

要启用此参数，请将 **Add high-shelf filter** 设置为 `on`。

### **High-shelf cutoff frequency (Hz)** — 高搁架截止频率 `15e3`（默认）| 标量

高搁架滤波器的截止频率，以 Hz 为单位，指定为大于或等于 `0` 的标量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Add high-shelf filter** 设置为 `on`，并将 **Specify high-shelf cutoff from input port** 设置为 `off`。

### **Specify high-shelf slope from input port** — 从输入端口指定高搁架斜率 `off`（默认）| `on`

选择此参数以从输入端口指定高搁架滤波器的斜率。

#### 依赖关系

要启用此参数，请将 **Add high-shelf filter** 设置为 `on`。

### **High-shelf filter slope** — 高搁架斜率 `1.5`（默认）| 正标量

高搁架滤波器的斜率，指定为正标量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Add high-shelf filter** 设置为 `on`，并将 **Specify high-shelf slope from input port** 设置为 `off`。

### **Specify high-shelf gain from input port** — 从输入端口指定高搁架增益 `off`（默认）| `on`

选择此参数以从输入端口指定高搁架滤波器的增益。

#### 依赖关系

要启用此参数，请将 **Add high-shelf filter** 设置为 `on`。

### **High-shelf filter gain (dB)** — 高搁架增益 `0`（默认）| 实标量

高搁架滤波器的增益，指定为实标量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Add high-shelf filter** 设置为 `on`，并将 **Specify high-shelf gain from input port** 设置为 `off`。

### **Add lowpass filter** — 向均衡器添加低通滤波器 `off`（默认）| `on`

选择此参数以向均衡器添加低通滤波器。

### **Specify lowpass cutoff from input port** — 从输入端口指定低通截止频率 `off`（默认）| `on`

选择此参数以从输入端口指定低通滤波器的截止频率。

#### 依赖关系

要启用此参数，请将 **Add lowpass filter** 设置为 `on`。

### **Lowpass cutoff frequency (Hz)** — 低通截止频率 `18e3`（默认）| 标量

低通滤波器的截止频率，以 Hz 为单位，指定为大于或等于 `0` 的标量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Add lowpass filter** 设置为 `on`，并将 **Specify lowpass cutoff from input port** 设置为 `off`。

### **Specify lowpass slope from input port** — 从输入端口指定低通斜率 `off`（默认）| `on`

选择此参数以从输入端口指定低通滤波器的斜率。

#### 依赖关系

要启用此参数，请将 **Add lowpass filter** 设置为 `on`。

### **Lowpass filter slope** — 低通斜率 `12`（默认）| 范围 `[0:6:48]` 内的实标量

低通滤波器的斜率，以 dB/octave 为单位，指定为范围 `[0:6:48]` 内的实标量。不是 6 的倍数的值将舍入到最接近的 6 的倍数。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Add lowpass filter** 设置为 `on`，并将 **Specify lowpass slope from input port** 设置为 `off`。

### **Add highpass filter** — 向均衡器添加高通滤波器 `off`（默认）| `on`

选择此参数以向均衡器添加高通滤波器。

### **Specify highpass cutoff from input port** — 从输入端口指定高通截止频率 `off`（默认）| `on`

选择此参数以从输入端口指定高通滤波器的截止频率。

#### 依赖关系

要启用此参数，请将 **Add highpass filter** 设置为 `on`。

### **Highpass cutoff frequency (Hz)** — 高通截止频率 `20`（默认）| 非负实标量

高通滤波器的截止频率，以 Hz 为单位，指定为大于或等于 `0` 的实标量。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Add highpass filter** 设置为 `on`，并将 **Specify highpass cutoff from input port** 设置为 `off`。

### **Specify highpass slope from input port** — 从输入端口指定高通斜率 `off`（默认）| `on`

选择此参数以从输入端口指定高通滤波器的斜率。

#### 依赖关系

要启用此参数，请将 **Add highpass filter** 设置为 `on`。

### **Highpass filter slope** — 高通斜率 `30`（默认）| 范围 `[0:6:48]` 内的实标量

高通滤波器的斜率，以 dB/octave 为单位，指定为范围 `[0:6:48]` 内的实标量。不是 6 的倍数的值将舍入到最接近的 6 的倍数。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Add highpass filter** 设置为 `on`，并将 **Specify highpass slope from input port** 设置为 `off`。

### **Oversample** — 过采样开关 `off`（默认）| `on`

过采样开关，指定为以下之一：

- `off` —— 以输入采样率运行多频段参数均衡器。
- `on` —— 以输入采样率的两倍运行多频段参数均衡器。过采样可最小化双线性变换引入的频率扭曲效应。

半带内插器在均衡之前实现过采样。半带抽取器在均衡之后将采样率降低回输入采样率。

### **Simulate using** — 指定要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

要运行的仿真类型，指定为以下之一：

- `Interpreted execution` —— 使用 MATLAB 解释器仿真模型。此选项可缩短启动时间，且仿真速度与 `Code generation` 相当。在此模式下，您可以调试模块的源代码。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不更改，C 代码将在后续仿真中重用。此选项需要额外的启动时间，但后续仿真的速度快于 `Interpreted execution`。

**可调：** 否
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

**在 R2021b 中引入**

## 描述

多频段参数均衡器

Multiband Parametric EQ 模块使用指定的中心频率、增益和品质因数，在输入的每个通道上独立执行多频段参数均衡。您可以将此模块配置为最多 10 个频段。您可以添加低搁架和高搁架滤波器以及高通（低切）和低通（高切）滤波器。
