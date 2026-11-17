---
type: simulink-block
title: 'Steering System'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Steering'
documentation_page: 'steeringsystem'
documentation_source_path: 'ref/steeringsystem.html'
language: en
---

# Steering System

## Ports
```yaml
ports:
- name: VehSpd
  summary: Vehicle speed scalar
  direction: input
- name: CstrAng
  summary: Wheel caster angle 1-by-2 vector
  direction: input
- name: WhlAngFdk
  summary: Wheel steer angle feedback 1-by-2 vector
  direction: input
- name: AngIn
  summary: Steering wheel angle input scalar
  direction: input
- name: TrqIn
  summary: Steering torque input scalar
  direction: input
- name: PwrAstTrq
  summary: Power assist torque scalar
  direction: input
- name: PctAck
  summary: Percent Ackermann value scalar
  direction: input
- name: TireFdk
  summary: Tire forces and moments feedback 1-by-12 vector
  direction: input
- name: LftKpM
  summary: Left kingpin moment scalar
  direction: input
- name: RghtKpM
  summary: Right kingpin moment scalar
  direction: input
- name: Info
  summary: Vehicle dynamics information bus
  direction: output
- name: AngLft
  summary: Left wheel steer angle scalar
  direction: output
- name: AngRght
  summary: Right wheel steer angle scalar
  direction: output
```

### Input

### **VehSpd** — Vehicle speed scalar

Vehicle speed, *v*, in m/s, specified as a scalar.
This is the magnitude of the vehicle CG longitudinal velocity
vector.

#### Dependencies

To enable this parameter, select the **Power
assist** Block Option.

### **CstrAng** — Wheel caster angle 1-by-2 vector

Wheel caster angle, *τL*, in
radians, specified as a 1-by-2 vector. The first element is the angle
for the left wheel and the second is the angle for the right
wheel.

#### Dependencies

To enable this port, clear **Input signals** > **Kingpin moment**.

### **WhlAngFdk** — Wheel steer angle feedback 1-by-2 vector

Wheel steer angle feedback, in radians, specified as a 1-by-2 vector.
The first element is the angle feedback from the left wheel and the
second element is the angle feedback from the right wheel:

- **AngLft**
- **AngRght**

You can specify the wheel steer angle feedback using
steering angle responses from a vehicle plant model or the wheel angle
outputs from this block.

#### Dependencies

To enable this port, clear **Input signals** > **Kingpin moment**.

### **AngIn** — Steering wheel angle input scalar

Steering wheel angle input from driver, in radians, specified as a
scalar.

#### Dependencies

To enable this port, select **Steering inputs** > **Angle**.

### **TrqIn** — Steering torque input scalar

Steering wheel torque input from driver, in N\*m, specified as a
scalar.

#### Dependencies

To enable this port, select **Steering inputs** > **Torque**.

### **PwrAstTrq** — Power assist torque scalar

The torque value of power assist on the steering shaft, in N\*m,
specified as a scalar. The value is supplied externally into this
port.

#### Dependencies

To enable this port, select **Input signals** > **Power assist**.

### **PctAck** — Percent Ackermann value scalar

The Ackermann value in percent, specified as a scalar. The value is
supplied externally into this port.

#### Dependencies

To enable this port, select **Input signals** > **Ackerman steering**.

### **TireFdk** — Tire forces and moments feedback 1-by-12 vector

Tire forces and moments feedback from both right and left tires,
specified as a 1-by-12 vector that contains the following values, in the
order specified in this table:

| Description | Unit |
| --- | --- |
| *x*-directional Force, Left | N |
| *x*-directional Force, Right | N |
| *y*-directional Force, Left | N |
| *y*-directional Force, Right | N |
| *z*-directional Force, Left | N |
| *z*-directional Force, Right | N |
| *x*-directional Moment, Left | N\*m |
| *x*-directional Moment, Right | N\*m |
| *y*-directional Moment, Left | N\*m |
| *y*-directional Moment, Right | N\*m |
| *z*-directional Moment, Left | N\*m |
| *z*-directional Moment, Right | N\*m |

#### Dependencies

To enable this port, clear **Input signals** > **Kingpin moment**.

### **LftKpM** — Left kingpin moment scalar

Left kingpin moment, in N\*m, specified as a scalar.

#### Dependencies

To enable this port, select **Input signals** > **Kingpin moment**.

### **RghtKpM** — Right kingpin moment scalar

Right kingpin moment, in N\*m, specified as a scalar.

#### Dependencies

To enable this port, select **Input signals** > **Kingpin moment**.
### Output

### **Info** — Vehicle dynamics information bus

Vehicle dynamics information, returned as a bus signal that contains
these signals:

| Signal | Description | Unit |
| --- | --- | --- |
| `StrWhlAngFdk` | Steering wheel angle | rad |
| `AstTrq` | Torque applied by power assist | N·m |
| `AstPwr` | Power applied by power assist | W |
| `LftTieRodForce` | Axial force in left tie rod | N |
| `RghtTieRodForce` | Axial force in right tie rod | N |
| `LftKpM` | Left kingpin moment | N·m |
| `RghtKpM` | Right kingpin moment | N·m |
| `LftWhlAng` | Left wheel steer angle | rad |
| `RghtWhlAng` | Right wheel steer angle | rad |
| `LftWhlSpd` | Left wheel steer angle velocity | rad/s |
| `RghtWhlSpd` | Right wheel steer angle velocity | rad/s |
| `TrqIn` | Torque applied by driver on steering wheel | N·m |

