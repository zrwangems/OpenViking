---
type: simulink-block
title: 'Bus Creator'
family: signal-routing
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'buscreator'
---

# Bus Creator

Group input signals, buses, or messages into bus

## Libraries

Simulink / Commonly Used Blocks Simulink / Signal Routing HDL Coder / Signal Routing

## Description

The Bus Creator block combines input signals, buses, or messages into a bus,
which retains the separate identities of the signals, nested buses, and messages. By
default, the Bus Creator block creates a *virtual
bus*, which is analogous to a bundle of wires held together by tie wraps.
Alternatively, the block can create a *nonvirtual bus*, which is
analogous to a structure in C code.

Elements of a bus must have unique names. By default, each element of the bus inherits
the name of the element connected to the Bus Creator block. If duplicate
names are present, the Bus Creator block appends the port number to all
input element names. For elements that do not have names, the Bus Creator
block generates names in the form `signaln`, where `n`
is the port number connected to the element. You can refer to elements by name when you
search for their sources or select elements for connection to other blocks. For element
naming guidelines, see Signal Names and Labels.

To extract elements from the bus by name, use a Bus
Selector block.

To create a bus that contains other buses, connect the other buses to the Bus
Creator block input ports.

**Tip**

For buses at subsystem and model interfaces, use Out
Bus Element blocks instead of a Bus Creator block with an
Outport block. Out Bus Element blocks:

- Reduce line complexity and clutter in a block diagram.
- Allow you to more easily change the interface incrementally.

## Ports

### Input

### **Port\_1** — Input element to include in bus scalar | vector | matrix | array | bus

The input ports accept the elements to include in the bus. The number
of input ports is driven by the **Number of inputs**
parameter.

Each Bus Creator block supports these combinations of input elements:

- Signals only
- Signals and signal buses
- Messages only
- Messages and buses
- Buses only

You can specify variable-size input signals with upper bounds smaller
than the upper bounds of the variable-size signals that the corresponding Bus
Creator block input ports can accept. To configure the upper bounds of
variable-size signals that Bus Creator block input ports accept, use a
`Simulink.BusElement` object. For more information, see `Simulink.BusElement`. Variable-size input signals must have the same
dimensionality as the variable-size signals that the corresponding Bus
Creator block input ports are configured to accept.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Output virtual or nonvirtual bus scalar | bus

The output bus is composed of the input elements.

The **Output as nonvirtual bus** parameter specifies whether
the output bus is a virtual or nonvirtual bus. The software treats a
virtual bus as its constituent elements and a nonvirtual bus as a
scalar.

For more information about the types of buses, see Composite Interface Guidelines.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated` | `bus`
**Complex Number Support:** Yes

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Number of inputs** — Number of block inputs `2` (default) | integer

To create a bus, the number of block inputs must be an integer greater than or equal to
2.

Increasing the number of inputs adds unconnected input ports to the block.
Before you simulate the model, make sure that an input connects to each
input port.

If each input port is already connected, you can add an input port to the Bus
Creator block by connecting another line to it.

A line is dragged near a Bus Creator block with two connected ports and a third port appears.

Interactively adding a port updates the **Number of inputs** parameter
value and adds the new input to the **Inputs** list.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

Specify the number of inputs as an integer greater than or equal to 2.

|  |  |
| --- | --- |
| **Parameter:** | `Inputs` |
| **Values:** | `'2'` (default) | integer in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param(gcb,
Inputs="3")`

### **Inputs** — Block inputs list of element names

The **Inputs** list provides the elements that enter the
block, including the elements of nested buses. An arrow next to an element
indicates that an input is a bus. To display the contents of that bus, click
the arrow.

To reorder the input elements, select one or more top-level elements from
the **Inputs** list. Then, drag the elements to a new
position.

To add or remove input elements, click Add or Remove, respectively. Before you simulate the
model, make sure that each input port is connected.

To refresh the list of input elements, click Refresh. For example, refresh the list of input
elements when:

- You rename an input element while the dialog box is
  open.
- You add, remove, or reorder unnamed input elements. The
  Bus Creator block names these elements
  `signalN`, where
  *N* is the number of the corresponding
  block port. When the corresponding block port changes, the
  autogenerated name changes.

To filter the input elements by name with or without regular expressions,
enter the search term in the **Filter** box. Do not enclose
the search term in quotation marks. Optionally, display the filtered results
as a flat list by clicking Show filtered results as a flat list. The flat list uses dot notation to
reflect the bus hierarchy. By default, the filtered results appear in a
hierarchical tree.

*Before R2025a: To filter with regular expressions,
click Show filtering options. Then, select **Enable regular
expression**.*

