---
type: simulink-block
title: 'FIFO Read HDRS'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / RS-232 / RS232'
documentation_page: 'fiforeadhdrs'
documentation_source_path: 'io_ref/fiforeadhdrs.html'
language: zh-CN
chinese_source: worker-translation
---

# FIFO Read HDRS

## 端口

### 输入

### **F** — 要从其读取数据的 FIFO serialfifoptr

连接到包含从串行端口读取的数据的软件 FIFO。

### **E** — 启用从 FIFO 读取 `true` | `false`

如果为 `true`，则从 FIFO 读取。

#### 依赖关系

要使此端口可见，请设置参数 **启用输入**。
### 输出

### **1** — 编号输出流，每个标头向量一个

包含从 FIFO 读取的已解析数据的向量。每个输出对应一个标头。

#### 依赖关系

要确定此向量的数据类型，请设置参数 **输出向量类型**。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

## 参数

### **标头** — ASCII 数据流中的搜索目标 cell array of character vector

输入希望模块在来自 FIFO 的数据块中查找的标头。将每个标头以单引号形式作为 cell array 中的一个元素输入。

#### 编程用法

|  |
| --- |
| **模块参数：** `hdr` |

### **终止字符串** — 结束数据流的字符 `[13 10]`（默认） | [integer]

输入数据的终止 character vector。输入定义 character vector 末尾的字符，通常为一个或两个字符。

#### 编程用法

|  |
| --- |
| **模块参数：** `nterm` |

### **输出行为** — 无新数据时的行为 `Zero output if no new data`（默认） | `Hold last output if no new data`

从列表中选择当 FIFO 未收到新数据时模块的行为：

- `Hold last output if no new
  data` — 模块保留上一条 FIFO
  消息的输出。
- `Zero output if no new data` —
  模块用 `0` 覆盖输出的第一个元素。

#### 编程用法

|  |
| --- |
| **模块参数：** `hold` |

### **启用输入** — 启用从 FIFO 读取 `off`（默认） | `on`

要创建启用或禁用读取操作的输入端口，请选中此复选框。该输入端口接受 Boolean 信号。

#### 依赖关系

使输入端口 `E` 可见。

#### 编程用法

|  |
| --- |
| **模块参数：** `enable` |

### **最大读取大小** — 模块返回的最大字符数 `1024`（默认） | integer

指定此模块要返回的最大字符数。生成的向量大小比该最大字符数大一。此模块通过将额外元素用作以下内容来指示正在返回的字符数：

- 对于 8-bit 数据类型，用作 NULL 终止符
- 对于 16-bit 和 32-bit 数据类型，用作字符计数

输入足够大的数字。如果此数字太小，模块无法返回任何内容。例如，如果输入值 `10`，但在执行时 FIFO 包含 `11` 个字符加上 null 终止符，则模块不返回任何字符。如果包含 `5`，则模块返回 `5` 个字符加上 NULL 终止符。

#### 编程用法

|  |
| --- |
| **模块参数：** `maxsize` |

### **输出向量类型** — 指定输出数据类型 `8 bit uint null terminated`（默认） | `count+32 bit int` | `count+32 bit uint` | `count+16 bit int` | `count+16 bit uint` | `8 bit int null terminated`

8-bit 数据类型在输出向量中生成 NULL-terminated character vector。对于 16-bit 和 32-bit 数据类型，第一个元素包含预期在输出向量其余部分中出现的元素数。

#### 编程用法

|  |
| --- |
| **模块参数：** `outputtype` |

### **采样时间** — 模块的采样时间 `-1`（默认） | numeric

输入基本采样时间或基本采样时间的倍数。`-1` 表示采样时间继承。

#### 编程用法

```
sampletime
```

## 所属库

Simulink Real-Time / RS232

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

根据标头信息读取多个 ASCII 数据流

FIFO Read HDRS 模块识别并分离包含嵌入式标识符的 ASCII 数据流。

特定标头后面的数据长度可以变化，但具有共同的终止标记，例如 `<CR><LF>`。尽管可以使用 FIFO Read 模块实现相同的功能，但它需要一个复杂的状态机，其行为如下：

- 如果在模块上次执行后，同一个标头多次到达 FIFO，则模块返回该标头的最新实例。模块会跟上比模块执行速度更快到达的数据。
- 如果到达 FIFO 的标头与标头列表中的项不匹配，则模块丢弃该消息。
- 如果到达 FIFO 的字节与标头不匹配，则模块将该消息解释为具有未指定标头。模块会跳过这些字节。

示例模型 `slrt_ex_serialbaseboardasciitest` 和 `slrt_ex_serialbaseboardasciisplit` 展示如何使用 FIFO Read HDRS 模块。要查找并打开这些模型，请在 MATLAB® 命令窗口中键入：

```
modelfinder('slrealtime')
```

有关详细信息，请参阅 RS-232 Serial Communication 和 RS-232 Legacy Drivers。
