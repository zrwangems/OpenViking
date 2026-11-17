---
type: simulink-block
title: 'Allpass Filter'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Filtering / Filter Implementations'
documentation_page: 'allpassfilter'
documentation_source_path: 'ref/allpassfilter.html'
language: en
---

# Allpass Filter

## Ports
```yaml
ports:
- name: x
  summary: Input data column vector | row vector | matrix
  direction: input
  data_types: single | double
- name: coeffs
  summary: Allpass filter coefficients column vector | row vector | matrix
  direction: input
  data_types: single | double | int8 | int16 | int32 | uint8 | uint16 | uint32
- name: Port_1
  summary: Output of the allpass filter column vector | row vector | matrix
  direction: output
  data_types: single | double
```

### Input

### **x** — Input data column vector | row vector | matrix

Input data that is passed into the allpass filter. The block accepts
real-valued or complex-valued multichannel inputs, that is,
*m*-by-*n* size inputs, where
*m* ≥ 1 and *n* ≥ 1. The block
also accepts variable-size inputs, that is, you can change the size of
each input channel during simulation. However, the number of channels
cannot change.

This port is unnamed until you set **Internal allpass
structure** to `Minimum
multiplier` or `Lattice`, and
select the **Specify coefficients from input port**
parameter.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **coeffs** — Allpass filter coefficients column vector | row vector | matrix

This port inputs the coefficients of the allpass filter. When you set
**Internal allpass structure** to
`Minimum multiplier`, the
**coeffs** port accepts matrices of size
*N*-by-1 or *N*-by-2. When you set
**Internal allpass structure** to
`Lattice`, the **coeffs**
port accepts an *N*-by-1 column vector or an
1-by-*N* row vector.

#### Dependencies

This port appears when you set **Internal allpass
structure** to `Minimum
multiplier` or `Lattice`,
and select the **Specify coefficients from input
port** parameter.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### Output

### **Port\_1** — Output of the allpass filter column vector | row vector | matrix

The size of the filtered output matches the size of the input.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters:
- name: Internal allpass structure
  summary: Filter structure Minimum multiplier (default) | Wave Digital Filter | Lattice
  group: ''
- name: Specify coefficients from input port
  summary: Flag to specify allpass polynomial coefficients off (default) | on
  group: ''
- name: Allpass polynomial coefficients
  summary: Coefficients in minimum multiplier form [-2^(-1/2), 1/2] (default) | *N*-by-1 matrix | *N*-by-2 matrix | *N*-by-4
    matrix
  group: ''
- name: Wave Digital Filter allpass coefficients
  summary: Coefficients in wave digital filter form [1/2, -2^(1/2)/3] (default) | *N*-by-1 matrix | *N*-by-2 matrix
  group: ''
- name: Indicate if last section is first order
  summary: Is last section first order off (default) | on
  group: ''
- name: Lattice allpass coefficients
  summary: Coefficients in lattice form [-2^(1/2)/3, 1/2] (default) | *N*-by-1 column vector | 1-by-*N* row vector
  group: ''
- name: View Filter Response
  summary: Visualize filter response button
  group: ''
- name: Simulate using
  summary: Type of simulation to run Interpreted execution (default) | Code generation
  group: ''
