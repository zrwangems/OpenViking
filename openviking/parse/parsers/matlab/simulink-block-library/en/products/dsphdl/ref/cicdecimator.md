---
type: simulink-block
title: 'CIC Decimator'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized Filters and Transforms'
documentation_page: 'cicdecimator'
documentation_source_path: 'ref/cicdecimator.html'
language: en
---

# CIC Decimator

## Ports

### Input

### **data** — Input data scalar | column vector

Input data, specified as a scalar or a column vector with a length from 1 to 64.
The input data must be a signed integer or a signed fixed point with a word length
less than or equal to 32. The **Decimation factor (R)** parameter
must be an integer multiple of the input frame size.

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

### **R** — Variable decimation rate scalar

Use this port to dynamically specify the variable decimation rate during run
time.

This value must have the data type `fixdt(0,12,0)` and it must be
an integer in the range from 1 to the **Decimation factor (Rmax)**
parameter value.

#### Dependencies

To enable this port, on the **Main** tab, set the
**Decimation factor source** parameter to `Input
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

### **data** — CIC-decimated output data scalar | column vector

The block returns filtered output data as a scalar or a column vector with a
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

## Parameters

### Main

### **Decimation factor source** — Source of decimation factor `Property` (default) | `Input port`

Select whether the block operates with a fixed or variable decimation rate.

- `Property` — Use a fixed decimation rate
  specified from the **Decimation factor (R)** parameter.
- `Input port` — Use a variable decimation rate
  specified from the **R** input port.

**Note**

For vector inputs, the block does not support variable decimation.

### **Decimation factor (R)** — Decimation factor `2` (default) | integer from 1 to 2048

Specify the decimation factor rate at which the block decimates the input.

#### Dependencies

To enable this parameter, set the **Decimation factor source**
parameter to `Property`.

### **Decimation factor (Rmax)** — Upper bound of variable decimation factor `2` (default) | integer from 1 to 2048

Specify the upper bound of the range of valid values for the
**R** input port.

**Note**

For vector inputs, the block does not support variable decimation.

#### Dependencies

To enable this parameter, set the **Decimation factor source**
parameter to `Input port`.

### **Differential delay (M)** — Differential delay `1` (default) | `2`

Specify the differential delay of the comb part of the block.

### **Number of sections (N)** — Number of integrator and comb sections `2` (default) | `1` | `3` | `4` | `5` | `6`

Specify the number of sections in either the comb part or the integrator part of
the block.

### **Gain correction** — Output gain compensation `off` (default) | `on`

Select this parameter to compensate for the output gain of the block.

The latency of the block changes depending on the type of input, the decimation
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
  length** parameter. When you select this option, the block applies the
  pruning algorithm. For more information about the pruning algorithm, see [1].

### **Output word length** — Word length of output `16` (default) | integer from 2 to 104

Specify the word length of the output.

**Note**

When this value is `2`, `3`,
`4`, `5`, or `6`, the block
can overflow the output data.

#### Dependencies

To enable this parameter, set the **Output data type**
parameter to `Minimum section word lengths`.

### Control Ports

### **Enable reset input port** — Reset signal `off` (default) | `on`

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

**Introduced in R2019b**

### R2022a: Moved to DSP HDL Toolbox from DSP System Toolbox

Before R2022a, this block was named CIC Decimation HDL Optimized and was
included in the DSP System Toolbox™
**DSP System Toolbox HDL Support** library.

### R2022a: Changes to decimation factor parameters

You can now set the decimation factor to `1`. In previous releases, a
decimation factor of `1` was invalid.

| Configuration | Before R2022a | After 2022a |
| --- | --- | --- |
| Variable decimation factor | Select the **Variable decimation** parameter and set the **Decimation factor (R)** parameter to the maximum expected decimation factor. | Set the **Decimation factor source** parameter to `Input port` and set the **Decimation factor (Rmax)** parameter to the maximum expected decimation factor. The **decimFactor**  port is renamed to **R**. |
| Fixed decimation factor | Clear the **Variable decimation** parameter and set the **Decimation factor (R)** parameter to the desired decimation factor. | Set the **Decimation factor source** parameter to `Property` and set the **Decimation factor (R)** to the desired decimation factor. |

### R2021b: High-throughput interface

The block accepts and returns a column vector of elements that represent samples in
time. The input vector can contain up to 64 samples. When you use frame-based input, you
must use a fixed decimation factor.

### R2020a: Gain correction and programmable decimation factor

You can optionally enable automatic gain correction. You can also specify the decimation
factor as an input port.

## Description

Decimate signal using CIC filter

The CIC Decimator block decimates an input signal by using a cascaded
integrator-comb (CIC) decimation filter. CIC decimation filters are a class of linear phase
finite impulse response (FIR) filters consisting of a comb part and an integrator part. The
CIC decimation filter structure consists of *N* sections of cascaded
integrators, a rate change factor of *R*, and *N* sections
of cascaded comb filters. For more information about CIC decimation filters, see Algorithms.

The block supports these combinations of input and output data.

- Scalar input and scalar output — Support for fixed and variable decimation
  rates
- Vector input and scalar output — Support for fixed decimation rates
  only
- Vector input and vector output — Support for fixed decimation rates
  only

The block provides an architecture suitable for HDL code generation and hardware
deployment.

**Note**

You can also generate HDL code for this hardware-optimized algorithm, without creating a
Simulink® model, by using the DSP HDL IP Designer app. The app
provides the same interface and configuration options as the Simulink block.
