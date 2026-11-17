---
type: simulink-block
title: 'EtherCAT Sync SDO Download'
family: 'ethercat'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'EtherCAT'
documentation_page: 'ethercatsyncsdodownload'
documentation_source_path: 'io_ref/ethercatsyncsdodownload.html'
language: zh-CN
chinese_source: worker-translation
---

# EtherCAT Sync SDO Download

## 端口

### 输入

### **Data** — 要写入从站设备的数据 numeric

用于写入 EtherCAT 从站设备的输入数据。
### 输出

### **Error** — 报告 EtherCAT 网络错误 `0` | integer

如果未发生错误，此端口发送 `0`。否则，它发送非零值。有关错误代码列表，请参阅 EtherCAT 错误代码。

## 参数

### **Index** — CANopen 寄存器的索引 integer

指定 CANopen 寄存器的十六进制（例如，0x7）或十进制索引。

如果指定无效索引，模块将通过 `Error` 输出返回非零值。

#### 编程用法

|  |
| --- |
| **模块参数：** `index` |

### **Subindex** — CANopen 寄存器的子索引 integer

指定 CANopen 寄存器的十六进制（例如，0x7）或十进制子索引。

如果指定无效子索引，模块将通过 `Error` 输出返回非零值。

#### 编程用法

|  |
| --- |
| **模块参数：** `subIndex` |

### **Data Type** — CANopen 寄存器的数据类型 `double` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

从列表中选择 CANopen 寄存器的数据类型。

如果选择的数据类型与条目的类型不匹配，模块将通过 `Error` 输出返回非零值。

#### 编程用法

|  |
| --- |
| **模块参数：** `sig_type` |

### **Dimension** — CANopen 寄存器的维度 `1` (default)

指定 CANopen 寄存器的行维度和列维度。

输入从站设备手册中的 CoE 描述所给出的向量长度。

#### 编程用法

|  |
| --- |
| **模块参数：** `sig_dim` |

### **Network Device Index** — EtherCAT 网络标识符 `0` (default) | `0-11`

要将模块与 EtherCAT 网络关联，请将代表该网络的 EtherCAT Init 模块中的 **Network Device Index** 值输入到该模块的 **Network Device Index** 中。

#### 编程用法

|  |
| --- |
| **模块参数：** `device_id` |

### **SubDevice Name** — 包含 CANopen 寄存器的设备名称 character vector

从列表中选择包含 CANopen 寄存器的设备名称。

模块使用配置文件的内容填充此下拉列表。

#### 编程用法

|  |
| --- |
| **模块参数：** `subdevice_name` |

### **Sample time** — 模块的采样时间 `-1` (default) | numeric

输入基本采样时间或基本采样时间的倍数。`-1` 表示采样时间继承。

#### 编程用法

|  |
| --- |
| **模块参数：** `sample_time` |

### **Timeout** — 等待从站设备响应的时间 numeric

返回超时错误之前等待响应的最大 milliseconds 数。

#### 编程用法

|  |
| --- |
| **模块参数：** `timeout` |

## 所属库

Simulink Real-Time / EtherCAT

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

将数据同步传输到由服务数据对象表示的从站设备

EtherCAT Sync SDO Download 模块通过指定的 EtherCAT® 从站设备中的 **Index** 值选择 CANopen 寄存器，并发送写请求。然后，该模块等待，直到收到响应或超时期限结束。

对操作的响应需要几个主任务采样时间节拍。为同步模块分配比主任务采样时间更慢的采样时间。
