---
type: simulink-block
title: 'SynRM Torque Estimator'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Control Algorithm Design / Controls / Control Reference'
documentation_page: 'synrmtorqueestimator'
documentation_source_path: 'ref/synrmtorqueestimator.html'
language: en
---

# SynRM Torque Estimator

## Ports

### Input

### **Id** — D-axis current scalar

Current (in amperes) along the *d*-axis of the rotating
*dq* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **Iq** — Q-axis current scalar

Current (in amperes) along the *q*-axis of the rotating
*dq* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **ωm** — Mechanical speed of rotor scalar

Mechanical speed (in rad/s) of the rotor.

**Data Types:** `single` | `double` | `fixed point`

### **Ld** — D-axis inductance scalar

D-axis winding inductance (in henries).

#### Dependencies

To enable this input port, set **Motor parameter input
method** to either `Input port based Ld and
Lq` or `Input port based Ld, Lq and
FluxPM`.

**Data Types:** `single` | `double` | `fixed point`

### **Lq** — Q-axis inductance scalar

Q-axis winding inductance (in henries).

#### Dependencies

To enable this input port, set **Motor parameter input
method** to either `Input port based Ld and
Lq` or `Input port based Ld, Lq and
FluxPM`.

**Data Types:** `single` | `double` | `fixed point`

### **FluxPM** — Permanent magnet flux linkage scalar

Peak permanent magnet flux linkage (in weber).

#### Dependencies

To enable this input port, set **Motor topology** to
`PM-assisted synchronous reluctance motor` and
**Motor parameter input method** to `Input
port based Ld, Lq and FluxPM`.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **Te** — Estimated torque scalar

Mechanical torque (in Nm) output of the motor.

**Data Types:** `single` | `double` | `fixed point`

### **Pe** — Estimated power scalar

Power output of the motor (in watts).

**Data Types:** `single` | `double` | `fixed point`

## Parameters

#### Motor Parameters

### **Motor topology** — Synchronous reluctance motor topology `Synchronous reluctance motor` (default) | `PM-assisted synchronous reluctance motor`

Type of synchronous reluctance motor.

### **Definition of d-axis and q-axis** — Alignment of *d*- and *q*-axes `Ld > Lq (different from PMSM)` (default) | `Lq > Ld (same as PMSM)`

Type of alignment for the *d*- and *q*-axes.
You can select one of the following options:

- `Ld > Lq (different from PMSM)` — Select this
  option to use a *d*- and *q*-axes
  alignment that is different from that of PMSM.
- `Lq > Ld (same as PMSM)` — Select this option to
  use a *d*- and *q*-axes alignment that is
  identical to that of PMSM.

For more information regarding the type of alignment, see SynRM Constraint Curves and Their Application.

### **Number of pole pairs** — Number of pole pairs available in motor `4` (default) | scalar

Number of pole pairs available in the motor.

### **Motor parameter input method** — Type of motor parameters `Linear model with lumped parameters` (default) | `Non-linear model with D,Q-flux linkage LUTs` | `Non-linear model with Ld and Lq LUTs` | `Non-linear model with Ld, Lq, and FluxPM LUTs` | `Input port based Ld and Lq` | `Input port based Ld, Lq, and FluxPM`

Motor parameters that the block uses to generate torque and power estimates.

- `Linear model with lumped parameters` — Generate
  estimates using lumped-circuit values for motor parameters
  *Ld*,
  *Lq*, and
  *FluxPM*.
- `Non-linear model with D,Q-flux linkage LUTs` —
  Generate estimates using *d*-axis flux linkage
  *FluxD* and *q*-axis flux linkage
  *FluxQ* lookup tables (LUTs).
- `Non-linear model with Ld and Lq LUTs` — Generate
  estimates using *Ld* and
  *Lq* LUTs, specified as block
  parameters.
