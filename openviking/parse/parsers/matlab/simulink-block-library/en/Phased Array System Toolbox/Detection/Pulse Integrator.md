---
type: simulink-block
title: 'Pulse Integrator'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection'
documentation_page: 'pulseintegrator'
documentation_source_path: 'ref/pulseintegrator.html'
language: en
---

# Pulse Integrator

## Ports
```yaml
ports:
- name: x
  summary: Pulse input data matrix
  direction: input
  data_types: double
- name: ∑x
  summary: Integrated pulse column vector
  direction: output
  data_types: double
```

### Input

### **x** — Pulse input data matrix

Pulse input data, specified as a matrix. Each column of
`x` is one pulse.

**Data Types:** `double`
### Output

### **∑x** — Integrated pulse column vector

Integrated pulse, returned as an *N*-by-1 column
vector, where *N* is the number of rows in the input
`x`.

**Data Types:** `double`
## Parameters
```yaml
parameters:
- name: Integration method
  summary: Integration method Coherent (default) | Noncoherent
  group: ''
- name: Number of pulses to integrate
  summary: Number of pulses to integrate 10 (default)
  group: ''
- name: Integration overlap (in pulses)
  summary: Integration overlap 0 (default)
  group: ''
```

### **Integration method** — Integration method `Coherent` (default) | `Noncoherent`

Specify the integration method as `Coherent` or
`Noncoherent`.

### **Number of pulses to integrate** — Number of pulses to integrate `10` (default)

Specify the number of pulses to integrate as an integer.

### **Integration overlap (in pulses)** — Integration overlap `0` (default)

Specify the number of overlapped pulses in successive integrations as an
integer. This number must be less than the value specified in
**Number of pulses to integrate**.
## Libraries

Phased Array System Toolbox / Detection

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014b**

## Description

Coherent or noncoherent pulse integration

The Pulse Integrator block performs coherent or noncoherent integration of
successive pulses of a signal and puts out an integrated output. You can specify how
many pulses to integrate and the number of overlapped pulses in successive
integrations.
