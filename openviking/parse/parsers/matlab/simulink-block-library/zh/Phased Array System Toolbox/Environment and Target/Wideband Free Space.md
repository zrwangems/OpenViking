---
type: simulink-block
title: 'Wideband Free Space'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Environment and Target'
documentation_page: 'widebandfreespace'
documentation_source_path: 'ref/widebandfreespace.html'
language: zh-CN
chinese_source: worker-translation
---

# Wideband Free Space

## 端口
```yaml
ports: []
```

**注意**

模块输入和输出端口对应于底层 System object 的 `step` 方法中描述的输入和输出参数。请参阅本页底部的链接。

| 端口 | 描述 | 支持的数据类型 |
| --- | --- | --- |
| `X` | 输入信号。 | 双精度浮点 |
| `Pos1` | 信号源位置。 | 双精度浮点 |
| `Pos2` | 信号目的地位置。 | 双精度浮点 |
| `Vel1` | 信号源速度。 | 双精度浮点 |
| `Vel2` | 信号目的地速度。 | 双精度浮点 |
| `Out` | 传播后的信号。 | 双精度浮点 |
## 参数
```yaml
parameters: []
```

**Signal Propagation speed (m/s)**
:   将信号的传播速度指定为正标量，单位为米每秒。您可以使用函数 `physconst` 来指定光速。

**Signal carrier frequency (Hz)**
:   将窄带信号的载波频率指定为正标量，单位为赫兹。

**Number of subbands**
:   用于子带处理的子带数量，指定为正整数。

**Perform two-way propagation**
:   选中此复选框可在起点和目的地之间执行往返传播。否则，模块执行从起点到目的地的单向传播。

**Inherit sample rate**
:   选中此复选框可从上游模块继承采样率。否则，使用 **Sample rate (Hz)** 参数指定采样率。

**Sample rate (Hz)**
:   将信号采样率（以赫兹为单位）指定为正标量。此参数仅在未选中 **Inherit sample rate** 参数时显示。

**Maximum one-way propagation distance (m)**
:   起点和目的地之间的最大距离（以米为单位），指定为正标量。传播距离超过此值的任何信号的幅度将被设置为零。

**Simulate using**
:   模块仿真方法，指定为 `Interpreted Execution` 或 `Code Generation`。如果您希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果您希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

    当您在开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。当您对结果满意时，可以使用 `Code Generation` 运行模块。长时间仿真比解释执行运行更快。您可以重复执行而无需重新编译。但是，如果您更改任何模块参数，模块将在执行前自动重新编译。

    设置此参数时，必须考虑整体模型仿真模式。下表显示了 **Simulate using** 参数与整体仿真模式的交互方式。

    当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

    **加速模式**

    |  |  |  |  |
    | --- | --- | --- | --- |
    | 模块仿真 | 仿真行为 | | |
    | `Normal` | `Accelerator` | `Rapid Accelerator` |
    | `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
    | `Code Generation` | 模块被编译。 | 模型中的所有模块被编译。 |

    有关更多信息，请参阅 Choosing a Simulation Mode (Simulink)。
## 所属库

R2025b 中未记录。

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2015b 中引入**

## 描述

宽带自由空间环境

宽带自由空间信道模块将信号从空间中的一点传播到另一点。该模块对传播时间、自由空间传播损耗和多普勒频移进行建模。该模块假设传播速度远大于目标或阵列速度，在这种情况下停跳模型成立。

当信号在自由空间中传播到物体并返回时，您可以选择使用单个模块来计算双程自由空间传播延迟，或使用两个模块在每个方向上执行单程传播延迟。由于自由空间传播延迟不一定是采样间隔的整数倍，因此当您使用双程传播模块时，以采样点为单位的总往返延迟可能与您使用两个单程传播模块时的以采样点为单位的延迟不同。因此，建议在可能的情况下使用单个双程传播模块。
