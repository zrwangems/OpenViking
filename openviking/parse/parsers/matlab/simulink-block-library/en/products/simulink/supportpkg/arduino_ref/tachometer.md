---
type: simulink-block
title: 'Tachometer'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Sensors / Motor and Vehicle Sensors'
documentation_page: 'tachometer'
documentation_source_path: 'supportpkg/arduino_ref/tachometer.html'
language: en
---

# Tachometer

## Ports

### Output

### **Port\_1** — Rotational speed of shaft scalar

The port outputs the rotational speed of the shaft connected to the
hardware.

**Data Types:** `uint32`

## Parameters

### **Pin number** — Pin number on hardware `2` (default)

Specify the pin number on the hardware to which the tachometer is
connected.

Click **View pin map** to open the Arduino Pin Mapping
table.

To know how to assign pins for the block, see Pin Mapping for Arduino Timer-Independent Blocks.

For more information about the pins supported on the hardware for
interrupts from the tachometer, see Pins With Interrupts.

### **Interrupt mode** — Counting technique of tachometer signal `RISING` (default) | `FALLING` | `CHANGE` | `LOW` | `HIGH`

The interrupt mode specifies how the tachometer counts its output signal.
The counting technique is different for different interrupt modes:

- `RISING` – Counts every rising edge
  of the signal.
- `FALLING` – Counts every falling edge
  of the signal.
- `CHANGE` – Counts every rising and
  falling edge of the signal.
- `LOW` – Counts every low
  signal.
- `HIGH` – Counts every high
  signal.

This figure shows how the tachometer counts its output signal in different
interrupt modes.

### **Pulse count per rotation** — Number of interrupts each rotation `1` (default) | any positive integer

Specify the number of interrupts the block receives each rotation.

### **Sample time** — Time interval to read value from tachometer `0.1` (default)

Specify how often the block reads the rotational speed from the
tachometer, in seconds.

## Libraries

Simulink Support Package for Arduino Hardware / Sensors

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Read rotational speed of shaft

The Tachometer block reads the rotational speed of the shaft from the
tachometer connected to the hardware. The block outputs the speed of rotation as a
`uint32` value.

If you simulate a model that contains the Tachometer block without
connecting the hardware, the block outputs zeros. For more information, see Block Produces Zeros or Does Nothing in Simulation.
