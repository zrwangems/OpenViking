---
type: simulink-block
title: 'SENT'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC3x / Peripheral Management / AURIX TC3x'
documentation_page: 'sent'
documentation_source_path: 'infineonaurixtc3x/ref/sent.html'
language: en
---

# SENT

## Ports

### Input

### **DataSel** — Data selection based on features or sensors configured `scalar`

This input port requests data based on sensor or feature selection
configuration in SENT Configuration.

**Note**

- You can provide the input as 1, 2 or 3 if you select **SPC
  Mode** parameter as `Feature
  selection`.
- You can provide the input as 1, 2, 3 or 4 (based on the number of
  sensors interfaced on SENT channel) if you select **SPC
  Mode** parameter as `Sensor
  selection`.

#### Dependencies

To enable this port, set the **SENT Protocol** as
**SPC Mode** and select the **SPC
Mode**parameter as `Feature selection`
or `Sensor selection`.

**Data Types:** `uint8`
### Output

### **Data** — 32-bit data `scalar` | `vector`

The block outputs 32-bit value that represents the sensor data, packing 8
nibbles (4-bit data) together.

**Data Types:** `uint32`

### **Serial-data** — 16-bit serial data `scalar` | `vector`

The block outputs the 16-bit serial data that represents the sensor
data.

#### Dependencies

To enable this port, select the **Serial**
parameter.

**Data Types:** `uint16`

### **Status & Comm** — Status and Communication nibble data (one nibble) `scalar`

The block outputs the Status and Communication nibble data sent by the
sensor (1st nibble information), which generally
provides diagnostic information like fault data, part numbers, and so
on.

#### Dependencies

To enable this port, select the **Status and communication nibble** parameter.

**Data Types:** `uint8`

### **Channel status** — Status of read operation over SENT protocol `scalar`

The block outputs the status of the data that was read, or the errors that
occurred during the data transfer, as a `unit32` scalar
value.

| Bit | Status | Description |
| --- | --- | --- |
| Bit 0 | Receive success | This bit is set at the successfully received end of a frame. If CRC check is enabled, it also indicates successful CRC check. |
| Bit 1 | Receive data success | This bit is set when received frame is moved to data register. Both RSI and RDI. |
| Bit 2 | Receive buffer overflow | This bit is set when new data is received while older one is still not read from data register. Older data gets overwritten by new data. |
| Bit 3 | Transfer data | This bit is set after the trigger condition was detected. Data to be transferred has been moved internally and new value can be written in SPC control register. |
| Bit 4 | Transmit buffer underflow | This bit is set after data has been successfully transferred and no new data was written to SPC control register. |
| Bit 5 | Frequency range error | This bit is set after a Synchronization / Calibration pulse was received that deviates more than +/- 25% from the nominal value. |
| Bit 6 | Frequency drift error | This bit is set after a subsequent Synchronization / Calibration pulse was received that deviates more than 1.5625% from its predecessor. |
| Bit 7 | Wrong number of nibbles received | This bit is set if less/more nibbles have been received than expected. |
| Bit 8 | Nibbles value out of range | This bit is set if value off Nibble is not in range. It is less than 0 or greater than 15. |
| Bit 9 | CRC error | This bit is set when CRC fails. |
| Bit 10 | Wrong SC Nibble | This bit is set if Status and Communication nibble shows a start bit in a frame other than frame number nx16. |
| Bit 11 | Serial data received | This bit is set after all serial data bits are received using the Status and Communication nibble. |
| Bit 12 | Serial data CRC error | This bit is set if the CRC of the serial message fails. |
| Bit 13 | Watch dog error | This bit is set if watchdog timer of the channel has expired. |

#### Dependencies

To enable this port, select the **Enable channel status
port** parameter.

**Data Types:** `uint32`

## Parameters

### Basic

### **Data format selection** — Select data format `None` (default) | `Serial` | `Status and Communication Nibble`

Select the data format.

- `Serial` - In this data format, the block outputs
  serial data based on the SENT protocol.

  When you select this option, the block configures the
  `Serial-data` output port.
- `Status and Communication Nibble` - In this data
  format, the block provides the Status and Communication nibble data based
  on the SENT protocol.

  When you select this option, the block configures the `Status
  & Comm` output port.

### **Enable channel status port** — Enable output data that specifies data read status and error `off` (default) | `on`

Enable output data that specifies data read status and errors (if any) based
on bit-wise categorization.

### **Sample time** — Frequency at which block reads the received data `-1` (default) | `scalar` | `vector`

Specify in seconds how often the block should read the received data.

When you specify this parameter as `-1`, Simulink® determines the best sample time for the block based on the block
context within the model.

### Advanced

### **SENT Protocol** — Select the SENT protocol `Standard` (default) | `SPC`

Select SENT protocol as standard or short PWM code (SPC) transmission for
the channel.

Selection of this parameter as `SPC` enables
options in **Advanced** tab in the SENT Configuration .

### **SPC Mode** — Mode of SPC transmission `Synchronization` (default) | `Feature selection` | `Sensor selection`

Select mode of SPC transmission.

Selection of this parameter enables the related parameters in the SENT Configuration.

#### Dependencies

To view this parameter, set the **SENT Protocol**
parameter as `SPC Mode`.

## Libraries

Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / AURIX TC3x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024b**

## Description

Read high-resolution sensor data over Single Edge Nibble Transmission (SENT) protocol

The SENT block reads high-resolution data from sensor and provides 32-bit data output
based on SENT (Single Edge Nibble Transmission) protocol (SAE J2716). The output based on
SENT protocol is a unidirectional signal from sensor to controller, encoding sensor data
information in the form of nibbles (4-bit data), packing 8 nibbles together.

The block also provides the options to enable additional outputs about the Status and
Communication nibble, serial data, and the status of data reception.
