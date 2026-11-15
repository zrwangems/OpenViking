---
type: simulink-block
title: 'Modbus RS485 Server Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / Communication'
documentation_page: 'modbusrs485serverread'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/modbusrs485serverread.html'
language: en
---

# Modbus RS485 Server Read

## Ports

### Output

### **data** — Output data scalar

The block outputs the data read by the server device from its register as a 1-bit
scalar.

- If you select the Coil or Discrete Input read operations, the server reads its
  registers as a 1-bit read operation. The block outputs the read data as a Boolean
  data type.
- If you select the Holding Register or Input Register read operations, the
  server reads its registers as a 16-bit read operation. The block outputs the read
  data as a uint16 data type.

**Data Types:** `Boolean` | `uint16`

### **status** — Status of read operation `0` | `1`

The block outputs the status of the server read operation on the server register.

- `1`: Indicates an unsuccessful read operation, which means
  that the data received on the **data** port is invalid.
- `0`: Indicates a successful read operation, which means
  that the data received on the **data** port is valid.

**Data Types:** `uint8`

## Parameters

### **Function** — Type of read operation `Read Coil` (default) | `Read Discrete input` | `Read Holding register` | `Read Input register`

Select the type of read operation you want to perform on the server register.
Specify any one of the following:

- `Read Coil`: Read data from the coil register address
  specified in the **Coil Address** parameter
- `Read Discrete input`: Read data from the discrete
  input register address specified in the **Discrete Input Address**
  parameter
- `Read Holding register`: Read data from the holding
  register address specified in the **Holding Register Address**
  parameter
- `Read Input register`: Read data from the input
  register address specified in the **Input Register Address**
  parameter

### **Coil Address** — Address of coil register `0` (default) | scalar

To notify the server to read data from a specific coil register, specify the coil
register address in this parameter. For example, for the server to read data from the
coil register with the address `10`, enter
`10`.

#### Dependencies

To enable this parameter, set **Function** to `Read
Coil`.

### **Discrete Input Address** — Address of discrete input register `0` (default) | scalar

To notify the server to read data from a specific discrete input register, specify
the discrete input register address in this parameter. For example, for the server to
read data from the discrete input register with the address `80`, enter
`80`.

#### Dependencies

To enable this parameter, set **Function** to `Read
Discrete input`.

### **Holding Register Address** — Address of holding register `0` (default) | scalar

To notify the server to read data from a specific holding register, specify the
holding register address in this parameter. For example, for the server to read data
from the holding register with the address `37`, enter
`37`.

#### Dependencies

To enable this parameter, set **Function** to `Read
Holding register`.

### **Input Register Address** — Address of input register `0` (default) | scalar

To notify the server to read data from a specific input register, specify the input
register address in this parameter. For example, for the server to read data from the
input register with the address `25`, enter
`25`.

#### Dependencies

To enable this parameter, set **Function** to `Read
Input register`.

### **Sample Time** — Time interval at which server reads data `0.1` (default) | scalar

Enter the time interval (in seconds) at which the server reads data from its
register.

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

## Version History

**Introduced in R2021b**

## Description

Server device reads data from the server device register over RS485 network

In the Modbus RS485 Server Read block, the server device reads data from
its registers. The server can read data only from one register per read operation.

Simulink®
Coder™ Support Package for STMicroelectronics® Nucleo Boards and Embedded Coder® Support Package for STMicroelectronics Discovery Boards supports the Modbus® communication protocol over the RS485 network. Each device on the RS485 network
is referenced by a unique 8-bit address or identifier.

This table categories the server registers referenced by the Modbus server
device.

| Register Type | Register Size |
| --- | --- |
| Coil | 1-bit |
| Discrete Input | 1-bit |
| Holding Register | 16-bit |
| Input Register | 16-bit |

The server can perform either a read or a write operation on its registers.
