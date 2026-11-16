---
type: simulink-block
title: 'EtherCAT Get Notifications'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'EtherCAT'
documentation_page: 'ethercatgetnotifications'
documentation_source_path: 'io_ref/ethercatgetnotifications.html'
language: zh-CN
chinese_source: worker-translation
---

# EtherCAT Get Notifications

## 端口

### 输出

### **Values** — 自描述 21 元素向量，包含 EtherCAT 通知代码 [`Length` `20 * Notification`]

- `Length` (`0` – `20`) — 向量中的通知数量。
- `Notification` — 由通知类型和特定值组成的复合值。类型包括：
- - `EC_NOTIFY_GENERIC`
    [`0x00000000`
    (`0`)] — 表示状态变化，例如：`0x00000001`
    (`1`) — `EtherCAT
    operational state change`.
  - `EC_NOTIFY_ERROR`
    [`0x00010000`
    (`65536`)] — 表示错误状态，例如 `0x00010001`
    (`65537`)：`cyclic command:
    working counter error`。有些描述错误状态的变化。
  - `EC_NOTIFY_SCANBUS`
    [`0x00030000`
    (`3*65536`)] — 表示 ScanBus 错误状态，例如
    `0x00030002`
    (`196610`)：`ScanBus
    mismatch`.
  - `EC_NOTIFY_HOTCONNECT`
    [`0x00040000`
    (`4*65536`)] — 表示 Hot Connect 状态，例如
    `0x00040005`
    (`262149`)：`Subordinate device
    disappears`.

要打印有效的通知值和描述，请在不带参数的情况下调用
`slrealtime.EtherCAT.filterNotifications`。

**数据类型：** `int32`

## 参数

### **网络设备索引** — EtherCAT 网络标识符 `0`（默认） | `0-11`

要将模块与 EtherCAT 网络关联，请将表示该网络的 EtherCAT Init 模块中的 **网络设备索引** 值输入到该模块的 **网络设备索引** 中。

#### 编程用法

|  |
| --- |
| **模块参数：** `device_id` |

### **采样时间** — 模块的采样时间 `-1`（默认） | numeric

输入基本采样时间或基本采样时间的倍数。使用 EtherCAT 任务采样时间。

#### 编程用法

|  |
| --- |
| **模块参数：** `sample_time` |

## 所属库

Simulink Real-Time / EtherCAT

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

从 EtherCAT 总线收集通知

EtherCAT Get Notifications 模块从 EtherCAT® 堆栈收集通知，并将它们作为 `int32` 的 21 元素向量呈现在输出端。在每个时间步，该模块输出其已累积的通知，并为下一个时间步清除自身。

该向量在元素 `1` 中包含通知数量，后面最多跟 `20` 个通知代码。最大通知数量为 `20`。如果总线向输出呈现超过 `20` 个通知，该模块会丢弃最新的通知，并呈现最先收到的 `20` 个通知。
