---
type: simulink-block
title: 'Receiver Thermal Noise'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'RF Impairments and Components'
documentation_page: 'receiverthermalnoise'
documentation_source_path: 'ref/receiverthermalnoise.html'
language: zh-CN
chinese_source: worker-translation
---

# Receiver Thermal Noise

## 端口

### 输入

### **In1** — 基带信号 标量 | 列向量 | 矩阵

基带信号，指定为复值标量、*N*S 元素列向量或 *N*S×*N*C 矩阵。*N*S 是样本数，*N*C 是通道数。

**数据类型：** `double` | `single`
**复数支持：** 是
### 输出

### **Out1** — 输出信号 标量 | 列向量 | 矩阵

输出信号，返回为复值标量、列向量或矩阵，其长度和数据类型与输入信号相同。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Specification method** — 热噪声指定方法 `Noise temperature`（默认）| `Noise figure` | `Noise factor`

热噪声指定方法，指定为以下选项之一。

- `Noise temperature` 以开尔文为单位指定噪声。
- `Noise figure` 指定相对于 290 K 输入噪声温度的接收机附加噪声，以 dB 为单位。噪声系数是噪声因子的分贝等效值。
- `Noise factor` 指定相对于 290 K 输入噪声温度的接收机附加噪声。噪声因子是噪声系数的线性等效值。

### **Noise temperature (K)** — 噪声温度 `290`（默认）| 标量

噪声温度，以开尔文为单位，指定为标量。

**可调：** 是

#### 依赖关系

当 **Specification method** 设置为 `Noise temperature` 时，此参数适用。

**数据类型：** `double` | `single`

### **Noise figure (dB)** — 接收机噪声系数 `3.0103`（默认）| 标量

接收机噪声系数，相对于 290 K 噪声温度，以 dB 为单位，指定为标量。

**注意**

此参数仅指定接收机电路的噪声贡献。要添加天线噪声的影响，请选择 **Add 290K antenna noise**。

**可调：** 是

#### 依赖关系

当 **Specification method** 设置为 `Noise figure` 时，此参数适用。

**数据类型：** `double` | `single`

### **Noise factor** — 接收机噪声因子 `2`（默认）| 标量

接收机噪声因子，相对于 290 K 噪声温度，指定为标量。

**注意**

此参数仅指定接收机电路的噪声贡献。要添加天线噪声的影响，请选择 **Add 290K antenna noise**。

**可调：** 是

#### 依赖关系

当 **Specification method** 设置为 `Noise factor` 时，此参数适用。

**数据类型：** `double` | `single`

### **Add 290K antenna noise** — 添加 290 K 天线噪声的选项 `off`（默认）| `on`

选择此参数可将 290 K 天线噪声添加到信号中。

#### 依赖关系

当 **Specification method** 设置为 `Noise factor` 或 `Noise figure` 时，此参数适用。

### **Reference load (ohm)** — 参考负载 `1`（默认）| 标量

参考负载值，以欧姆为单位，指定为标量。此值用于根据信号和噪声功率电平计算电压电平。

**可调：** 是

**数据类型：** `double` | `single`

### **Random number source** — 随机数流来源 `Global stream`（默认）| `mt19937ar with seed`

随机数流来源，指定为 `Global stream` 或 `mt19937ar with seed`。

### **Initial seed** — 初始种子值 `67987`（默认）| 标量

随机数生成器的初始种子值，指定为标量。

#### 依赖关系

当 **Random number source** 设置为 `mt19937ar with seed` 时，此参数适用。

**数据类型：** `double` | `single`

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认）| `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度快于 `Interpreted execution` 选项。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但后续仿真的速度慢于 `Code generation` 选项。在此模式下，您可以调试模块的源代码。

有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。

## 所属库

Communications Toolbox / RF Impairments and Components

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

### R2023b：多通道输入支持

`Receiver Thermal Noise` System object™ 接受矩阵输入基带信号。矩阵的每一列表示来自多天线系统一个通道的基带信号。

### R2023b：可变大小支持

此支持使您能够在仿真中每次模块执行时改变输入信号的长度。

### R2023b：随机数生成器更新

Receiver Thermal Noise 模块更新了随机数生成器（RNG）来源。您现在可以使用 **Random number source** 参数选择 `Global stream` 或 `mt19937ar with seed` 作为 RNG 来源。要在 For Each Subsystem (Simulink) 中使用此模块，必须将 **Random number source** 设置为 `Global Stream`。这确保每次运行都会生成独立的噪声样本。

对于在 R2023b 之前创建的仿真，模块默认为传统模式。在传统模式下，模块使用 Random Source 模块生成噪声，并使用 Ziggurat 方法（V5 RANDN 算法）生成随机数。每次重新运行仿真时，模块都会重用相同的初始种子，因此每次运行仿真时此模块输出相同的信号。

要在使用 Receiver Thermal Noise 模块的 R2023b 之前模型中运行仿真时改进统计特性，请运行 **Update Model** 并将 R2023b 之前的模型转换为使用新的 Receiver Thermal Noise 模块功能。

### R2023b：代码生成

代码生成默认启用。有关详细信息，请参阅 **Simulate using**。

### R2023b：单数据类型支持

如果输入信号为 single 类型，则模块以单精度原生计算，返回的输出也为 single 类型。

## 描述

对复信号应用接收机热噪声

Receiver Thermal Noise 模块对复信号应用接收机热噪声。该模块模拟热噪声对复信号的影响。**Specification method** 参数允许基于噪声温度、噪声系数或噪声因子来指定热噪声。