- `Non-linear model with Ld, Lq, and FluxPM LUTs` —
  Generate estimates using *Ld*, *Lq*, and *FluxPM* LUTs, specified as block
  parameters.
- `Input port based Ld and Lq` — Generate estimates
  using *Ld* and
  *Lq* LUTs, specified as block
  inputs.
- `Input port based Ld, Lq and FluxPM` — Generate
  estimates using *Ld*, *Lq*, and *FluxPM* LUTs, specified as block
  inputs.

### **D-axis current breakpoint vector, id (A)** — D-axis current lookup vector `[0,10,20,30]` (default) | vector

D-axis current vector used in the following lookup tables, depending on the
method used to specify the motor parameters.

- *FluxD(id,iq)*
  and
  *FluxQ(id,iq)*
  for the `Non-linear model with D,Q-flux linkage
  LUTs` method.
- *Ld(id,iq)*,
  *Lq(id,iq)*,
  and
  *FluxPM(id,iq)*
  for the `Non-linear model with Ld, Lq, and FluxPM
  LUTs` method.

#### Dependencies

To enable this parameter, set **Motor parameter input
method** to `Non-linear model with D,Q-flux linkage
LUTs`, `Non-linear model with Ld and Lq
LUTs`, or `Non-linear model with Ld, Lq, and FluxPM
LUTs`.

### **Q-axis current breakpoint vector, iq (A)** — Q-axis current lookup vector `[0,10,20,30,40]` (default) | vector

Q-axis current vector used in the following lookup tables, depending on the
method used to specify the motor parameters.

- *FluxD(id,iq)*
  and
  *FluxQ(id,iq)*
  for the `Non-linear model with D,Q-flux linkage
  LUTs` method.
- *Ld(id,iq)*,
  *Lq(id,iq)*,
  and
  *FluxPM(id,iq)*
  for the `Non-linear model with Ld, Lq, and FluxPM
  LUTs` method.

#### Dependencies

To enable this parameter, set **Motor parameter input
method** to `Non-linear model with D,Q-flux linkage
LUTs`, `Non-linear model with Ld and Lq
LUTs`, or `Non-linear model with Ld, Lq, and FluxPM
LUTs`.

#### Linear Model with Lumped Parameters

### **Stator d-axis inductance, Ld (H)** — D-axis stator winding inductance `0.9e-3` (default) | scalar

Stator winding inductance (henry) along the direct-axis of the rotating
*dq* reference frame.

#### Dependencies

To enable this parameter, set **Motor parameter input method** to
`Linear model with lumped parameters`.

### **Stator q-axis inductance, Lq (H)** — Q-axis stator winding inductance `0.15e-3` (default) | scalar

Stator winding inductance (henry) along the quadrature-axis of the rotating
*dq* reference frame.

#### Dependencies

To enable this parameter, set **Motor parameter input method** to
`Linear model with lumped parameters`.

### **Permanent magnet flux linkage, FluxPM (Wb)** — Permanent magnet flux linkage `0.4e-4` (default) | scalar

Peak permanent magnet flux linkage (weber).

#### Dependencies

To enable this parameter, set **Motor topology** to
`PM-assisted synchronous reluctance motor` and
**Motor parameter input method** to `Linear
model with lumped parameters`.

#### Non-Linear Model with D,Q-Flux Linkage LUTs

### **D-axis flux linkage LUT, FluxD(id,iq) (Wb)** — D-axis flux linkage lookup data `[0,0,0,0,0;0.009,0.009,0.009,0.009,0.0090;0.018,0.018,0.018,0.018,0.0180;0.027,0.027,0.027,0.027,0.0270]` (default) | matrix

D-axis flux linkage
*FluxD(id,iq)* lookup
table data (in weber).

#### Dependencies

To enable this parameter, set **Motor parameter input method** to
`Non-linear model with D,Q-flux linkage LUTs`.

