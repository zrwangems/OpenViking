---
type: simulink-block
title: 'Inductor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Electrical / Electrical Elements'
documentation_page: 'inductor'
documentation_source_path: 'ref/inductor.html'
language: en
---

# Inductor

## Ports
```yaml
ports:
- name: +
  summary: Positive terminal electrical
  direction: conserving
- name: '-'
  summary: Negative terminal electrical
  direction: conserving
```

### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the inductor positive terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the inductor negative terminal.
## Parameters
```yaml
parameters:
- name: Inductance
  summary: Inductance of the inductor 1e-6 H (default) | positive scalar
  group: ''
- name: Series resistance
  summary: Small parasitic effects 0 Ohm (default) | nonnegative scalar
  group: ''
- name: Parallel conductance
  summary: Small parasitic effects 1e-9 1/Ohm (default) | nonnegative scalar
  group: ''
```

### **Inductance** — Inductance of the inductor `1e-6 H` (default) | positive scalar

Inductance value.

### **Series resistance** — Small parasitic effects `0 Ohm` (default) | nonnegative scalar

Represents small parasitic effects. The series resistance can be used to represent
the DC winding resistance or the resistance due to the skin effect.

### **Parallel conductance** — Small parasitic effects `1e-9 1/Ohm` (default) | nonnegative scalar

Represents small parasitic effects. Simulation of some circuits may require the
presence of a small parallel conductance.
## Libraries

Simscape / Foundation Library / Electrical / Electrical Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Linear inductor in electrical systems

The Inductor block models a linear inductor, described with
the following equation:

V=LdIdt

where:

- *V* is voltage.
- *L* is inductance.
- *I* is current.
- *t* is time.

The **Series resistance** and **Parallel conductance**
parameters represent small parasitic effects. The series resistance can be used to represent
the DC winding resistance or the resistance due to the skin effect. Simulation of some
circuits may require the presence of a small parallel conductance. For more information, see
Modeling Best Practices.

Connections + and – are conserving electrical ports corresponding to the positive and
negative terminals of the inductor, respectively. The current is positive if it flows from
positive to negative, and the voltage across the inductor is equal to the difference between
the voltage at the positive and the negative terminal, *V*(+) –
*V*(–).

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
