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
language: zh-CN
chinese_source: worker-translation
---

# Modbus Read

## 端口

### 输出

### **data** — 输出数据向量

该模块将客户端从服务器设备寄存器读取的数据输出为 *N*×1 向量，其中 *N* 表示服务器设备上的寄存器数量。

- 如果选择 Coil 或 Discrete Input 读取操作，客户端将服务器寄存器作为 1-bit 读取操作读取。该模块将读取的数据输出为 `Boolean` 数据。
- 如果选择 Holding Register 或 Input Register 读取操作，客户端将服务器寄存器作为 16-bit 读取操作读取。该模块将读取的数据输出为 `uint16` 数据。

**数据类型：** `Boolean` | `uint16`

## 参数

### **模块类型** — Modbus 读取模块类型 `Client`（默认）| `Server`

选择 Modbus 读取模块类型。

### **服务器 ID** — 唯一的 8-bit Modbus 服务器标识符 `0`（默认）| scalar，范围为 [`1`, `255`]

输入唯一的 8-bit Modbus 服务器地址或标识符，以标识客户端从中读取数据的服务器。

### **寄存器类型** — 读取操作的类型 `Coil`（默认）| `Discrete input` | `Holding register` | `Input register`

选择要对其执行读取操作的服务器寄存器。指定以下任一项：

- `Coil`：从 **Coil 地址** 参数中指定的地址开始，从 Coil 寄存器读取数据。
- `Discrete input`：从 **Discrete Input 地址** 参数中指定的地址开始，从 Discrete Input 寄存器读取数据。
- `Holding register`：从 **Holding Register 地址** 参数中指定的地址开始，从 Holding Register 寄存器读取数据。
- `Input register`：从 **Input Register 地址** 参数中指定的地址开始，从 Input Register 寄存器读取数据。

### **地址** — 读取命令的起始地址 `0`（默认）| scalar

指定要执行读取操作的起始地址。使用从零开始的索引；例如，要从第 10 个位置读取，请将值指定为 9。

### **寄存器数量** — 客户端要读取的寄存器数量 `1`（默认）| scalar

指定客户端从中读取数据的寄存器数量。例如，要使客户端从位置范围为 `10` 到 `14` 的 Coil 寄存器读取数据，请输入 `5`。

### **UART/USART 模块** — 用于 MODBUS 通信的 USART 或 UART 模块 `USART1`（默认）| `USART2` | `UART4`

配置用于 MODBUS 通信的 USART 或 UART 模块。

要启用对特定寄存器的读取，请导航到模型的 **配置参数 > 硬件实现 > 目标硬件资源 > USART/UART** 属性。

### **超时** — 允许完成操作的时间 `0.1`（默认）| scalar

模型在每个仿真时间步期间等待数据的时间量，单位为 seconds。

### **采样时间** — 客户端读取数据的时间间隔 `1`（默认）| scalar

输入客户端从服务器设备寄存器读取数据的时间间隔（以 seconds 为单位）。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F7xx Based Boards

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2025a 中引入**

## 描述

通过 RS485 网络从服务器设备寄存器读取数据

在 Modbus Read 模块中，

- **Client**：从连接在 RS485 网络上的 Modbus® 服务器读取数据。
- **Server：** 从自己的寄存器读取数据。

Modbus Read 模块根据寄存器类别，将读取的值输出为 `uint16` 或逻辑值的 [Nx1] 数组。

Embedded Coder® Support Package for STMicroelectronics® STM32 Processors 支持通过 RS485 网络的 Modbus 通信协议。为了成功进行 Modbus 通信，客户端和服务器必须连接在同一 RS485 网络上。RS485 网络上的每个设备都由唯一的 8-bit 地址或标识符引用。

下表对 Modbus 客户端设备引用的服务器设备寄存器进行分类。

| 寄存器类型 | 寄存器大小 | 允许的客户端对寄存器的操作 |
| --- | --- | --- |
| Coil | 1-bit | 读取和写入 |
| Discrete Input | 1-bit | 读取 |
| Holding Register | 16-bit | 读取和写入 |
| Input Register | 16-bit | 读取 |

客户端可以对服务器设备的寄存器执行读取或写入操作（取决于寄存器类型）。

**注意**

确保客户端写入寄存器的数量不超过服务器读取寄存器的数量。

要在特定 UART 上启用 Modbus 通信，请导航到模型的 **配置参数 > 硬件实现 > 目标硬件资源 > USART/UART** 属性，并执行以下操作：

1. 在所需的 USART/UART 外设上启用 Modbus。
2. 将 **MODBUS 模式** 参数选择为 **Server** 或 **Client**。如果将 **MODBUS 模式** 设置为 `Server`，请相应地配置寄存器。
3. 选择要配置的寄存器类型，并在 **起始地址** 字段中输入寄存器地址。有关更多信息，请参阅 UART/USART。

UART/USART 配置
