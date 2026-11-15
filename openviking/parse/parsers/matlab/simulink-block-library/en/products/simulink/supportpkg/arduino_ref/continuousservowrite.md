---
type: simulink-block
title: 'Continuous Servo Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Motors, Servo Motors, and Motor Drivers'
documentation_page: 'continuousservowrite'
documentation_source_path: 'supportpkg/arduino_ref/continuousservowrite.html'
language: en
---

# Continuous Servo Write

## Ports

### Input

### **Data** — Input value that determines speed and direction of continuous rotation servo motor positive integer in the range [`0`, `255`]

The value sent to the block at the input port determines the speed and direction
of rotation of the continuous rotation servo motor interfaced with the Arduino hardware board. For example:

- Sending `-90` to the block produces the maximum rate of
  rotation in one direction.
- Sending `90` to the block produces the maximum rate of
  rotation in the opposite direction.
- Sending `0` to the block stops the servo motor.
- Sending out-of-range values, such as `-95` or
  `300`, to the block has the same effect as sending the
  minimum or maximum input values, respectively.

The block input port inherits the data type of the upstream block, and internally
converts it to `uint8` with an offset of `90`.

**Data Types:** `uint8`

## Parameters

### **Pin number** — Continuous servo write pin number `2` (default) | scalar

Specify the Arduino hardware board pin number to which the continuous rotation servo motor
input signal is connected.

**Note**

Do not assign the same pin number to multiple blocks within a Simulink model.

For more information on how to assign pins or view the pins for the
Continuous Servo Write block, see Pin Mapping for Arduino Timer-Dependent Blocks.

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

Set direction and speed of continuous rotation servo motor

The Continuous Servo Write block sets the direction and speed of a
continuous rotation servo motor depending on the input value sent to the block on the
Arduino® hardware pin.

The characteristics of some motors cause them to continue rotating even when the block
input is `0`. You can experiment to find an offset value that stops the
motor.

With Arduino Mega 2560 hardware, you can use External mode to determine the offset while your
model is running on the hardware. For more details, see Tune and Monitor Model Running on Hardware.

You can run a Simulink® model containing Continuous Servo Write block in Connected IO mode on
Arduino boards.

**Note**

If you use the Continuous Servo Write block along with the Serial Receive and Serial Transmit blocks in a Simulink model, use longer sample times to avoid overruns.

### Maximum Number of Servo Blocks Allowed per Simulink Model

The number of Servo blocks, Standard Servo Read, Standard Servo Write, and Continuous Servo Write, you can use in
your Simulink model depends on the number of timers on your Arduino hardware board. Every timer on the Arduino board can support up to 12 Servo blocks.

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
