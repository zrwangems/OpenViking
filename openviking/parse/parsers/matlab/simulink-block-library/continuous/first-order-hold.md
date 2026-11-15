---
type: simulink-block
title: 'First Order Hold'
family: continuous
documentation_release: R2025b
official_category: 'Continuous'
documentation_page: 'firstorderhold'
---

# First Order Hold

Implement linearly extrapolated first order hold on input signal

## Libraries

Simulink / Continuous

## Description

The First Order Hold block generates a continuous piecewise linear
approximation of the input signal. Use the First Order Hold block to
convert a sampled discrete signal to a continuous signal without triggering a solver
reset.

You can also use the First Order Hold block to break algebraic loops in
your model.

## Ports

### Input

### **Port 1** — Input signal scalar | vector | matrix

Input signal, specified as a real scalar, vector, or matrix.

**Data Types:** `double`
### Output

### **Port 1** — Linearly approximated output signal scalar | vector | matrix

Piecewise linear approximation of the input signal.

**Data Types:** `double`

## Parameters

### **Initial output** — Initial output `0` (default) | scalar | vector

Specify the output that the block generates until the simulation time exceeds the first sample
hit time of the discrete input.

#### Dependencies

- The initial output of this block cannot be `inf` or `NaN`.
- A `Run-to-run tunable parameter` cannot be changed during simulation run time. However, changing it before a simulation begins does not cause Accelerator or Rapid Accelerator to regenerate code.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InitialOutput` |
| **Type:** character vector, string |
| **Values:** scalar | vector |
| **Default:** `'0'` |

### **Output algorithm** — Output signal approximation technique `Slow (Avoid Overshoot)` (default) | `Fast (Minimize Error)`

Specify the approximation technique used to generate the output signal.
The slow, low pass algorithm avoids overshooting the input signal. The fast,
high pass algorithm minimizes error in the approximated output but can
overshoot the input signal.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `OutputAlgorithm` |
| **Type:** character vector, string |
| **Values:** `Slow (Avoid Overshoot)`| `Fast (Minimize Error)` |
| **Default:** `'Slow (Avoid Overshoot)'` |

### **Reset if relative extrapolation error exceeds** — Error tolerance for solver reset `inf` (default) | non-negative real scalar

Specify the tolerance level for the extrapolation error of the output
algorithm. Extrapolation error greater than the specified value causes
Simulink® to reset the solver for the model.

**Tip**

Enabling the **Allow continuous input** parameter
when this parameter is set to `inf` can lead to
numerical inaccuracies in simulation.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `ErrorTolerance` |
| **Type:** character vector, string |
| **Values:** scalar |
| **Default:** `'inf'` |

### **Allow continuous input** — Apply hold on continuous signals `off` (default) | `on`

Select this parameter to enable the block to accept continuous signals as
input. Enabling this parameter creates a delay between the input and output
continuous signals.

**Note**

Enable this parameter when using this block to break an algebraic
loop.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `AllowContinuousInput` |
| **Type:** character vector, string |
| **Values:** `'off'`| `'on'` |
| **Default:** `'off'` |

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code generation.

Consider discretizing your model.

## Version History

**Introduced in R2019b**
