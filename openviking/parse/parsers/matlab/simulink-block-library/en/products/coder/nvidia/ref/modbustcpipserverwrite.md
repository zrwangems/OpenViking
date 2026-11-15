---
type: simulink-block
title: 'Modbus TCP/IP Server Write'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Network'
documentation_page: 'modbustcpipserverwrite'
documentation_source_path: 'nvidia/ref/modbustcpipserverwrite.html'
language: en
---

# Modbus TCP/IP Server Write

## Ports

### Input

### **Input** — Input data scalar

The input to the block is the data that the server writes to its registers as a
1-bit scalar.

- If you select the Coil or Discrete Input write operations, the server writes
  data to its registers as a 1-bit write operation as Boolean data.
- If you select the Holding Register or Input Register write operations, the
  server writes data to its registers as a 16-bit write operation as
  `uint16` data.

**Data Types:** `Boolean` | `uint16`

## Parameters

### **Function** — Type of write operation `Write Coil` (default) | `Write Discrete Input` | `Write Holding register` | `Write Input register`

Select the type of write operation you want to perform on the server register.
Specify one of the following:

| Value | Description |
| --- | --- |
| `Write Coil` | Write data to the coil register address specified in the **Coil Address** parameter. |
| `Write Discrete Input` | Write data to the discrete input register address specified in the **Discrete Input Address** parameter. |
| `Write Holding Register` | Write data to the holding register address specified in the **Holding Register Address** parameter. |
| `Write Input Register` | Write data to the input register address specified in the **Input Register Address** parameter. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Function` |
| **Type:** character vector |
| **Values:** `'Write Coil'` | `'Write Discrete Input'` | `'Write Holding Register'` | `'Write Input Register'` |
| **Default:**  `'Write Coil'` |

### **Coil Address** — Address of coil register `0` (default) | scalar

To notify the server to write data to a specific coil register, specify the coil
register address in this parameter. For example, for the server to write data to the
coil register with the address `10`, enter
`10`.

#### Dependencies

To enable this parameter, set **Function** to `Write
Coil`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CoilAddress` |
| **Type:** character vector |
| **Values:** `'0'` | scalar |
| **Default:**  `'0'` |

### **Discrete Input Address** — Address of discrete input register `0` (default) | scalar

To notify the server to write data to a specific discrete input register, specify
the discrete input register address in this parameter. For example, for the server to
write data to the discrete input register with the address `80`, enter
`80`.

#### Dependencies

To enable this parameter, set **Function** to `Write
Discrete Input`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DiscreteInputAddress` |
| **Type:** character vector |
| **Values:** `'0'` | scalar |
| **Default:**  `'0'` |

### **Holding Register Address** — Address of holding register `0` (default) | scalar

To notify the server to write data to a specific holding register, specify the
holding register address in this parameter. For example, for the server to write data to
the holding register with the address `37`, enter
`37`.

#### Dependencies

To enable this parameter, set **Function** to `Write
Holding register`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `HoldingRegisterAddress` |
| **Type:** character vector |
| **Values:** `'0'` | scalar |
| **Default:**  `'0'` |

### **Input Register Address** — Address of input register `0` (default) | scalar

To notify the server to write data to a specific input register, specify the input
register address in this parameter. For example, for the server to write data to the
input register with the address `25`, enter
`25`.

#### Dependencies

To enable this parameter, set **Function** to `Write
Input register`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputRegisterAddress` |
| **Type:** character vector |
| **Values:** `'0'` | scalar |
| **Default:**  `'0'` |

## Libraries

NVIDIA Jetson and NVIDIA DRIVE / Network

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022a**

## Description

Server device writes data to server device register over TCP/IP network

In the Modbus TCP/IP Server Write block, the server device writes data to
its registers. The server can write data to only one register per read operation.

MATLAB®
Coder™ Support Package for NVIDIA®
Jetson™ and NVIDIA DRIVE® Platforms supports the Modbus® communication protocol over the TCP/IP network on Jetson platforms.

**Note**

The Modbus TCP/IP Server Write block is not supported on NVIDIA DRIVE platforms.

The server can perform read and write operation on these server register(s).

| Register Type | Register Size |
| --- | --- |
| Coil | 1-bit |
| Discrete Input | 1-bit |
| Holding Register | 16-bit |
| Input Register | 16-bit |
