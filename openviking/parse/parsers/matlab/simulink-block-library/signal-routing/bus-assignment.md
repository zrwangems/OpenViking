---
type: simulink-block
title: 'Bus Assignment'
family: signal-routing
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'busassignment'
---

# Bus Assignment

Assign new values to specified bus elements

## 中文

为指定的总线元素赋予新值

### 所属库

Simulink / Signal Routing HDL Coder / Signal Routing

### 描述

Bus Assignment 模块为选定总线元素赋予新值。使用 Bus Assignment 模块更改元素值，而无需提取元素并用所需元素重新组合为总线。Bus Assignment 模块简化了总线的更新，以反映在一个单独的组件（如子系统或引用模型）中发生的处理。

Bus Assignment 模块将连接到赋值端口的元素赋给连接到总线输入端口的总线的指定元素。该模块将替换先前分配给这些元素的元素。此更改不影响总线的构成。此更改仅影响元素的值。未替换的元素不受其他元素替换的影响。

被赋值的元素可以是非总线信号或总线（包括总线数组），只要它们是输入总线的元素即可。新值必须与原始总线中元素的属性匹配。

默认情况下，软件会修复 Bus Assignment 模块中由于上游总线层次结构发生变化而失效的选择。如果修复修改了模型，系统会向您发送警告通知。为防止软件自动进行这些修复，请将**修复总线选择**配置参数设置为**报错但不修复**。

### 端口

#### 输入

#### **Bus** — 具有要重新赋值的元素的输入总线 总线

输入虚拟或非虚拟总线可以包含该软件支持的任何数据类型的实数值或复数值元素，包括总线对象、定点数据类型和枚举数据类型。总线也可以包含总线数组。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
**复数支持:** 是

#### **:=** — 要赋给总线元素的新值 标量 | 向量 | 矩阵 | 数组 | 总线

**要赋值的元素**列表中的每个元素都对应一个赋值端口。端口标签指示对应于该端口的总线元素。对于名为 `signal1` 的元素，端口标签为**:= signal1**。

连接到赋值端口的总线或非总线信号必须具有与对应元素相同的结构体、数据类型和采样时间。要更改一个或多个元素的采样时间，请使用 Rate Transition 模块。有关详细信息，请参阅 Modify Sample Times for Nonvirtual Buses。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
**复数支持:** 是
#### 输出

#### **Bus** — 输出总线 总线

输出虚拟或非虚拟总线包含选定元素所赋予的总线元素值和其他元素的未修改的总线元素值。

**数据类型:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
**复数支持:** 是

### 参数

要以交互方式编辑 Bus Assignment 模块参数，请双击该模块。

#### **总线中的元素** — 输入总线的元素 只读: 元素名称列表

此 参数 为只读。

选择输入总线中要对其进行操作的元素。

元素名称旁边的箭头表示该元素是嵌套总线。要显示嵌套总线中的元素，请点击该箭头。

选择一个或多个元素后，点击：

- **查找** - 查找选定元素的源。软件将打开并突出显示包含元素源的系统。
- **选择** - 将选定元素添加到要赋值的元素列表中。有关详细信息，请参阅**要赋值的元素**。

要过滤输入元素长列表，请在**按名称过滤**框中指定搜索词。请勿将搜索词括在引号内。过滤器执行部分字符串搜索。

要访问过滤选项，请点击**按名称过滤**框右侧的 Show filtering options。

- **启用正则表达式** - 允许使用 MATLAB® 正则表达式来过滤元素名称。例如，要显示其名称以小写字母 `t` 结尾的所有元素（及其直接父级），请在**按名称过滤**框中输入 `t$`。有关详细信息，请参阅 正则表达式。
- **将过滤结果显示为扁平列表** - 以扁平列表形式显示过滤后的元素，该列表使用圆点表示法来反映总线层次结构。默认情况下，输入元素的列表以层次结构树形式显示元素。

