---
type: simulink-block
title: 'BPSK Demodulator Baseband'
family: 'communications-toolbox-hdl-support'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Modulation / PM'
documentation_page: 'bpskdemodulatorbaseband'
documentation_source_path: '../comm/ref/bpskdemodulatorbaseband.html'
language: en
---

# BPSK Demodulator Baseband

## Ports
```yaml
ports:
- name: In
  summary: BPSK-modulated baseband signal scalar | vector | matrix
  direction: input
  data_types: double | single | fixed point
- name: Var
  summary: Noise Variance positive scalar | vector of positive values
  direction: input
  data_types: double
- name: Out
  summary: Demodulated signal scalar | vector
  direction: output
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
```

### Input

### **In** — BPSK-modulated baseband signal scalar | vector | matrix

BPSK-modulated baseband signal, specified as a scalar, vector, or
matrix. When this input is a matrix, each column is treated as an
independent channel. This port is unnamed until the
`Var` port is enabled. When the noise variance or
signal power result in computations involving extreme positive or
negative magnitudes, see BPSK Soft Demodulation for
demodulation decision type considerations.

**Data Types:** `double` | `single` | `fixed point`
**Complex Number Support:** Yes

### **Var** — Noise Variance positive scalar | vector of positive values

Noise variance, specified as a positive scalar or vector of positive
values. When the noise variance or signal power result in computations
involving extreme positive or negative magnitudes, see BPSK Soft Demodulation for
demodulation decision type considerations.

#### Dependencies

To enable this parameter, set the **Noise variance
source** parameter to
`Port`.

**Data Types:** `double`
### Output

### **Out** — Demodulated signal scalar | vector

Demodulated signal, returned as a scalar or vector. If the output is a
scalar, the value is an integer. If the output is a vector, it is an
integer-valued or binary-valued vector.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
## Parameters
```yaml
parameters:
- name: Decision type
  summary: Decision type Hard decision (default) | Log-likelihood ratio | Approximate log-likelihood ratio
  group: Main
- name: Noise variance source
  summary: Noise variance source Dialog (default) | Port
  group: Main
- name: Noise variance
  summary: Noise Variance 1 (default) | positive scalar | vector of positive values
  group: Main
- name: Phase offset (rad)
  summary: Phase of zeroth point 0 (default) | real-valued scalar
  group: Main
- name: Output data type
  summary: Output data type Inherit via internal rule (default) | Smallest unsigned integer | double | single | ...
  group: Data Types
- name: Derotate factor
  summary: Derotate factor Same word length as input (default) | Specify word length
  group: Data Types
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Main

### **Decision type** — Decision type `Hard decision` (default) | `Log-likelihood ratio` | `Approximate log-likelihood ratio`

Decision type used during demodulation, specified as `Hard
decision`, `Log-likelihood
ratio` or `Approximate log-likelihood
ratio`. For more information, see BPSK Hard-Decision Demodulation and BPSK Soft Demodulation.

The output matches the data type of the input values when
**Decision type** is set to
`Log-likelihood ratio` or
`Approximate log-likelihood ratio`.

### **Noise variance source** — Noise variance source `Dialog` (default) | `Port`

Noise variance source, specified as `Dialog`
or `Port`.

- `Dialog` — The noise variance is
  set using the `Noise variance` parameter.
- `Port` — The noise variance is
  set using the `Var` input port.

### **Noise variance** — Noise Variance `1` (default) | positive scalar | vector of positive values

Noise variance, specified as a positive scalar or vector of positive
values.

- When specified as a scalar, that value is used on all
  elements in the input signal.
- When specified as a vector, the vector length must be
  equal to the number of columns in the input signal. Each
  noise variance vector element is applied to its
  corresponding column in the input signal.

When the noise variance or signal power result in computations
involving extreme positive or negative magnitudes, see BPSK Soft Demodulation for
demodulation decision type considerations.

This parameter is tunable in normal mode, accelerator mode and rapid
accelerator mode. If you use the Simulink
Coder™ rapid simulation (RSIM) target to build an RSIM
executable, then you can tune the parameter without recompiling the
model. This is useful for Monte Carlo simulations, in which you run the
simulation multiple times (perhaps on multiple computers) with different
amounts of noise.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set the `Decision type` parameter to set to either
`Log-likelihood ratio` or
`Approximate log-likelihood ratio` and
set the **Noise variance source** parameter to
`Dialog`.

### **Phase offset (rad)** — Phase of zeroth point `0` (default) | real-valued scalar

Phase of the zeroth point, specified as a real-valued scalar. Units
are in radians.

**Example:** `pi/4`

### Data Types

### **Output data type** — Output data type `Inherit via internal rule` (default) | `Smallest unsigned integer` | `double` | `single` | ...

Output data type, specified as one of these options

- When you set the **Decision type** parameter
  to **Hard decision**:

  - `Inherit via internal
    rule` — The block inherits the output
    data type from the input port. If the input is a
    floating-point type (`single` or
    `double`), the output data type
    is the same as the input data type. If the input
    data type is fixed-point, the output data type works
    as if you set this parameter to `Smallest
    unsigned integer`.
  - `Smallest unsigned
    integer` — The block selects the
    output data type based on the settings used in the
    **Hardware Implementation** pane
    of the Configuration Parameters dialog box of the
    model. If you select `ASIC/FPGA` in
    the **Hardware Implementation**
    pane, the output data type is the ideal minimum
    one-bit size, that is, `ufix(1)`.
    For all other selections, the output data type is an
    unsigned integer with the smallest available word
    length large enough to fit one bit, usually
    corresponding to the size of a character (for
    example, `uint8`).
  - `double`
  - `single`
  - `int8`
  - `uint8`
  - `int16`
  - `uint16`
  - `int32`
  - `uint32`
  - `boolean`
- When you set the **Decision type** parameter
  to **Log-likelihood ratio** or
  **Approximate log-likelihood ratio** — The
  block inherits the output data type matches the data type of the
  input.

For information about specifying data types, see Data Type Assistant.

### **Derotate factor** — Derotate factor `Same word length as input` (default) | `Specify word length`

Derotate factor, specified as `Same word length as
input` or `Specify word
length`.

#### Dependencies

This parameter applies only when the input is fixed-point and the
**Phase offset (rad)** parameter is not a
multiple of π/2.
## Libraries

Communications Toolbox / Modulation / Digital Baseband Modulation / PSK Communications Toolbox HDL Support / Modulation / PM

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed pointa, b` | `integer` | `single` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |
|  |  |
| --- | --- |
| a Fixed-point inputs must be signed.  b ufix(1) only at the output when ASIC/FPGA is selected in the Hardware Implementation Pane. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Architecture**

This block has one default HDL architecture.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

## Version History

**Introduced before R2006a**

## Description

Demodulate BPSK-modulated data

The BPSK Demodulator Baseband block demodulates a signal that was modulated using the binary phase shift
keying (BPSK) method. The input is a baseband representation of the modulated signal.
This block accepts a scalar or column vector input signal. The input signal must be a
discrete-time complex signal. The block maps the points exp(jϕ) or -exp(jϕ) to 0 and 1, respectively. The `Phase offset
(rad)` parameter specifies the value of ϕ.
