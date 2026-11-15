---
type: simulink-block
title: 'Analog Output'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / System Peripherals'
documentation_page: 'analogoutput'
documentation_source_path: 'supportpkg/arduino_ref/analogoutput.html'
language: en
---

# Analog Output

## Ports

### Input

### **Port\_1** — Input voltage scalar

The block inputs the digital voltage.

**Data Types:** `uint16`

## Parameters

### **DAC pin** — DAC pin on Arduino board `DAC0` (default) | `DAC1` | `DAC2`

Select a DAC pin on which to generate analog voltage.

This table lists the Arduino boards and DAC pin configuration that the block
supports.

| Arduino Boards | Supported Number of DAC Pins | Supported DAC Pins | Supported Number of Bits for DAC Pins |
| --- | --- | --- | --- |
| Arduino Due | Two | DAC0, DAC1 | 12-bit |
| Arduino Nano 33 BLE Sense | Two | DAC0, DAC1 | 12-bit |
| Arduino MKR1000 | One | DAC0 | 10-bit |
| Arduino MKR Wi-Fi 1010 | One | DAC0 | 10-bit |
| Arduino MKR ZERO | One | DAC0 | 10-bit |
| Arduino Nano 33 IoT | One | DAC0 | 10-bit |
| Arduino Uno R4 Wi-Fi | One | DAC0 | 12-bit |
| Arduino Uno R4 Minima | One | DAC0 | 12-bit |
| Arduino compatible ESP32 – WROOM | Two | DAC1, DAC2 | 8-bit |
| Arduino compatible ESP32 – WROVER | Two | DAC1, DAC2 | 8-bit |

Click **View pin map** to open the Arduino Pin Mapping
table. To know how to assign pins for the block, see Pin Mapping for Arduino Timer-Independent Blocks.

## Libraries

Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2014a**

## Description

Generate voltage on the specified DAC pin

The Analog Output block generates voltage on the specified DAC pin of
the board.

You can run a Simulink® model containing Analog Output block in Connected IO mode
on Arduino® boards.

### Supported Arduino Boards

- Arduino Due
- Arduino Nano 33 BLE Sense
- Arduino MKR 1000
- Arduino MKR Zero
- Arduino MKR Wi-Fi® 1010
- Arduino Nano 33 IoT
- Arduino compatible ESP32 – WROOM and ESP32 – WROVER
- Arduino Uno R4 Wi-Fi
- Arduino Uno R4 Minima

The block outputs voltage
(`Vout`) on the DAC
pin, such that:

```
Vout = VrefX(input/2N-1)+ Voffset
```

This table explains the variables in the formula.

| Variable | Arduino Boards | | | | Description |
| --- | --- | --- | --- | --- | --- |
| Arduino Due, Arduino 33 BLE Sense | Arduino MKR1000, Arduino MKR Wi-Fi 1010, Arduino ZERO, Arduino Nano 33 IoT | Arduino Uno R4 Wi-Fi, Arduino Uno R4 Minima | Arduino Compatible ESP32 boards |
| `Vref` | 2.2 | 3.27 | 5 | 3.3 | Reference voltage for the DAC pin. |
| `input` | 0 < `input` < 4095 | 0 < `input` < 1023 | 0 < `input` < 4095 | 0 < `input` < 255 | Input voltage to the block must lie within this range. Any value outside the given range saturates the voltage output at the DAC pin. |
| `N` | 12 | 10 | 12 | 8 | Number of bits on DAC channel. |
| `Voffset` | 0.56 | 0.007 | 0 | 0 | Offset voltage on Arduino board. |
