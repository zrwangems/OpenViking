---
type: simulink-block
title: 'PN Sequence Generator'
family: 'communications-toolbox-hdl-support'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Comm Sources'
documentation_page: 'pnsequencegenerator'
documentation_source_path: '../comm/ref/pnsequencegenerator.html'
language: en
---

# PN Sequence Generator

## Ports
```yaml
ports:
- name: Mask
  summary: Output mask binary vector
  direction: input
  data_types: double | uint8 | ufix1
- name: oSiz
  summary: Output size integer
  direction: input
  data_types: double
- name: Ref
  summary: Reference input column vector
  direction: input
  data_types: double
- name: Rst
  summary: Reset sequence generator 0 | 1
  direction: input
  data_types: Boolean
- name: Out
  summary: Pseudorandom noise sequence binary vector
  direction: output
```

### Input

### **Mask** — Output mask binary vector

Output mask to delay the PN sequence from initial time, specified as a binary
vector with *N* elements. *N* is the degree of the
generator polynomial.

#### Dependencies

To enable this port, set **Output mask
source** to `Input port`.

**Data Types:** `double` | `uint8` | `ufix1`

### **oSiz** — Output size integer

Output size for variable-size output signals, specified as an integer. For
information about variable-size signals, see Variable-Size Signal Basics (Simulink).

#### Dependencies

To enable this port, select **Output
variable-size signals** and set **Maximum
output size source** to `Dialog
parameter`.

**Data Types:** `double`

### **Ref** — Reference input column vector

Reference input, specified as a column vector that determines the maximum and
current output sequence length. The **Ref** input must be a variable-size
signal. For information about variable-size signals, see Variable-Size Signal Basics (Simulink).

#### Dependencies

To enable this port, select **Output
variable-size signals** and set **Maximum
output size source** to `Inherit from reference
input`.

**Data Types:** `double`

### **Rst** — Reset sequence generator 0 | 1

Reset sequence generator, specified as `0` or
`1`. For more information, see Reset Behavior.

#### Dependencies

To enable this port, select **Reset on nonzero
input**.

**Data Types:** `Boolean`
### Output

### **Out** — Pseudorandom noise sequence binary vector

