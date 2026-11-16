---
type: simulink-block
title: 'Zerocenter 1D'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning with Simulink / Input Layer Normalizations'
documentation_page: 'zerocenter1d'
documentation_source_path: 'ref/zerocenter1d.html'
language: zh-CN
chinese_source: worker-translation
---

# Zerocenter 1D

## 端口

### 输入

### **Port\_1** — 输入数据 二维数组 | 一维数组

要归一化的输入数据。数据必须具有一个或两个维度，对应于使用 **Data format** 参数指定的格式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 归一化输出数据 二维数组 | 一维数组

归一化输出数据。输出数据具有一个或两个维度，对应于使用 **Data format** 参数指定的格式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条上的 **Simulation** 选项卡中，在 **Prepare** 库中选择 **Property Inspector**。

### 主要

### **Layer** — 对应的层对象 `layerObject`（默认） | `featureInputLayer` 对象 | `sequenceInputLayer` 对象

指定一个工作区变量的名称，该变量包含来自已训练网络的 `featureInputLayer` 或 `sequenceInputLayer` 对象，并且其 `Normalization` 属性设置为 `"zerocenter"`。Zerocenter 1D 模块使用该对象的属性来配置自身，并使用该对象的 `Mean` 属性计算模块输出。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Layer` |
| **类型：** 工作区变量 |
| **值：** `featureInputLayer` 对象 | `sequenceInputLayer` 对象 |
| **默认值：** `'layerObject'` |

### **Data format** — 输入数据的格式 `CT`（默认） | `C`

输入数据的数据格式。这些选项使用与 `dlarray` 对象的 `fmt` 参数相同的表示法，不同之处在于层模块不支持 Batch（`B`）维度，而是假定观测数量为 `1`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DataFormat` |
| **类型：** 字符向量 |
| **值：** `'CT'` | `'C'` |
| **默认值：** `'CT'` |

### 数据类型

### **Output minimum** — 用于范围检查的最小输出值 `[]`（默认） | 标量

软件检查的输出范围的最小值。

软件使用最小值来执行：

- 对某些模块进行参数范围检查。有关详细信息，请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)。
- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges (Simulink) 和
  Enable Simulation Range Checking (Simulink)。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output minimum** 不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `'[]'`（默认） | 带引号的标量 |

### **Output maximum** — 用于范围检查的最大输出值 `[]`（默认） | 标量

软件检查的输出范围的最大值。

软件使用最大值来执行：

- 对某些模块进行参数范围检查。有关详细信息，请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)。
- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges (Simulink) 和
  Enable Simulation Range Checking (Simulink)。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可能会移除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认） | 带引号的标量 |

### **Output data type** — 输出的数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Keep MSB` | `Inherit: Keep LSB` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `Inherit: Same as accumulator` | `<data type expression>`

选择输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，如 `Simulink.NumericType`。当选择 `Inherit: Inherit via internal rule` 时，Simulink 会选择一种数据类型来平衡数值精度、性能和生成的代码大小，同时考虑嵌入式目标硬件的属性。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认） | `'Inherit: Keep MSB'` | `'Inherit: Keep LSB'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'Inherit: Same as accumulator'` | `<data type expression>` |

### **Lock output data type setting against changes by the fixed-point tools** — 防止定点工具覆盖 Output data type 的选项 `off`（默认） | `on`

选择此参数可防止定点工具覆盖你在模块上指定的 **Output** 数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `LockScale` |
| **值：** | `'off'`（默认） | `'on'` |

### **Output integer rounding mode** — 定点输出转换操作的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定由最终定点转换操作生成的模块输出值的舍入模式。有关其他内部模块操作的舍入模式，请参阅 **Internal integer rounding mode**。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RndMeth` |
| **值：** | `'Floor'`（默认） | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Output saturate on integer overflow** — 输出转换操作的溢出动作方法 `off`（默认） | `on`

指定由最终定点转换操作生成的模块输出值在整数溢出时是饱和还是回绕。有关内部模块操作的溢出动作方法，请参阅 **Internal saturate on integer overflow**。

- `on` — 溢出饱和到该数据类型可表示的最小值或最大值。
- `off` — 溢出回绕到该数据类型可表示的相应值。

例如，有符号 8 位整数 `int8` 可表示的最大值是 127。任何大于最大值的模块操作结果都会导致 8 位整数溢出。

- 选择此参数时，模块输出在 127 处饱和。类似地，模块输出在最小输出值 –128 处饱和。
- 清除此参数时，软件会将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。

