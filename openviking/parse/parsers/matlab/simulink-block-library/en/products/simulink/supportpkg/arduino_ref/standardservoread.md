---
type: simulink-block
title: 'Standard Servo Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Motors, Servo Motors, and Motor Drivers'
documentation_page: 'standardservoread'
documentation_source_path: 'supportpkg/arduino_ref/standardservoread.html'
language: en
---

# Standard Servo Read

## Ports

### Output

### **Data** — Standard servo motor shaft rotation angle positive integer in the range [`0`, `180`]

The block outputs the shaft rotation angle from `0` to
`180` degrees for the standard servo motor that you interface with
the Arduino hardware board. When simulating without the hardware, the block outputs
zeroes.

**Data Types:** `uint8`

## Parameters

### **Pin number** — Standard servo read pin number `2` (default) | scalar

Specify the Arduino hardware board pin number to which the standard servo read motor input
signal is connected.

**Note**

Do not assign the same pin number to multiple blocks within a Simulink model.

For more information on how to assign pins or view the pins for the Standard
Servo Read block, see Pin Mapping for Arduino Timer-Dependent Blocks.

### **Sample time** — Time interval at which block reads shaft rotation data `0.1` (default) | scalar

Enter the time interval in seconds at which the block reads the shaft rotation angle
of the standard servo motor. The minimum sample time is
`0.000001`.

### **View Pin Map** — Open pin mapping for Arduino hardware boards button

Click this button to view the pin mapping table associated with the Arduino hardware board you select.

## Libraries

Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2012a**

## Description

Measure shaft position of standard servo motor in degrees

The Standard Servo Read block measures the shaft position in degrees of the
standard servo motor interfaced with the Arduino® hardware board.

You can run a Simulink® model containing Standard Servo Read block in Connected IO mode on Arduino boards.

**Note**

If you use the Standard Servo Read block along with the Serial Receive and Serial Transmit blocks in a Simulink model, use longer sample times to avoid overruns.

### Maximum Number of Servo Blocks Allowed Per Simulink Model

The number of Servo blocks, Standard Servo Read, Standard Servo Write, and Continuous Servo Write, you can use in your
Simulink model depends on the number of timers on your Arduino hardware board. Every timer on the Arduino board can support up to 12 Servo blocks.

For example, consider the Arduino Mega 2560/ADK board. The maximum number of servo
blocks that can be used per Simulink model is 48. If your Simulink model utilizes a total number of 48 Servo blocks and the board has 5 timers,
timer 5 supports the first set of 12 (1 to 12) Servo blocks. Similarly, timer 1 supports the
next set of 12 (13-24) Servo blocks, timer 3 supports the next set of 12 (25-36) Servo
blocks, and finally, timer `4` supports the last set of 12 (37-48) servo
blocks.

The Servo blocks are grouped as follows:

- **Set 1**: Servo blocks 1 to 12
- **Set 2**: Servo blocks 13 to 24
- **Set 3**: Servo blocks 25 to 36
- **Set 4**: Servo blocks 37 to 48
- **Set 5**: Servo blocks 49 to 60

This table shows how to assign timers to Servo blocks depending on the Arduino board you are using. It also provides the maximum number of Servo blocks that
you can use per Simulink model.

| Arduino Board Type | Timer | Maximum Number of Servo Blocks per Simulink Model |
| --- | --- | --- |
| Uno, Nano 3.0 | 1 | Set 1 |
| Mega 2560/ADK | 1 | Set 2 |
| 3 | Set 3 |
| 4 | Set 4 |
| 5 | Set 1 |
| Leonardo, Robot Control Board, Robot Motor Board, Micro | 1 | Set 1 |
| MKR 1000, MKR WiFi 1010, MKR Zero | TC4 | Set 1 |
| Nano 33 IoT | TC4 | Set 1 |
| Due | TC3\_CH0 | Set 1 |
| TC4\_CH1 | Set 2 |
| TC5\_CH2 | Set 3 |
| TC2\_CH2 | Set 4 |
| TC0\_CH0 | Set 5 |
| Uno R4 WiFi and Minima | FSP Timer | Set 1 |
| Arduino-compatible Teensy 4.0 and 4.1 | PIT0 | Set 4 |
| PIT1 |
| PIT2 |
| PIT3 |
| Arduino-compatible ESP32-WROOM and ESP32-WROVER | 0 | Set 4 |
| 1 |
| 2 |
| 3 |
| Arduino-compatible Pico and Pico W | 0 | Set 1 |
