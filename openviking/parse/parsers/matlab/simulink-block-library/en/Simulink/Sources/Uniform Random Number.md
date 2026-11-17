---
type: simulink-block
title: 'Uniform Random Number'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'uniformrandomnumber'
documentation_source_path: 'slref/uniformrandomnumber.html'
language: en
---

# Uniform Random Number

## Ports
```yaml
ports:
- name: Port_1
  summary: Random number output signal scalar | vector
  direction: output
  data_types: double
```

### Output

### **Port\_1** — Random number output signal scalar | vector

Output signal of generated uniformly distributed random numbers over
the interval you specify.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Minimum
  summary: Minimum interval 0 (default) | scalar | vector | matrix | N-D array
  group: ''
  block_parameter: Minimum
  type: character vector
  values: scalar
  default: '''-1'''
- name: Maximum
  summary: Maximum interval 0 (default) | scalar | vector | matrix | N-D array
  group: ''
  block_parameter: Maximum
  type: character vector
  values: scalar
  default: '''1'''
- name: Seed
  summary: Random number seed 0 (default) | scalar | vector | matrix | N-D array
  group: ''
  block_parameter: Seed
  type: character vector
  values: scalar
  default: '''0'''
- name: Sample time
  summary: Sample time 0.1 (default) | scalar
  group: ''
  block_parameter: SampleTime
  type: character vector
  values: scalar
  default: '''0.1'''
- name: Interpret vector parameters as 1-D
  summary: Treat vectors as 1-D on (default) | off
  group: ''
  block_parameter: VectorParams1D
  type: character vector
  values: '''on'' | ''off'''
  default: '''on'''
```

### **Minimum** — Minimum interval `0` (default) | scalar | vector | matrix | N-D array

Specify the minimum of the interval.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Minimum` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'-1'` |

### **Maximum** — Maximum interval `0` (default) | scalar | vector | matrix | N-D array

Specify the maximum of the interval.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Maximum` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'1'` |

### **Seed** — Random number seed `0` (default) | scalar | vector | matrix | N-D array

Specify the starting seed for the random number generator.

The seed must be 0 or a positive integer. Output is repeatable for a given
seed.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Seed` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'0'` |

### **Sample time** — Sample time `0.1` (default) | scalar

Specify the time interval between samples. See Specify Sample Time for
more information.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTime` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'0.1'` |

### **Interpret vector parameters as 1-D** — Treat vectors as 1-D `on` (default) | `off`

Select this check box to output a vector of length `N` if the
**Constant value** parameter evaluates to an
`N`-element row or column vector.

- When you select this check box, the block outputs a vector of length
  `N` if the **Constant value** parameter
  evaluates to an `N`-element row or column vector. For example,
  the block outputs a matrix of dimension `1-by-N` or
  `N-by-1`.
- When you clear this check box, the block does not output a vector of length
  `N` if the **Constant value** parameter
  evaluates to an `N`-element row or column vector.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `VectorParams1D` |
| **Type:** character vector |
| **Values:** `'on' | 'off'` |
| **Default:** `'on'` |
## Libraries

Simulink / Sources

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced before R2006a**

## Description

Generate uniformly distributed random numbers

The Uniform Random Number block generates uniformly distributed random
numbers over an interval that you specify. To generate normally distributed random
numbers, use the Random Number block. Both blocks use the
Normal (Gaussian) random number generator (`'v4'`: legacy MATLAB® 4.0 generator of the `rng` function).

You can generate a repeatable sequence using any Uniform Random Number block
with the same nonnegative seed and parameters. The seed resets to the specified value
each time a simulation starts.

Avoid integrating a random signal, because solvers must integrate relatively smooth signals.
Instead, use the Band-Limited White Noise block.

The numeric parameters of this block must have the same dimensions
after scalar expansion. If you select the **Interpret vector parameters as 1-D** check box and the numeric parameters
are row or column vectors after scalar expansion, the block outputs
a 1-D signal. If you clear the **Interpret vector parameters as 1-D** check box, the block outputs a signal of the same dimensionality as the parameters.
