---
type: simulink-block
title: 'Serial Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Serial'
documentation_page: 'serialreceive'
documentation_source_path: 'supportpkg/arduino_ref/serialreceive.html'
language: en
---

# Serial Receive

## Ports

### Output

### **Data** — Output data [`Nx1`] array

The block outputs the data it receives from the Arduino serial port. When no data is available on the Arduino serial port, the block outputs zeros.

**Data Types:** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Status** — Status of input data length `0` | `1`

The block outputs the status of the length of the input data that the Arduino serial port receives.

- `0` — Indicates that the length of the input data received
  on the Arduino serial port is less than or equal to the data length specified in
  the **Data length** parameter.
- `1` — Indicates that the length of the input data received
  on the Arduino serial port is more than the data length specified in the
  **Data length** parameter.

#### Dependencies

To enable this parameter, set **Data length option** to
`Length via dialog` or `Length via input
port`.

**Data Types:** `uint8`

### **Length** — Status of read operation scalar

The block outputs length of the data that the Arduino serial port receives.

#### Dependencies

To enable this parameter, set **Data length option** to
`Variable length`.

**Data Types:** `uint8`

## Parameters

### **Port number** — Arduino port number for serial communication `0` (default) | positive integer

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

### **Data type** — Type of output data `uint8` (default) | `double` | `single` | `int8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

Select the data type of the output data.

### Data Frame

### **Data length option** — Data length `Length via dialog` (default) | `Length via input port` | `Variable length`

Select an option to specify the data length.

- `Length via dialog` — The block receives the data
  length from the input you specify in the **Data length**
  parameter.
- `Length via input port` — The block receives the
  data length from its input port.
- `Variable length` — The block receives data until
  the value you specify in the **Terminator**  parameter matches
  the data on the Arduino serial port. The block waits until the timeout value when the data
  is not available on the Arduino serial port. The block also outputs the length of data that the
  Arduino hardware receives on the **Length** output
  port.

### **Data length** — Length of data in bytes `1` (default) | positive integer

Specify the number of data bytes the block must receive on the Arduino serial port for the data type you set in the **Data
type** parameter.

#### Dependencies

To enable this parameter, set **Data length option** to
`Length via dialog`.

### **Maximum data length** — Maximum length of data in bytes `10` (default) | positive integer

Specify the maximum number of data bytes the block should receive on the
Arduino serial port according to the Serial Receive (Instrument Control Toolbox)length specified in the input port.

#### Dependencies

To enable this parameter, set **Data length option** to
`Length via input port`.

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

You can also specify this parameter using the hexadecimal
representation of the ASCII characters.

### **Sample time** — Frequency at which block reads data from Arduino serial port `0.1` (default) | scalar

Specify how often the block reads data available on the Arduino serial port.

### **Timeout (ms)** — Time for which block waits to receive data `0` (default) | positive scalar

Specify the time in milliseconds that the block must wait during each time step if
the data is not available on the Arduino serial port to read. If a timeout occurs, the block aborts the read
operation.

#### Dependencies

To enable this parameter, set **Data length option** to
`Variable length`.

## Libraries

Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2018b**

## Description

Receive data over Arduino serial port

Use the Serial Receive block to receive a *N*x1 array of
data of variable length on the Arduino® serial port.

During simulations without the hardware, this block emits zeroes. If you use this block in
a Simulink® model that has the Standard Servo Read, Standard Servo Write, or Continuous Servo Write block, specify longer
sample times to avoid overruns.

**Warning**

Do not connect the serial port pins to an RS-232 serial interface, such as the DE-9M
connector on a computer, without limiting the voltage. The RS-232 standard allows higher
voltages that can damage your hardware. For more information, read the documentation for
your Arduino hardware.
