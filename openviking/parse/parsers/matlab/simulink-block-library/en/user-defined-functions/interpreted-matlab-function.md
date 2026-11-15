---
type: simulink-block
title: 'Interpreted MATLAB Function'
family: user-defined-functions
documentation_release: R2025b
official_category: 'User-Defined Functions'
documentation_page: 'interpretedmatlabfunction'
language: en
---

# Interpreted MATLAB Function

## Ports

### Input

### **In** — Input of a Interpreted MATLAB function scalar | vector | matrix

The Interpreted MATLAB Function block accepts one real
or complex input of type `double` and generates real or
complex output of type `double`, depending on the
setting of the **Output signal type** parameter.

**Data Types:** `double`
### Output

### **Out** — Output of a Interpreted MATLAB function scalar | vector | matrix

The Interpreted MATLAB Function block accepts one real
or complex input of type `double` and generates real or
complex output of type `double`, depending on the
setting of the **Output signal type** parameter.

**Data Types:** `double`

## Parameters

### **MATLAB Function** — Specify the function or expression function (default)

Specify the function or expression. If you specify a function only, it is
not necessary to include the input argument in parentheses.

### **Output dimensions** — Specify the dimensions of the block output signal scalar | matrix | vector | inherited

Specify the dimensions of the block output signal, for example,
`2` for a two-element vector. The output dimensions
must match the dimensions of the value returned by the function or
expression in the **MATLAB function** field.

Specify `-1` to inherit the dimensions from the output of
the specified function or expression. To determine the output dimensions,
Simulink runs the function or expression once before simulation starts.

**Note**

If you specify `-1` for this parameter and your
function has persistent variables, then the variables might update
before the simulation starts. If you need to use persistent
variables, consider setting this parameter to a value other than
`-1`.

### **Output signal type** — Specify the block output signal type auto (default) | real | complex

Specify the output signal type of the block as `real`,
`complex`, or `auto`. A value of
`auto` sets the output type to be the same as the type
of the input signal.

### **Collapse 2-D results to 1-D** — Output a 2-D array as a 1-D array off (default) | on

Select this check box to output a 2-D array as a 1-D array containing the
2-D array's elements in column-major order.

### **Sample time** — Specify sample time in the block scalar

**Note**

This parameter is not visible in the block dialog box unless it is explicitly set
to a value other than `-1`. To learn more, see Blocks for Which Sample Time Is Not Recommended.

## Libraries

Simulink / User-Defined Functions

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2011a**

### R2022b: To be removed

The Interpreted MATLAB Function block will be removed in a future
release. Use built-in blocks instead is recommended. Use the MATLAB Function block if MATLAB
code is required for modeling. You can also consider writing the function as a MEX
file S-function and implement it using the S-Function block.

## Description

(To be removed) Apply MATLAB function or expression to input

The Interpreted MATLAB Function block applies the specified MATLAB® function or expression to the input. The output of the function must match
the output dimensions of the block. Use the Interpreted MATLAB Function block only in the
current workspace.

Some valid expressions for this block are:

```
sin
atan2(u(1), u(2))
u(1)^u(2)
```

**Note**

This block is slow because it calls the MATLAB parser during each integration step. Consider using built-in blocks
such as the Math Function block instead. Alternatively, you can write the function
as a MEX file S-function, then access it using the S-Function block.
