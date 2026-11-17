---
type: simulink-block
title: 'PS Lookup Table (4D)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Lookup Tables'
documentation_page: 'pslookuptable4d'
documentation_source_path: 'ref/pslookuptable4d.html'
language: en
---

# PS Lookup Table (4D)

## Ports
```yaml
ports:
- name: x1
  summary: Input query point or N-D array of query points along the first axis, untyped physical signal
  direction: input
- name: x2
  summary: Input query point or N-D array of query points along the second axis, untyped physical signal
  direction: input
- name: x3
  summary: Input query point or N-D array of query points along the third axis, untyped physical signal
  direction: input
- name: x4
  summary: Input query point or N-D array of query points along the fourth axis, untyped physical signal
  direction: input
- name: f
  summary: Output function value, untyped physical signal
  direction: output
```

### Input

### **x1** — Input query point or N-D array of query points along the first axis, untyped physical signal

Input query point or points along the first axis. The signal size is
either a scalar, for a single query point, or an N-D array that
represents the coordinates of the query points along the first
axis.

### **x2** — Input query point or N-D array of query points along the second axis, untyped physical signal

Input query point or points along the second axis. The signal size
must match the signal size along the first axis.

### **x3** — Input query point or N-D array of query points along the third axis, untyped physical signal

Input query point or points along the third axis. The signal size must
match the signal size along the first axis.

### **x4** — Input query point or N-D array of query points along the fourth axis, untyped physical signal

Input query point or points along the fourth axis. The signal size
must match the signal size along the first axis.
### Output

### **f** — Output function value, untyped physical signal

Output function value, based on applying the lookup table to the four
input values. The output signal size matches the input signal size along
the first axis. The output signal unit is determined by the unit of the
**4D array of table values** parameter.
## Parameters
```yaml
parameters:
- name: Table grid vector 1
  summary: Vector of data values along the first axis [1, 2, 3] (default)
  group: ''
- name: Table grid vector 2
  summary: Vector of data values along the second axis [1, 2, 3, 4] (default)
  group: ''
- name: Table grid vector 3
  summary: Vector of data values along the third axis [1, 2, 3] (default)
  group: ''
- name: Table grid vector 4
  summary: Vector of data values along the fourth axis [1, 2, 3, 4, 5] (default)
  group: ''
- name: 4D array of table values
  summary: Four-dimensional array of function values at table grid vertices ones(3, 4, 3, 5) (default)
  group: ''
- name: Interpolation method
  summary: Select the interpolation method Linear (default) | Smooth
  group: ''
- name: Extrapolation method
  summary: Select the extrapolation method Linear (default) | Nearest | Error
  group: ''
```

### **Table grid vector 1** — Vector of data values along the first axis `[1, 2, 3]` (default)

Specify the vector of data values along the first axis as a
1-by-`m` array. The vector must be strictly monotonic,
either increasing or decreasing. The values can be nonuniformly spaced. For
smooth interpolation, the vector must contain at least three values. For
linear interpolation, two values are sufficient.

Parameter unit must be commensurate with the unit of the input signal at
port **x1**. By default, the unit is `1`
(unitless). You can select a different unit from the drop-down list or type
the desired unit name, such as `rpm`, or a valid
expression, such as `rad/s`. For more information and a
list of unit abbreviations, see How to Specify Units in Block Dialogs and Unit Definitions.

### **Table grid vector 2** — Vector of data values along the second axis `[1, 2, 3, 4]` (default)

Specify the vector of data values along the second axis as a
1-by-`n` array. The vector must be strictly monotonic,
either increasing or decreasing. The values can be nonuniformly spaced. For
smooth interpolation, the vector must contain at least three values. For
linear interpolation, two values are sufficient.

Parameter unit must be commensurate with the unit of the input signal at
port **x2**. By default, the unit is `1`
(unitless). You can select a different unit from the drop-down list or type
the desired unit name, such as `rpm`, or a valid
expression, such as `rad/s`. For more information and a
list of unit abbreviations, see How to Specify Units in Block Dialogs and Unit Definitions.

### **Table grid vector 3** — Vector of data values along the third axis `[1, 2, 3]` (default)

Specify the vector of data values along the third axis as a
1-by-`p` array. The vector must be strictly monotonic,
either increasing or decreasing. The values can be nonuniformly spaced. For
smooth interpolation, the vector must contain at least three values. For
linear interpolation, two values are sufficient.

Parameter unit must be commensurate with the unit of the input signal at
port **x3**. By default, the unit is `1`
(unitless). You can select a different unit from the drop-down list or type
the desired unit name, such as `rpm`, or a valid
expression, such as `rad/s`. For more information and a
list of unit abbreviations, see How to Specify Units in Block Dialogs and Unit Definitions.