#### 提示

- 当你的模型可能发生溢出，并且你希望在生成的代码中具有显式饱和保护时，将此参数设置为 `on`。
- 为了优化生成代码的效率，请为此参数保留默认的 `off` 设置。使用默认设置还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。
- 选择此参数时，饱和仅适用于输出或结果。
- 通常，代码生成过程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认） | `'on'` |

### **Mean** — Mean 的数据类型 `Inherit: Inherit via back propagation`（默认） | `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将使用 **Layer** 参数指定的对象的 `Mean` 属性值转换为该数据类型。该类型可以继承、直接指定，或表示为数据类型对象，如 `Simulink.NumericType`。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `MeanDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'`（默认） | `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Accumulator** — 累加器的数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Same as first input` | `<data type expression>`

选择累加器的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，如 `Simulink.NumericType`。当选择 `Inherit: Inherit via internal rule` 时，Simulink 会选择一种数据类型来平衡数值精度、性能和生成的代码大小，同时考虑嵌入式目标硬件的属性。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `AccumDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认） | `'Inherit: Same as first input'` | `<data type expression>` |

### **Internal integer rounding mode** — 内部定点操作的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定除输出操作之外的内部定点计算的舍入模式。有关输出操作的舍入模式，请参阅 **Output integer rounding mode**。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB 舍入函数的表达式。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InternalRndMeth` |
| **值：** | `'Floor'`（默认） | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Internal saturate on integer overflow** — 内部模块操作的溢出动作方法 `off`（默认） | `on`

指定模块内部操作在整数溢出时是饱和还是回绕。有关模块输出的溢出动作方法，请参阅 **Output saturate on integer overflow**。

- `on` — 溢出饱和到该数据类型可表示的最小值或最大值。
- `off` — 溢出回绕到该数据类型可表示的相应值。

例如，有符号 8 位整数 `int8` 可表示的最大值是 127。任何大于最大值的模块操作结果都会导致 8 位整数溢出。

- 选择此参数时，模块输出在 127 处饱和。类似地，模块输出在最小输出值 –128 处饱和。
- 清除此参数时，软件会将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。

#### 提示

- 当你的模型可能发生溢出，并且你希望在生成的代码中具有显式饱和保护时，将此参数设置为 `on`。
- 为了优化生成代码的效率，请为此参数保留默认的 `off` 设置。使用默认设置还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。
- 选择此参数时，饱和仅适用于模块的内部操作。
- 通常，代码生成过程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InternalSaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认） | `'on'` |

### 执行

### **Sample time** — 用于指定采样时间的选项 `-1`（默认） | 标量

指定采样时间命中之间的离散间隔，或指定另一种采样时间类型，例如连续（`0`）或继承（`-1`）。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，模块根据模型内模块的上下文继承其采样时间。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |
| --- |
| **参数：** `SampleTime` |
| **数据类型：** `char` |
| **值：** `'-1'`（默认） | 标量 |

## 所属库

Deep Learning Toolbox / Deep Learning Layers / Input Layer Normalizations

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

### R2025a: **Layer** 参数默认值为 `'layerObject'`

从 R2025a 开始，**Layer** 参数的默认值为 `'layerObject'`。在之前的版本中，默认值为 `'layer'`。如果你有以程序化方式创建 Simulink 并依赖于名称为 `'layer'` 的变量的代码，请更新代码，使该变量名称为 `'layerObject'`。

### R2025a: 更新了整数舍入模式、整数溢出饱和和累加器参数

**Integer rounding mode** 和 **Saturate integer overflow** 参数现在拆分为参数的输出版本和内部版本。**Output integer rounding mode** 和 **Output saturate on integer overflow** 控制模块输出的最终转换操作的行为。**Internal integer rounding mode** 和 **Internal saturate on integer overflow** 控制内部模块操作。

新的 **Accumulator** 参数控制层模块内累加器的数据类型。

## 描述

带 zerocenter 归一化的一维输入层

Zerocenter 1D 模块将一维数据输入神经网络，并通过减去传入模块的层对象的 `Mean` 属性值来重新缩放输入。

输入数据可以仅具有通道数据的单个维度，也可以具有两个维度，分别按顺序对应通道数据和时间步。

`exportNetworkToSimulink` 函数生成此模块，以表示 `Normalization` 属性设置为 `"zerocenter"` 的 `featureInputLayer` 或 `sequenceInputLayer` 对象。
