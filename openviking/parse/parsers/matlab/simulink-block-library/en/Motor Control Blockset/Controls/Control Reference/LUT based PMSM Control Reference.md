---
type: simulink-block
title: 'LUT based PMSM Control Reference'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'lutbasedpmsmcontrolreference'
documentation_source_path: 'ref/lutbasedpmsmcontrolreference.html'
language: en
---

# LUT based PMSM Control Reference

## Ports

### Input

### **Tref** — Reference torque value scalar

Reference torque input value (in Nm) for which the block computes the reference
current.

**Data Types:** `single` | `double` | `fixed point`

### **⍵m** — Mechanical speed scalar

Reference mechanical speed value (in rad/sec) for which the block computes the reference
current.

**Data Types:** `single` | `double` | `fixed point`

### **Vdc** — DC bus voltage scalar

Variable DC bus voltage (in volts).

#### Dependencies

To enable this port, set **Vdc input method** to `Input
port - use 3D LUT (voltage slice based)` or
`Input port - use 2D LUT (scaled-w
based)`.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **Idref** — Reference *d*-axis current scalar

Reference *d*-axis phase current (in amperes).

**Data Types:** `single` | `double` | `fixed point`

### **Iqref** — Reference *q*-axis current scalar

Reference *q*-axis phase current (in amperes).

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### Motor Parameters

### **Motor topology** — Type of PMSM `Interior PMSM` (default) | `Surface PMSM`

Type of PMSM based on the placement of the permanent magnets.

### **Field weakening control method** — Type of field weakening control `CVCP` (default) | `CCCP` | `VCLMT` | `NONE`

Type of field weakening control, specified as one of these:

- `CVCP` — Constant voltage constant
  power (CVCP) control method.
- `CCCP` — Constant current constant
  power (CCCP) control method.
- `VCLMT` — Voltage and current limited
  maximum torque (VCLMT) control method.

You can configure this parameter only for a surface PMSM. For a
surface PMSM, the block enables the motor parameters **Motor
parameter input method** and **Vdc input
method** (and therefore, availability of **Motor
Parameters** and their dependencies described in this page
are valid) only when you use the `VCLMT`
control method.

For a surface PMSM, if you set **Field weakening control
method** to `CVCP`,
`CCCP`, or `NONE`,
the block only shows the following motor parameters:

- **Number of pole pairs**
- **Stator resistance per phase, Rs
  (Ohm)**
- **Stator d-axis inductance, Ld
  (H)**
- **Permanent magnet flux linkage
  (Wb)**
- **DC voltage to compute LUTs (V)**
- **Enable custom breakpoint vectors for torque and
  speed**
- **Current Limit, I\_limit (A)**
- **Viscous damping coefficient, Bv
  (Nm-s/rad)**

#### Dependencies

To enable this parameter, set **Motor topology** to
`Surface PMSM` and set **Motor
parameter input method** to either `Linear
model with lumped parameters` or
`Non-linear model with Ld, Lq, and FluxPM
LUTs`.

### **Number of pole pairs** — Number of pole pairs available in motor `4` (default) | scalar

Number of pole pairs available in the motor.

### **Stator resistance per phase, Rs (Ohm)** — Resistance of stator phase winding (ohms) `0.36` (default) | scalar

Resistance of the stator phase winding (in ohms).

### **Vdc input method** — Input method for Vdc `Specify via dialog` (default) | `Input port - use 3D LUT (voltage slice based)` | `Input port - use 2D LUT (scaled-w based)`

Use one of these methods to specify the *Vdc* input.

- `Specify via dialog` — Specify the
  fixed reference voltage *Vdc* using the
  **DC voltage to compute LUTs (V)**
  parameter.
- `Input port - use 3D LUT (voltage slice
  based)` — Specify the variable reference
  voltage *Vdc* using the input port
  **Vdc**. When using this option, the block
  computes the reference current data for the given voltage by
  using a 3-D lookup table (LUT) based on voltage slicing.
