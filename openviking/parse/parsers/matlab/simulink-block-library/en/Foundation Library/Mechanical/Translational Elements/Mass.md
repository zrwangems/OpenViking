---
type: simulink-block
title: 'Mass'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Mechanical / Translational Elements'
documentation_page: 'mass'
documentation_source_path: 'ref/mass.html'
language: en
---

# Mass

## Ports
```yaml
ports:
- name: M
  summary: Port that connects mass to the circuit mechanical translational
  direction: conserving
- name: N
  summary: Second graphical port mechanical translational
  direction: conserving
```

### Conserving

### **M** — Port that connects mass to the circuit mechanical translational

Mechanical translational conserving port that connects the mass to the physical
network.

### **N** — Second graphical port mechanical translational

Second mechanical translational conserving port that lets you connect the mass in
series with other elements in the block diagram. This port is rigidly connected to
port **M**, therefore the difference between the one-port and
two-port block representations is purely graphical.

#### Dependencies

To enable this port, set the **Number of graphical ports**
parameter to `2`.
## Parameters
```yaml
parameters:
- name: Mass
  summary: Constant mass 1 kg (default) | positive scalar
  group: ''
- name: Number of graphical ports
  summary: Select whether the block is graphically connected to the side of a circuit or in series with other elements 1 (default)
    | 2
  group: ''
```

### **Mass** — Constant mass `1 kg` (default) | positive scalar

Mass value. The mass is constant during simulation.

### **Number of graphical ports** — Select whether the block is graphically connected to the side of a circuit or in series with other elements `1` (default) | `2`

Select how to connect the block to the rest of the circuit:

- `1` — The block has one conserving port that
  connects it to the mechanical translational circuit. When the block has one port,
  attach it to a connection line between two other blocks.
- `2` — Selecting this option exposes the second
  port, which lets you connect the block in series with other blocks in the circuit.
  The two ports are rigidly connected and have the same velocity, therefore the block
  functions exactly the same as if it had one port.
## Libraries

Simscape / Foundation Library / Mechanical / Translational Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Ideal mechanical translational mass

The Mass block represents an ideal mechanical translational
mass that is described with the following equation:

F=mdvdt

where:

- *F* is inertia force.
- *m* is mass.
- *v* is velocity.
- *t* is time.

By default, the block has one mechanical translational conserving port. The block positive
direction is from its port to the reference point. This means that the inertia force is
positive if mass is accelerated in the positive direction.

In some applications, it is customary to display mass in series with other elements in the
block diagram layout. To support this use case, the **Number of graphical
ports** parameter lets you display a second port on the opposite side of the block
icon. The two-port variant is purely graphical: the two ports have the same velocity, so the
block functions exactly the same whether it has one or two ports. The block icon changes
depending on the value of the **Number of graphical ports** parameter.

| Number of graphical ports | Block Icon |
| --- | --- |
| `1` |  |
| `2` |  |

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
