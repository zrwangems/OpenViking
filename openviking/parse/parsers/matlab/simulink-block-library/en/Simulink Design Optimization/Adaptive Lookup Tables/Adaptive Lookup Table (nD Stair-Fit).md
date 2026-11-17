---
type: simulink-block
title: 'Adaptive Lookup Table (nD Stair-Fit)'
family: 'sldo'
product_id: 'sldo'
product_name: 'Simulink Design Optimization'
documentation_release: R2025b
official_category: 'Adaptive Lookup Tables'
documentation_page: 'adaptivelookuptablendstairfit'
documentation_source_path: 'ref/adaptivelookuptablendstairfit.html'
language: en
---

# Adaptive Lookup Table (nD Stair-Fit)

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters: []
```

**Number of table dimensions**
:   The number of dimensions for the adaptive lookup table.

**Table breakpoints (cell array)**
:   A set of one-dimensional vectors that contains possible block
    input values for the input variables. Each input row must be monotonically
    increasing, but the rows do not have to be the same length. For example,
    if the **Number of table dimensions** is `3`,
    you can set the table breakpoints as follows:

    ```
    {[1 2 3], [5 7], [1 3 5 7]}
    ```

**Make initial table an input**
:   Selecting this check box forces the Adaptive Lookup Table (nD
    Stair-Fit) block to ignore the **Table data (initial)** parameter,
    and creates a new input port `Tin`. Use this port
    to input the table data.

**Table data (initial)**
:   The initial table output values. This (n-D) array must be of
    size (n-1)-by-(n-1) ... -by- (n-1), (D times), where D is the number
    of dimensions and n is the number of input breakpoints.

**Table numbering data**
:   Number values assigned to cells. This vector must be the same
    size as the table data array, and each value must be unique.

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

    **Note**

    The Adaptive Lookup Table (n-D Stair Fit) block cannot output
    a table of 3 or more dimensions.

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

Adaptive lookup table of arbitrary dimension

The Adaptive Lookup Table (nD Stair-Fit) block creates an adaptive
lookup table of arbitrary dimension by dynamically updating the underlying
lookup table. The block uses the outputs of your system to do the
adaptations.

Each indexing parameter may take a value within a set of adapting
data points, which are called *breakpoints.* Breakpoints
in each dimension define a *cell.* The set of all
breakpoints in one of the dimensions defines a *grid*.
In the n-dimensional case, each cell has two n breakpoints and is
an (n-1) hypersurface.

You can use the Adaptive Lookup Table (nD Stair-Fit) block to
model time-varying systems with 2 or more inputs.
