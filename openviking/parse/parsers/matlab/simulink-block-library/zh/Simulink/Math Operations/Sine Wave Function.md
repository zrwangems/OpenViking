---
type: simulink-block
title: 'Sine Wave Function'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'sinewavefunction'
documentation_source_path: 'slref/sinewavefunction.html'
language: zh-CN
chinese_source: worker-translation
---

# Sine Wave Function

## 端口
```yaml
ports:
- name: Port_1
  summary: 时间源信号 标量
  direction: input
  data_types: double
- name: Output 1
  summary: 输出正弦波信号 标量
  direction: output
  data_types: double
```

### 输入

### **Port\_1** — 时间源信号 标量

表示正弦波计算中时间源的输入信号。

**数据类型：** `double`
### 输出

### **Output 1** — 输出正弦波信号 标量

生成的正弦波的输出信号。

**数据类型：** `double`
## 参数
```yaml
parameters:
- name: Sine type
  summary: 正弦波类型 Time based（默认）| Sample based
  group: ''
  block_parameter: SineType
  type: character vector
  values: '''Time based'' | ''Sample based'''
  default: '''Time based'''
- name: Time (t)
  summary: 时间变量来源 Use external signal（默认）| Use simulation time
  group: ''
  block_parameter: TimeSource
  type: character vector
  values: '''Use simulation time'' | ''Use external signal'''
  default: '''Use external signal'''
- name: Amplitude
  summary: 正弦波幅值 1（默认）| 标量
  group: ''
  block_parameter: Amplitude
  type: character vector
  values: scalar
  default: '''1'''
- name: Bias
  summary: 添加到正弦波的常量 0（默认）| 标量
  group: ''
  block_parameter: Bias
  type: character vector
  values: scalar
  default: '''0'''
- name: Frequency (rad/sec)
  summary: 正弦波频率 1（默认）| 标量
  group: ''
  block_parameter: Frequency
  type: character vector
  values: scalar
  default: '''1'''
- name: Phase (rad)
  summary: 正弦波相移 0（默认）| 标量
  group: ''
  block_parameter: Phase
  type: character vector
  values: scalar
  default: '''0'''
- name: Samples per period
  summary: 每周期采样数 0（默认）| integer
  group: ''
  block_parameter: Samples
  type: character vector
  values: scalar
  default: '''10'''
- name: Number of offset samples
  summary: 时间采样数偏移 0（默认）| integer
  group: ''
  block_parameter: Offset
  type: character vector
  values: scalar
  default: '''0'''
- name: Sample time
  summary: 采样周期 0（默认）| 标量
  group: ''
  block_parameter: SampleTime
  type: character vector
  values: scalar
  default: '''0'''
- name: Interpret vector parameters as 1-D
  summary: 单行或单列矩阵的输出维度 off（默认）| on
  group: ''
  block_parameter: VectorParams1D
  type: character vector
  values: '''off'' | ''on'''
  default: '''on'''
```

### **Sine type** — 正弦波类型 `Time based`（默认）| `Sample based`

指定此模块生成的正弦波类型。对话框中的某些参数会根据您选择基于时间还是基于采样而显示。

#### 编程使用

|  |
| --- |
| **模块参数**：`SineType` |
| **类型**：character vector |
| **值**：`'Time based'` | `'Sample based'` |
| **默认值**：`'Time based'` |

### **Time (t)** — 时间变量来源 `Use external signal`（默认）| `Use simulation time`

指定是将仿真时间还是外部源作为时间变量的值来源。如果指定外部时间源，模块将为时间源创建一个输入端口。

#### 编程使用

|  |
| --- |
| **模块参数**：`TimeSource` |
| **类型**：character vector |
| **值**：`'Use simulation time'` | `'Use external signal'` |
| **默认值**：`'Use external signal'` |

### **Amplitude** — 正弦波幅值 `1`（默认）| 标量

指定输出正弦波信号的幅值。

#### 编程使用

|  |
| --- |
| **模块参数**：`Amplitude` |
| **类型**：character vector |
| **Value**: scalar |
| **默认值**：`'1'` |

