---
type: simulink-block
title: 'Coupled Lines (Three-Phase)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / Lines'
documentation_page: 'coupledlinesthreephase'
documentation_source_path: 'ref/coupledlinesthreephase.html'
language: en
---

# Coupled Lines (Three-Phase)

## Ports
```yaml
ports:
- name: ~1
  summary: Lines positive terminals electrical
  direction: conserving
- name: ~2
  summary: Lines negative terminals electrical
  direction: conserving
- name: a1
  summary: Line *a* positive terminal electrical
  direction: conserving
- name: a2
  summary: Line *a* negative terminal electrical
  direction: conserving
- name: b1
  summary: Line *b* positive terminal electrical
  direction: conserving
- name: b2
  summary: Line *b* negative terminal electrical
  direction: conserving
- name: c1
  summary: Line *c* positive terminal electrical
  direction: conserving
- name: c2
  summary: Line *c* negative terminal electrical
  direction: conserving
```

### Conserving

### **~1** — Lines positive terminals electrical

Expandable three-phase
electrical conserving port associated with the positive
terminals of lines *a*, *b*, and
*c*.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports`

### **~2** — Lines negative terminals electrical

Expandable three-phase
electrical conserving port associated with the negative
terminals of lines *a*, *b*, and
*c*.

#### Dependencies

To enable this port, set **Electrical
connection** to `Composite three-phase
ports`

### **a1** — Line *a* positive terminal electrical

Electrical conserving port associated with the positive terminal of
line *a*.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`

### **a2** — Line *a* negative terminal electrical

Electrical conserving port associated with the negative terminal of
line *a*.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`

### **b1** — Line *b* positive terminal electrical

Electrical conserving port associated with the positive terminal of
line *b*.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`

### **b2** — Line *b* negative terminal electrical

Electrical conserving port associated with the negative terminal of
line *b*.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`

### **c1** — Line *c* positive terminal electrical

Electrical conserving port associated with the positive terminal of
line *c*.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`

### **c2** — Line *c* negative terminal electrical

Electrical conserving port associated with the negative terminal of
line *c*.

#### Dependencies

