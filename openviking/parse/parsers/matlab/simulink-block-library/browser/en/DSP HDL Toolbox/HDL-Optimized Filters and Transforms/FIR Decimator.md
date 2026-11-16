---
type: simulink-block
title: 'FIR Decimator'
family: 'dsphdl'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized Filters and Transforms'
documentation_page: 'firdecimator'
documentation_source_path: 'ref/firdecimator.html'
language: en
---

# FIR Decimator

## Ports

### Input

### **data** — Input data scalar | vector

Input data must be a real- or complex-valued scalar or
vector. When you use vector input and the vector size is
less than the decimation factor, the decimation factor
must be an integer multiple of the vector size. When you
use vector input and the vector size is greater than the
decimation factor, the vector size must be an integer
multiple of the decimation factor. The vector size must be
less than or equal to 64.

When the input data type is an integer type or a
fixed-point type, the block uses fixed-point arithmetic
for internal calculations.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
**Complex Number Support:** Yes

### **valid** — Indicates valid input data scalar

Control signal that indicates if the input data is valid.
When **valid** is `1`
(`true`), the block captures the
values from the input **data** port. When
**valid** is `0`
(`false`), the block ignores the
values from the input **data**
port.

**Data Types:** `Boolean`

### **coeff** — Filter coefficients real or complex row vector

*Since R2025a*

Filter coefficients, specified as a row vector of real or
complex values. You can change the input coefficients at
any time. The size of the coefficient vector must match
the size of the sample coefficients specified in the
**Coefficients prototype**
parameter. The prototype specifies a sample coefficient
vector that is representative of the
zero-valued locations of the expected
input coefficients. The block uses the prototype to
optimize the filter
by
removing multipliers for zero-valued coefficients.

If the input **data** is a fixed-point
type, the **coeff** values must also be
of a fixed point type. If the input
**data** is a floating-point data
type, the **coeff** values must be of the
same data type.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

#### Dependencies

To enable this port, set **Coefficients
source** to `Input port
(Parallel interface)`.

**Data Types:** `fixed point` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `single` | `double`

### **reset** — Clears internal states scalar

Control signal that clears internal states. When
**reset** is `1`
(`true`), the block stops the
current calculation and clears internal states. When the
**reset** is `0`
(`false`) and the input
**valid** is `1`
(`true`), the block captures data
for processing.

For more reset considerations, see the Reset Signal section on the Hardware Control Signals page.

#### Dependencies

To enable this port, on the **Control
Ports** tab, select **Enable
reset input port**.

**Data Types:** `Boolean`
### Output

### **data** — Filtered output data scalar

Filtered output data, returned as a real- or
complex-valued scalar. When the input data type is a
floating-point type, the output data inherits the data
type of the input data. When the input data type is an
integer type or a fixed-point type, the
**Output** parameter on the
**Data Types** tab specifies the
output data type.

