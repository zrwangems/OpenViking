---
type: simulink-block
title: 'Bus Selector'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'busselector'
documentation_source_path: '../simulink/slref/busselector.html'
language: en
---

# Bus Selector

## Ports

### Input

### **Port\_1** — Input virtual or nonvirtual bus bus

The input virtual or nonvirtual bus contains the elements to be selected.

For arrays of buses, use a Selector block to select the bus that
you want to use with the Bus Selector block.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Selected elements of input bus scalar | vector | matrix | array | bus

By default, the block outputs each of the selected elements from a separate output port
that is labeled with the corresponding bus element name.

When the **Output as virtual bus**
parameter is selected, the block outputs the selected elements from one port, grouped
in a virtual bus.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
**Complex Number Support:** Yes

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

By default, the Property Inspector uses a vertical layout, with the output
elements under the list of elements in the bus. To view the elements in the bus and the
output elements side by side, click Change layout.

### **Elements in the bus** — Input bus hierarchy Read-only: list of element names

This parameter is read-only.

The list of elements in the bus provides the elements that enter the
block, including nested buses and their elements. An arrow next to an
element indicates that an input element is a bus. To display the contents of
that bus, click the arrow.

To filter the elements in the bus by name with or without regular
expression, enter the search term in the **Filter** box. Do
not enclose the search term in quotation marks. Optionally, display the
filtered results as a flat list by clicking Show filtered results as a flat list. The flat list uses dot notation to
reflect the bus hierarchy. By default, the filtered results appear in a
hierarchical tree.

To select the source of an element that enters the block, select the element in the list.
Then, click Select source blocks. Alternatively, right-click the element.
Then, select **Select source blocks**. The Property
Inspector shows the parameters of the selected source block. When
you select the source block of multiple elements, the Property
Inspector shows the parameters of the source block that has
focus.

To refresh the list of elements that enter the block, click Refresh. For example, click this button when you
change an element name while the dialog box is open.

#### Tips

- A green check mark icon appears next to selected output
  elements.
- When you pause on a selected output element, a parenthetical
  displays how many times the Bus Selector block
  selects that element.
- Regular expressions let you filter based on whether the input
  elements match a pattern. For example, enter
  `t$` in the **Filter** box
  to display all elements whose names end with a lowercase
  `t`. For more informations, see Regular Expressions.

#### Programmatic Use

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `InputSignals` |
| **Values:** | Read-only: cell array of element names |

**Example:** `get_param(gcb,'InputSignals')`

### **Output elements** — Selected output elements list of element names

The list of selected elements provides the elements that exit the block.
The list uses the fully qualified name for each element.

In the Simulink Editor, when **Output as virtual bus** is
cleared, select elements from the input bus by adding ports to the block.

1. Click the output edge of the Bus Selector
   block. Alternatively, when the block receives a bus and all
   output ports connect to other ports, draw a new line close to
   the output edge of the Bus Selector block.
2. Specify an element to select.

In the Property Inspector or Block Parameters dialog box, select elements
from the input bus by adding elements to the **Output
elements** list.

1. In the **Elements in the bus** list, select
   one or more elements that you want to add to the block
   output.

   When you select multiple elements from the **Elements
   in the bus** list, the order in which you select
   them sets their order when you add them to the **Output
   elements** list.
2. Optionally, in the **Output elements** list,
   select the element that you want to add elements below. When you
   select no element, the software adds the elements at the end of
   the list.
3. Click Add to output (vertical layout) or Add to output (horizontal layout), depending on the layout of
   the dialog box. Alternatively, right-click one of the selected
   elements. Then, click **Add to
   output**.

To change the order of the output elements, drag elements in the
**Output elements** list to a different position. Port
connectivity is maintained when you change the element order.

To remove elements from the block output, select the elements to remove from the
**Output elements** list. Then, click Remove. Alternatively, right-click one of the
selected elements. Then, select **Remove**.

If an element in the list is not in the input bus, the element name is
red. Remove the element from the list of selected elements or modify the
input bus to include an element with the specified name. To remove all
output elements that are not in the input bus, right-click an element name
that is red. Then, select **Remove all invalid
elements**.

#### Limitations

To avoid a recursion limit, select fewer than 500 elements per
Bus Selector block.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutputSignals` |
| **Values:** | `'signal1,signal2'` (default) | comma-separated list of element names in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param(gcb,'OutputSignals','constant,sine')`

### **Output as virtual bus** — Option to output selected elements as virtual bus `off` (default) | `on`

By default, the block outputs each of the selected elements from a separate output port
that is labeled with the corresponding bus element name. To output the
selected elements from one port, grouped in a virtual bus, select this
parameter.

To convert the output to a nonvirtual bus, insert a Signal Conversion block after the Bus Selector block. Set the
Signal Conversion block **Output** parameter to
`Nonvirtual bus` and set the **Data type**
to a `Simulink.Bus` object.

When the **Output elements** list includes only one element and you
select this parameter, that element is not wrapped in a bus. For example, if
the element is a bus, the output element is that bus. If the element is not
a bus, the output element is not a bus.

#### Dependencies

