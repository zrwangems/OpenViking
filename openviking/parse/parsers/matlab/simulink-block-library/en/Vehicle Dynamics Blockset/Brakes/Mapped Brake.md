---
type: simulink-block
title: 'Rotational Brake'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Brakes'
documentation_page: 'rotationalbrake'
documentation_source_path: 'ref/rotationalbrake.html'
language: en
---

# Rotational Brake

## Ports

### Input

### **BrkPrs** — Brake pressure scalar | *N*-by-`1` vector

Brake pressure, in Pa.

Vector is the number of wheels,
*N*, by `1`. If you provide a scalar value, the
block assumes that number of wheels is one.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Disc`, `Drum`, or
`Mapped`.

### **Omega** — Wheel angular velocity scalar | *N*-by-`1` vector

Wheel angular velocity, *ω*, about wheel-fixed
*y*-axis, in rad/s.

Vector is the number of wheels,
*N*, by `1`. If you provide a scalar value, the
block assumes that number of wheels is one.

#### Dependencies

To enable this parameter, set **Rotation type** to
`No inertia`.

### **BrkTrqMax** — Maximum brake torque scalar | *N*-by-`1` vector

Maximum brake torque, in N·m. This torque represents the maximum available
resistive frictional braking torque and is applied accordingly to the rotational
dynamics. You do not need to consider the wheel direction.
**BrkTrqMax** differs from **BrkTrq**, which
is the instantaneous torque due to friction calculated based on speed, applied brake
pressure, or other friction brake characteristics.

Vector is the number of wheels,
*N*, by `1`. If you provide a scalar value, the
block assumes that number of wheels is one.

#### Dependencies

To enable this parameter, set **Brake Type** to
`External Torque`.

### **AxlTrq** — Axle torque scalar | *N*-by-`1` vector

Axle torque, *Ta*, about wheel spin axis,
in N·m.

Vector is the number of wheels,
*N*, by `1`. If you provide a scalar value, the
block assumes that number of wheels is one.

#### Dependencies

To enable this parameter, set **Rotation type** to
`Rotational Inertia`.

### **WhlTrq** — Wheel torque scalar | *N*-by-`1` vector

Wheel torque, in N·m. The wheel torque is the combined moment from a tire model
about the spin axis. This value includes the tractive and rolling resistance moments
as projected onto the spin axis plane.

Vector is the number of wheels,
*N*, by `1`. If you provide a scalar value, the
block assumes that number of wheels is one.

#### Dependencies

To enable this parameter, set **Rotation type** to
`Rotational Inertia`.
### Output

### **Info** — Block data bus

Bus containing these block values.

| Signal | | | Description | Units |
| --- | --- | --- | --- | --- |
| `Trq` | | `Axl` | Axle torque about body-fixed *y*-axis | N·m |
| `Whl` | Wheel torque about body-fixed *y*-axis | N·m |
| `Damp` | Damping torque about body-fixed *y*-axis | N·m |
| `Brk` | Brake torque about body-fixed *y*-axis | N·m |
| `Omega` | | | Wheel angular velocity about body-fixed *y*-axis | rad/s |
| `Omegadot` | | | Wheel angular acceleration about body-fixed *y*-axis | rad/s^2 |

#### Dependencies

To enable this parameter, select **Output Info bus**.

### **Omega** — Wheel angular velocity scalar | *N*-by-`1` vector

Wheel angular velocity, *ω*, about wheel-fixed
*y*-axis, in rad/s.

Vector is the number of wheels,
*N*, by `1`. If you provide a scalar value, the
block assumes that number of wheels is one.

#### Dependencies

To enable this parameter, set **Rotation type** to
`Rotational inertia` or set **Brake
Type** to `External torque`.

### **BrkTrqMax** — Maximum brake torque scalar | *N*-by-`1` vector

Maximum brake torque, in N·m. This torque represents the maximum available
resistive frictional braking torque and is applied accordingly to the rotational
dynamics. You do not need to consider the wheel direction.
**BrkTrqMax** differs from **BrkTrq**, which
is the instantaneous torque due to friction calculated based on speed, applied brake
pressure, or other friction brake characteristics.

Vector is the number of wheels,
*N*, by `1`. If you provide a scalar value, the
block assumes that number of wheels is one.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Disc`, `Drum`, or
`Mapped`.

## Parameters

To edit block parameters interactively, use the
Property Inspector. From the Simulink® Toolstrip, on the **Simulation** tab, in the
**Prepare** gallery, select **Property
Inspector**.

### Tire Options

### **Brake type** — Brake type `Disc` | `Drum` | `Mapped` | `External torque`