To enable this port, set **Electrical
connection** to `Expanded three-phase
ports`
## Parameters
```yaml
parameters:
- name: Electrical connection
  summary: Whether to model composite or expanded three-phase ports Composite three-phase ports (default) | Expanded three-phase
    ports
  group: Main
- name: Parameterization
  summary: Line impedance parameterization Balanced impedance (default) | General impedance
  group: Main
- name: Line a inductance
  summary: Line *a* self-inductance 1e-3 H (default) | positive scalar
  group: Main
- name: Line b inductance
  summary: Line *b* self-inductance 1e-3 H (default) | positive scalar
  group: Main
- name: Line c inductance
  summary: Line *c* self-inductance 1e-3 H (default) | positive scalar
  group: Main
- name: Line inductance
  summary: Self-inductance 1e-3 H (default) | positive scalar
  group: Main
- name: Line a-b mutual inductance
  summary: Mutual inductance between *a*-*b* 3e-4 H (default) | positive scalar
  group: Main
- name: Line b-c mutual inductance
  summary: Mutual inductance between *b*-*c* 3e-4 H (default) | positive scalar
  group: Main
- name: Line a-c mutual inductance
  summary: Mutual inductance between *a*-*c* 3e-4 H (default) | positive scalar
  group: Main
- name: Mutual inductance
  summary: Mutual inductance 3e-4 H (default) | positive scalar
  group: Main
- name: Line a resistance
  summary: Line *a* series resistance 0.001 Ohm (default) | nonnegative scalar
  group: Resistance
- name: Line b resistance
  summary: Line *b* series resistance 0.001 Ohm (default) | nonnegative scalar
  group: Resistance
- name: Line c resistance
  summary: Line *c* series resistance 0.001 Ohm (default) | nonnegative scalar
  group: Resistance
- name: Line a-b mutual resistance
  summary: Mutual resistance between *a*-*b* 0 Ohm (default) | nonnegative scalar
  group: Resistance
- name: Line a-c mutual resistance
  summary: Mutual resistance between *a*-*c* 0 Ohm (default) | nonnegative scalar
  group: Resistance
- name: Line b-c mutual resistance
  summary: Mutual resistance between *b*-*c* 0 Ohm (default) | nonnegative scalar
  group: Resistance
- name: Line resistance
  summary: Series resistance 0.001 Ohm (default) | nonnegative scalar
  group: Resistance
- name: Mutual resistance
  summary: Mutual resistance 0 Ohm (default) | nonnegative scalar
  group: Resistance
- name: Line a leakage conductance
  summary: Line *a* parallel leakage conductance 1e-9 1/Ohm (default) | nonnegative scalar
  group: Resistance
- name: Line b leakage conductance
  summary: Line *b* parallel leakage conductance 1e-9 1/Ohm (default) | nonnegative scalar
  group: Resistance
- name: Line c leakage conductance
  summary: Line *c* parallel leakage conductance 1e-9 1/Ohm (default) | nonnegative scalar
  group: Resistance
- name: Line leakage conductance
  summary: Parallel leakage conductance 1e-9 1/Ohm (default) | nonnegative scalar
  group: Resistance
- name: Port 1 connection fault
  summary: Option to add fault to port 1 Add fault
  group: Faults
- name: Fault type
  summary: Type of fault Single-phase to ground (a-g) (default) | Single-phase to ground (b-g) | Single-phase to ground (c-g)
    | Two-phase (a-b) | Two-phase (b-c) | Two-phase (c-a) | Two-phase to ground (a-b-g) | Two-phase to ground (b-c-g) | Two-phase
    to ground (c-a-g) | Three-phase (a-b-c) | Three-phase to ground (a-b-c-g)
  group: Faults
- name: Faulted phase-neutral resistance
  summary: Faulted resistance between phase connection and neutral point 1e-3 Ohm (default) | positive scalar
  group: Faults
- name: Faulted neutral-ground resistance
  summary: Faulted resistance between neutral point and electrical reference 1e-3 Ohm (default) | positive scalar
  group: Faults
- name: Unfaulted phase-neutral conductance
  summary: Unfaulted conductance between phase connection and neutral point 1e-6 1/Ohm (default) | positive scalar
  group: Faults
- name: Trigger type
  summary: Trigger type Always on (default) | Timed | Additional triggers | Conditional | Manual
  group: Faults
- name: Trigger fault at time
  summary: Time before entering faulted state 0 s (default) | nonnegative scalar
  group: Faults
- name: Trigger configuration
  summary: Option to enable additional trigger types Open fault properties
  group: Faults
- name: Port 2 connection fault
  summary: Option to add fault to port 2 Add fault
  group: Faults
- name: Fault type
  summary: Type of fault Single-phase to ground (a-g) (default) | Single-phase to ground (b-g) | Single-phase to ground (c-g)
    | Two-phase (a-b) | Two-phase (b-c) | Two-phase (c-a) | Two-phase to ground (a-b-g) | Two-phase to ground (b-c-g) | Two-phase
    to ground (c-a-g) | Three-phase (a-b-c) | Three-phase to ground (a-b-c-g)
  group: Faults
- name: Faulted phase-neutral resistance
  summary: Faulted resistance between phase connection and neutral point 1e-3 Ohm (default) | positive scalar
  group: Faults
- name: Faulted neutral-ground resistance
  summary: Faulted resistance between neutral point and electrical reference 1e-3 Ohm (default) | positive scalar
  group: Faults
- name: Unfaulted phase-neutral conductance
  summary: Unfaulted conductance between phase connection and neutral point 1e-6 1/Ohm (default) | positive scalar
  group: Faults
- name: Trigger type
  summary: Trigger type Always on (default) | Timed | Additional triggers | Conditional | Manual
  group: Faults
- name: Trigger fault at time
  summary: Time before entering faulted state 0 s (default) | nonnegative scalar
  group: Faults
- name: Trigger configuration
  summary: Option to enable additional trigger types Open fault properties
  group: Faults
```

### Main

### **Electrical connection** — Whether to model composite or expanded three-phase ports `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to model composite or expanded three-phase ports.

Composite three-phase ports represent three individual electrical
conserving ports with a single block port. You can use composite
three-phase ports to build models that correspond to single-line
diagrams of three-phase electrical systems.

Expanded three-phase ports represent the individual phases of a
three-phase system using three separate electrical conserving
ports.

### **Parameterization** — Line impedance parameterization `Balanced impedance` (default) | `General impedance`

Specify how to parameterize the impedance of the three lines:

- `Balanced impedance` — Specify
  the same series resistance, series inductance, and parallel
  leakage conductance for all lines.
- `General impedance` — Specify the
  series resistance, series inductance, and parallel leakage
  conductance separately for each line.

