---
type: simulink-block
title: 'C28x CAN Transmit'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / C28x'
documentation_page: 'c28xcantransmit'
documentation_source_path: 'ref/c28xcantransmit.html'
language: en
---

# C28x CAN Transmit

## Ports

### Input

### **Msg** — Message data scalar

Input message data.

**Data Types:** `uint8` | `uint16` | `uint32` | `CAN_MESSAGE_TYPE`

## Parameters

### **Module** — CAN module the block configures `CAN_A` (default) | `CAN_B`

Determines the CAN module configured by this instance of the CAN
Transmit block.

### **Mailbox number(0–31)** — Sets value of mailbox number register (MBNR) `1` (default) | integer in the range [0 31]

A unique number from 0 to 15 for standard or from 0 to 31 for enhanced CAN
mode. The number refers to a mailbox area in RAM. In standard mode, the
mailbox number determines priority.

**Note**

In a model, multiple CAN Transmit blocks can have a same
`Mailbox number`. But the same mailbox number
cannot be used by CAN Receive block.

### **Message identifier** — Value of message identifier register (MID) bin2dec('111000111') (default) | numeric identifier of length 11 or 29 bits

The message identifier is 11 bits long for the standard frame size or 29
bits long for the extended frame size in decimal, binary, or hex. For binary
and hex formats, use `bin2dec(' ')` and `hex2dec('
')`, respectively, to convert the entry. The message identifier
is coded into a message that is sent to the CAN bus.

**Note**

CAN messages use the value of the message identifier parameter in
the CAN Pack block for transmission when it is used
with C28x CAN Transmit block to create the CAN
message.

### **Message type** — Message identifier type `Standard (11-bit identifier)` (default) | `Extended (29-bit identifier)`

The message identifier type.

### **Enable blocking mode** — Sets blocking mode `off` (default) | `on`

If selected, the CAN block waits indefinitely for a transmit (XMT)
acknowledgment. If not selected, the CAN block does not wait for a transmit
(XMT) acknowledgment, which is useful if the hardware fails to acknowledge
transmissions.

### **Post interrupt when message is transmitted** — Posts asynchronous interrupt when message is transmitted `off` (default) | `on`

When selected, this block posts an asynchronous interrupt when data is
transmitted.

### **Interrupt Line** — Interrupt line of asynchronous interrupt `0` (default) | `1`

The interrupt line the asynchronous interrupt uses. The value of this
parameter sets bit 2 (GIL) in the global interrupt mask register
(CANGIM):

- `1` maps the global interrupts to the
  CAN1INT line.
- `0` maps the global interrupts to the
  CAN0INT line.

**Note**

For information about setting the timing parameters of the CAN module,
see Configuring Timing Parameters for CAN Blocks.

#### Dependencies

This parameter appears only when **Post interrupt when
message is transmitted** is selected.

## Libraries

C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C281x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28p65x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Enhanced Controller Area Network transmit mailbox

The CAN Transmit block generates source code for transmitting enhanced
Controller Area Network (CAN) messages through an CAN mailbox. CAN modules on the
processor provide serial communication capability and have 32 mailboxes configurable for
receive or transmit. This block supports CAN data frames in standard or extended format.

**Note**

Fixed-point inputs are not supported by this block.

The block supports CAN or DCAN depending upon the type of C2000 processors.

Configure the CAN modules for a specific hardware board by navigating to **Hardware Implementation** > **Target hardware resources**. Verify that these settings meet the requirements of your
application.