- `Input port - use 2D LUT (scaled-w
  based)` — Specify the variable reference
  voltage *Vdc* using the input port
  `Vdc`. When using this option, the block
  computes the reference current data for the given voltage by
  using a 2-D LUT based on motor speed (ω) scaling.

#### Dependencies

To enable this parameter:

- Set **Motor topology** to
  `Interior PMSM`.

or

- Set **Motor topology** to
  `Surface PMSM`.
- Set **Field-weakening control** method to
  `VCLMT`.

### **DC voltage to compute LUTs (V)** — DC bus voltage (volts) `24` (default) | scalar

DC bus voltage (in volts).

#### Dependencies

To enable this parameter, set **Vdc input
method** to `Specify via
dialog` or `Input port - use 2D LUT
(scaled-w based)`.

### **DC bus voltage breakpoint vector, Vdc (V)** — DC bus voltage lookup vector (volts) `[18,30]` (default) | vector

DC bus voltage lookup vector used in
*id* and *iq* lookup tables (in volts).

#### Dependencies

To enable this parameter, set **Vdc input
method** to `Input port - use 3D LUT
(voltage slice based)`.

### **Motor parameter input method** — Type of motor parameters `Linear model with lumped parameters` (default) | `Non-linear model with D,Q-flux linkage LUTs` | `Non-linear model with Ld, Lq, and FluxPM LUTs` | `Non-linear model with id and iq LUTs`

Motor parameters that the block uses to generate the control reference
currents. Set the parameter to one of these values:

- `Linear model with lumped parameters`
  — Generate current reference tables using lumped circuit values
  for motor parameters *Ld*, *Lq*, and *FluxPM*.
- `Non-linear model with D,Q-flux linkage
  LUTs` — Generate current reference tables using
  *d*-axis and *q*-axis flux
  linkage lookup tables.
- `Non-linear model with Ld, Lq, and FluxPM
  LUTs` — Generate current reference tables using
  *Ld*,
  *Lq*, and
  *FluxPM* lookup tables.
- `Non-linear model with id and iq
  LUTs` — Determine the current reference using
  the *id* and
  *iq* lookup
  tables.

#### Dependencies

To enable this parameter:

- Set **Motor topology** to
  `Interior PMSM`.

or

- Set **Motor topology** to
  `Surface PMSM`.
- Set **Field-weakening control** method to
  `VCLMT`.

### **Enable percentages for torque breakpoint vector** — Enable percentage values for torque breakpoint vector `off` (default) | on

Select this parameter to specify the percentage torque breakpoint
vector values and the torque envelope values for the speed breakpoint
vector (in the following parameters):

- **Reference percentage torque breakpoint vector,
  Trefpct (%)**
- **Torque envelope for speed breakpoint vector, wrpm
  (rpm)**

### **Enable custom breakpoint vectors for torque and speed** — Use custom breakpoints for torque and speed `off` (default) | on

Select this parameter to use custom lookup vectors for motor torque and speed
quantities.

#### Dependencies

To enable this parameter, set **Motor parameter input
method** to either `Linear model with
lumped parameters`, `Non-linear model
with D,Q-flux linkage LUTs`, or
`Non-linear model with Ld, Lq, and FluxPM
LUTs`.

### **Reference percentage torque breakpoint vector, Trefpct (%)** — Torque reference lookup vector (in percentage) `[0,50,100]` (default) | vector

Torque reference lookup vector used in the
*id* and *iq* lookup tables (in percentage). The vector can have any number
of elements.

#### Dependencies

To enable this parameter, either:

- Set **Motor parameter input method**
  to either `Linear model with lumped
  parameters`, `Non-linear
  model with D,Q-flux linkage LUTs`, or
  `Non-linear model with Ld, Lq, and
  FluxPM LUTs`.
- Select the **Enable custom breakpoint vectors
  for torque and speed** parameter.
- Select the **Enable percentages for torque
  breakpoint vector** parameter.

or

- Set **Motor parameter input method** to
  `Non-linear model with id and iq
  LUTs`.
- Select the **Enable percentages for torque
  breakpoint vector** parameter.

### **Torque envelope for speed breakpoint vector, wrpm (rpm)** — Torque envelope values for speed breakpoint vector `[0.3 0.3 0.15 0.05]` (default) | vector

