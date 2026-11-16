---
type: simulink-block
title: 'Parameter Writer'
family: signal-routing
documentation_release: R2025b
official_category: 'Signal Routing'
documentation_page: 'parameterwriter'
language: en
---

# Parameter Writer

Write to block parameter or variable

## Libraries

Simulink / Signal Routing

## Description

The Parameter Writer block changes block parameter values by writing to
one of the following:

- A parameter of a block that is tunable during simulation
- An instance parameter that belongs to a Model block that references a
  model
- A masked subsystem parameter
- A model workspace variable
- A base workspace variable
- A variable created in `Simulink.data.Dictionary`

A block with a parameter that can be written by a Parameter Writer block is
called a *parameter owner block*. For the Parameter
Writer block to find the supported parameters of a parameter owner block,
the supported parameters must be enabled.

Use the Parameter Writer block with the Initialize
Function, Reinitialize Function, and Reset
Function blocks to respond to events. For example, an event could be reading
the value from a hardware sensor and then updating a block parameter based on the sensor
value. For more information about using the Parameter Writer block, see
Initialize and Reset Parameter
Values.

For a Parameter Writer block in a masked subsystem, the
Parameter Writer block and corresponding parameter owner block must
have the same immediate parent masked subsystem.

Otherwise, a Parameter Writer block must be in the same mask as either:

- The block whose parameter is directly written by the Parameter
  Writer block, which could be a built-in block such as a
  Gain block, a Model block, a masked
  subsystem block, or a User-Defined Functions block such as an
  S-Function block
- The block whose parameter is indirectly written through a workspace
  variable

It is recommended to use the Parameter Writer block inside a conditionally
executed subsystem to improve the simulation performance. For more information about
using conditionally executed subsystems, see Conditionally Executed Subsystems and Models.

To write to a base or model workspace variable, a variable created in
`Simulink.data.Dictionary`, mask parameter, or Model
block instance parameter with a Parameter Writer block, the variables and
the parameters must be used by a parameter owner block or C MEX S-function with run-time
tunable parameters.

When a Parameter Writer block writes values with data type other than
`double` (the default data type) to a mask parameter, you must
initialize the mask parameter with a value of the same data type as the value written by
the Parameter Writer block. To initialize the mask parameter,
double-click the block to open the mask dialog box, specify the data type and value of
the mask parameter. Alternatively, to initialize mask parameter programmatically, use
**MaskValues** parameter with `set_param`
function. For more information, see Control Masks Programmatically.

In this example shown, a Parameter Writer block writes a value with data type
`single` to a Gain  block parameter inside a masked
subsystem. The mask parameter is initialized to 1 with data type
`single`.

Mask parameter value setting when Parameter Writer block writes data with datatype other then double to a parameter inside a masked subsystem

When a Parameter Writer block writes to an instance parameter with storage
class set to `Model default`, the code generator uses the
default configuration for **Model parameter arguments** when generating
code for the parameter. See Specify Instance-Specific Parameter Values for Reusable Referenced Model (Simulink Coder).

**Note**

When you create a library block with a Parameter Writer block, you
must also include the corresponding parameter owner block in the library block. In
addition to custom library blocks created using the workflow mentioned in Create Custom Library, Simulink® treats model components created using Subsystem Reference block as a one-block library.

### Identify Parameter Owner Blocks

You can determine whether a block is a supported parameter owner block by the value of
the `IsParamOwnerBlock` block parameter. Use the
`get_param` function with the block name or handle,
`blk`, and the `IsParamOwnerBlock` block
parameter.

```
get_param(blk,'IsParamOwnerBlock')
```

The function returns `'on'` if the block is a supported parameter owner
block and `'off'` otherwise.

A Parameter Writer block and the parameter owner block of the value that
the block writes constitute a set of related blocks. You can select a Parameter
Writer block to highlight the related parameter owner block or vice versa. When a
related block is highlighted, blocks in the current model that contain the related block are
also highlighted. For example, an Initialize Function block is highlighted
when it contains a Parameter Writer block that is related to the selected
block. The blocks that are highlighted in the model canvas are also highlighted in the
miniature map.

To show a related block in an open diagram or new tab, pause on the ellipsis that appears
after selection. Then, select the **Related Blocks** button
 from the action bar. Window focus goes to the
open diagram or new tab that shows the related block.

## Ports

### Input

### **In** — Parameter value scalar | vector

Parameter value written by the block.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **Validate parameter** — Option to validate parameter during normal mode simulation `on` (default) | `off`

*Since R2023a*

Locally enable parameter validation for this block.

When parameter validation is disabled for a Paramer Writer block,
normal mode simulation of the block is faster.

