---
type: simulink-block
title: 'Lookup Table Dynamic'
family: lookup-tables
documentation_release: R2025b
official_category: 'Lookup Tables'
documentation_page: 'lookuptabledynamic'
language: en
---

# Lookup Table Dynamic

## Ports

### Input

### **x** — input vector scalar | vector | 2-D array

The block accepts real-valued or complex-valued inputs.

**Example:** `2:12`

#### Dependencies

The `x` input vector and the
`xdat` breakpoint data must have the same sign,
bias, and fractional slope. Also, the precision and range for
`x` must be greater than or equal to the
precision and range for `xdat`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

### **xdat** — breakpoint data 1-by-n vector of strictly monotonically increasing values

The `xdat` vector is the breakpoint data, which must
be strictly monotonically increasing. The value of the next element in
the vector must be greater than the value of the preceding element after
conversion to a fixed-point data type. Due to quantization,
`xdat` can be strictly monotonic for a
floating-point data type, but not after conversion to a fixed-point data
type.

**Tip**

Breakpoints with even spacing can make Simulink
Coder generated code division-free. For more information,
see `fixpt_evenspace_cleanup` in the Simulink documentation and Identify questionable fixed-point operations (Embedded Coder) in the
Simulink
Coder documentation.

**Example:** `1:10`

#### Dependencies

The `xdat` breakpoint data and the
`x` input vector must have the same sign, bias,
and fractional slope. Also, the precision and range for
`x` must be greater than or equal to the
precision and range for `xdat`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

### **ydat** — table data 1-by-n vector

The `ydat` input is a 1-by-n vector of real-valued or
complex-valued table data, which is an evaluation of the function at the
breakpoint values.

**Example:**
`[0 3 12 27 48 75 108 147 192 243 300]`

#### Dependencies

The `ydat` table data and the
`y` output vector must have the same sign,
bias, and fractional slope.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`
### Output

### **y** — Approximation of `y = f(x)` using dynamic table data 1-by-n vector

The block computes an approximation of a function `y =
f(x)` using the `xdat` and
`ydat` input vectors. The lookup method can use
interpolation, extrapolation, or the original values of the
input.

#### Dependencies

The `ydat` table data and the
`y` output vector must have the same sign,
bias, and fractional slope.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### Main Tab

### **Lookup Method** — Specify the lookup method `Interpolation-Use End Values` (default) | `Interpolation-Extrapolation` | `Use Input Nearest` | `Use Input Below` | `Use Input Above`

The block computes output by applying the **Lookup
Method** you select to the input vectors of breakpoint data
(`xdat`) and table data (`ydat`).
For details, see How the Block Generates Output.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LookUpMeth` |
| **Type:** character vector |
| **Values:** `'Interpolation-Extrapolation' | 'Interpolation-Use End Values' | 'Use Input Nearest' | 'Use Input Below' | 'Use Input Above'` |
| **Default:** `'Interpolation-Use End Values'` |

### Signal Attributes Tab

### **Output data type** — Output data type `double` (default) | `'Inherit: Inherit via back propagation'` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16,0)` | `fixdt(1,16,2^0,0)` | `<data type expression>`

Specify the data type of the output signal
`y`.

The **Data Type Assistant** helps you set data
attributes. To use the **Data Type Assistant**, click the Show data type assistant button. For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

The `ydat` table data and the
`y` output vector must have the same sign,
bias, and fractional slope.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutDataTypeStr` |
| **Type:** character vector |
| **Values:** `'Inherit: Inherit via back propagation' | 'double' | 'single' | 'int8' | 'uint8' | 'int16' | 'uint16' | 'int32' | 'uint32' | 'int64' | 'uint64' | 'boolean' | 'fixdt(1,16,0)' | 'fixdt(1,16,2^0,0)' | <data type expression>` |
| **Default:** `'double'` |

### **Lock output data type setting against changes by the fixed-point tools** — Option to prevent fixed-point tools from overriding Output data type `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the
**Output** data type you specify on the block. For more
information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LockScale` |
| **Values:** | `'off'` (default) | `'on'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations. For more information, see Rounding Modes (Fixed-Point Designer).

