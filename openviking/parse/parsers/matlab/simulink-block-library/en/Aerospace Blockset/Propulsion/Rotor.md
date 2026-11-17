---
type: simulink-block
title: 'Rotor'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Propulsion'
documentation_page: 'rotor'
documentation_source_path: 'rotor.html'
language: en
---

# Rotor

## Ports
```yaml
ports:
- name: Ω (rad/sec)
  summary: Rotor speed scalar
  direction: input
  data_types: double
- name: ρ
  summary: Air density positive scalar
  direction: input
  data_types: double
- name: Vb
  summary: Body velocity of rotor 3-by-1 vector | 1-by-3 vector
  direction: input
  data_types: double
- name: ωb
  summary: Angular velocity 3-by-1 vector | 1-by-3 vector
  direction: input
  data_types: double
- name: θ0
  summary: Collective blade pitch angle scalar
  direction: input
  data_types: double
- name: θc
  summary: Lateral cyclic pitch angle scalar
  direction: input
  data_types: double
- name: θs
  summary: Longitudinal cyclic pitch angle scalar
  direction: input
  data_types: double
- name: CT
  summary: Input thrust coefficient nonzero positive scalar
  direction: input
  data_types: double
- name: CQ
  summary: Input torque coefficient nonzero positive scalar
  direction: input
  data_types: double
- name: Fxyz(N)
  summary: Total force three-element vector
  direction: output
  data_types: double
- name: Mxyz(Nm)
  summary: Net moment three-element vector
  direction: output
  data_types: double
- name: CT
  summary: Computed thrust coefficient positive scalar
  direction: output
  data_types: double
- name: CQ
  summary: Computed torque coefficient positive scalar
  direction: output
  data_types: double
```

### Input

### **Ω (rad/sec)** — Rotor speed scalar

Rotor speed, specified as a scalar in rad/sec in body frame.

**Data Types:** `double`

### **ρ** — Air density positive scalar

Air density, specified as a positive scalar in specified units.

**Data Types:** `double`

### **Vb** — Body velocity of rotor 3-by-1 vector | 1-by-3 vector

Velocity of rotor, specified as a 3-by-1 or 1-by-3 vector in body frame. To perform a
multisystem analysis, consider connecting output from a State-Space or
Integrator block to this port.

#### Dependencies

To enable this input, set `Modeling` to `With flap
effects`.

The unit of velocity depends on the value of the `Units`
parameter.

**Data Types:** `double`

### **ωb** — Angular velocity 3-by-1 vector | 1-by-3 vector

Angular velocity of entire vehicle, specified as a 3-by-1 or 1-by-3 vector in rad/s in
body frame.

#### Dependencies

To enable this input, set `Modeling` to `With flap
effects`.

**Data Types:** `double`

### **θ0** — Collective blade pitch angle scalar

Collective blade pitch angle, specified as a scalar in radians.

#### Dependencies

To enable this input port, select the **Include pitch angle inputs** check
box and set the **CT and CQ Source** dropdown to
`Compute using BEMT`.

**Data Types:** `double`

### **θc** — Lateral cyclic pitch angle scalar

Lateral cyclic pitch angle, specified as a scalar in radians.

#### Dependencies

To enable this input port,

- Select the **Include pitch angle inputs** check
  box.
- Set **Modeling** to `With flap
  effects`.

**Data Types:** `double`

### **θs** — Longitudinal cyclic pitch angle scalar

Longitudinal cyclic pitch angle, specified as a scalar in radians.

#### Dependencies

To enable this input port,

- Select the **Include pitch angle inputs** check
  box.
- Set **Modeling** to `With flap
  effects`.

**Data Types:** `double`

### **CT** — Input thrust coefficient nonzero positive scalar

Input thrust coefficient, specified as a nonzero positive scalar.

#### Dependencies

To enable this input port, set the **CT and CQ Source** dropdown to `'Ports'`.

**Data Types:** `double`

### **CQ** — Input torque coefficient nonzero positive scalar

Input torque coefficient, specified as a nonzero positive scalar.

#### Dependencies

To enable this output port, set the **CT and CQ Source** dropdown to `'Ports'`.

**Data Types:** `double`
### Output

### **Fxyz(N)** — Total force three-element vector

