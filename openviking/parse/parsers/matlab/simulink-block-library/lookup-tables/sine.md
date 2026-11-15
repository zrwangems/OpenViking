---
type: simulink-block
title: 'Sine'
family: lookup-tables
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Lookup Tables'
documentation_page: 'sine'
---

# Sine

Implement fixed-point sine or cosine wave using lookup table approach that exploits quarter wave symmetry

## 中文

通过利用象限波对称性的查找表方法实现定点正弦或余弦波

### 所属库

Simulink / Lookup Tables

### 描述

Sine 和 Cosine 模块通过利用象限波对称性的查找表方法来实现定点正弦波、余弦波或同时实现两者。模块可以输出输入信号的以下函数，具体取决于您为**输出公式**参数选择的设置：

- sin(2π*u*)
- cos(2π*u*)
- exp(*j*2π*u*)
- sin(2π*u*) and cos(2π*u*)

请在**查找表的数据点数**参数中定义查找表点数。当您将查找表数据点指定为 `(2^n)+1`（其中 *n* 是整数）时，模块实现最有效。

使用**输出字长**参数指定定点输出数据类型的字长。输出的小数长度等于输出字长减去 2。

### 端口

#### 输入

#### **u** — 要实现为定点正弦波或余弦波的输入信号 实数值信号

输入信号 u，指定为实数值标量、向量或矩阵。

要获得有意义的模块输出，模块输入值应位于 [0, 1) 的范围内。对于不在此范围内的输入值，它们将被转换为无符号数据类型，发生溢出时将进行绕回。对于这些超出范围的输入，模块输出可能没有意义。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
#### 输出

#### **sin(2\*pi\*u)** — 定点正弦波 实数值定点信号

定点正弦波，使用查找表方法实现。

##### 依赖关系

当**输出公式**设置为 **sin(2\*pi\*u)** 或 **sin(2\*pi\*u) and cos(2\*pi\*u)** 时，此端口启用。

**数据类型:** `fixed point`

#### **cos(2\*pi\*u)** — 定点余弦波 实数值定点信号

定点余弦波，使用查找表方法实现。

##### 依赖关系

当**输出公式**设置为 **cos(2\*pi\*u)** 或 **sin(2\*pi\*u) and cos(2\*pi\*u)** 时，此端口启用。

**数据类型:** `fixed point`

#### **exp(j\*2\*pi\*u)** — exp(j\*2\*pi\*u) 复数值定点信号

**exp(j\*2\*pi\*u)**，使用查找表方法实现。

##### 依赖关系

当**输出公式**设置为 **exp(j\*2\*pi\*u)** 时，此端口启用。

**数据类型:** `fixed point`

### 参数

#### **输出公式** — 选择要输出的信号 **cos(2\*pi\*u)** | **sin(2\*pi\*u)** | **exp(j\*2\*pi\*u)** | **sin(2\*pi\*u) and cos(2\*pi\*u)**

选择要输出的信号。

对于 Sine 模块，此参数的默认值为 **sin(2\*pi\*u)**。

对于 Cosine 模块，此参数的默认值为 **cos(2\*pi\*u)**。

##### 编程用法

|  |
| --- |
| **模块参数：**`Formula` |
| **值：**`'sin(2*pi*u)' | 'cos(2*pi*u)' | 'exp(j*2*pi*u)' | 'sin(2*pi*u) and cos(2*pi*u)'` |

#### **查找表的数据点数** — 指定要从查找表中检索的数据点数量 `(2^5)+1` (默认) | 整数，大于或等于 2

当您将查找表的数据点指定为 `(2^n)+1`（其中 *n* 是整数）时，实现的效率最高。为了与**输出字长**参数兼容，**查找表的数据点数**必须小于或等于 (2^(**Output word length**-2)+1)。

##### 编程用法

|  |
| --- |
| **模块参数：**`NumDataPoints` |
| **类型：**标量 |
| **值：**大于或等于 2 的整数 |
| **默认值：**`'(2^5)+1'` |

#### **输出字长** — 指定输出信号的定点数据类型的字长 `16` (默认) | 从 2 到 53 的整数

输出的小数长度等于输出字长减去 2。为了与**查找表的数据点数**参数兼容，(2^(**Output word length** - 2) +1) 必须大于或等于**查找表的数据点数**。

**注意**

模块使用双精度浮点值来构造查找表。因此，输出中可以实现的最大精度为 53 位。将字长值设置为大于 53 位并不会提高输出的精度。

##### 编程用法

|  |
| --- |
| **模块参数：**`OutputWordLength` |
| **类型：**标量 |
| **值：**从 2 到 53 的整数 |
| **默认值：**`'16'` |

#### **查找表的内部规则优先级** — 指定进行中间计算的内部规则 **速度** (默认) | **精度**

选择**速度**可以提高计算速度。但这样可能会损失精度，通常最多 2 位。

##### 编程用法

