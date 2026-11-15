---
type: simulink-block
title: 'Switch Case'
family: ports-and-subsystems
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Ports and Subsystems'
documentation_page: 'switchcase'
---

# Switch Case

Select subsystem execution using logic similar to switch statement

## 中文

使用类似于 switch 语句的逻辑选择子系统执行

### 所属库

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

### 描述

Switch Case 模块以及包含 Action Port 模块的 Switch Case Action Subsystem 模块，实现 switch 逻辑来控制子系统的执行。有关使用 Switch Case 模块的示例，请参阅选择子系统执行。

Model ex\_switch\_case\_block

Switch Case 模块具有单个输入。要选择一个 case，请使用 **Case 条件**参数定义输入值。计算顺序为从第一种情况开始由上往下进行。

每个 case 都与一个连接到 Switch Case Action Subsystem 模块的输出端口相关联。当选择一个 case 时，相关联的输出端口发送动作信号来执行子系统。

在所有其他 case 条件的计算结果都为 false 时，会选择 `default` case。提供 `default` case 是可选的，即使其他 case 条件没有用完每个可能的输入值也是如此。

Switch Case 模块的 case 在 Switch Case Action Subsystem 模块执行后包含一个隐含的中断。因此，Simulink® Switch Case 模块没有标准 C 语言的 `switch` 语句中存在的 fall-through（落空）行为。

### 端口

#### 输入

#### **u1 (logical operator)** — case 选择的值 标量

对于 Switch Case 模块上标签为 **u1** 的端口，输入可以是：

- 具有 Simulink 支持的内置数据类型的标量值。然而，Switch Case 模块不支持布尔或定点数据类型，它将数值输入截断为 32 位有符号整数。
- 任何枚举数据类型的标量值。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `enumerated`
#### 输出

#### **case** — 用于 Switch Case Action Subsystem 模块的动作信号 标量

来自 **Case** 和**默认**端口的输出是连接到 Switch Case Action Subsystem 模块的动作信号。

### 参数

#### **Case 条件** — 指定 case 值 `{1}` (默认) | case 列表

使用 MATLAB® 元胞表示法指定 case 值。

{1}
:   指定当输入端口值为 `1` 时标签为 `case[1]` 的输出端口输出动作信号。

具有 case 分配的端口列表
:   使用 MATLAB 元胞表示法指定多个 case 和端口。例如，输入 `{1,[7,9,4]}` 将指定当输入值为 `1` 时，运行输出端口 `case[1]`；当输入值为 `7`、`9` 或 `4` 时，运行输出端口 `case [7 9 4]`。

    可使用冒号表示法指定某一整数范围内的情况条件。例如，输入 `{[1:5]}` 将指定当输入值为 `1`、`2`、`3`、`4` 或 `5` 时，运行输出端口 **case[1 2 3 4 5]**。

    根据模块大小，对于较长的 case 条件列表，其中的 case 可能在 Switch Case 模块上以终止省略号 (...) 缩略显示。

    可使用一个枚举类型的名称指定一个情况条件，其中包含对应于该枚举类型中每个值的情况。

##### 编程用法

|  |
| --- |
| **模块参数**：`CaseConditions` |
| **类型**：字符向量 |
| **值**：`'{1}'` | 用引号引起来的 case 列表 |
| **默认值**：`'{1}'` |

#### **显示默认 case** — 控制默认输出端口的显示 `on` (默认) | `off`

控制默认输出端口的显示。

on
:   将默认输出端口显示为 Switch Case 模块的最后一个 case。您可由此指定默认 case，以在输入值与任何其他 case 值都不匹配时执行。

off
:   隐藏默认输出端口。

##### 编程用法

|  |
| --- |
| **模块参数**：`ShowDefaultCase` |
| **类型**：字符向量 |
| **值**：`'on'` | `'off'` |
| **默认值**：`'on'` |

#### **启用过零检测** — 控制过零检测 `on` (默认) | `off`