### **AngLft** — Left wheel steer angle `scalar`

Left wheel steer angle, *δL*,
in radians, returned as a scalar.

### **AngRght** — Right wheel steer angle `scalar`

Right wheel steer angle, *δR*,
in radians, returned as a scalar.
## Parameters
```yaml
parameters:
- name: Type
  summary: Steering type Rack and pinion (default)
  group: ''
  block_parameter: StrgType
  values: Rack and pinion (default)
- name: Intermediate shaft type
  summary: Intermediate shaft type Single Cardan joint (default) | Double Cardan joints
  group: ''
  block_parameter: IntmdShaftType
  values: Single Cardan joint (default) | Double Cardan joints
- name: Power assist
  summary: Option to model power assist on (default) | off
  group: ''
  block_parameter: PwrAst
  values: on (default) | off
- name: Ackerman steering
  summary: Option to use Ackermann steering on (default) | off
  group: ''
  block_parameter: AckStr
  values: on (default) | off
- name: Power assist
  summary: External power assist torque off (default) | on
  group: ''
  block_parameter: PwrAstOverride
  values: off (default) | on
- name: Ackerman steering
  summary: External Ackermann percent off (default) | on
  group: ''
  block_parameter: AckStrOverride
  values: off (default) | on
- name: Kingpin moment
  summary: Left and right kingpin moments off (default) | on
  group: ''
  block_parameter: KingpinOverride
  values: off (default) | on
- name: Steered axle
  summary: Location of steering system Front (default) | Rear
  group: ''
  block_parameter: Loc
  values: Front (default) | Rear
- name: Steering inputs
  summary: Steering wheel angle or torque Angle (default) | Torque
  group: ''
  block_parameter: StrIn
  values: Angle (default) | Torque
- name: Track width, TrckWdth
  summary: Track width 1 (default) | scalar
  group: ''
  block_parameter: TrckWdth
  values: 1 (default) | scalar
- name: Steering angle input range, StrRng
  summary: Steering wheel range 1.25*pi (default) | scalar
  group: ''
  block_parameter: StrRng
  values: 1.25*pi (default) | scalar
- name: Steering angle input deadband width, DbWdth
  summary: Steering angle input deadband width 0 (default) | scalar
  group: ''
  block_parameter: DbWdth
  values: 0 (default) | scalar
- name: Steering wheel inertia, StrWhlInert
  summary: Steering wheel inertia 0.1 (default) | scalar
  group: ''
  block_parameter: StrWhlInert
  values: 0.1 (default) | scalar
- name: Steering shaft inertia, StrColInert
  summary: Inertia of steering shaft 0.01 (default) | scalar
  group: ''
  block_parameter: StrCollnert
  values: 0.01 (default) | scalar
- name: Kingpin offset, KngpnOfst
  summary: Kingpin offset 0.075 (default) | scalar
  group: ''
  block_parameter: KngpnOfst
  values: 0.075 (default) | scalar
- name: Kingpin inclination angle, Lambda
  summary: Kingpin inclination angle 0.2094 (default) | scalar
  group: ''
  block_parameter: Lambda
  values: 0.2094 (default) | scalar
- name: Hub lead, HbLead
  summary: Hub lead 4.00E-05 (default) | scalar
  group: ''
  block_parameter: HbLead
  values: 4.00E-05 (default) | scalar
- name: Static loaded radius, StcLdRadius
  summary: Static loaded radius 0.4 (default) | scalar
  group: ''
  block_parameter: StcLdRadius
  values: 0.4 (default) | scalar
- name: Overall steering ratio, OvrlStrRatio
  summary: Overall steering ratio 17.42 (default) | scalar
  group: ''
  block_parameter: OvrlStrRatio
  values: 17.42 (default) | scalar
- name: Steering angle breakpoints, StrgAngBpts
  summary: Steering wheel angle breakpoints [-6.2832 -5.0265 -3.7699 -2.5133 -1.2566 0 1.2566 2.5133 3.7699 5.0265 6.2832]
    (default) | 1-by-11 vector
  group: ''
  block_parameter: StrgAngBpts
  values: '[-6.2832 -5.0265 -3.7699 -2.5133 -1.2566 0 1.2566 2.5133 3.7699 5.0265 6.2832] (default) | 1-by-11 vector'
- name: CstrAng
  summary: Caster angle 0 (default) | scalar
  group: ''
  block_parameter: CstrAng
  values: 0 (default) | scalar
- name: Rack gain parameterized by
  summary: Rack gain parameterization Constant (default) | Lookup table
  group: ''
  block_parameter: StrgRatioType
  values: Constant (default) | Lookup table
- name: Rack gain, RckGn
  summary: Rack gain 0.062 (default) | scalar
  group: ''
  block_parameter: RckGn
  values: 0.062 (default) | scalar
- name: Rack gain table, RckGnTbl
  summary: Rack gain table ones(1,11)*0.0057*2*pi (default) | 1-by-11 vector
  group: ''
  block_parameter: RckGnTbl
  values: ones(1,11)*0.0057*2*pi (default) | 1-by-11 vector
- name: Steering arm length, StrgArmLngth
  summary: Steering arm length 0.1 (default) | scalar
  group: ''
  block_parameter: StrgArmLngth
  values: 0.1 (default) | scalar
- name: Rack casing length, RckCsLngth
  summary: Rack length 0.5 (default) | scalar
  group: ''
  block_parameter: RckCsLngth
  values: 0.5 (default) | scalar
- name: Tie rod length, TieRodLngth
  summary: Tie rod length 0.248 (default) | scalar
  group: ''
  block_parameter: TieRodLngth
  values: 0.248 (default) | scalar
- name: Distance between axis and rack, Dst
  summary: Distance between axle and rack 0.2 (default) | scalar
  group: ''
  block_parameter: Dst
  values: 0.2 (default) | scalar
- name: Efficiency of gears, Epsilon
  summary: Efficiency of gears 0.9 (default) | scalar
  group: ''
  block_parameter: Epsilon
  values: 0.9 (default) | scalar
- name: Pinion inertia, PnInert
  summary: Pinion inertia 0.1 (default) | scalar
  group: ''
  block_parameter: PnInert
  values: 0.1 (default) | scalar
- name: Spatial angle for the single Cardan joint, SptlAng
  summary: Spatial angle for the single Cardan joint 2.6178 (default) | scalar
  group: ''
  block_parameter: SptlAng
  values: 2.6178 (default) | scalar
- name: Spatial angle for the upper Cardan joint, Alpha_b
  summary: Spatial angle for upper Cardan joint 2.6178 (default) | scalar
  group: ''
  block_parameter: Alpha_b
  values: 2.6178 (default) | scalar
- name: Spatial angle for the lower Cardan joint, Alpha_c
  summary: Spatial angle for lower Cardan joint 2.7051 (default) | scalar
  group: ''
  block_parameter: Alpha_c
  values: 2.7051 (default) | scalar
- name: Edge view angle between the planes of the two joints, Sigma_bc
  summary: Edge view angle between planes of the two joints 0.2618 (default) | scalar
  group: ''
  block_parameter: Sigma_bc
  values: 0.2618 (default) | scalar
- name: Phase angle, Gamma
  summary: Phase angle 0.2618 (default) | scalar
  group: ''
  block_parameter: Gamma
  values: 0.2618 (default) | scalar
- name: Steering wheel torque breakpoints, TrqBpts
  summary: Steering wheel torque breakpoints [-100 0 100] (default) | 1-by-*M* vector
  group: ''
  block_parameter: TrqBpts
  values: '[-100 0 100] (default) | 1-by-*M* vector'
- name: Vehicle speed breakpoints, VehSpdBpts
  summary: Vehicle speed breakpoints [0 20] (default) | 1-by-*N* vector
  group: ''
  block_parameter: VehSpdBpts
  values: '[0 20] (default) | 1-by-*N* vector'
- name: Assisting torque table, TrqTbl
  summary: Torque assist table [0 -100;0 0;0 100] (default) | *M*-by-*N* matrix
  group: ''
  block_parameter: TrqTbl
  values: '[0 -100;0 0;0 100] (default) | *M*-by-*N* matrix'
- name: Assisting torque limit, TrqLmt
  summary: Torque assist limit 100 (default) | scalar
  group: ''
  block_parameter: TrqLmt
  values: 100 (default) | scalar
- name: Assisting power limit, PwrLmt
  summary: Assist power limit 1000 (default) | scalar
  group: ''
  block_parameter: PwrLmt
  values: 1000 (default) | scalar
- name: Assisting torque efficiency, Eta
  summary: Torque assist efficiency 1 (default) | scalar
  group: ''
  block_parameter: Eta
  values: 1 (default) | scalar
- name: Cutoff frequency, CutOmege [rad/s]
  summary: Cutoff frequency 200 (default) | scalar
  group: ''
  block_parameter: omega_c
  values: 200 (default) | scalar
- name: Percent Ackerman parameterized by
  summary: Ackermann parameterization Constant (default) | Lookup table
  group: ''
  block_parameter: AckParamType
  values: Constant (default) | Lookup table
- name: Percent Ackerman, PctAck
  summary: Percent Ackermann 100 (default) | scalar
  group: ''
  block_parameter: PctAck
  values: 100 (default) | scalar
- name: Percent Ackerman table, PctAckTbl
  summary: Percent Ackermann table ones(1,11)*100 (default) | 1-by-11 vector
  group: ''
  block_parameter: PctAckTbl
  values: ones(1,11)*100 (default) | 1-by-11 vector
- name: Sealing stiffness, SlgStf
  summary: Sealing stiffness 1.5e4 (default) | scalar
  group: ''
  block_parameter: SlgStf
  values: 1.5e4 (default) | scalar
- name: Upper boundary friction, UpprFric
  summary: Upper boundary friction 1 (default) | scalar
  group: ''
  block_parameter: UpprFric
  values: 1 (default) | scalar
- name: Pressure change due to friction boundary increase, PrsFric
  summary: Pressure change due to friction boundary increase 1e-5 (default) | scalar
  group: ''
  block_parameter: PrsFric
  values: 1e-5 (default) | scalar
- name: Maxwell element stiffness, MaxStf
  summary: Maxwell element stiffness 10000 (default) | scalar
  group: ''
  block_parameter: MaxStf
  values: 10000 (default) | scalar
- name: Maxwell element upper boundary friction, MaxUpprFric
  summary: Maxwell element upper boundary friction 0.2 (default) | scalar
  group: ''
  block_parameter: MaxUpprFric
  values: 0.2 (default) | scalar
- name: Maxwell linear damping coefficient, MaxDamp
  summary: Maxwell linear damping coefficient 1 (default) | scalar
  group: ''
  block_parameter: MaxDamp
  values: 1 (default) | scalar
- name: Torsion bar stiffness coefficient, TorStf
  summary: Torsional stiffness of steering shaft 30 (default) | scalar
  group: ''
  block_parameter: TorStf
  values: 30 (default) | scalar
- name: Torsion bar damping coefficient, TorDamp
  summary: Torsional viscous damping in steering shaft 1 (default) | scalar
  group: ''
  block_parameter: TorDamp
  values: 1 (default) | scalar
- name: Integral anti-windup gain, A []
  summary: Integral anti-windup gain 0 (default) | scalar
  group: ''
  block_parameter: A
  values: 0 (default) | scalar
- name: Derivative gain, D []
  summary: Derivative gain 0.1 (default) | scalar
  group: ''
  block_parameter: D
  values: 0.1 (default) | scalar
- name: Integral gain, I []
  summary: Integral gain 5 (default) | scalar
  group: ''
  block_parameter: I
  values: 5 (default) | scalar
- name: Steering torque output saturation lower limit, OutSatLowLmt [Nm]
  summary: Output saturation lower limit -500 (default) | scalar
  group: ''
  block_parameter: OutSatLowLmt
  values: -500 (default) | scalar
- name: Steering torque output saturation upper limit, OutSatUpLmt [Nm]
  summary: Steering torque output saturation upper limit 500 (default) | scalar
  group: ''
  block_parameter: OutSatUpLmt
  values: 500 (default) | scalar
- name: Proportional gain, P []
  summary: Proportional gain 150 (default) | scalar
  group: ''
  block_parameter: P
  values: 150 (default) | scalar
```

