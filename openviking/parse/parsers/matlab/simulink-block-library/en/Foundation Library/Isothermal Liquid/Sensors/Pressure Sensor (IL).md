---
type: simulink-block
title: 'Pressure Sensor (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Isothermal Liquid / Sensors'
documentation_page: 'pressuresensoril'
documentation_source_path: 'ref/pressuresensoril.html'
language: en
---

# Pressure Sensor (IL)

## Ports

### Output

### **P** — Pressure difference measurement, Pa physical signal

Physical signal output port for the pressure difference measurement.

#### Dependencies

This port is visible if you set the **Pressure Measurements**
parameter to `Pressure difference`.

### **Pa** — Absolute pressure measurement, in Pascal (Pa) physical signal

Physical signal output port for the absolute pressure measurement.

#### Dependencies

This port is visible if you set the **Pressure Measurements**
parameter to `Absolute pressure`.

### **Pg** — Gauge pressure measurement, Pa physical signal

Physical signal output port for the gauge pressure measurement.

#### Dependencies

This port is visible if you set the **Pressure Measurements**
parameter to `Gauge pressure`.
### Conserving

### **A** — Sensor inlet isothermal liquid

Isothermal liquid conserving port.

### **B** — Sensor outlet isothermal liquid

Isothermal liquid conserving port.

#### Dependencies

This port is visible if you set the **Pressure Measurements**
parameter to `Pressure difference`.

## Parameters

### **Pressure Measurements** — Select whether the sensor measures pressure difference, absolute pressure, or gauge pressure `Pressure difference` (default) | `Absolute pressure` | `Gauge pressure`

Select the type of measurements:

- `Pressure difference` — The sensors measures the
  pressure difference across the sensor. Selecting this option exposes the physical
  signal output port **P** and the second isothermal liquid port
  **B**. The measurement is positive when the value at port
  **A** is greater than the value at port
  **B**.
- `Absolute pressure` — The sensors measures the
  absolute pressure at port **A**. Selecting this option exposes the
  physical signal output port **Pa**.
- `Gauge pressure` — The sensors measures the
  gauge pressure at port **A**. Selecting this option exposes the
  physical signal output port **Pg**.

## Libraries

Simscape / Foundation Library / Isothermal Liquid / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Measure pressure differences, absolute pressure, or gauge pressure

The Pressure Sensor (IL) block represents an ideal sensor
that measures pressure in an isothermal liquid network. There is no mass flow through the
sensor.

The **Pressure Measurements** parameter controls the measurement type and
sensor configuration:

- `Pressure difference` — The physical signal port
  **P** reports the pressure difference across the sensor:

  P=pA−pB,

  where *p*A and
  *p*B are pressures at the sensor ports. The
  measurement is positive when the value at port **A** is greater than the
  value at port **B**.
- `Absolute pressure` — The physical signal port
  **Pa** reports the absolute pressure at port
  **A**:

  Pa=pA,

  where *p*A is pressure at port
  **A**, measured with respect to absolute zero. In this configuration,
  the sensor has only one isothermal liquid port.
- `Gauge pressure` — The physical signal port
  **Pg** reports the gauge pressure at port **A**:

  Pg=pA−patm,

  where *p*A is pressure at port
  **A**, measured with respect to absolute zero, and
  *p*atm is the atmospheric pressure specified by
  the Isothermal Liquid Properties (IL) block connected to
  the circuit. In this configuration, the sensor has only one isothermal liquid port.

The block icon changes depending on the value of the **Pressure
Measurements** parameter.

| Pressure Measurements | Block Icon |
| --- | --- |
| `Pressure difference` |  |
| `Absolute pressure` |  |
| `Gauge pressure` |  |
