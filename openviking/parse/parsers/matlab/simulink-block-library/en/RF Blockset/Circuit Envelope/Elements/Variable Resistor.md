---
type: simulink-block
title: 'Variable Resistor'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'variableresistor'
documentation_source_path: 'ref/variableresistor.html'
language: en
---

# Variable Resistor

## Ports
```yaml
ports:
- name: R
  summary: Simulink control signal scalar
  direction: input
  data_types: double
```

### Input

### **R** — Simulink control signal scalar

Simulink control signal, specified as a scalar.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Simulate noise
  summary: Simulate thermal noise on (default) | off
  group: ''
```

### **Simulate noise** — Simulate thermal noise `on` (default) | `off`

Select this parameter, to simulate thermal noise in the variable resistor.
Then, in the Configuration block dialog box,
also select the **Simulate noise** check box. By default,
both **Simulate noise** check boxes are selected.

This parameter inserts a current noise source with the single-sided power
density of 4
*k**T*/*R*
A2/Hz, where:

- k is the Boltzmann constant
- T is the value of the **Temperature** parameter,
  in degrees Kelvin. (Also located in the Configuration
  block.)
## Libraries

RF Blockset / Circuit Envelope / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2017b**

### R2021b: Variable Resistor block icon updated

Starting in R2021b, the Variable Resistor block icon is now
updated. The block icons are now dynamic and show the current state of the noise
parameter.

When you open a model created before R2021b containing a Variable
Resistor block, the software replaces the block icon with the R2021b
version.

## Description

Model variable resistor

The Variable Resistor block controls the output of RF Blockset™ feedback circuits using Simulink® controlled resistance in ohms. The minimum value of the resistance
(*Rmin*) is an RF Blockset defined constant independent of the
Simulink control signal. The block has two electrical terminals. One terminal is for the
Simulink control signal and one terminal is for the RF Blockset signal.

Variable Resistor block mask icons are dynamic and show the current
state of the applied noise parameter. This table shows you how the icons on this block
vary based on the state of the **Simulate noise** parameter on the
block.

| Simulate noise: `on` | Simulate noise: `off` |
| --- | --- |
| Variable Resistor block icon with Simulate noise is set to on. | Variable Resistor block icon with Simulate noise is set to off. |
