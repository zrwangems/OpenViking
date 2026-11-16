---
type: simulink-block
title: 'Dugoff Wheel 2DOF'
family: 'vdynblks'
product_id: 'vdynblks'
product_name: 'Vehicle Dynamics Blockset'
documentation_release: R2025b
official_category: 'Wheels and Tires'
documentation_page: 'dugoffwheel2dof'
documentation_source_path: 'ref/dugoffwheel2dof.html'
language: en
---

# Dugoff Wheel 2DOF

## Ports

### Input

### **BrkPrs** — Brake pressure scalar | *N*-by-`1` vector

Brake pressure, in Pa.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

#### Dependencies

To enable this port, set the **Brake Type** parameter, to one of
these types:

- `Disc`
- `Drum`
- `Mapped`

### **AxlTrq** — Axle torque scalar | *N*-by-`1` vector

Axle torque, *Ta*, about wheel spin axis, in N·m.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **Vx** — Longitudinal velocity scalar | *N*-by-`1` vector

Axle longitudinal velocity, *Vx*, along
tire-fixed *x*-axis, in m/s.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **Vy** — Lateral velocity scalar | *N*-by-`1` vector

Axle lateral velocity, *Vy*, along tire-fixed
*y*-axis, in m/s.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **Camber** — Inclination angle scalar | *N*-by-`1` vector

Camber angle, *ɣ*, or inclination angle, *ε*, in
rad.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **YawRate** — Tire angular velocity scalar | *N*-by-`1` vector

Tire angular velocity, *r*, about the tire-fixed
*z*-axis (yaw rate), in rad/s.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **Prs** — Tire inflation pressure scalar | *N*-by-`1` vector

Tire inflation pressure, *pi*, in Pa.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **Gnd** — Ground displacement scalar | *N*-by-`1` vector

Ground displacement along tire-fixed *z*-axis, in m. Positive input
produces wheel lift.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **Fext** — Axle force applied to tire scalar | *N*-by-`1` vector

Axle force applied to tire,
*Fext*, along vehicle-fixed
*z*-axis (positive input compresses the tire), in
N.

Vector is the number of wheels,
*N*, by `1`. If you provide a
scalar value, the block assumes that number of wheels is one.

#### Dependencies

To enable this parameter, set **Vertical Motion**
to `None` or `Mapped stiffness
and damping`.

### **RadialDeflct** — Tire radial deflection scalar | *N*-by-`1` vector

Tire radial deflection, *RadialDeflct*. This value is
used directly in the effective radius calculation.

Vector is the number of wheels,
*N*, by `1`. If you provide a
scalar value, the block assumes that number of wheels is one.

#### Dependencies

To enable this port, set **Vertical Motion** to
`External Deflection`.

### **ScaleFctrs** — Scale factor scalar | *N*-by-`1` vector

Scale factor to account for variations in the coefficient of
friction.

Vector is the number of wheels,
*N*, by `1`. If you provide a
scalar value, the block assumes that number of wheels is one.
### Output

### **Info** — Block data bus

Block data, returned as a bus signal containing these block values.

| Signal | Description | Units |
| --- | --- | --- |
| `AxlTrq` | Axle torque about wheel-fixed *y*-axis | N·m |
| `Omega` | Wheel angular velocity about wheel-fixed *y*-axis | rad/s |
| `Fx` | Longitudinal vehicle force along tire-fixed *x*-axis | N |
| `Fy` | Lateral vehicle force along tire-fixed *y*-axis | N |
| `Fz` | Vertical vehicle force along tire-fixed *z*-axis | N |
| `Mx` | Overturning moment about tire-fixed *x*-axis | N·m |
| `My` | Rolling resistance torque about tire-fixed *y*-axis | N·m |
| `Mz` | Aligning moment about tire-fixed *z*-axis | N·m |
| `Vx` | Vehicle longitudinal velocity along tire-fixed *x*-axis | m/s |
| `Vy` | Vehicle lateral velocity along tire-fixed *y*-axis | m/s |
| `Re` | Loaded effective radius | m |
| `Kappa` | Longitudinal slip ratio | NA |
| `Alpha` | Side slip angle | rad |
| `a` | Contact patch half length | m |
| `b` | Contact patch half width | m |
| `Gamma` | Camber angle | rad |
| `psidot` | Tire angular velocity about the tire-fixed *z*-axis (yaw rate) | rad/s |
| `BrkTrq` | Brake torque about the vehicle-fixed *y*-axis | N·m |
| `BrkPrs` | Brake pressure | Pa |
| `z` | Axle vertical displacement along tire-fixed *z*-axis | m |
| `zdot` | Axle vertical velocity along tire-fixed *z*-axis | m/s |
| `Gnd` | Ground displacement along tire-fixed *z*-axis (positive input produces wheel lift) | m |
| `GndFz` | Vertical sidewall force on ground along tire-fixed *z*-axis | N |
| `Prs` | Tire inflation pressure | Pa |
| `WhlTrq` | Wheel torque | N·m |
| `RL` | Loaded radius | m |
| `RadialDeflct` | Tire radial deflection | m |

### **Omega** — Wheel angular velocity scalar | *N*-by-`1` vector

Wheel angular velocity, *ω*, about wheel-fixed *y*-axis, in rad/s.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **Fx** — Longitudinal axle force scalar | *N*-by-`1` vector

Longitudinal force acting on axle, *Fx*, along
tire-fixed *x*-axis, in N. Positive force acts to move the vehicle
forward.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **Fy** — Lateral axle force scalar | *N*-by-`1` vector

Lateral force acting on axle, *Fy*, along
tire-fixed *y*-axis, in N.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **Fz** — Vertical axle force scalar | *N*-by-`1` vector

Vertical force acting on axle, *Fz*, along
tire-fixed *z*-axis, in N.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **Mx** — Overturning moment scalar | *N*-by-`1` vector

Longitudinal moment acting on axle, *Mx*,
about tire-fixed *x*-axis, in N·m.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **My** — Rolling resistive moment scalar | *N*-by-`1` vector

Lateral moment acting on axle, *My*, about
tire-fixed *y*-axis, in N·m.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

### **Mz** — Aligning moment scalar | *N*-by-`1` vector

Vertical moment acting on axle, *Mz*, about
tire-fixed *z*-axis, in N·m.

Vector is the number of wheels, *N*,
by `1`. If you provide a scalar value, the block assumes that number of
wheels is one.

## Parameters

### Block Options

### **Tire type** — Select type `User defined` (default) | `Light passenger car 205/60R15` | `Light passenger car 245/60R16` | `Mid-size passenger car 235/45R18` | `Performance car 225/40R19` | `SUV 265/50R20` | `Light truck 275/65R18` | `Commercial truck 295/75R22.5`

Use the **Tire type** parameter to either
input tire parameter values or select a fitted tire parameter set.

