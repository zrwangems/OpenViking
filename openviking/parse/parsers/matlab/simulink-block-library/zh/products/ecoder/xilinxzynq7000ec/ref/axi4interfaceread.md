---
type: simulink-block
title: 'AXI4-Interface Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / AMD SoC Devices / Modeling'
documentation_page: 'axi4interfaceread'
documentation_source_path: 'xilinxzynq7000ec/ref/axi4interfaceread.html'
language: zh-CN
chinese_source: worker-translation
---

# AXI4-Interface Read

## 端口

### 输出

### **Port\_1** — 来自 IP 核寄存器的数据向量 *N*×1 向量

从 IP 核上的内存映射寄存器读取的 *N*×1 向量，起始于 **寄存器偏移量**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中，选择 **属性检查器**。

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

### **设备名称** — IP 核设备的路径和名称 `/dev/mwipcore`（默认）| 字符数组

输入 IP 核的路径和名称。

**注意**

如果使用 HDL Coder 生成 IP 核，HDL Coder 会将 IP 核映射到 `/dev/mwipcore`。

#### 编程用法

|  |
| --- |
| **模块参数：** `DeviceName` |

### **寄存器偏移量** — 寄存器相对于 IP 核基地址的偏移量 `hex2dec( '0104' )`（默认）| 十进制数

输入寄存器相对于 IP 核基地址的偏移量。该模块从此寄存器读取数据。使用十六进制数字字符向量指定地址偏移量时，请使用 `hex2dec` 函数。

**注意**

如果使用 HDL Coder 生成 IP 核，可以从 Custom IP Core Report (HDL Coder) 的 Register Address Mapping 部分获取地址偏移量的值。有关详细信息，请参阅 Register Address Mapping (HDL Coder)。

#### 编程用法

|  |
| --- |
| **模块参数：** `RegisterOffset` |

### **输出向量大小** — 要从 IP 核读取的数据向量的大小 `1`（默认）| 正整数

输入要从 IP 核设备读取的数据向量的大小。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataLength` |

### **数据类型** — IP 核的数据类型 `uint16`（默认）| `double` | `single` | `int8` | `uint8` | `int16` | `int32` | `uint32` | `boolean`

选择 IP 核使用的数据类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataType` |

### **采样时间** — 以 seconds 为单位的采样时间 `0.001`（默认）| 正标量

AXI4-Interface Read 模块输出的信号数据使用 AXI4-Lite 协议直接从 IP 核轮询。**采样时间**参数值或子系统的基本速率指定寄存器的轮询速率。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |

## 所属库

Embedded Coder Support Package for AMD SoC Devices

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2013a 中引入**

## 描述

从 AMD SoC 设备上的 IP 核读取数据

此模块从 HDL Coder™ 生成的 IP 核上的一组连续内存映射寄存器中读取数据向量。AXI4-Interface Read 模块使用处理系统的中央互连，提供与 FPGA 上 IP 核的简单内存映射通信。此模块最适合低吞吐量通信，例如检查状态、状态或控制寄存器。
