---
type: simulink-block
title: 'Input Capture'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / System Peripherals'
documentation_page: 'inputcapture'
documentation_source_path: 'supportpkg/arduino_ref/inputcapture.html'
language: en
---

# Input Capture

## Ports

### Output

### **Frequency** — Frequency of external input signal scalar

The block outputs the frequency of the external input signal in Hertz.

**Data Types:** `uint32`

### **Duty Cycle** — Duty cycle of external input signal `1` to `100`

The block outputs the duty cycle of the external input signal as a
percentage.

**Data Types:** `uint8`

## Parameters

### **Input capture pin number** — Pin to which external input signal is connected `48` (default) | scalar

Enter the Arduino hardware board pin number to which the external input signal is
connected.

**Note**

Do not assign the same pin number to multiple blocks within a model.

To know more on how to assign pins or to view the fixed pins for the Input
Capture block, see Pin Mapping for Arduino Timer-Dependent Blocks.

### **Sample Time** — Time interval at which external input signal is read `0.1` (default) | scalar

Enter the time interval in seconds at which the block reads the external input
signal from the specified pin number.

## Libraries

Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Measure frequency and duty cycle of external input signal

The Input Capture block measures the frequency and duty cycle of the
external input signal on the digital pin of the Arduino® hardware board. The block utilizes the timer counters available on the
Arduino hardware board along with the interrupt service routines to compute the
frequency and duty cycle of the external input signal.

You can run a Simulink® model containing Input Capture block in Connected IO mode on
Arduino boards.

For more information on the conflicting usage of digital pins for a Simulink model that uses one or more combination of PWM, Standard Servo Read, Standard Servo Write, Continuous Servo Write, and Input
Capture blocks, see the Conflicting Pin Configurations on Arduino Timer section.

### Limitations

This table lists the maximum measurable frequency and their corresponding measurable
duty cycle range for the Arduino boards.

| Arduino Board Architecture | Maximum Measurable Frequency | Measurable Duty Cycle Range |
| --- | --- | --- |
| AVR | `50`KHz | `20`% to `80`% |
| SAMD | `400`KHz |
| SAM | `400`KHz |
| Nano 33 BLE Sense | `50`KHz |

This table lists the maximum and minimum frequency and duty cycle that can be measured
using the Arduino-compatible Teensy 4.0 and 4.1 boards.

| Arduino Board Architecture | CPU Frequency (MHz) | Minimum and Maximum Measurable Frequency Range | Measurable Duty Cycle Range |
| --- | --- | --- | --- |
| Teensy 4.0 and 4.1 | 1008 | 1.2KHz - 1MHz | `20`% to `80`% |
| 960 |
| 912 |
| 816 |
| 720 |
| 600 |
| 528 |
| 450 |
| 396 | 1.2KHz - 500KHz |
| 150 | 1.2KHz - 250KHz |
| 24 | 200Hz - 5KHz |
