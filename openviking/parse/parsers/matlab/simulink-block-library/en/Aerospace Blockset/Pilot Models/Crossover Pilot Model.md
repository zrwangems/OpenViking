---
type: simulink-block
title: 'Crossover Pilot Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Pilot Models'
documentation_page: 'crossoverpilotmodel'
documentation_source_path: 'crossoverpilotmodel.html'
language: en
---

# Crossover Pilot Model

## Ports
```yaml
ports:
- name: x com
  summary: Signal command scalar
  direction: input
  data_types: double
- name: x
  summary: Signal scalar
  direction: input
  data_types: double
- name: u
  summary: Aircraft command scalar
  direction: output
  data_types: double
```

### Input

### **x com** — Signal command scalar

Signal command that the pilot model controls, specified as a scalar.

**Data Types:** `double`

### **x** — Signal scalar

Signal that the pilot model controls, specified as a scalar.

**Data Types:** `double`
### Output

### **u** — Aircraft command scalar

Aircraft command, returned as a scalar.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Type of control
  summary: Dynamics control Proportional (default) | Rate or velocity | Spiral divergence | Second order - Short period |
    Acceleration(*) | Roll attitude(*) | Unstable short period(*) | Second order - Phugoid(*)
  group: ''
  block_parameter: sw_popup
  type: character vector
  values: '''Proportion'' | ''Rate or velocity'' |''Spiral divergence'' | ''Second order - Short period'' | ''Acceleration(*)''
    | ''Roll attitude(*)'' | ''Unstable short period(*)'' | ''Second order - Phugoid(*)'''
  default: '''Proportion'''
- name: Calculated value
  summary: Crossover frequency or pilot gain Crossover frequency (default) | Pilot gain
  group: ''
  block_parameter: freq_gain_popup
  type: character vector
  values: '''Crossover frequency'' | ''Pilot gain'''
  default: '''Crossover frequency'''
- name: Controlled element gain
  summary: Controlled element gain 1 (default) | scalar
  group: ''
  block_parameter: Kc
  type: character vector
  values: double scalar
  default: '''1'''
- name: Pilot gain
  summary: Pilot gain 3 (default) | scalar
  group: ''
  block_parameter: Kp
  type: character vector
  values: double scalar
  default: '''3'''
- name: Crossover frequency (rad/s)
  summary: Crossover frequency 3 (default) | scalar in the range of 1 and 10
  group: ''
  block_parameter: omega_c
  type: character vector
  values: double scalar
  default: '''3'''
- name: Pilot time delay(s)
  summary: Pilot time delay 0.1 (default) | scalar
  group: ''
  block_parameter: time_delay
  type: character vector
  values: double scalar
  default: '''0.1'''
- name: Pilot lead constant
  summary: Pilot lead constant 1 (default) | scalar
  group: ''
  block_parameter: T
  type: character vector
  values: double scalar
  default: '''1'''
- name: Pilot lag constant
  summary: Pilot lag constant 5 (default) | scalar
  group: ''
  block_parameter: Ti
  type: character vector
  values: double scalar
  default: '''5'''
