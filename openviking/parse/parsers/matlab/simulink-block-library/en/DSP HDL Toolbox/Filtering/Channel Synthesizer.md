---
type: simulink-block
title: 'Channel Synthesizer'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: 'channelsynthesizer'
documentation_source_path: 'ref/channelsynthesizer.html'
language: en
---

# Channel Synthesizer

## Ports
```yaml
ports:
- name: data
  summary: Input data real-valued row vector | complex-valued row vector
  direction: input
  data_types: fixed point | single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: valid
  summary: Indicates valid input data scalar
  direction: input
  data_types: Boolean
- name: reset
  summary: Clears internal states scalar
  direction: input
  data_types: Boolean
- name: data
  summary: Synthesized output data complex-valued column vector
  direction: output
  data_types: fixed point | single | double
- name: valid
  summary: Indicates valid output data scalar
  direction: output
  data_types: Boolean
```

### Input

### **data** — Input data real-valued row vector | complex-valued row vector

Input data, specified as a real- or complex-valued row vector.

The vector length must be a power of 2 and in the range [4, 64].

You can use `double` and `single` data types for
simulation, but not for HDL code generation.

**Data Types:** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
**Complex Number Support:** Yes

### **valid** — Indicates valid input data scalar

Control signal that indicates if the input data is valid. When
**valid** is `1` (`true`), the
block captures the values from the input **data** port. When
**valid** is `0` (`false`), the
block ignores the values from the input **data** port.

**Data Types:** `Boolean`

### **reset** — Clears internal states scalar

Control signal that clears internal states. When **reset** is
`1` (`true`), the block stops the current
calculation and clears internal states. When the **reset** is
`0` (`false`) and the input
**valid** is `1` (`true`), the
block captures data for processing.

For more reset considerations, see the Reset Signal section on the
Hardware Control Signals page.

#### Dependencies

To enable this port, on the **Control Ports** tab, select the
**Enable reset input port** parameter.

**Data Types:** `Boolean`
### Output

### **data** — Synthesized output data complex-valued column vector

Synthesized output data, returned as a complex-valued column vector.

When the input data type is a floating-point type, the output data inherits the
data type of the input data. When the input data type is an integer type or a
fixed-point type, the **Output** parameter on the **Data
Types** tab controls the output data type.

The output size is same as the input size and is equal to the number of frequency
bands or IFFT length. The output order is bit natural. The output data type depends on
the IFFT bit growth, required to avoid overflow, and the data type set in the
**Output** parameter.

**Data Types:** `fixed point` | `single` | `double`
**Complex Number Support:** Yes

### **valid** — Indicates valid output data scalar

Control signal that indicates if the data from the output
**data** port is valid. When **valid** is
`1` (`true`), the block returns valid data from
the output **data** port. When **valid** is
`0` (`false`), the values from the output
**data** port are not valid.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Filter coefficients
  summary: Polyphase filter coefficients [-0.0329 0.1218 0.3183 0.4829 0.5469 0.4829 0.5469 0.4829 0.3183 0.1218 -0.0329]
    (default) | complex-valued vector
  group: Main
- name: Filter structure
  summary: HDL filter architecture Direct form transposed (default) | Direct form systolic
  group: Main
- name: Complex multiplication
  summary: HDL implementation of complex multipliers Use 4 multipliers and 2 adders (default) | Use 3 multipliers and 5 adders
  group: Main
- name: Divide butterfly outputs by two
  summary: IFFT scaling on (default) | off
  group: Main
- name: Rounding mode
  summary: Rounding mode for typecasting output Floor (default) | Ceiling | Convergent | Nearest | Round | Zero
  group: Data Types
- name: Saturate on integer overflow
  summary: Overflow handling for typecasting output off (default) | on
  group: Data Types
- name: Coefficients
  summary: 'Data type of the coefficients Inherit: Same word length as input (default) | <data type expression>'
  group: Data Types
- name: Output
  summary: 'Data type of block output Inherit: via internal rule (default) | Inherit: Same as input | <data type expression>'
  group: Data Types
- name: Enable reset input port
  summary: Option to enable reset input port off (default) | on
  group: Control Ports