要刷新列表以反映对输入总线的修改，请点击**刷新**。

##### 编程用法

要以编程方式获取模块参数值，请使用 `get_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `InputSignals` |
| **值:** | 只读: list of element names in a cell array or cell array of cell arrays |

**示例:** `get_param(gcb,'InputSignals')`

#### **要赋值的元素** — 要被赋予新值的总线元素 元素名称列表

对于此列表中的每个元素，模块都有一个对应的赋值端口。端口标签包含对应元素的名称。

要为元素添加赋值端口，请执行以下操作：

1. 从**总线中的元素**列表中选择一个或多个元素。

   如果您从**总线中的元素**列表中选择了多个元素，则您选择它们的顺序将确定它们在**要赋值的元素**列表中的顺序。
2. （可选）指定希望元素出现在**要赋值的元素**列表中的位置。选择希望添加的元素出现在其下方的元素。如果不选择元素，添加的元素会出现在列表的末尾。
3. 点击**选择**。

要更改赋值端口的顺序，请选择列表中的一个元素或多个连续元素，然后点击**上移**或**下移**。当您更改元素顺序时，端口会保持连接。

要删除赋值端口，请在列表中选择对应的元素，然后点击**删除**。

如果列表中的某个元素不在输入总线中，则该元素名称以三个问号 (`???`) 开头。请修改输入总线以包含指定名称的元素，或从列表中删除该元素。

##### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `AssignedSignals` |
| **值:** | `'signal1'` (默认) | comma-separated list of element names in quotes |
| **数据类型:** | `char` | `string` |

**示例:** `set_param(gcb,'AssignedSignals','sine,chirp')`

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

实际数据类型或功能支持取决于模块实现。

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

**数据类型支持**

此模块支持使用以下数据类型进行 HDL 代码生成：

| 输入端口 | 维度 | 定点 | 浮点 | 内置整数 | 布尔 | 复信号 |
| --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | 标量  向量  矩阵 | 是 | 半精度  单精度  双精度 | 是 | 是 | 是 |

**HDL 建模规范**

有关最佳做法，请参阅：

- Use Buses to Improve Readability of Model and Generate HDL Code (HDL Coder)

**限制和注意事项**

要了解有关使用总线进行 HDL 代码生成的更多信息，请参阅Buses (HDL Coder)。

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

#### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

实际数据类型或功能支持取决于模块实现。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Signal Routing HDL Coder / Signal Routing

## Description

The Bus Assignment block assigns new values to selected bus elements. Use a
Bus Assignment block to change element values without extracting
elements and reassembling the bus with the desired elements. A Bus
Assignment block simplifies updating a bus to reflect the processing that
occurs in a separate component, such as a subsystem or referenced model.

The Bus Assignment block assigns elements connected to the assignment ports
to specified elements of the bus connected to the bus input port. The block replaces the
elements previously assigned to those elements. The change does not affect the
composition of the bus. The change affects only the values of the elements. Elements not
replaced are unaffected by the replacement of other elements.

The elements to which you assign values can be nonbus signals or buses, including arrays of
buses, as long as they are elements of the input bus. The new values must match the attributes
of the elements in the original bus.

By default, the software repairs broken selections for a Bus Assignment block
that are due to upstream bus hierarchy changes. A warning notifies you when a repair modifies
the model. To prevent the software from making these repairs automatically, set the
**Repair bus selections** configuration
parameter to `Error without repair`.

## Ports

### Input

### **Bus** — Input bus with elements to reassign bus

The input virtual or nonvirtual bus can have elements with real or complex values of any
data type supported by the software, including bus objects, fixed-point
data types, and enumerated data types. The bus can also contain arrays
of buses.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
**Complex Number Support:** Yes

### **:=** — New value to assign to bus element scalar | vector | matrix | array | bus

Each element in the **Elements that are
being assigned** list receives an assignment port. The port label
indicates the bus element that corresponds to the port. For an element named
`signal1`, the port label is **:=
signal1**.

The bus or nonbus signal connected to an assignment port must have the same structure,
data type, and sample time as the corresponding element. To change the
sample time of one or more elements, use a Rate
Transition block. For more information, see Modify Sample Times for Nonvirtual Buses.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
**Complex Number Support:** Yes
### Output

### **Bus** — Output bus bus

The output virtual or nonvirtual bus includes the assigned bus element values for the
selected elements and the unmodified bus element values for the other elements.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
**Complex Number Support:** Yes

## Parameters

To edit Bus Assignment block parameters interactively, double-click the
block.

### **Elements in the bus** — Elements of input bus Read-only: list of element names

This parameter is read-only.

Select elements in the input bus to operate on them.

An arrow next to an element name indicates that an element is a nested bus. To
display the elements in a nested bus, click the arrow.

With one or more elements selected, click:

- **Find** — Find the source of the selected elements. The
  software opens and highlights the system containing the element source.
- **Select** — Add the selected elements to the list of
  elements to be assigned values. For more information, see **Elements that
  are being assigned**.

To filter a long list of input elements, specify a search term in the
**Filter by name** box. Do not enclose the search term
in quotation marks. The filter does a partial string search.

To access filtering options, click Show filtering options to the right of the **Filter by name**
box.

- **Enable regular expression** — Enable the use
  of MATLAB® regular expressions for filtering element names. For
  example, to display all elements whose names end with a lowercase
  `t` and their immediate parents, enter
  `t$` in the **Filter by name**
  box. For more information, see Regular Expressions.
- **Show filtered
  results as a flat list** — Display filtered elements
  in a flat list that uses dot notation to reflect the bus hierarchy.
  By default, the list of input elements displays elements in a
  hierarchical tree.

To refresh the list to reflect modifications to the input bus, click
**Refresh**.

#### Programmatic Use

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `InputSignals` |
| **Values:** | Read-only: list of element names in a cell array or cell array of cell arrays |

**Example:** `get_param(gcb,'InputSignals')`

### **Elements that are being assigned** — Bus elements to be assigned new values list of element names

For each element in this list, the block has an assignment port. The port label contains
the name of the corresponding element.

To add assignment ports for elements:

1. Select one or more elements from the **Elements in the bus**
   list.

   If you select multiple elements from the **Elements in the bus**
   list, the order in which you select them sets their order in the
   **Elements that are being assigned** list.
2. Optionally, specify where you want the elements to appear in the
   **Elements that are being assigned** list. Select the element
   below which you want the added elements to appear. If you do not select an
   element, added elements appear at the end of the list.
3. Click **Select**.

To change the order of the assignment ports, select an element or multiple contiguous
elements in the list, then click **Up** or
**Down**. Port connectivity is maintained when you change the
element order.

To remove assignment ports, select the corresponding elements in the list, then click
**Remove**.

If an element in the list is not in the input bus, the element name starts with three
question marks (`???`). Modify the input bus to include an element of
the specified name, or remove the element from the list.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `AssignedSignals` |
| **Values:** | `'signal1'` (default) | comma-separated list of element names in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param(gcb,'AssignedSignals','sine,chirp')`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual data type or capability support depends on block implementation.

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

**Data Type Support**

This block supports these data types for HDL code generation:

| Input Port | Dimension | Fixed-Point | Floating-Point | Built-in Integers | Boolean | Complex Signal |
| --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | Scalar  Vector  Matrix | Yes | Half  Single  Double | Yes | Yes | Yes |

**HDL Modeling Guidelines**

For best practices, see:

- Use Buses to Improve Readability of Model and Generate HDL Code (HDL Coder)

**Limitations and Considerations**

To learn more about using buses for HDL code generation, see Buses (HDL Coder).

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type or capability support depends on block implementation.

## Version History

**Introduced before R2006a**
