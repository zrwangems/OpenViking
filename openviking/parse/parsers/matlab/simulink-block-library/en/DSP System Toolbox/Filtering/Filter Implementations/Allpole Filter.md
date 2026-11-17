---
type: simulink-block
title: 'Allpole Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Implementations'
documentation_page: 'allpolefilter'
documentation_source_path: 'ref/allpolefilter.html'
language: en
---

# Allpole Filter

## Ports
```yaml
ports:
- name: In
  summary: Data input vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: Den
  summary: Filter denominator coefficients scalar | row vector
  direction: input
  data_types: single | double | int8 | int16 | int32 | fixed point
- name: Out
  summary: Filtered output vector | matrix
  direction: output
  data_types: single | double | int8 | int16 | int32 | fixed point
```

### Input

### **In** — Data input vector | matrix

Specify the data input as a vector or a matrix. The block accepts
variable-size inputs. During simulation, you can change the size of each
input channel, but the number of channels must remain the same.

The data input and the filter coefficients must have the same data
type.

If the input is fixed point, it must be a signed integer or a
signed fixed point value with a power-of-two slope and zero bias.

This port is unnamed until you set **Coefficient
source** to `Input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**Complex Number Support:** Yes

### **Den** — Filter denominator coefficients scalar | row vector

Specify the denominator coefficients of the filter transfer function
as a scalar or a row vector. The data input and the filter coefficients
must have the same data type.

#### Dependencies

To enable this port, set **Coefficient source**
to `Input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Out** — Filtered output vector | matrix

Filtered output, returned as a vector or a matrix. The size, data
type, and complexity of the output signal matches that of the input
signal.

This port is unnamed until you set **Coefficient
source** to `Input port`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Coefficient source
  summary: Coefficient source Dialog parameters (default) | Input port
  group: Main Tab
- name: Filter structure
  summary: Specify filter structure Direct form (default) | Direct form transposed | Lattice AR
  group: Main Tab
- name: Coefficients
  summary: Filter denominator coefficients [1 0.1] (default) | scalar | row vector
  group: Main Tab
- name: Input processing
  summary: Input processing Columns as channels (frame based) (default) | Elements as channels (sample based)
  group: Main Tab
- name: Initial states
  summary: Initial conditions of filter states 0 (default) | scalar | vector | matrix
  group: Main Tab
- name: Coefficients
  summary: 'Coefficient data type Inherit: Same word length as input (default) | int8 | uint8 | int16 | uint16 | int32 | uint32
    | int64 | uint64 | fixdt(1,16) | fixdt(1,16,0)'
  group: Data Types Tab
- name: Coefficients Minimum
  summary: Minimum value of filter coefficients [] (default) | scalar
  group: Data Types Tab
- name: Coefficients Maximum
  summary: Maximum value of filter coefficients [] (default) | scalar
  group: Data Types Tab
- name: Product output
  summary: 'Product output data type Inherit: Inherit via internal rule (default) | Inherit: Same as input | int8 | uint8
    | int16 | uint16 | int32 | uint32 | int64 | uint64 | fixdt(1,16,0)'
  group: Data Types Tab
- name: Accumulator
  summary: 'Accumulator data type Inherit: Inherit via internal rule (default) | Inherit: Same as input | Inherit: Same as
    product output | int8 | uint8 | int16 | uint16 | int32 | uint32 | int64 | uint64 | fixdt(1,16,0)'
  group: Data Types Tab
- name: State
  summary: 'State data type Inherit: Same as accumulator (default) | Inherit: Same as input | int8 | uint8 | int16 | uint16
    | int32 | uint32 | int64 | uint64 | fixdt(1,16,0)'
  group: Data Types Tab
- name: Output
  summary: 'Output data type Inherit: Same as input (default) | Inherit: Same as accumulator | int8 | uint8 | int16 | uint16
    | int32 | uint32 | int64 | uint64 | fixdt(1,16) | fixdt(1,16,0)'
  group: Data Types Tab
- name: Output Minimum
  summary: Output minimum [] (default) | scalar
  group: Data Types Tab