| Goal | Action |
| --- | --- |
| Input user-defined tire parameter values. | Update the block parameters with user-defined parameter values:  1. Set **Tire type** to `User    defined`. 2. In the **Wheel and Tire Parameters**    section, input user-defined values. 3. Click **Apply**. |
| Select one of the built-in Dugoff tire models to drive the lateral and longitudinal calculations. [Link]. | Update the applicable block parameters with values from a built-in tire model:  1. Set **Tire type** to the tire that you    want to implement. Options include:  - `Light passenger car      205/60R15`    - `Light passenger car      245/60R16`    - `Mid-size passenger car      235/45R18`    - `Performance car      225/40R19`    - `SUV      265/50R20`    - `Light truck      275/65R18`    - `Commercial truck      295/75R22.5` 2. Click **Update block with applicable tire    values**. In the **Wheel and Tire    Parameters** section, the block updates the    applicable **Longitudinal and Lateral**    parameters. 3. Click **Apply**. |

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `tireType` |
| **Values:** | `External file` (default) | `Light passenger car 205/60R15` | `Light passenger car 245/60R16` | `Mid-size passenger car 235/45R18` | `Performance car 225/40R19` | `SUV 265/50R20` | `Light truck 275/65R18` | `Commercial truck 295/75R22.5` |
| **Data Types:** | `character vector` |

### **Model slip type** — Model slip type `Nominal slip` | `Extended slip`

Use the **Model slip type** parameter to
select slip type.

| Action | Model Slip Type Setting |
| --- | --- |
| Calculate longitudinal and lateral forces under nominal slip conditions | `Nominal slip` |
| Calculate longitudinal and lateral forces with additional correction factors for a more accurate response at higher slip values | `Extended slip` |

#### Dependencies

Setting **Model slip type** to `Extended
slip` enables these parameters:

| Setting | Parameters Enabled |
| --- | --- |
| `Extended slip` | - **Longitudinal squared slip correction factor,   gx1** - **Longitudinal squared slip friction   correction factor, gx2** - **Longitudinal linear slip correction factor,   gx3** - **Longitudinal linear slip friction correction   factor, gx4** - **Longitudinal offset correction factor,   gx5** - **Lateral maximum friction correction factor,   gy1** - **Lateral offset correction factor,   gy2** |

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `slipType` |
| **Values:** | `Nominal slip` | `Extended slip` |
| **Data Types:** | `character vector` |

### **Brake type** — Brake type `None` | `Disc` | `Drum` | `Mapped`

Use the **Brake Type** parameter to select the
brake.

| Action | Brake Type Setting |
| --- | --- |
| No braking | `None` |
| Implement brake that converts the brake cylinder pressure into a braking force | `Disc` |
| Implement simplex drum brake that converts the applied force and brake geometry into a net braking torque | `Drum` |
| Implement lookup table that is a function of the wheel speed and applied brake pressure | `Mapped` |

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `BrakeType` |
| **Values:** | `None` | `Disc` | `Drum` | `Mapped` |
| **Data Types:** | `character vector` |

### **Rolling Resistance** — Rolling resistance torque `None` (default) | `Pressure and velocity` | `ISO 28580` | `Magic Formula` | `Mapped torque`

To calculate the rolling resistance torque, specify one of these **Rolling
Resistance** parameters.

| Setting | Block Implementation |
| --- | --- |
| `None` | None |
| `Pressure and velocity` | Method in *Stepwise Coastdown Methodology for Measuring Tire Rolling Resistance*. The rolling resistance is a function of tire pressure, normal force, and velocity. |
| `ISO 28580` | Method specified in ISO 28580:2018, *Passenger car, truck and bus tyre rolling resistance measurement method — Single point test and correlation of measurement results*. |
| `Magic Formula` | Magic formula equations from 4.E70 in *Tire and Vehicle Dynamics*. The magic formula is an empirical equation based on fitting coefficients. |
| `Mapped torque` | Lookup table that is a function of the normal force and spin axis longitudinal velocity. |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `rollingType` |
| **Values:** | `None` (default) | `Pressure and velocity` | `ISO 28580` | `Magic Formula` | `Mapped torque` |
| **Data Types:** | `character vector` |

#### Dependencies

Each **Rolling Resistance** setting enables additional
parameters.

| Setting | Parameters Enabled |
| --- | --- |
| `Pressure and velocity` | - **Velocity independent force coefficient,   aMy** - **Linear velocity force component,   bMy** - **Quadratic velocity force component,   cMy** - **Tire pressure exponent,   alphaMy** - **Normal force exponent,   betaMy** |
| `ISO 28580` | - **Parasitic losses force,   Fpl** - **Rolling resistance constant,   Cr** - **Thermal correction factor,   Kt** - **Measured temperature,   Tmeas** - **Parasitic losses force,   Fpl** - **Ambient temperature, Tamb** |
| `Magic Formula` | **Rolling resistance torque coefficient, QSY**  **Longitudinal force rolling resistance coefficient, QSY2**  **Linear rotational speed rolling resistance coefficient, QSY3**  **Quartic rotational speed rolling resistance coefficient, QSY4**  **Camber squared rolling resistance torque, QSY5**  **Load based camber squared rolling resistance torque, QSY6**  **Normal load rolling resistance coefficient, QSY7**  **Pressure load rolling resistance coefficient, QSY8**  **Rolling resistance scaling factor, lam\_My** |
| `Mapped torque` | **Spin axis velocity breakpoints, VxMy**  **Normal force breakpoints, FzMy**  **Rolling resistance torque map, MyMap** |

### **Vertical Motion** — Vertical motion model `None` (default) | `Mapped stiffness and damping` | `External deflection`

To calculate vertical motion, specify
one of these **Vertical Motion**
parameters.

| Setting | Block Implementation |
| --- | --- |
| `None` | Block passes the applied chassis forces directly through to the rolling resistance and longitudinal force calculations. |
| `Mapped stiffness and damping` | Vertical motion depends on wheel stiffness and damping. Stiffness is a function of tire sidewall displacement and pressure. Damping is a function of tire sidewall velocity and pressure. |
| `External deflection` | The block uses the defined sidewall deflection directly in the effective radius calculation. |

#### Dependencies

Setting **Vertical Motion** to
`Mapped stiffness and damping` enables
these parameters:

| Setting | Parameters Enabled |
| --- | --- |
| `Mapped stiffness and damping` | - **Wheel mass, MASS** - **Initial tire displacement,   zo** - **Initial velocity,   zdoto** - **Initial wheel vertical velocity   (wheel fixed frame), zdoto** - **Vertical deflection breakpoints,   zFz** - **Pressure breakpoints,   pFz** - **Force due to deflection,   Fzz** - **Vertical velocity breakpoints,   zdotFz** - **Force due to velocity,   Fzzdot** |

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `vertType` |
| **Values:** | `None` (default) | `Mapped stiffness and damping` | `External deflection` |
| **Data Types:** | `character vector` |

### Longitudinal and Lateral

### **Longitudinal stiffness, Ckappa** — Longitudinal stiffness `1e7` (default) | scalar | *N*-by-`1` vector

Longitudinal stiffness,
*Cκ*, specified as a
scalar or *N*-by-`1` vector, in N. If
you specify a scalar, the block uses that value for all wheels. If you
specify a vector, you must specify vectors for the other longitudinal
and lateral parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Ckappa` |
| **Values:** | `1e7` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Lateral stiffness per slip angle, Calpha** — Lateral stiffness `4.5e4` (default) | scalar | *N*-by-`1` vector

Lateral stiffness per slip angle,
*Cα*, specified as a
scalar or *N*-by-`1` vector, in N/rad.
If you specify a scalar, the block uses that value for all wheels. If
you specify a vector, you must specify vectors for the other
longitudinal and lateral parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Calpha` |
| **Values:** | `4.5e4` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Camber stiffness, Cgamma** — Camber stiffness `1e3` (default) | scalar | *N*-by-`1` vector

