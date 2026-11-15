---
type: simulink-block
title: 'Modbus TCP/IP Server Read'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Network'
documentation_page: 'modbustcpipserverread'
documentation_source_path: 'supportpkg/raspberrypi_ref/modbustcpipserverread.html'
language: zh-CN
chinese_source: worker-translation
---

# Modbus TCP/IP Server Read

## 端口

### 输出

### **Data** — 输出数据标量

该模块将服务器设备从其寄存器读取的数据输出为 1-bit 标量。

- 如果选择线圈或离散输入读取操作，服务器将其寄存器作为 1-bit 读取操作读取。该模块将读取的数据输出为 Boolean 数据。
- 如果选择保持寄存器或输入寄存器读取操作，服务器将其寄存器作为 16-bit 读取操作读取。该模块将读取的数据输出为 uint16 数据。

**数据类型：** `Boolean` | `uint16`

### **Status** — 读取操作的状态 `0` | `1`

该模块输出服务器寄存器上服务器读取操作的状态。

- `0`：表示读取操作不成功，这意味着在 **data** 端口上接收到的数据无效。
- `1`：表示读取操作成功，这意味着在 **data** 端口上接收到的数据有效。

**数据类型：** `uint8`

## 参数

### **Function** — 读取操作的类型 `Read Coil`（默认） | `Read Discrete Input` | `Read Holding register` | `Read Input register`

选择要在服务器寄存器上执行的读取操作类型。指定以下任意一项：

- `Read Coil`：从 **Coil Address** 参数中指定的线圈寄存器地址读取数据。
- `Read Discrete Input`：从 **Discrete Input Address** 参数中指定的离散输入寄存器地址读取数据。
- `Read Holding register`：从 **Holding Register Address** 参数中指定的保持寄存器地址读取数据。
- `Read Input register`：从 **Input Register Address** 参数中指定的输入寄存器地址读取数据。

### **Coil Address** — 线圈寄存器地址 `0`（默认） | 标量

要通知服务器从特定线圈寄存器读取数据，请在该参数中指定线圈寄存器地址。例如，要让服务器从地址为 `10` 的线圈寄存器读取数据，请输入 `10`。

#### 依赖关系

要启用该参数，请将 **Function** 设置为 `Read Coil`。

### **Discrete Input Address** — 离散输入寄存器地址 `0`（默认） | 标量

要通知服务器从特定离散输入寄存器读取数据，请在该参数中指定离散输入寄存器地址。例如，要让服务器从地址为 `80` 的离散输入寄存器读取数据，请输入 `80`。

#### 依赖关系

要启用该参数，请将 **Function** 设置为 `Read Discrete Input`。

### **Holding Register Address** — 保持寄存器地址 `0`（默认） | 标量

要通知服务器从特定保持寄存器读取数据，请在该参数中指定保持寄存器地址。例如，要让服务器从地址为 `37` 的保持寄存器读取数据，请输入 `37`。

#### 依赖关系

要启用该参数，请将 **Function** 设置为 `Read Holding register`。

### **Input Register Address** — 输入寄存器地址 `0`（默认） | 标量

要通知服务器从特定输入寄存器读取数据，请在该参数中指定输入寄存器地址。例如，要让服务器从地址为 `25` 的输入寄存器读取数据，请输入 `25`。

#### 依赖关系

要启用该参数，请将 **Function** 设置为 `Read Input register`。

### **Sample Time** — 服务器读取数据的时间间隔 `0.1`（默认） | 标量

输入服务器从其寄存器读取数据的时间间隔（以 seconds 为单位）。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Network

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2021a 中引入**

## 描述

服务器设备通过 TCP/IP 网络从服务器设备寄存器读取数据

在 Modbus TCP/IP Server Read 模块中，服务器设备从其寄存器读取数据。服务器每次读取操作只能从一个寄存器读取数据。

Simulink® Support Package for Raspberry Pi® Hardware 支持 TCP/IP 网络上的 Modbus® 通信协议。

服务器可以对这些服务器寄存器执行读取和写入操作。

| 寄存器类型 | 寄存器大小 |
| --- | --- |
| 线圈 | 1-bit |
| 离散输入 | 1-bit |
| 保持寄存器 | 16-bit |
| 输入寄存器 | 16-bit |

服务器可以对其寄存器执行读取或写入操作。

**注意**

要为该模块生成 C/C++ 代码，必须具有 Embedded Coder® 许可证。
