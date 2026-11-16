---
type: simulink-block
title: 'Multiplication Layer'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning Layers / Combination Layers'
documentation_page: 'multiplicationlayer'
documentation_source_path: 'ref/multiplicationlayer.html'
language: zh-CN
chinese_source: worker-translation
---

# Multiplication Layer

## 端口

### 输入

### **Port\_1** — 第一个输入数据 标量 | 向量 | 矩阵

要相乘的第一个输入，以数组形式提供，该数组遵循您使用 **数据格式** 参数指定的格式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_2** — 第二个输入数据 标量 | 向量 | 矩阵

要相乘的第二个输入，以数组形式提供，该数组遵循您使用 **数据格式** 参数指定的格式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **Port\_N** — 第 *N* 个输入数据 标量 | 向量 | 矩阵

要相乘的第 *N* 个输入，以数组形式提供，该数组遵循您使用 **数据格式** 参数指定的格式。模块具有的输入端口数量等于您使用 **输入数目** 模块参数指定的值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 输出

### **Port\_1** — 输出数据 标量 | 向量 | 矩阵

输入数据的逐元素乘积。输出数据使用您使用 **数据格式** 模块参数指定的格式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### 主要

### **输入数目** — 层模块的输入值数目 `2`（默认） | `3` | `4` | `5`

指定模块的输入数目。该模块计算输入的乘积。

#### 程序化使用

|  |
| --- |
| **模块参数**：`NumInputs` |
| **类型**：character vector |
| **值**：`'2'` | `'3'` | `'4'` | `'5'` |
| **默认值**：`'2'` |

### **数据格式** — 输入数据的格式 `SSC`（默认） | `C` | `CT` | `SC` | `SSSC`

输入数据的数据格式。这些选项使用与 `dlarray` 对象的 `fmt` 参数相同的表示法，但层模块不支持 Batch (`B`) 维度，而是假定观测编号为 `1`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `DataFormat` |
| **类型：** character vector |
| **值：** `'SSC'` | `'C'` | `'CT'` | `'SC'` | `'SSSC'` |
| **默认值：** `'SSC'` |

### 数据类型

### **输出最小值** — 用于范围检查的最小输出值 `[]`（默认） | 标量

软件检查的输出范围的最小值。

软件使用最小值执行：

- 对某些模块进行参数范围检查。有关详细信息，请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)。
- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)。
- 定点数据类型的自动定标。
- 优化您从模型生成的代码。此优化可以删除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**输出最小值** 不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `'[]'`（默认） | 带引号的标量 |

### **输出最大值** — 用于范围检查的最大输出值 `[]`（默认） | 标量

软件检查的输出范围的最大值。

软件使用最大值执行：

- 对某些模块进行参数范围检查。有关详细信息，请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)。
- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)。
- 定点数据类型的自动定标。
- 优化您从模型生成的代码。此优化可以删除算法代码并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**输出最大值** 不会饱和或裁剪实际输出信号。请改用 Saturation (Simulink) 模块。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认） | 带引号的标量 |

### **输出数据类型** — 输出的数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

选择输出的数据类型。该类型可以继承、直接指定，或表示为数据类型对象，例如 `Simulink.NumericType`。当您选择 `Inherit: Inherit via internal rule` 时，Simulink 会选择一种数据类型，以在数值精度、性能和生成的代码大小之间取得平衡，同时考虑嵌入式目标硬件的属性。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认） | `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### **锁定输出数据类型设置以防止定点工具更改** — 防止定点工具覆盖输出数据类型的选项 `off`（默认） | `on`

选择此参数可防止定点工具覆盖您在模块上指定的 **Output** 数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `LockScale` |
| **值：** | `'off'`（默认） | `'on'` |

### **整数舍入模式** — 定点运算的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RndMeth` |
| **值：** | `'Floor'`（默认） | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **整数溢出时饱和** — 溢出操作的方法 `off`（默认） | `on`

指定整数溢出是饱和还是回绕。

- `on` — 溢出饱和到数据类型可以表示的最小值或最大值。
- `off` — 溢出回绕到数据类型可以表示的相应值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于最大值的模块运算结果都会导致 8 位整数溢出。

- 选择此参数后，模块输出在 127 处饱和。类似地，模块输出在最小输出值 –128 处饱和。
- 清除此参数后，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。

#### 提示

- 当您的模型可能发生溢出并且您希望在生成的代码中具有显式饱和保护时，请将此参数设置为 `on`。
- 要优化生成代码的效率，请为此参数保留默认的 `off` 设置。使用默认设置还有助于避免过度指定模块处理超出范围信号的方式。有关详细信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。
- 选择此参数后，饱和适用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认） | `'on'` |

### 执行

### **采样时间** — 用于指定采样时间的选项 `-1`（默认） | 标量

指定采样时间命中之间的离散间隔，或指定其他类型的采样时间，例如连续 (`0`) 或继承 (`-1`)。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，模块根据其在模型中的上下文继承采样时间。

#### 程序化使用

要以程序化方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |
| --- |
| **参数：** `SampleTime` |
| **数据类型：** `char` |
| **值：** `'-1'`（默认） | 标量 |

## 所属库

Deep Learning Toolbox / Deep Learning Layers / Combination Layers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

## 描述

乘法层

Multiplication Layer 模块逐元素乘以来自多个神经网络层的输入。Multiplication Layer 模块的每个非标量输入必须具有相同的维度，并且必须遵循您使用 **数据格式** 模块参数指定的数据格式。该模块将标量输入扩展为与其他输入具有相同的维度。

`exportNetworkToSimulink` 函数生成此模块以表示 `multiplicationLayer` 对象。