Camber stiffness,
*Cɣ*, specified as a
scalar or *N*-by-`1` vector, in N/rad.
If you specify a scalar, the block uses that value for all wheels. If
you specify a vector, you must specify vectors for the other
longitudinal and lateral parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Cgamma` |
| **Values:** | `1e3` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Maximum friction scaling coefficient, mu0** — Maximum friction scaling coefficient `0.8` (default) | scalar | *N*-by-`1` vector

Maximum friction scaling coefficient,
*μ0*, specified as a
scalar or *N*-by-`1` vector,
dimensionless. If you specify a scalar, the block uses that value for
all wheels. If you specify a vector, you must specify vectors for the
other longitudinal and lateral parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `mu0` |
| **Values:** | `0.8` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Friction reduction factor, As** — Friction reduction factor `0.01` (default) | scalar | *N*-by-`1` vector

Friction reduction factor,
*As*, specified as a
scalar or *N*-by-`1` vector,
dimensionless. If you specify a scalar, the block uses that value for
all wheels. If you specify a vector, you must specify vectors for the
other longitudinal and lateral parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `As` |
| **Values:** | `0.01` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Longitudinal relaxation length, Lrelx** — Longitudinal relaxation length `0.05` (default) | scalar | *N*-by-`1` vector

Longitudinal relaxation length,
*Lrelx*, specified as a
scalar or *N*-by-`1` vector, in m. If
you specify a scalar, the block uses that value for all wheels. If you
specify a vector, you must specify vectors for the other longitudinal
and lateral parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Lrelx` |
| **Values:** | `0.05` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Lateral relaxation length, Lrely** — Lateral relaxation length `0.15` (default) | scalar | *N*-by-`1` vector

Lateral relaxation length,
*Lrely*, specified as a
scalar or *N*-by-`1` vector, in m/rad.
If you specify a scalar, the block uses that value for all wheels. If
you specify a vector, you must specify vectors for the other
longitudinal and lateral parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Lrely` |
| **Values:** | `0.15` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

#### Extended slip

### **Longitudinal squared slip correction factor, gx1** — Longitudinal squared slip correction factor `1.14` (default) | scalar

Longitudinal squared slip correction factor,
*gx1*, dimensionless.

#### Dependencies

To enable this parameter, set **Tire type** to `User
defined` and **Model slip type**
to `Extended slip`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `gx1` |
| **Values:** | `1.14` (default) | scalar |
| **Data Types:** | `double` |

### **Longitudinal squared slip friction correction factor, gx2** — Longitudinal squared slip friction correction factor `-0.75` (default) | scalar

Longitudinal squared slip friction correction factor,
*gx2*, dimensionless.

#### Dependencies

To enable this parameter, set **Tire type** to `User
defined` and **Model slip type**
to `Extended slip`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `gx2` |
| **Values:** | `-0.75` (default) | scalar |
| **Data Types:** | `double` |

### **Longitudinal linear slip correction factor, gx3** — Longitudinal linear slip correction factor `1.63` (default) | scalar

Longitudinal linear slip correction factor,
*gx3*, dimensionless.

#### Dependencies

To enable this parameter, set **Tire type** to `User
defined` and **Model slip type**
to `Extended slip`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `gx3` |
| **Values:** | `1.63` (default) | scalar |
| **Data Types:** | `double` |

### **Longitudinal linear slip friction correction factor, gx4** — Longitudinal linear slip friction correction factor `-0.75` (default) | scalar

Longitudinal linear slip friction correction factor,
*gx4*, dimensionless.

#### Dependencies

To enable this parameter, set **Tire type** to `User
defined` and **Model slip type**
to `Extended slip`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `gx4` |
| **Values:** | `-0.75` (default) | scalar |
| **Data Types:** | `double` |

### **Longitudinal offset correction factor, gx5** — Longitudinal offset correction factor `1.5` (default) | scalar

Longitudinal offset correction factor,
*gx5*, dimensionless.

#### Dependencies

To enable this parameter, set **Tire type** to `User
defined` and **Model slip type**
to `Extended slip`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `gx5` |
| **Values:** | `1.5` (default) | scalar |
| **Data Types:** | `double` |

### **Lateral maximum friction correction factor, gy1** — Lateral maximum friction correction factor `-1.6` (default) | scalar

Lateral maximum friction correction factor,
*gy1*, dimensionless.

#### Dependencies

To enable this parameter, set **Tire type** to `User
defined` and **Model slip type**
to `Extended slip`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `gy1` |
| **Values:** | `-1.6` (default) | scalar |
| **Data Types:** | `double` |

### **Lateral offset correction factor, gy2** — Lateral offset correction factor `1.5` (default) | scalar

Lateral offset correction factor, *gy2*,
dimensionless.

#### Dependencies

To enable this parameter, set **Tire type** to `User
defined` and **Model slip type**
to `Extended slip`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `gy2` |
| **Values:** | `1.5` (default) | scalar |
| **Data Types:** | `double` |

### Rolling Resistance

#### Pressure and Velocity

### **Velocity independent force coefficient, aMy** — Velocity-independent force coefficient `84e-4` (default) | scalar

Velocity-independent force coefficient, *a*,
dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `aMy` |
| **Values:** | `84e-4` (default) | scalar |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to `Pressure
and velocity`.

### **Linear velocity force component, bMy** — Linear velocity force component `6.2e-4` (default) | scalar

Linear velocity force component, *b*, in s/m.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `bMy` |
| **Values:** | `6.2e-4` (default) | scalar |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to `Pressure
and velocity`.

### **Quadratic velocity force component, cMy** — Quadratic velocity force component `1.6e-4` (default) | scalar

Quadratic velocity force component, *c*, in s^2/m^2.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `cMy` |
| **Values:** | `1.6e-4` (default) | scalar |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to `Pressure
and velocity`.

### **Tire pressure exponent, alphaMy** — Tire pressure exponent `-0.003` (default) | scalar

Tire pressure exponent, *ɑ*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `alphaMy` |
| **Values:** | `-0.003` (default) | scalar |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to `Pressure
and velocity`.

### **Normal force exponent, betaMy** — Normal force exponent `0.97` (default) | scalar

Normal force exponent, *β*, dimensionless.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param` function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `betaMy` |
| **Values:** | `0.97` (default) | scalar |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to `Pressure
and velocity`.

#### ISO 28580

### **Parasitic losses force, Fpl** — Parasitic force loss `10` (default) | scalar

Parasitic force loss, *Fpl*, in N.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Fpl` |
| **Values:** | `10` (default) | scalar |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to `ISO
28580`.

### **Rolling resistance constant, Cr** — Rolling resistance constant `1e-3` (default) | scalar

Rolling resistance constant, *Cr*, in N/kN. ISO
28580 specifies the rolling resistance unit as one newton of tractive resistance for every
kiloNewtons of normal load.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Cr` |
| **Values:** | `1e-3` (default) | scalar |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to `ISO
28580`.

### **Thermal correction factor, Kt** — Thermal correction factor `0.008` (default) | scalar

