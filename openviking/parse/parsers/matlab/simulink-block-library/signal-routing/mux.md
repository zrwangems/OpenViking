---
type: simulink-block
title: 'Mux'
family: signal-routing
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'mux'
---

# Mux

Combine input signals of same data type and complexity into virtual vector

## 中文

将相同数据类型和复/实性的输入信号合并为虚拟向量

### 所属库

Simulink / Commonly Used Blocks Simulink / Signal Routing HDL Coder / Commonly Used Blocks HDL Coder / Signal Routing

### 描述

Mux 模块将具有相同数据类型和复/实性的输入合并为一个虚拟向量。您可以使用多个 Mux 模块分多个阶段创建复路信号，但结果是平面结构，就像您只使用一个 Mux 模块一样。

理想情况下，使用 Mux 模块仅对函数调用信号进行分组。

Mux 模块可以基于具有相同数据类型和复/实性的信号创建一个虚拟向量，但其他模块可以更灵活、更高效地对信号进行分组。

- 要对信号或消息进行分组，请使用 Bus Creator 模块，而不是 Mux 模块。Bus Creator 模块会创建虚拟总线，让您能够灵活地将不同数据类型和复/实性的元素进行组合。虚拟总线还允许您按名称而不是索引来访问元素。如果模块需要虚拟向量而不是虚拟总线，模型编译会将总线转换为向量。
- 要串联输入信号，请使用 Vector Concatenate 模块，而不是 Mux 模块。Vector Concatenate 模块创建一个非虚拟向量，这可提高生成代码的效率。

有关复路信号、虚拟总线和串联信号的比较，请参阅Explore Composite Interfaces。

### 端口

#### 输入

#### **Port\_1** — 要包含在复路信号中的输入信号 标量 | 向量

要包含在复路信号中的输入信号，指定为标量或向量。

Mux 模块的输入信号可以是标量和向量的任意组合，但它们必须具有相同的数据类型和复/实性或为函数调用信号。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `image`
**复数支持:** 是
#### 输出

#### **Port\_1** — 输出复路信号 向量

由合并的输入信号组成的输出复路信号，以向量形式返回。

输出复路信号的元素按照输入信号的端口顺序排列。有关各种模块方向的端口顺序的描述，请参阅标识旋转或翻转模块上的端口位置。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `image`

### 参数

#### **输入数目** — 输入信号的数量 2 (默认) | 标量 | 向量 | 元胞数组 | 以逗号分隔的信号名称列表

输入信号的数量，指定为标量、向量、元胞数组或以逗号分隔的信号名称列表。其中一些格式允许您指定信号名称和大小，如下表中所述。

| 格式 | 模块行为 |
| --- | --- |
| 标量 | Mux 模块的输入数目。  使用此格式时，模块接受任何大小的标量或向量信号。软件为每个输入指定名称 `signalN`，其中 `N` 表示输入端口号。 |
| 向量 | 向量的长度指定输入数目。每个元素指定对应输入的大小。  正值指定对应的端口只能接受该大小的向量。例如，`[2 3]` 指定两个大小分别为 `2` 和 `3` 的输入端口。如果输入信号的宽度与预期的宽度不匹配，则会显示错误消息。值 `-1` 指定对应的端口可以接受任意大小的标量或向量。 |
| 元胞数组 | 元胞数组的长度指定输入数目。每个元胞的值指定对应输入的大小。  标量值 `N` 指定向量大小 `N`。值为 `-1` 意味着对应的端口可以接受任意大小的标量或向量信号。 |
| 以逗号分隔的信号名称列表 | 以逗号分隔的信号名称列表。软件将每个名称分配给对应的端口和信号。例如，如果输入 `position,velocity`，Mux 模块将有两个输入，名称分别为 `position` 和 `velocity`。 |

不支持指定非双精度值，例如 `single(3)`。

##### 提示

如果您为**输入数目**参数指定了标量，而所有输入端口都已连接，则当您在靠近 Mux 模块输入端的位置绘制新的信号线时，软件会添加一个端口并更新该参数。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `Inputs` |
| **值:** | `'2'` (默认) | scalar in quotes | vector in quotes | cell array in quotes | comma-separated list of signal names in quotes |
| **数据类型:** | `char` | `string` |

**示例:** `set_param(gcb,'Inputs','5')`

**示例:** `set_param(gcb,'Inputs','[2 3]')`

**示例:** `set_param(gcb,'Inputs','{3}')`

**示例:** `set_param(gcb,'Inputs','position,velocity')`

#### **显示选项** — 模块图标外观 **bar** (默认) | **信号** | **无**

模块图标外观，指定为**竖线**、**信号**或**无**。

- **竖线** - 不显示文本
- **信号** - 显示输入信号名称
- **无** - 显示模块的类型 (Mux)

根据需要调整模块的大小，以适合模块图标上的文本。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `DisplayOption` |
| **值:** | `'bar'` (默认) | `'signals'` | `'none'` |

