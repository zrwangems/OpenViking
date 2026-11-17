---
type: simulink-block
title: 'Barker Code Generator'
family: 'comm-sources'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Comm Sources / Sequence Generators'
documentation_page: 'barkercodegenerator'
documentation_source_path: 'ref/barkercodegenerator.html'
language: zh-CN
chinese_source: worker-translation
---

# Barker Code Generator

## 端口

### 输出

### **output** — Barker 码帧列向量

Barker 码帧，以列向量形式返回。如果帧长度超过 Barker 码长度，则该模块通过重复 Barker 码来填充帧。

#### 依赖项

使用 **Output data type** 参数设置输出的数据类型。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条上，在 **Simulation** 选项卡的 **Prepare** 库中，选择 **Property Inspector**。

### **Code length** — 生成码的长度 `7` (默认) | `1` | `2` | `3` | `4` | `5` | `11` | `13`

生成码的长度，指定为 `1`、
`2`、`3`、`4`、
`5`、`7`、`11` 或
`13`。有关详细信息，请参阅 Barker 码。

**示例：** `2` 输出 Barker 码
[–1;1]。

### **Sample time** — 输出采样时间 `1` (默认) | -1 | 正标量

正标量指定输出信号每个样本之间的时间，以 seconds 为单位。如果将采样时间设置为 `-1`，则输出
信号从下游继承采样时间。有关
**Sample time** 与 **Samples per frame** 参数之间关系的信息，
请参阅采样时序。

### **Samples per frame** — 每个输出帧的样本数 `1` (默认) | 正整数

每个输出帧的样本数，指定为正整数。如果
**Samples per frame** 为 *M*，则该
模块输出一个包含 *M* 个样本的帧，该帧由
长度为 *N* 的 Barker 码序列组成。*N* 是
所生成码的长度，由 **Code
length** 参数设置。当 *M* 不是 *N*
的整数倍时，连续帧在帧边界上保持
Barker 码的连续性。

有关 **Sample
time** 与 **Samples per frame** 参数之间关系的信息，请参阅采样时序。

### **Output data type** — 输出数据类型 `double` (默认) | `int8`

输出数据类型，指定为 `double` 或
`int8`。

### **Simulate using** — 要运行的仿真类型 `Code generation` (默认) | `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或
`Interpreted execution`。

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比使用 `Interpreted execution` 选项时更快。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但后续仿真的速度比使用 `Code generation` 选项时更慢。在此模式下，您可以调试模块的源代码。

有关详细信息，请参阅解释执行与代码生成 (Simulink)。

## 所属库

Communications Toolbox Communications Toolbox / Comm Sources / Sequence Generators

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `integer` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 不支持仅生成整数代码。

## 版本历史

**在 R2006a 之前引入**

### R2020a：现有模型会自动将此模块更新为当前版本

从 R2020a 开始，Simulink 不再允许您使用 R2015b 之前可用的 Barker Code Generator 模块版本。

现有模型会自动更新，以加载在 Source blocks output frames of contiguous time samples but do not use frame attribute 中宣布的 Barker Code Generator 模块版本。有关模块转发的详细信息，请参阅 Maintain Compatibility of Library Blocks Using Forwarding Tables (Simulink)。

## 描述

生成双极性 Barker 码

Barker Code Generator 模块生成双极性 Barker 码。较短的长度和低相关旁瓣使 Barker 码适用于数字通信系统中的帧同步。有关详细信息，请参阅 Barker 码。
