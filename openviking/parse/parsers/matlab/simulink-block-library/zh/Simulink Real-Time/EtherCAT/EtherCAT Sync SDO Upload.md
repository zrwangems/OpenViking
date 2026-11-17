---
type: simulink-block
title: 'EtherCAT Sync SDO Upload'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'EtherCAT'
documentation_page: 'ethercatsyncsdoupload'
documentation_source_path: 'io_ref/ethercatsyncsdoupload.html'
language: zh-CN
chinese_source: worker-translation
---

# EtherCAT Sync SDO Upload

## 端口
```yaml
ports:
- name: Data
  summary: 从从站设备接收的数据 numeric
  direction: output
- name: Error
  summary: 报告 EtherCAT 网络错误 0 | integer
  direction: output
```

### 输出

### **Data** — 从从站设备接收的数据 numeric

返回从 EtherCAT 从站设备接收的数据。

### **Error** — 报告 EtherCAT 网络错误 `0` | integer

如果未发生错误，此端口输出
`0`。否则，输出非零值。有关错误代码列表，
请参阅 EtherCAT Error Codes。
## 参数
```yaml
parameters:
- name: Index
  summary: CANopen 寄存器的索引 integer
  group: ''
  block_parameter: index
- name: Subindex
  summary: CANopen 寄存器的子索引 integer
  group: ''
  block_parameter: subIndex
- name: Data Type
  summary: CANopen 寄存器的数据类型 double (default) | single | int8 | uint8 | int16 | uint16 | int32 | uint32 | boolean
  group: ''
  block_parameter: sig_type
- name: Dimension
  summary: CANopen 寄存器的维度 1 (default)
  group: ''
  block_parameter: sig_dim
- name: Network Device Index
  summary: EtherCAT 网络标识符 0 (default) | 0-11
  group: ''
  block_parameter: device_id
- name: SubDevice Name
  summary: 包含 CANopen 寄存器的设备名称 character vector
  group: ''
  block_parameter: subdevice_name
- name: Sample time
  summary: 模块的采样时间 -1 (default) | numeric
  group: ''
  block_parameter: sample_time
- name: Timeout
  summary: 等待从站设备响应的时间 numeric
  group: ''
  block_parameter: timeout
```

### **Index** — CANopen 寄存器的索引 integer

指定 CANopen
寄存器的十六进制（例如 0x7）或十进制索引。

如果指定无效索引，模块将通过
`Error` 输出返回非零值。

#### 编程使用

|  |
| --- |
| **模块参数**：`index` |

### **Subindex** — CANopen 寄存器的子索引 integer

指定 CANopen
寄存器的十六进制（例如 0x7）或十进制子索引。

如果指定无效子索引，模块将通过
`Error` 输出返回非零值。

#### 编程使用

|  |
| --- |
| **模块参数**：`subIndex` |

### **Data Type** — CANopen 寄存器的数据类型 `double` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

从列表中选择 CANopen 寄存器的数据类型。

如果选择的数据类型与条目的类型不匹配，模块将通过
`Error` 输出返回非零值。

#### 编程使用

|  |
| --- |
| **模块参数**：`sig_type` |

### **Dimension** — CANopen 寄存器的维度 `1` (default)

指定 CANopen 寄存器的行和列维度。

按照从站设备手册中的 CoE 描述输入向量长度。

#### 编程使用

|  |
| --- |
| **模块参数**：`sig_dim` |

### **Network Device Index** — EtherCAT 网络标识符 `0` (default) | `0-11`

要将模块与 EtherCAT 网络关联，请将表示该网络的 EtherCAT Init 模块中的 **Network Device Index** 值输入到该模块的 **Network
Device Index** 中。

#### 编程使用

|  |
| --- |
| **模块参数**：`device_id` |

### **SubDevice Name** — 包含 CANopen 寄存器的设备名称 character vector

从列表中选择包含 CANopen 寄存器的设备名称。

模块使用配置文件的内容填充此下拉列表。

#### 编程使用

|  |
| --- |
| **模块参数**：`subdevice_name` |

### **Sample time** — 模块的采样时间 `-1` (default) | numeric

输入基本采样时间或基本采样时间的倍数。`-1` 表示
采样时间继承。

#### 编程使用

|  |
| --- |
| **模块参数**：`sample_time` |

### **Timeout** — 等待从站设备响应的时间 numeric

返回超时错误之前等待响应的最大毫秒数。

#### 编程使用

|  |
| --- |
| **模块参数**：`timeout` |
## 所属库

Simulink Real-Time / EtherCAT

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

通过服务数据对象同步读取从站设备表示的数据

EtherCAT Sync SDO Upload 模块通过指定的 EtherCAT® 从站设备中的
**Index** 值选择 CANopen 寄存器，并发送读取请求。然后模块等待，
直到收到响应或超时时间结束。

操作的响应需要主
任务采样时间的若干个节拍。为同步模块分配比主任务采样
时间更慢的采样时间。
