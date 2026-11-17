---
type: simulink-block
title: 'EtherCAT Get Emergency'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'EtherCAT'
documentation_page: 'ethercatgetemergency'
documentation_source_path: 'io_ref/ethercatgetemergency.html'
language: zh-CN
chinese_source: worker-translation
---

# EtherCAT Get Emergency

## 端口
```yaml
ports:
- name: Err Code
  summary: 错误代码 uint16
  direction: output
  data_types: uint16
- name: Err Reg
  summary: 错误寄存器 uint8
  direction: output
  data_types: uint8
- name: Data
  summary: 紧急数据向量 uint8
  direction: output
  data_types: uint8
- name: Name
  summary: 站地址 uint8
  direction: output
  data_types: uint8
```

### 输出

### **Err Code** — 错误代码 uint16

`Err Code` 输出提供设备针对某一类紧急问题产生的主要错误代码。

**数据类型：** `uint16`

### **Err Reg** — 错误寄存器 uint8

`Err Reg` 输出提供特定的错误信息，用于标识由错误代码所指定的紧急问题类别中的具体紧急问题。

**数据类型：** `uint8`

### **Data** — 紧急数据向量 uint8

`Data` 输出是一个由 5 个 uint8 值组成的向量，设备可发送该向量以将数值附加到指定的紧急问题。其中至少有一个值必须为非零。

**数据类型：** `uint8`

### **Name** — 站地址 uint8

`Name` 输出是一个以 null 结尾的字符数组，用于标识发送紧急消息的设备。此输出是 ENI 文件中设备的名称。根据 TwinCAT® 或 EC-Engineer 软件用于标识设备的字符串不同，此名称可能有所不同。

**数据类型：** `uint8`
## 参数
```yaml
parameters:
- name: Network Device Index
  summary: EtherCAT 网络标识符 0（默认）| 0-11
  group: ''
  block_parameter: device_id
- name: Log messages to statusmonitor
  summary: 启用消息日志记录 on（默认）| off
  group: ''
  block_parameter: logmsg
- name: Sample time
  summary: 模块的采样时间 .001（默认）| 数值
  group: ''
  block_parameter: sample_time
```

### **Network Device Index** — EtherCAT 网络标识符 `0`（默认）| `0-11`

要将模块与 EtherCAT 网络关联，请将表示该网络的 EtherCAT Init 模块中的 **Network Device Index** 值输入到该模块的 **Network Device Index** 中。

#### 编程使用

|  |
| --- |
| **模块参数**：`device_id` |

### **Log messages to statusmonitor** — 启用消息日志记录 `on`（默认）| `off`

`Log messages to statusmonitor` 参数用于启用将消息记录到状态监视器。

#### 编程使用

|  |
| --- |
| **模块参数**：`logmsg` |

### **Sample time** — 模块的采样时间 `.001`（默认）| 数值

输入基本采样时间或基本采样时间的倍数。使用 EtherCAT 任务采样时间。

#### 编程使用

|  |
| --- |
| **模块参数**：`sample_time` |
## 所属库

Simulink Real-Time / EtherCAT

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

从 EtherCAT 总线收集紧急消息

EtherCAT Get Emergency 模块从 EtherCAT® 设备收集紧急消息，并将这些消息作为输出呈现在模型中。该模块还可以选择将条件记录到 Target Computer Status Monitor。模型中的输出和记录的状态包含所有紧急数据，因此可以在模型中采取相应措施。

添加一个模块以调用通知代码来收集紧急消息。EtherCAT Technology Group 定义了紧急错误代码的一般类型。具体的信息编码可在各设备制造商的文档中找到。

虽然设备发送的紧急消息错误代码可能存在重叠，但设备制造商通常不会实现所有代码，也不会对类似的紧急问题使用相同的代码。有关更多信息，请参阅制造商提供的设备文档。例如，在 Elmo Gold 系列电机驱动器应用手册中搜索，可以找到驱动器可能遇到的错误情况的错误代码和错误寄存器值的描述。下表显示了该手册中的部分信息。

**Elmo Gold 系列电机驱动器错误代码（子集）**

| 描述 | 错误代码 | 错误寄存器 | 数据字段 |
| --- | --- | --- | --- |
| CAN 消息丢失 | `0x8110` | `11` | `[0 0 0 0 0]` |
| 电机堵转 | `0x7121` | `21` | `[0 0 0 0 0]` |
| 队列过低。 | `0xff00` | `81` | `[0x56, idx, 0, 0, 0]` |