### **Line a inductance** — Line *a* self-inductance `1e-3` `H` (default) | positive scalar

Self-inductance of line *a*.

#### Dependencies

To enable this parameter, set
**Parameterization** to `General
impedance`.

### **Line b inductance** — Line *b* self-inductance `1e-3` `H` (default) | positive scalar

Self-inductance of line *b*.

#### Dependencies

To enable this parameter, set
**Parameterization** to `General
impedance`.

### **Line c inductance** — Line *c* self-inductance `1e-3` `H` (default) | positive scalar

Self-inductance of line *c*.

#### Dependencies

To enable this parameter, set
**Parameterization** to `General
impedance`.

### **Line inductance** — Self-inductance `1e-3` `H` (default) | positive scalar

Self-inductance of lines *a*, *b*,
and *c*.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Balanced
impedance`.

### **Line a-b mutual inductance** — Mutual inductance between *a*-*b* `3e-4` `H` (default) | positive scalar

Mutual inductance between lines *a* and
*b*. If you know the coupling factor, set this
value to kLaLb. To have a physically realizable mutual inductance,
this value must satisfy:

−LaLb<Lm,ab<LaLb.

#### Dependencies

To enable this parameter, set
**Parameterization** to `General
impedance`.

### **Line b-c mutual inductance** — Mutual inductance between *b*-*c* `3e-4` `H` (default) | positive scalar

Mutual inductance between lines *b* and
*c*. If you know the coupling factor, set this
value to kLbLc. To have a physically realizable mutual inductance,
this value must satisfy:

−LbLc<Lm,bc<LbLc.

#### Dependencies

To enable this parameter, set
**Parameterization** to `General
impedance`.

### **Line a-c mutual inductance** — Mutual inductance between *a*-*c* `3e-4` `H` (default) | positive scalar

Mutual inductance between lines *a* and
*c*. If you know the coupling factor, set this
value to kLaLc. To have a physically realizable mutual inductance,
this value must satisfy:

−LaLc<Lm,ac<LaLc.

#### Dependencies

To enable this parameter, set
**Parameterization** to `General
impedance`.

### **Mutual inductance** — Mutual inductance `3e-4` `H` (default) | positive scalar

Mutual inductance between each pair of lines. If you know the coupling
factor, set this value to *kL*, where
*L* is the series inductance of each of the lines.
To have a physically realizable mutual inductance, this value must satisfy:

−L<Lm<L.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Balanced
impedance`.

### Resistance

### **Line a resistance** — Line *a* series resistance `0.001` `Ohm` (default) | nonnegative scalar

Series resistance of line *a*.

#### Dependencies

To enable this parameter, set
**Parameterization** to `General
impedance`.

### **Line b resistance** — Line *b* series resistance `0.001` `Ohm` (default) | nonnegative scalar

Series resistance of line *b*.

#### Dependencies

To enable this parameter, set
**Parameterization** to `General
impedance`.

### **Line c resistance** — Line *c* series resistance `0.001` `Ohm` (default) | nonnegative scalar

Series resistance of line *c*.

#### Dependencies

To enable this parameter, set
**Parameterization** to `General
impedance`.

### **Line a-b mutual resistance** — Mutual resistance between *a*-*b* `0` `Ohm` (default) | nonnegative scalar

*Since R2025a*

Mutual resistance between lines *a* and
*b*.

#### Dependencies

To enable this parameter, set
**Parameterization** to `General
impedance`.

### **Line a-c mutual resistance** — Mutual resistance between *a*-*c* `0` `Ohm` (default) | nonnegative scalar

*Since R2025a*

Mutual resistance between lines *a* and
*c*.

#### Dependencies

To enable this parameter, set
**Parameterization** to `General
impedance`.

### **Line b-c mutual resistance** — Mutual resistance between *b*-*c* `0` `Ohm` (default) | nonnegative scalar

*Since R2025a*

Mutual resistance between lines *b* and
*c*.

#### Dependencies

To enable this parameter, set
**Parameterization** to `General
impedance`.

### **Line resistance** — Series resistance `0.001` `Ohm` (default) | nonnegative scalar

Series resistance of lines *a*, *b*,
and *c*.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Balanced
impedance`.

### **Mutual resistance** — Mutual resistance `0` `Ohm` (default) | nonnegative scalar

Mutual resistance between each pair of lines. Use this value to
account for losses in a common return path.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Balanced
impedance`.

