---
type: simulink-block
title: 'Modbus TCP/IP Client Read'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Network'
documentation_page: 'modbustcpipclientread'
documentation_source_path: 'nvidia/ref/modbustcpipclientread.html'
language: en
---

# Modbus TCP/IP Client Read

## Ports

### Output

### **Data** — Output data vector

The block outputs the data read by the client from the server device register(s)
as a *N*-by-1 vector, where *N* represents the
number of registers on the server device.

- If you select the Coil or Discrete Input read operations, the client reads the
  server registers as a 1-bit read operation. The block outputs the read data as
  Boolean data.
- If you select the Holding Register or Input Register read operations, the
  client reads the server registers as a 16-bit read operation. The block outputs
  the read data as `uint16` data.

**Data Types:** `Boolean` | `uint16`

### **Status** — Status of read operation `0` | `1`

The block outputs the status of the client read operation on the server device register.

- `0`: Indicates an unsuccessful read operation, which means
  that the data received on the **data** port is invalid.
- `1`: Indicates a
  successful read operation, which
  means that the data received on the **data** port is
  valid.

**Data Types:** `uint8`

## Parameters

### **Server address** — Unique IP address for server device `127.0.0.1` (default) | IP address

Enter the IP address of the server device. The client reads data from this server
device.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `serverIP` |
| **Type:** character vector |
| **Values:** `'127.0.0.1'` | `Valid IP address` |
| **Default:**  `'127.0.0.1'` |

### **Function** — Type of client read operation `Read Coil` (default) | `Read Discrete Input` | `Read Holding Register` | `Read Input Register` | `Read Multiple Coils` | `Read Multiple Discrete Inputs` | `Read Multiple Holding Registers` | `Read Multiple Input Registers`

Select the type of read operation you want to perform on the server register(s).
Specify one of these:

| Value | Description |
| --- | --- |
| `Read Coil` | Read data from the coil register address specified in the **Coil Address** parameter. |
| `Read Discrete Input` | Read data from the discrete input register address specified in the **Discrete Input Address** parameter. |
| `Read Holding Register` | Read data from the holding register address specified in the **Holding Register Address** parameter. |
| `Read Input Register` | Read data from the input register address specified in the **Input Register Address** parameter. |
| `Read Multiple Coils` | Read data from multiple coil registers depending on the values specified in the **Coil Address** and **Number of Coils** parameters. |
| `Read Multiple Discrete Inputs` | Read data from multiple discrete input registers depending on the values specified in the **Discrete Input Address** and **Number of Discrete Inputs** parameters. |
| `Read Multiple Holding Registers` | Read data from multiple holding registers depending on the values specified in the **Holding Register Address** and **Number of Holding registers** parameters. |
| `Read Multiple Input Registers` | Read data from multiple input registers depending on the values specified in the **Input Register Address** and **Number of Input registers** parameters. |

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `Function` |
| **Type:** character vector |
| **Values:** `'Read Coil'` | `'Read Discrete Input'` | `'Read Holding Register'` | `'Read Input Register'` | `'Read Multiple Coils'` | `'Read Multiple Discrete Inputs'` | `'Read Multiple Holding Registers'` | `'Read Multiple Input Registers'` |
| **Default:**  `'Read Coil'` |

### **Coil address** — Address of coil register `0` (default) | scalar

To notify the client to read data from a specific coil register, specify the coil
register address in this parameter. For example, for the client to read data from the
coil register with the address `10`, enter
`10`.

To notify the client to read data from a group of coil registers, specify the
address of the first coil register in the group. For example, for the client to read
data from the coil registers with addresses ranging from `10` to
`14`, enter `10`.

#### Dependencies

To enable this parameter, set **Function** to `Read
Coil` or `Read Multiple Coils`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `CoilAddress` |
| **Type:** character vector |
| **Values:** `'0'` | scalar |
| **Default:**  `'0'` |

### **Number of coils** — Number of coil registers to be read by client `1` (default) | scalar

Enter the number of coil registers from which you want the client to read the data.
For example, for the client to read data from the coil registers with addresses ranging
from `10` to `14`, enter `5`.

#### Dependencies

To enable this parameter, set **Function** to `Read
Multiple Coils`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `numElements_coil` |
| **Type:** character vector |
| **Values:** `'1'` | scalar |
| **Default:**  `'1'` |

