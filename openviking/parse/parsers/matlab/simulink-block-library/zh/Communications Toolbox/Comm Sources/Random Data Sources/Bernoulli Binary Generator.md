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

要以交互方式编辑模块参数，请使用 **属性检查器**。在 Simulink® Toolstrip 的 **仿真** 选项卡上的 **准备** 库中，选择 **属性检查器**。

### **零的概率** — 在输出端生成零的概率 `0.5`（默认值） | [0, 1] 范围内的标量 | [0, 1] 范围内的标量向量

**零的概率** 必须在 [0, 1] 范围内。**零的概率** 参数中的元素数对应于模块输出的独立通道数。参数为 *p* 的伯努利分布以概率 *p* 生成零，并以概率 *1-p* 生成一。

### **初始种子的来源** — 随机数生成器的初始种子来源 `Auto`（默认值） | `Parameter`

随机数生成器的初始种子来源，指定为以下之一：

- `Auto` –– 模块使用全局随机数流。如果您使用 `parsim` (Simulink) 函数，请参阅提示。
- `Parameter` –– 模块将随机数生成器种子设置为 **初始种子**。

有关详细信息，请参阅使用 RandStream 和随机数生成器管理全局流。

### **初始种子** — 随机数生成器的初始种子 非负整数

随机数生成器的初始种子值，指定为非负整数。如果此参数为常量，则生成的序列可重复。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **初始种子的来源** 设置为 `Parameter`。

### **采样时间** — 输出信号的采样时间 `1`（默认值） | -1 | 正标量

正标量指定输出信号每个样本之间的时间（以 seconds 为单位）。如果将采样时间设置为 `-1`，则输出信号从下游继承采样时间。有关 **采样时间** 和 **每帧样本数** 参数之间关系的信息，请参阅采样时序。

### **每帧样本数** — 输出信号的每帧样本数 `1`（默认值） | 正标量

输出信号一个通道中的每帧样本数，指定为正整数。有关 **采样时间** 和 **每帧样本数** 之间关系的信息，请参阅采样时序。

### **输出数据类型** — 输出信号的数据类型 `double`（默认值） | `single` | `uint8` | `uint16` | `uint32` | `boolean`

输出数据类型，指定为 `double`、`single`、`uint8`、`uint16`、`uint32` 或 `boolean`。

### **模拟使用** — 要运行的仿真类型 `Code generation`（默认值） | `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 通过使用生成的 C 代码来仿真模型。第一次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比使用 `Interpreted execution` 选项更快。
- `Interpreted execution` — 通过使用 MATLAB® 解释器来仿真模型。此选项可缩短启动时间，但后续仿真的速度比使用 `Code generation` 选项更慢。在此模式下，您可以调试模块的源代码。

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

### R2024a: 随机数流处理更新

对 Bernoulli Binary Generator 模块的随机数流处理进行的更新移除了一些限制。在此更新之前，某些运行模式会导致该模块在每次运行仿真时生成相同的数字。此更改移除了针对这些运行模式所指出的限制。

### R2024a: 种子值必须为整数

Bernoulli Binary Generator 模块要求 **Seed** 参数使用非负整数值。

### R2024a: R2015b Bernoulli Binary Generator 模块版本不再自动更新

从 R2024a 开始，包含尚未从 R2015b 版本更新的 Bernoulli Binary Generator 模块的模型，需要替换为当前 Bernoulli Binary Generator 模块版本。

### R2020a: Upgrade Advisor 中支持 Bernoulli Binary Generator 模块更新

从 R2020a 开始，Bernoulli Binary Generator 模块允许您使用 Upgrade Advisor。您可以更新为 R2015b 中宣布的模块版本，或保留 R2015b 之前可用的模块版本。

- 使用 Upgrade Advisor 更新包含 Bernoulli Binary Generator 模块的现有模型。
- 随机数生成器的行为已更改。统计特性得到改进。有关详细信息，请参阅源模块输出连续时间样本的帧，但不使用帧属性。

## 描述

生成伯努利分布的随机二进制数

Bernoulli Binary Generator 模块使用伯努利分布生成随机二进制数。使用此模块生成随机数据位，以仿真数字通信系统并获得性能指标，例如误码率。参数为 *p* 的伯努利分布以概率 *p* 生成零，并以概率 *1-p* 生成一。伯努利分布的均值为 *1-p*，方差为 *p*(*1-p*)。**零的概率** 参数指定 *p*，并且可以是 [0, 1] 范围内的任何实数。

输出信号可以是列向量或行向量、二维矩阵或标量。输出信号中的行数对应于一个帧中的样本数，并由 **每帧样本数** 参数设置。输出信号中的列数对应于通道数，并由 **零的概率** 参数中的元素数设置。有关更多详细信息，请参阅接收器。
