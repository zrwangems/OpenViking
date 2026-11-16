---
type: simulink-block
title: 'Tire (Magic Formula)'
family: 'sdl'
product_id: 'sdl'
product_name: 'Driveline'
documentation_release: R2025b
official_category: 'Tires & Vehicles'
documentation_page: 'tiremagicformula'
documentation_source_path: 'ref/tiremagicformula.html'
language: en
---

# Tire (Magic Formula)

## Ports

### Input

### **N** — Normal force, N physical signal

Physical signal input port associated with the normal force acting on
the tire, in N. The normal force is positive if it acts downward on the
tire, pressing it against the pavement.

### **M** — Magic formula coefficients, unitless physical signal | vector

Physical signal input port associated with the Magic Formula
coefficients. Provide the Magic Formula coefficients as a four-element
vector, specified in the order [*B*, *C*,
*D*, *E*].

#### Dependencies

To enable this port, set **Parameterize by** to
`Physical signal Magic Formula
coefficients`.
### Output

### **S** — Slip physical signal

Physical signal output port associated with the relative slip,
*k*, between the tire and road.
### Conserving

### **A** — Axle mechanical rotational

Mechanical rotational port associated with the axle that the tire sits
on.

### **H** — Hub mechanical rotational

Mechanical rotational port associated with the wheel hub.

## Parameters

### Main

### **Parameterize by** — Parameterization method `Peak longitudinal force and corresponding slip` (default) | `Constant Magic Formula coefficients` | `Load-dependent Magic Formula coefficients` | `Physical signal Magic Formula coefficients`

Magic Formula tire simulation option. Select how the block parameterizes the tire using
the Magic Formula:

- `Peak longitudinal force and corresponding
  slip` — Parameterize the Magic Formula with
  the physical characteristics of the tire.
- `Constant Magic Formula
  coefficients` — Specify the parameters that
  define the constant *B*,
  *C*, *D*, and
  *E* coefficients as scalars.
- `Load-dependent Magic Formula
  coefficients` — Specify the parameters that
  define the load-dependent *C*,
  *D*, *E*,
  *K*, *H*, and
  *V* coefficients as vectors, one for
  each coefficient.
- `Physical signal Magic Formula
  coefficients` — Specify the Magic Formula
  coefficients using port **M** as a
  four-element vector in the order [*B*,
  *C*,
  *D*,*E*].

### **Rated vertical load** — Rated load force `3000` `N` (default) | positive scalar

Rated vertical load force
*Fz0*.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Peak longitudinal force and corresponding
slip`.

### **Peak longitudinal force at rated load** — Maximum longitudinal force at rated load `3500` `N` (default) | positive scalar

Maximum longitudinal force
*Fx0* that the tire exerts
on the wheel when the vertical load equals its rated value
*Fz0*.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Peak longitudinal force and corresponding
slip`.

### **Slip at peak force at rated load (percent)** — Percent slip at maximum longitudinal force and rated load `10` (default) | positive scalar

Contact slip, *k0*, expressed as a percentage
(%), when the longitudinal force equals its maximum value
*Fx0* and the vertical
load equals its rated value
*Fz0*.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Peak longitudinal force and corresponding
slip`.

### **Magic Formula B coefficient** — Constant Magic Formula *B* coefficient `10` (default) | positive scalar

Load-independent Magic Formula *B*
coefficient.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Constant Magic Formula
coefficients`.

### **Magic Formula C coefficient** — Constant Magic Formula *C* coefficient `1.9` (default) | positive scalar

Load-independent Magic Formula *C*
coefficient.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Constant Magic Formula
coefficients`.

### **Magic Formula D coefficient** — Constant Magic Formula *D* coefficient `1` (default) | positive scalar

Load-independent Magic Formula *D*
coefficient.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Constant Magic Formula
coefficients`.

### **Magic Formula E coefficient** — Constant Magic Formula *E* coefficient `0.97` (default) | positive scalar

Load-independent Magic Formula *E*
coefficient.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Constant Magic Formula
coefficients`.

### **Tire nominal vertical load, FNOMIN** — Normal force `4000` `N` (default) | positive scalar

Nominal normal force *Fz0* on the tire.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Load-dependent Magic Formula
coefficients`.

### **Magic Formula C-coefficient parameter, p\_Cx1** — Variable Magic Formula *C* coefficient `1.685` (default) | scalar

