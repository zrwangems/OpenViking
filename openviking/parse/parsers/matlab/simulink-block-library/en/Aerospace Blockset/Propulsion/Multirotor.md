---
type: simulink-block
title: 'Multirotor'
family: 'aeroblks'
product_id: 'aeroblks'
product_name: 'Aerospace Blockset'
documentation_release: R2025b
official_category: 'Propulsion'
documentation_page: 'multirotor'
documentation_source_path: 'multirotor.html'
language: en
---

# Multirotor

## Ports

### Input

### **Ω (rad/sec)** — Rotor speed *N*-element vector

Rotor speed, specified as an *N*-element vector in rad/sec in
body frame. The ordering of the rotors for the two quadcopter configurations
(*N* = 4) considered in the block are as shown in Arm Computations.

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

### **θ0** — Collective blade pitch angle N-by-1 vector | 1-by-N vector

Collective blade pitch angle, specified as an *N*-element vector.

#### Dependencies

To enable this input port, select the **Include pitch angle
inputs** check box and set the **CT and CQ Source**
dropdown to `Compute using BEMT`.

**Data Types:** `double`

### **θc** — Lateral cyclic pitch angle N-by-1 vector | 1-by-N vector

Lateral cyclic pitch angle, specified as an *N*-element vector.

#### Dependencies

To enable this input port,

- Select the **Include pitch angle inputs** check
  box.
- Set **Modeling** to `With flap
  effects`.

**Data Types:** `double`

### **θs** — Longitudinal cyclic pitch angle N-by-1 vector | 1-by-N vector

Longitudinal cyclic pitch angle, specified as an *N*-element vector.

#### Dependencies

To enable this input port,

- Select the **Include pitch angle inputs** check
  box.
- Set **Modeling** to `With flap
  effects`.

**Data Types:** `double`

### **CT** — Input thrust coefficient nonzero positive scalar | N-by-1 vector

Input thrust coefficient, specified as a nonzero positive scalar or M-by-1
vector.

If scalar, all rotors are assumed to have same value of
`CT`.

#### Dependencies

To enable this input port, set the **CT and CQ Source**
dropdown to `'Ports'`.

**Data Types:** `double`

### **CQ** — Input torque coefficient nonzero positive scalar | N-by-1 vector

Input torque coefficient, specified as a nonzero positive scalar or N-by-1
vector.

If scalar, all rotors are assumed to have same value of
`CQ`.

#### Dependencies

To enable this output port, set the **CT and CQ Source**
dropdown to `'Ports'`.

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

### **CT** — Computed thrust coefficient positive vector

Computed thrust coefficient, returned as a positive vector of *N* elements.

#### Dependencies

To enable this output port, select the **Output computed CT and
CQ** check box and set the **CT and CQ Source**
dropdown to `Compute using BEMT`.

### **CQ** — Computed torque coefficient positive vector

Computed torque coefficient, returned as a positive vector of *N* elements.

#### Dependencies

To enable this output port, select the **Output computed CT and
CQ** check box and set the **CT and CQ Source**
dropdown to `Compute using BEMT`.

## Parameters

### Main

### **Units** — Input and output units `Metric (MKS)` (default) | `English (Velocity in ft/s)` | `English (Velocity in kts)`

| Units | Velocity | Density | Force | Moment | Arm Length | Height | Radius | Chord | Hinge offset |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `Metric (MKS)` | Meters per second | kg/m3 | Newtons | Newton-meter | Meters | Meters | Meters | Meters | Meters |
| `English (Velocity in ft/s)` | Feet per second | slug/ft3 | Pound force | Pound force-feet | Feet | Feet | Feet | Feet | Feet |
| `English (Velocity in kts)` | Knots | slug/ft3 | Pound force | Pound force-feet | Feet | Feet | Feet | Feet | Feet |

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `units` |
| **Type**: character vector |
| **Values**: `'Metric (MKS)'` | `'English (Velocity in ft/s)'` | `'English (Velocity in kts)'` |
| **Default**: `'Metric (MKS)'` |

### **Modeling** — Rotor thrust calculation method `Without flap effects` (default) | `With flap effects`

