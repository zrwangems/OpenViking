---
type: simulink-block
title: 'MinMax'
family: math-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'minmax'
---

# MinMax

Output minimum or maximum input value

## 中文

输出最小或最大输入值

### 所属库

Simulink / Math Operations HDL Coder / Math Operations

### 描述

MinMax 模块输出输入的最小或最大元素。您可以通过设置**函数**参数来选择模块是否输出最小值或最大值。

MinMax 模块将忽略类型为 `NaN` 的任何输入值，除非每个输入值为 `NaN`。当所有输入值均为 `NaN` 时，输出为 `NaN`，要么是标量，要么是每个输出向量元素的值。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

提供输入信号，模块根据该输入信号输出最大值或最小值。

- 如果模块只有一个输入端口，则输入必须为标量或向量。模块将输出等于输入向量的最小或最大元素的标量。
- 如果模块有多个输入端口，则所有非标量输入都必须具有相同的维度。模块会扩展任何标量输入，使其与非标量输入具有相同的维度。模块将输出与输入具有相同维度的信号。每个输出元素等于对应输入元素的最小值或最大值。

##### 依赖关系

要支持矩阵输入，您必须将**输入端口数目**参数设置为大于 1 的整数。所有的非标量输入信号必须具有相同的维度。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

#### **Port\_N** — 第 *N* 个输入信号 标量 | 向量 | 矩阵

提供输入信号，模块根据该输入信号输出最大值或最小值。

如果模块有多个输入端口，则所有非标量输入都必须具有相同的维度。模块会扩展任何标量输入，使其与非标量输入具有相同的维度。模块将输出与输入具有相同维度的信号。每个输出元素等于对应输入元素的最小值或最大值。

##### 依赖关系

要提供多个输入信号，请将**输入端口数目**设置为大于 1 的整数。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
#### 输出

#### **Port\_1** — 输入的最小值或最大值 标量 | 向量 | 矩阵

当模块有一个输入时，输出是标量值，该标量等于输入元素的最小值或最大值。当模块有多个输入时，输出是与输入具有相同维度的信号。每个输出元素等于对应输入元素的最小值或最大值。如果模块输入具有不同的输入数据类型，则输出与输入的大小相同，但精度可能较低。例如，如果一个输入的数据类型为 `int8`，一个为 `uint8`，则输出数据类型仍为 8 位，即 `sfix8_E1`，但精度较低。

**数据类型:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 参数

#### 常设

#### **函数** — 指定最小值或最大值 **最小值** (默认) | **最大值**

指定对输入应用 `min` 函数还是 `max` 函数。

##### 编程用法

|  |
| --- |
| **模块参数**：`Function` |
| **类型：**字符向量 |
| **值：**`'min' | 'max'` |
| **默认值：**`'min'` |

#### **输入端口数目** — 指定输入端口个数 `1` (默认) | `positive integer`

指定模块的输入数目。

##### 编程用法

|  |
| --- |
| **模块参数**：`Inputs` |
| **类型：**字符向量 |
| **值：**`positive integer` |
| **默认值：**`'1'` |

#### **应用于** — 如何沿指定维度应用函数 **所有维度** (默认) | **指定的维度**

指定如何沿指定维度应用函数。

- **所有维度** - 对所有维度的所有输入值应用函数。
- **指定维度** - 对指定维度的所有输入值应用函数。

例如，在此模型中，**函数**设置为**最大值**，**应用于**设置为**所有维度**。该模块返回所有维度中最大的输入值。

2D matrix with Constant block value [1 3 5;3 6 7;9 10 1] as input to MinMax block configured for all dimensions

##### 依赖关系

要启用此参数，**输入端口数目**必须为 `1`。

##### 编程用法

|  |
| --- |
| **模块参数**：`CollapseMode` |
| **类型：**字符向量 |
| **值**：`'All dimensions'` | `'Specified dimension'` |
| **默认值：**`'All dimensions'` |

#### **维度** — 指定沿其应用函数的维度 `1` (默认) | 正整数 | `...` | `N`