Total force, returned as a three-element vector in body frame. Units depend on the
**Units** parameter.

**Data Types:** `double`

### **Mxyz(Nm)** — Net moment three-element vector

Net moment in the *x*-*y*-*z*
direction, returned as a three-element vector in body frame. Units depend on the
**Units** parameter.

**Data Types:** `double`

### **CT** — Computed thrust coefficient positive scalar

Computed thrust coefficient, returned as a positive scalar.

#### Dependencies

To enable this output port, select the **Output computed CT
and CQ** check box and set the **CT and CQ
Source** dropdown to `Compute using
BEMT`.

**Data Types:** `double`

### **CQ** — Computed torque coefficient positive scalar

Computed torque coefficient, returned as a positive scalar.

#### Dependencies

To enable this output port, select the **Output computed CT
and CQ** check box and set the **CT and CQ
Source** dropdown to `Compute using
BEMT`.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Units
  summary: Input and output units Metric (MKS) (default) | English (Velocity in ft/s) | English (Velocity in kts)
  group: ''
  block_parameter: units
  type: character vector
  values: '''Metric (MKS)'' | ''English (Velocity in ft/s)'' | ''English (Velocity in kts)'''
  default: '''Metric (MKS)'''
- name: Modeling
  summary: Rotor thrust calculation method Without flap effects (default) | With flap effects
  group: ''
  block_parameter: modelMode
  type: character vector
  values: '''Without flap effects'' | ''With flap effects'''
  default: '''Without flap effects'''
- name: Include pitch angle inputs
  summary: Enable pitch angle inputs off (default) | on
  group: ''
  block_parameter: controlInput
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: CT and CQ Source
  summary: Dropdown to select the source of thrust and torque coefficient values 'Dialog' (default) | 'Compute using BEMT'
    | 'Ports'
  group: ''
  block_parameter: CTCQMode
  type: character vector
  values: '''Dialog'' | ''Compute using BEMT'''
  default: '''Dialog'''
- name: Thrust coefficient (CT)
  summary: Thrust coefficient 0.0107 (default) | nonzero positive scalar
  group: ''
  block_parameter: CT
  type: character vector
  values: '''0.0107'' | nonzero positive scalar'
  default: '''0.0107'''
- name: Torque coefficient (CQ)
  summary: Torque coefficient 7.8263e-4 (default) | nonzero positive scalar
  group: ''
  block_parameter: CQ
  type: character vector
  values: '''7.8263e-4'' | nonzero positive scalar'
  default: '''7.8263e-4'''
- name: Number of blades
  summary: Number of blades per rotor 2 (default) | nonzero positive scalar
  group: ''
  block_parameter: Nb
  type: character vector
  values: '''2'' | nonzero positive scalar'
  default: '''2'''
- name: Output computed CT and CQ
  summary: Output computed thrust coefficient and torque coefficient off (default) | on
  group: ''
  block_parameter: CTout
  type: character vector
  values: '''on'' | ''off'''
  default: '''off'''
- name: Radius (m)
  summary: Rotor radius 0.0330 (default) | nonzero positive scalar
  group: ''
  block_parameter: radius
  type: character vector
  values: '''0.0330'' | nonzero positive scalar'
  default: '''0.0330'''
- name: Chord (m)
  summary: Blade chord 0.0080 (default) | nonzero positive scalar
  group: ''
  block_parameter: chord
  type: character vector
  values: '''0.0080'' | nonzero positive scalar'
  default: '''0.0080'''
- name: Hinge offset (m)
  summary: Hinge offset 0 (default) | positive scalar
  group: ''
  block_parameter: hingeOffset
  type: character vector
  values: '''0'' | positive scalar'
  default: '''0'''
- name: Lift curve slope (per rad)
  summary: Lift curve slope 5.5 (default) | nonzero positive scalar
  group: ''
  block_parameter: clalpha
  type: character vector
  values: '''5.5'' | nonzero positive scalar'
  default: '''5.5'''
- name: Mean drag coefficient
  summary: Mean drag coefficient 0 (default) | positive scalar
  group: ''
  block_parameter: cd0
  type: character vector
  values: '''0'' | positive scalar'
  default: '''0'''
