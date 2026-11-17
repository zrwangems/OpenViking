---
type: simulink-block
title: 'Transmitter'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Transmitters and Receivers'
documentation_page: 'transmitter'
documentation_source_path: 'ref/transmitter.html'
language: zh-CN
chinese_source: worker-translation
---

# Transmitter

## 端口

### 输入

### **Input 1** — 输入波形 复值矩阵

输入波形，指定为复值矩阵。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能会发生大小变化。

**数据类型：** `double`
### 输出

### **Y** — 发射波形 复值矩阵

发射信号，输出为复值矩阵。
`Y` 是经过放大的输入波形，其中放大基于发射机的特性，例如峰值功率和增益。

**数据类型：** `double`

### **TR** — 发射机开关状态 0 | 1

发射机开关状态，输出为 0 或 1。1 表示发射机开启，0 表示发射机关闭。

#### 依赖关系

要启用此端口，请选中 **Enable transmitter status output** 复选框。

**数据类型：** `double`

### **Ph** — 相位噪声 标量

相位噪声，输出为标量。

#### 依赖关系

要启用此端口，请选中 **Enable pulse phase noise output** 复选框。

**数据类型：** `double`

## 参数

#### 主

### **Peak power (W)** — 峰值功率 `5000`（默认）| 正标量

峰值功率，指定为正标量。单位为瓦特。

**数据类型：** `single` | `double`

### **Gain method** — 增益方法 `Linear`（默认）| `Cubic polynomial` | `Lookup table`

应用于发射信号的增益方法，指定为
`Linear`、`Cubic polynomial` 或 `Lookup table`。

- 设置为 `Linear` 时，应用线性增益。
- 设置为 `Cubic polynomial` 时，使用三次多项式模型应用非线性增益。
- 设置为 `Lookup table` 时，定义查找表以直接指定输出功率和相移作为输入功率的函数。

**数据类型：** `char` | `string`

### **Gain (dB)** — 线性发射机增益 `20`（默认）| 实标量 | 长度为 *N* 的实数值向量

线性发射机增益，指定为实标量或长度为 *N* 的实数值向量。*N* 是通道数。如果 **Gain (dB)** 参数是标量，则对所有通道应用相同的值。单位为 dB。

#### 依赖关系

要启用此属性，请将 **Gain method** 参数设置为 `Linear` 或 `Cubic polynomial`。

**数据类型：** `single` | `double`

### **Output IP3 (dBm)** — 输出 IP3 `Inf`（默认）| 标量 | 长度为 *N* 的实数值向量

输出 IP3，指定为标量或长度为 *N* 的实数值向量。*N* 是通道数。OIP3 表示发射机或接收机的非线性。OIP 也称为三阶截点。如果 OIP3 是标量，则对所有通道应用相同的值。有关 OIP3 的详细讨论，请参见 Nonlinearities and Noise in Idealized Baseband Amplifier Block (RF Blockset)。单位为 dBm。

#### 依赖关系

要启用此属性，请将 **Gain method** 参数设置为 `Cubic polynomial`。

**数据类型：** `single` | `double`

### **Lookup table** — 查找表 `[-25, 5, -1; -10, 20, -2; 0, 27, 5; 5, 28, 12]`（默认）| *M*×*N* 实值矩阵 | *M*×*N* 实值矩阵

AM/AM-AM/PM 查找表，指定为
3×*M*×*N* 实值数组。查找表指定放大器功率特性。*M*
是表项数，*N* 是通道数。表中的每一行表示输出功率或相位变化作为输入功率的函数关系。以
*[Pin(dBm),Pout(dBm),Phase
shift(degrees)]*×*M* 矩阵或
*[Pin(dBm),Pout(dBm),Phase
shift(degrees)]*×*M*×*N*
数组的形式指定 AM/AM（单位：dB/dB）和 AM/PM（单位：deg/dB）特性。使用该表对功率值进行线性插值或外推。第 1 列输入功率必须单调递增。表中必须至少有 3 行。功率输出可以写为：

uout=TAM−AM(|u|)eTAM−PM(|u|+∠u)

#### 依赖关系

要启用此属性，请将 **Gain method** 参数设置为 `Lookup table`。

**数据类型：** `single` | `double`

### **Loss factor (dB)** — 发射损耗因子 `0`（默认）| 非负标量 | 长度为 *N* 的非负值向量

发射损耗因子，指定为非负标量或长度为 *N* 的非负值向量。
*N* 是通道数。如果 **Loss factor (dB)** 参数是标量，则对所有通道应用相同的值。

#### 依赖关系

要启用此属性，请将 **Gain method** 参数设置为 `Linear`。

**数据类型：** `double` | `single`

### **Enable transmitter status output** — 启用发射机状态输出 off（默认）| on

选中此复选框可输出每个输出样本的发射机使用状态，从输出端口 **TR** 输出。

**数据类型：** `Boolean`

### **Preserve coherence among pulses** — 保持脉冲间相干性 on（默认）| off

选中此复选框可保持发射脉冲之间的相干性。

- 选中此复选框时，发射机不会向输出脉冲添加随机相位。
- 清除此复选框时，发射机向每个发射脉冲添加随机相位噪声。随机相位噪声通过将脉冲值乘以 *e<sup>jϕ</sup>* 引入，其中 *ϕ* 是区间 [0,2π] 上均匀分布的随机变量。

**数据类型：** `Boolean`

### **Enable pulse phase noise output** — 启用脉冲相位噪声输出 off（默认）| on