- name: Output Maximum
  summary: Output maximum [] (default) | scalar
  group: Data Types Tab
- name: Lock data type settings against changes by the fixed-point tools
  summary: Prevent fixed-point tools from overriding data types off (default) | on
  group: Data Types Tab
- name: Integer rounding mode
  summary: Integer rounding mode Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest | Zero
  group: Data Types Tab
- name: Saturate on integer overflow
  summary: Saturate on integer overflow off (default) | on
  group: Data Types Tab
```

### Main Tab

### **Coefficient source** — Coefficient source `Dialog parameters` (default) | `Input port`

Select whether you want to specify the filter coefficients in the block mask or through
an input port.

### **Filter structure** — Specify filter structure `Direct form` (default) | `Direct form transposed` | `Lattice AR`

Specify the filter structure as one of these:

- `Direct form`
- `Direct form transposed`
- `Lattice AR`

The block does not support analysis methods for fixed-point processing if you specify
the structure as `Direct form` or
`Direct form transposed`.

### **Coefficients** — Filter denominator coefficients [1 0.1] (default) | scalar | row vector

Specify the denominator coefficients of the filter transfer function
as a scalar or a row vector.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Coefficient
source** to `Dialog
parameters`.

### **Input processing** — Input processing `Columns as channels (frame based)` (default) | `Elements as channels (sample based)`

Specify whether the block performs sample- or frame-based processing.
You can select one of the following options:

- `Columns as channels (frame based)`
  — Treat each column of the input as an independent
  channel (frame-based processing).
- `Elements as channels (sample based)`
  — Treat each element of the input as an independent
  channel (sample-based processing).

### **Initial states** — Initial conditions of filter states `0` (default) | scalar | vector | matrix

Specify the initial conditions of the filter states as a scalar,
vector, or a matrix.

The Allpole Filter block initializes the internal
filter states to zero by default, which has the same effect as assuming
that past inputs and outputs are zero. You can optionally use this
parameter to specify nonzero initial conditions for the filter
delays.

To determine the number of initial states you must specify and how to
specify them, see the table on valid initial states. The
**Initial states** parameter can take one of the
forms described in this table.

**Valid Initial States**

| Initial Condition | Description |
| --- | --- |
| Scalar | The block initializes all delay elements in the filter to the scalar value. |
| Vector or matrix   (for applying different delay elements to each channel) | Each vector or matrix element specifies a unique initial condition for a corresponding delay element in a corresponding channel:  - The vector length equals the product of the   number of input channels and the number of delay   elements in the filter,   `#_of_filter_coeffs-1` (or   `#_of_reflection_coeffs` for   `Lattice AR`). - The matrix must have the same number of rows   as the number of delay elements in the filter,   `#_of_filter_coeffs-1`   (`#_of_reflection_coeffs` for   `Lattice AR`), and must   have one column for each channel of the input   signal. |

### Data Types Tab

### **Coefficients** — Coefficient data type `Inherit: Same word length as input` (default) | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)`

Specify the coefficient data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Same word length as
  input`
- A built-in integer, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

Click the **Show data type assistant** button
Double greater than symbols to display the **Data Type
Assistant**, which helps you set the
**Coefficients** parameter.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

### **Coefficients Minimum** — Minimum value of filter coefficients `[]` (default) | scalar

Specify the minimum value of the filter coefficients. The default value is
`[]` (unspecified). Simulink software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters (Simulink))
- Automatic scaling of fixed-point data types

### **Coefficients Maximum** — Maximum value of filter coefficients `[]` (default) | scalar

Specify the maximum value of the filter coefficients. The default value is
`[]` (unspecified). Simulink software uses this value to perform:

- Parameter range checking (see Specify Minimum and Maximum Values for Block Parameters (Simulink))
- Automatic scaling of fixed-point data types

### **Product output** — Product output data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)`

