---
type: simulink-block
title: 'Modbus TCP/IP Client Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Network'
documentation_page: 'modbustcpipclientwrite'
documentation_source_path: 'supportpkg/raspberrypi_ref/modbustcpipclientwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Modbus TCP/IP Client Write

## 端口

### 输入

### **Data** — 输入数据向量

块的输入是客户端写入服务器寄存器的数据。将输入数据指定为 *N*×1 向量，其中 *N* 表示服务器设备上的寄存器数量。

- 如果选择 Coil 或 Discrete Input 写操作，则客户端以 Boolean 数据形式执行 1-bit 写操作，将数据写入服务器寄存器。
- 如果选择 Holding Register 或 Input Register 写操作，则客户端以 uint16 数据形式执行 16-bit 写操作，将数据写入服务器寄存器。

**数据类型：** `Boolean` | `uint16`

## 参数

### **Server address** — 服务器设备的唯一 IP 地址 `127.0.0.1`（默认）| IP 地址

输入服务器设备的 IP 地址，以标识客户端将数据写入的服务器。

### **Function** — 写操作类型 `Write Coil`（默认）| `Write Holding register` | `Write Multiple Coils` | `Write Multiple Holding registers`

选择要在服务器寄存器上执行的写操作类型。指定以下任一项：

- `Write Coil`：将数据写入 **Coil Address** 参数中指定的线圈寄存器地址。
- `Write Holding register`：将数据写入 **Holding Register Address** 参数中指定的保持寄存器地址。
- `Write Multiple Coils`：根据 **Coil Address** 和 **Number of Coils** 参数中指定的值，将数据写入多个线圈寄存器。
- `Write Multiple Holding registers`：根据 **Holding Register Address** 和 **Number of Holding registers** 参数中指定的值，将数据写入多个保持寄存器。

### **Coil Address** — 线圈寄存器地址 `0`（默认）| 标量

- 要通知客户端将数据写入特定线圈寄存器，请在此参数中指定线圈寄存器地址。例如，要让客户端将数据写入地址为 `10` 的线圈寄存器，请输入 `10`。
- 要通知客户端将数据写入一组线圈寄存器，请指定该组中第一个线圈寄存器的地址。例如，要让客户端将数据写入地址范围为 `10` 到 `14` 的线圈寄存器，请输入 `10`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Write Coil`。

### **Number of Coils** — 客户端要写入的线圈寄存器数量 `1`（默认）| 标量

输入您希望客户端将数据写入的线圈寄存器数量。例如，要让客户端将数据写入地址范围为 `10` 到 `14` 的线圈寄存器，请输入 `5`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Write Multiple Coils`。

### **Holding Register Address** — 保持寄存器地址 `0`（默认）| 标量

- 要通知客户端将数据写入特定保持寄存器，请在此参数中指定保持寄存器地址。例如，要让客户端将数据写入地址为 `37` 的保持寄存器，请输入 `37`。
- 要通知客户端将数据写入一组保持寄存器，请指定该组中第一个保持寄存器的地址。例如，要让客户端将数据写入地址范围为 `37` 到 `44` 的保持寄存器，请输入 `37`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Write Holding register`。

### **Number of Holding registers** — 客户端要写入的保持寄存器数量 `1`（默认）| 标量

输入您希望客户端将数据写入的保持寄存器数量。例如，要让客户端将数据写入地址范围为 `37` 到 `44` 的保持寄存器，请输入 `8`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Write Multiple Holding registers`。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Network

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2021a 中引入**

## 描述

客户端设备通过 TCP/IP 网络将数据写入服务器设备寄存器

在 Modbus TCP/IP Client Write 模块中，客户端设备将数据写入服务器设备的寄存器。

Simulink® Support Package for Raspberry Pi® Hardware 支持基于 TCP/IP 网络的 Modbus® 通信协议。客户端和服务器必须连接到 TCP/IP 网络，才能成功进行 Modbus 通信。

客户端可以根据服务器寄存器类型，对服务器寄存器执行读取、写入或读取和写入操作。

| 寄存器类型 | 寄存器大小 | 客户端执行的操作 |
| --- | --- | --- |
| Coil | 1-bit | 读取和写入 |
| Discrete Input | 1-bit | 读取 |
| Holding Register | 16-bit | 读取和写入 |
| Input Register | 16-bit | 读取 |

客户端可以根据寄存器类型，对服务器设备的寄存器执行读取或写入操作。

**注意**

要为该模块生成 C/C++ 代码，您必须拥有 Embedded Coder® 许可证。
