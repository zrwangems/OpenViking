---
type: simulink-block
title: 'C28x CAN Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / C28x'
documentation_page: 'c28xcanreceive'
documentation_source_path: 'ref/c28xcanreceive.html'
language: en
---

# C28x CAN Receive

## Ports

### Output

### **f()** — Function call port scalar

Connect a function call subsystem to this port. When a new message is
received, the subsystem is executed.

### **Msg** — Message data port vector

The received data is output in the form of a vector of elements of the
selected data type. The length of the vector is 8 bytes. When the block
is used in polling mode, and a new message is not created between
consecutive executions of the block, the existing message is
repeated.

To use the CAN Receive block with the CAN
Unpack block in the `canmsglib` library,
set **Data type** to
`CAN_MESSAGE_TYPE`.

**Data Types:** `uint8` | `uint16` | `uint32` | `CAN_MESSAGE_TYPE`

### **len** — Length of output message scalar

The length of output message received in bytes.

#### Dependencies

This port appears only if the **Output message
length** parameter is selected.

**Data Types:** `uint16`

### **ID** — Output message identifier scalar

The port outputs message identifier of received message.

#### Dependencies

To enable this port, select **Output message ID**
parameter.

**Data Types:** `uint32`

## Parameters

### **Module** — CAN module the block configures `CAN_A` (default) | `CAN_B`

Determines the CAN module configured by the CAN Receive
block.

### **Mailbox number(0–31)** — Sets value of mailbox number register (MBNR) `0` (default) | integer in the range [0 31]

For standard CAN controller (SCC) mode, enter a unique number from
`0` to `15`. For high-end CAN
controller (HECC) mode, enter a unique number from `0` to
`31`. In SCC mode, transmissions from the mailbox with
the highest number have the highest priority. In HECC mode, the mailbox
number only determines priority if the transmit priority level (TPL) of two
mailboxes is equal.

**Note**

In a model, the same mailbox number cannot be used by either CAN
Transmit block or other CAN Receive blocks.

### **Message identifier** — Sets value of message identifier register (MID) bin2dec('111000111') (default) | numeric identifier of length 11 or 29 bits

The message identifier is 11 bits long for the standard frame size or 29
bits long for the extended frame size in decimal, binary, or hex format. For
binary and hex formats, use `bin2dec(' ')` and
`hex2dec(' ')`, respectively, to convert the
entry.

### **Message type** — Message identifier type `Standard (11-bit identifier)` (default) | `Extended (29-bit identifier)`

The message identifier type.

### **Enable acceptance filter** — Enable to use ID filtering `off` (default) | `on`

Enable this parameter to use ID filtering. ID filtering depends on
**Message type (Standard or extended)** ,
**Message identifier** and **Message identifier
mask**.

CAN module scans the received message ID's and compares it with the filter
mask. Received messages which pass the acceptance filtering are stored into
the message RAM.

**Note**

Acceptance filtering in self test mode is only supported for specific
processors. F2805x/F2806x and older processors does not support
acceptance filtering in self test mode.

### **Message identifier mask** — identifier mask `0` (default) | `1` | numeric identifier of length 11 or 29 bits

The **Message identifier mask** is 11 bits long for the
standard frame size or 29 bits long for the extended frame size in decimal,
binary, or hex format. For binary and hex formats, use `bin2dec('
')` and `hex2dec(' ')`, respectively, to
convert the entry.

- 0 - if the bit in **Message identifier mask** is
  set to `0`, then corresponding bit in the
  **Message identifier** will not be considered
  for acceptance filtering.
- 1 - if the bit in **Message identifier mask** is
  set to `1`, then corresponding bit in the
  **Message identifier** will be considered for
  acceptance filtering.

#### Dependencies

To enable **Message identifier mask parameter**,
select **Enable acceptance filter**.

### **Sample time** — Frequency at which mailbox is polled for new message `1` (default) | `-1` | scalar

A new message causes a function call to be sent from the mailbox. If you
want to update the message output only when a new message arrives, the block
needs to be executed asynchronously. To execute the block asynchronously,
set this parameter to `-1`, and select the **Post
interrupt when message is received** option.

**Note**

For information about setting the timing parameters of the CAN
module, see Configuring Timing Parameters for CAN Blocks.

### **Data type** — Output message data type `uint16` (default) | `uint8` | `uint32` | `CAN_MESSAGE_TYPE`

The options available are:

- `uint8`: Vector length = 8
  elements
- `uint16`: Vector length = 4
  elements
- `uint32`: Vector length = 2
  elements
- `CAN_MESSAGE_TYPE`: Outputs data as a
  structure. Use the CAN Unpack block to extract the
  data from the structure.

The length of the vector for the received message is at most 8 bytes. If
the message is less than 8 bytes, the data buffer bytes are right-aligned in
the output. The data are unpacked as follows using the data buffer, which is
8 bytes.

