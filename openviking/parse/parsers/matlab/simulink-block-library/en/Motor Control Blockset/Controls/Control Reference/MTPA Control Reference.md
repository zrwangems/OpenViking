---
type: simulink-block
title: 'MTPA Control Reference'
family: 'mcb'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Controls / Control Reference'
documentation_page: 'mtpacontrolreference'
documentation_source_path: 'ref/mtpacontrolreference.html'
language: en
---

# MTPA Control Reference

## Ports

### Input

### **Tref** — Reference torque value scalar

Reference torque input value for which the block computes the reference current.
The unit of this port depends on the **Input units** parameter value.
If you set this parameter to `SI Units`, the port accepts
input signal in Nm.

**Data Types:** `single` | `double` | `fixed point`

### **⍵m** — Mechanical speed scalar

Reference mechanical speed value for which the block computes the reference
current. The unit of this port depends on the **Input units**
parameter value. If you set this parameter to `SI Units`, the
port accepts input signal in mechanical radians/sec.

**Data Types:** `single` | `double` | `fixed point`

### **Vdc** — DC bus voltage scalar

Variable DC bus voltage. The unit of this port depends on the **Input
units** parameter value. If you set this parameter to `SI
Units`, the port accepts input signal in volts.

#### Dependencies

To enable this port, set **Type of motor** to
`Interior PMSM` and **Vdc input method**
to `Input port`.

**Data Types:** `single` | `double` | `fixed point`
### Output

### **Idref** — Reference *d*-axis current scalar

Reference *d*-axis phase current that can efficiently generate
the input torque and speed values.

The unit of this port depends on the block input units defined by the
**Input units** parameter. If you set this parameter to
`SI Units`, the port outputs signal in amperes.

**Data Types:** `single` | `double` | `fixed point`

### **Iqref** — Reference *q*-axis current scalar

Reference *q*-axis phase current that can efficiently generate
the input torque and speed values.

The unit of this port depends on the block input units defined by the
**Input units** parameter. If you set this parameter to
`SI Units`, the port outputs signal in amperes.

**Data Types:** `single` | `double` | `fixed point`

## Parameters

### Motor Parameters

### **Type of motor** — Type of PMSM `Interior PMSM` (default) | `Surface PMSM`

Type of PMSM based on the location of the permanent magnets.

### **Number of pole pairs** — Number of available pole pairs `4` (default) | scalar

Number of pole pairs available in the motor.

### **Stator resistance per phase (Ohm)** — Resistance of stator phase winding (ohms) `0.36` (default) | scalar

Resistance of the stator phase winding (in ohms).

#### Dependencies

To enable this parameter, set **Type of motor** to
`Interior PMSM`.

### **Stator d-axis inductance (H)** — *d*-axis stator winding inductance `0.2e-3` (default) | scalar

Stator winding inductance (in henry) along the *d*-axis of the
rotating *dq* reference frame.

### **Stator q-axis inductance (H)** — *q*-axis stator winding inductance `0.4e-3` (default) | scalar

Stator winding inductance (in henry) along the *q*-axis of the
rotating *dq* reference frame.

#### Dependencies

To enable this parameter, set **Type of motor** to
`Interior PMSM`.

### **Permanent magnet flux linkage (Wb)** — Magnetic flux linkage of permanent magnets `6.4e-3` (default) | scalar

Magnetic flux linkage (in weber) between the stator windings and permanent magnets
on the rotor (weber).

### **Max current (A)** — Maximum phase current limit for motor (amperes) `7.1` (default) | scalar

Maximum phase current limit for the motor (in amperes).

### **Vdc input method** — Input method for Vdc `Specify via dialog` (default) | `Input port`

Use one of these methods to specify the *Vdc* input.

- `Specify via dialog` — Specify the fixed reference
  voltage *Vdc* using the parameter **DC voltage
  (V)**.
- `Input port` — Specify the variable reference voltage
  *Vdc* using the input port `Vdc`.

  **Note**

  If you select the `Input port` input method for
  *Vdc*, ensure that you configure the **Base voltage
  (V)** parameter in the **Input Units** tab.

#### Dependencies

To enable this parameter, set **Type of motor** to
`Interior PMSM`.

