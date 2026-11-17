---
type: simulink-block
title: 'LRT Detector'
family: 'detection'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection'
documentation_page: 'lrtdetector'
documentation_source_path: 'ref/lrtdetector.html'
language: zh-CN
chinese_source: worker-translation
---

# LRT Detector

## 端口

### 输入

### **X** — 输入数据 实值 *N*×*1* 向量 | 复值 *N*×*1* 向量 | 实值 *N*×*M* 矩阵 | 复值 *N*×*M* 矩阵

输入数据，指定为实值或复值 *N*×*1* 向量，或 *N*×*M* 实值或复值矩阵。*N* 是信号长度，*M* 是数据通道数。每个数据通道有 *N* 个样本，从而得到 *N*×*M* 矩阵。每一行表示长度为 *M* 的数据向量的分量。当 *M = 1* 时，`X` 表示单通道数据。当 *M > 1* 时，`X` 可以表示来自 *M* 个数据通道的 *N* 个样本。检测沿 `X` 的列执行。每一行的大小 *M* 在仿真期间不能改变。

LRT 检测器假定 `X` 的每一列具有相同的信号模型。无噪声信号包含在 *N* 维数据向量 `Xknown` 中。由噪声功率 `NCov` 定义的高斯噪声被添加到每一列。对于该信号模型，LRT 检测器确定是否拒绝零假设 `Xknown` `= 0`。由于只有一个已知信号模型，LRT 检测器为 `X` 的每一列输出一个检测结果。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **XK** — 已知信号 实值 *N*×1 向量 | 复值 *N*×1 向量

已知无噪声信号，指定为实值或复值 *N*×1 向量。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **NCov** — 噪声功率 正标量

噪声功率或协方差，指定为正标量。

**示例：** `2.0`

**数据类型：** `single` | `double`
### 输出

### **Y** — 检测结果 1×*M* 逻辑值向量 | 1×*L* 整数值向量

检测结果，返回为 1×*M* 逻辑值向量或 1×*L* 整数值向量。`Y` 的格式取决于 **输出格式** 参数的值。默认情况下，**输出格式** 参数设置为 `'Detection result'`。

- 当 **输出格式** 参数设置为 `'Detection result'` 时，`Y` 是 1×*M* 向量，包含逻辑检测结果，其中 *M* 是 `X` 的列数。如果 `X` 的对应列中存在检测，则 `Y` 为 `true`。否则，`Y` 为 `false`。
- 当 **输出格式** 参数设置为 `'Detection index'` 时，`Y` 是 1×*L* 整数值向量，包含检测索引，其中 *L* 是在所有 *M* 个通道中找到的检测数。

**数据类型：** `single` | `double` | `Boolean`
**复数支持：** Yes

### **Stat** — 检测统计量 *D*×*M*（默认）| 矩阵 | 1×*L* 向量

检测统计量，返回为 *D*×*M* 矩阵或 1×*L* 向量。`stat` 的格式取决于 **输出格式** 参数的设置。

- 当 **输出格式** 参数为 `'Detection result'` 时，`stat` 是 *D*×*M* 矩阵。
- 当 **输出格式** 参数为 `'Detection index'` 时，`stat` 是 1×*L* 向量，包含 `Y` 中每个对应检测的检测统计量。

#### 依赖项

要启用此端口，请选中 **输出检测统计量和阈值** 复选框。

**数据类型：** `single` | `double`
**复数支持：** Yes

### **Th** — 检测阈值 标量

检测阈值，返回为标量。

#### 依赖项

要启用此端口，请选中 **输出检测统计量和阈值** 复选框。

**数据类型：** `single` | `double`

## 参数

### **虚警概率** — 虚警概率 `0.1`（默认）| 非负标量

虚警概率，指定为 0 到 1 之间（含 0 和 1）的正标量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ProbabilityFalseAlarm` |
| **类型：** double, single |
| **值：** `scalar` | |
| **默认值：** 0.1 |

**数据类型：** `single` | `double`

### **输出格式** — 输出数据的格式 `Detection result`（默认）| `Detection index`

输出数据的格式，指定为 `Detection result` 或 `Detection index`。输出数据在 `Y` 端口返回。

**示例：** `Detection index`

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutputFormat` |
| **类型：** char, string |
| **值：** `Detection result` | `Detection index` |
| **默认值：** `Detection result` |

**数据类型：** `char` | `string`

### **输出检测统计量和阈值** — 输出检测统计量和阈值 `false`（默认）| `true`

选中此复选框以使用 **Stat** 和 **Th** 端口输出检测统计量和检测阈值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ThresholdOutputPort` |
| **类型：** check box |
| **值：** 0 | 1 |
| **默认值：** `0` |

### **仿真使用** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间编译，但通常运行更快。

解释执行在开发和调整模型时很有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改和执行模型。当对结果满意时，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，模块将在执行前自动重新编译。

此表显示 **仿真使用** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **仿真使用** 指定的模块模式会覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块都被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 程序化使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认值：** `Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Detection

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

似然比检验检测器

似然比检验 (LRT) 检测器在有噪声的情况下执行二元信号检测。二元检测器基于数据测量在零假设 *H*0 和备择假设 *H*1 之间进行选择。零假设表示不存在任何信号，而备择假设表示存在某种信号。
