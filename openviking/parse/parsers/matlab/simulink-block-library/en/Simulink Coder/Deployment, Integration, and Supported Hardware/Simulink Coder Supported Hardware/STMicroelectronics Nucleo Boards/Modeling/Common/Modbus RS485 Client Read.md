---
type: simulink-block
title: 'Modbus RS485 Client Read'
family: 'rtw'
product_id: 'rtw'
product_name: 'Simulink Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Simulink Coder Supported Hardware / STMicroelectronics Nucleo Boards / Modeling / Common'
documentation_page: 'modbusrs485clientread'
documentation_source_path: 'nucleo/ref/modbusrs485clientread.html'
language: en
---

# Modbus RS485 Client Read

## Ports

### Output

### **data** — Output data vector

The block outputs the data read by the client from the server device register(s)
as a *N*-by-1 vector, where *N* represents the
number of registers on the server device.

- If you select the Coil or Discrete Input read operations, the client reads the
  server registers as a 1-bit read operation. The block outputs the read data as
  `Boolean` data.
- If you select the Holding Register or Input Register read operations, the
  client reads the server registers as a 16-bit read operation. The block outputs
  the read data as `uint16` data.

**Data Types:** `Boolean` | `uint16`

### **status** — Status of read operation `0` | `1`

The block outputs the status of the client read operation on the server device register.

- `1`: Indicates an unsuccessful read operation, which means
  that the data received on the **data** port is invalid.
- `0`: Indicates a successful read operation, which means
  that the data received on the **data** port is valid.

**Data Types:** `uint8`

## Parameters

### **Server address (0 for broadcast)** — Unique 8-bit Modbus server identifier `1` (default) | scalar in the range [`1`, `255`]

Enter the unique 8-bit Modbus server address or identifier to identify the server from which the client
reads the data.

### **Function** — Type of read operation `Read Coil` (default) | `Read Discrete input` | `Read Holding register` | `Read Input register` | `Read Multiple Coils` | `Read Multiple Discrete inputs` | `Read Multiple Holding registers` | `Read Multiple Input registers`

Select the type of read operation you want to perform on the server register(s).
Specify any one of the following:

- `Read Coil`: Read data from the coil register address
  specified in the **Coil Address** parameter.
- `Read Discrete input`: Read data from the discrete
  input register address specified in the **Discrete Input Address**
  parameter.
- `Read Holding register`: Read data from the holding
  register address specified in the **Holding Register Address**
  parameter.
- `Read Input register`: Read data from the input
  register address specified in the **Input Register Address**
  parameter.
- `Read Multiple Coils`: Read data from multiple coil
  registers depending on the values specified in the **Coil Address**
  and **Number of Coils** parameters.
- `Read Multiple Discrete inputs`: Read data from
  multiple discrete input registers depending on the values specified in the
  **Discrete Input Address** and **Number of Discrete
  Inputs** parameters.
- `Read Multiple Holding registers`: Read data from
  multiple holding registers depending on the values specified in the
  **Holding Register Address** and **Number of Holding
  registers** parameters.
- `Read Multiple Input registers`: Read data from
  multiple input registers depending on the values specified in the **Input
  Register Address** and **Number of Input registers**
  parameters.

### **Coil Address** — Address of coil register `0` (default) | scalar

- To notify the client to read data from a specific coil register, specify the
  coil register address in this parameter. For example, for the client to read data
  from the coil register with the address `10`, enter
  `10`.
- To notify the client to read data from a group of coil registers, specify the
  address of the first coil register in the group. For example, for the client to read
  data from the coil registers with addresses ranging from `10` to
  `14`, enter `10`.

#### Dependencies

To enable this parameter, set **Function** to `Read
Coil`.

### **Number of Coils** — Number of coil registers to be read by client `1` (default) | scalar

Enter the number of coil registers from which you want the client to read the data.
For example, for the client to read data from the coil registers with addresses ranging
from `10` to `14`, enter `5`.

#### Dependencies

To enable this parameter, set **Function** to `Read
Multiple Coils`.

### **Discrete Input Address** — Address of discrete input register `0` (default) | scalar

- To notify the client to read data from a specific discrete input register,
  specify the discrete input register address in this parameter. For example, for the
  client to read data from the discrete input register with the address
  `80`, enter `80`.
- To notify the client to read data from a group of discrete input registers,
  specify the address of the first discrete input register in the group. For example,
  for the client to read data from the discrete input registers with addresses ranging
  from `80` to `89`, enter
  `80`.

#### Dependencies

To enable this parameter, set **Function** to `Read
Discrete input`.

### **Number of Discrete Inputs** — Number of discrete input registers to be read by client `1` (default) | scalar

Enter the number of discrete input registers from which you want the client to read
the data. For example, for the client to read data from the discrete input registers
with addresses ranging from `80` to `89`, enter
`10`.

#### Dependencies

To enable this parameter, set **Function** to `Read
Multiple Discrete inputs`.

### **Holding Register Address** — Address of holding register `0` (default) | scalar

- To notify the client to read data from a specific holding register, specify the
  holding register address in this parameter. For example, for the client to read data
  from the holding register with the address `37`, enter
  `37`.
- To notify the client to read data from a group of holding registers, specify the
  address of the first holding register in the group. For example, for the client to
  read data from the holding registers with addresses ranging from
  `37` to `44`, enter
  `37`.

#### Dependencies

To enable this parameter, set **Function** to `Read
Holding register`.

### **Number of Holding registers** — Number of holding registers to be read by client `1` (default) | scalar

Enter the number of holding registers from which you want the client to read the
data. For example, for the client to read data from the holding registers with addresses
ranging from `37` to `44`, enter
`8`.

#### Dependencies

To enable this parameter, set **Function** to `Read
Multiple Holding registers`.

### **Input Register Address** — Address of input register `0` (default) | scalar

- To notify the client to read data from a specific input register, specify the
  input register address in this parameter. For example, for the client to read data
  from the input register with the address `25`, enter
  `25`.
- To notify the client to read data from a group of input registers, specify the
  address of the first input register in the group. For example, for the client to
  read data from the input registers with addresses ranging from `25`
  to `26`, enter `25`.

#### Dependencies

To enable this parameter, set **Function** to `Read
Input register`.

### **Number of Input registers** — Number of input registers to be read by client `1` (default) | scalar

Enter the number of input registers from which you want the client to read the data.
For example, for the client to read data from the input registers with addresses ranging
from `25` to `26`, enter `2`.

#### Dependencies

To enable this parameter, set **Function** to `Read
Multiple Input registers`.

### **Sample Time** — Time interval at which client reads data `0.1` (default) | scalar

Enter the time interval (in seconds) at which the client reads data from the server
device register(s).

## Libraries

Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A)

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Client device reads data from server device register(s) over RS485 network

In the Modbus RS485 Client Read block, the client device reads data from
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
