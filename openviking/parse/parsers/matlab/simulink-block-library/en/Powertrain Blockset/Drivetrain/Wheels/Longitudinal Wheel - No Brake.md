---
type: simulink-block
title: 'Longitudinal Wheel'
family: 'autoblks'
product_id: 'autoblks'
product_name: 'Powertrain Blockset'
documentation_release: R2025b
official_category: 'Drivetrain / Wheels'
documentation_page: 'longitudinalwheel'
documentation_source_path: 'ref/longitudinalwheel.html'
language: en
---

# Longitudinal Wheel

## Ports

### Input

### **BrkPrs** — Brake pressure `scalar`

Brake pressure, in Pa.

#### Dependencies

To enable this port, for the **Brake
Type** parameter, specify one of these types:

- `Disc`
- `Drum`
- `Mapped`

### **AxlTrq** — Axle torque `scalar`

Axle torque, *Ta*,
about wheel spin axis, in N·m.

### **Vx** — Velocity `scalar`

Axle longitudinal velocity along vehicle(body)-fixed
*x*-axis, in m/s.

### **Fz** — Normal force `scalar`

Absolute value of suspension or vehicle normal force along body-fixed
*z*-axis, in N.

### **Gnd** — Ground displacement `scalar`

Ground displacement,
`Grndz`, along negative wheel-fixed
*z*-axis, in m.

Figure of inclined plan with tires and body-fixed, wheel-fixed, and inertial frames

#### Dependencies

To create `Gnd`:

- Set **Vertical Motion** to
  `Mapped stiffness and
  damping`.
- On the **Vertical** pane, select
  **Input ground
  displacement**.

### **lam\_mux** — Friction scaling factor `scalar`

Longitudinal friction scaling factor, dimensionless.

#### Dependencies

To enable this port, select **Input friction scale
factor**.

### **TirePrs** — Tire pressure `scalar`

Tire pressure, in Pa.

#### Dependencies

To enable this port:

- Set one of these parameters:

  - **Longitudinal Force** to
    `Magic Formula pure longitudinal
    slip`.
  - **Rolling Resistance** to
    `Pressure and velocity`
    or `Magic
    Formula`.
  - **Vertical Motion** to
    `Mapped stiffness and
    damping`.
- On the **Wheel Dynamics** pane,
  select **Input tire pressure**.

### **Tamb** — Ambient temperature `scalar`

Ambient temperature, *Tamb*,
in K.

The ambient temperature,
*Tamb*, is the temperature
near tire in application environment, in K. For example, the measured
ambient temperature is the ambient temperature near the tire when the
vehicle is on the road.

Select to create input port `Tamb` to input the
measured ambient temperature.

#### Dependencies

To enable this port:

1. Set **Rolling Resistance** to
   `ISO 28580`.
2. On the **Rolling Resistance** pane,
   select to **Input ambient
   temperature**.
### Output

### **Info** — Bus signal bus

Bus signal containing these block calculations.

| Signal | | | Description | Units |
| --- | --- | --- | --- | --- |
| `AxlTrq` | | | Axle torque about body-fixed *y*-axis | N·m |
| `Omega` | | | Wheel angular velocity about body-fixed *y*-axis | rad/s |
| `Omegadot` | | | Wheel angular acceleration about body-fixed *y*-axis | rad/s^2 |
| `Fx` | | | Longitudinal vehicle force along body-fixed *x*-axis | N |
| `Fz` | | | Vertical vehicle force along body-fixed *z*-axis | N |
| `Fzb` | | | Tire normal force due to wheel damping along the wheel-fixed *z*-axis | N |
| `Fzk` | | | Tire normal force due to wheel stiffness along the wheel-fixed *z*-axis | N |
| `My` | | | Rolling resistance torque about body-fixed *y*-axis | N·m |
| `Myb` | | | Rolling resistance torque due to damping about body-fixed *y*-axis | N·m |
| `Kappa` | | | Slip ratio | NA |
| `Vx` | | | Vehicle longitudinal velocity along body-fixed *x*-axis | m/s |
| `Re` | | | Wheel effective radius along wheel-fixed *z*-axis | m |
| `BrkTrq` | | | Brake torque about body-fixed *y*-axis | N·m |
| `BrkPrs` | | | Brake pressure | Pa |
| `z` | | | Wheel vertical deflection along wheel-fixed *z*-axis | m |
| `zdot` | | | Wheel vertical velocity along wheel-fixed *z*-axis | m/s |
| `zddot` | | | Wheel vertical acceleration along wheel-fixed *z*-axis | m/s^2 |
| `Gndz` | | | Ground displacement along negative of wheel-fixed *z*-axis (positive input produces wheel lift) | m |
| `GndFz` | | | Vertical wheel force on ground along negative of wheel-fixed *z*-axis | N |
| `TirePrs` | | | Tire pressure | Pa |
| `Fpatch` | | | Tractive force (Fx considering relaxation effects). Use for vehicle transient maneuvers. | N |
| `PwrInfo` | `PwrTrnsfrd` | `PwrRoad` | External torque applied by the axle to the wheel | W |
| `PwrAxlTrq` | Vertical force applied to the wheel by the vehicle or suspension | W |
| `PwrFz` | Tractive power loss | W |
| `PwrNotTrnsfrd` | `PwrSlip` | Rolling resistance power | W |
| `PwrMyRoll` | Braking power | W |
| `PwrMyBrk` | Rolling viscous damping loss | W |
| `PwrMyb` | Vertical damping power | W |
| `PwrFzDamp` | Rate of change of vertical kinetic energy | W |
| `PwrStored` | `PwrStoredzdot` | Rate of change of rotational kinetic energy | W |
| `PwrStoredq` | Rate of change of stored sidewall potential energy | W |
| `PwrStoredFsFzSprng` | Rate of change of gravitational potential energy | W |
| `PwrStoredGrvty` | Tractive power applied from the axle | W |

