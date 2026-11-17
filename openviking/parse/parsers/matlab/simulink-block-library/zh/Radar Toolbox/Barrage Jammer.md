---
type: simulink-block
title: 'Barrage Jammer'
family: 'radar'
product_id: 'radar'
product_name: 'Radar Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'barragejammer'
documentation_source_path: 'ref/barragejammer.html'
language: zh-CN
chinese_source: worker-translation
---

# Barrage Jammer

## 端口
```yaml
ports: []
```

**注意**

模块的输入和输出端口对应于底层 System object 的 `step` 方法中描述的输入和输出参数。请参阅本页底部的链接。

| 端口 | 描述 | 支持的数据类型 |
| --- | --- | --- |
| `Ref` | 参考信号输入 | 双精度浮点 |
| `Out` | 干扰机输出 | 双精度浮点 |
## 参数
```yaml
parameters: []
```

**Effective radiated power (W)**
:   以正标量形式指定干扰信号的有效辐射功率（ERP），单位为瓦特。

**Source of number of samples per frame**
:   将每帧采样数的来源指定为 `Property` 或 `Derive from reference input port`。当选择 `Property` 时，模块从 **Number of samples per frame** 参数获取采样数。当选择 `Derive from reference input port` 时，模块使用传入 `Ref` 输入端口的参考信号的采样数。

**Number of samples per frame**
:   以正整数形式指定干扰信号输出中的采样数。采样数必须与信号源产生的采样数匹配。此参数仅在 **Source of number of samples per frame** 设置为 `Property` 时显示。例如，如果您使用 Rectangular Waveform 模块作为信号源，并将其 **Output signal format** 设置为 `Samples`，则 **Number of samples per frame** 的值应与 Rectangular Waveform 模块的 **Number of samples in output** 参数匹配。如果将 **Output signal format** 设置为 `Pulses`，则 **Number of samples per frame** 应等于 **Sample rate** 与 **Number of pulses in output** 的乘积除以 **Pulse repetition frequency**。

**Simulate using**
:   模块仿真方法，指定为 `Interpreted Execution` 或 `Code Generation`。如果您希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果您希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

    解释执行在开发和调整模型时非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意时，可以使用 `Code Generation` 运行模块。长时间仿真比解释执行运行更快。您可以重复执行而无需重新编译。但是，如果您更改任何模块参数，模块将在执行前自动重新编译。

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

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021a 中引入**

## 描述

Barrage jammer interference source

Barrage Jammer 模块生成宽带类噪声干扰信号。