Rotor thrust calculation method, specified as:

- `Without flap effects` — Model rotor thrust using
  force and moment calculations. For more information, see Force and Moment.
- `With flap effects` — Effect of tilt in rotor disc
  due to flap motion, while in forward flight, is included. The steady state lateral
  and longitudinal flap angles are calculated using the equations from [1] and used in
  the computation of forces and moments [2]. For more
  information, see Force and Moment.

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

### Vehicle

### **Configuration** — Vehicle configuration `Quadcopter X` (default) | `Quadcopter +`

Quadcopter configuration, specified as:

- `Quadcopter X` — Propellers configured as an
  `X` shape, considered as more stable than the
  `Quadcopter +` configuration.
- `Quadcopter +` — Propellers configured as a
  `+` shape.

For more information, see Arm Computations.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `config` |
| **Type**: character vector |
| **Values**: `'Quadcopter X'` | `'Quadcopter +'` |
| **Default**: `'Quadcopter X'` |

### **Arm length (m)** — Vehicle arm length `0.0624` (default) | nonzero positive scalar

Vehicle arm length, specified as a nonzero positive scalar. This length is the
rotor displacement from the center of mass of the vehicle. For more information on arm
lengths, see Algorithms.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `armLength` |
| **Type**: character vector |
| **Values**: `'0.0624'` | nonzero positive scalar |
| **Default**: `'0.0624'` |

### **Height (m)** — Vertical offset from vehicle center of gravity `-0.0159` (default) | nonzero scalar

Vertical offset from vehicle center of gravity, specified as a nonzero
scalar.

#### Programmatic Use

|  |
| --- |
| **Block Parameter**: `rotorHeight` |
| **Type**: character vector |
| **Values**: `'-0.0159'` | nonzero positive scalar |
| **Default**: `'-0.0159'` |

### Rotor

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

### **Thrust coefficient (CT)** — Thrust coefficient `0.0107` (default) | nonzero positive scalar | nonzero positive N-by-1 vector

Thrust coefficient, specified as a nonzero positive scalar or N-by-1
vector.

If you define `Thrust coefficient (CT)` as a scalar, all the
rotors are assumed to have same values for *CT*. If vector, the
ordering of the rotors is as shown in Arm Computations.

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

### **Torque coefficient (CQ)** — Torque coefficient `7.8263e-4` (default) | nonzero positive scalar | nonzero positive N-by-1 vector

Torque coefficient, specified as a nonzero positive scalar or N-by-1 element
vector.

If you define `Torque coefficient (CQ)` as a scalar, all the
rotors are assumed to have same values for *CQ*. If vector, the
ordering of the rotors is as shown in Arm Computations.

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

Number of blades per rotor, specified as a nonzero positive scalar.

#### Dependencies

To enable this checkbox,

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

### R2025a: Multirotor block now includes thrust and torque coefficient as input

Starting R2025a, you can include `CT` and
`CQ` as optional input ports for the
Multirotor block, when you set the **CT and CQ Source**
dropdown to `'Ports'`.

### R2024b: Multirotor block now includes swashplate as input

- The Multirotor block has been updated to support swashplate inputs.
  This addition allows for the inclusion of collective and cyclic blade pitch angles in
  the calculation of Forces and Moments through new optional input ports.
- `Thrust coefficient (CT)` and `Torque coefficient
  (CQ)` parameters now also accept N-element vectors as inputs.
- Starting R2024b, the Multirotor block has been updated to include
  the dropdown **CT and CQ Source** with two options:
  `'Dialog'` and `'Compute using BEMT'`.

  - Select `'Dialog'` to manually enter the thrust and torque
    coefficient values.
  - Select `'Compute using BEMT'` to compute the values using
    Blade Element Momentum Theory (BEMT). For more information on BEMT, see Thrust Coefficient and Torque Coefficient Calculations. This option is equivalent to the **Compute CT and CQ**
    checkbox from previous releases.

## Description

Compute aerodynamic forces and moments

The Multirotor block computes the aerodynamic forces and moments generated
by multiple rotating propellers or rotors, such as quadcopters, in all three dimensions. You
can also include simplified flap, or steady state, aerodynamics.
