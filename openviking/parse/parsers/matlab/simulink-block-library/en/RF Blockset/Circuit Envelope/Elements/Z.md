---
type: simulink-block
title: 'Impedance'
family: 'simrf'
product_id: 'simrf'
product_name: 'RF Blockset'
documentation_release: R2025b
official_category: 'Circuit Envelope / Elements'
documentation_page: 'impedance'
documentation_source_path: 'ref/impedance.html'
language: en
---

# Impedance

## Ports
```yaml
ports: []
```

Not documented in R2025b.
## Parameters
```yaml
parameters:
- name: Impedance type
  summary: Frequency dependency Frequency independent (default) | Frequency dependent
  group: ''
- name: Complex impedance (Ohm)
  summary: Impedance value 50 (default) | scalar complex number | vector of complex numbers
  group: ''
- name: Frequency
  summary: Frequency values for frequency dependent impedance 1e9 (default) | nonnegative scalar number | nonnegative vector
    numbers
  group: ''
```

### **Impedance type** — Frequency dependency `Frequency independent` (default) | `Frequency dependent`

Frequency dependency for the impedance, specified as
`Frequency independent` or
`Frequency dependent`.

Choose `Frequency independent` to apply the same
impedance for all frequencies. Choose `Frequency
dependent` to apply the impedance as a piecewise linear
function.

**Data Types:** `double`

### **Complex impedance (Ohm)** — Impedance value `50` (default) | scalar complex number | vector of complex numbers

Impedance value, specified as a scalar complex number in ohms or a vector
for complex numbers with each element unit in ohms.

When **Impedance type** is set to `Frequency
independent`, impedance is a scalar complex number that is
applied to all simulation frequencies. When **Impedance
type** is set to `Frequency
dependent`, impedance is a vector of complex numbers, [*Z*1,
*Z*2,
*Z*3, …]. This vector is linearly interpolated for all simulation
frequencies.

**Data Types:** `double`

### **Frequency** — Frequency values for frequency dependent impedance `1e9` (default) | nonnegative scalar number | nonnegative vector numbers

Frequency values for frequency dependent impedance, specified as a
nonnegative scalar number in Hz or nonnegative vector number with each
element unit in Hz.

When **Impedance type** is set to `Frequency
dependent`, you can specify a vector of nonnegative
frequencies, [*f*1,
*f*2,
*f*3, …]. The pairs, *f*i,
*Z*i, define a piecewise linear function, *Z*(*f*), that is linearly interpolated for the simulation
frequencies. For values outside the range, there is constant
extrapolation.

**Data Types:** `double`
## Libraries

RF Blockset / Circuit Envelope / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2010b**

### R2021b: Impedance block icon updated

Starting in R2021b, the Impedance block icon has updated. When you
open a model created before R2021b containing an Impedance block, the
software replaces the block icon with the R2021b version.

## Description

Model complex impedance

The Impedance block implements the relation, *v*k(*t*) =
*Z*(*f*k)\**i*k(*t*), for each simulation frequency, *f*k, where:

- *Z*(*f*k) represents complex-valued impedance at a specified
  simulation frequency.
- *v*k(*t*) represents the voltage across the terminals of the element
  at time *t*.
- *i*k(*t*) represents the current through the element at time
  *t*.

Circuit envelope current and voltage signals comprise in-phase,
*Ik*, and quadrature,
*Qk*, components at each frequency,
*fk*.

Frequency-dependent impedance typically cannot be realized as a physical network such
as an RLC chain. You can, however, use the Impedance block to model
nonphysical behavior, such as frequency-independent negative capacitance or negative
inductance. You can also use this block to specify resonant frequency offsets in filter
networks.