### **Fx** — Longitudinal axle force `scalar`

Longitudinal force acting on axle, along body-fixed
*x*-axis, in N. Positive force acts to move the
vehicle forward.

### **Omega** — Wheel angular velocity `scalar`

Wheel angular velocity, about body-fixed *y*-axis,
in rad/s.

### **z** — Wheel vertical deflection `scalar`

Wheel vertical deflection along wheel-fixed
*z*-axis, in m.

#### Dependencies

To enable this port, set **Vertical Motion** to
`Mapped stiffness and damping`.

### **zdot** — Wheel vertical velocity `scalar`

Wheel vertical velocity along wheel-fixed *z*-axis,
in m/s.

#### Dependencies

To enable this port, set **Vertical Motion** to
`Mapped stiffness and damping`.

## Parameters

### Block Options

### **Longitudinal Force** — Select type `Magic Formula constant value` (default) | `Magic Formula pure longitudinal slip` | `Mapped force`

The block models longitudinal force as a function of wheel slip
relative to the road surface. To calculate the longitudinal force, specify one of these
**Longitudinal Force** parameters.

| Setting | Block Implementation |
| --- | --- |
| `Magic Formula constant value` | Magic Formula with constant coefficient for stiffness, shape, peak, and curvature. |
| `Magic Formula pure longitudinal slip` | Magic Formula with load-dependent coefficients that implement equations 4.E9 through 4.E18 in *Tire and Vehicle Dynamics*. |
| `Mapped force` | Lookup table that is a function of the normal force and wheel slip ratio. |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `FxType` |
| **Values:** | `Magic Formula constant value` (default) | `Magic Formula pure longitudinal slip` | `Mapped force` |
| **Data Types:** | `character vector` |

#### Dependencies

| Selecting | Enables These Parameters |
| --- | --- |
| `Magic Formula constant value` | **Pure longitudinal peak factor, Dx**  **Pure longitudinal shape factor, Cx**  **Pure longitudinal stiffness factor, Bx**  **Pure longitudinal curvature factor, Ex** |
| `Magic Formula pure longitudinal slip` | **Cfx shape factor, PCX1**  **Longitudinal friction at nominal normal load, PDX1**  **Frictional variation with load, PDX2**  **Frictional variation with camber, PDX3**  **Longitudinal curvature at nominal normal load, PEX1**  **Variation of curvature factor with load, PEX2**  **Variation of curvature factor with square of load, PEX3**  **Longitudinal curvature factor with slip, PEX4**  **Longitudinal slip stiffness at nominal normal load, PKX1**  **Variation of slip stiffness with load, PKX2**  **Slip stiffness exponent factor, PKX3**  **Horizontal shift in slip ratio at nominal normal load, PHX1**  **Variation of horizontal slip ratio with load, PHX2**  **Vertical shift in load at nominal normal load, PVX1**  **Variation of vertical shift with load, PVX2**  **Linear variation of longitudinal slip stiffness with tire pressure, PPX1**  **Quadratic variation of longitudinal slip stiffness with tire pressure, PPX2**  **Linear variation of peak longitudinal friction with tire pressure, PPX3**  **Quadratic variation of peak longitudinal friction with tire pressure, PPX4**  **Linear variation of longitudinal slip stiffness with tire pressure, PPX1**  **Slip speed decay function scaling factor, lam\_muV**  **Brake slip stiffness scaling factor, lam\_Kxkappa**  **Longitudinal shape scaling factor, lam\_Cx**  **Longitudinal curvature scaling factor, lam\_Ex**  **Longitudinal horizontal shift scaling factor, lam\_Hx**  **Longitudinal vertical shift scaling factor, lam\_Vx** |
| `Mapped force` | **Slip ratio breakpoints, kappaFx**  **Normal force breakpoints, FzFx**  **Longitudinal force map, FxMap** |

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

### **Brake Type** — Select type `None` | `Disc` | `Drum` | `Mapped`

There are four types of Longitudinal Wheel
blocks. Each block implements a different brake type.

| Block Name | Brake Type Setting | Brake Implementation |
| --- | --- | --- |
| Longitudinal Wheel - No Brake | `None` | None |
| Longitudinal Wheel - Disc Brake | `Disc` | Brake that converts the brake cylinder pressure into a braking force. |
| Longitudinal Wheel - Drum Brake | `Drum` | Simplex drum brake that converts the applied force and brake geometry into a net braking torque. |
| Longitudinal Wheel - Mapped Brake | `Mapped` | Lookup table that is a function of the wheel speed and applied brake pressure. |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `BrakeType` |
| **Values:** | `None` | `Disc` | `Drum` | `Mapped` |
| **Data Types:** | `character vector` |

### **Vertical Motion** — Select type `None` (default) | `Mapped stiffness and damping`

To calculate vertical
motion, specify one of these **Vertical Motion**
parameters.

