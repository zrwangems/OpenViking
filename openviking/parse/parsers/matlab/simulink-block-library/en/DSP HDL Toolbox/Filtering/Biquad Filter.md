---
type: simulink-block
title: 'Biquad Filter'
family: 'dsp-system-toolbox-hdl-support'
product_id: 'dsphdl'
product_name: 'DSP HDL Toolbox'
documentation_release: R2025b
official_category: 'Filtering'
documentation_page: 'biquadfilter'
documentation_source_path: 'ref/biquadfilter.html'
language: en
---

# Biquad Filter

## Ports

### Input

### **data** — Input data scalar or column vector of real values

Input data, specified as a scalar or column vector of real values. When the input
has an integer or fixed-point data type, the block uses fixed-point arithmetic for
internal calculations.

Vector input is supported only when you set **Filter structure**
to `Pipelined feedback form`. The block accepts vectors of up
to 64 samples, but large vector sizes can make the calculation of internal data types
challenging. Vector sizes of up to 16 samples are practical for hardware
implementation.

When you set **Filter structure** to `Direct form I
fully serial`, the block has an output **ready**
signal that indicates when the block is ready for new input. You apply input data only
when the output **ready** signal is `1`
(`true`). Your design can react to the **ready**
signal to provide the next input sample, or you can space your input data with enough
cycles in between to process each sample. The block icon displays the cycles required
to process one sample.

The software supports `double` and
`single` data types for simulation, but not for HDL code generation.

**Data Types:** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **valid** — Indicates valid input data scalar

Control signal that indicates if the input data is valid. When
**valid** is `1` (`true`), the
block captures the values from the input **data** port. When
**valid** is `0` (`false`), the
block ignores the values from the input **data** port.

**Data Types:** `Boolean`
### Output

### **data** — Filtered output data scalar or column vector of real values

Filtered output data, returned as a scalar or column vector of real values. The
output dimensions match the input dimensions. When the input data type is a
floating-point type, the output data inherits the data type of the input data. When
the input data type is an integer type or a fixed-point type, the
**Output** parameter on the **Data Types** tab
controls the output data type.