For `uint8` data, the CAN Receive
block reads each unit of 8 bytes in the registers and outputs 8-bit data to
eight elements (using the lower part of the 16-bit memory).

```
Output[0] = data_buffer[0];
Output[1] = data_buffer[1];
Output[2] = data_buffer[2];
Output[3] = data_buffer[3];
Output[4] = data_buffer[4];
Output[5] = data_buffer[5];
Output[6] = data_buffer[6];
Output[7] = data_buffer[7];
```

For `uint16` data, the CAN Receive
block reads each unit of 8 bytes in the registers and outputs 16-bit data to
four elements.

```
Output[0] = data_buffer[1..0];
Output[1] = data_buffer[3..2];
Output[2] = data_buffer[5..4];
Output[3] = data_buffer[7..6];
```

For `uint32` data, the CAN Receive
block reads each unit of 8 bytes in the registers and outputs 32-bit data to
two elements.

```
Output[0] = data_buffer[3..0];
Output[1] = data_buffer[7..4];
```

For example, if the received message has two bytes:

```
data_buffer[0] = 0x21
data_buffer[1] = 0x43
```

The `uint16` output is:

```
Output[0] = 0x4321
Output[1] = 0x0000
Output[2] = 0x0000
Output[3] = 0x0000
```

When you select `CAN_MESSAGE_TYPE`, the block outputs the
following struct data (defined in `can_message.h`):

```
struct {

  /* Is Extended frame */
  uint8_T Extended;

  /* Length */
  uint8_T Length;

  /* RTR */
  uint8_T Remote;

  /* Error */
  uint8_T Error;

  /* CAN ID */
  uint32_T ID;

  /*
  TIMESTAMP_NOT_REQUIRED is a macro that will be defined by Target teams
  PIL, if they do not require the timestamp field during code
  generation. By default, timestamp is defined. If the targets do not require
  the timestamp field, they should define the macro TIMESTAMP_NOT_REQUIRED before
  including this header file for code generation.
  */
  #ifndef TIMESTAMP_NOT_REQUIRED
    /* Timestamp */
    double Timestamp;
  #endif

  /* Data field */
  uint8_T Data[8];

};
```

#### Limitations

The following are the limitations when **Data type**
is set as `CAN_MESSAGE_TYPE`.

- CAN unpack status can be used for data validity only when
  CAN unpack is directly connected to CAN Receive block
  without **function trigger** and
  **Action when message not received** to
  `Reset all fields to zero`.
- CAN unpack status will not be valid in any case if
  **Action when message not received** of
  CAN Receive block is set to `Output last received
  values`.
- Always use function trigger as indication of status with
  or without CAN unpack block for all scenarios.

### **Initial output** — Sets output before receiving data `0` (default) | integer

The value of the output before receiving data. You can specify the initial
output values based on the **Data type** selected.

### **Action when message not received** — Action when no new CAN message received `Output last message received` (default) | `Reset all fields to zero`

Select an action when no new CAN message is received. You can either
choose `Output last message received` or `Reset all
fields to zero`.

### **Output message ID** — Output message identifier status `off` (default) | `on`

When you select the **Output message ID** parameter, the
block configures an output port, **ID**. The port outputs
the status of output message identifier.

#### Dependencies

To enable **Output message ID**, select
**Enable acceptance filter**.

### **Output message length** — Output message length in bytes `off` (default) | `on`

The message length in bytes, sent to the **len** port. If
not selected, the **len** port is not visible.

### **Post interrupt when message is received** — Posts asynchronous interrupt when message is received `off` (default) | `on`

When selected, the block posts an asynchronous interrupt when a message is
received.

### **Interrupt line** — Interrupt line of asynchronous interrupt `0` (default) | `1`

The interrupt line the asynchronous interrupt uses. The value of this
parameter sets bit 2 (GIL) in the global interrupt mask register (CANGIM):

- `1` maps the global interrupts to the
  CAN1INT line.
- `0` maps the global interrupts to the
  CAN0INT line.

#### Dependencies

This parameter appears only when you select **Post
interrupt when message is received**.

## Libraries

C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p65x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Enhanced Controller Area Network receive mailbox

The CAN Receive block generates source code for receiving enhanced
Controller Area Network (CAN) messages through an CAN mailbox. CAN modules on the
processor provide serial communication capability and have 32 mailboxes configurable for
receive or transmit. The block supports CAN data frames in standard or extended
format.

The block supports CAN or DCAN depending upon the type of C2000 processors.

To use the CAN Receive block with the CAN Pack block in
the `canmsglib` library, set **Data type** to
`CAN_MESSAGE_TYPE`.

Configure the CAN modules for a specific hardware board by navigating to **Hardware Implementation** > **Target hardware resources**. Verify that these settings meet the requirements of your
application.
