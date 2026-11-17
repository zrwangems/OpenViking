---
type: simulink-block
title: 'Random Source'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'randomsource'
documentation_source_path: 'ref/randomsource.html'
language: zh-CN
chinese_source: worker-translation
---

# Random Source

## 端口
```yaml
ports:
- name: Port_1
  summary: 随机分布值的信号 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double
```

### 输出

### **Port\_1** — 随机分布值的信号 标量 | 向量 | 矩阵

具有均匀或高斯（正态）分布的随机值信号。模块对话框中的设置决定信号的大小、数据类型和复杂度。

该模块可以生成单通道或多通道信号。**Samples per frame** 参数决定信号每个通道（列）中的样本数。**Output data type** 和 **Signal complexity** 参数决定信号的数据类型和复杂度。

**数据类型：** `single` | `double`
**复数支持：** 是
## 参数
```yaml
parameters:
- name: Distribution
  summary: 均匀或高斯 Uniform（默认）| Gaussian
  group: ''
- name: Minimum
  summary: 均匀分布的最小值 0（默认）| 标量 | 行向量
  group: ''
- name: Maximum
  summary: 均匀分布的最大值 1（默认）| 标量 | 行向量
  group: ''
- name: Mean
  summary: 高斯分布的均值 0（默认）| 标量 | 行向量
  group: ''
- name: Variance
  summary: 高斯分布的方差 1（默认）| 标量 | 行向量
  group: ''
- name: Repeatability
  summary: 重复模块输出的选项 Specify seed（默认）| Not repeatable
  group: ''
- name: Initial seed
  summary: 随机数生成器的初始种子 1（默认）| 标量
  group: ''
- name: Inherit via output port
  summary: 从下游模块继承输出端口参数 off（默认）| on
  group: ''
- name: Sample time
  summary: 输出采样周期 1（默认）| −1 | 实正标量
  group: ''
- name: Samples per frame
  summary: 每个输出帧的样本数 1（默认）| 正整数
  group: ''
- name: Signal complexity
  summary: 输出的复杂度 Real（默认）| Complex
  group: ''
- name: Output data type
  summary: 输出数据类型 double（默认）| single
  group: ''
- name: Simulate using
  summary: 要运行的仿真类型 Interpreted execution（默认）| Code generation
  group: ''
```

#### 分布设置

### **Distribution** — 均匀或高斯 `Uniform`（默认）| `Gaussian`

指定从中抽取随机值的分布，为以下之一：

- `Uniform` —— 模块从均匀分布中抽取输出样本。您可以分别使用 **Minimum** 和 **Maximum** 参数指定分布的最小值和最大值。您可以通过将 **Signal complexity** 参数设置为 `Complex` 来从均匀分布生成复数。

  此 [**Minimum** **Maximum**] 范围内的所有值被选中的可能性相等。

  有关示例，请参阅 Generate Random Signal with Uniform Distribution。
- `Gaussian` —— 模块使用 Ziggurat 方法生成高斯随机值。您可以使用 **Mean** 和 **Variance** 参数指定分布的均值和方差。您可以通过将 **Signal complexity** 参数设置为 `Complex` 来生成复高斯信号。

  有关示例，请参阅 Generate Random Signal with Gaussian Distribution。

### **Minimum** — 均匀分布的最小值 `0`（默认）| 标量 | 行向量

将均匀分布中的最小值指定为标量或长度为 *N* 的行向量。当您指定行向量时，模块生成一个 *M*×*N* 矩阵，每个通道包含一个唯一的随机分布。*M* 是您在 **Samples per frame** 参数中指定的值。

例如，当您将 **Minimum** 设置为 `[0 0 -3 -3]` 并将 **Maximum** 设置为 `[10 10 20 20]` 时，模块生成一个四通道输出，其第一列和第二列包含范围 [0, 10] 内的随机值，第三列和第四列包含范围 [-3, 20] 内的随机值。

**Minimum** 和 **Maximum** 值必须是标量或具有相同的列数。当您仅将 **Minimum** 和 **Maximum** 参数之一指定为向量时，模块会扩展另一个参数使其与向量长度相同。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Distribution** 设置为 `Uniform`。

### **Maximum** — 均匀分布的最大值 `1`（默认）| 标量 | 行向量

