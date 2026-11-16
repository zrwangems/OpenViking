---
type: simulink-block
title: 'C Caller'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Quick Insert / User-Defined Functions'
documentation_page: 'ccaller'
documentation_source_path: 'slref/ccaller.html'
language: en
---

# C Caller

## Ports

### Input

### **Port\_1** — Input port scalar | vector | matrix

The number of input ports and their names are inferred through the selected
function in your external C code. To provide data to a C Caller block,
connect an input signal to the input ports.

The input label has the same name as your input port unless changed by editing the
**Label** column under **Port
Specification** from the **Block Dialog**. If you
rename the label to an input port, the C Caller block changes the name
of the port.

For input variables, you can change the input scope to parameters or constants
using the **Scope** column.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus` | `string`
### Output

### **Port\_1** — Output port scalar | vector | matrix

The number of output ports and their names are inferred through the selected
function in your external C code. To send data from your C Caller
block, connect a block to the output port of your C Caller
block.

The output port label has the same name as your output port unless you change it
by editing the **Label** column under **Port
Specification** from the **Block Dialog**. If you
rename the label to an input port, the C Caller block changes the name
of the port.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `enumerated` | `bus` | `string`

## Parameters

### **Function name** — Name of function character vector | string scalar

Name of the function parsed for the C Caller block, specified as a
character vector or string scalar. For a list of available functions, see Available Functions.

**Tunable:** Yes

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FunctionName` |
| **Type:** character vector or string scalar |

```
myFunctionName = get_param(gcb,"FunctionName")
```

```
myFunctionName =

    'mean_filter'
```

### **Port specification** — Port properties table

Port properties, specified as a table. The table indicates the attributes of each
input and output element of the block. If the scope is an
`input`, you can modify this variable to a
`parameter` or a `constant`. These
properties include

**Name** — Demonstrates the variable name inferred from
your source code.

A bold argument name indicates that the port or parameter is a global
argument.

**Scope** — Indicates the role of the variables from
your source code. If the variable is an input argument in the C Caller
block source code, you can change the scope type to a constant or a parameter. If the
variable is an output argument in the source code, you cannot change the scope
type.

**Label** — Labels the input or output variable for the
Simulink model. You can change the labels using this table. If the scope is a
parameter, enter the parameter name in this field. If the scope is a constant, enter the
constant value.

**Type** — Indicates the data type coming from the
ports.

**Size** — Indicates the size of the input and output
data.

Name, scope, type, and size are inferred from your source code.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FunctionPortSpecification` |
| **Type:** `FunctionPortSpecification` object |

### **Available Functions** — List of available functions cell array

List of all available functions that can be mapped to a C Caller
block, specified as a cell array.

The C Caller block in your model imports all functions in your
external source code, and shows the function names next to the Function name on the block
dialog. To select and use a function in your block, confirm that the function name
appears in the `Available Functions` table. If you are missing
one of the functions, reload the source code by clicking Refresh custom code button. on the block dialog. To change the names of functions,
modify your source code and click the **Refresh** button to reload.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AvailableFunctions` |
| **Type:** cell array |

```
allAvailableFunctions = get_param(gcb, "AvailableFunctions")
```

```
allAvailableFunctions =

  1×1 cell array

    {'add'}
```

### **Sample time** — Sample period `-1` (default) | scalar | vector

Sample period, specified in seconds. See Types of Sample Time
and Specify Sample Time.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: string scalar or character vector |
| **Default**: `"-1"` |

## Libraries

Simulink / User-Defined Functions

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `busa` | `doublea` | `enumerateda` | `fixed pointa` | `integera` | `singlea` | `stringa` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yesa` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Actual data type or capability support depends on block implementation. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Actual data type or capability support depends on block implementation.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2018b**

### R2024b: Enhancements related to block and function interface

- The block now accepts Simulink strings at its ports when the block calls a C
  function that uses character pointer (`char*`) or character array
  (`char[]`) as input or output data types.
- You can now use command line APIs to manually add global variables from custom code
  to the block as global arguments or delete existing global arguments from the block.
  This enhancement enables you to more directly control the behavior of global variables
  in the custom code called by the block.

## Description

Integrate C code in Simulink

The C Caller block integrates your external C code into Simulink®. This block imports and lists the functions in your external C code, and enables
you to select your resolved C functions to integrate in your Simulink models. The C Caller block standalone supports code generation.
For more complex models, code generation depends on the capabilities of your Simulink model.

To use the C Caller block, define your source code and any supporting files
using **Simulation Target** under **Configuration
Parameters**. Then, bring a C Caller block to the Simulink canvas, using **Library Browser** > **Simulink** > **User Defined Functions**. To change the defined source code file and its dependencies, go to
**Simulation Target** tab in **Configuration
Parameters** by clicking the Configure custom code settings button. from the block dialog. After changing your source code or any
of its dependencies, refresh the list of functions by clicking the Refresh custom code button. on the block dialog. To browse the function definitions in
your source code, use the Go to function button. icon to access your source files.

You can use the `addGlobalArg`
function to add global variables from custom code as global arguments to the block, or use the
`deleteGlobalArg`
function to delete global arguments from the block. *(since R2024b)*