Torque envelope values used to compute the percentage values of the
torque reference lookup vector (specified in the **Reference
percentage torque breakpoint vector, Trefpct (%)**
parameter).

#### Dependencies

To enable this parameter, either:

- Set **Motor parameter input method**
  to either `Linear model with lumped
  parameters`, `Non-linear
  model with D,Q-flux linkage LUTs`, or
  `Non-linear model with Ld, Lq, and
  FluxPM LUTs`.
- Select the **Enable custom breakpoint vectors
  for torque and speed** parameter.
- Select the **Enable percentages for torque
  breakpoint vector** parameter.

or

- Set **Motor parameter input method** to
  `Non-linear model with id and iq
  LUTs`.
- Select the **Enable percentages for torque
  breakpoint vector** parameter.

### **Reference torque breakpoint vector, Tref (Nm)** — Torque reference lookup vector `[0,0.15,0.3]` (default) | vector

Torque reference lookup vector used in the
*id* and *iq* lookup tables (in Nm). The vector can have any number of
elements.

#### Dependencies

To enable this parameter, either:

- Set **Motor parameter input method**
  to either `Linear model with lumped
  parameters`, `Non-linear
  model with D,Q-flux linkage LUTs`, or
  `Non-linear model with Ld, Lq, and
  FluxPM LUTs`.
- Select the **Enable custom breakpoint vectors
  for torque and speed** parameter.

or

- Set **Motor parameter input method** to
  `Non-linear model with id and iq
  LUTs`.

### **Mechanical speed breakpoint vector, wrpm (rpm)** — Rotor speed lookup vector `[0,1000,2000,6000]` (default) | vector

Rotor speed lookup vector used in the
*id* and *iq* lookup tables (in rpm). The vector can have any number of
elements.

#### Dependencies

To enable this parameter, either:

- Set **Motor parameter input method**
  to either `Linear model with lumped
  parameters`, `Non-linear
  model with D,Q-flux linkage LUTs`, or
  `Non-linear model with Ld, Lq, and
  FluxPM LUTs`.
- Select the **Enable custom breakpoint vectors
  for torque and speed** parameter.

or

- Set **Motor parameter input method** to
  `Non-linear model with id and iq
  LUTs`.

### **Current Limit, I\_limit (A)** — Maximum phase current limit for motor (amperes) `7.1` (default) | scalar

Maximum phase current limit for the motor (in amperes).

### **Viscous damping coefficient, Bv (Nm-s/rad)** — Viscous damping coefficient `2.636875217824e-6` (default) | scalar

Viscous damping coefficient *Bv* of the motor in N·m/(rad/s).

### **D-axis current breakpoint vector, id (A)** — D-axis current lookup vector `[-40, -20, 0, 20]` (default) | vector

D-axis current vector (in amperes) in the
*Ld*, *Lq*, and *FluxPM* lookup tables.

#### Dependencies

To enable this parameter, set **Motor parameter input
method** parameter to either `Non-linear
model with D,Q-flux linkage LUTs` or
`Non-linear model with Ld, Lq, and FluxPM
LUTs`.

### **Q-axis current breakpoint vector, iq (A)** — Q-axis current lookup vector `[-40, -20, 0, 20, 40]` (default) | vector

Q-axis current vector (in amperes) in the
*Ld*, *Lq*, and *FluxPM* lookup tables.

#### Dependencies

To enable this parameter, set **Motor parameter input
method** parameter to either `Non-linear
model with D,Q-flux linkage LUTs` or
`Non-linear model with Ld, Lq, and FluxPM
LUTs`.

### **Use measured (instead of computed) torque** — Use measured value of torque `off` (default) | on

Enable this parameter to provide measured (instead of computed) torque
lookup data to the block.

#### Dependencies

To enable this parameter, set **Motor parameter input
method** to either `Non-linear model with
D,Q-flux linkage LUTs` or `Non-linear
model with Ld, Lq, and FluxPM LUTs`.

