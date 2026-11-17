---
type: simulink-block
title: 'Heat Flow Rate Source'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal / Thermal Sources'
documentation_page: 'heatflowratesource'
documentation_source_path: 'ref/heatflowratesource.html'
language: en
---

# Heat Flow Rate Source

## Ports
```yaml
ports:
- name: A
  summary: Source inlet thermal
  direction: conserving
- name: B
  summary: Source outlet thermal
  direction: conserving
```

### Conserving

### **A** — Source inlet thermal

Thermal conserving port associated with the source inlet.

### **B** — Source outlet thermal

Thermal conserving port associated with the source outlet.
## Parameters
```yaml
parameters:
- name: Heat flow rate
  summary: Heat flow rate through the source 0 W (default)
  group: ''
```

### **Heat flow rate** — Heat flow rate through the source 0 W (default)

Constant Heat flow rate through the source. Positive heat flow rate flows
from port A to port B.
## Libraries

Simscape / Foundation Library / Thermal / Thermal Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017b**

## Description

Constant source of thermal energy, characterized by heat flow

The Heat Flow Rate Source block represents an ideal source of thermal
energy that is powerful enough to maintain specified heat flow at its outlet regardless
of the temperature difference across the source.

The source generates constant heat flow rate, defined by the **Heat flow
rate** parameter value.
