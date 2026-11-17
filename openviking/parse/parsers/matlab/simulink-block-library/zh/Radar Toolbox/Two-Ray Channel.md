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

**Specify atmospheric parameters**
:   选中此复选框以启用大气衰减建模。

**Temperature (degrees Celsius)**
:   环境大气温度，指定为实值标量。单位为摄氏度。当您选中 **Specify atmospheric parameters** 复选框时，此参数出现。单位为摄氏度。

**Dry air pressure (Pa)**
:   大气干空气压力，指定为正实值标量。单位为帕斯卡（Pa）。此属性的值 101325 对应一个标准大气压。当您选中 **Specify atmospheric parameters** 复选框时，此参数出现。

**Water vapour density (g/m^3)**
:   大气水蒸气密度，指定为正实值标量。单位为 gm/m3。当您选中 **Specify atmospheric parameters** 复选框时，此参数出现。

**Liquid water density (g/m^3)**
:   雾或云中的液态水密度，指定为非负实值标量。单位为 gm/m3。液态水密度的典型值为：中等雾 0.05，浓雾 0.5。当您选中 **Specify atmospheric parameters** 复选框时，此参数出现。

**Rain rate (mm/hr)**
:   降雨率，指定为非负实值标量。单位为 mm/hour。当您选中 **Specify atmospheric parameters** 复选框时，此参数出现。

**Inherit sample rate**
:   选中此复选框以从上游模块继承采样率。否则，使用 **Sample rate (Hz)** 参数指定采样率。

**Sample rate (Hz)**
:   将信号采样率（以赫兹为单位）指定为正标量。仅当未选中 **Inherit sample rate** 参数时，此参数才出现。

**Ground reflection coefficient**
:   入射信号幅度中反射到接收端的比例。

**Combine two rays at output**
:   选中此复选框以在输出端相干求和直接路径和反射路径信号。清除此复选框以保持两条射线分离。

**Maximum one-way propagation distance (m)**
:   信号源与目的地之间的最大距离，指定为正标量。单位为米。任何传播距离超过此距离的信号的幅度将被设置为零。

**Simulate using**
:   模块仿真方法，指定为 `Interpreted Execution` 或 `Code Generation`。如果您希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果您希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

    当您开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。当您对结果满意时，可以使用 `Code Generation` 运行模块。长时间仿真比解释执行运行更快。您可以重复执行而无需重新编译。但是，如果您更改任何模块参数，则模块会在执行前自动重新编译。

    设置此参数时，必须考虑整体模型仿真模式。下表显示了 **Simulate using** 参数如何与整体仿真模式交互。

    当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式会覆盖仿真模式。

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

双射线信道环境

Two-Ray Channel 模块通过直接路径和地面反射路径将窄带信号从空间中的一个点传播到多个点，或从多个点传播回一个点。该模块对传播时间、自由空间传播损耗和多普勒频移进行建模。该模块假设传播速度远大于物体速度，在这种情况下停走模型是有效的。
