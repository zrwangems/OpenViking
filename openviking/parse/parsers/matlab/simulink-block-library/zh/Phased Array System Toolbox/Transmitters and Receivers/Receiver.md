---
type: simulink-block
title: 'Receiver'
family: 'transmitters-and-receivers'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Transmitters and Receivers'
documentation_page: 'receiverblock'
documentation_source_path: 'ref/receiverblock.html'
language: zh-CN
chinese_source: worker-translation
---

# Receiver

## 端口

### 输入

### **X** — 接收信号 复值向量 | 复值矩阵

接收信号电压，输入为复值向量或复值矩阵。行数等于样本数。

如果 **X** 是向量，则 **Y** 的行数等于 `X` 的行数。**Y** 的列数等于接收机中的通道数。

在 **X** 是向量的情况下，通道数由指示通道号的主动参数确定，例如 **Noise figure (dB)**、**Reference temperature (K)**、**Gain (dB)** 和 **Phase offset (degrees)**。

接收机效应按固定顺序应用于信号，尽管某些效应可以省略。效应用于输入信号的顺序为：

- 当选中 **Add noise to input signal** 复选框时，添加输入噪声。
- 根据 **Noise method** 参数中指定的方法添加系统噪声。
- 根据 **Gain method** 参数中指定的方法应用信号增益。
- 根据 **Phase offset (degrees)** 参数向信号添加相位偏移。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **EN** — 使能信号 实值向量（默认）| 实值矩阵 | 逻辑值向量 | 逻辑值矩阵

使能信号，输入为实值向量或矩阵，或逻辑值向量或矩阵。

- 如果 **EN** 是向量，则其行数必须与端口 **X** 中的输入信号矩阵的行数相同。然后，**EN** 每一行中的值应用于 **X** 的所有列。
- 如果 **EN** 是矩阵，则 **EN** 必须与 **X** 大小相同，并且 **EN** 中的每个元素应用于 **X** 中的对应元素。

如果 **EN** 的类型为 single 或 double，当 **EN** 的某个元素为零时，接收机关闭，输入信号设置为零。当 **EN** 的元素非零时，接收机开启，输入通过接收机。

如果 **EN** 为逻辑类型，则每当 **EN** 的某个元素为 `true` 时接收机启用，并且每当 **EN** 的某个元素为 `false` 时接收机禁用。

#### 依赖关系

要启用此参数，请选择 **Enable signal enabling input** 复选框。

**数据类型：** `double` | `single` | `Boolean`
### 输出

### **Y** — 放大后的信号 复值向量 | 复值矩阵

放大后的接收信号电压，以复值向量或复值矩阵返回。如果 **X** 是矩阵，则 **y** 的大小等于 **X** 的大小。该变换基于接收机特性，例如增益、非线性和噪声。功率根据信号电压计算，假设参考阻抗为 1 Ohm。

**数据类型：** `single` | `double`
**复数支持：** Yes

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

#### 输入信号

### **Enable signal enabling input** — 启用信号输入 `false`0（默认）| `true`1

选中此复选框以允许接收机通过 **EN** 端口接受输入。

**示例：**

**数据类型：** `Boolean`

### **Add noise to input signal** — 向输入信号添加噪声 `off`（默认）| `on`

选中此复选框以在应用接收机效应之前向输入信号添加噪声。**Input noise temperature (K)** 参数确定添加噪声的功率。**Sample rate (Hz)** 参数确定噪声带宽。

**示例：**
`true`

**数据类型：** `Boolean`

### **Input noise temperature (K)** — 输入噪声温度 `290`（默认）| 正标量 | 长度为 *N* 的正值向量

输入噪声温度，指定为正标量或长度为 *N* 的正值向量，其中 *N* 是接收机通道数。如果 **Input noise temperature (K)** 参数是标量，则同一值应用于所有通道。单位为 Kelvin degrees。

**示例：** `300`

#### 依赖关系

要启用此参数，请选中 **Input noise temperature (K)** 复选框。

**数据类型：** `single` | `double`

### **Sample rate (Hz)** — 采样率 `1e6`（默认）| 正标量

输入信号的采样率，指定为正标量。使用此参数向信号添加噪声。**Sample rate (Hz)** 参数仅用于推导信号的噪声带宽。

#### 依赖关系

要启用此属性，请选中 **Add noise to input signal** 复选框，或将 **Noise method** 参数设置为 `Noise figure`、`Noise factor` 或 `Noise temperature`。

**数据类型：** `single` | `double`

### **Inherit sample rate** — 从上游模块继承采样率 on（默认）| off

选择此参数以从上游模块继承采样率。否则，使用 **Sample rate (Hz)** 参数指定采样率。

**数据类型：** `Boolean`

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要编译时间，但通常运行更快。

在开发和调整模型时，解释执行很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，则模块会在执行前自动重新编译。

此表显示 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都会被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认：** `Interpreted Execution` |

#### 系统噪声

### **Noise method** — 噪声方法 `None` | `Noise figure` | `Noise factor` | `Noise temperature`

定义系统噪声的方法，指定为 `None`、`Noise figure`、`Noise factor` 或 `Noise temperature`。

- 当设置为 `None` 时，不应用噪声。
- 当设置为 `Noise figure` 时，**Noise figure (dB)** 参数确定噪声水平。
- 当设置为 `Noise temperature` 时，**Input noise temperature (K)** 参数确定噪声水平。
- 当设置为 `Noise factor` 时，**Noise factor** 参数确定噪声水平。