### **DC voltage (V)** — DC bus voltage (volts) `24` (default) | scalar

DC bus voltage (in volts).

#### Dependencies

To enable this parameter, set **Type of motor** to
`Interior PMSM` and **Vdc input method**
to `Specify via dialog`.

### Input Units

### **Input signal units** — Unit of block input values `Per-Unit (PU)` (default) | `SI Units`

Unit of the block input values.

### **Base speed (rpm)** — Base speed of motor (rpm) `4107` (default) | scalar

Speed of the motor (in rpm) at the rated voltage and rated current outside the
field-weakening region.

#### Dependencies

To enable this parameter, set **Input signal units** to
`Per-Unit (PU)`.

### **Base current (A)** — Base current for per-unit conversion (amperes) `19.3` (default) | scalar

Current (in amperes) corresponding to 1 per-unit. We recommend that you use the
maximum current detected by an analog to digital converter (ADC) as the base
current.

#### Dependencies

To enable this parameter, set **Input signal units** to
`Per-Unit (PU)`.

### **Base torque (Nm)** — Base torque for per-unit conversion (Nm) `0.74112` (default) | scalar

Torque (in Nm) corresponding to 1 per-unit. See Per-Unit System page for more
details.

You cannot specify this value. The block computes this value internally using
other parameters.

#### Dependencies

To display this parameter, set **Input signal units** to
`Per-Unit (PU)`.

### **Base voltage (V)** — Base voltage for per-unit conversion (volts) `24/sqrt(3)` (default) | scalar

Voltage (in volts) corresponding to 1 per-unit. See Per-Unit System page for more
details.

You cannot specify this value. The block computes this value internally using
other parameters.

#### Dependencies

To display this parameter, set **Input signal units** to
`Per-Unit (PU)`.

### Implementation

### **Prioritise execution time** — Scale down computations to reduce algorithm execution time `on` (default) | `off`

If you select this parameter, the block follows computational approximations to
prioritize and reduce the algorithm execution time. Clear this field to run the block
algorithms iteratively without using approximations.

## Libraries

Motor Control Blockset / Controls / Control Reference

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

### Fixed-Point Conversion Design and simulate fixed-point systems using Fixed-Point Designer™.

## Version History

**Introduced in R2020a**

## Description

Compute reference currents for maximum torque per ampere (MTPA) and field-weakening operation

The MTPA Control Reference block computes the *d*-axis and
*q*-axis reference current values for maximum torque per ampere (MTPA) and
field-weakening operations. The computed reference current values result in efficient output
for the permanent magnet synchronous motor (PMSM).

You can specify the reference torque and feedback mechanical speed and the block outputs
the corresponding *d*- and *q*-axes reference current values
for MTPA and field-weakening operations. For a given mechanical speed, in addition to the
highest possible torque values, the block also supports reference torque values that are less
than the rated torque of a PMSM.

The block computes the reference current values by solving mathematical
relationships.

In addition, you can use the **Vdc input method** parameter to configure
the block to accept a fixed reference DC voltage through the **DC voltage
(V)** parameter or a variable reference DC voltage through a separate input port
**Vdc**.

These equations describe the computation of reference *d*-axis and
*q*-axis current values by the block:

### Mathematical Model of PMSM

These model equations describe the dynamics of the PMSM in the rotor flux reference
frame:

vd=idRs+ dλddt − ωeLqiq

vq=iqRs+ dλqdt + ωeLdid+ ωeλpm

λd=Ldid+ λpm

λq=Lqiq

Te= 32p(λpmiq+(Ld− Lq)idiq)

Te− TL=Jdωmdt +Bωm

where:

- vd is the *d*-axis voltage (volts).
- vq is the *q*-axis voltage (volts).
- id is the *d*-axis current (amperes).
- iq is the *q*-axis current (amperes).
- Rs is the stator phase winding resistance (ohms).
- λpm is the permanent magnet flux linkage (weber).
- λd is the *d*-axis flux linkage (weber).
- λq is the *q*-axis flux linkage (weber).
- ωe is the electrical speed corresponding to frequency of stator voltages
  (radians/ sec).
