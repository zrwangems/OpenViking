---
type: simulink-block
title: 'Modbus TCP/IP Server Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Network'
documentation_page: 'modbustcpipserverread'
documentation_source_path: 'supportpkg/raspberrypi_ref/modbustcpipserverread.html'
language: en
---

# Modbus TCP/IP Server Read

## Ports

### Output

### **Data** — Output data scalar

The block outputs the data read by the server device from its register as a 1-bit
scalar.

- If you select the Coil or Discrete Input read operations, the server reads its
  registers as a 1-bit read operation. The block outputs the read data as Boolean
  data.
- If you select the Holding Register or Input Register read operations, the
  server reads its registers as a 16-bit read operation. The block outputs the read
  data as uint16 data.

**Data Types:** `Boolean` | `uint16`

### **Status** — Status of read operation `0` | `1`

The block outputs the status of the server read operation on the server register.

- `0`: Indicates an unsuccessful read operation, which means
  that the data received on the **data** port is invalid.
- `1`: Indicates a successful read operation, which means
  that the data received on the **data** port is valid.

**Data Types:** `uint8`

## Parameters

### **Function** — Type of read operation `Read Coil` (default) | `Read Discrete Input` | `Read Holding register` | `Read Input register`

Select the type of read operation you want to perform on the server register.
Specify any one of the following:

- `Read Coil`: Read data from the coil register address
  specified in the **Coil Address** parameter.
- `Read Discrete Input`: Read data from the discrete
  input register address specified in the **Discrete Input Address**
  parameter.
- `Read Holding register`: Read data from the holding
  register address specified in the **Holding Register Address**
  parameter.
- `Read Input register`: Read data from the input
  register address specified in the **Input Register Address**
  parameter.

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
Discrete Input`.

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

Simulink Support Package for Raspberry Pi Hardware / Network

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021a**

## Description

Server device reads data from server device register over TCP/IP network

In the Modbus TCP/IP Server Read block, the server device reads data from
its registers. The server can read data from only one register per read operation.

Simulink® Support Package for Raspberry Pi® Hardware supports the Modbus® communication protocol over the TCP/IP network.

The server can perform read and write operation on these server register(s).

| Register Type | Register Size |
| --- | --- |
| Coil | 1-bit |
| Discrete Input | 1-bit |
| Holding Register | 16-bit |
| Input Register | 16-bit |

The server can perform either a read or a write operation on its registers.

**Note**

To generate C/C++ code for this block, you must have an Embedded Coder® license.
