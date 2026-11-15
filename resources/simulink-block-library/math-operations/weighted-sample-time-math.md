---
type: simulink-block
title: 'Weighted Sample Time Math'
family: math-operations
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'weightedsampletimemath'
---

# Weighted Sample Time Math

Support calculations involving sample time

## Libraries

Simulink / Math Operations

## Description

The Weighted Sample Time block outputs a weighted sample time, weighted
sample rate, or mathematically adjusted weighted sample time, depending on settings of
the **Operation** and **Weight value** parameters and
the execution context of the function outputs.

You specify the block operation by using the **Operation**
parameter.

The sample time used to derive the output depends on whether the block is used within a
periodic or aperiodic (or triggered) execution context. For a periodic execution context,
the block uses the sample time of the model. For an aperiodic or triggered execution
context, the block uses the sample time of the discrete signal.

Use the **Weight value** parameter to specify the sample time weight
factor. If the weight value, `w`, is `1`, that value does
not appear in the equation on the block icon.

**Tip**

You can use the
Weighted Sample Time and Weighted Sample Time Math
blocks to extract the sample time from a Simulink® signal. Set the **Operation** parameter to
`Ts Only` and the **Weight value**
parameter to `1.0`. With this configuration, the block outputs the
sample time of the input signal.

The block computes its output by using the precedence rules for MATLAB® operators. For example, if the **Operation** parameter is set
to `+`, the block calculates the output by using this expression:

```
u + (Ts * w)
```

If the **Operation** parameter is set to `/`, the block
calculates the output by using this expression:

```
(u / Ts) / w)
```

For more information, see Operator Precedence.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Specify input signal as a scalar, vector, or matrix.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector | matrix

Depending on settings of the
**Operation** and
**Weight value** parameters and
the execution context of the function that
contains the block, the block outputs a weighted
sample time, weighted sample rate, or
mathematically adjusted weighted sample
time.

- Weighted sample time – When used in a periodic function, the weighted sample time
  is the sample time of an input signal times the value specified for the
  **Weight value** parameter (`Ts * w`). When used
  in an aperiodic or triggered function, the weighted sample time is the elapsed time
  since the last execution times the weight value.
- Weighted sample rate – When used in a periodic function, the weighted sample rate
  is the reciprocal of the weighted sample time (`1/(Ts * w)`). The
  weighted sample rate is not relevant when the block is used in an aperiodic
  function.
- Mathematically adjusted weighted sample time – The block adds the value of an
  input signal `u` to, subtracts `u` from, or
  multiplies or divides `u` by a weighted sample time.

The sample time used to derive the output
and the data type of the output depend on whether
the block is used within a periodic or aperiodic
(or triggered) execution context.

| Execution Context of Block | Sample Time Used to Derive Output | Data Type of Output Signal |
| --- | --- | --- |
| Periodic | Sample time of the model | - Sign is the same sign as the value of the   input signal. - Word length is the larger value of the input   signal word length or half of a `long   long`. - Scaling is best precision scaling of the   weighted sample time. |
| Aperiodic or triggered | Elapsed time since the last execution | - Data type is unsigned. - Word length is large enough to account for   the setting of model configuration parameter   **Application lifespan**. - Scaling is best precision scaling of the   setting of model configuration parameter   **Clock resolution**. |

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## Parameters

### Main

### **Operation** — Math operation `+` (default) | `-` | `*` | `/` | `Ts Only` | `1/Ts Only`

Specify the operation to use for adjusting the input signal. For
example, if you specify the `+` operation, the
block adds the weighted sample time to the value of the input signal.
The value `1/Ts Only` is not relevant when you
use the block in an aperiodic function.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TsampMathOp` |
| **Type:** character vector |
| **Values:** `'+' | '-' | '*' | '/' | 'Ts Only' | '1/Ts Only'` |
| **Default:** `'+'` |

### **Weight value** — Weight for sample time `1.0` (default) | real-valued scalar

Enter the weight for the sample time as a real-valued scalar. The block multiplies the
sample time of the input signal by the value that you specify. For example, if you use
the block in a periodic function of a model that has a sample time of
`0.2` and you specify a weight value of `3`, the
weighted sample time is `0.6`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `weightValue` |
| **Type:** character vector |
| **Values:** real-valued scalar |
| **Default:** `1.0` |

### **Implement using** — Method for adjusting sample time `Online Calculations` (default) | `Offline Scaling Adjustment`

Select whether to adjust the sample time by applying online calculations or by applying
offline scaling. This option applies only for fixed-point and integer
operations. The block disregards it for floating-point data types.

| Result of `Ts * w` | Output Data Type of Two Modes | Block Execution |
| --- | --- | --- |
| Power of 2 (positive or negative) or an integer value | The same when **Output data type** is set to `Inherit: Inherit via internal rule` | Equally efficient in both modes |
| Not a power of 2 and not an integer value | Different | More efficient for the offline scaling mode |

**Note**

When the **Implement using** parameter is not enabled, operations
default to online calculations.

#### Dependencies

To enable this parameter, set **Operation** to `*` or `/`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `TsampMathImp` |
| **Type:** character vector |
| **Values:** `'Online Calculations' | 'Offline Scaling Adjustment'` |
| **Default:** `'Online Calculations'` |

### Signal Attributes

### **Output data type** — Data type of output signal `Inherit: Inherit via internal rule` (default) | `Inherit: Inherit via back propagation` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `fixdt(1,16,20,0)` | `<data type expression>`

Specify the data type for the block output signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `OutDataTypeStr` |
| **Type**: character vector |
| **Values**: `'Inherit: Inherit via internal rule'` | `'Inherit: Inherit via back propagation'` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)` | `fixdt(1,16,20,0)` | `'<data type expression>'` |
| **Default**: `'Inherit: Inherit via internal rule'` |

