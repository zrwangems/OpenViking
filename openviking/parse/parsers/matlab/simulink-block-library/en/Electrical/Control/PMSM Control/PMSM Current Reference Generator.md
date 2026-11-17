---
type: simulink-block
title: 'PMSM Current Reference Generator'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / PMSM Control'
documentation_page: 'pmsmcurrentreferencegenerator'
documentation_source_path: 'ref/pmsmcurrentreferencegenerator.html'
language: en
---

# PMSM Current Reference Generator

## Ports
```yaml
ports:
- name: TqRef
  summary: Reference torque, N\*m scalar
  direction: input
  data_types: single | double
- name: wMechanical
  summary: Rotor mechanical speed, rad/s scalar
  direction: input
  data_types: single | double
- name: Vdc
  summary: DC-link voltage, V scalar
  direction: input
  data_types: single | double
- name: idqRef
  summary: Reference currents, A vector
  direction: output
  data_types: single | double
- name: TqRefSat
  summary: Reference torque, N\*m scalar
  direction: output
  data_types: single | double
- name: TqLim
  summary: Torque limit, N\*m scalar
  direction: output
  data_types: single | double
```

### Input

### **TqRef** — Reference torque, N\*m scalar

Desired mechanical torque produced by the PMSM, in N\*m.

**Data Types:** `single` | `double`

### **wMechanical** — Rotor mechanical speed, rad/s scalar

Mechanical angular velocity of the rotor, obtained via direct
measurement of the PMSM, in rad/s.

**Data Types:** `single` | `double`

### **Vdc** — DC-link voltage, V scalar

DC-link voltage of the converter, in V. For the ZDAC method, this
value is used to limit the output reference torque and torque limit. For
the lookup table method, this value is used as an input to the lookup
tables.

**Data Types:** `single` | `double`
### Output

### **idqRef** — Reference currents, A vector

Reference *d*- and *q*-currents
to be given as inputs to a PMSM current controller, in A.

**Data Types:** `single` | `double`

### **TqRefSat** — Reference torque, N\*m scalar

Reference torque saturated by the calculated torque limit
**TqLim**, in N\*m.

**Data Types:** `single` | `double`

### **TqLim** — Torque limit, N\*m scalar

Torque limit imposed by both the electrical and mechanical constraints
of the system, in N\*m.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Nominal dc-link voltage (V)
  summary: Rated DC voltage 300V (default) | positive number
  group: ''
- name: Maximum power (W)
  summary: Rated power 30000W (default) | positive number
  group: ''
- name: Maximum torque (N\*m)
  summary: Rated torque 250N*m (default) | positive number
  group: ''
- name: Sample time (-1 for inherited)
  summary: Block sample time -1 (default) | -1 or positive number
  group: ''
- name: Current references
  summary: Current reference strategy Zero d-axis control (default) | Lookup-table based | Automatically generated lookup-table
  group: ''
- name: Mechanical speed vector, wMechanical (rpm)
  summary: Rotor speed lookup vector [0, 3000]rpm (default) | positive monotonically increasing vector
  group: ''
- name: Torque reference vector, TqRef (N\*m)
  summary: Torque reference lookup vector [-100, 0, 100]N*m (default) | positive monotonically increasing vector
  group: ''
- name: DC-link voltage vector, Vdc (V)
  summary: DC-link voltage lookup vector [300, 350]V (default) | positive monotonically increasing vector
  group: ''
- name: D-axis current reference matrix, id(wMechanical,TqRef,Vdc) (A)
  summary: Reference d-axis current values zeros(2,3,2)A (default) | real matrix
  group: ''
- name: Q-axis current reference matrix, iq(wMechanical,TqRef,Vdc) (A)
  summary: Reference q-axis current values zeros(2,3,2)A (default) | real matrix
  group: ''
- name: PWM method
  summary: 'Pulse width modulation method SVM: space vector modulation (default) | SPWM: sinusoidal PWM'
  group: ''
- name: Modulation factor
  summary: Modulation factor 1 (default) | positive scalar
  group: ''
- name: Number of pole pairs
  summary: Pole pairs 8 (default) | positive integer
  group: ''
- name: Permanent magnet flux linkage (Wb)
  summary: PM Flux Linkage 0.04Wb (default) | positive scalar
  group: ''
