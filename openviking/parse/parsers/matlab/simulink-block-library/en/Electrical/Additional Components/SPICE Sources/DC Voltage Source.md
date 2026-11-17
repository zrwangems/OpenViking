---
type: simulink-block
title: 'DC Voltage Source'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'dcvoltagesource'
documentation_source_path: 'ref/dcvoltagesource.html'
language: en
---

# DC Voltage Source

## Ports
```yaml
ports:
- name: +
  summary: Positive voltage electrical
  direction: conserving
- name: '-'
  summary: Negative voltage electrical
  direction: conserving
```

### Conserving

### **+** — Positive voltage electrical

Electrical conserving port associated with the DC current source
positive voltage

### **-** — Negative voltage electrical

Electrical conserving port associated with the DC current source
negative voltage
## Parameters
```yaml
parameters:
- name: Constant value, DC
  summary: DC output voltage 0 V (default)
  group: ''
```

### **Constant value, DC** — DC output voltage `0` `V` (default)

Value of the DC output voltage, in V.
## Libraries

Simscape / Electrical / Additional Components / SPICE Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Constant voltage source

The DC Voltage Source block represents a constant
voltage source whose output voltage value is independent of the current through the
source.
