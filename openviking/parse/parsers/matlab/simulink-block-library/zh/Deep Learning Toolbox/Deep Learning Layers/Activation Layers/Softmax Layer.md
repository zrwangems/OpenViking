---
type: simulink-block
title: 'Softmax Layer'
family: 'deeplearning'
product_id: 'deeplearning'
product_name: 'Deep Learning Toolbox'
documentation_release: R2025b
official_category: 'Deep Learning Layers / Activation Layers'
documentation_page: 'softmaxlayer'
documentation_source_path: 'ref/softmaxlayer.html'
language: zh-CN
chinese_source: worker-translation
---

# Softmax Layer

## 端口

### 输入

### **Port\_1** — 输入数据 标量 | 向量 | 矩阵

要对其应用 softmax 函数的矩阵。数据必须采用您使用 **数据格式** 模块参数指定的格式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 输出数据 标量 | 向量 | 矩阵

对输入矩阵应用 softmax 函数的结果。输出数据使用您使用 **数据格式** 模块参数指定的格式。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### 主要

### **数据格式** — 输入数据的格式 `C`（默认） | `CT` | `SC` | `SSC` | `SSSC`

输入数据的数据格式。这些选项使用与 `dlarray` 对象的 `fmt` 参数相同的表示法，但层模块不支持 Batch (`B`) 维度，而是假定观测编号为 `1`。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataFormat` |
| **类型：** character vector |
| **值：** `C` | `'CT'` | `'SC'` | `'SSC'` | `'SSSC'` |
| **默认：** `'C'` |

### 数据类型

### **近似方法** — 计算层输出的近似方法 `None`（默认） | `Lookup`

指定用于计算输出的近似类型。

| 近似方法 | 支持的数据类型 | 何时使用此方法 |
| --- | --- | --- |
| `None`（默认） | 浮点 | 您仅处理浮点数据。 |
| `Lookup` | 浮点和定点 | 您处理定点数据。 |

#### 编程用法

|  |
| --- |
| **模块参数：** `ApproximationMethod` |
| **类型：** character vector |
| **值：** `'none'` | `'Lookup'` |
| **默认：** `'none'` |

### **输出最小值** — 用于范围检查的最小输出值 `[]`（默认） | 标量

软件检查的输出范围的最小值。

软件使用最小值来执行：

- 某些模块的参数范围检查。有关详细信息，请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)。
- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)。
- 定点数据类型的自动定标。
- 优化您从模型生成的代码。此优化可以移除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**输出最小值** 不会使实际输出信号饱和或限幅。请改用 Saturation (Simulink) 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMin` |
| **值：** | `'[]'`（默认） | 带引号的标量 |

### **输出最大值** — 用于范围检查的最大输出值 `[]`（默认） | 标量

软件检查的输出范围的最大值。

软件使用最大值来执行：

- 某些模块的参数范围检查。有关详细信息，请参阅 Specify Minimum and Maximum Values for Block Parameters (Simulink)。
- 仿真范围检查。有关详细信息，请参阅 Specify Signal Ranges (Simulink) 和 Enable Simulation Range Checking (Simulink)。
- 定点数据类型的自动定标。
- 优化您从模型生成的代码。此优化可以移除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅 Optimize using the specified minimum and maximum values (Embedded Coder)。

#### 提示

**输出最大值** 不会使实际输出信号饱和或限幅。请改用 Saturation (Simulink) 模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutMax` |
| **值：** | `'[]'`（默认） | 带引号的标量 |

### **输出数据类型** — 输出的数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Keep MSB` | `Inherit: Match scaling` | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `<data type expression>`

