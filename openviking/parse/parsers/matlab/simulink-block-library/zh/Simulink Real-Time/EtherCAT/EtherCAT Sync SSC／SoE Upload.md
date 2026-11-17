---
type: simulink-block
title: 'EtherCAT Sync SSC/SoE Upload'
family: 'ethercat'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'EtherCAT'
documentation_page: 'ethercatsyncsscsoeupload'
documentation_source_path: 'io_ref/ethercatsyncsscsoeupload.html'
language: zh-CN
chinese_source: worker-translation
---

# EtherCAT Sync SSC/SoE Upload

## 端口

### 输出

### **Data** — 从下级设备接收的数据 numeric

返回从 EtherCAT 下级设备接收的数据。数据信号的类型由“数据类型”参数指定，向量维度由“维度”参数给定。

### **Error** — 报告 EtherCAT 网络错误 `0` | integer

如果未发生错误，此端口发送 `0`。否则，发送非零值。有关错误代码列表，请参见 EtherCAT 错误代码。

## 参数

### **IDN** — 标识号 character vector

标识参数。

您的 EtherCAT 设备文档指定了 **IDN** 值。您可以选择 **IDN** 作为表示 16 位整数的 character vector（根据 IEC 61800 -7 -204），例如 `S-0-0150` 或 `P-0-0150`，其中：

- 第一个字段（位 15）：`S` 表示标准数据，`P` 表示产品特定数据
- 第二个字段（位 14 - 12）：`0..7` 表示参数集
- 第三个字段（位 11 - 0）：`0..4095` 表示数据块编号

#### 编程使用

|  |
| --- |
| **模块参数：** `idn` |

### **驱动器编号** — 驱动器的索引号 integer

指定驱动器的十进制索引。

SoE 模块仅适用于电机控制器。单个下级设备可以支持一个或多个驱动器或电机通道。驱动器编号是此下级设备上此模块所针对的驱动器或电机通道的从零开始的索引。在 SoE 术语中，驱动器是向电机发送控制信号的逻辑。通常，此逻辑是下级设备内部的一个小型处理器。

#### 编程使用

|  |
| --- |
| **模块参数：** `drive` |

### **数据类型** — IDN 的数据类型 `double` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

要确定 IDN 的数据类型，请参阅下级设备文档，了解 IDN 的描述及其使用的数据类型。从列表中选择 **IDN** 的数据类型。

如果您选择的数据类型与条目的类型不匹配，模块将通过 `Error` 输出返回非零值。

#### 编程使用

|  |
| --- |
| **模块参数：** `sig_type` |

### **维度** — 此 IDN 的数据维度 `1` (default)

指定此 IDN 的数据行维度。

要确定 IDN 的数据维度（向量大小），请参阅下级设备文档，了解 IDN 的描述及其使用的数据类型值数量（维度）。在 SoE 描述中按下级设备手册中的说明输入向量长度。

#### 编程使用

|  |
| --- |
| **模块参数：** `sig_dim` |

### **网络设备索引** — EtherCAT 网络标识符 `0` (default) | `0-11`

要将模块与 EtherCAT 网络关联，请将表示该网络的 EtherCAT Init 模块中的 **网络设备索引** 值输入到该模块的 **网络设备索引** 中。

#### 编程使用

|  |
| --- |
| **模块参数：** `device_id` |

### **子设备名称** — 包含 IDN 的设备名称 character vector

从列表中选择包含 **IDN** 的设备的名称。

此模块使用配置文件的内容填充此下拉列表。

#### 编程使用

|  |
| --- |
| **模块参数：** `subdevice_name` |

### **采样时间** — 模块的采样时间 `-1` (default) | numeric

输入基本采样时间或基本采样时间的倍数。`-1` 表示采样时间继承。EtherCAT Sync SSC/SoE Download 模块和 EtherCAT Sync SSC/SoE Upload 模块需要主 EtherCAT 处理任务的至少三个步长。选择主任务采样时间三倍的采样时间，否则模型可能过载并停止。

#### 编程使用

|  |
| --- |
| **模块参数：** `sample_time` |

### **超时** — 等待下级设备响应的时间 numeric

输入等待 EtherCAT 下级设备响应的最大 milliseconds 数。

#### 编程使用

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

从下级设备同步读取由服务数据对象表示的数据

EtherCAT Sync SSC/SoE Upload 模块提供同步 SERCOS 接口 (SErial Real time COmmunication Specification) over EtherCAT® (SoE) 上传。该模块在指定的下级设备中选择一个 **IDN**，并发送上传（读取）请求。然后，该模块等待直到收到对该请求的响应，或直到超时时间到期。

一次操作的响应需要主任务采样时间的多个 tick。为同步模块分配比主任务采样时间更慢的采样时间。