### **Line a leakage conductance** — Line *a* parallel leakage conductance `1e-9` `1/Ohm` (default) | nonnegative scalar

Parallel leakage conductance of line *a*.

#### Dependencies

To enable this parameter, set
**Parameterization** to `General
impedance`.

### **Line b leakage conductance** — Line *b* parallel leakage conductance `1e-9` `1/Ohm` (default) | nonnegative scalar

Parallel leakage conductance of line *b*.

#### Dependencies

To enable this parameter, set
**Parameterization** to `General
impedance`.

### **Line c leakage conductance** — Line *c* parallel leakage conductance `1e-9` `1/Ohm` (default) | nonnegative scalar

Parallel leakage conductance of line *a*.

#### Dependencies

To enable this parameter, set
**Parameterization** to `General
impedance`.

### **Line leakage conductance** — Parallel leakage conductance `1e-9` `1/Ohm` (default) | nonnegative scalar

Parallel leakage conductance of lines *a*,
*b*, and *c*.

#### Dependencies

To enable this parameter, set
**Parameterization** to `Balanced
impedance`.

### Faults

### **Port 1 connection fault** — Option to add fault to port 1 `Add fault`

*Since R2025a*

Option to add a fault to the three-phase connection port
**~1** of the block.

To add a fault, click the **Add fault**
hyperlink.

### **Fault type** — Type of fault `Single-phase to ground (a-g)` (default) | `Single-phase to ground (b-g)` | `Single-phase to ground (c-g)` | `Two-phase (a-b)` | `Two-phase (b-c)` | `Two-phase (c-a)` | `Two-phase to ground (a-b-g)` | `Two-phase to ground (b-c-g)` | `Two-phase to ground (c-a-g)` | `Three-phase (a-b-c)` | `Three-phase to ground (a-b-c-g)`

*Since R2025a*

Type of fault to model. The visibility of the related parameters
depends on the fault model.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for the
**Port 1 connection fault** parameter.

### **Faulted phase-neutral resistance** — Faulted resistance between phase connection and neutral point `1e-3` `Ohm` (default) | positive scalar

*Since R2025a*

Resistance between the phase connection and the neutral point when the
fault is active.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for the
**Port 1 connection fault** parameter, and set
**Fault type** to one of these options:

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

### **Faulted neutral-ground resistance** — Faulted resistance between neutral point and electrical reference `1e-3` `Ohm` (default) | positive scalar

*Since R2025a*

Resistance between the neutral point and the electrical reference when
fault is active.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for the
**Port 1 connection fault** parameter, and set
**Fault type** to one of these options:

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

### **Unfaulted phase-neutral conductance** — Unfaulted conductance between phase connection and neutral point `1e-6` `1/Ohm` (default) | positive scalar

*Since R2025a*

Conductance between the phase connection and the neutral point when
the fault is not active.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for the
**Port 1 connection fault** parameter and set
**Fault type** to one of these options:

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

### **Trigger type** — Trigger type `Always on` (default) | `Timed` | `Additional triggers` | `Conditional` | `Manual`

Trigger type, specified as one of these options:

- `Always On` — The fault injects at the start of the
  simulation.
- `Timed` — The fault injects when the simulation time
  reaches the value you specify for the **Trigger fault at time**
  parameter.
- `Additional triggers` — The fault injects as a result
  of additional triggers not available in the block dialog box. Select this option
  and click the **Open fault properties** hyperlink to set the
  **Trigger type** to one of these values in the Property
  Inspector:

  - `Conditional` — The fault injects as a result
    of a condition that reflects a behavior associated with a signal.
    Conditionals evaluate the Boolean expression in the
    **Condition** parameter at each time step. To learn
    more, see Create and Manage Conditionals.
  - `Manual` — The fault injects or clears when
    you toggle the status in the **Fault Dashboard** pane.
    To learn more, see Manually Trigger Faults in Models.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Port 1 connection fault**
parameter.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for the
**Port 1 connection fault** parameter and set
**Trigger type** to
`Timed`.

### **Trigger configuration** — Option to enable additional trigger types `Open fault properties`

Option to enable additional trigger types not available in the block dialog box. To set the
**Trigger type** parameter to `Conditional` or
`Manual`, click the **Open fault properties**
hyperlink and set the **Trigger type** in the Property Inspector.

To enable this parameter, click the **Add fault** hyperlink for the
**Port 1 connection fault** parameter and set
**Trigger type** to
`Additional triggers`.

