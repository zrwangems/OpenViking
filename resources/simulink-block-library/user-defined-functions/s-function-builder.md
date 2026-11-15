---
type: simulink-block
title: 'S-Function Builder'
family: user-defined-functions
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'sfunctionbuilder'
---

# S-Function Builder

Integrate C or C++ code to create S-functions

## Libraries

Simulink / User-Defined Functions

## Description

The S-function Builder block integrates new or existing C or C++ code
and creates a C MEX S-function (system-function) from specifications you provide. A C
MEX S-function is a computer language description of a Simulink® block written in C or C++. S-functions use a special calling syntax called
the S-function API that enables you to interact with the Simulink engine. This interaction is very similar to the interaction that takes
place between the engine and built-in Simulink blocks. To learn more about C MEX S-functions, see What Is an S-Function?.
To learn more about building C MEX S-Functions using the S-function
Builder block, see Build S-Functions Automatically Using S-Function Builder. For an example with a step-by-step procedure,
see Use a Bus with S-Function Builder to Create an S-Function.

Instances of the S-Function Builder block also serve as wrappers for
generated S-functions in Simulink models. When simulating a model that contains instances of an
S-Function Builder block, Simulink invokes the generated C MEX S-function to call your C or C++ code in the
instances of `mdlStart`, `mdlOutputs`,
`mdlDerivatives`, `mdlUpdate` and
`mdlTerminate` methods. To learn how Simulink engine interacts with S-functions, see Simulink Engine Interaction with C S-Functions.

**Note**

The S-Function Builder block does not support masking. However, you
can mask a Subsystem block that contains an
S-Function Builder block. For more information, see Create Library Blocks Using Self-Modifiable Masks and Variant Blocks.

## Ports

### Input

### **Port\_1** — S-function input scalar | vector | matrix

The S-Function Builder block can accept real and
complex, 1-D, or 2-D signals and nonvirtual buses. For each of these
cases, the signals must have a data type that Simulink supports.

For more information, see Data Types Supported by Simulink in the Simulink documentation.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`
### Output

### **Out** — S-function output scalar | vector | matrix

The S-Function Builder can produce real and complex,
1-D, or 2-D signals and nonvirtual buses. For each of these cases, the
signals must have a data type that Simulink supports.

For more information, see Data Types Supported by Simulink in the Simulink documentation.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

## Parameters

Use the S-Function Builder editor to create user-defined parameters.
For more information on creating user-defined parameters from the editor, see Specify Ports and Parameters for the S-Function.

**Note**

You do not need to set these listed Simulink block parameters for this block using the block dialog. The
Simulink block parameters are set using the information from the
S-Function Builder editor.

### **S-function name** — Name of the S-function `system` (default) | S-function name

Use this parameter to specify the name of your S-function.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `FunctionName` |
| **Values:** | `'system'` (default) | S-function name in quotes |

### **S-function parameters** — Additional S-function parameters MATLAB® expressions | comma-separated variables

Specify the additional S-function parameters.

The function parameters can be specified as MATLAB expressions or as variables separated by commas. For
example:

```
A, B, C, D, [eye(2,2);zeros(2,2)]
```

Although individual parameters can be enclosed in brackets, the list of
parameters must not be enclosed in brackets.

#### Programmatic Use

|  |  |
| --- | --- |
| **Parameter:** | `Parameters` |
| **Values:** | `''` (default) | S-function parameters in quotes |

### **S-function modules** — Additional files for code generation `''` (default) | filenames

This parameter applies only if this block represents a C MEX S-function
and you intend to use the Simulink
Coder™ software to generate code from the model containing the block.
If you use it, when you are ready to generate code, you must force the coder
to rebuild the top model as explained in Control Regeneration of Top Model Code (Simulink Coder).

For more information on using this parameter, see Specify Additional Source Files for an S-Function (Simulink Coder).

#### Programmatic Use

|  |  |
| --- | --- |
| **Parameter:** | `SFunctionModules` |
| **Values:** | `''` (default) | filenames in quotes |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

S-functions that call into MATLAB are not supported for code generation.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**
