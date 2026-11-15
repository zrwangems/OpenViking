---
type: simulink-block
title: 'Shift Arithmetic'
family: logic-and-bit-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'shiftarithmetic'
---

# Shift Arithmetic

Shift bits or binary point of signal

## 中文

移动信号的位或二进制小数点

### 所属库

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

### 描述

Shift Arithmetic 模块可以移动输入信号中的数位和/或二进制小数点。

例如，将 `sfix(8)` 数据类型的输入信号中的二进制小数点向右和向左移动两位，将得到以下小数值。

| 移位运算 | 二进制值 | 十进制值 |
| --- | --- | --- |
| 无移位（原始数字） | 11001.011 | -6.625 |
| 二进制小数点向右移动两位 | 1100101.1 | -26.5 |
| 二进制小数点向左移动两位 | 110.01011 | -1.65625 |

此模块对有符号数字执行算术移位。因此，模块为每一次移位回收最高有效位。将 `sfix(8)` 数据类型的输入信号中的数位向右和向左移动两位，将得到以下小数值。

| 移位运算 | 二进制值 | 十进制值 |
| --- | --- | --- |
| 无移位（原始数字） | 11001.011 | -6.625 |
| 向右移动两位 | 11110.010 | -1.75 |
| 向左移动两位 | 00101.100 | 5.5 |

### 端口

#### 输入

#### **u** — 要对其执行运算的数 标量 | 向量 | 数组

要对其执行运算的数，指定为标量、向量或数组。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

#### **s** — 要移位的位数 标量

要移位的位数，指定为标量。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
#### 输出

#### **Port\_1** — 运算结果 标量 | 向量 | 数组

运算结果，以标量、向量或数组形式返回。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 参数

#### **二进制位移位数:源** — 要移位的位的源 **对话框** (默认) | **输入端口**

指定是直接在对话框中输入要移动的位数，还是从输入端口继承值。

**可调:** No

##### 编程用法

|  |
| --- |
| **模块参数**：`BitShiftNumberSource` |
| **类型**：字符向量、字符串 |
| **值**：`'Dialog'` | `'Input port'` |
| **默认值**：`'Dialog'` |

#### **二进制位移位数:方向** — 移位的方向 **双向** (默认) | **左侧** | **右侧**

指定移位的方向：向左、向右或双向。

**可调:** No

##### 编程用法

|  |
| --- |
| **模块参数**：`BitShiftDirection` |
| **类型**：字符向量、字符串 |
| **值**：`'Left'` | `'Right'` | `'Bidirectional'` |
| **默认值**：`'Bidirectional'` |

#### **二进制位移位数:数量** — 二进制位移位数 `8` (默认) | 标量 | 向量 | 数组

指定标量、向量或移位值数组。

| 如果方向为... | 则... |
| --- | --- |
| **左侧**或**右侧** | 使用正整数指定移位。 |
| **双向** | 使用正整数表示右移，使用负整数表示左移。 |

**可调:** No

##### 依赖关系

要启用此参数，请将**二进制位移位数:源**设置为**对话框**。

##### 编程用法

|  |
| --- |
| **模块参数**：`BitShiftNumber` |
| **类型**：字符向量、字符串 |
| **值**：标量 | 向量 | 矩阵 |
| **默认值**：`'8'` |

#### **二进制小数点移位数:数量** — 二进制小数点移位的位数 `0` (默认) | 标量

指定将输入信号中的二进制小数点移动的整数位数。正值表示右移，负值表示左移。

**可调:** No

##### 编程用法

|  |
| --- |
| **模块参数**：`BinPtShiftNumber` |
| **类型**：字符向量、字符串 |
| **值**：标量 |
| **默认值**：`'0'` |

#### **超范围移位值的诊断** — 诊断操作 **无** (默认) | **警告** | **错误**

指定当模块包含超出范围的移位值时，是否在仿真过程中生成警告或错误消息。选项包括：

- `None` - 软件不执行任何操作。
- `Warning` - 软件显示警告并继续进行仿真。
- `Error` - 该软件终止仿真并显示错误。

有关详细信息，请参阅超范围移位值的仿真和加速模式结果。

##### 编程用法

|  |
| --- |
| **模块参数**：`DiagnosticForOORShift` |
| **类型**：字符向量、字符串 |
| **值**：`'None'` | `'Warning'` | `'Error'` |
| **默认值**：`'None'` |

#### **检查生成代码中是否有超出范围的 '二进制位移位数'** — 检查生成代码中是否有超出范围的二进制位移位数 `off` (默认) | `on`

如果选中此复选框，将在生成的代码中包含条件语句，以防移位值超出范围。当**二进制位移位数:源**为**输入端口**时，此复选框才可用。

有关详细信息，请参阅超范围移位值的代码生成。

##### 编程用法

|  |
| --- |
| **模块参数**：`CheckOORBitShift` |
| **类型**：字符向量、字符串 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'off'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