### **Port 2 connection fault** — Option to add fault to port 2 `Add fault`

*Since R2025a*

Option to add a fault to the three-phase connection port
**~2** of the block.

To add a fault, click the **Add fault**
hyperlink.

### **Fault type** — Type of fault `Single-phase to ground (a-g)` (default) | `Single-phase to ground (b-g)` | `Single-phase to ground (c-g)` | `Two-phase (a-b)` | `Two-phase (b-c)` | `Two-phase (c-a)` | `Two-phase to ground (a-b-g)` | `Two-phase to ground (b-c-g)` | `Two-phase to ground (c-a-g)` | `Three-phase (a-b-c)` | `Three-phase to ground (a-b-c-g)`

*Since R2025a*

Type of fault to model. The visibility of the related parameters
depends on the fault model.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Port 2 connection fault**
parameter.

### **Faulted phase-neutral resistance** — Faulted resistance between phase connection and neutral point `1e-3` `Ohm` (default) | positive scalar

*Since R2025a*

Resistance between the phase connection and the neutral point when the
fault is active.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Port 2 connection fault**
parameter and set **Fault type** to one of these options:

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

### **Faulted neutral-ground resistance** — Faulted resistance between neutral point and electrical reference `1e-3` `Ohm` (default) | positive scalar

*Since R2025a*

Resistance between the neutral point and the electrical reference when
fault is active.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Port 2 connection fault**
parameter and set **Fault type** to one of these options:

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

### **Unfaulted phase-neutral conductance** — Unfaulted conductance between phase connection and neutral point `1e-6` `1/Ohm` (default) | positive scalar

*Since R2025a*

Conductance between the phase connection and the neutral point when
the fault is not active.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Port 2 connection fault**
parameter and set **Fault type** to one of these options:

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

### **Trigger type** — Trigger type `Always on` (default) | `Timed` | `Additional triggers` | `Conditional` | `Manual`

Trigger type, specified as one of these options:

- `Always On` — The fault injects at the start of the
  simulation.
- `Timed` — The fault injects when the simulation time
  reaches the value you specify for the **Trigger fault at time**
  parameter.
- `Additional triggers` — The fault injects as a result
  of additional triggers not available in the block dialog box. Select this option
  and click the **Open fault properties** hyperlink to set the
  **Trigger type** to one of these values in the Property
  Inspector:

  - `Conditional` — The fault injects as a result
    of a condition that reflects a behavior associated with a signal.
    Conditionals evaluate the Boolean expression in the
    **Condition** parameter at each time step. To learn
    more, see Create and Manage Conditionals.
  - `Manual` — The fault injects or clears when
    you toggle the status in the **Fault Dashboard** pane.
    To learn more, see Manually Trigger Faults in Models.

#### Dependencies

To enable this parameter, click the **Add fault**
hyperlink for the **Port 2 connection fault**
parameter.

### **Trigger fault at time** — Time before entering faulted state `0` `s` (default) | nonnegative scalar

Simulation time at which the block enters the faulted state.

#### Dependencies

To enable this parameter, click the **Add fault** hyperlink for the
**Port 2 connection fault** parameter and set
**Trigger type** to
`Timed`.

### **Trigger configuration** — Option to enable additional trigger types `Open fault properties`

Option to enable additional trigger types not available in the block dialog box. To set the
**Trigger type** parameter to `Conditional` or
`Manual`, click the **Open fault properties**
hyperlink and set the **Trigger type** in the Property Inspector.

To enable this parameter, click the **Add fault** hyperlink for the
**Port 2 connection fault** parameter and set
**Trigger type** to
`Additional triggers`.
## Libraries

Simscape / Electrical / Passive / Lines

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2025a: Model faults at the three-phase connection ports

You can now model a phase-to-ground or a phase-to-phase fault at each of the two
three-phase connection ports of the block. To specify the value of the faulted
resistances and the unfaulted conductance, use the **Faulted phase-neutral
resistance**, **Faulted neutral-ground resistance**,
and **Unfaulted phase-neutral conductance** parameters.

### R2025a: The **Modeling Option** parameter has changed

The **Modeling option** parameter has been replaced
with the **Electrical connection** parameter inside the
**Main** section in the block dialog box or
Property Inspector.

If a model you created in an earlier release contains this block, the software
automatically sets the value of the **Electrical
connection** parameter to the value you specified for the **Modeling option** parameter.

