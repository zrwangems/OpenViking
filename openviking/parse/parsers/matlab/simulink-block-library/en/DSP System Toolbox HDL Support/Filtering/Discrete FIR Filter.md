---
type: simulink-block
title: 'Discrete FIR Filter'
family: 'hdlcoder'
product_id: 'dsp-system-toolbox-hdl-support'
product_name: 'DSP System Toolbox HDL Support'
documentation_release: R2025b
official_category: 'HDL Floating Point Operations'
documentation_page: 'discretefirfilter'
documentation_source_path: '../dsphdl/ref/discretefirfilter.html'
language: en
---

# Discrete FIR Filter

## Ports
```yaml
ports:
- name: data
  summary: Input data scalar | column vector | row vector
  direction: input
  data_types: fixed point | single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: valid
  summary: Indicates valid input data scalar
  direction: input
  data_types: Boolean
- name: coeff
  summary: Filter coefficients (Parallel interface) real or complex row vector
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: coeff
  summary: Filter coefficients (Memory interface) real or complex scalar
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | fixed point
- name: caddr
  summary: Filter coefficient address (Memory interface) scalar
  direction: input
  data_types: fixdt(0,N,0)
- name: cwren
  summary: Filter coefficients write enable (Memory interface) scalar
  direction: input
  data_types: Boolean
- name: cdone
  summary: Filter coefficient write complete (Memory interface) scalar
  direction: input
  data_types: Boolean
- name: reset
  summary: Clears internal states scalar
  direction: input
  data_types: Boolean
- name: data
  summary: Filtered output data scalar | column vector | row vector
  direction: output
  data_types: fixed point | single | double
- name: valid
  summary: Indicates valid output data scalar
  direction: output
  data_types: Boolean
- name: ready
  summary: Indicates block is ready for new input data scalar
  direction: output
  data_types: Boolean
```

### Input

### **data** — Input data scalar | column vector | row vector

Input data, specified as a scalar, column vector, or row
vector of real or complex values. Use a column vector to
increase throughput by processing samples in parallel.

You can use a row
vector, `[c1 c2 c3]`, to represent input
samples for multiple channels on a single cycle, or you
can provide scalar multichannel data with the channels
interleaved: `c1` data sample on cycle 1,
`c2` data sample on cycle 2,
`c3` data sample on cycle 3. The
channels can have independent filter coefficients.
 *(since R2023a)*

Waveform of row vector and scalar multichannel data signals.

*In R2023a and
R2023b: you can use multichannel row-vector input
only if there are at least as many invalid cycles
between inputs as there are channels. When the input
is a multichannel vector, the****Filter
structure*** *must be
set to* `Partly
serial
systolic`*, and****Number of
cycles*** *must be
equal to or greater than the number of channels.
This time allows the block to implement a
partly-serial architecture that shares resources
between the channels.*

Frame-based (column vector) input is not supported with
multichannel coefficients. To implement a high-throughput
multichannel filter, you can use a For Each block to
implement a high throughput filter for each channel. This
implementation cannot share resources between the
channels.

The size of the row or column vector must be less than or
equal to 64 elements. To implement a multichannel filter
with more than 64 channels, you must use interleaved
scalar input.

When the input data type is an integer type or a
fixed-point type, the block uses fixed-point arithmetic
for internal calculations and provides parameters on the
**Data Types** tab to customize the
data types. When the input data type is a floating-point
type, the block uses that input floating-point type for
internal calculations and the output data type.

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

### **coeff** — Filter coefficients (Parallel interface) real or complex row vector

Filter coefficients, specified as a row vector of real or
complex values. You can change the input coefficients at
any time. When you use scalar input data, the size of the
coefficient vector depends on the size and symmetry of the
sample coefficients specified in the
**Coefficients prototype**
parameter. The prototype specifies a sample coefficient
vector that is representative of the symmetry and
zero-valued locations of the expected input coefficients.
The block uses the prototype to optimize the filter by
sharing multipliers for symmetric or antisymmetric
coefficients, and by removing multipliers for zero-valued
coefficients. Therefore, provide only the nonduplicate
coefficients at the port. For example, if you set the
**Coefficients prototype**
parameter to a symmetric 14-tap filter, the block expects
a vector of 7 values on the **coeff**
input port. You must still provide zeros in the input
**coeff** vector for the
nonduplicate zero-valued coefficients.

When you use frame-based input data, the block does not
optimize the filter for coefficient symmetry. The block
still uses the **Coefficients prototype**
to remove multipliers for zero-valued coefficients. At the
**coeff** input port, specify a
vector that is the same size as the prototype.

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

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **coeff** — Filter coefficients (Memory interface) real or complex scalar

*Since R2023a*

