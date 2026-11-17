---
type: simulink-block
title: 'Barrage Jammer'
family: 'radar-toolbox'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: 'Radar Toolbox'
documentation_page: 'barragejammer'
documentation_source_path: 'ref/barragejammer.html'
language: zh-CN
chinese_source: worker-translation
---

# Barrage Jammer

## 端口

**注意**

模块的输入和输出端口对应于底层 System object 的 `step` 方法中描述的输入和输出参数。请参阅本页底部的链接。

| 端口 | 描述 | 支持的数据类型 |
| --- | --- | --- |
| `Ref` | 参考信号输入 | Double-precision floating point |
| `Out` | 干扰机输出 | Double-precision floating point |

## 参数

**有效辐射功率 (W)**
:   将干扰信号的有效辐射功率 (ERP) 指定为正标量，其数值以 watts 表示。

**每帧采样点数的来源**
:   将每帧采样点数的来源指定为 `Property` 或 `Derive from reference input port`。选择 `Property` 时，模块从 **每帧采样点数** 参数获取采样点数。选择 `Derive from reference input port` 时，模块使用传入 `Ref` 输入端口的参考信号的采样点数。

**每帧采样点数**
:   将干扰信号输出中的采样点数指定为正整数。采样点数必须与信号源生成的采样点数一致。仅当 **每帧采样点数的来源** 设置为 `Property` 时，才会显示此参数。例如，如果使用 Rectangular Waveform 模块作为信号源，并将其 **输出信号格式** 设置为 `Samples`，则 **每帧采样点数** 的值应与 Rectangular Waveform 模块的 **输出中的采样点数** 参数一致。如果将 **输出信号格式** 设置为 `Pulses`，则 **每帧采样点数** 应等于 **采样率** 与 **输出中的脉冲数** 的乘积除以 **脉冲重复频率** 所得的值。

**仿真方式**
:   模块仿真方法，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要一定的编译时间，但通常运行速度更快。

    在开发和调优模型时，解释执行很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。对结果满意后，即可使用 `Code Generation` 运行模块。与解释执行相比，长时间仿真的运行速度更快。您无需重新编译即可重复执行。但是，如果更改任何模块参数，模块会在执行前自动重新编译。

    设置此参数时，必须考虑模型的整体仿真模式。下表显示了 **仿真方式** 参数与整体仿真模式的交互方式。

    当 Simulink® 模型处于 `Accelerator` 模式时，通过 **仿真方式** 指定的模块模式将覆盖仿真模式。

    **加速模式**

    |  |  |  |  |
    | --- | --- | --- | --- |
    | 模块仿真 | 仿真行为 | | |
    | `Normal` | `Accelerator` | `Rapid Accelerator` |
    | `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 根据模型创建独立可执行文件。 |
    | `Code Generation` | 编译模块。 | 编译模型中的所有模块。 |

    有关详细信息，请参阅选择仿真模式 (Simulink)。

## 所属库

在 R2025b 中未提供文档。

## 模块特性

在 R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中推出**

## 描述

阻塞式干扰机干扰源

Barrage Jammer 模块生成类似噪声的宽带干扰信号。
