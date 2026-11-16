---
type: simulink-block
title: 'SynRM FeedForward Control'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'synrmfeedforwardcontrol'
documentation_source_path: 'ref/synrmfeedforwardcontrol.html'
language: en
---

# SynRM FeedForward Control

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

Mechanical speed of the rotor (in rad/s).

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

### **Vsat** — Output voltage saturation limit scalar

Variable saturation limit (in volts) for the output voltages
*Vd
FF* and
*Vq
FF*.

#### Dependencies

To enable this port, set **Vsat input method** to
`Input port`.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **Vd FF** — D-axis feedforward voltage gain scalar

Feedforward voltage gain (in volts) along the *d*-axis of
the rotating *dq* reference frame.

**Data Types:** `single` | `double` | `fixed point`

### **Vq FF** — Q-axis feedforward voltage gain scalar

Feedforward voltage gain (in volts) along the *q*-axis of
the rotating *dq* reference frame.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### Motor Parameters

### **Motor topology** — Synchronous reluctance motor topology `Synchronous reluctance motor` (default) | `PM-assisted synchronous reluctance motor`

Type of synchronous reluctance motor.

### **Definition of d-axis and q-axis** — Alignment of *d*- and *q*-axes `Ld > Lq (different from PMSM)` (default) | `Lq > Ld (same as PMSM)`

Type of alignment for the *d*- and
*q*-axes. You can select one of the following options:

- `Ld > Lq (different from PMSM)` — Select this
  option to use a *d*- and *q*-axes
  alignment that is different from that of PMSM.
- `Lq > Ld (same as PMSM)` — Select this option
  to use a *d*- and *q*-axes alignment
  that is identical to that of PMSM.

For more information regarding the type of alignment, see SynRM Constraint Curves and Their Application.

### **Number of pole pairs** — Number of pole pairs available in motor `4` (default) | scalar

Number of pole pairs available in the motor.

### **Motor parameter input method** — Type of motor parameters `Linear model with lumped parameters` (default) | `Non-linear model with D,Q-flux linkage LUTs` | `Non-linear model with Ld and Lq LUTs` | `Non-linear model with Ld, Lq and FluxPM LUTs` | `Input port based Ld and Lq` | `Input port based Ld, Lq, and FluxPM`

Motor parameters that the block uses to generate feedforward gains.

- `Linear model with lumped parameters` —
  Generate feedforward voltages using lumped circuit values for motor
  parameters *Ld*, *Lq*, and *FluxPM*.
- `Non-linear model with D,Q-flux linkage LUTs`
  — Generate feedforward voltages using *d*-axis flux
  linkage *FluxD* and *q*-axis flux
  linkage *FluxQ* lookup tables (LUTs).
- `Non-linear model with Ld and Lq LUTs` —
  Generate feedforward voltages using
  *Ld* and
  *Lq* LUTs, specified as
  block parameters.
- `Non-linear model with Ld, Lq and FluxPM
  LUTs` — Generate feedforward voltages using
  *Ld*,
  *Lq*, and
  *FluxPM* LUTs, specified as block parameters.
- `Input port based Ld and Lq` — Generate
  feedforward voltages using *Ld* and *Lq* LUTs, specified as block inputs.
- `Input port based Ld, Lq, and FluxPM` —
  Generate feedforward voltages using *Ld*, *Lq*, and *FluxPM* LUTs, specified as block
  inputs.

#### Dependencies

- To enable `Non-linear model with Ld and Lq
  LUTs` and `Input port based Ld and
  Lq` options, set **Motor topology**
  to `Synchronous reluctance motor`.
- To enable `Non-linear model with Ld, Lq, and FluxPM
  LUTs` and `Input port based Ld, Lq, and
  FluxPM` options, set **Motor
  topology** to `PM-assisted synchronous
  reluctance motor`.

### **Vsat input method** — Input method for Vsat `Specify via dialog` (default) | `Input port`

Use one of these methods to specify the output voltage saturation limit
(*Vsat*).

- `Specify via dialog` — Specify the fixed output voltage
  saturation limit *Vsat* using the **Output voltage
  saturation (V)** parameter.
