---
type: simulink-block
title: 'Convolution 1D Layer'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning Layers / Convolution and Fully Connected Layers'
documentation_page: 'convolution1dlayer'
documentation_source_path: 'ref/convolution1dlayer.html'
language: zh-CN
chinese_source: worker-translation
---

# Convolution 1D Layer

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入数据 二维数组
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: 卷积输出数据 二维数组
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输入

### **Port\_1** — 输入数据 二维数组

要在其上执行卷积运算的输入数据。数据必须具有两个维度，对应于使用 **Data format** 模块参数指定的格式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 卷积输出数据 二维数组

对输入数据进行卷积的结果。输出数据具有两个维度，对应于使用 **Data format** 模块参数指定的格式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## 参数
```yaml
parameters:
- name: Layer
  summary: 对应的层对象 layerObject（默认）| convolution1dLayer 对象
  group: 主要
  block_parameter: Layer
  type: workspace variable
  values: convolution1dLayer object
  default: '''layerObject'''
- name: Data format
  summary: 输入数据的格式 CT（默认）| SC
  group: 主要
  block_parameter: DataFormat
  type: character vector
  values: '''CT'' | ''SC'''
  default: '''CT'''
- name: Output minimum
  summary: 用于范围检查的最小输出值 []（默认）| 标量
  group: 数据类型
  block_parameter: OutMin
  values: '''[]''（默认）| 带引号的标量'
- name: Output maximum
  summary: 用于范围检查的最大输出值 []（默认）| 标量
  group: 数据类型
  block_parameter: OutMax
  values: '''[]''（默认）| 带引号的标量'
- name: Output data type
  summary: '输出的数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Keep MSB | Inherit: Keep LSB | Inherit: Inherit via back
    propagation | Inherit: Same as first input | Inherit: Same as accumulator | <data type expression>'
  group: 数据类型
  block_parameter: OutDataTypeStr
  values: '''Inherit: Inherit via internal rule''（默认）| ''Inherit: Keep MSB'' | ''Inherit: Keep LSB'' | ''Inherit: Inherit
    via back propagation'' | ''Inherit: Same as first input'' | ''Inherit: Same as accumulator'' | <data type expression>'
- name: Lock output data type setting against changes by the fixed-point tools
  summary: 防止定点工具覆盖 Output data type 的选项 off（默认）| on
  group: 数据类型
  block_parameter: LockScale
  values: '''off''（默认）| ''on'''
- name: Output integer rounding mode
  summary: 定点输出转换运算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型
  block_parameter: RndMeth
  values: '''Floor''（默认）| ''Ceiling'' | ''Convergent'' | ''Nearest'' | ''Round'' | ''Simplest'' | ''Zero'''
- name: Output saturate on integer overflow
  summary: 输出转换运算的溢出操作方式 off（默认）| on
  group: 数据类型
  block_parameter: SaturateOnIntegerOverflow
  values: '''off''（默认）| ''on'''
- name: Weights
  summary: '权重的数据类型 Inherit: Inherit via back propagation（默认）| Inherit: Inherit from ''Constant value'' | <data type expression>'
  group: 数据类型
  block_parameter: WeightsDataTypeStr
  values: '''Inherit: Inherit via back propagation''（默认）| ''Inherit: Inherit from ''Constant value'''' | <data type expression>'
- name: Bias
  summary: '偏置的数据类型 Inherit: Inherit via back propagation（默认）| Inherit: Inherit from ''Constant value'' | <data type expression>'
  group: 数据类型
  block_parameter: BiasDataTypeStr
  values: '''Inherit: Inherit via back propagation''（默认）| ''Inherit: Inherit from ''Constant value'''' | <data type expression>'
- name: Accumulator
  summary: '累加器的数据类型 Inherit: Inherit via internal rule（默认）| Inherit: Same as first input | <data type expression>'
  group: 数据类型
  block_parameter: AccumDataTypeStr
  values: '''Inherit: Inherit via internal rule''（默认）| ''Inherit: Same as first input'' | <data type expression>'
- name: Internal integer rounding mode
  summary: 内部定点运算的舍入模式 Floor（默认）| Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: 数据类型
  block_parameter: InternalRndMeth
  values: '''Floor''（默认）| ''Ceiling'' | ''Convergent'' | ''Nearest'' | ''Round'' | ''Simplest'' | ''Zero'''
- name: Internal saturate on integer overflow
  summary: 内部模块运算的溢出操作方式 off（默认）| on
  group: 数据类型
  block_parameter: InternalSaturateOnIntegerOverflow
  values: '''off''（默认）| ''on'''
- name: Sample time
  summary: 指定采样时间的选项 -1（默认）| 标量
  group: 执行
  block_parameter: SampleTime
  values: '''-1''（默认）| 标量'
```

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### 主要