**示例:** `set_param(gcb,'DisplayOption','signals')`

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

实际数据类型或功能支持取决于模块实现。

为了提高所生成代码的效率，请使用 Vector Concatenate 模块，而不是 Mux 模块。Vector Concatenate 模块创建一个非虚拟向量。

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

**复数数据支持**

此模块支持复信号的代码生成。

**限制**

HDL 代码生成不支持总线。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型或功能支持取决于模块实现。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Commonly Used Blocks Simulink / Signal Routing HDL Coder / Commonly Used Blocks HDL Coder / Signal Routing

## Description

The Mux block combines inputs with the same data type and complexity
into a virtual vector. You can use multiple Mux blocks to create a mux signal
in stages, but the result is flat as if you used a single Mux block.

Ideally, use Mux blocks to group only function-call signals.

While a Mux block can create a virtual vector from signals that have the
same data type and complexity, other blocks group signals in ways that provide more
flexibility and efficiency.

- To group signals or messages, use a Bus Creator block instead of a Mux block. The Bus
  Creator block creates virtual buses, which give you the flexibility to group
  elements of different data types and complexity. Virtual buses also let you access
  elements by name instead of by index. If a block requires a virtual vector instead of a
  virtual bus, model compilation converts the bus to a vector.
- To concatenate input signals, use a Vector Concatenate block instead of a Mux block. The
  Vector Concatenate block creates a nonvirtual vector, which improves the
  efficiency of generated code.

For a comparison of mux signals, virtual buses, and concatenated signals, see Explore Composite Interfaces.

## Ports

### Input

### **Port\_1** — Input signal to include in mux signal scalar | vector

Input signal to include in the mux signal, specified as a scalar or
vector.

The input signals for a Mux block can be any
combination of scalars and vectors, but they must have the same data type and
complexity or be function-call signals.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `image`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Output mux signal vector

Output mux signal composed of the combined input signals, returned as
a vector.

The elements of the output mux signal take their order from the port
order of the input signals. For a description of the port order for
various block orientations, see Identify Port Location on Rotated or Flipped Block.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `image`

## Parameters

### **Number of inputs** — Number of input signals 2 (default) | scalar | vector | cell array | comma-separated list of signal names

The number of input signals, specified as a scalar, vector, cell array, or
comma-separated list of signal names. Some of these formats allow you to specify the
signal names and sizes, as described in this table.

| Format | Block Behavior |
| --- | --- |
| Scalar | The number of inputs to the Mux block.  When you use this format, the block accepts scalar or vector signals of any size. The software assigns each input the name `signalN`, where `N` is the input port number. |
| Vector | The length of the vector specifies the number of inputs. Each element specifies the size of the corresponding input.  A positive value specifies that the corresponding port can accept only vectors of that size. For example, `[2 3]` specifies two input ports of sizes `2` and `3`, respectively. If an input signal width does not match the expected width, an error message appears. A value of `-1` specifies that the corresponding port can accept scalars or vectors of any size. |
| Cell array | The length of the cell array specifies the number of inputs. The value of each cell specifies the size of the corresponding input.  A scalar value `N` specifies a vector of size `N`. A value of `-1` means that the corresponding port can accept scalar or vector signals of any size. |
| Comma-separated list of signal names | A list of signal names separated by commas. The software assigns each name to the corresponding port and signal. For example, if you enter `position,velocity`, the Mux block has two inputs, named `position` and `velocity`. |

Specifying
a nondouble value, such as `single(3)`, is not
supported.

#### Tips

If you specify a scalar for the **Number of inputs** parameter
and all of the input ports are connected, as you draw a new signal line close to input
side of a Mux block, the software adds a port and updates the
parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Inputs` |
| **Values:** | `'2'` (default) | scalar in quotes | vector in quotes | cell array in quotes | comma-separated list of signal names in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param(gcb,'Inputs','5')`

**Example:** `set_param(gcb,'Inputs','[2 3]')`

**Example:** `set_param(gcb,'Inputs','{3}')`

**Example:** `set_param(gcb,'Inputs','position,velocity')`

### **Display option** — Block icon appearance `bar` (default) | `signals` | `none`

Block icon appearance, specified as `bar`,
`signals`, or `none`.

- `bar` — Displays no text
- `signals` — Displays the input signal names
- `none` — Displays the type of block
  (Mux)

Resize the block as necessary to fit the text on the block icon.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `DisplayOption` |
| **Values:** | `'bar'` (default) | `'signals'` | `'none'` |

**Example:** `set_param(gcb,'DisplayOption','signals')`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual data type or capability support depends on block implementation.

To improve the efficiency of generated code, use a Vector
Concatenate block instead of a Mux block. The Vector
Concatenate block creates a nonvirtual vector.

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

**Complex Data Support**

This block supports code generation for complex signals.

**Restrictions**

Buses are not supported for HDL code generation.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type or capability support depends on block implementation.

## Version History

**Introduced before R2006a**
