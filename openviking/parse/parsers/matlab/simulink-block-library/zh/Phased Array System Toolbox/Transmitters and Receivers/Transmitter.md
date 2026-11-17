---
type: simulink-block
title: 'Transmitter'
family: 'transmitters-and-receivers'
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

### **Input 1** — 输入波形复值矩阵

输入波形，指定为复值矩阵。

输入矩阵第一维的大小可以变化，以模拟变化的信号长度。例如，在具有可变脉冲重复频率的脉冲波形情况下，可能会发生大小变化。

**数据类型：** `double`

### 输出

### **Y** — 发射波形复值矩阵

发射信号，输出为复值矩阵。`Y` 是放大后的输入波形，其中放大基于发射机的特性，例如峰值功率和增益。

**数据类型：** `double`

### **TR** — 发射机开-关状态 0 | 1

发射机开-关状态，输出为 0 或 1。1 表示发射机开启，0 表示发射机关闭。

#### 依赖关系

要启用此端口，请选中 **启用发射机状态输出** 复选框。

**数据类型：** `double`

### **Ph** — 相位噪声标量

相位噪声，输出为标量。

#### 依赖关系

要启用此端口，请选中 **启用脉冲相位噪声输出** 复选框。

**数据类型：** `double`

## 参数

#### 主要

### **峰值功率 (W)** — 峰值功率 `5000` (默认) | 正标量

峰值功率，指定为正标量。单位为 W。

**数据类型：** `single` | `double`

### **增益方法** — 增益方法 `Linear` (默认) | `Cubic polynomial` | `Lookup table`

向发射信号应用增益的方法，指定为 `Linear`、`Cubic polynomial` 或 `Lookup table`。

- 设置为 `Linear` 时，应用线性增益。
- 设置为 `Cubic polynomial` 时，使用三次多项式模型应用非线性增益。
- 设置为 `Lookup table` 时，定义查找表以直接指定输出功率和相移与输入功率的函数关系。

**数据类型：** `char` | `string`

### **增益 (dB)** — 线性发射机增益 `20` (默认) | 实标量 | 长度为 *N* 的实数值向量

线性发射机增益，指定为实标量或长度为 *N* 的实数值向量。*N* 是通道数。如果 **增益 (dB)** 参数是标量，则同一值应用于所有通道。单位为 dB。

#### 依赖关系

要启用此属性，请将 **增益方法** 参数设置为 `Linear` 或 `Cubic polynomial`。

**数据类型：** `single` | `double`

### **输出 IP3 (dBm)** — 输出 IP3 `Inf` (默认) | 标量 | 长度为 *N* 的实数值向量

输出 IP3，指定为标量或长度为 *N* 的实数值向量。*N* 是通道数。OIP3 表示发射机或接收机的非线性。OIP 也称为三阶截取点。如果 OIP3 是标量，则同一值应用于所有通道。有关 OIP3 的详细讨论，请参阅 Nonlinearities and Noise in Idealized Baseband Amplifier Block (RF Blockset)。单位为 dBm。

#### 依赖关系

要启用此属性，请将 **增益方法** 参数设置为 `Cubic polynomial`。

**数据类型：** `single` | `double`

### **查找表** — 查找表 `[-25, 5, -1; -10, 20, -2; 0, 27, 5; 5, 28, 12]` (默认) | *M*-by-*N* 实值矩阵 | *M*-by-*N* 实值矩阵

AM/AM-AM/PM 查找表，指定为 3-by-*M*-by-*N* 实值数组。查找表指定放大器功率特性。*M* 是表项数，*N* 是通道数。表中的每一行表示输出功率或相位变化与输入功率的函数关系。在 *[Pin(dBm),Pout(dBm),Phase shift(degrees)]*-by-*M* 矩阵或 *[Pin(dBm),Pout(dBm),Phase shift(degrees)]*-by-*M*-by-*N* 数组中指定 AM/AM（dB/dB）和 AM/PM（deg/dB）特性。使用该表对功率值进行线性插值或外插。第 1 列输入功率必须单调递增。表中必须至少有 3 行。功率输出可写为：

uout=TAM−AM(|u|)eTAM−PM(|u|+∠u)

#### 依赖关系

要启用此属性，请将 **增益方法** 参数设置为 `Lookup table`。

**数据类型：** `single` | `double`

### **损耗因子 (dB)** — 发射损耗因子 `0` (默认) | 非负标量 | 长度为 *N* 的非负值向量

发射损耗因子，指定为非负标量或长度为 *N* 的非负值向量。*N* 是通道数。如果 **损耗因子 (dB)** 参数是标量，则同一值应用于所有通道。

#### 依赖关系

要启用此属性，请将 **增益方法** 参数设置为 `Linear`。

**数据类型：** `double` | `single`

### **启用发射机状态输出** — 启用发射机状态输出 off (默认) | on

选中此复选框以从输出端口 **TR** 输出每个输出样本的发射机使用状态。

**数据类型：** `Boolean`

### **保持脉冲间的相干性** — 保持脉冲间的相干性 on (默认) | off

选中此复选框以保持发射脉冲之间的相干性。

- 选中此复选框时，发射机不会向输出脉冲添加随机相位。
- 清除此复选框时，发射机会向每个发射脉冲添加随机相位噪声。随机相位噪声通过将脉冲值乘以 *ejϕ* 引入，其中 *ϕ* 是区间 [0,2π] 上均匀分布的随机变量。

**数据类型：** `Boolean`

### **启用脉冲相位噪声输出** — 启用脉冲相位噪声输出 off (默认) | on

选中此复选框以创建输出端口 **Ph**，如果清除了 **保持脉冲间的相干性**，则输出引入的样本随机相位噪声。该输出端口可连接到接收机以模拟相干接收系统。

