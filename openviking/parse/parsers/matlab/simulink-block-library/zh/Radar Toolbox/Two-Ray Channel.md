---
type: simulink-block
title: 'Two-Ray Channel'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'tworaychannel'
documentation_source_path: 'ref/tworaychannel.html'
language: zh-CN
chinese_source: worker-translation
---

# Two-Ray Channel

## 端口

**注意**

模块的输入和输出端口对应于底层 System object 的 `step` 方法中描述的输入和输出参数。请参阅本页面底部的链接。

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
:   将信号的传播速度指定为正标量，单位为 meters per second。可以使用函数 `physconst` 指定光速。

**信号载波频率 (Hz)**
:   将窄带信号的载波频率指定为正标量，单位为 hertz。

**指定大气参数**
:   选中此复选框可启用大气衰减建模。

**温度 (degrees Celsius)**
:   环境大气温度，指定为实值标量。单位为 degrees Celsius。选中 **指定大气参数** 复选框时，会显示此参数。单位为 degrees Celsius。

**干空气压力 (Pa)**
:   大气干空气压力，指定为正实值标量。单位为 Pascals (Pa)。此属性的值 101325 对应于一个标准大气压。选中 **指定大气参数** 复选框时，会显示此参数。

**水蒸气密度 (g/m^3)**
:   大气水蒸气密度，指定为正实值标量。单位为 gm/m3。选中 **指定大气参数** 复选框时，会显示此参数。

**液态水密度 (g/m^3)**
:   雾或云的液态水密度，指定为非负实值标量。单位为 gm/m3。液态水密度的典型值：中等浓度的雾为 0.05，浓雾为 0.5。选中 **指定大气参数** 复选框时，会显示此参数。

**降雨速率 (mm/hr)**
:   降雨速率，指定为非负实值标量。单位为 mm/hour。选中 **指定大气参数** 复选框时，会显示此参数。

**继承采样率**
:   选中此复选框可从上游模块继承采样率。否则，使用 **采样率 (Hz)** 参数指定采样率。

**采样率 (Hz)**
:   将信号采样率（以 hertz 为单位）指定为正标量。仅当未选中 **继承采样率** 参数时，才会显示此参数。

**地面反射系数**
:   入射信号幅度中朝向接收机反射的部分所占的比例。

**在输出端合并两条射线**
:   选中此复选框可在输出端对直接路径和反射路径信号进行相干求和。清除此复选框可使两条射线保持分离。

**最大单程传播距离 (m)**
:   信号起点与目的地之间的最大距离，指定为正标量。单位为 meters。任何传播距离超过此距离的信号，其幅度都将设置为零。

**仿真方式**
:   模块仿真方法，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间来编译，但通常运行速度更快。

    解释执行在开发和调优模型时非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真的运行速度比解释执行时更快。无需重新编译即可重复运行。但是，如果更改任何模块参数，模块会在执行前自动重新编译。

    设置此参数时，必须考虑整体模型仿真模式。下表列出了 **仿真方式** 参数与整体仿真模式的交互方式。

    当 Simulink® 模型处于 `Accelerator` 模式时，使用 **仿真方式** 指定的模块模式会覆盖仿真模式。

    **加速模式**

    |  |  |  |  |
    | --- | --- | --- | --- |
    | 模块仿真 | 仿真行为 | | |
    | `Normal` | `Accelerator` | `Rapid Accelerator` |
    | `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 根据模型创建独立可执行文件。 |
    | `Code Generation` | 模块已编译。 | 模型中的所有模块均已编译。 |

    有关详细信息，请参阅选择仿真模式 (Simulink)。

## 所属库

R2025b 中未提供文档。

## 模块特性

R2025b 中未提供文档。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

双射线信道环境

Two-Ray Channel 模块通过直接路径和地面反射路径，将窄带信号从空间中的一个点传播到多个点，或从多个点传播回一个点。该模块对传播时间、自由空间传播损耗和多普勒频移进行建模。该模块假设传播速度远大于物体的速度，此时停走模型有效。
