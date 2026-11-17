---
type: simulink-block
title: 'Flow Rate Sensor (2P)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Foundation Library'
documentation_release: R2025b
official_category: 'Two-Phase Fluid / Sensors'
documentation_page: 'flowratesensor2p'
documentation_source_path: 'ref/flowratesensor2p.html'
language: en
---

# Flow Rate Sensor (2P)

## Ports
```yaml
ports:
- name: M
  summary: Mass flow rate measurement, kg/s physical signal
  direction: output
- name: V
  summary: Volumetric flow rate, m^3/s physical signal
  direction: output
- name: φ
  summary: Energy flow rate measurement, W physical signal
  direction: output
- name: A
  summary: Sensor inlet two-phase fluid
  direction: conserving
- name: B
  summary: Sensor outlet two-phase fluid
  direction: conserving
```

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

### **A** — Sensor inlet two-phase fluid

Two-phase fluid conserving port. Flow rates are positive if fluid flows from port
**A** to port **B**.

### **B** — Sensor outlet two-phase fluid

Two-phase fluid conserving port. Flow rates are positive if fluid flows from port
**A** to port **B**.
## Parameters
```yaml
parameters:
- name: Mass flow rate
  summary: Control output port visibility for measuring mass flow rate On (default) | Off
  group: ''
- name: Volumetric flow rate
  summary: Control output port visibility for measuring volumetric flow rate Off (default) | On
  group: ''
- name: Energy flow rate
  summary: Control output port visibility for measuring energy flow rate On (default) | Off
  group: ''
```

### **Mass flow rate** — Control output port visibility for measuring mass flow rate `On` (default) | `Off`

Selecting this check box exposes the output port **M**, which lets
you measure mass flow rate.

### **Volumetric flow rate** — Control output port visibility for measuring volumetric flow rate `Off` (default) | `On`

Selecting this check box exposes the output port **V**, which lets
you measure volumetric flow rate.

### **Energy flow rate** — Control output port visibility for measuring energy flow rate `On` (default) | `Off`

Selecting this check box exposes the output port **φ**, which lets
you measure energy flow rate.
## Libraries

Simscape / Foundation Library / Two-Phase Fluid / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2023a**

### R2023a: Usability enhancement for thermal liquid sensors

In R2023a, separate Mass & Energy Flow Rate Sensor (2P) and
Volumetric Flow Rate Sensor (2P) blocks have been combined into a single
Flow Rate Sensor (2P) block that lets you measure mass flow rate, energy
flow rate, and volumetric flow rate. The new block lets you use the block parameters to
expose only the ports that you need for measurements in a particular model, which helps to
reduce clutter and improve the block diagram layout.

This change has no compatibility impact when you use these Foundation library blocks in
your models. When you open an existing model, the Mass & Energy Flow Rate Sensor
(2P) and Volumetric Flow Rate Sensor (2P) blocks within it are
automatically replaced by Flow Rate Sensor (2P) blocks with the appropriate
ports exposed.

However, if you use the Mass & Energy Flow Rate Sensor (2P) and
Volumetric Flow Rate Sensor (2P) blocks in your custom composite
components, you need to update the composite component code.

| Sensor Block to Update | Old Syntax | New Syntax |
| --- | --- | --- |
| Mass & Energy Flow Rate Sensor (2P) | `sensor = foundation.two_phase_fluid.sensors.mass_flow_energy_flow_sensor;` | `sensor = foundation.two_phase_fluid.sensors.flow_sensor;` |
| Volumetric Flow Rate Sensor (2P) | `sensor = foundation.two_phase_fluid.sensors.volumetric_flow_sensor;` | `sensor = foundation.two_phase_fluid.sensors.flow_sensor(volumetric_flow_measure=true);` |

## Description

Measure mass, energy, and volumetric flow rates in two-phase fluid networks

The Flow Rate Sensor (2P) block represents an ideal sensor
that measures mass flow rate, energy flow rate, and volumetric flow rate in a two-phase fluid
network. There is no change in pressure or temperature across the sensor.

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
