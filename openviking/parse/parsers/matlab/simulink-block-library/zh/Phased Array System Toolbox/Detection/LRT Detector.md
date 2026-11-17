---
type: simulink-block
title: 'LRT Detector'
family: 'phased'
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
```yaml
ports:
- name: X
  summary: 输入数据 实值 *N*×*1* 向量 | 复值 *N*×*1* 向量 | 实值 *N*×*M* 矩阵 | 复值 *N*×*M* 矩阵
  direction: input
  data_types: single | double
- name: XK
  summary: 已知信号 实值 *N*×1 向量 | 复值 *N*×1 向量
  direction: input
  data_types: single | double
- name: NCov
  summary: 噪声功率 正标量
  direction: input
  data_types: single | double
- name: Y
  summary: 检测结果 1×*M* 逻辑值向量 | 1×*L* 整数值向量
  direction: output
  data_types: single | double | Boolean
- name: Stat
  summary: 检测统计量 *D*×*M*（默认）| 矩阵 | 1×*L* 向量
  direction: output
  data_types: single | double
- name: Th
  summary: 检测阈值 标量
  direction: output
  data_types: single | double
```

### 输入

### **X** — 输入数据 实值 *N*×*1* 向量 | 复值 *N*×*1* 向量 | 实值 *N*×*M* 矩阵 | 复值 *N*×*M* 矩阵

输入数据，指定为实值或复值 *N*×*1* 向量，或 *N*×*M* 实值或复值矩阵。*N* 是信号长度，*M* 是数据通道数。每个数据通道有 *N* 个样本，构成 *N*×*M* 矩阵。每一行表示长度为 *M* 的数据向量的分量。当 *M = 1* 时，`X` 表示单通道数据。当 *M > 1* 时，`X` 可以表示来自 *M* 个数据通道的 *N* 个样本。检测沿 `X` 的列执行。每行的大小 *M* 在仿真期间不能改变。

LRT 检测器假设 `X` 的每一列具有相同的信号模型。无噪声信号包含在 *N* 维数据向量 `Xknown` 中。由噪声功率 `NCov` 定义的高斯噪声被添加到每一列。对于该信号模型，LRT 检测器确定是否拒绝零假设 `Xknown` `= 0`。由于只有一个已知信号模型，LRT 检测器对 `X` 的每一列输出一个检测结果。

**数据类型：** `single` | `double`
**复数支持：** 是

### **XK** — 已知信号 实值 *N*×1 向量 | 复值 *N*×1 向量

已知无噪声信号，指定为实值或复值 *N*×1 向量。

**数据类型：** `single` | `double`
**复数支持：** 是

### **NCov** — 噪声功率 正标量

噪声功率或协方差，指定为正标量。

**示例：** `2.0`

**数据类型：** `single` | `double`
### 输出

### **Y** — 检测结果 1×*M* 逻辑值向量 | 1×*L* 整数值向量

检测结果，返回为 1×*M* 逻辑值向量或 1×*L* 整数值向量。`Y` 的格式取决于 **Output format** 参数的值。默认情况下，**Output format** 参数设置为 `'Detection result'`。

- 当 **Output format** 参数设置为 `'Detection result'` 时，`Y` 是包含逻辑检测结果的 1×*M* 向量，其中 *M* 是 `X` 的列数。如果 `X` 的对应列中存在检测，则 `Y` 为 `true`。否则，`Y` 为 `false`。
- 当 **Output format** 参数设置为 `'Detection index'` 时，`Y` 是包含检测索引的 1×*L* 整数值向量，其中 *L* 是在所有 *M* 个通道中找到的检测数量。

**数据类型：** `single` | `double` | `Boolean`
**复数支持：** 是

### **Stat** — 检测统计量 *D*×*M*（默认）| 矩阵 | 1×*L* 向量

检测统计量，返回为 *D*×*M* 矩阵或 1×*L* 向量。`stat` 的格式取决于 **Output format** 参数的设置。

- 当 **Output format** 参数为 `'Detection result'` 时，`stat` 是 *D*×*M* 矩阵。
- 当 **Output format** 参数为 `'Detection index'` 时，`stat` 是包含 *Y* 中每个对应检测的检测统计量的 1×*L* 向量。

#### 依赖

要启用此端口，请选中 **Output detection statistics and threshold** 复选框。

**数据类型：** `single` | `double`
**复数支持：** 是

