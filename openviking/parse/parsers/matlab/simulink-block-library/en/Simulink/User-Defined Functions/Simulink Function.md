---
type: simulink-block
title: 'Simulink Function'
family: 'simevents'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: ''
documentation_page: 'simulinkfunction'
documentation_source_path: 'slref/simulinkfunction.html'
language: en
---

# Simulink Function

## Ports

### Input

### **In** — Signal input to a subsystem block scalar | vector | matrix

Placing an Inport block in a subsystem block adds an
external input port to the block. The port label matches the name of the
Inport block.

Use Inport blocks to receive signals from the local
environment.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image` | `struct`

### **ArgIn** — Argument input to a subsystem block scalar | vector | matrix

An Argument Inport block in a subsystem block provides
an input port corresponding to an input argument. A port is not
displayed on the subsystem block.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image` | `struct`
### Output

### **Out** — Signal output from a subsystem scalar | vector | matrix

Placing an Outport block in a subsystem block adds an
output port from the block. The port label on the subsystem block is the
name of the Outport block.

Use Outport blocks to send signals to the local
environment.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image` | `struct`

### **ArgOut** — Argument output from a subsystem block scalar | vector | matrix

An Argument Outport block in a subsystem block provides
an output port corresponding to an output argument. A port is not
displayed on the subsystem block.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `image` | `struct`

## Parameters

### Main

### **Show port labels** — Display options for port labels `FromPortIcon` (default) | `FromPortBlockName` | `SignalName` | `none`

Select how to display port labels on the Subsystem block icon.

- `none` — Do not display port labels.
- `FromPortIcon` — If the corresponding port icon displays a signal name, display the signal name on the Subsystem block. Otherwise, display the port block name or the port number if the block name is a default name.
- `FromPortBlockName` — Display the name of the corresponding port block on the Subsystem block.
- `SignalName` — If the signal connected to the port is named, display the name of the signal on the Subsystem block. Otherwise, display the name of the corresponding port block.

For port label editing on Subsystem blocks, see Edit Port Labels on Subsystem Blocks.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ShowPortLabels` |
| **Values:** | `'FromPortIcon'` (default) | `'FromPortBlockName'` | `'SignalName'` | `'none'` |

### **Read/Write permissions** — Levels of access to contents of subsystem `ReadWrite` (default) | `ReadOnly` | `NoReadOrWrite`

Control user access to the contents of the subsystem.

- `ReadWrite` — Enable opening and modification of subsystem contents.
- `ReadOnly` — Enable opening but not modification of the subsystem. If the subsystem resides in a block library, you can create and open links to the subsystem and can make and modify local copies of the subsystem but cannot change the permissions or modify the contents of the original library instance.
- `NoReadOrWrite` — Disable opening or modification of subsystem. If the subsystem resides in a library, you can create links to the subsystem in a model but cannot open, modify, change permissions, or create local copies of the subsystem.

You do not receive a response if you attempt to view the contents of a subsystem whose **Read/Write permissions** parameter is set to `NoReadOrWrite`. For example, when double-clicking such a subsystem, the software does not open the subsystem and does not display any messages.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Permissions` |
| **Values:** | `'ReadWrite'` (default) | `'ReadOnly'` | `'NoReadOrWrite'` |

### **Name of error callback function** — Name of function to be called if error occurs no default

Enter the name of a function to be called if an error occurs while the software executes the
subsystem.

The software passes two arguments to the function: the handle of the subsystem and a
character vector that specifies the error type. If no function is specified, the software
displays a generic error message if executing the subsystem causes an error.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ErrorFcn` |
| **Values:** | `''` (default) | function name in quotes |
| **Data Types:** | `char` | `string` |

### **Permit hierarchical resolution** — Resolution for workspace variable names `All` (default) | `ExplicitOnly` | `None`

Select whether to resolve names of workspace variables referenced by this subsystem.

For more information, see Symbol Resolution and Symbol Resolution Process.

- `All` — Resolve all names of workspace variables used by this subsystem, including those used to specify block parameter values and Simulink data objects (for example, `Simulink.Signal` objects).
- `ExplicitOnly` — Resolve only names of workspace variables used to specify block parameter values, data store memory (where no block exists), signals, and states marked as “must resolve”.
- `None` — Do not resolve any workspace variable names.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PermitHierarchicalResolution` |
| **Values:** | `'All'` (default) | `'ExplicitOnly'` | `'None'` |

**Note**

To configure the scope visibility and synchronicity of a Simulink
Function block, open the block parameters of the Trigger block located inside of
the Simulink Function block.

## Libraries

Simulink / User-Defined Functions

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `halfa` | `imagea` | `integera` | `singlea` | `stringa` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yesa` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Actual data type or capability support depends on block implementation. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual code generation support depends on block implementation.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Actual data type support depends on block implementation.

