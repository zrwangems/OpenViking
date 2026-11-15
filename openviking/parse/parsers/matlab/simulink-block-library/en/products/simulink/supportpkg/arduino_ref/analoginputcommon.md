---
type: simulink-block
title: 'Analog Input'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / System Peripherals'
documentation_page: 'analoginputcommon'
documentation_source_path: 'supportpkg/arduino_ref/analoginputcommon.html'
language: en
---

# Analog Input

## Ports

### Output

### **Pin 1 value** — Voltage of analog input pin scalar

The block outputs the digitally converted voltage value that is received on the
analog input pin of the Arduino board.

**Data Types:** `double`

## Parameters

### **Pin number** — ADC pin number `4` (default) | Arduino board pin number

Specify the Arduino board analog input pin number. To open the Arduino pin mapping table, click **View pin map**. To know how
to assign pins for the block, see Pin Mapping for Arduino Timer-Independent Blocks.

### **Sample time** — Time interval at which the blocks read input pin value `–1` (default) | scalar

Specify how often the block measures voltage of the analog input pin, in seconds.
Enter a value greater than zero. When you specify this parameter as
`–1`, Simulink® determines the best sample time for the block based on the block context
within the model.

## Libraries

Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014a**

## Description

Measure voltage of analog input pin

Use the Analog Input block to measure the voltage of an analog pin relative
to the analog input reference voltage on the Arduino® hardware. The block outputs the measurement as a value that ranges from
`0` to `1023`.

- If the measured voltage equals the ground voltage, the block output emits
  `0`.
- If the measured voltage equals the analog reference voltage, the block output emits
  `1023`.

The default value of the analog input reference voltage for most of the Arduino boards is 5 V. To change the **Analog input reference voltage**
parameter in your model Configuration Parameters, navigate to **Hardware
Implementation** > **Target hardware resources** >
**Analog input channel properties**.

The analog input reference voltage for Arduino Due, Nano 33 IoT, MKR boards, and Nano 33 BLE Sense boards is 3.3 V. You cannot
change this value.

**Warning**

The range of the voltage that can be applied to the analog input pin depends on the
analog input reference voltage. For details, read the documentation for your Arduino hardware.
