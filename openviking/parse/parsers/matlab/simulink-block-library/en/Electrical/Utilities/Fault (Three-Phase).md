---
type: simulink-block
title: 'Fault (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'faultthreephase'
documentation_source_path: 'ref/faultthreephase.html'
language: en
---

# Fault (Three-Phase)

## Ports

### Conserving

### **~** — Three-phase port electrical

Expandable electrical conserving three-phase
port for connecting the fault to the system.
### Input

### **F** — Externally triggered fault control input physical

Physical signal scalar control input port for enabling an externally
triggered fault.

#### Dependencies

To enable this port, on the **External Trigger**
settings, set the **Enable external fault trigger**
parameter to `Yes`.
### Output

### **X** — Fault state physical

Physical signal scalar output port for reporting the fault state:

- 1 — Faulted
- 0 — Unfaulted

#### Dependencies

To enable this port, on the **Main** settings,
set the **State port** parameter to
`Visible`.

## Parameters

### **Modeling option** — Whether to model composite or expanded three-phase ports `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to model composite or expanded three-phase ports.

Composite three-phase ports represent three individual electrical conserving ports
with a single block port. You can use composite three-phase ports to build models that
correspond to single-line diagrams of three-phase electrical systems.

Expanded three-phase ports represent the individual phases of a three-phase system
using three separate electrical conserving ports.

### Main

### **Failure mode** — Type of fault `None` (default) | `Single-phase to ground (a-g)` | `Single-phase to ground (b-g)` | `Single-phase to ground (c-g)` | `Two-phase (a-b)` | `Two-phase (b-c)` | `Two-phase (c-a)` | `Two-phase to ground (a-b-g)` | `Two-phase to ground (b-c-g)` | `Two-phase to ground (c-a-g)` | `Three-phase (a-b-c)` | `Three-phase to ground (a-b-c-g)`

Type of fault to model. The visibility of related parameters depends
on the fault model. Options are:

- `None` — Specifies that the
  fault is not active.
- `Single-phase to ground (a-g)`
- `Single-phase to ground (b-g)`
- `Single-phase to ground (c-g)`
- `Two-phase (a-b)`
- `Two-phase (b-c)`
- `Two-phase (c-a)`
- `Two-phase to ground (a-b-g)`
- `Two-phase to ground (b-c-g)`
- `Two-phase to ground (c-a-g)`
- `Three-phase (a-b-c)`
- `Three-phase to ground
  (a-b-c-g)`

### **Faulted phase-neutral resistance** — Faulted phase-neutral resistance `1e-3` `Ohm` (default)

Resistance between the phase connection and the neutral point when the
fault is active.

#### Dependencies

To enable this parameter set the **Failure mode**
parameter to:

- `Single-phase to ground
  (a-g)`
- `Single-phase to ground
  (b-g)`
- `Single-phase to ground
  (c-g)`
- `Two-phase (a-b)`
- `Two-phase (b-c)`
- `Two-phase (c-a)`
- `Two-phase to ground
  (a-b-g)`
- `Two-phase to ground
  (b-c-g)`
- `Two-phase to ground
  (c-a-g)`
- `Three-phase (a-b-c)`
- `Three-phase to ground
  (a-b-c-g)`

### **Faulted neutral-ground resistance** — Faulted neutral-ground resistance `1e-3` `Ohm` (default)

Resistance between the neutral point and the electrical reference when
fault is active.

#### Dependencies

To enable this parameter set the **Failure mode**
parameter to:

- `Single-phase to ground
  (a-g)`
- `Single-phase to ground
  (b-g)`
- `Single-phase to ground
  (c-g)`
- `Two-phase to ground
  (a-b-g)`
- `Two-phase to ground
  (b-c-g)`
- `Two-phase to ground
  (c-a-g)`
- `Three-phase to ground
  (a-b-c-g)`

### **State port** — State port visibility `Hidden` (default) | `Visible`

Option to hide or expose port **x**, a physical
signal output port that reports the fault state:

- `Hidden` — Port
  **x** is not visible if you select this
  option.
- `Visible` — Port
  **x** is visible only if you select this
  option.

### External Trigger

### **Enable external fault trigger** — External fault model `No` (default) | `Yes`

External fault model. Choose between

- `No` — Do not model an
  external fault. Physical signal input port
  **F** is not visible if you select this
  option.
- `Yes` — Model an external
  fault. Related parameters and physical signal input port
  **F** are visible only if you select
  this option.

### **Fault threshold** — Threshold value that triggers the fault `0.5` (default)

The threshold value that triggers the fault when the external signal
crosses it in the direction, specified by the fault condition. This
parameter is visible only if the **Enable external fault
trigger** parameter is set to `Yes`. The
default value is `0.5`.

#### Dependencies

To enable this parameter, set the **Enable external fault
trigger** parameter to `Yes`.

### **External fault trigger** — Fault condition `Faulted if F >= Fault threshold` (default) | `Faulted if F <= Fault threshold`

Choose the fault condition:

