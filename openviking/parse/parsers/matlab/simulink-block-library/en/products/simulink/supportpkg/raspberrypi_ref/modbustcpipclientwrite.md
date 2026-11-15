---
type: simulink-block
title: 'Modbus TCP/IP Client Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Network'
documentation_page: 'modbustcpipclientwrite'
documentation_source_path: 'supportpkg/raspberrypi_ref/modbustcpipclientwrite.html'
language: en
---

# Modbus TCP/IP Client Write

## Ports

### Input

### **Data** — Input data vector

The input to the block is the data that the client writes to the server
register(s). Specify the input data as a *N*-by-1 vector, where
*N* represents the number of registers on the server device.

- If you select the Coil or Discrete Input write operations, the client writes
  data to the server registers as a 1-bit write operation as Boolean data.
- If you select the Holding Register or Input Register write operations, the
  client writes data to the server registers as a 16-bit write operation as uint16
  data.

**Data Types:** `Boolean` | `uint16`

## Parameters

### **Server address** — Unique IP address for server device `127.0.0.1` (default) | IP address

Enter the IP address of the server device to identify the server to which the client
writes the data.

### **Function** — Type of write operation `Write Coil` (default) | `Write Holding register` | `Write Multiple Coils` | `Write Multiple Holding registers`

Select the type of write operation you want to perform on the server register(s).
Specify any one of the following:

- `Write Coil`: Write data to the coil register address
  specified in the **Coil Address** parameter.
- `Write Holding register`: Write data to the holding
  register address specified in the **Holding Register Address**
  parameter.
- `Write Multiple Coils`: Write data to multiple coil
  registers depending on the values specified in the **Coil Address**
  and **Number of Coils** parameters.
- `Write Multiple Holding registers`: Write data to
  multiple holding registers depending on the values specified in the
  **Holding Register Address** and **Number of Holding
  registers** parameters.

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

## Libraries

Simulink Support Package for Raspberry Pi Hardware / Network

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2021a**

## Description

Client device writes data to server device register(s) over TCP/IP network

In the Modbus TCP/IP Client Write block, the client device writes data to
the register(s) of the server device.

Simulink® Support Package for Raspberry Pi® Hardware supports the Modbus® communication protocol over the TCP/IP network. The client and the server must
be connected to the TCP/IP network for successful Modbus communication.

The client can perform either a read, write, or a read and write operation on the server
register depending on the server register(s) type.

| Register Type | Register Size | Operation Performed by Client |
| --- | --- | --- |
| Coil | 1-bit | Read and Write |
| Discrete Input | 1-bit | Read |
| Holding Register | 16-bit | Read and Write |
| Input Register | 16-bit | Read |

The client can perform either a read or a write operation (depending on the register type)
on register(s) of a server device.

**Note**

To generate C/C++ code for this block, you must have an Embedded Coder® license.