### **Layer** — 对应的层对象 `layerObject`（默认）| `convolution1dLayer` 对象

指定包含来自训练网络的 `convolution1dLayer` 对象的工作区变量名称。Convolution 1D Layer 模块通过使用该对象的属性来配置自身，并通过使用该对象的可学习参数来计算模块输出。

#### 编程使用

|  |
| --- |
| **模块参数**：`Layer` |
| **类型**：workspace variable |
| **值**：`convolution1dLayer` object |
| **默认值**：`'layerObject'` |

### **Data format** — 输入数据的格式 `CT`（默认）| `SC`

输入数据的格式。这些选项使用与 `dlarray` 对象的 `fmt` 参数相同的表示法，但层模块不支持 Batch（`B`）维度，而是假定观测数为 `1`。

#### 编程使用

|  |
| --- |
| **模块参数**：`DataFormat` |
| **类型**：character vector |
| **值**：`'CT'` | `'SC'` |
| **默认值**：`'CT'` |

### 数据类型

### **Output minimum** — 用于范围检查的最小输出值 `[]`（默认）| 标量

软件检查的输出范围的最小值。

软件使用最小值来执行：

- 对某些模块进行参数范围检查。有关详细信息，请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)。
- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output minimum** 不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `OutMin` |
| **值**：| `'[]'`（默认）| 带引号的标量 |

### **Output maximum** — 用于范围检查的最大输出值 `[]`（默认）| 标量

软件检查的输出范围的最大值。

软件使用最大值来执行：

- 对某些模块进行参数范围检查。有关详细信息，请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)。
- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式的结果，例如 SIL 或外部模式。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `OutMax` |
| **值**：| `'[]'`（默认）| 带引号的标量 |

### **Output data type** — 输出的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Keep MSB` | `Inherit: Keep LSB` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `Inherit: Same as accumulator` | `<data type expression>`

选择输出的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象（如 `Simulink.NumericType`）。当您选择 `Inherit: Inherit via internal rule` 时，Simulink 会在考虑嵌入式目标硬件属性的同时，选择一种数据类型以平衡数值精度、性能和生成的代码大小。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `OutDataTypeStr` |
| **值**：| `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Keep MSB'` | `'Inherit: Keep LSB'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'Inherit: Same as accumulator'` | `<data type expression>` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖 Output data type 的选项 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在模块上指定的 **Output** 数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `LockScale` |
| **值**：| `'off'`（默认）| `'on'` |

### **Output integer rounding mode** — 定点输出转换运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定由最终定点转换运算生成的模块输出值的舍入模式。有关其他内部模块运算的舍入模式，请参阅 **Internal integer rounding mode**。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `RndMeth` |
| **值**：| `'Floor'`（默认）| `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Output saturate on integer overflow** — 输出转换运算的溢出操作方式 `off`（默认）| `on`

指定由最终定点转换运算生成的模块输出值在整数溢出时是饱和还是回绕。有关内部模块运算的溢出操作方式，请参阅 **Internal saturate on integer overflow**。

- `on` — 溢出饱和到该数据类型可以表示的最小值或最大值。
- `off` — 溢出回绕到该数据类型可以表示的相应值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于该最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出饱和于 127。类似地，模块输出饱和于最小输出值 –128。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。

#### 提示

- 当您的模型可能存在溢出并且您希望在生成的代码中具有显式饱和保护时，请将此参数设置为 `on`。
- 为了优化生成代码的效率，请保留此参数的默认设置 `off`。使用默认设置还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。
- 当您选择此参数时，饱和仅应用于输出或结果。
- 通常，代码生成过程可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **值**：| `'off'`（默认）| `'on'` |

### **Weights** — 权重的数据类型 `Inherit: Inherit via back propagation`（默认）| `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将您使用 **Layer** 参数指定的对象的 `Weights` 属性值转换为此数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象（如 `Simulink.NumericType`）。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `WeightsDataTypeStr` |
| **值**：| `'Inherit: Inherit via back propagation'`（默认）| `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Bias** — 偏置的数据类型 `Inherit: Inherit via back propagation`（默认）| `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将您使用 **Layer** 参数指定的对象的 `Bias` 属性值转换为此数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象（如 `Simulink.NumericType`）。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `BiasDataTypeStr` |
| **值**：| `'Inherit: Inherit via back propagation'`（默认）| `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Accumulator** — 累加器的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as first input` | `<data type expression>`

