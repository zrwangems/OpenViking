---
type: simulink-block
title: 'Bernoulli Binary Generator'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Sources / Random Data Sources'
documentation_page: 'bernoullibinarygenerator'
documentation_source_path: 'ref/bernoullibinarygenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Bernoulli Binary Generator

## 端口

### 输出

### **Out** — 输出数据信号 标量 | 向量 | 矩阵

输出数据信号，以标量、向量或矩阵形式返回。

**数据类型：** `double`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Probability of zero** — 输出端生成零的概率 `0.5`（默认）| [0, 1] 范围内的标量 | [0, 1] 范围内的标量向量

Probability of zero 必须在 [0, 1] 范围内。**Probability of zero** 参数中的元素个数对应于模块输出的独立通道数。参数为 *p* 的伯努利分布以概率 *p* 产生零，以概率 *1-p* 产生一。

### **Source of initial seed** — 随机数生成器的初始种子来源 `Auto`（默认）| `Parameter`

随机数生成器的初始种子来源，指定为以下之一：

- `Auto` —— 模块使用全局随机数流。如果使用 `parsim` (Simulink) 函数，请参阅提示。
- `Parameter` —— 模块将随机数生成器种子设置为 **Initial seed**。

有关详细信息，请参阅 Managing the Global Stream Using RandStream and Random Number Generators。

### **Initial seed** — 随机数生成器的初始种子 非负整数

随机数生成器的初始种子值，指定为非负整数。如果此参数为常量，则生成的序列是可重复的。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Source of initial seed** 设置为 `Parameter`。

### **Sample time** — 输出信号的采样时间 `1`（默认）| -1 | 正标量

正标量指定输出信号每个采样之间的时间（以秒为单位）。如果将采样时间设置为 `-1`，则输出信号从下游继承采样时间。有关 **Sample time** 和 **Samples per frame** 参数之间关系的信息，请参阅 Sample Timing。

### **Samples per frame** — 输出信号的每帧采样数 `1`（默认）| 正标量

输出信号一个通道中的每帧采样数，指定为正整数。有关 **Sample time** 和 **Samples per frame** 之间关系的信息，请参阅 Sample Timing。

### **Output data type** — 输出信号的数据类型 `double`（默认）| `single` | `uint8` | `uint16` | `uint32` | `boolean`

输出数据类型，指定为 `double`、`single`、`uint8`、`uint16`、`uint32` 或 `boolean`。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度快于 `Interpreted execution` 选项。
- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但后续仿真的速度慢于 `Code generation` 选项。在此模式下，您可以调试模块的源代码。

有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。

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

Bernoulli Binary Generator 模块的随机数流处理更新移除了一些限制。在此更新之前，某些操作模式会导致模块在每次运行仿真时生成相同的数字。此更改移除了针对这些操作模式所注明的限制。

### R2024a：种子值必须为整数

Bernoulli Binary Generator 模块要求 **Seed** 参数为非负整数值。

### R2024a：R2015b Bernoulli Binary Generator 模块版本不再自动更新

从 R2024a 开始，包含尚未从 R2015b 版本更新的 Bernoulli Binary Generator 模块的模型，需要替换为当前版本的 Bernoulli Binary Generator 模块。

### R2020a：Upgrade Advisor 中支持 Bernoulli Binary Generator 模块更新

从 R2020a 开始，Bernoulli Binary Generator 模块允许您使用 Upgrade Advisor。您可以更新到 R2015b 中宣布的模块版本，或保留 R2015b 之前可用的模块版本。

- 使用 Upgrade Advisor 更新包含 Bernoulli Binary Generator 模块的现有模型。
- 随机数生成器的行为已更改。统计特性得到改进。有关详细信息，请参阅 Source blocks output frames of contiguous time samples but do not use frame attribute。

## 描述

生成伯努利分布的随机二进制数

Bernoulli Binary Generator 模块使用伯努利分布生成随机二进制数。使用此模块生成随机数据比特，以仿真数字通信系统并获取误码率等性能指标。参数为 *p* 的伯努利分布以概率 *p* 产生零，以概率 *1-p* 产生一。伯努利分布的均值为 *1-p*，方差为 *p*(*1-p*)。**Probability of zero** 参数指定 *p*，可以是 [0, 1] 范围内的任意实数。

输出信号可以是列向量或行向量、二维矩阵或标量。输出信号中的行数对应于一个帧中的采样数，由 **Samples per frame** 参数设置。输出信号中的列数对应于通道数，由 **Probability of zero** 参数中的元素个数设置。有关更多详细信息，请参阅 Sinks。
