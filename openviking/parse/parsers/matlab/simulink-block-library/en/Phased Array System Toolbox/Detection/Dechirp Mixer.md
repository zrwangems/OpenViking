---
type: simulink-block
title: 'Dechirp Mixer'
family: 'phased'
product_id: 'phased'
product_name: 'Phased Array System Toolbox'
documentation_release: R2025b
official_category: 'Detection'
documentation_page: 'dechirpmixer'
documentation_source_path: 'ref/dechirpmixer.html'
language: en
---

# Dechirp Mixer

## Ports
```yaml
ports:
- name: RefX
  summary: Reference signal complex-valued *M*-by-1 vector
  direction: input
  data_types: single | double
- name: X
  summary: Input signal complex-valued *M*-by-*N* matrix
  direction: input
  data_types: single | double
- name: Port_1
  summary: Dechirped output signal *M*-by-*N* matrix
  direction: output
  data_types: single | double
```

### Input

### **RefX** — Reference signal complex-valued *M*-by-1 vector

Reference signal, specified as a complex-valued
*M*-by-1 vector.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes

### **X** — Input signal complex-valued *M*-by-*N* matrix

Input signal, specified as a complex-valued
*M*-by-*N* matrix. Each column of
`X` is an independent signal and is individually
mixed with the signal input to the `RefX`
port.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
### Output

### **Port\_1** — Dechirped output signal *M*-by-*N* matrix

Dechirped signal, returned as an
*M*-by-*N* matrix. Each column of
the `Port_1` port is the mixed output for the
corresponding column of `X`.

**Data Types:** `single` | `double`
**Complex Number Support:** Yes
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Phased Array System Toolbox / Detection

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Usage notes and limitations:

Does not support variable-size inputs.

## Version History

**Introduced in R2014b**

## Description

Dechirping operation on input signal

The Dechirp block mixes the incoming signal from the `X`
port with a reference signal incoming through the `RefX` port. The
signals can be complex baseband signals. The input signal can be a matrix where each
column is an independent channel. The reference signal is a vector. The reference signal
is complex-conjugated and then multiplied with each signal column to compute the
output.
