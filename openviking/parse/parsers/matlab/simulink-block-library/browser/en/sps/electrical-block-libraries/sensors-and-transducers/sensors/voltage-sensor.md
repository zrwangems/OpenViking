---
type: simulink-block
title: 'Voltage Sensor'
family: 'sps'
product_id: 'sps'
product_name: 'Simscape Electrical'
documentation_release: R2025b
official_category: 'Electrical Block Libraries / Sensors and Transducers / Sensors'
documentation_page: 'voltagesensor'
documentation_source_path: '../simscape/ref/voltagesensor.html'
language: en
---

# Voltage Sensor

## Ports

### Output

### **V** — Voltage, V physical signal

Physical signal output port for the voltage measurement.
### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the sensor positive terminal.

### **-** — Negative terminal electrical

Electrical conserving port associated with the sensor negative terminal.

## Parameters

Not documented in R2025b.

## Libraries

Simscape / Foundation Library / Electrical / Electrical Sensors Simscape / Electrical / Sensors & Transducers

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2007a**

## Description

Voltage sensor in electrical systems

The Voltage Sensor block represents an ideal voltage
sensor, that is, a device that converts voltage measured between two points of an electrical
circuit into a physical signal proportional to the voltage.

Use the **+** and **-** ports to connect the sensor in
parallel with the block (or several blocks) where you want to measure the voltage. Port
**V** outputs the measurement result as a physical signal. Use a PS-Simulink Converter block to connect this port to Simulink® blocks, such as Scope or Display.
