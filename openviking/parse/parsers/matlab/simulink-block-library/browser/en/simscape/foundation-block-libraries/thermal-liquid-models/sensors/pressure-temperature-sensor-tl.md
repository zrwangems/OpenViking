---
type: simulink-block
title: 'Pressure & Temperature Sensor (TL)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Thermal Liquid Models / Sensors'
documentation_page: 'pressuretemperaturesensortl'
documentation_source_path: 'ref/pressuretemperaturesensortl.html'
language: en
---

# Pressure & Temperature Sensor (TL)

## Ports

### Output

### **Pa** — Absolute pressure measurement, in Pascal (Pa) physical signal

Physical signal output port for absolute pressure measurement.

#### Dependencies

To enable this port, set the **Measurement reference**
parameter to `Absolute`, select the
**Pressure** check box, and set the **Pressure
type** parameter to `Absolute pressure`.

### **Pg** — Gauge pressure measurement, Pa physical signal

Physical signal output port for gauge pressure measurement.

#### Dependencies

To enable this port, set the **Measurement reference**
parameter to `Absolute`, select the
**Pressure** check box, and set the **Pressure
type** parameter to `Gauge pressure`.

### **P** — Pressure difference measurement, Pa physical signal

Physical signal output port for pressure difference measurement.

#### Dependencies

To enable this port, set the **Measurement reference**
parameter to `Difference` and select the
**Pressure** check box.

### **T** — Temperature measurement, K physical signal

Physical signal output port for temperature measurement.

#### Dependencies

To enable this port, select the **Temperature** check
box.
### Conserving

### **A** — Sensor inlet thermal liquid

Thermal liquid conserving port. Use this port to measure absolute pressure or
temperature.

### **B** — Sensor outlet thermal liquid

Thermal liquid conserving port. When the sensor measures absolute pressure or
temperature, this port is hidden because the sensor contains an implicit reference
node. Enable this port to measure relative pressure or temperature between two nodes
in the model. The measurements are positive when the values at port
**A** are greater than the values at port
**B**.

#### Dependencies

To enable this port, set the **Measurement reference**
parameter to `Difference`.

## Parameters

### **Measurement reference** — Select between absolute and relative measurements `Absolute` (default) | `Difference`

Select between absolute and relative measurements:

- `Absolute` — The sensor measures pressure and
  temperature at port **A**. The sensor contains an implicit
  reference node, which means that you need only one port to make absolute
  measurements.
- `Difference` — The sensor measures the
  difference in pressure or temperature between two nodes in the model. Selecting this
  option exposes port **B** on the block icon.

### **Pressure** — Control output port visibility for measuring pressure `On` (default) | `Off`

Selecting this check box exposes the output port **Pa**,
**Pg**, or **P**, to let you measure
pressure.

### **Pressure type** — Select between absolute and gauge pressure `Absolute pressure` (default) | `Gauge pressure`

Select whether the sensor measures absolute or gauge pressure:

- `Absolute pressure` — The sensor measures
  absolute pressure at port **A**. Selecting this option exposes port
  **Pa** on the block icon.
- `Gauge pressure` — The sensor measures gauge
  pressure at port **A**. Selecting this option exposes port
  **Pg** on the block icon.

#### Dependencies

To enable this parameter, set **Measurement reference** to
`Absolute` and select the **Pressure**
check box.

### **Temperature** — Control output port visibility for measuring temperature `Off` (default) | `On`

Selecting this check box exposes the output port **T**, which lets
you measure temperature.

## Libraries

Simscape / Foundation Library / Thermal Liquid / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2013b**

### R2023a: Usability enhancement for thermal liquid sensors

Thermal liquid sensor blocks with multiple output ports now have conditional port
visibility on the block icon. You can use the block parameters to expose only the ports that
you need for measurements in a particular model.

Additionally, the Pressure & Temperature Sensor (TL)
block now contains an implicit reference node, which means that you need only one port to
make absolute measurements of pressure or temperature. Expose the second port only if you
need to measure the difference in pressure or temperature between two nodes in the model.

In previous releases, to measure the absolute pressure and absolute temperature at port
**A**, you needed to connect port **B** to an
Absolute Reference (TL) block. This is no longer necessary
because you can now make absolute measurements by setting the **Measurement
reference** parameter to `Absolute`, but existing models
that have these connections continue to work as before.

There is no compatibility impact when you use the Pressure &
Temperature Sensor (TL) block in your models. However, if you use this
block in your custom composite components, you need to update the composite component code.

| Old Syntax | New Syntax |
| --- | --- |
| `sensor = foundation.thermal_liquid.sensors.pressure_temperature_sensor;` | `sensor = foundation.thermal_liquid.sensors.pressure_temperature_sensor(reference=foundation.enum.MeasurementReference.difference, temperature=true);` |

## Description

Measure pressure and temperature in thermal liquid networks

The Pressure & Temperature Sensor (TL) block represents
an ideal sensor that measures pressure and temperature in a thermal liquid network. There is
no mass or energy flow through the sensor.

The sensor contains an implicit reference node, which means that you need only one port,
port **A**, to make absolute measurements of pressure or temperature. Expose
the second port, port **B**, only if you need to measure the difference in
pressure or temperature between two nodes in the model. The measurements are positive when the
values at port **A** are greater than the values at port
**B**.

Four physical signal ports are available to output the measurement data:

- Port **Pa** outputs the absolute pressure.
- Port **Pg** outputs the gauge pressure.
- Port **P** outputs the pressure difference across the sensor.
- Port **T** outputs the temperature.

These ports have conditional port visibility on the block icon. Use the block parameters
to expose only the ports that you need for measurements in a particular model.

Connect the measurement ports to PS-Simulink Converter blocks to transform the output physical signals into
Simulink® signals, for example, for plotting or additional data processing.