噪声带宽根据输入信号采样率推导。

**示例：** `Noise figure`

**数据类型：** `char` | `string`

### **Noise figure (dB)** — 噪声系数 `3`（默认）| 实标量 | 长度为 *N* 的实数值向量

接收机噪声系数，指定为实标量或长度为 *N* 的实数值向量。*N* 是通道数。如果 **Noise figure (dB)** 是标量，则同一值应用于所有通道。噪声相对于 **Reference temperature (K)** 参数定义的温度生成。

#### 依赖关系

要启用此属性，请将 **Noise method** 参数设置为 `Noise figure`。

**数据类型：** `single` | `double`

### **Noise factor** — 噪声因子 `2`（默认）| 正标量 | 长度为 *N* 的正值向量

接收机噪声因子，指定为正标量或长度为 *N* 的正值向量。*N* 是通道数。如果 **Noise factor** 参数是标量，则同一值应用于所有通道。噪声相对于 **Reference temperature (K)** 参数定义的温度生成。

#### 依赖关系

要启用此属性，请将 **Noise method** 参数设置为 `Noise factor`。

**数据类型：** `single` | `double`

### **Reference temperature (K)** — 参考温度 `290`（默认）| 正标量 | 长度为 *N* 的正值向量

参考温度，指定为正标量或长度为 *N* 的正值向量。*N* 是通道数。如果 **Reference temperature (K)** 参数是标量，则同一值应用于所有通道。

#### 依赖关系

要启用此属性，请将 **Noise method** 参数设置为 `Noise figure` 或 `Noise factor`。

**数据类型：** `single` | `double`

#### 增益

### **Gain method** — 增益方法 `Linear`（默认）| `Cubic polynomial` | `Lookup table`

对接收信号应用增益的方法，指定为 `Linear`、`Cubic polynomial` 或 `Lookup table`。

- 当设置为 `Linear` 时，应用线性增益。
- 当设置为 `Cubic polynomial` 时，使用三次多项式模型应用非线性增益。
- 当设置为 `Lookup table` 时，定义查找表以直接将输出功率和相移指定为输入功率的函数。

**数据类型：** `char` | `string`

### **Gain (dB)** — 线性接收机增益 `20`（默认）| 实标量 | 长度为 *N* 的实数值向量

线性接收机增益，指定为实标量或长度为 *N* 的实数值向量。*N* 是通道数。如果 **Gain (dB)** 参数是标量，则同一值应用于所有通道。单位为 dB。

#### 依赖关系

要启用此属性，请将 **Gain method** 参数设置为 `Linear` 或 `Cubic polynomial`。

**数据类型：** `single` | `double`

### **Output IP3 (dBm)** — 输出 IP3 `Inf`（默认）| 标量 | 长度为 *N* 的实数值向量

输出 IP3，指定为标量或长度为 *N* 的实数值向量。*N* 是通道数。OIP3 表示发射机或接收机的非线性。OIP 也称为三阶截点。如果 OIP3 是标量，则同一值应用于所有通道。有关 OIP3 的详细讨论，请参阅 Nonlinearities and Noise in Idealized Baseband Amplifier Block (RF Blockset)。单位为 dBm。

#### 依赖关系

要启用此属性，请将 **Gain method** 参数设置为 `Cubic polynomial`。

**数据类型：** `single` | `double`

### **Lookup table** — 查找表 `[-25, 5, -1; -10, 20, -2; 0, 27, 5; 5, 28, 12]`（默认）| *M*×*N* 实值矩阵 | *M*×*N* 实值矩阵

查找表，指定为 3-by-*M*-by-*N* 实值数组。在 [Pin(dBm),Pout(dBm),Phase shift(degrees)]-by-*M* 或 [Pin(dBm),Pout(dBm),Phase shift(degrees)]-by-*M*-by-*N* 矩阵中指定 AM/AM（以 dB/dB 为单位）和 AM/PM（以 deg/dB 为单位）特性。*M* 是表项数，*N* 是通道数。矩阵元素必须为实数。第 1 列的输入功率必须单调增加。表中必须至少有 3 行。

#### 依赖关系

要启用此属性，请将 **Gain method** 参数设置为 `Lookup table`。

**数据类型：** `single` | `double`

#### PhaseOffset

### **Phased offset (degrees)** — 相位偏移 `0`（默认）| 标量 | 长度为 *N* 的实数值向量

相位偏移，指定为实标量或长度为 *N* 的实数值向量。*N* 是通道数。如果 **Phase offset (degrees)** 是标量，则同一值应用于所有通道。单位为 degrees。

**数据类型：** `single` | `double`

#### 随机化

### **Source of seed for random number generator** — 随机数生成器种子的来源 `Auto`（默认）| `Property`

随机数生成器种子的来源，指定为 `Auto` 或 `Property`。当来源为 `Auto` 时，种子自动生成。当来源为 `Property` 时，使用 **Seed for random number generator** 参数设置种子。

**示例：** `Property`

**数据类型：** `char` | `string`

### **Seed for random number generator** — 随机数生成器的种子 0（默认）| 正整数

随机生成器的种子，指定为正整数。

**数据类型：** `single` | `double`

## 所属库

Phased Array System Toolbox / Transmitters and Receivers

## 模块特性

未在 R2025b 中记载。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024a 中引入**

## 描述

Receiver

放大输入信号，并加入非线性失真和噪声。