#### Block Options

### **Type** — Steering type `Rack and pinion` (default)

Set the steering type for the steering system.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StrgType` |
| **Values:** | `Rack and pinion` (default) |
| **Data Types:** | `character vector` |

### **Intermediate shaft type** — Intermediate shaft type `Single Cardan joint` (default) | `Double Cardan joints`

Select whether to model the intermediate shaft type using single or double
Cardan joints.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `IntmdShaftType` |
| **Values:** | `Single Cardan joint` (default) | `Double Cardan joints` |
| **Data Types:** | `character vector` |

### **Power assist** — Option to model power assist `on` (default) | `off`

Select this parameter to model power assist within the steering
system.

#### Dependencies

To enable this parameter, in the **Input signals**
section, clear **Power assist**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PwrAst` |
| **Values:** | `on` (default) | `off` |
| **Data Types:** | `character vector` |

### **Ackerman steering** — Option to use Ackermann steering `on` (default) | `off`

Select this parameter to set the Ackermann steering percentage within the
Steering System block.

#### Dependencies

To enable this parameter, in the **Input signals**
section, clear **Ackerman steering**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `AckStr` |
| **Values:** | `on` (default) | `off` |
| **Data Types:** | `character vector` |

#### Input Signals

### **Power assist** — External power assist torque `off` (default) | `on`

