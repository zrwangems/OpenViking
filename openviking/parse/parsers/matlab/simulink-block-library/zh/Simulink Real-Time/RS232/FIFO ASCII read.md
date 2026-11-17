---
type: simulink-block
title: 'FIFO Read'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'RS232'
documentation_page: 'fiforead'
documentation_source_path: 'io_ref/fiforead.html'
language: zh-CN
chinese_source: worker-translation
---

# FIFO Read

## 端口

### 输入

### **F** — 从中读取数据的 FIFO serialfifoptr

连接到包含从串行端口读取的数据的软件 FIFO。

### **MAX** — 从 FIFO 读取的最大字节数 integer

该模块返回的最大字节数。

#### 依赖

要使此端口可见，请设置参数 **Max and Min read size ports**。

### **MIN** — 从 FIFO 读取的最小字节数 integer

该模块返回的最小字节数。

#### 依赖

要使此端口可见，请设置参数 **Max and Min read size ports**。

### 输出

### **D** — 从 FIFO 读取的解析数据 vector

包含从 FIFO 读取的解析数据的向量。

#### 依赖

要确定此向量的数据类型，请设置参数 **Output vector type**。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

### **ENA** — 传递 `MAX` 的值 integer

将端口 `MAX` 的值传递到读取 `ENA` 端口的模块。

#### 依赖

要使此端口可见，请设置参数 **Max and Min read size ports** 和 **Enable passthrough**。

## 参数

### **Maximum read size** — 模块返回的最大字符数 `1024`（默认）| integer

指定此模块返回的最大字符数。生成的向量大小比此最大字符数多一。此模块通过使用额外元素来指示返回的字符数，方式如下：

- 对于 8 位数据类型，作为空终止符
- 对于 16 位和 32 位数据类型，作为字符计数

输入一个足够大的数字。如果此数字太小，模块将无法返回任何内容。例如，如果您输入值 `10`，但在执行时 FIFO 包含 `11` 个字符加上空终止符，则模块不会返回任何字符。如果 FIFO 包含 `5`，则模块返回 `5` 个字符加上空终止符。

如果您选择参数 **Max and Min read size ports**，模块将端口 `MAX` 上输入的值解释为要返回的最大字符数。实际要返回的最大字符数是端口 `MAX` 上的值与模块参数中最大读取大小中的较小者。在二进制模式下且未选择 **Read to delimiter** 复选框时使用此值。

#### 编程使用

|  |
| --- |
| **模块参数：** `maxsize` |

### **Minimum read size** — 模块返回的最小字符数 `1`（默认）| integer

输入最小读取大小（以字节为单位）。FIFO 必须至少包含此数量的元素后才会返回元素。

如果您选择参数 **Max and Min read size ports**，端口 `MIN` 的值将取代此值。

#### 编程使用

|  |
| --- |
| **模块参数：** `minsize` |

### **Read to delimiter** — 返回分隔元素集 `on`（默认）| `off`

选中此复选框以启用返回以 **Delimiter** 值终止的元素集。在处理基于字符的元素时使用此参数。

#### 编程使用

|  |
| --- |
| **模块参数：** `usedelimiter` |

### **Delimiter** — 分隔元素集的终止值 `13`（默认）| `uint`

输入 8 位输入终止符的十进制值。此参数指定 FIFO 读取操作终止时所依据的值。此值与 **Read to delimiter** 参数配合使用。默认情况下，此模块查找回车符。仅当找到回车符时才返回字符。作为参考，回车符的十进制值为 `13`，换行符的十进制值为 `10`。

#### 编程使用

|  |
| --- |
| **模块参数：** `delimiter` |

### **Output vector type** — 指定输出数据类型 `8 bit uint null terminated`（默认）| `count+32 bit int` | `count+32 bit uint` | `count+16 bit int` | `count+16 bit uint` | `8 bit int null terminated`

8 位数据类型在输出向量中生成以 NULL 结尾的字符向量。对于 16 位和 32 位数据类型，第一个元素包含输出向量其余部分中预期元素的数量。

#### 编程使用

|  |
| --- |
| **模块参数**：`outputtype` |

### **Max and Min read size ports** — 启用最大和最小输入端口 `off`（默认）| `on`

当您选中此复选框时：

- 来自输入端口 `MAX` 的值是要从 FIFO 中移除的最大字符数。如果此数值超过 **Maximum read size** 的值，模块将忽略来自最大输入端口的数值。它将 **Maximum read size** 的值作为要从 FIFO 中移除的最大字符数。
- 来自输入端口 `MIN` 的值是在可以返回元素之前 FIFO 必须包含的最小字符数。此值将取代通过 **Minimum read size** 参数设置的值。

此设置使输入端口 `MAX` 和 `MIN` 可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`enable` |

### **Enable passthrough** — 启用 `MAX` 值的直通 `off`（默认）| `on`

选中此复选框可将输入端口 `MAX` 的值传递到输出端口 `ENA`。

#### 依赖关系

使输出端口 `ENA` 变为可见。

#### 编程使用

|  |
| --- |
| **模块参数**：`enableout` |

### **Sample time** — 模块的采样时间 `-1`（默认）| 数值

输入基本采样时间或基本采样时间的倍数。`-1` 表示采样时间继承。

#### 编程使用

```
sampletime
```

## 所属库

Simulink Real-Time / RS232

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ Code Generation 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

读取简单数据流

FIFO Read 模块是 FIFO 读/写对的读取端。您可以使用此模块解析简单的数据流。该模块以两种模式运行，您可以通过 **Read to delimiter** 复选框进行设置。

- 如果选中 **Read to delimiter** 复选框，则仅当指定的分隔符已写入 FIFO Write 模块时，该模块才会读取元素。如果找到分隔符，该模块将在输出向量中返回截至并包括该分隔符在内的元素。如果未找到分隔符，该模块将返回由数据类型确定的零长度向量。（如果得到零长度向量，您可以让模型执行特定操作或忽略该情况。）
- 如果清除 **Read to delimiter** 复选框，该模块将返回介于 **Minimum read size** 与 FIFO 中当前元素数量和 **Maximum read size** 两者中较小值之间的元素。

  执行 ASCII 读取时，请选中 **Read to delimiter** 复选框。执行二进制读取时，请清除此复选框。

以下是一些如何设置 FIFO Read 模块的示例：

- **中断服务程序的发送端** — 如果中断原因不是 UART 上的空硬件 FIFO，则 maximum 输入端口接收值 `0`。如果硬件 FIFO 为空，则它接收硬件 FIFO 的大小。minimum 输入端口接收常量值 `1`。
- **中断服务程序的接收端** — ASCII 数据的典型情况是禁用 minimum 和 maximum 输入端口。选中 **Read to delimiter parameter** 复选框，并且 **Delimiter** 参数的值为回车或换行。**Maximum read size** 参数的值很大（大约为 FIFO 大小的量级），并且 **Minimum read size** 参数的值为 1。在这种形式下，驱动程序的行为类似于非阻塞读取行。

  对于固定长度二进制数据块的另一种接收端配置，将 **Maximum read size** 和 **Minimum read size** 参数的值设置为该块的固定长度。不选中 **Read to delimiter** 参数。

对于复杂数据流，请考虑使用 FIFO Read HDRS 和 FIFO Read Binary 模块。有关何时使用这些模块的指南，请参阅 RS-232 FIFO Read Blocks。

有关详细信息，请参阅 RS-232 Serial Communication 和 RS-232 Legacy Drivers。
