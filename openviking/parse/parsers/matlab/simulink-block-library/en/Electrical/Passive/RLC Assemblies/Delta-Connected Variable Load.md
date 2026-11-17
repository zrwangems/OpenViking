---
type: simulink-block
title: 'Delta-Connected Variable Load'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / RLC Assemblies'
documentation_page: 'deltaconnectedvariableload'
documentation_source_path: 'ref/deltaconnectedvariableload.html'
language: en
---

# Delta-Connected Variable Load

## Ports
```yaml
ports:
- name: P
  summary: Real power physical signal
  direction: input
- name: '~'
  summary: Three-phase port electrical
  direction: conserving
```

### Input

### **P** — Real power physical signal

Physical signal input port associated with the real power.
### Conserving

### **~** — Three-phase port electrical

Expandable three-phase
electrical conserving port.
## Parameters
```yaml
parameters:
- name: Modeling option
  summary: Whether to model composite or expanded three-phase ports Composite three-phase ports (default) | Expanded three-phase
    ports
  group: ''
- name: Rated voltage
  summary: Rated line-line voltage 24e3 V (default) | positive scalar
  group: ''
- name: Minimum real power
  summary: Minimum real power 1e3 W (default) | positive scalar
  group: ''
```

### **Modeling option** — Whether to model composite or expanded three-phase ports `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to model composite or expanded three-phase ports.

Composite three-phase ports represent three individual electrical conserving ports
with a single block port. You can use composite three-phase ports to build models that
correspond to single-line diagrams of three-phase electrical systems.

Expanded three-phase ports represent the individual phases of a three-phase system
using three separate electrical conserving ports.

### **Rated voltage** — Rated line-line voltage `24e3` `V` (default) | positive scalar

RMS of rated line-line voltage for the resistance equation.

### **Minimum real power** — Minimum real power `1e3` `W` (default) | positive scalar

Minimum real power that the three-phase load dissipates when supplied at
the rated voltage. The value must be greater than 0.
## Libraries

Simscape / Electrical / Passive / RLC Assemblies

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Three-phase variable load wired in delta configuration

The Delta-Connected Variable Load block models a three-phase
variable load wired in a delta configuration. Each limb of the load contains a resistor.
The block calculates the resistance required to draw the real power of the physical
signal input **P** at the rated voltage that you specify. Therefore,
the block can represent a real load.

To ensure that the resistance is always greater than zero, you specify the minimum
real power that the load consumes. The minimum real power must be greater than zero.

### Equations

The resistance is defined by

R=3VRated2P,

where:

- *R* is the per-phase series resistance.
- *VRated* is the RMS of rated
  line-line voltage.
- *P* is the three-phase real power required. If the
  value of the **P** input port is less than the value of
  the **Minimum real power** parameter, the block uses
  the minimum real power to calculate the resistance.