选中此复选框可创建一个输出端口 **Ph**，当 **Preserve coherence among pulses** 被清除时，该端口输出引入的随机相位噪声样本。该输出端口可连接到接收机以模拟相干接收系统。

#### 依赖关系

此复选框仅在未选中 **Preserve coherence among pulses** 时出现。

**数据类型：** `Boolean`

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间编译，但通常运行更快。

解释执行在开发和调优模型时非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。当对结果满意时，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，模块将在执行前自动重新编译。

下表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式会覆盖仿真模式。

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

#### 噪声

### **Add noise to input signal** — 向输入信号添加噪声 `off`（默认）| `on`

选中此复选框可在应用接收机效应之前向输入信号添加噪声。**Input noise temperature (K)** 参数决定所添加噪声的功率。**Sample rate (Hz)** 参数决定噪声带宽。

**示例：** `true`

**数据类型：** `Boolean`

### **Input noise temperature (K)** — 输入噪声温度 `290`（默认）| 正标量 | 长度为 *N* 的正值向量

输入噪声温度，指定为正标量或长度为 *N* 的正值向量，其中 *N* 是接收机通道数。如果 **Input noise temperature (K)** 参数是标量，则对所有通道应用相同的值。单位为开尔文度。

**示例：** `300`

#### 依赖关系

要启用此参数，请选中 **Input noise temperature (K)** 复选框。

**数据类型：** `single` | `double`

### **Noise method** — 噪声方法 `None` | `Noise figure` | `Noise factor` | `Noise temperature`

用于定义系统噪声的方法，指定为 `None`、`Noise figure`、`Noise factor` 或 `Noise temperature`。

- 当设置为 `None` 时，不应用噪声。
- 当设置为 `Noise figure` 时，**Noise figure (dB)** 参数决定噪声水平。
- 当设置为 `Noise temperature` 时，**Input noise temperature (K)** 参数决定噪声水平。
- 当设置为 `Noise factor` 时，**Noise factor** 参数决定噪声水平。

噪声带宽由输入信号采样率导出。

**示例：** `Noise figure`

**数据类型：** `char` | `string`

### **Noise figure (dB)** — 噪声系数 `3`（默认）| 实标量 | 长度为 *N* 的实值向量

接收机噪声系数，指定为实标量或长度为 *N* 的实值向量。*N* 是通道数。如果 **Noise figure (dB)** 是标量，则对所有通道应用相同的值。噪声是相对于由 **Reference temperature (K)** 参数定义的温度生成的。

#### 依赖关系

要启用此属性，请将 **Noise method** 参数设置为 `Noise figure`。

**数据类型：** `single` | `double`

### **Noise factor** — 噪声因子 `2`（默认）| 正标量 | 长度为 *N* 的正值向量

接收机噪声因子，指定为正标量或长度为 *N* 的正值向量。*N* 是通道数。如果 **Noise factor** 参数是标量，则对所有通道应用相同的值。噪声是相对于由 **Reference temperature (K)** 参数定义的温度生成的。

#### 依赖关系

要启用此属性，请将 **Noise method** 参数设置为 `Noise factor`。

**数据类型：** `single` | `double`

### **Reference temperature (K)** — 参考温度 `290`（默认）| 正标量 | 长度为 *N* 的正值向量

参考温度，指定为正标量或长度为 *N* 的正值向量。*N* 是通道数。如果 **Reference temperature (K)** 参数是标量，则对所有通道应用相同的值。

#### 依赖关系

要启用此属性，请将 **Noise method** 参数设置为 `Noise figure` 或 `Noise factor`。

**数据类型：** `single` | `double`

### **Sample rate (Hz)** — 采样率 `1e6`（默认）| 正标量

输入信号的采样率，指定为正标量。使用此参数向信号添加噪声。**Sample rate (Hz)** 参数仅用于导出信号的噪声带宽。

#### 依赖关系

要启用此属性，请选中 **Add noise to input signal** 复选框，或将 **Noise method** 参数设置为 `Noise figure`、`Noise factor` 或 `Noise temperature`。

**数据类型：** `single` | `double`

### **Inherit sample rate** — 从上游模块继承采样率 开（默认）| 关

选择此参数以从上游模块继承采样率。否则，使用 **Sample rate (Hz)** 参数指定采样率。

**数据类型：** `Boolean`

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

在开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object。您可以快速更改并执行模型。当对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，模块将在执行前自动重新编译。

下表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

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
| **值：** `Interpreted Execution`、`Code Generation` |
| **默认：** `Interpreted Execution` |

#### PhaseOffset

### **Phased offset (degrees)** — 相位偏移 `0`（默认）| 标量 | 长度为 *N* 的实数向量

相位偏移，指定为实数标量或长度为 *N* 的实数向量。*N* 是通道数。如果 **Phase offset (degrees)** 是标量，则对所有通道应用相同的值。单位为度。

**数据类型：** `single` | `double`

#### Randomization

### **Source of seed for random number generator** — 随机数生成器种子的来源 `Auto`（默认）| `Property`

随机数生成器种子的来源，指定为 `Auto` 或 `Property`。当来源为 `Auto` 时，种子自动生成。当来源为 `Property` 时，使用 **Seed for random number generator** 参数设置种子。

**示例：** `Property`

**数据类型：** `char` | `string`

### **Seed for random number generator** — 随机数生成器的种子 0（默认）| 正整数

随机数生成器的种子，指定为正整数。

**数据类型：** `single` | `double`

## 所属库

Phased Array System Toolbox / Transmitters and Receivers

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

放大并发射信号

Transmitter 模块放大并发射波形脉冲。发射机可以保持脉冲之间的相干性，也可以插入相位噪声。
