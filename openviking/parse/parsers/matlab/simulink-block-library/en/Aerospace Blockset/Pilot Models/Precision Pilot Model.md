---
type: simulink-block
title: 'Precision Pilot Model'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Pilot Models'
documentation_page: 'precisionpilotmodel'
documentation_source_path: 'precisionpilotmodel.html'
language: en
---

# Precision Pilot Model

## Ports
```yaml
ports:
- name: x com
  summary: Signal command scalar
  direction: input
  data_types: double
- name: x
  summary: Signal controlled by pilot scalar
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

### **x** — Signal controlled by pilot scalar

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
  summary: Aircraft dynamics control Proportional (default) | Rate or velocity | Acceleration | Second order
  group: ''
  block_parameter: sw_popup
  type: character vector
  values: '''Proportion'' | ''Rate or velocity'' | ''Acceleration'' | ''Second order'''
  default: '''Proportion'''
- name: Pilot gain
  summary: Pilot gain 1 (default) | scalar
  group: ''
  block_parameter: Kp
  type: character vector
  values: double scalar
  default: '''1'''
- name: Pilot time delay(s)
  summary: Pilot time delay 0.1 (default) | scalar
  group: ''
  block_parameter: time_delay
  type: character vector
  values: double scalar
  default: '''0.1'''
- name: Equalizer lead constant
  summary: Equalizer lead constant 1 (default) | scalar
  group: ''
  block_parameter: TL
  type: character vector
  values: double scalar
  default: '''1'''
- name: Equalizer lag constant
  summary: Equalizer lag constant 5 (default) | scalar
  group: ''
  block_parameter: TI
  type: character vector
  values: double scalar
  default: '''5'''
- name: Lag constant for neuromuscular system
  summary: Lag constant 0.1 (default) | scalar
  group: ''
  block_parameter: TN1
  type: character vector
  values: double scalar
  default: '0.1'
- name: Undamped natural frequency neuromuscular system (rad/s)
  summary: Undamped natural frequency 20 (default) | scalar
  group: ''
  block_parameter: nat_freq
  type: character vector
  values: double scalar
  default: '20'
- name: Damping neuromuscular system
  summary: Damping neuromuscular system 0.7 (default) | scalar
  group: ''
  block_parameter: damp
  type: character vector
  values: double scalar
  default: '0.7'
- name: Controlled element undamped natural frequency (rad/s)
  summary: Controlled element undamped natural frequency 15 (default) | scalar
  group: ''
  block_parameter: omega_m
  type: character vector
  values: double scalar
  default: '15'
```

### **Type of control** — Aircraft dynamics control `Proportional` (default) | `Rate or velocity` | `Acceleration` | `Second order`

Aircraft dynamics control. The equalizer form changes according to these values. For more
information, see [2]. To
help you decide, this table lists the options and associated
dynamics.

| Option (Controlled Element Transfer Function) | Transfer Function of Controlled Element (*Yc*) | Transfer Function of Pilot (*Yp*) |
| --- | --- | --- |
| Proportional | Kc | Lag-lead, TI >> TL |
| Rate or velocity | Kcs | 1 |
| Acceleration | Kcs2 | Lead-lag, TL >> TI |
| Second order | Kcωn2s2+2ζωns+ωn2 | Lead-lag if ωm << 2/τ.  Lag-lead if ωm >> 2/τ. |

This table defines the variables used in the list of control
options.

| Variable | Description |
| --- | --- |
| K c | Aircraft gain. |
| T I | Lag constant. |
| T L | Lead constant. |
| ζ | Damping ratio for the aircraft. |
| ω n | Natural frequency of the aircraft. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `sw_popup` |
| **Type**: character vector |
| **Values**: `'Proportion'` | `'Rate or velocity'` | `'Acceleration'` | `'Second order'` |
| **Default**: `'Proportion'` |

### **Pilot gain** — Pilot gain `1` (default) | scalar

Pilot gain, specified as a double scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Kp` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'1'` |

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

### **Equalizer lead constant** — Equalizer lead constant `1` (default) | scalar

Equalizer lead constant, specified as a double scalar.

#### Dependencies

To enable this parameter, set **Type of control** to
`Proportional`,
`Acceleration`, or `Second
order`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `TL` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'1'` |

### **Equalizer lag constant** — Equalizer lag constant `5` (default) | scalar

Equalizer lag constant, specified as a double scalar.

#### Dependencies

To enable this parameter, set **Type of control** to
`Proportional`,
`Acceleration`, or `Second
order`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `TI` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `'5'` |

### **Lag constant for neuromuscular system** — Lag constant `0.1` (default) | scalar

Neuromuscular system lag constant, specified as a double scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `TN1` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `0.1` |

### **Undamped natural frequency neuromuscular system (rad/s)** — Undamped natural frequency `20` (default) | scalar

Undamped natural frequency of the neuromuscular system, specified as a double scalar, in
rad/s.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `nat_freq` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `20` |

### **Damping neuromuscular system** — Damping neuromuscular system `0.7` (default) | scalar

Damping neuromuscular system, specified as a double scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `damp` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `0.7` |

### **Controlled element undamped natural frequency (rad/s)** — Controlled element undamped natural frequency `15` (default) | scalar

Controlled element undamped natural frequency, specified as a double scalar, in
rad/s.

#### Dependencies

To enable this parameter, set **Type of control** to
`Second order`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `omega_m` |
| **Type**: character vector |
| **Values**: double scalar |
| **Default**: `15` |
## Libraries

Aerospace Blockset / Pilot Models

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2012b**

## Description

Represent precision pilot model

The Precision Pilot Model block represents the pilot model described in
*Mathematical Models of Human Pilot Behavior*
[1]. This pilot model
is a single input, single output (SISO) model that represents some aspects of human
behavior when controlling aircraft. When modeling human pilot models, use this block for
more accuracy than that provided by the Tustin Pilot Model and Crossover Pilot Model blocks.

This block has non-linear behavior. If you want to linearize the block (for example, with
`linearize` (Simulink Control Design) or one of the `linmod` functions), you might need to change the Pade approximation
order. The Precision Pilot Model block implementation incorporates the
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

This block is an extension of the Crossover Pilot Model block. It
implements the equation described in Algorithms.
