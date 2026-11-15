---
type: simulink-block
title: 'CAN Transmit'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Communication'
documentation_page: 'cantransmit'
documentation_source_path: 'nvidia/ref/cantransmit.html'
language: en
---

# CAN Transmit

## Ports

### Input

### **Port1** — Message data vector | scalar

Message data, specified as vector or scalar.

**Data Types:** `uint8` | `CAN Msg`
### Output

### **Port1** — Status vector | scalar

Output status.

#### Dependencies

To enable this parameter, select **Output Status**

## Parameters

### **CAN interface** — CAN device ID can0 (default) | valid CAN ID

Device ID of the CAN controller to use.

### **Set up CAN interface** — Bring up CAN interface `off` (default) | on

Select this parameter to bring up the CAN interface on the NVIDIA target before transmitting CAN frames.

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

### **Data is input as** — Data input type `Raw data` (default) | `CAN Msg`

Data input type used for transmitting messages.

### **Output Status** — Indicates output status `off` (default) | `on`

Select this option to indicate the status of message transfer. Status port outputs
`0` for successful
transmit and error codes in case of failure. Error codes are listed in this
table.

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 00 | 00 | ABTF | MLOA | TXERR | TXBO | TXEP | TXWAR |
| bit7 | bit6 | bit5 | bit4 | bit3 | bit2 | bit1 | bit0 |

ABTF: Message Aborted Flag bit

MLOA: Message Lost Arbitration bit

TXERR: Transmission Error Detected bit

TXBO: Bus-Off Error Flag bit

TXEP: Transmit Error-Passive Flag bit

TXWAR: Transmit Error Warning Flag bit

### **Wait until data sent** — Wait until data is sent `off` (default) | `on`

When selected, the block waits for the time specified in the **Time out
in seconds** parameter before transferring data.

### **Time out in seconds** — Waiting time for sending data 1 (default) | integer

Wait time for transferring data. After the specified time, the block times
out.

#### Dependencies

To enable this parameter, select **Wait until data
sent**.

### **Identifier Type** — Message identifier type `Standard (11-bit identifier)` (default) | `Extended (29-bit identifier)`

Message identifier type.

#### Dependencies

To enable this parameter, set **Data is input as** to
`Raw data`.

### **Message ID** — Message identifier 100 (default) | numeric identifier of length 11 or 29 bits

Message identifier, which is 11 bits long for the standard frame size or 29 bits
long for the extended frame size, specified in decimal, binary, or hex. For binary and
hex formats, use `bin2dec(' ')` and `hex2dec(' ')`,
respectively, to convert the entry. The message identifier is coded into a message that
is sent to the CAN bus.

#### Dependencies

To enable this parameter, set **Data is input as** to
`Raw data`.

### **Message Length** — Length of message 8 (default) | positive integer

Message length.

#### Dependencies

To enable this parameter, set **Data is input as** to
`Raw data`.

### **Request Remote Frame** — Enable remote message `off` (default) | `on`

When selected, this block sends request for remote frames.

#### Dependencies

To enable this parameter, set **Data is input as** to
`Raw data`.

## Libraries

NVIDIA Jetson and NVIDIA DRIVE / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021b**

## Description

Transmit messages on the controller area network (CAN) bus

The CAN Transmit block transmits messages on the CAN bus through the time
triggered CAN (TTCAN) controller available on NVIDIA® embedded boards. This block uses the SocketCAN interface to communicate with the
CAN controller hardware on NVIDIA boards.

You can also use this block to interact with a virtual CAN interface. A virtual CAN
interface allows transmission and reception of CAN frames without a native CAN interface
associated with real hardware. For more information on how to set up a virtual CAN interface,
see Setup Virtual CAN Interface.

The CAN Transmit block supports `Raw data` and
`CAN Msg` as input types. To use CANdb (CAN database) file or to
specify signals manually, use `CAN Msg` input type and CAN
Pack block. The CAN Pack block is available from the Vehicle Network Toolbox™.