| Setting | Block Implementation |
| --- | --- |
| `None` | Block passes the applied chassis forces directly through to the rolling resistance and longitudinal force calculations. |
| `Mapped stiffness and damping` | Vertical motion depends on wheel stiffness and damping. Stiffness is a function of tire sidewall displacement and pressure. Damping is a function of tire sidewall velocity and pressure. |
| `External deflection` | The block uses the defined sidewall deflection directly in the effective radius calculation. |

| Selecting | Enables These Parameters | Creates These Output Ports |
| --- | --- | --- |
| `Mapped stiffness and damping` | **Wheel and unsprung mass, m**  **Initial deflection, zo**  **Initial velocity, zdoto**  **Gravitational acceleration, g**  **Vertical deflection breakpoints, zFz**  **Pressure breakpoints, pFz**  **Force due to deflection, Fzz**  **Vertical velocity breakpoints, zdotFz**  **Force due to velocity, Fzzdot**  **Ground displacement, Gndz**  **Input ground displacement** | `z`  `zdot` |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `vertType` |
| **Values:** | `None` (default) | `Mapped stiffness and damping` |
| **Data Types:** | `character vector` |

### **Longitudinal scaling factor, lam\_x** — Friction scaling factor `1` (default)

Longitudinal friction scaling factor, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `lam_x` |
| **Values:** | `1` (default) |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, clear **Input friction scale
factor**.

### **Input friction scale factor** — Selection `off` (default) | `on`

Create input port for longitudinal friction scaling factor.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `extMu` |
| **Values:** | `off` (default) | `on` |
| **Data Types:** | `character vector` |

#### Dependencies

Selecting this parameter:

- Creates input port `lam_mux`.
- Disables parameter **Longitudinal scaling
  factor, lam\_x**.

### Wheel Dynamics

### **Axle viscous damping coefficient, br** — Damping `0.001` (default) | `scalar`

Axle viscous damping coefficient, *br*, in
N·m·s/rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `br` |
| **Values:** | `0.001` (default) | `scalar` |
| **Data Types:** | `double` |

### **Wheel inertia, Iyy** — Inertia `0.8` (default) | `scalar`

Wheel inertia, in kg·m^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Iyy` |
| **Values:** | `0.8` (default) | `scalar` |
| **Data Types:** | `double` |

### **Wheel initial angular velocity, omegao** — Wheel speed `0` (default) | `scalar`

Initial angular velocity of wheel, along body-fixed
*y*-axis, in rad/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `omegao` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

### **Relaxation length, Lrel** — Relaxation length `0.5` (default) | `scalar`

Wheel relaxation length, in m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Lrel` |
| **Values:** | `0.5` (default) | `scalar` |
| **Data Types:** | `double` |

### **Loaded radius, Re** — Loaded radius `0.3` (default) | `scalar`

Loaded wheel radius, `Re`, in m.

Figure of inclined plan with tires and body-fixed, wheel-fixed, and inertial frames

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Re` |
| **Values:** | `0.3` (default) | `scalar` |
| **Data Types:** | `double` |

### **Unloaded radius, UNLOADED\_RADIUS** — Unloaded radius `0.4` (default) | `scalar`

Unloaded wheel radius, in m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `UNLOADED_RADIUS` |
| **Values:** | `0.4` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, set **Rolling
Resistance** to `Pressure and
velocity` or `Magic
Formula`.

### **Nominal longitudinal speed, LONGVL** — Speed `16` (default) | `scalar`

Nominal longitudinal speed along body-fixed
*x*-axis, in m/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `LONGVL` |
| **Values:** | `16` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Longitudinal Force** to
`Magic Formula pure longitudinal slip`.

### **Nominal camber angle, gamma** — Camber `0` (default) | `scalar`

Nominal camber angle, in rad.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `gamma` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set either:

- **Longitudinal Force** to `Magic Formula pure
  longitudinal slip`.
- **Rolling Resistance** to `Magic
  Formula`.

### **Nominal pressure, NOMPRES** — Pressure `220000` (default) | `scalar`

Nominal pressure, in Pa.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `NOMPRES` |
| **Values:** | `220000` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set either:

- **Longitudinal Force** to `Magic Formula pure
  longitudinal slip`.
- **Rolling Resistance** to `Magic
  Formula`.

### **Pressure, press** — Pressure `220000` (default) | `scalar`

Pressure, in Pa.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `press` |
| **Values:** | `220000` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter:

- Set one of these:

  - **Longitudinal Force** to
    `Magic Formula pure longitudinal
    slip`.
  - **Rolling Resistance** to
    `Pressure and velocity`
    or `Magic
    Formula`.
  - **Vertical Motion** to
    `Mapped stiffness and
    damping`.
- On the **Wheel Dynamics** pane, clear
  **Input tire pressure**.

### Longitudinal

#### Magic Formula Constant Value

### **Pure longitudinal peak factor, Dx** — Factor `1` (default) | `scalar`

Pure longitudinal peak factor, dimensionless.

The coefficients are
based on empirical tire data. These values are typical sets of constant Magic Formula
coefficients for common road conditions.

| Surface | B | C | D | E |
| --- | --- | --- | --- | --- |
| Dry tarmac | 10 | 1.9 | 1 | 0.97 |
| Wet tarmac | 12 | 2.3 | 0.82 | 1 |
| Snow | 5 | 2 | 0.3 | 1 |
| Ice | 4 | 2 | 0.1 | 1 |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Dx` |
| **Values:** | `1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal
Force** parameter `Magic Formula constant value`.

### **Pure longitudinal shape factor, Cx** — Factor `1.65` (default) | `scalar`

Pure longitudinal shape factor, dimensionless.

The coefficients are
based on empirical tire data. These values are typical sets of constant Magic Formula
coefficients for common road conditions.

| Surface | B | C | D | E |
| --- | --- | --- | --- | --- |
| Dry tarmac | 10 | 1.9 | 1 | 0.97 |
| Wet tarmac | 12 | 2.3 | 0.82 | 1 |
| Snow | 5 | 2 | 0.3 | 1 |
| Ice | 4 | 2 | 0.1 | 1 |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Cx` |
| **Values:** | `1.65` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal
Force** parameter `Magic Formula constant value`.

