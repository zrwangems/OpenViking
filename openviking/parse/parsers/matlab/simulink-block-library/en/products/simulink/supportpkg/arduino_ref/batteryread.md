---
type: simulink-block
title: 'Battery Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Motors, Servo Motors, and Motor Drivers'
documentation_page: 'batteryread'
documentation_source_path: 'supportpkg/arduino_ref/batteryread.html'
language: en
---

# Battery Read

## Ports

### Output

### **Port\_1** — Voltage of battery scalar in the range [0, 4095]

The port outputs the voltage of the battery connected to the MKR or
Nano Motor Carrier. The block outputs the voltage as a 12-bit digital
value ranging between `0` and `4095`.
An output of `0` corresponds to the minimum volts, and
an output of `4095` corresponds to the maximum volts on
an analog pin connected to the battery.

**Data Types:** `uint16`

## Parameters

### **Sample time** — Time interval to read battery voltage `0.1` (default) | `-1` | nonnegative real value

Specify how often the block reads the voltage of the battery, in seconds.
When you specify this parameter as `-1`, Simulink® determines the best sample time for the block based on the
block context within the model.

## Libraries

Simulink Support Package for Arduino Hardware / Arduino Motor Carrier

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2019a**

## Description

Read voltage of battery

The Battery Read block reads the voltage of the battery connected to an
MKR or Nano Motor Carrier. The block outputs the voltage as a 12-bit digital value
ranging between `0` and `4095`. An output of
`0` corresponds to minimum volts and an output of
`4095` corresponds to maximum volts on an analog pin connected to
the battery.

If you simulate a model that contains the Battery Read block without
connecting the hardware, the block outputs zeros. For more information, see Block Produces Zeros or Does Nothing in Simulation.

### Supported Hardware

You can use the Battery Read block only with MKR and Nano 33 IoT
boards.
