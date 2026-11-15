---
type: simulink-block
title: 'Tire-Road Interaction (Magic Formula)'
family: 'sdl'
product_id: 'sdl'
product_name: 'Simscape Driveline'
documentation_release: R2025b
official_category: 'Tires and Vehicles'
documentation_page: 'tireroadinteractionmagicformula'
documentation_source_path: 'ref/tireroadinteractionmagicformula.html'
language: en
---

# Tire-Road Interaction (Magic Formula)

## Ports

### Input

### **N** — Normal force, N physical signal

Physical signal input port associated with the normal force acting on
the tire, in N. The normal force is positive if it acts downward on the
tire, pressing it against the pavement.

### **M** — Magic formula coefficients, unitless physical signal | vector

Physical signal input port associated with the Magic Formula coefficients. Provide the
Magic Formula coefficients as a four-element vector specified in the
order [*B*, *C*,
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

### **T** — Tire tread mechanical rotational

Mechanical rotational port associated with the tire tread.

### **H** — Hub mechanical rotational

Mechanical rotational port associated with the wheel hub.

## Parameters

### Main

### **Parameterize by** — Parameterization method `Peak longitudinal force and corresponding slip` (default) | `Constant Magic Formula coefficients` | `Load-dependent Magic Formula coefficients` | `Physical signal Magic Formula coefficients`

Magic Formula tire simulation option. Select how the block parameterizes the tire using
the Magic Formula:

- `Peak longitudinal force and corresponding
  slip` — Parameterize the Magic Formula by
  using the physical characteristics of the tire.
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

Contact slip *κ'0*, expressed
as a percentage (%), when the longitudinal force equals its maximum
value *Fx0* and the vertical
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

Nominal normal force *Fz0* on
tire.

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

### Scaling

### **Enable scaling coefficients** — Scaling option `off` (default) | `on`

Whether to include scaling coefficients in the Magic Formula
parameterization.

#### Dependencies

To enable this parameter, set **Parameterize by**
to `Load-dependent Magic Formula
coefficients`.

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

To enable this parameter, set **Parameterize by** to
`Load-dependent Magic Formula
coefficients` and select **Enable scaling
coefficients**.

### Advanced

### **Lower boundary of slip denominator, VXLOW** — Lower boundary of slip denominator `1` `m/s` (default) | positive scalar

Lower boundary of slip denominator,
*VXLOW*.
`VXLOW` is the TIR file identifier.

### **Velocity threshold** — Wheel hub velocity threshold for mathematical slip model `0.1` `m/s` (default) | positive scalar

Wheel hub velocity, *Vth*, below which the block
smooths the transition to zero.

### **Minimum valid wheel slip, KPUMIN** — Minimum wheel slip threshold `-1.5` (default) | scalar

Minimum valid wheel slip.
A
negative value represents wheel slip in the reverse rotational
direction.

### **Maximum valid wheel slip, KPUMAX** — Maximum wheel slip threshold `1.5` (default) | scalar

Maximum valid wheel slip.

## Libraries

Simscape / Driveline / Tires & Vehicles / Tire Subcomponents

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

You can set **Parameterize by** to `Load-dependent Magic
Formula coefficients` to enable load-dependent Magic Formula
coefficients.

These parameters are new for all parameterizations:

- **Lower boundary of slip denominator, VXLOW**
- **Minimum valid wheel slip, KPUMIN**
- **Maximum valid wheel slip, KPUMAX**

## Description

Tire-road dynamics given by Magic Formula coefficients

The Tire-Road Interaction (Magic Formula) block represents
the interaction between the tire tread and the road pavement. The Magic Formula predicts
the longitudinal force that results from this interaction by using an empirical equation
based on fitting coefficients. The block ignores tire properties such as compliance and
inertia. You can easily visualize the longitudinal friction force with respect to the
wheel slip. To view the figure, click the **Plot friction force versus
slip** hyperlink in the **Description** section of the
block dialog box.

Longitudinal force versus wheel slip figure window

### Tire-Road Interaction Model

The block represents the longitudinal forces at the tire-road contact patch using the Magic
Formula of Pacejka [2].

The figure displays the forces on the tire. The table defines the tire model
variables.

Tire illustration demonstrating F\_z, F\_x, V\_x, and rotational velocity, Omega

| Symbol | Description |
| --- | --- |
| *Ω* | Wheel angular velocity. |
| *rw* | Wheel radius. |
| *Vx* | Wheel hub longitudinal velocity. |
| rwΩ | Tire tread longitudinal velocity. |
| *u* | Tire longitudinal deformation. |
| VT=rwΩ′=rwΩ+u˙ | Tire tread longitudinal velocity. Typically, the tire tread longitudinal velocity has a component due to tire rotation, *rwΩ*, and an optional component due to tire deformation, u˙. Because port **T** computes *VT*, the calculations for tire rotations and deformation occur outside of the block. |
| Vsx=Vx−VT | Contact patch slip velocity. If there is no tire longitudinal compliance, then u=0. |
| k=−Vsx|Vx|smooth | Wheel slip for a tire without compliance. |
| *Fz* | Vertical load on tire. |
| *Fz0* | Nominal vertical load on tire. |
| Fx=f(k,Fz) | Longitudinal force exerted on the tire at the contact point.  *f* is a characteristic function of the tire. |

### Tire Response

You can model tire roll and slip.

**Forces and Characteristic Function**

The block uses a steady-state tire characteristic function, Fx=f(k,Fz), where:

- *Fx* is the longitudinal force
  on the tire.
- *Fz* is the vertical
  load.
- *k* is the wheel slip

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

**Magic Formula Coefficients for Typical Road Conditions**

The block uses numerical values based on empirical tire data. These values are typical
sets of constant Magic Formula coefficients for common road conditions.

| Surface | B | C | D | E |
| --- | --- | --- | --- | --- |
| Dry tarmac | 10 | 1.9 | 1 | 0.97 |
| Wet tarmac | 12 | 2.3 | 0.82 | 1 |
| Snow | 5 | 2 | 0.3 | 1 |
| Ice | 4 | 2 | 0.1 | 1 |

### Parameterizations

**Peak Longitudinal Force and Corresponding Slip**

When you set **Parameterize by** to `Peak
longitudinal force and corresponding slip`, the block uses a
representative set of Magic Formula coefficients. The block scales the
coefficients to yield the peak longitudinal force
*Fx0* at the corresponding slip
*κ0* that you specify, for rated
vertical load *Fz0*.

**Magic Formula with Constant Coefficients**

When you set **Parameterize by** to `Constant Magic Formula
coefficients`, the block uses the dimensionless coefficients,
*B*, *C*, *D*, and
*E*, or stiffness, shape, peak, and curvature, such
that

Fx=f(κ,Fz)=Fz⋅D⋅sin(C⋅arctan{Bκ−E[Bκ−arctan(Bκ)]}).

The slope of *f* at k=0 is BCD⋅Fz.

**Magic Formula with Load-Dependent Coefficients**

When you set **Parameterize by** to
`Load-dependent Magic Formula coefficients`, the
block uses dimensionless coefficients that are functions of the tire load. A
more complex set of parameters `p_i`, entered in the property
inspector, specifies these functions:

Fx0=Dxsin(Cxarctan{Bxκx−Ex[Bxκx−arctan(Bxκx)]})+SVx,

where:

dfz= (Fz–Fz0)Fz0

κx=κ+SHx

Cx= p\_Cx1

Dx=μx·Fz

μx= p\_Dx1 + p\_Dx2·dfz

Ex= (p\_Ex1 + p\_Ex2·dfz+ p\_Ex3·dfz2)[1 – p\_Ex4·sgn(κx)]

Kxκ=Fz⋅(p\_Kx1 + p\_Kx2·dfz)⋅e(p\_Kx3·dfz)

Bx=KxκCxDx+εx

SHx= p\_Hx1 + p\_Hx2·dfz

SVx=Fz·(p\_Vx1 + p\_Vx2·dfz)

*SHx* and
*SVx* represent offsets to the
slip and longitudinal force in the force-slip function, or horizontal and
vertical offsets if the function is plotted as a curve.
*μx* is the longitudinal
load-dependent friction coefficient.
*εx* is a small number that prevents
division by zero as *Fz* approaches
zero.

### Assumptions and Limitations

The Tire-Road Interaction (Magic Formula) block
assumes only longitudinal motion and includes no camber, turning, or lateral
motion.
