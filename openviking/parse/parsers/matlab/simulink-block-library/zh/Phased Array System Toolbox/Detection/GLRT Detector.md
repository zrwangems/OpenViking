---
type: simulink-block
title: 'GLRT Detector'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection'
documentation_page: 'glrtdetector'
documentation_source_path: 'ref/glrtdetector.html'
language: zh-CN
chinese_source: worker-translation
---

# GLRT Detector

## 端口

### 输入

### **X** — 输入数据 实值 *N*×*1* 向量 | 复值 *N*×*1* 向量 | 实值 *N*×*M* 矩阵 | 复值 *N*×*M* 矩阵

输入数据，指定为实值或复值 *N*×*1* 向量，或 *N*×*M* 实值或复值矩阵。*N* 是信号长度，*M* 是数据通道数。检测沿 `X` 的列执行。每行的大小 *M* 在仿真期间不能更改。当 *M = 1* 时，`X` 表示单通道数据。当 *M > 1* 时，`X` 可以表示来自 *M* 个数据通道的 *N* 个样本。数据流之后可以合并，例如通过波束成形。

输入数据具有一般性解释。例如，数据可以解释为：

- 时间序列 – 时间序列的 *N* 个样本
- 传感器 – *N* 表示来自一组传感器的数据样本快照

**数据类型：** `single` | `double`
**复数支持：** 是

### **Hyp** — 增广线性等式约束矩阵 实值 *R*×(*P* + 1) 矩阵 | 复值 *R*×(*P* + 1) 矩阵

增广线性等式约束矩阵，指定为实值或复值 *R*×(*P* + 1) 矩阵。该矩阵的形式为 **[A,b]**，表示方程：

AΘ=b

其中未知参数由 ϴ 表示。**A** 的秩为 *R ≥ 1*。增广线性等式约束矩阵表示零假设 *H*0。

对于该信号模型，GLRT 检测器确定是否拒绝零假设，零假设以 **A\*ϴ = b** 的形式表示，其中 **A** 是 *R*×*P* 矩阵，*R ≤ P*，秩 *R ≥ 1*，**b** 是 *R*×1 向量。**A** 和 **b** 包含在增广线性等式约束矩阵 **hyp = [A,b]** 中。由于存在 *D* 个信号模型，GLRT 检测器为 `X` 的每一列输出 *D* 个检测结果。

**数据类型：** `single` | `double`
**复数支持：** 是

### **Obs** — 观测矩阵 *N*×*P*×*D* 数组

线性确定性信号模型的观测矩阵，指定为 *N*×*P*×*D* 数组，*N > p* 且秩为 *P*，*D* 是信号模型的数量，白高斯 `noise` 是由协方差 `ncov` 参数确定的 *N*×1 向量。观测矩阵定义为 `X` = `obs`\*`param` + `noise`，

**示例：** 20.0

**数据类型：** `single` | `double`
**复数支持：** 是

### **Ncov** — 已知噪声功率 正标量

已知噪声功率，指定为标量或长度为 *D* 的行向量。当 `ncov` 为标量时，它表示 *D* 个模型的相等已知噪声功率。当 `ncov` 为长度为 *D* 的行向量时，它分别表示 *D* 个模型的已知噪声功率。

**示例：** `20.0`

#### 依赖关系

要启用此参数，请将 `NoiseInputPort` 属性设置为 `true`。

**数据类型：** `single` | `double`
### 输出

### **Y** — 检测结果 *D*×*M* 逻辑值向量 | 1×*L* 整数值向量 | 2×*L* 整数值矩阵

*D* 个模型对 *M* 个独立数据样本的检测结果，以 *D*×*M* 逻辑值向量形式返回。`Y` 的格式取决于 `OutputFormat` 属性的指定方式。默认情况下，`OutputFormat` 属性设置为 `'Detection result'`。

当 `OutputFormat` 为 `'Detection result'` 时，`Y` 是一个 *D*×*M* 矩阵，包含逻辑检测结果，其中 *D* 是信号模型的数量，*M* 是 `X` 的列数。对于每一行，如果 `arg` 的对应列中存在检测，则 `Y` 在该列中为 `true`。否则，`Y` 为 `false`。

当 `OutputFormat` 为 `'Detection index'` 时，`Y` 是一个 1×`L` 向量或 2×*L* 矩阵，包含检测索引，其中 *L* 是在 *M* 个数据样本和 *D* 个模型中发现的检测数量。当 `X` 是列向量时，*Y* 是 1×*L* 向量，包含在 *D* 个模型中发现的检测的索引。当 `X` 是矩阵时，`Y` 是 2×*L* 矩阵，`Y` 的每一列具有 `[detrow;detcol]` 的形式，其中 `detrow` 是模型的索引，`detcol` 是 *X* 的列索引。

