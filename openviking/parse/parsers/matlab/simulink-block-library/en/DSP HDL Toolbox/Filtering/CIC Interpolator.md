---
type: simulink-block
title: 'CIC Interpolator'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: 'cicinterpolator'
documentation_source_path: 'ref/cicinterpolator.html'
language: en
---

# CIC Interpolator

## Ports

### Input

### **data** — Input data scalar | column vector

Input data, specified as a scalar or a column vector with a length from 1 to 64.
The input data must be a signed integer or signed fixed point with a word length less
than or equal to 32.

While processing the input data, the block implements the rounding method
`Floor` and the overflow action `Wrap`. For more
details, see Rounding Modes and Overflow Handling.

**Data Types:** `int8` | `int16` | `int32` | `signed fixed point`
**Complex Number Support:** Yes

### **valid** — Indicates valid input data scalar

Control signal that indicates if the input data is valid. When
**valid** is `1` (`true`), the
block captures the values from the input **data** port. When
**valid** is `0` (`false`), the
block ignores the values from the input **data** port.

**Data Types:** `Boolean`

### **R** — Variable interpolation rate scalar

Use this port to dynamically specify the variable interpolation rate during run
time.

This value must have the data type `fixdt(0,12,0)` and must be an
integer in the range from 1 to the **Interpolation factor (Rmax)**
parameter value.

#### Dependencies

To enable this port, on the **Main** tab, set the
**Interpolation factor source** parameter to `Input
port`.

**Data Types:** `fixdt(0,12,0)`

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

### **data** — CIC-interpolated output data scalar | column vector

CIC-interpolated output data, returned as a scalar or a column vector with a
length from 1 to 64. You can define the data type of this output by setting the
**Output data type** parameter on the **Data
Types** tab.

**Data Types:** `int8` | `int16` | `int32` | `signed fixed point`
**Complex Number Support:** Yes

### **valid** — Indicates valid output data scalar

Control signal that indicates if the data from the output
**data** port is valid. When **valid** is
`1` (`true`), the block returns valid data from
the output **data** port. When **valid** is
`0` (`false`), the values from the output
**data** port are not valid.

**Data Types:** `Boolean`

### **ready** — Indicates block is ready for new input data scalar

Control signal that indicates that the block is ready for new input data sample on
the next cycle. When **ready** is `1`
(`true`), you can specify the **data**
and **valid**  inputs for the next time step. When
**ready** is `0`
(`false`), the block ignores any input data in the next time step.

**Data Types:** `Boolean`

## Parameters

### Main

### **Interpolation factor source** — Source of interpolation factor `Property` (default) | `Input port`

Select whether the block operates with a fixed or variable interpolation
rate.

- `Property` — Use a fixed interpolation rate
  specified from the **Interpolation factor (R)** parameter.
- `Input port` — Use a variable interpolation
  rate specified from the **R** input port.

**Note**

The block does not support variable interpolation for these two combinations of
input and output:

- Scalar input and vector output
- Vector input and vector output

### **Interpolation factor (R)** — Interpolation factor `2` (default) | integer from 1 to 2048

Specify the interpolation factor rate at which the block interpolates the input.
This value must be an integer. The range of available values depends on the type of
input and output data.

| Input Data | Output Data | Interpolation factor (R) Valid Values |
| --- | --- | --- |
| Scalar | Scalar | Integer from 1 to 2048 |
| Scalar | Vector | Integer from 1 to 64 |
| Vector | Vector | Integer from 1 to 64 |

**Note**

For vector inputs, select the interpolation factor rate and input vector length
such that their multiplication value does not exceed 64.

#### Dependencies

To enable this parameter, set the **Interpolation factor
source** parameter to `Property`.

### **Interpolation factor (Rmax)** — Upper bound of variable interpolation factor `2` (default) | integer from 1 to 2048

Specify the upper bound of the range of valid values for the
**R** input port.

**Note**

The block does not support variable interpolation for these two combinations of
input and output:

- Scalar input and vector output
- Vector input and vector output

#### Dependencies

To enable this parameter, set the **Interpolation factor
source** parameter to `Input port`.

### **Differential delay (M)** — Differential delay `1` (default) | `2`

Specify the differential delay of the comb part of the block.

### **Number of sections (N)** — Number of integrator and comb sections `2` (default) | `1` | `3` | `4` | `5` | `6`

Specify the number of sections in either the comb part or the integrator part of
the block.

### **Minimum number of cycles between valid input samples** — Minimum number of cycles between valid input samples `1` (default) | factors or multiples of *R*

Specify the minimum number of cycles between the valid input samples as
`1`, factors of *R*, or multiples of
*R* based on the type of input and output data, where
*R* is the interpolation factor.

| Input Data | Output Data | Minimum Number of Cycles Between Valid Input Samples |
| --- | --- | --- |
| Scalar | Scalar | greater than or equal to *R* |
| Scalar | Vector | factors less than R |
| Vector | Vector | 1 |

#### Dependencies

To enable this parameter, set the **Interpolation factor
source** parameter to `Property`.

### **Gain correction** — Output gain compensation `off` (default) | `on`

Select this parameter to compensate for the output gain of the block.

The latency of the block changes depending on the type of input, the interpolation
you specify, the number of sections, and the value of this parameter. For more
information on the latency of the block, see Latency.

### Data Types

### **Output data type** — Data type of output `Full precision` (default) | `Same word length as input` | `Minimum section word lengths`

Select the data type for the output data.

- `Full precision` — The output data type has a
  word length equal to the input word length plus gain bits.
- `Same word length as input` — The output data
  type has a word length equal to the input word length.
- `Minimum section word lengths` — The output
  data type uses the word length you specify in the **Output word
  length** parameter.

### **Output word length** — Word length of output `16` (default) | integer from 2 to 104

Specify the word length of the output as an integer from 2 to 104.

#### Dependencies

To enable this parameter, set the **Output data type**
parameter to `Minimum section word lengths`.

### Control Ports

### **Enable reset input port** — Option to enable reset input port `off` (default) | `on`

Select this parameter to enable the **reset** input port. The
reset signal implements a local synchronous reset of the data path registers.

For more reset considerations, see Tips.

### **Use HDL global reset** — Option to connect data path registers to generated HDL global reset signal `off` (default) | `on`

Select this parameter to connect the generated HDL global reset signal to the data
path registers. This parameter does not change the appearance of the block or modify
simulation behavior in Simulink. When you clear this parameter, the generated HDL global reset clears
only the control path registers. The generated HDL global reset can be synchronous or
asynchronous depending on the **HDL Code Generation** > **Global Settings** > **Reset type** parameter in the model Configuration Parameters.

For more reset considerations, see Tips.

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

Interpolate signal using CIC filter

The CIC Interpolator block interpolates an input signal by using a cascaded
integrator-comb (CIC) interpolation filter. CIC interpolation filters are a class of linear
phase finite impulse response (FIR) filters consisting of a comb part and an integrator part.
The CIC interpolation filter structure consists of *N* sections of cascaded
comb filters, a rate change factor of *R*, and *N* sections
of cascaded integrators. For more information about CIC interpolation filters, see Algorithms.

The block supports these combinations of input and output data.

- Scalar input and scalar output — Support for fixed and variable interpolation
  rates
- Scalar input and vector output — Support for fixed interpolation rates
  only
- Vector input and vector output — Support for fixed interpolation rates
  only

The block provides an architecture suitable for HDL code generation and hardware
deployment.

**Note**

You can also generate HDL code for this hardware-optimized algorithm, without creating a
Simulink® model, by using the DSP HDL IP Designer app. The app
provides the same interface and configuration options as the Simulink block.
