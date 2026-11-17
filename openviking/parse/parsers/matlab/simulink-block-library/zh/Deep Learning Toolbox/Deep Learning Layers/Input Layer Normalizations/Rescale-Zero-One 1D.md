---
type: simulink-block
title: 'Rescale-Zero-One 1D'
family: 'deep-learning-layers'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning Layers / Input Layer Normalizations'
documentation_page: 'rescalezeroone1d'
documentation_source_path: 'ref/rescalezeroone1d.html'
language: zh-CN
chinese_source: worker-translation
---

# Rescale-Zero-One 1D

## 端口

### 输入

### **Port\_1** — 输入数据 二维数组 | 一维数组

要归一化的输入数据。数据必须具有一个或两个维度，对应于使用 **数据格式** 参数指定的格式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 输出

### **Port\_1** — 归一化输出数据 二维数组 | 一维数组

归一化后的输出数据。输出数据具有一个或两个维度，对应于使用 **数据格式** 参数指定的格式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### 主要

### **层** — 对应的层对象 `layerObject`（默认） | `featureInputLayer` 对象 | `sequenceInputLayer` 对象

指定包含 `featureInputLayer` 或 `sequenceInputLayer` 对象的工作区变量名称，该对象来自经过训练的网络，并且其 `Normalization` 属性设置为 `"rescale-zero-one"`。Rescale-Zero-One 1D 模块使用该对象的属性自行配置，并使用该对象的 `Min` 和 `Max` 属性计算模块输出。

#### 编程用法

|  |
| --- |
| **模块参数：** `Layer` |
| **类型：** 工作区变量 |
| **值：** `featureInputLayer` 对象 | `sequenceInputLayer` 对象 |
| **默认值：** `'layerObject'` |

### **数据格式** — 输入数据的格式 `CT`（默认） | `C`

输入数据的数据格式。这些选项使用与 `dlarray` 对象的 `fmt` 参数相同的表示法，但层模块不支持 Batch (`B`) 维度，而是假定观测数为 `1`。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataFormat` |
| **类型：** 字符向量 |
| **值：** `'CT'` | `'C'` |
| **默认值：** `'CT'` |

### 数据类型

### **输出最小值** — 用于范围检查的最小输出值 `[]`（默认） | 标量

软件检查的输出范围的最小值。

软件使用该最小值执行：

- 对某些模块进行参数范围检查。有关详细信息，请参阅为模块参数指定最小值和最大值 (Simulink)。
- 仿真范围检查。有关详细信息，请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)。
- 定点数据类型的自动缩放。
- 对从模型生成的代码进行优化。此优化可能会删除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

#### 提示

**输出最小值** 不会使实际输出信号饱和或裁剪。请改用 Saturation (Simulink) 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `'[]'`（默认） | 引号中的标量 |

### **输出最大值** — 用于范围检查的最大输出值 `[]`（默认） | 标量

软件检查的输出范围的最大值。

软件使用该最大值执行：

- 对某些模块进行参数范围检查。有关详细信息，请参阅为模块参数指定最小值和最大值 (Simulink)。
- 仿真范围检查。有关详细信息，请参阅指定信号范围 (Simulink) 和启用仿真范围检查 (Simulink)。
- 定点数据类型的自动缩放。
- 对从模型生成的代码进行优化。此优化可能会删除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和最大值进行优化 (Embedded Coder)。

#### 提示

**输出最大值** 不会使实际输出信号饱和或裁剪。请改用 Saturation (Simulink) 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认） | 引号中的标量 |

### **输出数据类型** — 输出的数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Keep MSB` | `Inherit: Keep LSB` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `Inherit: Same as accumulator` | `<data type expression>`

选择输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。当选择 `Inherit: Inherit via internal rule` 时，Simulink 会选择一种数据类型，以在考虑嵌入式目标硬件属性的同时，平衡数值精度、性能和生成的代码大小。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认） | `'Inherit: Keep MSB'` | `'Inherit: Keep LSB'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'Inherit: Same as accumulator'` | `<data type expression>` |

### **锁定数据类型设置以防止定点工具更改** — 防止定点工具覆盖数据类型 `off`（默认） | `on`

