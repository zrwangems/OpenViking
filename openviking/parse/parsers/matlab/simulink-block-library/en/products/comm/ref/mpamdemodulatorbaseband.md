---
type: simulink-block
title: 'M-PAM Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Modulation / Digital Baseband Modulation / Amplitude Modulation'
documentation_page: 'mpamdemodulatorbaseband'
documentation_source_path: 'ref/mpamdemodulatorbaseband.html'
language: en
---

# M-PAM Demodulator Baseband

## Ports

### Input

### **In** — *M*-PAM-modulated signal scalar | column vector

*M*-PAM-modulated signal, specified as a scalar or
column vector. This port is unnamed on the block.

**Data Types:** `double` | `single` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Out** — Demodulated signal scalar | vector

Demodulated signal, returned as a scalar or vector. The dimensions of
the demodulated signal depend on the value you specify for the
**Output
data type** parameter. This port is unnamed on the
block.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **M-ary number** — Modulation order `4` (default) | positive, even integer

Modulation order, specified as a positive, even integer. The
modulation order, *M*, specifies the number of points
in the signal constellation. The block scales the signal constellation
based on how you set the **Normalization method**
parameter.

### **Output type** — Output type `Integer` (default) | `Bit`

Output type, specified as `Integer` or
`Bit`. When you set this parameter to
`Bit`, the **M-ary
number** parameter must be
2*K* for some
positive integer *K*.

### **Constellation ordering** — Mapping order of symbols `Binary` (default) | `Gray`

Mapping order of the symbols, specified as
`Gray` or
`Binary`. This parameter determines how the
block maps each symbol to a group of output bits or an integer.

The **Constellation ordering** parameter indicates
how the block assigns binary words to points of the signal
constellation. For more information, see Integer-Valued Signals and Binary-Valued Signals.

### **Normalization method** — Scaling method for the constellation `Min. distance between symbols` (default) | `Average Power` | `Peak Power`

Scaling method for the constellation, specified as `Min.
distance between symbols`, `Average
Power`, or `Peak Power`. For
more information, see Integer-Valued Signals and Binary-Valued Signals.

### **Minimum distance** — Distance between two nearest constellation points `2` (default) | positive scalar

Distance between the two nearest constellation points, specified as a
positive scalar.

#### Dependencies

This parameter appears when you set **Normalization method** to `Min. distance
between symbols`.

### **Average power, referenced to 1 ohm (watts)** — Average power `1` (default) | positive scalar

Average power of the symbols in the constellation in watts, specified
as a positive scalar. Power values assume a nominal impedance of 1
ohm.

#### Dependencies

This parameter appears when you set **Normalization method** to `Average
Power`.

### **Peak power, referenced to 1 ohm (watts)** — Maximum power `1` (default) | positive scalar

Maximum power of the symbols in the constellation in watts, specified
as a positive scalar. Power values assume a nominal impedance of 1
ohm.

#### Dependencies

This parameter appears when you set **Normalization method** to `Peak
Power`.

### Data Types

### **Output data type** — Output data type `Inherit via internal rule` (default) | `Smallest unsigned integer` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Output data type, specified as `Inherit via internal
rule`, `Smallest unsigned
integer`, `double`,
`single`, `int8`,
`uint8`, `int16`,
`uint16`, `int32`,
`uint32`, or
`boolean`.

- When you select `Inherit via internal
  rule`, the block inherits the data type based
  on an internal rule. For more information on this rule, see
  Inherit via Internal Rule. The output data type is the
  same as the input data type if the input is of type
  `single` or
  `double`. Otherwise, the output
  data type is the same as for `'Smallest unsigned
  integer'`.
- When you select `'Smallest unsigned
  integer'`, the block sets the output data type
  based on the settings in the **Hardware
  Implementation** pane of the Configuration
  Parameters dialog box. If `ASIC/FPGA` is
  selected in the **Hardware Implementation**
  pane, the output data type is the ideal minimum size, that is,
  `ufix(1)` for bit outputs and
  `ufix(ceil(log2(M)))` for integer outputs.
  For all other selections, it is an unsigned integer with the
  smallest available word length large enough to fit the ideal
  minimum size, usually corresponding to the size of a char (for
  example, `uint8`).