#### Tips

To globally enable or disable parameter validation for Parameter
Writer blocks, use the **Parameter Writer
block validation** configuration parameter.

#### Dependencies

To disable parameter validation for this block, the block must not directly or
indirectly change the value of a Model block instance
parameter. For example, the block must not change the value of variable
or mask parameter that specifies the value of a Model
block instance parameter.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `IsParameterValidationOn` |
| **Values:** | `'on'` (default) | `'off'` |

**Example:** `set_param(gcb,'IsParameterValidationOn','off')`

### **Destination** — Option to write to variables and parameters `Block parameter` (default) | `Model workspace variable` | `Base workspace variable`

*Since R2024a*

Write to block parameters, model workspace variables, base workspace variables, or
variables you create in `Simulink.data.Dictionary`.
Select one of these options:

- `Block parameter` — Write to block
  parameters.
- `Model workspace variable` — Write to
  variables in the model workspace.
- `Base workspace variable` — Write to
  variables in the base workspace or variables you create in
  `Simulink.data.Dictionary`.

**Note**

- The **Destination** parameter replaces
  the **Access model workspace parameter**
  parameter.
- You can switch the active variant during simulation or
  execution of the generated code by using the Parameter Writer block placed inside a
  conditionally executed subsystem or in an Initialize
  Function block, a Reinitialize Function block, a Reset
  Function block. Set the
  **Destination** parameter based on the
  location of your variant control variable and select the
  **Validate parameter**. For more
  information see Variant
  Subsystem.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Destination` |
| **Values:** | `'Block parameter'` (default) | `'Model workspace variable'` | `'Base workspace variable'` |

**Example:** `set_param(gcb, Destination="Block parameter")`

### **Workspace variable name** — Name of the workspace variable no default

Specify the name of the workspace variable whose value this block writes.

**Note**

The **Workspace
variable name** parameter replaces the existing
**Model workspace parameter name**
parameter. *(since R2023b)*

#### Dependencies

To enable this parameter, select the `Model workspace
variable` or `Base workspace
variable` from the **Destination**
parameter options.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `WorkspaceVariableName` |
| **Values:** | `''` (default) | character vector | string scalar |

**Example:** `set_param(gcb,'WorkspaceVariableName','var')`

### **Parameter owner block** — Block path of parameter owner block and name of block parameter no default

Specify the block path of the parameter owner block and the name of the parameter
whose value this block writes.

The **Parameter Owner Selector Tree** provides the writable
parameters in a hierarchical tree list. Expand the nodes on the path to the parameter
owner block. Then, select the parameter under the parameter owner block.

#### Tips

If the name of a parameter owner block contains a slash (`/`),
the slash appears as two slashes (`//`) in the Parameter
Writer block parameters. This notation distinguishes the slash in the block
name itself from slashes that separate names at different levels of the model
hierarchy.

#### Dependencies

To enable this parameter, select the `Block parameter` option
from the **Destination** parameter list.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

First, specify the block path of a parameter owner block using the
`ParameterOwnerBlock`
parameter.

|  |  |
| --- | --- |
| **Parameter:** | `ParameterOwnerBlock` |
| **Values:** | `''` (default) | character vector | string scalar |
| **Data Types:** | `char` | `string` |

**Example:** `set_param(gcb,'ParameterOwnerBlock','mymodel/Gain1')`

Then, specify the programmatic name of a block parameter of the parameter owner
block using the `ParameterName`
parameter.

|  |  |
| --- | --- |
| **Parameter:** | `ParameterName` |
| **Values:** | `''` (default) | character vector | string scalar |

**Example:** `set_param(gcb,'ParameterName','Gain')`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `bus` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

### R2024a: Write to base workspace variable and variables in data dictionary

You can now use this block to write to base workspace variables and variables you create in
a data dictionary in addition to model workspace variables and block parameters. Use
the **Destination** parameter to specify whether you want to
write to a variable or a block parameter. Before R2024a, you could use this block to
write to model workspace variables or block parameters only.

### R2023b: Write to invisible masked subsystem parameters

A Parameter Writer block can write to a masked subsystem parameter that is enabled regardless of whether the mask dialog box displays the parameter.

### R2023a: Disable parameter validation during normal mode simulation

Optionally, disable parameter validation that occurs during normal mode simulation for
Parameter Writer blocks. When parameter validation is disabled for a
Parameter Writer block, normal mode simulation of the block is
faster.

To locally enable or disable parameter validation for a Parameter Writer
block, use the **Validate parameter** block parameter.

To globally enable or disable parameter validation for Parameter Writer
blocks, use the **Parameter Writer block
validation** configuration parameter.