- name: Lock number
  summary: Lock number 0.6051 (default) | nonzero positive scalar
  group: ''
  block_parameter: gamma
  type: character vector
  values: '''0.6051'' | nonzero positive scalar'
  default: '''0.6051'''
- name: Twist distribution
  summary: Rotor blade twist distribution Linear (default) | Ideal
  group: ''
  block_parameter: twistType
  type: character vector
  values: '''Linear'' | ''Ideal'''
  default: '''Linear'''
- name: Blade root angle (rad)
  summary: Blade root pitch angle 0.2548 (default) | real scalar
  group: ''
  block_parameter: thetaRoot
  type: real scalar
  values: '''0.2548'' | nonzero positive scalar'
  default: '''0.2548'''
- name: Blade twist angle (rad)
  summary: Blade twist angle -0.1361 (default) | real scalar
  group: ''
  block_parameter: thetaTwist
  type: real scalar
  values: '''0.1018'' | positive scalar'
  default: '''0.1018'''
- name: Blade tip angle (rad)
  summary: Blade tip pitch angle 0.1018 (default) | real scalar
  group: ''
  block_parameter: thetaTip
  type: real scalar
  values: '''0.06'' | nonzero positive scalar'
  default: '''0.06'''
```

#### Main

### **Units** — Input and output units `Metric (MKS)` (default) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

| Units | Velocity | Density | Force | Moment | Radius | Chord | Hinge offset |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `Metric (MKS)` | Meters per second | kg/m3 | Newtons | Newton-meter | Meters | Meters | Meters |
| `English (Velocity in ft/s)` | Feet per second | slug/ft3 | Pound force | Pound force-feet | Feet | Feet | Feet |
| `English (Velocity in kts)` | Knots | slug/ft3 | Pound force | Pound force-feet | Feet | Feet | Feet |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `units` |
| **Type**: character vector |
| **Values**: `'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **Default**: `'Metric (MKS)'` |

### **Modeling** — Rotor thrust calculation method `Without flap effects` (default) | `With flap effects`

Rotor thrust calculation method, specified as:

- `Without flap effects` — Model rotor thrust using force and moment calculations. For more information, see Force and Moment.
- `With flap effects` — Effect of tilt in rotor disc due to flap motion, while in forward flight, is included. The steady state lateral and longitudinal flap angles are calculated using the equations from [1] and used in the computation of forces and moments [2]. For more information, see Force and Moment.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `modelMode` |
| **Type**: character vector |
| **Values**: `'Without flap effects'` | `'With flap effects'` |
| **Default**: `'Without flap effects'` |

### **Include pitch angle inputs** — Enable pitch angle inputs `off` (default) | `on`

Select this check box to enable the pitch angle (swash plate) input ports.

#### Dependencies

To enable this checkbox

- Set the **CT and CQ Source** dropdown to
  `Compute using BEMT`

and/or

- Set **Modeling** to `'With flap
  effects'`

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `controlInput` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

#### Rotor

### **CT and CQ Source** — Dropdown to select the source of thrust and torque coefficient values `'Dialog'` (default) | `'Compute using BEMT'` | `'Ports'`

Select the source of the thrust coefficient and torque coefficient values, specified as a
character vector of value `'Dialog'`, `'Compute using BEMT'`
or `'Ports'`. The block assumes the aerodynamic and structural parameters to
be constant.

- Select `'Dialog'` to manually enter the thrust and torque coefficient
  values.
- Select `'Compute using BEMT'` to compute the values using Blade
  Element Momentum Theory (BEMT). For more information on BEMT, see Thrust Coefficient and Torque Coefficient Calculations.
- Select `'Ports'` to accept the thrust and torque coefficient values
  as inputs.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CTCQMode` |
| **Type**: character vector |
| **Values**: `'Dialog'` | `'Compute using BEMT'` |
| **Default**: `'Dialog'` |

### **Thrust coefficient (CT)** — Thrust coefficient `0.0107` (default) | nonzero positive scalar

Thrust coefficient, specified as a nonzero positive scalar.

#### Dependencies

To enable this parameter, set the **CT and CQ Source** dropdown
to `'Dialog'`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CT` |
| **Type**: character vector |
| **Values**: `'0.0107'` | nonzero positive scalar |
| **Default**: `'0.0107'` |

