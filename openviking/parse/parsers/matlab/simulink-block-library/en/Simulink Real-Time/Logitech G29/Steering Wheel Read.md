---
type: simulink-block
title: 'Logitech G29 Steering Wheel'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Logitech G29'
documentation_page: 'logitechg29steeringwheel'
documentation_source_path: 'io_ref/logitechg29steeringwheel.html'
language: en
---

# Logitech G29 Steering Wheel

## Ports
```yaml
ports:
- name: Buttons
  summary: Status of steering wheel buttons 0 (= unpressed) | 1 (= pressed)
  direction: output
  data_types: Boolean
- name: Steering
  summary: Value of steering wheel position 0 (= left most) | 65535 (= right most)
  direction: output
  data_types: uint16
- name: Pedals
  summary: Status of throttle, brake, and clutch pedals 0 (= not engaged) | 255 (= fully engaged)
  direction: output
  data_types: uint8
- name: Direction
  summary: Status of direction pad buttons on steering wheel 0 (= UP) | 2 (= RIGHT) | 4 (= DOWN) | 6 (= LEFT) | 8 (= UNPRESSED)
  direction: output
  data_types: uint8
- name: Status
  summary: Status of communications with steering wheel 0 (default) | negative value
  direction: output
  data_types: int32
```

### Output

### **Buttons** — Status of steering wheel buttons 0 (= unpressed) | 1 (= pressed)

The `Buttons` output is a vector of Boolean values that indicate
the status of buttons on the steering wheel. The order of the button values in the
vector is:

1. Square
2. X
3. Circle
4. Triangle
5. LPaddle
6. RPaddle
7. L2
8. R2
9. L3
10. R3
11. Share
12. Option
13. PS

**Data Types:** `Boolean`

### **Steering** — Value of steering wheel position 0 (= left most) | 65535 (= right most)

The `Steering` output value indicates the position of the
steering wheel.

**Data Types:** `uint16`

### **Pedals** — Status of throttle, brake, and clutch pedals 0 (= not engaged) | 255 (= fully engaged)

The `Pedals` output is a vector of values that indicate the
status of the throttle, brake, and clutch pedals. The order of the pedal values in the
vector is:

1. Throttle
2. Brake
3. Clutch

**Data Types:** `uint8`

### **Direction** — Status of direction pad buttons on steering wheel 0 (= UP) | 2 (= RIGHT) | 4 (= DOWN) | 6 (= LEFT) | 8 (= UNPRESSED)

The `Direction` output value indicates a button press on the
direction pad. When you press the direction pad in between the pad buttons,
intermediate values occur.

**Data Types:** `uint8`

### **Status** — Status of communications with steering wheel 0 (default) | negative value

The `Status` output value indicates successful communications
with the steering wheel (0) or unsuccessful communications (negative value).

**Data Types:** `int32`
## Parameters
```yaml
parameters:
- name: sampleTime
  summary: Sample time for steering wheel data -1 (inherited) (default)
  group: ''
  block_parameter: sampleTime
```

### **sampleTime** — Sample time for steering wheel data -1 (inherited) (default)

Select the sample time for steering wheel data. The recommended
`sampleTime` is 10ms.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `sampleTime` |
## Libraries

Simulink Real-Time / Logitech G29

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2018b**

## Description

Receive Logitech G29 Steering Wheel read data

The Logitech G29 Steering Wheel block reads data from a Logitech® G29 Steering Wheel (PS3 only). The block does not support a Stick Shift module.

**Note**

Connect the Logitech G29 Steering Wheel device to the USB port on the target
computer.
