---
type: simulink-block
title: 'Audio Oscillator'
family: 'audio'
product_id: 'audio'
product_name: 'Audio Toolbox'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'audiooscillator'
documentation_source_path: 'ref/audiooscillator.html'
language: zh-CN
chinese_source: worker-translation
---

# Audio Oscillator

## 端口

### 输入

### **F** — 频率 (Hz) 非负标量 | 非负值向量

#### 依赖关系

要启用此端口，请为 Frequency (Hz) 参数选择 **Specify frequency from input
port**。

**数据类型：** `single` | `double`

### **A** — 幅值 非负标量 | 非负值向量

#### 依赖关系

要启用此端口，请为 Amplitude 参数选择 **Specify amplitude from input
port**。

**数据类型：** `single` | `double`

### **DC** — 直流偏移 标量 | 向量

#### 依赖关系

要启用此端口，请为 DC offset 参数选择 **Specify DC offset from input
port**。

**数据类型：** `single` | `double`
### 输出

### **Port\_1** — 输出信号 向量

Audio Oscillator 模块输出由模块参数定义的周期信号。

**数据类型：** `single` | `double`

## 参数

如果某个参数被列为可调，则可以在仿真期间更改其值。

### **Signal type** — 生成波形的类型 `sine`（默认）| `square` | `sawtooth`

这些波形使用 `sin`、`square` 和
`sawtooth`
函数指定的算法生成。

### **Frequency (Hz)** — 生成波形的频率 `100`（默认）| 非负标量 | 非负值向量

- 如果 Signal type 设置为
  `sine`，请将 **Frequency (Hz)** 指定为
  标量或向量。如果 **Frequency (Hz)** 设置为
  *N* 元素向量，则模块的输出是
  *N* 个正弦波的单通道求和。如果 **Frequency
  (Hz)** 设置为 *N* 元素向量，则 Amplitude、Phase offset 和 DC offset 必须是标量
  或 *N* 元素向量。
- 对于方波，请将 **Frequency (Hz)** 指定为
  标量。
- 对于锯齿波，请将 **Frequency (Hz)** 指定为
  标量。

要从输入端口指定 **Frequency (Hz)**，请选择
**从输入端口指定频率**。

**可调：** 是

### **Amplitude** — 生成波形的幅值 `1`（默认）| 非负标量 | 非负值向量

- 如果 Signal type 设置为
  `sine`，请将 **Amplitude** 指定为
  标量或向量。如果 **Amplitude** 设置为
  *N* 元素向量，则模块的输出是
  *N* 个正弦波的单通道求和。如果
  **Amplitude** 设置为 *N* 元素向量，
  则 Frequency (Hz)、Phase offset 和 DC offset 必须是标量
  或 *N* 元素向量。
- 对于方波，请将 **Amplitude** 指定为标量。
- 对于锯齿波，请将 **Amplitude** 指定为
  标量。

要从输入端口指定 **Amplitude**，请选择
**从输入端口指定幅值**。

**可调：** 是

### **Phase offset** — 生成波形的归一化相位偏移 `0`（默认）| 范围 [0, 1] 内的标量 | 值在范围 [0, 1] 内的向量

相位偏移范围 `[0,1]` 对应于归一化的 2π
弧度区间。

- 如果 Signal type 设置为
  `sine`，请将 **Phase offset** 指定为
  标量或向量。如果 **Phase offset** 设置为
  *N* 元素向量，则模块的输出是
  *N* 个正弦波的单通道求和。如果 **Phase
  offset** 设置为 *N* 元素向量，则 Frequency (Hz)、Amplitude 和 DC offset 必须是标量
  或 *N* 元素向量。
- 对于方波，请将 **Amplitude** 指定为标量。
- 对于锯齿波，请将 **Amplitude** 指定为
  标量。

### **DC offset** — 添加到生成波形每个元素的值 `0`（默认）| 标量 | 向量

- 如果 Signal type 设置为
  `sine`，请将 **DC offset** 指定为
  标量或向量。如果 **DC offset** 设置为
  *N* 元素向量，则模块的输出是
  *N* 个正弦波的单通道求和。如果 **DC
  offset** 设置为 *N* 元素向量，则 Frequency (Hz)、Amplitude 和 Phase offset 必须是标量
  或 *N* 元素向量。
- 对于方波，请将 **Amplitude** 指定为标量。
- 对于锯齿波，请将 **Amplitude** 指定为
  标量。

要从输入端口指定 **DC offset**，请选择
**从输入端口指定直流偏移**。

**可调：** 是

### **Duty cycle** — 方波占空比 `0.5`（默认）| 范围 [0, 1] 内的标量

*方波占空比* 是波形高于中值幅值的一个周期所占的百分比。占空比值为 1 或 0
等效于直流信号。

#### 依赖关系

要启用此参数，请将 **Signal type** 设置为
`square`。

### **Width** — 锯齿波宽度 `1`（默认）| 范围 [0, 1] 内的标量

*锯齿波宽度* 确定锯齿波波形
周期中出现最大值的位置。

#### 依赖关系

要启用此属性，请将 **Signal type** 设置为
`sawtooth`。

### **Samples per frame** — 每帧样本数 `512`（默认）| 正整数

每帧样本数，指定为正整数。

### **Sample rate (Hz)** — 生成波形的采样率 `44100`（默认）| 正标量

采样率必须大于 Frequency (Hz) 中指定值的两倍。

### **Output data type** — 生成波形的数据类型 `double`（默认）| `single`

生成波形的数据类型，指定为 `double` 或
`single`。

**可调：** 否

### **Simulate using** — 指定要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

- `Code generation` – 使用
  生成的 C 代码仿真模型。首次运行仿真时，Simulink® 会为该模块生成 C 代码。只要模型不变，C 代码就会在后续
  仿真中重用。此选项需要额外的
  启动时间，但后续仿真的速度与
  `Interpreted execution` 相当。
- `Interpreted execution` – 使用
  MATLAB® 解释器仿真模型。此选项可减少启动时间，并且仿真的
  速度与 `Code generation` 相当。在此模式下，
  您可以调试模块的源代码。

## 所属库

Audio Toolbox / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020a 中引入**

## 描述

生成正弦波、方波和锯齿波波形

Audio Oscillator 模块生成可调波形。典型用途
包括为测试平台生成测试信号，以及为音频效果生成控制信号。Audio Oscillator 模块的参数指定生成的
波形类型。

Audio Oscillator 模块使您能够调整波形的相位偏移、直流偏移、频率和幅值。
