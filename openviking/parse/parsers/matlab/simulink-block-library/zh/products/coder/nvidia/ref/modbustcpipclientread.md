---
type: simulink-block
title: 'Modbus TCP/IP Client Read'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Network'
documentation_page: 'modbustcpipclientread'
documentation_source_path: 'nvidia/ref/modbustcpipclientread.html'
language: zh-CN
chinese_source: worker-translation
---

# Modbus TCP/IP Client Read

## 端口

### 输出

### **Data** — 输出数据向量

该模块将客户端从服务器设备寄存器读取的数据输出为 *N*×1 向量，其中 *N* 表示服务器设备上的寄存器数量。

- 如果选择 Coil 或 Discrete Input 读取操作，客户端将服务器寄存器作为 1-bit 读取操作读取。该模块将读取的数据输出为 Boolean 数据。
- 如果选择 Holding Register 或 Input Register 读取操作，客户端将服务器寄存器作为 16-bit 读取操作读取。该模块将读取的数据输出为 `uint16` 数据。

**数据类型：** `Boolean` | `uint16`

### **Status** — 读取操作的状态 `0` | `1`

该模块输出客户端对服务器设备寄存器执行读取操作的状态。

- `0`：表示读取操作未成功，这意味着在 **data** 端口上接收到的数据无效。
- `1`：表示读取操作成功，这意味着在 **data** 端口上接收到的数据有效。

**数据类型：** `uint8`

## 参数

### **Server address** — 服务器设备的唯一 IP 地址 `127.0.0.1`（默认） | IP address

输入服务器设备的 IP 地址。客户端从此服务器设备读取数据。

#### 编程用法

|  |
| --- |
| **模块参数：** `serverIP` |
| **类型：** character vector |
| **值：** `'127.0.0.1'` | `Valid IP address` |
| **默认值：**  `'127.0.0.1'` |

### **Function** — 客户端读取操作的类型 `Read Coil`（默认） | `Read Discrete Input` | `Read Holding Register` | `Read Input Register` | `Read Multiple Coils` | `Read Multiple Discrete Inputs` | `Read Multiple Holding Registers` | `Read Multiple Input Registers`

选择要在服务器寄存器上执行的读取操作类型。指定以下之一：

| 值 | 描述 |
| --- | --- |
| `Read Coil` | 从 **Coil Address** 参数中指定的线圈寄存器地址读取数据。 |
| `Read Discrete Input` | 从 **Discrete Input Address** 参数中指定的离散输入寄存器地址读取数据。 |
| `Read Holding Register` | 从 **Holding Register Address** 参数中指定的保持寄存器地址读取数据。 |
| `Read Input Register` | 从 **Input Register Address** 参数中指定的输入寄存器地址读取数据。 |
| `Read Multiple Coils` | 根据 **Coil Address** 和 **Number of Coils** 参数中指定的值，从多个线圈寄存器读取数据。 |
| `Read Multiple Discrete Inputs` | 根据 **Discrete Input Address** 和 **Number of Discrete Inputs** 参数中指定的值，从多个离散输入寄存器读取数据。 |
| `Read Multiple Holding Registers` | 根据 **Holding Register Address** 和 **Number of Holding registers** 参数中指定的值，从多个保持寄存器读取数据。 |
| `Read Multiple Input Registers` | 根据 **Input Register Address** 和 **Number of Input registers** 参数中指定的值，从多个输入寄存器读取数据。 |

#### 编程用法

|  |
| --- |
| **模块参数：** `Function` |
| **类型：** character vector |
| **值：** `'Read Coil'` | `'Read Discrete Input'` | `'Read Holding Register'` | `'Read Input Register'` | `'Read Multiple Coils'` | `'Read Multiple Discrete Inputs'` | `'Read Multiple Holding Registers'` | `'Read Multiple Input Registers'` |
| **默认值：**  `'Read Coil'` |

### **Coil address** — 线圈寄存器地址 `0`（默认） | scalar

要通知客户端从特定线圈寄存器读取数据，请在此参数中指定线圈寄存器地址。例如，要让客户端从地址为 `10` 的线圈寄存器读取数据，请输入 `10`。

要通知客户端从一组线圈寄存器读取数据，请指定该组中第一个线圈寄存器的地址。例如，要让客户端从地址范围为 `10` 到 `14` 的线圈寄存器读取数据，请输入 `10`。

#### 依赖项

要启用此参数，请将 **Function** 设置为 `Read Coil` 或 `Read Multiple Coils`。

#### 编程用法

|  |
| --- |
| **模块参数：** `CoilAddress` |
| **类型：** character vector |
| **值：** `'0'` | scalar |
| **默认值：**  `'0'` |

### **Number of coils** — 客户端要读取的线圈寄存器数量 `1`（默认） | scalar

输入希望客户端读取数据的线圈寄存器数量。例如，要让客户端从地址范围为 `10` 到 `14` 的线圈寄存器读取数据，请输入 `5`。

#### 依赖项

要启用此参数，请将 **Function** 设置为 `Read Multiple Coils`。

#### 编程用法

|  |
| --- |
| **模块参数：** `numElements_coil` |
| **类型：** character vector |
| **值：** `'1'` | scalar |
| **默认值：**  `'1'` |

### **Discrete Input Address** — 离散输入寄存器地址 `0`（默认） | scalar

要通知客户端从特定离散输入寄存器读取数据，请在此参数中指定离散输入寄存器地址。例如，要让客户端从地址为 `80` 的离散输入寄存器读取数据，请输入 `80`。

