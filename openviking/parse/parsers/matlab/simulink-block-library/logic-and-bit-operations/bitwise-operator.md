---
type: simulink-block
title: 'Bitwise Operator'
family: logic-and-bit-operations
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'bitwiseoperator'
---

# Bitwise Operator

Specified bitwise operation on inputs

## 中文

对输入执行指定的按位运算

### 所属库

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

### 描述

Bitwise Operator 模块执行您为一个或多个操作数指定的按位运算。与 Logical Operator 模块的逻辑运算不同的是，按位运算将操作数视为位向量，而不是单个值。

#### 对模块运算的限制

Bitwise Operator 模块不支持移位运算。对于移位运算，请使用 Shift Arithmetic 模块。

当配置为多输入 XOR 门时，此模块将按照 IEEE® 逻辑元素标准的规定执行模 2 加法。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量

输入信号，指定为标量或向量。

- NOT 运算符仅接受一个输入，该输入可以是标量也可以是向量。如果输入为向量，则输出为相同大小的向量，其中包含输入向量元素的按位逻辑补码。
- 对于单个向量输入，模块会将运算（除 NOT 运算符外）应用于向量的所有元素。
- 对于两个或更多输入，模块将在所有输入之间执行运算。如果输入为向量，模块将在对应的向量元素之间执行运算以生成向量输出。

**数据类型:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
#### 输出

#### **Port\_1** — 输出信号 标量 | 向量

指定为输出数据类型的输出信号，模块从驱动模块继承该输出数据类型，且该数据类型必须准确表示零。满足此条件的数据类型包括有符号整数和无符号整数数据类型。

模块输出的大小取决于输入数目、向量大小以及您选择的运算符。如果您不指定位掩码，则输出为标量。如果您指定位掩码，则输出为向量。

**数据类型:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### 参数

#### **运算符** — 按位逻辑运算符 AND (默认) | OR | NOR | NAND | XOR | NOT

为模块操作数指定按位逻辑运算符。

您可以选择以下按位运算之一：

| 按位运算 | 描述 |
| --- | --- |
| AND | 如果对应的位全部为 TRUE，则为 TRUE |
| OR | 如果至少一个对应的位为 TRUE，则为 TRUE |
| NAND | 如果至少一个对应的位为 FALSE，则为 TRUE |
| NOR | 如果没有对应的位为 TRUE，则为 TRUE |
| XOR | 如果有奇数个对应位为 TRUE，则为 TRUE |
| NOT | 如果输入为 FALSE，则为 TRUE（仅适用于单个输入） |

##### 编程用法

|  |
| --- |
| **模块参数**：`logicop` |
| **类型**：字符向量 |
| **值**：`'AND'`|`'OR'` |`'NAND'`|`'NOR'` |`'XOR'`  | `'NOT'` |
| **默认值**：`'AND'` |

#### **使用位掩码** — 选择使用位掩码 选中 (默认) | 未选中

选择要使用位掩码。清除此复选框将启用**输入端口数目**并禁用**位掩码**和**将掩码视为**。

##### 编程用法

|  |
| --- |
| **模块参数**：`UseBitMask` |
| **类型**：字符向量 |
| **值**：`'off'`|`'on'` |
| **默认值**：`'on'` |

#### **输入端口数目** — 输入信号的数量 1 (默认) | 整数

指定输入数目。您可以有多个输入端口。

##### 依赖关系

清除**使用位掩码**复选框将启用**输入端口数目**并禁用**位掩码**和**将掩码视为**。

##### 编程用法

|  |
| --- |
| **模块参数**：`NumInputPorts` |
| **类型**：字符向量 |
| **值**：正整数 |
| **默认值**：`'1'` |

#### **位掩码** — 要与单个输入关联的位掩码 bin2dec (默认)

指定要与单个输入关联的位掩码。此参数将值读取为十六进制值。

您可以使用位掩码设置、获取或清除输入位。

| 要执行... | 将 Operator 参数设置为... | 并按此方式创建位掩码... |
| --- | --- | --- |
| 位设置 | OR | 对您要设置为 1 的每个对应的输入位使用 1 |
| 位清除 | AND | 对您要设置为 0 的每个对应的输入位使用 0 |
| 位获取 | AND | 对您要获取的每个对应的输入位使用 1 |

假设您要设置 8 位输入向量的第四位。位掩码将为 00010000，对于**位掩码**参数，您可以将其指定为 `2^4`。要清除该位，位掩码将为 11101111，对于**位掩码**参数，您可以将其指定为 `2^7+2^6+2^5+2^3+2^2+2^1+2^0`。

**提示**

不要使用大于 53 位的掩码。否则，仿真过程中将出现错误消息。

##### 依赖关系

仅当您选择**使用位掩码**时，此参数才可用。

##### 编程用法

|  |
| --- |
| **模块参数**：`BitMask` |
| **类型**：字符向量 |
| **值**：正整数 |
| **默认值**：`'bin2dec('11011001')'` |

#### **将掩码视为** — 将掩码视为真实值还是存储的整数 **存储的整数** (默认) | **真实值**

指定将掩码视为真实值还是存储的整数。

编码方案是 *`V`* = *`SQ`* + *`B`*，如 Fixed-Point Designer™ 文档中的定标 (Fixed-Point Designer)部分所述。**真实值**将掩码视为 *`V`*。**存储的整数**将掩码视为 *`Q`*。

##### 依赖关系

