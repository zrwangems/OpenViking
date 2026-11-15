---
type: simulink-block
title: 'Matrix Square'
family: matrix-operations
documentation_release: R2025b
official_category: 'Matrix Operations'
documentation_page: 'matrixsquare'
language: en
---

# Matrix Square

Compute square of input matrix

## Libraries

Simulink / Matrix Operations

## Description

The Matrix Square block computes the square of an
*M*-by-*N* input matrix, *u*, by
premultiplying with the Hermitian transpose. The equivalent MATLAB® code is:

```
y = u' * u
```

The block treats length-*M*
unoriented vector inputs as an
*M*-by-1 matrix. When the input
is an *M*-by-*N*
matrix, the output of the block is an
*N*-by-*N* matrix.

### Applications

The Matrix Square block can be used in a variety of applications:

- General matrix squares — The Matrix
  Square block computes the output matrix,
  *y*, without explicitly forming
  *u'*. It is therefore more efficient than other methods for computing the matrix square.
- Sum of squares — When the input is a column vector
  (*N*=1), the operation of the block is equivalent to a
  multiply-accumulate (MAC) process, or inner product. The output is the sum
  of the squares of the input, and is always a real scalar.
- Correlation matrix — When the input
  is a row vector (*M*=1), the
  output, *y*, is the symmetric autocorrelation matrix, or outer product.

## Ports

### Input

### **Port\_1** — Input matrix *M*-by-1 matrix | 1-by-*N* matrix | *M*-by-*N* matrix

Input matrix, specified as an *M*-by-1, 1-by-*N*, or
*M*-by-*N* matrix.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `fixed point`
### Output

### **Port\_1** — Output matrix *M*-by-*M* matrix | *N*-by-*N* matrix

Output matrix, returned as an *N*-by-*N* or
*M*-by-*M* matrix.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## Parameters

### **Output minimum** — Minimum output value for range checking `[]` (default) | scalar

Minimum output value for range checking that Simulink® checks. Simulink software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges)
- Automatic scaling of fixed-point data types

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutMin` |
| **Type**: character vector |
| **Values**: `'[ ]'`| scalar |
| **Default**: `'[ ]'` |

### **Output maximum** — Maximum output value for range checking `[]` (default) | scalar

Maximum output value for range checking that Simulink checks. Simulink software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges)
- Automatic scaling of fixed-point data types

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutMax` |
| **Type**: character vector |
| **Values**: `'[ ]'`| scalar |
| **Default**: `'[ ]'` |

### **Output data type** — Output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Inherit via back propagation` | `Inherit: Same as input` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `fixdt(1,16,0)` | `<data type expression>`

Specify the output data type for this block.

You can select one of these options:

- A rule that specifies how to inherit a data type, such as
  `Inherit: Inherit via internal rule`.
  For more information on this rule, see Inherit via Internal Rule (DSP System Toolbox).
- An expression that evaluates to a valid data type, for example,
  `fixdt([],16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the **Output data
type** parameter. For more information, see Specify Data Types Using Data Type Assistant.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Same as input'` | `'Inherit: Inherit via internal rule'`| `'Inherit: Inherit via back propagation'` | `'double'` | `'single'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `fixdt(1,16,0)` | `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |

### **Lock output data type setting against changes by the fixed-point tools** — Output data type locking `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the
**Output data type** you specify on the block mask. For
more information, see Use Lock Output Data Type Setting (Fixed-Point Designer).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `LockScale` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Select the rounding
mode (DSP System Toolbox) for fixed-point operations.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **Default:** `'Floor'` |

### **Saturate on integer overflow** — Behavior when integer overflow occurs `off` (default) | `on`

Select this check box to have overflows saturate to the maximum or minimum
value that the data type can represent. If you clear this check box, the
block wraps all overflows. See Precision and
Range (DSP System Toolbox) for more information.

When you select this check box, saturation applies to every internal
operation on the block, not just the output or result. The code generation
process can generally detect when overflow is not possible. In this case,
the code generator does not produce saturation code.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SaturateOnIntegerOverflow` |
| **Type**: character vector |
| **Value**: `'off'` | `'on'` |
| **Default**: `'off'` |

### **Mode** — Category of data to specify `Inherit` (default) | `Built in` | `Fixed point` | `Expression`

Select how you would like to specify the data type properties of the
**Output** data type. You can choose:

- `Inherit` — Lets you specify a
  rule for inheriting a data type, for example,
  `Inherit: Inherit via internal
  rule`
- `Built in`— Lets you specify a
  built-in data type.
- `Fixed point` — Lets you
  specify the fixed-point attributes of the data type.
- `Expression` — Lets you
  specify an expression that evaluates to a valid data type, for
  example, `fixdt([],16,0)`

#### Dependencies

To enable this parameter, click **>>** at the
**Output data type** parameter.

### **Signedness** — Specify signed or unsigned `Signed` (default) | `Unsigned`

Specify the **Signedness** for the
**Output** data type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Scaling** — Method for scaling fixed-point data `Binary point` (default)

Specify the **Scaling** for the
**Output** data type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Data type override** — Specify data type override mode for this signal `Inherit` | `Off`

Select the data type override mode for this signal.

- `Inherit` — Inherits the data type
  override setting specified for the model.
- `Off` — Ignores the data type
  override setting specified for the model and uses the fixed-point
  data type you specify

For more information, see Specify Data Types Using Data Type Assistant
in the Simulink
documentation.

#### Tips

The ability to turn off data type override for an individual data type
provides greater control over the data types in your model when you
apply data type override. For example, you can use this option to ensure
that data types meet the requirements of downstream blocks regardless of
the data type override setting.

#### Dependencies

To enable this parameter, click the **Show data type
assistant** button, and set **Mode** to
`Built in` or `Fixed
point`.

### **Word length** — Bit size of the word that holds the quantized integer `16` (default) | integer from 0 to 32

Specify the bit size of the word that holds the quantized integer. For
more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Mode** to
`Fixed point`.

### **Fraction length** — Specify fraction length for fixed-point data type `0` (default) | scalar integer

Specify fraction length for fixed-point data type as a positive or
negative integer. For more information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set:

- **Mode** to `Fixed
  point`
- **Scaling** to `Binary
  point`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `half` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2021b: Matrix Square Block Moved to Simulink Matrix Operations Library

The Matrix Square block has been moved from the **DSP System Toolbox** > **Math Functions** > **Matrices and Linear Algebra** > **Matrix Operations** to the **Simulink** > **Matrix Operations**. All existing models continue to work.
