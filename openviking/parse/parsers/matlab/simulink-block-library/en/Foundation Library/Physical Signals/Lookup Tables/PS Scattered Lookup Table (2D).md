---
type: simulink-block
title: 'PS Scattered Lookup Table (2D)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Physical Signals / Lookup Tables'
documentation_page: 'psscatteredlookuptable2d'
documentation_source_path: 'ref/psscatteredlookuptable2d.html'
language: en
---

# PS Scattered Lookup Table (2D)

## Ports
```yaml
ports:
- name: x1
  summary: Input query point or N-D array of query points along the first direction, untyped physical signal
  direction: input
- name: x2
  summary: Input query point or N-D array of query points along the second direction, untyped physical signal
  direction: input
- name: f
  summary: Output function value, untyped physical signal
  direction: output
```

### Input

### **x1** — Input query point or N-D array of query points along the first direction, untyped physical signal

The query input value along the first direction, specified as a scalar or as an
N-D array.

### **x2** — Input query point or N-D array of query points along the second direction, untyped physical signal

The query input value along the second direction, specified as a scalar or as an
N-D array. The signal size must match the signal size along the first
direction.
### Output

### **f** — Output function value, untyped physical signal

Output function value, based on applying the scattered lookup method to the two
input values. The output signal size matches the input signal size along the first
direction. The output signal unit is determined by the unit of the **Data
points function value** parameter.
## Parameters
```yaml
parameters:
- name: Data points coordinate 1
  summary: Data set of input values along the first direction [1, 2, 3, 4, 5] 1 (default)
  group: ''
- name: Data points coordinate 2
  summary: Data set of input values along the second direction [7, 6, 3, 2, 9] 1 (default)
  group: ''
- name: Data points function value
  summary: Data set of function values for the lookup [1, 2, 3, 4, 5] 1 (default)
  group: ''
- name: Extrapolation method
  summary: Select the extrapolation method Linear (default) | Nearest
  group: ''
```

### **Data points coordinate 1** — Data set of input values along the first direction `[1, 2, 3, 4, 5] 1` (default)

Data set of input values along the first direction, specified as a one-dimensional
array. Specify at least three values.

Parameter unit must be commensurate with the unit of the input signal at port
**x1**. By default, the unit is `1` (unitless). You
can select a different unit from the drop-down list or type the desired unit name, such
as `rpm`, or a valid expression, such as `rad/s`. For
more information and a list of unit abbreviations, see How to Specify Units in Block Dialogs and Unit Definitions.

### **Data points coordinate 2** — Data set of input values along the second direction `[7, 6, 3, 2, 9] 1` (default)

Data set of input values along the second direction, specified as a one-dimensional
array of the same size as **Data points coordinate 1**.

Parameter unit must be commensurate with the unit of the input signal at port
**x2**. By default, the unit is `1` (unitless). You
can select a different unit from the drop-down list or type the desired unit name, such
as `rpm`, or a valid expression, such as `rad/s`. For
more information and a list of unit abbreviations, see How to Specify Units in Block Dialogs and Unit Definitions.

### **Data points function value** — Data set of function values for the lookup `[1, 2, 3, 4, 5] 1` (default)

Data set of function values for the lookup, specified as a one-dimensional array of
the same size as**Data points coordinate 1**.

Parameter unit determines the unit of the output signal at port
**f**. By default, the unit is `1` (unitless). You
can select a different unit from the drop-down list or type the desired unit name, such
as `rpm`, or a valid expression, such as `rad/s`. For
more information and a list of unit abbreviations, see How to Specify Units in Block Dialogs and Unit Definitions.

### **Extrapolation method** — Select the extrapolation method `Linear` (default) | `Nearest`

Select the approximation method for calculating the output value when the input
value is outside the convex hull of the data set:

- `Linear` — Linear extrapolation based on
  boundary gradients.
- `Nearest` — Nearest neighbor extrapolation.
  This method evaluates to the value of the nearest neighbor on the boundary.
## Libraries

Simscape / Foundation Library / Physical Signals / Lookup Tables

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

## Description

Approximate two-dimensional function using scattered data lookup

The PS Scattered Lookup Table (2D) block computes an
approximation to some function `f=f(x1,x2)` given the coordinates of a
scattered set of input data points in a 2D space and function values at each of these data
points. The two inputs and the output are physical signals. The inputs specify the coordinates
of a query point along the two directions. The output is the computed function value
corresponding to the input query point.

The block computes an output value by using Delaunay triangulation to interpolate the
query input value against an unstructured, or scattered, set of data points. You define the
lookup table by specifying the **Data points coordinate 1** parameter (vector
of data point coordinates along the first direction), the **Data points coordinate
2** parameter (vector of coordinates of the same data points along the second
direction), and the **Data points function value** (vector of function values
corresponding to each of these data points). All three vectors must be of the same size.
