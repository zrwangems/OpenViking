---
type: simulink-block
title: 'Signal Conversion'
family: signal-attributes
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Signal Attributes'
documentation_page: 'signalconversion'
---

# Signal Conversion

Convert signal to new type without altering signal values

## 中文

将信号转换为新类型，而不改变信号值

### 所属库

Simulink / Signal Attributes HDL Coder / Signal Attributes

### 描述

Signal Conversion 模块可将信号从一种类型转换为另一种类型。要选择要执行的转换类型，请使用**输出**参数或下列预配置的 Signal Conversion 模块之一：

- Signal Copy 模块
- To Virtual Bus 模块
- To Nonvirtual Bus 模块

### 端口

#### 输入

#### **Port\_1** — 要转换的输入信号 标量 | 向量 | 矩阵 | 数组 | 总线

输入信号是标量、向量、矩阵、数组或总线，此模块可将其转换为另一种类型。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
#### 输出

#### **Port\_1** — 转换信号 标量 | 向量 | 矩阵 | 数组 | 总线

输出信号是转换为指定类型的输入信号。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

### 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条中，在**仿真**选项卡的**准备**库中，选择**属性检查器**。

#### **输出** — 转换的类型 **信号副本** | **虚拟总线** | **非虚拟总线**

指定要执行的转换类型。

- **信号副本** - 创建输入信号的连续副本。此值是 Signal Conversion 和 Signal Copy 模块的默认值。
- **虚拟总线** - 将非虚拟总线转换为虚拟总线。此值是 To Virtual Bus 模块的默认值。
- **非虚拟总线** - 将虚拟总线转换为非虚拟总线。此值是 To Nonvirtual Bus 模块的默认值。

对于**信号副本**选项，输入类型决定了模块如何生成副本。

例如，假设该模块接收复路信号，该信号包含占用不连续内存区域的元素。在每个时间步中，转换将为复路信号的元素分配连续的内存区域，并将由模块的输入端口表示的不连续区域的值复制到由模块的输出端口表示的连续区域。输出是向量，其元素占据连续内存区域。

您使用的转换类型取决于您的建模目的。

| 建模目的 | 选项 |
| --- | --- |
| 减少为复路信号生成的代码。  有关涉及 Simulink Coder™ 软件的示例，请参阅Generate Reentrant Code from Subsystems (Simulink Coder)。 | **信号副本** |
| 将具有常数采样时间的模块连接到使能子系统的输出端口。 | **信号副本** |
| 将非虚拟总线转换为虚拟总线，以便节约内存。 | **虚拟总线** |
| 将虚拟总线传递给需要非虚拟总线的建模结构。 | **非虚拟总线** |
| 创建总线数组的副本。  该模块无法将总线数组转换为非虚拟或虚拟总线。要从总线数组中提取一个总线，请使用 Selector 模块。 | **信号副本** |

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `ConversionOutput` |
| **值:** | `'Signal copy'` (默认) | `'Virtual bus'` | `'Nonvirtual bus'` |

**示例:** `set_param(gcb,'ConversionOutput','Virtual bus')`

#### **数据类型** — 非虚拟总线数据类型 `Inherit: auto` (默认) | `Bus: <object name>` | `<data type expression>`

指定此模块生成的非虚拟总线的输出数据类型。

- `Inherit: auto` - 从上游模块继承数据类型。例如，从上游 Bus Creator 模块继承 `Simulink.Bus` 对象数据类型。
- `Bus: <object name>` 或 `<data type expression>` - 指定与输入总线的层次结构匹配的 `Simulink.Bus` 对象。如果上游 Bus Creator 模块指定总线对象，请指定相同的总线对象。

**数据类型助手**可帮助您设置数据属性。要使用**数据类型助手**，请点击 the Show data type assistant button。有关详细信息，请参阅使用数据类型助手指定数据类型。

##### 依赖关系

要启用此参数，请将**输出**设置为**非虚拟总线**。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `OutDataTypeStr` |
| **值:** | `'Inherit: auto'` (默认) | `'Bus: <object name>'` | `'<data type expression>'` |

**示例:** `set_param(gcb,'OutDataTypeStr','Bus: myBusObj')`

#### **从 '模块简化' 优化中排除此模块** — 从模块简化优化中排除模块的选项 `off` (默认) | `on`

默认情况下，当输入信号的元素占据连续内存区域时，软件会从编译的模型中消除此模块以作为优化。有关详细信息，请参阅Block reduction。

要防止从编译的模型中消除此模块，请选择此参数。

