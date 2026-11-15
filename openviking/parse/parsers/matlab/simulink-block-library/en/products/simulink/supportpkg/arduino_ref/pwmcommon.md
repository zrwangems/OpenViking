---
type: simulink-block
title: 'PWM Common'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / System Peripherals'
documentation_page: 'pwmcommon'
documentation_source_path: 'supportpkg/arduino_ref/pwmcommon.html'
language: en
---

# PWM Common

## Ports

### Input

### **Data** — Input value that determines width of square pulses positive integer in the range [0, 255]

The value sent to the block input determines the width of the square wave, called
*duty-cycle*, that the Arduino hardware outputs on the specified PWM pin.

For example:

- Sending the maximum value, `255`, to the block input
  produces 100% duty-cycle, which results in full power on the PWM pin.
- Sending the minimum value, `0`, to the block input produces
  0% duty-cycle, which results in no power on the PWM pin.
- Sending an intermediate value to the block input produces a proportional
  duty-cycle and power output on the PWM pin. For example, sending
  `204` to the block input produces 80% duty cycle and power
  (204/255 = 0.8).
- Sending out-of-range values, such as `500` or
  `-500`, to the block input has the same effect as sending the
  maximum or minimum input values, respectively.

The block input port inherits the data type of the upstream block, and internally
converts it to `uint8`.

**Data Types:** `uint8`

## Parameters

### **Pin number** — PWM pin number `5` (default) | scalar

Specify the Arduino hardware board pin number to which the PWM input signal is connected.
Click **View pin map** to open the Arduino pin mapping table. For more information on how to assign pins or view the
pins for the PWM block, see Pin Mapping for Arduino Timer-Dependent Blocks.

**Note**

Do not assign the same pin number to multiple blocks within a model.

### **Frequency** — PWM output frequency `Default` (default) | `Specify`

Configure the frequency of the PWM signal.

When you set the **Frequency** as:

- `Default` –– The block generates PWM signal with
  default frequency. For more information on default PWM frequencies and pins that
  support PWM on different Arduino boards, see PWM supported pins and
  frequencies and Supported Default PWM Frequencies and Pins on Arduino Compatible Teensy Boards.
- `Specify` –– Using this parameter, you can specify
  the frequency of the PWM signal. Using this option enables the
  **Desired(Hz)** and **Achievable(Hz)**
  parameters. In the **Desired(Hz)** parameter, specify the desired
  frequency of the PWM signal. The block generates the PWM signals with achievable
  frequency that is closest to the frequency specified in the
  **Desired(Hz)** parameter.

**Note**

In the connected I/O mode, you cannot use the `Specify`
option. The block generates the PWM signal only with default frequencies.

### **Desired (Hz)** — Desired PWM output frequency `490.2` (default) | scalar

Specify the desired output frequency of the PWM signal.

#### Dependencies

To enable this parameter, set **Frequency** to
`Specify`.

### **Achievable (Hz)** — Achievable PWM output frequency by Arduino board scalar

The block generates the PWM signals with the frequency that is closest to the
frequency specified in the **Desired(Hz)** parameter.

#### Dependencies

To enable this parameter, set **Frequency** to
`Specify`.

## Libraries

Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2012b**

## Description

Generate pulse width modulated signal on analog output pin

The PWM block generates square pulses of varying duty cycle depending on
the input value sent to the block on the Arduino® hardware pin. This block enables a digital output to provide a range of
different power levels, similar to that of an analog output.

For more information on how to select pins when you Simulink® model contains PWM, Standard Servo Read, Standard Servo Write, Continuous Servo Write, and Input Capture
blocks, see Conflicting Pin Configurations on Arduino Timer.

### Maximum Achievable PWM Frequency

This table specifies the maximum PWM frequency that can be generated on the digital pins
of the following Arduino boards.

| Arduino Board Type | Maximum Achievable PWM Frequency |
| --- | --- |
| Uno, Nano 3.0, Mega 2560/ADK, Leonardo, Robot Control Board, Robot Motor Board, Micro | `4 MHz` |
| Nano 33 IoT, MKR Zero, MKR 1000 | `24 MHz` |
| Due | `21 MHz` |
| Arduino compatible ESP32 WROOM and WROVER | `31.25 KHz` |
| Arduino Uno R4 Wi-Fi® and Arduino Uno R4 Minima | `1 MHz` |

### Limitations

- If you use the PWM block along with the Serial Receive and Serial Transmit blocks in a Simulink model, use longer sample times to avoid overruns.
- This table specifies the upper limit of the output frequency that can be generated
  on the digital pins of the following Arduino boards.

  | Arduino Board Type | Arduino Pin Number | Generated PWM Output Frequencies (Hz) |
  | --- | --- | --- |
  | Uno, Nano 3.0 | `5`, `6` | `980.4` |
  | `3`, `11` | `31372.55`, `3921.16`, `980.4`, `490.2`, `245.1`, `122.55`, `30.64` |
  | Mega 2560/ADK | `4`, `13` | `980.4` |
  | `9`, `10` | `31372.55`, `3921.16`, `980.4`, `490.2`, `245.1`, `122.55`, `30.64` |
  | Leonardo, Robot Control Board, Robot Motor Board, Micro | `3`, `11` | `980.4` |