Filter coefficients, specified as a real or complex scalar
value to write to internal memory. To load a single
coefficient value to internal memory, specify a
**coeff** value with a
corresponding address on the **caddr**
port and an enable signal on the
**cwren** port. You can change the
input coefficients at any time.

Waveform that shows writing a set of coefficients to the filter by using the memory interface

While you write new coefficients into memory, the block
ignores any input data, but still returns
`dataOut` with
`validOut` until it clears the
filter pipeline. The block resumes accepting input the
cycle after **cdone** is set to
`1` (`true`).

Waveform that shows the filter stops processing input data while receiving new coefficients on the memory interface

The
coefficient memory has the same number of addresses as the
size of the **Coefficients prototype**
parameter. The prototype specifies a sample coefficient
vector that is representative of the symmetry and
zero-valued locations of the expected input coefficients.
When
you use scalar input data, the block uses the prototype to
optimize the filter by sharing multipliers for symmetric
or antisymmetric coefficients, and by removing multipliers
for zero-valued coefficients.
You
must write the entire set of coefficients to memory,
including symmetric or zero-value coefficients. For
example, if you set the **Coefficients
prototype** parameter to a symmetric 14-tap
filter, you must write 14 values to the memory interface.

When you use frame-based input data, the block does not
optimize the filter for coefficient symmetry. The block
still uses the **Coefficients prototype**
parameter to remove multipliers for zero-valued
coefficients. The coefficient memory has the same number
of locations as the size of the prototype.

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
(Memory interface)`.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

### **caddr** — Filter coefficient address (Memory interface) scalar

*Since R2023a*

Specify the filter coefficient address as a scalar integer
value represented as an unsigned fixed-point type with
zero fractional bits. The block derives the size of this
integer value, and the size of the internal memory, from
the number of unique coefficients in the
**Coefficients prototype**
parameter value.

#### Dependencies

To enable this port, set **Coefficients
source** to `Input port
(Memory interface)`.

**Data Types:** `fixdt(0,N,0)`

### **cwren** — Filter coefficients write enable (Memory interface) scalar

*Since R2023a*

Set this input to `1`
(`true`) to write the value on the
**coeff** port into the
**caddr** location in internal
memory.

#### Dependencies

To enable this port, set **Coefficients
source** to `Input port
(Memory interface)`.

**Data Types:** `Boolean`

### **cdone** — Filter coefficient write complete (Memory interface) scalar

*Since R2023a*

Set this input to `1`
(`true`) to indicate that the
current port values write the final coefficient value to
memory.

#### Dependencies

To enable this port, set **Coefficients
source** to `Input port
(Memory interface)`.

**Data Types:** `Boolean`

### **reset** — Clears internal states scalar

Control signal that clears internal states. When
**reset** is `1`
(`true`), the block stops the
current calculation and clears internal states. When
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

### **data** — Filtered output data scalar | column vector | row vector

Filtered output data, returned as a scalar, column vector,
or row vector of real or complex values. The dimensions of
the output match the dimensions of the input. When the
input data type is a floating-point type, the output data
inherits the data type of the input data. When the input
data type is an integer type or a fixed-point type, the
**Output** parameter on the
**Data Types** tab controls the
output data type.

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

### **ready** — Indicates block is ready for new input data scalar

Control signal that indicates the block is ready for a new
input data sample on the next cycle. When **ready** is `1`
(`true`), you can specify the
**data** and **valid**  inputs for the next
time step. When **ready** is
`0` (`false`), the
block ignores any input data in the next time step.

When using the partly serial architecture, the block
processes one sample at a time. If your design waits for
this block to return **ready** set to `0`
(`false`) before setting the input
**valid** to
`0` (`false`),
then one additional cycle of input data arrives at the
port. The block stores this additional data while
processing the current data, and does not set **ready**  to
`1` (`true`) until
your model processes the additional input data.

#### Dependencies

To enable this port, set **Filter
structure** to `Partly serial
systolic`.

**Data Types:** `Boolean`
## Parameters
```yaml
parameters:
- name: Coefficient source
  summary: Source of filter coefficients Property (default) | Input port (Parallel interface) | Input port (Memory interface)
  group: Main
- name: Coefficients
  summary: Discrete FIR filter coefficients [0.5, 0.5] (default) | row vector | multichannel matrix
  group: Main
- name: Coefficients prototype
  summary: Prototype filter coefficients [] (default) | real or complex vector
  group: Main
- name: Filter structure
  summary: HDL filter architecture Direct form systolic (default) | Direct form transposed | Partly serial systolic
  group: Main
- name: Specify serialization factor as
  summary: Rule to define serial implementation Minimum number of cycles between valid input samples (default) | Maximum number
    of multipliers
  group: Main