Thermal correction factor, *Kt*, in
1/degC.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Kt` |
| **Values:** | `0.008` (default) | scalar |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to `ISO
28580`.

### **Measured temperature, Tmeas** — Temperature during testing `298.15` (default) | scalar

Measured ambient temperature, *Tmeas*, near tire
during tire testing, in K.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Tmeas` |
| **Values:** | `298.15` (default) | scalar |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to `ISO
28580`.

### **Ambient temperature, Tamb** — Temperature in application environment `298.15` (default) | scalar

Measured ambient temperature, *Tamb*, near tire
in application environment, in K. For example, the measured ambient temperature is the
ambient temperature near the tire when the vehicle is on the road.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Tamb` |
| **Values:** | `298.15` (default) | scalar |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to `ISO
28580`.

### **Input ambient temperature** — Option to input ambient temperature `off` (default) | on

Select to create input port **Tamb** to input the measured ambient
temperature.

The measured ambient temperature, *Tamb*, is the
temperature near tire in application environment, in K. For example, the measured ambient
temperature is the ambient temperature near the tire when the vehicle is on the road.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Tamb` |
| **Values:** | `off` (default) | on |
| **Data Types:** | `character vector` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to `ISO
28580`.

#### Magic Formula

### **Rolling resistance torque coefficient, QSY1** — Torque coefficient `0.007` (default) | scalar

Rolling resistance torque coefficient, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSY1` |
| **Values:** | `0.007` (default) | scalar |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to `Magic
Formula`.

### **Longitudinal force rolling resistance coefficient, QSY2** — Force resistance coefficient `0` (default) | scalar

Longitudinal force rolling resistance coefficient, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSY2` |
| **Values:** | `0` (default) | scalar |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to `Magic
Formula`.

### **Linear rotational speed rolling resistance coefficient, QSY3** — Linear speed coefficient `0.0015` (default) | scalar

Linear rotational speed rolling resistance coefficient, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSY3` |
| **Values:** | `0.0015` (default) | scalar |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to `Magic
Formula`.

### **Quartic rotational speed rolling resistance coefficient, QSY4** — Quartic speed coefficient `8.5e-05` (default) | scalar

Quartic rotational speed rolling resistance coefficient, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSY4` |
| **Values:** | `8.5e-05` (default) | scalar |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to `Magic
Formula`.

### **Camber squared rolling resistance torque, QSY5** — Camber resistance torque `0` (default) | scalar

Camber squared rolling resistance torque, in 1/rad^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSY5` |
| **Values:** | `0` (default) | scalar |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to `Magic
Formula`.

### **Load based camber squared rolling resistance torque, QSY6** — Load resistance torque `0` (default) | scalar

Load based camber squared rolling resistance torque, in 1/rad^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSY6` |
| **Values:** | `0` (default) | scalar |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to `Magic
Formula`.

### **Normal load rolling resistance coefficient, QSY8** — Normal resistance coefficient `0.9` (default) | scalar

Normal load rolling resistance coefficient, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSY8` |
| **Values:** | `0.9` (default) | scalar |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to `Magic
Formula`.

### **Pressure load rolling resistance coefficient, QSY8** — Pressure resistance coefficient `-0.4` (default) | scalar

Pressure load rolling resistance coefficient, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `QSY8` |
| **Values:** | `-0.4` (default) | scalar |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to `Magic
Formula`.

### **Rolling resistance scaling factor, lam\_My** — Scaling factor `1` (default) | scalar

Rolling resistance scaling factor, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `lam_My` |
| **Values:** | `1` (default) | scalar |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to `Magic
Formula`.

#### Mapped

### **Spin axis velocity breakpoints, VxMy** — Spin axis velocity breakpoints `-20:1:20` (default) | vector

Spin axis velocity breakpoints, in m/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `VxMy` |
| **Values:** | `-20:1:20` (default) | vector |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to `Mapped
torque`.

### **Normal force breakpoints, FzMy** — Normal force breakpoints `0:200:1e4` (default) | vector

Normal force breakpoints, in N.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `FzMy` |
| **Values:** | `0:200:1e4` (default) | vector |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to `Mapped
torque`.

### **Rolling resistance torque map, MyMap** — Rolling resistance torque map array

Rolling resistance torque versus axle speed and normal force, in N·m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `MyMap` |
| **Values:** | array |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to `Mapped
torque`.

### Aligning

### **Tire nominal section width, WIDTH** — Tire nominal section width scalar

Tire nominal section width, *WIDTH*, in m.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `WIDTH` |
| **Values:** | scalar |
| **Data Types:** | `double` |

### **Linear yaw rate resistance, bMz** — Linear yaw rate resistance `0` | scalar

Linear yaw rate resistance,
*bMz*, in N·m·s/rad.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `bMz` |
| **Values:** | `0` | scalar |
| **Data Types:** | `double` |

### Brake

### **Static friction coefficient, mu\_static** — Static friction coefficient `0.3` (default) | scalar | *N*-by-`1` vector

Static friction coefficient, specified as a
scalar or *N*-by-`1` vector, dimensionless. If
you specify a scalar, the block uses that value for all wheels. If you specify a
vector, you must specify vectors for the other brake parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Disc`, `Drum`, or
`Mapped`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `mu_static` |
| **Values:** | `0.3` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Kinetic friction coefficient, mu\_kinetic** — Kinetic friction `0.2` (default) | scalar | *N*-by-`1` vector

Kinematic friction coefficient, specified as
a scalar or *N*-by-`1` vector, dimensionless.
If you specify a scalar, the block uses that value for all wheels. If you
specify a vector, you must specify vectors for the other brake
parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Disc`, `Drum`, or
`Mapped`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `mu_kinetic` |
| **Values:** | `0.2` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

#### Disc

### **Disc brake actuator bore, disc\_abore** — Bore distance `0.05` (default) | scalar | *N*-by-`1` vector

Disc brake actuator bore, specified as a
scalar or *N*-by-`1` vector, in m. If you
specify a scalar, the block uses that value for all wheels. If you specify a
vector, you must specify vectors for the other brake parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Disc`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `disc_abore` |
| **Values:** | `0.05` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Brake pad mean radius, Rm** — Radius `0.177` (default) | scalar | *N*-by-`1` vector

Brake pad mean radius, specified as a scalar
or *N*-by-`1` vector, in m. If you specify a
scalar, the block uses that value for all wheels. If you specify a vector, you
must specify vectors for the other brake parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Disc`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Rm` |
| **Values:** | `0.177` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Number of brake pads, num\_pads** — Number of brake pads `2` (default) | scalar | *N*-by-`1` vector

Number of brake pads, specified as a scalar
or *N*-by-`1` vector, dimensionless. If you
specify a scalar, the block uses that value for all wheels. If you specify a
vector, you must specify vectors for the other brake parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Disc`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `num_pads` |
| **Values:** | `2` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

#### Drum

### **Drum brake actuator bore, drum\_abore** — Bore distance `0.0508` (default) | scalar | *N*-by-`1` vector

Drum brake actuator bore, specified as a
scalar or *N*-by-`1` vector, in m. If you
specify a scalar, the block uses that value for all wheels. If you specify a
vector, you must specify vectors for the other brake parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Dependencies

To enable this parameter, set **Brake Type** to
`Drum`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

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

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

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

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

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

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

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

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

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

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

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

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

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

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `brake_n_bpt` |
| **Values:** | vector |
| **Data Types:** | `double` |

### **Brake torque map, f\_brake\_t** — Lookup table for brake torque array

The lookup table for the brake
torque, fbrake(P,N), is a function of applied brake pressure and wheel speed, where:

- *T* is brake torque, in N·m.
- *P* is applied brake pressure, in bar.
- *N* is wheel speed, in rpm.

Plot showing brake torque as a function of wheel speed and applied brake pressure

#### Dependencies

To enable this parameter, set **Brake Type** to
`Mapped`.

#### Programmatic Use

To set the block parameter
value programmatically, use the `set_param`
function.

To get the block parameter
value programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_brake_t` |
| **Values:** | vector |
| **Data Types:** | `double` |