PN sequence, returned as a binary vector. The data type of the output is specified
by **Output data
type**.
## Parameters
```yaml
parameters:
- name: Generator polynomial
  summary: Generator polynomial 'z^6 + z + 1' (default) | character vector | string scalar | binary row vector | integer vector
  group: ''
- name: Initial states
  summary: Initial shift register states [0 0 0 0 0 1] (default) | binary row vector
  group: ''
- name: Output mask source
  summary: Output mask source Dialog parameter (default) | Input port
  group: ''
- name: Output mask vector (or scalar shift value)
  summary: Output mask vector or scalar shift value 0 (default) | integer scalar | binary vector
  group: ''
- name: Output variable-size signals
  summary: Option to output variable-length signals off (default) | on
  group: ''
- name: Sample time
  summary: Output sample time 1 (default) | -1 | positive scalar
  group: ''
- name: Samples per frame
  summary: Samples per frame 1 (default) | positive integer
  group: ''
- name: Maximum output size source
  summary: Maximum output size source Dialog parameter (default) | Inherit from reference port
  group: ''
- name: Maximum output size
  summary: Maximum output size [10 1] (default) | vector of the form [*n* 1]
  group: ''
- name: Reset on nonzero input
  summary: Reset on nonzero input off (default) | on
  group: ''
- name: Enable bit-packed outputs
  summary: Enable bit-packed outputs off (default) | on
  group: ''
- name: Number of packed bits
  summary: Number of packed bits 8 (default) | integer in the range [1, 32]
  group: ''
- name: Interpret bit-packed values as signed
  summary: Interpret bit-packed values as signed off (default) | on
  group: ''
- name: Output data type
  summary: Output data type double (default) | boolean | Smallest unsigned integer
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Generator polynomial** — Generator polynomial `'z^6 + z + 1'` (default) | character vector | string scalar | binary row vector | integer vector

Generator polynomial that determines the feedback connections of the shift register,
specified as one of these options:

- Character vector or string scalar of a polynomial whose constant term is
  `1`. For more information, see Representation of Polynomials in Communications Toolbox.
- Binary-valued row vector that represents the coefficients of the polynomial in
  order of descending powers. The length of this vector must be *N*
  + 1, where *N* is the degree of the polynomial. The first and
  last entries must be `1`, indicating the leading term with degree
  *N* and a constant term of 1.
- Integer-valued row vector of elements that represent the exponents for the
  nonzero terms of the polynomial in order of descending powers. The last entry must
  be `0`, indicating a constant term of 1.

For more information, see Simple Shift Register Generator and Polynomial Order and Shift Register Orientation.

**Example:** `'z^8 + z^2 + 1'`, `[1 0 0 0 0 0 1 0 1]`,
and `[8 2 0]` represent the same polynomial,
*p*(*z*) = *z*
8 + *z*
2 + 1.

### **Initial states** — Initial shift register states `[0 0 0 0 0 1]` (default) | binary row vector

Initial shift register states of the PN sequence generator when the simulation
starts, specified as a binary-valued row vector. The length of the vector must equal the
degree of the generator polynomial specified by the **Generator
polynomial**. For more information, see Simple Shift Register Generator and Polynomial Order and Shift Register Orientation.

**Note**

For the block to generate a nonzero sequence, the **Initial
states** vector must contain at least one nonzero element.

### **Output mask source** — Output mask source `Dialog parameter` (default) | `Input port`

Output mask source that indicates how the output mask information is given to the
block, specified as one of these:

- `Dialog parameter` to use the `Output
  mask vector (or scalar shift value)` parameter setting.
- `Input port` to add and use the
  `Mask` input port.

### **Output mask vector (or scalar shift value)** — Output mask vector or scalar shift value 0 (default) | integer scalar | binary vector

Output mask vector or scalar shift value, specified as an integer scalar or binary
row vector of length *N*, where *N* is the degree of
the generator polynomial. This parameter determines the delay of the PN sequence from
the initial time. For more information, see Shifting PN Sequence Starting Point.

#### Dependencies

To enable this parameter, set **Output mask
source** to `Dialog parameter`.

### **Output variable-size signals** — Option to output variable-length signals `off` (default) | `on`

Select this parameter to enable variable-length output sequences during simulation.
When you clear this parameter, the block outputs fixed-length sequences. When you select
this parameter, the block can output variable-length sequences. For information about
variable-size signals, see Variable-Size Signal Basics (Simulink).

### **Sample time** — Output sample time `1` (default) | -1 | positive scalar

Positive scalars specify the time in seconds between each
sample of the output signal. If you set the sample time to `-1`, the output
signal inherits the sample time from downstream. For information on the relationship between the
**Sample time** and **Samples per frame** parameters,
see
Sample Timing.

**Example:** `1` specifies a sample time of 1 second.

#### Dependencies

To enable this parameter, clear **Output
variable-size signals**.

### **Samples per frame** — Samples per frame `1` (default) | positive integer

Samples per frame in one channel of the output signal, specified as a positive
integer. For information on the relationship between **Sample time**
and **Samples per frame**, see Sample Timing.

#### Dependencies

To enable this parameter, clear **Output variable-size
signals**.

### **Maximum output size source** — Maximum output size source `Dialog parameter` (default) | `Inherit from reference port`

Select how to specify the maximum sequence output size.

- `Dialog parameter` — Select this value to
  configure the block to use the **Maximum output size**
  parameter setting as the maximum permitted output sequence length. The
  **oSiz** input port specifies the current size of the
  output signal, and the block output inherits the sample time from the input
  signal. The input value of **oSiz** must be less than or
  equal to the **Maximum output size** parameter.
- `Inherit from reference port` — Select this value
  to enable the **Ref** input port and configure the block to
  inherit the sample time, maximum size, and current output size from the
  variable-sized signal at the **Ref** input port. These set
  the maximum permitted output sequence length.

#### Dependencies

To enable this parameter, select **Output variable-size
signals**.

### **Maximum output size** — Maximum output size `[10 1]` (default) | vector of the form [*n* 1]

Specify the maximum output size for the block. *n* is a positive
scalar.

**Example:** `[10 1]` specifies a 10-by-1 maximum size for the output
signal.

#### Dependencies

To enable this parameter, select **Output variable-size
signals** and set **Maximum output size source** to
`Dialog parameter`.

### **Reset on nonzero input** — Reset on nonzero input off (default) | on

Select this parameter to add the `Rst` input port. For more
information, see Reset Behavior.

### **Enable bit-packed outputs** — Enable bit-packed outputs off (default) | on

Select this parameter to make the **Number of packed
bits** and **Interpret bit-packed
values as signed** parameters available.

When this parameter is selected, the block generates
(*M*×*P*) bits. *M* is the number
of samples per frame specified in the **Samples per
frame** parameter. *P* is the size of the bit-packed words
specified in the **Number of packed bits** parameter. Each group of
*P* bits is packed into an integer, resulting in an integer-valued
output vector containing *M* elements. The data type of the output is
specified by **Output data
type**.

**Note**

For the integer representation, the top-most bit in each group of
*P* bits is considered the MSB, while the bottom-most bit is the
LSB.

### **Number of packed bits** — Number of packed bits 8 (default) | integer in the range [1, 32]

Number of packed bits, specified as an integer in the range [1, 32].

#### Dependencies

To enable this parameter, select **Enable bit-packed
outputs**.

### **Interpret bit-packed values as signed** — Interpret bit-packed values as signed off (default) | on

Interpret bit-packed values as signed integer data values when selected or unsigned
integer data values when cleared. When selected, a 1 in the most significant bit (sign
bit) indicates a negative value.

#### Dependencies

To enable this parameter, select **Enable bit-packed
outputs**.

### **Output data type** — Output data type `double` (default) | `boolean` | `Smallest unsigned integer`

Output data type, specified as `double`,
`boolean`, or `Smallest unsigned
integer`.

- When **Enable bit-packed
  outputs** is cleared, the output data type can be specified as a
  `double`, `boolean`, or `Smallest
  unsigned integer`. When the **Output data type**
  parameter is set to `Smallest unsigned integer`, the output data
  type is selected based on the settings used in the **Hardware
  Implementation** pane of the Configuration Parameters dialog box of the
  model. If `ASIC/FPGA` is selected in the **Hardware
  Implementation** pane, the output data type `ufix(1)`
  = ideal minimum one-bit size. For all other selections, it is an unsigned integer
  with the smallest available word length large enough to fit one bit, usually
  corresponding to the size of a char (for example,
  `uint8`).
- When **Enable bit-packed
  outputs** is selected, the output data type can be specified as
  `double` or `Smallest unsigned integer`. When
  the **Output data type** parameter is set to `Smallest
  unsigned integer`, the output data type is selected based on the
  **Interpret bit-packed
  values as signed** and **Number of packed
  bits** parameters, and the settings used in the **Hardware
  Implementation** pane of the Configuration Parameters dialog box of the
  model. If `ASIC/FPGA` is selected in the **Hardware
  Implementation** pane, the output data type is the ideal minimum
  *n*-bit size, such as `sfix(n)` or
  `ufix(n)`, based on the **Interpret bit-packed values
  as signed** parameter. For all other selections, it is a signed or
  unsigned integer with the smallest available word length large enough to fit
  *n* bits.
## Libraries

Communications Toolbox / Comm Sources / Sequence Generators Communications Toolbox HDL Support / Comm Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `fixed point` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

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

**Restrictions**

- You can select `Input port` as the **Output mask
  source** on the block. In this case, the `Mask` input
  signal must be a vector of data type `ufix1`.
- If you select **Reset on nonzero input**, the input to the
  `Rst` port must have data type `Boolean`.
- Outputs of type `double` are not supported for HDL code
  generation. All other output types (including bit-packed
  outputs) are supported.
- You cannot generate HDL for this block inside a Resettable Synchronous Subsystem (HDL Coder).
- You cannot generate HDL for this block inside a Triggered Subsystem
  if the **Use trigger signal as clock** option is selected. See Using Triggered Subsystems for HDL Code Generation (HDL Coder).

## Version History

**Introduced before R2006a**

### R2020a: Existing models automatically update this block to current version

Starting in R2020a, Simulink no longer allows you to use the PN Sequence Generator block version available before
R2015b.

Existing models automatically update to load the PN Sequence Generator block version announced in
Source blocks output frames of contiguous time samples but do not use frame attribute. For more information on
block forwarding, see Maintain Compatibility of Library Blocks Using Forwarding Tables (Simulink).

## Description

Generate pseudonoise sequence

The PN Sequence Generator block generates a sequence of pseudorandom binary numbers using a
linear-feedback shift register (LFSR). Pseudonoise sequences are typically used for
pseudorandom scrambling, and in direct-sequence spread-spectrum systems. For more information,
see More About.

These icons shows the block with all ports enabled.