### **Q-axis flux linkage LUT, FluxQ(id,iq) (Wb)** — Q-axis flux linkage lookup data `[0,0.0015,0.0030,0.0045,0.0060;0,0.0015,0.0030,0.0045,0.0060;0,0.0015,0.0030,0.0045,0.0060;0,0.0015,0.0030,0.0045,0.0060]` (default) | matrix

Q-axis flux linkage
*FluxQ(id,iq)* lookup
table data (in weber).

#### Dependencies

To enable this parameter, set **Motor parameter input method** to
`Non-linear model with D,Q-flux linkage LUTs`.

#### Non-Linear Model with *Ld* and *Lq* (as well as *Ld*, *Lq*, and *FluxPM*) LUTs

### **Ld LUT, Ld(id,iq) (H)** — D-axis inductance lookup data `0.9e-3 * ones(4, 5)` (default) | matrix

D-axis inductance
*Ld(id,iq)*
lookup table data (in henry).

#### Dependencies

To enable this parameter, set **Motor parameter input
method** to either `Non-linear model with Ld and Lq
LUTs` or `Non-linear model with Ld, Lq, and FluxPM
LUTs`.

### **Lq LUT, Lq(id,iq) (H)** — Q-axis inductance lookup table data `0.15e-3 * ones(4, 5)` (default) | matrix

Q-axis inductance
*Lq(id,iq)*
lookup table data (in henry).

#### Dependencies

To enable this parameter, set **Motor parameter input
method** to either `Non-linear model with Ld and Lq
LUTs` or `Non-linear model with Ld, Lq, and FluxPM
LUTs`.

### **PM flux linkage LUT, FluxPM(id,iq) (Wb)** — PM flux linkage lookup data `0.4e-4 * ones(4, 5)` (default) | matrix

Permanent magnet flux linkage
*FluxPM(id,iq)*
lookup table data (in weber).

#### Dependencies

To enable this parameter, set **Motor topology** to
`PM-assisted synchronous reluctance motor` and
**Motor parameter input method** to `Non-linear
model with Ld, Lq and FluxPM LUTs`.

#### Input Units

### **Input units** — Unit of input values `Per-Unit (PU)` (default) | `SI Units`

Unit of the input values.

### **Base Voltage (V)** — Nominal voltage limit `24/sqrt(3)` (default) | scalar

Base voltage (in volts) for per-unit system.

#### Dependencies

To enable this parameter, set **Input units** to
`Per-Unit (PU)`.

### **Base Current (A)** — Nominal current limit `19.3` (default) | scalar

Base current (in amperes) for per-unit system.

#### Dependencies

To enable this parameter, set **Input units** to
`Per-Unit (PU)`.

### **Base Speed (rpm)** — Nominal speed limit `4107` (default) | scalar

Base speed (in rpm) for per-unit system.

#### Dependencies

To enable this parameter, set **Input units** to
`Per-Unit (PU)`.

### **Base torque (Nm)** — Nominal torque limit `0.93271` (default) | scalar

Base torque (in Nm) for per-unit system. See Per-Unit System page for more
details.

You cannot configure this parameter when you set **Motor parameter
input method** to `Linear model with lumped
parameters`, `Non-linear model with Ld and Lq
LUTs`, or `Non-linear model with Ld, Lq, and FluxPM
LUTs`. The block computes its value using the other
parameters.

#### Dependencies

To display this parameter, set **Input units** to
`Per-Unit (PU)`.

### **Base power (W)** — Nominal power limit `401.143` (default) | scalar

Base power (in W) for per-unit system. See Per-Unit System page for more
details.

You cannot configure this parameter when you set **Motor parameter
input method** to `Linear model with lumped
parameters`, `Non-linear model with Ld and Lq
LUTs`, or `Non-linear model with Ld, Lq, and FluxPM
LUTs`. The block computes its value using the other
parameters.

#### Dependencies

To display this parameter, set **Input units** to
`Per-Unit (PU)`.

