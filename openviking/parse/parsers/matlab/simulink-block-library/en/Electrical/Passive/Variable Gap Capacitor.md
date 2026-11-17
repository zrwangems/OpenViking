---
type: simulink-block
title: 'Variable Gap Capacitor'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Passive'
documentation_page: 'variablegapcapacitor'
documentation_source_path: 'ref/variablegapcapacitor.html'
language: en
---

# Variable Gap Capacitor

## Ports
```yaml
ports:
- name: +
  summary: Positive terminal electrical
  direction: conserving
- name: '-'
  summary: Negative terminal electrical
  direction: conserving
- name: R
  summary: Follower plate mechanical translational
  direction: conserving
- name: C
  summary: Base plate mechanical translational
  direction: conserving
```

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the capacitor positive
terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the capacitor negative
terminal.

### **R** — Follower plate mechanical translational

Mechanical translational conserving port associated with the follower
plate.

### **C** — Base plate mechanical translational

Mechanical translational conserving port associated with the base
plate.
## Parameters
```yaml
parameters:
- name: Capacitor plate area
  summary: Capacitor plate area 1e-3 m^2 (default) | positive scalar
  group: ''
- name: Dielectric medium thickness
  summary: Dielectric medium thickness 1e-4 m (default) | positive scalar
  group: ''
- name: Specify properties of dielectric medium
  summary: Option to specify properties of dielectric medium Off (default) | On
  group: ''
- name: Relative permittivity of dielectric medium
  summary: Relative permittivity of dielectric 1.0 (default) | positive scalar
  group: ''
- name: Young's modulus of dielectric material
  summary: Young's modulus of dielectric material 0 Pa (default) | nonnegative scalar
  group: ''
```

### **Capacitor plate area** — Capacitor plate area `1e-3` `m^2` (default) | positive scalar

Area of the plate.

### **Dielectric medium thickness** — Dielectric medium thickness `1e-4` `m` (default) | positive scalar

Thickness of the dielectric medium.

### **Specify properties of dielectric medium** — Option to specify properties of dielectric medium `Off` (default) | `On`

Option to specify the properties of the dielectric medium. If you clear
this parameter, the block assumes that the dielectric medium is a vacuum and
that the elastic force is zero.

### **Relative permittivity of dielectric medium** — Relative permittivity of dielectric `1.0` (default) | positive scalar

Permittivity of the dielectric medium relative to the permittivity of a
vacuum.

#### Dependencies

To enable this parameter, select the **Specify properties of
dielectric medium** parameter.

### **Young's modulus of dielectric material** — Young's modulus of dielectric material `0` `Pa` (default) | nonnegative scalar

Young's modulus of the dielectric material.

#### Dependencies

To enable this parameter, select the **Specify properties of
dielectric medium** parameter.
## Libraries

Simscape / Electrical / Passive

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023b**

## Description

Capacitor with parallel plates and variable gap

The Variable Gap Capacitor block models a capacitor
with parallel plates and a variable gap. When you apply a voltage to the block, the
voltage produces an electric field between the plates, creating an attractive
electrostatic force.

You can specify the properties of the dielectric medium by selecting the
**Specify properties of dielectric medium** parameter. If you
specify the Young's modulus of the dielectric material, the displacement between the
plates deforms the dielectric medium, which produces an elastic force. If you do not
specify the properties of the dielectric medium, the block assumes that the dielectric
medium is a vacuum and that the displacement does not produce an elastic force.

When the capacitor is charged, the translational forces can also affect the
capacitance, current, and voltage of the capacitor.

### Equations

The capacitance is defined by this equation:

C=ε0εAd+x,

where:

- ε0 is the permittivity of a vacuum.
- *ε* is the **Relative permittivity of
  dielectric medium** parameter.
- *A* is the **Capacitor plate area**
  parameter.
- *d* is the **Dielectric medium
  thickness** parameter.
- *x* is the displacement of the plate.

The attractive electrostatic force is given by this equation:

F=C2V22Aε0ε,

where *V* is the voltage across the
capacitor.

The elastic force is given by this equation:

Fdef=EAxd,

where *E* is the **Young's modulus of
dielectric material** parameter.

The total force through the block is the sum of the attractive electrostatic force
and the elastic force.

### Variables

To set the priority and initial target values for the block variables before simulation,
use the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. You can
specify nominal values using different sources, including the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see System Scaling by Nominal Values.