将沿其应用函数的维度指定为正整数。例如，对于二维矩阵，`1` 将函数应用于每列，`2` 将函数应用于每行。

例如，在此模型中，**函数**设置为**最大值**，**应用于**设置为**指定维度**，**维度**设置为 `2`。该模块返回每行的最大输入值。

2D matrix with Constant block value [1 3 5;3 6 7;9 10 1] as input to MinMax block configured for dimension 2

##### 依赖关系

要启用此参数，请将**应用于**设置为**指定的维度**。

##### 编程用法

|  |
| --- |
| **模块参数**：`CollapseDim` |
| **类型：**字符向量 |
| **值：**正整数 |
| **默认值：**`'1'` |

#### **启用过零检测** — 启用过零检测 `on` (默认) | `off`

选择此项以启用过零检测。有关详细信息，请参阅过零检测。

##### 编程用法

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型**：字符向量 | 字符串 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

#### **采样时间(-1 表示继承)** — 采样之间的时间间隔 `-1` (默认) | 标量 | 向量

指定采样时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

##### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时才可见。要了解详细信息，请参阅不建议设置采样时间的模块。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SampleTime` |
| **值:** | `"-1"` (默认) | scalar or vector in quotes |

#### 信号属性

#### **要求所有输入具有相同的数据类型** — 输入必须具有相同的数据类型 `off` (默认) | `on`

选中此复选框将要求所有输入具有相同的数据类型。

##### 编程用法

|  |
| --- |
| **模块参数**：`InputSameDT` |
| **类型：**字符向量 |
| **值：**`'off' | 'on'` |
| **默认值：**`'off'` |

#### **输出最小值** — 范围检查的最小输出值 `[]` (默认) | 标量

软件检查的输出范围的下限值。

软件使用最小值执行下列操作：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围和启用仿真范围检查）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

##### 提示

**输出最小值**不会对实际输出信号进行饱和处理或截断。请改用 Saturation 模块。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `OutMin` |
| **值:** | `'[]'` (默认) | scalar in quotes |

#### **输出最大值** — 范围检查的最大输出值 `[]` (默认) | 标量

软件检查的输出范围的上限值。

软件使用最大值执行下列操作：

- 某些模块的参数范围检查（请参阅指定模块参数的最小值和最大值）。
- 仿真范围检查（请参阅指定信号范围和启用仿真范围检查）。
- 定点数据类型的自动定标。
- 从模型生成的代码的优化。此优化可删除算法代码，并影响某些仿真模式（如 SIL 或外部模式）的结果。有关详细信息，请参阅使用指定的最小值和值进行优化 (Embedded Coder)。

##### 提示

**输出最大值**不会对实际输出信号进行饱和处理或截断。请改用 Saturation 模块。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `OutMax` |
| **值:** | `'[]'` (默认) | scalar in quotes |

#### **输出数据类型** — 指定输出数据类型 **继承: 从内部规则继承** (默认) | **继承: 通过反向传播继承** | **继承: 与第一个输入相同** | **double** | **single** | **half** | **int8** | **uint8** | **int16** | **uint16** | **int32** | **uint32** | **int64** | **uint64** | **fixdt(1,16,0)** | **fixdt(1,16,2^0,0)** | **<数据类型表达式>**

为输出选择数据类型。该类型可以继承、直接指定或表示为数据类型对象，如 `Simulink.NumericType`。

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 依赖关系

当输入是小于单精度的浮点数据类型时，**继承: 从内部规则继承**输出数据类型取决于 Inherit floating-point output type smaller than single precision 配置参数的设置。当对数据类型进行编码所需的位数小于对单精度数据类型编码所需的 32 位时，数据类型小于单精度。例如，`half` 和 `int16` 小于单精度。

##### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Inherit via internal rule'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

#### **锁定输出数据类型设置以防止被定点工具更改** — 用于防止定点工具覆盖输出数据类型的选项 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您在模块上指定的**输出**数据类型。有关详细信息，请参阅Use Lock Output Data Type Setting (Fixed-Point Designer)。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `LockScale` |
| **值:** | `'off'` (默认) | `'on'` |

