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
language: zh-CN
chinese_source: worker-translation
---

# Modbus RS485 Server Write

## 端口

### 输入

### **Input** — 输入数据标量

模块的输入是服务器要以 1-bit 标量形式写入其寄存器的数据。

- 如果选择线圈或离散输入写操作，则服务器将数据作为具有 Boolean 数据类型的 1-bit 写操作写入其寄存器。
- 如果选择保持寄存器或输入寄存器写操作，则服务器将数据作为具有 uint16 数据类型的 16-bit 写操作写入其寄存器。

**数据类型：** `Boolean` | `uint16`

## 参数

### **Function** — 写操作类型 `Write Coil`（默认） | `Write Discrete input` | `Write Holding register` | `Write Input register`

选择要在服务器寄存器上执行的写操作类型。指定以下任一项：

- `Write Coil`：将数据写入 **Coil Address** 参数中指定的线圈寄存器地址
- `Write Discrete input`：将数据写入 **Discrete Input Address** 参数中指定的离散输入寄存器地址
- `Write Holding register`：将数据写入 **Holding Register Address** 参数中指定的保持寄存器地址
- `Write Input register`：将数据写入 **Input Register Address** 参数中指定的输入寄存器地址

### **Coil Address** — 线圈寄存器地址 `0`（默认） | 标量

要通知服务器将数据写入特定线圈寄存器，请在此参数中指定线圈寄存器地址。例如，要使服务器将数据写入地址为 `10` 的线圈寄存器，请输入 `10`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Write Coil`。

### **Discrete Input Address** — 离散输入寄存器地址 `0`（默认） | 标量

要通知服务器将数据写入特定离散输入寄存器，请在此参数中指定离散输入寄存器地址。例如，要使服务器将数据写入地址为 `80` 的离散输入寄存器，请输入 `80`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Write Discrete input`。

### **Holding Register Address** — 保持寄存器地址 `0`（默认） | 标量

要通知服务器将数据写入特定保持寄存器，请在此参数中指定保持寄存器地址。例如，要使服务器将数据写入地址为 `37` 的保持寄存器，请输入 `37`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Write Holding register`。

### **Input Register Address** — 输入寄存器地址 `0`（默认） | 标量

要通知服务器将数据写入特定输入寄存器，请在此参数中指定输入寄存器地址。例如，要使服务器将数据写入地址为 `25` 的输入寄存器，请输入 `25`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Write Input register`。

## 所属库

Simulink Support Package for Arduino Hardware / Common

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2020b 中引入**

## 描述

服务器设备通过 RS485 网络将数据写入服务器设备寄存器

在 Modbus RS485 Server Write 模块中，服务器设备将数据写入其寄存器。服务器每次写操作只能向一个寄存器写入数据。

Simulink® Support Package for Arduino® Hardware 支持通过 RS485 网络的 Modbus® 通信协议。RS485 网络上的每个设备都由唯一的 8-bit 地址或标识符引用。

此表对 Modbus 服务器设备引用的服务器寄存器进行分类。

| 寄存器类型 | 寄存器大小 |
| --- | --- |
| 线圈 | 1-bit |
| 离散输入 | 1-bit |
| 保持寄存器 | 16-bit |
| 输入寄存器 | 16-bit |