- ωm is the rotor mechanical speed (radians/ sec).
- Ld is the *d*-axis winding inductance (henry).
- Lq is the *q*-axis winding inductance (henry).
- Te is the electromechanical torque produced by the PMSM (Nm).
- TL is the load torque (Nm).
- p is the number of motor pole pairs.
- J is the inertia coefficient (kg-m2).
- B is the friction coefficient (kg-m2/
  sec).

### Base Speed

Base speed is the maximum motor speed at the rated voltage and rated load, outside the
field-weakening region. These equations describe the computation of the motor base
speed.

The inverter voltage constraint is defined by computing the *d*-axis
and *q*-axis voltages:

vdo=− ωeLqiq

vqo=ωe(Ldid+ λpm)

vmax= vdc 3 −Rsimax ≥ vdo2+ vqo2

The current limit circle defines the current constraint which can be considered
as:

imax2= id 2+ iq2

In the preceding equation, id is zero for surface PMSMs. For interior PMSMs, the block considers values
of id and iq corresponding to MTPA.

Using these equations, we can compute the base speed as:

ωbase= 1p⋅ vmax(Lqiq)2+(Ldid+ λpm)2

where:

- ωe is the electrical speed corresponding to frequency of stator voltages
  (radians/ sec).
- ωbase is the mechanical base speed of the motor (radians/ sec).
- id is the *d*-axis current (amperes).
- iq is the *q*-axis current (amperes).
- vdo is the *d*-axis voltage when id is zero (volts).
- vqo is the *q*-axis voltage when iq is zero (volts).
- Ld is the *d*-axis winding inductance (henry).
- Lq is the *q*-axis winding inductance (henry).
- Rs is the stator phase winding resistance (ohms).
- λpm is the permanent magnet flux linkage (weber).
- vd is the *d*-axis voltage (volts).
- vq is the *q*-axis voltage (volts).
- vmax is the maximum fundamental line to neutral voltage (peak) supplied to
  the motor (volts).
- vdc is the dc voltage supplied to the inverter (volts).
- imax is the maximum phase current (peak) of the motor (amperes).
- p is the number of motor pole pairs.

### Surface PMSM

For a surface PMSM, you can achieve maximum torque by using zero
*d*-axis current when the motor is below the base speed. For the
field-weakening operation, the block calculates the reference *d*-axis
current using the constant-voltage-constant-power control (CVCP) algorithm defined by these
equations:

If ωm≤ ωbase:

- id\_mtpa= 0
- iq\_mtpa= Tref32⋅p⋅λpm
- id\_sat= id\_mtpa= 0
- iq\_sat=sat(iq\_mtpa,  imax)

If ωm> ωbase:

- id\_fw= (ωe\_base− ωe)λpmωeLd
- id\_sat=max(id\_fw,  −imax)
- iq\_fw= Tref32⋅p⋅λpm
- iq\_lim= imax2− id\_sat2
- iq\_sat=sat(iq\_fw,  iq\_lim)

The saturation function to compute iq\_sat is:

If iq\_fw< −iq\_lim,

iq\_sat= −iq\_lim

If iq\_fw>iq\_lim,

iq\_sat= iq\_lim

If  −iq\_lim≤iq\_fw≥iq\_lim,

iq\_sat= iq\_fw

The block outputs these values:

Idref=id\_sat

Iqref=iq\_sat

where:

- ωe is the electrical speed corresponding to frequency of stator voltages
  (radians/ sec).
- ωm is the rotor mechanical speed (radians/ sec).
- ωbase is the mechanical base speed of the motor (radians/ sec).
- ωe\_base is the electrical base speed of the motor (radians/ sec).
- id\_mtpa is the *d*-axis phase current corresponding to MTPA
  (amperes).
- iq\_mtpa is the *q*-axis phase current corresponding to MTPA
  (amperes).
- Tref is the reference torque (Nm).
- p is the number of motor pole pairs.
- λpm is the permanent magnet flux linkage (weber).
- id\_fw is the *d*-axis field weakening current
  (amperes).
- iq\_fw is the *q*-axis field weakening current
  (amperes).