#### **整数舍入模式** — 定点运算的舍入模式 **向下** (默认) | **向上** | **收敛** | **最邻近值** | **舍入** | **最简** | **零**

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式 (Fixed-Point Designer)。

模块参数始终舍入到最邻近的可表示值。要控制模块参数的舍入方法，请在封装字段中使用 MATLAB® 舍入函数输入表达式。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `RndMeth` |
| **值:** | `'Floor'` (默认) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

#### **对整数溢出进行饱和处理** — 溢出操作的方法 `off` (默认) | `on`

指定对溢出是进行饱和处理还是绕回处理。

- `on` - 将溢出饱和处理为数据类型能够表示的最小值或最大值。
- `off` - 溢出将绕回到数据类型可以表示的合适值。

例如，有符号 8 位整数 `int8` 可以表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选择此参数后，模块输出将在达到 127 时饱和。类似地，模块输出将在达到最小输出值 -128 时饱和。
- 清除此参数后，软件会将导致溢出的值解释为 `int8`，这可能产生意外结果。例如，以 `int8` 表示的模块结果 130（二进制 1000 0010）为 -126。

##### 提示

- 如果您的模型存在可能的溢出，而您希望在生成的代码中进行显式饱和保护，请考虑选中此参数。
- 如果您希望优化生成的代码的效率，请考虑清除此参数。清除此参数还可以帮助您避免过度地指定信号超出范围时模块的处理方式。有关详细信息，请参阅信号范围错误故障排除。
- 如果选中此参数，饱和将应用于模块中的每个内部操作，而不仅仅应用于输出或结果。
- 一般情况下，代码生成进程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SaturateOnIntegerOverflow` |
| **值:** | `'off'` (默认) | `'on'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `是` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

| 架构 | 额外的延迟周期 | 描述 |
| --- | --- | --- |
| **树****（默认值）** | 0 | 生成树状结构的比较器。 |

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

| 原生浮点 | |
| --- | --- |
| **LatencyStrategy** | 指定对于浮点运算符是否将设计中的模块映射到 `inherit`、`Max`、`Min` 或 `Zero`。默认值为 **inherit**。另请参阅LatencyStrategy (HDL Coder)。 |

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

#### R2024a: MinMax 模块支持指定的维度

MinMax 模块使您能够使用这些新参数查找一个指定维度上的最小值或最大值：

- **应用于** - 对所有或指定的维度应用函数。
- **维度** - 要对其应用函数的维度。

## Libraries

Simulink / Math Operations HDL Coder / Math Operations

## Description

The MinMax block outputs either the minimum or the maximum element or
elements of the inputs. You choose whether the block outputs the minimum or maximum
values by setting the **Function** parameter.

The MinMax block ignores any input value that is `NaN`,
except when every input value is `NaN`. When all input values are
`NaN`, the output is `NaN`, either as a scalar or
the value of each output vector element.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Provide an input signal from which the block outputs the maximum or minimum
values.

- When the block has one input port, the input must be a scalar
  or a vector. The block outputs a scalar equal to the minimum or
  maximum element of the input vector.
- When the block has multiple input ports, all nonscalar inputs
  must have the same dimensions. The block expands any scalar
  inputs to have the same dimensions as the nonscalar inputs. The
  block outputs a signal having the same dimensions as the input.
  Each output element equals the minimum or maximum of the
  corresponding input elements.

#### Dependencies

To support matrix input, you must set the **Number of
input ports** parameter to an integer greater than one.
All nonscalar inputs must have the same dimensions.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **Port\_N** — *N*th input signal scalar | vector | matrix

Provide an input signal from which the block outputs the maximum or
minimum values.

When the block has multiple input ports, all nonscalar inputs must
have the same dimensions. The block expands any scalar inputs to have
the same dimensions as the nonscalar inputs. The block outputs a signal
having the same dimensions as the input. Each output element equals the
minimum or maximum of the corresponding input elements.

