---
type: simulink-block
title: 'SM Current Reference Generator'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Control / SM Control'
documentation_page: 'smcurrentreferencegenerator'
documentation_source_path: 'ref/smcurrentreferencegenerator.html'
language: en
---

# SM Current Reference Generator

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
- name: idqfRef
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

Desired mechanical torque produced by the synchronous machine.

**Data Types:** `single` | `double`

### **wMechanical** — Rotor mechanical speed, rad/s scalar

Mechanical angular velocity of the synchronous machine rotor, obtained
via direct measurement from the synchronous machine.

**Data Types:** `single` | `double`

### **Vdc** — DC-link voltage, V scalar

DC-link voltage of the converter. For the ZDAC method, this value is
used to limit the output reference torque and torque limit. For the
lookup table method, this value is used as an input to the lookup
tables.

**Data Types:** `single` | `double`
### Output

### **idqfRef** — Reference currents, A vector

Reference d-q and field currents to be given as inputs to a current
controller.

**Data Types:** `single` | `double`

### **TqRefSat** — Reference torque, N\*m scalar

Reference torque saturated by the calculated torque limit
**TqLim**.

**Data Types:** `single` | `double`

### **TqLim** — Torque limit, N\*m scalar

Torque limit imposed by both the electrical and mechanical constraints
of the system.

**Data Types:** `single` | `double`
## Parameters
```yaml
parameters:
- name: Nominal dc-link voltage (V)
  summary: Rated DC voltage 300V (default) | positive number
  group: ''
- name: Maximum power (W)
  summary: Maximum power 30000W (default) | positive number
  group: ''
- name: Maximum torque (N\*m)
  summary: Maximum torque 250N*m (default) | positive number
  group: ''
- name: Maximum field current (A)
  summary: Maximum field current 25A (default) | positive number
  group: ''
- name: Sample time (-1 for inherited)
  summary: Block sample time -1 (default) | -1 or positive number
  group: ''
- name: Current references
  summary: Current reference strategy Zero d-axis control (default) | Lookup-table based
  group: ''
- name: Torque constant (N\*m/A)
  summary: Torque constant 0.0375 (default) | positive number
  group: ''
- name: Mechanical speed vector, wMechanical (rpm)
  summary: Rotor speed lookup vector [0, 3000] (default) | positive monotonically increasing vector
  group: ''
- name: Torque reference vector, TqRef (N\*m)
  summary: Torque reference lookup vector [-100, 0, 100] (default) | positive monotonically increasing vector
  group: ''
- name: DC-link voltage vector, Vdc (V)
  summary: DC-link voltage lookup vector [300, 350] (default) | positive monotonically increasing vector
  group: ''
- name: D-axis current reference matrix, id(wMechanical,TqRef,Vdc), (A)
  summary: Reference d-axis current values zeros(2,3,2) (default) | real matrix
  group: ''
- name: Q-axis current reference matrix, iq(wMechanical,TqRef,Vdc), (A)
  summary: Reference q-axis current values zeros(2,3,2) (default) | real matrix
  group: ''
- name: Field current reference matrix, iq(wMechanical,TqRef,Vdc), (A)
  summary: Reference field current values zeros(2,3,2) (default) | real matrix
  group: ''
```

#### General Parameters

### **Nominal dc-link voltage (V)** — Rated DC voltage `300``V` (default) | positive number

Nominal DC-link voltage of the electrical source.

### **Maximum power (W)** — Maximum power `30000``W` (default) | positive number

Maximum synchronous machine power.

### **Maximum torque (N\*m)** — Maximum torque `250``N*m` (default) | positive number

Maximum synchronous machine torque.

### **Maximum field current (A)** — Maximum field current `25``A` (default) | positive number

Maximum field current of the synchronous machine.

### **Sample time (-1 for inherited)** — Block sample time `-1` (default) | -1 or positive number

Sample time for the block (-1 for inherited). If this block is used inside
a triggered subsystem, the sample time should be -1. If this block is used
in a continuous variable-step model, then the sample time can be explicitly
specified.

#### Reference Generation Strategy

### **Current references** — Current reference strategy `Zero d-axis control` (default) | `Lookup-table based`

Select the strategy for determining current references.

### **Torque constant (N\*m/A)** — Torque constant `0.0375` (default) | positive number

Torque constant of the synchronous machine.

### **Mechanical speed vector, wMechanical (rpm)** — Rotor speed lookup vector `[0, 3000]` (default) | positive monotonically increasing vector

Speed vector used in the lookup-tables for determining current
references.

### **Torque reference vector, TqRef (N\*m)** — Torque reference lookup vector `[-100, 0, 100]` (default) | positive monotonically increasing vector

Torque vector used in the lookup-tables for determining current
references.

### **DC-link voltage vector, Vdc (V)** — DC-link voltage lookup vector `[300, 350]` (default) | positive monotonically increasing vector

DC-link voltage vector used in the lookup-tables for determining current
references.

### **D-axis current reference matrix, id(wMechanical,TqRef,Vdc), (A)** — Reference d-axis current values `zeros(2,3,2)` (default) | real matrix

Direct-axis current reference lookup data.

### **Q-axis current reference matrix, iq(wMechanical,TqRef,Vdc), (A)** — Reference q-axis current values `zeros(2,3,2)` (default) | real matrix

Quadrature-axis current reference lookup data.

### **Field current reference matrix, iq(wMechanical,TqRef,Vdc), (A)** — Reference field current values `zeros(2,3,2)` (default) | real matrix

Field current reference lookup data.
## Libraries

Simscape / Electrical / Control / SM Control

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Synchronous machine current reference generator

The SM Current Reference Generator block implements a current reference
generator for synchronous machine (SM) current control in the rotor
*d*-*q* reference frame.

### Defining Equations

The SM Current Reference Generator block can obtain the current
reference using one of these methods:

- Zero *d*-axis control (ZDAC).
- Lookup tables.

For the ZDAC method, the block sets:

- The *d*-axis current reference idref to zero:

  idref=0,
- The field current reference ifref using the torque reference:

  ifref=|Trefif,max|Tmax,

  where
  *if,max* is the maximum
  field current and *Tmax* is the
  maximum torque.
- The *q*-axis current reference iqref using the torque equation:

  iqref= TrefKtifref,

  where *Tref*
  is the reference torque input and
  *Kt* is the torque constant
  of the synchronous machine expressed by the simplified torque equation T=Ktifiq.

For operation below the base speed of the synchronous machine, ZDAC is a suitable
method. Above base speed, a field weakening controller is required to adjust the
*d*-axis reference.

To pregenerate the current references for several operating points, define three
lookup tables using the lookup tables approach:

idref=f(nm,Tref,vdc),

iqref= g(nm,Tref,vdc),

and

ifref= h(nm,Tref,vdc).
