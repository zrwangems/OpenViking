---
type: simulink-block
title: 'Serial Configuration'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Architecture and Component Design / Blocks for Embedded Targets'
documentation_page: 'serialconfiguration'
documentation_source_path: 'ref/serialconfiguration.html'
language: zh-CN
chinese_source: worker-translation
---

# Serial Configuration

## 端口

R2025b 中未记录。

## 参数

### **Port** — 串行通信端口 可用的通信端口

您要配置的计算机上的串行端口。使用此配置的端口通过 Serial Send 和 Serial Receive 模块发送和接收数据。如果您尚未配置端口，则在运行模型时该模块会返回错误。

**注意**

每个 Serial Send 和 Serial Receive 模块都必须有一个已配置的 Serial Configuration 模块。如果您在仿真中使用多个串行端口，则必须使用单独的 Serial Configuration 模块配置每个端口。

#### 编程用法

|  |
| --- |
| **模块参数：** `Port` |
| **类型：** character vector, string |

### **Baud rate** — 通信速度 9600（默认） | 正整数

串行接口传输比特的速率，单位为 bits per second。

#### 编程用法

|  |
| --- |
| **模块参数：** `BaudRate` |
| **类型：** character vector, string |
| **值：** 正整数 |
| **默认值：** `'9600'` |

### **Data bits** — 表示一个数据字符的位数 `8`（默认） | `5` | `6` | `7`

通过串行接口传输的数据位数。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataBits` |
| **类型：** character vector, string |
| **值：** `'5'` | `'6'` | `'7'` | `'8'` |
| **默认值：** `'8'` |

### **Parity** — 奇偶校验位类型 `none`（默认） | `even` | `odd`

添加到串行端口所传输数据的奇偶校验位类型。您可以使用此参数向数据添加奇偶校验位（也称为校验位）。向二进制代码串添加奇偶校验位是一种通过确保 1 比特的总数为偶数或奇数来检测数据传输错误的方法。

奇偶校验位的值由给定比特集中 1 的数量决定，并按如下方式设置。

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

### **Stop bits** — 指示字符结束的位模式 `1`（默认） | 正标量

用于指示字节结束的位数。此参数取决于您为 **Data bits** 参数选择的值。如果选择数据位 `6`、`7` 或 `8`，则默认值为 `1`，另一个可用选项为 `2`。如果选择数据位 `5`，则默认值为 `1`，另一个可用选项为 `1.5`。

#### 编程用法

|  |
| --- |
| **模块参数：** `StopBits` |
| **类型：** character vector, string |
| **值：** 正标量 |
| **默认值：** `'1'` |

### **Byte order** — 字节的顺序 `little-endian`（默认） | `big-endian`

将字节排列为更大数值时所采用的前后顺序。如果字节顺序为 `little-endian`，则仪器将第一个字节存储到第一个内存地址。如果字节顺序为 `big-endian`，则仪器将最后一个字节存储到第一个内存地址。

在执行读取或写入操作之前，请将字节顺序配置为适合您仪器的值。有关仪器存储字节顺序的信息，请参阅仪器文档。

#### 编程用法

|  |
| --- |
| **模块参数：** `ByteOrder` |
| **类型：** character vector, string |
| **值：** `'little-endian'` | `'big-endian'` |
| **默认值：** `'little-endian'` |

### **Flow control** — 管理数据传输速率的模式 `none`（默认） | `hardware`

管理串行端口上数据传输速率的过程。选择 `none` 表示无流控制，或选择 `hardware` 让硬件确定流控制。

#### 编程用法

|  |
| --- |
| **模块参数：** `FlowControl` |
| **类型：** character vector, string |
| **值：** `'none'` | `'hardware'` |
| **默认值：** `none` |

### **Timeout** — 完成操作所允许的时间 10（默认） | 正标量

模型在每个仿真时间步期间等待数据的时间量。

#### 编程用法

|  |
| --- |
| **模块参数：** `Timeout` |
| **类型：** character vector, string |
| **值：** 正标量 |
| **默认值：** `'10'` |

## 所属库

Instrument Control Toolbox Motor Control Blockset / Protection and Diagnostics

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块仅针对宿主机的平台（Windows®、macOS、Linux®）生成平台特定的代码。

## 版本历史

**在 R2008a 中引入**

### R2021a：**Parity** 参数在 Serial Configuration 模块中不再支持 `mark` 或 `space`

**Parity** 参数的 `mark` 和 `space` 选项在 Serial Configuration 模块中不再受支持。**Parity** 的有效值为 `none`（默认）、`even` 和 `odd`。

如果您尝试打开一个已将 **Parity** 值设置为 `mark` 或 `space` 的现有模型，MATLAB® 会返回警告，并将该参数更改为默认值 `none`。

## 描述

配置串行端口参数

Serial Configuration 模块为可用于发送和接收数据的串行端口配置参数。在设置 Serial Receive 和 Serial Send 模块之前，请使用此模块设置串行端口的参数。

**注意**

在指定 Serial Receive 和 Serial Send 模块参数之前，必须使用 Serial Configuration 模块配置串行端口参数。

### 其他支持的功能

- Serial Configuration 模块支持使用 Simulink® Accelerator 模式，但不支持 Rapid Accelerator。
  此功能可加快 Simulink 模型的执行速度。
- Serial Configuration 模块支持使用模型引用。
  此功能允许您的模型将其他 Simulink 模型作为模块化组件包含在内。
- Serial Configuration 模块支持 C/C++ 代码生成。
  此功能允许您使用 Simulink Coder™ 生成 C 和 C++ 代码。

有关这些功能的详细信息，请参阅 Simulink 文档。
