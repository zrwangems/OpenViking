---
type: simulink-block
title: 'Liquid Properties Sensor (IL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Isothermal Liquid Models / Sensors'
documentation_page: 'liquidpropertiessensoril'
documentation_source_path: 'ref/liquidpropertiessensoril.html'
language: en
---

# Liquid Properties Sensor (IL)

## Ports

### Output

### **rho** — Density measurement, kg/m^3 physical signal

Physical signal output port for measuring the density of isothermal liquid
mixture.

#### Dependencies

To enable this port, select the **Density** check box.

### **beta** — Isothermal bulk modulus measurement, Pa physical signal

Physical signal output port for measuring the bulk modulus of isothermal liquid
mixture.

#### Dependencies

To enable this port, select the **Isothermal bulk modulus**
check box.

### **theta** — Fraction of entrained air measurement, unitless physical signal

Physical signal output port for measuring the fraction of entrained (undissloved)
air, (*entrained air*)/(*entrained air* +
*dissolved air*). Value of 1 means no air is dissolved. Value of 0
means all air is dissolved.

#### Dependencies

To enable this port, select the **Fraction of air that is
entrained** check box.
### Conserving

### **A** — Sensor inlet isothermal liquid

Isothermal liquid conserving port. Connect this port to the node in the isothermal
liquid network where you want to measure the liquid properties. All measurements are
taken with respect to absolute zero.

## Parameters

### **Density** — Control output port visibility to measure density `On` (default) | `Off`

Select this check box to expose output port **rho**, which lets you
measure fluid density.

### **Isothermal bulk modulus** — Control output port visibility to measure bulk modulus `Off` (default) | `On`

Select this check box to expose output port **beta**, which lets
you measure bulk modulus.

### **Fraction of air that is entrained** — Control output port visibility to measure fraction of air that is entrained `Off` (default) | `On`

Select this check box to expose output port **theta**, which lets
you measure the fraction of undissolved air.

## Libraries

Simscape / Foundation Library / Isothermal Liquid / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2020a**

## Description

Measure density, bulk modulus, and fraction of entrained air in isothermal liquid network

The Liquid Properties Sensor (IL) block represents an ideal
sensor that lets you measure mixture density, bulk modulus, and fraction of entrained air in
an isothermal liquid network. There is no mass flow through the sensor.

The block measures these properties at the node connected to port **A**.
All measurements are taken with respect to absolute zero.
