---
type: simulink-block
title: 'Thermodynamic Properties Sensor (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Sensors'
documentation_page: 'thermodynamicpropertiessensorma'
documentation_source_path: 'ref/thermodynamicpropertiessensorma.html'
language: en
---

# Thermodynamic Properties Sensor (MA)

## Ports

### Output

### **h** — Specific enthalpy measurement, J/kg physical signal

Physical signal output port for measuring the specific enthalpy of the
air mixture.

#### Dependencies

To enable this port, select the **Enthalpy**
check box.

### **ρ** — Density measurement, kg/m^3 physical signal

Physical signal output port for measuring the density of the air
mixture.

#### Dependencies

To enable this port, select the **Density** check
box.

### **cp** — Specific heat at constant pressure measurement, J/(kg\*K) physical signal

Physical signal output port for measuring the specific heat of the air
mixture at constant pressure.

#### Dependencies

To enable this port, select the **Specific heat**
check box.

### **s** — Specific entropy measurement, J/(kg\*K) physical signal

Physical signal output port for measuring the specific entropy of the
air mixture.

#### Dependencies

To enable this port, select the **Entropy** check
box.
### Conserving

### **A** — Sensor inlet moist air

Moist air conserving port. Connect this port to the node in the moist
air network where you want to measure the thermodynamic properties.

## Parameters

### **Measurements based on** — Select measurement convention for sensor output `Unit mass of moist air mixture` (default) | `Unit mass of dry air and trace gas`

Select whether measurements are normalized by the mass of the whole air
mixture, or by the mass of dry air and trace gas only:

- `Unit mass of moist air mixture` —
  For each thermodynamic property, the measured mass of that property
  in a moist air volume is divided by the mass of the most air
  mixture.
- `Unit mass of dry air and trace gas`
  — For each thermodynamic property, the measured mass of that
  property in a moist air volume is divided by the mass of dry air and
  trace gas (leaving out the mass of the water vapor). Use this option
  when you need to compare your measurements with ASHRAE figures and
  charts.

### **Enthalpy** — Control output port visibility for measuring specific enthalpy `Off` (default) | `On`

Selecting this check box exposes the output port **h**,
which lets you measure the specific enthalpy of the air mixture.

### **Enthalpy reference state** — Select reference state for specific enthalpy output `As provided in Moist Air Properties (MA) block` (default) | `0 degC with water as vapor` | `0 degC with water as liquid`

Select the reference state for specific enthalpy output:

- `As provided in Moist Air Properties (MA)
  block` — The sensor outputs mixture enthalpy
  based directly on the enthalpy vectors provided in the
  Moist Air Properties (MA) block,
  with no adjustments. This option is for informational purposes only
  because the library blocks use adjusted values.
- `0 degC with water as vapor` — The
  sensor outputs mixture enthalpy adjusted to reference state of 0
  kJ/kg at 0 degC. These are the values used in the library blocks and
  shown in the simulation data log.
- `0 degC with water as liquid` —
  The sensor outputs mixture enthalpy adjusted so that liquid water
  has the reference state of 0 kJ/kg at 0 degC. In this case, enthalpy
  of water vapor includes the enthalpy of vaporization, or latent
  heat, at the reference state. These are the values used in the wall
  condensation calculations.

#### Dependencies

To enable this parameter, select the **Enthalpy**
check box.

### **Density** — Control output port visibility for measuring density `On` (default) | `Off`

Selecting this check box exposes the output port **ρ**,
which lets you measure the density of the air mixture.

### **Specific heat** — Control output port visibility for measuring specific heat `Off` (default) | `On`

Selecting this check box exposes the output port **cp**,
which lets you measure the specific heat of the air mixture.

### **Entropy** — Control output port visibility for measuring specific entropy `Off` (default) | `On`

Selecting this check box exposes the output port **s**,
which lets you measure the specific entropy of the air mixture.

## Libraries

Simscape / Foundation Library / Moist Air / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2023b: Consistent reference state for specific enthalpy in moist air domain

To ensure consistency in a moist air mixture, all the specific enthalpies must
have the same reference temperature. Therefore, starting in R2023b, the moist air
domain uses a consistent reference temperature of 0 degC. When you enter specific
enthalpy vectors in the Moist Air Properties (MA)
block, the block internally shifts these vectors to be 0 kJ/kg at 0 degC. The
library blocks then use these adjusted values in the internal calculations. The
simulation data log also displays the adjusted specific enthalpy values.

The new **Enthalpy reference state** parameter in the
Thermodynamic Properties Sensor (MA) block lets
you view the specific enthalpy values adjusted with respect to different reference
states. The `As provided in Moist Air Properties (MA)
block` option outputs the same values as in previous
releases.

### R2023a: Usability enhancement for moist air sensors

Moist air sensor blocks with multiple output ports now have conditional port
visibility on the block icon. You can use the block parameters to expose only the
ports that you need for measurements in a particular model.

There is no compatibility impact when you use the Thermodynamic
Properties Sensor (MA) block in your models. However, if you use
this block in your custom composite components, you need to update the composite
component code.

| Old Syntax | New Syntax |
| --- | --- |
| `sensor = foundation.moist_air.sensors.thermodynamic_sensor;` | `sensor = foundation.moist_air.sensors.thermodynamic_sensor(enthalpy=true, specific_heat=true, entropy=true);` |

## Description

Measure specific enthalpy, density, specific heat at constant pressure, and specific entropy of air mixture

The Thermodynamic Properties Sensor (MA) block
represents an ideal sensor that measures specific enthalpy, density, specific heat at
constant pressure, and specific entropy of the air mixture in a moist air network. There
is no mass or energy flow through the sensor.

The block measures these thermodynamic properties at the node connected to port
**A**.

You have a choice of outputting these measurements normalized by the mass of the whole
air mixture, or by the mass of dry air and trace gas only. The second option is
consistent with the American Society of Heating, Refrigerating and Air Conditioning
Engineers (ASHRAE) standards.

The specific entropy reference value, used for sensor calibration, is 0 for each
constituent of the moist mixture at atmospheric pressure and atmospheric temperature.
Atmospheric pressure and atmospheric temperature are defined by the parameters of the
Moist Air Properties (MA) block connected to the
circuit.
