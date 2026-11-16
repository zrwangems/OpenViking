---
type: simulink-block
title: 'Flow Rate Sensor (G)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Gas / Sensors'
documentation_page: 'flowratesensorg'
documentation_source_path: 'ref/flowratesensorg.html'
language: en
---

# Flow Rate Sensor (G)

## Ports

### Output

### **M** — Mass flow rate measurement, kg/s physical signal

Physical signal output port for mass flow rate measurement.

#### Dependencies

To enable this port, select the **Mass flow rate** check
box.

### **V** — Volumetric flow rate, m^3/s physical signal

Physical signal output port for the volumetric flow rate measurement.

#### Dependencies

To enable this port, select the **Volumetric flow rate** check
box.

### **φ** — Energy flow rate measurement, W physical signal

Physical signal output port for energy flow rate measurement.

#### Dependencies

To enable this port, select the **Energy flow rate** check
box.
### Conserving

### **A** — Sensor inlet gas

Gas conserving port. Flow rates are positive if gas flows from port
**A** to port **B**.

### **B** — Sensor outlet gas

Gas conserving port. Flow rates are positive if gas flows from port
**A** to port **B**.

## Parameters

### **Mass flow rate** — Control output port visibility for measuring mass flow rate `On` (default) | `Off`

Selecting this check box exposes the output port **M**, which lets
you measure mass flow rate.

### **Volumetric flow rate** — Control output port visibility for measuring volumetric flow rate `Off` (default) | `On`

Selecting this check box exposes the output port **V**, which lets
you measure volumetric flow rate.

### **Volumetric flow measurement conditions** — Specify conditions for measuring volumetric flow rate `Actual conditions` (default) | `Standard conditions`

Select whether the sensor calculates volumetric flow rate at actual working
conditions or at a standard pressure and temperature:

- `Actual conditions` — The sensor calculates the
  volumetric flow rate by using density at the actual working conditions of the
  system.
- `Standard conditions` — The sensor calculates
  the volumetric flow rate by using density at standard conditions. When you select
  this option, additional parameters become available to let you specify the standard
  pressure and temperature.

#### Dependencies

To enable this parameter, select the **Volumetric flow rate**
check box.

### **Standard pressure** — Gas pressure at standard conditions `0.10132 MPa` (default)

Gas pressure at standard conditions.

#### Dependencies

To enable this parameter, set **Volumetric flow measurement
conditions** to `Standard conditions`.

### **Standard temperature** — Gas temperature at standard conditions `20 degC` (default)

Gas temperature at standard conditions.

#### Dependencies

To enable this parameter, set **Volumetric flow measurement
conditions** to `Standard conditions`.

### **Energy flow rate** — Control output port visibility for measuring energy flow rate `On` (default) | `Off`

Selecting this check box exposes the output port **φ**, which lets
you measure energy flow rate.

## Libraries

Simscape / Foundation Library / Gas / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

### R2023a: Usability enhancement for gas sensors

In R2023a, separate Mass & Energy Flow Rate Sensor (G) and
Volumetric Flow Rate Sensor (G) blocks have been combined into a single
Flow Rate Sensor (G) block that lets you measure mass flow rate, energy
flow rate, and volumetric flow rate. The new block lets you use the block parameters to
expose only the ports that you need for measurements in a particular model, which helps to
reduce clutter and improve the block diagram layout.

This change has no compatibility impact when you use these Foundation library blocks in
your models. When you open an existing model, the Mass & Energy Flow Rate Sensor
(G) and Volumetric Flow Rate Sensor (G) blocks within it are
automatically replaced by Flow Rate Sensor (G) blocks with the appropriate
ports exposed.

However, if you use the Mass & Energy Flow Rate Sensor (G) and
Volumetric Flow Rate Sensor (G) blocks in your custom composite components,
you need to update the composite component code.

| Sensor Block to Update | Old Syntax | New Syntax |
| --- | --- | --- |
| Mass & Energy Flow Rate Sensor (G) | `sensor = foundation.gas.sensors.mass_flow_energy_flow_sensor;` | `sensor = foundation.gas.sensors.flow_sensor;` |
| Volumetric Flow Rate Sensor (G) | `sensor = foundation.gas.sensors.volumetric_flow_sensor;` | `sensor = foundation.gas.sensors.flow_sensor(volumetric_flow_measure=true);` |

Additionally, when the sensor measures volumetric flow rate, you can now select whether
to calculate the volumetric flow rate by using density at standard pressure and temperature
or at the actual working conditions of the system. In previous releases, the
Volumetric Flow Rate Sensor (G) block could only use actual working
conditions. This change has no compatibility impact because the default block behavior is
unchanged.

## Description

Measure mass, energy, and volumetric flow rates in gas networks

The Flow Rate Sensor (G) block represents an ideal sensor
that measures mass flow rate, energy flow rate, and volumetric flow rate in a gas network. The
energy flow rate is the advection of total enthalpy. There is no change in pressure or
temperature across the sensor.

Because the flow rates are Through variables, the block must connect in series with the
component being measured.

The relative orientation of ports **A** and **B**
establishes the measurement sign. The sign is positive if flow occurs from port
**A** to port **B**. Switching port connections reverses
the measurement sign.

Three physical signal ports are available to output the measurement data:

- Port **M** outputs the mass flow rate.
- Port **V** outputs the volumetric flow rate.
- Port **φ** outputs the energy flow rate.

These ports have conditional port visibility on the block icon. Use the block parameters
to expose only the ports that you need for measurements in a particular model.

Connect the measurement ports to PS-Simulink Converter blocks to transform the output physical signals into
Simulink® signals, for example, for plotting or additional data processing.