### Wheel

### **Rotational damping, br** — Rotational damping scalar | *N*-by-`1` vector

Rotational damping, specified as a scalar or
*N*-by-`1` vector, in N·m·s/rad. If you specify a
scalar, the block uses that value for all wheels. If you specify a vector, you must
specify vectors for the other rotational parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `br` |
| **Values:** | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Tire rotational inertia (rolling axis), IYY** — Tire rotational inertia scalar | *N*-by-`1` vector

Tire rotational inertia (rolling axis), specified as
a scalar or *N*-by-`1` vector, in
kg·m2. If you specify a scalar, the block uses that value
for all wheels. If you specify a vector, you must specify vectors for the other
rotational parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `IYY` |
| **Values:** | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Initial wheel rotational velocity, omegao** — Initial wheel rotational velocity scalar | *N*-by-`1` vector

Initial wheel rotational velocity, specified as a
scalar or *N*-by-`1` vector, in rad/s. If you specify
a scalar, the block uses that value for all wheels. If you specify a vector, you must
specify vectors for the other rotational parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omegao` |
| **Values:** | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Tire unloaded radius, UNLOADED\_RADIUS** — Tire unloaded radius `0.309384029954441` (default) | scalar

Tire unloaded radius, in m.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `UNLOADED_RADIUS` |
| **Values:** | `0.309384029954441` (default) | scalar |
| **Data Types:** | `double` |

### Vertical

### **Tire mass, MASS** — Tire mass `9.46491996974568` (default) | scalar | *N*-by-`1` vector

Tire mass, specified as a scalar or
*N*-by-`1` vector, in kg. If you
specify a scalar, the block uses that value for all wheels. If you
specify a vector, you must specify vectors for the other vertical
parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Dependencies

To enable this parameter, set **Vertical Motion** to `Mapped
stiffness and damping`.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `MASS` |
| **Values:** | `9.46491996974568` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Initial tire displacement, zo** — Initial tire displacement `0` (default) | scalar | *N*-by-`1` vector

Initial tire displacement, specified
as a scalar or *N*-by-`1` vector, in
m. If you specify a scalar, the block uses that value for all wheels. If
you specify a vector, you must specify vectors for the other vertical
parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Dependencies

To enable this parameter, set **Vertical Motion** to `Mapped
stiffness and damping`.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `zo` |
| **Values:** | `0` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Initial wheel vertical velocity (wheel fixed frame), zdoto** — Initial wheel vertical velocity `0` (default) | scalar | *N*-by-`1` vector

Initial wheel vertical velocity,
specified as a scalar or *N*-by-`1`
vector, in m/s. If you specify a scalar, the block uses that value for
all wheels. If you specify a vector, you must specify vectors for the
other vertical parameters.

*N* is the number of wheels and must match the input signal dimensions.

#### Dependencies

To enable this parameter, set **Vertical Motion** to `Mapped
stiffness and damping`.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `zdoto` |
| **Values:** | `0` (default) | scalar | *N*-by-`1` vector |
| **Data Types:** | `double` |

### **Gravitational acceleration, GRAVITY** — Gravitational acceleration `-9.81` (default) | scalar

Gravitational acceleration, in m/s^2.

#### Dependencies

To enable this parameter, set **Vertical Motion** to `Mapped
stiffness and damping`.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `GRAVITY` |
| **Values:** | `-9.81` (default) | scalar |
| **Data Types:** | `double` |

#### Mapped Stiffness and Damping

### **Vertical deflection breakpoints, zFz** — Vertical deflection breakpoints `[0 .01 .1]` (default) | vector

Vector of sidewall deflection breakpoints corresponding to the force
table, in m.

#### Dependencies

To enable this parameter, set **Vertical Motion** to `Mapped
stiffness and damping`.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `zFz` |
| **Values:** | `[0 .01 .1]` (default) | vector |
| **Data Types:** | `double` |

### **Pressure breakpoints, pFz** — Pressure breakpoints `[10000 1000000]` (default) | vector

Vector of pressure data points corresponding to the force table, in
Pa.

#### Dependencies

To enable this parameter, set **Vertical Motion** to `Mapped
stiffness and damping`.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `pFz` |
| **Values:** | `[10000 1000000]` (default) | vector |
| **Data Types:** | `double` |

### **Force due to deflection, Fzz** — Force due to deflection `[0 1e3 1e4; 0 1e4 1e5]` (default) | vector

Force due to sidewall deflection and pressure along wheel-fixed
*z*-axis, in N.

#### Dependencies

To enable this parameter, set **Vertical Motion** to `Mapped
stiffness and damping`.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Fzz` |
| **Values:** | `[0 1e3 1e4; 0 1e4 1e5]` (default) | vector |
| **Data Types:** | `double` |

### **Vertical velocity breakpoints, zdotFz** — Vertical velocity breakpoints `[-20 0 20]` (default) | vector

Vector of sidewall velocity breakpoints corresponding to the force due
to velocity table, in m.

#### Dependencies

To enable this parameter, set **Vertical Motion** to `Mapped
stiffness and damping`.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `zdotFz` |
| **Values:** | `[-20 0 20]` (default) | vector |
| **Data Types:** | `double` |

### **Force due to velocity, Fzzdot** — Force due to velocity `[500 0 -500;250 0 -250]` (default) | array

Force due to sidewall velocity and pressure along wheel-fixed
*z*-axis, in N.

#### Dependencies

To enable this parameter, set **Vertical Motion** to `Mapped
stiffness and damping`.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `Fzzdot` |
| **Values:** | `[500 0 -500;250 0 -250]` (default) | array |
| **Data Types:** | `double` |

### Simulation Setup

### **Maximum normal force, FZMAX** — Maximum normal force `10000` (default) | scalar

Maximum normal force, in N. Used with all vertical force calculations.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `FZMAX` |
| **Values:** | `10000` (default) | scalar |
| **Data Types:** | `double` |

### **Minimum normal force, FZMIN** — Minimum normal force `0` (default) | scalar

Minimum normal force, in N. Used with all vertical force calculations.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `FZMIN` |
| **Values:** | `0` (default) | scalar |
| **Data Types:** | `double` |

### **Maximum pressure, PRESMAX** — Maximum pressure `1003118` (default) | scalar

Maximum pressure, *PRESMAX*, in Pa.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PRESMAX` |
| **Values:** | `1003118` (default) | scalar |
| **Data Types:** | `double` |

### **Minimum pressure, PRESMIN** — Minimum pressure `9982` (default) | scalar

Minimum pressure, *PRESMIN*, in Pa.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PRESMIN` |
| **Values:** | `9982` (default) | scalar |
| **Data Types:** | `double` |

### **Max allowable slip ratio (absolute), KPUMAX** — Max allowable slip ratio `0.999` (default) | scalar

