---
type: simulink-block
title: 'Digital DATCOM Forces and Moments'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Aerodynamics'
documentation_page: 'digitaldatcomforcesandmoments'
documentation_source_path: 'digitaldatcomforcesandmoments.html'
language: en
---

# Digital DATCOM Forces and Moments

## Ports
```yaml
ports:
- name: Port_1
  summary: Angle of attack scalar
  direction: input
  data_types: double
- name: Port_2
  summary: Sideslip angle scalar
  direction: input
  data_types: double
- name: Port_3
  summary: Mach number scalar
  direction: input
  data_types: double
- name: Port_4
  summary: Altitude scalar
  direction: input
  data_types: double
- name: Port_5
  summary: Dynamic pressure scalar
  direction: input
  data_types: double
- name: Port_6
  summary: Velocity three-element vector
  direction: input
  data_types: double
- name: Port_7
  summary: Angle of attack rate scalar
  direction: input
  data_types: double
- name: Port_8
  summary: Body angular rates three-element vector
  direction: input
  data_types: double
- name: Port_9
  summary: Ground height scalar
  direction: input
  data_types: double
- name: Port_10
  summary: Control surface deflection scalar
  direction: input
  data_types: double
- name: Port_1
  summary: Aerodynamic forces at the center of gravity three-element vector
  direction: output
  data_types: double
- name: Port_2
  summary: Aerodynamic moments at the center of gravity three-element vector
  direction: output
  data_types: double
```

### Input

### **Port\_1** — Angle of attack scalar

Angle of attack, specified as a scalar.

**Data Types:** `double`

### **Port\_2** — Sideslip angle scalar

Sideslip angle, specified as a scalar, in radians.

**Data Types:** `double`

### **Port\_3** — Mach number scalar

Mach number, specified as a scalar.

**Data Types:** `double`

### **Port\_4** — Altitude scalar

Altitude, specified as a scalar, in selected length units.

**Data Types:** `double`

### **Port\_5** — Dynamic pressure scalar

Dynamic pressure, specified as a scalar, in selected pressure
units.

**Data Types:** `double`

### **Port\_6** — Velocity three-element vector

Velocity, specified as a three-element vector, in selected velocity
units and selected force axes.

**Data Types:** `double`

### **Port\_7** — Angle of attack rate scalar

Angle of attack rate, specified as a scalar, in radians per second.

#### Dependencies

Appears when DAMP Control Card is used in input to Digital
DATCOM.

**Data Types:** `double`

### **Port\_8** — Body angular rates three-element vector

Body angular rates, specified as a three-element vector, in radians
per second.

#### Dependencies

Appears when DAMP Control Card is used in input to Digital
DATCOM.

**Data Types:** `double`

### **Port\_9** — Ground height scalar

Ground height, specified as a scalar, in select units of length.

#### Dependencies

Appears when GRNDEF Namelist is used in input to Digital
DATCOM.

**Data Types:** `double`

### **Port\_10** — Control surface deflection scalar

Control surface deflection, specified as a scalar, in radians.

#### Dependencies

Appears when ASYFLP or SYMFLP and GRNDEF namelists are used in
input to Digital DATCOM.

**Data Types:** `double`
### Output

### **Port\_1** — Aerodynamic forces at the center of gravity three-element vector

Aerodynamic forces at the center of gravity, returned as a
three-element vector, in selected coordinate system: Body
(*F*,
*F*yx,
and *F*z), or Wind
(*F*D,
*F*y, and
*F*L).

**Data Types:** `double`

### **Port\_2** — Aerodynamic moments at the center of gravity three-element vector

Aerodynamic moments at the center of gravity, returned as a
three-element vector, in body coordinates
(*M*x,
*M*y, and
*M*z).

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Units
  summary: Units Metric (MKS) (default) | English (Velocity in ft/s) | English (Velocity in kts)
  group: ''
  block_parameter: units
  type: character vector
  values: '''Metric (MKS)'' | ''English (Velocity in ft/s)'' | ''English (Velocity in kts)'''
  default: '''Metric (MKS)'''
- name: Digital DATCOM structure
  summary: Digital DATCOM data structure factstruct{1} (default) | structure
  group: ''
  block_parameter: dcase
  type: character vector
  values: factstruct{1} | structure
  default: factstruct{1}
- name: Force axes
  summary: Coordinate system for aerodynamic force Body (default) | Wind
  group: ''
  block_parameter: fmode
  type: character vector
  values: '''Body'' | ''Wind'''
  default: '''Body'''
- name: Interpolation method
  summary: Interpolation method None - flat (default) | Linear
  group: ''
  block_parameter: imethod
  type: character vector
  values: '''None (flat)'' | ''Linear'''
  default: '''None (flat)'''
