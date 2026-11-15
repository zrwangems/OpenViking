---
type: simulink-block
title: 'Serial Transmit'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Serial'
documentation_page: 'serialtransmit'
documentation_source_path: 'supportpkg/arduino_ref/serialtransmit.html'
language: en
---

# Serial Transmit

## Ports

### Input

### **Data** — Input data [`Nx1`] array

The block inputs the data it transmits over the Arduino serial port to the serial device.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## Parameters

### **Serial port** — Arduino port number for serial communication `0` (default) | positive integer

Specify the serial port number to which you have connected the Arduino board. For more information on the fixed ports and the allocated pins for
the block, see Pin Mapping for Arduino Timer-Independent Blocks.

You can assign a Serial Transmit block and a Serial
Receive block to the same serial port. Do not assign more than one
Serial Receive block to the same Arduino serial port. Do not assign the Arduino pin numbers used by the serial port to other blocks within the same
Simulink model.

The `XCP over Serial`
Communication interface uses serial port 0 in the monitor and tune mode,
and as a result, you cannot use this port in the Serial Transmit block.
You can select any other communication interface or use the build and deploy mode to use
serial port 0.

### **Send mode** — Data transmission mode `write` (default) | `print` | `println`

Select the mode to transmit data over the Arduino serial port.

- `write` — Writes raw binary data to the Arduino serial port.
- `print` — Prints data to the Arduino serial port as ASCII text.
- `println` — Prints data to the Arduino serial port as ASCII text followed by a carriage return character
  '\r' and a newline character '\n'.

Use the `print` and `println`
options to print messages for debugging and logging purposes.

### **Header** — Header for data numeric array | integer from 0 to 255, inclusive

Specify a header that indicates the beginning of your data block.

The numeric array specified in this parameter is the `uint8`
integer representation of the corresponding ASCII characters. The exact form of this
parameter depends on the type of the ASCII character.

| Type of ASCII Character | Example ASCII Character | MATLAB® Command | Parameter Value |
| --- | --- | --- | --- |
| Special character | `"#"` | `uint8('#')` | `[35]` |
| Numeric | `"81"` | `uint8('81')` | `[56 49]` |
| Alphabet | `"Start"` | `uint8('Start')` | `[83 116 97 114 116]` |

You can also specify this parameter using the hexadecimal representation of the
ASCII characters.

#### Dependencies

To enable this parameter, set **Send mode** to
`write`.

### **Terminator** — Terminator for data character array (default)

Specify a terminator that indicates the end of your data block.

The numeric array specified in this parameter is the `uint8`
integer representation of the corresponding ASCII characters. The exact form of this
parameter depends on the type of the ASCII character.

| Type of ASCII Character | Example ASCII Character | MATLAB Command | Parameter Value |
| --- | --- | --- | --- |
| Special character | `"#"` | `uint8('#')` | `[35]` |
| Numeric | `"81"` | `uint8('81')` | `[56 49]` |
| Alphabet | `"End"` | `uint8('End')` | `[69 110 100]` |

| Type of ASCII Character | Example ASCII Character | MATLAB Command | Parameter Value |
| --- | --- | --- | --- |
| Special character | `"#"` | `uint8('#')` | `[35]` |
| Numeric | `"81"` | `uint8('81')` | `[56 49]` |
| Alphabet | `"End"` | `uint8('End')` | `[69 110 100]` |

You can also specify this parameter using the hexadecimal representation
of the ASCII characters.

#### Dependencies

To enable this parameter, set **Send mode** to
`write`.

### **Label** — Title for data character vector

Specify a title for that data you want to print over the Arduino serial port.

#### Dependencies

To enable this parameter, set **Send mode** to
`print` or `println`.

### **Format** — Data printing format `Decimal` (default) | `Hexadecimal` | `Binary` | `Octal`

Select the format in which you want to print data over the Arduino serial port.

#### Dependencies

To enable this parameter, set **Send mode** to
`print` or `println`.

### **Precision** — Precision of decimal data format `2` (default) | positive integer

Specify the precision of the decimal data format that the Arduino hardware transmits over serial communication.

#### Dependencies

To enable this parameter, set **Send mode** to
`print` or `println` and
**Format** to `Decimal`.

## Libraries

Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Transmit data over Arduino serial port

Use the Serial Transmit block to transmit a *N*x1 array
of data of variable length over the Arduino® serial port to the serial device.

During simulations without the hardware, this block does not transmit the data. If you use
this block in a Simulink® model that has the Standard Servo Read, Standard Servo Write, or Continuous Servo Write block, use longer sample
times to avoid overruns.

**Warning**

Do not connect the serial port pins to an RS-232 serial interface, such as the DE-9M
connector on a computer, without limiting the voltage. The RS-232 standard allows higher
voltages that can damage your hardware. For more information, read the documentation for
your Arduino hardware.

**Note**

For Arduino Uno, Mega, and Nano boards, the double data type occupies 4 bytes. For
Arduino SAMD, Due, ESP32 compatible, Teensy, and Nano 33 BLE hardware boards, the
double data type occupies 8 bytes.
