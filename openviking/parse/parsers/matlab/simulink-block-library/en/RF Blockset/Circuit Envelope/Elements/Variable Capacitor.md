---
type: simulink-block
title: 'Variable Capacitor'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'variablecapacitor'
documentation_source_path: 'ref/variablecapacitor.html'
language: en
---

# Variable Capacitor

## Ports
```yaml
ports:
- name: C
  summary: Simulink control signal scalar
  direction: input
  data_types: double
```

### Input

### **C** — Simulink control signal scalar

Simulink control signal, specified as a scalar.

**Data Types:** `double`
## Parameters
```yaml
parameters: []
```

The Variable Capacitor block has no parameters.
## Libraries

RF Blockset / Circuit Envelope / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2016b**

### R2021b: Variable Capacitor block icon updated

Starting in R2021b, the Variable Capacitor block icon is now
updated. When you open a model created before R2021b containing a Variable
Capacitor block, the software replaces the block icon with the R2021b
version.

## Description

Model variable capacitor

The Variable Capacitor block controls the output
of RF Blockset™ feedback circuits using Simulink® controlled
capacitance in farads. The minimum value of the capacitance (*Cmin*)
is a RF Blockset defined constant independent of the Simulink control
signal. The block has two electrical terminals. One terminal is for
the Simulink control signal and one terminal is for the RF Blockset
signal.
