---
type: simulink-block
title: 'M-APSK Modulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / APSK'
documentation_page: 'mapskmodulatorbaseband'
documentation_source_path: 'ref/mapskmodulatorbaseband.html'
language: en
---

# M-APSK Modulator Baseband

## Ports
```yaml
ports:
- name: In
  summary: Input signal scalar | vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32 | Boolean
- name: Out
  summary: APSK modulated signal scalar | vector | matrix
  direction: output
```

### Input

### **In** — Input signal scalar | vector | matrix

Input signal, specified as a scalar, vector, or matrix. The input
signal must consist of binary values or integers in the range [0,
(*M* – 1)], where *M* is the Modulation Order for M-APSK.
This port is unnamed on the block.

**Note**

To process the input signal as binary elements, set the
Input type parameter value to
`Bit`. For binary inputs, the
number of rows must be an integer multiple of
log2(*M*). Groups of
log2(*M*) bits in a
column are mapped onto a symbol, with the first bit representing
the MSB and the last bit representing the LSB.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### Output

### **Out** — APSK modulated signal scalar | vector | matrix

APSK modulated signal, returned as a complex scalar, vector, or
matrix. The output signal dimensions depend on the specified Input type value. This port is unnamed on the
block.

| **Input type** | Dimensions of Output Signal |
| --- | --- |
| `Integer` | The output signal has the same dimensions as the input signal. |
| `Bit` | The number of rows in the output signal equals the number of rows in the input signal divided by log2(*M*), where *M* is the Modulation Order for M-APSK. |

Use Output data type to specify the output data type.
## Parameters
```yaml
parameters:
- name: Constellation points per circle
  summary: Constellation points per PSK ring [4,12] (default) | vector
  group: ''
- name: Radius of each circle
  summary: Radius per PSK ring [0.5,1] (default) | vector
  group: ''
- name: Phase offset of each circle (rad)
  summary: Phase offset per PSK ring [pi/4,pi/12] (default) | scalar | vector
  group: ''
- name: Symbol mapping
  summary: Symbol mapping Auto (default) | Contourwise-gray | Gray | User-defined
  group: ''
- name: Custom symbol mapping
  summary: Custom symbol mapping [0,4,12,8,1,3,2,6,7,5,13,15,14,10,11,9] (default) | integer vector
  group: ''
- name: Input type
  summary: Input type Integer (default) | Bit
  group: ''
- name: Output data type
  summary: Output data type double (default) | single
  group: ''
- name: View Constellation
  summary: Plot reference constellation button
  group: ''
- name: Simulate using
  summary: Type of simulation to run Code generation (default) | Interpreted execution
  group: ''
```

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### **Constellation points per circle** — Constellation points per PSK ring `[4,12]` (default) | vector

Constellation points per PSK ring, specified as a vector with more than
one element. Each vector element indicates the number of constellation
points in its corresponding PSK ring. The first element corresponds to the
innermost circle, and so on until the last element, which corresponds to the
outermost circle. The sum of the elements in **Constellation points
per circle** determines the modulation order. Element values
must be multiples of four, and the modulation order must be a power of
two.

**Example:** `[4,12,16]` specifies a three PSK ring
constellation with a modulation order of 32.

### **Radius of each circle** — Radius per PSK ring `[0.5,1]` (default) | vector

Radius per PSK ring, specified as a vector with the same length as
Constellation points per circle. Each vector element
indicates the radius of its corresponding PSK ring. The first element
corresponds to the innermost circle, and so on until the last element, which
corresponds to the outermost circle. These element values must be positive
and arranged in increasing order.

**Example:** `[0.5,1,2]` defines radii for three constellation
PSK rings. The inner ring has a radius of 0.5, the second ring has a radius
of 1.0, and the outer ring has a radius of 2.0.

### **Phase offset of each circle (rad)** — Phase offset per PSK ring `[pi/4,pi/12]` (default) | scalar | vector

Phase offset per PSK ring in radians, specified as a scalar or vector with
the same length as Constellation points per circle. Each vector element
indicates the phase offset of its corresponding PSK ring. The first element
corresponds to the innermost circle, and so on until the last element, which
corresponds to the outermost circle. The **Phase offset of each
circle (rad)** can be a scalar only if all the elements of
**Constellation points per circle** are the same value.