Specify the product output data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`. For more information on this rule, see
  Inherit via Internal Rule.
- A built-in data type, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

Click the **Show data type assistant** button
Double greater than symbols to display the **Data Type
Assistant**, which helps you set the **Product
output** parameter.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

### **Accumulator** — Accumulator data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as input` | `Inherit: Same as product output` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)`

Specify the accumulator data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Inherit via internal
  rule`. For more information on this rule, see
  Inherit via Internal Rule.
- A built-in data type, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

Click the **Show data type assistant** button
Double greater than symbols to display the **Data Type
Assistant**, which helps you set the
**Accumulator** parameter.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

### **State** — State data type `Inherit: Same as accumulator` (default) | `Inherit: Same as input` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16,0)`

Specify the state data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Same as
  accumulator`
- A built-in integer, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

Click the **Show data type assistant** button
Double greater than symbols to display the **Data Type
Assistant**, which helps you set the
**State** parameter.

See Specify Data Types Using Data Type Assistant (Simulink) for more information.

#### Dependencies

To enable this parameter, set **Filter
structure** to `Lattice
AR`.

### **Output** — Output data type `Inherit: Same as input` (default) | `Inherit: Same as accumulator` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)`

Specify the output data type. You can set it to:

- A rule that inherits a data type, for example,
  `Inherit: Same as
  accumulator`
- A built-in data type, for example,
  `int8`
- A data type object, for example, a
  `Simulink.NumericType` object
- An expression that evaluates to a data type, for example,
  `fixdt(1,16,0)`

Click the **Show data type assistant** button
 to display the **Data Type
Assistant**, which helps you set the
**Output** parameter.

See Control Data Types of Signals (Simulink) for more
information.

### **Output Minimum** — Output minimum `[]` (default) | scalar

Specify the minimum value that the block must output. The default value is
`[]` (unspecified). Simulink software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges (Simulink))
- Automatic scaling of fixed-point data types

### **Output Maximum** — Output maximum `[]` (default) | scalar

Specify the maximum value that the block must output. The default value is
`[]` (unspecified). Simulink software uses this value to perform:

- Simulation range checking (see Specify Signal Ranges (Simulink))
- Automatic scaling of fixed-point data types

### **Lock data type settings against changes by the fixed-point tools** — Prevent fixed-point tools from overriding data types `off` (default) | `on`

Select this parameter to prevent the fixed-point tools from overriding the data types
you specify in the block dialog box.

### **Integer rounding mode** — Integer rounding mode `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Specify the rounding mode for fixed-point operations.

### **Saturate on integer overflow** — Saturate on integer overflow `off` (default) | `on`

When you select this check box, the block applies saturation to every
internal operation and not just the output or result. In general, the
code generation process can detect when overflow is not possible. In
this case, the code generator does not produce saturation code.

| Action | Reasons for Taking This Action | What Happens for Overflows | Example |
| --- | --- | --- | --- |
| Select this check box. | Your model has possible overflow and you want explicit saturation protection in the generated code. | Overflows saturate to either the minimum or maximum value that the data type can represent. | An overflow associated with a signed 8-bit integer can saturate to -128 or 127. |
| Do not select this check box. | You want to optimize efficiency of your generated code.  You want to avoid overspecifying how a block handles out-of-range signals. For more information, see Troubleshoot Signal Range Errors (Simulink). | Overflows wrap to the appropriate value that is representable by the data type. | The number 130 does not fit in a signed 8-bit integer and wraps to -126. |
## Libraries

DSP System Toolbox / Filtering / Filter Implementations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed pointa` | `integera` | `single` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a This block only supports signed fixed-point data types. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2011b**

## Description

Model allpole filters

The Allpole Filter block independently filters each channel of the input
signal with the specified allpole filter. The block can implement static filters with
fixed coefficients and time-varying filters with coefficients that change over time. You
can tune the coefficients of a static filter during simulation.

This block filters each channel of the input signal independently over time. The
**Input processing** parameter allows you to specify whether the
block treats each element of the input as an independent channel (sample-based
processing), or each column of the input as an independent channel (frame-based
processing).

This block supports the Simulink® state logging feature. See State (Simulink) for more information.
