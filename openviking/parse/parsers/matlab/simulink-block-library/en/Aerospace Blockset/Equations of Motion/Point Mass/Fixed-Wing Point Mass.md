---
type: simulink-block
title: 'Fixed-Wing Point Mass'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Equations of Motion / Point Mass'
documentation_page: 'fixedwingpointmass'
documentation_source_path: 'fixedwingpointmass.html'
language: en
---

# Fixed-Wing Point Mass

## Ports
```yaml
ports:
- name: Lift
  summary: Lift scalar
  direction: input
  data_types: double
- name: Drag
  summary: Drag scalar
  direction: input
  data_types: double
- name: Weight
  summary: Weight scalar
  direction: input
  data_types: double
- name: Thrust
  summary: Thrust scalar
  direction: input
  data_types: double
- name: ɣa
  summary: Flight path angle relative to the air mass scalar
  direction: input
  data_types: double
- name: μ
  summary: Bank angle scalar
  direction: input
  data_types: double
- name: ɑ
  summary: Angle of attack scalar
  direction: input
  data_types: double
- name: Vwind
  summary: Wind vector three-element vector
  direction: input
  data_types: double
- name: V
  summary: Airspeed scalar
  direction: output
  data_types: double
- name: G
  summary: Ground speed projection scalar
  direction: output
  data_types: double
- name: Va
  summary: Velocity vector relative to air mass three-element vector
  direction: output
  data_types: double
- name: Ve
  summary: Velocity vector relative to Earth with [North East Down] orientation three-element vector
  direction: output
  data_types: double
- name: VENU
  summary: Velocity vector relative to Earth three-element vector
  direction: output
  data_types: double
- name: Xe
  summary: Position vector relative to Earth three-element vector
  direction: output
  data_types: double
- name: XENU
  summary: Position vector relative to Earth three-element vector
  direction: output
  data_types: double
- name: γa
  summary: Flight path angle relative to air mass scalar
  direction: output
  data_types: double
- name: γ
  summary: Flight path angle relative to Earth scalar
  direction: output
  data_types: double
- name: χa
  summary: Heading angle relative to air mass scalar
  direction: output
  data_types: double
- name: χ
  summary: Heading angle relative to Earth scalar
  direction: output
  data_types: double
```

### Input

### **Lift** — Lift scalar

Lift, specified as a scalar in units of force.

**Data Types:** `double`

### **Drag** — Drag scalar

Drag, specified as a scalar in units of force.

**Data Types:** `double`

### **Weight** — Weight scalar

Weight, specified as a scalar in units of force.

**Data Types:** `double`

### **Thrust** — Thrust scalar

Thrust, specified as a scalar in units of force.

**Data Types:** `double`

### **ɣa** — Flight path angle relative to the air mass scalar

Flight path angle relative to the air mass, specified as a scalar in
radians.

**Data Types:** `double`

### **μ** — Bank angle scalar

Bank angle, specified as a scalar in radians.

**Data Types:** `double`

### **ɑ** — Angle of attack scalar

Angle of attack, specified as a scalar in radians.

**Data Types:** `double`

### **Vwind** — Wind vector three-element vector

Wind vector in the direction in which the air mass is moving,
specified as a three-element vector.

**Data Types:** `double`
### Output

### **V** — Airspeed scalar

Airspeed, returned as a scalar.

**Data Types:** `double`

### **G** — Ground speed projection scalar

Ground speed over the Earth (speed of motion over the ground),
returned as a scalar.

**Data Types:** `double`

### **Va** — Velocity vector relative to air mass three-element vector

Velocity vector relative to the air mass, returned as a three-element
vector.

**Data Types:** `double`

### **Ve** — Velocity vector relative to Earth with [North East Down] orientation three-element vector

Velocity vector relative to Earth with `[North East
Down]` orientation, returned as a three-element
vector.

#### Dependencies

To enable this port, set **Reference frame
orientation** to `[North East
Down]`.

