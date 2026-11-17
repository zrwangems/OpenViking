---
type: simulink-block
title: 'EtherCAT Async SDO Download'
family: 'ethercat'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'EtherCAT'
documentation_page: 'ethercatasyncsdodownload'
documentation_source_path: 'io_ref/ethercatasyncsdodownload.html'
language: zh-CN
chinese_source: worker-translation
---

# EtherCAT Async SDO Download

## 端口

### 输入

### **Data** — 要写入从站设备的数据 numeric

输入数据，用于写入 EtherCAT 从站设备。

### **Enable** — 使模块能够下载数据 int32

值为 `0` 会禁用下载。值大于或等于 `1` 会启用模块下载数据。

### 输出

### **Status** — 数据传输状态 `0` | `1` | `2` | `3`

异步数据传输的状态：

- `0` — 邮箱传输对象空闲，传输未运行
- `1` — 邮箱传输对象正在运行，传输未完成
- `2` — 传输成功执行
- `3` — 传输请求期间发生错误

### **Error** — 报告 EtherCAT 网络错误 `0` | integer

如果未发生错误，此端口发送 `0`。否则，它发送非零值。有关错误代码的列表，请参阅 EtherCAT 错误代码。

## 参数

### **索引** — CANopen 寄存器的索引 integer

指定 CANopen 寄存器的十六进制（例如，0x7）或十进制索引。

如果指定无效索引，该模块会通过 `Status` 输出返回 `3`，并通过 `Error` 输出返回非零值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `index` |

### **访问模式** — 选择 CoE 变量的访问模式 `Single Subindex`（默认） | `Complete Access`

当 **访问模式** 为 `Complete Access` 时，用于访问 CoE 变量的协议提供：

- 可访问单个终端设备的 CoE 字典中附加到单个索引的所有子索引。
- 在读取或写入其中一个子索引所需的时间内读取或写入所有子索引。
- 在写入调整参数集时同时更新所有子索引
- 捕获所有子索引的同时读取
- 允许使用需要完整访问才能进行配置的 EtherCAT 设备

#### 程序化使用

|  |
| --- |
| **模块参数：** `complete` |

### **子索引** — CANopen 寄存器的子索引 integer

指定 CANopen 寄存器的十六进制（例如，0x7）或十进制子索引。

如果指定无效子索引，该模块会通过 `Error` 输出返回非零值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `subIndex` |

### **数据类型** — CANopen 寄存器的数据类型 `double`（默认） | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

从列表中选择 CANopen 寄存器的数据类型。

如果选择的数据类型与该条目的类型不匹配，该模块会通过 `Error` 输出返回非零值。

#### 程序化使用

|  |
| --- |
| **模块参数：** `sig_type` |

### **维度** — CANopen 寄存器的维度 `1`（默认）

指定 CANopen 寄存器的行维度和列维度。

输入在从站设备手册的 CoE 描述中找到的向量长度。

#### 程序化使用

|  |
| --- |
| **模块参数：** `sig_dim` |

### **网络设备索引** — EtherCAT 网络标识符 `0`（默认） | `0-11`

要将模块与 EtherCAT 网络关联，请将表示该网络的 EtherCAT Init 模块中的 **网络设备索引** 值输入到该模块的 **网络设备索引** 中。

#### 程序化使用

|  |
| --- |
| **模块参数：** `device_id` |

### **子设备名称** — 包含 CANopen 寄存器的设备名称 character vector

从列表中选择包含 CANopen 寄存器的设备名称。

该模块使用配置文件的内容填充此下拉列表。

#### 程序化使用

|  |
| --- |
| **模块参数：** `subdevice_name` |

### **采样时间** — 模块的采样时间 `-1`（默认） | numeric

输入基本采样时间或基本采样时间的倍数。`-1` 表示继承采样时间。

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

**R2020b 中引入**

### R2022a：Complete Access 模式

可以为 EtherCAT Async SDO Upload 模块和 EtherCAT Async SDO Download 模块选择访问模式。

## 描述

将数据异步传输到由服务数据对象表示的从站设备

EtherCAT Async SDO Download 模块通过 **索引** 值在指定的 EtherCAT® 从站设备中选择一个 CANopen 寄存器，并发送写请求。然后该模块立即继续处理其输入数据。
