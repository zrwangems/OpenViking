---
type: simulink-block
title: 'Time Varying Gain'
family: 'detection'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection'
documentation_page: 'timevaryinggain'
documentation_source_path: 'ref/timevaryinggain.html'
language: zh-CN
chinese_source: worker-translation
---

# Time Varying Gain

## 端口

### 输入

### **Port\_1** — 输入信号 向量 | 矩阵 | 数组

输入信号，指定为向量、矩阵或数组。

输入矩阵第一个维度的大小可以变化，以模拟信号长度的变化。例如，对于脉冲重复频率可变的脉冲波形，可能会发生这种大小变化。

**数据类型：** `double` | `single`

### **Port\_2** — 距离损耗 列向量

距离损耗，指定为列向量。该向量的长度必须等于或大于 **Port\_1** 中输入信号的行数。

该过程对所有样本的功率电平进行均衡，以匹配给定的参考距离。增益独立应用于 **Port\_1** 中的每一列。**Port\_1** 的行数不能超过 **距离损耗 (dB)** 参数中指定的损耗向量的长度。

#### 依赖关系

要启用此端口，请将 **距离损耗源** 参数设置为 `Input port`。

**数据类型：** `double` | `single`

### 输出

### **Port\_1** — 经距离补偿的信号 向量 | 矩阵 | 数组

经距离补偿的信号，以向量、矩阵或数组形式返回。经距离补偿的信号与输入信号具有相同的大小。

**数据类型：** `double` | `single`

## 参数

### **距离损耗源** — 距离损耗的来源 `Property` (默认) | `Input Port`

距离损耗的来源，指定为 `Property` 或 `Input Port`。

|  |  |
| --- | --- |
| `Property` | 使用 **距离损耗 (dB)** 参数指定距离损耗。 |
| `Input port` | 使用输入端口 **Port\_2** 指定距离损耗。 |

**数据类型：** `char` | `string`

### **距离损耗 (dB)** — 各输入采样点对应距离处的损耗 `0` (默认) | 向量

各输入采样点对应距离处的损耗，指定为向量。向量元素对应于输入信号中的样本。单位为 dB。

#### 依赖关系

要启用此参数，请将 **距离损耗源** 参数设置为 `Input port`。

**数据类型：** `double` | `single`

### **参考距离损耗 (dB)** — 参考距离处的损耗 `0` (默认) | 标量

给定参考距离处的损耗，指定为标量。单位为 dB。

**数据类型：** `double` | `single`

### **仿真方式** — 模块仿真方法 `Interpreted Execution` (默认) | `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要一定的编译时间，但通常运行速度更快。

在开发和调优模型时，解释执行非常有用。该模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。对结果满意后，即可使用 `Code Generation` 运行模块。与解释执行相比，长时间仿真使用生成的代码运行得更快。您可以在不重新编译的情况下重复执行，但如果更改任何模块参数，模块会在执行前自动重新编译。

下表显示了 **仿真方式** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **仿真方式** 指定的模块模式会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 根据模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅选择仿真模式 (Simulink)。

#### 编程使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`、`Code Generation` |
| **默认值：** `Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Detection

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2014b 中推出**

## 描述

时变增益 (TVG) 控制

Time Varying Gain 模块对输入信号施加时变增益，以补偿每个距离门处的几何距离损耗。时变增益 (TVG) 有时称为自动增益控制 (AGC)。
