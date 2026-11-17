---
type: simulink-block
title: 'FIFO Write'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'RS232'
documentation_page: 'fifowrite'
documentation_source_path: 'io_ref/fifowrite.html'
language: zh-CN
chinese_source: worker-translation
---

# FIFO Write

## 端口
```yaml
ports:
- name: D
  summary: 要写入 FIFO 的数据向量
  direction: input
  data_types: int8 | uint8 | int16 | uint16 | int32 | uint32
- name: F
  summary: FIFO 向量 serialfifoptr
  direction: output
- name: DP
  summary: 如果 FIFO 中存在新数据则为 True true | false
  direction: output
```

### 输入

### **D** — 要写入 FIFO 的数据向量

包含要写入 FIFO 的数据的向量。

#### 依赖关系

要确定此向量的数据类型，请设置参数 **Input vector type**。

**数据类型：** `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`
### 输出

### **F** — FIFO 向量 serialfifoptr

连接到将数据写入串行端口的 FIFO。

### **DP** — 如果 FIFO 中存在新数据则为 `True` `true` | `false`

如果 FIFO 中存在数据，则返回 `true`。

#### 依赖关系

要使此端口可见，请设置参数 **Max and Min read size ports** 和 **Enable passthrough**。
## 参数
```yaml
parameters:
- name: Size
  summary: FIFO 的大小，以字节为单位 1024（默认值）| 整数
  group: ''
  block_parameter: size
- name: Input vector type
  summary: 指定输入数据类型 8 bit uint null terminated（默认值）| count+32 bit int | count+32 bit uint | count+16 bit int | count+16 bit
    uint | 8 bit int null terminated
  group: ''
  block_parameter: inputtype
- name: Data present output
  summary: 启用输出 DP off（默认值）| on
  group: ''
  block_parameter: present
- name: Sample time
  summary: 模块的采样时间 -1（默认值）| 数值
  group: ''
- name: ID
  summary: 溢出消息的标识符 字符向量
  group: ''
  block_parameter: id
```

### **Size** — FIFO 的大小，以字节为单位 `1024`（默认值）| 整数

输入 FIFO 一次可以容纳的元素数量。如果对 FIFO 的写操作导致元素数量超过 **Size**，则会发生错误。

#### 程序化使用

|  |
| --- |
| **模块参数：** `size` |

### **Input vector type** — 指定输入数据类型 `8 bit uint null terminated`（默认值）| `count+32 bit int` | `count+32 bit uint` | `count+16 bit int` | `count+16 bit uint` | `8 bit int null terminated`

对于 16 位和 32 位数据类型，将输入向量其余部分中预期元素的数量作为第一个元素包含在内。该计数控制模块复制到 FIFO 中的字节数。模块不会将计数本身复制到 FIFO 中。

对于 8 位数据类型，在输出向量中提供以 NULL 结尾的字符向量。模块将数据复制到 FIFO 中，直到但不包括 NULL 终止符。

有关详细信息，请参阅 RS-232 Legacy Drivers。

#### 程序化使用

|  |
| --- |
| **模块参数：** `inputtype` |

### **Data present output** — 启用输出 `DP` `off`（默认值）| `on`

选中此复选框以创建布尔输出 `DP`。如果 FIFO 中存在数据，`DP` 变为 `true`。发送/接收子系统的发送端使用此输出。此输出被提供给 Enable TX 模块，该模块启用发送器缓冲区空中断。

此设置使输出端口 `DP` 可见。

#### 程序化使用

|  |
| --- |
| **模块参数：** `present` |

### **Sample time** — 模块的采样时间 `-1`（默认值）| 数值

输入基本采样时间或基本采样时间的倍数。`-1` 表示采样时间继承。

#### 程序化使用

```
sampletime
```

### **ID** — 溢出消息的标识符 字符向量

输入用户定义的 FIFO 溢出消息标识符。

#### 程序化使用

|  |
| --- |
| **模块参数：** `id` |
## 所属库

Simulink Real-Time / RS232

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

写入简单数据流

FIFO Write 模块是 FIFO 读/写对的写入端。使用此模块生成简单数据流。

有关详细信息，请参阅 RS-232 Serial Communication 和 RS-232 Legacy Drivers。
