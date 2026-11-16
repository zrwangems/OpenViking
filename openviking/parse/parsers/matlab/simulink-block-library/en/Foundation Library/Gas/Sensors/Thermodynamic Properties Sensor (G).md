---
type: simulink-block
title: 'Thermodynamic Properties Sensor (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Sensors'
documentation_page: 'thermodynamicpropertiessensorg'
documentation_source_path: 'ref/thermodynamicpropertiessensorg.html'
language: en
---

# Thermodynamic Properties Sensor (G)

## Ports

### Output

### **h** — Specific enthalpy measurement, kJ/kg physical signal

Physical signal output port for measuring the gas specific enthalpy.

#### Dependencies

To enable this port, select the **Enthalpy**
check box.

### **ρ** — Density measurement, kg/m^3 physical signal

Physical signal output port for measuring the gas density.

#### Dependencies

To enable this port, select the **Density** check
box.

### **cp** — Specific heat at constant pressure measurement, kJ/(kg\*K) physical signal

Physical signal output port for measuring the gas specific heat
at constant pressure.

#### Dependencies

To enable this port, select the **Specific heat**
check box.

### **s** — Specific entropy measurement, kJ/(kg\*K) physical signal

Physical signal output port for measuring the gas specific entropy.

#### Dependencies

To enable this port, select the **Entropy** check
box.
### Conserving

### **A** — Sensor inlet gas

Gas conserving port. Connect this port to the node in the gas
network where you want to measure the thermodynamic properties. All
measurements are taken with respect to absolute zero.

## Parameters

### **Enthalpy** — Control output port visibility for measuring specific enthalpy `Off` (default) | `On`

Selecting this check box exposes the output port **h**,
which lets you measure the gas specific enthalpy.

### **Density** — Control output port visibility for measuring density `On` (default) | `Off`

Selecting this check box exposes the output port **ρ**,
which lets you measure the gas density.

### **Specific heat** — Control output port visibility for measuring specific heat `Off` (default) | `On`

Selecting this check box exposes the output port **cp**,
which lets you measure the gas specific heat.

### **Entropy** — Control output port visibility for measuring specific entropy `Off` (default) | `On`

Selecting this check box exposes the output port **s**,
which lets you measure the gas specific entropy.

### **Specific entropy at reference pressure and temperature** — Reference specific entropy used for sensor calibration 3.8635 kJ/kg/K (default)

The sensor is calibrated so that it outputs this specific entropy value
when port **A** is at reference pressure and
temperature.

#### Dependencies

To enable this parameter, select the **Entropy**
check box.

### **Reference pressure for specific entropy** — Reference pressure used for sensor calibration 0.101325 MPa (default)

The sensor is calibrated so that it outputs the value specified by the
**Specific entropy at reference pressure and
temperature** parameter when port **A** is at
reference pressure and temperature.

#### Dependencies

To enable this parameter, select the **Entropy**
check box.

### **Reference temperature for specific entropy** — Reference temperature used for sensor calibration 293.15 K (default)

The sensor is calibrated so that it outputs the value specified by the
**Specific entropy at reference pressure and
temperature** parameter when port **A** is at
reference pressure and temperature.

#### Dependencies

To enable this parameter, select the **Entropy**
check box.

## Libraries

Simscape / Foundation Library / Gas / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2017a**

### R2023a: Usability enhancement for gas sensors

Gas sensor blocks with multiple output ports now have conditional port visibility
on the block icon. You can use the block parameters to expose only the ports that
you need for measurements in a particular model.

There is no compatibility impact when you use the Thermodynamic
Properties Sensor (G) block in your models. However, if you use
this block in your custom composite components, you need to update the composite
component code.

| Old Syntax | New Syntax |
| --- | --- |
| `sensor = foundation.gas.sensors.thermodynamic_sensor;` | `sensor = foundation.gas.sensors.thermodynamic_sensor(enthalpy=true, specific_heat=true, entropy=true);` |

## Description

Measure specific enthalpy, density, specific heat at constant pressure, and specific entropy

The Thermodynamic Properties Sensor (G) block represents an
ideal sensor that measures specific enthalpy, density, specific heat at constant
pressure, and specific entropy in a gas network. There is no mass or energy flow through
the sensor.

The block measures these thermodynamic properties at the node connected to port
**A**. The first three measurements (specific enthalpy, density,
specific heat at constant pressure) are taken with respect to absolute zero. There is no
universal definition of what constitutes zero entropy, therefore you can use the block
parameters to provide the reference entropy value for sensor calibration.
