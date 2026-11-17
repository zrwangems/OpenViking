---
type: simulink-block
title: 'Host Serial Transmit'
family: 'mcb'
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
```yaml
ports:
- name: data
  summary: 用于接收待发送数据的端口 标量
  direction: input
  data_types: single | int8 | uint8 | int16 | uint16 | int32 | uint32
```

### 输入

### **data** — 用于接收待发送数据的端口 标量

此端口接受一维和矩阵数据，用于向目标硬件发送。

**数据类型：** `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`
## 参数
```yaml
parameters:
- name: Serial Connection
  summary: 用于发送数据的串口 Serial 1（默认）| Serial 2 | Serial 3 | Serial 4
  group: ''
- name: Additional package header
  summary: 包头部数据 'S'（默认）| 标量
  group: ''
- name: Additional package terminator
  summary: 包终止符数据 'E'（默认）| 标量
  group: ''
- name: Enable blocking mode
  summary: 在发送数据时阻塞仿真 off（默认）| on
  group: ''
```

### **Serial Connection** — 用于发送数据的串口 `Serial 1`（默认）| `Serial 2` | `Serial 3` | `Serial 4`

指定一个串口以向目标硬件发送数据。从列表中选择一个可用的串口。您可以使用 Host Serial Setup 模块配置所选端口。如果您未配置串口，该模块会提示您进行配置。每个 Host Serial Transmit 模块必须有一个已配置的串口。如果您在仿真中使用多个端口，则必须分别配置每个端口。

### **Additional package header** — 包头部数据 `'S'`（默认）| 标量

指定位于所发送数据包前端的数据，该数据不属于正在发送的数据，通常表示数据的起始。附加包头部必须是一个 ASCII 值。您可以使用文本值或范围在 (0–255) 内的数值。您必须在此字段中输入的文本两侧加上单引号，但引号不会被发送，也不计入总字节数。

### **Additional package terminator** — 包终止符数据 `'E'`（默认）| 标量

指定位于所发送数据包末端的数据，该数据不属于正在发送的数据，通常表示数据的结束。附加包终止符必须是一个 ASCII 值。您可以使用文本值或范围在 (0–255) 内的数值。您必须在此字段中输入的文本两侧加上单引号，但引号不会被发送，也不计入总字节数。

### **Enable blocking mode** — 在发送数据时阻塞仿真 `off`（默认）| `on`

选择此参数可在发送数据时阻塞仿真。如果您不希望写操作阻塞仿真，请清除此参数。
## 所属库

Motor Control Blockset / Protection and Diagnostics

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2020a 中引入**

## 描述

配置主机端串行通信接口以将数据发送到串行端口

Host Serial Transmit 模块指定其发送到目标硬件的配置。

该模块发送的数据包限制为 16 字节的 ASCII 字符，包括包头和包尾。通过将包头、包尾或两者以及数据大小相加来计算包的大小。此表显示了每种数据类型的字节数。

| 数据类型 | 字节数 |
| --- | --- |
| `single` | 4 字节 |
| `int8` 和 `uint8` | 1 字节 |
| `int16` 和 `uint16` | 2 字节 |
| `int32` 和 `uint32` | 4 字节 |

例如，如果您的数据包具有包头 'S'（1 字节）和包尾 'E'（1 字节），则剩余 14 字节用于实际数据。如果您的数据为 `int8` 类型，则数据包中有空间容纳 14 个 `int8`。如果您的数据为 `uint16` 类型，则数据包中有空间容纳 7 个 `uint16`。如果您的数据为 `int32` 类型，则数据包中仅有空间容纳 3 个 `int32`，剩余 2 字节。即使您可以在剩余空间中容纳两个 `int8` 或一个 `uint16`，也不应这样做，因为您不能在同一包中混合数据类型。

可容纳到数据包中的数据类型数量决定了数据大小。在前面的示例中，`int8` 的数据大小为 14，`uint16` 的数据大小为 7。当数据大小超过 16 字节时，可能会出现意外行为，包括运行时错误。
