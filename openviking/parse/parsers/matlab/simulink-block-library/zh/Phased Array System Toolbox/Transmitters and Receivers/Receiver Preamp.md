---
type: simulink-block
title: 'Receiver Preamp'
family: 'phased'
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
```yaml
ports:
- name: X
  summary: 输入信号 复值矩阵
  direction: input
  data_types: double
- name: TR
  summary: 启用使能信号 逻辑值标量 | 标量
  direction: input
  data_types: double | Boolean
- name: Ph
  summary: 输入相位噪声 标量
  direction: input
  data_types: double
- name: Out 1
  summary: 输出 复值矩阵
  direction: output
  data_types: double
```

### 输入

### **X** — 输入信号 复值矩阵

输入信号，指定为复值矩阵。

输入矩阵第一维的大小可以变化，以模拟信号长度的变化。例如，在脉冲重复频率可变的脉冲波形情况下，可能会发生大小变化。

**数据类型：** `double`

### **TR** — 启用使能信号 逻辑值标量 | 标量

启用使能信号，指定为列向量，其长度等于输入信号 `X` 的行数。
`TR` 中每个等于
`0` 或 `false` 的元素表示接收机已关闭，没有输入信号通过接收机。
`TR` 中每个非零或
`true` 的元素表示接收机已开启，
输入信号通过。

#### 依赖关系

要启用此端口，请选中 **Enable enabling signal
input** 复选框。

**数据类型：** `double` | `Boolean`

### **Ph** — 输入相位噪声 标量

`X` 的每个输入样本的相位噪声，指定为列向量，其长度等于
`X` 的行数。

输入矩阵第一维的大小可以变化，以模拟信号长度的变化。例如，在脉冲重复频率可变的脉冲波形情况下，可能会发生大小变化。

#### 依赖关系

要启用此端口，请选中 **Enable phase noise
input** 复选框。

**数据类型：** `double`
### 输出

### **Out 1** — 输出 复值矩阵

输出信号，以复值矩阵形式返回。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Gain (dB)
  summary: 接收机增益 20（默认值）
  group: ''
- name: Loss factor (dB)
  summary: 接收机损耗因子 0（默认值）
  group: ''
- name: Noise specification method
  summary: 噪声指定方法 Noise temperature（默认值）| Noise power
  group: ''
- name: Noise power (W)
  summary: 噪声功率 0（默认值）
  group: ''
- name: Noise figure (dB)
  summary: 接收机噪声系数 0（默认值）
  group: ''
- name: Reference temperature (K)
  summary: 接收机参考温度 290（默认值）
  group: ''
- name: Inherit sample rate
  summary: 继承采样率 开启（默认值）| 关闭
  group: ''
- name: Sample rate (Hz)
  summary: 信号采样率 1e6（默认值）| 正实值标量
  group: ''
- name: Enable enabling signal input
  summary: 添加输入以指定使能信号 关（默认）| 开
  group: ''
- name: Enable phase noise input
  summary: 添加输入以指定相位噪声 关（默认）| 开
  group: ''
- name: Simulate using
  summary: 模块仿真方法 Interpreted Execution（默认）| Code Generation
  group: ''
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution、Code Generation
```

### **Gain (dB)** — 接收机增益 `20`（默认值）

指定一个标量，包含接收机前置放大器的增益，单位为 dB。

### **Loss factor (dB)** — 接收机损耗因子 `0`（默认值）

指定一个标量，包含接收机前置放大器的损耗因子，单位为 dB。

### **Noise specification method** — 噪声指定方法 `Noise temperature`（默认值）| `Noise power`

将接收机噪声指定为 `Noise power` 或
`Noise temperature`。

### **Noise power (W)** — 噪声功率 `0`（默认值）

指定一个标量，包含接收机前置放大器处的噪声功率，单位为瓦特。如果接收机具有多个通道或传感器，则噪声带宽适用于每个通道或传感器。

#### 依赖关系

仅当将 **Noise specification
method** 设置为 `Noise power` 时，此参数才会显示。

### **Noise figure (dB)** — 接收机噪声系数 `0`（默认值）

指定一个标量，包含接收机前置放大器的噪声系数。
单位为 dB。如果接收机具有多个通道或传感器，则噪声系数适用于每个通道或传感器。仅当将 **Noise specification method** 设置为
`Noise temperature` 时，此参数才会显示。

#### 依赖关系

仅当将 **Noise specification
method** 设置为 `Noise
temperature` 时，此参数才会显示。

### **Reference temperature (K)** — 接收机参考温度 `290`（默认值）

一个标量，包含接收机前置放大器的参考温度，单位为开尔文。如果接收机具有多个通道或传感器，则参考温度适用于每个通道或传感器。

#### 依赖关系

仅当将 **Noise specification
method** 设置为 `Noise
temperature` 时，此参数才会显示。

### **Inherit sample rate** — 继承采样率 开启（默认值）| 关闭

选中此复选框可从上游模块继承采样率。
否则，使用 **Sample
rate** 参数指定采样率。

#### 依赖关系

仅当将 **Noise specification
method** 设置为 `Noise
temperature` 时，此参数才会显示。

### **Sample rate (Hz)** — 信号采样率 `1e6`（默认值）| 正实值标量

将信号采样率指定为正标量。单位为 Hz。

#### 依赖关系

要启用此参数，请清除 **Inherit sample rate** 复选框。

**数据类型：** `double`

### **Enable enabling signal input** — 添加输入以指定使能信号 关（默认）| 开

选中此复选框可通过输入端口 `TR` 输入接收机使能信号。T

#### 依赖关系

此参数仅在将 **Noise specification method** 设置为 `Noise temperature` 时出现。

### **Enable phase noise input** — 添加输入以指定相位噪声 关（默认）| 开

选中此复选框可通过输入端口 `Ph` 为每个输入样本输入相位噪声。您可以使用此信息来模拟相干接收系统。

#### 依赖关系

此参数仅在将 **Noise specification method** 设置为 `Noise temperature` 时出现。

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果您希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果您希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

当您在开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果您更改任何模块参数，模块将在执行前自动重新编译。

下表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块被编译。 |

有关更多信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`、`Code Generation` |
| **默认：** `Interpreted Execution` |
## 所属库

Phased Array System Toolbox / Transmitters and Receivers

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

接收机前置放大器

Receiver Preamp 模块实现了一个接收机前置放大器，用于放大输入信号并添加热噪声。此外，您还可以使用输入端口添加相位噪声。