### **Bias** — 添加到正弦波的常量 `0`（默认）| 标量

指定添加到正弦波以产生输出的常量值。

#### 编程使用

|  |
| --- |
| **模块参数**：`Bias` |
| **类型**：character vector |
| **Value**: scalar |
| **默认值**：`'0'` |

### **Frequency (rad/sec)** — 正弦波频率 `1`（默认）| 标量

指定频率，以弧度每秒为单位。

#### 依赖关系

要启用此参数，请将 **Sine type** 设置为 `Time based`。

#### 编程使用

|  |
| --- |
| **模块参数**：`Frequency` |
| **类型**：character vector |
| **Value**: scalar |
| **默认值**：`'1'` |

### **Phase (rad)** — 正弦波相移 `0`（默认）| 标量

指定正弦波的相移。

如果将 **Time (t)** 设置为 `Use simulation time`，则无法将此参数配置为在生成的代码中显示为可调全局变量。例如，如果将 **Default parameter behavior** 设置为 `Tunable` 或将存储类应用于 `Simulink.Parameter` 对象，则 **Phase** 参数不会在生成的代码中显示为可调全局变量。

要生成可在执行期间调整相位的代码，请将 **Time (t)** 设置为 `Use external signal`。您可以提供自己的时间输入信号，或使用 Digital Clock 模块生成时间信号。有关示例，请参阅 Tune Phase Parameter of Sine Wave Block During Code Execution (Simulink Coder)。

#### 依赖关系

要启用此参数，请将 **Sine type** 设置为 `Time based`。

#### 编程使用

|  |
| --- |
| **模块参数**：`Phase` |
| **类型**：character vector |
| **Value**: scalar |
| **默认值**：`'0'` |

### **Samples per period** — 每周期采样数 `0`（默认）| `integer`

指定每周期的采样数。

#### 依赖关系

要启用此参数，请将 **Sine type** 设置为 `Sample based`。

#### 编程使用

|  |
| --- |
| **模块参数**：`Samples` |
| **类型**：character vector |
| **Value**: scalar |
| **默认值**：`'10'` |

### **Number of offset samples** — 时间采样数偏移 `0`（默认）| `integer`

指定以采样时间数表示的偏移（离散相移）。

#### 依赖关系

要启用此参数，请将 **Sine type** 设置为 `Sample based`。

#### 编程使用

|  |
| --- |
| **模块参数**：`Offset` |
| **类型**：character vector |
| **Value**: scalar |
| **默认值**：`'0'` |

### **Sample time** — 采样周期 `0`（默认）| 标量

指定采样周期，以秒为单位。默认值为 `0`。如果正弦类型为基于采样，则采样时间必须大于 0。请参阅 Specify Sample Time。

#### 编程使用

|  |
| --- |
| **模块参数**：`SampleTime` |
| **类型**：character vector |
| **Value**: scalar |
| **默认值**：`'0'` |

### **Interpret vector parameters as 1-D** — 单行或单列矩阵的输出维度 `off`（默认）| `on`

当其他参数为单行和单列矩阵时，指定输出维度为 1-D 向量信号。如果未选中此框，模块将输出与数值参数维度相同的信号。请参阅 Determine the Output Dimensions of Source Blocks。当外部信号指定时间时，此参数不可用。在这种情况下，如果数值参数为列或行矩阵值，则输出为 1-D 向量。

#### 编程使用

|  |
| --- |
| **模块参数**：`VectorParams1D` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |
## 所属库

Simulink / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

当置于触发子系统层次结构中时，依赖于绝对时间。这些模块在配置为基于采样操作时不引用绝对时间。在基于时间操作时，它们依赖于绝对时间。

## 版本历史

**在 R2006a 之前引入**

## 描述

使用外部信号作为时间源生成正弦波

Sine Wave Function 模块输出正弦波形。该模块可以基于时间或基于采样模式运行。

**注意**

