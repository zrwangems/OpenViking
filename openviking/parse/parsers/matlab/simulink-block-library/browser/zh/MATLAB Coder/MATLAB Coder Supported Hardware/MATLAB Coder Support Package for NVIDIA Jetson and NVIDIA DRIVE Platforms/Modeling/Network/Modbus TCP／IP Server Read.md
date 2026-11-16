---
type: simulink-block
title: 'Modbus TCP/IP Server Read'
family: 'coder'
product_id: 'coder'
product_name: 'MATLAB Coder'
documentation_release: R2025b
official_category: 'MATLAB Coder Supported Hardware / MATLAB Coder Support Package for NVIDIA Jetson and NVIDIA DRIVE Platforms / Modeling / Network'
documentation_page: 'modbustcpipserverread'
documentation_source_path: 'nvidia/ref/modbustcpipserverread.html'
language: zh-CN
chinese_source: worker-translation
---

# Modbus TCP/IP Server Read

## 端口

### 输出

### **Data** — 输出数据标量

模块将服务器设备从其寄存器读取的数据作为 1-bit 标量输出。

- 如果选择 Coil 或 Discrete Input 读取操作，服务器会将其
  寄存器作为 1-bit 读取操作进行读取。模块将读取的数据作为 Boolean
  数据输出。
- 如果选择 Holding Register 或 Input Register 读取操作，服务器会将其
  寄存器作为 16-bit 读取操作进行读取。模块将读取的数据作为 `uint16` 数据输出。

**数据类型：** `Boolean` | `uint16`

### **Status** — 读取操作的状态 `0` | `1`

模块输出服务器对服务器寄存器执行读取操作的状态。

- `0`：表示读取操作不成功，这意味着
  **data** 端口上接收到的数据无效。
- `1`：表示读取操作成功，这意味着
  **data** 端口上接收到的数据有效。

**数据类型：** `uint8`

## 参数

### **Function** — 读取操作的类型 `Read Coil`（默认）| `Read Discrete Input` | `Read Holding Register` | `Read Input Register`

选择要在服务器寄存器上执行的读取操作类型。指定以下项之一：

| 值 | 描述 |
| --- | --- |
| `Read Coil` | 从 **Coil Address** 参数中指定的 coil 寄存器地址读取数据。 |
| `Read Discrete Input` | 从 **Discrete Input Address** 参数中指定的 discrete input 寄存器地址读取数据。 |
| `Read Holding Register` | 从 **Holding Register Address** 参数中指定的 holding register 地址读取数据。 |
| `Read Input Register` | 从 **Input Register Address** 参数中指定的 input register 地址读取数据。 |

#### 编程使用

|  |
| --- |
| **模块参数：** `Function` |
| **类型：** character vector |
| **值：** `'Read Coil'` | `'Read Discrete Input'` | `'Read Holding Register'` | `'Read Input Register'` |
| **默认值：**  `'Read Coil'` |

### **Coil Address** — coil 寄存器地址 `0`（默认）| scalar

要通知服务器从特定 coil 寄存器读取数据，请在此参数中指定 coil 寄存器地址。例如，要让服务器从地址为 `10` 的 coil 寄存器读取数据，请输入 `10`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Read Coil`。

#### 编程使用

|  |
| --- |
| **模块参数：** `CoilAddress` |
| **类型：** character vector |
| **值：** `'0'` | scalar |
| **默认值：**  `'0'` |

### **Discrete Input Address** — discrete input 寄存器地址 `0`（默认）| scalar

要通知服务器从特定 discrete input 寄存器读取数据，请在此参数中指定 discrete input 寄存器地址。例如，要让服务器从地址为 `80` 的 discrete input 寄存器读取数据，请输入 `80`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Read Discrete Input`。

#### 编程使用

|  |
| --- |
| **模块参数：** `DiscreteInputAddress` |
| **类型：** character vector |
| **值：** `'0'` | scalar |
| **默认值：**  `'0'` |

### **Holding Register Address** — holding register 地址 `0`（默认）| scalar

要通知服务器从特定 holding register 读取数据，请在此参数中指定 holding register 地址。例如，要让服务器从地址为 `37` 的 holding register 读取数据，请输入 `37`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Read Holding Register`。

#### 编程使用

|  |
| --- |
| **模块参数：** `HoldingRegisterAddress` |
| **类型：** character vector |
| **值：** `'0'` | scalar |
| **默认值：**  `'0'` |

### **Input Register Address** — input register 地址 `0`（默认）| scalar

要通知服务器从特定 input register 读取数据，请在此参数中指定 input register 地址。例如，要让服务器从地址为 `25` 的 input register 读取数据，请输入 `25`。

#### 依赖关系

要启用此参数，请将 **Function** 设置为 `Read Input Register`。

#### 编程使用

|  |
| --- |
| **模块参数：** `InputRegisterAddress` |
| **类型：** character vector |
| **值：** `'0'` | scalar |
| **默认值：**  `'0'` |

### **Sample time** — 服务器读取数据的时间间隔 `0.1`（默认）| scalar

输入服务器从其寄存器读取数据的时间间隔（以 seconds 为单位）。

#### 编程使用

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

服务器设备通过 TCP/IP 网络从服务器设备寄存器读取数据

在 Modbus TCP/IP Server Read 模块中，服务器设备从其寄存器读取数据。服务器每次读取操作只能从一个寄存器读取数据。

MATLAB® Coder™ Support Package for NVIDIA® Jetson™ and NVIDIA DRIVE® Platforms 支持在 Jetson 平台上通过 TCP/IP 网络的 Modbus® 通信协议。

**注意**

NVIDIA DRIVE 平台不支持 Modbus TCP/IP Server Read 模块。

服务器可对这些服务器寄存器执行读取和写入操作。

| 寄存器类型 | 寄存器大小 |
| --- | --- |
| Coil | 1-bit |
| Discrete Input | 1-bit |
| Holding Register | 16-bit |
| Input Register | 16-bit |

服务器可对其寄存器执行读取或写入操作。
