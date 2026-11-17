---
type: simulink-block
title: 'Bus Assignment'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'busassignment'
documentation_source_path: '../simulink/slref/busassignment.html'
language: en
---

# Bus Assignment

## Ports
```yaml
ports:
- name: Bus
  summary: Input bus with elements to reassign bus
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | string
- name: :=
  summary: New value to assign to bus element scalar | vector | matrix | array | bus
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | string
- name: Bus
  summary: Output bus bus
  direction: output
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated | bus | string
```

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
```yaml
parameters:
- name: Elements in the bus
  summary: 'Elements of input bus Read-only: list of element names'
  group: ''
  block_parameter: InputSignals
  values: 'Read-only: list of element names in a cell array or cell array of cell arrays'
- name: Elements that are being assigned
  summary: Bus elements to be assigned new values list of element names
  group: ''
  block_parameter: AssignedSignals
  values: '''signal1'' (default) | comma-separated list of element names in quotes'
```

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
## Libraries

Simulink / Signal Routing HDL Coder / Signal Routing

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

## Description

Assign new values to specified bus elements

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