- Ld is the *d*-axis winding inductance (henry).
- imax is the maximum phase current (peak) of the motor (amperes).
- id\_sat is the *d*-axis saturation current (amperes).
- iq\_sat is the *q*-axis saturation current (amperes).
- Idref is the *d*-axis current corresponding to the
  reference torque and reference speed (amperes).
- Iqref is the *q*-axis current corresponding to the
  reference torque and reference speed (amperes).

### Interior PMSM

For an interior PMSM, you can achieve maximum torque by computing the
*d*-axis and *q*-axis reference currents from the torque
equation. For the field-weakening operation, the block computes the reference
*d*-axis current using the voltage and current limited maximum torque
control (VCLMT) algorithm.

The reference currents for MTPA and field-weakening operations are defined by these
equations:

im\_ref= 2⋅Tref3⋅p⋅λpm

im=min(im\_ref,  imax)

id\_mtpa=λpm4(Lq−Ld)−λpm216(Lq−Ld)2+im22

iq\_mtpa=im2−(id\_mtpa)2

vdo=−ωeLqiq

vqo=ωe(Ldid+ λpm)

vdo2+vqo2=vmax2

(Lqiq)2+(Ldid+ λpm)2≤ vmax2ωe2

iq= imax2− id2

(Ld2− Lq2)id2+2λpmLdid+ λpm2+ Lq2imax2−vmax2ωe2=0

These two equations describe the computation of field-weakening currents for maximum
possible torque corresponding to a given speed value:

id\_fw= −λpmLd+ (λpmLd)2− (Ld2− Lq2)(λpm2+  Lq2imax2− vmax2ωe2  )(Ld2− Lq2)

iq\_fw= imax2− id\_fw2

These two equations describe the computation of field-weakening currents for a given
speed and torque value.

9p2(Ld−Lq)2Lq2ωe2iq\_fw4+(9p2λpm2Lq2ωe2−9p2(Ld−Lq)2vmax2)iq\_fw2−12TrefpλpmLdLqωe2iq\_fw+4(Tref)2Ld2ωe2=0

id\_fw=−λpmLd+1Ldvmax2ωe2−(Lqiq\_fw)2

To reduce the computation time, the block uses approximations to solve the preceding
polynomial.

If ωm≤ ωbase,

Idref= id\_mtpa

Iqref= iq\_mtpa

If ωm> ωbase,

Idref=max(id\_fw,−imax)

iq\_fw= imax2− id\_fw2

If iq\_fw<im,

Iqref=iq\_fw

If iq\_fw≥im,

Iqref=im

For negative reference torque values, the block updates the sign of im and Iqref and modifies the equations accordingly.

where:

- im\_ref is the estimated maximum current to produce the reference torque
  (amperes).
- im is the saturated value of estimated maximum current (amperes).
- id\_max is the maximum *d*-axis phase current (peak)
  (amperes).
- iq\_max is the maximum *q*-axis phase current (peak)
  (amperes).
- Tref is the reference torque (Nm).
- Idref is the *d*-axis current component corresponding to
  the reference torque and reference speed (amperes).
- Iqref is the *q*-axis current component corresponding to
  the reference torque and reference speed (amperes).
- p is the number of motor pole pairs.
- λpm is the permanent magnet flux linkage (weber).
- id\_mtpa is the *d*-axis phase current corresponding to MTPA
  (amperes).
- iq\_mtpa is the *q*-axis phase current corresponding to MTPA
  (amperes).
- Ld is the *d*-axis winding inductance (henry).
- Lq is the *q*-axis winding inductance (henry).
- imax is the maximum phase current (peak) of the motor (amperes).
- vmax is the maximum fundamental line to neutral voltage (peak) supplied to
  the motor (volts).
- vdo is the *d*-axis voltage when id is zero (volts).
- vqo is the *q*-axis voltage when iq is zero (volts).
- ωe is the electrical speed corresponding to frequency of stator voltages
  (radians/ sec).
- id is the *d*-axis current (amperes).
- iq is the *q*-axis current (amperes).
- id\_fw is the *d*-axis field weakening current
  (amperes).
- iq\_fw is the *q*-axis field weakening current
  (amperes).
- ωbase is the mechanical base speed of the motor (radians/ sec).
