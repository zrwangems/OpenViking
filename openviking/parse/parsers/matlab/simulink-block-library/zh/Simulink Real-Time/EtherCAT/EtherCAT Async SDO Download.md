---
type: simulink-block
title: 'EtherCAT Async SDO Download'
family: 'slrealtime'
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
```yaml
ports:
- name: Data
  summary: 要写入从站设备的数据 numeric
  direction: input
- name: Enable
  summary: 使能模块下载数据 int32
  direction: input
- name: Status
  summary: 数据传输状态 0 | 1 | 2 | 3
  direction: output
- name: Error
  summary: 报告 EtherCAT 网络错误 0 | integer
  direction: output
```

### 输入

### **Data** — 要写入从站设备的数据 numeric

用于写入 EtherCAT 从站设备的输入数据。

### **Enable** — 使能模块下载数据 int32

值为 `0` 时禁用下载。值大于或等于 `1` 时使能模块下载数据。

### 输出

### **Status** — 数据传输状态 `0` | `1` | `2` | `3`

异步数据传输的状态：

- `0` — 邮箱传输对象空闲，传输未运行
- `1` — 邮箱传输对象运行中，传输未完成
- `2` — 传输成功执行
- `3` — 传输请求期间发生错误

### **Error** — 报告 EtherCAT 网络错误 `0` | integer

如果未发生错误，此端口输出 `0`。否则，输出非零值。有关错误代码列表，请参阅 EtherCAT Error Codes。
## 参数
```yaml
parameters:
- name: Index
  summary: CANopen 寄存器索引 integer
  group: ''
  block_parameter: index
- name: Access Mode
  summary: 选择 CoE 变量的访问模式 Single Subindex (default) | Complete Access
  group: ''
  block_parameter: complete
- name: Subindex
  summary: CANopen 寄存器子索引 integer
  group: ''
  block_parameter: subIndex
- name: Data Type
  summary: CANopen 寄存器数据类型 double (default) | single | int8 | uint8 | int16 | uint16 | int32 | uint32 | boolean
  group: ''
  block_parameter: sig_type
- name: Dimension
  summary: CANopen 寄存器维度 1 (default)
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
  summary: 模块采样时间 -1 (default) | numeric
  group: ''
  block_parameter: sample_time
```

### **Index** — CANopen 寄存器索引 integer

指定 CANopen 寄存器的十六进制（例如 0x7）或十进制索引。

如果指定无效索引，模块将通过 `Status` 输出返回 `3`，并通过 `Error` 输出返回非零值。

#### 编程使用

|  |
| --- |
| **模块参数**：`index` |

### **Access Mode** — 选择 CoE 变量的访问模式 `Single Subindex` (default) | `Complete Access`

当 **Access Mode** 为 `Complete Access` 时，CoE 变量访问协议提供：

- 访问单个终端设备在 CoE 字典中单个索引下附加的所有子索引。
- 在读取或写入其中一个子索引所需的时间内读取或写入所有子索引。
- 在写入整定参数集时同时更新所有子索引
- 捕获所有子索引的同时读取
- 允许使用需要完整访问进行配置的 EtherCAT 设备

#### 编程使用

|  |
| --- |
| **模块参数**：`complete` |

### **Subindex** — CANopen 寄存器子索引 integer

指定 CANopen 寄存器的十六进制（例如 0x7）或十进制子索引。

如果指定无效子索引，模块将通过 `Error` 输出返回非零值。

#### 编程使用

|  |
| --- |
| **模块参数**：`subIndex` |

### **Data Type** — CANopen 寄存器数据类型 `double` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

从列表中选择 CANopen 寄存器的数据类型。

如果选择的数据类型与条目类型不匹配，模块将通过 `Error` 输出返回非零值。

#### 编程使用

|  |
| --- |
| **模块参数**：`sig_type` |

### **Dimension** — CANopen 寄存器维度 `1` (default)

指定 CANopen 寄存器的行和列维度。

输入从站设备手册中 CoE 描述中所列的向量长度。

#### 编程使用

|  |
| --- |
| **模块参数**：`sig_dim` |

### **Network Device Index** — EtherCAT 网络标识符 `0` (default) | `0-11`

要将模块与 EtherCAT 网络关联，请将表示该网络的 EtherCAT Init 模块中的 **Network Device Index** 值输入到该模块的 **Network Device Index** 中。

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

### **Sample time** — 模块采样时间 `-1` (default) | numeric

输入基本采样时间或基本采样时间的倍数。`-1` 表示采样时间继承。

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

**在 R2020b 中引入**

### R2022a：完全访问模式

您可以为 EtherCAT Async SDO Upload 模块和 EtherCAT Async SDO Download 模块选择访问模式。

## 描述

通过服务数据对象异步向从站设备发送数据

EtherCAT Async SDO Download 模块通过指定的 EtherCAT® 从站设备中的 **Index** 值选择 CANopen 寄存器，并发送写入请求。然后该模块立即继续处理其输入数据。