Load-dependent Magic Formula *C* coefficient.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Load-dependent Magic Formula
coefficients`.

### **Magic Formula D-coefficient parameters, [p\_Dx1 p\_Dx2]** — Variable Magic Formula *D* coefficient `[1.21, -.037]` (default) | vector

Load-dependent Magic Formula *D* coefficient.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Load-dependent Magic Formula
coefficients`.

### **Magic Formula E-coefficient parameters, [p\_Ex1 p\_Ex2 p\_Ex3 p\_Ex4]** — Variable Magic Formula *E* coefficient `[.344, .095, -.02, 0]` (default) | vector

Load-dependent Magic Formula *E* coefficient.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Load-dependent Magic Formula
coefficients`.

### **Magic Formula BCD-coefficient parameters, [p\_Kx1 p\_Kx2 p\_Kx3]** — Variable Magic Formula *K* coefficient `[21.51, -.163, .245]` (default) | vector

Load-dependent Magic Formula *K* coefficient.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Load-dependent Magic Formula
coefficients`.

### **Magic Formula H-coefficient parameters, [p\_Hx1 p\_Hx2]** — Variable Magic Formula *H* coefficient `[-.002, .002]` (default) | vector

Load-dependent Magic Formula *H* coefficient.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Load-dependent Magic Formula
coefficients`.

### **Magic Formula V-coefficient parameters, [p\_Vx1 p\_Vx2]** — Variable Magic Formula *V* coefficient `[0, 0]` (default) | vector

Load-dependent Magic Formula *V* coefficient.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Load-dependent Magic Formula
coefficients`.

### Geometry

### **Effective rolling radius model** — Rolling radius model option `Constant radius` (default) | `Load and velocity dependent (Magic Formula)`

Whether to treat the rolling radius as constant or dependent on load
and velocity.

#### Dependencies

To enable this parameter, set **Parameterize** to
`Load-dependent Magic Formula
coefficients`.

### **Rolling radius** — Loaded tire radius `0.3` `m` (default) | positive scalar

Loaded tire-wheel radius,
*rw*.

#### Dependencies

To enable this parameter, either set:

- **Parameterize by** to
  `Load-dependent Magic Formula
  coefficients` and **Effective
  rolling radius model** to
  `Constant radius`,
  or
- **Parameterize by** to
  `Peak longitudinal force and
  corresponding slip`,
  `Constant Magic Formula
  coefficients`, or `Physical
  signal Magic Formula
  coefficients`.

### **Non-rolling free tire radius, R0** — Non-rolling free tire radius `0.3` `m` (default) | positive scalar

Non-rolling free tire radius value associated with the Magic Formula.
`R0` is the TIR file identifier.

#### Dependencies

To enable this parameter, set **Parameterize by** to
`Load-dependent Magic Formula
coefficients` and **Effective rolling
radius model** to `Load and velocity
dependent (Magic Formula)`.

### **Low load stiffness effective rolling radius, BREFF** — *Breff* variable `8.39` (default) | positive scalar

Effective rolling radius at low load stiffness.
`BREFF` is the TIR file identifier.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Load-dependent Magic Formula
coefficients` and **Effective rolling
radius model** to `Load and velocity
dependent (Magic Formula)`.

### **Peak value of effective rolling radius, DREFF** — *Dreff* variable `0.26` (default) | positive scalar

Peak value of effective rolling radius. `DREFF` is
the TIR file identifier.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Load-dependent Magic Formula
coefficients` and **Effective rolling
radius model** to `Load and velocity
dependent (Magic Formula)`.

### **High load stiffness effective rolling radius, FREFF** — *Freff* variable `0.074` (default) | positive scalar

Effective rolling radius at high load stiffness.
`FREFF` is the TIR file identifier.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Load-dependent Magic Formula
coefficients` and **Effective rolling
radius model** to `Load and velocity
dependent (Magic Formula)`.

### **Ratio of nominal tire radius with non-rolling free tire radius, Q\_RE0** — *qre0* variable `0.99` (default) | positive scalar

Ratio of the nominal tire radius to the non-rolling free tire radius.
`Q_RE0` is the TIR file identifier.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Load-dependent Magic Formula
coefficients` and **Effective rolling
radius model** to `Load and velocity
dependent (Magic Formula)`.

### **Tire radius increase with speed, Q\_V1** — *qv1* variable `0.008` (default) | positive scalar