Block parameters always round to the nearest representable value. To control the
rounding of a block parameter, enter an expression using a MATLAB® rounding function into the mask field.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RndMeth` |
| **Values:** | `'Floor'` (default) | `'Ceiling'` | `'Convergent'` | `'Nearest'` | `'Round'` | `'Simplest'` | `'Zero'` |

### **Saturate to max or min when overflows occur** — Method of overflow action `off` (default) | `on`

When you select this check box, overflows saturate to the maximum or minimum value
that the data type can represent. Otherwise, overflows wrap.

When you select this check box, saturation applies to every internal operation on the
block, not just the output or result. In general, the code generation process can detect
when overflow is not possible. In this case, the code generator does not produce
saturation code.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DoSatur` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

## Libraries

Simulink / Lookup Tables

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

The Lookup Table Dynamic block does not generate code when the **Lookup
Method** parameter is set to
`Interpolation-Extrapolation`.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

The Simulink
PLC Coder™ software does not support the Simulink
Lookup Table Dynamic block. For your convenience, the
plclib/Simulink/Lookup Tables library contains an implementation of a dynamic table
lookup block using the Prelookup and Interpolation Using
Prelookup blocks.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Approximate a one-dimensional function using dynamic table

### How This Block Differs from Other Lookup Table Blocks

The Lookup Table Dynamic block computes an approximation of a function
`y = f(x)` using `xdat` and
`ydat` vectors. The lookup method can use interpolation,
extrapolation, or the original values of the input.

Using the Lookup Table Dynamic block, you can change the table data without
stopping the simulation. For example, you can incorporate new table data if the
physical system you are simulating changes.

As an alternative to Lookup Table Dynamic block, see n-D Lookup Table.

### Inputs for Breakpoint and Table Data

The `xdat` vector is the breakpoint data, which must be
*strictly monotonically increasing*. The value of the next
element in the vector must be greater than the value of the preceding element after
conversion to a fixed-point data type. Due to quantization, `xdat`
can be strictly monotonic for a floating-point data type, but not after conversion
to a fixed-point data type.

The `ydat` vector is the table data, which is an evaluation of
the function at the breakpoint values.

**Note**

The inputs to `xdat` and `ydat` cannot be
scalar (one-element array) values. If you provide a scalar value to either of
these inputs, you see an error upon simulation. Provide a 1-by-n vector to both
the `xdat` and `ydat` inputs.

### Lookup Table Definition

You define the lookup table by feeding `xdat` and `ydat`
as 1-by-n vectors to the block. To reduce ROM usage in the generated code for this
block, you can use different data types for `xdat` and
`ydat`.

**Tip**

Breakpoints with even spacing can make Simulink®
Coder™ generated code division-free. For more information, see `fixpt_evenspace_cleanup` in
the Simulink documentation and Identify questionable fixed-point operations (Embedded Coder) in the Simulink
Coder documentation.

### How the Block Generates Output

The block uses the input values to generate output using the method you select for
**Lookup Method**:

| Lookup Method | Block Action |
| --- | --- |
| `Interpolation-Extrapolation` | Performs linear interpolation and extrapolation of the inputs.  - If the input matches a breakpoint, the output is the   corresponding element in the table data. - If the input does not match a breakpoint, the block   performs linear interpolation between two elements of   the table to determine the output. If the input falls   outside the range of breakpoint values, the block   extrapolates using the first two or last two   points.  **Note**  If you select this lookup method, Simulink Coder software cannot generate code for this block. |
| `Interpolation-Use End Values` (default) | Performs linear interpolation but does not extrapolate outside the end points of the breakpoint data. Instead, the block uses the end values. |
| `Use Input Nearest` | Finds the element in `xdat` nearest the current input. The corresponding element in `ydat` is the output. |
| `Use Input Below` | Finds the element in `xdat` nearest and below the current input. The corresponding element in `ydat` is the output. If there is no element in `xdat` below the current input, the block finds the nearest element. |
| `Use Input Above` | Finds the element in `xdat` nearest and above the current input. The corresponding element in `ydat` is the output. If there is no element in `xdat` above the current input, the block finds the nearest element. |

**Note**

The `Use Input Nearest`, `Use Input Below`,
and `Use Input Above` methods perform the same action when the
input `x` matches a breakpoint value.

Some continuous solvers subdivide the simulation time span into major and minor time steps.
A minor time step is a subdivision of the major time step. The solver produces a
result at each major time step and uses results at minor time steps to improve the
accuracy of the result at the major time step. For continuous solvers, the output of
the Lookup Table Dynamic block can appear like a stair step because
the signal is fixed in minor time step to avoid incorrect results. For more
information about the effect of solvers on block output, see Compare Solvers in the Simulink documentation.
