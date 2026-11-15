---
type: simulink-block
title: 'Zscore 3D'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning with Simulink / Input Layer Normalizations'
documentation_page: 'zscore3d'
documentation_source_path: 'ref/zscore3d.html'
language: zh-CN
chinese_source: worker-translation
---

# Zscore 3D

## 端口

### 输入

### **Port\_1** — 输入数据 4 维数组

要归一化的输入数据。数据必须具有四个维度，对应于三个空间维度和一个通道维度，按该顺序。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 归一化输出数据 4 维数组

归一化输出数据。输出数据具有四个维度，对应于三个空间维度和一个通道维度，按该顺序。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。从 Simulink® 工具条，在 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### 主要

### **Layer** — 对应层对象 `layerObject`（默认）| `image3dInputLayer` 对象

指定包含 `image3dInputLayer` 对象的工作区变量名称，该对象来自经过训练的网络，并且其 `Normalization` 属性设置为 `"zscore"`。Zscore 3D 模块通过使用该对象的属性来配置自身，并通过使用该对象的 `Mean` 和 `StandardDeviation` 属性来计算模块输出。

#### 程序化使用

|  |
| --- |
| **模块参数：** `Layer` |
| **类型：** 工作区变量 |
| **值：** `image3dInputLayer` 对象 |
| **默认：** `'layerObject'` |

### **数据格式** — 输入数据的格式 `SSSC`（默认）

输入数据的数据格式。这些选项使用与 `dlarray` 对象的 `fmt` 参数相同的表示法，不同之处在于层模块不支持 Batch (`B`) 维度，而是假设观测数为 `1`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DataFormat` |
| **类型：** 字符向量 |
| **值：** `'SSSC'` |
| **默认：** `'SSSC'` |

### 数据类型

### **输出最小值** — 用于范围检查的最小输出值 `[]`（默认）| 标量

软件检查的输出范围的最小值。

软件使用最小值来执行：

- 对某些模块进行参数范围检查。有关详细信息，请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)。
- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**输出最小值** 不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **输出最大值** — 用于范围检查的最大输出值 `[]`（默认）| 标量

软件检查的输出范围的最大值。

软件使用最大值来执行：

- 对某些模块进行参数范围检查。有关详细信息，请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)。
- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)。
- 定点数据类型的自动定标。
- 优化从模型生成的代码。此优化可以移除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**输出最大值** 不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认）| 带引号的标量 |

### **输出数据类型** — 输出的数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

选择输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。当您选择 `Inherit: Inherit via internal rule` 时，Simulink 会选择一种数据类型，以平衡数值精度、性能和生成代码大小，同时考虑嵌入式目标硬件的属性。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认）| `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### **锁定输出数据类型设置以防止定点工具更改** — 防止定点工具覆盖输出数据类型的选项 `off`（默认）| `on`

选择此参数可防止定点工具覆盖您在模块上指定的 **Output** 数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `LockScale` |
| **值：** | `'off'`（默认）| `'on'` |

### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RndMeth` |
| **值：** | `'Floor'`（默认）| `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **整数溢出时饱和** — 溢出操作的方法 `off`（默认）| `on`

指定整数溢出是饱和还是回绕。

- `on` — 溢出饱和到数据类型可表示的最小值或最大值。
- `off` — 溢出回绕到数据类型可表示的相应值。

例如，有符号 8 位整数 `int8` 可表示的最大值是 127。任何大于最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出在 127 处饱和。类似地，模块输出在最小输出值 –128 处饱和。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 是 –126。

#### 提示

- 当您的模型可能发生溢出并且您希望在生成代码中提供显式饱和保护时，请将此参数设置为 `on`。
- 要优化生成代码的效率，请保留此参数的默认设置 `off`。使用默认设置还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。
- 选中此参数时，饱和适用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测何时不可能发生溢出。在这种情况下，代码生成器不生成饱和代码。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认）| `'on'` |

### **Mean** — 均值的数据类型 `Inherit: Inherit via back propagation`（默认）| `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将您使用 **Layer** 参数指定的对象的 `Mean` 属性值转换为该数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `MeanDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'`（默认）| `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### **标准差** — 标准差的数据类型 `Inherit: Inherit via back propagation`（默认）| `Inherit: Inherit from 'Constant value'` | `<data type expression>`

模块将您使用 **Layer** 参数指定的对象的 `StandardDeviation` 属性值转换为该数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `StandardDeviationDataTypeStr` |
| **值：** | `'Inherit: Inherit via back propagation'`（默认）| `'Inherit: Inherit from 'Constant value''` | `<data type expression>` |

### 执行

### **采样时间** — 用于指定采样时间的选项 `-1`（默认）| 标量

指定采样时间命中之间的离散间隔，或指定其他类型的采样时间，例如连续 (`0`) 或继承 (`-1`)。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，模块根据模型中模块的上下文继承其采样时间。

#### 程序化使用

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |
| --- |
| **参数：** `SampleTime` |
| **数据类型：** `char` |
| **值：** `'-1'`（默认）| 标量 |

## 所属库

Deep Learning Toolbox / Deep Learning Layers / Input Layer Normalizations

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

### R2025a: **Layer** 参数默认值为 `'layerObject'`

从 R2025a 开始，**Layer** 参数的默认值为 `'layerObject'`。在以前的版本中，默认值为 `'layer'`。如果您有以编程方式创建 Simulink 并依赖名称为 `'layer'` 的变量的代码，请更新您的代码，使该变量具有名称 `'layerObject'`。

## 描述

3-D 输入层，带 zscore 归一化

Zscore 3D 模块将 3 维图像数据（具有四个维度的数据，对应于三个空间维度和一个通道维度，按该顺序）输入到神经网络，并通过减去传入模块的层对象的 `Mean` 属性值，然后将该结果除以 `StandardDeviation` 属性值，来重新缩放输入。

`exportNetworkToSimulink` 函数生成此模块，以表示一个 `image3dInputLayer` 对象，该对象的 `Normalization` 参数设置为 `"zscore"`。