To use this parameter, the block output must not include messages.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutputAsBus` |
| **Values:** | `'off'` (default) | `'on'` |

**Example:** `set_param(gcb,'OutputAsBus','on')`

## Libraries

Simulink / Commonly Used Blocks Simulink / Signal Routing HDL Coder / Signal Routing

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

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Data Type Support**

The block supports these data types for HDL code generation:

| Input Port | Dimension | Fixed-Point | Floating-Point | Built-in Integers | Bus | Boolean | Complex Signal |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | Scalar  Vector  Matrix (up to 2-D) | Yes | Half  Single  Double | Yes | Yes | Yes | Yes |

**Optimizations**

The block participates in these HDL optimizations to optimize the speed, and
area.

**Area Optimization**

| Optimization | Description |
| --- | --- |
| Resource Sharing (HDL Coder) | *Resource sharing* is an area optimization in which HDL Coder identifies multiple functionally equivalent resources and replaces them with a single resource. |
| Streaming (HDL Coder) | *Streaming* is an area optimization in which HDL Coder transforms a vector data path to a scalar data path (or to several smaller-sized vector data paths). |

**Speed Optimization**

| Optimization | Description |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *Distributed pipelining*, or register retiming, is a speed optimization that moves existing delays in a design to reduce the critical path while preserving functional behavior. |
| Adaptive Pipelining (HDL Coder) | *Adaptive pipelining* optimization creates patterns or combination of blocks with registers that can improve the achievable clock frequency and reduce the area usage on the FPGA boards by inserting pipeline registers to the blocks in your design. |

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

### R2024b: Specify parameters using Property Inspector

You can now specify Bus Selector block parameters in the Property
Inspector. When you make changes in the Property Inspector
or Block Parameters dialog box, the changes apply immediately. The
**Apply** and **OK** buttons have been
removed.

The Bus Selector block must have at least one output element. To completely
replace the output elements, add elements from the input bus to the block output.
Then, remove the original output elements. For example, for a new Bus
Selector block, add elements from the input bus to the block output.
Then, right-click the placeholder element named `signal1` and
select **Remove all invalid elements**.

When you find the source blocks of input elements, the source blocks are now selected
instead of highlighted. The Property Inspector shows the parameters of
the selected source block. When you select the source block of multiple elements,
the Property Inspector shows the parameters of the source block that
has focus. To reflect this change, the **Highlight source
blocks** option () is now called **Select source
blocks**.

### R2024a: Right-click elements to access options

In the Block Parameters dialog box of a Bus Selector block,
right-click elements and select the desired action.

- **Add to output** — Add elements from the input bus to
  the block output.
- **Highlight source blocks** — Highlight the source
  blocks of elements in the input bus.
- **Remove** — Remove elements from the block
  output.
- **Remove all invalid elements** — Remove all output
  elements that are not in the input bus. The invalid element names are
  red.

To view the available actions for an element, right-click the element. To view the
available actions for multiple selected elements, right-click one of the elements in
the selection. For example, suppose your selection includes only invalid elements.
When you right-click, you receive two options: **Remove** and
**Remove all invalid elements**. If your selection includes a
valid element, you receive one option: **Remove**.

### R2024a: Renamed parameters and more intuitive interactions

When you interact with Bus Selector blocks, the results of your
actions are more clear.

- The Select elements button  is now the Add to output button
  .
- The **Selected elements** list is now the
  **Output elements** list.
- The Output as virtual bus button  is now the **Output as virtual
  bus** check box.

### R2023b: Streamlined dialog box design

The Bus Selector block dialog box has a streamlined design with
additional functionality.

- In the **Elements in the bus** list, a green check mark
  icon appears next to selected output elements.
- In the **Elements in the bus** list, when you pause on a
  selected output element, a parenthetical displays how many times the
  Bus Selector block selects that element.
- Filtering supports regular expressions by default.
- You can toggle between vertical and horizontal layouts.

The previous functionality remains.

By default, the dialog box opens in a vertical layout, with the selected elements
under the list of elements in the bus. To view the elements in the bus and the
selected output elements side by side, click Change layout.

The horizontal layout more closely mimics the previous Bus Selector
block dialog box design.

## Description

Select elements from input bus

The Bus Selector block extracts the elements you select by name from the
input bus hierarchy. The block can output the selected elements separately or in a new virtual
bus. When the block outputs the selected elements separately, each selected element
corresponds to an output port. When the block outputs a new virtual bus, the block has one
output port for the virtual bus that contains each selected element.

While multiple elements can have the same name in different locations in the bus
hierarchy, each element has a unique fully qualified name that the Bus Selector
block uses. For example, the top-level bus and a nested bus can both have an element named
`chirp`. The fully qualified name for the element in the top-level bus is
`chirp`. The fully qualified name for the element in the nested bus is
`nestedbus.chirp`, where `nestedbus` is the name of the
nested bus.

**Tip**

For buses at subsystem and model interfaces, use In
Bus Element blocks instead of an Inport block with a Bus
Selector block. In Bus Element blocks:

- Reduce line complexity and clutter in a block diagram.
- Allow you to more easily change the interface incrementally.
- Allow access to a bus element closer to the point of usage, avoiding the use of a
  Bus Selector and Goto block configuration.
