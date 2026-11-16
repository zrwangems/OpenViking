---
type: simulink-block
title: 'Wideband Free Space'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Waveform Design and Signal Synthesis / Signal Propagation and Targets'
documentation_page: 'widebandfreespace'
documentation_source_path: 'ref/widebandfreespace.html'
language: zh-CN
chinese_source: worker-translation
---

# Wideband Free Space

## 端口

**注意**

模块的输入和输出端口对应于底层 System object 的 `step` 方法中描述的输入和输出参数。请参阅本页底部的链接。

| 端口 | 描述 | 支持的数据类型 |
| --- | --- | --- |
| `X` | 输入信号。 | Double-precision floating point |
| `Pos1` | 信号源位置。 | Double-precision floating point |
| `Pos2` | 信号目标位置。 | Double-precision floating point |
| `Vel1` | 信号源速度。 | Double-precision floating point |
| `Vel2` | 信号目标速度。 | Double-precision floating point |
| `Out` | 传播后的信号。 | Double-precision floating point |

## 参数

**信号传播速度 (m/s)**
:   将信号的传播速度指定为正标量，单位为米每秒。您可以使用 `physconst` 函数指定光速。

**信号载波频率 (Hz)**
:   将窄带信号的载波频率指定为正标量，单位为赫兹。

**子带数量**
:   用于子带处理的子带数量，指定为正整数。

**执行双向传播**
:   选中此复选框可执行起点与终点之间的往返传播。否则，模块执行从起点到终点的单向传播。

**继承采样率**
:   选中此复选框可从上游模块继承采样率。否则，使用 **采样率 (Hz)** 参数指定采样率。

**采样率 (Hz)**
:   将信号采样率指定为正标量，单位为赫兹。仅当未选中 **继承采样率** 参数时，才会显示此参数。

**最大单向传播距离 (m)**
:   起点与终点之间的最大距离，指定为正标量，单位为米。传播距离超过此距离的任何信号，其幅值都将设置为零。

**仿真方式**
:   模块仿真方法，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要一定的编译时间，但通常运行速度更快。

    解释执行在开发和调整模型时很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真的运行速度比采用解释执行时更快。无需重新编译即可重复执行。但是，如果更改任何模块参数，模块会在执行前自动重新编译。

    设置此参数时，必须考虑模型的整体仿真模式。下表显示了 **仿真方式** 参数与整体仿真模式的交互方式。

    当 Simulink® 模型处于 `Accelerator` 模式时，使用 **仿真方式** 指定的模块模式会覆盖仿真模式。

    **加速模式**

    |  |  |  |  |
    | --- | --- | --- | --- |
    | 模块仿真 | 仿真行为 | | |
    | `Normal` | `Accelerator` | `Rapid Accelerator` |
    | `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 根据模型创建独立可执行文件。 |
    | `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

    有关详细信息，请参阅选择仿真模式 (Simulink)。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

R2025b 中未提供文档。

## 版本历史

**在 R2015b 中推出**

## 描述

宽带自由空间环境

Wideband Free Space Channel 模块将信号从空间中的一个点传播到另一个点。该模块对传播时间、自由空间传播损耗和多普勒频移进行建模。该模块假设传播速度远大于目标或阵列的速度，在这种情况下，stop-and-hop 模型有效。

当信号在自由空间中传播到物体并返回时，您可以选择使用单个模块计算双向自由空间传播延迟，或者使用两个模块分别计算每个方向上的单向传播延迟。由于自由空间传播延迟不一定是采样间隔的整数倍，因此，使用双向传播模块时的总往返延迟（以采样数计）可能不同于使用两个单向传播模块时的延迟（以采样数计）。因此，建议在可能的情况下使用单个双向传播模块。
