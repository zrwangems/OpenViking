---
type: simulink-block
title: 'Python Code'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'pythoncode'
documentation_source_path: 'ref_extras/pythoncode.html'
language: en
---

# Python Code

## Ports

### Input

### **Port\_1** — Input port scalar | vector | matrix

The number of input ports is determined by the number of symbols with
`Input` scope defined in the **Ports and
Parameters** table in the block parameters dialog box. Each input port
label is the same as the name of the `Input` symbol unless
you change it by editing the **Label** field in the
**Symbols** table of the block dialog box.

Python Code does not support array of buses as input.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `bus` | `fixedpoint`
### Output

### **Port\_1** — Output port scalar | vector | matrix

The number of output ports is determined by the number of symbols with
`Output` scope defined in the **Symbols**
table in the block parameters dialog box. Each output port label is the same as the
name of the `Output` symbol unless you change it by editing
the **Label** field in the **Symbols** table of the
block dialog box.

Python Code does not support array of buses as output.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `bus` | `fixedpoint`

## Parameters

### **Port and Parameter Symbols** — Symbols and symbol properties table

Symbols and symbol properties used in the Python code, specified as a table. You
must enter the following attributes of each symbol in the table:

- **Name** — Symbol name in the code.

  Each symbol you specify represents a python object. The
  **Name** field serves as the name given to that Python
  object.
- **Scope** — Scope of the symbol. These scopes are available:

  - `Input` — Input to the block.
  - `Output` — Output to the block.
  - `Parameter` — Block parameter that appears on the block
    parameter mask. The parameter name is defined by the
    **Label** of the symbol.
  - `Persistent` — Persistent block data, which retains its
    value from one time step to the next during simulation. A Python Code block
    configured with persistent variable does not support continuous sample time
    and stepping back of simulation.

    You can share an arbitrary Python object between code sections or time
    steps by defining a symbol with `Persistent` scope and
    using `PythonObject` as the **Type** for
    the symbol.
- **Label** — Label of the symbol. For a symbol
  with `Input` or `Output` scope,
  the label appears as the port name on the block. For a symbol with
  `Parameter` scope, the label appears on the block
  parameter mask. You cannot define a label for
  `Persistent` scope symbols.
- **Type** — Data type of the symbol. Select a data
  type from the drop-down list or specify a custom data type. A
  `PythonObject` type can only be set for symbols with scope as
  `Persistent`.
- **Size** — Size of the symbol data. You can use a
  size expression to define the size of an output or use `-1` to
  inherit size.
- **Port** — Port index of the symbol. For an
  `Input` or `Output` symbol,
  **Port** specifies the port index on the block of
  the port or ports corresponding to the symbol. For a
  `Parameter` symbol, **Port** specifies the order that the symbol appears in the block
  parameter mask.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SymbolSpec` |
| **Type:** `SymbolSpec` object |
| **Value:** `SymbolSpec` object |
| **Default:** Empty array of `Symbol` objects |

### **Sample time** — Sample period `-1` (default) | scalar | vector

Sample period, specified in seconds. See Types of Sample Time
and Specify Sample Time. If the block
defines persistent symbols, you cannot specify a continuous sample time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: string scalar or character vector |
| **Default**: `"-1"` |

### **Output** — Output code no default

Output code that the block executes at each time step during simulation, specified
as a character vector or string scalar. For example, use this parameter to call a
function from external python code, make modifications to the results, and perform
operations to pass the results to other blocks.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputCode` |
| **Type:** character vector or string scalar |
| **Value:** `""` | `Python code` |
| **Default:** `""` |

### **Start** — Initialization code no default

Initialization code that the block executes one time at the start of simulation. For
example,use this parameter to initialize persistent symbols.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `StartCode` |
| **Type:** character vector or string scalar |
| **Value:** `""` | `Python code` |
| **Default:** `""` |

### **Terminate** — Termination code no default

Termination code that the block executes one time at the end of simulation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TerminateCode` |
| **Type:** character vector or string scalar |
| **Value:** `""` | `Python code` |
| **Default:** `""` |

## Libraries

Simulink / User-Defined Functions

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `busa` | `doublea` | `fixedpointa` | `integera` | `singlea` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Actual data type or capability support depends on block implementation. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Generates calls to Python CAPI in order to execute python code. Generated code must be
built along with the python development headers and link to Python interpreter.

## Version History

**Introduced in R2025a**

## Description

Integrate native Python code into a Simulink model

The Python Code block integrates native Python® code into a Simulink® model. Use this block to import external code and customize the integration of
your code by specifying the block interface and writing Python code for block initialization, output, and termination.

The Python Code block supports initializing persistent data. Persistent
data can include a Python class object. Use persistent variables that store Python objects to preserve state values between time steps.

For steps to integrate your Python code using this block, see Integrate Python Code into Simulink Using Python Code Block.

**Note**

You must have a compatible version of Python installed in your system to use this block. This might involve installing the
corresponding Python development headers in Linux and Mac. You must set the
`ExecutionMode` of Python in MATLAB as `InProcess`. For
more information, see Configure Your System to Use Python.

Python Code is not supported for simulation inside a Dataflow Subsystem. It is also not
supported for simulation in rapid accelerator mode when placed within a For Each
Subsystem
