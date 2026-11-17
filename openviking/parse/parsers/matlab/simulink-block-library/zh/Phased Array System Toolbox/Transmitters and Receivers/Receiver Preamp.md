---
type: simulink-block
title: 'Receiver Preamp'
family: 'transmitters-and-receivers'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Transmitters and Receivers'
documentation_page: 'receiverpreamp'
documentation_source_path: 'ref/receiverpreamp.html'
language: zh-CN
chinese_source: worker-translation
---

# Receiver Preamp

## 端口

### 输入

### **X** — 输入信号复值矩阵

输入信号，指定为复值矩阵。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，大小可能发生变化。

**数据类型：** `double`

### **TR** — 使能信号逻辑值标量 | 标量

使能信号，指定为列向量，其长度等于输入信号 `X` 的行数。
`TR` 的每个等于 `0` 或 `false` 的元素表示接收器关闭，没有输入信号通过接收器。
`TR` 的每个非零或 `true` 的元素表示接收器开启，输入信号通过。

#### 依赖项

要启用此端口，请选中 **启用使能信号输入** 复选框。

**数据类型：** `double` | `Boolean`

### **Ph** — 输入相位噪声标量

`X` 的每个输入采样点的相位噪声，指定为列向量，其长度等于 `X` 的行数。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，大小可能发生变化。

#### 依赖项

要启用此端口，请选中 **启用相位噪声输入** 复选框。

**数据类型：** `double`
### 输出

### **Out 1** — 输出复值矩阵

输出信号，以复值矩阵形式返回。

**数据类型：** `double`

## 参数

### **增益 (dB)** — 接收器增益 `20` (默认值)

指定一个标量，包含接收器前置放大器的增益，单位为 dB。

### **损耗因子 (dB)** — 接收器损耗因子 `0` (默认值)

指定一个标量，包含接收器前置放大器的损耗因子，单位为 dB。

### **噪声指定方法** — 噪声指定方法 `Noise temperature` (默认值) | `Noise power`

将接收器噪声指定为 `Noise power` 或 `Noise temperature`。

### **噪声功率 (W)** — 噪声功率 `0` (默认值)

指定一个标量，包含接收器前置放大器处的噪声功率，单位为瓦特。如果接收器有多个通道或传感器，则噪声带宽适用于每个通道或传感器。

#### 依赖项

仅当将 **噪声指定方法** 设置为 `Noise power` 时，此参数才会出现。

### **噪声系数 (dB)** — 接收器噪声系数 `0` (默认值)

指定一个标量，包含接收器前置放大器的噪声系数。单位为 dB。如果接收器有多个通道或传感器，则噪声系数适用于每个通道或传感器。仅当将 **噪声指定方法** 设置为 `Noise temperature` 时，此参数才会出现。

#### 依赖项

仅当将 **噪声指定方法** 设置为 `Noise temperature` 时，此参数才会出现。

### **参考温度 (K)** — 接收器参考温度 `290` (默认值)

一个标量，包含接收器前置放大器的参考温度，单位为开尔文。如果接收器有多个通道或传感器，则参考温度适用于每个通道或传感器。

#### 依赖项

仅当将 **噪声指定方法** 设置为 `Noise temperature` 时，此参数才会出现。

### **继承采样率** — 继承采样率 on (默认值) | off

选中此复选框以从上游模块继承采样率。否则，使用 **采样率** 参数指定采样率。

#### 依赖项

仅当将 **噪声指定方法** 设置为 `Noise temperature` 时，此参数才会出现。

### **采样率 (Hz)** — 信号采样率 `1e6` (默认值) | 正实值标量

将信号采样率指定为正标量。单位为 Hz。

#### 依赖项

要启用此参数，请清除 **继承采样率** 复选框。

**数据类型：** `double`

### **启用使能信号输入** — 添加输入以指定使能信号 off (默认值) | on

选中此复选框以允许通过输入端口 `TR` 输入接收器使能信号。T

#### 依赖项

仅当将 **噪声指定方法** 设置为 `Noise temperature` 时，此参数才会出现。

### **启用相位噪声输入** — 添加输入以指定相位噪声 off (默认值) | on

选中此复选框以允许使用输入端口 `Ph` 为每个输入采样点输入相位噪声。您可以使用此信息来模拟相干接收 (coherent-on-receive) 系统。

#### 依赖项

仅当将 **噪声指定方法** 设置为 `Noise temperature` 时，此参数才会出现。

### **仿真方式** — 模块仿真方法 `Interpreted Execution` (默认值) | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果要让模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果要让模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间编译，但通常运行更快。

解释执行在开发和调整模型时很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果您更改任何模块参数，则模块会在执行前自动重新编译。

此表显示 **仿真方式** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **仿真方式** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认值：** `Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Transmitters and Receivers

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

接收器前置放大器

Receiver Preamp 模块实现一个接收器前置放大器，它放大输入信号并添加热噪声。此外，您可以使用输入端口添加相位噪声。
