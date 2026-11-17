---
type: simulink-block
title: 'Rescale-Zero-One 2D'
family: 'deep-learning-layers'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning Layers / Input Layer Normalizations'
documentation_page: 'rescalezeroone2d'
documentation_source_path: 'ref/rescalezeroone2d.html'
language: zh-CN
chinese_source: worker-translation
---

# Rescale-Zero-One 2D

## 端口

### 输入

### **Port\_1** — 输入数据 3 维数组

要归一化的输入数据。数据必须具有三个维度，依次对应两个空间维度和一个通道维度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 归一化输出数据 3 维数组

归一化输出数据。输出数据具有三个维度，依次对应两个空间维度和一个通道维度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

要交互式编辑模块参数，请使用
Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在
**Prepare** 库中，选择 **Property
Inspector**。

### 主要

### **Layer** — 对应层对象 `layerObject` (默认) | `imageInputLayer` 对象

指定工作区变量的名称，该变量包含一个
`imageInputLayer` 对象，该对象来自训练后的网络，并且其
`Normalization` 属性设置为
`"rescale-zero-one"`。Rescale-Zero-One 2D 模块
使用该对象的属性配置自身，并使用该对象的 `Min` 和 `Max` 属性
计算模块输出。

#### 编程用法

|  |
| --- |
| **模块参数：** `Layer` |
| **类型：** 工作区变量 |
| **值：** `imageInputLayer` 对象 |
| **默认值：** `'layerObject'` |

### **Data format** — 输入数据的格式 `SSC` (默认)

输入数据的数据格式。选项使用的表示法与
`dlarray` 对象的 `fmt` 参数相同，但层模块不支持 Batch
(`B`) 维度，而是假定观测编号为
`1`。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataFormat` |
| **类型：** character vector |
| **值：** `'SSC'` |
| **默认值：** `'SSC'` |

### 数据类型

### **Output minimum** — 用于范围检查的最小输出值 `[]` (默认) | scalar

软件检查的输出范围的最小值。

软件使用最小值执行以下操作：

- 对某些模块进行参数范围检查。有关详细信息，请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)。
- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges (Simulink) 和
  Enable Simulation Range Checking (Simulink)。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可以移除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅
  Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output minimum** 不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `'[]'` (默认) | scalar in quotes |

### **Output maximum** — 用于范围检查的最大输出值 `[]` (默认) | scalar

软件检查的输出范围的最大值。

软件使用最大值执行以下操作：

- 对某些模块进行参数范围检查。有关详细信息，请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)。
- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges (Simulink) 和
  Enable Simulation Range Checking (Simulink)。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可以移除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅
  Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**Output maximum** 不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'` (默认) | scalar in quotes |

### **Output data type** — 输出的数据类型 `Inherit: Inherit via internal rule` (默认) | `Inherit: Keep MSB` | `Inherit: Keep LSB` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `Inherit: Same as accumulator` | `<data type expression>`

选择输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。当选择 `Inherit: Inherit via internal rule` 时，
Simulink 会选择一种数据类型来平衡数值精度、性能和生成代码大小，同时考虑嵌入式目标硬件的属性。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'` (默认) | `'Inherit: Keep MSB'` | `'Inherit: Keep LSB'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'Inherit: Same as accumulator'` | `<data type expression>` |

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您在此模块上指定的数据类型。有关详细信息，请参阅 Lock the Output Data Type Setting (Fixed-Point Designer)。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |
| --- |
| **模块参数：** `LockScale` |
| **类型：** character vector |
| **值：** `'off' | 'on'` |
| **默认值：** `'off'` |

### **Output integer rounding mode** — 定点输出转换操作的舍入模式 `Floor` (默认) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定由最终定点转换操作生成的模块输出值的舍入模式。有关其他内部模块操作的舍入模式，请参阅 **Internal integer rounding mode**。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RndMeth` |
| **值：** | `'Floor'` (默认) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Output saturate on integer overflow** — 输出转换操作的溢出操作方式 `off` (默认) | `on`

指定由最终定点转换操作生成的模块输出值在整数溢出时饱和还是绕回。有关内部模块操作的溢出操作方式，请参阅 **Internal saturate on integer overflow**。

- `on` — 溢出饱和到数据类型可以表示的最小值或最大值。
- `off` — 溢出绕回到数据类型可以表示的相应值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于最大值的模块操作结果都会导致 8 位整数溢出。

- 选择此参数后，模块输出饱和于 127。
  类似地，模块输出饱和于最小输出值 –128。
- 清除此参数后，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。
  例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。

#### 提示

- 当您的模型可能发生溢出，并且您希望在生成代码中显式提供饱和保护时，请将此参数设置为 `on`。
- 为了优化生成代码的效率，请保留此参数的默认设置 `off`。使用默认设置还有助于避免过度指定模块处理超范围信号的方式。有关详细信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。
- 选择此参数时，饱和仅应用于输出或结果。
- 通常，代码生成过程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `'off'` (默认) | `'on'` |