控制过零检测。

on
:   检测过零点。

off
:   不检测过零点。

##### 编程用法

|  |
| --- |
| **模块参数**：`ZeroCross` |
| **类型：**字符向量 |
| **值：**`'on'` | `'off'` |
| **默认值：**`'on'` |

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `enumerated` | `integer` | `single` |
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

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

当在 For Each Subsystem 模块中使用此模块时，不支持代码生成。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Ports & Subsystems HDL Coder / Ports & Subsystems

## Description

The Switch Case block with
Switch
Case Action Subsystem blocks containing
Action
Port blocks, implements switch logic to control subsystem execution. For an
example that uses the Switch Case block, see Select Subsystem Execution.

Model ex\_switch\_case\_block

A Switch Case block has a single input. To select a case, define the
input value using the **Case conditions** parameter. The cases are evaluated
top down starting with the first case.

Each case is associated with an output port that is attached to a Switch Case
Action Subsystem block. When a case is selected, the associated output port
sends an action signal to execute the subsystem.

A `default` case is selected after all of the other case conditions
evaluate to false. Providing a `default` case is optional, even if the
other case conditions do not exhaust every possible input value.

Cases for the Switch Case block contain an implied break after a
Switch Case Action Subsystem block is executed. Therefore, there is
no fall through behavior for the Simulink®
Switch Case block as found in standard C `switch`
statements.

## Ports

### Input

### **u1 (logical operator)** — Value for case selection scalar

Input to the port labeled **u1** of a Switch
Case block can be:

- A scalar value with a built-in data type that Simulink supports. However, the Switch Case
  block does not support Boolean or fixed-point data types, and it
  truncates numeric inputs to 32-bit signed integers.
- A scalar value of any enumerated data type.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `enumerated`
### Output

### **case** — Action signal for a Switch Case Action Subsystem block scalar

Output from the **Case** and
**default** ports are action signals connected to
Switch Case Action Subsystem blocks.

## Parameters

### **Case conditions** — Specify case values `{1}` (default) | list of cases

Specify the cases values using MATLAB® cell notation.

{1}
:   Specify the output port labeled
    `case[1]`outputs an action signal when the
    input port value is `1`.

list of ports with case assignments
:   Specify multiple cases and ports using MATLAB cell notation. For example, entering
    `{1,[7,9,4]}` specifies that output port
    `case[1]` is run when the input value is
    `1`, and output port `case [7 9
    4]` is run when the input value is
    `7`, `9`, or
    `4`.

    You can use colon notation to specify a range of integer case
    conditions. For example, entering `{[1:5]}`
    specifies that output port **case[1 2 3 4 5]**
    is run when the input value is `1`,
    `2`, `3`,
    `4`, or `5`.

    Depending on block size, cases from a long list of case
    conditions are displayed in shortened form on the face of the
    Switch Case block, using a terminating
    ellipsis (...).

    You can use the name of an enumerated type to specify case
    conditions that include a case for every value in that
    enumerated type.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CaseConditions` |
| **Type**: character vector |
| **Values**: `'{1}'` | list of cases in quotes |
| **Default**: `'{1}'` |

### **Show default case** — Control display of default output port `on` (default) | `off`

Control display of default output port.

on
:   Display default output port as the last case on the
    Switch Case block. This allows you to specify
    a default case that executes when the input value does not match
    any of the other case values.

off
:   Hide default output port.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `ShowDefaultCase` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'on'` |

### **Enable zero-crossing detection** — Control zero-crossing detection `on` (default) | `off`

Control zero-crossing detection.

on
:   Detect zero crossings.

off
:   Do not detect zero crossings.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ZeroCross` |
| **Type:** character vector |
| **Values:** `'on'` | `'off'` |
| **Default:** `'on'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `enumerated` | `integer` | `single` |
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

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

Code generation not supported when this block is used inside a For Each
Subsystem block.

## Version History

**Introduced before R2006a**
