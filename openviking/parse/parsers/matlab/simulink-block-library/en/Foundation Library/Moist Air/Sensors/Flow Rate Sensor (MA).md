---
type: simulink-block
title: 'Flow Rate Sensor (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Moist Air / Sensors'
documentation_page: 'flowratesensorma'
documentation_source_path: 'ref/flowratesensorma.html'
language: en
---

# Flow Rate Sensor (MA)

## Ports

### Output

### **M** — Mixture mass flow rate, kg/s physical signal

Physical signal output port for the mixture mass flow rate measurement.

#### Dependencies

To enable this port, select the **Mass flow rate** check
box.

### **V** — Mixture volumetric flow rate, m^3/s physical signal

Physical signal output port for the mixture volumetric flow rate measurement.

#### Dependencies

To enable this port, select the **Volumetric flow rate** check
box.

### **φ** — Mixture energy flow rate, W physical signal

Physical signal output port for the mixture energy flow rate measurement.

### **Mw** — Water vapor mass flow rate, kg/s physical signal

Physical signal output port for the water vapor mass flow rate measurement.

#### Dependencies

To enable this port, select the **Water vapor mass flow rate**
check box.

### **Mg** — Trace gas mass flow rate, kg/s physical signal

Physical signal output port for the trace gas mass flow rate measurement.

#### Dependencies

To enable this port, select the **Trace gas mass flow rate**
check box.

### **Md** — Water droplet mass flow rate, kg/s physical signal

Physical signal output port for the water droplets mass flow rate, in kg/s.

#### Dependencies

To enable this port, select the **Water droplets mass flow
rate** check box.
### Conserving

### **A** — Sensor inlet moist air

Moist air conserving port. Flow rates are positive if air flows from port
**A** to port **B**.

### **B** — Sensor outlet moist air

Moist air conserving port. Flow rates are positive if air flows from port
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
conditions or at a standard pressure, temperature, and relative humidity:

- `Actual conditions` — The sensor calculates the
  volumetric flow rate by using the moist air density at the actual working conditions
  of the system.
- `Standard conditions` — The sensor calculates
  the volumetric flow rate by using the moist air density at standard conditions. When
  you select this option, additional parameters become available to let you specify
  the standard pressure, temperature, and relative humidity.

#### Dependencies

To enable this parameter, select the **Volumetric flow rate**
check box.

### **Standard pressure** — Moist air pressure at standard conditions `0.10132 MPa` (default)

Moist air pressure at standard conditions.

#### Dependencies

To enable this parameter, set **Volumetric flow measurement
conditions** to `Standard conditions`.

### **Standard temperature** — Moist air temperature at standard conditions `20 degC` (default)

Moist air temperature at standard conditions.

#### Dependencies

To enable this parameter, set **Volumetric flow measurement
conditions** to `Standard conditions`.

### **Standard relative humidity** — Moist air relative humidity at standard conditions `0.65` (default)

Moist air relative humidity at standard conditions.

#### Dependencies

To enable this parameter, set **Volumetric flow measurement
conditions** to `Standard conditions`.

### **Energy flow rate** — Control output port visibility for measuring energy flow rate `On` (default) | `Off`

Selecting this check box exposes the output port **φ**, which lets
you measure energy flow rate.

### **Water vapor mass flow rate** — Control output port visibility for measuring water vapor mass flow rate `On` (default) | `Off`

Selecting this check box exposes the output port **Mw**, which lets
you measure water vapor mass flow rate.

### **Trace gas mass flow rate** — Control output port visibility for measuring trace gas mass flow rate `On` (default) | `Off`

Selecting this check box exposes the output port **Mg**, which lets
you measure trace gas mass flow rate.

### **Water droplets mass flow rate** — Control output port visibility for measuring water droplets mass flow rate `Off` (default) | `On`

Selecting this check box exposes the output port **Md**, which lets
you measure the water droplets mass flow rate.

## Libraries

Simscape / Foundation Library / Moist Air / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

### R2024b: Model water droplets suspended in moist air flow

Blocks in the moist air domain can now model water droplets suspended in a moist air flow. To model water droplets, select **Enable entrained water droplets** in the Moist Air Properties (MA) block connected to your moist air network.

### R2023a: Usability enhancement for moist air sensors

In R2023a, separate Mass & Energy Flow Rate Sensor (MA) and
Volumetric Flow Rate Sensor (MA) blocks have been combined into a single
Flow Rate Sensor (MA) block that lets you measure mass flow rate, energy
flow rate, and volumetric flow rate. The new block lets you use the block parameters to
expose only the ports that you need for measurements in a particular model, which helps to
reduce clutter and improve the block diagram layout.

This change has no compatibility impact when you use these Foundation library blocks in
your models. When you open an existing model, the Mass & Energy Flow Rate Sensor
(MA) and Volumetric Flow Rate Sensor (MA) blocks within it are
automatically replaced by Flow Rate Sensor (G) blocks with the appropriate
ports exposed.

However, if you use the Mass & Energy Flow Rate Sensor (MA) and
Volumetric Flow Rate Sensor (MA) blocks in your custom composite
components, you need to update the composite component code.

| Sensor Block to Update | Old Syntax | New Syntax |
| --- | --- | --- |
| Mass & Energy Flow Rate Sensor (MA) | `sensor = foundation.moist_air.sensors.mass_flow_energy_flow_sensor;` | `sensor = foundation.moist_air.sensors.flow_sensor;` |
| Volumetric Flow Rate Sensor (MA) | `sensor = foundation.moist_air.sensors.volumetric_flow_sensor;` | `sensor = foundation.moist_air.sensors.flow_sensor(volumetric_flow_measure=true);` |

## Description

Measure mass, energy, and volumetric flow rates in moist air networks

The Flow Rate Sensor (MA) block represents an ideal sensor
that measures mass flow rate, energy flow rate, and volumetric flow rate in a moist air
network. There is no change in pressure, temperature, specific humidity, or trace gas mass
fraction across the sensor.

Because the flow rates are Through variables, the block must connect in series with the
component being measured.

The relative orientation of ports **A** and **B**
establishes the measurement sign. The sign is positive if flow occurs from port
**A** to port **B**. Switching port connections reverses
the measurement sign.

Five physical signal ports are available to output the measurement data:

- Port **M** outputs the mass flow rate.
- Port **V** outputs the volumetric flow rate.
- Port **φ** outputs the energy flow rate.
- Port **Mw** outputs the water vapor mass flow rate.
- Port **Mg** outputs the trace gas mass flow rate.
- Port **Md** outputs the water droplets mass flow rate.

These ports have conditional port visibility on the block icon. Use the block parameters
to expose only the ports that you need for measurements in a particular model.

Connect the measurement ports to PS-Simulink Converter blocks to transform the output physical signals into
Simulink® signals, for example, for plotting or additional data processing.