要通知客户端从一组离散输入寄存器读取数据，请指定该组中第一个离散输入寄存器的地址。例如，要让客户端从地址范围为 `80` 到 `89` 的离散输入寄存器读取数据，请输入 `80`。

#### 依赖项

要启用此参数，请将 **Function** 设置为 `Read Discrete Input` 或 `Read Multiple Discrete Inputs`。

#### 编程用法

|  |
| --- |
| **模块参数：** `DiscreteInputAddress` |
| **类型：** character vector |
| **值：** `'0'` | scalar |
| **默认值：**  `'0'` |

### **Number of Discrete Inputs** — 客户端要读取的离散输入寄存器数量 `1`（默认） | scalar

输入希望客户端读取数据的离散输入寄存器数量。例如，要让客户端从地址范围为 `80` 到 `89` 的离散输入寄存器读取数据，请输入 `10`。

#### 依赖项

要启用此参数，请将 **Function** 设置为 `Read Multiple Discrete Inputs`。

#### 编程用法

|  |
| --- |
| **模块参数：** `numElements_input` |
| **类型：** character vector |
| **值：** `'1'` | scalar |
| **默认值：**  `'1'` |

### **Holding Register Address** — 保持寄存器地址 `0`（默认） | scalar

要通知客户端从特定保持寄存器读取数据，请在此参数中指定保持寄存器地址。例如，要让客户端从地址为 `37` 的保持寄存器读取数据，请输入 `37`。

要通知客户端从一组保持寄存器读取数据，请指定该组中第一个保持寄存器的地址。例如，要让客户端从地址范围为 `37` 到 `44` 的保持寄存器读取数据，请输入 `37`。

#### 依赖项

要启用此参数，请将 **Function** 设置为 `Read Holding Register` 或 `Read Multiple Holding Registers`。

#### 编程用法

|  |
| --- |
| **模块参数：** `HoldingRegisterAddress` |
| **类型：** character vector |
| **值：** `'0'` | scalar |
| **默认值：**  `'0'` |

### **Number of Holding registers** — 客户端要读取的保持寄存器数量 `1`（默认） | scalar

输入希望客户端读取数据的保持寄存器数量。例如，要让客户端从地址范围为 `37` 到 `44` 的保持寄存器读取数据，请输入 `8`。

#### 依赖项

要启用此参数，请将 **Function** 设置为 `Read Multiple Holding Registers`。

#### 编程用法

|  |
| --- |
| **模块参数：** `numElements_holdingReg` |
| **类型：** character vector |
| **值：** `'1'` | scalar |
| **默认值：**  `'1'` |

### **Input Register Address** — 输入寄存器地址 `0`（默认） | scalar

- 要通知客户端从特定输入寄存器读取数据，请在此参数中指定输入寄存器地址。例如，要让客户端从地址为 `25` 的输入寄存器读取数据，请输入 `25`。
- 要通知客户端从一组输入寄存器读取数据，请指定该组中第一个输入寄存器的地址。例如，要让客户端从地址范围为 `25` 到 `26` 的输入寄存器读取数据，请输入 `25`。

#### 依赖项

要启用此参数，请将 **Function** 设置为 `Read Input Register` 或 `Read Multiple Input Registers`。

#### 编程用法

|  |
| --- |
| **模块参数：** `InputRegisterAddress` |
| **类型：** character vector |
| **值：** `'0'` | scalar |
| **默认值：**  `'0'` |

### **Number of Input registers** — 客户端要读取的输入寄存器数量 `1`（默认） | scalar

输入希望客户端读取数据的输入寄存器数量。例如，要让客户端从地址范围为 `25` 到 `26` 的输入寄存器读取数据，请输入 `2`。

#### 依赖项

要启用此参数，请将 **Function** 设置为 `Read Multiple Input Registers`。

#### 编程用法

|  |
| --- |
| **模块参数：** `numElements_inputReg` |
| **类型：** character vector |
| **值：** `'1'` | scalar |
| **默认值：**  `'1'` |

### **Sample Time** — 客户端读取数据的时间间隔 `0.1`（默认） | scalar

输入客户端从服务器设备寄存器读取数据的时间间隔（以 seconds 为单位）。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |
| **类型：** character vector |
| **值：** scalar | vector |
| **默认值：** `'0.1'` |

## 所属库

NVIDIA Jetson and NVIDIA DRIVE / Network

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2022a 中引入**

## 描述

客户端设备通过 TCP/IP 网络从服务器设备寄存器读取数据

在 Modbus TCP/IP Client Read 模块中，客户端设备从服务器设备的寄存器读取数据。

MATLAB® Coder™ Support Package for NVIDIA® Jetson™ and NVIDIA DRIVE® Platforms 支持 Jetson 平台上的基于 TCP/IP 网络的 Modbus® 通信协议。客户端和服务器必须连接到 TCP/IP 网络，才能成功进行 Modbus 通信。

**注意**

NVIDIA DRIVE 平台上不支持 Modbus TCP/IP Client Read 模块。

根据服务器寄存器类型，客户端可对服务器寄存器执行读取、写入或读取和写入操作。

| 寄存器类型 | 寄存器大小 | 客户端执行的操作 |
| --- | --- | --- |
| Coil | 1-bit | 读取和写入 |
| Discrete Input | 1-bit | 读取 |
| Holding Register | 16-bit | 读取和写入 |
| Input Register | 16-bit | 读取 |