Max allowable slip ratio (absolute), *KPUMAX*, dimensionless.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `KPUMAX` |
| **Values:** | `0.999` (default) | scalar |
| **Data Types:** | `double` |

### **Minimum allowable slip ratio (absolute), KPUMIN** — Minimum allowable slip ratio `-0.999` (default) | scalar

Minimum allowable slip ratio (absolute), *KPUMIN*,
dimensionless.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `KPUMIN` |
| **Values:** | `-0.999` (default) | scalar |
| **Data Types:** | `double` |

### **Max allowable slip angle (absolute), ALPMAX** — Max allowable slip angle `1.5708` (default) | scalar

Max allowable slip angle (absolute), *ALPMAX*, in rad.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ALPMAX` |
| **Values:** | `1.5708` (default) | scalar |
| **Data Types:** | `double` |

### **Minimum allowable slip angle (absolute), ALPMIN** — Minimum allowable slip angle `-1.5708` (default) | scalar

Minimum allowable slip angle (absolute), *ALPMIN*, in rad.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `ALPMIN` |
| **Values:** | `-1.5708` (default) | scalar |
| **Data Types:** | `double` |

### **Maximum allowable camber angle, CAMMAX** — Maximum allowable camber angle `0.173` | scalar

Maximum allowable camber angle *CAMMAX*, in rad.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CAMMAX` |
| **Values:** | `0.173` | scalar |
| **Data Types:** | `double` |

### **Minimum allowable camber angle, CAMMIN** — Minimum allowable camber angle `-0.173` | scalar

Minimum allowable camber angle, *CAMMIN*, in rad.

#### Programmatic Use

To set the block parameter value
programmatically, use the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `CAMMIN` |
| **Values:** | `-0.173` | scalar |
| **Data Types:** | `double` |

### **Minimum ambient temperature, TMIN** — Minimum ambient temperature `0` (default) | scalar

Minimum ambient temperature, *TMIN*, in
K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `TMIN` |
| **Values:** | `0` (default) | scalar |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to `ISO
28580`.

### **Maximum ambient temperature, TMAX** — Maximum ambient temperature `400` (default) | scalar

Maximum ambient temperature, *TMAX*, in
K.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `TMAX` |
| **Values:** | `400` (default) | scalar |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Rolling Resistance** to
`ISO 28580`.

### Plotting

### **Install Extended Tire Features** — Option to install Extended Tire Features for Vehicle Dynamics Blockset™ support package button

Click **Install Extended Tire Features** to install the
Extended Tire Features for Vehicle Dynamics Blockset support package. With the support package, you can plot
steady-state force and moment tire responses from the Dugoff Wheel 2DOF Block
Parameters dialog box.

### **Plot steady state force, moment response** — Option to plot steady-state force and moment tire responses button

Click **Plot steady state force, moment response** to
generate these plots:

- **Lateral force [N] vs Slip angle [rad]**
- **Self-aligning moment [Nm] vs Slip angle
  [rad]**
- **Longitudinal force [N] vs Longitudinal slip
  []**
- **Longitudinal force [N] vs Lateral force
  [N]**

#### Dependencies

To enable this parameter, click **Install Extended Tire
Features**.

## Libraries

Vehicle Dynamics Blockset / Wheels and Tires

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

### R2024b: New **Tire type** option

Starting in R2024b, you can specify **Tire type** to use the new built-in
tire model, `Light passenger car 245/60R16`.

### R2024b: New **Vertical Motion** option

Starting in R2024b, specifying **Vertical Motion** as `External Deflection` enables the **RadialDeflct** port. Use this port to define the sidewall deflection when interfacing with a tire in cases where forces are not provided.

### R2024b: New signals added to the **Info** port bus

Starting in R2024b, the **Info** port bus contains these new signals.

| Signal | Description |
| --- | --- |
| `RadialDeflct` | Tire radial deflection |
| `RL` | Loaded radius |
| `WhlTrq` | Wheel torque |

### R2024b: Renamed block parameters

Starting in R2024b, these parameters have been renamed.

| Old Name | New Name |
| --- | --- |
| **Wheel width** | **Tire nominal section width** |
| **Unloaded radius** | **Tire unloaded radius** |
| **Initial rotational velocity** | **Initial wheel rotational velocity** |
| **Wheel mass** | **Tire mass** |
| **Rotational inertia** | **Tire rotational inertia** |

### R2024a: Block parameter update

Starting in R2024a, the options `Nominal slip` and
`Extended slip` are available for the new parameter
**Model slip type** instead of **Tire
type**.

These options are now available for **Tire type**:

- `User defined`
- `Light passenger car 205/60R15`
- `Mid-size passenger car 235/45R18`
- `Performance car 225/40R19`
- `SUV 265/50R20`
- `Light truck 275/65R18`
- `Commercial truck 295/75R22.5`

### R2024a: Plot steady-state force and moment responses

If you have the Extended Tire Features for Vehicle Dynamics Blockset support package installed, you can use the new **Plot
steady state force, moment response** button to generate plots.

## Description

Dugoff Wheel 2DOF wheel with disc, drum, or mapped brake

The Dugoff Wheel 2DOF block implements a simplified tire with lateral
and longitudinal slip capability based on the H. Dugoff model[1]. The block uses a translational friction model to calculate the
forces and moments during combined longitudinal and lateral slip, requiring fewer
parameters than the Combined Slip Wheel 2DOF block. If you do not have
the tire coefficients needed by the Magic Formula, consider using this block for studies
that do not involve extensive nonlinear combined lateral slip or lateral dynamics. If
your study does require nonlinear combined slip or lateral dynamics, consider using the
Combined Slip Wheel 2DOF block.

The block determines the wheel rotation rate, vertical motion, and forces and moments
in all six degrees-of-freedom (DOFs) based on the driveline torque, brake pressure, road
height, wheel camber angle, and inflation pressure. You can use this block for these
types of analyses:

- Driveline and vehicle simulations that require low frequency tire-road and
  braking forces for vehicle acceleration, braking, and wheel rolling
  resistance calculations with minimal tire parameters.
- Wheel interaction with an idealized road surface.
- Ride and handling maneuvers for vehicles undergoing mild combined slip.
  For this analysis, you can connect the block to driveline and chassis
  components such as differentials, suspension, and vehicle body
  systems.
- Yaw stability. For this analysis, you can connect this block to more
  detailed braking system models.
- Tire stiffness and unsprung mass interactions with ground variations, load
  transfer, or chassis motion using the block vertical DOF.

The block integrates rotational wheel, vertical mass, and braking dynamics
models.

You can set your own user-defined model parameter values or use a built-in tire
model.

If you install the Extended Tire Features for Vehicle Dynamics Blockset support package, these additional capabilities are available:

- Plot generation — Click the **Plot steady state force, moment
  response** button to generate these plots:

  - **Lateral force [N] vs Slip angle [rad]**
  - **Self-aligning moment [Nm] vs Slip angle
    [rad]**
  - **Longitudinal force [N] vs Longitudinal slip
    []**
  - **Longitudinal force [N] vs Lateral force
    [N]**
- Import tire parameters — Use the `tireModel.get` method to import tire parameter values defined in the
  Dugoff Wheel 2DOF block to a `tireModel` object.
- Export tire parameters — Use the `set`
  method to export tire parameter values from a `tireModel` object to
  the Dugoff Wheel 2DOF block.