Select this parameter to enable the **PwrAstTrq**
port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PwrAstOverride` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

### **Ackerman steering** — External Ackermann percent `off` (default) | `on`

Select this parameter to enable the **PctAck**
port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `AckStrOverride` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

### **Kingpin moment** — Left and right kingpin moments `off` (default) | `on`

Select this parameter to enable the **LftKpM** and
**RghtKpM** ports.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `KingpinOverride` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

### **Steered axle** — Location of steering system `Front` (default) | `Rear`

Select either the front or rear axle as the location of the Steering
System.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Loc` |
| **Values:** | `Front` (default) | `Rear` |
| **Data Types:** | `character vector` |

### **Steering inputs** — Steering wheel angle or torque `Angle` (default) | `Torque`

Select either the **AngIn** or **TrqIn**
port as the driver input.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StrIn` |
| **Values:** | `Angle` (default) | `Torque` |
| **Data Types:** | `character vector` |

#### General

### **Track width, TrckWdth** — Track width `1` (default) | scalar

Track width, *TW*, in m, specified as a scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `TrckWdth` |
| **Values:** | `1` (default) | scalar |
| **Data Types:** | `double` |

### **Steering angle input range, StrRng** — Steering wheel range `1.25*pi` (default) | scalar

Steering wheel angle from straight-ahead to either left or right lock, in
rad, specified as a scalar. This parameter causes both steered wheels to
remain within their designed steering range.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StrRng` |
| **Values:** | `1.25*pi` (default) | scalar |
| **Data Types:** | `double` |

### **Steering angle input deadband width, DbWdth** — Steering angle input deadband width `0` (default) | scalar

Steering wheel deadband angle, in radians, from left-engagement to
right-engagement.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `DbWdth` |
| **Values:** | `0` (default) | scalar |
| **Data Types:** | `double` |

### **Steering wheel inertia, StrWhlInert** — Steering wheel inertia `0.1` (default) | scalar

Steering wheel moment of inertia, in kg\*m2,
specified as a scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StrWhlInert` |
| **Values:** | `0.1` (default) | scalar |
| **Data Types:** | `double` |

### **Steering shaft inertia, StrColInert** — Inertia of steering shaft `0.01` (default) | scalar

Steering shaft moment of inertia, in kg\*m2,
specified as a scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StrCollnert` |
| **Values:** | `0.01` (default) | scalar |
| **Data Types:** | `double` |

### **Kingpin offset, KngpnOfst** — Kingpin offset `0.075` (default) | scalar

Kingpin offset, in m, specified as a scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `KngpnOfst` |
| **Values:** | `0.075` (default) | scalar |
| **Data Types:** | `character vector` |

### **Kingpin inclination angle, Lambda** — Kingpin inclination angle `0.2094` (default) | scalar