- `Input port` — Specify the variable output voltage
  saturation limit *Vsat* using the input port
  **Vsat**.

### **Output saturation (V)** — Saturation limit for output values `24/sqrt(3)` (default) | scalar

Saturation limit (in volts) for the output voltages
*Vd
FF* and *Vq
FF*.

#### Dependencies

To enable this parameter, set **Vsat input method** to
`Specify via dialog`.

### **D-axis current breakpoint vector (A)** — D-axis current lookup vector `[0,10,20,30]` (default) | vector

D-axis current vector (in amperes) in these lookup tables, depending on the
method you use to specify the motor parameters.

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
LUTs`, or `Non-linear model with Ld, Lq, and
FluxPM LUTs`.

### **Q-axis current breakpoint vector (A)** — Q-axis current lookup vector `[0,10,20,30,40]` (default) | vector

Q-axis current vector (in amperes) in these lookup tables, depending on the
method you use to specify the motor parameters.

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
LUTs`, or `Non-linear model with Ld, Lq, and
FluxPM LUTs`.

### Linear Model with Lumped Parameters

### **Stator d-axis inductance (H)** — D-axis stator winding inductance `0.9e-3` (default) | scalar

Stator winding inductance (in henries) along the direct-axis of the rotating
*dq* reference frame.

#### Dependencies

To enable this parameter, set **Motor parameter input method**
to `Linear model with lumped parameters`.

### **Stator q-axis inductance (H)** — Q-axis stator winding inductance `0.15e-3` (default) | scalar

Stator winding inductance (in henries) along the quadrature-axis of the rotating
*dq* reference frame.

#### Dependencies

To enable this parameter, set **Motor parameter input method**
to `Linear model with lumped parameters`.

### **Permanent magnet flux linkage (Wb)** — PM flux linkage `6.4e-3` (default) | scalar

Peak permanent magnet flux linkage (in weber).

#### Dependencies

To enable this parameter, set **Motor topology** to
`PM-assisted synchronous reluctance motor` and
**Motor parameter input method** to `Linear
model with lumped parameters`.

### Non-Linear Model with D,Q-Flux Linkage LUTs

### **D-axis flux linkage LUT, FluxD(id,iq) (Wb)** — D-axis flux linkage lookup data `[0,0,0,0,0;0,0,0,0,0.0090;0,0,0,0,0.0180;0,0,0,0,0.0270]` (default) | matrix

D-axis flux linkage
*FluxD(id,iq)*
lookup table data (in weber).

#### Dependencies

To enable this parameter, set **Motor parameter input method**
to `Non-linear model with D,Q-flux linkage LUTs`.

### **Q-axis flux linkage LUT, FluxQ(id,iq) (Wb)** — Q-axis flux linkage lookup data `[0,0,0,0,0.0060;0,0,0,0,0.0060;0,0,0,0,0.0060;0,0,0,0,0.0060]` (default) | matrix

Q-axis flux linkage
*FluxQ(id,iq)*
lookup table data (in weber).

#### Dependencies

To enable this parameter, set **Motor parameter input method**
to `Non-linear model with D,Q-flux linkage LUTs`.

### Non-Linear Model with *Ld* and *Lq* (as well as *Ld*, *Lq*, and *FluxPM*) LUTs

### **Ld LUT, Ld(id,iq) (H)** — D-axis inductance lookup data `0.9e-3 * ones(4, 5)` (default) | matrix

D-axis inductance
*Ld(id,iq)*
lookup table data (in henries).

#### Dependencies

To enable this parameter, set **Motor parameter input
method** to either `Non-linear model with Ld and Lq
LUTs` or `Non-linear model with Ld, Lq, and
FluxPM LUTs`.

### **Lq LUT, Lq(id,iq) (H)** — Q-axis inductance lookup data `0.15e-3 * ones(4, 5)` (default) | matrix

Q-axis inductance
*Lq(id,iq)*
lookup table data (in henries).

#### Dependencies

To enable this parameter, set **Motor parameter input
method** to either `Non-linear model with Ld and Lq
LUTs` or `Non-linear model with Ld, Lq, and
FluxPM LUTs`.

