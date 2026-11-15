---
type: simulink-block
title: 'Function Element Call'
family: ports-and-subsystems
documentation_release: R2025b
official_category: 'Ports and Subsystems'
documentation_page: 'functionelementcall'
language: en
---

# Function Element Call

Specify function call to be issued via invoking function port

## Libraries

Simulink / Ports & Subsystems

## Description

The Function Element Call block allows a Function Caller block
in a referenced model to call a Simulink® function in another referenced model. The Function Element
Call block, when placed at the root level of a model referenced by a
Model block, creates an invoking function port in the
Model block. When the invoking function port is connected to an
exporting function port of another Model block, a Function
Caller block in the Model block can issue function calls to
Simulink functions in that other Model block and receive return
values through the respective function ports of the Model blocks.

Simulink canvas showing 2 referenced models with function ports and a line connecting them.

Simulink canvas showing Function Element Call block and Function-Call Subsystem block, with a Function Caller block inside the subsystem.

By using multiple Function Element Call blocks, multiple Function
Caller blocks in a referenced model can issue function calls through a
single invoking function port. All Function Element Call blocks that use
the same port share a dialog box. A model can have more than one invoking function
port.

A Function Element Call block must be placed at the root level of model
designated as an export-function model. See Export-Function Models Overview.
For each Function Element Call block, a Function-Call
Subsystem block should also be placed at the root level of the model, and a
Function Caller block should be placed inside the subsystem,
designating the function to call through the Function Element Call
block.

## Ports

### Output

### **Port\_1** — Selected input from external port function

Select a function from the corresponding external input port of the
parent model.

## Parameters

To edit the element associated with a
Function Element Call
block, in the Simulink Editor, edit the block label.

To edit port attributes, use the Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Block Label

### **Port name** — Name of invoking function port `client` (default) | port name

Specify a port name that is not already in use by another block or
port within the model. The name appears as a port label on the parent
Model block. The name also appears next to the block.
Multiple blocks can access the same port.

Use the same port name to qualify, with dot notation, the function name in the
**Function prototype** parameter of the
Function Caller block issuing function calls through
the
port.

```
[OutArg1,OutArg2,...] = PortName.FunctionElementName(InArg1,InArg2,...)
```

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PortName` |
| **Values:** | `'client'` (default) | port name in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Function Element Call",
PortName="clientPort")`

### **Element** — Optional function element specification `f1` (default) | element path

To specify the element that the block selects, in the Simulink Editor, edit the second text field of the block
label.

Multiple blocks can access the same element.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Element` |
| **Values:** | `'f1'` (default) | element path in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Function Element Call",
Element="f3")`

### Port Tab

To toggle whether the tabs are visible, click Show attributes or Hide attributes.

For information about the port name, see **Port
name**.

### **Port number** — Position of port on parent block `1` (default) | real integer

Specify the order in which the port that corresponds to the block
appears on the parent Model block.

- If you add a block that creates another port, the port
  number is the next available number.
- Deleting all blocks associated with a port deletes the
  port. The software renumbers other ports to be sequential
  and does not skip any numbers.
- Specifying a port number that exceeds the number of ports
  creates a port for that number and for any skipped
  sequential numbers.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Port` |
| **Values:** | `'1'` (default) | real integer in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Function Element Call",
Port="5")`

### Signal Tab

To toggle whether the tabs are visible, click Show attributes or Hide attributes.

When you specify the port data type, a parenthetical appears next to the port
name. To display the specified data type in full, click the attribute
summary.

*Before R2025a: To specify the port data type, pause on the port
name in the tree. Then, click Specify attributes. Alternatively, when available, click the
attribute summary.*

### **Data type** — Port data type `Inherit: auto` (default) | `Bus: <object name>` | `ValueType: <object name>`

The port data type can be inherited or specified.

- `Inherit: auto` — Inherited data
  type.
- `Bus: <object name>` — Use the
  name of the `Simulink.ServiceBus` object preceded
  by `Bus:`. For example, specify
  `Bus: myServiceInterface`.
- `ValueType: <object name>`  — Use
  the name of the `Simulink.ValueType` object
  preceded by `ValueType:`. For example, specify
  `ValueType: windVelocity`. The data
  type of the `Simulink.ValueType` object must be a
  `Simulink.ServiceBus` object.

#### Tips

- To edit a `Simulink.ServiceBus` or
  `Simulink.ValueType` object, click Open Type Editor.
- To create a `Simulink.ServiceBus` or
  `Simulink.ValueType` object, use the
  Architectural Data Editor or Interface Editor (System Composer).

#### Programmatic Use

To programmatically set the port data type, use the `set_param`
function. Specify the port as the model name, a forward slash,
and the port name.

|  |  |
| --- | --- |
| **Parameter:** | `OutDataTypeStr` |
| **Values:** | `"Inherit: auto"` (default) | `"Bus: <object name>"` | `"ValueType: <object name>"` |

**Example:** `set_param("mymodel/client",
OutDataTypeStr="Bus:
ServiceInterface")`

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

## Version History

**Introduced in R2022a**

### R2025a: Specify port attributes more easily

You can now specify port attributes more easily.

- To toggle the display of port attributes, click Show attributes or Hide attributes. Port attributes now appear on the
  **Port** and **Signal**
  tabs. The Show attributes or Hide attributes button replaces the button that appears
  when you pause on the port name in a previous release.
- To edit the port name, double-click the name of the port. Alternatively,
  on the **Port** tab, specify **Port
  name**.
- To change block colors, click Set color of blocks associated with selected elements and select a standard color or specify a
  custom color.
- To create a `Simulink.Bus` object using the Type
  Editor, on the **Signal** tab, click Open Type Editor.

### R2024a: Select new options when dragging block to new location

When you press **Ctrl** and drag a Function Element
Call block to a new location, you receive clearer options:

- **New Port** — Create a
  port.
- **New Element** — Add an element to the
  port.
- **Duplicate** — Create a duplicate Function
  Element Call block.

In previous releases, you receive two options:

- **Create New Port** — Create a port.
- **Use Existing Port** — Create a duplicate
  Function Element Call block.

### R2024a: Adding or copying block creates a port

These actions now consistently create a port:

- Double-click the canvas. Then, start typing `Function Element
  Call`, and select the block from the menu.
- Copy and paste a Function Element Call block.

In previous releases, these actions create a port, add an element to a port, or
duplicate a block.
