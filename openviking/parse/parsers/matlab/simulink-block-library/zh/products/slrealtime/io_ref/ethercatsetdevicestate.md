---
type: simulink-block
title: 'EtherCAT Set Device State'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / EtherCAT'
documentation_page: 'ethercatsetdevicestate'
documentation_source_path: 'io_ref/ethercatsetdevicestate.html'
language: zh-CN
chinese_source: worker-translation
---

# EtherCAT Set Device State

## 端口

### 输入

### **New State** — 传输到 EtherCAT 网络的状态 `1` | `2` | `4` | `8`

| 状态 | 值 | 描述 |
| --- | --- | --- |
| `INIT` | 1 | 初始化 — 系统查找终端设备并初始化通信控制器。 |
| `PREOP` | 2 | 预运行 — 系统使用通信控制器交换系统特定的初始化数据。在此状态下，网络不能发送或接收信号数据。 |
| `SAFEOP` | 4 | 安全运行 — 网络正在运行并准备好进行全面操作。监控器将输入数据发送到终端设备。终端设备输出保持在安全状态。 |
| `OP` | 8 | 运行 — 网络处于完全运行状态。监控器将输入数据发送到终端设备。终端设备以输出数据响应。 |

### **Enable** — 使模块能够发送状态请求 `0` | `1`

该端口采用 Boolean 值。当为 true (1) 时，模块发送新的状态请求。当为 false (0) 时，模块不执行任何操作。

### 输出

### **Prev State** — 所选设备的先前状态 `1` | `2` | `4` | `8`

此端口返回设备的先前状态值。该值可能不与此模块的先前状态相同。

### **Error** — 报告 EtherCAT 状态错误 `0` | integer

如果未发生错误，此端口返回 `0`。否则，返回非零值。有关详细信息，请参阅 EtherCAT 错误代码。

## 参数

### **网络设备索引** — EtherCAT 网络标识符 `0` (默认) | `0-11`

要将模块与 EtherCAT 网络关联，请将代表该网络的 EtherCAT Init 模块中的 **网络设备索引** 值输入到该模块的 **网络设备索引** 中。

#### 编程用法

|  |
| --- |
| **模块参数：** `device_id` |

### **子设备名称** — EtherCAT 从站设备的名称 character vector

从 ENI 配置文件中提供的可用从站设备列表中选择一个 EtherCAT 从站设备。该配置文件由 EtherCAT Init 模块选择。

#### 编程用法

|  |
| --- |
| **模块参数：** `device_name` |

### **采样时间** — 模块的采样时间 `-1` (默认) | numeric

输入基本采样时间或基本采样时间的倍数。`-1` 表示采样时间为继承。

#### 编程用法

|  |
| --- |
| **模块参数：** `sample_time` |

## 所属库

Simulink Real-Time / EtherCAT

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2021b 中引入**

## 描述

设置 EtherCAT 网络的状态

EtherCAT Set Device State 模块将 EtherCAT® 网络上设备的状态设置为通过 `New State` 端口传入的值。