- Tire model conversion — Use the `convert` method to convert a tire model of one of these types to a
  Dugoff tire model that you can import to the Dugoff Wheel 2DOF block:

  - Magic Formula 5.2
  - Magic Formula 6.2
  - Fiala

Use the **Tire type** parameter to either
input tire parameter values or select a fitted tire parameter set.

| Goal | Action |
| --- | --- |
| Input user-defined tire parameter values. | Update the block parameters with user-defined parameter values:  1. Set **Tire type** to `User    defined`. 2. In the **Wheel and Tire Parameters**    section, input user-defined values. 3. Click **Apply**. |
| Select one of the built-in Dugoff tire models to drive the lateral and longitudinal calculations. [Link]. | Update the applicable block parameters with values from a built-in tire model:  1. Set **Tire type** to the tire that you    want to implement. Options include:  - `Light passenger car      205/60R15`    - `Light passenger car      245/60R16`    - `Mid-size passenger car      235/45R18`    - `Performance car      225/40R19`    - `SUV      265/50R20`    - `Light truck      275/65R18`    - `Commercial truck      295/75R22.5` 2. Click **Update block with applicable tire    values**. In the **Wheel and Tire    Parameters** section, the block updates the    applicable **Longitudinal and Lateral**    parameters. 3. Click **Apply**. |

Use the **Model slip type** parameter to
select slip type.

| Action | Model Slip Type Setting |
| --- | --- |
| Calculate longitudinal and lateral forces under nominal slip conditions | `Nominal slip` |
| Calculate longitudinal and lateral forces with additional correction factors for a more accurate response at higher slip values | `Extended slip` |

Use the **Brake Type** parameter to select the
brake.

| Action | Brake Type Setting |
| --- | --- |
| No braking | `None` |
| Implement brake that converts the brake cylinder pressure into a braking force | `Disc` |
| Implement simplex drum brake that converts the applied force and brake geometry into a net braking torque | `Drum` |
| Implement lookup table that is a function of the wheel speed and applied brake pressure | `Mapped` |

To calculate the rolling resistance torque, specify one of these **Rolling
Resistance** parameters.

| Setting | Block Implementation |
| --- | --- |
| `None` | None |
| `Pressure and velocity` | Method in *Stepwise Coastdown Methodology for Measuring Tire Rolling Resistance*. The rolling resistance is a function of tire pressure, normal force, and velocity. |
| `ISO 28580` | Method specified in ISO 28580:2018, *Passenger car, truck and bus tyre rolling resistance measurement method — Single point test and correlation of measurement results*. |
| `Magic Formula` | Magic formula equations from 4.E70 in *Tire and Vehicle Dynamics*. The magic formula is an empirical equation based on fitting coefficients. |
| `Mapped torque` | Lookup table that is a function of the normal force and spin axis longitudinal velocity. |

To calculate vertical
motion, specify one of these **Vertical Motion**
parameters.

| Setting | Block Implementation |
| --- | --- |
| `None` | Block passes the applied chassis forces directly through to the rolling resistance and longitudinal force calculations. |
| `Mapped stiffness and damping` | Vertical motion depends on wheel stiffness and damping. Stiffness is a function of tire sidewall displacement and pressure. Damping is a function of tire sidewall velocity and pressure. |
| `External deflection` | The block uses the defined sidewall deflection directly in the effective radius calculation. |

### Rotational Wheel Dynamics

The block calculates the inertial response of the wheel subject to:

- Axle losses
- Brake and drive torque
- Tire rolling resistance
- Ground contact through the tire-road interface

The input torque is the summation of the applied axle torque, braking torque, and
moment arising from the combined tire torque.

Ti=Ta−Tb+Td

For the moment arising from the combined tire torque, the block implements
tractive wheel forces and rolling resistance with first-order dynamics. The rolling
resistance has a time constant parameterized in terms of a relaxation length.

Td(s)=1Le|ω|Res+1(FxRe+My)

To calculate the rolling resistance torque, you can specify one
of these **Rolling Resistance** parameters.

| Setting | Block Implementation |
| --- | --- |
| `None` | Block sets rolling resistance, `My`, to zero. |
| `Pressure and velocity` | Block uses the method in SAE *Stepwise Coastdown Methodology for Measuring Tire Rolling Resistance*. The rolling resistance is a function of tire pressure, normal force, and velocity, specifically:  My=Re{a+b|Vx|+cVx2}{Fzβpiα}tanh(4Vx) |
| `ISO 28580` | Block uses the method specified in ISO 28580:2018, *Passenger car, truck and bus tyre rolling resistance measurement method — Single point test and correlation of measurement results*. The method accounts for normal load, parasitic loss, and thermal corrections from test conditions, specifically:  My=Re(FzCr1+Kt(Tamb−Tmeas)−Fpl)tanh(ω) |
| `Magic Formula` | Block calculates the rolling resistance, `My`, using the Magic Formula equations from 4.E70 in *Tire and Vehicle Dynamics*. The magic formula is an empirical equation based on fitting coefficients. |
| `Mapped torque` | For the rolling resistance, `My`, the block uses a lookup table that is a function of the normal force and spin axis longitudinal velocity. |

If the brakes are enabled, the block determines the braking locked or unlocked
condition based on an idealized dry clutch friction model. Based on the lock-up
condition, the block implements these friction and dynamic models.

| Equation | Lock-Up Condition | Friction Model | Dynamic Model |
| --- | --- | --- | --- |
| ω≠0orTS<|Ti+Tf−ωb| | Unlocked | Tf=Tk,whereTk=FcReffμktanh[4(−ωd)]Ts=FcReffμsReff=2(Ro3−Ri3)3(Ro2−Ri2) | ω˙J=−ωb+Ti+To |
| ω=0andTS≥|Ti+Tf−ωb| | Locked | Tf=Ts | ω=0 |

The equations use these variables.

| Variable | Value |
| --- | --- |
| *ω* | Wheel angular velocity |
| *a* | Velocity-independent force component |
| *b* | Linear velocity force component |
| *c* | Quadratic velocity force component |
| *Le* | Tire relaxation length |
| *J* | Moment of inertia |
| *My* | Rolling resistance torque |
| *Ta* | Applied axle torque |
| *Tb* | Braking torque |
| *Td* | Combined tire torque |
| *Tf* | Frictional torque |
| *Ti* | Net input torque |
| *Tk* | Kinetic frictional torque |
| *To* | Net output torque |
| *Ts* | Static frictional torque |
| *Fc* | Applied clutch force |
| *Fx* | Longitudinal force developed by the tire road interface due to slip |
| *Reff* | Effective clutch radius |
| *Ro* | Annular disk outer radius |
| *Ri* | Annular disk inner radius |
| *Re* | Effective tire radius while under load and for a given pressure |
| *Vx* | Longitudinal axle velocity |
| *Fz* | Vehicle normal force |
| *Cr* | Rolling resistance constant |
| *Tamb* | Ambient temperature |
| *Tmeas* | Measured temperature for rolling resistance constant |
| *Fpl* | Parasitic force loss |
| *Kt* | Thermal correction factor |
| *ɑ* | Tire pressure exponent |
| *β* | Normal force exponent |
| *pi* | Tire pressure |
| *μs* | Coefficient of static friction |
| *μk* | Coefficient of kinetic friction |

