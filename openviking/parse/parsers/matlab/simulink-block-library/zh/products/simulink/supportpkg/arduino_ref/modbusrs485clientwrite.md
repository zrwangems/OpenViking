---
type: simulink-block
title: 'Modbus RS485 Client Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Modbus'
documentation_page: 'modbusrs485clientwrite'
documentation_source_path: 'supportpkg/arduino_ref/modbusrs485clientwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Modbus RS485 Client Write

## 端口

### 输入

### **data** — 输入数据向量

模块的输入是客户端要写入服务器寄存器的数据，为 *N*-by-1 向量，其中 *N* 表示服务器设备上的寄存器数量。

- 如果您选择 Coil 或 Discrete Input 写操作，则客户端将数据作为具有 Boolean 数据类型的 1-bit 写操作写入服务器寄存器。
- 如果您选择 Holding Register 或 Input Register 写操作，则客户端将数据作为具有 uint16 数据类型的 16-bit 写操作写入服务器寄存器。

**数据类型：** `Boolean` | `uint16`

## 参数

### **Server address** — 唯一 8 位 Modbus 服务器标识符 `1`（默认值）| 范围 [`1`, `255`] 中的标量

输入唯一的 8 位 Modbus 服务器地址或标识符，以标识客户端将数据写入的服务器。

### **Function** — 写操作类型 `Write Coil`（默认值）| `Write Holding register` | `Write Multiple Coils` | `Write Multiple Holding registers`

选择您要对服务器寄存器执行的写操作类型。指定以下任一项：

- `Write Coil`：将数据写入 **Coil Address** 参数中指定的线圈寄存器地址
- `Write Holding register`：将数据写入 **Holding Register Address** 参数中指定的保持寄存器地址
- `Write Multiple Coils`：根据 **Coil Address** 和 **Number of Coils** 参数中指定的值，将数据写入多个线圈寄存器
- `Write Multiple Holding registers`：根据 **Holding Register Address** 和 **Number of Holding registers** 参数中指定的值，将数据写入多个保持寄存器

### **Coil Address** — 线圈寄存器地址 `0`（默认值）| 标量

- 要通知客户端将数据写入特定线圈寄存器，请在此参数中指定线圈寄存器地址。例如，要让客户端将数据写入地址为 `10` 的线圈寄存器，请输入 `10`。
- 要通知客户端将数据写入一组线圈寄存器，请指定该组中第一个线圈寄存器的地址。例如，要让客户端将数据写入地址范围为 `10` 到 `14` 的线圈寄存器，请输入 `10`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Write Coil`。

### **Number of Coils** — 客户端要写入的线圈寄存器数量 `1`（默认值）| 标量

输入您希望客户端将数据写入的线圈寄存器数量。例如，要让客户端将数据写入地址范围为 `10` 到 `14` 的线圈寄存器，请输入 `5`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Write Multiple Coils`。

### **Holding Register Address** — 保持寄存器地址 `0`（默认值）| 标量

- 要通知客户端将数据写入特定保持寄存器，请在此参数中指定保持寄存器地址。例如，要让客户端将数据写入地址为 `37` 的保持寄存器，请输入 `37`。
- 要通知客户端将数据写入一组保持寄存器，请指定该组中第一个保持寄存器的地址。例如，要让客户端将数据写入地址范围为 `37` 到 `44` 的保持寄存器，请输入 `37`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Write Holding register`。

### **Number of Holding registers** — 客户端要写入的保持寄存器数量 `1`（默认值）| 标量

输入您希望客户端将数据写入的保持寄存器数量。例如，要让客户端将数据写入地址范围为 `37` 到 `44` 的保持寄存器，请输入 `8`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Write Multiple Holding registers`。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

## 描述

客户端设备通过 RS485 网络将数据写入服务器设备寄存器

在 Modbus RS485 Client Write 模块中，客户端设备将数据写入服务器设备的寄存器。

Simulink® Support Package for Arduino® Hardware 支持通过 RS485 网络进行 Modbus® 通信协议。为了实现成功的 Modbus 通信，客户端和服务器必须连接在同一 RS485 网络上。RS485 网络上的每个设备通过唯一的 8 位地址或标识符引用。

下表对 Modbus 客户端设备引用的服务器设备寄存器进行分类。

| 寄存器类型 | 寄存器大小 | 允许的客户端对寄存器操作 |
| --- | --- | --- |
| 线圈 | 1-bit | 读取和写入 |
| 离散输入 | 1-bit | 读取 |
| 保持寄存器 | 16-bit | 读取和写入 |
| 输入寄存器 | 16-bit | 读取 |

客户端可以对服务器设备的寄存器执行读或写操作（取决于寄存器类型）。