- name: Number of cycles
  summary: Serialization requirement for input timing 2 (default) | positive integer
  group: Main
- name: Number of multipliers
  summary: Serialization requirement for resource usage 2 (default) | positive integer
  group: Main
- name: Optimize symmetric coefficients
  summary: Share multipliers for symmetric coefficients with frame-based input on (default) | off
  group: Main
- name: Rounding mode
  summary: Rounding mode for type-casting the output Floor (default) | Ceiling | Convergent | Nearest | Round | Zero
  group: Data Types
- name: Saturate on integer overflow
  summary: Overflow handling for type-casting the output off (default) | on
  group: Data Types
- name: Coefficients
  summary: 'Data type of discrete FIR filter coefficients Inherit: Same word length as input (default) | <data type expression>'
  group: Data Types
- name: Output
  summary: 'Data type of filter output Inherit: Inherit via internal rule (default) | Inherit: Same word length as input |
    <data type expression>'
  group: Data Types
- name: Enable reset input port
  summary: Option to enable reset input port off (default) | on
  group: Control Ports
- name: Use HDL global reset
  summary: Option to connect data path registers to generated HDL global reset signal off (default) | on
  group: Control Ports
- name: Coefficient multiplication
  summary: Coefficient multiplier implementation in hardware Multiplier (default) | CSD/Factored-CSD
  group: Implementation
- name: Use multiplier for +/- 1 and power of 2 coefficients
  summary: Special-value coefficient multiplier implementation in hardware on (default) | off
  group: Implementation
