---
type: simulink-block
title: 'EtherCAT Async SDO Upload'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'EtherCAT'
documentation_page: 'ethercatasyncsdoupload'
documentation_source_path: 'io_ref/ethercatasyncsdoupload.html'
language: zh-CN
chinese_source: worker-translation
---

# EtherCAT Async SDO Upload

## 端口

### 输入

### **Enable** — 使模块能够上传 int32 数据

值 `0` 禁用上传。常量值
1 将在状态每次返回到空闲状态时发送新请求。
### 输出

### **Data** — 从站设备接收的数据 numeric

返回从 EtherCAT 从站设备接收的数据。

### **Status** — 数据传输状态 `0` | `1` | `2` | `3`

异步数据传输状态：

- `0` — 邮箱传输对象空闲，传输未运行
- `1` — 邮箱传输对象运行中，传输未完成
- `2` — 传输成功执行
- `3` — 传输请求期间发生错误

### **Error** — 报告 EtherCAT 网络错误 `0` | integer

如果未发生错误，此端口传输
`0`。否则，它传输非零值。有关错误代码的列表，
请参阅 EtherCAT Error Codes。

## 参数

### **索引** — CANopen 寄存器的索引 integer

指定 CANopen 寄存器的十六进制（例如，0x7）或十进制索引。

如果指定无效索引，模块将通过
`Status` 输出返回 `3`，并通过
`Error` 输出返回非零值。

#### 编程使用

|  |
| --- |
| **模块参数：** `index` |

### **访问模式** — 选择 CoE 变量的访问模式 `Single Subindex` (默认) | `Complete Access`

当 **访问模式** 为 `Complete
Access` 时，子索引参数被隐藏，并且在每种情况下会假定正确的
子索引。用于对变量进行 CoE 访问的完整访问协议提供：

- 访问单个终端设备的 CoE 字典中附加到单个索引的所有子索引。
- 在读取或写入其中一个子索引所需的时间内读取或写入所有子索引。
- 在写入整定参数集时同时更新所有子索引
- 捕获所有子索引的同时读取
- 允许使用需要完整访问才能进行配置的 EtherCAT 设备

#### 编程使用

|  |
| --- |
| **模块参数：** `complete` |

### **子索引** — CANopen 寄存器的子索引 integer

指定 CANopen 寄存器的十六进制（例如，0x7）或十进制子索引。

如果指定无效子索引，模块将通过
`Error` 输出返回非零值。

#### 编程使用

|  |
| --- |
| **模块参数：** `subIndex` |

### **数据类型** — CANopen 寄存器的数据类型 `double` (默认) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

从列表中选择 CANopen 寄存器的数据类型。

如果选择的数据类型与条目的类型不匹配，模块将通过
`Error` 输出返回非零值。

#### 编程使用

|  |
| --- |
| **模块参数：** `sig_type` |

### **维度** — CANopen 寄存器的维度 `1` (默认)

指定 CANopen 寄存器的行维度和列维度。

输入从站设备手册中 CoE 描述给出的向量长度。

#### 编程使用

|  |
| --- |
| **模块参数：** `sig_dim` |

### **网络设备索引** — EtherCAT 网络标识符 `0` (默认) | `0-11`

要将模块与 EtherCAT 网络关联，请将表示该网络的
EtherCAT Init 模块中的 **网络设备索引** 值输入到该模块的 **网络
设备索引** 中。

#### 编程使用

|  |
| --- |
| **模块参数：** `device_id` |

### **子设备名称** — 包含 CANopen 寄存器的设备名称 character vector

从列表中选择包含 CANopen 寄存器的设备名称。

模块使用配置文件的内容填充此下拉列表。

#### 编程使用

|  |
| --- |
| **模块参数：** `subdevice_name` |

### **采样时间** — 模块的采样时间 `-1` (默认) | numeric

输入基本采样时间或基本采样时间的倍数。`-1` 表示
采样时间继承。

#### 编程使用

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

**在 R2020b 中引入**

### R2022a：Complete Access 模式

您可以为 EtherCAT Async SDO Upload
模块和 EtherCAT Async SDO Download 模块选择访问模式。

## 描述

从由服务数据对象表示的从站设备异步读取数据

EtherCAT Async SDO Upload 模块通过
**索引** 值在指定 EtherCAT® 从站设备中选择 CANopen 寄存器，并发送读取请求。然后，它立即返回在之前对该模块的调用中从设备返回的值。
