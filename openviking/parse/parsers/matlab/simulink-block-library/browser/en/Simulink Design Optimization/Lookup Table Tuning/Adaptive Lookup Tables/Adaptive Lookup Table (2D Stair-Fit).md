---
type: simulink-block
title: 'Adaptive Lookup Table (2D Stair-Fit)'
family: 'sldo'
product_id: 'sldo'
product_name: 'Simulink Design Optimization'
documentation_release: R2025b
official_category: 'Lookup Table Tuning / Adaptive Lookup Tables'
documentation_page: 'adaptivelookuptable2dstairfit'
documentation_source_path: 'ref/adaptivelookuptable2dstairfit.html'
language: en
---

# Adaptive Lookup Table (2D Stair-Fit)

## Ports

Not documented in R2025b.

## Parameters

**First input (row) breakpoint set**
:   The vector of values containing possible block input values
    for the first input variable. The first input vector must be monotonically
    increasing.

**Second input (column) breakpoint set**
:   The vector of values containing possible block input values
    for the second input variable. The second input vector must be monotonically
    increasing.

**Make initial table an input**
:   Selecting this check box forces the Adaptive Lookup Table (2D
    Stair-Fit) block to ignore the **Table data (initial)** parameter,
    and creates a new input port `Tin`. Use this port
    to input the table data.

**Table data (initial)**
:   The initial table output values. This 2-by-2 matrix must be
    of size (n-1)-by-(m-1), where n is the number of first input breakpoints
    and m is the number of second input breakpoints.

**Table numbering data**
:   Number values assigned to cells. This matrix must be the same
    size as the table data matrix, and each value must be unique.

**Adaptation method**
:   Choose `Sample mean` or `Sample mean
    with forgetting`. Sample mean averages all the values received
    within a cell. Sample mean with forgetting gives more weight to the
    new data. How much weight is determined by the **Adaptation
    gain** parameter. For more information, see Selecting an Adaptation Method.

**Adaptation gain (0 to 1)**
:   A number from 0 to 1 that regulates the weight given to new
    data during the adaptation. A 0 means short memory (last data becomes
    the table value), and 1 means long memory (average all data received
    in a cell).

**Make adapted table an output**
:   Selecting this check box creates an additional output port `Tout` for
    the adapted table.

**Add adaptation enable/disable/reset port**
:   Selecting this check box creates an additional input port `Enable` that
    enables, disables, or resets the adaptive lookup table. A signal value
    of `0` applied to the port disables the adaptation,
    and signal value of `1` enables the adaptation. Setting
    the signal value to `2` resets the table values to
    the initial table data.

**Add cell lock enable/disable port**
:   Selecting this check box creates an additional input port `Lock` that
    provides the means for updating only specified cells during a simulation
    run. A signal value of `0` unlocks the specified
    cells and signal value of `1` locks the specified
    cells.

**Action for out-of-range input**
:   `Ignore` or `Adapt` by extrapolating
    beyond the extreme breakpoints.

## Libraries

Not documented in R2025b.

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2009a**

## Description

Two-dimensional adaptive table lookup

The Adaptive Lookup Table (2D Stair-Fit) block creates a two-dimensional
adaptive lookup table by dynamically updating the underlying lookup
table. The block uses the outputs, *y*, of your
system to do the adaptations.

Each indexing parameter *u* may take a value
within a set of adapting data points, which are called *breakpoints.* Two
breakpoints in each dimension define a *cell.* The
set of all breakpoints in one of the dimensions defines a *grid*.
In the two-dimensional case, each cell has four breakpoints and is
a flat surface.

You can use the Adaptive Lookup Table (2D Stair-Fit) block to
model time-varying systems with two inputs.