为输出选择数据类型。该类型可以继承、直接指定，或表示为数据类型对象，如 `Simulink.NumericType`。当您选择 `Inherit: Inherit via internal rule` 时，Simulink 会选择一种数据类型，以在考虑嵌入式目标硬件属性的同时，平衡数值精度、性能和生成代码大小。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认） | `'Inherit: Keep MSB'` | `'Inherit: Match scaling'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `<data type expression>` |

### **锁定输出数据类型设置，防止定点工具更改** — 用于防止定点工具覆盖输出数据类型的选项 `off`（默认） | `on`

选中此参数可防止定点工具覆盖您在模块上指定的 **Output** 数据类型。有关详细信息，请参阅 Use Lock Output Data Type Setting (Fixed-Point Designer)。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `LockScale` |
| **值：** | `'off'`（默认） | `'on'` |

### **输出整数舍入模式** — 输出定点转换操作的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定模块输出值的舍入模式，该值由最终定点转换操作生成。有关其他内部模块操作的舍入模式，请参阅 **内部整数舍入模式**。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB® 舍入函数的表达式。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `RndMeth` |
| **值：** | `'Floor'`（默认） | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **输出在整数溢出时饱和** — 输出转换操作的溢出操作方式 `off`（默认） | `on`

指定对于由最终定点转换操作生成的模块输出值，整数溢出是饱和还是回绕。有关内部模块操作的溢出操作方式，请参阅 **内部在整数溢出时饱和**。

- `on` — 溢出饱和到该数据类型可表示的最小值或最大值。
- `off` — 溢出回绕到该数据类型可表示的相应值。

例如，有符号 8 位整数 `int8` 可表示的最大值为 127。任何大于该最大值的模块运算结果都会导致该 8 位整数溢出。

- 选中此参数时，模块输出在 127 处饱和。类似地，模块输出在最小输出值 –128 处饱和。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。

#### 提示

- 当您的模型可能存在溢出，并且您希望在生成代码中具有显式饱和保护时，将此参数设置为 `on`。
- 为了优化生成代码的效率，请为此参数保留默认的 `off` 设置。使用默认设置还有助于避免过度指定模块处理超出范围信号的方式。有关详细信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。
- 选中此参数时，饱和仅应用于输出或结果。
- 通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认） | `'on'` |

### **累加器数据类型** — 累加器的数据类型 `Inherit: Inherit via internal rule`（默认） | `Inherit: Same as first input` | `<data type expression>`

为累加器选择数据类型。该类型可以继承、直接指定，或表示为数据类型对象，如 `Simulink.NumericType`。当您选择 `Inherit: Inherit via internal rule` 时，Simulink 会选择一种数据类型，以在考虑嵌入式目标硬件属性的同时，平衡数值精度、性能和生成代码大小。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `OutDataTypeStr` |
| **值：** | `'Inherit: Inherit via internal rule'`（默认） | `'Inherit: Same as first input'` | `<data type expression>` |

### **内部整数舍入模式** — 内部定点运算的舍入模式 `Floor`（默认） | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定除输出操作之外的内部定点计算的舍入模式。有关输出操作的舍入模式，请参阅 **输出整数舍入模式**。有关详细信息，请参阅 Rounding Modes (Fixed-Point Designer)。

模块参数始终舍入到最接近的可表示值。要控制模块参数的舍入，请在掩码字段中输入使用 MATLAB 舍入函数的表达式。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InternalRndMeth` |
| **值：** | `'Floor'`（默认） | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **内部在整数溢出时饱和** — 内部模块操作的溢出操作方式 `off`（默认） | `on`

指定对于模块的内部操作，整数溢出是饱和还是回绕。有关模块输出的溢出操作方式，请参阅 **输出在整数溢出时饱和**。

- `on` — 溢出饱和到该数据类型可表示的最小值或最大值。
- `off` — 溢出回绕到该数据类型可表示的相应值。

例如，有符号 8 位整数 `int8` 可表示的最大值为 127。任何大于该最大值的模块运算结果都会导致该 8 位整数溢出。

- 选中此参数时，模块输出在 127 处饱和。类似地，模块输出在最小输出值 –128 处饱和。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 –126。

#### 提示

- 当您的模型可能存在溢出，并且您希望在生成代码中具有显式饱和保护时，将此参数设置为 `on`。
- 为了优化生成代码的效率，请为此参数保留默认的 `off` 设置。使用默认设置还有助于避免过度指定模块处理超出范围信号的方式。有关详细信息，请参阅 Troubleshoot Signal Range Errors (Simulink)。
- 选中此参数时，饱和仅应用于模块的内部操作。
- 通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |  |
| --- | --- |
| **参数：** | `InternalSaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认） | `'on'` |

### 执行

### **采样时间** — 用于指定采样时间的选项 `-1`（默认） | 标量

指定采样时间命中之间的离散间隔，或指定其他类型的采样时间，例如连续 (`0`) 或继承 (`-1`)。有关更多选项，请参阅 Types of Sample Time (Simulink)。

默认情况下，模块根据其在模型中的上下文继承采样时间。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` (Simulink) 函数。

|  |
| --- |
| **参数：** `SampleTime` |
| **数据类型：** `char` |
| **值：** `'-1'`（默认） | 标量 |

## 所属库

Deep Learning Toolbox / Deep Learning Layers / Activation Layers

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2024b 中引入**

### R2025a：更新了整数舍入模式和整数溢出饱和参数

**Integer rounding mode** 和 **Saturate integer overflow** 参数现在拆分为输出版本和内部版本的参数。**Output integer rounding mode** 和 **Output saturate on integer overflow** 控制模块输出的最终转换操作的行为。**Internal integer rounding mode** 和 **Internal saturate on integer overflow** 控制内部模块操作。

## 描述

Softmax 层

Softmax Layer 模块对层输入应用 softmax 函数。输入数据必须遵循您使用 **数据格式** 模块参数指定的数据格式。

`exportNetworkToSimulink` 函数生成此模块以表示 `softmaxLayer` 对象。
