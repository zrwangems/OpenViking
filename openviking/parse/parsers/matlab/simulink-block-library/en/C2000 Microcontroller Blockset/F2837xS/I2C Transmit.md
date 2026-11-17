---
type: simulink-block
title: 'C28x I2C Transmit'
family: 'ti-c2000'
product_id: 'ti-c2000'
product_name: 'C2000 Microcontroller Blockset'
documentation_release: R2025b
official_category: 'C2802x'
documentation_page: 'c28xi2ctransmit'
documentation_source_path: 'ref/c28xi2ctransmit.html'
language: en
---

# C28x I2C Transmit

## Ports
```yaml
ports:
- name: SAR
  summary: Peripheral address register value scalar
  direction: input
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32 | single | double | Boolean
- name: WD
  summary: Data written to I2C bus scalar | vector
  direction: input
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32
- name: status
  summary: I2C communication status scalar
  direction: output
  data_types: uint16
```

### Input

### **SAR** — Peripheral address register value scalar

The peripheral address register
value.

#### Dependencies

This port appears only when **peripheral address
source** is set to
`Input port`.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `single` | `double` | `Boolean`

### **WD** — Data written to I2C bus scalar | vector

The data written to the I2C bus.

**Data Types:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`
### Output

### **status** — I2C communication status scalar

Status values from the I2C status register (I2CSTR).

#### Dependencies

This port appears only when **Output transmitting
status** is selected.

**Data Types:** `uint16`
## Parameters
```yaml
parameters:
- name: Module
  summary: Module for communication I2C_A (default) | I2C_B
  group: ''
- name: Addressing format
  summary: Address format for communication 7–Bit addressing (default) | 10–Bit addressing | Free data format
  group: ''
- name: peripheral address source
  summary: peripheral address source of I2C peripheral Specify via dialog (default) | Input port
  group: ''
- name: Peripheral address register
  summary: Peripheral address register value 80 (default) | scalar
  group: ''
- name: Bit count
  summary: Bit count for communication 8 (default) | integer in [1 8]
  group: ''
- name: Enable stop condition
  summary: Send stop bit to indicate that data transmission is complete off (default) | on
  group: ''
- name: Enable repeat mode
  summary: Retransmit data until stop or start condition is detected off (default) | on
  group: ''
- name: Output transmitting status
  summary: Indicates when I2C transmit block transmits message off (default) | on
  group: ''
```

### **Module** — Module for communication `I2C_A` (default) | `I2C_B`

The I2C module to be used for communication. The number of I2C modules
supported varies across different C2000™
processors.

### **Addressing format** — Address format for communication `7–Bit addressing` (default) | `10–Bit addressing` | `Free data format`

The address format for communication. The diagram shows the format for
each option. The I2C Transmit block sets the R/W bit to
1.

S — Start bit

R/W — Read/Write

ACK — Acknowledge

P — Stop bit

MSB — Most significant bit

LSB — Least significant bit

### **peripheral address source** — peripheral address source of I2C peripheral `Specify via dialog` (default) | `Input port`

The method for setting the peripheral address register of the I2C
peripheral.

### **Peripheral address register** — Peripheral address register value `80` (default) | scalar

Enter a 7- or 10-bit peripheral address according to the addressing format
selected.

#### Dependencies

This parameter appears only when **Peripheral address
source** is set to
`Specify via dialog`.

### **Bit count** — Bit count for communication `8` (default) | integer in [1 8]

The number of bits in the data byte received by the I2C module.

### **Enable stop condition** — Send stop bit to indicate that data transmission is complete `off` (default) | `on`

When the I2C module is configured as controller, the I2C module sends out
a stop bit to the I2C bus to indicate that the data transmission is
complete. The I2C bus is free for any other I2C module to initiate a
read/write operation.

### **Enable repeat mode** — Retransmit data until stop or start condition is detected `off` (default) | `on`

When you enable repeat mode, the I2C module transmits data continuously
until it detects a stop or start condition. If you use this mode, also
consider selecting **Enable stop condition** to ensure that
data transmit stops after the stop condition.

If you disable repeat mode, the I2C module operates in standard mode,
sending a specific number of data values once.

### **Output transmitting status** — Indicates when I2C transmit block transmits message `off` (default) | `on`

Enables the status output port, which indicates when the I2C transmit
block transmits a message.
## Libraries

C2000 Microcontroller Blockset / C2802x C2000 Microcontroller Blockset / C2803x C2000 Microcontroller Blockset / C2805x C2000 Microcontroller Blockset / C2806x C2000 Microcontroller Blockset / C280x C2000 Microcontroller Blockset / C2833x C2000 Microcontroller Blockset / C2834x C2000 Microcontroller Blockset / F280013x C2000 Microcontroller Blockset / F280015x C2000 Microcontroller Blockset / F28002x C2000 Microcontroller Blockset / F28003x C2000 Microcontroller Blockset / F28004x C2000 Microcontroller Blockset / F2807x C2000 Microcontroller Blockset / F2837xD C2000 Microcontroller Blockset / F2837xS C2000 Microcontroller Blockset / F2838x / C28x C2000 Microcontroller Blockset / F28M35x / C28x C2000 Microcontroller Blockset / F28M36x / C28x C2000 Microcontroller Blockset / F28p65x C2000 Microcontroller Blockset / F28p55x

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

Not documented in R2025b.

## Description

Configure inter-integrated circuit (I2C) module to transmit data to I2C bus

The I2C Transmit block configures the inter-integrated circuit (I2C)
module to transmit data to the two-wire I2C serial bus. The I2C Transmit
block supports I2C bus communication between the processor and external peripherals or
other controllers. The block can run in either peripheral or controller
mode.

When the I2C module is configured as controller, the module receives data from a
peripheral. When the I2C module is configured as a
peripheral, the module receives data from the controller.
Configure the I2C module by navigating to **Configuration Parameters** > **Hardware Implementation** > **Target hardware resources**.

To read data from a peripheral, send the address of the
register to be read using the I2C Transmit block to the
peripheral. Ensure that the data is sent from the Tx FIFO to
the peripheral before the data is read from the
peripheral using the I2C Receive block. For
more information, see Using the I2C Bus to Access Sensors.