Use the **Brake Type** parameter
to select the brake type.

| Action | Brake Type Setting |
| --- | --- |
| Implement brake that converts the brake cylinder pressure into a braking force. | `Disc` |
| Implement simplex drum brake that converts the applied force and brake geometry into a net braking torque. | `Drum` |
| Implement lookup table that is a function of the wheel speed and applied brake pressure. | `Mapped` |
| Specify maximum available braking torque for brake implementation. | `External torque` |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `BrakeType` |
| **Values:** | `Disc` | `Drum` | `Mapped` | `External torque` |
| **Data Types:** | `char` |

### **Rotation type** — Rotation type `Rotational inertia` (default) | `No inertia`

Specify the rotation type as `Rotational inertia` or
`No inertia`

#### Dependencies

To enable this parameter, set **Brake type** to
`Disc`, `Drum`, or
`Mapped`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `rotType` |
| **Values:** | `Rotational inertia` (default) | `No inertia` |
| **Data Types:** | `char` |

### **Output Info bus** — Option to output Info bus `off` (default) | `on`

Select this parameter to enable the **Info** output port.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `extInfo` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `char` |

### Wheel and Tire Parameters

### **Wheel inertia, Iyy** — Wheel inertia scalar | *N*-by-`1` vector

Wheel inertia, specified as a scalar or
*N*-by-`1` vector, in
kg·m2. If you specify a scalar, the block uses that value
for all wheels. If you specify a vector, you must specify vectors for the other
rotational parameters.

*N* is the number of wheels and
must match the input signal dimensions.

#### Dependencies

To enable this parameter, set **Rotation type** to
`Rotational inertia`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Iyy` |
| **Values:** | scalar | *N*-by-`1` vector |
| **Data Types:** | `char` |

### **Axle viscous damping coefficient, br** — Axle viscous damping coefficient scalar | *N*-by-`1` vector

Axle viscous damping coefficient, specified as a scalar or
*N*-by-`1` vector, in N·m·s/rad. If you specify a
scalar, the block uses that value for all wheels. If you specify a vector, you must
specify vectors for the other rotational parameters.

*N* is the number of wheels and
must match the input signal dimensions.

#### Dependencies

To enable this parameter, set **Rotation type** to
`Rotational inertia`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `br` |
| **Values:** | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Wheel initial angular velocity, omegao** — Wheel initial angular velocity scalar | *N*-by-`1` vector

Wheel initial angular velocity, specified as a
scalar or *N*-by-`1` vector, in rad/s. If you
specify a scalar, the block uses that value for all wheels. If you specify a vector,
you must specify vectors for the other rotational parameters.

*N* is the number of wheels and
must match the input signal dimensions.

#### Dependencies

To enable this parameter, set **Rotation type** to
`Rotational inertia`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omegao` |
| **Values:** | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### Brake

### **Static friction coefficient, mu\_static** — Static friction coefficient `0.3` (default) | scalar | *N*-by-`1` vector

Static friction coefficient, specified as a
scalar or *N*-by-`1` vector, dimensionless. If you
specify a scalar, the block uses that value for all wheels. If you specify a vector,
you must specify vectors for the other brake parameters.

*N* is the number of wheels and
must match the input signal dimensions.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `mu_static` |
| **Values:** | `0.3` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Kinetic friction coefficient, mu\_kinetic** — Kinetic friction `0.2` (default) | scalar | *N*-by-`1` vector

Kinematic friction coefficient, specified as a
scalar or *N*-by-`1` vector, dimensionless. If you
specify a scalar, the block uses that value for all wheels. If you specify a vector,
you must specify vectors for the other brake parameters.

*N* is the number of wheels and
must match the input signal dimensions.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `mu_kinetic` |
| **Values:** | `0.2` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

#### Disc

### **Disc brake actuator bore, disc\_abore** — Bore distance `0.05` (default) | scalar | *N*-by-`1` vector

Disc brake actuator bore, specified as a scalar
or *N*-by-`1` vector, in m. If you specify a scalar,
the block uses that value for all wheels. If you specify a vector, you must specify
vectors for the other brake parameters.