### **Allow scaled-down motor parameters with CodeGen (higher precision with Fixed-Point data type)** — Scale down internal parameters to match per-unit scale `on` (default) | `off`

Option to scale down internal parameters to match per-unit scale when generating
code.

- When you enable this option, the block scales down the internal constants and
  coefficients to match the per-unit scale. This allows for higher precision when you
  use the fixed-point data type. If you use this option with the single or double data
  type, some precision loss can occur depending on the number of bits allotted to the
  integer portion.
- When you disable this option, the block converts all the constants and
  coefficients used for internal calculations to SI units and then converts them back
  to the PU scale. This allows you to update the lookup table values in the generated
  code, typically, for applications such as controller tuning or end-of-line
  operations. You can also update the values manually for debugging or reusing
  previously generated code.

#### Dependencies

To enable this parameter, set **Input units** to
`Per-Unit (PU)`.

## Libraries

Motor Control Blockset / Controls / Control Reference

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024a**

## Description

Estimate electromechanical torque and power

The SynRM Torque Estimator block generates electromechanical torque and
power estimates to enable field-oriented control of a synchronous reluctance motor (SynRM)
and permanent magnet-assisted synchronous reluctance motor (PMaSynRM). The block outputs
mathematically computed electromechanical torque for the given motor parameters. To measure
the torque value accurately, consider using a physical sensor.

The block accepts feedback values of *d-* and *q*-axis
currents and mechanical speed as inputs.

The block generates these estimates from motor parameters specified using one of these
methods.

- `Linear model with lumped parameters` — Lumped parameters
  with *d*-axis and *q*-axis stator winding
  inductances and permanent magnet flux linkage.
- `Non-linear model with D,Q-flux linkage LUTs` — Nonlinear
  model with *d*-axis and *q*-axis flux linkage
  lookup tables.
- `Non-linear model with Ld and Lq LUTs` — Nonlinear model
  with *d*-axis and *q*-axis stator winding
  inductance lookup tables.
- `Non-linear model with Ld, Lq, and FluxPM LUTs` —
  Nonlinear model with *d*-axis and *q*-axis stator
  winding inductances and permanent magnet flux linkage lookup tables.
- `Input port based Ld and Lq` — *d*-axis
  and *q*-axis stator winding inductance values provided using
  separate input ports.
- `Input port based Ld, Lq, and FluxPM` —
  *d*-axis and *q*-axis stator winding inductances
  and permanent magnet flux linkage values provided using separate input ports.

### Equations

If you select `Per-Unit (PU)` in the **Input
units** parameter, the block scales down the internal parameters to match
the per-unit scale by default. You can also configure the block to convert the inputs to
SI units before performing any computation and convert them back to per unit values
after calculating the output by using the **Allow scaled-down motor parameters
with CodeGen (higher precision with Fixed-Point data type)**
parameter.

These equations describe the computation of electromechanical torque and power
estimates by the block.

**Note**

The following equations for SynRM and PMaSynRM follow a
*d*-*q* axis notation that is identical to
that of a permanent magnet synchronous motor (PMSM).

For SynRM:

Te=32p(Ld−Lq)IdIq

For PMSynRM:

Te=32p{ψmIq+(Ld−Lq)IdIq}

or

For both SynRM and PMaSynRM:

Te=32p(ψdiq−ψqid)

Pe=Te⋅ωm

where:

- Ld and Lq are the *d*-axis and *q*-axis stator
  winding inductances (henry).
- Id and Iq are the *d*-axis and *q*-axis
  current (amperes).
- *ψm* is the permanent magnet flux linkage
  (weber).
- *ψd* and
  *ψq*are the magnetic fluxes along the
  *d-* and *q*-axes (weber).
- p is the number of pole pairs available in the motor.
- ωm is the mechanical speed of the rotor (rad/s).

For a detailed set of equations and assumptions that Motor Control Blockset™ uses for a synchronous reluctance machine, see Synchronous Reluctance Machine (Simscape Electrical).