将均匀分布中的最大值指定为标量或长度为 *N* 的行向量。当您指定行向量时，模块生成一个 *M*×*N* 矩阵，每个通道包含一个唯一的随机分布。*M* 是您在 **Samples per frame** 参数中指定的值。

例如，当您将 **Minimum** 设置为 `[0 0 -3 -3]` 并将 **Maximum** 设置为 `[10 10 20 20]` 时，模块生成一个四通道输出，其第一列和第二列包含范围 [0, 10] 内的随机值，第三列和第四列包含范围 [−3, 20] 内的随机值。

**Minimum** 和 **Maximum** 值必须是标量或具有相同的列数。当您仅将 **Minimum** 和 **Maximum** 参数之一指定为向量时，模块会扩展另一个参数使其与向量长度相同。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Distribution** 设置为 `Uniform`。

### **Mean** — 高斯分布的均值 `0`（默认）| 标量 | 行向量

将高斯（正态）分布的均值指定为标量或长度为 *N* 的行向量。当您指定行向量时，模块生成一个 *M*×*N* 矩阵，每个通道包含一个不同的随机分布。*M* 是您在 **Samples per frame** 参数中指定的值。

**Mean** 和 **Variance** 值必须是标量或具有相同的列数。当您仅将 **Mean** 和 **Variance** 参数之一指定为向量时，模块会扩展另一个参数使其与向量长度相同。

要生成具有 `Gaussian` 分布的复数输出信号，请将 **Signal complexity** 设置为 `Complex` 并在 **Mean** 参数中指定复数值。有关详细信息，请参阅 **Signal complexity** 参数说明。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Distribution** 设置为 `Gaussian`。

**复数支持：** 是

### **Variance** — 高斯分布的方差 `1`（默认）| 标量 | 行向量

将高斯（正态）分布的方差指定为标量或长度为 *N* 的行向量。当您指定行向量时，模块生成一个 *M*×*N* 矩阵，每个通道包含一个不同的随机分布。*M* 是您在 **Samples per frame** 参数中指定的值。

**Mean** 和 **Variance** 值必须是标量或具有相同的列数。当您仅将 **Mean** 和 **Variance** 参数之一指定为向量时，模块会扩展另一个参数使其与向量长度相同。

要生成具有 `Gaussian` 分布的复数输出信号，**Variance** 参数 σ2 指定每个输出通道的总方差。此值是该通道中实部和虚部分量方差之和。有关详细信息，请参阅 **Signal complexity** 参数说明。

#### 依赖关系

要启用此参数，请将 **Distribution** 设置为 `Gaussian`。

#### 随机生成器设置

### **Repeatability** — 重复模块输出的选项 `Specify seed`（默认）| `Not repeatable`

重复模块输出的选项，指定为以下之一：

- `Specify seed` —— 模块使用您在 **Initial seed** 参数中指定的初始种子，为每次仿真生成可重复的输出。
- `Not repeatable` —— 模块随机选择初始种子，并为每次仿真生成不同的伪随机序列。

有关显示此参数行为的示例，请参阅 Repeat Random Signal Output。

### **Initial seed** — 随机数生成器的初始种子 `1`（默认）| 标量

将随机数生成器的初始种子指定为标量。每次使用特定初始种子仿真模块时，生成器产生相同的伪随机数序列。

#### 依赖关系

要启用此参数，请将 **Repeatability** 设置为 `Specify seed`。

#### 信号属性

### **Inherit via output port** — 从下游模块继承输出端口参数 `off`（默认）| `on`

当您选中此复选框时，模块从下游模块继承信号属性，如每帧样本数、输出数据类型、信号复杂度和采样时间，并禁用模块对话框中的相应参数。有关示例，请参阅 Inherit Signal Properties Via Output Port。

