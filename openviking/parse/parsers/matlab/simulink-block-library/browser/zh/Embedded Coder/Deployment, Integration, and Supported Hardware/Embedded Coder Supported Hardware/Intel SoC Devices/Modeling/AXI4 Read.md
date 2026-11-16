---
type: simulink-block
title: 'AXI4 Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Intel SoC Devices / Modeling'
documentation_page: 'axi4read'
documentation_source_path: 'alterasoc/ref/axi4read.html'
language: zh-CN
chinese_source: worker-translation
---

# AXI4 Read

## 端口

### 输出

### **Port\_1** — 输出信号 N×1 向量

从 IP 核上的寄存器读取 N×1 向量，起始位置为距 IP 核基地址的 **偏移地址**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

### **设备名称** — IP 核设备的路径和文件名 `/dev/mwipcore`（默认） | character vector

输入 IP 核设备的路径和文件名。

**注意**

如果您使用 HDL Coder™ 生成 IP 核，则该 IP 核映射到 `/dev/mwipcore`。

#### 编程用法

|  |
| --- |
| **模块参数：** `DeviceName` |
| **默认值：** `/dev/mwipcore` |

### **偏移地址** — 从 IP 核基地址到寄存器的偏移量 `hex2dec( '0100' )`（默认） | decimal number

输入从 IP 核基地址到寄存器的偏移量。该模块从此寄存器读取数据。当您使用以 character vector 表示的十六进制数指定偏移地址时，请使用 `hex2dec` 函数。

**注意**

使用 HDL Coder 生成 IP 核时，您可以从 Custom IP Report (HDL Coder) 的 Register Address Mapping 部分获取偏移地址的值。有关详细信息，请参阅 Register Address Mapping (HDL Coder)。

#### 编程用法

|  |
| --- |
| **模块参数：** `RegisterOffset` |
| **默认值：** `hex2dec('0100')` |

### **数据类型** — IP 核使用的数据类型 `'uint16'`（默认） | `'single'` | `'double'` | `'int8'` | `'uint8'` | `'int16'` | `'int32'` | `'uint32'` | `'boolean'` | character vector

输入 IP 核使用的数据类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataType` |
| **默认值：** `'uint16'` |

### **输出向量大小** — 来自 IP 核的数据向量大小 `1`（默认） | positive integer scalar

输入从 IP 核设备读取的数据向量大小。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataLength` |
| **默认值：** `1` |

### **采样时间** — 采样时间 `-1`（默认）

输入采样时间，单位为秒。该模块轮询 IP 核上的寄存器以获取数据。当 **采样时间** 设置为 `-1` 时，包含此模块的子系统的基速率决定轮询频率。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |
| **默认值：** `-1` |

## 所属库

Embedded Coder Support Package for Intel SoC Devices

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

通过 AXI4-Lite 接口从目标硬件上的 IP 核读取数据

使用 AXI4-Lite 接口将数据向量从 Programmable Logic IP Core 上的一组连续寄存器读入嵌入式处理器。AXI4 Read 模块仅支持 AXI4-Lite 协议，允许进行简单、低吞吐量的内存映射通信。此协议的典型用途包括从控制和状态寄存器读取。