#### Dependencies

To provide more than one input signal, set the **Number of
input ports** to an integer greater than 1.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Minimum or maximum values of inputs scalar | vector | matrix

When the block has one input, the output is a scalar value, equal to the minimum or
maximum of the input elements. When the block has multiple inputs, the
output is a signal having the same dimensions as the input. Each output
element equals the minimum or maximum of the corresponding input
elements. If the block input has different input data types, the output
is the same size as the input, but might have less precision. For
example, if one input is `int8` and one is
`uint8`, the output data type is still 8 bits,
`sfix8_E1`, but with less precision.

**Data Types:** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### Main

### **Function** — Specify minimum or maximum `min` (default) | `max`

Specify whether to apply the function `min` or
`max` to the input.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Function` |
| **Type:** character vector |
| **Values:** `'min' | 'max'` |
| **Default:** `'min'` |

### **Number of input ports** — Specify number of input ports `1` (default) | `positive integer`

Specify the number of inputs to the block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Inputs` |
| **Type:** character vector |
| **Values:** `positive integer` |
| **Default:** `'1'` |

### **Apply over** — How to apply function along specified dimensions `All dimensions` (default) | `Specified dimension`

Specify how to apply the function along specified dimensions.

- `All dimensions` — Apply function for
  all input values for all dimensions.
- `Specified dimension` — Apply
  function for all input values for specified dimension.

For example, in this model, **Function** is set to
`max`, and **Apply
over** is set to `All
dimensions`. The block returns the largest input value from
all dimensions.

2D matrix with Constant block value [1 3 5;3 6 7;9 10 1] as input to MinMax block configured for all dimensions

#### Dependencies

To enable this parameter, **Number of input
ports** must be `1`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CollapseMode` |
| **Type:** character vector |
| **Values:** `'All dimensions'` | `'Specified dimension'` |
| **Default:** `'All dimensions'` |

### **Dimension** — Specify the dimension along which to apply function `1` (default) | positive integer | `...` | `N`

Specify the dimension along which to apply the function as a positive
integer. For example, for a 2-D matrix, `1` applies the
function to each column, and `2` applies the function
to each row.

For example, in this model, **Function** is set to
`max`, **Apply over** is
set to `Specified dimension`, and
**Dimension** is set to `2`. The
block returns the largest input value from each row.

2D matrix with Constant block value [1 3 5;3 6 7;9 10 1] as input to MinMax block configured for dimension 2

#### Dependencies

To enable this parameter, set **Apply over** to
`Specified dimension`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CollapseDim` |
| **Type:** character vector |
| **Values:** positive integer |
| **Default:** `'1'` |

### **Enable zero-crossing detection** — Enable zero-crossing detection `on` (default) | `off`

Select to enable zero-crossing detection. For more information, see Zero-Crossing Detection.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ZeroCross` |
| **Type**: character vector | string |
| **Values**: `'off'` | `'on'` |
| **Default**: `'on'` |

### **Sample time (-1 for inherited)** — Interval between samples `-1` (default) | scalar | vector

Specify the time interval between samples. To inherit the sample time, set this
parameter to `-1`. For more information, see Specify Sample Time.

#### Dependencies

This parameter is visible only if you set it to a value other than
`-1`. To learn more, see Blocks for Which Sample Time Is Not Recommended.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **Values:** | `"-1"` (default) | scalar or vector in quotes |

### Signal Attributes

### **Require all inputs to have the same data type** — Inputs must have the same data type `off` (default) | `on`

Select this check box to require that all inputs have the same data
type.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputSameDT` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Output minimum** — Minimum output value for range checking `[]` (default) | scalar

Lower value of the output range that the software checks.

The software uses the minimum to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
  for some blocks.
- Simulation range checking (see Specify Signal Ranges and
  Enable Simulation Range Checking).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

#### Tips