|  |
| --- |
| **模块参数：**`InternalRulePriority` |
| **值：**`'Speed' | 'Precision'` |
| **默认值：**`'Speed'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

HDL 代码通过使用您在 Simulink 模块参数中指定的四分之一波查找表来实现 Cosine 和 Sine 模块。

要避免在 HDL 代码中生成除法运算符 (`/`)，对于**查找表的数据点数**，请输入 `(2^n)+1`。*`n`* 是整数。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

**限制**

如果您使用 Intel® MAX 10 设备，要将查找表映射到 RAM，请当在 Quartus 工具中创建工程时添加以下 Tcl 命令：

`set_global_assignment -name INTERNAL_FLASH_UPDATE_MODE "SINGLE IMAGE WITH ERAM"`

**注意**

基于查找表的正弦和余弦模块不会生成硬件优化的 HDL 代码。为了获得更好的综合结果，请使用 Sine HDL Optimized and Cosine HDL Optimized (HDL Coder) 模块。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Lookup Tables

## Description

The Sine and Cosine blocks implement a sine wave, cosine
wave, or both in fixed point using a lookup table method that exploits quarter wave
symmetry. The block can output the following functions of the input signal, depending
upon what you select for the **Output formula** parameter:

- sin(2π*u*)
- cos(2π*u*)
- exp(*j*2π*u*)
- sin(2π*u*) and
  cos(2π*u*)

You define the number of lookup table points in the **Number of data points
for lookup table** parameter. The block implementation is most efficient
when you specify the lookup table data points to be
`(2^n)+1`, where *n* is an
integer.

Use the **Output word length** parameter to specify the word length
of the fixed-point output data type. The fraction length of the output is the output
word length minus 2.

## Ports

### Input

### **u** — Input signal to implement as fixed-point sine or cosine wave real-valued signal

Input signal, u, specified as a real-valued scalar, vector, or
matrix.

To obtain meaningful block output, the block input values should fall
within the range [0, 1). For input values that fall outside this range,
the values are cast to an unsigned data type, where overflows wrap. For
these out-of-range inputs, the block output might not be
meaningful.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **sin(2\*pi\*u)** — Fixed-point sine wave real-valued fixed-point signal

Fixed-point sine wave, implemented using a lookup table approach.

#### Dependencies

This port is enabled when the **Output formula**
is set to `sin(2*pi*u)` or
`sin(2*pi*u) and cos(2*pi*u)`.

**Data Types:** `fixed point`

### **cos(2\*pi\*u)** — Fixed-point cosine wave real-valued fixed-point signal

Fixed-point cosine wave, implemented using a lookup table
approach.

#### Dependencies

This port is enabled when the **Output formula**
is set to `cos(2*pi*u)` or
`sin(2*pi*u) and cos(2*pi*u)`.

**Data Types:** `fixed point`

### **exp(j\*2\*pi\*u)** — exp(j\*2\*pi\*u) complex-valued fixed-point signal

`exp(j*2*pi*u)`,
implemented using a lookup table approach.

#### Dependencies

This port is enabled when the **Output formula**
is set to `exp(j*2*pi*u)`.

**Data Types:** `fixed point`

## Parameters

### **Output formula** — Select the signals to output `cos(2*pi*u)` | `sin(2*pi*u)` | `exp(j*2*pi*u)` | `sin(2*pi*u) and cos(2*pi*u)`

Select the signals to output.

For the Sine block, the default value of this parameter is
`sin(2*pi*u)`.

For the Cosine block, the default value of this parameter
is `cos(2*pi*u)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Formula` |
| **Values:** `'sin(2*pi*u)' | 'cos(2*pi*u)' | 'exp(j*2*pi*u)' | 'sin(2*pi*u) and cos(2*pi*u)'` |

### **Number of data points for lookup table** — Specify the number of data points to retrieve from the lookup table `(2^5)+1` (default) | integer greater than or equal to 2

The implementation is most efficient when you specify the lookup table
data points to be `(2^n)+1`, where
*n* is an integer. To be compatible with the
**Output word length** parameter, the **Number
of data points for lookup table** must be less than or equal to (2^(**Output word
length**-2)+1).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `NumDataPoints` |
| **Type:** scalar |
| **Value:** integer greater than or equal to 2 |
| **Default:** `'(2^5)+1'` |

### **Output word length** — Specify the word length for the fixed-point data type of the output signal `16` (default) | integer from 2 to 53

The fraction length of the output is the output word length minus 2. To be
compatible with the **Number of data points for lookup
table** parameter, (2^(**Output word length** - 2)
+1) must be greater than or equal to **Number of data
points for lookup table**.

**Note**

The block uses double-precision floating-point values to construct
lookup tables. Therefore, the maximum amount of precision you can
achieve in your output is 53 bits. Setting the word length to values
greater than 53 bits does not improve the precision of your
output.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputWordLength` |
| **Type:** scalar |
| **Value:** integer from 2 to 53 |
| **Default:** `'16'` |

### **Internal rule priority for lookup table** — Specify the internal rule for intermediate calculations `Speed` (default) | `Precision`

Select `Speed` for faster calculations. If you
do, a loss of accuracy might occur, usually up to 2 bits.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InternalRulePriority` |
| **Values:** `'Speed' | 'Precision'` |
| **Default:** `'Speed'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

The HDL code implements Cosine and Sine blocks
by using the quarter-wave lookup table that you specify in the Simulink block
parameters.

To avoid generating a division operator
(`/`) in the HDL code, for **Number of data points
for lookup table**, enter
`(2^n)+1`.
*`n`* is an integer.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Limitations**

If you use Intel® MAX 10 device, to map the lookup table to RAM, add this Tcl
command when creating the project in the Quartus tool:

`set_global_assignment -name INTERNAL_FLASH_UPDATE_MODE "SINGLE IMAGE
WITH ERAM"`

**Note**

Lookup table-based sine and cosine blocks do not generate
hardware-optimized HDL code. For better synthesis results, use Sine HDL Optimized and Cosine HDL Optimized (HDL Coder) blocks.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
