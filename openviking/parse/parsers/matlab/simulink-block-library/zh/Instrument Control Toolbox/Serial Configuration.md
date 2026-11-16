---
type: simulink-block
title: 'Serial Configuration'
family: 'instrument'
product_id: 'instrument'
product_name: 'Instrument Control Toolbox'
documentation_release: R2025b
official_category: ''
documentation_page: 'serialconfiguration'
documentation_source_path: 'serialconfiguration.html'
language: zh-CN
chinese_source: worker-translation
---

# Serial Configuration

## 端口

在 R2025b 中未记录。

## 参数

### **Port** — 串行通信端口 可用通信端口

要配置的计算机上的串行端口。使用此配置的端口与 Serial Send 和 Serial Receive 模块发送和接收数据。如果尚未配置端口，则运行模型时该模块会返回错误。

**注意**

每个 Serial Send 和 Serial Receive 模块都必须有一个已配置的 Serial Configuration 模块。如果仿真中使用多个串行端口，则必须使用单独的 Serial Configuration 模块配置每个端口。

#### 编程用法

|  |
| --- |
| **模块参数：** `Port` |
| **类型：** character vector, string |

### **Baud rate** — 通信速度 9600（默认）| positive integer

串行接口传输 bits 的速率，以 bits per second 为单位。

#### 编程用法

|  |
| --- |
| **模块参数：** `BaudRate` |
| **类型：** character vector, string |
| **值：** positive integer |
| **默认值：** `'9600'` |

### **Data bits** — 表示一个数据字符的 bits 数 `8`（默认）| `5` | `6` | `7`

通过串行接口传输的 data bits 数。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataBits` |
| **类型：** character vector, string |
| **值：** `'5'` | `'6'` | `'7'` | `'8'` |
| **默认值：** `'8'` |

### **Parity** — 奇偶校验位类型 `none`（默认）| `even` | `odd`

添加到串行端口所传输数据的奇偶校验位类型。可以使用此参数向数据中添加奇偶校验位（也称为校验位）。向二进制代码字符串中添加奇偶校验位是一种通过确保 1-bits 的总数为偶数或奇数来检测数据传输错误的方法。

奇偶校验位的值由给定 bits 集合中 1 的数量确定，并按如下方式设置。

| 奇偶校验位类型 | 奇偶校验位值 | |
| --- | --- | --- |
| 如果 1 的数量为偶数 | 如果 1 的数量为奇数 |
| `none` | 未设置奇偶校验位 | 未设置奇偶校验位 |
| `even` | 0 | 1 |
| `odd` | 1 | 0 |

**注意**

从 R2021a 开始，**Parity** 参数不再支持 `mark` 或 `space`。有关详细信息，请参阅 Serial Configuration 模块中的 Parity 参数不再支持 mark 或 space。

#### 编程用法

|  |
| --- |
| **模块参数：** `Parity` |
| **类型：** character vector, string |
| **值：** `'none'` | `'even'` | `'odd'` |
| **默认值：** `'none'` |

### **Stop bits** — 指示字符结束的 bits 模式 `1`（默认）| positive scalar

用于指示一个 byte 结束的 bits 数。此参数取决于为 **Data bits** 参数选择的值。如果为 **Data bits** 选择 `6`、`7` 或 `8`，则默认值为 `1`，另一个可用选项为 `2`。如果选择 data bit `5`，则默认值为 `1`，另一个可用选项为 `1.5`。

#### 编程用法

|  |
| --- |
| **模块参数：** `StopBits` |
| **类型：** character vector, string |
| **值：** positive scalar |
| **默认值：** `'1'` |

### **Byte order** — bytes 的先后顺序 `little-endian`（默认）| `big-endian`

将 bytes 排列为更大数值时的先后顺序。如果 **Byte order** 为 `little-endian`，则仪器将第一个 byte 存储在第一个内存地址中。如果 **Byte order** 为 `big-endian`，则仪器将最后一个 byte 存储在第一个内存地址中。

在执行读或写操作之前，将 **Byte order** 配置为适合仪器的值。有关仪器存储 bytes 的顺序的信息，请参阅仪器文档。

#### 编程用法

|  |
| --- |
| **模块参数：** `ByteOrder` |
| **类型：** character vector, string |
| **值：** `'little-endian'` | `'big-endian'` |
| **默认值：** `'little-endian'` |

### **Flow control** — 管理数据传输速率的模式 `none`（默认）| `hardware`

管理串行端口上数据传输速率的过程。选择 `none` 表示无流控制，或选择 `hardware` 表示让硬件确定流控制。

#### 编程用法

|  |
| --- |
| **模块参数：** `FlowControl` |
| **类型：** character vector, string |
| **值：** `'none'` | `'hardware'` |
| **默认值：** `none` |

### **Timeout** — 完成操作所允许的时间 10（默认）| positive scalar

在每个仿真时间步中，模型等待数据的时间量。

#### 编程用法

|  |
| --- |
| **模块参数：** `Timeout` |
| **类型：** character vector, string |
| **值：** positive scalar |
| **默认值：** `'10'` |

## 所属库

Instrument Control Toolbox Motor Control Blockset / Protection and Diagnostics

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块仅为主机平台生成特定于平台的代码（Windows®、macOS、Linux®）。

## 版本历史

**在 R2008a 中引入**

### R2021a：**Parity** 参数在 Serial Configuration 模块中不再支持 `mark` 或 `space`

Serial Configuration 模块中不再支持 **Parity** 参数的 `mark` 和 `space` 选项。**Parity** 的有效值为 `none`（默认）、`even` 和 `odd`。

如果尝试打开一个已将 **Parity** 值设置为 `mark` 或 `space` 的现有模型，MATLAB® 会返回警告并将该参数更改为默认值 `none`。

## 描述

配置串行端口的参数

Serial Configuration 模块配置串行端口的参数，您可以使用该端口发送和接收数据。在设置 Serial Receive 和 Serial Send 模块之前，使用此模块设置串行端口的参数。

**注意**

在指定 Serial Receive 和 Serial Send 模块参数之前，必须使用 Serial Configuration 模块配置串行端口参数。

### 其他支持的功能

- Serial Configuration 模块支持使用 Simulink® Accelerator 模式，但不支持 Rapid Accelerator。此功能可加速 Simulink 模型的执行。
- Serial Configuration 模块支持使用模型引用。此功能允许您的模型将其他 Simulink 模型作为模块化组件包含在内。
- Serial Configuration 模块支持 C/C++ 代码生成。此功能允许您使用 Simulink Coder™ 生成 C 和 C++ 代码。

有关这些功能的详细信息，请参阅 Simulink 文档。
