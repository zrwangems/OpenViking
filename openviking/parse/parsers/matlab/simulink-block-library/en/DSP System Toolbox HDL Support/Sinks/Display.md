---
type: simulink-block
title: 'Display'
family: 'hdlcoder'
product_id: 'dsp-system-toolbox-hdl-support'
product_name: 'DSP System Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'display'
documentation_source_path: '../simulink/slref/display.html'
language: en
---

# Display

## Ports

### Input

### **Port\_1** — Input data scalar | vector

Input data to display.

**Data Types:** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `string` | `Boolean` | `fixed point` | `enumerated`

## Parameters

### **Numeric display format** — Format to display numeric input data `short` (default) | `long` | `short_e` | `long_e` | `bank` | `hex (Stored Integer)` | `binary (Stored Integer)` | `decimal (Stored Integer)` | `octal (Stored Integer)`

Specify the format of the numeric data that appears.

| If You Select... | The Block Displays... |
| --- | --- |
| `short` | A 5-digit scaled value with fixed decimal point |
| `long` | A 15-digit scaled value with fixed decimal point |
| `short_e` | A 5-digit value with a floating decimal point |
| `long_e` | A 16-digit value with a floating decimal point |
| `bank` | A value in fixed dollars and cents format (but with no $ or commas) |
| `hex (Stored Integer)` | The stored integer value of a fixed-point input in hexadecimal format |
| `binary (Stored Integer)` | The stored integer value of a fixed-point input in binary format |
| `decimal (Stored Integer)` | The stored integer value of a fixed-point input in decimal format |
| `octal (Stored Integer)` | The stored integer value of a fixed-point input in octal format |

If the numeric input to a Display block has a
`single`, `double`, or
`half` data type, and the display format is a
stored-integer, the output displays using the `long`
format.

If the numeric input to a Display block has an enumerated
data type (see Simulink Enumerations and Define Simulink Enumerations):

- The block displays enumerated values, not the values of underlying
  integers.
- Setting **Numeric display format** to any of the
  `Stored Integer` settings causes an
  error.

If the incoming signal is of type string, the selection of the
**Numeric display format** parameter does not affect
the display of the string.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Format` |
| **Type:** character vector |
| **Values:** `'short'` | `'long'` | `'short_e'` | `'long_e'` | `'bank'` | `'hex (Stored Integer)'` | `'binary (Stored Integer)'` | `'decimal (Stored Integer)'` | `'octal (Stored Integer)'` |
| **Default:** `'short'` |

### **Decimation** — Display rate `1` (default) | `integer`

Specify how often to display data.

The amount of data that appears and the time steps at which the data
appears depend on the **Decimation** block parameter and
the `SampleTime` property.

- The **Decimation** parameter enables you to
  display data at every *n*th sample, where
  *n* is the decimation factor. The default
  decimation, `1`, displays data at every time
  step.

  **Note**

  The Display block updates its display at the initial time,
  even when the **Decimation** value is greater
  than one.
- The `SampleTime` property, which you can set with
  `set_param`,
  enables you to specify a sampling interval at which to display
  points. This property is useful when you are using a variable-step
  solver where the interval between time steps is not the same. The
  default sample time, `-1`, causes the block to
  ignore the sampling interval when determining the points to display.

  **Note**

  If the block inherits a sample time of
  `Inf`, the
  **Decimation** parameter is
  ignored.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Decimation` |
| **Type:** character vector |
| **Values:** `'1'` | integer |
| **Default:** `'1'` |

### **Floating display** — Floating display `off` (default) | `on`

To use the block as a floating display, select **Floating display**.
The block input port disappears and the block displays the value of the
signal on a selected line.

If you select **Floating display**:

- Turn off signal storage reuse for your model. See Signal storage reuse (Simulink Coder) for more information.
- Do not connect a multidimensional signal to a floating display.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Floating` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

## Libraries

Simulink / Sinks HDL Coder / Sinks

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `enumerated` | `fixed point` | `half` | `integer` | `single` | `string` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Ignored for code generation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `No HDL` | Do not generate HDL code for this block. |

**HDL Block Properties**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | Control the removal of unconnected logic. The default is `off`, which means unconnected logic is not preserved in HDL code. For more details, see PreserveUpstreamLogic (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Show value of input

The Display block shows the value of the input data. You can specify the
frequency of the display. For numeric input data, you can also specify the format of
display.

If the block input is an array, you can resize the block vertically or horizontally to
show more than just the first element. If the block input is a vector, the block
sequentially adds display fields from left to right and top to bottom. The block
displays as many values as possible. A black triangle indicates that the block is not
displaying all input array elements.

The Display block shows the first 200 elements of a vector signal and the
first 20 rows and 10 columns of a matrix signal.

**Note**

If you specify a numeric display format that is not large enough to display all
the digits of a value, the displayed values may lose precision. The result depends
on your computer hardware and operating system.

### Display Abbreviations

The following abbreviations appear on the Display block to help you identify
the format of the value.

| When You See... | The Value That Appears Is... |
| --- | --- |
| `(SI)` | The stored integer value  **Note**  `(SI)` does not appear when the signal is of an integer data type. |
| `hex` | In hexadecimal format |
| `bin` | In binary format |
| `oct` | In octal format |

### Displaying Strings

When working with strings, the Display block displays:

- Strings with double quotes.
- Special characters such as newline are shown as escaped sequences, for
  example `'\n'`.
- Non-displayable characters as escaped octal number, for example
  `'\201'`.

If the incoming signal is of type string, the **Numeric display
format** parameter selection does not affect the display of the
string.
