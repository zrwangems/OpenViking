---
type: simulink-block
title: 'Modbus TCP/IP Client Write'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Network'
documentation_page: 'modbustcpipclientwrite'
documentation_source_path: 'nvidia/ref/modbustcpipclientwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Modbus TCP/IP Client Write

## 端口

### 输入

### **Data** — 输入数据向量

模块的输入是客户端写入服务器寄存器的数据。将输入数据指定为 *N*×1 向量，其中 *N* 表示服务器设备上的寄存器数量。

- 如果选择 Coil 或 Discrete Input 写操作，客户端将数据作为 Boolean 数据的 1 位写操作写入服务器寄存器。
- 如果选择 Holding Register 或 Input Register 写操作，客户端将数据作为 `uint16` 数据的 16 位写操作写入服务器寄存器。

**数据类型：** `Boolean` | `uint16`

## 参数

### **服务器地址** — 服务器设备的唯一 IP 地址 `127.0.0.1`（默认）| IP 地址

输入服务器设备的 IP 地址，以标识客户端要向其写入数据的服务器。

#### 编程用法

|  |
| --- |
| **模块参数：** `serverIP` |
| **类型：** 字符向量 |
| **取值：** `'127.0.0.1'` | `Valid IP address` |
| **默认值：**  `'127.0.0.1'` |

### **功能** — 写入操作的类型 `Write Coil`（默认）| `Write Holding Register` | `Write Multiple Coils` | `Write Multiple Holding Registers`

选择要在服务器寄存器上执行的写入操作类型。指定以下之一：

| 取值 | 描述 |
| --- | --- |
| `Write Coil` | 将数据写入 **线圈地址** 参数中指定的线圈寄存器地址。 |
| `Write Holding Register` | 将数据写入 **保持寄存器地址** 参数中指定的保持寄存器地址。 |
| `Write Multiple Coils` | 根据 **线圈地址** 和 **线圈数量** 参数中指定的值，将数据写入多个线圈寄存器。 |
| `Write Multiple Holding Registers` | 根据 **保持寄存器地址** 和 **保持寄存器数量** 参数中指定的值，将数据写入多个保持寄存器。 |

#### 编程用法

|  |
| --- |
| **模块参数：** `Function` |
| **类型：** 字符向量 |
| **取值：** `'Write Coil'` | `'Write Holding Register'` | `'Write Multiple Coils'` | `'Write Multiple Holding Registers'` |
| **默认值：**  `'Write Coil'` |

### **线圈地址** — 线圈寄存器的地址 `0`（默认）| 标量

- 要通知客户端将数据写入特定的线圈寄存器，请在此参数中指定线圈寄存器地址。例如，要让客户端将数据写入地址为 `10` 的线圈寄存器，请输入 `10`。
- 要通知客户端将数据写入一组线圈寄存器，请指定该组中第一个线圈寄存器的地址。例如，要让客户端将数据写入地址范围为 `10` 到 `14` 的线圈寄存器，请输入 `10`。

#### 依赖关系

要启用此参数，请将 **功能** 设置为 `Write Coil` 或 `Write Multiple Coils`。

#### 编程用法

|  |
| --- |
| **模块参数：** `CoilAddress` |
| **类型：** 字符向量 |
| **取值：** `'0'` | 标量 |
| **默认值：**  `'0'` |

### **线圈数量** — 客户端要写入的线圈寄存器数量 `1`（默认）| 标量

输入希望客户端将数据写入的线圈寄存器数量。例如，要让客户端将数据写入地址范围为 `10` 到 `14` 的线圈寄存器，请输入 `5`。

#### 依赖关系

要启用此参数，请将 **功能** 设置为 `Write Multiple Coils`。

#### 编程用法

|  |
| --- |
| **模块参数：** `numElements_coil` |
| **类型：** 字符向量 |
| **取值：** `'1'` | 标量 |
| **默认值：**  `'1'` |

### **保持寄存器地址** — 保持寄存器的地址 `0`（默认）| 标量

- 要通知客户端将数据写入特定的保持寄存器，请在此参数中指定保持寄存器地址。例如，要让客户端将数据写入地址为 `37` 的保持寄存器，请输入 `37`。
- 要通知客户端将数据写入一组保持寄存器，请指定该组中第一个保持寄存器的地址。例如，要让客户端将数据写入地址范围为 `37` 到 `44` 的保持寄存器，请输入 `37`。

#### 依赖关系

要启用此参数，请将 **功能** 设置为 `Write Holding Register`。

#### 编程用法

|  |
| --- |
| **模块参数：** `HoldingRegisterAddress` |
| **类型：** 字符向量 |
| **取值：** `'0'` | 标量 |
| **默认值：**  `'0'` |

### **保持寄存器数量** — 客户端要写入的保持寄存器数量 `1`（默认）| 标量

输入希望客户端将数据写入的保持寄存器数量。例如，要让客户端将数据写入地址范围为 `37` 到 `44` 的保持寄存器，请输入 `8`。

#### 依赖关系

要启用此参数，请将 **功能** 设置为 `Write Multiple Holding Registers`。

#### 编程用法

|  |
| --- |
| **模块参数：** `numElements_holdingReg` |
| **类型：** 字符向量 |
| **取值：** `'1'` | 标量 |
| **默认值：**  `'1'` |

## 所属库

NVIDIA Jetson and NVIDIA DRIVE / Network

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2022a 中引入**

## 描述

客户端设备通过 TCP/IP 网络将数据写入服务器设备的寄存器。

在 Modbus TCP/IP Client Write 模块中，客户端设备将数据写入服务器设备的寄存器。

MATLAB® Coder™ Support Package for NVIDIA® Jetson™ and NVIDIA DRIVE® Platforms 支持在 Jetson 平台上通过 TCP/IP 网络使用 Modbus® 通信协议。客户端和服务器必须连接到 TCP/IP 网络，才能成功进行 Modbus 通信。

**注意**

NVIDIA DRIVE 平台不支持 Modbus TCP/IP Client Write 模块。

客户端可以根据服务器寄存器类型，对服务器寄存器执行读取、写入或读取和写入操作。

| 寄存器类型 | 寄存器大小 | 客户端执行的操作 |
| --- | --- | --- |
| 线圈 | 1-bit | 读取和写入 |
| 离散输入 | 1-bit | 读取 |
| 保持寄存器 | 16-bit | 读取和写入 |
| 输入寄存器 | 16-bit | 读取 |

客户端可以根据寄存器类型，对服务器设备的寄存器执行读取或写入操作。
