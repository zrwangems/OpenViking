---
type: simulink-block
title: 'Modbus RS485 Client Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / STMicroelectronics STM32 Processors / STMicroelectronics Discovery Boards / Modeling / STMicroelectronics STM32F746G/STM32F769I-Discovery Board Blocks / Communication'
documentation_page: 'modbusrs485clientwrite'
documentation_source_path: 'stmicroelectronicsstm32f4discovery/ref/modbusrs485clientwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Modbus RS485 Client Write

## 端口

### 输入

### **data** — 输入数据向量

模块的输入是客户端要写入服务器寄存器的数据，形式为 *N*-by-1 向量，其中 *N* 表示服务器设备上的寄存器数量。

- 如果选择 Coil 或 Discrete Input 写操作，客户端以具有 Boolean 数据类型的 1-bit 写操作将数据写入服务器寄存器。
- 如果选择 Holding Register 或 Input Register 写操作，客户端以具有 uint16 数据类型的 16-bit 写操作将数据写入服务器寄存器。

**数据类型：** `Boolean` | `uint16`

### 输出

### **status** — 写操作的状态 `0` | `1`

模块输出客户端设备寄存器上客户端写操作的状态。

- `1`：表示对服务器寄存器的写操作未成功，或未在超时时间内收到服务器响应。
- `0`：表示对服务器寄存器的写操作成功，并在超时时间内收到预期响应。

#### 依赖项

要启用此端口，请选择 **Output status** 参数。

**数据类型：** `uint8`

## 参数

### **Server address (0 for broadcast)** — 唯一的 8-bit Modbus 服务器标识符 `1`（默认）| 范围 [`1`, `255`] 内的标量

输入唯一的 8-bit Modbus 服务器地址或标识符，以标识客户端将数据写入的服务器。

### **Function** — 写操作类型 `Write Coil`（默认）| `Write Holding register` | `Write Multiple Coils` | `Write Multiple Holding registers`

选择要在服务器寄存器上执行的写操作类型。指定以下任一项：

- `Write Coil`：将数据写入 **Coil Address** 参数中指定的 Coil 寄存器地址
- `Write Holding register`：将数据写入 **Holding Register Address** 参数中指定的 Holding Register 地址
- `Write Multiple Coils`：根据 **Coil Address** 和 **Number of Coils** 参数中指定的值，将数据写入多个 Coil 寄存器
- `Write Multiple Holding registers`：根据 **Holding Register Address** 和 **Number of Holding registers** 参数中指定的值，将数据写入多个 Holding Register

### **Coil Address** — Coil 寄存器地址 `0`（默认）| 标量

- 要通知客户端将数据写入特定 Coil 寄存器，请在此参数中指定 Coil 寄存器地址。例如，要让客户端将数据写入地址为 `10` 的 Coil 寄存器，请输入 `10`。
- 要通知客户端将数据写入一组 Coil 寄存器，请指定该组中第一个 Coil 寄存器的地址。例如，要让客户端将数据写入地址范围为 `10` 到 `14` 的 Coil 寄存器，请输入 `10`。

#### 依赖项

要启用此参数，请将 **Function** 设置为 `Write Coil`。

### **Number of Coils** — 客户端要写入的 Coil 寄存器数量 `1`（默认）| 标量

输入希望客户端将数据写入的 Coil 寄存器数量。例如，要让客户端将数据写入地址范围为 `10` 到 `14` 的 Coil 寄存器，请输入 `5`。

#### 依赖项

要启用此参数，请将 **Function** 设置为 `Write Multiple Coils`。

### **Holding Register Address** — Holding Register 地址 `0`（默认）| 标量

- 要通知客户端将数据写入特定 Holding Register，请在此参数中指定 Holding Register 地址。例如，要让客户端将数据写入地址为 `37` 的 Holding Register，请输入 `37`。
- 要通知客户端将数据写入一组 Holding Register，请指定该组中第一个 Holding Register 的地址。例如，要让客户端将数据写入地址范围为 `37` 到 `44` 的 Holding Register，请输入 `37`。

#### 依赖项

要启用此参数，请将 **Function** 设置为 `Write Holding register`。

### **Number of Holding registers** — 客户端要写入的 Holding Register 数量 `1`（默认）| 标量

输入希望客户端将数据写入的 Holding Register 数量。例如，要让客户端将数据写入地址范围为 `37` 到 `44` 的 Holding Register，请输入 `8`。

#### 依赖项

要启用此参数，请将 **Function** 设置为 `Write Multiple Holding registers`。

### **Output status** — 启用输出状态 `off`（默认）| `on`

选择 **Output Status** 参数时，模块会配置一个输出端口 **Status**。该端口输出状态消息。

## 所属库

Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F746G-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32F769I-Discovery Embedded Coder Support Package for STMicroelectronics STM32 Processors / STM32L475VG-Discovery (B-L475E-IOT01A) Simulink Coder Support Package for STMicroelectronics Nucleo Boards / Common

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

客户端设备通过 RS485 网络将数据写入服务器设备寄存器

在 Modbus RS485 Client Write 模块中，客户端设备将数据写入服务器设备的寄存器。

Simulink® Coder™ Support Package for STMicroelectronics® Nucleo Boards 和 Embedded Coder® Support Package for STMicroelectronics Discovery Boards 支持通过 RS485 网络的 Modbus® 通信协议。客户端和服务器必须连接到同一 RS485 网络才能成功进行 Modbus 通信。RS485 网络上的每个设备都由唯一的 8-bit 地址或标识符引用。

此表对 Modbus 客户端设备引用的服务器设备寄存器进行分类。

| 寄存器类型 | 寄存器大小 | 寄存器上允许的客户端操作 |
| --- | --- | --- |
| Coil | 1-bit | Read and Write |
| Discrete Input | 1-bit | Read |
| Holding Register | 16-bit | Read and Write |
| Input Register | 16-bit | Read |

客户端可以在服务器设备的寄存器上执行读操作或写操作（取决于寄存器类型）。
