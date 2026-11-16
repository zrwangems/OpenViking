---
type: simulink-block
title: 'AXI4 Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / Intel SoC Devices / Modeling'
documentation_page: 'axi4write'
documentation_source_path: 'alterasoc/ref/axi4write.html'
language: zh-CN
chinese_source: worker-translation
---

# AXI4 Write

## 端口

### 输入

### **Port\_1** — 输入信号 1-D 向量

从 IP 核的基地址开始，在 **偏移地址** 处写入 IP 核上寄存器的一维向量。

**数据类型：** `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

要交互式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上的 **准备** 库中，选择 **属性检查器**。

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

### **设备名称** — IP 核设备的路径和文件名 `/dev/mwipcore`（默认值）| character vector

输入 IP 核设备的路径和文件名。

**注意**

如果您使用 HDL Coder™ 生成 IP 核，则 IP 核会映射到 `/dev/mwipcore`。

#### 编程用法

|  |
| --- |
| **模块参数：** `DeviceName` |
| **默认值：** `/dev/mwipcore` |

### **偏移地址** — 从 IP 核的基地址到寄存器的偏移量 `hex2dec( '0100' )`（默认值）| decimal number

输入从 IP 核的基地址到寄存器的偏移量。模块从该寄存器读取数据。当您使用以 character vector 表示的十六进制数指定偏移地址时，请使用 `hex2dec` 函数。

**注意**

使用 HDL Coder 生成 IP 核时，您可以从 Custom IP Report (HDL Coder) 的 Register Address Mapping 部分获取偏移地址的值。有关详细信息，请参阅 Register Address Mapping (HDL Coder)。

#### 编程用法

|  |
| --- |
| **模块参数：** `RegisterOffset` |
| **默认值：** `hex2dec('0100')` |

## 所属库

Embedded Coder Support Package for Intel SoC Devices

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2014b 中引入**

## 描述

通过 AXI4-Lite 接口将数据写入目标硬件上的 IP 核

使用 AXI4 接口将来自嵌入式处理器的向量数据写入可编程逻辑 IP 核上的一组连续寄存器。AXI4 Write 模块仅支持 AXI4-Lite 协议，从而允许简单、低吞吐量的内存映射通信。此协议的典型用途包括写入控制和状态寄存器。

模块输入信号的采样率控制此模块向寄存器写入数据的频率。