### **Th** — 检测阈值 标量

检测阈值，返回为标量。

#### 依赖

要启用此端口，请选中 **Output detection statistics and threshold** 复选框。

**数据类型：** `single` | `double`
## 参数
```yaml
parameters:
- name: Probability of false alarm
  summary: 虚警概率 0.1（默认）| 非负标量
  group: ''
  block_parameter: ProbabilityFalseAlarm
  type: double, single
  values: scalar |
- name: Output format
  summary: 输出数据的格式 Detection result（默认）| Detection index
  group: ''
  block_parameter: OutputFormat
  type: char, string
  values: Detection result | Detection index
- name: Output detection statistics and threshold
  summary: 输出检测统计量和检测门限 false（默认）| true
  group: ''
  block_parameter: ThresholdOutputPort
  type: check box
  values: 0 | 1
- name: Simulate using
  summary: 模块仿真方法 Interpreted Execution（默认）| Code Generation
  group: ''
  block_parameter: SimulateUsing
  type: enum
  values: Interpreted Execution, Code Generation
```

### **Probability of false alarm** — 虚警概率 `0.1`（默认）| 非负标量

虚警概率，指定为 0 到 1 之间（含端点）的正标量。

#### 程序化使用

|  |
| --- |
| **模块参数：**`ProbabilityFalseAlarm` |
| **类型：**double, single |
| **值：**`scalar` | |
| **默认：**0.1 |

**数据类型：** `single` | `double`

### **Output format** — 输出数据的格式 `Detection result`（默认）| `Detection index`

输出数据的格式，指定为 `Detection result` 或 `Detection index`。输出数据在 `Y` 端口中返回。

**示例：** `Detection index`

#### 编程方式使用

|  |
| --- |
| **模块参数：**`OutputFormat` |
| **类型：**char, string |
| **值：**`Detection result` | `Detection index` |
| **默认：**`Detection result` |

**数据类型：** `char` | `string`

### **Output detection statistics and threshold** — 输出检测统计量和检测门限 `false`（默认）| `true`

选中此复选框可使用 **Stat** 和 **Th** 端口输出检测统计量和检测门限。

#### 编程方式使用

|  |
| --- |
| **模块参数：**`ThresholdOutputPort` |
| **类型：**check box |
| **值：**0 | 1 |
| **默认：**`0` |

### **Simulate using** — 模块仿真方法 `Interpreted Execution`（默认）| `Code Generation`

模块仿真，指定为 `Interpreted Execution` 或 `Code Generation`。如果希望模块使用 MATLAB® 解释器，请选择 `Interpreted Execution`。如果希望模块作为编译代码运行，请选择 `Code Generation`。编译代码需要时间进行编译，但通常运行更快。

在开发和调优模型时，解释执行非常有用。模块在 MATLAB 中运行底层 System object™。您可以快速更改并执行模型。当您对结果满意后，可以使用 `Code Generation` 运行模块。长时间仿真使用生成的代码比解释执行运行更快。您可以重复执行而无需重新编译，但如果更改任何模块参数，模块将在执行前自动重新编译。

下表显示了 **Simulate using** 参数如何影响整体仿真行为。

当 Simulink® 模型处于 `Accelerator` 模式时，使用 **Simulate using** 指定的模块模式将覆盖仿真模式。

**加速模式**

|  |  |  |  |
| --- | --- | --- | --- |
| 模块仿真 | 仿真行为 | | |
| `Normal` | `Accelerator` | `Rapid Accelerator` |
| `Interpreted Execution` | 模块使用 MATLAB 解释器执行。 | 模块使用 MATLAB 解释器执行。 | 从模型创建独立可执行文件。 |
| `Code Generation` | 模块被编译。 | 模型中的所有模块被编译。 |

有关详细信息，请参阅 Choosing a Simulation Mode (Simulink)。

#### 编程方式使用

|  |
| --- |
| **模块参数：** `SimulateUsing` |
| **类型：** enum |
| **值：** `Interpreted Execution`, `Code Generation` |
| **默认：** `Interpreted Execution` |
## 所属库

Phased Array System Toolbox / Detection

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

似然比检验检测器

似然比检验（LRT）检测器在存在噪声的情况下执行二进制信号检测。二进制检测器基于数据测量在零假设 *H*0 和备择假设 *H*1 之间进行选择。零假设表示不存在任何信号，而备择假设表示存在某种信号。
