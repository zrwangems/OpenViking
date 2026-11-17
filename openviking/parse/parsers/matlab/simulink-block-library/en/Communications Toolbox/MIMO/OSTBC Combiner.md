---
type: simulink-block
title: 'OSTBC Combiner'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'MIMO'
documentation_page: 'ostbccombiner'
documentation_source_path: 'ref/ostbccombiner.html'
language: en
---

# OSTBC Combiner

## Ports
```yaml
ports:
- name: Rx
  summary: Received signal column vector | matrix | 3-D array
  direction: input
  data_types: single | double | fixed point
- name: cEst
  summary: Channel estimate matrix | 3-D array | 4-D array
  direction: input
  data_types: single | double | fixed point
- name: Out
  summary: Output data matrix | 3-D array
  direction: output
  data_types: single | double | fixed point
```

### Input

### **Rx** — Received signal column vector | matrix | 3-D array

Received signal, specified as a matrix or 3-D array. For more
information, see Input-to-Output Dimensions.

**Data Types:** `single` | `double` | `fixed point`
**Complex Number Support:** Yes

### **cEst** — Channel estimate matrix | 3-D array | 4-D array

Channel estimate, specified as a matrix or 3-D array. For more
information, see Input-to-Output Dimensions.

**Data Types:** `single` | `double` | `fixed point`
**Complex Number Support:** Yes
### Output

### **Out** — Output data matrix | 3-D array

Output data, returned as a matrix or 3-D array. For more information,
see Input-to-Output Dimensions.

The output signal inherits the data type from the input signal. For
fixed-point signals, the complex conjugation might cause overflows,
which you must manage with the **Saturate on integer overflow** fixed-point
parameter.

This port is unnamed on the block icon.

