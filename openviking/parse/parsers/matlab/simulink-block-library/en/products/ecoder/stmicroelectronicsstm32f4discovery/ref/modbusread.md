---
type: simulink-block
title: 'Modbus Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Communication'
documentation_page: 'modbusread'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/modbusread.html'
language: en
---

# Modbus Read

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

## Parameters

### **Block type** — Modbus read block type `Client` (default) | `Server`

Select the Modbus read block type.

### **Server ID** — Unique 8-bit Modbus server identifier `0` (default) | scalar in the range [`1`, `255`]

Enter the unique 8-bit Modbus server address or identifier to identify the server from which the
client reads the data.

### **Register type** — Type of read operation `Coil` (default) | `Discrete input` | `Holding register` | `Input register`

Select the server register on which you want to perform read operation. Specify
any one of the following:

- `Coil`: Read data from the coil register starting
  at the address specified in the **Coil Address**
  parameter.
- `Discrete input`: Read data from the discrete input
  register starting at the address specified in the **Discrete Input
  Address** parameter.
- `Holding register`: Read data from the holding
  register starting at the address specified in the **Holding Register
  Address** parameter.
- `Input register`: Read data from the input register
  starting at the address specified in the **Input Register
  Address** parameter.

### **Address** — Start address of the read command `0` (default) | scalar

Specify the start address to execute the read operation. Use zero-based
indexing; for example, to read from the 10th location, specify the value as
9.

### **Number of registers** — Number of registers for the client to read `1` (default) | scalar

Specify the number of registers the client reads data from. For example, for
the client to read data from the coil registers with location ranging from
`10` to `14`, enter
`5`.

### **UART/USART module** — USART or UART module for MODBUS communication `USART1` (default) | `USART2` | `UART4`

Configure the USART or UART module for MODBUS communication.

To enable read of a particular register, navigate to the
**Configuration Parameters > Hardware Implementation > Target hardware
resources > USART/UART** properties.

### **Timeout** — Allowed time to complete operations `0.1` (default) | scalar

Amount of time in seconds that the model waits for data during each simulation
time step.

### **Sample Time** — Time interval at which client reads data `1` (default) | scalar

Enter the time interval (in seconds) at which the client reads data from the server
device register(s).

## Libraries

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2025a**

## Description

Read data from server device register(s) over RS485 network

In the Modbus Read block,

- **Client**: Read data from a Modbus® server connected on the RS485 network.
- **Server:** Reads data from its own registers.

The Modbus Read block outputs the values read as an [Nx1] array of
`uint16` or logical values based on the register category.

Embedded Coder® Support Package for STMicroelectronics® STM32 Processors supports the Modbus communication protocol over the RS485 network. The client and the server must
be connected on the same RS485 network for successful Modbus communication. Each device on the RS485 network is referenced by a unique
8-bit address or identifier.

This table categories the server device registers referenced by the Modbus client device.

| Register Type | Register Size | Allowed Client Operation on Register |
| --- | --- | --- |
| Coil | 1-bit | Read and Write |
| Discrete Input | 1-bit | Read |
| Holding Register | 16-bit | Read and Write |
| Input Register | 16-bit | Read |

The client can perform either a read or a write operation (depending on the register
type) on register(s) of a server device.

**Note**

Ensure that the number of client write registers does not exceed the server read
register count.

To enable the Modbus communication on a particular UART, navigate to the
**Configuration Parameters > Hardware Implementation > Target hardware resources
> USART/UART** properties of the model and perform the following:

1. Enable the Modbus on required USART/UART peripheral.
2. Select the **MODBUS Mode** parameter as
   **Server** or **Client**. If you set the
   **MODBUS Mode** to `Server`, configure the
   registers accordingly.
3. Select the register type to configure and enter the register address in the
   **Start address** field. For more information, see UART/USART.

UART/USART Configuration
