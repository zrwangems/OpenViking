---
type: simulink-block
title: 'EtherCAT Async SSC/SoE Upload'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'EtherCAT'
documentation_page: 'ethercatasyncsscsoeupload'
documentation_source_path: 'io_ref/ethercatasyncsscsoeupload.html'
language: zh-CN
chinese_source: worker-translation
---

# EtherCAT Async SSC/SoE Upload

## 端口
```yaml
ports:
- name: Enable
  summary: 使能模块上传数据 int32
  direction: input
- name: Data
  summary: 从从站设备接收的数据 numeric
  direction: output
- name: Status
  summary: 数据传输状态 0 | 1 | 2 | 3
  direction: output
- name: Error
  summary: 报告 EtherCAT 网络错误 0 | integer
  direction: output
```

### 输入

### **Enable** — 使能模块上传数据 int32

值为 `0` 时禁用上传。值大于或等于 `1` 时使能模块上传数据。

### 输出

### **Data** — 从从站设备接收的数据 numeric

返回从 EtherCAT 从站设备接收的数据。数据信号的类型由 Data Type 指定，向量维度由 Dimension 指定。

### **Status** — 数据传输状态 `0` | `1` | `2` | `3`

异步数据传输状态：

- `0` — 邮箱传输对象空闲，传输未运行
- `1` — 邮箱传输对象运行中，传输未完成
- `2` — 传输成功执行
- `3` — 传输请求期间发生错误

### **Error** — 报告 EtherCAT 网络错误 `0` | integer

如果未发生错误，此端口输出 `0`。否则，输出非零值。有关错误代码列表，请参阅 EtherCAT Error Codes。
## 参数
```yaml
parameters:
- name: IDN
  summary: 标识号 character vector
  group: ''
  block_parameter: idn
- name: Drive Number
  summary: 驱动器的索引号 integer
  group: ''
  block_parameter: drive
- name: Data Type
  summary: IDN 的数据类型 double (default) | single | int8 | uint8 | int16 | uint16 | int32 | uint32 | boolean
  group: ''
  block_parameter: sig_type
- name: Dimension
  summary: 此 IDN 的数据维度 1 (default)
  group: ''
  block_parameter: sig_dim
- name: Network Device Index
  summary: EtherCAT 网络标识符 0 (default) | 0-11
  group: ''
  block_parameter: device_id
- name: SubDevice Name
  summary: 包含 IDN 的设备名称 character vector
  group: ''
  block_parameter: subdevice_name
- name: Sample time
  summary: 模块的采样时间 -1 (default) | numeric
  group: ''
  block_parameter: sample_time
- name: Timeout
  summary: 等待从属设备响应的时间 数值
  group: ''
  block_parameter: timeout
```

### **IDN** — 标识号 character vector

标识参数。

EtherCAT 设备的文档指定了 **IDN** 值。您可以选择 **IDN** 为表示 16 位整数的字符向量（根据 IEC 61800 -7 -204），例如 `S-0-0150` 或 `P-0-0150`，其中：

- 第一字段（位 15）：`S` 表示标准数据，`P` 表示产品特定数据
- 第二字段（位 14 - 12）：`0..7` 表示参数集
- 第三字段（位 11 - 0）：`0..4095` 表示数据块编号

#### 编程使用

|  |
| --- |
| **模块参数**：`idn` |

### **Drive Number** — 驱动器的索引号 integer

指定驱动器的十进制索引。

SoE 模块仅适用于电机控制器。单个从站设备可以支持一个或多个驱动器或电机通道。驱动器编号是此模块所指向的从站设备上驱动器或电机通道的从零开始的索引。在 SoE 术语中，驱动器是向电机发送控制信号的逻辑。通常，该逻辑是从站设备内部的一个小型处理器。

#### 编程使用

|  |
| --- |
| **模块参数**：`drive` |

### **Data Type** — IDN 的数据类型 `double` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

要确定 IDN 的数据类型，请参阅从站设备文档中关于 IDN 的描述及其使用的数据类型。从列表中选择 **IDN** 的数据类型。

如果选择的数据类型与条目的类型不匹配，模块将通过 `Error` 输出返回非零值。

#### 编程使用

|  |
| --- |
| **模块参数**：`sig_type` |

### **Dimension** — 此 IDN 的数据维度 `1` (default)

指定此 IDN 数据的行维度。

要确定 IDN 的数据维度（向量大小），请参阅从站设备文档中关于 IDN 的描述及其使用的数据类型值数量（维度）。输入从站设备手册中 SoE 描述中所找到的向量长度。

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

### **SubDevice Name** — 包含 IDN 的设备名称 character vector

从列表中选择包含 **IDN** 的设备名称。

模块使用配置文件的内容填充此下拉列表。

#### 编程使用

|  |
| --- |
| **模块参数**：`subdevice_name` |

### **Sample time** — 模块的采样时间 `-1` (default) | numeric

输入基本采样时间或基本采样时间的倍数。`-1` 表示采样时间继承。

#### 程序化使用

|  |
| --- |
| **模块参数：** `sample_time` |

### **Timeout** — 等待从属设备响应的时间 数值

输入等待 EtherCAT 从属设备响应的最大毫秒数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `timeout` |
## 所属库

Simulink Real-Time / EtherCAT

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

从服务数据对象所表示的从属设备异步读取数据

EtherCAT Async SSC/SoE Upload 模块通过 EtherCAT®（SoE）提供异步 SERCOS 接口（SErial Real time COmmunication Specification）上传功能。该模块在指定的从属设备中选择一个 **IDN**，并发送上传（读取）请求。发送请求后，该模块立即返回设备在先前调用该模块时返回的值。
