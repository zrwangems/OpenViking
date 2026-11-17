---
type: simulink-block
title: 'DC Current Source'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Additional Components / SPICE Sources'
documentation_page: 'dccurrentsource'
documentation_source_path: 'ref/dccurrentsource.html'
language: en
---

# DC Current Source

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
  summary: DC output current 0 A (default)
  group: ''
- name: Include parallel conductance, GMIN
  summary: Whether to include parallel conductance Yes (default) | No
  group: ''
```

### **Constant value, DC** — DC output current `0` `A` (default)

Value of the DC output current, in A.

### **Include parallel conductance, GMIN** — Whether to include parallel conductance `Yes` (default) | `No`

Specify if the current source includes a parallel conductance. The value of the parallel conductance, *GMIN*, depends on whether your model contains an Environment Parameters block.

This table shows the possible values of the parallel conductance,
*GMIN*:

**Values of parallel conductance, GMIN**

| Include parallel conductance, GMIN | | | | |
| --- | --- | --- | --- | --- |
| *`Yes`* | | *`No`* | | |
| **Model contains Environment Parameters block** | **Model does not contain Environment Parameters block** | Parallel conductance, *GMIN*, is not included and it does not affect the current source. | | |
| *GMIN* is equal to the value of the **GMIN** parameter in the Environment Parameters block. | *GMIN* = `1e-12` `Ohm` |
## Libraries

Simscape / Electrical / Additional Components / SPICE Sources

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Constant current source

The DC Current Source block represents a constant
current source whose output current value is independent of the voltage across its
terminals.

The block uses a small conductance internally to prevent numerical simulation issues.
The conductance connects the + and - ports of the device and has a conductance
*GMIN*:

- By default, *GMIN* matches the **GMIN**
  parameter of the Environment Parameters
  block, whose default value is 1e–12.
- To change *GMIN*, add an Environment
  Parameters block to your model and set the
  **GMIN** parameter to the desired value.
