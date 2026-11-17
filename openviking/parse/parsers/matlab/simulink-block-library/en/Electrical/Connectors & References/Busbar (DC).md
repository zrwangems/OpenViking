---
type: simulink-block
title: 'Busbar (DC)'
family: 'sps'
product_id: 'sps'
product_name: 'Electrical'
documentation_release: R2025b
official_category: 'Connectors & References'
documentation_page: 'busbardc'
documentation_source_path: 'ref/busbardc.html'
language: en
---

# Busbar (DC)

## Ports
```yaml
ports:
- name: Vt
  summary: Voltage, V physical signal
  direction: output
- name: P
  summary: Power, W physical signal
  direction: output
- name: 1+
  summary: Positive connection 1 electrical
  direction: conserving
- name: 2+
  summary: Positive connection 2 electrical
  direction: conserving
- name: 3+
  summary: Positive connection 3 electrical
  direction: conserving
- name: 4+
  summary: Positive connection 4 electrical
  direction: conserving
- name: 1-
  summary: Negative connection 1 electrical
  direction: conserving
- name: 2-
  summary: Negative connection 2 electrical
  direction: conserving
- name: 3-
  summary: Negative connection 3 electrical
  direction: conserving
- name: 4-
  summary: Negative connection 4 electrical
  direction: conserving
```

### Output

### **Vt** — Voltage, V physical signal

Physical signal port associated with the per-unit voltage measurement,
in Volts.

#### Dependencies

To enable this port, in the **Parameters**
settings, set the **Measurements ports** parameter
to `Yes`.

### **P** — Power, W physical signal

Physical signal port associated with the power measurement, in
watts.

#### Dependencies

To enable this port, in the **Parameters**
settings, set the **Measurements ports** parameter
to `Yes` and the **Number of
connections** parameter to
`2`, `3`, or
`4`.
### Conserving

### **1+** — Positive connection 1 electrical

Electrical conserving port associated with the first positive
connection.

### **2+** — Positive connection 2 electrical

Electrical conserving port associated with the second positive
connection.

#### Dependencies

To enable this port, in the **Parameters**
settings, set the **Number of connections**
parameter to `2`,
`3`, or
`4`.

### **3+** — Positive connection 3 electrical

Electrical conserving port associated with the third positive
connection.

#### Dependencies

To enable this port, in the **Parameters**
settings, set the **Number of connections**
parameter to `3` or
`4`.

### **4+** — Positive connection 4 electrical

Electrical conserving port associated with the fourth positive
connection.

#### Dependencies

To enable this port, in the **Parameters**
settings, set the **Number of connections**
parameter to `4`.

### **1-** — Negative connection 1 electrical

Electrical conserving port associated with the first negative
connection.

### **2-** — Negative connection 2 electrical

Electrical conserving port associated with the second negative
connection.

#### Dependencies

To enable this port, in the **Parameters**
settings, set the **Number of connections**
parameter to `2`,
`3`, or
`4`.

### **3-** — Negative connection 3 electrical

Electrical conserving port associated with the third negative
connection.

#### Dependencies

To enable this port, in the **Parameters**
settings, set the **Number of connections**
parameter to `3` or
`4`.

### **4-** — Negative connection 4 electrical

Electrical conserving port associated with the fourth negative
connection.

#### Dependencies

To enable this port, in the **Parameters**
settings, set the **Number of connections**
parameter to `4`.
## Parameters
```yaml
parameters:
- name: Number of connections
  summary: Number of port connections 2 (default) | 1 | 3 | 4
  group: ''
- name: Rated DC voltage
  summary: Busbar rated DC voltage 1e3 V (default) | positive scalar
  group: ''
- name: Measurement type
  summary: Measurement type Instantaneous (default) | Average over a specified period
  group: ''
- name: Averaging period
  summary: Averaging period of measurement 1e-2 s (default) | positive scalar
  group: ''
- name: Measurement ports
  summary: Measurement port exposure No (default) | Yes
  group: ''
```

### **Number of connections** — Number of port connections `2` (default) | `1` | `3` | `4`

Number of port connections to expose on the block.

### **Rated DC voltage** — Busbar rated DC voltage `1e3` `V` (default) | positive scalar

Rated DC voltage of the busbar. This block uses this value to scale the
per-unit voltage value.

### **Measurement type** — Measurement type `Instantaneous` (default) | `Average over a specified period`

Type of measurement. In time simulation mode, you can set this parameter
to either `Instantaneous` or `Average
over a specified period`. In frequency-time simulation
mode, you must set this parameter to
`Instantaneous`.

### **Averaging period** — Averaging period of measurement `1e-2` `s` (default) | positive scalar

Period over which the voltage and power values are averaged.

#### Dependencies

To enable this parameter, set **Measurement type** to
`Average over a specified period`.

### **Measurement ports** — Measurement port exposure `No` (default) | `Yes`

Whether to expose the **Vt** and **P**
physical signal output measurement ports.
## Libraries

Simscape / Electrical / Connectors & References

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022a**

## Description

Load flow analysis DC busbar connector

The Busbar (DC) block is a DC connector for load-flow
analysis. You can use this block with Simscape™
Electrical™ DC networks that are configured to run in time or frequency-time
simulation mode. You can view the voltage and power values by enabling simulation data
logging or by exposing the optional measurement ports on the block. For more information
about data logging, see About Simscape Data Logging.