### **Min** — 最小值的数据类型 `Inherit: Inherit via back propagation` (默认) | `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将使用 **Layer** 参数指定的对象的 `Min` 属性值转换为该数据类型。
该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `MinDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'` (默认) | `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Max** — 最大值的数据类型 `Inherit: Inherit via back propagation` (默认) | `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将使用 **Layer** 参数指定的对象的 `Max` 属性值转换为该数据类型。
该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `MaxDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'` (默认) | `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **Divide output** — 除法输出的数据类型 `Inherit: Inherit via internal rule` (默认) | `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

选择 Rescale Zero-One-2D 模块内每个 Neighborhood Processing Subsystem (Simulink) 模块内部的 Divide (Simulink) 模块输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。当选择 `Inherit: Inherit via internal rule` 时，
Simulink 会选择一种数据类型来平衡数值精度、性能和生成代码大小，同时考虑嵌入式目标硬件的属性。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `DivideOutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'` (默认) | `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### **Subtract Min Accumulator** — SubtractMin 模块的累加器数据类型 `Inherit: Inherit via internal rule` (默认) | `Inherit: Same as first input` | `<data type expression>`

选择层模块内 SubtractMin 模块的数据类型。
此模块从输入中减去训练得到的最小值。该类型可以继承、直接指定，或表示为数据类型对象（如 `Simulink.NumericType`）。当选择 `Inherit: Inherit via internal rule` 时，
Simulink 会选择一种数据类型来平衡数值精度、性能和生成代码大小，同时考虑嵌入式目标硬件的属性。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SubtractMinAccumDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'` (默认) | `'Inherit: Same as first input'` | `<data type expression>` |

### **Internal integer rounding mode** — 内部定点运算的舍入模式 `Floor` (默认) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定除输出操作之外的内部定点计算的舍入模式。有关输出操作的舍入模式，请参阅 **Output integer rounding mode**。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB 舍入函数的表达式。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InternalRndMeth` |
| **值：** | `'Floor'` (默认) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Internal saturate on integer overflow** — 内部模块操作的溢出操作方式 `off` (默认) | `on`

指定模块的内部操作在整数溢出时饱和还是绕回。有关模块输出的溢出操作方式，请参阅 **Output saturate on integer overflow**。

- `on` — 溢出饱和到数据类型可以表示的最小值或最大值。
- `off` — 溢出绕回到数据类型可以表示的相应值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于最大值的模块操作结果都会导致 8 位整数溢出。

- 选择此参数后，模块输出饱和于 127。
  类似地，模块输出饱和于最小输出值 –128。
- 清除此参数后，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。
  例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。

#### 提示

- 当您的模型可能发生溢出，并且您希望在生成代码中显式提供饱和保护时，请将此参数设置为 `on`。
- 为了优化生成代码的效率，请保留此参数的默认设置 `off`。使用默认设置还有助于避免过度指定模块处理超范围信号的方式。有关详细信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。
- 选择此参数时，饱和仅应用于模块的内部操作。
- 通常，代码生成过程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

要以编程方式设置模块参数值，请使用
`set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InternalSaturateOnIntegerOverflow` |
| **值：** | `'off'` (默认) | `'on'` |

### 执行

### **Sample time** — 用于指定采样时间的选项 `-1` (默认) | scalar

指定采样时间命中之间的离散间隔，或指定其他类型的采样时间，如连续 (`0`) 或继承 (`-1`)。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，模块根据其在模型中的上下文继承采样时间。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |
| --- |
| **参数：** `SampleTime` |
| **数据类型：** `char` |
| **值：** `'-1'` (默认) | scalar |

## 所属库

Deep Learning Toolbox / Deep Learning Layers / Input Layer Normalizations

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

### R2025a: **Layer** 参数默认值为 `'layerObject'`

从 R2025a 开始，**Layer** 参数的默认值为 `'layerObject'`。在以前的版本中，默认值为 `'layer'`。如果您有以编程方式创建 Simulink 并依赖名为 `'layer'` 的变量的代码，请更新代码，使该变量名为 `'layerObject'`。

### R2025a: 更新了整数舍入模式、整数溢出时饱和和累加器参数

**Integer rounding mode** 和 **Saturate integer overflow** 参数现在拆分为输出和内部版本的参数。**Output integer rounding mode** 和 **Output saturate on integer overflow** 控制模块输出的最终转换操作的行为。**Internal integer rounding mode** 和 **Internal saturate on integer overflow** 控制内部模块操作。

新的 **Subtract Min Accumulator** 参数控制层模块内累加器的数据类型。

## 描述

具有 rescale-zero-one 归一化的 2-D 输入层

Rescale-Zero-One 2D 模块将 2 维图像数据（数据具有三个维度，依次对应两个空间维度和一个通道维度）输入到神经网络，并将输入重新缩放至范围 [0, 1]。

`exportNetworkToSimulink` 函数生成此模块以表示一个 `imageInputLayer`
对象，该对象的 `Normalization` 属性设置为
`"rescale-zero-one"`。
