---
type: simulink-block
title: 'Modbus RS485 Client Write'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Common'
documentation_page: 'modbusrs485clientwrite'
documentation_source_path: 'nucleo/ref/modbusrs485clientwrite.html'
language: en
---

# Modbus RS485 Client Write

## Ports

### Input

### **data** — Input data vector

The input to the block is the data to be written to the server register(s) by the
client as a *N*-by-1 vector, where *N* represents
the number of registers on the server device.

- If you select the Coil or Discrete Input write operations, the client writes
  data to the server registers as a 1-bit write operation having the Boolean data
  type.
- If you select the Holding Register or Input Register write operations, the
  client writes data to the server registers as a 16-bit write operation having the
  uint16 data type.

**Data Types:** `Boolean` | `uint16`
### Output

### **status** — Status of write operation `0` | `1`

The block outputs the status of the client write operation on the client device register.

- `1`: Indicates an unsuccessful write operation to the
  server registers or didn’t receive the response from the server within the
  timeout.
- `0`: Indicates a successful write operation to the server
  registers and received expected response within the timeout.

#### Dependencies

To enable this port, select the **Output status**
parameter.

**Data Types:** `uint8`

## Parameters

### **Server address (0 for broadcast)** — Unique 8-bit Modbus server identifier `1` (default) | scalar in the range [`1`, `255`]

Enter the unique 8-bit Modbus server address or identifier to identify the server to which the client
writes the data.

### **Function** — Type of write operation `Write Coil` (default) | `Write Holding register` | `Write Multiple Coils` | `Write Multiple Holding registers`

Select the type of write operation you want to perform on the server register(s).
Specify any one of the following:

- `Write Coil`: Write data to the coil register address
  specified in the **Coil Address** parameter
- `Write Holding register`: Write data to the holding
  register address specified in the **Holding Register Address**
  parameter
- `Write Multiple Coils`: Write data to multiple coil
  registers depending on the values specified in the **Coil Address**
  and **Number of Coils** parameters
- `Write Multiple Holding registers`: Write data to
  multiple holding registers depending on the values specified in the
  **Holding Register Address** and **Number of Holding
  registers** parameters

### **Coil Address** — Address of coil register `0` (default) | scalar

- To notify the client to write data to a specific coil register, specify the coil
  register address in this parameter. For example, for the client to write data to the
  coil register with the address `10`, enter
  `10`.
- To notify the client to write data to a group of coil registers, specify the
  address of the first coil register in the group. For example, for the client to
  write data to the coil registers with addresses ranging from `10`
  to `14`, enter `10`.

#### Dependencies

To enable this parameter, set **Function** to `Write
Coil`.

### **Number of Coils** — Number of coil registers to be written by client `1` (default) | scalar

Enter the number of coil registers to which you want the client to write the data.
For example, for the client to write data to the coil registers with addresses ranging
from `10` to `14`, enter `5`.

#### Dependencies

To enable this parameter, set **Function** to `Write
Multiple Coils`.

### **Holding Register Address** — Address of holding register `0` (default) | scalar

- To notify the client to write data to a specific holding register, specify the
  holding register address in this parameter. For example, for the client to write
  data to the holding register with the address `37`, enter
  `37`.
- To notify the client to write data to a group of holding registers, specify the
  address of the first holding register in the group. For example, for the client to
  write data to the holding registers with addresses ranging from
  `37` to `44`, enter
  `37`.

#### Dependencies

To enable this parameter, set **Function** to `Write
Holding register`.

### **Number of Holding registers** — Number of holding registers to be written by client `1` (default) | scalar

Enter the number of holding registers from which you want the client to write the
data. For example, for the client to write data to the holding registers with addresses
ranging from `37` to `44`, enter
`8`.

#### Dependencies

To enable this parameter, set **Function** to `Write
Multiple Holding registers`.

### **Output status** — Enable output status `off` (default) | `on`

When you select the **Output Status** parameter, the block
configures an output port, **Status**. The port outputs the status
message.

## Libraries

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A)

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Client device writes data to server device register(s) over RS485 network

In the Modbus RS485 Client Write block, the client device writes data to
the register(s) of the server device.

Simulink®
Coder™ Support Package for STMicroelectronics® Nucleo Boards and Embedded Coder® Support Package for STMicroelectronics Discovery Boards supports the Modbus® communication protocol over the RS485 network. The client and the server must be
connected on the same RS485 network for successful Modbus communication. Each device on the RS485 network is referenced by a unique 8-bit
address or identifier.

This table categories the server device registers referenced by the Modbus client device.

| Register Type | Register Size | Allowed Client Operation on Register |
| --- | --- | --- |
| Coil | 1-bit | Read and Write |
| Discrete Input | 1-bit | Read |
| Holding Register | 16-bit | Read and Write |
| Input Register | 16-bit | Read |

The client can perform either a read or a write operation (depending on the register type)
on register(s) of a server device.
