---
type: simulink-block
title: 'MCAN Transmit'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Infineon AURIX TC4x / Peripheral Management / AURIX TC4x'
documentation_page: 'mcantransmit'
documentation_source_path: 'infineonaurix/ref/mcantransmit.html'
language: en
---

# MCAN Transmit

## Ports

### Input

### **Data** — Input data port vector | scalar

Specify the messages in the raw data format at this port.

#### Dependencies

To enable this port, set the **Data format** parameter
to `Raw data` and disable the **Remote
transmit** parameter.

**Data Types:** `uint8`

### **Remote Request** — Remote transmission request scalar

Specify the remote transmission request at this port as:

- `1 —` To activate the remote transmission
  request
- `0 —` To deactivate the remote transmission
  request

#### Dependencies

To enable this port, set the **Data format** parameter
to `Raw data`, the **Frame format**
parameter to `Classic CAN`, and enable the
**Remote transmit parameter**.

**Data Types:** `Boolean`

### **ID** — CAN message identifier scalar

Specify the CAN message identifier at this port as one of these values:

- `0-0x7ff —` For a standard (11-bit)
  identifier
- `0-0x1fffffff —` For an extended (29-bit)
  identifier

#### Dependencies

To enable this parameter, set the **Data format**
parameter to `Raw data` and select the **Enable
input port for identifier** parameter.

**Data Types:** `uint32`

### **ID Type** — CAN message identifier type scalar

Specify the CAN message identifier type at this port as one of these values:

- `0 —` If the identifier is an 11-bit standard
  identifier
- `1` or any value other than `0 —` If
  the identifier is an 29-bit standard identifier

#### Dependencies

To enable this parameter, set the **Data format**
parameter to `Raw data` and select the **Enable
input port for identifier type** parameter.

**Data Types:** `uint8`

### **Length** — CAN message length scalar

Specify the length of the transmitted CAN message in bytes at this
port.

**Note**

The **Length** value determines the size of the data to
be transmitted over the CAN bus. If the value at the
**Length** port is greater than the size of the value at
the **Data** port, then Simulink prioritizes the **Data** value over the
**Length** value.

#### Dependencies

To enable this parameter, set the **Data format**
parameter to `Raw data` and select the **Enable
input port for data length** parameter.

**Data Types:** `uint8`

### **Msg** — Input CAN message vector | scalar

Specify the messages in the CAN message format.

You can create your messages or you can upload a CAN database file from the
CAN Pack or CAN FD Pack blocks
depending on the value in the **Frame format**
parameter.

**Note**

To create a CAN message using the CAN Pack block, enable the
**Output as bus** parameter in the CAN Pack
block.

#### Dependencies

To enable this port, set the **Data format** parameter
to `CAN message`.

**Data Types:** `CAN message`

### **Buffer Number** — Number of buffers in buffer transmit mode scalar

Specify the number of buffers for CAN transmission.

#### Dependencies

To enable this port, set the **Data format**
parameter to `CAN message`, **Mode**
parameter to `Buffer`, and select the
**Enable input port for buffer number**
parameter.

**Data Types:** `uint8`
### Output

### **Status** — Status of data transmission scalar

Specify the data transmission status at this port as one of these values:

- `0` — No error in CAN data transmission
- `1` — Error in CAN data transmission due to
  timeout
- `2` — Error in CAN data transmission due to
  invalid buffer configuration

#### Dependencies

To enable this port, select the **Enable status
port** parameter.

**Data Types:** `uint8`

### **FIFO Level** — FIFO register filling level scalar

Output port to display the level of the FIFO register.

#### Dependencies

To enable this parameter, set the **Mode** parameter to
`FIFO or Queue` and select the **Output
FIFO transmit free level** parameter.

## Parameters

### **Data format** — Data output type `Raw data` (default) | `CAN message`

Set the data type of the transmitted message as one of these values:

- `Raw data` — Transmit the message as a
  1-by-*N*
  `uint8` array.
- `CAN message` — Transmit message in CAN
  message format. Depending on the value of the **Frame
  format** parameter, use CAN Pack or CAN FD Pack
  blocks along with the MCAN Transmit block to pack the CAN message.

**Note**

To create a CAN message using the CAN Pack block, enable the
**Output as bus** parameter in the CAN Pack block.

### **Frame format** — Frame format type `CAN-FD` (default) | `Classic CAN`

Select the frame format of the transmitted message.

### **Remote transmit** — Option to enable remote message transmission `off` (default) | `on`

Select this parameter to transmit a remote frame in the CAN message.

#### Dependencies