### **Discrete Input Address** — Address of discrete input register `0` (default) | scalar

To notify the client to read data from a specific discrete input register, specify
the discrete input register address in this parameter. For example, for the client to
read data from the discrete input register with the address `80`, enter
`80`.

To notify the client to read data from a group of discrete input registers, specify
the address of the first discrete input register in the group. For example, for the
client to read data from the discrete input registers with addresses ranging from
`80` to `89`, enter `80`.

#### Dependencies

To enable this parameter, set **Function** to `Read
Discrete Input` or `Read Multiple Discrete
Inputs`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `DiscreteInputAddress` |
| **Type:** character vector |
| **Values:** `'0'` | scalar |
| **Default:**  `'0'` |

### **Number of Discrete Inputs** — Number of discrete input registers to be read by client `1` (default) | scalar

Enter the number of discrete input registers from which you want the client to read
the data. For example, for the client to read data from the discrete input registers
with addresses ranging from `80` to `89`, enter
`10`.

#### Dependencies

To enable this parameter, set **Function** to `Read
Multiple Discrete Inputs`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `numElements_input` |
| **Type:** character vector |
| **Values:** `'1'` | scalar |
| **Default:**  `'1'` |

### **Holding Register Address** — Address of holding register `0` (default) | scalar

To notify the client to read data from a specific holding register, specify the
holding register address in this parameter. For example, for the client to read data
from the holding register with the address `37`, enter
`37`.

To notify the client to read data from a group of holding registers, specify the
address of the first holding register in the group. For example, for the client to read
data from the holding registers with addresses ranging from `37` to
`44`, enter `37`.

#### Dependencies

To enable this parameter, set **Function** to `Read
Holding Register` or `Read Multiple Holding
Registers`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `HoldingRegisterAddress` |
| **Type:** character vector |
| **Values:** `'0'` | scalar |
| **Default:**  `'0'` |

### **Number of Holding registers** — Number of holding registers to be read by client `1` (default) | scalar

Enter the number of holding registers from which you want the client to read the
data. For example, for the client to read data from the holding registers with addresses
ranging from `37` to `44`, enter
`8`.

#### Dependencies

To enable this parameter, set **Function** to `Read
Multiple Holding Registers`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `numElements_holdingReg` |
| **Type:** character vector |
| **Values:** `'1'` | scalar |
| **Default:**  `'1'` |

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
Input Register`. or `Read Multiple Input
Registers`

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `InputRegisterAddress` |
| **Type:** character vector |
| **Values:** `'0'` | scalar |
| **Default:**  `'0'` |

### **Number of Input registers** — Number of input registers to be read by client `1` (default) | scalar

Enter the number of input registers from which you want the client to read the data.
For example, for the client to read data from the input registers with addresses ranging
from `25` to `26`, enter `2`.

#### Dependencies

To enable this parameter, set **Function** to `Read
Multiple Input Registers`.

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `numElements_inputReg` |
| **Type:** character vector |
| **Values:** `'1'` | scalar |
| **Default:**  `'1'` |

### **Sample Time** — Time interval at which client reads data `0.1` (default) | scalar

Enter the time interval (in seconds) at which the client reads data from the server
device register(s).

#### Programmatic Use

|  |
| --- |
| **Block Parameter:** `SampleTime` |
| **Type:** character vector |
| **Values:** scalar | vector |
| **Default:** `'0.1'` |

## Libraries

NVIDIA Jetson and NVIDIA DRIVE / Network

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2022a**

## Description

Client device reads data from server device register(s) over TCP/IP network

In the Modbus TCP/IP Client Read block, the client device reads data from
the register(s) of the server device.

MATLAB®
Coder™ Support Package for NVIDIA®
Jetson™ and NVIDIA DRIVE® Platforms supports the Modbus® communication protocol over the TCP/IP network on Jetson platforms. The client and the server must be connected to the TCP/IP network for successful
Modbus communication.

**Note**

The Modbus TCP/IP Client Read block is not supported on NVIDIA DRIVE platforms.

The client can perform either a read, write, or a read and write operation on the server
register depending on the server register(s) type.

| Register Type | Register Size | Operation Performed by client |
| --- | --- | --- |
| Coil | 1-bit | Read and write |
| Discrete Input | 1-bit | Read |
| Holding Register | 16-bit | Read and write |
| Input Register | 16-bit | Read |