### **Stat** — 检测统计量 *N*×*M*（默认）| 1×*L*

检测统计量，以 *N*×*M* 矩阵或 1×*L* 向量形式返回。`stat` 的格式取决于 `OutputFormat` 属性。

- 当 `OutputFormat` 为 `'Detection result'` 时，`stat` 的大小与 *Y* 相同。
- 当 `OutputFormat` 为 `'Detection index'` 时，`stat` 是一个 1×*L* 向量，包含 *Y* 中每个对应检测的检测统计量。

#### 依赖关系

要启用此端口，请选中 **Output detection statistics and threshold** 复选框。

### **Th** — 检测阈值 标量

检测阈值，以标量形式返回。

#### 依赖关系

要启用此端口，请选中 **Output detection statistics and threshold** 复选框。

### **Param** — 信号参数的最大似然估计 *P*×*M*×*D* 数组

未知信号参数的最大似然估计（MLE），以 *P*×*M*×*D* 数组形式返回。

#### 依赖关系

要启用此端口，请选中 **Output MLEs of unknown signal parameters** 复选框。

### **N** — 估计噪声功率 正标量

估计噪声功率，以正标量形式返回。当 `OutputFormat` 属性为 `'Detection result'` 时，`estnoise` 的大小与 `Y` 相同。当 `OutputFormat` 属性为 `'Detection index'` 时，`estnoise` 返回大小为 1×*L* 的噪声功率估计，对应于 `Y` 中的每个检测。

#### 依赖关系

要启用此端口，请选中 **Output estimated noise power** 复选框。

## 参数

### **Probability of false alarm** — 虚警概率 `0.1`（默认）| 非负标量

虚警概率，指定为 0 到 1（含）之间的正标量。

#### 编程使用

|  |
| --- |
| **模块参数：**`ProbabilityFalseAlarm` |
| **类型：**double, single |
| **值：**`scalar` | |
| **默认：**0.1 |

**数据类型：** `single` | `double`

### **Output format** — 输出数据格式 `Detection result`（默认）| `Detection index`

输出数据格式，指定为 `Detection result` 或 `Detection index`。输出数据通过 `Y` 端口返回。

**示例：** `Detection index`

#### 编程使用

|  |
| --- |
| **模块参数：**`OutputFormat` |
| **类型：**char, string |
| **值：**`Detection result` | `Detection index` |
| **默认：**`Detection result` |

**数据类型：** `char` | `string`

### **Output detection statistics and threshold** — 输出检测统计量和阈值 `0`（默认）| `1`

选中此复选框以使用 **Stat** 和 **Th** 端口输出检测统计量和检测阈值。

#### 编程使用

|  |
| --- |
| **模块参数：**`ThresholdOutputPort` |
| **类型：**复选框 |
| **值：**0 | 1 |
| **默认：**`0` |

### **Enable known noise power input** — 启用已知噪声功率输入 `1`（默认）| `1`

选中此复选框以允许使用 **NCov** 端口输入噪声功率。

#### 依赖关系

要选中此复选框，请取消选中 **Output estimated noise power** 复选框。

#### 程序化使用

|  |
| --- |
| **模块参数：**`NoiseInputPort` |
| **类型：**复选框 |
| **值：**0 | 1 |
| **默认值：**`0` |

### **Output MLEs of unknown signal parameters** — 输出未知信号参数的 MLE 0（默认）| 1

选中此复选框以使用 `Param` 端口输出信号参数的最大似然估计。

#### 程序化使用

|  |
| --- |
| **模块参数：**`SignalParamterOutputPort` |
| **类型：**复选框 |
| **值：**0 | 1 |
| **默认值：**`0` |

### **Output estimated noise power** — 输出估计噪声功率 0（默认）| 1

选中此复选框以使用 `N` 端口输出估计噪声功率。

#### 程序化使用

|  |
| --- |
| **模块参数：**`NoisePowerOutputPort` |
| **类型：**复选框 |
| **值：**0 | 1 |
| **默认值：**`0` |

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

在开发和调整模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，模块将在执行前自动重新编译。

下表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

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
| **值：** `Interpreted Execution`、`Code Generation` |
| **默认值：** `Interpreted Execution` |

## 所属库

Phased Array System Toolbox / Detection

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

执行广义似然比检验检测

广义似然比检验检测器（GLRT）在存在噪声的情况下执行未知参数信号的检测。未知参数包括信号幅度、相位、频率和到达时间。该检测器在信号不存在 *H*0 和备择信号存在 *H*1 假设下，用未知参数的最大似然估计替换未知参数。然后，二元检测器根据测量结果在原假设 *H*0 和备择假设 *H*1 之间进行选择。如果 *H*0 假设最能解释数据，检测器则声明目标不存在。如果 *H*1 假设最能解释数据，检测器则声明目标存在。
