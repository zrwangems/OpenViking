---
type: simulink-block
title: 'Environment Parameters'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Utilities'
documentation_page: 'environmentparameters'
documentation_source_path: 'ref/environmentparameters.html'
language: en
---

# Environment Parameters

## Ports
```yaml
ports:
- name: OUT
  summary: Output port electrical
  direction: conserving
```

### Conserving

### **OUT** — Output port electrical

Electrical conserving port associated with the environment parameters
output.
## Parameters
```yaml
parameters:
- name: Temperature
  summary: SPICE temperature 300.15 K (default) | positive scalar
  group: ''
- name: GMIN
  summary: Minimum conductance 1e-12 1/Ohm (default) | positive scalar
  group: ''
```

### **Temperature** — SPICE temperature `300.15` `K` (default) | positive scalar

Temperature of the connected SPICE-compatible blocks.

### **GMIN** — Minimum conductance `1e-12` `1/Ohm` (default) | positive scalar

Minimum conductance for applicable connected SPICE-compatible
blocks.
## Libraries

Simscape / Electrical / Utilities

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2008a**

## Description

Set parameters that apply to all connected SPICE-compatible blocks

The Environment Parameters block lets you set
parameters that apply to all SPICE-compatible blocks in an electrical network:

- Circuit temperature
- Minimum conductance

If your model does not contain an Environment
Parameters block, all blocks use the default values of these
parameters. To override the default values, connect every network in the system to an
Environment Parameters block.

**Note**

The simple semiconductor models in the Semiconductors sublibrary are not
temperature dependent, so the Environment Parameters
block only changes the minimum conductance parameter used by the exponential diode
and bipolar transistor models.