#### 依赖关系

仅当未选中 **保持脉冲间的相干性** 时，此复选框才会出现。

**数据类型：** `Boolean`

### **仿真方式** — 模块仿真方法 `Interpreted Execution` (默认) | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间编译，但通常运行更快。

当您在开发和调优模型时，解释执行很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，则模块会在执行前自动重新编译。

此表显示 **仿真方式** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **仿真方式** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认值：** `Interpreted Execution` |

#### 噪声

### **向输入信号添加噪声** — 向输入信号添加噪声 `off` (默认) | `on`

选中此复选框以在应用接收机效应之前向输入信号添加噪声。**输入噪声温度 (K)** 参数确定所添加噪声的功率。**采样率 (Hz)** 参数确定噪声带宽。

**示例：**
`true`

**数据类型：** `Boolean`

### **输入噪声温度 (K)** — 输入噪声温度 `290` (默认) | 正标量 | 长度为 *N* 的正值向量

输入噪声温度，指定为正标量或长度为 *N* 的正值向量，其中 *N* 是接收机通道数。如果 **输入噪声温度 (K)** 参数是标量，则同一值应用于所有通道。单位为 Kelvin degrees。

**示例：** `300`

#### 依赖关系

要启用此参数，请选中 **输入噪声温度 (K)** 复选框。

**数据类型：** `single` | `double`

### **噪声方法** — 噪声方法 `None` | `Noise figure` | `Noise factor` | `Noise temperature`

定义系统噪声的方法，指定为 `None`、`Noise figure`、`Noise factor` 或 `Noise temperature`。

- 设置为 `None` 时，不应用噪声。
- 设置为 `Noise figure` 时，**噪声系数 (dB)** 参数确定噪声水平。
- 设置为 `Noise temperature` 时，**输入噪声温度 (K)** 参数确定噪声水平。
- 设置为 `Noise factor` 时，**噪声因子** 参数确定噪声水平。

噪声带宽根据输入信号采样率推导得出。

**示例：** `Noise figure`

**数据类型：** `char` | `string`

### **噪声系数 (dB)** — 噪声系数 `3` (默认) | 实标量 | 长度为 *N* 的实数值向量

接收机噪声系数，指定为实标量或长度为 *N* 的实数值向量。*N* 是通道数。如果 **噪声系数 (dB)** 是标量，则同一值应用于所有通道。噪声是相对于 **参考温度 (K)** 参数定义的温度生成的。

#### 依赖关系

要启用此属性，请将 **噪声方法** 参数设置为 `Noise figure`。

**数据类型：** `single` | `double`

### **噪声因子** — 噪声因子 `2` (默认) | 正标量 | 长度为 *N* 的正值向量

接收机噪声因子，指定为正标量或长度为 *N* 的正值向量。*N* 是通道数。如果 **噪声因子** 参数是标量，则同一值应用于所有通道。噪声是相对于 **参考温度 (K)** 参数定义的温度生成的。

#### 依赖关系

要启用此属性，请将 **噪声方法** 参数设置为 `Noise factor`。

**数据类型：** `single` | `double`

### **参考温度 (K)** — 参考温度 `290` (默认) | 正标量 | 长度为 *N* 的正值向量

参考温度，指定为正标量或长度为 *N* 的正值向量。*N* 是通道数。如果 **参考温度 (K)** 参数是标量，则同一值应用于所有通道。

#### 依赖关系

要启用此属性，请将 **噪声方法** 参数设置为 `Noise figure` 或 `Noise factor`。

**数据类型：** `single` | `double`

### **采样率 (Hz)** — 采样率 `1e6` (默认) | 正标量

输入信号的采样率，指定为正标量。使用此参数向信号添加噪声。**采样率 (Hz)** 参数仅用于推导信号的噪声带宽。

#### 依赖关系

要启用此属性，请选中 **向输入信号添加噪声** 复选框，或将 **噪声方法** 参数设置为 `Noise figure`、`Noise factor` 或 `Noise temperature`。

**数据类型：** `single` | `double`

### **继承采样率** — 从上游模块继承采样率 on (默认) | off

选择此参数以从上游模块继承采样率。否则，使用 **采样率 (Hz)** 参数指定采样率。

**数据类型：** `Boolean`

### **仿真方式** — 模块仿真方法 `Interpreted Execution` (默认) | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间编译，但通常运行更快。

当您在开发和调优模型时，解释执行很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，则模块会在执行前自动重新编译。

此表显示 **仿真方式** 参数如何影响整体仿真行为。

当 Simulink 模型处于 `Accelerator` 模式时，使用 **仿真方式** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认值：** `Interpreted Execution` |

#### PhaseOffset

### **相位偏移 (degrees)** — 相位偏移 `0` (默认) | 标量 | 长度为 *N* 的实数值向量

相位偏移，指定为实标量或长度为 *N* 的实数值向量。*N* 是通道数。如果 **相位偏移 (degrees)** 是标量，则同一值应用于所有通道。单位为 degrees。

**数据类型：** `single` | `double`

#### 随机化

### **随机数生成器种子的来源** — 随机数生成器种子的来源 `Auto` (默认) | `Property`

随机数生成器种子的来源，指定为 `Auto` 或 `Property`。当来源为 `Auto` 时，种子自动生成。当来源为 `Property` 时，使用 **随机数生成器的种子** 参数设置种子。

**示例：** `Property`

**数据类型：** `char` | `string`

### **随机数生成器的种子** — 随机数生成器的种子 0 (默认) | 正整数

随机生成器的种子，指定为正整数。

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

Transmitter 模块放大并发射波形脉冲。发射机可以在脉冲之间保持相干性，或者插入相位噪声。