Kingpin inclination angle, in rad, specified as a scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Lambda` |
| **Values:** | `0.2094` (default) | scalar |
| **Data Types:** | `double` |

### **Hub lead, HbLead** — Hub lead `4.00E-05` (default) | scalar

Hub lead, in m, specified as a scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `HbLead` |
| **Values:** | `4.00E-05` (default) | scalar |
| **Data Types:** | `double` |

### **Static loaded radius, StcLdRadius** — Static loaded radius `0.4` (default) | scalar

Static loaded tire radius, in m, specified as a scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StcLdRadius` |
| **Values:** | `0.4` (default) | scalar |
| **Data Types:** | `double` |

### **Overall steering ratio, OvrlStrRatio** — Overall steering ratio `17.42` (default) | scalar

Overall steering ratio, specified as a scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OvrlStrRatio` |
| **Values:** | `17.42` (default) | scalar |
| **Data Types:** | `double` |

### **Steering angle breakpoints, StrgAngBpts** — Steering wheel angle breakpoints `[-6.2832 -5.0265 -3.7699 -2.5133 -1.2566 0 1.2566 2.5133 3.7699 5.0265 6.2832]` (default) | 1-by-11 vector

Steering wheel angle breakpoints, in rad, specified as a 1-by-11 vector.
These breakpoints are used to parameterize either Ackermann value or rack
gain.

#### Dependencies

To enable this parameter, set one of these parameters to
`Lookup table`:

- **Rack and pinion** > **Rack gain parameterized by**
- **Ackerman steering** > **Percent Ackerman parameterized
  by**

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StrgAngBpts` |
| **Values:** | `[-6.2832 -5.0265 -3.7699 -2.5133 -1.2566 0 1.2566 2.5133 3.7699 5.0265 6.2832]` (default) | 1-by-11 vector |
| **Data Types:** | `double` |

### **CstrAng** — Caster angle `0` (default) | scalar

Caster angle, in rad, specified as a scalar.

#### Dependencies

To enable this parameter, select **Input signals** > **Kingpin moment**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CstrAng` |
| **Values:** | `0` (default) | scalar |
| **Data Types:** | `double` |

#### Rack and Pinion

### **Rack gain parameterized by** — Rack gain parameterization `Constant` (default) | `Lookup table`

Whether to parameterize the rack gain as a constant value or by using a
lookup table.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StrgRatioType` |
| **Values:** | `Constant` (default) | `Lookup table` |
| **Data Types:** | `character vector` |

### **Rack gain, RckGn** — Rack gain `0.062` (default) | scalar

Rack gain, in m/rev, specified as a scalar.

#### Dependencies

To enable this parameter, set **Rack gain parameterized
by** to `Constant`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RckGn` |
| **Values:** | `0.062` (default) | scalar |
| **Data Types:** | `double` |

### **Rack gain table, RckGnTbl** — Rack gain table `ones(1,11)*0.0057*2*pi` (default) | 1-by-11 vector

Rack gain table, in m/rev, specified as a 1-by-11 vector.

#### Dependencies

To enable this parameter, set **Rack gain parameterized
by** to `Lookup table`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RckGnTbl` |
| **Values:** | `ones(1,11)*0.0057*2*pi` (default) | 1-by-11 vector |
| **Data Types:** | `double` |

### **Steering arm length, StrgArmLngth** — Steering arm length `0.1` (default) | scalar

Steering arm length, in m, specified as a scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `StrgArmLngth` |
| **Values:** | `0.1` (default) | scalar |
| **Data Types:** | `double` |

### **Rack casing length, RckCsLngth** — Rack length `0.5` (default) | scalar

Rack length (distance between inner tie rod ends), in m, specified as a
scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `RckCsLngth` |
| **Values:** | `0.5` (default) | scalar |
| **Data Types:** | `double` |

### **Tie rod length, TieRodLngth** — Tie rod length `0.248` (default) | scalar

Tie rod length, *lrod*, in m,
specified as a scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `TieRodLngth` |
| **Values:** | `0.248` (default) | scalar |
| **Data Types:** | `double` |

### **Distance between axis and rack, Dst** — Distance between axle and rack `0.2` (default) | scalar

Longitudinal distance between the steered axle and rack centerline,
*D*, in m, specified as a scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Dst` |
| **Values:** | `0.2` (default) | scalar |
| **Data Types:** | `double` |

### **Efficiency of gears, Epsilon** — Efficiency of gears `0.9` (default) | scalar

Efficiency of the rack and pinion mechanism, *ɛ*,
specified as a scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Epsilon` |
| **Values:** | `0.9` (default) | scalar |
| **Data Types:** | `double` |

### **Pinion inertia, PnInert** — Pinion inertia `0.1` (default) | scalar

Pinion inertia, in kg\*m2, specified as a
scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PnInert` |
| **Values:** | `0.1` (default) | scalar |
| **Data Types:** | `double` |

#### Single Cardan Joint

### **Spatial angle for the single Cardan joint, SptlAng** — Spatial angle for the single Cardan joint `2.6178` (default) | scalar

Spatial angle for the single Cardan joint, in rad, specified as a
scalar.

#### Dependencies

To enable this parameter, set **Intermediate shaft
type** to `Single Cardan
joint`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SptlAng` |
| **Values:** | `2.6178` (default) | scalar |
| **Data Types:** | `double` |

#### Double Cardan Joints

### **Spatial angle for the upper Cardan joint, Alpha\_b** — Spatial angle for upper Cardan joint `2.6178` (default) | scalar