### **Measured torque LUT, T(id,iq) (Nm)** — Measured lookup data `[-3.4560,-1.7280,0, 1.7280, 3.4560;-2.4960,-1.2480,0, 1.2480, 2.4960;-1.5360,-0.7680,0, 0.7680, 1.5360;-0.5760,-0.2880,0, 0.2880, 0.5760]` (default) | vector

Measured torque lookup table data (in weber).

#### Dependencies

To enable this parameter:

- Set **Motor parameter input method** to
  either `Non-linear model with D,Q-flux linkage
  LUTs` or `Non-linear model with
  Ld, Lq, and FluxPM LUTs`.
- Select the **Use measured (instead of computed)
  torque** parameter.

### Linear Model with Lumped Parameters

### **Stator d-axis inductance, Ld (H)** — D-axis stator winding inductance `0.2e-3` (default) | scalar

Stator winding inductance (in henry) along the direct-axis of the rotating
*dq* reference frame.

#### Dependencies

To enable this parameter, set **Motor parameter input
method** to `Linear model with lumped
parameters`.

### **Stator q-axis inductance, Lq (H)** — Q-axis stator winding inductance `0.4e-3` (default) | scalar

Stator winding inductance (in henry) along the quadrature-axis of the rotating
*dq* reference frame.

#### Dependencies

To enable this parameter, set **Motor topology**
to `Interior PMSM` and **Motor
parameter input method** to `Linear model
with lumped parameters`.

### **Permanent magnet flux linkage (Wb)** — Permanent magnet flux linkage `6.4e-3` (default) | scalar

Peak permanent magnet flux linkage (in weber).

#### Dependencies

To enable this parameter, select the `Linear model
with lumped parameters` option in the
**Motor parameter input method**
parameter.

### Non-Linear Model with D,Q-Flux Linkage LUTs

### **D-axis flux linkage LUT, FluxD (id,iq) (Wb)** — Reference d-axis flux linkage lookup data `[-1.6,-1.6,-1.6,-1.6,-1.6;2.4,2.4,2.4,2.4,2.4;6.4,6.4,6.4,6.4,6.4;10.4,10.4,10.4,10.4,10.4]*1e-3` (default) | vector

D-axis flux linkage lookup table data (in weber).

#### Dependencies

To enable this parameter, set **Motor parameter input
method** to `Non-linear model with D,Q-flux
linkage LUTs`.

### **Q-axis flux linkage LUT, FluxQ (id,iq) (Wb)** — Reference q-axis flux linkage lookup data `2*[-8,-4,0,4,8;-8,-4,0,4,8;-8,-4,0,4,8;-8,-4,0,4,8]*1e-3` (default) | vector

Q-axis flux linkage lookup table data (in weber).

#### Dependencies

To enable this parameter, set **Motor parameter input
method** to `Non-linear model with D,Q-flux
linkage LUTs`.

### Non-Linear Model with *Ld* , *Lq*, and *FluxPM* LUTs

### **Ld LUT, Ld(id,iq) (H)** — D-axis inductance lookup data `0.2e-3 * ones(4, 5)` (default) | matrix

D-axis inductance lookup table data (in henry).

#### Dependencies

To enable this parameter, set **Motor parameter input method** to
`Non-linear model with Ld, Lq, and FluxPM
LUTs`.

### **Lq LUT, Lq(id,iq) (H)** — Q-axis inductance lookup data `0.4e-3 * ones(4, 5)` (default) | matrix

Q-axis inductance lookup table data (in henry).

#### Dependencies

To enable this parameter, set **Motor topology** to
`Interior PMSM` and **Motor
parameter input method** to `Non-linear
model with Ld, Lq, and FluxPM LUTs`.

### **PM flux linkage LUT, FluxPM(id,iq) (Wb)** — Permanent magnet flux linkage lookup data `6.4e-3 * ones(4, 5)` (default) | matrix

Permanent magnet flux linkage lookup table data (in weber).

#### Dependencies

To enable this parameter, set **Motor parameter input method** to
`Non-linear model with Ld, Lq, and FluxPM
LUTs`.

### Non-Linear Model with *id* and *iq* LUTs

