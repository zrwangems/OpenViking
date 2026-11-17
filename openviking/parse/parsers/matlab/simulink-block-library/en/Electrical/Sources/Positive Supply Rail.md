---
type: simulink-block
title: 'Positive Supply Rail'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'positivesupplyrail'
documentation_source_path: 'ref/positivesupplyrail.html'
language: en
---

# Positive Supply Rail

## Ports
```yaml
ports:
- name: '-'
  summary: Positive voltage electrical
  direction: conserving
```

### Conserving

### **-** — Positive voltage electrical

Electrical conserving port associated to the positive supply rail
positive voltage.
## Parameters
```yaml
parameters:
- name: Constant voltage
  summary: Constant output voltage 1 V (default)
  group: ''
```

### **Constant voltage** — Constant output voltage `1` `V` (default)

The voltage at the output port relative to the Electrical
Reference block ground port.
## Libraries

Simscape / Electrical / Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Ideal positive supply rail

The Positive Supply Rail block represents an ideal
positive supply rail. Use this block instead of the Simscape™
DC Voltage Source block to define the output voltage
relative to the Simscape
Electrical Reference block that must appear in each
model.

**Note**

Do not attach more than one Positive Supply Rail
block to *any* connected line.
