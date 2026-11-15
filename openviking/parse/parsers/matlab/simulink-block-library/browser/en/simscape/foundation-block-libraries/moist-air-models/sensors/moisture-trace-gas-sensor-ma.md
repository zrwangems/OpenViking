---
type: simulink-block
title: 'Moisture & Trace Gas Sensor (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Moist Air Models / Sensors'
documentation_page: 'moisturetracegassensorma'
documentation_source_path: 'ref/moisturetracegassensorma.html'
language: en
---

# Moisture & Trace Gas Sensor (MA)

## Ports

### Output

### **W** — Humidity measurement, unitless physical signal

Physical signal output port for humidity measurement. To select the
quantity you want to measure, use the **Measured humidity
specification** parameter.

#### Dependencies

To enable this port, select the **Humidity**
check box and set the **Measured humidity
specification** parameter to

- `Relative humidity`
- `Specific humidity`
- `Mole fraction`
- `Humidity ratio`

### **Tw** — Wet-bulb temperature measurement, K physical signal

Physical signal output port for wet-bulb temperature measurement.

#### Dependencies

To enable this port, select the **Humidity**
check box and set the **Measured humidity
specification** parameter to `Wet-bulb
temperature`.

### **G** — Trace gas level measurement, unitless physical signal

Physical signal output port for trace gas level measurement. To select
the quantity you want to measure, use the **Measured trace gas
specification** parameter.

#### Dependencies

To enable this port, select the **Trace gas**
check box.

### **D** — Mass ratio of water droplets to moist air, unitless physical signal

Physical signal output port for the mass ratio of water droplets to
moist air.

#### Dependencies

To enable this port, select the **Water
droplets** check box.
### Conserving

### **A** — Sensor inlet moist air

Moist air conserving port. Connect this port to the node in the moist
air network where you want to measure the moisture and trace gas level.

## Parameters

### **Humidity** — Control output port visibility for measuring humidity `On` (default) | `Off`

Selecting this check box exposes the output port **W** or
**Tw**, which lets you measure the quantity specified
by the **Measured humidity specification** parameter
value.

### **Measured humidity specification** — Select the humidity property to measure `Relative humidity` (default) | `Specific humidity` | `Mole fraction` | `Humidity ratio` | `Wet-bulb temperature`

Select the property to measure:

- `Relative humidity` ― Physical signal
  port **W** reports the relative humidity.
- `Specific humidity` ― Physical signal
  port **W** reports the specific humidity.
- `Mole fraction` ― Physical signal port
  **W** reports the water vapor mole
  fraction.
- `Humidity ratio` ― Physical signal port
  **W** reports the humidity ratio.
- `Wet-bulb temperature` ― Physical signal
  port **Tw** reports the wet-bulb
  temperature.

### **Trace gas** — Control output port visibility for measuring trace gas `On` (default) | `Off`

Selecting this check box exposes the output port **G**,
which lets you measure the quantity specified by the **Measured
trace gas specification** parameter value.

### **Measured trace gas specification** — Select the trace gas property to measure `Mass fraction` (default) | `Mole fraction`

Select the property to measure:

- `Mass fraction` ― Physical signal port
  **G** reports the trace gas mass
  fraction.
- `Mole fraction` ― Physical signal port
  **G** reports the trace gas mole
  fraction.

### **Water droplets** — Control output port visibility for measuring water droplets `Off` (default) | `On`

Selecting this check box exposes the output port **D**,
which lets you measure the mass ratio of water droplets to moist air.

## Libraries

Simscape / Foundation Library / Moist Air / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2024b: Renamed from Humidity & Trace Gas Sensor (MA)

The Humidity & Trace Gas Sensor (MA) block is
now the Moisture & Trace Gas Sensor (MA) block.

### R2024b: Model water droplets suspended in moist air flow

Blocks in the moist air domain can now model water droplets suspended in a moist air flow. To model water droplets, select **Enable entrained water droplets** in the Moist Air Properties (MA) block connected to your moist air network.

### R2023a: Use wet-bulb temperature to measure humidity

The block now has an option to measure humidity by using the wet-bulb temperature.
Wet-bulb temperature is a method of measuring humidity that involves wrapping a wet
cloth around a thermometer, so that you can measure the temperature including energy
loss due to evaporation. Traditional psychrometers output data in the form of
wet-bulb temperature.

Additionally, moist air sensor blocks with multiple output ports now have
conditional port visibility on the block icon. You can use the block parameters to
expose only the ports that you need for measurements in a particular model.

These changes have no compatibility impact.

## Description

Measure humidity, water droplets, and trace gas levels in moist air network

The Moisture & Trace Gas Sensor (MA) block measures
the amount of humidity, water droplets, and trace gas in a moist air network. There is
no mass or energy flow through the sensor.

The physical signal ports **W**, **Tw**,
**D**, and **G** report the humidity, wet-bulb
temperature, water droplet mass ratio, and trace gas level, respectively, measured at
port **A**. Use the block parameters to control the port visibility and
select the quantities to measure. Connect these ports to PS-Simulink Converter blocks to transform the output physical
signals into Simulink® signals, for example, for plotting or additional data processing.

The sensor measurements correspond to the moisture and trace gas level upstream of the
measured node. For example, if port **A** of the
Moisture & Trace Gas Sensor (MA) is connected to
a node between pipe 1 and pipe 2 and the moist air flows from pipe 1 to pipe 2, then the
moisture and trace gas level measured at port **A** are those of the
moist air volume in pipe 1. If the air flow then switches direction and flows from pipe
2 to pipe 1, then the moisture and trace gas level measured at port
**A** are those of the moist air volume in pipe 2. If the moisture
and trace gas levels of the two moist air volumes are different, then the measured
values change when the flow direction switches. If there are two or more upstream flow
paths merging at the node, then the moisture and trace gas level measurement at the node
represents the weighted average based on the ideal mixing of the merging flow.