对此参数的更改将在下次编译模型时生效。

##### 依赖关系

要启用此参数，请将**输出**设置为**信号副本**。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `OverrideOpt` |
| **值:** | `'off'` (默认) | `'on'` |

**示例:** `set_param(gcb,'OverrideOpt','on')`

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `image` | `integer` | `single` | `string` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有直通实现。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复信号的代码生成。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Signal Attributes HDL Coder / Signal Attributes

## Description

The Signal Conversion block converts a signal from one type to another. To
select the type of conversion to perform, use the **Output**
parameter or one of the preconfigured Signal Conversion blocks:

- Signal Copy block
- To Virtual Bus block
- To Nonvirtual Bus block

## Ports

### Input

### **Port\_1** — Input signal to convert scalar | vector | matrix | array | bus

The input signal is a scalar, vector, matrix, array, or bus that this block converts to
another type.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`
### Output

### **Port\_1** — Converted signal scalar | vector | matrix | array | bus

The output signal is the input signal converted to the specified type.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image`

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Output** — Type of conversion `Signal copy` | `Virtual bus` | `Nonvirtual bus`

Specify the type of conversion to perform.

- `Signal copy` — Create a contiguous copy of the input
  signal. This value is the default value for the Signal Conversion and
  Signal Copy blocks.
- `Virtual bus` — Convert a nonvirtual bus to a virtual
  bus. This value is the default value for the To Virtual Bus
  block.
- `Nonvirtual bus` — Convert a virtual bus to a
  nonvirtual bus. This value is the default value for the To Nonvirtual
  Bus block.

For the `Signal copy` option, the type of input determines how
the block makes the copy.

For example, suppose the block receives a mux signal, which has elements that occupy
discontiguous areas of memory. The conversion allocates a contiguous area of memory for
the elements of the mux signal and copies the values from the discontiguous areas
represented by the block input to the contiguous areas represented by the block output
at each time step. The output is a vector with elements that occupy contiguous areas of
memory.

The type of conversion that you use depends on your modeling goal.

| Modeling Goal | Option |
| --- | --- |
| Reduce generated code for a muxed signal.  For an example involving Simulink Coder™ software, see Generate Reentrant Code from Subsystems (Simulink Coder). | `Signal copy` |
| Connect a block with a constant sample time to an output port of an enabled subsystem. | `Signal copy` |
| Save memory by converting a nonvirtual bus to a virtual bus. | `Virtual bus` |
| Pass a virtual bus to a modeling construct that requires a nonvirtual bus. | `Nonvirtual bus` |
| Create a copy of an array of buses.  The block cannot convert an array of buses to a nonvirtual or virtual bus. To extract a bus from an array of buses, use a Selector block. | `Signal copy` |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ConversionOutput` |
| **Values:** | `'Signal copy'` (default) | `'Virtual bus'` | `'Nonvirtual bus'` |

**Example:** `set_param(gcb,'ConversionOutput','Virtual
bus')`

### **Data type** — Nonvirtual bus data type `Inherit: auto` (default) | `Bus: <object name>` | `<data type expression>`

Specify the output data type of the nonvirtual bus that this block
produces.

- `Inherit: auto` — Inherit the data type from an
  upstream block. For example, inherit the `Simulink.Bus` object
  data type from an upstream Bus Creator
  block.
- `Bus: <object name>` or `<data type
  expression>` — Specify a `Simulink.Bus`
  object that matches the hierarchy of the input bus. If an upstream
  Bus Creator block specifies a bus object, specify
  the same bus object.

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, set **Output** to `Nonvirtual
bus`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutDataTypeStr` |
| **Values:** | `'Inherit: auto'` (default) | `'Bus: <object name>'` | `'<data type expression>'` |

**Example:** `set_param(gcb,'OutDataTypeStr','Bus:
myBusObj')`

### **Exclude this block from 'Block reduction' optimization** — Option to exclude block from block reduction optimization `off` (default) | `on`

When the elements of the input signal occupy contiguous areas of memory, by default,
the software eliminates this block from the compiled model as an optimization. For more
information, see Block reduction.

To prevent this block from being eliminated from the compiled model, select this
parameter.

Changes to this parameter take effect the next time you compile the model.

#### Dependencies

To enable this parameter, set **Output**
to `Signal copy`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OverrideOpt` |
| **Values:** | `'off'` (default) | `'on'` |

**Example:** `set_param(gcb,'OverrideOpt','on')`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `image` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Architecture**

This block has a pass-through implementation.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Complex Data Support**

This block supports code generation for complex signals.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