```

### Main

### **Filter coefficients** — Polyphase filter coefficients `[-0.0329 0.1218 0.3183 0.4829 0.5469 0.4829 0.5469 0.4829 0.3183 0.1218 -0.0329]` (default) | complex-valued vector

Polyphase filter coefficients, specified as a vector of numeric values. If the
number of coefficients is not a multiple of the number of frequency bands or the IFFT
length, the block pads this vector with zeros. The default filter specification is a
raised-cosine FIR filter, `rcosdesign(0.25,2,4,'sqrt')`. You can
specify a vector of coefficients or a call to a filter design function that returns
the coefficient values. By default, the block casts the coefficients to the same word
length as the input.

### **Filter structure** — HDL filter architecture `Direct form transposed` (default) | `Direct form systolic`

Specify the HDL filter architecture as one of these values:

- `Direct form transposed` — This architecture is a
  fully parallel implementation that is suitable for FPGA and ASIC applications.
  For architecture and performance details, see Fully Parallel Transposed Architecture.
- `Direct form systolic` — This architecture provides
  a fully parallel filter implementation that makes efficient use of Intel® and AMD® DSP blocks. For architecture and performance details, see Fully Parallel Systolic Architecture.

### **Complex multiplication** — HDL implementation of complex multipliers `Use 4 multipliers and 2 adders` (default) | `Use 3 multipliers and 5 adders`

Specify the HDL implementation of complex multipliers as either `Use 4
multipliers and 2 adders` or `Use 3 multipliers and 5
adders`. The speed of the multipliers depends on your synthesis tool
and target device.

### **Divide butterfly outputs by two** — IFFT scaling `on` (default) | `off`

When you select this parameter, the IFFT implements an overall
1/*N* scale factor by scaling the result of each pipeline stage by
2, where *N* is the IFFT length. This adjustment keeps the output of
the IFFT in the same amplitude range as its input. If you disable scaling, the IFFT
avoids overflow by increasing the word length by one bit at each stage.

### Data Types

### **Rounding mode** — Rounding mode for typecasting output `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

Use fixed-point arithmetic for internal calculations when the input is an integer
or fixed-point data type. This option does not apply when the input is
`single` or `double`. For more details, see Rounding Modes.

### **Saturate on integer overflow** — Overflow handling for typecasting output `off` (default) | `on`

Use fixed-point arithmetic for internal calculations when the input is an integer
or fixed-point data type. This option does not apply when the input is
`single` or `double`. Cast the coefficients and
output of the polyphase filter to the data types you specify. For more information,
see Overflow Handling.

### **Coefficients** — Data type of the coefficients `Inherit: Same word length as input` (default) | `<data type expression>`

Cast the polyphase filter coefficients to this data type using the rounding and
overflow settings you specify. When you select `Inherit: Same word length
as input` (default), the block selects the binary point using
`fixed point` best-precision rules.

### **Output** — Data type of block output `Inherit: via internal rule` (default) | `Inherit: Same as input` | `<data type expression>`

When you select `Inherit: via internal rule`, the block
selects a best-precision binary point by considering filter coefficients values and
the input data type range. When you select `Inherit: Same as
input`, the block casts the output of the polyphase filter to the input
data type, using the rounding and overflow settings you specify.

### Control Ports

### **Enable reset input port** — Option to enable reset input port `off` (default) | `on`

Select this parameter to enable the **reset** input port. The
reset signal implements a local synchronous reset of the data path registers.
## Libraries

DSP HDL Toolbox / Filtering

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports C/C++ code generation for Simulink accelerator and rapid accelerator modes and for DPI component generation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL implementation and
synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

## Version History

**Introduced in R2022a**

## Description

Combine narrowband signals into multichannel signal

The Channel Synthesizer block combines narrowband signals into a
multi-channel signal using the polyphase filter bank technique.

The block accepts a real- or complex-valued row-vector input data and control signals, and
outputs synthesized column-vector and a control signal. You can achieve gigasamples-per-second
(GSPS) throughput, also called super sample rates, using this block. The block implements a
polyphase filter, with one subfilter per input vector element. The block supports HDL code
generation and hardware deployment.

**Note**

You can also generate HDL code for this hardware-optimized algorithm, without creating a
Simulink® model, by using the DSP HDL IP Designer app. The app
provides the same interface and configuration options as the Simulink block.