- name: D-axis inductance (H)
  summary: Inductance of d-axis 0.00024 (default) | positive scalar
  group: ''
- name: Q-axis inductance (H)
  summary: Inductance of q-axis 0.00029 (default) | positive scalar
  group: ''
- name: Stator resistance (Ohm)
  summary: Resistance of stator 0.01 (default) | positive scalar
  group: ''
```

#### General Parameters

### **Nominal dc-link voltage (V)** — Rated DC voltage `300``V` (default) | positive number

Nominal DC-link voltage of the electrical source.

### **Maximum power (W)** — Rated power `30000``W` (default) | positive number

Maximum allowable PMSM power.

### **Maximum torque (N\*m)** — Rated torque `250``N*m` (default) | positive number

Maximum allowable PMSM torque.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | -1 or positive number

Sample time for the block (-1 for inherited). If you use this block inside
a triggered subsystem, set the sample time to -1. If you use this block in a
continuous variable-step model, you can specify the sample time
explicitly.

#### Reference Generation Strategy

### **Current references** — Current reference strategy `Zero d-axis control` (default) | `Lookup-table based` | `Automatically generated lookup-table`

Select the strategy for determining current references.

### **Mechanical speed vector, wMechanical (rpm)** — Rotor speed lookup vector `[0, 3000]``rpm` (default) | positive monotonically increasing vector

Speed vector used in the lookup tables for determining current
references.

### **Torque reference vector, TqRef (N\*m)** — Torque reference lookup vector `[-100, 0, 100]``N*m` (default) | positive monotonically increasing vector

Torque vector used in the lookup tables for determining current
references.

### **DC-link voltage vector, Vdc (V)** — DC-link voltage lookup vector `[300, 350]``V` (default) | positive monotonically increasing vector

DC-link voltage vector used in the lookup tables for determining current
references.

### **D-axis current reference matrix, id(wMechanical,TqRef,Vdc) (A)** — Reference d-axis current values `zeros(2,3,2)``A` (default) | real matrix

Direct-axis current reference lookup data.

### **Q-axis current reference matrix, iq(wMechanical,TqRef,Vdc) (A)** — Reference q-axis current values `zeros(2,3,2)``A` (default) | real matrix

Quadrature-axis current reference lookup data.

### **PWM method** — Pulse width modulation method `SVM: space vector modulation` (default) | `SPWM: sinusoidal PWM`

Specify the waveform technique.

#### Dependencies

This parameter is only visible when **Current
references** is set to `Automatically generated
lookup-table`.

### **Modulation factor** — Modulation factor `1` (default) | positive scalar

Safety factor used to compute the maximum allowed phase voltage for
current references generation.

#### Dependencies

This parameter is only visible when **Current
references** is set to `Automatically generated
lookup-table`.

### **Number of pole pairs** — Pole pairs `8` (default) | positive integer

Number of permanent magnet pole pairs on the rotor.

### **Permanent magnet flux linkage (Wb)** — PM Flux Linkage `0.04``Wb` (default) | positive scalar

Peak permanent magnet flux linkage.

### **D-axis inductance (H)** — Inductance of d-axis `0.00024` (default) | positive scalar

Direct-axis inductance.

### **Q-axis inductance (H)** — Inductance of q-axis `0.00029` (default) | positive scalar

Quadrature-axis inductance.

### **Stator resistance (Ohm)** — Resistance of stator `0.01` (default) | positive scalar

Stator resistance per phase.
## Libraries

Simscape / Electrical / Control / PMSM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Permanent magnet synchronous machine current reference generator

The PMSM Current Reference Generator block implements a current
reference generator for permanent magnet synchronous machine (PMSM) current control in
the rotor *d*-*q* reference frame.

You typically use this block in a series of blocks making up a control structure.

- You can generate a voltage reference in the d-q frame by placing this
  block before a PMSM
  Current Controller or PMSM
  Current Controller with Pre-Control block.
- You can implement velocity control by placing this block after a Velocity
  Controller block.

For an example of a full control structure, from machine measurements to machine
inputs, see the PMSM Field-Oriented
Control block.

### Equations

The PMSM Current Reference Generator block obtains the current
reference by using one of these methods:

- Zero *d*-axis control (ZDAC)
- User-defined lookup tables
- Automatically-generated lookup tables

For the ZDAC method, the block sets the *d*-axis current
reference idref to zero and determines the *q*-axis current
reference iqref using the torque equation:

idref=0,

and

iqref= 2Tref3pψm,

where:

- *Tref* is the reference torque
  input.
- *p* is the number of pole pairs.
- *ψm* is the permanent magnet
  flux linkage.

For operation below the base speed of the synchronous machine, ZDAC is a suitable
method. Above the base speed, the generator requires a field weakening controller to
adjust the *d*-axis reference.

To pregenerate the optimal current references for several operating points
offline, define two lookup tables using the user-defined lookup table approach:

idref=f(nm,Tref,vdc),

and

iqref= g(nm,Tref,vdc),

where:

- *nm* is the rotor angular
  velocity.
- *vdc* is the DC-link voltage
  of the converter.

To let the block create the lookup tables, choose the automatically-generated
lookup table approach. The block generates the lookup table using two strategies:

- Maximum torque per ampere
- Field weakening

The selection between the two strategies depends on the modulation
index. This equation calculates the modulation index,

M=VskVph\_max,

where *Vs* is the stator
voltage amplitude, *k* is the modulation factor, and
*Vph\_max* is the maximum allowable
phase voltage. If the modulation index is greater than 1, the block generates the
current references by using the field weakening procedure. Otherwise, the block
calculates the current references by using the maximum torque per ampere
procedure.

### Maximum Torque Per Ampere

You can generate current references in the constant torque region (occurring below
rated speed) by using the maximum torque per ampere (MTPA) strategy.

These equations defines the direct and quadrature components of the stator current
in terms of angle and magnitude,

id=−Issinβ

iq= Iscosβ

where:

- *β* is the angle of the stator current vector.
- *Is* is the stator current amplitude.

Using the angle-magnitude variant of the d-q currents, this equation calculates
the PMSM torque equation,

Te=3p2ψmIscosβ+3p4(Lq−Ld)Is2sin2β,

where *Ld* and
*Lq* are the direct and quadrature
inductances, respectively.

To obtain fast transient response and maximize torque with the smallest possible
stator current amplitude, MTPA imposes
(*dTe*)/*dβ* = 0 to the
torque equation, which yields

−3p2ψmIssinβ+3p2(Lq−Ld)Is2(cos2β−sin2β)=0.

The MTPA *d*-axis current
*id\_mtpa* is written in terms of the
*q*-axis component
*iq\_mtpa* by substituting the d-q
currents back from their angle and magnitude variants:

id\_mtpa=ψm2(Lq−Ld)−ψm24(Lq−Ld)2+iq\_mtpa2.

Finally, by plugging the previous equation into the d-q variant
of the PMSM torque equation, the block obtains this polynomial:

9p2(Lq−Ld)2iq\_mtpa4+6Trefpψmiq\_mtpa−4Tref2=0.

The *q*-axis component is the solution of this
polynomial.

### Field Weakening

You can generate current references in the above rated speed region by using the
field weakening (FW) strategy.

Above the rated speed, the stator voltage is limited by the power converter and
the available DC-link voltage. The maximum stator voltage is

Vs=vd2+vq2≤Vph\_max,

where *Vph\_max* is the
maximum available stator phase voltage.

The steady-state voltage equations for PMSMs are

vd=Rsid−ωeLqiq ,

and

vq=Rsiq+ωe(Ldid+ψm),

where *ωe* is the rotor
electrical angular velocity, in rad/s.

For rotor speeds above rated, the stator resistance is negligible, and the field
weakening *d*-axis current component
*id\_fw* is obtained in terms of the
*q*-axis component *iq\_fw*from the *vq* steady-state equation:

id\_fw=−ψmLd+1LdVph\_max2ωe2−(Lqiq\_fw)2,

Finally, by plugging the *id\_fw* equation
into the PMSM torque equation, the block obtains this polynomial:

9p2(Ld−Lq)2Lq2ωe2iq\_fw4+(9p2ψm2Lq2ωe2−9p2(Ld−Lq)2Vph\_max2)iq\_fw2−12TrefpψmLdLqωe2iqfw+4Tref2Ld2ωe2=0

The *q*-axis component is the solution of this
polynomial.

### Assumptions

The machine parameters are constants.

### Limitations

The automatically generated current references introduce latency in the
presimulation phase. For medium-power PMSM drives the latency is around 300
ms.
