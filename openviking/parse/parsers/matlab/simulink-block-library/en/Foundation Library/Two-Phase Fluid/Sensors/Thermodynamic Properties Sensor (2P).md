---
type: simulink-block
title: 'Thermodynamic Properties Sensor (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Sensors'
documentation_page: 'thermodynamicpropertiessensor2p'
documentation_source_path: 'ref/thermodynamicpropertiessensor2p.html'
language: en
---

# Thermodynamic Properties Sensor (2P)

## Ports

### Output

### **T** — Temperature measurement, K physical signal

Physical signal output port for measuring the temperature of two-phase fluid.

#### Dependencies

To enable this port, select the **Temperature** check
box.

### **h** — Specific enthalpy measurement, kJ/kg physical signal

Physical signal output port for measuring the specific enthalpy of two-phase
fluid.

#### Dependencies

To enable this port, select the **Enthalpy** check box.

### **ρ** — Density measurement, kg/m^3 physical signal

Physical signal output port for measuring the density of two-phase fluid.

#### Dependencies

To enable this port, select the **Density** check box.

### **v** — Specific volume measurement, m^3/kg physical signal

Physical signal output port for measuring the specific volume of two-phase fluid.

#### Dependencies

To enable this port, select the **Specific volume** check
box.

### **s** — Specific entropy measurement, kJ/(kg\*K) physical signal

Physical signal output port for measuring the specific entropy of two-phase fluid.

#### Dependencies

To enable this port, select the **Entropy** check box.
### Conserving

### **A** — Sensor inlet two-phase fluid

Two-phase fluid conserving port. Connect this port to the node in the two-phase
fluid network where you want to measure the thermodynamic properties. All measurements
are taken with respect to absolute zero.

## Parameters

### **Temperature** — Control output port visibility for measuring temperature `Off` (default) | `On`

Selecting this check box exposes the output port **T**, which lets
you measure the temperature of two-phase fluid.

### **Enthalpy** — Control output port visibility for measuring specific enthalpy `Off` (default) | `On`

Selecting this check box exposes the output port **h**, which lets
you measure the specific enthalpy of two-phase fluid.

### **Density** — Control output port visibility for measuring density `On` (default) | `Off`

Selecting this check box exposes the output port **ρ**, which lets
you measure the density of two-phase fluid.

### **Specific volume** — Control output port visibility for measuring specific volume `Off` (default) | `On`

Selecting this check box exposes the output port **v**, which lets
you measure the specific volume of two-phase fluid.

### **Entropy** — Control output port visibility for measuring specific entropy `Off` (default) | `On`

Selecting this check box exposes the output port **s**, which lets
you measure the specific entropy of two-phase fluid.

## Libraries

Simscape / Foundation Library / Two-Phase Fluid / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2015b**

### R2023a: Usability enhancement for two-phase fluid sensors

The Thermodynamic Properties Sensor (2P) block can now also measure
density.

The block ports now have conditional visibility on the block icon. You can use the block
parameters to expose only the ports that you need for measurements in a particular model.

There is no compatibility impact when you use the Thermodynamic
Properties Sensor (2P) block in your models. However, if you use this
block in your custom composite components, you need to update the composite component code.

| Old Syntax | New Syntax |
| --- | --- |
| `sensor = foundation.two_phase_fluid.sensors.thermodynamic_sensor;` | `sensor = foundation.two_phase_fluid.sensors.thermodynamic_sensor(temperature=true, enthalpy=true, specific_volume=true, entropy=true);` |

## Description

Measure temperature, density, specific enthalpy, specific entropy, and specific volume in two-phase fluid networks

The Thermodynamic Properties Sensor (2P) block represents an ideal sensor
that measures temperature, density, specific enthalpy, specific entropy, and specific volume
in a two-phase fluid network. There is no mass or energy flow through the sensor.

The block measures these thermodynamic properties at the node connected to port
**A**. All measurements are taken with respect to absolute zero.
