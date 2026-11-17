---
type: simulink-block
title: 'OVSF Code Generator'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Sources / Sequence Generators'
documentation_page: 'ovsfcodegenerator'
documentation_source_path: 'ref/ovsfcodegenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# OVSF Code Generator

## 端口
```yaml
ports:
- name: Out
  summary: 输出数据列向量
  direction: output
  data_types: double | int8
```

### 输出

### **Out** — 输出数据列向量

输出数据，返回为包含由一组正交码生成的 OVSF 码的二进制值列向量。

**数据类型：** `double` | `int8`
## 参数
```yaml
parameters:
- name: Code length
  summary: 码长度 64（默认）| 正整数
  group: ''
- name: Code index
  summary: OVSF 码矩阵的行索引 60（默认）| 整数
  group: ''
- name: Sample time
  summary: 采样时间，以秒为单位 1（默认）| 正标量
  group: ''
- name: Samples per frame
  summary: 输出的 OVSF 码片数量 1（默认）| 正整数
  group: ''
- name: Output data type
  summary: 输出类型 double（默认）| int8
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Code generation（默认）| Interpreted execution
  group: ''
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Code length** — 码长度 `64`（默认）| 正整数

生成的码的长度，指定为 2 的正整数次幂。码长度值是码的扩频因子。有关详细信息，请参阅 Spread Spectrum。

扩频因子是从 OVSF 码矩阵中选择的码的长度。OVSF 码定义为 *N*×*N* 矩阵 *C**N* 的行。**Code index** 参数将 *C*N 矩阵的行指定为感兴趣的码。有关详细信息，请参阅 Orthogonal Variable Spreading Factor Codes。

### **Code index** — OVSF 码矩阵的行索引 `60`（默认）| 整数

OVSF 码矩阵的行索引，指定为范围 [0, (*N* – 1)] 内的整数，其中 *N* 是由 **Code length** 参数值指定的扩频因子。OVSF 码定义为 *N*×*N* 矩阵 *C**N* 的行。此属性的值将 *C*N 矩阵的行指定为感兴趣的码。有关详细信息，请参阅 Recovering and Reconstructing OVSF Codes。

### **Sample time** — 采样时间，以秒为单位 `1`（默认）| 正标量

正标量指定输出信号每个采样之间的时间（以秒为单位）。如果将采样时间设置为 `-1`，则输出信号从下游继承采样时间。有关 **Sample time** 和 **Samples per frame** 参数之间关系的信息，请参阅 Sample Timing。

### **Samples per frame** — 输出的 OVSF 码片数量 `1`（默认）| 正整数

输出的 OVSF 码片数量，指定为正整数。每次模块运行时，它输出由 **Code length** 和 **Code index** 属性值指定的 OVSF 码的前 **Samples per frame** 个码片。有关详细信息，请参阅 Spread Spectrum。

有关 **Sample time** 和 **Samples per frame** 之间关系的信息，请参阅 Sample Timing。

### **Output data type** — 输出类型 `double`（默认）| `int8`

输出数据类型，指定为 `double` 或 `int8`。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 为模块生成 C 代码。除非模型发生变化，否则模型在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度快于 `Interpreted execution` 选项。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项缩短了启动时间，但后续仿真的速度慢于 `Code generation` 选项。在此模式下，您可以调试模块的源代码。

有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。
## 所属库

Communications Toolbox / Comm Sources / Sequence Generators

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `integer` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

### R2020a：现有模型自动将此模块更新到当前版本

从 R2020a 开始，Simulink 不再允许您使用 R2015b 之前可用的 OVSF Code Generator 模块版本。

现有模型会自动更新，以加载在 Source blocks output frames of contiguous time samples but do not use frame attribute 中宣布的 OVSF Code Generator 模块版本。有关模块转发的详细信息，请参阅 Maintain Compatibility of Library Blocks Using Forwarding Tables (Simulink)。

## 描述

生成 OVSF 码

OVSF Code Generator 模块从正交可变扩频因子（OVSF）矩阵生成码。使用 OVSF 码在扩频通信系统中保持不同信道之间的正交性。有关详细信息，请参阅 Algorithms。