*N* is the number of wheels and
must match the input signal dimensions.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Disc`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `disc_abore` |
| **Values:** | `0.05` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Brake pad mean radius, Rm** — Radius `0.177` (default) | scalar | *N*-by-`1` vector

Brake pad mean radius, specified as a scalar or
*N*-by-`1` vector, in m. If you specify a scalar,
the block uses that value for all wheels. If you specify a vector, you must specify
vectors for the other brake parameters.

*N* is the number of wheels and
must match the input signal dimensions.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Disc`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Rm` |
| **Values:** | `0.177` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Number of brake pads, num\_pads** — Number of brake pads `2` (default) | scalar | *N*-by-`1` vector

Number of brake pads, specified as a scalar or
*N*-by-`1` vector, dimensionless. If you specify a
scalar, the block uses that value for all wheels. If you specify a vector, you must
specify vectors for the other brake parameters.

*N* is the number of wheels and
must match the input signal dimensions.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Disc`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `num_pads` |
| **Values:** | `2` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

#### Drum

### **Drum brake actuator bore, drum\_abore** — Bore distance `0.0508` (default) | scalar | *N*-by-`1` vector

Drum brake actuator bore, specified as a scalar
or *N*-by-`1` vector, in m. If you specify a scalar,
the block uses that value for all wheels. If you specify a vector, you must specify
vectors for the other brake parameters.

*N* is the number of wheels and
must match the input signal dimensions.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Drum`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `drum_abore` |
| **Values:** | `0.0508` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Shoe pin to drum center distance, drum\_a** — Shoe pin to drum center distance `0.123` (default) | scalar

Shoe pin to drum center distance, in m.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Drum`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `drum_a` |
| **Values:** | `0.123` (default) | scalar |
| **Data Types:** | `double` |

### **Shoe pin center to force application point distance, drum\_c** — Shoe pin center to force application point distance `0.212` (default) | scalar

Shoe pin center to force application point distance, in m.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Drum`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `drum_c` |
| **Values:** | `0.212` (default) | scalar |
| **Data Types:** | `double` |

### **Drum internal radius, drum\_r** — Drum internal radius `0.15` (default) | scalar

Drum internal radius, in m.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Drum`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `drum_r` |
| **Values:** | `0.15` (default) | scalar |
| **Data Types:** | `double` |

### **Shoe pin to pad start angle, drum\_theta1** — Shoe pin to pad start angle `0` (default) | scalar

Shoe pin to pad start angle, in deg.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Drum`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `drum_theta1` |
| **Values:** | `0` (default) | scalar |
| **Data Types:** | `double` |

### **Shoe pin to pad end angle, drum\_theta2** — Shoe pin to pad end angle `126` (default) | scalar

Shoe pin to pad end angle, in deg.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Drum`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `drum_theta2` |
| **Values:** | `126` (default) | scalar |
| **Data Types:** | `double` |

#### Mapped

### **Brake actuator pressure breakpoints, brake\_p\_bpt** — Brake actuator pressure breakpoints vector

Brake actuator pressure breakpoints, in bar.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Mapped`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `brake_p_bpt` |
| **Values:** | vector |
| **Data Types:** | `double` |

### **Wheel speed breakpoints, brake\_n\_bpt** — Wheel speed breakpoints vector

Wheel speed breakpoints, in rpm.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Mapped`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `brake_n_bpt` |
| **Values:** | vector |
| **Data Types:** | `double` |

### **Brake torque map, f\_brake\_t** — Lookup table for brake torque array

The lookup table for the brake torque, fbrake(P,N), is a function of applied brake pressure and wheel speed, where:

- *T* is brake torque, in N·m.
- *P* is applied brake pressure, in bar.
- *N* is wheel speed, in rpm.

Plot showing brake torque as a function of wheel speed and applied brake pressure

#### Dependencies