- For integer outputs, you can set this parameter to
  `Smallest unsigned integer`,
  `int8`,
  `uint8`,
  `int16`,
  `uint16`,
  `int32`,
  `uint32`,
  `single`, and
  `double`. For bit outputs, the
  options are `Smallest unsigned
  integer`, `int8`,
  `uint8`,
  `int16`,
  `uint16`,
  `int32`,
  `uint32`,
  `boolean`,
  `single`, or
  `double`.

For information about specifying data types, see Data Type Assistant.

### **Denormalization factor** — Denormalization factor data type `Inherit: Same word length as input` (default) | `fixdt(1,16)` | `<data type expression>`

Specify the denormalization factor data type as `Inherit:
Same word length as input`,
`fixdt(1,16)`, or `<data
type expression>`. This scaling factor is derived from
**Normalization method** and other parameter of
the block. The block always uses a best-precision fraction
length.

For information about specifying data types, see Data Type Assistant.

#### Dependencies

This parameter applies only when the input signal is fixed-point
and the derived denormalization factor is a nonunity value (not
equal to 1).

### **Product output** — Product output data type `Inherit: Inherit via internal rule` (default) | `fixdt(1,16)` | `<data type expression>`

Specify the product data type as `Inherit: Inherit via
internal rule`, `fixdt(1,16)`,
or `<data type expression>`.

When you select `Inherit: Inherit via internal
rule`, the block computes the full-precision product
word length and fraction length. For information about the
full-precision **Product output** internal rule, see
Internal Rule for
Product Data Types.

The block uses rounding mode when the result of a fixed-point
calculation does not map exactly to a number representable by the data
type and scaling storing the result. For more information, see Rounding Modes or Rounding Mode: Simplest (Fixed-Point Designer).

For information about specifying data types, see Data Type Assistant.

#### Dependencies

This parameter applies only when the input is a fixed-point signal
and the derived denormalization factor is a nonunity value (not
equal to 1).

### **Rounding mode** — Rounding mode for fixed-point operations `Wrap` (default) | `Saturate`

Specify the rounding mode for **Product output** fixed-point operations as
`Wrap` or
`Saturate`. The block uses rounding mode
when the result of a fixed-point calculation does not map exactly to a
number representable by the data type. For more information, see Rounding
Modes or Rounding Mode: Simplest (Fixed-Point Designer).

#### Dependencies

This parameter applies for **Product output** only.

### **Saturate on integer overflow** — Option to saturate on integer overflow `off` (default) | `on`

Select this check box to saturate on integer overflow.

#### Dependencies

This parameter applies for **Product output** only.

### **Sum** — Sum data type `Inherit: Inherit via internal rule` (default) | `Inherit: Same as product output` | `fixdt(1,16)` | `<data type expression>`

Specify the sum data type as `Inherit: Inherit via
internal rule`, `Inherit: Same as product
output`, `fixdt(1,16)`, or
`<data type expression>`.

- When you select `Inherit: Inherit via internal
  rule`, the block computes the full-precision
  sum word length and fraction length, based on the two inputs to
  the sum in the flow diagram of the fixed-point Hard Decision
  Algorithm signal. The rule is the same as the
  fixed-point inherit rule of the internal **Accumulator
  data type** parameter in the Sum (Simulink) block.
- When you select `Inherit: Same as product
  output` and **Product
  output** applies, the block configures the data
  type of the **Sum** parameter to be the same
  as the **Product output** data type.
- When you select `Inherit: Same as product
  output` and **Product
  output** does not apply, then the block ignores
  this setting and uses the `Inherit: Inherit via
  internal rule` and computed sum.

For information about specifying data types, see Data Type Assistant.

#### Dependencies

This parameter applies only when the input is a fixed-point
signal.

## Libraries

Communications Toolbox / Modulation / Digital Baseband Modulation / AM

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed pointa, b` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
|  |  |
| --- | --- |
| a Fixed-point inputs must be signed.  b When ASIC/FPGA is selected in the Hardware Implementation Pane, output is ufix(1) for bit outputs, and ufix(ceil(log2(M))) for integer outputs. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Demodulate M -PAM-modulated data

The M-PAM Demodulator Baseband block demodulates a signal that was modulated using
*M*-ary pulse amplitude modulation.

**Note**

All values of power assume a nominal impedance of 1 ohm.