**Data Types:** `fixed point` | `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **valid** — Indicates valid output data scalar

Control signal that indicates if the data from the output
**data** port is valid. When **valid** is
`1` (`true`), the block returns valid data from
the output **data** port. When **valid** is
`0` (`false`), the values from the output
**data** port are not valid.

**Data Types:** `Boolean`

### **ready** — Indicates block is ready for new input data scalar

Control signal that indicates the block is ready for new input data sample on the
next cycle. When **ready** is `1`
(`true`), you can specify the **data**
and **valid**  inputs for the next time step. When
**ready** is `0`
(`false`), the block ignores any input data in the next time step.

When using the fully serial architecture, the block processes one sample at a
time. If your design waits for this block to return **ready** set to `0` (`false`) before
setting the input **valid** to `0`
(`false`), then one additional cycle of input data arrives at the
port. The block stores this additional data while processing the current data, and
does not set **ready**  to `1`
(`true`) until your model processes the additional input
data.

#### Dependencies

To enable this port, set **Filter structure** to
`Direct form I fully serial`.

**Data Types:** `Boolean`

## Parameters

### Main

### **Filter structure** — HDL filter architecture `Direct form II` (default) | `Direct form II transposed` | `Pipelined feedback form` | `Direct form I fully serial`

Both the `Direct form II` and `Direct form II
transposed` architectures are pipelined and quantized to fit well into
FPGA DSP blocks. The output of these filters matches the output of the DSP System Toolbox™ System objects `dsp.SOSFilter`
and `dsp.FourthOrderSectionFilter`. These architectures minimize the number of
multipliers used by the filter but have a critical path through the feedback loop and
sometimes cannot achieve higher clock rates. These architectures do not support vector
input.

`Pipelined feedback form` implements a pipelined
architecture that uses more multipliers than either direct-form II structure, but
achieves higher clock rates after synthesis. Vector input is supported only when you
use `Pipelined feedback form`. The output of the pipelined
filter is slightly different than the DSP System Toolbox functions `dsp.SOSFilter`
and `dsp.FourthOrderSectionFilter` because of the timing of data samples applied
in the pipelined filter stages.

`Direct form I fully serial` implements a fully serial
architecture that uses only one multiplier. When you select this option, the block
stores the numerator, denominator, and scale values in the same ROM. You can control
the data type of the ROM by using the **Coefficients** data type
parameter. When you select this architecture, the output **ready**
port appears on the block. The **ready** signal indicates when the
block is ready for new input data. Apply input data only when
**ready** is `1` (`true`). This
architecture does not support vector input.

### **Numerator coefficients of filter** — Coefficients for numerator `[1,2,1]` (default) | *NumSections*-by-3 matrix

Specify the numerator coefficients as a matrix of
*NumSections*-by-3 values. *NumSections* is the
number of second-order filter sections. The block infers the number of filter sections
from the size of the numerator and denominator coefficients. The numerator coefficient
and denominator coefficient matrices must be the same size. The default filter has one
section.

### **Denominator coefficients of filter** — Coefficients for denominator `[1,.1,.2]` (default) | *NumSections*-by-3 matrix

Specify the denominator coefficients as a matrix of
*NumSections*-by-3 values. The block assumes the first denominator
coefficient of each section is `1.0`. *NumSections*
is the number of second-order filter sections. The block infers the number of sections
from the size of the numerator and denominator coefficients. The numerator coefficient
and denominator coefficient matrices must be the same size. The default filter has one
section.

### **Scale values of filter** — Gain values applied before and after second-order filter sections `[1]` (default) | vector of 1 to *NumSections*+1 values

Specify the gain values as a vector of up to *NumSections*+1
values. *NumSections* is the number of second-order filter sections.
The block infers the number of sections from the size of the numerator and denominator
coefficients. If the vector has only one value, the block applies that gain before the
first section. If you specify fewer values than there are filter sections, the block
sets the remaining section gain values to one. The diagram shows a 3-section filter
and the locations of the four scale values before and after the sections.

Implementing these gain factors outside the filter sections reduces the
multipliers needed to implement the numerator of the filter.

### Data Types

### **Rounding mode** — Rounding mode for type-casting the output `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Zero`

Rounding mode for type-casting the output and accumulator values to the data types
specified by the **Output** and **Accumulator**
parameters. When the input data type is floating point, the block ignores this
parameter. For more details, see Rounding Modes.

### **Saturate on integer overflow** — Overflow handling for type-casting the output `off` (default) | `on`

Overflow handling for type-casting the output and accumulator values to the data
types specified by the **Output** and
**Accumulator** parameters. When the input data type is floating
point, the block ignores this parameter. For more details, see Overflow Handling.

### **Numerator** — Data type of numerator coefficients `Inherit: Same word length as input` (default) | `<data type expression>`

The block casts the numerator coefficients to this data type. The quantization
rounds to the nearest representable value and saturates on overflow. When the input
data type is floating point, the block ignores this parameter.

The block returns a warning if the data type of the coefficients does not have
enough fractional length to represent the coefficients accurately.

#### Dependencies

To enable this parameter, set **Filter structure** to
`Direct form II transposed`, `Direct form
II`, or `Pipelined feedback form`.

### **Denominator** — Data type of denominator coefficients `Inherit: Same word length as input` (default) | `<data type expression>`

The block casts the denominator coefficients to this data type. The quantization
rounds to the nearest representable value and saturates on overflow. When the input
data type is floating point, the block ignores this parameter.

The block returns a warning if the data type of the coefficients does not have
enough fractional length to represent the coefficients accurately.

#### Dependencies

To enable this parameter, set **Filter structure** to
`Direct form II transposed`, `Direct form
II`, or `Pipelined feedback form`.

### **ScaleValues** — Data type of gain `Inherit: Same word length as input` (default) | `<data type expression>`

The block casts the scale values to this data type. The quantization rounds to the
nearest representable value and saturates on overflow. When the input data type is
floating point, the block ignores this parameter.

#### Dependencies

To enable this parameter, set **Filter structure** to
`Direct form II transposed`, `Direct form
II`, or `Pipelined feedback form`.

### **Coefficients** — Data type of coefficient memory when using serial filter architecture `Inherit: Same word length as input` (default) | `<data type expression>`

The block casts the numerator, denominator, and scale values to this data type and
stores them in an eight-element memory of this word length. The quantization rounds to
the nearest representable value and saturates on overflow. When the input data type is
floating point, the block ignores this parameter.

#### Dependencies

To enable this parameter, set **Filter structure** to
`Direct form I fully serial`.

### **Accumulator** — Data type of accumulator signals within each section `Inherit: Same as first input` (default) | `<data type expression>`

The block casts the internal accumulator signals (as indicated in the diagrams in
the Algorithms section) to this
data type. The quantization uses the settings of the **Rounding
mode** and **Saturate on integer overflow** parameters.
When the input data type is floating point, the block ignores this parameter.

### **Output** — Data type of filter output `Inherit: Inherit via internal rule` (default) | `Inherit: Same as first input` | `<data type expression>`

The block casts the output of the filter to this data type. The quantization uses
the settings of the **Rounding mode** and **Saturate on
integer overflow** parameters. When the input data type is floating point,
the block ignores this parameter.

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

### R2023a: Minimum resource architecture

The block now has the option to set the **Filter structure** parameter
to `Direct form I fully serial` to implement a fully serial
architecture that uses only one multiplier. When you select this option, the block stores
the numerator, denominator, and scale values in the same ROM, and you can control the data
type of the ROM by using the **Coefficient** data type parameter. When you
select this architecture, the block has an output **ready** signal that
indicates when the block is ready for new input. You can apply input data only when the
output **ready** signal is `1`
(`true`).

## Description

Biquadratic IIR (SOS) filter

A biquad filter is a form of infinite-impulse response (IIR) filter where the numerator
and denominator are split into a series of second-order sections connected by gain blocks.
This type of filter can replace a large FIR filter that uses an impractical amount of hardware
resources. Designs often use biquad filters as DC blocking filters or to meet a specification
originally implemented with an analog filter, such as a pre-emphasis filter.

**Note**

You can also generate HDL code for this hardware-optimized algorithm, without creating a
Simulink® model, by using the DSP HDL IP Designer app. The app
provides the same interface and configuration options as the Simulink block.
