---
type: simulink-block
title: 'Modbus Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / Peripherals / Connectivity Peripherals / Communication'
documentation_page: 'modbuswrite'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/modbuswrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Modbus Write

## 端口

### 输入

### **data** — 输入数据向量

模块的输入是客户端要写入服务器寄存器的数据，形式为 *N*-by-1 向量，其中 *N* 表示服务器设备上的寄存器数量。

- 如果选择 Coil 或 Discrete Input 写操作，则客户端将数据作为具有 Boolean 数据类型的 1-bit 写操作写入服务器寄存器。
- 如果选择 Holding Register 或 Input Register 写操作，则客户端将数据作为具有 uint16 数据类型的 16-bit 写操作写入服务器寄存器。

**数据类型：** `Boolean` | `uint16`

## 参数

### **模块类型** — Modbus 模块类型 `Client`（默认） | `Server`

选择 Modbus 写入模块类型。

### **服务器 ID** — 唯一的 8-bit Modbus 服务器标识符 `0`（默认） | 范围 [`1`, `255`] 中的标量

输入唯一的 8-bit Modbus 服务器 ID 或标识符，以标识客户端要将数据写入的服务器。

### **寄存器类型** — 写操作类型 `Coil`（默认） | `Discrete input` | `Holding register` | `Input register`

选择要在服务器寄存器上执行的写操作类型。指定以下任一项：

- `Coil`：将数据写入线圈寄存器，从 **Coil 地址** 参数中指定的地址开始。
- `Discrete input`：将数据写入离散输入寄存器，从 **Discrete Input 地址** 参数中指定的地址开始。客户端模式不支持将数据写入离散输入寄存器地址
- `Holding register`：将数据写入保持寄存器，从 **Holding Register 地址** 参数中指定的地址开始。
- `Input register`：将数据写入输入寄存器，从 **Input Register 地址** 参数中指定的地址开始。

### **地址** — 写命令的起始地址 `0`（默认） | 标量

指定要执行写操作的起始地址。使用从零开始的索引；例如，要从第 10 个位置读取，请将值指定为 9。

### **寄存器数量** — 客户端要写入的寄存器数量 `1`（默认） | 标量

指定客户端要写入数据的寄存器数量。例如，要使客户端写入位置范围从 `10` 到 `14` 的线圈寄存器中的数据，请输入 `5`。

### **UART/USART 模块** — 用于 MODBUS 通信的 USART 或 UART 模块 `USART1`（默认） | `USART2` | `UART4`

配置用于 MODBUS 通信的 USART 或 UART 模块。

要启用对特定寄存器的读取，请导航到 **配置参数 > 硬件实现 > 目标硬件资源 > USART/UART** 属性。

### **超时** — 完成操作所允许的时间 `0.1`（默认） | 标量

模型在每个仿真时间步期间等待数据的时间量，单位为 seconds。

### **采样时间** — 客户端写入数据的时间间隔 `1`（默认） | 标量

输入客户端向服务器设备寄存器写入数据的时间间隔（以 seconds 为单位）。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2025a 中引入**

## 描述

通过 RS485 网络将数据写入服务器设备寄存器

Modbus Write 模块将数据写入服务器设备的寄存器。

Modbus Write 模块对于单寄存器写操作接受 `uint16` 类型的数据，对于多寄存器写操作接受 `uint16` 类型的 [Nx1] 向量数据。

Embedded Coder® Support Package for STMicroelectronics® STM32 Processors 支持通过 RS485 网络的 Modbus® 通信协议。客户端和服务器必须连接到同一 RS485 网络，才能成功进行 Modbus 通信。RS485 网络上的每个设备都由唯一的 8-bit 地址或标识符引用。

此表对 Modbus 客户端设备引用的服务器设备寄存器进行了分类。

| 寄存器类型 | 寄存器大小 | 允许的客户端寄存器操作 |
| --- | --- | --- |
| Coil | 1-bit | 读取和写入 |
| Discrete Input | 1-bit | 读取 |
| Holding Register | 16-bit | 读取和写入 |
| Input Register | 16-bit | 读取 |

客户端可以对服务器设备的寄存器执行读操作或写操作（取决于寄存器类型）。

**注意**

确保客户端写入寄存器数量不超过服务器读取寄存器数量。

要在特定 UART 上启用 Modbus 通信，请导航到模型的 **配置参数 > 硬件实现 > 目标硬件资源 > USART/UART** 属性，并执行以下操作：

1. 在所需的 USART/UART 外设上启用 Modbus。
2. 将 **MODBUS 模式** 参数选择为 **Server** 或 **Client**。如果将 **MODBUS 模式** 设置为 `Server`，请相应配置寄存器。
3. 选择要配置的寄存器类型，并在 **起始地址** 字段中输入寄存器地址。有关更多信息，请参阅 UART/USART。

UART/USART 配置
