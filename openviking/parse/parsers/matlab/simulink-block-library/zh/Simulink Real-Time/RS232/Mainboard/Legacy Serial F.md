---
type: simulink-block
title: 'Legacy Serial Port F'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'RS232 / Mainboard'
documentation_page: 'legacyserialportf'
documentation_source_path: 'io_ref/legacyserialportf.html'
language: zh-CN
chinese_source: worker-translation
---

# Legacy Serial Port F

## 端口
```yaml
ports:
- name: XMT
  summary: 要发送的数据向量 vector
  direction: input
  data_types: int8 | int16 | int32 | uint8 | uint16 | uint32
- name: FIFO
  summary: 通过串口接收的数据的 FIFO serialfifoptr
  direction: output
```

### 输入

### **XMT** — 要发送的数据向量 vector

用于通过端口发送的数据向量。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **FIFO** — 通过串口接收的数据的 FIFO serialfifoptr

包含从串口接收到的数据的先进先出（FIFO）缓冲区。
## 参数
```yaml
parameters:
- name: Serial port
  summary: 正在访问的端口 Legacy Serial Port 1（默认）| .. | Legacy Serial Port 8 | USB Serial Port 1 | .. | USB Serial Port 8
  group: ''
  block_parameter: port
- name: Baud rate
  summary: 数据传输的波特率 115200（默认）| 57600 | 38400 | 19200 | 9600 | 4800 | 2400 | 1200 | 600 | 300 | 110
  group: ''
  block_parameter: baud
- name: Data bits
  summary: 每个字符的位数 8（默认）| 7 | 6 | 5
  group: ''
  block_parameter: width
- name: Stop bits
  summary: 端口的停止位数 1（默认）| 2
  group: ''
  block_parameter: nstop
- name: Parity
  summary: 用于检查数据传输的奇偶校验 None（默认）| Even | Odd | Mark | Space
  group: ''
  block_parameter: parity
- name: Enable auto RTS/CTS
  summary: 启用 RTS/CTS 握手 off（默认）| on
  group: ''
  block_parameter: ctsmode
- name: Port to modify
  summary: 正在访问的端口 1（默认）| 2
  group: ''
  block_parameter: port
- name: Receive FIFO size
  summary: FIFO 大小（以字节为单位） 1024（默认）
  group: ''
  block_parameter: fifosize
- name: Transmit data type
  summary: 发送器的数据类型 count+32 bit int（默认）| count+32 bit uint | count+16 bit int | count+16 bit uint | 8 bit int null terminated
    | 8 bit uint null terminated
  group: ''
  block_parameter: idtype
- name: Sample Time
  summary: 采样时间 -1（默认）| 数值
  group: ''
  block_parameter: sampletime
```

### **Serial port** — 正在访问的端口 `Legacy Serial Port 1`（默认）| .. | `Legacy Serial Port 8` | `USB Serial Port 1` | .. | `USB Serial Port 8`

指定用于通信的串口。

如果使用 USB 转串口适配器，目标计算机会按照适配器连接到串行设备的顺序将这些适配器检测为 `serusb1`、`serusb2` 等。

如果端口连接没有变化，端口分配的顺序在目标计算机或串行设备的电源循环期间保持不变。

#### 程序化使用

|  |
| --- |
| **模块参数：** `port` |

### **Baud rate** — 数据传输的波特率 `115200`（默认）| `57600` | `38400` | `19200` | `9600` | `4800` | `2400` | `1200` | `600` | `300` | `110`

选择通过调制解调器发送和接收数据的波特率。

#### 程序化使用

|  |
| --- |
| **模块参数：** `baud` |

### **Data bits** — 每个字符的位数 `8`（默认）| `7` | `6` | `5`

选择编码一个字符的位数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `width` |

### **Stop bits** — 端口的停止位数 `1`（默认）| `2`

选择字符流的停止位数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `nstop` |

### **Parity** — 用于检查数据传输的奇偶校验 `None`（默认）| `Even` | `Odd` | `Mark` | `Space`

选择用于检查数据完整性的奇偶校验方式。

#### 程序化使用

|  |
| --- |
| **模块参数：** `parity` |

### **Enable auto RTS/CTS** — 启用 RTS/CTS 握手 `off`（默认）| `on`

要启用通用异步收发器（UART）的请求发送/清除发送（RTS/CTS）握手以进行流控制，请选中此复选框。串行控制器使用 RTS/CTS 握手来防止由于发送目标设备上的硬件 FIFO 溢出而导致的数据丢失。

通常，中断服务程序的执行速度足以清空 FIFO。如果您的模型出现 FIFO 溢出，请选中此复选框。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ctsmode` |

### **Port to modify** — 正在访问的端口 `1`（默认）| `2`

此参数指定您要查看或修改参数的端口。在 Simulink® 模块上，上方端口为端口 `1`，下方端口为端口 `2`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `port` |

### **Receive FIFO size** — FIFO 大小（以字节为单位） `1024`（默认）

此参数指定接收 FIFO 的大小（以字节为单位）。

**示例：** `1024`

#### 程序化使用

|  |
| --- |
| **模块参数：** `fifosize` |

**数据类型：** `int32`

### **Transmit data type** — 发送器的数据类型 `count+32 bit int`（默认）| `count+32 bit uint` | `count+16 bit int` | `count+16 bit uint` | `8 bit int null terminated` | `8 bit uint null terminated`

此参数指定发送器的数据类型。8 位数据类型要求输入向量为以 NULL 结尾的字符向量。

16 位和 32 位数据类型保留第一个完整元素来包含输入向量其余部分中预期元素的数量。每个数据元素仅发送低字节。设置此数据类型可以使用更宽的数据类型来容纳字节。

如果数据流需要 NULL 字节，请选择 16 位或 32 位数据类型之一。由于 8 位数据类型是以 NULL 结尾的字符向量，NULL 字节会终止字符向量。

#### 程序化使用

|  |
| --- |
| **模块参数：** `idtype` |

### **Sample Time** — 采样时间 `-1`（默认）| 数值

输入基本采样时间或基本采样时间的倍数。
`-1` 表示采样时间继承。

#### 程序化使用

|  |
| --- |
| **模块参数：** `sampletime` |
## 所属库

Simulink Real-Time / RS232 / Mainboard

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2008a 中引入**

### R2021b：RS232 模块的 USB 转串口

RS232 主板模块支持连接 USB 串口适配器端口。Legacy Serial
Read 模块、Legacy Serial Write 模块、Legacy
Serial Setup 模块、Legacy Serial Port 模块和
Legacy Serial Port F 模块的 `Serial port` 参数意味着您可以选择
`USB Serial Port` 或 `Legacy Serial
Port`。

## 描述

通过主板基板串口使用 FIFO 发送和接收数据

Send/Receive FIFO 模块设置串行接口以发送和
接收字符流和二进制流。它像
Send/Receive 模块一样发送输入数据，但它通过先进先出（FIFO）输出传播接收到的数据。

包含 Send/Receive FIFO 模块和 FIFO
Read 模块的模型提供与 Send/Receive
模块相同的功能。包含 Send/Receive FIFO 模块和 FIFO
Read HDRS 或 FIFO Read Binary 模块的模型提供比
Send/Receive 模块更强大的功能。

有关详细信息，请参阅 RS-232 Serial Communication 和
RS-232 Legacy Drivers。
