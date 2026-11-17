---
type: simulink-block
title: 'Mass (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Elements'
documentation_page: 'masspb'
documentation_source_path: 'ref/masspb.html'
language: en
---

# Mass (PB)

## Ports
```yaml
ports:
- name: R
  summary: Port that connects mass to the circuit position-based mechanical translational
  direction: conserving
```

### Conserving

### **R** — Port that connects mass to the circuit position-based mechanical translational

Position-based mechanical translational conserving port that connects the mass to
the physical network.
## Parameters
```yaml
parameters:
- name: Mass
  summary: Constant mass 1 kg (default) | positive scalar
  group: ''
```

### **Mass** — Constant mass `1 kg` (default) | positive scalar

Mass value. The mass is constant during simulation.
## Libraries

Simscape / Foundation Library / Translational / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

Point mass with gravitational effects

The Mass (PB) block represents a point mass with
gravitational effects that moves along an inclined rail. Gravity can induce motion along the
rail. The force flow equations are:

facc=m⋅v˙

facc=f+fgp

fgp=−m⋅g⋅sin(θ)

where:

- *f*acc is force proportional to mass
  acceleration. Positive force accelerates the mass in the positive direction.
- *f* is net force of the other mechanical components in the network
  acting on the mass.
- *f*gp is force proportional to the parallel
  component of gravitational acceleration, that is, to the gravitational acceleration acting
  along the rail.
- *m* is the mass.
- *v* is the mass velocity.
- *g* is the gravitational acceleration.
- *θ* is the rail incline angle.

The Mechanical Translational Properties (PB) block
specifies the gravitational acceleration and rail incline angle in the network. For more
information, see Interpreting Logged Forces in Mass Blocks.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
