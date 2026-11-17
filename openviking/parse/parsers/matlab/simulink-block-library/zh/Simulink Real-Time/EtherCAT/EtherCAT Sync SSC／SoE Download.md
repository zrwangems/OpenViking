---
type: simulink-block
title: 'EtherCAT Sync SSC/SoE Download'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'EtherCAT'
documentation_page: 'ethercatsyncsscsoedownload'
documentation_source_path: 'io_ref/ethercatsyncsscsoedownload.html'
language: zh-CN
chinese_source: worker-translation
---

# EtherCAT Sync SSC/SoE Download

## 端口

### 输入

### **Data** — 要写入从站设备的数据 numeric

用于写入 EtherCAT 从站设备的输入数据。该数据信号具有 **Data Type** 中指定的类型，以及 **Dimension** 给定的向量维度。

### 输出

### **Error** — 报告 EtherCAT 网络错误 `0` | integer

如果未发生错误，此端口输出 `0`。否则，它输出一个非零值。有关错误代码列表，请参阅 EtherCAT Error Codes。

## 参数

### **IDN** — 标识号 character vector

标识参数。

您的 EtherCAT 设备文档指定了 **IDN** 值。您可以选择 **IDN** 作为表示 16 位整数的字符向量（根据 IEC 61800 -7 -204），例如 `S-0-0150` 或 `P-0-0150`，其中：

- 第一个字段（位 15）：`S` 表示标准数据，`P` 表示产品特定数据
- 第二个字段（位 14 - 12）：`0..7` 表示参数集
- 第三个字段（位 11 - 0）：`0..4095` 表示数据块编号

#### 编程使用

|  |
| --- |
| **模块参数**：`idn` |

### **Drive Number** — 驱动器的索引号 integer

指定驱动器的十进制索引。

SoE 模块仅适用于电机控制器。单个从站设备可以支持一个或多个驱动器或电机通道。驱动器编号是此从站设备上此模块所针对的驱动器或电机通道的从零开始的索引。在 SoE 术语中，驱动器是向电机发送控制信号的逻辑。通常，该逻辑是从站设备内部的一个小型处理器。

#### 编程使用

|  |
| --- |
| **模块参数**：`drive` |

### **Data Type** — IDN 的数据类型 `double` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

要确定 IDN 的数据类型，请参阅从站设备文档中关于 IDN 的描述及其使用的数据类型。从列表中选择 **IDN** 的数据类型。

如果您选择的数据类型与条目的类型不匹配，该模块将通过 `Error` 输出返回一个非零值。

#### 编程使用

|  |
| --- |
| **模块参数**：`sig_type` |

### **Dimension** — 此 IDN 的数据维度 `1` (default)

指定此 IDN 的数据行维度。

要确定 IDN 的数据维度（向量大小），请参阅从站设备文档中关于 IDN 的描述及其使用的数据类型值数量（维度）。在从站设备手册的 SoE 描述中输入向量长度。

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

该模块使用配置文件的内容填充此下拉列表。

#### 编程使用

|  |
| --- |
| **模块参数**：`subdevice_name` |

### **Sample time** — 模块的采样时间 `-1` (default) | numeric

输入基本采样时间或基本采样时间的倍数。`-1` 表示采样时间被继承。EtherCAT Sync SSC/SoE Download 模块和 EtherCAT Sync SSC/SoE Upload 模块需要至少三个主 EtherCAT 处理任务步骤。请选择主任务采样时间三倍的采样时间，否则模型可能过载并停止。

#### 编程使用

|  |
| --- |
| **模块参数**：`sample_time` |

### **Timeout** — 等待从站设备响应的时长 numeric

输入等待 EtherCAT 从站设备响应的最大毫秒数。

#### 程序化使用

|  |
| --- |
| **模块参数：** `timeout` |

## 所属库

Simulink Real-Time / EtherCAT

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2020b 中引入**

## 描述

通过服务数据对象向从站设备同步发送数据

EtherCAT Sync SSC/SoE Download 模块提供基于 EtherCAT® (SoE) 下载的同步 SERCOS 接口（SErial Real time COmmunication Specification）。该模块在指定的从站设备中选择一个 **IDN**，并发送下载（写入）请求。然后该模块等待，直到收到对该请求的响应或直到超时时间到期。

对一次操作的响应需要主任务采样时间的若干个节拍。为同步模块分配比主任务采样时间更慢的采样时间。