- name: Extrapolation method
  summary: Extrapolation method None - clip (default) | Linear
  group: ''
  block_parameter: emethod
  type: character vector
  values: '''None (flat)'' | ''Linear'''
  default: '''None (flat)'''
- name: Process out-of-range input
  summary: Handle out-of-range input Clip to Range (default) | Linear Extrapolation
  group: ''
  block_parameter: rmethod
  type: character vector
  values: '''Clip to Range'' | ''Linear Extrapolation'''
  default: '''Clip to Range'''
- name: Action for out-of-range input
  summary: Out-of-range block behavior None (default) | Warning | Error
  group: ''
  block_parameter: action
  type: character vector
  values: '''None'' | ''Warning'' | ''Error'''
  default: '''Warning'''
```

### **Units** — Units `Metric (MKS)` (default) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

Input and output units, specified as:

| Units | Force | Moment | Length | Velocity | Pressure |
| --- | --- | --- | --- | --- | --- |
| `Metric (MKS)` | Newton | Newton-  meter | Meters | Meters per second | Pascal |
| `English (Velocity in ft/s)` | Pound | Foot-pound | Feet | Feet per second | Pound per square inch |
| `English (Velocity in kts)` | Pound | Foot-pound | Feet | Knots | Pound per square inch |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `units` |
| **Type**: character vector |
| **Values**: `'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **Default**: `'Metric (MKS)'` |

### **Digital DATCOM structure** — Digital DATCOM data structure `factstruct{1}` (default) | structure

MATLAB® structure containing the digital DATCOM data. This structure
is generated by the `datcomimport` function.
To
include dynamic derivatives in the generated output file, call the
`datomimport` function with the
`damp` keyword.

For more information on creating the digital DATCOM structure, see Import from USAF Digital DATCOM Files. This example shows
how to bring United States Air Force (USAF) Digital DATCOM files into the
MATLAB environment using the Aerospace Toolbox software.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `dcase` |
| **Type**: character vector |
| **Values**: `factstruct{1}` | structure |
| **Default**: `factstruct{1}` |

### **Force axes** — Coordinate system for aerodynamic force `Body` (default) | `Wind`

Coordinate system for aerodynamic force, specified as
`Body` or `Wind`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `fmode` |
| **Type**: character vector |
| **Values**: `'Body'` | `'Wind'` |
| **Default**: `'Body'` |

### **Interpolation method** — Interpolation method `None - flat` (default) | `Linear`

Interpolation method, specified as `None (flat)` or
`Linear`. The block uses the interpolation method to
interpolate the static and dynamic stability coefficients in the
**Digital DATCOM structure**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `imethod` |
| **Type**: character vector |
| **Values**: `'None (flat)'` | `'Linear'` |
| **Default**: `'None (flat)'` |

### **Extrapolation method** — Extrapolation method `None - clip` (default) | `Linear`

Extrapolation method, specified as `None (clip)` or
`Linear`. The block uses the extrapolation method to
extrapolate the static and dynamic stability coefficients in the
**Digital DATCOM structure**.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `emethod` |
| **Type**: character vector |
| **Values**: `'None (flat)'` | `'Linear'` |
| **Default**: `'None (flat)'` |

### **Process out-of-range input** — Handle out-of-range input `Clip to Range` (default) | `Linear Extrapolation`

Handle out-of-range input action, `Linear Extrapolation`
or `Clip to Range`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `rmethod` |
| **Type**: character vector |
| **Values**: `'Clip to Range'` | `'Linear Extrapolation'` |
| **Default**: `'Clip to Range'` |

### **Action for out-of-range input** — Out-of-range block behavior `None` (default) | `Warning` | `Error`

Out-of-range block behavior, specified as:

| Action | Description |
| --- | --- |
| `None` | No action. |
| `Warning` | Warning in the Diagnostic Viewer, model simulation continues. |
| `Error` (default) | Error in the Diagnostic Viewer, model simulation stops. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `action` |
| **Type**: character vector |
| **Values**: `'None'` | `'Warning'` | `'Error'` |
| **Default**: `'Warning'` |
## Libraries

Aerospace Blockset / Aerodynamics

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2006b**

## Description

Compute aerodynamic forces and moments using Digital DATCOM static and dynamic stability derivatives

The Digital DATCOM Forces and Moments block computes the
aerodynamic forces and moments about the center of gravity using aerodynamic
coefficients from Digital DATCOM.

The Digital DATCOM Forces and Moments block port labels change based on
the input and output units selected from the **Units** list.
