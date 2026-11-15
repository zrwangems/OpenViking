---
type: simulink-block
title: 'PS Lookup Table (1D)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Physical Signal Manipulation / Lookup Tables'
documentation_page: 'pslookuptable1d'
documentation_source_path: 'ref/pslookuptable1d.html'
language: en
---

# PS Lookup Table (1D)

## Ports

### Input

### **x** — Input query point or N-D array of query points along the *x*-axis, untyped physical signal

Input query point or points along the *x*-axis. The
signal size is either a scalar, for a single query point, or an N-D
array that represents the coordinates of the query points along the
*x*-axis.
### Output

### **f** — Output function value, untyped physical signal

Output function value, based on applying the lookup table to the input
query. The output signal size matches the input signal size. The output
signal unit is determined by the unit of the **Table
values** parameter.

## Parameters

### **Table grid vector** — Vector of data points along the *x*-axis `[1, 2, 3, 4, 5] 1` (default)

Specify the vector of data points along the *x*-axis. The
vector must be strictly monotonic, either increasing or decreasing. The
values can be nonuniformly spaced. For smooth interpolation, the vector must
contain at least three values. For linear interpolation, two values are
sufficient.

Parameter unit must be commensurate with the unit of the input signal at
port **x**. By default, the unit is `1`
(unitless). You can select a different unit from the drop-down list or type
the desired unit name, such as `rpm`, or a valid
expression, such as `rad/s`. For more information and a
list of unit abbreviations, see How to Specify Units in Block Dialogs and Unit Definitions.

### **Table values** — Vector of output values along the *f*-axis `[0, 1, 2, 3, 4] 1` (default)

Specify the vector of output function values. The function values vector
must be of the same size as the data points vector.

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

- `Linear` — Uses a linear function.
  Select this option to get the best performance.
- `Smooth` — Uses a modified Akima
  interpolation algorithm. For details, see `tablelookup`. Select this option to produce a
  continuous curve with continuous first-order derivatives.

### **Extrapolation method** — Select the extrapolation method `Linear` (default) | `Nearest` | `Error`

Select one of the following extrapolation methods for determining the
output value when the input value is outside the range specified in the
argument list:

- `Linear` — Extends from the edge
  of the interpolation region linearly. The slope of the linear
  extrapolation is equal to the slope of the interpolated curve at the
  edge of the interpolation region.
- `Nearest` — Extends from the edge
  of the interpolation region as a constant. The value of the nearest
  extrapolation is equal to the value of the interpolated curve at the
  edge of the interpolation region. Select this option to produce an
  extrapolation that does not go above the highest point in the data
  or below the lowest point in the data.
- `Error` — Issues an error if the
  input signal is outside the range of the table. Select this option
  to avoid going into the extrapolation mode when you want your data
  to be within the table range.

## Libraries

Simscape / Foundation Library / Physical Signals / Lookup Tables

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

### R2019a: Unit Propagation

Prior to R2019a, this block did not propagate physical units.

If your model contains legacy blocks without unit propagation, use the Upgrade Advisor to
upgrade your blocks to the latest version. For more information, see Upgrading Models with Legacy Physical Signal Blocks.

## Description

Approximate one-dimensional function using specified lookup method

The PS Lookup Table (1D) block computes an
approximation to some function `f=f(x)` by interpolating the input
query point coordinates against a one-dimensional lookup table.

You define the lookup table by specifying the **Table grid vector**
parameter (vector of data points along the *x* axis) and the
**Table values** parameter (vector of corresponding function
values). The length of these two vectors must match. Also, the `x` data
vector must be strictly monotonic, either increasing or decreasing.

The block input and output are physical signals of matching size. The block generates
the output based on the input query and the table grid lookup, using the selected
interpolation and extrapolation methods. You have a choice of two interpolation methods
and two extrapolation methods. You also have an option for the block to issue an error
if the input signal value is outside the table grid vector range.

### Plotting Table Data

Plotting a lookup table lets you visualize the data before simulating the model,
to make sure that the table is correct. The plot reflects tabulated data specified
for the block, as well as the selected interpolation and extrapolation options.

To plot the data, right-click the block in your model and, from the context menu,
select **Foundation Library** > **Plot
Table**. For more information, see Plot Lookup Tables.
