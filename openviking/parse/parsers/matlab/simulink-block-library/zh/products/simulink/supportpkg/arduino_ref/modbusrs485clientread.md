---
type: simulink-block
title: 'Modbus RS485 Client Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Arduino Hardware / Peripherals / Communication Protocols / Modbus'
documentation_page: 'modbusrs485clientread'
documentation_source_path: 'supportpkg/arduino_ref/modbusrs485clientread.html'
language: zh-CN
chinese_source: worker-translation
---

# Modbus RS485 Client Read

## 端口

### 输出

### **data** — 输出数据向量

该模块将客户端从服务器设备寄存器读取的数据输出为 *N*×1 向量，其中 *N* 表示服务器设备上的寄存器数量。

- 如果选择线圈或离散输入读取操作，客户端会将服务器寄存器作为 1-bit 读取操作读取。该模块将读取的数据输出为 `Boolean` 数据。
- 如果选择保持寄存器或输入寄存器读取操作，客户端会将服务器寄存器作为 16-bit 读取操作读取。该模块将读取的数据输出为 `uint16` 数据。

**数据类型：** `Boolean` | `uint16`

### **status** — 读取操作状态 `0` | `1`

该模块输出客户端在服务器设备寄存器上读取操作的状态。

- `0`：表示读取操作不成功，这意味着在 **data** 端口接收到的数据无效。
- `1`：表示读取操作成功，这意味着在 **data** 端口接收到的数据有效。

**数据类型：** `uint8`

## 参数

### **Server address** — 唯一的 8 位 Modbus 服务器标识符 `1`（默认）| 范围 [`1`, `255`] 中的标量

输入唯一的 8 位 Modbus 服务器地址或标识符，以标识客户端读取数据的服务器。

### **Function** — 读取操作类型 `Read Coil`（默认）| `Read Discrete input` | `Read Holding register` | `Read Input register` | `Read Multiple Coils` | `Read Multiple Discrete inputs` | `Read Multiple Holding registers` | `Read Multiple Input registers`

选择要在服务器寄存器上执行的读取操作类型。
指定以下任一项：

- `Read Coil`：从 **Coil Address** 参数中指定的线圈寄存器地址读取数据。
- `Read Discrete input`：从 **Discrete Input Address** 参数中指定的离散输入寄存器地址读取数据。
- `Read Holding register`：从 **Holding Register Address** 参数中指定的保持寄存器地址读取数据。
- `Read Input register`：从 **Input Register Address** 参数中指定的输入寄存器地址读取数据。
- `Read Multiple Coils`：根据 **Coil Address** 和 **Number of Coils** 参数中指定的值，从多个线圈寄存器读取数据。
- `Read Multiple Discrete inputs`：根据 **Discrete Input Address** 和 **Number of Discrete Inputs** 参数中指定的值，从多个离散输入寄存器读取数据。
- `Read Multiple Holding registers`：根据 **Holding Register Address** 和 **Number of Holding registers** 参数中指定的值，从多个保持寄存器读取数据。
- `Read Multiple Input registers`：根据 **Input Register Address** 和 **Number of Input registers** 参数中指定的值，从多个输入寄存器读取数据。

### **Coil Address** — 线圈寄存器地址 `0`（默认）| 标量

- 要通知客户端从特定线圈寄存器读取数据，请在此参数中指定线圈寄存器地址。例如，要让客户端从地址为 `10` 的线圈寄存器读取数据，请输入 `10`。
- 要通知客户端从一组线圈寄存器读取数据，请指定该组中第一个线圈寄存器的地址。例如，要让客户端从地址范围为 `10` 到 `14` 的线圈寄存器读取数据，请输入 `10`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Read Coil`。

### **Number of Coils** — 客户端要读取的线圈寄存器数量 `1`（默认）| 标量

输入希望客户端从中读取数据的线圈寄存器数量。例如，要让客户端从地址范围为 `10` 到 `14` 的线圈寄存器读取数据，请输入 `5`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Read Multiple Coils`。

### **Discrete Input Address** — 离散输入寄存器地址 `0`（默认）| 标量

- 要通知客户端从特定离散输入寄存器读取数据，请在此参数中指定离散输入寄存器地址。例如，要让客户端从地址为 `80` 的离散输入寄存器读取数据，请输入 `80`。
- 要通知客户端从一组离散输入寄存器读取数据，请指定该组中第一个离散输入寄存器的地址。例如，要让客户端从地址范围为 `80` 到 `89` 的离散输入寄存器读取数据，请输入 `80`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Read Discrete input`。

### **Number of Discrete Inputs** — 客户端要读取的离散输入寄存器数量 `1`（默认）| 标量

输入希望客户端从中读取数据的离散输入寄存器数量。例如，要让客户端从地址范围为 `80` 到 `89` 的离散输入寄存器读取数据，请输入 `10`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Read Multiple Discrete inputs`。

### **Holding Register Address** — 保持寄存器地址 `0`（默认）| 标量

- 要通知客户端从特定保持寄存器读取数据，请在此参数中指定保持寄存器地址。例如，要让客户端从地址为 `37` 的保持寄存器读取数据，请输入 `37`。
- 要通知客户端从一组保持寄存器读取数据，请指定该组中第一个保持寄存器的地址。例如，要让客户端从地址范围为 `37` 到 `44` 的保持寄存器读取数据，请输入 `37`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Read Holding register`。

### **Number of Holding registers** — 客户端要读取的保持寄存器数量 `1`（默认）| 标量

输入希望客户端从中读取数据的保持寄存器数量。例如，要让客户端从地址范围为 `37` 到 `44` 的保持寄存器读取数据，请输入 `8`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Read Multiple Holding registers`。

### **Input Register Address** — 输入寄存器地址 `0`（默认）| 标量

- 要通知客户端从特定输入寄存器读取数据，请在此参数中指定输入寄存器地址。例如，要让客户端从地址为 `25` 的输入寄存器读取数据，请输入 `25`。
- 要通知客户端从一组输入寄存器读取数据，请指定该组中第一个输入寄存器的地址。例如，要让客户端从地址范围为 `25` 到 `26` 的输入寄存器读取数据，请输入 `25`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Read Input register`。

### **Number of Input registers** — 客户端要读取的输入寄存器数量 `1`（默认）| 标量

输入希望客户端从中读取数据的输入寄存器数量。例如，要让客户端从地址范围为 `25` 到 `26` 的输入寄存器读取数据，请输入 `2`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Read Multiple Input registers`。

### **Sample Time** — 客户端读取数据的时间间隔 `0.1`（默认）| 标量

输入客户端从服务器设备寄存器读取数据的时间间隔（以 seconds 为单位）。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

## 描述

客户端设备通过 RS485 网络从服务器设备寄存器读取数据

在 Modbus RS485 Client Read 模块中，客户端设备从服务器设备的寄存器读取数据。

Simulink® Support Package for Arduino® Hardware 支持通过 RS485 网络的 Modbus® 通信协议。客户端和服务器必须连接到同一个 RS485 网络，才能成功进行 Modbus 通信。RS485 网络上的每个设备都由唯一的 8 位地址或标识符引用。

此表对 Modbus 客户端设备引用的服务器设备寄存器进行分类。

| 寄存器类型 | 寄存器大小 | 允许的客户端寄存器操作 |
| --- | --- | --- |
| 线圈 | 1-bit | 读取和写入 |
| 离散输入 | 1-bit | 读取 |
| 保持寄存器 | 16-bit | 读取和写入 |
| 输入寄存器 | 16-bit | 读取 |

客户端可以对服务器设备的寄存器执行读取或写入操作（具体取决于寄存器类型）。