**Data Types:** `double`

### **VENU** — Velocity vector relative to Earth three-element vector

Velocity vector relative to Earth with `[East North
Up]` orientation, returned as a three-element
vector.

#### Dependencies

To enable this port, set **Reference frame
orientation** to `[East North
Up]`.

**Data Types:** `double`

### **Xe** — Position vector relative to Earth three-element vector

Position vector relative to Earth with `[North East
Down]` orientation, returned as a three-element
vector.

#### Dependencies

To enable this port, set **Reference frame
orientation** to `[North East
Down]`.

**Data Types:** `double`

### **XENU** — Position vector relative to Earth three-element vector

Position vector relative to Earth with `[East North
Up]` orientation, returned as a three-element
vector.

#### Dependencies

To enable this port, set **Reference frame
orientation** to `[East North
Up]`.

**Data Types:** `double`

### **γa** — Flight path angle relative to air mass scalar

Flight path angle relative to the air mass, returned as a
scalar.

**Data Types:** `double`

### **γ** — Flight path angle relative to Earth scalar

Flight path angle relative to Earth, returned as a scalar.

**Data Types:** `double`

### **χa** — Heading angle relative to air mass scalar

Heading angle relative to air mass, returned as a scalar.

#### Dependencies

To enable this port, set **Degrees of Freedom**
to `6th Order (Coordinated Flight)`.

**Data Types:** `double`

### **χ** — Heading angle relative to Earth scalar

Heading angle relative to Earth, returned as a scalar.

#### Dependencies

To enable this port, set **Degrees of Freedom**
to `6th Order (Coordinated Flight)`.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Units
  summary: Units Metric (MKS) (default) | English (velocity in ft/s) | English (velocity in kts)
  group: ''
  block_parameter: units
  type: character vector
  values: '''Metric (MKS)'' | ''English (velocity in ft/s)'' | ''English (velocity in kts)'''
  default: '''Metric (MKS)'''
- name: Reference frame orientation
  summary: Reference frames [North East Down] (default) | [East North Up]
  group: ''
  block_parameter: frame
  type: character vector
  values: '''[East North Up]'' | ''[North East Down]'''
  default: '''[North East Down]'''
- name: Degrees of freedom
  summary: Degrees of freedom 6th Order (Coordinated Flight) (default) | 4th Order (Longitudinal)
  group: ''
  block_parameter: order
  type: character vector
  values: '''4th Order (Longitudinal)'' | ''6th Order (Coordinated Flight)'''
  default: '''6th Order (Coordinated Flight)'''
- name: Initial crossrange
  summary: Initial East (Earth) crossrange location 0 (default) | scalar
  group: ''
  block_parameter: east
  type: character vector
  values: scalar
  default: '''0'''
- name: Initial downrange
  summary: Initial North (Earth) downrange 0 (default) | scalar
  group: ''
  block_parameter: north
  type: character vector
  values: scalar
  default: '''0'''
- name: Initial altitude
  summary: Initial altitude 0 (default) | scalar
  group: ''
  block_parameter: altitude
  type: character vector
  values: scalar
  default: '''0'''
- name: Initial airspeed
  summary: Initial airspeed 50 (default) | scalar
  group: ''
  block_parameter: '''airspeed'''
  type: character vector
  values: scalar
  default: '''50'''
- name: Initial flight path angle
  summary: Initial flight path angle 0 (default) | scalar
  group: ''
  block_parameter: gamma
  type: character vector
  values: scalar
  default: '''0'''
- name: Initial heading angle
  summary: Initial heading angle 0 (default) | scalar
  group: ''
  block_parameter: chi
  type: character vector
  values: scalar
  default: '''0'''
- name: Mass
  summary: Point mass 10 (default) | scalar
  group: ''
  block_parameter: mass
  type: character vector
  values: scalar
  default: '''10'''
