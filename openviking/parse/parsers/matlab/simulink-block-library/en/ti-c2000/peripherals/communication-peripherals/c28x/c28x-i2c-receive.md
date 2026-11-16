---
type: simulink-block
title: 'C28x I2C Receive'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'Peripherals / Communication Peripherals / C28x'
documentation_page: 'c28xi2creceive'
documentation_source_path: 'ref/c28xi2creceive.html'
language: en
---

# C28x I2C Receive

## Ports

### Input

### **SAR** — Peripheral address register value scalar

The peripheral address register
value.

#### Dependencies

This port appears only when **Peripheral address
source** is set to
`Input port`.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`
### Output

### **RD** — Received data from I2C bus scalar | vector

The data read from the I2C bus.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **status** — I2C communication status scalar

Status values from the I2C status register (I2CSTR).

#### Dependencies

This port appears only when **Output receiving
status** is selected.

**Data Types:** `uint16`

## Parameters

### **Module** — Module for communication `I2C_A` (default) | `I2C_B`

The I2C module to be used for communication. The number of I2C modules
supported varies across different C2000™
processors.

### **Addressing format** — Address format for communication `7–Bit addressing` (default) | `10–Bit addressing` | `Free data format`

The address format for communication. The diagram shows the format for
each option. The I2C Receive block sets the R/W bit to
0.

S — Start bit

R/W — Read/Write

ACK — Acknowledge

P — Stop bit

MSB — Most significant bit

LSB — Least significant bit

### **Peripheral address source** — Peripheral address source of I2C peripheral `Specify via dialog` (default) | `Input port`

The method for setting the peripheral address register of the I2C
peripheral.

### **Peripheral address register** — Peripheral address register value `80` (default) | scalar

Enter a 7- or 10-bit peripheral address
according to the addressing format selected.

#### Dependencies

This parameter appears only when **Peripheral
address source** is set to
`Specify via dialog`.

### **Bit count** — Bit count for communication `8` (default) | integer in [1 8]

The number of bits in the data byte received by the I2C module.

### **Read data length** — Length of received data `1` (default) | scalar

The number of **Data type** the block receives (not
bytes). If this parameter is set to more than `1`, the
output will be a vector.

### **Initial output** — Value of I2C node output to model `0` (default) | scalar | vector

The value the I2C node outputs to the model before it has received data.
By default, the block outputs `0` if the I2C value is not
received.

### **Set NACK bit** — NACK bit during I2C acknowledge cycle `off` (default) | `on`

Generates a no-acknowledge bit (NACK) during the I2C acknowledge cycle and
ignores new bits from the transmitting I2C node.

### **Enable stop condition** — Stop message to I2C Transmit block `off` (default) | `on`

Enables the I2C Receive block (controller) to send a stop
message to the I2C Transmit block
(peripheral).

### **Output receiving status** — Indicates when I2C Receive block receives message `off` (default) | `on`

Enables the status output port, which indicates when the I2C
Receive block receives a message.

### **Sample time** — Frequency at which data is read from I2C device `0.001` (default) | `–1` | scalar

Sample time for the block in seconds. To execute this block
asynchronously, set this parameter to `-1`.

### **Data type** — Type of data in data vector `int8` (default) | `uint8` | `int16` | `uint16` | `int32` | `uint32`

Sets the data type of the data received. If the size of the received data
is less than 8 bits, then the data is right-justified.

## Libraries

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Configure inter-integrated circuit (I2C) module to receive data from I2C bus

The I2C Receive block configures the inter-integrated circuit (I2C)
module to receive data from the two-wire I2C serial bus. The I2C Receive
block supports I2C bus communication between the processor and external peripherals or
other controllers. The block can run in either peripheral or controller
mode.

When the I2C module is configured as controller, the module receives data from a
peripheral. When the I2C module is configured as a
peripheral, the module receives data from the controller.
Configure the I2C module by navigating to **Configuration Parameters** > **Hardware Implementation** > **Target hardware resources**.

To read data from a peripheral, send the address of the register to be read using the
I2C Transmit block to the peripheral. Ensure that the data is sent
from the Tx FIFO to the peripheral before the data is read from the peripheral using the
I2C Receive block. For more information, see Using the I2C Bus to Access Sensors.