### **Reference torque breakpoint vector, Tref (Nm)** — Torque reference lookup vector `[0 0.15 0.3]` (default) | vector

Torque reference lookup vector used in the *id* and *iq* lookup tables (in Nm).

#### Dependencies

To enable this parameter, set **Motor parameter input
method** to `Non-linear model with id and
iq LUTs`.

### **Mechanical speed breakpoint vector, wrpm (rpm)** — Rotor speed lookup vector `[0 1000 2000 6000]` (default) | vector

Rotor speed lookup vector used in the *id* and *iq* lookup tables (in rpm).

#### Dependencies

To enable this parameter, set **Motor parameter input
method** to `Non-linear model with id and
iq LUTs`.

### **Reference id LUT, id(Tref,wrpm) (A)** — Reference d-axis current lookup data `[0,0,0,-7.1;0,0,0,-7.1;0,0,0,-7.1]` (default) | matrix

D-axis current reference 2-D lookup table data (in amperes).

#### Dependencies

To enable this parameter, set **Motor parameter input
method** to `Non-linear model with id and
iq LUTs` and **Vdc input method**
to `Input port - use 2D LUT (scaled-w
based)`.

### **Reference id LUT, id(Tref,wrpm,Vdc) (A)** — Reference d-axis current lookup data `cat(3,[0,0,0,-7.1;-0.4579,-0.4579,-0.4579,-7.1;-1.4457,-1.4457,-1.4457,-7.1],[0,0,0,0;-0.4579,-0.4579,-0.4579,-1.2581;-1.4457,-1.4457,-1.4457,-4.5085])` (default) | matrix

D-axis current reference 3-D lookup table data (in amperes).

#### Dependencies

To enable this parameter, set **Motor parameter input
method** to `Non-linear model with id and
iq LUTs` and **Vdc input method**
to `Input port - use 3D LUT (voltage slice
based)`.

### **Reference iq LUT, iq(Tref,wrpm) (A)** — Reference q-axis current lookup data `[0,0,0,0;3.9091,3.9091,3.9091,0;7.1,7.1,7.1,0]` (default) | matrix

Q-axis current reference 2-D lookup table data (in amperes).

#### Dependencies

To enable this parameter, set **Motor parameter input
method** to `Non-linear model with id and
iq LUTs` and **Vdc input method**
to `Input port - use 2D LUT (scaled-w
based)`.

### **Reference iq LUT, iq(Tref,wrpm,Vdc) (A)** — Reference q-axis current lookup data `cat(3,[0,0,0,0;3.8539,3.8539,3.8539,0;6.9513,6.9513,6.9513,0],[0,0,0,0;3.8539,3.8539,3.8539,3.7611;6.9513,6.9513,6.9513,5.4848])` (default) | matrix

Q-axis current reference 3-D lookup table data (in amperes).

#### Dependencies

To enable this parameter, set **Motor parameter input
method** to `Non-linear model with id and
iq LUTs` and **Vdc input method**
to `Input port - use 3D LUT (voltage slice
based)`.

### Input Units

### **Input units** — Unit of measure of block input values `Per-Unit (PU)` (default) | `SI Units`

Unit of measure of the block input values.

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

### **Base torque (Nm)** — Nominal torque limit `0.74112` (default)

Torque (in Nm) corresponding to 1 per-unit. See Per-Unit System page
for more details.

You cannot configure this parameter. The block computes this value internally using the
other parameters.

#### Dependencies

To enable this parameter, set **Input units** to
`Per-Unit (PU)`.

### **Allow scaled-down motor parameters with CodeGen (higher precision with Fixed-Point data type)** — Scale down internal parameters to match per-unit scale `on` (default) | `off`

Option to scale down internal parameters to match the per-unit scale when generating
code.

- When you enable this option, the block scales down the
  internal constants and coefficients to match the per-unit scale.
  This allows for higher precision when you use the fixed-point
  data type. If you use this option with the single or double data
  type, some precision loss can occur depending on the number of
  bits allotted to the integer portion.