当**二进制位移位数:源**为**对话框**或**输入端口**时，您可以生成 HDL 代码。

**HDL 架构**

生成的 VHDL 代码使用 `shift_right` 函数和 `sll` 运算符。

生成的 Verilog 代码使用 `>>>` 和 `<<<` 移位运算符。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复信号的代码生成。

**限制**

当**二进制位移位数:源**为**输入端口**时，不支持二进制小数点移位。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

## Description

The Shift Arithmetic block can shift the bits or the binary point of an input
signal, or both.

For example, shifting the binary point on an input of data type `sfix(8)`
by two places to the right and left gives these decimal values.

| Shift Operation | Binary Value | Decimal Value |
| --- | --- | --- |
| No shift (original number) | 11001.011 | –6.625 |
| Binary point shift right by two places | 1100101.1 | –26.5 |
| Binary point shift left by two places | 110.01011 | –1.65625 |

This block performs arithmetic bit shifts on signed numbers. Therefore, the block recycles
the most significant bit for each bit shift. Shifting the bits on an input of data type
`sfix(8)` by two places to the right and left gives these decimal
values.

| Shift Operation | Binary Value | Decimal Value |
| --- | --- | --- |
| No shift (original number) | 11001.011 | –6.625 |
| Bit shift right by two places | 11110.010 | –1.75 |
| Bit shift left by two places | 00101.100 | 5.5 |

## Ports

### Input

### **u** — Number to be operated on scalar | vector | array

Number to be operated on, specified as a scalar, vector, or
array.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **s** — Number of bits to shift scalar

Number of bits to shift, specified as a scalar.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Result of operation scalar | vector | array

Result of operation, returned as a scalar, vector, or array.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Bits to shift: Source** — Source of bits to shift `Dialog` (default) | `Input port`

Specify whether to enter the bits to shift on the dialog box or to inherit the values
from an input port.

**Tunable:** No

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BitShiftNumberSource` |
| **Type**: character vector, string |
| **Values**: `'Dialog'` | `'Input port'` |
| **Default**: `'Dialog'` |

### **Bits to shift: Direction** — Direction in which to shift bits `Bidirectional` (default) | `Left` | `Right`

Specify the direction in which to shift bits: left, right, or
bidirectional.

**Tunable:** No

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BitShiftDirection` |
| **Type**: character vector, string |
| **Values**: `'Left'` | `'Right'` | `'Bidirectional'` |
| **Default**: `'Bidirectional'` |

### **Bits to shift: Number** — Bits to shift `8` (default) | scalar | vector | array

Specify a scalar, vector, or array of bit shift values.

| If the direction is... | Then... |
| --- | --- |
| `Left` or `Right` | Use positive integers to specify bit shifts. |
| `Bidirectional` | Use positive integers for right shifts and negative integers for left shifts. |

**Tunable:** No

#### Dependencies

To enable this parameter, set **Bits to shift:
Source** to `Dialog`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BitShiftNumber` |
| **Type**: character vector, string |
| **Values**: scalar | vector | array |
| **Default**: `'8'` |

### **Binary points to shift: Number** — Number of places to shift binary point `0` (default) | scalar

Specify an integer number of places to shift the binary point of the input
signal. A positive value indicates a right shift, while a negative value
indicates a left shift.

**Tunable:** No

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BinPtShiftNumber` |
| **Type**: character vector, string |
| **Values**: scalar |
| **Default**: `'0'` |

### **Diagnostic for out of range shift value** — Diagnostic action `None` (default) | `Warning` | `Error`

Specify whether to produce a warning or error during simulation when the
block contains an out-of-range shift value. Options include:

- `None` — The software takes no
  action.
- `Warning` — The software displays a
  warning and continues the simulation.
- `Error` — The software terminates the
  simulation and displays an error.

For more information, see Simulation and Accelerator Mode Results for Out-of-Range Bit Shift Values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `DiagnosticForOORShift` |
| **Type**: character vector, string |
| **Values**: `'None'` | `'Warning'` | `'Error'` |
| **Default**: `'None'` |

### **Check for out-of-range 'Bits to shift' in generated code** — Check for out-of-range bits to shift in generated code `off` (default) | `on`

Select this check box to include conditional statements in the generated
code that protect against out-of-range bit shift values. This check box is
available when **Bits to shift: Source** is
`Input port`.

For more information, see Code Generation for Out-of-Range Bit Shift Values.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CheckOORBitShift` |
| **Type**: character vector, string |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

You can generate HDL code when **Bits to shift: Source** is
**Dialog** or **Input port**.

**HDL Architecture**

The generated VHDL code uses the `shift_right` function and
`sll` operator.

The generated Verilog code uses the `>>>` and
`<<<` shift operators.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Complex Data Support**

This block supports code generation for complex signals.

**Restrictions**

When **Bits to shift: Source** is **Input
port**, binary point shifting is not supported.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
