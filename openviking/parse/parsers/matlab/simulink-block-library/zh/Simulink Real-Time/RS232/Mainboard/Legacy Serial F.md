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

### 输入

### **XMT** — 要传输的数据向量

用于通过端口传输的数据向量。

**数据类型:** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`
### 输出

### **FIFO** — 通过串行端口 serialfifoptr 接收的数据的 FIFO

先进先出（FIFO），包含已从串行端口接收到的数据。

## 参数

### **串行端口** — 正在访问的端口 `Legacy Serial Port 1`（默认） | .. | `Legacy Serial Port 8` | `USB Serial Port 1` | .. | `USB Serial Port 8`

指定用于通信的串行端口。

如果使用 USB 转串行适配器，目标计算机会按照适配器连接到串行设备的顺序，将这些适配器检测为 `serusb1`、`serusb2` 等。

如果与端口的连接没有变化，则端口分配顺序会在目标计算机或串行设备的电源循环期间保持不变。

#### 编程使用

|  |
| --- |
| **模块参数:** `port` |

### **波特率** — 用于传输数据的 baud `115200`（默认） | `57600` | `38400` | `19200` | `9600` | `4800` | `2400` | `1200` | `600` | `300` | `110`

选择用于通过调制解调器发送和接收数据的 baud。

#### 编程使用

|  |
| --- |
| **模块参数:** `baud` |

### **数据位** — 每个字符的位数 `8`（默认） | `7` | `6` | `5`

选择用于编码一个字符的位数。

#### 编程使用

|  |
| --- |
| **模块参数:** `width` |

### **停止位** — 端口的停止位数 `1`（默认） | `2`

选择字符流的停止位数。

#### 编程使用

|  |
| --- |
| **模块参数:** `nstop` |

### **奇偶校验** — 用于检查数据传输的奇偶校验 `None`（默认） | `Even` | `Odd` | `Mark` | `Space`

选择用于检查数据完整性的奇偶校验。

#### 编程使用

|  |
| --- |
| **模块参数:** `parity` |

### **启用自动 RTS/CTS** — 启用 RTS/CTS 握手 `off`（默认） | `on`

要为流控制启用 Universal Asynchronous Receiver-Transmitter (UART) 的 Request To Send/Clear To Send (RTS/CTS) 握手，请选中此复选框。串行控制器使用 RTS/CTS 握手来防止由于您发送到的设备上的硬件 FIFO 溢出而导致的数据丢失。

通常，中断服务例程执行得足够快，可以清空 FIFO。如果您的模型出现 FIFO 溢出，请选中此复选框。

#### 编程使用

|  |
| --- |
| **模块参数:** `ctsmode` |

### **要修改的端口** — 正在访问的端口 `1`（默认） | `2`

此参数指定您要查看或修改其参数的端口。在 Simulink® 模块上，上方端口是端口 `1`，下方端口是端口 `2`。

#### 编程使用

|  |
| --- |
| **模块参数:** `port` |

### **接收 FIFO 大小** — FIFO 大小，单位为 bytes `1024`（默认）

此参数指定接收 FIFO 大小，单位为 bytes。

**示例:** `1024`

#### 编程使用

|  |
| --- |
| **模块参数:** `fifosize` |

**数据类型:** `int32`

### **发送数据类型** — 发送器的数据类型 `count+32 bit int`（默认） | `count+32 bit uint` | `count+16 bit int` | `count+16 bit uint` | `8 bit int null terminated` | `8 bit uint null terminated`

此参数指定发送器的数据类型。8 位数据类型要求输入向量中有一个以 NULL 结尾的字符向量。

16 位和 32 位数据类型保留第一个完整元素，以包含输入向量其余部分中预期元素的数量。仅发送每个数据元素的低序字节。设置此数据类型可使更宽的数据类型保存这些字节。

如果数据流需要 NULL 字节，请选择 16 位或 32 位数据类型之一。由于 8 位数据类型是以 NULL 结尾的字符向量，因此 NULL 字节会终止该字符向量。

#### 编程使用

|  |
| --- |
| **模块参数:** `idtype` |

### **采样时间** — 采样时间 `-1`（默认） | numeric

输入基本采样时间或基本采样时间的倍数。`-1` 表示采样时间继承。

#### 编程使用

|  |
| --- |
| **模块参数:** `sampletime` |

## 所属库

Simulink Real-Time / RS232 / Mainboard

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2008a 中引入**

### R2021b: 用于 RS232 模块的 USB 转串口

RS232 主板模块支持连接 USB 串行适配器端口。Legacy Serial Read 模块、Legacy Serial Write 模块、Legacy Serial Setup 模块、Legacy Serial Port 模块和 Legacy Serial Port F 模块的 `Serial port` 参数意味着您可以选择 `USB Serial Port` 或 `Legacy Serial Port`。

## 描述

通过带 FIFO 的主板底板串行端口发送和接收数据

Send/Receive FIFO 模块设置串行接口以发送和接收字符流和二进制流。它像 Send/Receive 模块一样发送输入数据，但通过先进先出 (FIFO) 输出传播接收到的数据。

包含 Send/Receive FIFO 模块和 FIFO Read 模块的模型提供与 Send/Receive 模块相同的能力。包含 Send/Receive FIFO 模块以及 FIFO Read HDRS 或 FIFO Read Binary 模块的模型提供比 Send/Receive 模块更强的能力。

有关详细信息，请参阅 RS-232 Serial Communication 和 RS-232 Legacy Drivers。