- When you disable this option, the block converts all the
  constants and coefficients it uses for internal calculations to
  SI units and then converts them back to the per-unit scale. This
  allows you to update the lookup table values in the generated
  code, typically, for applications such as controller tuning or
  end-of-line operations. You can also update the values manually
  for debugging or reusing previously generated code.

#### Dependencies

To enable this parameter, set **Motor parameter input
method** to `Non-linear model with id and
iq LUTs` and **Input units** to
`Per-Unit (PU)`.

### Plotting Options

The block enables this tab only when you:

- Set **Motor parameter input method** to either
  `Linear model with lumped parameters`,
  `Non-linear model with D,Q-flux linkage LUTs`,
  or `Non-linear model with Ld, Lq, and FluxPM
  LUTs`.
- Set **Vdc input method** to `Specify via
  dialog`.

### **Enable saving the computed LUTs** — Enable block to save computed LUTs `off` (default) | `on`

Enable the block to save the lookup table data that the block computes
when you click the **Compute (and plot) id and iq
LUTs** button.

For more details, see Plot Constraint Curves and Drive Characteristics for PMSM and SynRM Directly from Block Parameters Dialog Box.

### **Compute (and plot) id and iq LUTs** — Compute (and plot) *id* and *iq* lookup data button

When you click this button, the block computes (and plots) the lookup
table data for *id* and *iq*
currents.

For more details, see Plot Constraint Curves and Drive Characteristics for PMSM and SynRM Directly from Block Parameters Dialog Box.

### **Use default options for plotting** — Use default options to plot constraint curves `on` (default) | `off`

Enable the block to use default plotting options when you click the
**Plot constraint curves** button to plot the
constraint curves of motor.

For more details, see Plot Constraint Curves and Drive Characteristics for PMSM and SynRM Directly from Block Parameters Dialog Box.

### **Motor speed (RPM)** — Motor speed for plotting constraint curves `3000` (default) | scalar

Motor speed (in RPM) that the block should use when you click the
**Plot constraint curves** button to plot the
constraint curves of motor.

For more details, see Plot Constraint Curves and Drive Characteristics for PMSM and SynRM Directly from Block Parameters Dialog Box.

#### Dependencies

To enable this parameter, clear the **Use default options
for plotting** parameter.

### **Motor torque (Nm)** — Motor torque for plotting constraint curves `0.1` (default) | scalar

Motor torque (in Nm) that the block should use when you click the
**Plot constraint curves** button to plot the
constraint curves of motor.

For more details, see Plot Constraint Curves and Drive Characteristics for PMSM and SynRM Directly from Block Parameters Dialog Box.

#### Dependencies

To enable this parameter, clear the **Use default options
for plotting** parameter.

### **Enable plotting the drive characteristics** — Enable block to plot drive characteristics `off` (default) | `on`

Enable the block to plot the drive characteristics when you click the
**Plot constraint curves** button to plot the
constraint curves of motor.

For more details, see Plot Constraint Curves and Drive Characteristics for PMSM and SynRM Directly from Block Parameters Dialog Box.

#### Dependencies

To enable this parameter, clear the **Use default options
for plotting** parameter.

### **Include the drive characteristics for an increased motor current** — Enable block to plot drive characteristics for an increased motor current `off` (default) | `on`

Enable the block to include drive characteristics for an increased
motor current (in the plot generated upon clicking the **Plot
constraint curves** button).

**Note**

To successfully plot the characteristics for an increased motor
current, the current must be higher than the rated current of the
motor.

For more details, see Plot Constraint Curves and Drive Characteristics for PMSM and SynRM Directly from Block Parameters Dialog Box.

#### Dependencies

To enable this parameter, clear the **Use default options
for plotting** parameter and select the
**Enable plotting the drive characteristics**
parameter.

### **Plot constraint curves** — Plot constraint curves of motor button

When you click this button, the block plots the constraint curves of
the motor.

For more details, see Plot Constraint Curves and Drive Characteristics for PMSM and SynRM Directly from Block Parameters Dialog Box.

### **Compute and show** — Compute and show characteristic torque and speed button

When you click this button, the block computes and shows the following
torque and speed characteristics:

