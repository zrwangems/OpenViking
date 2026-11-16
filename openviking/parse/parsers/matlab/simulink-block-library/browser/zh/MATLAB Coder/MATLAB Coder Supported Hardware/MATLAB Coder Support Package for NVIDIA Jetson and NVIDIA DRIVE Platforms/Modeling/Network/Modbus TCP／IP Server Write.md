---
type: simulink-block
title: 'Modbus TCP/IP Server Write'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Network'
documentation_page: 'modbustcpipserverwrite'
documentation_source_path: 'nvidia/ref/modbustcpipserverwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Modbus TCP/IP Server Write

## 端口

### Input

### **Input** — 输入数据标量

模块的输入是服务器作为 1 位标量写入其寄存器的数据。

- 如果选择 Coil 或 Discrete Input 写操作，服务器将数据作为 Boolean 数据以 1 位写操作写入其寄存器。
- 如果选择 Holding Register 或 Input Register 写操作，服务器将数据作为 `uint16` 数据以 16 位写操作写入其寄存器。

**数据类型：** `Boolean` | `uint16`

## 参数

### **Function** — 写操作类型 `Write Coil`（默认）| `Write Discrete Input` | `Write Holding register` | `Write Input register`

选择要在服务器寄存器上执行的写操作类型。指定以下之一：

| 值 | 描述 |
| --- | --- |
| `Write Coil` | 将数据写入 **Coil Address** 参数中指定的 coil 寄存器地址。 |
| `Write Discrete Input` | 将数据写入 **Discrete Input Address** 参数中指定的 discrete input 寄存器地址。 |
| `Write Holding Register` | 将数据写入 **Holding Register Address** 参数中指定的 holding register 地址。 |
| `Write Input Register` | 将数据写入 **Input Register Address** 参数中指定的 input register 地址。 |

#### 编程用法

|  |
| --- |
| **模块参数：** `Function` |
| **类型：** character vector |
| **值：** `'Write Coil'` | `'Write Discrete Input'` | `'Write Holding Register'` | `'Write Input Register'` |
| **默认值：**  `'Write Coil'` |

### **Coil Address** — coil 寄存器地址 `0`（默认）| scalar

要通知服务器将数据写入特定 coil 寄存器，请在此参数中指定 coil 寄存器地址。例如，要让服务器将数据写入地址为 `10` 的 coil 寄存器，请输入 `10`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Write Coil`。

#### 编程用法

|  |
| --- |
| **模块参数：** `CoilAddress` |
| **类型：** character vector |
| **值：** `'0'` | scalar |
| **默认值：**  `'0'` |

### **Discrete Input Address** — discrete input 寄存器地址 `0`（默认）| scalar

要通知服务器将数据写入特定 discrete input 寄存器，请在此参数中指定 discrete input 寄存器地址。例如，要让服务器将数据写入地址为 `80` 的 discrete input 寄存器，请输入 `80`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Write Discrete Input`。

#### 编程用法

|  |
| --- |
| **模块参数：** `DiscreteInputAddress` |
| **类型：** character vector |
| **值：** `'0'` | scalar |
| **默认值：**  `'0'` |

### **Holding Register Address** — holding register 地址 `0`（默认）| scalar

要通知服务器将数据写入特定 holding register，请在此参数中指定 holding register 地址。例如，要让服务器将数据写入地址为 `37` 的 holding register，请输入 `37`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Write Holding register`。

#### 编程用法

|  |
| --- |
| **模块参数：** `HoldingRegisterAddress` |
| **类型：** character vector |
| **值：** `'0'` | scalar |
| **默认值：**  `'0'` |

### **Input Register Address** — input register 地址 `0`（默认）| scalar

要通知服务器将数据写入特定 input register，请在此参数中指定 input register 地址。例如，要让服务器将数据写入地址为 `25` 的 input register，请输入 `25`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Write Input register`。

#### 编程用法

|  |
| --- |
| **模块参数：** `InputRegisterAddress` |
| **类型：** character vector |
| **值：** `'0'` | scalar |
| **默认值：**  `'0'` |

## 所属库

NVIDIA Jetson and NVIDIA DRIVE / Network

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022a 中引入**

## 描述

服务器设备通过 TCP/IP 网络将数据写入服务器设备寄存器

在 Modbus TCP/IP Server Write 模块中，服务器设备将数据写入其寄存器。服务器每次读操作只能写入一个寄存器。

MATLAB® Coder™ Support Package for NVIDIA® Jetson™ and NVIDIA DRIVE® Platforms 支持在 Jetson 平台上通过 TCP/IP 网络的 Modbus® 通信协议。

**注意**

Modbus TCP/IP Server Write 模块在 NVIDIA DRIVE 平台上不受支持。

服务器可对这些服务器寄存器执行读和写操作。

| Register Type | Register Size |
| --- | --- |
| Coil | 1-bit |
| Discrete Input | 1-bit |
| Holding Register | 16-bit |
| Input Register | 16-bit |
