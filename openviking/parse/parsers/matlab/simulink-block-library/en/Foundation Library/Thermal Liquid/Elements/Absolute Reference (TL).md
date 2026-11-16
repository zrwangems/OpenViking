---
type: simulink-block
title: 'Absolute Reference (TL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Thermal Liquid / Elements'
documentation_page: 'absolutereferencetl'
documentation_source_path: 'ref/absolutereferencetl.html'
language: en
---

# Absolute Reference (TL)

## Ports

### Conserving

### **A** — Pressure and temperature are zero thermal liquid

Thermal liquid conserving port where the pressure and temperature are both equal
to zero.

## Parameters

Not documented in R2025b.

## Libraries

Simscape / Foundation Library / Thermal Liquid / Elements

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

### R2023a: Absolute Reference (TL) block no longer recommended

The Pressure & Temperature Sensor (TL) block now
contains an implicit reference node, which means that you need only one port to make
absolute measurements of pressure or temperature. Expose the second port only if you need to
measure the difference in pressure or temperature between two nodes in the model.

In previous releases, to measure the absolute pressure and absolute temperature at port
**A**, you needed to connect port **B** to an
Absolute Reference (TL) block. This is no longer necessary
because you can now make absolute measurements by setting the **Measurement
reference** parameter of the Pressure & Temperature Sensor
(TL) block to `Absolute`.

This change has no compatibility impact. Existing models that have an
Absolute Reference (TL) block connected to a
Pressure & Temperature Sensor (TL) block continue to
work as before.

## Description

(Not recommended) Reference point at zero absolute temperature and pressure

The Absolute Reference (TL) block represents an absolute
reference for the pressure and temperature in thermal liquid systems. At port
**A**, the pressure and temperature are both equal to zero.