### **Table grid vector 4** — Vector of data values along the fourth axis `[1, 2, 3, 4, 5]` (default)

Specify the vector of data values along the third axis as a
1-by-`q` array. The vector must be strictly monotonic,
either increasing or decreasing. The values can be nonuniformly spaced. For
smooth interpolation, the vector must contain at least three values. For
linear interpolation, two values are sufficient.

Parameter unit must be commensurate with the unit of the input signal at
port **x4**. By default, the unit is `1`
(unitless). You can select a different unit from the drop-down list or type
the desired unit name, such as `rpm`, or a valid
expression, such as `rad/s`. For more information and a
list of unit abbreviations, see How to Specify Units in Block Dialogs and Unit Definitions.

### **4D array of table values** — Four-dimensional array of function values at table grid vertices `ones(3, 4, 3, 5)` (default)

Specify the output values as an
`m`-by-`n`-by-`p`-by-`q`
array, defining the function values at the data grid vertices. The array
size must match the dimensions defined by the data vectors.

Parameter unit determines the unit of the output signal at port
**f**. By default, the unit is `1`
(unitless). You can select a different unit from the drop-down list or type
the desired unit name, such as `rpm`, or a valid
expression, such as `rad/s`. For more information and a
list of unit abbreviations, see How to Specify Units in Block Dialogs and Unit Definitions.

### **Interpolation method** — Select the interpolation method `Linear` (default) | `Smooth`

Select one of the following interpolation methods for approximating the
output value when the input value is between two consecutive grid
points:

- `Linear` — Uses an extension of
  linear algorithm for multidimensional interpolation. The method
  performs linear interpolation first in
  *`x1`*-direction, then in
  *`x2`*-direction, then in
  *`x3`*-direction, and then in
  *`x4`*-direction. Select this option to
  get the best performance.
- `Smooth` — Uses a modified Akima
  interpolation algorithm. For details, see `tablelookup`. Select this option to produce a
  continuous surface with continuous first-order derivatives.

### **Extrapolation method** — Select the extrapolation method `Linear` (default) | `Nearest` | `Error`

Select one of the following extrapolation methods for determining the
output value when the input value is outside the range specified in the
argument list:

- `Linear` — Extends from the edge
  of the interpolation region linearly. The slope of the linear
  extrapolation is equal to the slope of the interpolated surface at
  the edge of the interpolation region.
- `Nearest` — Extends from the edge
  of the interpolation region as a constant. The value of the nearest
  extrapolation is equal to the value of the interpolated surface at
  the edge of the interpolation region. Select this option to produce
  an extrapolation that does not go above the highest point in the
  data or below the lowest point in the data.
- `Error` — Issues an error if any
  of the input signals is outside the range of the table. Select this
  option to avoid going into the extrapolation mode when you want your
  data to be within the table range.
## Libraries

Simscape / Foundation Library / Physical Signals / Lookup Tables

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2016b**

### R2019a: Unit Propagation

Prior to R2019a, this block did not propagate physical units.

If your model contains legacy blocks without unit propagation, use the Upgrade Advisor to
upgrade your blocks to the latest version. For more information, see Upgrading Models with Legacy Physical Signal Blocks.

## Description

Approximate four-dimensional function using specified lookup method

The PS Lookup Table (4D) block computes an
approximation to some function `f=f(x1,x2,x3,x4)` by interpolating the
input query point coordinates against a four-dimensional lookup table.

You define the lookup table by specifying the **Table grid vector 1**
parameter (vector of data points along the first axis), the **Table grid vector
2** parameter (vector of data points along the second axis), the
**Table grid vector 3** parameter (vector of data points along the
third axis), the **Table grid vector 4** parameter (vector of data
points along the fourth axis), and the **4D array of table values**
parameter (array of output values).

The table grid data vectors must be strictly monotonic, either increasing or
decreasing. The array size of the tabulated function values must match the dimensions
defined by the data vectors. That is, if the four data vectors have sizes
1-by-`m`, 1-by-`n`, 1-by-`p`, and
1-by-`q`, respectively, supply an
`m`-by-`n`-by-`p`-by-`q`
array of the output function values.

The four inputs and the output of the block are physical signals of matching size. The
block generates the output based on the input query and the table grid lookup, using the
selected interpolation and extrapolation methods. You have a choice of two interpolation
methods and two extrapolation methods. You also have an option for the block to issue an
error if any of the input signal values is outside the respective table grid vector
range.