### **Pure longitudinal stiffness factor, Bx** — Factor `10` (default) | `scalar`

Pure longitudinal stiffness factor, dimensionless.

The coefficients are
based on empirical tire data. These values are typical sets of constant Magic Formula
coefficients for common road conditions.

| Surface | B | C | D | E |
| --- | --- | --- | --- | --- |
| Dry tarmac | 10 | 1.9 | 1 | 0.97 |
| Wet tarmac | 12 | 2.3 | 0.82 | 1 |
| Snow | 5 | 2 | 0.3 | 1 |
| Ice | 4 | 2 | 0.1 | 1 |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Bx` |
| **Values:** | `10` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal
Force** parameter `Magic Formula constant value`.

### **Pure longitudinal curvature factor, Ex** — Factor `0.01` (default) | `scalar`

Pure longitudinal curvature factor, dimensionless.

The coefficients are
based on empirical tire data. These values are typical sets of constant Magic Formula
coefficients for common road conditions.

| Surface | B | C | D | E |
| --- | --- | --- | --- | --- |
| Dry tarmac | 10 | 1.9 | 1 | 0.97 |
| Wet tarmac | 12 | 2.3 | 0.82 | 1 |
| Snow | 5 | 2 | 0.3 | 1 |
| Ice | 4 | 2 | 0.1 | 1 |

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Ex` |
| **Values:** | `0.01` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal
Force** parameter `Magic Formula constant value`.

#### Magic Formula Pure Longitudinal Slip

### **Cfx shape factor, PCX1** — Factor `1.6` (default) | `scalar`

Cfx shape factor, PCX1, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PCX1` |
| **Values:** | `1.6` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

### **Longitudinal friction at nominal normal load, PDX1** — Factor `1` (default) | `scalar`

Longitudinal friction at nominal normal load, PDX1,
dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PDX1` |
| **Values:** | `1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

### **Frictional variation with load, PDX2** — Factor `-0.08` (default) | `scalar`

Frictional variation with load, PDX2, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PDX2` |
| **Values:** | `-0.08` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

### **Frictional variation with camber, PDX3** — Factor `0` (default) | `scalar`

Frictional variation with camber, PDX3, 1/rad^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PDX3` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

### **Longitudinal curvature at nominal normal load, PEX1** — Factor `0.112` (default) | `scalar`

Longitudinal curvature at nominal normal load, PEX1,
dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PEX1` |
| **Values:** | `0.112` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

### **Variation of curvature factor with load, PEX2** — Factor `0.313` (default) | `scalar`

Variation of curvature factor with load, PEX2, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PEX2` |
| **Values:** | `0.313` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

### **Variation of curvature factor with square of load, PEX3** — Factor `0` (default) | `scalar`

Variation of curvature factor with square of load, PEX3,
dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PEX3` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

### **Longitudinal curvature factor with slip, PEX4** — Factor `0.0016` (default) | `scalar`

Longitudinal curvature factor with slip, PEX4, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PEX4` |
| **Values:** | `0.0016` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

### **Longitudinal slip stiffness at nominal normal load, PKX1** — Factor `21.7` (default) | `scalar`

Longitudinal slip stiffness at nominal normal load, PKX1,
dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PKX1` |
| **Values:** | `21.7` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

### **Variation of slip stiffness with load, PKX2** — Factor `13.77` (default) | `scalar`

Variation of slip stiffness with load, PKX2, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PKX2` |
| **Values:** | `13.77` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

### **Slip stiffness exponent factor, PKX3** — Factor `-0.412` (default) | `scalar`

Slip stiffness exponent factor, PKX3, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PKX3` |
| **Values:** | `-0.412` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

### **Horizontal shift in slip ratio at nominal normal load, PHX1** — Factor `2.1585E-4` (default) | `scalar`

Horizontal shift in slip ratio at nominal normal load, PHX1,
dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PHX1` |
| **Values:** | `2.1585E-4` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

### **Variation of horizontal slip ratio with load, PHX2** — Factor `0.00115` (default) | `scalar`

Variation of horizontal slip ratio with load, PHX2,
dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PHX2` |
| **Values:** | `0.00115` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

### **Vertical shift in load at nominal normal load, PVX1** — Factor `1.5973E-5` (default) | `scalar`

Vertical shift in load at nominal normal load, PVX1,
dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PVX1` |
| **Values:** | `1.5973E-5` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

### **Variation of vertical shift with load, PVX2** — Factor `1.043E-4` (default) | `scalar`

Variation of vertical shift with load, PVX2, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PVX2` |
| **Values:** | `1.043E-4` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

### **Linear variation of longitudinal slip stiffness with tire pressure, PPX1** — Factor `-0.3489` (default) | `scalar`

Linear variation of longitudinal slip stiffness with tire pressure,
PPX1, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PPX1` |
| **Values:** | `-0.3489` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

### **Quadratic variation of longitudinal slip stiffness with tire pressure, PPX2** — Factor `0.382` (default) | `scalar`

Quadratic variation of longitudinal slip stiffness with tire pressure,
PPX2, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PPX2` |
| **Values:** | `0.382` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