Spatial angle for the upper Cardan joint, in rad, specified as a
scalar.

#### Dependencies

To enable this parameter, set **Intermediate shaft
type** to `Double Cardan
joints`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Alpha_b` |
| **Values:** | `2.6178` (default) | scalar |
| **Data Types:** | `double` |

### **Spatial angle for the lower Cardan joint, Alpha\_c** — Spatial angle for lower Cardan joint `2.7051` (default) | scalar

Spatial angle for the lower Cardan joint, in rad, specified as a
scalar.

#### Dependencies

To enable this parameter, set **Intermediate shaft
type** to `Double Cardan
joints`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Alpha_c` |
| **Values:** | `2.7051` (default) | scalar |
| **Data Types:** | `double` |

### **Edge view angle between the planes of the two joints, Sigma\_bc** — Edge view angle between planes of the two joints `0.2618` (default) | scalar

Edge view angle between the planes of the two joints, in rad, specified as
a scalar.

#### Dependencies

To enable this parameter, set **Intermediate shaft
type** to `Double Cardan
joints`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Sigma_bc` |
| **Values:** | `0.2618` (default) | scalar |
| **Data Types:** | `double` |

### **Phase angle, Gamma** — Phase angle `0.2618` (default) | scalar

Rotation phase angle between the two joints, in rad, specified as a
scalar.

#### Dependencies

To enable this parameter, set **Intermediate shaft
type** to `Double Cardan
joints`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Gamma` |
| **Values:** | `0.2618` (default) | scalar |
| **Data Types:** | `double` |

#### Power Assist

### **Steering wheel torque breakpoints, TrqBpts** — Steering wheel torque breakpoints `[-100 0 100]` (default) | 1-by-*M* vector

Steering wheel torque breakpoints, in N·m, specified as a
1-by-*M* vector.

#### Dependencies

To enable this parameter, select the **Power assist**
Block Option.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `TrqBpts` |
| **Values:** | `[-100 0 100]` (default) | 1-by-*M* vector |
| **Data Types:** | `double` |

### **Vehicle speed breakpoints, VehSpdBpts** — Vehicle speed breakpoints `[0 20]` (default) | 1-by-*N* vector

Vehicle speed breakpoints, in m/s, specified as a
1-by-*N* vector.

#### Dependencies

To enable this parameter, select the **Power assist**
Block Option.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `VehSpdBpts` |
| **Values:** | `[0 20]` (default) | 1-by-*N* vector |
| **Data Types:** | `double` |

### **Assisting torque table, TrqTbl** — Torque assist table `[0 -100;0 0;0 100]` (default) | *M*-by-*N* matrix

Torque assist table, *ƒtrq*, in
N·m, specified as an *M*-by-*N*
matrix.

The torque assist lookup table is a function of the vehicle speed,
*v*, and steering wheel input torque,
*τin*:

τast=ftrq(v,τin).

The block applies the steering wheel input torque and torque assist to the
pinion.

#### Dependencies

To enable this parameter, select the **Power assist**
Block Option.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `TrqTbl` |
| **Values:** | `[0 -100;0 0;0 100]` (default) | *M*-by-*N* matrix |
| **Data Types:** | `double` |

### **Assisting torque limit, TrqLmt** — Torque assist limit `100` (default) | scalar

Torque assist limit, in N·m, specified as a scalar.

#### Dependencies

To enable this parameter, select the **Power assist**
Block Option.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `TrqLmt` |
| **Values:** | `100` (default) | scalar |
| **Data Types:** | `double` |

### **Assisting power limit, PwrLmt** — Assist power limit `1000` (default) | scalar

Assist power limit, in watts, specified as a scalar.

#### Dependencies

To enable this parameter, select the **Power assist**
Block Option.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PwrLmt` |
| **Values:** | `1000` (default) | scalar |
| **Data Types:** | `double` |

### **Assisting torque efficiency, Eta** — Torque assist efficiency `1` (default) | scalar

Torque assist efficiency, specified as a scalar.

#### Dependencies

To enable this parameter, select the **Power assist**
Block Option.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Eta` |
| **Values:** | `1` (default) | scalar |
| **Data Types:** | `double` |

### **Cutoff frequency, CutOmege [rad/s]** — Cutoff frequency `200` (default) | scalar

Cutoff frequency, in rad/s, specified as a scalar.

#### Dependencies

To enable this parameter, select the **Power assist**
Block Option.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omega_c` |
| **Values:** | `200` (default) | scalar |
| **Data Types:** | `double` |

#### Ackerman Steering

### **Percent Ackerman parameterized by** — Ackermann parameterization `Constant` (default) | `Lookup table`

Whether to parameterize the Ackermann values as a constant value or by a
lookup table.

#### Dependencies

To enable this parameter, select the **Ackerman
steering** Block Option.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `AckParamType` |
| **Values:** | `Constant` (default) | `Lookup table` |
| **Data Types:** | `character vector` |

### **Percent Ackerman, PctAck** — Percent Ackermann `100` (default) | scalar

Percent Ackermann, specified as a scalar.

#### Dependencies

To enable this parameter, select the **Ackerman
steering** Block Option and set **Percent Ackerman
parameterized by** to
`Constant`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PctAck` |
| **Values:** | `100` (default) | scalar |
| **Data Types:** | `double` |

### **Percent Ackerman table, PctAckTbl** — Percent Ackermann table `ones(1,11)*100` (default) | 1-by-11 vector

Percent Ackermann table, specified as a 1-by-11 vector.