假设您想要反向传播一个一维向量。Random Source 模块的输出是长度为 *M* 的一维向量，其中模块从下游模块继承长度 *M*。当 **Minimum**、**Maximum**、**Mean** 或 **Variance** 参数指定 *N* 个通道时，一维向量输出包含来自每个通道的 *M*/*N* 个样本。在这种情况下，当 *M* 不是 `N` 的整数倍时会发生错误。

假设您想要反向传播一个 *M*×*N* 信号。当 *N* > `1` 时，您的信号有 *N* 个通道。当 *N* = `1` 时，您的信号有 *M* 个通道。**Minimum**、**Maximum**、**Mean** 或 **Variance** 参数的值可以是标量或长度等于通道数的向量。您可以将这些参数指定为行向量或列向量，除非信号是行向量。在这种情况下，您必须将 **Minimum**、**Maximum**、**Mean** 或 **Variance** 参数指定为行向量。

### **Sample time** — 输出采样周期 `1`（默认）| −1 | 实正标量

将随机输出序列的采样周期 *T*s 指定为实正标量或 `-1`。输出帧周期为 *MT*s。

如果 *T*s = −1，模块从其输出端口继承输出采样周期，但根据模块设置确定信号的维度和复杂度。

#### 依赖关系

要启用此参数，请清除 **Inherit via output port** 参数。

### **Samples per frame** — 每个输出帧的样本数 `1`（默认）| 正整数

将每个输出帧中的样本数 *M* 指定为正整数。输出帧周期为 *MT*s，其中 *T*s 是您在 **Sample time** 参数中指定的值。

#### 依赖关系

要启用此参数，请清除 **Inherit via output port** 参数。

### **Signal complexity** — 输出的复杂度 `Real`（默认）| `Complex`

将输出的复杂度指定为 `Real` 或 `Complex`。这些设置控制输出的所有通道。输出的实部和虚部分量在统计上独立。

对于具有 `Uniform` 分布的复数输出，模块从由该通道的 **Minimum** 和 **Maximum** 参数定义的同一均匀随机分布中抽取每个通道的实部和虚部分量。

对于具有 `Gaussian` 分布的复数输出，模块从具有不同均值的正态分布中抽取每个通道的实部和虚部分量。在这种情况下，每个通道的 **Mean** 参数必须是复数值。**Mean** 参数的实部指定通道中实部分量的均值，而虚部指定通道中虚部分量的均值。当您从 **Mean** 参数中省略实部或虚部时，模块对该分量的均值使用默认值 0。

例如，**Mean** 参数设置为 `[5+2i 0.5 3i]` 会生成具有以下均值的三通道输出。

|  |  |  |
| --- | --- | --- |
| 通道 1 均值 | *实部* = 5 | *虚部* = 2 |
| 通道 2 均值 | *实部* = 0.5 | *虚部* = 0 |
| 通道 3 均值 | *实部* = 0 | *虚部* = 3 |

有关更详细的示例，请参阅 Generate Complex Random Signal。

对于复数输出，**Variance** 参数 σ2 指定每个输出通道的总方差。此值是该通道中实部和虚部分量方差之和。

σ2=σRe2+σIm2

模块将您指定的方差值平均分配给实部和虚部分量。

σRe2=σ22σIm2=σ22

#### 依赖关系

要启用此参数，请清除 **Inherit via output port** 参数。

### **Output data type** — 输出数据类型 `double`（默认）| `single`

将输出的数据类型指定为双精度或单精度。

#### 依赖关系

要启用此参数，请清除 **Inherit via output port** 参数。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

指定要运行的仿真类型。您可以将此参数设置为：

- `Interpreted execution` —— 使用 MATLAB® 解释器仿真模型。此选项缩短启动时间。
- `Code generation` —— 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 为模块生成 C 代码。只要模型不更改，C 代码将复用于后续仿真。此选项需要额外的启动时间，但提供更快的后续仿真。
## 所属库

DSP System Toolbox / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

### R2024a：Random Source 模块已更新

Random Source 模块已更新，包含以下更改：

- 支持 Mersenne Twister 随机数生成器。
- `Gaussian` 分布始终使用 Ziggurat 方法。不再支持 `Sum of uniform values` 方法。
- 移除了 `Repeatable` 选项。要生成可重复的输出，请将 **Repeatability** 设置为 `Specify seed`。
- 初始种子必须是标量。您不能再指定种子值向量。
- 当您指定初始种子时，种子不再可调，即您无法在仿真期间更改种子的值。
- 移除了 **Sample mode** 参数。模块的采样模式现在始终为离散。

如果您打开在 R2023b 或更早版本的 MATLAB 中保存的模型，该模型在 R2024a 中继续使用旧版本的模块。要使用更新版本，请从 **DSP System Toolbox**/**Sources** 库中获取 Random Source 模块。

## 描述

生成随机分布的值

Random Source 模块输出具有均匀或高斯（正态）伪随机分布的随机信号。该模块使用 Mersenne Twister 随机数生成器生成序列。模块对话框中的设置决定信号的大小、数据类型和复杂度。

该模块可以生成单通道或多通道信号。
