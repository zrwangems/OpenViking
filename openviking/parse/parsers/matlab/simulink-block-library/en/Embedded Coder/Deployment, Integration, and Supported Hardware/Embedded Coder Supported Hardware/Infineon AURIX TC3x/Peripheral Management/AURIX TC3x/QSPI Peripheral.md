---
type: simulink-block
title: 'QSPI Peripheral'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC3x / Peripheral Management / AURIX TC3x'
documentation_page: 'qspiperipheral'
documentation_source_path: 'infineonaurixtc3x/ref/qspiperipheral.html'
language: en
---

# QSPI Peripheral

## Ports

### Input

### **SDO** — Serial data out `scalar` | `vector`

The port inputs the data to be communicated with peripheral device.
The datatype is based on the block mask configuration.

#### Dependencies

To enable this port, set the **Transfer mode** parameter
to `SPI Transmit`.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **SDImsg** — SoC Blockset simulation message `scalar`

If the **Transfer mode** is set to `SPI
Receive`, the QSPI block converts the SoC message
**SDImsg** into output data at the **SDI**
output port during simulation.

#### Dependencies

To enable this port, select the **Enable simulation
port** parameter and set the port type as **SoC Data
(Message based)**.

### **SDIsig** — Simulink based simulation signal `scalar` | `vector`

If the **Transfer mode** is set to `SPI
Receive`, this input port acts as pass-through with the
**SDI** output of QSPI block during simulation.

#### Dependencies

To enable this port, select the **Enable simulation
port** parameter and set the port type as
**Signal**.
### Output

### **SDI** — Serial data in `scalar` | `vector`

The port outputs the data received from the peripheral device. The
output datatype is based on the block mask configuration.

#### Dependencies

To enable this port, set the **Transfer mode** parameter
to `SPI Receive`.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **status** — Status of QSPI `scalar`

The block outputs the status of the data that was received, or the errors
that occurred during the data transmission and reception, as a
`unit16` scalar value

|  |  |
| --- | --- |
| **Bit** | **Status** |
| `Bit 0` | Transaction successful |
| `Bit 1` | Busy |
| `Bit 2` | Parity Error |
| `Bit 3` | Configuration Error |
| `Bit 4` | Baud Rate Error |
| `Bit 5` | Transmit buffer (Tx FIFO) Overflow Error |
| `Bit 6` | Tx FIFO Underflow Error |
| `Bit 7` | Receive buffer (Rx FIFO) Overflow Error |
| `Bit 8` | Rx FIFO Underflow Error |
| `Bit 9` | Timeout Error |
| `Bit 10` | SLSI Misplaced Inactivation |

For example, the status of 17 (sets 4th and
0th bit) represents successful transaction with
baud rate error.

#### Dependencies

To enable this port, select the **Enable status port**
parameter.

**Data Types:** `uint16`

### **SDOmsg** — SoC simulation message `scalar`

If the **Transfer mode** is set to `SPI
Transmit`, this port outputs the data received at
**SDO** port in message form during simulation.

#### Dependencies

To enable this port, select the **Enable simulation
port** parameter and set the port type as **SoC Data
(Message based)**.

### **SDOsig** — Simulink based simulation signal `scalar` | `vector`

If the **Transfer mode** is set to either `SPI
Transmit`, this port outputs the data received at
**SDO** port during simulation.

#### Dependencies

To enable this port, select the **Enable simulation
port** parameter and set the port type as
**Signal**.

## Parameters

### Basic

### **Transfer mode** — Select data type transfer `SPI Receive` (default) | `SPI Transmit`

Select the QSPI transfer mode.

- `SPI Transmit` - In this transfer mode, you
  can transmit the data without waiting to receive. Before
  initiating the data transfer, ensure the status is
  `1` i.e. not in progress from the QSPI
  Receive block.

  When you select this transfer mode, the block configures an
  input port, `SDO`.

  **Note**

  QSPI Receive block is responsible to handle the
  receive data from the peripheral device. In other words
  both QSPI Transmit block and QSPI Receive block must be
  used to complete the data transfer.
- `SPI Receive` - In this transfer mode, you
  can receive the data from peripheral device.

  When you select this transfer mode, the block configures an
  output port, `SDI`.

  **Note**

  The data should be transmitted using QSPI Transmit
  block before receiving the data. In other words, both
  QSPI Transmit and QSPI Receive block must be used to
  complete the data transfer.

### **Data bits** — Select data bits `32` (default) | `2` | `3` | `...`

Data bits parameter provides the frame length of each data element in
the QSPI communication. If the selected data bits is in the range:

- `2 to 8` - the valid data types are
  `int8` or
  `unit8`.
- `9 to 16` - the valid data types are
  `int16` or
  `unit16`.
- `17 to 32` - the valid data types are
  `int32` or
  `unit32`.

### **Enable status port** — Enable to configure output status port `off` (default) | `on`

Select this parameter to output status of data transfer.

When you select the output Status parameter, the block configures an output
port, Status.

### **Sample time** — Frequency at which block reads input data `-1` (default) | `scalar` | `vector`

Specify in seconds how often the block should read the input
data.

When you specify this parameter as `-1`, Simulink® determines the best sample time for the block based on the
block context within the model.

#### Dependencies

To enable this parameter, set the **Transfer
mode** to the `SPI Receive`

### **Enable simulation port** — Enable peripheral simulation ports in the block `off` (default) | `on`

Select this parameter to enable peripheral simulation capability.

### **Port Type** — Specify the type of peripheral simulation port `SoC Data (Message based)` (default) | `Signal`

Select this parameter to configure either the SoC compatible or the
Simulink signal based simulation ports to enable peripheral simulation
capability.

#### Dependencies

To view this parameter, select the **Enable simulation
port** parameter.

### Advanced

### **Output data length** — Specify data length to be received `1` (default) | `positive integer`

Specify the data length to be received from the peripheral
device.

**Note**

The data length specified must match the data transmitted using
QSPI Transmit block.

#### Dependencies

To enable this parameter, set the **Transfer
mode** to the `SPI Receive`

### **Output data type** — Select output data type option vary based on the value of Data bits parameter

Select the supported data types based on the data bits
selected.

#### Dependencies

To enable this parameter, set the **Transfer mode** to
`SPI Receive`.

## Libraries

Embedded Coder Support Package for Infineon AURIX TC3x Microcontrollers / AURIX TC3x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024a**

## Description

Write data to and read data from an SPI peripheral device

Write data to and read data from an SPI peripheral device

The Queued Synchronous Peripheral Interface (QSPI) Peripheral block accepts 1-D array of
data type `int8`, `uint8`, `int16`,
`uint16`, `int32`, and `uint32`. The
block outputs an array of the same size and data type as the input values.
