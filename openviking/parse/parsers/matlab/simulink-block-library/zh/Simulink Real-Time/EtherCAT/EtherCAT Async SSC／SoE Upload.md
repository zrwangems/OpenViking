---
type: simulink-block
title: 'EtherCAT Async SSC/SoE Upload'
family: 'ethercat'
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

### 输入

### **Enable** — 使模块能够上传数据 int32

值 `0` 禁用上传。大于或等于 `1` 的值使模块能够上传数据。

### 输出

### **Data** — 从从站设备接收的数据 numeric

返回从 EtherCAT 从站设备接收的数据。数据信号具有在 Data Type 中指定的类型以及由 Dimension 给出的向量维度。

### **Status** — 数据传输状态 `0` | `1` | `2` | `3`

异步数据传输的状态：

- `0` — 邮箱传输对象空闲，传输未运行
- `1` — 邮箱传输对象正在运行，传输未完成
- `2` — 传输成功执行
- `3` — 传输请求期间发生错误

### **Error** — 报告 EtherCAT 网络错误 `0` | integer

如果未发生错误，此端口发送 `0`。否则，它发送非零值。有关错误代码列表，请参阅 EtherCAT 错误代码。

## 参数

### **IDN** — 标识号 字符向量

标识参数。

EtherCAT 设备的文档指定 **IDN** 值。您可以选择 **IDN** 作为表示 16 位整数的字符向量（根据 IEC 61800 -7 -204），例如 `S-0-0150` 或 `P-0-0150`，其中：

- 第一个字段（位 15）：`S` 表示标准数据，`P` 表示产品特定数据
- 第二个字段（位 14 - 12）：`0..7` 表示参数集
- 第三个字段（位 11 - 0）：`0..4095` 表示数据块编号

#### 编程用法

|  |
| --- |
| **模块参数：** `idn` |

### **Drive Number** — 驱动器的索引号 integer

指定驱动器的十进制索引。

SoE 模块仅适用于电机控制器。单个从站设备可以支持一个或多个驱动器或电机通道。驱动器编号是此从站设备上此模块所针对的驱动器或电机通道的从零开始的索引。在 SoE 术语中，驱动器是向电机发送控制信号的逻辑。通常，该逻辑是从站设备内部的小型处理器。

#### 编程用法

|  |
| --- |
| **模块参数：** `drive` |

### **Data Type** — IDN 的数据类型 `double` (default) | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

要确定 IDN 的数据类型，请参阅从站设备文档中有关 IDN 的描述以及其使用的数据类型。从列表中，选择 **IDN** 的数据类型。

如果选择的数据类型与该条目的类型不匹配，模块将通过 `Error` 输出返回非零值。

#### 编程用法

|  |
| --- |
| **模块参数：** `sig_type` |

### **Dimension** — 此 IDN 的数据维度 `1` (default)

指定此 IDN 的数据行维度。

要确定 IDN 的数据维度（向量大小），请参阅从站设备文档中有关 IDN 的描述以及其使用的数据类型值的数量（维度）。输入从站设备手册中 SoE 描述内给出的向量长度。

#### 编程用法

|  |
| --- |
| **模块参数：** `sig_dim` |

### **Network Device Index** — EtherCAT 网络标识符 `0` (default) | `0-11`

要将模块与 EtherCAT 网络关联，请将表示该网络的 EtherCAT Init 模块中的 **Network Device Index** 值输入到该模块的 **Network Device Index** 中。

#### 编程用法

|  |
| --- |
| **模块参数：** `device_id` |

### **SubDevice Name** — 包含 IDN 的设备名称 字符向量

从列表中，选择包含 **IDN** 的设备名称。

模块使用配置文件的内容填充此下拉列表。

#### 编程用法

|  |
| --- |
| **模块参数：** `subdevice_name` |

### **Sample time** — 模块的采样时间 `-1` (default) | numeric

输入基础采样时间或基础采样时间的倍数。`-1` 表示采样时间继承。

#### 编程用法

|  |
| --- |
| **模块参数：** `sample_time` |

### **Timeout** — 等待从站设备响应的时间 numeric

输入等待 EtherCAT 从站设备响应的最大毫秒数。

#### 编程用法

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

从由服务数据对象表示的从站设备异步读取数据

EtherCAT Async SSC/SoE Upload 模块提供通过 EtherCAT® 的异步 SERCOS 接口（SErial Real time COmmunication Specification）(SoE) 上传。该模块在指定的从站设备中选择一个 **IDN**，并发送上传（读取）请求。发送请求后，该模块立即返回在对该模块的较早调用中从设备返回的值。
