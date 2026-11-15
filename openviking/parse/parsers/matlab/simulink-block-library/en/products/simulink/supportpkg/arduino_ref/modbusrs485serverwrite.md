---
type: simulink-block
title: 'Modbus RS485 Server Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Modbus'
documentation_page: 'modbusrs485serverwrite'
documentation_source_path: 'supportpkg/arduino_ref/modbusrs485serverwrite.html'
language: en
---

# Modbus RS485 Server Write

## Ports

### Input

### **Input** — Input data scalar

The input to the block is the data to be written to its registers by the server as
a 1-bit scalar.

- If you select the Coil or Discrete Input write operations, the server writes
  data to its registers as a 1-bit write operation having the Boolean data
  type.
- If you select the Holding Register or Input Register write operations, the
  server writes data to its registers as a 16-bit write operation having the uint16
  data type.

**Data Types:** `Boolean` | `uint16`

## Parameters

### **Function** — Type of write operation `Write Coil` (default) | `Write Discrete input` | `Write Holding register` | `Write Input register`

Select the type of write operation you want to perform on the server register.
Specify any one of the following:

- `Write Coil`: Write data to the coil register address
  specified in the **Coil Address** parameter
- `Write Discrete input`: Write data to the discrete
  input register address specified in the **Discrete Input Address**
  parameter
- `Write Holding register`: Write data to the holding
  register address specified in the **Holding Register Address**
  parameter
- `Write Input register`: Write data to the input
  register address specified in the **Input Register Address**
  parameter

### **Coil Address** — Address of coil register `0` (default) | scalar

To notify the server to write data to a specific coil register, specify the coil
register address in this parameter. For example, for the server to write data to the
coil register with the address `10`, enter
`10`.

#### Dependencies

To enable this parameter, set **Function** to `Write
Coil`.

### **Discrete Input Address** — Address of discrete input register `0` (default) | scalar

To notify the server to write data to a specific discrete input register, specify
the discrete input register address in this parameter. For example, for the server to
write data to the discrete input register with the address `80`, enter
`80`.

#### Dependencies

To enable this parameter, set **Function** to `Write
Discrete input`.

### **Holding Register Address** — Address of holding register `0` (default) | scalar

To notify the server to write data to a specific holding register, specify the
holding register address in this parameter. For example, for the server to write data to
the holding register with the address `37`, enter
`37`.

#### Dependencies

To enable this parameter, set **Function** to `Write
Holding register`.

### **Input Register Address** — Address of input register `0` (default) | scalar

To notify the server to write data to a specific input register, specify the input
register address in this parameter. For example, for the server to write data to the
input register with the address `25`, enter
`25`.

#### Dependencies

To enable this parameter, set **Function** to `Write
Input register`.

## Libraries

Simulink Support Package for Arduino Hardware / Common

## Block Characteristics

Not documented in R2025b.

## Extended Capabilities

Not documented in R2025b.

## Version History

**Introduced in R2020b**

## Description

Server device writes data to server device register over RS485 network

In the Modbus RS485 Server Write block, the server device writes data to
its registers. The server can write data only to one register per write operation.

Simulink® Support Package for Arduino® Hardware supports the Modbus® communication protocol over the RS485 network. Each device on the RS485 network
is referenced by a unique 8-bit address or identifier.

This table categories the server registers referenced by the Modbus server device.

| Register Type | Register Size |
| --- | --- |
| Coil | 1-bit |
| Discrete Input | 1-bit |
| Holding Register | 16-bit |
| Input Register | 16-bit |