```

If a parameter is listed as tunable, then you can change its value during
simulation.

### **Internal allpass structure** — Filter structure `Minimum multiplier` (default) | `Wave Digital Filter` | `Lattice`

- `Minimum multiplier` — This
  structure uses the minimum number of required multipliers,
  *n*, with 2*n* delay units
  and 2*n* adders. The coefficients to this
  structure are specified through the **Allpass polynomial
  coefficients** parameter.
- `Wave Digital Filter` — The
  structure uses *n* multipliers and
  *n* delay units, at the expense of
  3*n* adders. The coefficients to this
  structure are specified through the **Wave Digital
  Filter allpass coefficients** parameter.
- `Lattice` — The structure uses
  2*n* multipliers, *n*
  delay units, and 2*n* adders. The coefficients
  to this structure are specified through the **Lattice
  allpass coefficients** parameter.

For more details on these structures, see Algorithms.

### **Specify coefficients from input port** — Flag to specify allpass polynomial coefficients off (default) | on

When you select this check box and set **Internal allpass
structure** to `Minimum multiplier`,
the allpass polynomial coefficients are input through the
**coeffs** port. When you clear this check box, the
allpass polynomial coefficients are specified on the block dialog through
the **Allpass polynomial coefficients** parameter.

When you select this check box and set **Internal allpass
structure** to `Lattice`, the lattice
allpass coefficients are input through the **coeffs** port.
When you clear this check box, the lattice allpass coefficients are
specified on the block dialog through the **Lattice allpass
coefficients** parameter.

#### Dependencies

To enable this parameter, set **Internal allpass
structure** to `Minimum
multiplier` or
`Lattice`.

### **Allpass polynomial coefficients** — Coefficients in minimum multiplier form [`-2^(-1/2), 1/2`] (default) | *N*-by-1 matrix | *N*-by-2 matrix | *N*-by-4 matrix

Specify the real allpass polynomial filter coefficients in minimum
multiplier form as an *N*-by-1 matrix,
*N*-by-2 matrix, or an *N*-by-4 matrix.

- *N*-by-1 matrix — The block realizes
  *N* first-order allpass sections.
- *N*-by-2 matrix — The block realizes
  *N* second-order allpass sections.
- *N*-by-4 matrix — The block realizes
  *N* fourth-order allpass sections. *(since R2024a)*

The default value [`-2^(-1/2), 1/2`] defines a stable
second-order allpass filter with poles and zeros at ±π/3 in the
*z*-plane.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Internal allpass
structure** to `Minimum
multiplier` and clear the **Specify
coefficients from input port** parameter.

### **Wave Digital Filter allpass coefficients** — Coefficients in wave digital filter form [`1/2, -2^(1/2)/3`] (default) | *N*-by-1 matrix | *N*-by-2 matrix

Specify the real allpass filter coefficients in wave digital filter form.
The coefficients can be *N*-by-1 matrix for
*N* first-order allpass sections and
*N*-by-2 matrix for *N* second-order
allpass sections. The default value, [`1/2, -2^(1/2)/3`],
is a transformed version of the default value of allpass polynomial
coefficients. This value is computed using `allpass2wdf(Allpass
polynomial coefficients)`. These coefficients define the same
stable second-order allpass filter as when the allpass structure is set to
`Minimum multiplier`.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Internal allpass
structure** to `Wave Digital
Filter`.

### **Indicate if last section is first order** — Is last section first order `off` (default) | `on`

- `on` — When you set select this check box,
  the last section is considered first order. Also, the second element
  of the last row of the *N*-by-2 matrix is ignored.
  In case of the minimum multiplier structure, if you specify an
  *N*-by-4 matrix, this parameter has no effect
  on the filter coefficients.
- `off` — When you do not select this check
  box, the last section is considered second-order.

#### Dependencies

To enable this parameter, set **Internal allpass
structure** to `Minimum
multiplier` or `Wave Digital
Filter`.

### **Lattice allpass coefficients** — Coefficients in lattice form `[-2^(1/2)/3, 1/2]` (default) | *N*-by-1 column vector | 1-by-*N* row vector

Specify the real or complex allpass coefficients as lattice reflection
coefficients. The default value, `[-2^(1/2)/3, 1/2]`, is a
transformed and transposed version of the default value of the allpass
polynomial coefficients. This value is computed using
`transpose(tf2latc(1, [1 A]))`, where
*A* is the value specified in **Allpass
polynomial coefficients**.

**Tunable:** Yes

#### Dependencies

To enable this parameter, set **Internal allpass
structure** to `Lattice` and clear
the **Specify coefficients from input port**
parameter.

### **View Filter Response** — Visualize filter response button

Opens the Filter Visualization Tool, `fvtool`, and
displays the magnitude response of the allpass filter. The response is based
on the parameters. Changes made to these parameters update
`fvtool`.

To update the magnitude response while `fvtool` is
running, modify the block parameters and click
**Apply**.

To view the magnitude response and phase response simultaneously, click
the **Magnitude and Phase responses** button on the toolbar.

In this example, the magnitude response is flat and the phase response
varies with frequencies. This varying phase response has applications in
phase equalization, notch filtering, and multirate filtering. You can
realize a lowpass filter using a parallel combination of two allpass filters
that have 180 degrees of phase shift with respect to each other.

### **Simulate using** — Type of simulation to run `Interpreted execution` (default) | `Code generation`

Specify the type of simulation to run. You can set this parameter to:

- `Interpreted execution` –– Simulate model using
  the MATLAB® interpreter. This option shortens startup time.
- `Code generation` –– Simulate model using
  generated C code. The first time you run a simulation, Simulink® generates C code for the block. The C code is reused for
  subsequent simulations as long as the model does not change. This option
  requires additional startup time but provides faster subsequent
  simulations.
## Libraries

DSP System Toolbox / Filtering / Filter Implementations

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `single` |
| **Multidimensional Signals** | `No` |
| **Variable-Size Signals** | `Yes` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

### R2024a: Change in the default value of **Simulate using** parameter

The default value of the **Simulate using** parameter is now
`Interpreted execution`. With this change, the block uses the
MATLAB interpreter for simulation by default.

### R2024a: Minimum multiplier structure supports fourth-order allpass sections

When you set the **Internal allpass structure** parameter to
`Minimum multiplier`, you can specify an
*N*-by-4 matrix of filter coefficients in the **Allpass
polynomial coefficients** parameter, where *N* is the
number of filter sections.

## Description

Single-section or multiple-section allpass filter

The Allpass Filter block filters each channel of the input signal
independently using a single-section or multiple-section (cascaded) allpass filter. You
can implement the allpass filter using a minimum multiplier, wave digital filter, or a
lattice structure.

In minimum multiplier form, the block uses the minimum number of required multipliers,
*n*, with 2*n* delay units and
2*n* adders. In wave digital filter form, the block uses only
*n* multipliers and *n* delay units, at the
expense of 3*n* adders. The lattice structure uses
2*n* multipliers, *n* delay units, and
2*n* adders. For more details on these structures, see Algorithms.
