---
type: simulink-block
title: 'Thermodynamic Properties Sensor (TL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Thermal Liquid Models / Sensors'
documentation_page: 'thermodynamicpropertiessensortl'
documentation_source_path: 'ref/thermodynamicpropertiessensortl.html'
language: en
---

# Thermodynamic Properties Sensor (TL)

## Ports

### Output

### **u** — Specific internal energy measurement, kJ/kg physical signal

Physical signal output port for measuring the specific internal energy
of thermal liquid.

#### Dependencies

To enable this port, select the **Internal
energy** check box.

### **ρ** — Density measurement, kg/m^3 physical signal

Physical signal output port for measuring the density of thermal
liquid.

#### Dependencies

To enable this port, select the **Density** check
box.

### **cp** — Specific heat at constant pressure measurement, kJ/(kg\*K) physical signal

Physical signal output port for measuring the thermal liquid specific
heat at constant pressure.

#### Dependencies

To enable this port, select the **Specific heat**
check box.
### Conserving

### **A** — Sensor inlet thermal liquid

Thermal liquid conserving port. Connect this port to the node in the
thermal liquid network where you want to measure the thermodynamic
properties. All measurements are taken with respect to absolute
zero.

## Parameters

### **Internal energy** — Control output port visibility for measuring specific internal energy `Off` (default) | `On`

Selecting this check box exposes the output port **u**,
which lets you measure the specific internal energy of thermal
liquid.

### **Density** — Control output port visibility for measuring density `On` (default) | `Off`

Selecting this check box exposes the output port **ρ**,
which lets you measure the thermal liquid density.

### **Specific heat** — Control output port visibility for measuring specific heat `Off` (default) | `On`

Selecting this check box exposes the output port **cp**,
which lets you measure the thermal liquid specific heat at constant
pressure.

## Libraries

Simscape / Foundation Library / Thermal Liquid / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

### R2023a: Usability enhancement for thermal liquid sensors

Thermal liquid sensor blocks with multiple output ports now have conditional port
visibility on the block icon. You can use the block parameters to expose only the
ports that you need for measurements in a particular model.

There is no compatibility impact when you use the Thermodynamic
Properties Sensor (TL) block in your models. However, if you use
this block in your custom composite components, you need to update the composite
component code.

| Old Syntax | New Syntax |
| --- | --- |
| `sensor = foundation.thermal_liquid.sensors.thermodynamic_sensor;` | `sensor = foundation.thermal_liquid.sensors.thermodynamic_sensor(internal_energy=true, specific_heat=true);` |

## Description

Measure specific internal energy, density, and specific heat at constant pressure in thermal liquid networks

The Thermodynamic Properties Sensor (TL) block represents an ideal
sensor that measures specific internal energy, density, and specific heat at constant
pressure in a thermal liquid network. There is no mass or energy flow through the
sensor.

The block measures these thermodynamic properties at the node connected to port
**A**. All measurements are taken with respect to absolute
zero.