The output **valid** signal indicates
which samples are valid after decimation. When the input
vector size is greater than the decimation factor, the
output is a vector of
*VectorSize*/*DecimationFactor*
samples.

**Data Types:** `fixed point` | `single` | `double`
**Complex Number Support:** Yes

### **valid** — Indicates valid output data scalar

Control signal that indicates if the data from the output
**data** port is valid. When
**valid** is `1`
(`true`), the block returns valid
data from the output **data** port. When
**valid** is `0`
(`false`), the values from the
output **data** port are not
valid.

**Data Types:** `Boolean`

## Parameters

### Main

### **Coefficient source** — Source of filter coefficients `Property` (default) | `Input port (Parallel interface)`

*Since R2025a*

You can enter constant filter coefficients as a parameter
or provide time-varying filter coefficients by using an
input
port.

When you select `Input port (Parallel
interface)`, the
**coeff** port appears on the
block.

Selecting `Input port (Parallel
interface)`
enables the **Coefficients prototype**
parameter. Specify a prototype to enable the block to
optimize the filter implementation according to the values
of the coefficients.

When you use programmable coefficients with frame-based
input, the output after a change of coefficient values
might not match the output in the scalar case exactly.
This difference occurs because the subfilter calculations
are performed at different times relative to the input
coefficient values, compared with the scalar
implementation.

### **Coefficients** — FIR filter coefficients `fir1(35,0.4)` (default) | real- or complex-valued vector

FIR filter coefficients, specified as a real- or
complex-valued vector. You can specify the vector as a
workspace variable or as a call to a filter design
function. When the input data type is a floating-point
type, the block casts the coefficients to the same data
type as the input. When the input data type is an integer
type or a fixed-point type, set the data type for the
coefficients on the **Data Types**
tab.

**Example:** `firpm(30,[0 0.1 0.2 0.5]*2,[1 1 0
0])` defines coefficients using a
linear-phase filter design function.

#### Dependencies

To enable this parameter, set **Coefficients
source** to
`Property`.

**Complex Number Support:** Yes

### **Coefficients prototype** — Prototype filter coefficients `[]` (default) | real or complex vector

*Since R2025a*

Prototype filter coefficients, specified as a vector of
real or complex values. The prototype specifies a sample
coefficient vector that is representative of the
zero-valued locations of the expected
input coefficients. If all input coefficient vectors have
the same zero-valued coefficient
locations, set **Coefficients prototype**
to one of those vectors. The block uses the prototype to
optimize the filter
by
removing multipliers for zero-valued coefficients.

#### Dependencies

To enable this parameter, set **Coefficients
source** to `Input port
(Parallel
interface)`.

### **Filter structure** — HDL filter architecture `Direct form systolic` (default) | `Direct form transposed`

The block implements a polyphase decomposition filter by
using Discrete FIR
Filter  blocks. Both structures share
resources by interleaving the subfilter coefficients over
one filter implementation for each sample in the input
vector. Specify the HDL filter architecture as one of
these structures:

- `Direct form
  systolic` — This architecture
  provides a parallel or partly serial filter
  implementation that makes efficient use of
  Intel and Xilinx DSP blocks. For a partly serial
  implementation, specify a value greater than 1 for
  the **Minimum number of cycles between
  valid input samples** parameter. You
  cannot use frame-based input with the
  partly serial architecture.

  When **Minimum number of cycles
  between valid input samples** is greater
  than 1, the block chooses a filter architecture
  that results in the fewest multipliers. If
  *N* allows for a single
  multiplier in each subfilter, then the block
  implements a single serial filter and decimates
  the output samples.
- `Direct form
  transposed` — This architecture is a
  fully parallel implementation that is suitable for
  FPGA and ASIC applications.

All implementations share resources by interleaving the
subfilter coefficients over one filter implementation for
each sample in the input vector.

The block implements a polyphase decomposition filter
using Discrete FIR
Filter  blocks. For architecture details,
see FIR Filter Architectures for FPGAs and ASICs.

### **Decimation factor** — Decimation factor 2 (default) | integer greater than two

Specify an integer decimation factor greater than two.
When you use vector input and the vector size is less than
the decimation factor, the decimation factor must be an
integer multiple of the vector size. When you use vector
input and the vector size is greater than the decimation
factor, the vector size must be an integer multiple of the
decimation factor.

### **Minimum number of cycles between valid input samples** — Serialization requirement for input timing `1` (default) | positive integer

Serialization requirement for input timing, specified as a
positive integer. This parameter represents
*N*, the minimum number of cycles
between valid input samples. To implement a fully serial
architecture, set **Minimum number of cycles
between valid input samples** greater than
the filter length, *L*, or to
`Inf`.

The block applies coefficient optimizations before
serialization, so the sharing factor of the final filter
can be lower than the number of cycles that you specified.

#### Dependencies

To enable this parameter, set **Filter
structure** to `Direct form
systolic`.

You cannot use frame-based input with
**Minimum number of cycles between valid
input samples** greater than 1.

### **Optimize symmetric coefficients** — Share multipliers for symmetric coefficients on (default) | off

*Since R2024b*

Enable sharing multipliers across symmetric coefficients
in the polyphase filter architecture. This optimization
reduces latency and halves the number of
multipliers.

Polyphase decomposition of symmetric filter coefficients
does not result in symmetry in each polyphase branch. For
example, if the filter coefficients are `[1 2 3 4
4 3 2 1]`, after decomposition the two
polyphase branches are `[1 3 4 2]` and
`[2 4 3 1]`. Symmetric pairs
optimization refactors the coefficients to restore
symmetry on the polyphase branches. The implementation
includes a pre-adder to combine input samples for the
refactored polyphase branches. The filter output is the
same as the output of the non-optimized implementation.

### Data Types

### **Rounding mode** — Rounding mode for type-casting the output `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

Rounding mode for type-casting the output to the data type
specified by the **Output** parameter.
When the input data type is floating point, the block
ignores this parameter. For more details, see Rounding Modes.

### **Saturate on integer overflow** — Overflow handling for type-casting the output `off` (default) | `on`

Overflow handling for type-casting the output to the data
type specified by the **Output**
parameter. When the input data type is floating point, the
block ignores this parameter. For more details, see Overflow Handling.

### **Coefficients** — Data type of filter coefficients `Inherit: Same word length as input` (default) | `<data type expression>`

When the input is a fixed-point or integer type, the block
casts the filter coefficients using the rule or data type
in this parameter. The quantization rounds to the nearest
representable value and saturates on overflow. When the
input data type is a floating-point type, the block
ignores this parameter and all internal arithmetic uses
the same data type as the input.

The recommended data type for this parameter is
`Inherit: Same word length as
input`.

The block returns a warning or error if:

- The coefficients data type does not have
  enough fractional length to represent the
  coefficients accurately.
- The coefficients data type is unsigned, and
  the coefficients include negative values.

### **Output** — Data type of filter output `Inherit: Inherit via internal rule` (default) | `Inherit: Same word length as input` | `<data type expression>`

When the input is a fixed-point or integer type, the block
casts the output of the filter using the rule or data type
in this parameter. The quantization uses the settings of
the **Rounding mode** and
**Overflow mode** parameters. When
the input data type is floating point, the block ignores
this parameter and returns output in the same data type as
the input.

The block increases the word length for full precision
inside each filter tap and casts the final output to the
specified type. The maximum final internal data type
(*WF*) depends on the input data
type (*WI*), the coefficient data type
(*WC*), and the number of
coefficients (*L*) and is given by

`WF = WI +
WC +
ceil(log2(L))`.

Because the coefficient values limit the potential growth,
usually the actual full-precision internal word length is
smaller than *WF*.

### Control Ports

### **Enable reset input port** — Option to enable reset input port `off` (default) | `on`

Select this check box to enable the **reset** input port. The
reset signal implements a local synchronous reset of the data path
registers.

For more reset considerations, see the Reset Signal section on
the Hardware Control Signals
page.

### **Use HDL global reset** — Option to connect data path registers to generated HDL global reset signal `off` (default) | `on`

Select this check box to connect the generated HDL global reset signal to the
data path registers. This parameter does not change the appearance of the block
or modify simulation behavior in Simulink. When you clear this check box, the generated HDL global reset
clears only the control path registers. The generated HDL global reset can be
synchronous or asynchronous depending on the **HDL Code Generation** > **Global Settings** > **Reset type** parameter in the model Configuration Parameters.

For more reset considerations, see the Reset Signal section on
the Hardware Control Signals
page.

## Libraries

DSP HDL Toolbox / Filtering

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

This block supports C/C++ code generation for Simulink accelerator and rapid accelerator modes and for DPI component generation.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

HDL Coder™ provides additional configuration options that affect HDL
implementation and synthesized logic.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Restrictions**

The FIR Decimator block does not support resource sharing optimization
through HDL Coder settings. Instead, set the **Filter
structure** parameter to `Partly serial
systolic`, and configure a serialization factor
based on either input timing or resource usage.

## Version History

**Introduced in R2020b**

### R2025a: Programmable coefficients

The block provides an optional **coeff** port to allow
coefficient changes at any time. Set the **Coefficient
source** parameter to `Input port (Parallel
interface)`, and specify the filter coefficients as a row
vector of real or complex values.

You can set the **Coefficients prototype** property to
indicate the locations of consistently zero-valued coefficients, such as, if
all input coefficients are half-band filters. When given a prototype, the
block removes multipliers for zero-valued coefficients.

### R2024b: Optimize symmetric coefficients

Use the **Optimize symmetric coefficients** parameter to
enable optimizing symmetric coefficient multipliers in the polyphase filter
architecture. This optimization reduces latency and halves the number of
multipliers.

### R2022a: Moved to DSP HDL Toolbox from DSP System Toolbox

Before R2022a, this block was named FIR Decimation HDL
Optimized and was included in the DSP System Toolbox
**DSP System Toolbox HDL Support** library.

### R2022a: Serial systolic architecture

This block supports partly and fully serial systolic architecture. This
architecture enables you to share hardware resources if there is a regular
pattern of invalid cycles between valid input samples. To use the serial
systolic architecture, set **Filter structure** to
`Direct form systolic` and **Minimum
number of cycles between valid input samples** to a value
greater than 1. You cannot use frame-based input with the serial
architecture.

### R2022a: Input vector size can be greater than decimation factor

In previous releases, the block did not support input vector sizes greater
than the decimation factor.

## Description

Finite impulse response (FIR) decimation filter

The FIR Decimator block implements a single-rate polyphase FIR
decimation filter that is optimized for HDL code generation. The block provides a
hardware-friendly interface with input and output control signals. To provide a
cycle-accurate simulation of the generated HDL code, the block models
architectural latency including pipeline registers and resource sharing.

The block accepts scalar or vector input. When you use vector input and the vector
size is less than the decimation factor, the decimation factor must be an integer
multiple of the vector size. In this case, the output is scalar and an output
valid signal indicates which samples are valid after decimation. The output data
is valid every *DecimationFactor*/*VectorSize*
samples. The waveform shows an input vector of four samples and a decimation
factor of eight. The output data is a scalar that is valid every second
cycle.