### **Linear variation of peak longitudinal friction with tire pressure, PPX3** — Factor `-0.09634` (default) | `scalar`

Linear variation of peak longitudinal friction with tire pressure,
PPX3, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PPX3` |
| **Values:** | `-0.09634` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

### **Quadratic variation of peak longitudinal friction with tire pressure, PPX4** — Factor `0.06447` (default) | `scalar`

Quadratic variation of peak longitudinal friction with tire pressure,
PPX4, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `PPX4` |
| **Values:** | `0.06447` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

### **Slip speed decay function scaling factor, lam\_muV** — Factor `1` (default) | `scalar`

Slip speed decay function scaling factor, lam\_muV,
dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `lam_muV` |
| **Values:** | `1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

### **Brake slip stiffness scaling factor, lam\_Kxkappa** — Factor `1` (default) | `scalar`

Brake slip stiffness scaling factor, lam\_Kxkappa,
dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `lam_Kxkappa` |
| **Values:** | `1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

### **Longitudinal shape scaling factor, lam\_Cx** — Factor `1` (default) | `scalar`

Longitudinal shape scaling factor, lam\_Cx, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `lam_Cx` |
| **Values:** | `1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

### **Longitudinal curvature scaling factor, lam\_Ex** — Factor `0` (default) | `scalar`

Longitudinal curvature scaling factor, lam\_Ex, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `lam_Ex` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

### **Longitudinal horizontal shift scaling factor, lam\_Hx** — Factor `1` (default) | `scalar`

Longitudinal horizontal shift scaling factor, lam\_Hx,
dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `lam_Hx` |
| **Values:** | `1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

### **Longitudinal vertical shift scaling factor, lam\_Vx** — Factor `1` (default) | `scalar`

Longitudinal vertical shift scaling factor, lam\_Vx,
dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `lam_Vx` |
| **Values:** | `1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Magic Formula pure longitudinal
slip`.

#### Mapped Force

### **Slip ratio breakpoints, kappaFx** — Breakpoints `vector`

Slip ratio breakpoints, dimensionless.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `kappaFx` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Mapped force`.

### **Normal force breakpoints, FzFx** — Breakpoints `vector`

Normal force breakpoints, N.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `FzFx` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Mapped force`.

### **Longitudinal force map, FxMap** — Lookup table `array`

Longitudinal force versus slip ratio and normal force, N.

#### Programmatic Use

To set the block
parameter value programmatically, use the `set_param`
function.

To get the block
parameter value programmatically, use the `get_param`
function.

|  |  |
| --- | --- |
| **Parameter:** | `FxMap` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To create this parameter, select the **Longitudinal Force** parameter
`Mapped force`.

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

### Brake

### **Static friction coefficient, mu\_static** — Static friction `.3` (default) | `scalar`

Static friction coefficient,
specified as a scalar, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `mu_static` |
| **Values:** | `.3` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for the **Brake Type**
parameter, specify one of these types:

- `Disc`
- `Drum`
- `Mapped`

### **Kinetic friction coefficient, mu\_kinetic** — Kinetic friction `.2` (default) | `scalar`

Kinematic friction coefficient,
specified as a scalar, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `mu_kinetic` |
| **Values:** | `.2` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, for the **Brake Type**
parameter, specify one of these types:

- `Disc`
- `Drum`
- `Mapped`

#### Disc

### **Disc brake actuator bore, disc\_abore** — Bore distance `.05` (default) | `scalar`

Disc brake actuator bore, specified
as a scalar, in m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `disc_abore` |
| **Values:** | `.05` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable the disc brake parameters, select
`Disc` for the **Brake
Type** parameter.

### **Brake pad mean radius, Rm** — Radius `.177` (default) | `scalar`

Brake pad mean radius, specified as a
scalar, in m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Rm` |
| **Values:** | `.177` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable the disc brake parameters, select
`Disc` for the **Brake
Type** parameter.

### **Number of brake pads, num\_pads** — Count `2` (default) | `scalar`

Number of brake pads, specified as a
scalar, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `num_pads` |
| **Values:** | `2` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable the disc brake parameters, select
`Disc` for the **Brake
Type** parameter.

#### Drum

### **Drum brake actuator bore, disc\_abore** — Bore distance `0.0508` (default) | `scalar`

Drum brake actuator bore, specified
as a scalar, in m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `disc_abore` |
| **Values:** | `0.0508` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable the drum brake parameters, select
`Drum` for the **Brake
Type** parameter.

### **Shoe pin to drum center distance, drum\_a** — Distance `0.123` (default) | `scalar`

Shoe pin to drum center distance, in m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `drum_a` |
| **Values:** | `0.123` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable the drum brake parameters, select
`Drum` for the **Brake
Type** parameter.

### **Shoe pin center to force application point distance, drum\_c** — Distance `0.212` (default) | `scalar`

Shoe pin center to force application point distance, in m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `drum_c` |
| **Values:** | `0.212` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable the drum brake parameters, select
`Drum` for the **Brake
Type** parameter.

### **Drum internal radius, drum\_r** — Radius `0.15` (default) | `scalar`

Drum internal radius, in m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `drum_r` |
| **Values:** | `0.15` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable the drum brake parameters, select
`Drum` for the **Brake
Type** parameter.

### **Shoe pin to pad start angle, drum\_theta1** — Angle `0` (default) | `scalar`

