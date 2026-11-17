---
type: simulink-block
title: 'Capacitor'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'capacitor'
documentation_source_path: 'ref/capacitor.html'
language: en
---

# Capacitor

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Capacitance
  summary: Capacitance value 1e-12 F (default) | real number
  group: ''
```

### **Capacitance** — Capacitance value `1e-12 F` (default) | real number

Capacitance value, specified as a real number. Specify the units
of the capacitance from the corresponding drop-down menu.

If you set this parameter value between `0` and `1e-18` `F`, the block uses a value equal
to `1e-18` `F` during simulation. By default,
the value is `1e-12` `F`.
## Libraries

RF Blockset / Circuit Envelope / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

### R2021b: Capacitor block icon updated

Starting in R2021b, the Capacitor block icon has updated. When you
open a model created before R2021b containing a Capacitor block, the
software replaces the block icon with the R2021b version.

## Description

Model capacitor for circuit envelope analysis

The Capacitor block models a capacitor in circuit envelope environment.
