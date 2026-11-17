---
type: simulink-block
title: 'Infinite Flow Resistance (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Elements'
documentation_page: 'infiniteflowresistancema'
documentation_source_path: 'ref/infiniteflowresistancema.html'
language: en
---

# Infinite Flow Resistance (MA)

## Ports
```yaml
ports:
- name: A
  summary: Mass flow rate and energy flow rate are zero moist air
  direction: conserving
- name: B
  summary: Mass flow rate and energy flow rate are zero moist air
  direction: conserving
```

### Conserving

### **A** — Mass flow rate and energy flow rate are zero moist air

Moist air conserving port where the mass flow rate and energy flow
rate are both equal to zero.

### **B** — Mass flow rate and energy flow rate are zero moist air

Moist air conserving port where the mass flow rate and energy flow
rate are both equal to zero.
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Simscape / Foundation Library / Moist Air / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

## Description

Perfectly insulated break in moist air network

The Infinite Flow Resistance (MA) block represents a
break in a moist air network. There is no mass or energy flow through the break.
However, the moist air properties, specified by the Moist Air
Properties (MA) block connected to the circuit, are the same on both
sides of the break. Use this block to set the priority and initial target value to the
differences in pressure, temperature, specific humidity, and trace gas mass fraction
between port **A** and port **B**.

### Variables

To set the priority and initial target values for the block variables prior to simulation, use
the **Initial Targets** section in the block dialog box or Property
Inspector. For more information, see Set Priority and Initial Target for Block Variables and Initial Conditions for Blocks with Finite Moist Air Volume.

Nominal values provide a way to specify the expected magnitude of a variable in a model.
Using system scaling based on nominal values increases the simulation robustness. Nominal
values can come from different sources, one of which is the **Nominal
Values** section in the block dialog box or Property Inspector. For more
information, see Modify Nominal Values for a Block Variable.
