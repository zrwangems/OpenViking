---
type: simulink-block
title: 'Three-Winding Transformer'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'threewindingtransformer'
documentation_source_path: 'ref/threewindingtransformer.html'
language: en
---

# Three-Winding Transformer

## Ports

Not documented in R2025b.

## Parameters

### **Inductance L1** — Inductance value of first inductor `1e-6 H` (default) | nonnegative scalar integer

Inductance value of the first inductor, specified as a nonnegative scalar
integer in henries. Specify the units of the inductance from the
corresponding drop-down menu.

**Data Types:** `double`

### **Inductance L2** — Inductance value of second inductor `1e-6 H` (default) | nonnegative scalar integer

Inductance value of the second inductor, specified as a nonnegative scalar
integer in henries. Specify the units of the inductance from the
corresponding drop-down menu.

**Data Types:** `double`

### **Inductance L3** — Inductance value of third inductor `1e-6 H` (default) | nonnegative scalar integer

Inductance value of the third inductor, specified as a nonnegative scalar
integer in henries. Specify the units of the inductance from the
corresponding drop-down menu.

**Data Types:** `double`

### **Inductance L3** — Inductance value of third inductor `1e-6 H` (default) | nonnegative scalar integer

Inductance value of the third inductor, specified as a nonnegative scalar
integer in henries. Specify the units of the inductance from the
corresponding drop-down menu.

**Data Types:** `double`

### **Coefficient of coupling K12** — Coupling coefficient of first and second inductors `0.9` (default) | nonnegative scalar integer

Coupling coefficient for the mutual inductance of the first and second
inductors, specified as a nonnegative scalar integer between
`0` and `1`

**Data Types:** `double`

### **Coefficient of coupling K13** — Coupling coefficient of first and third inductors `0.9` (default) | nonnegative scalar integer

Coupling coefficient for the mutual inductance of the first and third
inductors, specified as a nonnegative scalar integer between
`0` and `1`

**Data Types:** `double`

### **Coefficient of coupling K23** — Coupling coefficient of second and third inductors `0.9` (default) | nonnegative scalar integer

Coupling coefficient for the mutual inductance of the second and third
inductors, specified as a nonnegative scalar integer between
`0` and `1`

**Data Types:** `double`

**Note**

The minimum nonzero inductance value that the RF Blockset environment
recognizes is `1e-18` `H`. During simulation, the block
uses a value of `1e-18` `H` for any inductance and mutual
inductance values specified between `0` and `1e-18` `H`.

## Libraries

RF Blockset / Circuit Envelope / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced before R2006a**

## Description

Compute sum of RF signals

The Three-Winding Transformer block models three coupled inductors
within the circuit envelope simulation environment.

The block implements the relations

v1(t)=L1ddt[i1(t)]+M12ddt[i2(t)]+M13ddt[i3(t)]v2(t)=M12ddt[i1(t)]+L2ddt[i2(t)]+M23ddt[i3(t)]v3(t)=M13ddt[i1(t)]+M23ddt[i2(t)]+L3ddt[i3(t)]Mpq=KpqLpLq

where:

- *L*1,
  *L*2, and
  *L*3 represent
  inductances.
- *Mpq* represents the mutual
  inductance between the *p*th and *q*th
  inductors, with coefficient of coupling
  *Kpq*.
- *v*1(*t*),
  *v*2(*t*), and
  *v*3(*t*)
  represent the voltage across the terminals of the inductors at time
  *t*.
- *i*1(*t*),
  *i*2(*t*), and
  *i*3(*t*)
  represent the current through the inductors at time *t*.
  The block uses standard dot notation to indicate the direction of positive
  current flow relative to a positive voltage.

RF Blockset™ current and voltage signals consist of in-phase
(*Ik*) and quadrature (*Qk*)
components at each frequency *fk* specified
in the Configuration block:

i(t)=∑{fk}(iIk(t)+j⋅iQk(t))ej(2πfk)tv(t)=∑{fk}(vIk(t)+j⋅vQk(t))ej(2πfk)t
