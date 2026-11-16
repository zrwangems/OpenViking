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

### 输出

### **Out** — 输出数据列向量

输出数据，返回为二进制值列向量，其中包含从一组正交码生成的 OVSF 码。

**数据类型：** `double` | `int8`

## 参数

要交互式编辑模块参数，请使用 Property Inspector。从 Simulink® Toolstrip 中，在 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### **Code length** — 代码长度 `64`（默认值）| 正整数

生成的码的长度，指定为 2 的正整数次幂。Code length 值是码的扩频因子。有关详细信息，请参阅扩频。

扩频因子是从 OVSF 码矩阵中选择的码的长度。OVSF 码定义为 *N*×*N* 矩阵 *C**N* 的行。**Code index** 参数将 *C*N 矩阵的该行指定为目标码。有关详细信息，请参阅正交可变扩频因子码。

### **Code index** — OVSF 码矩阵的行索引 `60`（默认值）| 整数

OVSF 码矩阵的行索引，指定为范围 [0, (*N* – 1)] 内的整数，其中 *N* 是由 **Code length** 参数的值指定的扩频因子。OVSF 码定义为 *N*×*N* 矩阵 *C**N* 的行。此属性的值将 *C*N 矩阵的该行指定为目标码。有关详细信息，请参阅恢复和重构 OVSF 码。

### **Sample time** — 采样时间，以 seconds 为单位 `1`（默认值）| 正标量

正标量指定输出信号每个采样之间的时间，以 seconds 为单位。如果将采样时间设置为 `-1`，则输出信号从下游继承采样时间。有关 **Sample time** 和 **Samples per frame** 参数之间关系的信息，请参阅采样定时。

### **Samples per frame** — 输出的 OVSF 码片数 `1`（默认值）| 正整数

输出的 OVSF 码片数，指定为正整数。每次模块运行时，它会输出由 **Code length** 和 **Code index** 属性值指定的 OVSF 码的前 **Samples per frame** 个码片。有关详细信息，请参阅扩频。

有关 **Sample time** 和 **Samples per frame** 之间关系的信息，请参阅采样定时。

### **Output data type** — 输出类型 `double`（默认值）| `int8`

输出数据类型，指定为 `double` 或 `int8`。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认值）| `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 通过使用生成的 C 代码来仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度快于 `Interpreted execution` 选项。
- `Interpreted execution` — 通过使用 MATLAB® 解释器来仿真模型。此选项可缩短启动时间，但后续仿真的速度慢于 `Code generation` 选项。在此模式下，您可以调试模块的源代码。

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

### R2020a：现有模型自动将此模块更新为当前版本

从 R2020a 开始，Simulink 不再允许您使用 R2015b 之前可用的 OVSF Code Generator 模块版本。

现有模型会自动更新，以加载在“源模块输出连续时间采样的帧，但不使用帧属性”中宣布的 OVSF Code Generator 模块版本。有关模块转发的详细信息，请参阅使用转发表维护库模块的兼容性 (Simulink)。

## 描述

生成 OVSF 码

OVSF Code Generator 模块从正交可变扩频因子 (OVSF) 矩阵生成一个码。使用 OVSF 码可保持扩频通信系统中不同信道之间的正交性。有关详细信息，请参阅算法。
