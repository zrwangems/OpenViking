---
type: simulink-block
title: 'Wye-Connected Variable Load'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Passive / RLC Assemblies'
documentation_page: 'wyeconnectedvariableload'
documentation_source_path: 'ref/wyeconnectedvariableload.html'
language: en
---

# Wye-Connected Variable Load

## Ports

### Input

### **P** — Real power physical signal

Physical signal input port associated with the real power.
### Conserving

### **~** — Three-phase port electrical

Expandable three-phase
port.

### **n** — Neutral phase electrical

Electrical conserving port associated with the neutral phase.

## Parameters

### **Modeling option** — Whether to model composite or expanded three-phase ports `Composite three-phase ports` (default) | `Expanded three-phase ports`

Whether to model composite or expanded three-phase ports.

Composite three-phase ports represent three individual electrical conserving ports
with a single block port. You can use composite three-phase ports to build models that
correspond to single-line diagrams of three-phase electrical systems.

Expanded three-phase ports represent the individual phases of a three-phase system
using three separate electrical conserving ports.

### **Rated voltage** — Rated line-line voltage `24e3` `V` (default)

RMS, rated line-line voltage for the resistance equation.

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

**Introduced in R2014b**

## Description

Three-phase variable load wired in wye configuration

The Wye-Connected Variable Load block models a
three-phase variable load wired in a wye configuration. Each limb of the load contains a
resistor. The block calculates the resistance required to draw the real power of the
physical signal input P at the rated voltage that you specify. Therefore, the block can
represent a real load.

To ensure that the resistance is always greater than zero, you specify the minimum
real power that the load consumes. The minimum real power must be greater than zero.

### Equations

The resistance is defined by

R=VRated2P,

where:

- *R* is the per-phase series resistance.
- *VRated* is the RMS, rated
  line-line voltage.
- *P* is the three-phase real power required.