To enable this parameter, set the **Data format** parameter
to `Raw data` and set the **Frame
format** parameter to `Classic
CAN`.

#### CAN FD

### **Enable bit rate switching** — Option to enable switching between nominal bit rate and data bit rate `off` (default) | `on`

Select this parameter to enable switching between the nominal bit rate and the
data bit rate.

#### Dependencies

To enable this parameter, set the **Data
Format** parameter to `Raw data` and
**Frame format** to `CAN-FD`.

#### Identifier type

### **Enable input port for identifier type** — Option to enable input port for identifier type `off` (default) | on

Select this parameter to enable the input port to specify the identifier
type.

#### Dependencies

To enable this parameter, set the **Data format** parameter
to `Raw data`.

### **Identifier type** — Message identifier type `Standard (11-bit identifier)` (default) | `Extended (29-bit identifier)`

Specify the type of message identifier.

#### Dependencies

To enable this parameter, set the **Data
Format** parameter to `Raw data` and disable the
**Enable input port for identifier type** parameter.

#### Identifier

### **Enable input port for identifier** — Option to enable input port for identifier `on` (default) | off

Select to enable input port for identifier.

#### Dependencies

To enable this parameter, set **Data format** parameter to
`Raw data`.

### **Identifier** — Message identifier `100` (default) | scalar in the range (0,0x7ff) for standard frame | scalar in the range (0,0x1fffffff) for extended frame

Specify an 11-bit identifier for the standard frame size or a 29-bit identifier
for the extended frame size. You can specify the identifier as a decimal, binary,
or hexadecimal value. For binary and hexadecimal formats, use `bin2dec` and `hex2dec` respectively to convert
the value. The block codes the identifier into a message and sends it to the CAN
bus.

#### Dependencies

To enable this parameter, set **Data format** parameter to
`Raw data` and disable the **Enable input
port for identifier type** parameter.

#### Data length

### **Enable input port for data length** — Option to enable input port for data length `on` (default) | off

Select this parameter to enable the input port to specify data length.

#### Dependencies

To enable this parameter, set the **Data format** as
`Raw data`.

### **Data length** — Length in bytes `8` (default) | scalar in the range (0,8) | `12` | `16` | `20` | `24` | `32` | `48` | `64`

Specify the data length in bytes.

#### Dependencies

To enable this parameter, set the **Data format** as
`Raw data` and disable the **Enable input port for
data length** parameter.

#### Node

### **Number of nodes** — Number of CAN nodes `1` (default) | scalar in the range (0 to 20)

Specify the number of CAN nodes for data transmission.

**Note**

The choice of the **Number of nodes** parameter determines
how many nodes you must configure in the Hardware Mapping tool (see MCAN
Transmit Peripheral Configuration).

### **Mode** — Message transmission mode `FIFO or Queue` (default) | `Buffer`

Select the mode of the CAN data transmission.

#### Buffer

### **Enable input port for buffer number** — Option to enable input port for buffer number `off` (default) | on

Select this parameter to enable the **Buffer Number** input
port in the block.

#### Dependencies

To enable this parameter, set the **Mode** parameter to
`Buffer`.

### **Buffer number (0 - 31)** — Number of buffers for data transmission `0` (default) | scalar in the range (0,31)

Specify the number of buffers to use for transmitting the CAN data.

#### Dependencies

To enable this parameter, set the **Mode** parameter to
`Buffer` and disable the **Enable input
port for buffer number** parameter.

#### Timeout

### **Timeout(s) in seconds** — Waiting time to complete write operation `0` (default) | scalar in the range (0,2147480)

Specify the maximum waiting time (in seconds) to transmit the CAN data.

### **Output FIFO transmit free level** — Option to enable output FIFO transmit free level `off` (default) | `on`

Select this parameter to enable the **FIFO level** port, which
outputs the transmitted FIFO message level.

#### Dependencies

To enable this parameter, set the **Mode** parameter to
`FIFO or Queue`.

### **Enable status port** — Option to enable output status port `off` (default) | `on`

Select this parameter to enable the **Status** port, which
outputs the data transmission status.

## Libraries

Embedded Coder Support Package for Infineon AURIX TC4x Microcontrollers / AURIX TC4x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2024b**

## Description

Write data to CAN bus

The MCAN Receive block is a Modular CAN (MCAN) that writes data to the controller area
network (CAN) bus.

The block accepts a 1-D array of type `uint8` when you set the data
format to `Raw data`. If you set the data format to
`CAN Message`, the block accepts a Simulink® bus signal from the CAN Pack or CAN FD Pack blocks, depending on
the frame format.