```

### Main

### **Coefficient source** — Source of filter coefficients `Property` (default) | `Input port (Parallel interface)` | `Input port (Memory interface)`

You can enter constant filter coefficients as a parameter,
provide time-varying filter coefficients by using an input
port, or provide time-varying coefficients by using a
memory-style interface.

You cannot use programmable coefficients with multichannel
data.

When you select `Input port (Parallel
interface)`, the
**coeff** port appears on the
block.

When you select `Input port (Memory
interface)`, a memory-style interface
appears on the block. This interface includes the
**coeff**,
**caddr**,
**cwren**, and
**cdone** ports.

Selecting `Input port (Parallel
interface)` or `Input port
(Memory interface)` enables the
**Coefficients prototype**
parameter. Specify a prototype to enable the block to
optimize the filter implementation according to the values
of the coefficients.

When you use programmable coefficients with frame-based
input, the block does not optimize the filter for
coefficient symmetry. Also, the output after a change of
coefficient values might not match the output in the
scalar case exactly. This difference occurs because the
subfilter calculations are performed at different times
relative to the input coefficient values, compared with
the scalar implementation.

#### Dependencies

*Before R2023b: To use
`Input port (Parallel
interface)`, set the **Filter
structure** parameter to
`Direct form systolic` or
`Direct form
transposed`.*

### **Coefficients** — Discrete FIR filter coefficients `[0.5, 0.5]` (default) | row vector | multichannel matrix

Discrete FIR filter coefficients, specified as a row
vector of real or complex values. You can specify
multichannel coefficients with a
*K*-by-*L* matrix
of real or complex values, where *K* is
the number of channels and *L* is the
filter length. To enable symmetry optimization, the
symmetry characteristics of all channels must align. For
example, if one channel is even-symmetric, all channels
must be even-symmetric.

You can also specify the coefficients as a workspace
variable or as a call to a filter design function. When
the input data type is a floating-point type, the block
casts the coefficients to the same data type as the input.
When the input data type is an integer type or a
fixed-point type, you can set the data type of the
coefficients on the **Data Types**
tab.

**Example:** `firpm(30,[0 0.1 0.2 0.5]*2,[1 1 0
0])`

#### Dependencies

To enable this parameter, set **Coefficients
source** to
`Property`.

### **Coefficients prototype** — Prototype filter coefficients `[]` (default) | real or complex vector

Prototype filter coefficients, specified as a vector of
real or complex values. The prototype specifies a sample
coefficient vector that is representative of the symmetry
and zero-valued locations of the expected input
coefficients. If all input coefficient vectors have the
same symmetry and zero-valued coefficient locations, set
**Coefficients prototype** to one
of those vectors. The block uses the prototype to optimize
the filter by sharing multipliers for symmetric or
antisymmetric coefficients, and by removing multipliers
for zero-valued coefficients.

When you use frame-based input data, the block does not
optimize the filter for coefficient symmetry. The block
still uses the **Coefficients prototype**
parameter to remove multipliers for zero-valued
coefficients.

| Coefficient Source | Input Size | If No Prototype |
| --- | --- | --- |
| `Input port (Parallel interface)` | When you use scalar input data, coefficient optimizations affect the expected size of the vector on the **coeff** port. Provide only the nonduplicate coefficients at the port. For example, if you set the **Coefficients prototype** parameter to a symmetric 14-tap filter, the block shares one multiplier between each pair of duplicate coefficients, so the block expects a vector of 7 values on the **coeff** port. You must still provide zeros in the input **coeff** vector for the nonduplicate zero-valued coefficients.  When you use frame-based input data, specify a **coeff** vector that is the same size as the prototype. | If your coefficients are unknown or not expected to share symmetry or zero-valued locations, you can set **Coefficients prototype** to `[]`. |
| `Input port (Memory interface)` | Write the same number of coefficient values as the size of the prototype. | **Coefficients prototype** cannot be empty. The block uses the prototype to determine the size of the coefficient memory. If your coefficients are unknown or not expected to share symmetry or zero-valued locations, set **Coefficients prototype** to a vector with the same length as your expected coefficients, which does not contain symmetry or zero values, for example `[1:1:NumCoeffs]`. |

#### Dependencies

To enable this parameter, set **Coefficients
source** to `Input port
(Parallel interface)` or
`Input port (Memory
interface)`.

### **Filter structure** — HDL filter architecture `Direct form systolic` (default) | `Direct form transposed` | `Partly serial systolic`

Specify the HDL filter architecture as one of these
structures:

- `Direct form
  systolic` — This architecture
  provides a fully parallel filter implementation
  that makes efficient use of Intel and AMD DSP blocks. For architecture
  details, see Fully Parallel Systolic Architecture. When you specify multichannel coefficients
  with this architecture (with interleaved input
  samples), the block interleaves the channel
  coefficients over a single parallel filter.
- `Direct form
  transposed` — This architecture is a
  fully parallel implementation that is suitable for
  FPGA and ASIC applications. For architecture
  details, see Fully Parallel Transposed Architecture. When you specify multichannel coefficients
  with this architecture (with interleaved input
  samples), the block interleaves the channel
  coefficients over a single parallel filter.
- `Partly serial
  systolic` — This architecture
  provides a serial filter implementation and
  options for tradeoffs between throughput and
  resource utilization. The architecture makes
  efficient use of Intel and AMD DSP blocks. The block implements a
  serial *L*-coefficient filter
  with *M* multipliers and requires
  input samples that are at least
  *N* cycles apart, such that
  *L* =
  *N*×*M*. You can
  specify either *M* or
  *N*. For this implementation, the
  block provides the output
  **ready** port which indicates
  when the block is ready for new input data. For
  architecture details, see Partly Serial Systolic Architecture (1 < N < L) and Fully Serial Systolic Architecture (N ≥ L). You cannot use frame-based input with the
  partly serial architecture.

  When you specify multichannel coefficients
  with a serial architecture, you must specify the
  serialization factor as the number of cycles
  between valid input samples.

  For multichannel input that is scalar and
  interleaved over the channels, the block
  implements these serial architectures:

  - When *N* <
    *L*: Partly serial filter with
    *L*/*N*
    multipliers.
  - When *N* >=
    *L*: Fully serial filter.

  For multichannel input that is a
  1-by-*K* vector, where
  *K* is the number of channels,
  the block implements these serial architectures:

  - When *N* = 1: Filter bank
    of fully parallel filters.
  - When 1
    < *N* <
    *K*: Filter bank of partly serial
    filters. *(since R2024a)*
  - When *N* =
    *K*: Fully parallel filter with
    channel coefficients interleaved.
  - When *K* <
    *N* <
    *L*×*K*: Partly
    serial filter with
    *L*×*K*/*N*
    multipliers.
  - When *N* >=
    *L*×*K*: Fully
    serial filter.

If any filter is symmetric, the architecture shares
multipliers for matching coefficients, so effectively
*L* becomes
`L/2`. To
enable the symmetry optimization for multichannel filters,
the symmetry characteristics of all channels must align.

All single-channel implementations remove multipliers for
zero-valued coefficients. Multichannel filters do not
optimize for zero-valued coefficients. The filter shares
multipliers for symmetric and antisymmetric coefficients.
Multichannel filters share resources between channels,
even if the filter coefficients are different across the
channels.

### **Specify serialization factor as** — Rule to define serial implementation `Minimum number of cycles between valid input samples` (default) | `Maximum number of multipliers`

You can specify the rule that the block uses to serialize
the filter as either:

- `Minimum number of cycles
  between valid input samples` —
  Specify a requirement for input data timing using
  the **Number of cycles**
  parameter.
- `Maximum number of
  multipliers` — Specify a requirement
  for resource usage using the **Number of
  multipliers** parameter. This option is
  not supported when you have multichannel
  coefficients.

For a filter with *L* coefficients, the
block implements a serial filter with not more than
*M* multipliers and requires input
samples that are at least *N* cycles
apart, such that *L* =
*N*×*M*. The block
might remove multipliers when it applies coefficient
optimizations, so the actual *M* or
*N* value of the filter
implementation might be lower than the specified
value.

If the filter is symmetric, the architecture shares
multipliers for matching coefficients, so effectively
`L =
L/2`.

When you use complex
input data and/or complex coefficients with a
single-channel partly serial architecture, the block
implements complex interleaving to share the multipliers
over inactive input cycles. For complex input and complex
coefficients, the block needs at least
*L*×3 cycles to implement the
filter with a single multiplier. For complex input with
real coefficients or complex coefficients with real input,
the block needs at least *L*×2 cycles to
implement the filter with a single multiplier.  *(since R2023b)*

#### Dependencies

To enable this parameter, set the **Filter
structure** parameter to
`Partly serial systolic`.

### **Number of cycles** — Serialization requirement for input timing `2` (default) | positive integer

Serialization requirement for input timing, specified as a
positive integer. This parameter represents
*N*, the minimum number of cycles
between valid input samples. In this case, the block
calculates *M* =
*L*/*N*. To
implement a fully serial architecture, set
**Number of cycles** to a value
greater than the filter length, *L*, or
to `Inf`. To implement a fully serial
architecture for a multichannel filter with
1-by-*K* vector input, set
**Number of cycles** to a value
greater than *L*×*K*,
where *K* is the number of channels.

To implement a fully serial architecture for a single
channel filter with complex input and complex
coefficients, set **Number of cycles**
greater than *L*×3. If you have complex
input with real coefficients or complex coefficients with
real input, set **Number of cycles**
greater than *L*×2.

If the filter is symmetric, the architecture shares
multipliers for matching coefficients, so effectively
`L =
L/2`. To enable the
symmetry optimization for multichannel filters, the
symmetry characteristics of all channels must align.

The block might remove multipliers when it applies
coefficient optimizations, so the actual
*M* and *N* values
of the filter can be lower than the value you
specified.

#### Dependencies

To enable this parameter, set **Filter
structure** to `Partly serial
systolic` and set **Specify
serialization factor as** to
`Minimum number of cycles between
valid input samples`.

### **Number of multipliers** — Serialization requirement for resource usage `2` (default) | positive integer

Serialization requirement for resource usage, specified as
a positive integer. This parameter represents
*M*, the maximum number of
multipliers in the filter implementation. In this case,
the block calculates *N* =
*L*/*M*. If the
input data is complex, the block allocates
`floor(M/2)`
multipliers for the real part of the filter and
`floor(M/2)`
multipliers for the imaginary part of the filter. To
implement a fully serial architecture, set
**Number of multipliers** to
`1`.

If the filter is symmetric, the architecture shares
multipliers for matching coefficients, so effectively
`L =
L/2`.

When you use complex input data and/or complex
coefficients with a single-channel partly serial
architecture, the block implements complex interleaving to
share the multipliers over inactive input cycles. For
complex input and complex coefficients, the block needs at
least *L*×3 cycles to implement the
filter with a single multiplier. For complex input with
real coefficients or complex coefficients with real input,
the block needs at least *L*×2 cycles to
implement the filter with a single multiplier.

The block might remove multipliers when it applies
coefficient optimizations, so the actual
*M* and *N* values
of the filter might be lower than the specified
value.

#### Dependencies

To enable this parameter, set the **Filter
structure** to `Partly serial
systolic`, and set **Specify
serialization factor as** to
`Maximum number of
multipliers`.

You cannot use this parameter when you specify
multichannel coefficients. Use the **Number
of cycles** parameter instead.

### **Optimize symmetric coefficients** — Share multipliers for symmetric coefficients with frame-based input on (default) | off

*Since R2025a*

Enable sharing multipliers across symmetric coefficients
in the polyphase filter architecture that is used when you
have frame-based input data. This optimization reduces
latency and halves the number of multipliers.

Polyphase decomposition of symmetric filter coefficients
does not result in symmetry in each polyphase branch. For
example, if the filter coefficients are `[1 2 3 4
4 3 2 1]`, after decomposition the
polyphase branches are `[1 3 4 2]` and
`[2 4 3 1]`. Symmetric pairs
optimization refactors the coefficients to restore
symmetry on the polyphase branches. The implementation
includes a pre-adder to combine output samples for the
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

### **Coefficients** — Data type of discrete FIR filter coefficients `Inherit: Same word length as input` (default) | `<data type expression>`

When the input is a fixed-point or integer type, the block
casts the filter coefficients using the rule or data type
in this parameter. The quantization rounds to the nearest
representable value and saturates on overflow. When the
input data type is a floating-point type, the block
ignores this parameter and all internal arithmetic uses
the same data type as the input.

The recommended setting for this parameter is
`Inherit: Same word length as
input`.

The block returns a warning or error if:

- The coefficients data type does not have
  enough fractional length to represent the
  coefficients accurately.
- The coefficients data type is unsigned and
  the coefficients include negative values.

#### Dependencies

To enable this parameter, set **Coefficients
source** to
`Property`.

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
coefficients (*L*), and is given by

`WF = WI +
WC +
ceil(log2(L))`.

When you specify a fixed set of coefficients, the actual
full-precision internal word length is usually smaller
than *WF*, because the coefficient values
limit the potential growth.

When you use programmable coefficients, the block cannot
calculate the dynamic range, and the internal data type is
always *WF*.

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

### Implementation

### **Coefficient multiplication** — Coefficient multiplier implementation in hardware `Multiplier` (default) | `CSD/Factored-CSD`

*Since R2023b*

By default, the block implements coefficient multipliers
using a hardware multiplier. Select
`CSD/Factored-CSD` to
replace coefficient multipliers with a CSD or factored-CSD
implementation. A CSD or factored-CSD implementation uses
shift and add operations rather than multipliers. When you
select CSD, coefficients of +/- 1 and power of 2 are also
implemented with shift logic.

The latency of the block does not change with multiplier
implementation. Each multiplier has the same number of
pipeline stages around it in either implementation.

#### Dependencies

To enable this parameter, set the **Filter
structure** parameter to
`Direct form transposed`.
Using CSD multipliers with systolic architecture is
not supported because it can prevent efficient use
of FPGA DSP blocks.

CSD implementations are not supported for
multichannel or programmable filters.

### **Use multiplier for +/- 1 and power of 2 coefficients** — Special-value coefficient multiplier implementation in hardware `on` (default) | `off`

*Since R2023b*

By default, the block implements special-value coefficient
multipliers using a hardware multiplier. Clear this check
box to replace special-value coefficient multipliers with
a shift implementation.

#### Dependencies

To enable this parameter, set **Filter
structure** to `Direct form
transposed`, and set
**Coefficient multiplication** to
`Multiplier`, or set
**Filter structure** to
`Direct form
systolic`.

CSD implementations are not supported for
multichannel or programmable filters.
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

**HDL Architecture**

You can set block parameters to make tradeoffs between throughput and
resource utilization.

- For highest throughput, choose a fully parallel
  systolic or transposed architecture. The generated
  code accepts input data and provides filtered output
  data on every cycle.
- For reduced area, choose partly serial systolic
  architecture. Then specify a rule that the block
  uses to serialize the filter based on either input
  timing or resource usage. To specify a serial filter
  using an input timing rule, set **Specify
  serialization factor as** to
  `Minimum number of cycles between
  valid input samples`, and set
  **Number of cycles** to a value
  greater than or equal to `2`.
  In this case, the filter accepts only input samples
  that are at least **Number of
  cycles** cycles apart. To specify a
  serial filter using a resource rule, set
  **Specify serialization factor
  as** to `Maximum number of
  multipliers`, and set
  **Number of multipliers** to a
  value less than the number of filter coefficients.
  In this case, the filter accepts input samples that
  are at least `NumCoeffs/NumMults`
  apart.

**HDL Block Properties**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | Number of registers to place at the outputs by moving existing delays within your design. Distributed pipelining does not redistribute these registers. The default is `0`. For more details, see ConstrainedOutputPipeline (HDL Coder). |
| **InputPipeline** | Number of input pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see InputPipeline (HDL Coder). |
| **OutputPipeline** | Number of output pipeline stages to insert in the generated code. Distributed pipelining and constrained output pipelining can move these registers. The default is `0`. For more details, see OutputPipeline (HDL Coder). |

**Restrictions**

The Discrete FIR Filter block does not support resource sharing optimization
through HDL Coder settings. Instead, set the **Filter
structure** parameter to `Partly serial
systolic`, and configure a serialization factor
based on either input timing or resource usage.

## Version History

**Introduced in R2017a**

### R2025a: Optimize symmetric coefficients for frame-based input

The block optimizes symmetric coefficient multipliers in the polyphase
filter architecture used with frame-based input. This optimization reduces
latency and halves the number of multipliers. To enable this optimization,
select **Optimize symmetric coefficients**.

### R2024a: Use multichannel vector input with fully parallel filters

The block supports multichannel vector input for `Direct form
systolic` and `Direct form
transposed` filter structures. The block also now
supports multichannel vector input for `Partly serial
systolic` filters with **Number of cycles**
less than the number of channels.

### R2023b: Multichannel optimization for symmetric filters

When you use multichannel input data, the block shares multipliers between
odd- or even-symmetric filter coefficients. To enable the symmetry
optimization, the symmetry characteristics of all channels must align. For
example, if one channel is even-symmetric, all channels must be
even-symmetric.

### R2023b: Partly serial FIR filter optimization for complex multipliers

When you use complex input data and/or complex coefficients with a
single-channel partly serial architecture, the block implements complex
interleaving to share the multipliers over inactive input cycles. This
optimization uses fewer multipliers and increases the latency of the filter.

For complex input and complex coefficients, the block needs at least
`NumCycles = 3*FilterLength` to implement the filter
with a single multiplier. For complex input with real coefficients or
complex coefficients with real input, the block needs at least
`NumCycles = 2*FilterLength` to implement the filter
with a single multiplier. The effective filter length is
`FilterLength/2` if the filter is symmetrical.

### R2023b: Programmable coefficients with serial architecture

The block supports using the parallel coefficients input port with the
`Partly serial systolic` architecture.

### R2023b: Canonical signed digit implementation

The block provides an option to replace coefficient multipliers with a CSD
or factored-CSD implementation when you use the `Direct form
transposed` architecture. A CSD or factored-CSD
implementation uses shift and add operations rather than multipliers. When
you use `Direct form systolic` or
`Direct form transposed`, you can optionally
replace multipliers with a shift implementation for coefficients that have
values equal to 1, -1, or a power of 2.

CSD implementations are not supported for multichannel or programmable
filters.

### R2023a: Load coefficients using memory-style interface

This block offers an optional memory-style interface to load coefficients.
To use this interface, set the **Coefficient source**
parameter to `Input port (Memory interface)`. You
can use this interface with any filter architecture.

### R2023a: Multichannel support

Specify coefficients as a K-by-L matrix, where K is the number of channels
and L is the filter length. You can supply input data as a K-by-1 row-vector
or as scalar input with the channels interleaved in time. The filter shares
resources between channels, even if the filter coefficients are different
across the channels. If the input data channels have enough cycles between
valid input samples, the block can implement the multichannel filter as a
single fully serial FIR filter. When the input is a multichannel vector, the
**Filter structure** must be set to
`Partly serial systolic`, and
**Number of cycles** must be equal to or greater than
the number of channels.

### R2022a: Moved to DSP HDL Toolbox from DSP System Toolbox

Before R2022a, this block was named Discrete FIR Filter HDL
Optimized and was included in the DSP System Toolbox™
**DSP System Toolbox HDL Support** library.

### R2022a: High-throughput interface

This block supports high-throughput data. You can apply input data as an
*N*-by-1 vector, where *N* can be up
to 64 values. You cannot use frame-based input with the partly serial
architecture.

### R2022a: Input coefficients must be a row vector

When you use programmable coefficients with this block, you must supply the
coefficients as a row vector (1-by-*N* matrix). Before
R2022a, the block accepted a one-dimensional array (for example,
`ones(5)`), a column vector
(*M*-by-1 matrix), or a row vector of coefficients.

### R2022a: RAM-based partly serial architecture

This block uses a RAM-based partly serial architecture, which uses fewer
resources than the former register-based architecture. Uninitialized RAM
locations can result in `X` values at the start of your HDL
simulation. You can avoid `X` values by having your test
initialize the RAM or by enabling the **Initialize all RAM
blocks** option in the model configuration parameters. This
parameter sets the RAM locations to `0` for simulation and
is ignored by synthesis tools. Another option to avoid transient effects
from uninitialized RAM locations is to hold reset for
*L*/*M* cycles, where
*L* is the number of coefficients and
*M* is the number of multipliers in the filter
implementation. This operation sets the RAM locations to zeros.

### R2019b: Complex coefficients

The block supports complex-valued coefficients. If both coefficients and
input data are complex, the block implements each filter tap with three
multipliers. If either data or coefficients are complex but not both, the
block uses two multipliers for each filter tap. You can use complex
coefficients with all architectures and with programmable
coefficients.

### R2019a: Programmable coefficients

The block provides the option to specify coefficients using an input port
when you select the `Direct form systolic`
architecture. You cannot use programmable coefficients with transposed or
partly serial systolic architectures.

### R2019a: Optimize symmetric coefficients

The block provides optimization of symmetric and antisymmetric coefficients.
This optimization reduces the number of multipliers and makes efficient use
of FPGA DSP resources.

In R2018b, the block performed these optimizations only for fully parallel
architectures.

### R2019a: Optional reset port

The block provides an optional reset port for any architecture, including a
serial systolic architecture with resource sharing. The
**reset** port provides a local synchronous reset of
the data path registers.

In R2018b, the block supported the **reset** port only for
fully parallel architectures.

### R2019a: Changes to serial filter parameters

Before R2019a, you specified the serial implementation by setting a
requirement for input timing. Starting in R2019a, you can specify the
serialization requirement based on either input timing or resource
usage.

For a filter with *L* coefficients, the block implements a
serial filter with not more than *M* multipliers and
requires input samples that are at least *N* cycles apart,
such that *L* = *N*×*M*.

| Serial Filter Requirement | Configuration Before R2019a | Configuration in R2019a |
| --- | --- | --- |
| Specify a serialization rule based on input timing, that is, *N* cycles. | - Set **Filter structure** to   `Direct form   systolic`. - Select **Share DSP   resources**. - Set **Sharing factor** to   *N*. | - Set the **Filter   structure** to `Partly serial   systolic`. - Set **Specify serialization factor   as** to `Minimum number of   cycles between valid input   samples`. - Set **Number of cycles** to   *N*. |
| Specify a serialization rule based on resource usage, that is, *M* multipliers. | Serialization by resource usage is not supported before R2019a. However, you can calculate *N* based on your multiplier requirement.  - Set **Filter structure** to   `Direct form   systolic`. - Select **Share DSP   resources**. - Set **Sharing factor** to   `ceil(NumCoeffs/M)`. | - Set the **Filter   structure** to `Partly serial   systolic`. - Set **Specify serialization factor   as** to `Maximum number of   multipliers`. - Set **Number of   multipliers** to   *M*. |

### R2018b: Transposed architecture

The block provides an option to select a direct form transposed
architecture.

### R2018b: Changes to parallel filter architecture

- The **validIn** port is mandatory. The
  **Enable valid input port** parameter is
  no longer available.
- The **ready** port is enabled when you select
  **Share DSP resources** and disabled when
  you clear **Share DSP resources**. The
  **Enable ready output port** parameter is
  no longer available.
- When you select `Direct form systolic`
  without **Share DSP resources** enabled, the
  block implements an improved fully parallel architecture
  compared to previous releases. This architecture might have
  different latency than in previous versions. Use the
  **validOut** signal to align with
  parallel delay paths. When using this architecture, the default
  global HDL reset now clears only the control path registers.
  Previous releases connected the global HDL reset to the data
  path registers and the control path registers. This change
  improves hardware performance and lowers the resources used. To
  implement the same fully parallel architecture as previous
  releases, select **Share DSP resources** and
  set **Sharing factor** to
  `1`.
- When you select `Direct form systolic`,
  select **Share DSP resources**, and use any
  **Sharing factor**, the implemented
  filter has the same latency and uses the same hardware resources
  as in previous releases. The reset behavior for this
  architecture is also the same as in previous releases.

## Description

Finite-impulse response filter

The Discrete FIR Filter block models finite-impulse response filter
architectures optimized for HDL code generation. The block accepts scalar or
frame-based input, supports multichannel input, and provides an option for
programmable coefficients by using a parallel interface or a memory interface. The
block provides a hardware-friendly interface with input and output control
signals. To provide a cycle-accurate simulation of the generated HDL code, the
block models architectural latency including pipeline registers and resource
sharing.

The block provides three filter structures.

- The direct form systolic architecture provides a fully parallel
  implementation that makes efficient use of Intel® and AMD® DSP blocks.
- The direct form transposed architecture is a fully parallel
  implementation and is suitable for FPGA and ASIC applications.
- The partly serial systolic architecture provides a configurable
  serial implementation that makes efficient use of FPGA DSP
  blocks.

For a filter implementation that matches multipliers, pipeline
registers, and pre-adders to the DSP configuration of your FPGA vendor, specify
your target device when you generate HDL code.

All single-channel filter structures remove multipliers for zero-valued
coefficients, such as in half-band filters and Hilbert transforms. The block also
provides an option to implement +/- 1 and power of 2 coefficients without a
multiplier, and an option to implement all coefficients with CSD or factored-CSD
logic. The filter shares multipliers for symmetric and antisymmetric coefficients.
Multichannel filters do not remove multipliers for zero-valued coefficients.
Multichannel filters share resources between channels, even if the filter
coefficients are different across the channels.

The
latency between valid input data and the corresponding valid output data depends
on the filter structure, serialization options, number of coefficients, and
whether the coefficient values provide optimization opportunities. For details of
structure and latency, see FIR Filter Architectures for FPGAs and ASICs.

**Note**

You can also generate HDL code for this hardware-optimized algorithm, without creating a
Simulink® model, by using the DSP HDL IP Designer app. The app
provides the same interface and configuration options as the Simulink block.
