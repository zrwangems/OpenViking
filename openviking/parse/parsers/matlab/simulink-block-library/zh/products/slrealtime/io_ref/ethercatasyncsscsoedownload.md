---
type: simulink-block
title: 'EtherCAT Async SSC/SoE Download'
family: 'slrealtime'
product_id: 'slrealtime'
product_name: 'Simulink Real-Time'
documentation_release: R2025b
official_category: 'Model Preparation for Real-Time Execution / Communication Protocols / EtherCAT'
documentation_page: 'ethercatasyncsscsoedownload'
documentation_source_path: 'io_ref/ethercatasyncsscsoedownload.html'
language: zh-CN
chinese_source: worker-translation
---

# EtherCAT Async SSC/SoE Download

## 端口

### 输入

### **Data** — 要写入从站设备的数据 numeric

用于写入 EtherCAT 从站设备的输入数据。该数据信号具有 **Data Type** 中指定的类型，以及由 **Dimension** 给定的向量维度。

### **Enable** — 使能模块下载数据 int32

Enable 输入是电平敏感的，当输入非零时，模块保持使能。要仅发送一次值，您可以使用单个采样时间脉冲使能模块。脉冲之后大约有三个周期的滞后，数据才会发送。

值 `0` 禁用下载。大于或等于 `1` 的值使能模块下载数据。

### 输出

### **Status** — 数据传输状态 `0` | `1` | `2` | `3`

异步数据传输的状态：

- `0` — 邮箱传输对象空闲，传输未运行
- `1` — 邮箱传输对象运行中，传输未完成
- `2` — 传输成功执行
- `3` — 传输请求期间发生错误

### **Error** — 报告 EtherCAT 网络错误 `0` | integer

如果未发生错误，此端口发送 `0`。否则，它发送非零值。有关错误代码列表，请参阅 EtherCAT Error Codes。

## 参数

### **IDN** — 标识号 character vector

标识参数。

您的 EtherCAT 设备文档指定了 **IDN** 值。您可以选择 **IDN** 作为表示 16-bit integer 的字符向量（根据 IEC 61800 -7 -204），例如 `S-0-0150` 或 `P-0-0150`，其中：

- 第一个字段（位 15）：`S` 表示标准数据，`P` 表示产品特定数据
- 第二个字段（位 14 - 12）：`0..7` 表示参数集
- 第三个字段（位 11 - 0）：`0..4095` 表示数据块编号

#### 编程用法

|  |
| --- |
| **模块参数：** `idn` |

### **Drive Number** — 驱动器的索引编号 integer

指定驱动器的十进制索引。

SoE 模块仅适用于电机控制器。单个从站设备可以支持一个或多个驱动器或电机通道。驱动器编号是此模块所针对的该从站设备上驱动器或电机通道的从零开始索引。在 SoE 术语中，驱动器是向电机发送控制信号的逻辑。通常，此逻辑是位于从站设备内部的小型处理器。

#### 编程用法

|  |
| --- |
| **模块参数：** `drive` |

### **Data Type** — IDN 的数据类型 `double`（默认） | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

要确定 IDN 的数据类型，请参阅从站设备文档中对该 IDN 的描述及其使用的数据类型。从列表中选择 **IDN** 的数据类型。

如果您选择的数据类型与该条目的类型不匹配，模块将通过 `Error` 输出返回非零值。

#### 编程用法

|  |
| --- |
| **模块参数：** `sig_type` |

### **Dimension** — 此 IDN 的数据维度 `1`（默认）

指定此 IDN 的数据行维度。

要确定 IDN 的数据维度（向量大小），请参阅从站设备文档中对该 IDN 的描述及其使用的数据类型值数量（维度）。输入从站设备手册中 SoE 描述所给出的向量长度。

#### 编程用法

|  |
| --- |
| **模块参数：** `sig_dim` |

### **Network Device Index** — EtherCAT 网络标识符 `0`（默认） | `0-11`

要将模块与 EtherCAT 网络关联，请将表示该网络的 EtherCAT Init 模块中的 **Network Device Index** 值输入到该模块的 **Network Device Index** 中。

#### 编程用法

|  |
| --- |
| **模块参数：** `device_id` |

### **SubDevice Name** — 包含 IDN 的设备名称 character vector

从列表中选择包含 **IDN** 的设备名称。

该模块使用配置文件的内容填充此下拉列表。

#### 编程用法

|  |
| --- |
| **模块参数：** `subdevice_name` |

### **Sample time** — 模块的采样时间 `-1`（默认） | numeric

输入基本采样时间或基本采样时间的倍数。`-1` 表示继承采样时间。

#### 编程用法

|  |
| --- |
| **模块参数：** `sample_time` |

### **Timeout** — 等待从站设备响应的时间 numeric

输入等待 EtherCAT 从站设备响应的最大时间，单位为 milliseconds。

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

将数据异步传输到由服务数据对象表示的从站设备

EtherCAT Async SSC/SoE Download 模块提供通过 EtherCAT® (SoE) 的异步 SERCOS 接口（SErial Real time COmmunication Specification）下载。该模块在指定的从站设备中选择一个 **IDN**，并发送下载（写入）请求。发送请求后，该模块立即继续处理其输入数据。
