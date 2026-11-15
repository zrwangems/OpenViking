---
type: simulink-block
title: 'Dead Zone'
family: discontinuities
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Discontinuities'
documentation_page: 'deadzone'
---

# Dead Zone

Provide region of zero output

## 中文

提供零值输出区域

### 所属库

Simulink / Discontinuities HDL Coder / Discontinuities

### 描述

Dead Zone 模块在指定的区域内生成零值输出，此区域称为死区。您可以通过**死区起点**和**死区终点**参数指定死区的下限 (`LL`) 和上限 (`UL`)。模块输出取决于输入 (`U`) 以及上限和下限的值。

| 输入 | 输出 |
| --- | --- |
| `U >= LL` 和 `U <= UL` | 零 |
| `U > UL` | `U` – `UL` |
| `U < LL` | `U` – `LL` |

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量

死区算法的输入信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
#### 输出

#### **Port\_1** — 输出信号 标量 | 向量

死区算法应用于输入信号后的输出信号。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 参数

#### **死区起点** — 指定死区的下界 `'-0.5'` (默认) | 标量 | 向量

指定死区下限。为**死区起点**设置小于或等于**死区终点**的值。当输入值小于**死区起点**时，模块会将输出值向下移动**死区起点**值。

##### 编程用法

|  |
| --- |
| **模块参数**：`LowerValue` |
| **类型**：字符向量 |
| **值**：小于或等于 `UpperValue` 的标量或向量。 |
| **默认值**：`'-0.5'` |

#### **死区终点** — 指定死区的上限。 `'0.5'` (默认) | 标量 | 向量

指定死区上限。为**死区终点**设置大于或等于**死区起点**的值。当输入值大于**死区终点**时，模块会将输出值向下移动**死区终点**值。

##### 编程用法

|  |
| --- |
| **模块参数**：`UpperValue` |
| **类型**：字符向量 |
| **值**：大于或等于 `LowerValue` 的标量或向量。 |
| **默认值**：`'0.5'` |

#### **对整数溢出进行饱和处理** — 溢出操作的方法 `on` (默认) | `off`

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
| **值:** | `'on'` (默认) | `'off'` |

#### **线性化时视为增益** — 指定增益值 `on` (默认) | `off`

Simulink® 软件中的线性化命令将此模块视为状态空间中的增益。选择此参数将使得这些命令将增益视为 1。清除此参数可使命令将增益视为 0。

##### 编程用法

|  |
| --- |
| **模块参数**：`LinearizeAsGain` |
| **类型**：字符向量 |
| **值**：`'off'` | `'on'` |
| **默认值**：`'on'` |

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

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `是` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Discontinuities HDL Coder / Discontinuities

## Description

The Dead Zone block generates zero output within a specified region,
called its dead zone. You specify the lower limit (`LL`) and upper
limit (`UL`) of the dead zone as the **Start of dead
zone** and **End of dead zone** parameters. The block
output depends on the input (`U`) and the values for the lower and
upper limits.

| Input | Output |
| --- | --- |
| `U >= LL` and `U <= UL` | Zero |
| `U > UL` | `U` – `UL` |
| `U < LL` | `U` – `LL` |

## Ports

### Input

### **Port\_1** — Input signal scalar | vector

Input signal to the dead-zone algorithm.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector

Output signal after the dead-zone algorithm is applied to the input
signal.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Start of dead zone** — Specify the lower bound of the dead zone `'-0.5'` (default) | scalar | vector

Specify dead zone lower limit. Set the value for **Start of dead
zone** less than or equal to **End of dead
zone**. When the input value is less than **Start of
dead zone**, then the block shifts the output value down by the
**Start of dead zone** value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LowerValue` |
| **Type**: character vector |
| **Value**: scalar or vector less than or equal to `UpperValue`. |
| **Default**: `'-0.5'` |

### **End of dead zone** — Specify the upper limit of the dead zone `'0.5'` (default) | scalar | vector

Specify dead zone upper limit. Set the value for **End of dead
zone** greater than or equal to **Start of dead
zone**. When the input value is greater than **End of
dead zone**, then the block shifts the output value down by the
**End of dead zone** value.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `UpperValue` |
| **Type**: character vector |
| **Value**: scalar or vector greater than or equal to `LowerValue`. |
| **Default**: `'0.5'` |

### **Saturate on integer overflow** — Method of overflow action `on` (default) | `off`

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
| **Values:** | `'on'` (default) | `'off'` |

### **Treat as gain when linearizing** — Specify the gain value `on` (default) | `off`

The linearization commands in Simulink® software treat this block as a gain in state space. Select this parameter
to cause the commands to treat the gain as 1. Clear this parameter to have the commands
treat the gain as 0.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LinearizeAsGain` |
| **Type**: character vector |
| **Value**: `'off'` | `'on'` |
| **Default**: `'on'` |

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

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