Shoe pin to pad start angle, in deg.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `drum_theta1` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable the drum brake parameters, select
`Drum` for the **Brake
Type** parameter.

### **Shoe pin to pad end angle, drum\_theta2** — Angle `126` (default) | `scalar`

Shoe pin to pad end angle, in deg.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `drum_theta2` |
| **Values:** | `126` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable the drum brake parameters, select
`Drum` for the **Brake
Type** parameter.

#### Mapped

### **Brake actuator pressure breakpoints, brake\_p\_bpt** — Breakpoints `vector`

Brake actuator pressure breakpoints, in bar.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `brake_p_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable the mapped brake parameters, select
`Mapped` for the **Brake
Type** parameter.

### **Wheel speed breakpoints, brake\_n\_bpt** — Breakpoints `vector`

Wheel speed breakpoints, in rpm.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `brake_n_bpt` |
| **Values:** | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable the mapped brake parameters, select
`Mapped` for the **Brake
Type** parameter.

### **Brake torque map, f\_brake\_t** — Lookup table `array`

The lookup
table for the brake torque, fbrake(P,N), is a function of applied brake pressure and wheel
speed, where:

- *T* is brake torque, in N·m.
- *P* is applied brake pressure, in
  bar.
- *N* is wheel speed, in rpm.

Plot showing brake torque as a function of wheel speed and applied brake pressure

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `f_brake_t` |
| **Values:** | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable the mapped brake parameters, select
`Mapped` for the **Brake
Type** parameter.

### Vertical

### **Nominal normal force, FNOMIN** — Force `2000` (default) | `scalar`

Nominal rated wheel load along wheel-fixed
*z*-axis, in N.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `FNOMIN` |
| **Values:** | `2000` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set either:

- **Longitudinal Force** to `Magic Formula pure
  longitudinal slip`.
- **Rolling Resistance** to `Magic
  Formula`.

### **Nominal rated load scaling factor, lam\_Fzo** — Factor `1` (default) | `scalar`

Nominal rated load scaling factor, dimensionless. Used to scale the
normal for specific applications and load conditions.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `lam_Fzo` |
| **Values:** | `1` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Longitudinal Force** to
`Magic Formula pure longitudinal slip`.

### **Wheel and unsprung mass, m** — Mass `10` (default) | `scalar`

Wheel and unsprung mass, in kg. Used in the vertical motion
calculations.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `m` |
| **Values:** | `10` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Vertical Motion** to `Mapped
stiffness and damping`.

### **Initial deflection, zo** — Deflection `0` (default) | `scalar`

Initial axle displacement along wheel-fixed
*z*-axis, in m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `zo` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Vertical Motion** to `Mapped
stiffness and damping`.

### **Initial velocity, zdoto** — Velocity `0` (default) | `scalar`

Initial axle velocity along wheel-fixed *z*-axis,
in m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `zdoto` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Vertical Motion** to `Mapped
stiffness and damping`.

### **Gravitational acceleration, g** — Gravity `9.81` (default) | `scalar`

Gravitational acceleration, in m/s^2.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `g` |
| **Values:** | `9.81` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Vertical Motion** to `Mapped
stiffness and damping`.

### **Ground displacement, Gndz** — Displacement `0` (default) | `scalar`

Ground displacement, `Grndz`, along negative wheel-fixed *z*-axis, in m.

Figure of inclined plan with tires and body-fixed, wheel-fixed, and inertial frames

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Gndz` |
| **Values:** | `0` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Vertical Motion** to `Mapped
stiffness and damping`.

#### Mapped Stiffness and Damping

### **Vertical deflection breakpoints, zFz** — Breakpoints `[0 .01 .1]` (default) | `vector`

Vector of sidewall deflection breakpoints corresponding to the force
table, in m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `zFz` |
| **Values:** | `[0 .01 .1]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Vertical Motion** to `Mapped
stiffness and damping`.

### **Pressure breakpoints, pFz** — Breakpoints `[10000 1000000]` (default) | `vector`

Vector of pressure data points corresponding to the force table, in
Pa.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `pFz` |
| **Values:** | `[10000 1000000]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Vertical Motion** to `Mapped
stiffness and damping`.

### **Force due to deflection, Fzz** — Force `[0 1e3 1e4; 0 1e4 1e5]` (default) | `vector`