仅当您选择**使用位掩码**时，此参数才可用。

##### 编程用法

|  |
| --- |
| **模块参数**：`BitMaskRealWorld` |
| **类型**：字符向量 |
| **值**：`'Real World Value'` | `'Stored Integer'` |
| **默认值**：`'Stored Integer'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Booleana` | `fixed point` | `integer` |
| **直接馈通** | `否` |
| **多维信号** | `是` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |
|  |  |
| --- | --- |
| a 建议不要对布尔信号进行位运算。 | |

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

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Logic and Bit Operations HDL Coder / Logic and Bit Operations

## Description

The Bitwise Operator block performs the bitwise operation that you
specify on one or more operands. Unlike logic operations of the Logical Operator block, bitwise
operations treat the operands as a vector of bits rather than a single value.

### Restrictions on Block Operations

The Bitwise Operator block does not support shift operations. For
shift operations, use the Shift Arithmetic block.

When configured as a multi-input XOR gate, this block performs modulo-2 addition
according to the IEEE® Standard for Logic Elements.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector

Input signal, specified as a scalar or vector.

- The NOT operator accepts only one input, which can be a scalar
  or a vector. If the input is a vector, the output is a vector of
  the same size containing the bitwise logical complements of the
  input vector elements.
- For a single vector input, the block applies the operation
  (except the NOT operator) to all elements of the vector.
- For two or more inputs, the block performs the operation
  between all of the inputs. If the inputs are vectors, the block
  performs the operation between corresponding elements of the
  vectors to produce a vector output.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector

The output signal specified as the output data type, which the block
inherits from the driving block, must represent zero exactly. Data types
that satisfy this condition include signed and unsigned integer data
types.

The size of the block output depends on the number of inputs, the
vector size, and the operator you select. If you do not specify a bit
mask, the output is a scalar. If you do specify a bit mask, the output
is a vector.

**Data Types:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### **Operator** — Bitwise logical operator AND (default) | OR | NOR | NAND | XOR | NOT

Specify the bitwise logical operator for the block operands.

You can select one of these bitwise operations:

| Bitwise Operation | Description |
| --- | --- |
| AND | TRUE if the corresponding bits are all TRUE |
| OR | TRUE if at least one of the corresponding bits is TRUE |
| NAND | TRUE if at least one of the corresponding bits is FALSE |
| NOR | TRUE if no corresponding bits are TRUE |
| XOR | TRUE if an odd number of corresponding bits are TRUE |
| NOT | TRUE if the input is FALSE (available only for single input) |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `logicop` |
| **Type**: character vector |
| **Values**: `'AND'`|`'OR'`|`'NAND'`|`'NOR'`|`'XOR'`  | `'NOT'` |
| **Default**: `'AND'` |

### **Use bit mask** — Select to use bit mask checked (default) | unchecked

Select to use the bit mask. Clearing this check box enables **Number of input ports** and disables **Bit Mask** and **Treat mask
as**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `UseBitMask` |
| **Type**: character vector |
| **Values**: `'off'`|`'on'` |
| **Default**: `'on'` |

### **Number of input ports** — Number of input signals 1 (default) | integer

Specify the number of inputs. You can have more than one input
ports.

#### Dependency

Clearing the **Use bit mask** check box enables
**Number of input ports** and disables
**Bit Mask** and **Treat mask as**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `NumInputPorts` |
| **Type**: character vector |
| **Values**: positive integer |
| **Default**: `'1'` |

### **Bit Mask** — Bit mask to associate with a single input bin2dec (default)

Specify the bit mask to associate with a single input. This parameter
reads values as hexadecimal values.

You can use the bit mask to set, get, or clear a bit on the input.

| To perform a... | Set the Operator parameter to... | And create a bit mask with... |
| --- | --- | --- |
| Bit set | OR | A 1 for each corresponding input bit that you want to set to 1 |
| Bit clear | AND | A 0 for each corresponding input bit that you want to set to 0 |
| Bit get | AND | A 1 for each corresponding input bit that you want to get |

Suppose you want to set the fourth bit of an 8-bit input vector. The bit
mask would be 00010000, which you can specify as `2^4` for
the **Bit Mask** parameter. To clear the bit, the bit mask
would be 11101111, which you can specify as
`2^7+2^6+2^5+2^3+2^2+2^1+2^0` for the **Bit
Mask** parameter.

**Tip**

Do not use a mask greater than 53 bits. Otherwise, an error message
appears during simulation.

#### Dependency

This parameter is available only when you select **Use bit
mask**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BitMask` |
| **Type**: character vector |
| **Values**: positive integer |
| **Default**: `'bin2dec('11011001')'` |

### **Treat mask as** — Treat the mask as a real-world value or a stored integer `Stored Integer` (default) | `Real World Value`

Specify whether to treat the mask as a real-world value or a stored
integer.

The encoding scheme is *`V`* = *`SQ`*
+ *`B`*, as described in Scaling (Fixed-Point Designer) in the Fixed-Point Designer™ documentation. `Real World Value`
treats the mask as *`V`*. `Stored
Integer` treats the mask as
*`Q`*.

#### Dependency

This parameter is available only when you select **Use bit
mask**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `BitMaskRealWorld` |
| **Type**: character vector |
| **Values**: `'Real World Value'` | `'Stored Integer'` |
| **Default**: `'Stored Integer'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `fixed point` | `integer` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Bit operations are not recommended for use with Boolean signals. | |

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

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
