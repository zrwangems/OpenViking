---
type: simulink-block
title: 'Inductor'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'inductor'
documentation_source_path: 'ref/inductor.html'
language: en
---

# Inductor

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Inductance
  summary: Inductance value 1e-9 H (default) | real number
  group: ''
```

### **Inductance** — Inductance value `1e-9 H` (default) | real number

Inductance value, specified as a real number. Specify the units
of the capacitance from the corresponding drop-down menu.

If you set this parameter to a value between `0` and `1e-18` `H`,
the block uses a value equal to `1e-18` `H` during
simulation. By default, the value is `1e-9` `H`.
## Libraries

RF Blockset / Circuit Envelope / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

### R2021b: Inductor block icon updated

Starting in R2021b, the Inductor block icon has updated. When you
open a model created before R2021b containing an Inductor block, the
software replaces the block icon with the R2021b version.

## Description

Model inductor for circuit envelope analysis

The Inductor block models an inductor in circuit
envelope environment.