Logic Analyzer waveform showing the input and output signals of the FIR Decimator block with the configuration described above

When you use vector input and the vector size is greater than the decimation
factor, the vector size must be an integer multiple of the decimation factor. In
this case, the output is a vector of
*VectorSize*/*DecimationFactor* samples.
The waveform shows an input vector of eight samples and a decimation factor of
four. The output data is a vector of two samples on every cycle.

Logic Analyzer waveform showing the input and output signals of the FIR Decimator block with the configuration described above

The block provides two filter structures. The direct form systolic architecture
provides an implementation that makes efficient use of Intel® and Xilinx® DSP blocks. This architecture can be fully parallel or serial. To
use a serial architecture, the input samples must be spaced out with a regular
number of invalid cycles between the valid samples. The direct form transposed
architecture is a fully parallel implementation that is suitable for FPGA and ASIC
applications. For a filter implementation that matches multipliers, pipeline
registers, and pre-adders to the DSP configuration of your FPGA vendor, specify
your target device when you generate HDL code.

All filter structures optimize hardware resources by sharing multipliers for
symmetric or antisymmetric filters and by removing the multipliers for zero-valued
coefficients such as in half-band filters and Hilbert transforms.

The block implements one filter for each sample in the input vector. The block
then shares this filter between the polyphase subfilters by interleaving the
subfilter coefficients in time.

**Note**

You can also generate HDL code for this hardware-optimized algorithm, without creating a
Simulink® model, by using the DSP HDL IP Designer app. The app
provides the same interface and configuration options as the Simulink block.
