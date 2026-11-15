---
type: simulink-block
title: 'Modbus TCP/IP Server Write'
family: 'simulink'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Simulink Supported Hardware / Raspberry Pi Hardware / Modeling / Network'
documentation_page: 'modbustcpipserverwrite'
documentation_source_path: 'supportpkg/raspberrypi_ref/modbustcpipserverwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Modbus TCP/IP Server Write

## 端口

### 输入

### **Input** — 输入数据标量

模块的输入是服务器以 1-bit 标量形式写入其寄存器的数据。

- 如果选择 Coil 或 Discrete Input 写操作，则服务器将数据作为 1-bit 写操作以 Boolean 数据写入其寄存器。
- 如果选择 Holding Register 或 Input Register 写操作，则服务器将数据作为 16-bit 写操作以 uint16 数据写入其寄存器。

**数据类型：** `Boolean` | `uint16`

## 参数

### **Function** — 写操作的类型 `Write Coil` (默认) | `Write Discrete Input` | `Write Holding register` | `Write Input register`

选择要在服务器寄存器上执行的写操作类型。指定以下任意一项：

- `Write Coil`：将数据写入 **Coil Address** 参数中指定的 coil 寄存器地址。
- `Write Discrete Input`：将数据写入 **Discrete Input Address** 参数中指定的 discrete input 寄存器地址。
- `Write Holding register`：将数据写入 **Holding Register Address** 参数中指定的 holding 寄存器地址。
- `Write Input register`：将数据写入 **Input Register Address** 参数中指定的 input 寄存器地址。

### **Coil Address** — coil 寄存器地址 `0` (默认) | scalar

要通知服务器将数据写入特定的 coil 寄存器，请在此参数中指定 coil 寄存器地址。例如，要让服务器将数据写入地址为 `10` 的 coil 寄存器，请输入 `10`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Write Coil`。

### **Discrete Input Address** — discrete input 寄存器地址 `0` (默认) | scalar

要通知服务器将数据写入特定的 discrete input 寄存器，请在此参数中指定 discrete input 寄存器地址。例如，要让服务器将数据写入地址为 `80` 的 discrete input 寄存器，请输入 `80`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Write Discrete Input`。

### **Holding Register Address** — holding 寄存器地址 `0` (默认) | scalar

要通知服务器将数据写入特定的 holding 寄存器，请在此参数中指定 holding 寄存器地址。例如，要让服务器将数据写入地址为 `37` 的 holding 寄存器，请输入 `37`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Write Holding register`。

### **Input Register Address** — input 寄存器地址 `0` (默认) | scalar

要通知服务器将数据写入特定的 input 寄存器，请在此参数中指定 input 寄存器地址。例如，要让服务器将数据写入地址为 `25` 的 input 寄存器，请输入 `25`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Write Input register`。

## 所属库

Simulink Support Package for Raspberry Pi Hardware / Network

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2021a 中引入**

## 描述

服务器设备通过 TCP/IP 网络将数据写入服务器设备寄存器

在 Modbus TCP/IP Server Write 模块中，服务器设备将数据写入其寄存器。服务器每次读操作只能向一个寄存器写入数据。

Simulink® Support Package for Raspberry Pi® Hardware 支持通过 TCP/IP 网络的 Modbus® 通信协议。

服务器可以对这些服务器寄存器执行读和写操作。

| 寄存器类型 | 寄存器大小 |
| --- | --- |
| Coil | 1-bit |
| Discrete Input | 1-bit |
| Holding Register | 16-bit |
| Input Register | 16-bit |

**注意**

要为该模块生成 C/C++ 代码，您必须具有 Embedded Coder® 许可证。
