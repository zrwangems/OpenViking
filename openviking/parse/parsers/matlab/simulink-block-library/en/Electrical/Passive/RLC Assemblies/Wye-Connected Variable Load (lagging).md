---
type: simulink-block
title: 'Wye-Connected Variable Load (lagging)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive / RLC Assemblies'
documentation_page: 'wyeconnectedvariableloadlagging'
documentation_source_path: 'ref/wyeconnectedvariableloadlagging.html'
language: en
---

# Wye-Connected Variable Load (lagging)

## Ports

### Input

### **P** — Real power physical signal

Physical signal input port associated with the real power.

### **Q** — Reactive power physical signal

Physical signal input port associated with the reactive power.
### Conserving

### **~** — Three-phase port electrical

Expandable three-phase
electrical conserving port.

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

### Main

### **Rated voltage** — Rated line-line voltage `24e3` `V` (default)

RMS, rated line-line voltage for the resistance equation.

### **Rated electrical frequency** — Nominal AC electrical frequency `60` `Hz` (default)

Nominal AC electrical frequency for the inductance equation.

### **Minimum real power** — Minimum real power `1e3` `W` (default) | positive scalar

Minimum real power that the three-phase load dissipates when supplied
at the rated voltage. The value must be greater than 0.

### **Minimum reactive power** — Minimum reactive power `1e3` `V*A` (default) | positive scalar

Minimum reactive power that the three-phase load dissipates when
supplied at the rated voltage. The value must be greater than 0.

### Parasitics

### **Parasitic parallel conductance** — Parasitic parallel conductance `1e-6` `1/Ohm` (default)

Conductance that the block adds, in parallel, to the series RL.

## Libraries

Simscape / Electrical / Passive / RLC Assemblies

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2014b**

## Description

Three-phase variable, lagging load wired in wye configuration

The Wye-Connected Variable Load (lagging) block models
a three-phase variable, lagging load wired in a wye configuration. Each limb of the load
contains a resistor (R) and an inductor (L) connected in series. The block calculates
the resistance and inductance required to draw the real and reactive powers of the
physical signal inputs P and Q at the rated voltage and rated frequency that you
specify. Therefore, the block can represent a real and lagging reactive load.

To ensure that the resistance and inductance are always greater than zero, you specify
the minimum real power and the reactive power that the load consumes. The minimum real
power and the reactive power must be greater than zero.

### Electrical Defining Equations

The per-phase series resistance and inductance are defined by

R=PVRated2P2+Q2

and

L=QVRated22πFRated(P2+Q2),

where:

- *R* is the per-phase series resistance.
- *L* is the per-phase series inductance.
- *VRated* is the RMS, rated
  line-line voltage.
- *FRated* is the nominal AC
  electrical frequency.
- *P* is the three-phase real power required.
- *Q* is the three-phase lagging reactive power
  required.

The inductance is defined as the ratio of the magnetic flux, φ, to the
steady-state current:

L(i)=ϕ(i)i.

Therefore the current-voltage relationship for the inductor is:

v=dLdti+Ldidt.

### Variables

To set the priority and initial target values for the block variables prior to simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