选择 Convolution 1D Layer 模块内每个 Convolution 模块的累加器的数据类型。该类型可以是继承的、直接指定的，或表示为数据类型对象（如 `Simulink.NumericType`）。当您选择 `Inherit: Inherit via internal rule` 时，Simulink 会在考虑嵌入式目标硬件属性的同时，选择一种数据类型以平衡数值精度、性能和生成的代码大小。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `AccumDataTypeStr` |
| **值**：| `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Same as first input'` | `<data type expression>` |

### **Internal integer rounding mode** — 内部定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定除输出运算之外的内部定点计算的舍入模式。有关输出运算的舍入模式，请参阅 **Output integer rounding mode**。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB 舍入函数的表达式。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `InternalRndMeth` |
| **值**：| `'Floor'`（默认）| `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Internal saturate on integer overflow** — 内部模块运算的溢出操作方式 `off`（默认）| `on`

指定模块的内部运算在整数溢出时是饱和还是回绕。有关模块输出的溢出操作方式，请参阅 **Output saturate on integer overflow**。

- `on` — 溢出饱和到该数据类型可以表示的最小值或最大值。
- `off` — 溢出回绕到该数据类型可以表示的相应值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于该最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出饱和于 127。类似地，模块输出饱和于最小输出值 –128。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。

#### 提示

- 当您的模型可能存在溢出并且您希望在生成的代码中具有显式饱和保护时，请将此参数设置为 `on`。
- 为了优化生成代码的效率，请保留此参数的默认设置 `off`。使用默认设置还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。
- 当您选择此参数时，饱和仅应用于模块的内部运算。
- 通常，代码生成过程可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **Parameter:** | `InternalSaturateOnIntegerOverflow` |
| **值**：| `'off'`（默认）| `'on'` |

### 执行

### **Sample time** — 指定采样时间的选项 `-1`（默认）| 标量

指定采样时间命中之间的离散间隔，或指定其他类型的采样时间，例如连续（`0`）或继承（`-1`）。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，模块根据其在模型中的上下文继承采样时间。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |
| --- |
| **Parameter:** `SampleTime` |
| **Data Types:** `char` |
| **值**：`'-1'`（默认）| 标量 |
## 所属库

Deep Learning Toolbox / Deep Learning Layers / Convolution and Fully Connected Layers

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

### R2025a：**Layer** 参数默认值为 `'layerObject'`

从 R2025a 开始，**Layer** 参数的默认值为 `'layerObject'`。在以前的版本中，默认值为 `'layer'`。如果您有以编程方式创建 Simulink 并依赖于名称为 `'layer'` 的变量的代码，请更新您的代码，使该变量的名称为 `'layerObject'`。

### R2025a：更新了整数舍入模式和整数溢出饱和参数

**Integer rounding mode** 和 **Saturate integer overflow** 参数现在拆分为输出版本和内部版本的参数。**Output integer rounding mode** 和 **Output saturate on integer overflow** 控制模块输出的最终强制转换操作的行为。**Internal integer rounding mode** 和 **Internal saturate on integer overflow** 控制内部模块操作。

## 描述

一维卷积层

Convolution 1D Layer 模块对一维输入应用滑动卷积滤波器。该层通过沿输入移动滤波器并计算权重与输入的点积，然后加上偏置项，对输入进行卷积。

该层进行卷积的维度取决于层输入：

- 对于 `CT` 格式（两个维度依次对应通道和时间步）的时间序列和向量序列输入，该层沿时间维度进行卷积。
- 对于 `SC` 格式（两个维度依次对应空间像素和通道）的一维图像输入，该层沿空间维度进行卷积。

`exportNetworkToSimulink` 函数生成此模块以表示 `convolution1dLayer` 对象。