### Longitudinal Force

The block implements the longitudinal force as a function of wheel slip relative
to the road surface using these equations.

| Calculation | Equation |
| --- | --- |
| Nominal Slip | Fx=Ckκ1−κf(z),wheref(z)={z(2−z)                when z<11                           when z≥1z=μFz(1−κ)2(Ckκ)2+(Cαtan(α))2 |
| Extended | Fx=Ckκ1−κf(z)gx,wheref(z)={z(2−z)                when z<11                           when z≥1z=μFz(1−κ)2(Ckκ)2+(Cαtan(α))2gx=(gx1+gx2μ)κ2−(gx3+gx4μ)κ+gx5 |
| Friction coefficient | μ=μ0(1−AsVs),whereVs=uκ2+tan2(α) |

The equations use these variables.

| Variable | Value |
| --- | --- |
| *Fx* | Longitudinal force acting on axle along tire-fixed *x*-axis |
| *Cκ* | Longitudinal stiffness |
| *Cα* | Lateral stiffness per slip angle |
| *k* | Longitudinal slip ratio of tires |
| *Fz* | Vertical contact patch normal force along tire-fixed *z*-axis |
| *u* | Velocity component in the wheel plane |
| *μ* | Maximum friction coefficient |
| *μ0* | Maximum friction scaling coefficient |
| *As* | Friction reduction factor |
| *Vs* | Friction reduction magnitude |
| *α* | Side slip angle of tires |
| *gx* | Longitudinal correction factor |
| *gx1* | Longitudinal squared slip correction factor |
| *gx2* | Longitudinal squared slip friction correction factor |
| *gx3* | Longitudinal linear slip correction factor |
| *gx4* | Longitudinal linear slip friction correction factor |
| *gx5* | Longitudinal offset correction factor |

### Lateral Force

The block implements the lateral force as a function of wheel slip angle state
using these equations.

| Calculation | Equation |
| --- | --- |
| Nominal Slip | Fy=Cαtan(α)1−κf(z)+γCγ,wheref(z)={z(2−z)                 when z<11                            when z≥1z=μFz(1−κ)2(Ckκ)2+(Cαtan(α))2 |
| Extended Slip | Fy=Cαtan(α)1−κf(z)gy+γCγ,wheref(z)={z(2−z)                when z<11                           when z≥1z=μFz(1−κ)2(Ckκ)2+(Cαtan(α))2gy=(μ+gy1)tan(α)+gy2 |
| Friction Coefficient | μ=μ0(1−AsVs),whereVs=uκ2+tan2(α) |

The equations use these variables.

| Variable | Value |
| --- | --- |
| *α* | Side slip angle of tires |
| *Fy* | Lateral force acting on axle along tire-fixed *y*-axis |
| *Fz* | Vertical contact patch normal force along tire-fixed *z*-axis |
| *ɣ* | Camber angle |
| *Cɣ* | Camber stiffness |
| *Cα* | Lateral stiffness per angle slip |
| *Ck* | Longitudinal stiffness |
| *k* | Longitudinal slip ratio of tires |
| *u* | Velocity component in the wheel plane |
| *μ* | Maximum friction coefficient |
| *μ0* | Maximum friction scaling coefficient |
| *Vs* | Friction reduction magnitude |
| *As* | Friction reduction factor |
| *gy* | Lateral correction factor |
| *gy1* | Lateral maximum friction correction factor |
| *gy2* | Lateral offset correction factor |

### Vertical Dynamics

The block implements these equations for the vertical dynamics.

| Calculation | Equation |
| --- | --- |
| Vertical response | z¨m=Fztire+mg−Fz |
| Tire normal force | Fztire=ρzk−bz˙ |
| Vertical sidewall deflection | ρz=zgnd−z,z≥0 |

The equations use these variables.

| Variable | Value |
| --- | --- |
| *z* | Tire deflection along tire-fixed *z*-axis |
| *zgnd* | Ground displacement along tire-fixed *z*-axis |
| *Fztire* | Tire normal force along tire-fixed *z*-axis |
| *Fz* | Vertical force acting on axle along tire-fixed *z*-axis |
| *ρz* | Vertical sidewall deflection along tire-fixed *z*-axis |
| *k* | Vertical sidewall stiffness |
| *b* | Vertical sidewall damping |

### Overturning, Aligning, and Scaling

This table summarizes the overturning, aligning, and scaling
implementation.

| Calculation | Implementation |
| --- | --- |
| Overturning moment | The Dugoff model does not define an overturning moment. The block implements this equation, requiring minimal parameters.  Mx=FyRecos(γ) |
| Aligning moment | The block implements the aligning moment as a combination of yaw rate damping and slip angle state.  Mz={ψ˙bMz                                               when |α'|>α'Criticaltanh(4α')wμ|Fz|(1−ξ)ξ3+ψ˙bMz    when |α'|≤α'Criticalξ=1−Ca|tan(α')|3μ|Fz| |
| Friction scaling | To vary the coefficient of friction, use the **ScaleFctr** input port. |

The equations use these variables.

| Variable | Value |
| --- | --- |
| *Mx* | Overturning moment acting on axle about tire-fixed *x*-axis |
| *Mz* | Aligning moment acting on axle about tire-fixed *z*-axis |
| *Re* | Effective contact patch to wheel carrier radial distance |
| *ɣ* | Camber angle |
| *k* | Vertical sidewall stiffness |
| *b* | Vertical sidewall damping |
| ψ˙ | Tire angular velocity about the tire-fixed *z*-axis (yaw rate) |
| *w* | Tire width |
| *α'* | Slip angle state |
| *bMz* | Linear yaw rate resistance |
| *Fy* | Lateral force acting on axle along tire-fixed *y*-axis |
| *Cɣ* | Camber stiffness |
| *Cα* | Lateral stiffness per slip angle |
| *μ* | Friction coefficient |
| *Fz* | Vertical contact patch normal force along tire-fixed *z*-axis |

### Tire and Wheel Coordinate Systems

To resolve the forces and moments, the block uses the Z-Up orientation of the tire and wheel coordinate systems.

- Tire coordinate system axes (*XT*, *YT*, *ZT*) are fixed in a reference frame attached to the tire. The origin is at the tire contact with the ground.
- Wheel coordinate system axes (*XW*, *YW*, *ZW*) are fixed in a reference frame attached to the wheel. The origin is at the wheel center.

**Z-Up Orientation**1

Z-Up tire and wheel coordinate systems showing wheel plane and road plane

### Brakes

**Disc**

If you specify the **Brake Type** parameter as
`Disc`, the block implements a disc brake. This figure
shows the side and front views of a disc brake.

Front and side view of disc brake, showing pad, disc, and caliper

A disc brake converts brake cylinder pressure from the brake cylinder into force. The disc brake applies the force at the brake pad mean radius.

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
`Drum`, the block implements a static (steady-state)
simplex drum brake. A simplex drum brake consists of a single two-sided hydraulic
actuator and two brake shoes. The brake shoes do not share a common hinge pin.

The simplex drum brake model uses the applied force and brake geometry to calculate a net torque for each brake shoe. The drum model assumes that the actuators and shoe geometry are symmetrical for both sides, allowing a single set of geometry and friction parameters to be used for both shoes.

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
`Mapped`, the block uses a lookup table to determine the
brake torque.

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