### **PM flux linkage LUT, FluxPM(id,iq) (Wb)** — PM flux linkage lookup data `6.4e-3 * ones(4, 5)` (default) | matrix

Permanent magnet flux linkage
*FluxPM(id,iq)*
lookup table data (in weber).

#### Dependencies

To enable this parameter, set **Motor parameter input
method** to `Non-linear model with Ld, Lq and FluxPM
LUTs`.

### Input Units

### **Input units** — Unit of input values `Per-Unit (PU)` (default) | `SI Units`

Unit of measure of the input values.

### **Base voltage (V)** — Nominal voltage limit `24/sqrt(3)` (default) | scalar

Base voltage (in volts) for the per-unit system.

#### Dependencies

To enable this parameter, set **Input units** to
`Per-Unit (PU)`.

### **Base current (A)** — Nominal current limit `19.3` (default) | scalar

Base current (in amperes) for the per-unit system.

#### Dependencies

To enable this parameter, set **Input units** to
`Per-Unit (PU)`.

### **Base speed (rpm)** — Nominal speed limit `4107` (default) | scalar

Base speed (in rpm) for the per-unit system.

#### Dependencies

To enable this parameter, set **Input units** to
`Per-Unit (PU)`.

### **Allow scaled-down motor parameters with CodeGen (higher precision with Fixed-Point data type)** — Scale down internal parameters to match per-unit scale `on` (default) | `off`

Option to scale down internal parameters to match the per-unit scale when
generating code.

- When you enable this option, the block scales down the internal constants and
  coefficients to match the per-unit scale. This allows for higher precision when
  you use the fixed-point data type. If you use this option with the single or
  double data type, some precision loss can occur depending on the number of bits
  allotted to the integer portion.
- When you disable this option, the block converts all the constants and
  coefficients it uses for internal calculations to SI units and then converts them
  back to the PU scale. This allows you to update the lookup table values in the
  generated code, typically, for applications such as controller tuning or
  end-of-line operations. You can also update the values manually for debugging or
  reusing previously generated code.

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

Decouple d -axis and q -axis current to eliminate disturbance

The SynRM FeedForward Control block decouples *d*-axis
and *q*-axis current controls and generates the corresponding feedforward
voltage gains to enable field-oriented control of a synchronous reluctance motor (SynRM)
and permanent magnet-assisted synchronous reluctance motor (PMaSynRM).

You can input feedback values of *d*-axis and *q*-axis
currents and the mechanical speed of the rotor.

The block generates feedforward gains from the specified motor parameters using one of
these methods:

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

In addition, you can use the **Vsat input method** parameter to
configure the block to accept a fixed saturation voltage through the **Output
saturation (V)** parameter or a variable saturation voltage through a separate
input port **Vsat**.

### Equations

If you select `Per-Unit (PU)` in the **Input
units** parameter, the block scales down the internal parameters to match
the per-unit scale by default. You can also configure the block to convert the inputs to
SI units before performing any computation and convert them back to per-unit values
after calculating the output by using the **Allow scaled-down motor parameters
with CodeGen (higher precision with Fixed-Point data type)**
parameter.

These equations describe how the block computes feedforward gain.

**Note**

The following equations for SynRM and PMaSynRM follow a
*d*-*q* axis notation that is identical to
that of a permanent magnet synchronous motor (PMSM).

ωe=pωm

For both SynRM and PMaSynRM:

VdFF=−ωeψq=−ωeLqIq

For SynRM:

VqFF=ωeψd=ωeLdId

For PMSynRM:

VqFF=ωeψd=ωeLdId+ωeψm

where:

- p is the number of pole pairs available in the motor.
- ωe is the electrical speed corresponding to frequency of stator voltages
  (rad/s).
- Ld and Lq are the *d*-axis and *q*-axis stator
  winding inductances (henries).
- Id and Iq are the *d*-axis and *q*-axis
  currents (amperes).
- *ψd* and
  *ψq*are the magnetic fluxes along the
  *d-* and *q*-axes (weber).
- *ψm* is the permanent magnet flux linkage
  (weber).

For a detailed set of equations and assumptions that Motor Control Blockset™ uses for a synchronous reluctance machine, see Synchronous Reluctance Machine (Simscape Electrical).