Force due to sidewall deflection and pressure along wheel-fixed
*z*-axis, in N.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Fzz` |
| **Values:** | `[0 1e3 1e4; 0 1e4 1e5]` (default) | `vector` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Vertical Motion** to `Mapped
stiffness and damping`.

### **Vertical velocity breakpoints, zdotFz** — Breakpoints `[-20 0 20]` (default) | `scalar`

Vector of sidewall velocity breakpoints corresponding to the force due
to velocity table, in m.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `zdotFz` |
| **Values:** | `[-20 0 20]` (default) | `scalar` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Vertical Motion** to `Mapped
stiffness and damping`.

### **Force due to velocity, Fzzdot** — Force `[500 0 -500;250 0 -250]` (default) | `array`

Force due to sidewall velocity and pressure along wheel-fixed
*z*-axis, in N.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `Fzzdot` |
| **Values:** | `[500 0 -500;250 0 -250]` (default) | `array` |
| **Data Types:** | `double` |

#### Dependencies

To enable this parameter, set **Vertical Motion** to `Mapped
stiffness and damping`.

### Simulation Setup

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

### **Max allowable slip ratio (absolute), kappamax** — Ratio `1.5` (default) | `scalar`

Maximum allowable absolute slip ratio, dimensionless.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `kappamax` |
| **Values:** | `1.5` (default) | `scalar` |
| **Data Types:** | `double` |

### **Velocity tolerance used to handle low velocity situations, VXLOW** — Tolerance `1` (default) | `scalar`

Velocity tolerance used to handle low-velocity situations, in
m/s.

#### Programmatic Use

To set the block parameter value programmatically, use
the `set_param` function.

To get the block parameter value
programmatically, use the `get_param` function.

|  |  |
| --- | --- |
| **Parameter:** | `VXLOW` |
| **Values:** | `1` (default) | `scalar` |
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

## Libraries

Powertrain Blockset / Drivetrain / Wheels Vehicle Dynamics Blockset / Wheels and Tires

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

## Description

Longitudinal wheel with disc, drum, or mapped brake

The Longitudinal Wheel block implements the longitudinal behavior of an
ideal wheel. You can specify the longitudinal force and rolling resistance calculation
method, and brake type. Use the block in driveline and longitudinal vehicle simulations
where low frequency tire-road and braking forces are required to determine vehicle
acceleration, braking, and wheel-rolling resistance. For example, you can use the block
to determine the torque and power requirements for a specified drive cycle or braking
event. The block is not suitable for applications that require combined lateral
slip.

There are four types of Longitudinal Wheel
blocks. Each block implements a different brake type.

| Block Name | Brake Type Setting | Brake Implementation |
| --- | --- | --- |
| Longitudinal Wheel - No Brake | `None` | None |
| Longitudinal Wheel - Disc Brake | `Disc` | Brake that converts the brake cylinder pressure into a braking force. |
| Longitudinal Wheel - Drum Brake | `Drum` | Simplex drum brake that converts the applied force and brake geometry into a net braking torque. |
| Longitudinal Wheel - Mapped Brake | `Mapped` | Lookup table that is a function of the wheel speed and applied brake pressure. |

The block models longitudinal force as a function of wheel slip
relative to the road surface. To calculate the longitudinal force, specify one of these
**Longitudinal Force** parameters.

| Setting | Block Implementation |
| --- | --- |
| `Magic Formula constant value` | Magic Formula with constant coefficient for stiffness, shape, peak, and curvature. |
| `Magic Formula pure longitudinal slip` | Magic Formula with load-dependent coefficients that implement equations 4.E9 through 4.E18 in *Tire and Vehicle Dynamics*. |
| `Mapped force` | Lookup table that is a function of the normal force and wheel slip ratio. |

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
tractive wheel forces and rolling resistance with first order dynamics. The rolling
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

| If | Lock-Up Condition | Friction Model | Dynamic Model |
| --- | --- | --- | --- |
| ω≠0orTS<|Ti+Tf−ωb| | Unlocked | Tf=Tk,whereTk=FcReffμktanh[4(−ωd)]Ts=FcReffμsReff=2(Ro3−Ri3)3(Ro2−Ri2) | ω˙J=−ωb+Ti+To |
| ω=0andTS≥|Ti+Tf−ωb| | Locked | Tf=Ts | ω=0 |

The equations use these variables.

|  |  |
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
| *Ro* | Annular disc outer radius |
| *Ri* | Annular disc inner radius |
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

### Longitudinal Force

To model the Longitudinal Wheel block longitudinal forces, you can
use the Magic Formula. The model provides a steady-state *tire
characteristic function*
*F*x =
*f*(*κ*,
*F*z), the longitudinal force
*F*x on the tire, based on:

- Vertical load *F*z
- Wheel slip *κ*

Image of tire with applied vertical and longitudinal forces

The Magic Formula model uses these variables.

|  |  |
| --- | --- |
| *Ω* | Wheel angular velocity |
| *r*w | Wheel radius |
| *V*x | Wheel hub longitudinal velocity |
| *rwΩ* | Tire tread longitudinal velocity |
| *V*sx = *r*wΩ – *V*x | Wheel slip velocity |
| *κ* = *V*sx/|*V*x| | Wheel slip |
| *F*z, *F*z0 | Vertical load and nominal vertical load on tire |
| *F*x = *f*(*κ*, *F*z) | Longitudinal force exerted on the tire at the contact point. Also a characteristic function *f* of the tire. |

**Magic Formula Constant Value**

If you set **Longitudinal Force** to `Magic
Formula constant value`, the block implements the Magic Formula
as a specific form of the tire characteristic function, characterized by four
dimensionless coefficients (*B*, *C*,
*D*, *E*), or stiffness, shape, peak, and curvature:

Fx=f(κ,Fz) =FzDsin(Ctan−1[ {Bκ−E[Bκ−tan−1(Bκ) ] } ] )

The slope of *f* at *κ* = 0 is *B**C**D*·*F*z.

The coefficients are
based on empirical tire data. These values are typical sets of constant Magic Formula
coefficients for common road conditions.

| Surface | B | C | D | E |
| --- | --- | --- | --- | --- |
| Dry tarmac | 10 | 1.9 | 1 | 0.97 |
| Wet tarmac | 12 | 2.3 | 0.82 | 1 |
| Snow | 5 | 2 | 0.3 | 1 |
| Ice | 4 | 2 | 0.1 | 1 |

**Magic Formula Pure Longitudinal Slip**

If you set **Longitudinal Force** to `Magic
Formula pure longitudinal slip`, the block implements a more
general Magic Formula using dimensionless coefficients that are functions of the
tire load. The block implements the longitudinal force equations in Chapter 4 of
*Tire and Vehicle Dynamics*, including 4.E9 through 4.E18:

Fx0=Dxsin(Cxtan−1[ {Bxκx−Ex[Bxκx−tan−1(Bxκx) ] } ] ) +SVxwhere:κx=κ+ SHxCx= pCx1λCxDx=μxFzς1μx= (pDx1+ pDx2dfz)(1+ppx3dpi+ppx4dpi2)(1−pDx3γ2)λ\*μxEx = (pEx1+ pEx2dfz + pEx3dfz2)[1– pEx4sgn(κx)] λExKxκ = Fz(pKx1+ pKx2dfz)exp(pKx3dfz)(1+ ppx1dpi + ppx2dpi2)Bx = Kxκ/(CxDx + εx)SHx = pHx1+ pHx2dfzSVx = Fz·(pVx1+ pVx2dfz)λVxλ'μxς1

*SHx* and
*SVx* represent offsets to the
slip and longitudinal force in the force-slip function, or horizontal and
vertical offsets if the function is plotted as a curve.
*μx* is the longitudinal
load-dependent friction coefficient.
*εx* is a small number inserted to
prevent division by zero as *Fz*
approaches zero.

### Vertical Dynamics

If you select no vertical degrees-of-freedom by setting **Vertical
Motion** to `None`, the block passes the
applied chassis forces directly through to the rolling resistance and longitudinal
force calculations.

If you set **Vertical Motion** to `Mapped stiffness
and damping`, the vertical motion depends on wheel stiffness and
damping. Stiffness is a function of tire sidewall displacement and pressure. Damping
is a function of tire sidewall velocity and pressure.

Fztire(z,z˙,Ptire)=Fzk(z,Ptire)+Fzb(z˙,Ptire)

The block determines the vertical response using this differential equation.

z¨m=Fztire−Fz−mg

When you disable the vertical degree-of-freedom, the input normal force from the
vehicle passes directly to the longitudinal and rolling force calculations.

z¨=z˙=m=0Fztire=mg

The block uses the wheel-fixed frame to resolve the vertical forces.

Figure of inclined plan with tires and body-fixed, wheel-fixed, and inertial frames

The equations use these variables.

|  |  |
| --- | --- |
| *Fztire* | Tire normal force along the wheel-fixed *z*-axis |
| *m* | Axle mass |
| *Fzk* | Tire normal force due to wheel stiffness along the wheel-fixed *z*-axis |
| *Fzb* | Tire normal force due to wheel damping along the wheel-fixed *z*-axis |
| *Fz* | Suspension or vehicle normal force along the wheel-fixed *z*-axis |
| *PTire* | Tire pressure |
| z,z˙,z¨ | Tire displacement, velocity, and acceleration, respectively, along the wheel-fixed *z*-axis |

### Power Accounting

For the power accounting, the block implements these equations.

| Bus Signal | | | Description | Equations |
| --- | --- | --- | --- | --- |
| `PwrInfo` | `PwrTrnsfrd` — Power transferred between blocks  - Positive signals indicate flow into block - Negative signals indicate flow out of block | `PwrRoad` | Tractive power applied from the axle | Proad=FxVx |
| `PwrAxlTrq` | External torque applied by the axle to the wheel | PT=Tω |
| `PwrFz` | Vertical force applied to the wheel by the vehicle or suspension | PFz=Fzz˙ |
| `PwrNotTrnsfrd` — Power crossing the block boundary, but not transferred  - Positive signals indicate an input - Negative signals indicate a loss | `PwrSlip` | Tractive power loss | Pκ=FxVx+(−FcpRe+My)ω |
| `PwrMyRoll` | Rolling resistance power | PMy=Myω |
| `PwrMyBrk` | Braking power | Pbrk=Mbrkω |
| `PwrMyb` | Rolling viscous damping loss | Pb=−bω2 |
| `PwrFzDamp` | Vertical damping power | PFzb= Fzbz˙ |
| `PwrStored` — Stored energy rate of change  - Positive signals indicate an increase - Negative signals indicate a decrease | `PwrStoredzdot` | Rate of change of vertical kinetic energy | Pz˙=mz¨z˙ |
| `PwrStoredq` | Rate of change of rotational kinetic energy | Pω=Iyyω˙ω |
| `PwrStoredFsFzSprng` | Rate of change of stored sidewall potential energy | PFzk=Fzkz˙x |
| `PwrStoredGrvty` | Rate of change of gravitational potential energy | Pg=−mgZ˙ |

The equations use these variables.

|  |  |
| --- | --- |
| *ω* | Wheel angular velocity |
| *b* | Linear velocity force component |
| *Fx* | Longitudinal force developed by the tire road interface due to slip |
| *Fcp* | Tire slip force at contact patch |
| *Fz* | Vehicle normal force |
| *Fzb* | Tire normal force due to wheel damping |
| *Fzk* | Tire normal force due to wheel stiffness |
| *Iyy* | Wheel rotational inertia |
| *Mbrk* | Braking moment |
| *My* | Rolling resistance torque |
| *Re* | Effective tire radius while under load and for a given pressure |
| *T* | Axle torque applied on wheel |
| *Vx* | Longitudinal axle velocity |
| z,z˙,z¨ | Tire displacement, velocity, and acceleration, respectively |
| *ω* | Wheel angular velocity |
| Z˙ | Vehicle vertical velocity along the vehicle-fixed *z*-axis |