选择此参数可防止定点工具覆盖您在此模块上指定的数据类型。有关详细信息，请参阅锁定输出数据类型设置 (Fixed-Point Designer)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** 字符向量 |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **输出整数舍入模式** — 定点输出转换操作的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定模块输出值的舍入模式，该输出值由最终的定点转换操作生成。有关其他内部模块操作的舍入模式，请参阅 **内部整数舍入模式**。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RndMeth` |
| **值：** | `'Floor'`（默认） | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **输出整数溢出饱和** — 输出转换操作的溢出操作方法 `off`（默认） | `on`

指定模块输出值在整数溢出时是饱和还是回绕，该输出值由最终的定点转换操作生成。有关内部模块操作的溢出操作方法，请参阅 **内部整数溢出饱和**。

- `on` — 溢出饱和到数据类型可表示的最小值或最大值。
- `off` — 溢出回绕到数据类型可表示的相应值。

例如，有符号 8 位整数 `int8` 可表示的最大值为 127。任何大于该最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出在 127 处饱和。类似地，模块输出在最小输出值 –128 处饱和。
- 清除此参数时，软件会将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。

#### 提示

- 当模型可能发生溢出并且您希望在生成的代码中提供显式饱和保护时，请将此参数设置为 `on`。
- 要优化生成代码的效率，请保留此参数的默认 `off` 设置。使用默认设置还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅排查信号范围错误 (Simulink)。
- 选中此参数时，饱和仅应用于输出或结果。
- 通常，代码生成过程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认） | `'on'` |

### **最小值** — 最小值的数据类型 `Inherit: Inherit via back propagation`（默认） | `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将使用 **层** 参数指定的对象的 `Min` 属性值转换为该数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `MinDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'`（默认） | `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **最大值** — 最大值的数据类型 `Inherit: Inherit via back propagation`（默认） | `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将使用 **层** 参数指定的对象的 `Max` 属性值转换为该数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `MaxDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'`（默认） | `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **除法输出** — 除法输出的数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

选择 Rescale-Zero-One 1D 模块内每个 Neighborhood Processing Subsystem (Simulink) 模块内的 Divide (Simulink) 模块输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。当选择 `Inherit: Inherit via internal rule` 时，Simulink 会选择一种数据类型，以在考虑嵌入式目标硬件属性的同时，平衡数值精度、性能和生成的代码大小。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `DivideOutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认） | `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### **减法最小值累加器** — SubtractMin 模块的累加器数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Same as first input` | `<data type expression>`

选择层模块内 SubtractMin 模块的数据类型。此模块从输入中减去经过训练的最小值。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。当选择 `Inherit: Inherit via internal rule` 时，Simulink 会选择一种数据类型，以在考虑嵌入式目标硬件属性的同时，平衡数值精度、性能和生成的代码大小。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SubtractMinAccumDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认） | `'Inherit: Same as first input'` | `<data type expression>` |

### **内部整数舍入模式** — 内部定点运算的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定除输出操作以外的内部定点计算的舍入模式。有关输出操作的舍入模式，请参阅 **输出整数舍入模式**。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB 舍入函数的表达式。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InternalRndMeth` |
| **值：** | `'Floor'`（默认） | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **内部整数溢出饱和** — 内部模块操作的溢出操作方法 `off`（默认） | `on`

指定模块内部操作在整数溢出时是饱和还是回绕。有关模块输出的溢出操作方法，请参阅 **输出整数溢出饱和**。

- `on` — 溢出饱和到数据类型可表示的最小值或最大值。
- `off` — 溢出回绕到数据类型可表示的相应值。

例如，有符号 8 位整数 `int8` 可表示的最大值为 127。任何大于该最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出在 127 处饱和。类似地，模块输出在最小输出值 –128 处饱和。
- 清除此参数时，软件会将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。

#### 提示

- 当模型可能发生溢出并且您希望在生成的代码中提供显式饱和保护时，请将此参数设置为 `on`。
- 要优化生成代码的效率，请保留此参数的默认 `off` 设置。使用默认设置还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅排查信号范围错误 (Simulink)。
- 选中此参数时，饱和仅应用于模块的内部操作。
- 通常，代码生成过程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InternalSaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认） | `'on'` |

### 执行

### **采样时间** — 用于指定采样时间的选项 `-1`（默认） | 标量

指定采样时间命中之间的离散间隔，或指定其他类型的采样时间，如连续 (`0`) 或继承 (`-1`)。有关更多选项，请参阅采样时间的类型 (Simulink)。

默认情况下，模块根据模型中模块的上下文继承其采样时间。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

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

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

### R2025a：**层** 参数默认值为 `'layerObject'`

从 R2025a 开始，**层** 参数的默认值为 `'layerObject'`。在以前的版本中，默认值为 `'layer'`。如果您的代码以编程方式创建 Simulink 并依赖名称为 `'layer'` 的变量，请更新代码，使该变量的名称为 `'layerObject'`。

### R2025a：更新了整数舍入模式、整数溢出饱和和累加器参数

**整数舍入模式** 和 **整数溢出饱和** 参数现在拆分为输出和内部版本的参数。**输出整数舍入模式** 和 **输出整数溢出饱和** 控制模块输出的最终转换操作的行为。**内部整数舍入模式** 和 **内部整数溢出饱和** 控制内部模块操作。

新增的 **减法最小值累加器** 参数控制层模块内累加器的数据类型。

## 描述

具有 rescale-zero-one 归一化的一维输入层

Rescale-Zero-One 1D 模块将一维数据输入神经网络，并将输入重新缩放到 [0, 1] 范围内。

输入数据可以具有仅包含通道数据的单一维度，也可以具有两个维度，分别对应通道数据和时间步，且按此顺序排列。

`exportNetworkToSimulink` 函数生成此模块以表示 `featureInputLayer` 或 `sequenceInputLayer` 对象，该对象的 `Normalization` 属性设置为 `"rescale-zero-one"`。
