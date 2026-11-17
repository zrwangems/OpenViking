---
type: simulink-block
title: 'Sample Rate Offset'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Impairments and Components'
documentation_page: 'samplerateoffset'
documentation_source_path: 'ref/samplerateoffset.html'
language: zh-CN
chinese_source: worker-translation
---

# Sample Rate Offset

## 端口

### 输入

### **In** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、*N*S 元素列向量或 *N*S×*N*C 矩阵。*N*S 是时间采样数。*N*C 是通道数。对于矩阵输入信号，采样率偏移独立应用于每一列。

**数据类型：** `double` | `single`
**复数支持：** 是
### 输出

### **Out** — 输出信号 标量 | 向量 | 矩阵

输出信号，以标量、向量或矩阵形式返回。此输出与输入信号具有相同的数据类型。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Sample rate offset** — 采样率偏移 10（默认）| 标量

采样率偏移，以百万分率（ppm）为单位，指定为大于 –1e6 的标量。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

要运行的仿真类型，指定为 `Interpreted execution` 或 `Code generation`。

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项需要较少的启动时间，但后续仿真的速度比 `Code generation` 选项慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比 `Interpreted execution` 选项快。

有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。

## 所属库

Communications Toolbox / RF Impairments and Components

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2022b 中引入**

## 描述

对输入信号应用采样率偏移

Sample Rate Offset 模块对输入信号应用采样率偏移。应用采样率偏移等效于改变 ADC 时钟速率。
