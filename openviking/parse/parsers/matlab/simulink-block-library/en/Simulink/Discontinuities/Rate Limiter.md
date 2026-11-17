---
type: simulink-block
title: 'Rate Limiter'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Discontinuities'
documentation_page: 'ratelimiter'
documentation_source_path: 'slref/ratelimiter.html'
language: en
---

# Rate Limiter

## Ports
```yaml
ports:
- name: Port_1
  summary: Input signal scalar | vector
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: Output signal scalar | vector
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### Input

### **Port\_1** — Input signal scalar | vector

The input signal to the rate limiter algorithm.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### Output

### **Port\_1** — Output signal scalar | vector

Output signal from the rate limiter algorithm.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## Parameters
```yaml
parameters:
- name: Rising slew rate
  summary: Limit of derivative for increasing input 1 (default) | real number
  group: ''
  block_parameter: RisingSlewLimit
  type: character vector
  values: real number
  default: '''1'''
- name: Falling slew rate
  summary: Limit of derivative for decreasing input -1 (default) | real number
  group: ''
  block_parameter: FallingSlewLimit
  type: character vector
  values: real number
  default: '''-1'''
- name: Sample time mode
  summary: Sample time mode inherited (default) | continuous
  group: ''
  block_parameter: SampleTimeMode
  type: character vector
  values: '''inherited'' | ''continuous'''
  default: '''inherited'''
- name: Initial condition
  summary: Initial output 0 (default) | scalar | vector
  group: ''
  block_parameter: InitialCondition
  type: character vector
  values: scalar
  default: '''0'''
- name: Treat as gain when linearizing
  summary: Specify the gain value on (default) | off
  group: ''
  block_parameter: LinearizeAsGain
  type: character vector
  values: '''off'' | ''on'''
  default: '''on'''
```

### **Rising slew rate** — Limit of derivative for increasing input `1` (default) | real number

Specify the limit of the rising rate of the input signal. This parameter
is tunable for fixed-point inputs.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `RisingSlewLimit` |
| **Type**: character vector |
| **Values**: real number |
| **Default**: `'1'` |

### **Falling slew rate** — Limit of derivative for decreasing input `-1` (default) | real number

Specify the lower limit on the falling rate of the input signal. This
parameter is tunable for fixed-point inputs.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `FallingSlewLimit` |
| **Type**: character vector |
| **Values**: real number |
| **Default**: `'-1'` |

### **Sample time mode** — Sample time mode `inherited` (default) | `continuous`

Specify the sample time mode, `continuous` or
`inherited` from the driving block.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `SampleTimeMode` |
| **Type**: character vector |
| **Values**: `'inherited'` | `'continuous'` |
| **Default**: `'inherited'` |

### **Initial condition** — Initial output `0` (default) | scalar | vector

Set the initial output of the simulation. Simulink® does not allow you to set the initial condition of this block
to `inf` or `NaN`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `InitialCondition` |
| **Type**: character vector |
| **Values**: `scalar` |
| **Default**: `'0'` |

### **Treat as gain when linearizing** — Specify the gain value `on` (default) | `off`

Select this parameter to cause the commands to treat the gain as 1. The linearization
commands in Simulink software treat this block as a gain in state space. Clear this parameter
to have the commands treat the gain as 0.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `LinearizeAsGain` |
| **Type**: character vector |
| **Values**: `'off'` | `'on'` |
| **Default**: `'on'` |
## Libraries

Simulink / Discontinuities

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed point` | `integer` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Cannot be used inside a triggered subsystem hierarchy.

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced before R2006a**

## Description

Limit rate of change of signal

The Rate Limiter block limits the first derivative of the signal passing through it.
The output changes no faster than the specified limit. The derivative is calculated
using this equation:

rate=u(i)−y(i−1)t(i)−t(i−1)

where *u(i)* and *t(i)* are the current block input
and time, and *y(i-1)* and *t(i-1))* are the
output and time at the previous step. The output is determined by comparing
*rate* to the **Rising slew rate** and
**Falling slew rate** parameters:

- If *rate* is greater than the **Rising
  slew rate** parameter (*R*), the output is
  calculated as

  y(i)=Δt⋅R+y(i−1).
- If *rate* is less than the **Falling slew
  rate** parameter (*F*), the output is calculated as

  y(i)=Δt⋅F+y(i−1).
- If *rate* is between the bounds of *R* and
  *F*, the change in output is equal to the change in input:

  y(i)=u(i)

When the block is running in continuous mode (for example, **Sample time
mode** is `inherited` and **Sample
time** of the driving block is zero), the **Initial
condition** is ignored. The block output at `t = 0` is
equal to the initial input:

y(0)=u(0)

When the block is running in discrete mode (for example, **Sample time
mode** is `inherited` and **Sample
time** of the driving block is nonzero), the **Initial
condition** is preserved:

y(−1)=Ic

where *Ic* is the initial condition. The block output at `t =
0` is calculated as if *rate* is outside the bounds of
*R* and *F*. For `t = 0`,
*rate* is calculated as follows:

rate=u(0)−y(−1)sample time
