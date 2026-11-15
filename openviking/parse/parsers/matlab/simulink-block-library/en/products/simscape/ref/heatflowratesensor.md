---
type: simulink-block
title: 'Heat Flow Rate Sensor'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Thermal Models / Thermal Sensors'
documentation_page: 'heatflowratesensor'
documentation_source_path: 'ref/heatflowratesensor.html'
language: en
---

# Heat Flow Rate Sensor

## Ports

### Output

### **H** — Heat flow rate measurement, W physical signal

Physical signal output port for heat flow measurement.
### Conserving

### **A** — Sensor inlet thermal

Thermal conserving port. The measurement is positive when the value at port
**A** is greater than the value at port
**B**.

### **B** — Sensor outlet thermal

Thermal conserving port. The measurement is positive when the value at port
**A** is greater than the value at port
**B**.

## Parameters

Not documented in R2025b.

## Libraries

Simscape / Foundation Library / Thermal / Thermal Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007b**

## Description

Ideal heat flow meter

The Heat Flow Rate Sensor block represents an ideal heat
flow meter, that is, a device that converts a heat flow passing through the meter into a
control signal proportional to this flow.

Connect this sensor in series with the block where you want to measure the heat flow
because heat flow is a Through variable (for the thermal domain). Connecting the sensor in
parallel may affect the simulation results because it is analogous to adding a bypass
connection line between the connection points. A series connection within an existing line
does not affect the simulation results and provides an accurate measurement.

Connections **A** and **B** are thermal conserving
ports. Port **H** is a physical signal port that outputs the heat flow
value.

The block positive direction is from port **A** to port
**B**.
