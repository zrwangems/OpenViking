---
type: simulink-block
title: 'CAN Receive'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Communication'
documentation_page: 'canreceive'
documentation_source_path: 'nvidia/ref/canreceive.html'
language: en
---

# CAN Receive

## Ports

### Output

### **Data** — Message data port vector | scalar

Received message data, returned as a vector or scalar.

If **Data to be output as** is set to `Raw
data`, the received message data is an 1-by-N array of type
`uint8`.

If **Data to be output as** is set to `CAN
Msg`, the data port is renamed to **CAN Msg** and the
received message data is output as a Simulink® bus signal. To extract data from Simulink bus signal, use the CAN Unpack block from Vehicle Network Toolbox.

**Data Types:** `uint8` | `CAN Msg`

### **Status** — Status of output message scalar

Status of the received output message.

**Data Types:** `uint8`

### **Error** — Error codes scalar

Error codes.

#### Dependencies

To enable this parameter, select **Output Error**.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 00 | 00 | 00 | 00 | RXWAR | RXEP | RX0OVR | RX1OVR |
| bit7 | bit6 | bit5 | bit4 | bit3 | bit2 | bit1 | bit0 |

RX1OVR: Receive Buffer 1 Overflow Flag bit

RX0OVR: Receive Buffer 0 Overflow Flag bit

RXEP: Receive Error-Passive Flag bit

RXWAR: Receive Error Warning Flag bit

### **Remote** — Remote message flag scalar

Remote message flag.

#### Dependencies

To enable this parameter, select **Output
Remote**.

## Parameters

### **CAN interface** — CAN interface name can0 (default) | valid device name

Specify the name of the real or virtual CAN interface to use.

### **Set up CAN interface** — Bring up CAN interface `off` (default) | on

Select this parameter to bring up the CAN interface on the NVIDIA target before receiving CAN frames.

### **CAN interface type** — Type of CAN interface `Real` (default) | `Virtual`

Select the type of CAN interface.

- If the CAN interface type is `Real`, set this
  parameter to `Real`. Setting this parameter to
  `Real` would not bring up the CAN interface in these
  scenarios.

  - The interface is already brought up on the target with a CAN-Bus Speed
    that does not match with the **CAN Bus
    Speed (kBit/s)** parameter. The block would not transmit the CAN
    frames. Bring the existing interface down before enabling this
    parameter.
  - If the interface is already brought up on the target with the CAN-Bus
    Speed that matches with the **CAN Bus
    Speed (kBit/s)** parameter. The block will transmit the CAN
    frames.
- If the CAN interface type is `Virtual`, set this
  parameter to `Virtual`.

#### Dependencies

To enable this parameter, select **Set up CAN
interface**.

### **Data to be output as** — Data output type `Raw data` (default) | `CAN Msg`

Data type used for receiving messages.

### **Identifier Type** — Message identifier type `Standard (11-bit identifier)` (default) | `Extended (29-bit identifier)`

Message identifier type.

#### Dependencies

To enable this parameter, set **Data to be output as** to
`Raw data`.

### **Message ID** — Message identifier 100 (default) | numeric identifier of length 11 or 29 bits

Message identifier, which is 11 bits long for the standard frame size or 29 bits
long for the extended frame size, specified in decimal, binary, or hex. For binary and
hex formats, use `bin2dec(' ')` and `hex2dec(' ')`,
respectively, to convert the entry. The message identifier is coded into a message that
is sent to the CAN bus.

#### Dependencies

To enable this parameter, set **Data to be output as** to
`Raw data`.

### **Message Length** — Length of message 8 (default) | positive integer

Message length.

#### Dependencies

To enable this parameter, set **Data to be output as** to
`Raw data`.

### **Sample time (seconds)** — Time frequency at which block receives data `0.1` (default) | `scalar`

Specify how often the block should read the port buffer. Enter a value greater than
`0` or `-1` (for inherited sample time).

When you specify this parameter as-1, Simulink determines the best sample time for the block based on the block context
within the model.

This value defaults to a sample time of `0.1` seconds. Smaller
values require the processor to complete the same number of instructions in less time
and this can cause task overruns.

### **Output Error** — Output error codes `off` (default) | on

Select to output error codes if the message transfer fails.

### **Output Remote** — Enable remote messages `off` (default) | on

Select to output remote messages.

## Libraries

NVIDIA Jetson and NVIDIA DRIVE / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

## Description

Receive messages from the controller area network (CAN) bus

The CAN Receive block receives messages from the CAN bus through the time
triggered CAN (TTCAN) controller available on NVIDIA® embedded boards. This block uses the SocketCAN interface to communicate with the
CAN controller hardware on NVIDIA boards.

You can also use this block to interact with a virtual CAN interface. A virtual CAN
interface allows transmission and reception of CAN frames without a native CAN interface
associated with real hardware. For more information on how to set up a virtual CAN interface,
see Setup Virtual CAN Interface.

The CAN Receive block supports `Raw data` and
`CAN Msg` as output types. To use CANdb (CAN database) file or to
specify signals manually, use `CAN Msg` output type and CAN
Unpack block. The CAN Unpack block is available from the Vehicle Network Toolbox™.