#### Dependencies

To enable this parameter, select the **Ackerman
steering** Block Option and set **Percent Ackerman
parameterized by** to `Lookup
table`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PctAckTbl` |
| **Values:** | `ones(1,11)*100` (default) | 1-by-11 vector |
| **Data Types:** | `double` |

#### Friction and Compliance

### **Sealing stiffness, SlgStf** — Sealing stiffness `1.5e4` (default) | scalar

Sealing stiffness, in N\*m/rad, specified as a scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `SlgStf` |
| **Values:** | `1.5e4` (default) | scalar |
| **Data Types:** | `double` |

### **Upper boundary friction, UpprFric** — Upper boundary friction `1` (default) | scalar

Upper boundary friction, in N, specified as a scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `UpprFric` |
| **Values:** | `1` (default) | scalar |
| **Data Types:** | `double` |

### **Pressure change due to friction boundary increase, PrsFric** — Pressure change due to friction boundary increase `1e-5` (default) | scalar

Pressure change due to friction boundary increase, in N/bar, specified as
a scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PrsFric` |
| **Values:** | `1e-5` (default) | scalar |
| **Data Types:** | `double` |

### **Maxwell element stiffness, MaxStf** — Maxwell element stiffness `10000` (default) | scalar

Maxwell element stiffness, in N\*m/rad, specified as a scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `MaxStf` |
| **Values:** | `10000` (default) | scalar |
| **Data Types:** | `double` |

### **Maxwell element upper boundary friction, MaxUpprFric** — Maxwell element upper boundary friction `0.2` (default) | scalar

Maxwell element upper boundary friction, in N, specified as a
scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `MaxUpprFric` |
| **Values:** | `0.2` (default) | scalar |
| **Data Types:** | `double` |

### **Maxwell linear damping coefficient, MaxDamp** — Maxwell linear damping coefficient `1` (default) | scalar

Maxwell linear damping coefficient, specified as a scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `MaxDamp` |
| **Values:** | `1` (default) | scalar |
| **Data Types:** | `double` |

### **Torsion bar stiffness coefficient, TorStf** — Torsional stiffness of steering shaft `30` (default) | scalar

Torsional stiffness of steering shaft, in N\*m/rad, specified as a
scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `TorStf` |
| **Values:** | `30` (default) | scalar |
| **Data Types:** | `double` |

### **Torsion bar damping coefficient, TorDamp** — Torsional viscous damping in steering shaft `1` (default) | scalar

Torsional viscous damping in steering shaft, in N\*m\*s/rad, specified as a
scalar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `TorDamp` |
| **Values:** | `1` (default) | scalar |
| **Data Types:** | `double` |

#### Steering Torque Controller

### **Integral anti-windup gain, A []** — Integral anti-windup gain `0` (default) | scalar

Integral anti-windup gain, specified as a scalar.

#### Dependencies

To enable this parameter, select **Steering inputs** > **Angle**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `A` |
| **Values:** | `0` (default) | scalar |
| **Data Types:** | `double` |

### **Derivative gain, D []** — Derivative gain `0.1` (default) | scalar

Derivative gain, specified as a scalar.

#### Dependencies

To enable this parameter, select **Steering inputs** > **Angle**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `D` |
| **Values:** | `0.1` (default) | scalar |
| **Data Types:** | `double` |

### **Integral gain, I []** — Integral gain `5` (default) | scalar

Integral gain, specified as a scalar.

#### Dependencies

To enable this parameter, select **Steering inputs** > **Angle**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `I` |
| **Values:** | `5` (default) | scalar |
| **Data Types:** | `double` |

### **Steering torque output saturation lower limit, OutSatLowLmt [Nm]** — Output saturation lower limit `-500` (default) | scalar

Steering torque output saturation lower limit, specified as a scalar, in
Nm.

#### Dependencies

