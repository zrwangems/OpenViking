---
type: simulink-block
title: 'Pulse Waveform Library'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'pulsewaveformlibrary'
documentation_source_path: 'ref/pulsewaveformlibrary.html'
language: zh-CN
chinese_source: worker-translation
---

# Pulse Waveform Library

## 端口
```yaml
ports:
- name: Idx
  summary: 波形索引 正整数
  direction: input
  data_types: double
- name: Y
  summary: 脉冲波形采样 复值列向量 | 复值矩阵
  direction: output
  data_types: double
```

### 输入

### **Idx** — 波形索引 正整数

用于选择波形的索引，指定为正整数。该索引从 **Specification of each waveform in the library** 参数所定义的波形集合中选择波形。

**数据类型：** `double`
### 输出

### **Y** — 脉冲波形采样 复值列向量 | 复值矩阵

脉冲波形采样，以复值向量或复值矩阵形式返回。

**数据类型：** `double`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Sample rate (Hz)
  summary: 输出波形的采样率 1e6（默认）| 正标量
  group: ''
- name: Specification of each waveform in the library
  summary: 库中的脉冲波形 {{'Rectangular','PRF',1e4,'PulseWidth',50e-6},{'LinearFM','PRF',1e4,'PulseWidth',50e-6,'SweepBandwidth',1e5,'SweepDirection','Up','SweepInterval','Positive'}}（默认）|
    元胞数组
  group: ''
- name: Source of simulation sample time
  summary: 仿真采样时间来源 Derive from waveform parameters（默认）| Inherit from Simulink engine
  group: ''
- name: Simulate using
  summary: 模块仿真方法 Interpreted Execution（默认）| Code Generation
  group: ''
```

### **Sample rate (Hz)** — 输出波形的采样率 `1e6`（默认）| 正标量

输出波形的采样率，指定为正标量。**Sample rate (Hz)** 与 **Pulse repetition frequency (Hz)** 向量中每个元素的比值必须为整数。此限制等价于要求脉冲重复间隔为采样间隔的整数倍。

### **Specification of each waveform in the library** — 库中的脉冲波形 `{{'Rectangular','PRF',1e4,'PulseWidth',50e-6},{'LinearFM','PRF',1e4,'PulseWidth',50e-6,'SweepBandwidth',1e5,'SweepDirection','Up','SweepInterval','Positive'}}`（默认）| 元胞数组

脉冲波形，指定为元胞数组。数组的每个元胞包含一个波形的规格。每个波形也是一个包含该波形参数的元胞数组。

```
{{Waveform 1 Specification},{Waveform 2 Specification},{Waveform 3 Specification}, ...}
```

此模块支持四种内置波形，也允许您指定自定义波形。每个内置波形说明符由一个波形标识符后跟若干名称-值对组成，用于设置波形的属性。

**内置波形**

|  |  |  |
| --- | --- | --- |
| 波形类型 | 波形标识符 | 波形名称-值对参数 |
| Linear FM | `'LinearFM'` | 参见 Linear FM Waveform Arguments |
| Phase coded | `'PhaseCoded'` | 参见 Phase-Coded Waveform Arguments |
| Rectangular | `'Rectangular'` | 参见 Rectangular Waveform Arguments |
| Stepped FM | `'SteppedFM'` | 参见 Stepped FM Waveform Arguments |

您可以使用用户自定义函数创建自定义波形。该函数的第一个输入参数必须是采样率。在波形规格的第一个元胞中使用函数句柄代替波形标识符。其余元胞包含除采样率之外的所有函数输入参数。按照传入函数的顺序指定所有输入参数。该函数必须至少有一个输出参数，以列向量形式返回每个脉冲的采样。仅当您将 **Simulate using** 设置为 `Interpreted Execution` 时，才能创建自定义波形。

### **Source of simulation sample time** — 仿真采样时间来源 `Derive from waveform parameters`（默认）| `Inherit from Simulink engine`

仿真采样时间来源，指定为 `Derive from waveform parameters` 或 `Inherit from Simulink engine`。当设置为 `Derive from waveform parameters` 时，模块以由所选波形的 PRF 决定的可变速率运行。经过时间是可变的。当设置为 `Inherit from Simulink engine` 时，模块以固定速率运行，因此经过时间是常量。

#### 依赖关系

要启用此参数，请选择 **Enable PRF selection input** 参数。

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code
Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

当您开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意时，可以使用 `Code
Generation` 运行模块。长时间仿真使用生成代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果您更改任何模块参数，模块将在执行前自动重新编译。

下表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。
## 所属库

Radar Toolbox

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

脉冲波形库

Pulse Waveform Library 从波形库中生成不同类型的脉冲波形。