```

### **Type of control** — Dynamics control `Proportional` (default) | `Rate or velocity` | `Spiral divergence` | `Second order - Short period` | `Acceleration(*)` | `Roll attitude(*)` | `Unstable short period(*)` | `Second order - Phugoid(*)`

Dynamics control that you want the pilot to have over the aircraft. This table lists the
options and associated dynamics.

| Option (Controlled Element Transfer Function) | Transfer Function of Controlled Element (  *Y c*) | Transfer Function of Pilot (  *Y p* ) | *Y c*  *Y p* | Notes |
| --- | --- | --- | --- | --- |
| `Proportion al` | Kc | Kpe−τss | KcKpe−τss |  |
| `Rate or velocity` | Kcs | Kpe−τs | KcKpe−τss |  |
| `Spiral divergence` | KcTIs−1 | Kpe−τs | KcKpe−τs(TIs−1) |  |
| `Second order - Short period` | Kcωn2s2+2ζωns+ωn2 | Kpe−τsTIs+1 | Kcωn2s2+2ζωns+ωn2×Kpe−τsTIs+1 | Short   period,   with ωn>1/τ |
| `Acceleration (*)` | Kcs2 | Kpse−τs | KcKpe−τss |  |
| `Roll attitude (*)` | Kcs(TIs+1) | Kp(TLs+1)e−τs | KcKpe−τss | With   T L ≈ T I |
| `Unstable short period(*)` | Kc(TI1s+1)(TI2s−1) | Kp(TLs+1)e−τs | KcKpe−τs(TI2s−1) | With   T L ≈ T I1 |
| `Second order - Phugoid(*)` | Kcωn2s2+2ζωns+ωn2 | Kp(TLs+1)e−τs | KcKpωn2e−τss | Phugoid,   with ωn≪1/τ,1/TL≈ζωn |

\* Indicates that the pilot model includes a Derivative block, which
produces a numerical derivative. For this reason, do not send discontinuous
(such as a step) or noisy input to the Crossover Pilot Model
block. Such inputs can cause large outputs that might render the system
unstable.

This table defines the variables used in the list of control
options.

| Variable | Description |
| --- | --- |
| K c | Aircraft gain. |
| K p | Pilot gain. |
| τ | Pilot time delay. |
| T I | Lag constant. |
| T L | Lead constant. |
| ζ | Damping ratio for the aircraft. |
| ω n | Natural frequency of the aircraft. |

#### Dependencies

The Crossover Pilot Model parameters are enabled and
disabled according to the **Type of control** options.
The **Calculated value**, **Controlled element
gain**, **Pilot gain**,
**Crossover frequency (rad/s)**, and
**Pilot time delay(s)** parameters are always
enabled.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `sw_popup` |
| **Type**: character vector |
| **Values**: `'Proportion'` | `'Rate or velocity'` |`'Spiral divergence'` | `'Second order - Short period'` | `'Acceleration(*)'` | `'Roll attitude(*)'` | `'Unstable short period(*)'` | `'Second order - Phugoid(*)'` |
| **Default**: `'Proportion'` |

### **Calculated value** — Crossover frequency or pilot gain `Crossover frequency` (default) | `Pilot gain`

Crossover frequency or pilot gain value you want the block to
calculate:

- `Crossover frequency` — The block
  calculates the crossover frequency value. The parameter value is
  disabled.
- `Pilot gain` — The block calculates the
  pilot gain value. The parameter value is disabled.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `freq_gain_popup` |
| **Type**: character vector |
| **Values**: `'Crossover frequency'` | `'Pilot gain'` |
| **Default**: `'Crossover frequency'` |

### **Controlled element gain** — Controlled element gain `1` (default) | scalar

Controlled element gain, specified as a double scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Kc` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'1'` |

### **Pilot gain** — Pilot gain `3` (default) | scalar

Pilot gain, specified as a double scalar.

#### Dependencies

To enable this parameter, set **Calculated value** to
`Pilot gain`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Kp` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'3'` |

### **Crossover frequency (rad/s)** — Crossover frequency `3` (default) | scalar in the range of 1 and 10

Crossover frequency value, specified as double scalar, in rad/s. The value must be in the
range between 1 and 10.

#### Dependencies

To enable this parameter, set **Calculated value** to
`Crossover frequency`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `omega_c` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'3'` |

### **Pilot time delay(s)** — Pilot time delay `0.1` (default) | scalar

Total pilot time delay, specified as a double scalar, in seconds. This value typically
ranges from 0.1 s to 0.2 s.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `time_delay` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'0.1'` |

### **Pilot lead constant** — Pilot lead constant `1` (default) | scalar

Pilot lead constant, specified as a double scalar.

#### Dependencies

To enable this parameter, set **Type of control** to one of the
following options:

- `Roll attitude (*)`
- `Unstable short period (*)`
- `Second order - Phygoid(*)`

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `T` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'1'` |

### **Pilot lag constant** — Pilot lag constant `5` (default) | scalar

Pilot lag constant, specified as a double scalar.

#### Dependencies

To enable this parameter, set **Type of control** to
`Second order - Short period`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Ti` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'5'` |
## Libraries

Aerospace Blockset / Pilot Models

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012b**

## Description

Represent crossover pilot model

The Crossover Pilot Model block represents the pilot model described in
*Mathematical Models of Human Pilot Behavior*
[1]). This pilot
model is a single input, single output (SISO) model that represents some aspects of
human behavior when controlling aircraft.

The Crossover Pilot Model takes into account the combined dynamics of the human pilot and
the aircraft, using the form described in Algorithms around the
crossover frequency.

This block has nonlinear behavior. If you want to linearize the block (for example, with
`linearize` (Simulink Control Design) or one of the `linmod` functions), you might need to change the Pade approximation
order. The Crossover Pilot Model block implementation incorporates the
Transport Delay block with the
**Pade order (for linearization)** parameter set to
`2` by default. To change this value, use the `set_param` function, for example:

```
set_param(gcb,'pade','3')
```

**Note**

The `linmod` function provides only basic linearization
capabilities. For full linearization functionality, use Simulink®
Control Design™ software. For more information, see Choose Linearization Tools (Simulink Control Design).

When modeling human pilot models, use this block for more accuracy than that provided
by the Tustin Pilot Model block. This block is
also less accurate than the Precision Pilot Model block.
