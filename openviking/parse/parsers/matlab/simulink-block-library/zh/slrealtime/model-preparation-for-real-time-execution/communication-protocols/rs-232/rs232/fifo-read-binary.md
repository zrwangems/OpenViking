---
type: simulink-block
title: 'FIFO Read Binary'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / RS-232 / RS232'
documentation_page: 'fiforeadbinary'
documentation_source_path: 'io_ref/fiforeadbinary.html'
language: zh-CN
chinese_source: worker-translation
---

# FIFO Read Binary

## 端口

### 输入

### **F** — 从中读取数据的 FIFO serialfifoptr

连接到包含从串行端口读取的数据的软件 FIFO。

### **E** — 启用从 FIFO 读取 `true` | `false`

如果为 `true`，则从 FIFO 读取。

#### 依赖关系

要使此端口可见，请设置参数 **启用输入**。

### 输出

### **1** — 编号输出流，每个报头向量一个

包含从 FIFO 读取的已解析数据的向量。每个输出对应一个报头。

#### 依赖关系

要确定此向量的数据类型，请设置参数 **输出向量类型**。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

## 参数

### **报头** — 二进制数据流中的搜索目标，二进制数据的元胞数组

输入您希望该模块在来自 FIFO 的数据块中查找的报头。将每个报头作为元胞数组中的一个元素输入，形式可以是带引号的字符向量，或对于不可打印的字节模式，使用 `char(val)` 进行串联。

#### 编程用法

|  |
| --- |
| **模块参数：** `hdr` |

### **消息长度** — 消息长度，以 bytes 为单位 `1024`（默认） | integer

输入消息长度，以 bytes 为单位。长度中包含报头。

#### 编程用法

|  |
| --- |
| **模块参数：** `lengths` |

### **输出行为** — 无新数据时的行为 `Zero output if no new data`（默认） | `Hold last output if no new data`

从列表中选择当 FIFO 未收到新数据时该模块的行为：

- `Hold last output if no new data` — 模块保持来自最后一条 FIFO 消息的输出。
- `Zero output if no new data` — 模块用 `0` 覆盖输出的第一个元素。

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

指定此模块要返回的最大字符数。生成的向量大小比此最大字符数多一。此模块通过将额外元素用作以下项来指示正在返回的字符数：

- 对于 8 位数据类型，用作 NULL 终止符
- 对于 16 位和 32 位数据类型，用作字符计数

输入足够大的数字。如果此数字太小，该模块无法返回任何内容。例如，如果输入值 `10`，但执行时 FIFO 包含 `11` 个字符加 null 终止符，则该模块不返回任何字符。如果它包含 `5`，则该模块返回 `5` 个字符加 NULL 终止符。

#### 编程用法

|  |
| --- |
| **模块参数：** `maxsize` |

### **输出向量类型** — 指定输出数据类型 `8 bit uint null terminated`（默认） | `count+32 bit int` | `count+32 bit uint` | `count+16 bit int` | `count+16 bit uint` | `8 bit int null terminated`

8 位数据类型在输出向量中生成以 NULL 终止的字符向量。对于 16 位和 32 位数据类型，第一个元素包含输出向量其余部分中应预期的元素数。

#### 编程用法

|  |
| --- |
| **模块参数：** `outputtype` |

### **采样时间** — 模块的采样时间 `-1`（默认） | numeric

输入基本采样时间或基本采样时间的倍数。`-1` 表示采样时间继承。

#### 编程用法

    sampletime

## 所属库

Simulink Real-Time / RS232

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

根据报头信息读取多个二进制数据流

FIFO Read Binary 模块从 FIFO 读取多个二进制报头。

此模块通过查找标记数据的唯一字节序列（报头）来识别和分离数据。每个报头指示固定长度二进制消息的起始位置。如果自该模块上次执行以来，同一报头多次到达 FIFO，则该模块丢弃较旧的数据。然后返回该报头的最新实例。该模块会跟上到达速度快于模块执行速度的数据。

示例模型 `slrt_ex_serialbaseboardbinarytest` 和 `slrt_ex_serialbaseboardbinarysplit` 展示了如何使用 FIFO Read HDRS 模块。要查找并打开这些模型，请在 MATLAB® 命令窗口中输入：

    modelfinder('slrealtime')

有关详细信息，请参阅 RS-232 串行通信和 RS-232 旧版驱动程序。