## Version History

**Introduced in R2014b**

### R2024a: Define variant control variables of a Simulink Function block in the mask or model workspace

Starting in R2024a, you can define the variant control variables of a
Simulink Function block with update diagram activation time in
the mask or model workspace.

### R2023b: Support nonunique function names when scoped to different ports

If scoped to different ports, function names of Simulink functions at the model
root level do not have to be unique.

### R2022b: Highlight related Function Caller blocks in referenced model

Starting in R2022b, when you select a Simulink Function block whose
related Function Caller block is in a referenced model, both the
Function Caller block and the Model block of the
referenced model are highlighted.

### R2022b: Specify asynchronous function execution

Starting in R2022b, you can specify a Simulink function to be executed asynchronously by selecting the new
**Execute function call asynchronously** parameter in the
Trigger block inside of the Simulink Function
block and in the Function Caller block.

### R2022a: Port-scoped Simulink Function blocks

A new port-scoped visibility option for the Simulink Function block
is added for R2022a. To create a port-scoped Simulink Function block,
set the **Function visibility** parameter of the Trigger block inside the
Simulink Function block to `port` and
enter the port name in the **Scope to port** field. Use
port-scoped Simulink Function blocks to implement functions called
through exporting function ports created by Function Element blocks.
See Model Client and Server Components Using Function Ports.

## Description

Define a function using Simulink blocks

A Simulink Function block is a Subsystem block preconfigured to enable implementation of a function using
Simulink® blocks. To define and call a function using a Simulink
Function block:

- Specify the function prototype, which includes the function name and input
  and output arguments, for example, `y = f(u)`.
- Implement function behavior using blocks from the Simulink library.
- Configure your Simulink Function block to be called and
  reused anywhere in the model hierarchy.

Simulink Function block with view of inside the subsystem.

When a function is called, the caller sends data through input arguments to the
function, executes the function based on the implemented behavior, and then receives
data back from the function through output arguments.

For more information, see Simulink Functions Overview.

### Specify Function Prototype

The function prototype is separate from the implementation of the function. It
specifies the input and output arguments and how the function should be called from
other blocks in the model hierarchy. Each input or output argument specified in the
function prototype is represented by an Argument Inport block or Argument Outport block,
respectively. You can edit the function prototype by double-clicking the text
displayed on the block.

### Implement Function Behavior

To implement the desired behavior of your function, add any necessary Simulink blocks inside the subsystem. In addition to Argument
Inport and Argument Outport blocks, a Simulink
Function block can use Inport and Outport blocks to input and output data.

For an example, see Monitor Ink Status on Shared Printer Using Simulink Functions.

### Configure Simulink Function Block

To configure a Simulink Function block, open the block parameters
of the Trigger block located inside of the
Simulink Function block.

- **Function name** –
  Specify the function name for the Simulink Function
  block.
- **Function visibility** – Select the scope visibility of
  the function.

  If **Function visibility** is set to
  `port`, you can also specify these
  parameters:

  - **Execute function call asynchronously** – Specify
    whether the function executes synchronously or
    asynchronously.
  - **Scope to port** – Specify the name of the
    exporting function port.

### Call a Simulink Function

You can use a function caller and the function prototype to call and execute your
function. A function defined in a Simulink Function block can be
called from a Function
Caller block, a Chart (Stateflow), a MATLAB Function block, a MATLAB System block, or an S-Function block.

For more information, see Call a Simulink Function from a Model.

### Model Considerations

When using a Simulink Function block, consider whether your model
requires persistence of states between functions calls or a continuous sample
time.

- Persistence of state between function calls – If a Simulink
  Function block contains any blocks with state (for example,
  Unit Delay or Memory blocks), then their
  state values are persistent between calls to the function. If there are
  multiple calls to that function, the state values are also persistent
  between the calls originating from different callers.
- Unable to inherit continuous sample time – A Simulink
  Function block cannot inherit a continuous sample time.

### Code Generation with Simulink Function Blocks

If you have Simulink
Coder™ or Embedded Coder®, you can generate code from models containing Simulink functions. For more information, see Simulink Function Blocks and Code Generation (Embedded Coder) and Configure Entry-Point Function Interfaces for Simulink Function and Function Caller Blocks (Embedded Coder).
