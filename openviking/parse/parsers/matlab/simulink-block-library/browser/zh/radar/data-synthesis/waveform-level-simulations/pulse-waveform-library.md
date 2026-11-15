---
type: simulink-block
title: 'Pulse Waveform Library'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: 'Data Synthesis / Waveform-Level Simulations'
documentation_page: 'pulsewaveformlibrary'
documentation_source_path: 'ref/pulsewaveformlibrary.html'
language: zh-CN
chinese_source: worker-translation
---

# Pulse Waveform Library

## 端口

### 输入

### **Idx** — 波形索引，正整数

用于选择波形的索引，指定为正整数。该索引从由 **Specification of each waveform in the library** 参数定义的波形集合中选择波形。

**数据类型：** `double`

### 输出

### **Y** — 脉冲波形采样，复值列向量 | 复值矩阵

脉冲波形采样，返回为复值向量或复值矩阵。

**数据类型：** `double`
**复数支持：** Yes

## 参数

### **Sample rate (Hz)** — 输出波形的采样率 `1e6`（默认） | 正标量

输出波形的采样率，指定为正标量。**Sample rate (Hz)** 与 **Pulse repetition frequency (Hz)** 向量中每个元素的比值必须为整数。该限制等同于要求脉冲重复间隔是采样间隔的整数倍。

### **Specification of each waveform in the library** — 库中的脉冲波形 `{{'Rectangular','PRF',1e4,'PulseWidth',50e-6},{'LinearFM','PRF',1e4,'PulseWidth',50e-6,'SweepBandwidth',1e5,'SweepDirection','Up','SweepInterval','Positive'}}`（默认） | 元胞数组

脉冲波形，指定为元胞数组。数组的每个元胞包含一个波形的规格。每个波形也是一个元胞数组，包含该波形的参数。

```
{{Waveform 1 Specification},{Waveform 2 Specification},{Waveform 3 Specification}, ...}
```

此模块支持四种内置波形，也允许您指定自定义波形。每个内置波形说明符由波形标识符后跟若干名称-值对组成，这些名称-值对用于设置波形的属性。

**内置波形**

|  |  |  |
| --- | --- | --- |
| 波形类型 | 波形标识符 | 波形名称-值对参数 |
| 线性 FM | `'LinearFM'` | 请参阅 Linear FM Waveform Arguments |
| 相位编码 | `'PhaseCoded'` | 请参阅 Phase-Coded Waveform Arguments |
| 矩形 | `'Rectangular'` | 请参阅 Rectangular Waveform Arguments |
| 步进 FM | `'SteppedFM'` | 请参阅 Stepped FM Waveform Arguments |

您可以使用用户定义函数创建自定义波形。该函数的第一个输入参数必须是采样率。在波形规格的第一个元胞中，使用函数句柄代替波形标识符。其余元胞包含除采样率之外的所有函数输入参数。按传递到函数的顺序指定所有输入参数。该函数必须至少有一个输出参数，以列向量形式返回每个脉冲的采样。仅当您将 **Simulate using** 设置为 `Interpreted Execution` 时，才能创建自定义波形。

### **Source of simulation sample time** — 仿真采样时间源 `Derive from waveform parameters`（默认） | `Inherit from Simulink engine`

仿真采样时间源，指定为 `Derive from waveform parameters` 或 `Inherit from Simulink engine`。当设置为 `Derive from waveform parameters` 时，该模块以由所选波形的 PRF 确定的可变速率运行。经过时间是可变的。当设置为 `Inherit from Simulink engine` 时，该模块以固定速率运行，因此经过时间是常量。

#### 依赖关系

要启用此参数，请选择 **Enable PRF selection input** 参数。

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认） | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果您希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果您希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

当您开发和调整模型时，解释执行很有用。该模块在 MATLAB 中运行基础 System object™。您可以快速更改并执行模型。当您对结果满意时，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行得更快。您可以在不重新编译的情况下重复执行，但如果更改任何模块参数，则该模块会在执行前自动重新编译。

下表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 该模块使用 MATLAB 解释器执行。 | 该模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 该模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

## 所属库

Radar Toolbox

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

脉冲波形库

Pulse Waveform Library 从波形库生成不同类型的脉冲波形。
