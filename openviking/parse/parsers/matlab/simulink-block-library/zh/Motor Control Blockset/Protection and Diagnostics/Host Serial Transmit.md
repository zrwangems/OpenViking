---
type: simulink-block
title: 'Host Serial Transmit'
family: 'protection-and-diagnostics'
product_id: 'mcb'
product_name: 'Motor Control Blockset'
documentation_release: R2025b
official_category: 'Protection and Diagnostics'
documentation_page: 'hostserialtransmit'
documentation_source_path: 'ref/hostserialtransmit.html'
language: zh-CN
chinese_source: worker-translation
---

# Host Serial Transmit

## 端口

### 输入

### **data** — 用于接收要传输的数据的端口（标量）

此端口接受一维数据和矩阵数据，以传输到目标硬件。

**数据类型：** `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

## 参数

### **Serial Connection** — 用于传输数据的串行端口 `Serial 1`（默认） | `Serial 2` | `Serial 3` | `Serial 4`

指定用于向目标硬件传输的串行端口。从列表中选择一个可用的串行端口。您可以使用 Host Serial Setup 模块配置所选端口。如果未配置串行端口，该模块会提示您进行配置。每个 Host Serial Transmit 模块都必须具有已配置的串行端口。如果您在仿真中使用多个端口，必须分别配置每个端口。

### **Additional package header** — 包头部数据 `'S'`（默认） | scalar

指定位于传输数据包前端的数据，该数据不属于正在传输的数据，通常表示数据开始。Additional package header 必须为 ASCII 值。您可以使用文本值或范围 (0–255) 内的数值。必须在此字段中输入的文本周围加上单引号，但引号不会被传输，也不计入总字节数。

### **Additional package terminator** — 包终止符数据 `'E'`（默认） | scalar

指定位于传输数据包末端的数据，该数据不属于正在传输的数据，通常表示数据结束。Additional package terminator 必须为 ASCII 值。您可以使用文本值或范围 (0–255) 内的数值。必须在此字段中输入的文本周围加上单引号，但引号不会被传输，也不计入总字节数。

### **Enable blocking mode** — 在发送数据时阻塞仿真 `off`（默认） | `on`

选择此参数可在传输数据时阻塞仿真。如果不希望写操作阻塞仿真，请清除此参数。

## 所属库

Motor Control Blockset / Protection and Diagnostics

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ Code Generation
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### Fixed-Point Conversion
使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中引入**

## 描述

配置主机侧串行通信接口，以将数据传输到串行端口

Host Serial Transmit 模块指定其向目标硬件传输的数据的配置。

该模块发送的数据包限制为 16 bytes 的 ASCII 字符，包括包头部和终止符。通过包括包头部、终止符或两者以及数据大小来计算包的大小。下表显示了每种数据类型的字节数。

| 数据类型 | 字节数 |
| --- | --- |
| `single` | 4 bytes |
| `int8` 和 `uint8` | 1 byte |
| `int16` 和 `uint16` | 2 bytes |
| `int32` 和 `uint32` | 4 bytes |

例如，如果您的数据包具有包头部 'S'（1 byte）和包终止符 'E'（1 byte），则为实际数据留下 14 bytes。如果您的数据类型为 `int8`，则数据包中有空间容纳 14 个 `int8`。如果您的数据类型为 `uint16`，则数据包中有空间容纳 7 个 `uint16`。如果您的数据类型为 `int32`，则数据包中仅有空间容纳 3 个 `int32`，剩余 2 bytes。即使您可以在剩余空间中容纳两个 `int8` 或一个 `uint16`，也不应这样做，因为不能在同一数据包中混合数据类型。

能够放入数据包的数据类型数量决定数据大小。在前面的示例中，`int8` 的数据大小为 14，`uint16` 的数据大小为 7。当数据大小超过 16 bytes 时，可能会出现意外行为，包括运行时错误。
