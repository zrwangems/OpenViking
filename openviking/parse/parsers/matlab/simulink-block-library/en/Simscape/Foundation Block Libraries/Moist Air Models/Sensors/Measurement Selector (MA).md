---
type: simulink-block
title: 'Measurement Selector (MA)'
family: 'simscape'
product_id: 'simscape'
product_name: 'Simscape'
documentation_release: R2025b
official_category: 'Foundation Block Libraries / Moist Air Models / Sensors'
documentation_page: 'measurementselectorma'
documentation_source_path: 'ref/measurementselectorma.html'
language: en
---

# Measurement Selector (MA)

## Ports

### Input

### **F** — Vector physical signal containing pressure, temperature, humidity, and trace gas levels data physical signal vector

Connect this port to the physical signal output port
**F** of a block with finite internal moist air
volume to access the data. Blocks with a finite moist air volume have a
physical signal output port **F**, which outputs a
vector signal containing the pressure (in Pa), temperature (in K),
humidity, water droplets mass ratio, and trace gas level measurements
inside the component. Use the Measurement Selector
(MA) block to unpack this vector signal.
### Output

### **P** — Pressure measurement, Pa physical signal

Physical signal output port for pressure measurement.

### **T** — Temperature measurement, K physical signal

Physical signal output port for temperature measurement.

### **W** — Humidity level measurement, unitless physical signal

Physical signal output port for humidity level measurement. To select
the quantity you want to measure, use the **Measured humidity
specification** parameter.

### **G** — Trace gas level measurement, unitless physical signal

Physical signal output port for trace gas level measurement. To select
the quantity you want to measure, use the **Measured trace gas
specification** parameter.

### **D** — Mass ratio of water droplets to moist air, unitless physical signal

Physical signal output port for the mass ratio of water droplets to
moist air.

## Parameters

### **Measured humidity specification** — Select the humidity property to measure `Relative humidity` (default) | `Specific humidity` | `Mole fraction` | `Humidity ratio`

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

### **Measured trace gas specification** — Select the trace gas property to measure `Mass fraction` (default) | `Mole fraction`

Select the property to measure:

- `Mass fraction` ― Physical signal port
  **G** reports the trace gas mass
  fraction.
- `Mole fraction` ― Physical signal port
  **G** reports the trace gas mole
  fraction.

## Libraries

Simscape / Foundation Library / Moist Air / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018a**

### R2024b: Model water droplets suspended in moist air flow

Blocks in the moist air domain can now model water droplets suspended in a moist air flow. To model water droplets, select **Enable entrained water droplets** in the Moist Air Properties (MA) block connected to your moist air network.

## Description

Measure pressure, temperature, humidity, and trace gas levels in moist air internal volumes

The Measurement Selector (MA) block lets you access the
pressure, temperature, moisture level, and trace gas level measurements inside a block
with a finite moist air volume. There is no mass or energy flow through the
sensor.

Blocks with a finite moist air volume contain an internal node, which represents the
moist air volume inside the component. For a complete list of these blocks, see Blocks with Moist Air Volume. Regular sensors
cannot connect to this internal node. Therefore, each of the blocks with a finite moist
air volume has a physical signal output port **F**, which outputs a
vector signal containing the pressure (in Pa), temperature (in K), humidity, water
droplets mass ratio, and trace gas level measurements inside the component. For more
information, see Measuring Moisture and Trace Gas Levels.

Use the Measurement Selector (MA) block to unpack the
vector signal and reassign units to pressure and temperature values. Connect the input
port **F** of the Measurement Selector
(MA) block to the physical signal output port **F**
of a block with finite internal moist air volume to access the data.

Connect the output ports of the Measurement Selector
(MA) block to PS-Simulink Converter blocks to transform the output physical
signals into Simulink® signals, for example, for plotting or additional data processing. Use the
**Output signal unit** parameter of the PS-Simulink Converter blocks connected to ports
**P** and **T** to reassign units to pressure and
temperature values, respectively.