- `Faulted if F >= Fault threshold`
  — The fault occurs when the external signal value becomes
  greater than, or equal to, the **Fault
  threshold** parameter value.
- `Faulted if F <= Fault threshold`
  — The fault occurs when the external signal value becomes
  less than, or equal to, the **Fault threshold**
  parameter value.

#### Dependencies

To enable this parameter, set the **Enable external fault
trigger** parameter to `Yes`.

### **Fault resets when fault trigger reverts** — Fault resets when fault trigger reverts `No` (default) | `Yes`

Select `Yes` to have the fault reset when the trigger
signal reverts. The default value is `No`.

#### Dependencies

To enable this parameter, set the **Enable external fault
trigger** parameter to `Yes`.

### Temporal Trigger

### **Enable temporal fault trigger** — Temporal fault model `No` (default) | `Yes`

Temporal fault model. Choose between

- `No` — Do not model a
  temporal fault.
- `Yes` — Model a temporal
  fault. Related parameters are visible only if you select
  this option.

### **Fault start time** — Fault start time `1` `s` (default)

Simulation time that the block enters the fault state.

#### Dependencies

To enable this parameter, set the **Enable temporal fault
trigger** parameter to `Yes`.

### **Fault duration** — Fault duration `0.1` `s` (default)

Simulation duration time for the fault. The block exits the fault
state when the duration time is over.

#### Dependencies

To enable this parameter, set the **Enable temporal fault
trigger** parameter to `Yes`.

### Parasitics

### **Unfaulted phase-neutral conductance** — Unfaulted phase-neutral conductance `1e-6` `1/Ohm` (default)

Conductance between the phase connections and the neutral point when a
phase is not involved in the fault.

## Libraries

Simscape / Electrical / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2019b**

## Description

Signal-enabled or time-based, single-phase, two-phase, or three-phase, grounded or ungrounded fault

The Fault (Three-Phase) models any permutation of a
single-phase, two-phase, or three-phase grounded or ungrounded fault. The block can
impose both time- and event-based faults. The block can impose one or both type of
faults, consecutively, at the same time, or for an overlapping time period.

For a time-based or temporal fault, specify the fault activation time using the block
**Fault start time** parameter. The fault becomes inactive when the
fault duration that you specify elapses.

For an event-based fault, specify the fault activation threshold using the block
**Threshold** parameter. An external control signal
*F* enables the fault. The fault is active when
*F* is greater than the threshold. The fault is inactive when
*F* is less than or equal to the threshold.

The block can represent these permutations:

- Single-phase-to-ground fault (*a*-*g*,
  *b*-*g*, or
  *c*-*g*)
- Two-phase fault (*a*-*b*,
  *b*-*c*, or
  *c*-*a*)
- Two-phase-to-ground fault
  (*a*-*b*-*g*,
  *b*-*c*-*g*, or
  *c*-*a*-*g*)
- Three-phase fault
  (*a*-*b*-*c*)
- Three-phase-to-ground fault
  (*a*-*b*-*c*-*g*)

The figure shows the equivalent circuit diagram for the block.

To determine the resistance in the equivalent circuit, apply the relevant equations
from the table.

| Failure mode | | Value of  *R a* | Value of  *R b* | Value of  *R c* | Value of  *R g* |
| --- | --- | --- | --- | --- | --- |
| None / inactive | | 1Gpn | 1Gpn | 1Gpn | Infinity / open circuit |
| Single phase to ground | *a*-*g* | Rpn | 1Gpn | 1Gpn | Rng |
| *b*-*g* | 1Gpn | Rpn | 1Gpn | Rng |
| *c*-*g* | 1Gpn | 1Gpn | Rpn | Rng |
| Two phase | *a*-*b* | Rpn | Rpn | 1Gpn | Infinity / open circuit |
| *b*-*c* | 1Gpn | Rpn | Rpn | Infinity / open circuit |
| *c*-*a* | Rpn | 1Gpn | Rpn | Infinity / open circuit |
| Two phase to ground | *a*-*b*-*g* | Rpn | Rpn | 1Gpn | Rng |
| *b*-*c*-*g* | 1Gpn | Rpn | Rpn | Rng |
| *c*-*a*-*g* | Rpn | 1Gpn | Rpn | Rng |
| Three phase | *a*-*b*-*c* | Rpn | Rpn | Rpn | Infinity / open circuit |
| Three phase to ground | *a*-*b*-*c*-*g* | Rpn | Rpn | Rpn | Rng |

where:

- *Ra* is the resistance between the
  *a*-phase and the neutral point of a wye
  connection.
- *Rb* is the resistance between the
  *b*-phase and the neutral point of a wye
  connection.
- *Rc* is the resistance between the
  *c*-phase and the neutral point of a wye
  connection.
- *Rg* is the resistance between the
  neutral point of a wye connection and electrical reference.
- *Rpn* is the value of the
  **Faulted phase-neutral resistance** parameter.
- *Rng* is the value of the
  **Faulted neutral-ground resistance** parameter.
- *Gpn* is the value of the
  **Unfaulted phase-neutral conductance**
  parameter.