### **Torque coefficient (CQ)** — Torque coefficient `7.8263e-4` (default) | nonzero positive scalar

Torque coefficient, specified as a nonzero positive scalar.

#### Dependencies

To enable this parameter, set the **CT and CQ Source** dropdown
to `'Dialog'`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CQ` |
| **Type**: character vector |
| **Values**: `'7.8263e-4'` | nonzero positive scalar |
| **Default**: `'7.8263e-4'` |

### **Number of blades** — Number of blades per rotor `2` (default) | nonzero positive scalar

Number of blades, specified as a nonzero positive scalar.

#### Dependencies

To enable this parameter,

- Set the **CT and CQ Source** dropdown to
  `Compute using BEMT`

and/or

- Set **Modeling** to `'With flap
  effects'`

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `Nb` |
| **Type**: character vector |
| **Values**: `'2'` | nonzero positive scalar |
| **Default**: `'2'` |

### **Output computed CT and CQ** — Output computed thrust coefficient and torque coefficient off (default) | on

Select this check box to output the calculated thrust coefficient and torque coefficient to
**CT** and
**CQ** output ports. For more
information on these calculations, see Thrust Coefficient and Torque Coefficient Calculations. The block assumes the
aerodynamic and structural parameters to be constant.

Otherwise, clear this check box.

#### Dependencies

To enable this parameter, set the **CT and CQ Source** dropdown
to `'Compute using BEMT'`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `CTout` |
| **Type**: character vector |
| **Values**: `'on'` | `'off'` |
| **Default**: `'off'` |

#### Blade

### **Radius (m)** — Rotor radius `0.0330` (default) | nonzero positive scalar

Rotor radius, specified as a nonzero positive scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `radius` |
| **Type**: character vector |
| **Values**: `'0.0330'` | nonzero positive scalar |
| **Default**: `'0.0330'` |

### **Chord (m)** — Blade chord `0.0080` (default) | nonzero positive scalar

Blade chord, specified as a nonzero positive scalar.

#### Dependencies

To enable this checkbox,

- Set the **CT and CQ Source** dropdown to
  `'Compute using BEMT'`.

and/or

- Set **Modeling** to `'With flap
  effects'`

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `chord` |
| **Type**: character vector |
| **Values**: `'0.0080'` | nonzero positive scalar |
| **Default**: `'0.0080'` |

### **Hinge offset (m)** — Hinge offset `0` (default) | positive scalar

Hinge offset, specified as a positive scalar. This value is typically
`0` for propellers.

#### Dependencies

To enable this checkbox,

- Set the **CT and CQ Source** dropdown to
  `'Compute using BEMT'`.

and/or

- Set **Modeling** to `'With flap
  effects'`

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `hingeOffset` |
| **Type**: character vector |
| **Values**: `'0'` | positive scalar |
| **Default**: `'0'` |

### **Lift curve slope (per rad)** — Lift curve slope `5.5` (default) | nonzero positive scalar

Lift curve slope, specified as a nonzero positive scalar. The block assumes the aerodynamic
and structural parameters to be constant. The block does not consider
variation with respect to angle of attack.

#### Dependencies

To enable this checkbox,

- Set the **CT and CQ Source** dropdown to
  `'Compute using BEMT'`.

and/or

- Set **Modeling** to `'With flap
  effects'`

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `clalpha` |
| **Type**: character vector |
| **Values**: `'5.5'` | nonzero positive scalar |
| **Default**: `'5.5'` |

### **Mean drag coefficient** — Mean drag coefficient 0 (default) | positive scalar

Mean drag coefficient, specified as a positive scalar. The block does not consider
variation with respect to angle of attack.

#### Dependencies

To enable this parameter, set the **CT and CQ Source** dropdown
to `'Compute using BEMT'`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `cd0` |
| **Type**: character vector |
| **Values**: `'0'` | positive scalar |
| **Default**: `'0'` |

### **Lock number** — Lock number `0.6051` (default) | nonzero positive scalar

Lock number, which is the ratio of aerodynamics forces to inertial forces, specified as a
nonzero positive scalar.

#### Dependencies