To enable this parameter, set **Brake Type** to
`Mapped`.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_brake_t` |
| **Values:** | vector |
| **Data Types:** | `double` |

## Libraries

Vehicle Dynamics Blockset / Brakes

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

Rotational brake with disc, drum, mapped, or external torque modes

The Rotational Brake block implements a rotational frictional brake
actuator. The brake implementation is similar to that of the Combined Slip Wheel
2DOF block. Use this block to specify an external maximum brake torque to interact
with one of these tire models that does not have an integrated brake model:

- Combined Slip Wheel
  CPI model or Combined Slip Wheel
  STI model
- Simscape™
  Multibody™ model
- Third-party tire model

The Rotational Brake block supports four brake types with or without a
rotational degree of freedom.

| Block | Brake Type Setting | Rotation type Setting | Configuration | Brake Implementation |
| --- | --- | --- | --- | --- |
| Disc Brake | `Disc` | `Rotational inertia` | Disc brake block icon with rotational inertia selected. | Brake that converts the brake cylinder pressure into a braking torque. |
| `No inertia` | Disc brake block icon without inertia. |
| Drum Brake | `Drum` | `Rotational inertia` | Drum brake block icon with rotational inertia selected. | Simplex drum brake that converts the applied force and brake geometry into a net braking torque. |
| `No inertia` | Drum brake block icon without inertia. |
| Mapped Brake | `Mapped` | `Rotational inertia` | Mapped brake block icon with rotational inertia selected. | Lookup table that is a function of the wheel speed and applied brake pressure. |
| `No inertia` | Mapped brake block icon without inertia. |
| External Torque Brake | `External Torque` | Not applicable. Rotational inertia is always enabled. | External torque brake block icon | User-specified maximum available braking torque for brake implementation. |

### Brakes

**Disc**

If you specify the **Brake Type** parameter as
`Disc`, the block implements a disc brake. This figure shows
the side and front views of a disc brake.

Front and side view of disc brake, showing pad, disc, and caliper

A disc brake converts brake cylinder pressure from the brake cylinder into force. The
disc brake applies the force at the brake pad mean radius.

The block uses these equations to calculate brake torque for the disc brake.

T={μPπBa2RmNpads4                when N≠0μstaticPπBa2RmNpads4         when N=0

Rm=Ro+Ri2

The equations use these variables.

| Variable | Value |
| --- | --- |
| *T* | Brake torque |
| *P* | Applied brake pressure |
| *N* | Wheel speed |
| *Npads* | Number of brake pads in disc brake assembly |
| *μstatic* | Disc pad-rotor coefficient of static friction |
| *μ* | Disc pad-rotor coefficient of kinetic friction |
| *Ba* | Brake actuator bore diameter |
| *Rm* | Mean radius of brake pad force application on brake rotor |
| *Ro* | Outer radius of brake pad |
| *Ri* | Inner radius of brake pad |

**Drum**

If you specify the **Brake Type** parameter as
`Drum`, the block implements a static (steady-state) simplex
drum brake. A simplex drum brake consists of a single two-sided hydraulic actuator and two
brake shoes. The brake shoes do not share a common hinge pin.

The simplex drum brake model uses the applied force and brake geometry to calculate a
net torque for each brake shoe. The drum model assumes that the actuators and shoe
geometry are symmetrical for both sides, allowing a single set of geometry and friction
parameters to be used for both shoes.

The block implements equations that are derived from these equations in
*Fundamentals of Machine Elements*.

Trshoe=(πμcr(cosθ2−cosθ1)Ba22μ(2r(cosθ2−cosθ1)+a(cos2θ2−cos2θ1))+a(2θ1−2θ2+sin2θ2−sin2θ1))PTlshoe=(πμcr(cosθ2−cosθ1)Ba2−2μ(2r(cosθ2−cosθ1)+a(cos2θ2−cos2θ1))+a(2θ1−2θ2+sin2θ2−sin2θ1))P

T={Trshoe+Tlshoe                 when N≠0(Trshoe+Tlshoe)μstaticμ   when N=0

Side view of drum brake

The equations use these variables.

| Variable | Value |
| --- | --- |
| *T* | Brake torque |
| *P* | Applied brake pressure |
| *N* | Wheel speed |
| *μstatic* | Disc pad-rotor coefficient of static friction |
| *μ* | Disc pad-rotor coefficient of kinetic friction |
| *Trshoe* | Right shoe brake torque |
| *Tlshoe* | Left shoe brake torque |
| *a* | Distance from drum center to shoe hinge pin center |
| *c* | Distance from shoe hinge pin center to brake actuator connection on brake shoe |
| *r* | Drum internal radius |
| *Ba* | Brake actuator bore diameter |
| *Θ1* | Angle from shoe hinge pin center to start of brake pad material on shoe |
| *Θ2* | Angle from shoe hinge pin center to end of brake pad material on shoe |

**Mapped**

If you specify the **Brake Type** parameter as
`Mapped`, the block uses a lookup table to determine the brake
torque.

T={fbrake(P,N)                   when N≠0(μstaticμ)fbrake(P,N)    when N=0

The equations use these variables.

| Variable | Value |
| --- | --- |
| *T* | Brake torque |
| fbrake(P,N) | Brake torque lookup table |
| *P* | Applied brake pressure |
| *N* | Wheel speed |
| *μstatic* | Friction coefficient of drum pad-face interface under static conditions |
| *μ* | Friction coefficient of disc pad-rotor interface |

The lookup table for the brake torque, fbrake(P,N), is a function of applied brake pressure and wheel speed, where:

- *T* is brake torque, in N·m.
- *P* is applied brake pressure, in bar.
- *N* is wheel speed, in rpm.

Plot of brake torque as a function of wheel speed and applied brake pressure