To enable this parameter, select **Steering inputs** > **Angle**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutSatLowLmt` |
| **Values:** | `-500` (default) | scalar |
| **Data Types:** | `double` |

### **Steering torque output saturation upper limit, OutSatUpLmt [Nm]** — Steering torque output saturation upper limit 500 (default) | scalar

Steering torque output saturation upper limit, specified as a scalar, in
Nm.

#### Dependencies

To enable this parameter, select **Steering inputs** > **Angle**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `OutSatUpLmt` |
| **Values:** | 500 (default) | scalar |
| **Data Types:** | `double` |

### **Proportional gain, P []** — Proportional gain `150` (default) | scalar

Proportional gain, specified as a scalar.

#### Dependencies

To enable this parameter, select **Steering inputs** > **Angle**.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `P` |
| **Values:** | `150` (default) | scalar |
| **Data Types:** | `double` |
## Libraries

Vehicle Dynamics Blockset / Steering

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

### R2024a: New steering torque controller parameters

Starting in R2024a, the Steering System block includes these parameters that you can
specify to define a steering torque controller:

- **Integral antiwindup gain**
- **Derivative gain**
- **Integral gain**
- **Output saturation lower limit**
- **Output saturation upper limit**
- **Proportional gain**

## Description

Steering system for Ackermann and rack-and-pinion steering mechanisms

The Steering System block implements dynamic steering to calculate the wheel steer angles
for rack-and-pinion mechanisms with friction[4], compliance, and Ackermann steering features. The block uses the
steering wheel input angle or torque input, vehicle speed, caster angle, and right and
left wheel feedbacks to calculate the wheel steer angles. The block uses the vehicle
coordinate system.

If you select the **Power assist** parameter, you can specify a
torque assist lookup table that is a function of the vehicle speed and steering wheel
input torque. The block uses the steering wheel input torque and torque assist to
calculate the steering dynamics. If you select the **Ackerman
steering** parameter, you can specify a lookup table of percentage
Ackermann values to calculate the Ackermann steering effects, or a constant Ackermann
percentage, where 100 percent means perfect Ackermann steering.

If you select the **Power assist**, **Ackerman
steering**, or **Kingpin moment**[5] parameters in the **Input signals** section, you
can specify additional inputs for the external power assist torques, percent Ackermann
values, or kingpin moments.

Use the **Steered axle** parameter to
specify whether the front or rear axle is steered.

| Setting | Implementation |
| --- | --- |
| **Front** | Front axle steering  Figure of front steering turning right |
| **Rear** | Rear axle steering  Figure of rear steering turning right |

### Steering Type

**Rack-and-Pinion**

For rack-and-pinion steering, pinion rotation causes linear motion of the rack, which
steers the wheels through the tie rods and steering arms.

Figure of rack, rod, and arm in rack and pinion steering mechanism

Figure of rod in rack and pinion steering mechanism

To calculate the steered wheel angles, the block uses these equations.

l1=TW−lrack2−ΔPl22=l12+D2ΔP=rδinβ=π2−tan−1[Dl1]−cos−1[larm2+l22−lrod22larml2]

The illustration and equations use these variables.

|  |  |
| --- | --- |
| *δin* | Pinion angle (steering shaft angle into pinion) |
| *δL* | Left wheel steer angle |
| *δR* | Right wheel steer angle |
| *TW* | Track width |
| *r* | Pinion radius |
| *ΔP* | Linear change in rack position from "straight ahead" position |
| *D* | Longitudinal distance between rack and steered axle |
| *lrack* | Rack length (distance between inner tie-rod ends) |
| *larm* | Steering arm length |
| *lrod* | Tie rod length |

### Steering Effects

**Ackerman**

For ideal Ackerman steering, the wheel angles have a common turning circle.

Figure of Ackerman steering turning right around turning circle

To calculate the ideal wheel angles, the block uses these equations.

cot(δL)−cot(δR)=TWWBδAck=δinγδL=tan−1(WBtan(δAck)WB+0.5TWtan(δAck))δR=tan−1(WBtan(δAck)WB−0.5TWtan(δAck))

After the block calculates the ideal wheel angles, it uses the Ackerman
percentage to adjust the outside wheel angle.

δo=δi−pAck(δi−δAck)

The outside wheel angle depends on the turn direction.

- Right turn

  - Outside angle,
    *δo*, is left
    wheel angle,
    *δL*
  - Inside angle,
    *δi*, is right wheel
    angle, *δR*
- Left turn

  - Outside angle,
    *δo*, is right
    wheel angle,
    *δR*
  - Inside angle,
    *δi*, is left wheel
    angle, *δL*

The illustration and equations use these variables.

|  |  |
| --- | --- |
| *δin* | Steering angle |
| *δL* | Left wheel angle |
| *δR* | Right wheel angle |
| *δo* | Outside wheel angle |
| *δi* | Inside wheel angle |
| *pAck* | Ackerman percentage |
| *TW* | Track width |
| *WB* | Wheel base |
| *γ* | Steering ratio |

**Kingpin Moment and Tie Rod Force**

If you do not select the **Kingpin moment** parameter in the
**Input signals** section to specify right and left kingpin
moment inputs, the block implements the total kingpin moment using these equations:

Mkp=Mkpfx+Mkpfy+Mkpfz+Mkpmx+Mkpmy+MkpmzwhereMkpfx=0Mkpfy=−Fy(nTcos(ν))cos(δ)nT=Hl+(rsltan(ν))Mkpfz=−(Fzsin(λ)rssin(δ))+(Fzsin(ν)rscos(δ))rs=Kpoffset−(rsltan(λ))Mkpmx=0Mkpmy=0Mkpmz=Mzcos((λ2+ν2)0.5)

The illustration and equations use these variables.

|  |  |
| --- | --- |
| *Mkp* | Total kingpin moment |
| *Mkpfx* | Moment due to tractive force |
| *Mkpfy* | Moment due to cornering force |
| *Mkpfz* | Moment due to vertical force |
| *Mkpmx* | Tire overturning moment |
| *Mkpmy* | Tire rolling resistance moment |
| *Mkpmz* | Tire aligning moment |
| *Fy* | *Fy* tire input |
| *nT* | Caster trail |
| *ν* | Dynamic caster angle input |
| *δ* | Dynamic steering angle |
| *ƛ* | Kingpin inclination angle |
| *Fz* | *Fz* tire input |
| *rs* | Scrub radius |
| *Mz* | *Mz* tire input |
| *Kpoffset* | Kingpin offset |
| *Hl* | Hub lead |
| *rsl* | Static loaded radius |

The block implements the tie rod force using these equations:

Ftie=MkpLsacos(λ)cos(δ)whereLsa=(rskrcos(λ)cos(ν)π)

The illustration and equations use these variables.

|  |  |
| --- | --- |
| *Ftie* | Tie rod force |
| *Mkp* | Kingpin moment |
| *Lsa* | Swing arm length for rack and pinon steering |
| *ƛ* | Kingpin inclination angle |
| *δ* | Dynamic steering angle |
| *rs* | Overall steer ratio |
| *kr* | Rack gain |
| *ν* | Dynamic caster angle input |