**Example:** `[pi/4,pi/12,pi/16]` defines phase offsets for
three constellation PSK rings. The inner ring has a phase offset of π/4, the
second ring has a phase offset of π/12, and the outer ring has a phase
offset of π/16.

### **Symbol mapping** — Symbol mapping `Auto` (default) | `Contourwise-gray` | `Gray` | `User-defined`

Symbol mapping, specified as one of the following:

- `Contourwise-gray` — Uses Gray
  mapping along the contour in the phase dimension for each PSK
  ring.
- `Gray` — Uses Gray mapping along the
  contour in both the amplitude and phase dimensions. For Gray
  symbol mapping, all the values for Constellation points per circle must be equal
  and all the values for Phase offset of each circle (rad) must be equal.
  For a description of the Gray mapping used, see [2].
- `User-defined` — See Custom symbol mapping.

The default symbol mapping depends on **Constellation
points per circle** and **Phase offset of each circle
(rad)**. When all the elements of **Constellation
points per circle** are equal and all the elements of
**Phase offset of each circle (rad)** are equal, the
default is `Gray`. For all other cases, the default
is `Contourwise-gray`.

### **Custom symbol mapping** — Custom symbol mapping `[0,4,12,8,1,3,2,6,7,5,13,15,14,10,11,9]` (default) | integer vector

Custom symbol mapping, specified as an integer vector. This vector must
consist of *M* unique elements with values in the range [0,
(*M* – 1)], where *M* is the Modulation Order for M-APSK. The
first element in **Custom symbol mapping** corresponds to
the constellation point in the first quadrant of the innermost circle, with
subsequent elements positioned counterclockwise around the PSK rings.

**Example:** The default value,
`[0,4,12,8,1,3,2,6,7,5,13,15,14,10,11,9]`, specifies
contourwise-gray symbol mapping. The distribution of constellation points is
nonuniform on all contours.

#### Dependencies

To enable this parameter, set Symbol mapping to
`User-defined`.

### **Input type** — Input type `Integer` (default) | `Bit`

Input type, specified as one of these options.

- `Integer` –– The input signal must
  consist of integers in the range [0, (*M* –
  1)].
- `Bit` –– The input signal must
  contain binary values, and the number of rows must be an integer
  multiple of log2(*M*),
  where *M* is the Modulation Order for M-APSK. Binary input signals are assumed to be left-MSB aligned and
  specified column-wise. Groups of log2(sum(*M*)) bits in a column are mapped onto a symbol,
  with the first bit representing the MSB and the last bit
  representing the LSB.

### **Output data type** — Output data type `double` (default) | `single`

Output data type, specified as `double` or
`single`.

### **View Constellation** — Plot reference constellation `button`

To plot the reference constellation, click the **View
Constellation** button.

**Tip**

Click **Apply** before clicking the
**View Constellation** to view latest
parameter values.

### **Simulate using** — Type of simulation to run `Code generation` (default) | `Interpreted execution`

Type of simulation to run, specified as `Code generation` or
`Interpreted execution`.

- `Code generation` — Simulate the model by using
  generated C code. The first time you run a simulation, Simulink generates C code for the block. The model reuses the C code
  for subsequent simulations unless the model changes. This option requires
  additional startup time, but the speed of the subsequent simulations is
  faster than with the `Interpreted execution`
  option.
- `Interpreted execution` — Simulate the model by
  using the MATLAB® interpreter. This option shortens startup time, but the speed
  of subsequent simulations is slower than with the `Code
  generation` option. In this mode, you can debug the source
  code of the block.

For more information, see Interpreted Execution vs. Code Generation (Simulink).
## Libraries

Communications Toolbox / Modulation / Digital Baseband Modulation / APM

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `integer` | `single` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

M -ary amplitude phase shift keying (APSK) modulation

The M-APSK Modulator Baseband block modulates the input signal using *M*-ary
amplitude phase shift keying (APSK) modulation. The output is a baseband representation
of the modulated signal. *M*, the Modulation Order for M-APSK, equals the sum of
the elements in Constellation points per circle. For a description of *M*-APSK modulation,
see Algorithms.

**Note**

M-APSK Modulator Baseband specifically applies to multiple ring PSK constellations. For a
single ring PSK constellation, use M-PSK Modulator Baseband.