To select the source of an element that enters the block, select the
element in the list. Then, click Select source blocks. The Property Inspector
shows the parameters of the selected source block. When you select the
source block of multiple elements, the Property Inspector shows
the parameters of the source block that has focus.

You cannot undo or redo changes to the
**Inputs** list.

#### Tips

- When you set **Output data type** to a
  `Simulink.Bus` object, to display which
  `Simulink.BusElement` object maps to a
  top-level input, pause on the top-level input. A parenthetical
  displays the mapping from the input to the
  `Simulink.BusElement` object, for example,
  `Input1 → BusElementObject1`.
- Regular expressions let you filter based on whether the input
  elements match a pattern. For example, to display all elements
  whose names end with a lowercase `t`, enter
  `t$` in the **Filter**
  box. For more information, see Regular Expressions.

### **Output data type** — Data type of output bus `Inherit: auto` (default) | `Bus: <object name>`

Specify the data type of the output bus.

If you select `Bus: <object name>`, replace
`<object name>` with the name of a `Simulink.Bus` object. The bus object must be accessible when you edit the
model.

#### Tips

- To create a `Simulink.Bus` object using the
  Type Editor, click Open Type Editor.
- To create a `Simulink.Bus` object from the
  output bus, use the `Simulink.Bus.createObject` function.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutDataTypeStr` |
| **Values:** | `"Inherit: auto"` (default) | `"Bus: <object name>"` |

**Example:** `set_param(gcb, OutDataTypeStr="Bus: control")`

### **Element names** — Source of output bus element names `From inputs` (default) | `From output data type`

By default, the Bus Creator block uses the names from the block inputs as
the names of the output bus elements, even when you specify a
`Simulink.Bus` object as the data type.

- `From inputs` — Inherit the names of the
  output bus elements from the block inputs.

  *Before R2025a: Select **Use names
  from inputs instead of from bus object**.*
- `From output data type` — Inherit the
  names of the output bus elements from the specified bus
  object.

  *Before R2025a: Clear **Use names
  from inputs instead of from bus object**.*

Setting **Element names** to `From output data
type`:

- Enforces strong data typing.
- Avoids having to enter an element name multiple times: in the bus
  object and in the model. Entering the name multiple times can create
  accidental element name mismatches.
- Supports the array of buses requirement to have consistent element
  names across array elements.

When you set **Element names** to `From
inputs`, consider setting the **Element name mismatch**
configuration parameter to `error`. This
configuration parameter checks that the input element names match the
corresponding names in the bus object.

#### Dependencies

To enable this parameter, set **Output data type** to a `Simulink.Bus`
object.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `InheritFromInputs` |
| **Values:** | `"on"` (default) | `"off"` |

**Example:** `set_param(gcb,
InheritFromInputs="off")`

This table maps the interactive values to the equivalent programmatic
values of this parameter.

| **Element names** Value | `InheritFromInputs` Value |
| --- | --- |
| `From inputs` (default) | `"on"` (default) |
| `From output data type` | `"off"` |

### **Output as nonvirtual bus** — Option to output nonvirtual bus `off` (default) | `on`

Select this parameter to output a nonvirtual bus.

A nonvirtual bus is analogous to a structure in C code. Select this
parameter to:

- Construct an array of buses.
- Have bus data cross MATLAB Function block or
  Stateflow® chart boundaries.
- Package bus data as structures in generated C code.
- Interface with external code through an S-function.
- Reduce the number of function arguments passed to a
  subcomponent in generated code.

All elements in a nonvirtual bus must have the same sample time, even if the elements of
the associated `Simulink.Bus` object specify inherited sample times for
some elements. Any operation resulting in a nonvirtual bus containing elements with
different sample rates generates an error. To change the sample time of an element or
bus that has a different sample time than the other nonvirtual bus input elements, use a
Rate Transition block. For details, see
Modify Sample Times for Nonvirtual Buses.

#### Dependencies

To enable this parameter, set **Output data
type** to a `Simulink.Bus` object.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `NonVirtualBus` |
| **Values:** | `"off"` (default) | `"on"` |

**Example:** `set_param(gcb, NonVirtualBus="on")`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `no` |
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

| Input Port | Dimension | Fixed-Point | Floating-Point | Built-in Integers | Bus | Boolean | Complex Signal |
| --- | --- | --- | --- | --- | --- | --- | --- |
| **Port\_1** | Scalar  Vector  Matrix (up to 2-D) | Yes | Half  Single  Double | Yes | Yes | Yes | Yes |

**Optimizations**

You can use these HDL Coder optimizations to optimize the speed, area, and
I/Os.

**Area Optimization**

| Optimization | Description |
| --- | --- |
| Resource Sharing (HDL Coder) | *Resource sharing* is an area optimization in which HDL Coder identifies multiple functionally equivalent resources and replaces them with a single resource. |
| Streaming (HDL Coder) | *Streaming* is an area optimization in which HDL Coder transforms a vector data path to a scalar data path (or to several smaller-sized vector data paths). |

**Speed Optimization**

| Optimization | Description |
| --- | --- |
| Distributed Pipelining (HDL Coder) | *Distributed pipelining*, or register retiming, is a speed optimization that moves existing delays in a design to reduce the critical path while preserving functional behavior.  For the Sqrt block, HDL Coder distributes pipeline registers around the blocks instead of within them. |
| Clock-Rate Pipelining (HDL Coder) | *Clock-rate pipelining* is an optimization framework in HDL Coder that allows other speed and area optimizations to introduce latency at the clock rate. |
| Adaptive Pipelining (HDL Coder) | *Adaptive pipelining* optimization creates patterns or combination of blocks with registers that can improve the achievable clock frequency and reduce the area usage on the FPGA boards by inserting pipeline registers to the blocks in your design. |
| Critical Path Estimation (HDL Coder) | To quickly identify the most likely critical path in your design, use *Critical Path Estimation*. Critical path estimation speeds up the iterative process of finding the critical path. To know blocks that are characterized in critical path estimation, see Characterized Blocks (HDL Coder). |

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

### R2025a: Specify parameter values more easily and intuitively

The Bus Creator block now provides more intuitive and streamlined editing
for block parameter values.

You can now specify Bus Creator block parameter values in the Property
Inspector. You can continue to use the Block Parameters dialog
box.

This table describes the parameter and interaction changes.

| Goal | Action Before R2025a | Action Since R2025a |
| --- | --- | --- |
| Apply changes. | Make your changes. Then, click **Apply** or **OK**. | Make your changes.  When you specify block parameter values in the Property Inspector or Block Parameters dialog box, the changes apply immediately. |
| Filter with regular expressions. | Click Show filtering options, and select **Enable regular expression**. Then, enter a search term in the **Filter by name** box. | Enter a search term in the **Filter** box. |
| Show filtered results as a flat list. | Click **Show filtered results as a flat list**. | Click Show filtered results as a flat list. |
| Find source blocks. | Select one or more inputs. Then, click **Find**.  The software highlights the source blocks. | Select one or more inputs. Then, click Select source blocks.  The software selects the source blocks, and the Property Inspector displays the parameters of the block that has focus. |
| Add block input. | Click **Add**. | Click Add. |
| Refresh the list of inputs. | Click **Refresh**. | Click Refresh. |
| Remove block input. | Click **Remove**. | Click Remove. |
| Reorder inputs. | Select one or more adjacent inputs. Then, click **Up** or **Down** until the inputs are in the desired position. | Select one or more inputs. Then, drag the inputs to the desired position. |
| Open the Type Editor to define a `Simulink.Bus` object. | Click Show data type assistant, and set **Mode** to `Bus object`. Then, click the **Edit** button. | Click Open Type Editor. |
| Specify the source of the output bus element names. | Select or clear the **Use names from inputs instead of from bus object** check box. | Set **Element names** to `From inputs` or `From output data type`. |
| Rename inputs. | Edit the signal labels of the input elements.  Alternatively, select **Require names of inputs to match names above**, select an element, and specify a new name in the **Rename selected signal** box. | Edit the signal labels of the input elements. |

### R2025a: **Require names of inputs to match names above** and **Rename selected signal** have been removed

The **Require names of inputs to match names above** and
**Rename selected signal** parameters have been removed. To
specify the required names, use a `Simulink.Bus` object
instead.

1. Set **Output
   data type** to a `Simulink.Bus` object.
2. Choose one of these options:

   - To inherit the output bus element names from the specified
     `Simulink.Bus` object, set **Element
     names** to `From output data
     type`.
   - To require the input names to match the names from the
     specified `Simulink.Bus` object, set
     **Element names** to `From
     inputs` and set the **Element name
     mismatch** configuration parameter to
     `error`. This configuration
     parameter checks that the input names match the corresponding
     names in the `Simulink.Bus` object.

Setting `Inputs` to a comma-separated list of element names is not
recommended.

For more information, see **Element
names** and **Element name mismatch**.

### R2023a: Variable-size input signal upper bound can be smaller than upper bound of variable-size signal that the corresponding Bus Creator block input port can accept

Starting in R2023a, the Bus Creator  block supports variable-size
input signals with upper bounds smaller than upper bounds of variable-size signals
that the corresponding Bus Creator block input ports can
accept.

This enhancement allows you to use variable-size input signals when the upper
bounds of input signals are not equal to the upper bounds of variable-size signals
that the corresponding Bus Creator block input ports can
accept.
