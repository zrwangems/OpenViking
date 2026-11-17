---
type: simulink-block
title: 'Mutual Inductor'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'mutualinductor'
documentation_source_path: 'ref/mutualinductor.html'
language: en
---

# Mutual Inductor

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Inductance L1
  summary: Inductance of first inductor 1e-6 H (default) | positive scalar
  group: ''
- name: Inductance L2
  summary: Inductance of second inductor 1e-6 H (default) | positive scalar
  group: ''
- name: Coefficient of coupling
  summary: Coefficient of coupling for mutual inductance 0.9 (default) | scalar
  group: ''
```

### **Inductance L1** — Inductance of first inductor `1e-6 H` (default) | positive scalar

Inductance of the first inductor, specified as a positive scalar in
`H`, `nH`,
`μH`, `mH`.

### **Inductance L2** — Inductance of second inductor `1e-6 H` (default) | positive scalar

Inductance of the second inductor, specified as a positive scalar in
`H`, `nH`,
`μH`, `mH`.

### **Coefficient of coupling** — Coefficient of coupling for mutual inductance `0.9` (default) | scalar

Coefficient of coupling for the mutual inductance of the two inductors,
specified as a scalar value from 0 through 1.
## Libraries

RF Blockset / Circuit Envelope / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2012a**

## Description

Model two coupled inductors for circuit envelope analysis

The Mutual Inductor block models an inductor within the RF Blockset™ circuit envelope simulation environment. For an introduction to RF
simulation, see the example, Simulate High Frequency Components.

The block implements the relations

v1(t)=L1ddt[i1(t)]+Mddt[i2(t)]v2(t)=Mddt[i1(t)]+L2ddt[i2(t)]M=KL1L2

where:

- *L*1 and
  *L*2 represent
  inductances.
- *M* represents a mutual inductance with coefficient of
  coupling *K*.
- *v*1(*t*) and
  *v*2(*t*)
  represent the voltage across the terminals of the inductors at time
  *t*.
- *i*1(*t*) and
  *i*2(*t*)
  represent the current through the inductors at time *t*.
  The block uses standard dot notation to indicate the direction of positive
  current flow relative to a positive voltage.

RF Blockset current and voltage signals consist of in-phase
(*Ik*) and quadrature (*Qk*)
components at each frequency *fk* specified
in the Configuration block:

i(t)=∑{fk}(iIk(t)+j⋅iQk(t))ej(2πfk)tv(t)=∑{fk}(vIk(t)+j⋅vQk(t))ej(2πfk)t