```

### **Units** — Units `Metric (MKS)` (default) | `English (velocity in ft/s)` | `English (velocity in kts)`

Input and output units, specified as follows:

| Units | Forces | Velocity | Position | Mass |
| --- | --- | --- | --- | --- |
| `Metric (MKS)` | newtons | meters per second | meters | kilograms |
| `English (velocity in ft/s)` | pounds | feet per second | feet | slugs |
| `English (velocity in kts)` | pounds | knots | feet | slugs |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `units` |
| **Type**: character vector |
| **Values**: `'Metric (MKS)'` | `'English (velocity in ft/s)'` | `'English (velocity in kts)'` |
| **Default**: `'Metric (MKS)'` |

### **Reference frame orientation** — Reference frames `[North East Down]` (default) | `[East North Up]`

Reference frames used for input ports and output ports, specified as
`[East North Up]` or `[North East
Down]`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `frame` |
| **Type**: character vector |
| **Values**: `'[East North Up]'` | `'[North East Down]'` |
| **Default**: `'[North East Down]'` |

### **Degrees of freedom** — Degrees of freedom `6th Order (Coordinated Flight)` (default) | `4th Order (Longitudinal)`

Degrees of freedom, specified as `4th Order
(Longitudinal)` or `6th Order (Coordinated
Flight)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `order` |
| **Type**: character vector |
| **Values**: `'4th Order (Longitudinal)'` | `'6th Order (Coordinated Flight)'` |
| **Default**: `'6th Order (Coordinated Flight)'` |

### **Initial crossrange** — Initial East (Earth) crossrange location `0` (default) | scalar

Initial East (Earth) location in the `[North East Down]`
orientation, specified as a scalar.

#### Dependencies

The direction specification of this parameter depends on the
**Reference frame orientation** and
**Degrees of Freedom** setting:

| Initial crossrange | Reference frame orientation | Degrees of freedom |
| --- | --- | --- |
| East | [North East Down] | 6th Order (Coordinated Flight) |
| North | [East North Up] | 6th Order (Coordinated Flight) |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `east` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'0'` |

### **Initial downrange** — Initial North (Earth) downrange `0` (default) | scalar

Initial North (Earth) downrange of the point mass, specified as a
scalar.

#### Dependencies

The direction specification of this parameter depends on the
**Reference frame orientation** and
**Degrees of Freedom** setting:

| Initial downrange | Reference frame orientation | Degrees of freedom |
| --- | --- | --- |
| North | [North East Down] | 6th Order (Coordinated Flight) |
| North | [North East Down] | 4th Order (Longitudinal) |
| East | [East North Up] | 6th Order (Coordinated Flight) |
| East | [East North Up] | 4th Order (Longitudinal) |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `north` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'0'` |

### **Initial altitude** — Initial altitude `0` (default) | scalar

Initial altitude of the point mass, specified as a scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `altitude` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'0'` |

### **Initial airspeed** — Initial airspeed `50` (default) | scalar

Initial airspeed of the point mass, specified as a scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `'airspeed'` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'50'` |

### **Initial flight path angle** — Initial flight path angle `0` (default) | scalar

Initial flight path angle of the point mass, specified as a scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `gamma` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'0'` |

### **Initial heading angle** — Initial heading angle `0` (default) | scalar

Initial heading angle of the point mass, specified as a scalar.

#### Dependencies

To enable this parameter, set **Degrees of Freedom**
to `6th Order (Coordinated Flight)`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `chi` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'0'` |

### **Mass** — Point mass `10` (default) | scalar

Mass of the point mass, specified as a scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `mass` |
| **Type**: character vector |
| **Values**: scalar |
| **Default**: `'10'` |
## Libraries

Aerospace Blockset / Equations of Motion / Point Mass UAV Toolbox / Algorithms

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021a**

## Description

Integrate fourth- or sixth-order point mass equations of motion in coordinated flight

The Fixed-Wing Point Mass block integrates fourth- or sixth-order point mass
equations of motion in coordinated flight.