## Description

Magnetically couple three-phase lines

The Coupled Lines (Three-Phase) block models three
magnetically coupled lines. Each line has a self-inductance, series resistance, and
parallel conductance. In addition, there is a mutual inductance and mutual resistance
between each pair of lines.

Use this block when the magnetic coupling in a three-phase network is nonnegligible.
These effects are most prominent when:

- The lines are parallel and close together.
- The self-inductances of the lines are high.
- The AC frequency of the network is high.

To model magnetic coupling of a single pair of lines, use the Coupled Lines
(Pair) block. To model capacitive coupling between the lines, use
the Transmission Line block.

### Equivalent Circuit

The equivalent circuit shows the coupling between two arbitrary phases
*i*, and *j*. The block models the magnetic
coupling using such an equivalent circuit between each of the three phases
*a*, *b*, and *c*.

In this figure:

- *Ri* and
  *Rj* are the series
  resistances of lines *i* and *j*,
  respectively.
- *Li* and
  *Lj* are the
  self-inductances of lines *i* and *j*,
  respectively.
- *Rm,ij* is the mutual
  resistance between lines *i* and *j*,
  respectively.
- *Lm,ij* is the mutual
  inductance between lines *i* and *j*,
  respectively.
- *Gi* and
  *Gj* are the leakage
  conductances of lines *i* and *j*,
  respectively.
- *Vi* and
  *Vj* are voltage drops
  across lines *i* and *j*,
  respectively.
- *Ii* and
  *Ij* are the currents
  through the resistors
  *Ri-Rm,ij*
  and
  *Rj-Rm,ij*,
  respectively.

### Equations

The defining equation for this block is:

V=[RaRm,abRm,acRm,abRbRm,bcRm,acRm,bcRc]I+[LaLm,abLm,acLm,abLbLm,bcLm,acLm,bcLc]dIdt,

where:

V=[VaVbVc],

I=[IaIbIc].

*Ia*,
*Ib*, and
*Ic* are, in general, not equal to
the currents in lines *a*, *b*, and
*c*. These terminal currents make up the vector:

Itotal=I+[Ga000Gb000Gc]V.

### Inductive Coupling

To quantify the strength of the coupling between the two lines, you can use a
coupling factor or coefficient of coupling *k*. The coupling factor
relates the mutual inductance to the line self-inductances:

Lm,ij=kLiLj.

This coupling factor must fall in the range −1<k<1, where a negative coupling factor indicates a reversal in
orientation of one of the coils. The magnitude of *k* indicates:

- |k|=0 — There is no magnetic coupling between the two
  lines.
- 0<|k|<0.5 — The two lines are loosely coupled and mutual
  magnetic effects are small.
- 0.5≤|k|<1 — The two lines are strongly coupled and mutual
  magnetic effects are large.

### Mutual Resistance

If the three lines share a common return path, you can model the resistance of
this return path using the **Mutual resistance** parameter
*Rm*. This workflow is equivalent to
setting the **Mutual resistance** to zero and explicitly modeling
the return path resistance *Rm*, as shown in
this diagram.

If the three lines do not share a common return path, set the mutual resistance
parameter to zero and model each of the return resistances explicitly.

### Faults

*Since R2025a*

To model a fault in the Coupled Lines (Three-Phase) block, in the **Faults** section, click **Add fault** next to the fault that you want to model. For more information about fault modeling, see Fault Behavior Modeling and Fault Triggering.

The Coupled Lines (Three-Phase) block allows you to model these types of fault:

- Single-phase-to-ground fault (a-g, b-g, or c-g)
- Two-phase fault (a-b, b-c, or c-a)
- Two-phase-to-ground fault (a-b-g, b-c-g, or c-a-g)
- Three-phase fault (a-b-c)
- Three-phase-to-ground fault (a-b-c-g)

You can model a fault at one of the two three-phase connection ports
or at both ports at the same time.

This figure shows how the block models the faults at the two three-phase ports:

For more information about adding faults to blocks and
specifying fault triggers, see Introduction to Simscape Faults.

### Variables

To set the priority and initial target values for the block variables prior to
simulation, use the **Initial Targets** section in the block dialog
box or Property Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a
model. Using system scaling based on nominal values increases the simulation
robustness. Nominal values can come from different sources, one of which is the
**Nominal Values** section in the block dialog box or Property
Inspector. For more information, see System Scaling by Nominal Values.
