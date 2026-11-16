---
type: simulink-block
title: 'FIFO Write'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / RS-232 / RS232'
documentation_page: 'fifowrite'
documentation_source_path: 'io_ref/fifowrite.html'
language: zh-CN
chinese_source: official
---

# FIFO Write

## 端口

### 输入

### **D** — 写入 FIFO 的数据 向量

包含要写入 FIFO 的数据的向量。

#### 依赖关系

要确定此向量的数据类型，请设置参数 **Input vector type**。

**数据类型:** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`
### 输出

### **F** — FIFO 向量 serialfifoptr

连接到将数据写入串行端口的 FIFO。

### **DP** — 如果 FIFO 中存在新数据则返回 `True` `true` | `false`

如果 FIFO 中存在数据，则返回 `true`。

#### 依赖关系

要使该端口可见，请设置参数 **Max and Min read size ports** 和 **Enable passthrough**。

## 参数

### **Size** — 先进先出队列的大小，单位为字节 `1024` (默认) | 整数

输入 FIFO 中可同时容纳的元素数量。若对 FIFO 的写操作导致元素数量超过 **Size**，则会发生错误。

#### 编程用法

|  |
| --- |
| **模块参数：**`size` |

### **Input vector type** — 指定输入数据类型 **8 bit uint null terminated** (默认) | **count+32 bit int** | **count+32 bit uint** | **count+16 bit int** | **count+16 bit uint** | **8 bit int null terminated**

对于 16 位和 32 位数据类型，需在输入向量的首元素处包含后续元素的数量。计数器控制该模块复制到 FIFO 中的字节数。该模块不会将计数值本身复制到 FIFO 中。

对于 8 位数据类型，在输出向量中提供一个以 NULL 结尾的字符向量。该模块将数据复制到 FIFO 中，直至但不包括 NULL 终止符。

有关详细信息，请参阅RS-232 Legacy Drivers。

#### 编程用法

|  |
| --- |
| **模块参数：**`inputtype` |

### **Data present output** — 启用输出 `DP` `off` (默认) | `on`

选中此复选框可创建布尔输出 `DP`。如果 FIFO 中存在数据，`DP` 将变为 `true`。发送/接收子系统的发送端使用此输出。该输出被提供给使能发射模块，从而启用发射缓冲区空闲中断。

此设置使输出端口 `DP` 可见。

#### 编程用法

|  |
| --- |
| **模块参数：**`present` |

### **Sample time** — 模块采样时间 `-1` (默认) | 数值

输入基本采样时间或其倍数。`-1` 表示采样时间继承自父级。

#### 编程用法

```
sampletime
```

### **ID** — 溢出消息标识符 字符向量

输入用户定义的 FIFO 溢出消息标识符。

#### 编程用法

|  |
| --- |
| **模块参数：**`id` |

## 所属库

Simulink Real-Time / RS232

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

## 版本历史

**在 R2020b 中推出**

## 描述

编写简单的数据流

FIFO Write 模块是 FIFO 读写对的写入侧。使用此模块生成简单的数据流。

有关详细信息，请参阅RS-232 串行通信和RS-232 Legacy Drivers。