此模块与 Math Operations 库中出现的 Sine Wave 模块相同。如果在模块对话框中将 **Time** 参数选择为 `Use simulation time`，则得到的是 Sine Wave Function 模块。

### 基于时间模式

模块计算输出波形。

y=amplitude×sin(frequency×time+phase)+bias。

在基于时间模式下，**Sample time** 参数的值决定模块以连续模式还是离散模式运行。

- `0`（默认值）使模块以连续模式运行。
- `>0` 使模块以离散模式运行。

有关详细信息，请参阅 Specify Sample Time。

**连续模式下的模块行为**

在连续模式下运行时，Sine Wave 模块可能因时间变得非常大时精度损失而变得不准确。

**离散模式下的模块行为**

**Sample time** 参数值大于零会使模块的行为如同驱动一个采样时间设置为该值的 Zero-Order Hold 模块。

这样，您可以构建具有纯离散正弦波源的模型，而不是混合连续/离散系统的模型。混合系统本质上更复杂，因此仿真需要更多时间。

在离散模式下，此模块使用差分增量算法，而不是基于绝对时间的算法。因此，该模块可用于打算无限期运行的模型，例如振动或疲劳测试。

差分增量算法基于前一个采样时间计算的值来计算正弦。此方法使用以下三角恒等式：

sin(t+Δt)=sin(t)cos(Δt)+sin(Δt)cos(t)cos(t+Δt)=cos(t)cos(Δt)−sin(t)sin(Δt)

以矩阵形式表示，这些恒等式为：

[sin(t+Δt)cos(t+Δt)]=[cos(Δt)sin(Δt)−sin(Δt)cos(Δt)][sin(t)cos(t)]

因为 Δ*t* 是常量，以下表达式是常量：

[cos(Δt)sin(Δt)−sin(Δt)cos(Δt)]

因此，问题变为将 sin(t) 的值与常量矩阵相乘得到 sin(t+Δt) 的矩阵乘法问题。

离散模式减少但不会消除舍入误差的累积，例如 `(4*eps)`。这种累积可能发生，因为每个时间步的模块输出计算依赖于前一个时间步的输出值。

**处理离散模式下舍入误差的方法**

要在 Sine Wave 模块以基于时间离散模式运行时处理舍入误差，请使用以下方法之一。

| 方法 | 理由 |
| --- | --- |
| 在 Sine Wave 模块的直接下游插入一个 Saturation 模块。 | 通过对 Sine Wave 模块输出设置饱和限值，可以消除因舍入误差累积导致的过冲。 |
| 设置 Sine Wave 模块使用 `sin()` 数学库函数来计算模块输出。  1. 在 Sine Wave 模块对话框中，将    **Time** 设置为 `Use    external signal`，使模块图标上出现一个输入   端口。 2. 使用    Digital    Clock 模块将时钟信号连接到此输入端口。 3. 将时钟信号的采样时间设置为    Sine Wave 模块的采样时间。 | `sin()` 数学库函数在每个时间步*独立*于其他时间步的输出值计算模块输出，防止舍入误差的累积。 |

### 基于采样模式

基于采样模式使用以下公式计算 Sine Wave 模块的输出。

y=Asin(2π(k+o)/p)+b

- *A* 是正弦波的幅值。
- *p* 是每个正弦波周期的采样数。
- *k* 是一个重复的整数值，范围从 0 到 *p*–1。
- *o* 是信号的偏移（相移）。
- *b* 是信号偏置。

在此模式下，Simulink® 在第一个时间步将 *k* 设置为 `0`，并使用公式计算模块输出。在下一个时间步，Simulink 递增 *k* 并重新计算模块输出。当 *k* 达到 *p* 时，Simulink 在计算模块输出之前将 *k* 重置为 `0`。此过程持续到仿真结束。

基于采样的方法在给定时间步计算模块输出不依赖于前一个时间步的输出。因此，此模式避免了舍入误差的累积。基于采样模式支持提供重置语义的子系统中的重置语义。例如，如果 Sine Wave 模块位于接收重置触发的可重置子系统中，则重复整数 `k` 重置，模块输出重置为其初始条件。