### **Integer rounding mode** — Rounding mode for fixed-point operations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations. For more information, see Rounding Modes (Fixed-Point Designer).

Block parameters round to the nearest representable value. To control the rounding of
a block parameter, enter an expression by using a MATLAB rounding function in the mask field.

#### Dependencies

To enable this parameter, set the **Operation** parameter to
`+`, `-`,
`*`, or `/`. If you set the
**Operation** to `*` or
`/`, you must also set the **Implement
using** parameter to `Online
Calculations`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `RndMeth` |
| **Type:** character vector |
| **Values:** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **Default:** `'Floor'` |

### **Saturate on integer overflow** — Method of overflow action `off` (default) | `on`

Specify whether integer overflows saturate or wrap.

| Goal | Action | Overflow Behavior | Example |
| --- | --- | --- | --- |
| Model has possible overflow conditions and you want explicit saturation protection in the generated code. | Select check box (`on`). | Saturate to the minimum or maximum value that the data type can represent. | The maximum value that the `int8` (signed, 8-bit integer) data type can represent is 127. A block operation result greater than this maximum value causes overflow of the 8-bit integer. When you select this parameter, the block output saturates at 127. Similarly, the block output saturates at a minimum output value of -128. |
| You want to optimize generated code.  You want to avoid overspecifying how a block handles out-of-range signals. For more information, see Troubleshoot Signal Range Errors. | Clear check box (`off`). | Wrap overflows to the appropriate value that is representable by the data type. | The maximum value that the `int8` (signed, 8-bit integer) data type can represent is 127. A block operation result greater than this maximum value causes overflow of the 8-bit integer. When you clear this parameter, the software interprets the overflow-causing value as `int8`, which can produce an unintended result. For example, a block result of 130 (binary 1000 0010) expressed as `int8`, is -126. |

When you select **Saturate on integer overflow**, saturation applies to every
internal operation on the block, not just the output, or result. When the code generator
detects that overflow is not possible, it does not produce saturation code.

#### Dependencies

To enable this parameter, set the **Operation** parameter to
`+`, `-`,
`*`, or `/`. If you set
**Operation** to `*` or
`/`, you must also set the **Implement
using** parameter to `Online
Calculations`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SaturateOnIntegerOverflow` |
| **Type:** character vector |
| **Values:** `'off' | 'on'` |
| **Default:** `'off'` |

### **Mode** — Data type mode `Inherit` (default) | `Built in` | `Fixed point` | `Expression`

Select how you would like to specify the data type properties of the **Output data type**. You can choose:

- `Inherit` — Specify a rule for inheriting a data type, for example, `Inherit: Same as input`.
- `Built in`— Specify a built-in data type, for example, `double`.
- `Fixed point` — Specify the fixed-point attributes of the data type.
- `Expression` — Specify an expression that evaluates to a valid data type, for example, `fixdt(1,16)`.

For more information, see Specify Data Types Using Data Type Assistant.

### **Signedness** — Signedness of fixed-point data `Signed` (default) | `Unsigned`

Specify whether the fixed-point data is signed or unsigned. `Signed` data can represent positive and negative values, but `Unsigned` data represents positive values only. For more information, see Specify Data Types Using Data Type Assistant.

### **Scaling** — Method for scaling fixed-point data `Best precision` (default) | `Binary point`

Specify the method for scaling your fixed-point data to avoid overflow conditions and minimize quantization errors. For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, set **Mode** to `Fixed point`

### **Word length** — Bit size of word that holds quantized integer `16` (default) | integer from 2 to 128

Specify the bit size of the word that holds the quantized integer as a positive integer from 2 to 128. For more information, see Specify Data Types Using Data Type Assistant.

#### Dependencies

To enable this parameter, set **Mode** to `Fixed point`.

### **Fraction length** — Fraction length for fixed-point data type `0` (default) | integer scalar

Specify the fraction length of the fixed-point data type as a positive or negative integer scalar.

#### Dependencies

To enable this parameter, set **Mode** to `Fixed point` and **Scaling** to `Binary point`.

### **Slope** — Specify slope for the fixed-point data type `2^0` (default) | positive, real-valued scalar

Specify slope for the fixed-point data type. For more information, see
Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Slope and bias`.

### **Bias** — Specify bias for the fixed-point data type `0` (default) | real-valued scalar

Specify bias for the fixed-point data type as any real number. For more
information, see Specifying a Fixed-Point Data Type.

#### Dependencies

To enable this parameter, set **Scaling** to
`Slope and bias`.

### **Data type override** — Data type override mode `Inherit` (default) | `Off`

Select the data type override mode for this signal. You can select:

- `Inherit` — Inherits the data type override setting specified for the model.
- `Off` — Ignores the data type override setting specified for the model and uses the fixed-point data type you specify.

#### Dependencies

To enable this parameter, set **Mode** to `Built in` or `Fixed point`. For more information, see Specify Data Types Using Data Type Assistant.

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

### R2023b: Weighted Sample Time Math Block Update

The Weighted Sample Time Math block now supports:

- Additional output types

  - `double`
  - `single`
  - `int8`
  - `uint8`
  - `int16`
  - `uint16`
  - `int32`
  - `uint32`
  - `int64`
  - `uint64`
  - `fixdt(1,16,0)`
  - `fixdt(1,16,20,0)`
- `Fixed point` as a new option to the
  **Mode** parameter, which enables the fixed-point
  parameters:

  - **Signedness**
  - **Scaling**
  - **Word length**
  - **Slope**
  - **Bias**
  - **Data type override**
