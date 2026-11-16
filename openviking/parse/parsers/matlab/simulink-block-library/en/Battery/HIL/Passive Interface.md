---
type: simulink-block
title: 'Passive Interface'
family: 'simscape-battery'
product_id: 'simscape-battery'
product_name: 'Battery'
documentation_release: R2025b
official_category: 'HIL'
documentation_page: 'passiveinterface'
documentation_source_path: 'ref/passiveinterface.html'
language: en
---

# Passive Interface

## Ports

### Input

### **Icsc\_discharge** — Discharge current from cell supervisory circuit, A physical signal | scalar

Discharge current from the cell supervisory circuit, in ampere.

### **SOC** — Battery state-of-charge, unitless physical signal | scalar

State-of-charge of the battery, in percent.

#### Dependencies

To enable this port, set the **Expose SOC input
port** parameter to
`Yes`.
### Output

### **Vbat** — Battery voltage, V physical signal

Voltage across the battery, in volt.

### **Icsc** — Cell supervisory circuit current, A physical signal

Current flowing through the cell supervisory circuit, in
ampere.

The value at this port is always numerically identical to the value at
the **Icsc\_discharge** port. This port simply provides
consistency with the Active Interface
block or with any hardware that requires it.

#### Dependencies

To enable this port, set the **Expose cell supervisory
circuit current measurement port** parameter to
`Yes`.

### **SOC** — Battery state-of-charge, unitless physical signal

State-of-charge of the battery, in percent.

#### Dependencies

To enable this port, set the **Expose SOC output
port** parameter to
`Yes`.

### **T** — Temperature measurement, K physical signal

Temperature of the battery, in kelvin.

#### Dependencies

To enable this port, set the **Expose temperature
measurement port** parameter to
`Yes`.
### Conserving

### **+** — Positive terminal electrical

Electrical conserving port associated with the positive terminal of
the interface.

### **-** — Negative terminal electrical

Electrical conserving port associated with the negative terminal of
the interface.

### **H** — Thermal port thermal

Thermal conserving port.

#### Dependencies

To enable this port, set the **Thermal port**
parameter to `Model`.

## Parameters

### **Expose cell supervisory circuit current measurement port** — Measurement port visibility for cell supervisory circuit current `Yes` (default) | `No`

Option to expose the port that measures the current from the cell
supervisory circuit.

### **Expose SOC input port** — SOC input port visibility `No` (default) | `Yes`

Option to expose the battery SOC input port.

### **Expose SOC output port** — SOC output port visibility `Yes` (default) | `No`

Option to expose the battery SOC output port.

#### Dependencies

To enable this parameter, set **Expose SOC input
port** to `Yes`.

### **Thermal port** — Thermal port visibility `Omit` (default) | `Model`

Option to model the thermal port of the passive interface.

### **Expose temperature measurement port** — Temperature measurement port visibility `Yes` (default) | `No`

Option to expose the port that measures the temperature of the
battery.

#### Dependencies

To enable this parameter, set **Thermal port** to
`Model`.

## Libraries

Simscape / Battery / HIL

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2022b**

## Description

Passive interface between battery and cell supervisory circuit

The Passive Interface block provides an abstracted
passive interface between a battery and a cell supervisory circuit. Use this block with
desktop simulations and hardware-in-the-loop battery emulation hardware.

A cell supervisory circuit is an electronic circuit that connects to battery cells or
parallel assemblies. You can use this circuit to normalize voltages or states-of-charge
(SOC) inside a module or pack. In the real world, you implement this equipment between
your battery and the battery management system (BMS) control.

In this figure, the items in blue represent real-world equipment, voltages, and currents.

To avoid damaging your battery and to test your cell balancing algorithms under
standard operational conditions and fault conditions, you can use hardware-in-the-loop
battery emulation hardware. An abstracted interface facilitates connecting, setting, and
configuring the passive balancing BMS to your emulated battery.

In this figure:

- The blue color represents real-world equipment, voltages, and
  currents.
- The green color represents the interface between the real-world equipment,
  voltages, and currents, as well as the simulated equipment, voltages, and
  currents.
- The orange color represents the simulated equipment, voltages, and
  currents.

The Passive Interface block provides the abstract
representation of power electronic equipment without the need to model it in detail. For
example, if you have a battery pack with different levels of temperature or voltage
within its constituent parts, you can use this block to check if the BMS is correctly
balancing your pack after a variety of operational scenarios.

### SOC Optional Ports

Use the optional SOC ports of the Passive Interface
block to avoid implementing an SOC estimation algorithm in the BMS, to validate and
verify the SOC estimation algorithm against the simulated SOC, or to represent a
real-world battery.

- If, in your model, the battery has an SOC output port, expose the SOC
  input port of this block and connect the ports appropriately. To expose the
  SOC input port of this block, set the **Expose SOC input
  port** parameter to `Yes`.
- To avoid implementing an SOC estimation algorithm in the BMS or to
  validate and verify the SOC estimation algorithm against the simulated SOC,
  expose the SOC output port of this block and connect it to your BMS. To
  expose the SOC output port of this block, set the **Expose SOC
  output port** parameter to
  `Yes`.
- To represent a real-world battery, do not expose the SOC ports of this
  block.

### Thermal and Temperature Optional Ports

Use the optional thermal and temperature ports of the Passive
Interface block to represent a battery with a temperature sensor
or to validate and verify the temperature estimation algorithm against the simulated
temperature.

- If, in your model, the battery has a temperature sensor, expose the
  thermal port **H** of this block and connect it to the
  thermal network. To expose the thermal port of this block, set the
  **Thermal port** parameter to
  `Model`.
- To validate and verify the temperature estimation algorithm against the
  simulated temperature, expose the thermal port **H** and
  the temperature measurement port **T** of this block and
  connect them to the thermal network and your BMS, respectively. To expose
  the temperature measurement port of this block, set the **Expose
  temperature measurement port** parameter to
  `Yes`.
- If, in your model, the battery does not include thermal effects or does
  not have a temperature sensor, do not expose the thermal and temperature
  ports of this block.