- Rated torque — Rated torque of motor (in Nm).
- Rated speed — Rated speed of motor (in RPM).
- Maximum speed — Maximum speed of motor (in RPM).

For more details, see Plot Constraint Curves and Drive Characteristics for PMSM and SynRM Directly from Block Parameters Dialog Box.

## Libraries

Motor Control Blockset / Controls / Control Reference

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2022b**

## Description

Generate lookup-table-based control reference currents for field-oriented control of permanent magnet synchronous motor

The LUT based PMSM Control Reference block generates the
*d*-axis and *q*-axis reference currents for
field-oriented control and field-weakening control of a permanent magnet synchronous
motor (PMSM). You can specify reference torque and feedback mechanical speed and the
block outputs the corresponding reference current values. The block also supports the
maximum torque per ampere (MTPA) and maximum torque per voltage (MTPV) operating
regions.

The block uses *id(T,ω)* and
*iq(T,ω)* lookup tables (LUTs) to
generate reference current values. Depending on the input method you use to specify the
motor parameters, the block can either generate LUTs or use the data you provide.

You can specify the motor parameters using one of these methods.

- `Linear model with lumped parameters` — Lumped
  parameters with *Ld*,
  *Lq*, and
  *FluxPM*

  This method uses the lumped parameters to compute the
  *id* and
  *iq* LUTs. The block obtains
  *id* and
  *iq* for the given
  *ω* and *T* inputs by solving the
  equations associated with these curves.

  Maximum torque per ampere (MTPA) curve (IPMSM),

  id2+idψm(Ld−Lq)=iq2.

  MTPA line (SPMSM), *id = 0*.

  Constant torque trajectory

  iq=T1.5Pp(ψm+(Ld−Lq)id).

  Current limit curve

  id2+iq2=imax2.

  Voltage limit curve

  (VDC3)2=(idRs−ωeLqiq)2+(iqRs+ωeLdid+ωeψm)2.

  - When the motor is operating within the voltage constraints, the block
    solves for the intersection of the MTPA line and the constant torque
    trajectory.
  - When the motor is operating beyond the voltage constraints, the block
    solves for the intersection of the voltage constraint curve and the
    constant torque trajectory.

  After computing the *id* and
  *iq* tables from a grid of
  *ω* and *T* values, the block uses
  interpolation to find
  *idref*
  and *iqref*
  for any *ω* and *T* inputs that lie within the
  range of the table values. The table values are clipped for *ω*
  and *T* values beyond the boundaries.
- `Non-linear model with Ld, Lq, and FluxPM LUTs` —
  Nonlinear model with *d*-axis and *q*-axis
  stator winding inductances and permanent magnet flux linkage lookup
  tables

  This method uses an approach similar to the lumped parameters method, except
  that the block updates the values for
  *Ld(id,iq)*,
  *Lq(id,iq)*,
  and
  *FluxPM(id,iq)*
  each time it computes *id* and
  *iq*. The block iterates these
  computations until the *id* and
  *iq* values converge.
- `Non-linear model with D,Q-flux linkage LUTs` —
  Nonlinear model with *d*-axis and *q*-axis
  flux linkage lookup tables

  This method uses an approach similar to the lumped parameters method, except
  that the block updates the values for
  *ψd(id,iq)*
  and
  *ψq(id,iq)*
  each time it computes *id* and *iq*. The block iterates these computations until the
  *id* and *iq* values converge.
- `Non-linear model with id and iq LUTs` — Use this
  method when you want to manually provide the
  *id(T,ω)* and
  *iq(T,ω)* tables. Typically, you
  obtain these tables through simulations or dyno tests.

You can also generate these tables using the `mcb.generateMotorLUT`
function in Motor Control Blockset™.

For a detailed set of equations and assumptions that Motor Control Blockset uses for a PMSM, see Mathematical Model of PMSM.

In addition, you can use the **Vdc input method** parameter to configure
the block to accept a fixed reference DC voltage through the **DC voltage to
compute LUTs (V)** parameter or a variable reference DC voltage through a
separate input port **Vdc**.

