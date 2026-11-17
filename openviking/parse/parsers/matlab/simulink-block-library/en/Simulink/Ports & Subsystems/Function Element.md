---
type: simulink-block
title: 'Function Element'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Ports & Subsystems'
documentation_page: 'functionelement'
documentation_source_path: 'slref/functionelement.html'
language: en
---

# Function Element

## Ports
```yaml
ports:
- name: Port_1
  summary: Full or partial output for external port function
  direction: input
```

### Input

### **Port\_1** — Full or partial output for external port function

Connect a function to pass to the corresponding external output port
of the parent model.
## Parameters
```yaml
parameters:
- name: Port name
  summary: Name of exporting function port server (default) | port name
  group: Block Label
  block_parameter: PortName
  values: '''server'' (default) | port name in quotes'
- name: Element
  summary: Optional function element specification f1 (default) | element path
  group: Block Label
  block_parameter: Element
  values: '''f1'' (default) | element path in quotes'
- name: Port number
  summary: Position of port on parent block 1 (default) | real integer
  group: Port Tab
  block_parameter: Port
  values: '''1'' (default) | real integer in quotes'
- name: Data type
  summary: 'Port data type Inherit: auto (default) | Bus: <object name> | ValueType: <object name>'
  group: Signal Tab
  block_parameter: OutDataTypeStr
  values: '"Inherit: auto" (default) | "Bus: <object name>" | "ValueType: <object name>"'
```

To edit the element associated with a
Function Element
block, in the Simulink Editor, edit the block label.

To edit port attributes, use the Property Inspector. From the Simulink Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Block Label

### **Port name** — Name of exporting function port `server` (default) | port name

Specify a port name that is not already in use by another port. The
name appears as a port label on the parent Model block.
The name also appears next to the block. Multiple blocks can access the
same port.

Use the same port name in the **Scope to port**
parameter of the Trigger block inside the port-scoped
Simulink Function block to be called through the
port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PortName` |
| **Values:** | `'server'` (default) | port name in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Function Element",
PortName="serverPort")`

### **Element** — Optional function element specification `f1` (default) | element path

To specify the element that the block selects, in the Simulink Editor, edit the second text field of the block
label.

Only one block can access each element.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Element` |
| **Values:** | `'f1'` (default) | element path in quotes |
| **Data Types:** | `char` | `string` |

**Example:** `set_param("mymodel/Function Element",
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

**Example:** `set_param("mymodel/Function Element",
Port="5")`

### Signal Tab

To toggle whether the tabs are visible, click Show attributes or Hide attributes.

When you specify the port data type, a parenthetical appears next to the port name. To
display the specified data type in full, click the attribute summary.

*Before R2025a: To specify the port data type, pause on the
port name in the tree. Then, click Specify attributes. Alternatively, when available, click the
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
## Libraries

Simulink / Ports & Subsystems

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
block to a new location, you receive clearer options:

- **New Port** — Create a
  port.
- **New Element** — When the dragged block represents
  an element of the port and not the full port, add an element to the
  port.

In previous releases, you receive two options:

- **Create New Port** — Create a port.
- **Use Existing Port** — When the dragged block
  represents an element of the port and not the full port, add an element
  to the port. Otherwise, create a port.

### R2024a: Adding or copying block creates a port

These actions now consistently create a port:

- Double-click the canvas. Then, start typing `Function
  Element`, and select the block from the menu.
- Copy and paste a Function Element block.

In previous releases, these actions create a port or add an element to a
port.

## Description

Specify function to be called via exporting function port

The Function Element block allows a Simulink® function in a referenced model to be called by a function caller in
another referenced model. The Function Element block, when placed at the
root level of a model referenced by a Model block, creates an exporting
function port in the Model block. When the exporting function port is
connected to an invoking function port of another Model block, a function
caller in that other Model block can issue function calls and receive
return values through the respective function ports of the Model
blocks.

Simulink canvas showing 2 referenced models with function ports and a line connecting them.

Simulink canvas showing Function Element block and Simulink Function block.

By using multiple Function Element blocks, multiple Simulink functions in a referenced model can be called through a single exporting
function port. All Function Element blocks that use the same port share a
dialog box. A model can have more than one exporting function port.

A Function Element block must be placed at the root level of model
designated as an export-function model. See Export-Function Models Overview.
For each Function Element block, a port-scoped Simulink
Function block should also be placed at the root level of the model,
defining the function to be called through the Function Element
block.
