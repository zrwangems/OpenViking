---
type: simulink-block
title: 'Random Integer Generator'
family: 'comm-sources'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Sources / Random Data Sources'
documentation_page: 'randomintegergenerator'
documentation_source_path: 'ref/randomintegergenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Random Integer Generator

## 端口

### 输出

### **Out** — 随机整数输出 标量 | 向量 | 矩阵

随机整数输出，以标量、向量或矩阵形式返回。此端口在模块上未命名。数据类型使用 Output data type 参数设置。

输出数据的行数等于 Samples per frame 参数的值，并对应于一个帧中的样本数。输出数据的列数等于 Set size 参数中元素的数量，并对应于通道数。

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上的 **准备** 库中，选择 **属性检查器**。

### **Set size** — Set size `8`（默认）| 正整数 | 正整数的行向量

Set size，*M*，指定为正整数或正整数的行向量。该模块生成范围 [0, (*M* – 1)] 内的整数。**Set size** 中的元素数量对应于模块输出的独立通道数。

- 如果 **Set size** 是标量，则所有输出随机变量都是独立同分布（i.i.d.）的。
- 如果 **Set size** 是向量，则向量的长度决定输出通道数。各通道可以具有不同的输出范围。

### **Source of initial seed** — Source of initial seed `Auto`（默认）| `Parameter`

用于随机数生成器的初始种子的来源，指定为以下之一：

- `Auto` —— 该模块使用全局随机数流。如果使用 `parsim` (Simulink) 函数，请参阅提示。
- `Parameter` —— 该模块将随机数生成器种子设置为 **Initial seed**。

有关详细信息，请参阅使用 RandStream 和随机数生成器管理全局流。

### **Initial seed** — 初始种子值 `0`（默认）| 非负整数

用于随机数生成器的初始种子值，指定为非负整数。如果 **Initial seed** 参数是常量，则结果序列可重复。

**可调：** Yes

#### 依赖项

要启用此参数，请将 **Source of initial seed** 参数设置为 `Parameter`。

### **Sample time** — Sample time `1`（默认）| -1 | 正标量

正标量指定输出信号每个采样之间的时间（以秒为单位）。如果将采样时间设置为 `-1`，输出信号将从下游继承采样时间。有关 **Sample time** 和 **Samples per frame** 参数之间关系的信息，请参阅采样时序。

### **Samples per frame** — Samples per frame `1`（默认）| 正整数

每帧样本数，指定为正整数，表示输出数据一个通道中每帧的样本数。有关 **Sample time** 和 **Samples per frame** 之间关系的信息，请参阅采样时序。

### **Output data type** — Output data type `double`（默认）| `single` | `uint8` | `uint16` | `uint32` | `boolean`

输出数据类型，指定为 `double`、`single`、`uint8`、`uint16`、`uint32` 或 `boolean`。如果将此参数设置为 `boolean`，则必须将 Set size 参数设置为 `2`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

要运行的仿真类型，指定为 `Interpreted execution` 或 `Code generation`。

- `Interpreted execution` —— 使用 MATLAB® 解释器对模型进行仿真。此选项需要较少的启动时间，但后续仿真的速度比使用 `Code generation` 选项慢。在此模式下，可以调试模块的源代码。
- `Code generation` —— 使用生成的 C 代码对模型进行仿真。首次运行仿真时，Simulink 会为模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比使用 `Interpreted execution` 选项快。

有关详细信息，请参阅解释执行与代码生成 (Simulink)。

## 所属库

Communications Toolbox / Comm Sources / Random Data Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

### R2024a：随机数流处理更新

对 Random Integer Generator 模块的随机数流处理进行了更新，消除了一些限制。在此更新之前，某些运行模式会导致该模块在每次运行仿真时生成相同的数字。此更改消除了针对这些运行模式所注明的限制。

### R2024a：种子值必须为整数

Random Integer Generator 模块要求 **Seed** 参数为非负整数值。

### R2024a：R2015b Random Integer Generator 模块版本不再自动更新

从 R2024a 开始，包含尚未从 R2015b 版本更新的 Random Integer Generator 模块的模型，需要替换为当前版本的 Random Integer Generator 模块。

### R2020a：Upgrade Advisor 中支持 Random Integer Generator 模块更新

从 R2020a 开始，Random Integer Generator 模块允许使用 Upgrade Advisor。您可以更新到 R2015b 中宣布的模块版本，或保留 R2015b 之前可用的模块版本。

- 使用 Upgrade Advisor 更新包含 Random Integer Generator 模块的现有模型。
- 随机数生成器的行为已更改。统计信息得到改进。有关详细信息，请参阅源模块输出连续时间样本的帧但不使用帧属性。

## 描述

生成在指定范围内随机分布的整数

Random Integer Generator 模块生成范围 [0, *M*-1] 内均匀分布的随机整数，其中 *M* 由 **Set size** 参数指定。使用此模块生成随机二进制值或整数值数据。
