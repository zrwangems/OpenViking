---
type: simulink-block
title: 'Modbus TCP/IP Client Write'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Network'
documentation_page: 'modbustcpipclientwrite'
documentation_source_path: 'nvidia/ref/modbustcpipclientwrite.html'
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
  data to the server registers as a 1-bit write operation of Boolean data.
- If you select the Holding Register or Input Register write operations, the
  client writes data to the server registers as a 16-bit write operation as
  `uint16` data.

**Data Types:** `Boolean` | `uint16`

## Parameters

### **Server address** — Unique IP address for server device `127.0.0.1` (default) | IP address

Enter the IP address of the server device to identify the server to which the client
writes the data.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `serverIP` |
| **Type:** character vector |
| **Values:** `'127.0.0.1'` | `Valid IP address` |
| **Default:**  `'127.0.0.1'` |

### **Function** — Type of write operation `Write Coil` (default) | `Write Holding Register` | `Write Multiple Coils` | `Write Multiple Holding Registers`

Select the type of write operation you want to perform on the server register(s).
Specify one of the following:

| Value | Description |
| --- | --- |
| `Write Coil` | Write data to the coil register address specified in the **Coil Address** parameter. |
| `Write Holding Register` | Write data to the holding register address specified in the **Holding Register Address** parameter. |
| `Write Multiple Coils` | Write data to multiple coil registers depending on the values specified in the **Coil Address** and **Number of Coils** parameters. |
| `Write Multiple Holding Registers` | Write data to multiple holding registers depending on the values specified in the **Holding Register Address** and **Number of Holding registers** parameters. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Function` |
| **Type:** character vector |
| **Values:** `'Write Coil'` | `'Write Holding Register'` | `'Write Multiple Coils'` | `'Write Multiple Holding Registers'` |
| **Default:**  `'Write Coil'` |

### **Coil address** — Address of coil register `0` (default) | scalar

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
Coil` or `Write Multiple Coils`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CoilAddress` |
| **Type:** character vector |
| **Values:** `'0'` | scalar |
| **Default:**  `'0'` |

### **Number of coils** — Number of coil registers to be written by client `1` (default) | scalar

Enter the number of coil registers to which you want the client to write the data.
For example, for the client to write data to the coil registers with addresses ranging
from `10` to `14`, enter `5`.

#### Dependencies

To enable this parameter, set **Function** to `Write
Multiple Coils`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `numElements_coil` |
| **Type:** character vector |
| **Values:** `'1'` | scalar |
| **Default:**  `'1'` |

### **Holding register address** — Address of holding register `0` (default) | scalar

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
Holding Register`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `HoldingRegisterAddress` |
| **Type:** character vector |
| **Values:** `'0'` | scalar |
| **Default:**  `'0'` |

### **Number of holding registers** — Number of holding registers to be written by client `1` (default) | scalar

Enter the number of holding registers from which you want the client to write the
data. For example, for the client to write data to the holding registers with addresses
ranging from `37` to `44`, enter
`8`.

#### Dependencies

To enable this parameter, set **Function** to `Write
Multiple Holding Registers`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `numElements_holdingReg` |
| **Type:** character vector |
| **Values:** `'1'` | scalar |
| **Default:**  `'1'` |

## Libraries

NVIDIA Jetson and NVIDIA DRIVE / Network

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022a**

## Description

Client device writes data to server device register(s) over TCP/IP network

In the Modbus TCP/IP Client Write block, the client device writes data to
the register(s) of the server device.

MATLAB®
Coder™ Support Package for NVIDIA®
Jetson™ and NVIDIA DRIVE® Platforms supports the Modbus® communication protocol over the TCP/IP network on Jetson platforms. The client and the server must be connected to the TCP/IP network for successful
Modbus communication.

**Note**

The Modbus TCP/IP Client Write block is not supported on NVIDIA DRIVE platforms.

The client can perform either a read, write, or a read and write operation on the server
register depending on the server register(s) type.

| Register Type | Register Size | Operation Performed by client |
| --- | --- | --- |
| Coil | 1-bit | Read and write |
| Discrete Input | 1-bit | Read |
| Holding Register | 16-bit | Read and write |
| Input Register | 16-bit | Read |

The client can perform either a read or a write operation (depending on the register type)
on register(s) of a server device.
