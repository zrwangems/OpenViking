---
type: simulink-block
title: 'Level-2 MATLAB S-Function'
family: user-defined-functions
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'level2matlabsfunction'
language: en
---

# Level-2 MATLAB S-Function

## Ports

### Input

### **In** — Signal input to a Level-2 MATLAB S-function block scalar | vector | matrix

The Level-2 MATLAB S-Function block accepts inputs of
the types listed in the Block Characteristics table. For more
information, see Data Types Supported by Simulink. You can configure input
port using the `setup` callback
function. Use the `setup` function to specify number of
input ports, dimension of input signals, sample time of each port, and
if ports are direct feedthrough.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Out** — Signal output of a Level-2 MATLAB S-function block scalar | vector | matrix

Signal output of a Level-2 MATLAB S-Function block that
the S-Function returns. You can configure input port using the `setup` callback
function. Use the `setup` function to specify number of
input ports, dimension of input signals and sample time of each
port.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## Parameters

### **S-Function Name** — Specify S-Function name `matlabfile` (default) | S-Function name

Specify the name of a MATLAB
function that defines the behavior of this block. The MATLAB function must follow the Level-2
standard for writing MATLAB
S-functions (see Write Level-2 MATLAB S-Functions for details).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `FunctionName` |
| **Type:** character vector |
| **Values:** `'matlabfile'` | S-Function name |
| **Default:** `'matlabfile'` |

### **Parameters** — Specify values of parameters for this block no default (default)

Specify values of parameters for this block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Parameters` |
| **Type:** character vector |
| **Values:** values of block parameters |
| **Default:** `' '` |

## Libraries

Simulink / User-Defined Functions

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Booleana` | `doublea` | `fixed pointa` | `integera` | `singlea` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a Level-1 MATLAB S-functions support only the double data type. Level-2 MATLAB S-functions support all data types that Simulink supports. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

- If a corresponding TLC file is available, the Level-2 MATLAB
  S-Function block uses the TLC file to generate code, otherwise
  code generation throws an error.
- Real-time code generation does not support S-functions that call
  MATLAB.
- Actual data type or capability support depends on block
  implementation.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

Level-1 MATLAB S-functions support only the `double` data type.
Level-2 MATLAB S-functions support all data types that Simulink
supports.

## Version History

**Introduced in R2010b**

## Description

Use Level-2 MATLAB S-function in model

This block allows you to use a Level-2 MATLAB® S-function (see Write Level-2 MATLAB S-Functions) in a model. To do this, create an
instance of this block in the model. Then enter the name of the Level-2 MATLAB S-function in the **S-function
name** field of the block's parameter dialog box.

**Note**

Use the S-Function block to include a Level-1 MATLAB S-function in a block.

If the Level-2 MATLAB S-function defines any
additional parameters, you can enter them in the **Parameters** field
of the block's parameter dialog box. Enter the parameters as MATLAB expressions that evaluate to their values in the order defined by the
MATLAB S-function. Use commas to separate
each expression.

If a model includes a Level-2 MATLAB S-Function block, and an error
occurs in the S-function, the Level-2 MATLAB S-Function block displays
MATLAB stack trace information for the
error in a dialog box. Click **OK** to close the dialog box.