Based on the method you select in the **Motor parameter input method**
parameter, you can use the lumped parameters or a nonlinear model to compute the
reference currents as shown in this table.

| **Motor parameter input method** | **Vdc input method** | Technique used to compute reference currents |
| --- | --- | --- |
| `Linear model with lumped parameters` | `Specify via dialog` | The block uses the lumped parameters to compute the *id* and *iq* LUTs for a fixed voltage specified in the **DC bus voltage, Vdc (V)** parameter, using which it determines the reference currents. |
| `Input port - use 3D LUT (voltage slice based)` | The block uses the lumped parameters to compute the 3-D *id* and *iq* LUTs containing data for different voltages (or voltage slices specified in the **DC bus voltage breakpoint vector, Vdc (V)** parameter). It uses this data to determine the reference currents corresponding to the voltage specified at the input port **Vdc**. |
| `Input port - use 2D LUT (scaled-w based)` | The block uses the lumped parameters to compute the 2-D *id* and *iq* LUTs for a fixed voltage specified in the **DC bus voltage, Vdc (V)** parameter. It uses these LUTs to compute the reference currents (corresponding to the voltage provided at the input port **Vdc**) by scaling the speed (ω). |
| `Non-linear model with D,Q-flux linkage LUTs` | `Specify via dialog` | The block computes the reference currents by using the *d*-axis and *q*-axis flux linkage LUTs for a fixed voltage specified in the **DC bus voltage, Vdc (V)** parameter. |
| `Input port - use 3D LUT (voltage slice based)` | The block uses the 3-D *d*-axis and *q*-axis flux linkage LUTs containing data for different voltages (or voltage slices specified in the **DC bus voltage breakpoint vector, Vdc (V)** parameter). It uses these LUTs to compute the reference currents corresponding to the voltage provided at the input port **Vdc**. |
| `Input port - use 2D LUT (scaled-w based)` | The block uses the 2-D *d*-axis and *q*-axis flux linkage LUTs for a fixed voltage specified in the **DC bus voltage, Vdc (V)** parameter. It uses these LUTs to compute the reference currents (corresponding to the voltage provided at the input port **Vdc**) by scaling the speed (ω). |
| `Non-linear model with Ld, Lq, and FluxPM LUTs` | `Specify via dialog` | The block computes the reference currents by using the given *Ld*, *Lq*, and permanent magnet flux linkage LUTs for a fixed voltage specified in the **DC bus voltage, Vdc (V)** parameter. |
| `Input port - use 3D LUT (voltage slice based)` | The block uses the given 3-D *Ld*, *Lq*, and permanent magnet flux linkage LUTs containing data for different voltages (or voltage slices specified in the **DC bus voltage breakpoint vector, Vdc (V)** parameter). It uses these LUTs to compute the reference currents corresponding to the voltage provided at the input port **Vdc**. |
| `Input port - use 2D LUT (scaled-w based)` | The block uses the given 2-D *Ld*, *Lq*, and permanent magnet flux linkage LUTs for a fixed voltage specified in the **DC bus voltage, Vdc (V)** parameter. It uses these LUTs to compute the reference currents (corresponding to the voltage provided at the input port **Vdc**) by scaling the speed (ω). |
| `Non-linear model with id and iq LUTs` | `Specify via dialog` | The block determines the reference currents by using the given *id*, *iq* LUTs for a fixed voltage specified in the **DC bus voltage, Vdc (V)** parameter. |
| `Input port - use 3D LUT (voltage slice based)` | The block uses the given 3-D *id*, *iq* LUTs containing data for different voltages (or voltage slices specified in the **DC bus voltage breakpoint vector, Vdc (V)** parameter). It uses these LUTs to determine the reference currents corresponding to the voltage provided at the input port **Vdc**. |
| `Input port - use 2D LUT (scaled-w based)` | The block uses the given 2-D *id*, *iq* LUTs for a fixed voltage specified in the **DC bus voltage, Vdc (V)** parameter. It uses these LUTs to compute the reference currents (corresponding to the voltage provided at the input port **Vdc**) by scaling the speed (ω). |
