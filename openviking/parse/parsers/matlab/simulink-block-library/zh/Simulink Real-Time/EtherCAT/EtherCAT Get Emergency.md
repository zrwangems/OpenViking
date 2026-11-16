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

### 输出

### **Err Code** — 错误码 uint16

`Err Code` 输出提供设备针对一类紧急问题产生的主错误码。

**数据类型：** `uint16`

### **Err Reg** — 错误寄存器 uint8

`Err Reg` 输出提供特定错误信息，用于标识由错误码指定的紧急问题类别内的特定紧急问题。

**数据类型：** `uint8`

### **Data** — 紧急数据向量 uint8

`Data` 输出是一个由 5 个 uint8 值组成的向量，设备可发送该向量以将值附加到指定的紧急问题。这些值中至少有一个必须非零。

**数据类型：** `uint8`

### **Name** — 站地址 uint8

`Name` 输出是一个以 null 结尾的字符数组，用于标识发送紧急消息的设备。此输出是 ENI 文件中设备的名称。根据 TwinCAT® 或 EC-Engineer 软件用于标识设备的字符串，此名称可能不同。

**数据类型：** `uint8`

## 参数

### **网络设备索引** — EtherCAT 网络标识符 `0`（默认）| `0-11`

要将模块与 EtherCAT 网络关联，请将表示该网络的 EtherCAT Init 模块中的 **网络设备索引** 值输入到该模块的 **网络设备索引** 中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `device_id` |

### **将消息记录到状态监视器** — 启用消息记录 `on`（默认）| `off`

`Log messages to statusmonitor` 参数启用将消息记录到状态监视器。

#### 程序化使用

|  |
| --- |
| **模块参数：** `logmsg` |

### **采样时间** — 模块的采样时间 `.001`（默认）| numeric

输入基础采样时间或基础采样时间的倍数。使用 EtherCAT 任务采样时间。

#### 程序化使用

|  |
| --- |
| **模块参数：** `sample_time` |

## 所属库

Simulink Real-Time / EtherCAT

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2023b 中引入**

## 描述

从 EtherCAT 总线收集紧急消息

EtherCAT Get Emergency 模块从 EtherCAT® 设备收集紧急消息，并将这些消息作为模型中的输出呈现。可选地，该模块可以将该状况记录到目标计算机状态监视器。模型中的输出和记录的状态包含所有紧急数据，因此可以在模型中采取行动。

添加一个模块以调用通知代码来收集紧急消息。EtherCAT 技术组定义紧急错误码的一般类型。具体信息编码可在各设备制造商提供的文档中找到。

虽然设备发送的紧急消息错误码可能存在重叠，但设备制造商通常不会实现所有代码，也不会对相似的紧急问题使用相同的代码。有关更多信息，请参阅制造商的设备文档。例如，在 Elmo Gold 系列电机驱动器应用手册中搜索，可以找到针对驱动器可能遇到的错误情况的错误码和错误寄存器值描述。下表显示了该手册中信息的一个子集。

**Elmo Gold 系列电机驱动器错误码（子集）**

| 描述 | 错误码 | 错误寄存器 | 数据字段 |
| --- | --- | --- | --- |
| CAN 消息丢失 | `0x8110` | `11` | `[0 0 0 0 0]` |
| 电机卡住 | `0x7121` | `21` | `[0 0 0 0 0]` |
| 队列过低。 | `0xff00` | `81` | `[0x56, idx, 0, 0, 0]` |
