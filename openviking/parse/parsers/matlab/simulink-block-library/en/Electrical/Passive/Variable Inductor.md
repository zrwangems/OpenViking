---
type: simulink-block
title: 'Variable Inductor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'variableinductor'
documentation_source_path: 'ref/variableinductor.html'
language: en
---

# Variable Inductor

## Ports
```yaml
ports:
- name: L
  summary: Inductance physical signal
  direction: input
- name: +
  summary: Positive terminal electrical
  direction: conserving
- name: '-'
  summary: Negative terminal electrical
  direction: conserving
```

### Input

### **L** — Inductance physical signal

Physical signal input port associated with the inductance. L must be
finite, greater than zero, and continuous (no step changes).
### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the inductor positive
voltage.

### **-** — Negative terminal electrical

Electrical conserving port associated with the inductor negative
voltage.
## Parameters
```yaml
parameters:
- name: Equation
  summary: Equation for block inductance V = L*dI/dt + dL/dt*I (default) | V = L*dI/dt
  group: ''
- name: Minimum inductance L>0
  summary: Minimum inductance 1e-6 H (default)
  group: ''
- name: Parallel conductance
  summary: Parallel conductance 1e-9 1/Ohm (default)
  group: ''
- name: Initial current
  summary: Initial current 0 A (default)
  group: ''
- name: Initial magnetic flux
  summary: Initial magnetic flux 0 Wb (default)
  group: ''
```

### **Equation** — Equation for block inductance `V = L*dI/dt + dL/dt*I` (default) | `V = L*dI/dt`

Select one of the following options for block inductance:

- `V = L*dI/dt + dL/dt*I` — This
  equation assumes the inductance is defined as the ratio of the
  magnetic flux to the steady-state current. This option is the
  default.
- `V = L*dI/dt` — This equation
  assumes the inductance is defined as the local gradient of the
  flux-current curve for a given current.

### **Minimum inductance L>0** — Minimum inductance `1e-6` `H` (default)

The lower limit on the value of the signal at port L. This limit prevents
the signal from reaching a value that has no physical meaning.

### **Parallel conductance** — Parallel conductance `1e-9` `1/Ohm` (default)

The value of the conductance placed in parallel with the variable
inductor.

### **Initial current** — Initial current `0` `A` (default)

The output current at the start of the simulation.

#### Dependencies

This parameter is visible only when you select `V =
L*dI/dt` for the **Equation**
parameter.

### **Initial magnetic flux** — Initial magnetic flux `0` `Wb` (default)

The magnetic flux at the start of the simulation.

#### Dependencies

This parameter is visible only when you select `V =
L*dI/dt + dL/dt*I` for the
**Equation** parameter.
## Libraries

Simscape / Electrical / Passive

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Linear time-varying inductor

The Variable Inductor block represents a linear
time-varying inductor. The block provides two options for the relationship between the
voltage *v* across the device and the current through the inductor
*i* when the inductance at port L is *L*. The
**Equation** parameter determines which of the following equations
the block uses:

- v=dLdti+Ldidt

  Use the preceding equation when the inductance is defined as the ratio of
  the magnetic flux Ф to the steady-state current:

  L(i)=Φ(i)i
- v=Ldidt

  Use the preceding equation when the inductance is defined as the local
  gradient of the flux-current curve for a given current:

  L(i)=dΦ(i)di

The block includes a conductance in parallel with the variable inductor. You can use
the conductor to represent the total insulation conductance of the inductor. You may
need to use the conductor to prevent numerical issues for some circuit topologies, such
as where a Variable Inductor block is connected in series
with another inductor block that does not have a parallel conductance.