Tire radius increase with respect to speed. `Q_V1` is
the TIR file identifier.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Load-dependent Magic Formula
coefficients` and **Effective rolling
radius model** to `Load and velocity
dependent (Magic Formula)`.

### **Nominal hub longitudinal speed, LONGVL** — Nominal hub longitudinal speed `17` `m/s` (default) | positive scalar

Nominal hub longitudinal speed. `LONGVL` is the TIR
file identifier.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Load-dependent Magic Formula
coefficients` and **Effective rolling
radius model** to `Load and velocity
dependent (Magic Formula)`.

### **Vertical stiffness** — Vertical stiffness `5e5` `N/m` (default) | positive scalar

Vertical stiffness of the tire.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Load-dependent Magic Formula
coefficients` and **Effective rolling
radius model** to `Load and velocity
dependent (Magic Formula)`.

### Rolling Resistance

### **Model rolling resistance** — Rolling resistance option `off` (default) | `on`

Whether to include rolling resistance in the tire simulation.

### **Resistance model** — Rolling resistance option `Constant coefficient` (default) | `Pressure and velocity dependent SAE J2452` | `Pressure and velocity dependent (Magic Formula)`

Whether to include resistance using a constant coefficient or pressure
and velocity dependent resistance:

- `Constant coefficient` — Neglect
  rolling resistance.
- `Pressure and velocity dependent SAE
  J2452` — Parameterize rolling resistance in
  accordance with SAE J2452.
- `Pressure and velocity dependent (Magic
  Formula)` — Parameterize rolling resistance in
  accordance with the Magic Formula.

#### Dependencies

To enable this parameter, select **Model rolling
resistance**.

### **Constant coefficient** — Proportionality constant `0.015` (default) | positive scalar

Coefficient that sets the proportionality between the normal force and
the rolling resistance force. The parameter must be greater than
zero.

#### Dependencies

To enable this parameter, select **Model rolling
resistance** and set **Rolling
resistance** to `Constant
coefficient`.

### **Tire pressure** — Tire pressure `250e3` `Pa` (default) | positive scalar

Inflation pressure of the tire. The parameter must be greater than
zero.

#### Dependencies

To enable this parameter, select **Model rolling
resistance** and set **Rolling
resistance** to `Pressure and velocity
dependent SAE J2452` or `Pressure and
velocity dependent (Magic Formula)`.

### **Alpha** — Tire pressure equation exponent `-0.003` (default) | scalar

Exponent of the tire pressure in the model equation.

#### Dependencies

To enable this parameter, select **Model rolling
resistance** and set **Rolling
resistance** to `Pressure and velocity
dependent SAE J2452`.

### **Beta** — Normal force equation exponent `0.97` (default) | scalar

Exponent of the normal force model equation.

#### Dependencies

To enable this parameter, select **Model rolling
resistance** and set **Rolling
resistance** to `Pressure and velocity
dependent SAE J2452`.

### **Coefficient A** — Velocity-independent force component *A* `84e-4` (default)

Velocity-independent force component in the model equation. The
parameter must be greater than zero.

#### Dependencies

To enable this parameter, select **Model rolling
resistance** and set **Rolling
resistance** to `Pressure and velocity
dependent SAE J2452`.

### **Coefficient B** — Velocity-dependent force component *B* `6.2e-4` `s/m` (default) | positive scalar

Velocity-dependent force component in the model equation. The
parameter must be greater than zero.

#### Dependencies

To enable this parameter, select **Model rolling
resistance** and set **Rolling
resistance** to `Pressure and velocity
dependent SAE J2452`.

### **Coefficient C** — Velocity-dependent force component *C* `1.6e-4` `s^2/m^2` (default) | positive scalar

Force component that depends on the square of the velocity term in the
model equation. The parameter must be greater than zero.

#### Dependencies

To enable this parameter, select **Model rolling
resistance** and set **Rolling
resistance** to `Pressure and velocity
dependent SAE J2452`.

### **Tire nominal pressure, NOMPRES** — Nominal tire pressure `240e3` `Pa` (default) | positive scalar

Nominal tire pressure. `NOMPRES` it the TIR file
identifier.

#### Dependencies

To enable this parameter, set **Resistance
model** to `Pressure and velocity dependent
(Magic Formula)`.

### **Tire nominal vertical load, FNOMIN** — Normal force `4000` `N` (default) | positive scalar

Nominal normal force, *Fz0*,
on tire. `FNOMIN` is the TIR file identifier.

#### Dependencies

To enable this parameter, set **Resistance
model** to `Pressure and velocity dependent
(Magic Formula)`.

### **Nominal hub longitudinal speed, LONGVL** — Nominal hub longitudinal speed `16` `m/s` (default) | positive scalar

Nominal hub longitudinal speed. `LONGVL` is the TIR
file identifier.

#### Dependencies

To enable this parameter, set **Resistance
model** to `Pressure and velocity dependent
(Magic Formula)`.

### **Q-coefficient parameters [qsy1 qsy2 qsy3 qsy4 qsy5 qsy6 qsy7 qsy8]** — Magic Formula Q-coefficients `[.0082, 0, .0014, .001, 0, 0, 1.08, -.5]` `1` (default) | vector of length 8

Magic Formula Q coefficients. `qsy1`,…,
`qsy8` correspond to the TIR file
identifiers.

#### Dependencies

To enable this parameter, set **Resistance
model** to `Pressure and velocity dependent
(Magic Formula)`.

### **Velocity threshold for rolling resistance** — Threshold for rolling resistance `0.001` `m/s` (default) | positive scalar

Velocity at which the full rolling resistance force is transmitted to
the rolling hub. The parameter ensures that the force remains continuous
during velocity direction changes, which increases the numerical
stability of the simulation. The parameter must be greater than
zero.

#### Dependencies

To enable this parameter, select **Model rolling
resistance**.

### Scaling

### **Enable scaling coefficients** — Scaling option `off` (default) | `on`

Whether to include scaling coefficients in the Magic Formula
parameterization.

#### Dependencies

To enable this parameter, set **Parameterize
by** to `Load-dependent Magic Formula
coefficients` or set **Resistance
model** to `Pressure and velocity
dependent (Magic Formula)`.

### **Scale factor of Fx nominal vertical load, LFZO** — *Fx* nominal vertical load `1` (default) | positive scalar

Scale factor of the *Fx*
nominal vertical load, *λFZO*.
`LFZO` is the TIR file identifier.

#### Dependencies

To enable this parameter, set **Parameterize by** to
`Load-dependent Magic Formula
coefficients` and select **Enable scaling
coefficients**.

### **Scale factor of Fx shape factor, LCX** — *Fx* shape factor `1` (default) | positive scalar

Scale factor of the *Fx* shape
factor, *λLCX*.
`LCX` is the TIR file identifier.

#### Dependencies

To enable this parameter, set **Parameterize by** to
`Load-dependent Magic Formula
coefficients` and select **Enable scaling
coefficients**.

### **Scale factor of Fx peak friction coefficient, LMUX** — *Fx* peak friction coefficient `1` (default) | positive scalar

Scale factor of the *Fx* peak
friction coefficient, *λμX*.
`LMUX` is the TIR file identifier.

#### Dependencies

To enable this parameter, set **Parameterize by** to
`Load-dependent Magic Formula
coefficients` and select **Enable scaling
coefficients**.

### **Scale factor of Fx curvature factor, LEX** — *Fx* curvature factor `1` (default) | positive scalar

Scale factor of the *Fx*
curvature factor, *λEX*.
`LEX` is the TIR file identifier.

#### Dependencies

To enable this parameter, set **Parameterize by** to
`Load-dependent Magic Formula
coefficients` and select **Enable scaling
coefficients**.

### **Scale factor of Fx slip stiffness, LKX** — *Fx* slip stiffness `1` (default) | positive scalar

Scale factor of the *Fx* slip
stiffness, *λKX*.
`LKX` is the TIR file identifier.

#### Dependencies

To enable this parameter, set **Parameterize by** to
`Load-dependent Magic Formula
coefficients` and select **Enable scaling
coefficients**.

### **Scale factor of Fx horizontal shift, LHX** — *Fx* horizontal shift `1` (default) | positive scalar

Scale factor of the *Fx*
horizontal shift, *λhX*.
`LHX` is the TIR file identifier.

#### Dependencies

To enable this parameter, set **Parameterize by** to
`Load-dependent Magic Formula
coefficients` and select **Enable scaling
coefficients**.

### **Scale factor of Fx vertical shift, LVX** — *Fx* vertical shift `1` (default) | positive scalar

Scale factor of the *Fx*
vertical shift, *λVX*.
`LVX` is the TIR file identifier.

#### Dependencies

To enable this parameter, set **Parameterize by** to
`Load-dependent Magic Formula
coefficients` and select **Enable scaling
coefficients**.

### **Scale factor of rolling resistance, LMY** — Rolling resistance `1` (default) | positive scalar

Scale factor of the rolling resistance,
*λMY*.
`LMY` is the TIR file identifier.

#### Dependencies

To enable this parameter, either set

- **Parameterize by** to
  `Load and velocity dependent (Magic
  Formula)`, or
- **Resistance model** to
  `Pressure and velocity dependent (Magic
  Formula)`

and select **Enable scaling
coefficients**.

### Dynamics

### **Compliance** — Dynamical compliance option `No compliance - Suitable for HIL simulation` (default) | `Specify stiffness and damping`

Whether to the include dynamical compliance of the tire:

- `No compliance - Suitable for HIL
  simulation` — The block neglects dynamical
  compliance.
- `Specify stiffness and damping` — The
  block treats the tire as a spring-damper system under
  load.

### **Longitudinal stiffness** — Longitudinal stiffness `1e6` `N/m` (default) | positive scalar

Tire longitudinal stiffness
*CFx*.

#### Dependencies

To enable this parameter, set **Compliance** to `Specify
stiffness and damping`.

### **Longitudinal damping** — Longitudinal damping `1000` `N/(m/s)` (default) | positive scalar

Tire longitudinal damping
*bFx*.

#### Dependencies

To enable this parameter, set **Compliance** to `Specify
stiffness and damping`.

### **Inertia** — Inertia model `No inertia` (default) | `Specify inertia and initial velocity`

Model for the rotational inertia of the tire.

- `No inertia` — The block neglects
  dynamical compliance.
- `Specify inertia and initial
  velocity` — The block treats the tire as a
  stiff, damped spring and deforms under load.

### **Tire inertia** — Rotational inertia `1` `kg*m^2` (default) | positive scalar

Rotational inertia *Iw* of the
wheel-tire assembly.

#### Dependencies

To enable this parameter, set **Inertia** to `Specify
inertia and initial velocity`.

### **Initial velocity** — Initial rotational velocity `0` `rad/s` (default) | scalar

Initial angular velocity, *Ω*(0), of the tire.

#### Dependencies

To enable this parameter, set **Inertia** to `Specify
inertia and initial velocity`.

### Advanced

### **Lower boundary of slip denominator, VXLOW** — Lower boundary of slip denominator `1` `m/s` (default) | positive scalar

Lower boundary of slip denominator,
*VXLOW*.
`VXLOW` is the TIR file identifier.

### **Velocity threshold** — Tire slip regime threshold `0.1` `m/s` (default) | positive scalar

Threshold velocity the block uses to transition between slip regimes,
*Vth*. To learn more,
see Roll and Slip.

### **Minimum valid wheel slip, KPUMIN** — Minimum wheel slip threshold `-1.5` (default) | scalar

Minimum valid wheel slip.
A
negative value represents wheel slip in the reverse rotational
direction.

### **Maximum valid wheel slip, KPUMAX** — Maximum wheel slip threshold `1.5` (default) | scalar

Maximum valid wheel slip.

## Libraries

Simscape / Driveline / Tires & Vehicles

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2011a**

### R2025a: Visualize friction force versus tread slip

You can now use the **Plot friction force versus slip**
hyperlink in the block dialog box easily visualize the longitudinal friction force
with respect to the wheel slip.

### R2024b: Track power dissipated due to tread slip

The block now logs `power_dissipated` in the
`simlog` workspace variable, which represents power dissipated
due to tread slip.

### R2023a: Magic Formula compatibility enhancements

The block includes a wider set of Magic Formula parameters. You can now parameterize the
block or the effective rolling radius by using load-dependent Magic Formula
coefficients by using these parameter settings:

- **Parameterize by** to `Load-dependent
  Magic Formula coefficients`
- **Effective rolling radius model** to
  `Load and velocity dependent (Magic
  Formula)`

You can also model scaling coefficients when you select
**Enable scaling coefficients**.

These parameters are new for all parameterizations:

- **Lower boundary of slip denominator, VXLOW**
- **Minimum valid wheel slip, KPUMIN**
- **Maximum valid wheel slip, KPUMAX**

## Description

Tire defined by Magic Formula coefficients

The Tire (Magic Formula) block represents a tire with
longitudinal behavior given by the
Magic Formula [1], an empirical equation based on four fitting
coefficients. You can model tire dynamics under constant or variable pavement
conditions. You can easily visualize the longitudinal friction force with respect to the
wheel slip. To view the figure, click the **Plot friction force versus
slip** hyperlink in the **Description** section of the
block dialog box.

Longitudinal force versus wheel slip figure window

The longitudinal direction of the tire is the same as its direction of motion as it
rolls on pavement. This block is a structural component based on the Tire-Road Interaction (Magic Formula) block.

To increase the fidelity of the tire model, you can specify properties such as compliance,
inertia, rolling resistance, and varying effective rolling radius. However, these
properties increase the complexity of the tire model and can slow down simulation.
Consider neglecting tire compliance and inertia if simulating the model in real time or
if preparing the model for hardware-in-the-loop (HIL) simulation.

### Tire Model

The block treats the tire as a rigid wheel-tire combination that is in contact with the
road and subject to slip. When torque drives the wheel axle, the tire transmits
longitudinal force, *Fx*, to the road. The
tire transfers the resulting reaction as a force back on the wheel. This action
rotates the wheel to generate longitudinal motion. If you model tire compliance, the
tire also flexibly deforms under load. If you set the **Effective rolling
radius model** to `Load and velocity dependent (Magic
Formula)`, the tire radius also changes depending on the load and
rotational velocity.

The figure shows the forces acting on the tire. The table defines the tire model
variables.

Tire illustration demonstrating F\_z, F\_x, V\_x, and rotational velocity, Omega

**Tire Model Variables**

| Symbol | Description |
| --- | --- |
| *rw* | Tire rolling radius. |
| *Vx* | Wheel hub longitudinal velocity. |
| *u* | Tire longitudinal deformation. |
| *Ω* | Wheel angular velocity. |
| Ω′=Ω+u˙rW | Contact point angular velocity. If there is no tire longitudinal deformation, u=0. |
| VT=rwΩ′=rwΩ+u˙ | Tire tread longitudinal velocity. Typically, the tire tread longitudinal velocity has a component due to tire rotation, *rwΩ*, and an optional component due to tire deformation, u˙. |
| Vsx=Vx−VT | Contact patch slip velocity. If there is no tire longitudinal compliance, u=0. |
| k=−Vsx|Vx|smooth | Wheel slip for a tire without compliance. |
| *Vth* | Wheel hub threshold velocity. |
| *VXLOW* | Lower boundary of slip denominator. |
| *Fz* | Vertical load on tire. |
| *Fx* | Longitudinal force exerted on the tire at the contact point. |
| CFx=(∂Fx∂u)0 | Tire longitudinal stiffness under deformation. |
| bFx=(∂Fx∂u˙)0 | Tire longitudinal damping under deformation. |
| *Iw* | Wheel-tire inertia, such that the effective mass is equal to Iwrw2 |
| *τdrive* | Torque applied by the axle to the wheel. |

### Tire Kinematics and Response

You can model roll, slip, and deformation.

**Roll and Slip**

The equation for translational motion of a non-slipping, non-compliant tire is Vx=rwΩ. When tires experience slip, they develop a longitudinal force,
*Fx*.

The contact patch slip velocity is Vsx=Vx−rwΩ−u˙. For a tire without compliance, *u* = 0. The unsmoothed contact patch slip is

k=−Vsx|Vx|,

and the block saturates the slip denominator as

|Vx|={VXLOWif  |Vx|<VXLOW|Vx|otherwise

where *VXLOW* is the
**Lower boundary of slip denominator, VXLOW** parameter. The block
smoothly transitions *|Vx|* to
*VXLOW* over the transition regions -*VXLOW* -
*Vth*/2 <
*Vx* <
-*VXLOW* +
*Vth*/2  and *VXLOW* -
*Vth*/2 <
*Vx* <
*VXLOW* +
*Vth*/2. The block saturates slip according to

k={kpuminif −Vsx|Vx|<kpuminkpumaxif −Vsx|Vx|>kpumax−Vsx|Vx|otherwise

where *kpumin* is the **Minimum valid wheel
slip, KPUMIN** parameter and *kpumax* is the **Maximum
valid wheel slip, KPUMAX** parameter. The block transitions
*k* over the regions *kpumin* - *kth*/2
< *k* < *kpumin* +
*kth*/2  and *kpumax* - *kth*/2
< *k* < *kpumax* +
*kth*/2. The block defines the slip smoothing threshold as

kth=Vth1m/s.

For this equation, a locked, sliding wheel has *k* = -1. For perfect rolling, *k* = 0.

**Deformation**

When you set **Compliance** to `Specify stiffness
and damping`, the block treats the tire as flexible. When the
tire deforms, the tire-road contact point turns at a slightly different angular
velocity, *Ω′*, from the wheel velocity, *Ω*,
which generates contact patch slip. The block defines the deforming tire as a
translational spring-damper of stiffness,
*CFx*,
and damping,
*bFx*.

When you set **Compliance** to `No compliance - Suitable for
HIL simulation`, u=0, and there is no tire longitudinal deformation at any time in
the simulation, such that Ω′=Ω.

### Tire and Wheel Dynamics

The block is equivalent to this component diagram. The block simulates both transient and
steady-state behavior and represents starting and stopping. The
Translational Spring and
Translational Damper blocks are equivalent to the
tire stiffness *CFx*
and damping *bFx*,
respectively. The Tire-Road Interaction (Magic
Formula) block represents the longitudinal force
*Fx* on the tire as a function of
*Fz*, and *k* using
the Magic Formula, where *k* is the independent slip variable and
*Fz* is the input signal at port
**N**.

The component diagram visually displays the equivalent Simscape system for the Tire (Magic Formula) block

The block labeled `Rolling Radius` is the tire rolling radius
*rw*. The inertia value is the
effective inertia, Iwrw2. The tire characteristic function
*f*(*k′*,
*Fz*) determines the longitudinal force
*Fx*. Together with the driveshaft
torque applied to the wheel axis, *Fx*
determines the wheel angular motion and longitudinal motion.

When you do not model tire compliance, the block omits the `Longitudinal
Stiffness` and `Longitudinal Damper` blocks in the
diagram, and contact variables revert to wheel variables. In this case, the tire
effectively has infinite stiffness, and port **P** of Rolling Radius
connects directly to port **C** of Ideal Force
Sensor block.

When you set **Rolling Resistance** to a setting other than
`Pressure and velocity dependent (Magic Formula)`, the
block omits the Ideal Force Sensor block and
connection **T** of the Rolling Resistance
block. When you set **Compliance** to `No compliance
- Suitable for HIL simulation`, Port **P** of the
**Rolling Radius** connects directly to the Ideal force sensor
port **C** or port **T** of the Tire-Road
Interaction (Magic Formula) block.

### Effective Rolling Radius

The block determines an effective rolling radius to account for centrifugal growth and
reduction due to loading such that

rw=RΩ−Fz0cz(Dreffarctan(BreffFzFz0)+FreffFzFz0)RΩ=R0(qre0+qv1(ΩR0V0)2)

where:

- *rw* is the effective rolling
  radius.
- *RΩ* is the centrifugal growth
  of the free tire radius.
- *Fz* is the vertical load on
  the tire.
- *Fz0* is the **Tire
  nominal vertical load, FNOMIN** parameter.
- *cz* is the
  **Vertical stiffness** parameter.
- *Ω* is the wheel rotational velocity.

The quantities *Fz* and
*Ω* vary with time.

These quantities correspond to TIR file values and block parameters:

| Variable | TIR File Identifier | Parameter Name |
| --- | --- | --- |
| *Breff* | `BREFF` | **Low load stiffness effective rolling radius, BREFF** |
| *Dreff* | `DREFF` | **Peak value of effective rolling radius, DREFF** |
| *Freff* | `FREFF` | **High load stiffness effective rolling radius, FREFF** |
| *qre0* | `Q_RE0` | **Ratio of nominal tire radius with non-rolling free tire radius, Q\_RE0** |
| *qv1* | `Q_V1` | **Tire radius increase with speed, Q\_V1** |

**Note**

If your TIR file does not provide `Q_RE0` and
`Q_V1`, set these values to 1 and 0, respectively. The
`sdlUtility.tirread` function handles this
automatically.

### Assumptions and Limitations

- The block assumes only longitudinal motion and includes no camber,
  turning, or lateral motion.
- Tire compliance implies a time lag in the response of the tire to the
  forces on it. Time lag simulation increases model fidelity but reduces
  simulation performance. See Adjust Model Fidelity.
