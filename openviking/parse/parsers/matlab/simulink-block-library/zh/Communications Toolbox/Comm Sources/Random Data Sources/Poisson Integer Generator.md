---
type: simulink-block
title: 'Poisson Integer Generator'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Sources / Random Data Sources'
documentation_page: 'poissonintegergenerator'
documentation_source_path: 'ref/poissonintegergenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Poisson Integer Generator

## 端口

### 输出

### **Out** — 随机整数输出 标量 | 向量 | 矩阵

随机整数输出，返回为标量、向量或矩阵。此端口在模块上未命名。使用 **输出数据类型** 参数设置数据类型。

- 输出数据中的行数对应于一个帧中的样本数，并等于 **每帧样本数** 参数的值。
- 输出信号中的列数对应于通道数，并等于 **泊松参数(Lambda)** 参数中的元素数。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条中，在 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

### **泊松参数(Lambda)** — 泊松参数 λ `0.1`（默认）| 正标量 | 正标量向量

泊松参数 λ，指定为正标量或正标量值的行向量。

- 如果将此参数设置为标量值，则输出向量中的每个元素共享同一个泊松参数。
- 如果将此参数设置为行向量，则元素数对应于该模块输出的独立通道数。

### **初始种子的来源** — 随机数生成器的初始种子来源 `Auto`（默认）| `Parameter`

随机数生成器的初始种子来源，指定为以下之一：

- `Auto` –– 该模块使用全局随机数流。如果使用 `parsim` (Simulink) 函数，请参阅提示。
- `Parameter` –– 该模块将随机数生成器种子设置为 **初始种子**。

有关详细信息，请参阅使用 RandStream 和随机数生成器管理全局流。

### **初始种子** — 随机数生成器的初始种子 非负整数

随机数生成器的初始种子值，指定为非负整数。如果此参数为常量，则生成的序列可重复。

**可调：** Yes

#### 依赖关系

要启用此参数，请将 **初始种子的来源** 设置为 `Parameter`。

### **采样时间** — 输出信号的采样时间 `1`（默认）| -1 | 正标量

正标量指定输出信号每两个样本之间的时间，以秒为单位。如果将采样时间设置为 `-1`，则输出信号将从下游继承采样时间。有关 **采样时间** 和 **每帧样本数** 参数之间关系的信息，请参阅采样时序。

### **每帧样本数** — 输出信号的每帧样本数 `1`（默认）| 正标量

输出信号一个通道中的每帧样本数，指定为正整数。有关 **采样时间** 和 **每帧样本数** 之间关系的信息，请参阅采样时序。

### **输出数据类型** — 输出信号的数据类型 `double`（默认）| `uint8` | `uint16` | `uint32` | `boolean`

输出数据类型，指定为 `double`、`uint8`、`uint16`、`uint32` 或 `boolean`。

### **仿真方式** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 通过使用生成的 C 代码来仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度快于使用 `Interpreted execution` 选项时。
- `Interpreted execution` — 通过使用 MATLAB® 解释器来仿真模型。此选项可缩短启动时间，但后续仿真的速度慢于使用 `Code generation` 选项时。在此模式下，可以调试模块的源代码。

有关详细信息，请参阅解释执行与代码生成 (Simulink)。

## 所属库

Communications Toolbox / Comm Sources / Random Data Sources

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

### R2024a：随机数流处理更新

对 Poisson Integer Generator 模块的随机数流处理进行的更新移除了一些限制。在此更新之前，某些运行模式会导致该模块每次运行仿真时生成相同的数字。此更改移除了针对这些运行模式指出的限制。

### R2024a：种子值必须为整数

Poisson Integer Generator 模块要求 **Seed** 参数为非负整数值。

### R2020a：现有模型自动将此模块更新为当前版本

从 R2020a 开始，Simulink 不再允许使用 R2015b 之前可用的 Poisson Integer Generator 模块版本。

- 现有模型会自动更新，以加载 R2015b 中宣布的 Poisson Integer Generator 模块版本。有关模块转发的详细信息，请参阅使用转发表保持库模块的兼容性 (Simulink)。
- 随机数生成器的行为已更改。统计信息得到了改进。有关详细信息，请参阅源模块输出连续时间样本的帧，但不使用帧属性。

## 描述

生成泊松分布的随机整数

Poisson Integer Generator 模块使用泊松分布生成随机整数。生成非负整数 *k* 的概率为 λkexp(−λ)/(k!)，其中 λ 是称为*泊松参数*的正数。

当使用此模块在二进制传输信道中生成噪声时，**泊松参数(Lambda)** 参数的典型值远小于 1。