To enable this parameter, set **Modeling** to `With flap effects`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `gamma` |
| **Type**: character vector |
| **Values**: `'0.6051'` | nonzero positive scalar |
| **Default**: `'0.6051'` |

### **Twist distribution** — Rotor blade twist distribution `Linear` (default) | `Ideal`

Rotor blade twist distribution, specified as:

- `Linear` — Close approximation of blade twist distribution.

  θ(r)=θroot+θtwistr
- `Ideal` — Optimal approximation of blade twist distribution.

  θ(r)=θtipr

where *r* is the nondimensional radial location along the
blade.

#### Dependencies

To enable this checkbox,

- Set the **CT and CQ Source** dropdown to
  `'Compute using BEMT'`.

and/or

- Set **Modeling** to `'With flap
  effects'`

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `twistType` |
| **Type**: character vector |
| **Values**: `'Linear'` | `'Ideal'` |
| **Default**: `'Linear'` |

### **Blade root angle (rad)** — Blade root pitch angle `0.2548` (default) | real scalar

Blade root pitch angle θroot, specified as a real scalar.

#### Dependencies

To enable this parameter:

- Set the **CT and CQ Source** dropdown
  to `'Compute using
  BEMT'`.

and/or

- Set **Modeling** to `'With
  flap effects'`

- Set **Twist distribution** to
  `Linear`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `thetaRoot` |
| **Type**: real scalar |
| **Values**: `'0.2548'` | nonzero positive scalar |
| **Default**: `'0.2548'` |

### **Blade twist angle (rad)** — Blade twist angle `-0.1361` (default) | real scalar

Blade twist angle θtwist, specified as a real scalar.

#### Dependencies

To enable this parameter:

- Set the **CT and CQ Source** dropdown to
  `'Compute using BEMT'`.

and/or

- Set **Modeling** to `'With flap
  effects'`

- Set **Twist distribution** to
  `Linear`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `thetaTwist` |
| **Type**: real scalar |
| **Values**: `'0.1018'` | positive scalar |
| **Default**: `'0.1018'` |

### **Blade tip angle (rad)** — Blade tip pitch angle `0.1018` (default) | real scalar

Blade tip pitch angle θtip for ideal twist distribution, specified as a
real scalar.

#### Dependencies

To enable this parameter:

- Set the **CT and CQ Source** dropdown
  to `'Compute using
  BEMT'`.

and/or

- Set **Modeling** to `'With
  flap effects'`

- Set **Twist distribution** to
  `Ideal`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `thetaTip` |
| **Type**: real scalar |
| **Values**: `'0.06'` | nonzero positive scalar |
| **Default**: `'0.06'` |
## Libraries

Aerospace Blockset / Propulsion

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2023a**

### R2025a: Rotor block now includes thrust and torque coefficient as input

Starting R2025a, you can include
`CT` and
`CQ` as optional
input ports for the Rotor block, when you set the
**CT and CQ Source** dropdown to
`'Ports'`.

### R2024b: Rotor block now includes swashplate as input

- Starting R2024b, the Rotor block has been
  updated to support swashplate inputs. This addition allows
  for the inclusion of collective and cyclic blade pitch
  angles in the calculation of Forces and Moments through new
  optional input ports.
- Rotor speed, Ω, also now accepts negative inputs.
- Starting R2024b, the Rotor block has been
  updated to include the dropdown **CT and CQ
  Source** with two options:
  `'Dialog'` and `'Compute
  using BEMT'`.

  - Select `'Dialog'` to
    manually enter the thrust and torque coefficient
    values.
  - Select `'Compute using
    BEMT'` to compute the values using Blade
    Element Momentum Theory (BEMT). For more
    information on BEMT, see Thrust Coefficient and Torque Coefficient Calculations. This option is equivalent to the
    **Compute CT and CQ** checkbox
    from previous releases.

## Description

Compute aerodynamic forces and moments

The Rotor block computes the aerodynamic forces and moments generated by a
rotating propeller or rotor in all three dimensions. The block lets you include the effect of
the tilt in rotor disc due to flap motion, while in forward flight, on the generated force and
moments. The Rotor block considers the effect of axial as well as
transverse flow through the rotor disc, as is required for analysis of rotorcraft systems.
