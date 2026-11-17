---
type: simulink-block
title: 'Mass With Length (PB)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Translational / Elements'
documentation_page: 'masswithlengthpb'
documentation_source_path: 'ref/masswithlengthpb.html'
language: en
---

# Mass With Length (PB)

## Ports
```yaml
ports:
- name: B
  summary: Base port position-based mechanical translational
  direction: conserving
- name: F
  summary: Follower port position-based mechanical translational
  direction: conserving
```

### Conserving

### **B** — Base port position-based mechanical translational

Position-based mechanical translational conserving port that represents the base
connection.

### **F** — Follower port position-based mechanical translational

Position-based mechanical translational conserving port that represents the
follower connection. For nonzero length, port **F** has a more
positive position than port **B**.
## Parameters
```yaml
parameters:
- name: Mass
  summary: Constant mass 1 kg (default) | positive scalar
  group: ''
- name: Length
  summary: Length of mass 0 m (default) | nonnegative scalar
  group: ''
- name: Log the position of an intermediate point
  summary: Whether to log position of intermediate point off (default) | on
  group: ''
- name: Intermediate point fractional length from B
  summary: Fractional length of logged point from port B 0.5 (default) | unitless scalar between 0 and 1
  group: ''
```

### **Mass** — Constant mass `1 kg` (default) | positive scalar

Mass value. The mass is constant during simulation.

### **Length** — Length of mass `0 m` (default) | nonnegative scalar

Length of mass, that is, distance between ports **B** and
**F**. This distance is constant during simulation.

### **Log the position of an intermediate point** — Whether to log position of intermediate point `off` (default) | `on`

Select this check box to log the position of an intermediate point between ports
**B** and **F**, for example, of the center of the
mass. For more information, see Data Logging.

### **Intermediate point fractional length from B** — Fractional length of logged point from port B `0.5` (default) | unitless scalar between 0 and 1

Fractional distance between port **B** and the intermediate point
being logged.

#### Dependencies

To enable this parameter, select the **Log the position of an
intermediate point** check box.
## Libraries

Simscape / Foundation Library / Translational / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2024b**

## Description

Mass with length and gravitational effects

The Mass With Length (PB) block represents a mass with
length and gravitational effects that moves along an inclined rail. Gravity can induce motion
along the rail.

The Mass With Length (PB) block is essentially a structural
component that consists of a Mass (PB) block connected to a
Spacer (PB) block.

Mass with length schematic

The force flow equations are:

facc=m⋅v˙

facc=f+fgp

fgp=−m⋅g⋅sin(θ)

length=xF−xB

xLog=xB+fractionLog⋅length

where:

- *f*acc is force proportional to mass
  acceleration. Positive force accelerates the mass in the positive direction.
- *f* is net force of other mechanical components in the network acting
  on the mass.
- *f*gp is force proportional to the parallel
  component of gravitational acceleration, that is, to gravitational acceleration acting
  along the rail.
- *m* is the mass.
- *v* is the mass velocity. Ports **B** and
  **F** have the same velocity,
  *v*B =
  *v*F.
- *g* is the gravitational acceleration.
- *θ* is the rail incline angle.
- *length* is the mass length.
- *x*B and
  *x*F are the absolute positions of ports
  **B** and **F**, respectively.
- *x*Log is the absolute position of an
  intermediate point, if you enable the **Log the position of an
  intermediate point** option.
- *fraction*Log is the intermediate point
  fractional length from port **B**.

For example, to log the position of the center of mass, select the **Log the position of an intermediate point** check box and set the
**Intermediate point fractional length from B** parameter to
`0.5`.

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
