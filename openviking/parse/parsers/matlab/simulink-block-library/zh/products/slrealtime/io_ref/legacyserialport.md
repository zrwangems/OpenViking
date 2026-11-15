---
type: simulink-block
title: 'Legacy Serial Port'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / RS-232 / RS232'
documentation_page: 'legacyserialport'
documentation_source_path: 'io_ref/legacyserialport.html'
language: zh-CN
chinese_source: worker-translation
---

# Legacy Serial Port

## 端口

### 输入

### **XMT** — 要发送的数据向量

用于通过端口发送的数据向量。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### 输出

### **RCV** — 通过串行端口接收的数据向量

包含从串行端口接收到的数据的向量。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

## 参数

### **串行端口** — 正在访问的端口 `Legacy Serial Port 1`（默认） | .. | `Legacy Serial Port 8` | `USB Serial Port 1` | .. | `USB Serial Port 8`

指定用于通信的串行端口。

如果使用 USB 转串口适配器，目标计算机会按照适配器连接到串行设备的顺序将这些适配器检测为 `serusb1`、`serusb2` 等。

如果端口连接没有变化，则端口分配顺序在目标计算机或串行设备的电源循环期间保持不变。

#### 编程用法

|  |
| --- |
| **模块参数：** `port` |

### **波特率** — 用于传输数据的波特率 `115200`（默认） | `57600` | `38400` | `19200` | `9600` | `4800` | `2400` | `1200` | `600` | `300` | `110`

选择用于通过调制解调器发送和接收数据的波特率。

#### 编程用法

|  |
| --- |
| **模块参数：** `baud` |

### **数据位** — 每个字符的位数 `8`（默认） | `7` | `6` | `5`

选择编码一个字符的位数。

#### 编程用法

|  |
| --- |
| **模块参数：** `width` |

### **停止位** — 端口的停止位数 `1`（默认） | `2`

选择字符流的停止位数。

#### 编程用法

|  |
| --- |
| **模块参数：** `nstop` |

### **奇偶校验** — 用于检查数据传输的奇偶校验 `None`（默认） | `Even` | `Odd` | `Mark` | `Space`

选择用于检查数据完整性的奇偶校验。

#### 编程用法

|  |
| --- |
| **模块参数：** `parity` |

### **启用自动 RTS/CTS** — 启用 RTS/CTS 握手 `off`（默认） | `on`

要启用通用异步收发器 (UART) 的请求发送/清除发送 (RTS/CTS) 握手以进行流控制，请选中此复选框。串行控制器使用 RTS/CTS 握手来防止由于要发送到的设备上的硬件 FIFO 溢出而导致的数据丢失。

通常，中断服务例程执行得足够快，可以清空 FIFO。如果您的模型发生 FIFO 溢出，请选中此复选框。

#### 编程用法

|  |
| --- |
| **模块参数：** `ctsmode` |

### **最大输出计数** — 模块返回的最大元素数 `1024`（默认） | integer

输入希望此模块单次调用返回的最大元素数。该模块使用此参数设置输出向量宽度。

如果选中 **读取到分隔符** 复选框，并且该模块在读取 **接收最大读取** 个字符之前未找到分隔符，则输出向量为空。

#### 编程用法

|  |
| --- |
| **模块参数：** `maxread` |

### **最小输出计数** — 模块返回的最小元素数 `1`（默认） | integer

输入要读取的最小字符数。如果 FIFO 中至少不包含此数量的字符，则输出向量为空。

#### 编程用法

|  |
| --- |
| **模块参数：** `minread` |

### **读取到分隔符** — 返回包括消息分隔符在内的字符 `on`（默认） | `off`

要使模块返回 FIFO 中的所有字符，直到并包括指定的分隔符，请选中此复选框。

如果缓冲区有错误，例如帧错误，调制解调器会返回字符，而不管是否存在分隔符。这些返回的字符有助于诊断错误，例如不匹配的波特率。

如果该模块在读取 **接收最大读取** 个字符之前未找到分隔符，则输出向量为空。

#### 编程用法

|  |
| --- |
| **模块参数：** `usedelimiter` |

### **分隔符** — 消息分隔符的数值 `13`（默认） | integer

输入作为消息分隔符的字符的数值。`0` 到 `255` 之间的任何值都有效。常见情况查找 `10`（换行）或 `13`（回车）。

#### 编程用法

|  |
| --- |
| **模块参数：** `delimiter` |

### **接收数据类型** — 接收器的数据类型 `8 bit int null terminated`（默认） | `8 bit uint null terminated` | `count+16 bit int` | `count+16 bit uint` | `count+32 bit int` | `count+32 bit uint`

此参数指定接收器的数据类型。8 位数据类型在输出向量中生成以 NULL 结尾的字符向量。

对于 16 位和 32 位数据类型，第一个元素包含输出向量其余部分中有效元素的数量。

对于 8 位数据类型，输出向量中仅包含字符数据，并追加 NULL 终止符。16 位或 32 位宽数据类型会使来自 UART 的错误状态放入每个数据元素的第二个字节中。（错误状态包含奇偶校验、溢出、帧和中断位。）字符数据位于每个元素的低 8 位中。向量的第一个元素包含后续数据元素的数量。

#### 编程用法

|  |
| --- |
| **模块参数：** `odtype` |

### **接收 FIFO 大小** — 以字节为单位的 FIFO 大小 `1024`（默认）

此参数指定接收 FIFO 大小（以字节为单位）。

**示例：** `1024`

#### 编程用法

|  |
| --- |
| **模块参数：** `fifosize` |

**数据类型：** `int32`

### **发送数据类型** — 发送器的数据类型 `count+32 bit int`（默认） | `count+32 bit uint` | `count+16 bit int` | `count+16 bit uint` | `8 bit int null terminated` | `8 bit uint null terminated`

此参数指定发送器的数据类型。8 位数据类型要求输入向量中以 NULL 结尾的字符向量。

16 位和 32 位数据类型保留第一个完整元素来包含输入向量其余部分中预期元素的数量。仅发送每个数据元素的低字节。设置此数据类型可使更宽的数据类型保存字节。

如果数据流需要 NULL 字节，请选择一种 16 位或 32 位数据类型。由于 8 位数据类型是以 NULL 结尾的字符向量，因此 NULL 字节会终止字符向量。

#### 编程用法

|  |
| --- |
| **模块参数：** `idtype` |

### **采样时间** — 采样时间 `-1`（默认） | numeric

输入基础采样时间或基础采样时间的倍数。`-1` 表示继承采样时间。

#### 编程用法

|  |
| --- |
| **模块参数：** `sampletime` |

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

通过主板基板串行端口发送和接收数据

Send/Receive 模块设置串行接口以发送和接收基本字符流。此模块在子系统内部具有基本的先进先出 (FIFO) 读取模块。它生成打包整数数组形式的输出（可设置为 8 位、16 位或 32 位）。字符出现在低字节中，接收状态信息出现在高字节中。

有关详细信息，请参阅 RS-232 Serial Communication 和 RS-232 Legacy Drivers。
