---
type: simulink-block
title: 'On-board CAN Transmit'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / CAN'
documentation_page: 'onboardcantransmit'
documentation_source_path: 'supportpkg/arduino_ref/onboardcantransmit.html'
language: en
---

# On-board CAN Transmit

## Ports

### Input

### **Message** — Transmitted CAN messages message vector

The block accepts CAN messages in raw or CAN message formats.

- Raw data — To accept the message as a `uint8` vector array,
  set Data is input as to
  `Raw data`.
- CAN message — To accept the message in the CAN message format, set Data is input as to
  `CAN Msg`.

**Data Types:** `uint8` | `CAN Msg`
### Output

### **Status** — Status of output CAN message scalar

The block outputs CAN message transmission status.

Arduino Due board uses these transmission statues.

- `1` — The CAN controller transmits data successfully on to
  the CAN network.
- `0` — The CAN controller cannot transmit data successfully
  on to the CAN network or if the transmission CAN mailbox is full.

Arduino Teensy boards use these transmission statues.

- `-2` — Value in the transmit error counter (TEC) is >= 96
  due to CAN controller failure or accumulation of transmission errors.
- `-1` — The CAN controller cannot transmit data successfully
  on to the CAN network or if no transmit mailboxes are available to transmit data
  on to the CAN network.
- `0` — No transmission queue available.
- `1` — The CAN controller transmits data successfully on to
  the CAN network.

#### Dependencies

- To enable this port, select **Output status**.

**Data Types:** `uint8`

## Parameters

### **CAN module** — CAN controller `CAN0` (default) | `CAN1` | `CAN2` | `CAN3`

Select the CAN controller according to the Arduino board you use.

| Arduino Boards | Supported CAN Controller |
| --- | --- |
| Arduino Due | CAN0 and CAN1 |
| Arduino compatible Teensy 4.0 and 4.1 | CAN1, CAN2, and CAN3 |

For more information on how to assign or view the Arduino board pins for the On-board CAN Receive block, click
**View pin map**.

### **Data is input as** — Data input type `Raw data` (default) | `CAN Msg`

Select the input message type.

- `Raw data` — Select this option to accept the input
  message as a 1-by-*N*
  `uint8` array.
- `CAN Msg` — Select this option to accept the input
  message in CAN message format.

  Perform these steps to accept message in CAN message format.

  - To your Simulink® model, add a CAN Pack (Vehicle Network Toolbox) from the Vehicle Network Toolbox™.
  - Connect the output of the CAN Pack (Vehicle Network Toolbox) to the input port of the
    On-board CAN Transmit block.
  - Using the options in the **Data is input as** list of
    the CAN Pack (Vehicle Network Toolbox) block, specify if you want to
    create your messages or you want to upload a CAN database file. If you
    choose to upload a CAN database file, the CAN Pack inherits the message
    properties from the uploaded file.

On-board CAN Transmit and CAN Pack blocks connections

### **Output status** — Status of data transmission `off` (default) | `on`

Select this option to request status of CAN message transmission.

### Message

To enable the parameters under the **Message** section, set
**Data is input as** to `Raw data`.

### **Identifier type** — CAN identifier type `Standard (11-bit identifier)` (default) | `Extended (29-bit identifier)`

Specify the CAN identifier type.

- `Standard (11-bit identifier)` — Use this option to
  transmit CAN messages with a standard 11-bit identifier.
- `Extended (29-bit identifier)` — Use this option to
  transmit CAN messages with an extended 29-bit identifier.

### **Message ID** — CAN message identifier `100` (default) | numeric identifier of length `11` or `29` bits

Specify the message identifier, which is 11 bits long for the standard CAN frame
size or 29 bit long for the extended CAN frame size. You can specify the value in
decimal, binary, or hexadecimal. For binary and hexadecimal formats, use `bin2dec` and `hex2dec`, respectively. The message
identifier is coded into a message that is sent to the CAN bus.

### **Message length** — CAN message length `8` (default) | positive integer [1, 8]

Specify the length of CAN message in bytes.

### **Remote frame** — Identify remote frames `off` (default) | `on`

Select this option to identify if the data frame the block transmits on the CAN
network is a remote frame or not.

## Libraries

Simulink Support Package for Arduino Hardware / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024b**

## Description

Transmit messages to CAN network using on-board Arduino CAN controller

Use the On-board CAN Transmit block to transmit CAN messages from the
on-board Arduino® CAN controller. The block transmits messages from the mailboxes into the CAN
network in a first-in, first-out method at every sample time.

### Supported Arduino Boards

- Arduino Due
- Arduino compatible Teensy 4.0 and 4.1
