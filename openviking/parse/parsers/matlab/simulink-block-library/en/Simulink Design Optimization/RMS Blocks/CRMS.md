---
type: simulink-block
title: 'CRMS'
family: 'sldo'
product_id: 'sldo'
product_name: 'Simulink Design Optimization'
documentation_release: R2025b
official_category: 'RMS Blocks'
documentation_page: 'crms'
documentation_source_path: 'ref/crms.html'
language: en
---

# CRMS

## Ports
```yaml
ports:
- name: Port_1
  summary: Input signal scalar
  direction: input
- name: Port_1
  summary: CRMS value scalar
  direction: output
```

### Input

### **Port\_1** — Input signal scalar

Input value, specified as a scalar signal.
### Output

### **Port\_1** — CRMS value scalar

Computed continuous-time, root mean square value, output as a scalar
signal.
## Parameters
```yaml
parameters: []
```

Not documented in R2025b.
## Libraries

Simulink Design Optimization / RMS Blocks

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code.

## Version History

**Introduced in R2009a**

## Description

Compute continuous-time, cumulative root mean square of signal

Attach the CRMS block to a signal to compute its continuous-time,
cumulative root mean square (CRMS) value, which provides a measure of the average energy in a
signal.

The continuous-time, cumulative root mean square value of a signal
*u*(*t*) is defined as

CRMS=1T∫0T‖u(t)‖2dt

To optimize the signal energy, use this block in conjunction with the Check Custom
Bounds block.