**Output minimum** does not saturate or clip the actual output
signal. Use the Saturation block instead.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutMin` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Output maximum** — Maximum output value for range checking `[]` (default) | scalar

Upper value of the output range that the software checks.

The software uses the maximum value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters)
  for some blocks.
- Simulation range checking (see Specify Signal Ranges and
  Enable Simulation Range Checking).
- Automatic scaling of fixed-point data types.
- Optimization of the code that you generate from the model. This
  optimization can remove algorithmic code and affect the results of some
  simulation modes such as SIL or external mode. For more information, see
  Optimize using the specified minimum and maximum values (Embedded Coder).

#### Tips

**Output maximum** does not saturate or clip the actual output
signal. Use the Saturation block instead.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutMax` |
| **Values:** | `'[]'` (default) | scalar in quotes |

### **Output data type** — Specify the output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Inherit via back propagation` | `Inherit: Same as first input` | `double` | `single` | `half` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Choose the data type for the output. The type can be inherited,
specified directly, or expressed as a data type object such as
`Simulink.NumericType`.

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

When input is a floating-point data type smaller than single
precision, the `Inherit: Inherit via internal
rule` output data type depends on the setting of
the Inherit floating-point output type smaller than single precision configuration parameter. Data types are smaller than single
precision when the number of bits needed to encode the data type is
less than the 32 bits needed to encode the single-precision data
type. For example, `half` and
`int16` are smaller than single
precision.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'double'` | `'single'` | `'half'` | `'int8'` | `'uint8'` | `'int16'` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `'fixdt(1,16,0)'` | `'fixdt(1,16,2^0,0)'` | `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |

### **Lock output data type setting against changes by the fixed-point tools** — Option to prevent fixed-point tools from overriding Output data type `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the
**Output** data type you specify on the block. For more
information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LockScale` |
| **Values:** | `'off'` (default) | `'on'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations. For more information, see Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To control the
rounding of a block parameter, enter an expression using a MATLAB® rounding function into the mask field.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RndMeth` |
| **Values:** | `'Floor'` (default) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Saturate on integer overflow** — Method of overflow action `off` (default) | `on`

Specify whether overflows saturate or wrap.

- `on` — Overflows saturate to either the minimum or maximum
  value that the data type can represent.
- `off` — Overflows wrap to the appropriate value that the data
  type can represent.

For example, the maximum value that the signed 8-bit integer `int8`
can represent is 127. Any block operation result greater than this maximum value causes
overflow of the 8-bit integer.

- With this parameter selected, the block output saturates at 127.
  Similarly, the block output saturates at a minimum output value of
  -128.
- With this parameter cleared, the software interprets the overflow-causing
  value as `int8`, which can produce an unintended result.
  For example, a block result of 130 (binary 1000 0010) expressed as
  `int8` is -126.

#### Tips

- Consider selecting this parameter when your model has a possible overflow
  and you want explicit saturation protection in the generated code.
- Consider clearing this parameter when you want to optimize efficiency of
  your generated code. Clearing this parameter also helps you to avoid
  overspecifying how a block handles out-of-range signals. For more
  information, see Troubleshoot Signal Range Errors.
- When you select this parameter, saturation applies to every internal
  operation on the block, not just the output or result.
- In general, the code generation process can detect when overflow is not
  possible. In this case, the code generator does not produce saturation
  code.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SaturateOnIntegerOverflow` |
| **Values:** | `'off'` (default) | `'on'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

| Architecture | Additional cycles of latency | Description |
| --- | --- | --- |
| `Tree` `(default)` | 0 | Generates a tree structure of comparators. |

**HDL Block Properties**

| General | |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

| Native Floating Point | |
| --- | --- |
| **LatencyStrategy** | Specify whether to map the blocks in your design to `inherit`, `Max`, `Min`, or `Zero` for the floating-point operator. The default is `inherit`. See also LatencyStrategy (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2024a: MinMax block supports specified dimensions

The MinMax block enables you to find minimum or maximum values over
a specified dimension using these new parameters:

- **Apply
  over** — Apply function over all or specified
  dimensions.
- **Dimension** — Dimension over which to apply the
  function.
