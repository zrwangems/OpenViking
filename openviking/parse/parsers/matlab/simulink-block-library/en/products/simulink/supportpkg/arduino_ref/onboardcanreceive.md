---
type: simulink-block
title: 'On-board CAN Receive'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / CAN'
documentation_page: 'onboardcanreceive'
documentation_source_path: 'supportpkg/arduino_ref/onboardcanreceive.html'
language: en
---

# On-board CAN Receive

## Ports

### Output

### **Data** — Data from Arduino on-board CAN controller message vector

The block outputs CAN data read from the on-board Arduino CAN controller. To output the CAN data as a `uint8`
message vector, set Data to be output as to
`Raw data`. To output the data in CAN message format, set
Data to be output as to
`CAN Msg`.

#### Dependencies

- To enable this port, set Data to be output as to
  `Raw data`.

**Data Types:** `uint8` | `CAN Msg`

### **Status** — Status of input CAN message `0` | `1`

The block outputs CAN message read status.

- The status is `1`, if the block reads new CAN
  message.
- The status is `0`, if the block reads no new CAN
  message.

#### Dependencies

- To enable this port, set **Data to be output as** to
  `Raw data`.

**Data Types:** `uint8`

### **Error** — Error status for CAN message `0` | `1`

The block outputs the CAN message error status.

- The status is `1`, if the input CAN message contains an
  error.
- The status is `0`, if the input CAN message to the block
  has no error.

#### Dependencies

- To enable this port, set Data to be output as to
  `Raw data` and select **Output
  error**.

**Data Types:** `uint8`

### **Remote** — Status for remote frames scalar

The block outputs the remote message frame status.

- The status is `1`, if the incoming CAN data is a remote
  frame.
- The status is `0`, if the incoming CAN data is not a remote
  frame.

#### Dependencies

- To enable this port, set **Data to be output as** to
  `Raw data` and select **Output
  remote**.

**Data Types:** `uint8`

### **CAN Msg** — Received CAN messages `arduinoCANMsg` | bus

The block outputs CAN messages at a particular timestamp as a signal bus or
`arduinoCANMsg`.

#### Dependencies

- To enable this port, set **Data to be output as** to
  `CAN Msg`.

**Data Types:** `uint8` | `bus`

## Parameters

### **CAN module** — CAN controller `CAN0` (default) | `CAN1` | `CAN2` | `CAN3`

Select the CAN controller according to the Arduino board you use.

| Arduino Boards | Supported CAN Controller |
| --- | --- |
| Arduino Due | CAN0 and CAN1 |
| Arduino compatible Teensy 4.0 and 4.1 | CAN1, CAN2, and CAN3 |

For more information on how to assign or view the Arduino board pins for the On-board CAN Receive block, click
**View pin map**.

### **Data to be output as** — Data output type `Raw data` (default) | `CAN Msg`

Select an output message type.

- `Raw data` — Select this option to read message as a
  1-by-*N*
  `uint8` array.
- `CAN Msg` — Select this option to read message in CAN
  message format.

  Perform these steps to read message in CAN message format.

  - To your Simulink model, add a CAN Unpack (Vehicle Network Toolbox) from the Vehicle Network Toolbox™.
  - Connect the output of the On-board CAN Receive block to
    the input of the CAN Unpack (Vehicle Network Toolbox) block.
  - Using the options in the **Data to be output as** list
    of the CAN Unpack (Vehicle Network Toolbox) block, specify if you want
    to create your messages or you want to upload a CAN database file. If you
    choose to upload a CAN database file, the CAN Unpack inherits the message
    properties from the uploaded file.

On-board CAN Receive and CAN Unpack blocks connections

### **Identifier type** — CAN identifier type `Standard (11-bit identifier)` (default) | `Extended (29-bit identifier)`

Specify the CAN identifier type.

- `Standard (11-bit identifier)` — Use this option to
  create CAN messages with a standard 11-bit identifier.
- `Extended (29-bit identifier)` — Use this option to
  create CAN messages with an extended 29-bit identifier.

#### Dependencies

- To enable this parameter, set **Data to be output as** to
  `Raw data`.

### **Message ID** — CAN message identifier `100` (default) | numeric identifier of length `11` or `29` bits

Specify the message identifier, which is 11 bits long for the standard CAN frame
size or 29 bit long for the extended CAN frame size. You can specify the value in
decimal, binary, or hexadecimal. For binary and hexadecimal formats, use `bin2dec` and `hex2dec`, respectively. The message
identifier is coded into a message that is sent to the CAN bus.

#### Dependencies

- To enable this parameter, set **Data to be output as** to
  `Raw data`.

### **Message length** — CAN message length `8` (default) | positive integer [1, 8]

Specify the length of CAN message in bytes.

#### Dependencies

- To enable this parameter, set **Data to be output as** to
  `Raw data`.

### **Sample time** — Frequency at which block reads CAN message `-1` (default) | nonnegative real value

Specify how often the block reads CAN messages from the on-board Arduino CAN controller, in seconds.

### Message

To enable the parameters under the **Message** section, set
**Data to be output as** to `Raw data`.

### **Output error** — Request error status `off` (default) | `on`

Select this option to request error status of the CAN message. To output the error
in the `CAN Msg` message type, select **Output
error** in the CAN Unpack (Vehicle Network Toolbox) block.

### **Output remote** — Request remote frames `off` (default) | `on`

Select this option to request data from a CAN node. This option enables the
**Remote** output port

## Libraries

Simulink Support Package for Arduino Hardware / Communication

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024b**

## Description

Receive messages using on-board Arduino CAN controller

Use the On-board CAN Receive block to receive CAN messages from the
on-board Arduino® CAN controller. The block stores input messages in mailboxes in a first-in,
first-out (FIFO) method. These mailboxes deliver the CAN messages to your Simulink® model in a queued order at every sample time.

### Supported Arduino Boards

- Arduino Due
- Arduino compatible Teensy 4.0 and 4.1
