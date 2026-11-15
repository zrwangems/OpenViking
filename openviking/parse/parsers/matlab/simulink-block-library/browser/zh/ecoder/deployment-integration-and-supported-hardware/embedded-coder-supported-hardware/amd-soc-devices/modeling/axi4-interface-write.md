---
type: simulink-block
title: 'AXI4-Interface Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / AMD SoC Devices / Modeling'
documentation_page: 'axi4interfacewrite'
documentation_source_path: 'xilinxzynq7000ec/ref/axi4interfacewrite.html'
language: zh-CN
chinese_source: worker-translation
---

# AXI4-Interface Write

## 端口

### 输入

### **Port\_1** — IP 核寄存器的输入信号 *N*-by-1 向量

指定写入 IP 核上存储器映射寄存器的 *N*-by-1 向量，起始位置为 **寄存器偏移量**。

**数据类型:** `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条中，于 **仿真** 选项卡的 **准备** 库中，选择 **属性检查器**。

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

### **设备名称** — IP 核设备的路径和名称 `/dev/mwipcore` (默认) | character array

输入 IP 核的路径和名称。

**注意**

如果使用 HDL Coder 生成 IP 核，HDL Coder 会将 IP 核映射到 `/dev/mwipcore`。

#### 编程用法

|  |
| --- |
| **模块参数:** `DeviceName` |

### **寄存器偏移量** — 寄存器相对于 IP 核基地址的偏移量 `hex2dec( '010C' )` (默认) | decimal number character array

输入寄存器相对于 IP 核基地址的偏移量。该模块将数据写入此寄存器。当使用十六进制数字 character vector 指定地址偏移量时，将该值表示为 `hex2dec` 函数内的参数。

**注意**

如果使用 HDL Coder 生成 IP 核，可以从自定义 IP 核报告 (HDL Coder) 的“寄存器地址映射”部分获取地址偏移量的值。有关详细信息，请参阅寄存器地址映射 (HDL Coder)。

#### 编程用法

|  |
| --- |
| **模块参数:** `RegisterOffset` |

## 所属库

Embedded Coder Support Package for AMD SoC Devices

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2013a 中引入**

## 描述

在 AMD SoC 设备上向 IP 核写入数据

此模块将数据向量写入 HDL Coder™ 生成的 IP 核上的一组连续存储器映射寄存器。AXI4-Interface Write 模块使用处理系统的中央互连，提供与 FPGA 上 IP 核的简单存储器映射通信。此模块最适合低吞吐量通信，例如设置状态、状态或控制寄存器。此图显示数据离开此模块后的路径。