**Data Types:** `single` | `double` | `fixed point`
## Parameters
```yaml
parameters:
- name: Number of transmit antennas
  summary: Number of transmit antennas 2 (default) | 3 | 4
  group: ''
- name: Rate
  summary: Symbol rate 3/4 (default) | 1/2
  group: ''
- name: Number of receive antennas
  summary: Number of receive antennas 1 (default) | integer in range [1,8]
  group: ''
- name: Rounding mode
  summary: Rounding mode for fixed-point calculations Floor (default) | Ceiling | Convergent | Nearest | Round | Simplest
    | Zero
  group: ''
- name: Saturate on integer overflow
  summary: Option to saturate on integer overflow off (default) | on
  group: ''
- name: Product Output
  summary: 'Complex product in numerator for diversity combining Inherit: Inherit via internal rule (default) | Inherit: Same
    as product output | fixdt(1,16,0) | <data type expression>'
  group: ''
- name: Accumulator
  summary: 'Summation in numerator for diversity combining Inherit: Inherit via internal rule (default) | Inherit: Same as
    product output | fixdt(1,16,0) | <data type expression>'
  group: ''
- name: Energy product output
  summary: 'Complex product in denominator Inherit: Inherit via internal rule (default) | Inherit: Same as product output
    | fixdt(1,16,0) | <data type expression>'
  group: ''
- name: Energy accumulator
  summary: 'Summation in denominator for calculating total energy in MIMO channel Inherit: Inherit via internal rule (default)
    | Inherit: Same as accumulator | Inherit: Same as energy product output | fixdt(1,16,0) | <data type expression>'
  group: ''
- name: Division output
  summary: 'Normalized diversity combining by total energy in MIMO channel Inherit: Same as accumulator | fixdt(1,16,0) |
    <data type expression>'
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

#### Main

### **Number of transmit antennas** — Number of transmit antennas `2` (default) | `3` | `4`

Number of transmit antennas, specified as `2`,
`3`, or `4`.

### **Rate** — Symbol rate `3/4` (default) | `1/2`

Symbol rate of the code, specified as `3/4` or
`1/2`. When you set **Number of
transmit antennas** to `2`, the symbol rate
is `1`.

#### Dependencies

To enable this parameter, set **Number of transmit
antennas** to `3` or
`4`.

### **Number of receive antennas** — Number of receive antennas `1` (default) | integer in range [1,8]

Number of receive antennas, specified as an integer in the range
[1,8].

#### Data Types

### **Rounding mode** — Rounding mode for fixed-point calculations `Floor` (default) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

Rounding mode for fixed-point calculations, specified as
`Floor`, `Ceiling`,
`Convergent`,
`Nearest`, `Round`,
`Simplest`, or `Zero`.
The block uses rounding method specified by this parameter to round off the
calculation to a representable number if a value cannot be represented
exactly by the specified data type and scaling. For more information, see
Rounding (Fixed-Point Designer).

### **Saturate on integer overflow** — Option to saturate on integer overflow off (default) | on

For fixed-point calculations, use this parameter to specify the method to
be used if the magnitude of a fixed-point calculation result does not fit
into the range of the data type and scaling that stores the result.

- To saturate on integer overflow, select this parameter.
- To wrap on integer overflow, do not select this
  parameter.

For more information, see Precision and Range.

**Data Types:** `Boolean`

### **Product Output** — Complex product in numerator for diversity combining `Inherit: Inherit via internal rule` (default) | `Inherit: Same as product output` | `fixdt(1,16,0)` | `<data type expression>`

Complex product in the numerator for diversity combining, specified as
`Inherit: Inherit via internal rule`,
`Inherit: Same as product output`,
`fixdt(1,16,0)`, or a custom
`<data type expression>`. For more
information, see Fixed-Point Signals.

### **Accumulator** — Summation in numerator for diversity combining `Inherit: Inherit via internal rule` (default) | `Inherit: Same as product output` | `fixdt(1,16,0)` | `<data type expression>`

Summation in the numerator for diversity combining. Fixed-point blocks
that must hold summation results for further calculation usually allow you
to specify the data type and scaling of the accumulator. Most such blocks
cast to the accumulator data type before summation:

Process showing that the result of each addition remains in the accumulator data type

Use the **Accumulator >> Mode** parameter to specify how
you would like to designate the accumulator word and fraction lengths:

- When you select `Inherit via internal
  rule`, the accumulator output word and fraction
  lengths are automatically calculated for you. For more
  information, see Inherit via Internal Rule.
- When you select `Same as product
  output`, these characteristics match those of
  the product output.
- When you select `Same as input`,
  these characteristics match those of the first input to the
  block.
- When you select `Binary point
  scaling`, you are able to enter the word length
  and the fraction length of the accumulator, in bits.
- When you select `Slope and bias
  scaling`, you are able to enter the word
  length, in bits, and the slope of the accumulator. The bias of
  all signals in DSP System Toolbox™ software is zero.

### **Energy product output** — Complex product in denominator `Inherit: Inherit via internal rule` (default) | `Inherit: Same as product output` | `fixdt(1,16,0)` | `<data type expression>`

Complex product in the denominator for calculating total energy in the
MIMO channel, specified as `Inherit: Inherit via internal
rule`, `Inherit: Same as product
output`, `fixdt(1,16,0)`, or a
custom `<data type expression>`.

### **Energy accumulator** — Summation in denominator for calculating total energy in MIMO channel `Inherit: Inherit via internal rule` (default) | `Inherit: Same as accumulator` | `Inherit: Same as energy product output` | `fixdt(1,16,0)` | `<data type expression>`

Summation in the denominator for calculating total energy in the MIMO
channel, specified as `Inherit: Inherit via internal
rule`, `Inherit: Same as
accumulator`, `Inherit: Same as energy product
output`, `fixdt(1,16,0)`, or a
custom `<data type expression>`

### **Division output** — Normalized diversity combining by total energy in MIMO channel `Inherit: Same as accumulator` | `fixdt(1,16,0)` | `<data type expression>`

Normalized diversity combining by total energy in the MIMO channel,
specified as `Inherit: Same as accumulator`,
`fixdt(1,16,0)`, or a custom
`<data type expression>`.
## Libraries

Communications Toolbox / MIMO

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed pointa` | `single` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `yes` |
|  |  |
| --- | --- |
| a Signed only. | |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2009a**

## Description

Combine inputs using orthogonal space-time block code

The OSTBC Combiner block combines the input signal (from all of the
receive antennas) and the channel estimate signal to extract the soft information of the
symbols encoded by an orthogonal space-time block code (OSTBC). The input channel
estimate does not need to be constant and can vary each time you run the block. The
combining algorithm uses only the estimate for the first symbol period per codeword
block. A multiple-input multiple-output (MIMO) communications system applies symbol
demodulation or decoding after the OSTBC combining process.

The block conducts the combining operation for each symbol independently. The
combining algorithm depends on the structure of the OSTBC. For more information, see
OSTBC Combining Algorithm.
