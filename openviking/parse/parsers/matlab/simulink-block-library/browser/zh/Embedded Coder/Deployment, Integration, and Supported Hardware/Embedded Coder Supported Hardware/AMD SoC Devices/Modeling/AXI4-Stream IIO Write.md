---
type: simulink-block
title: 'AXI4-Stream IIO Write'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / AMD SoC Devices / Modeling'
documentation_page: 'axi4streamiiowrite'
documentation_source_path: 'xilinxzynq7000ec/ref/axi4streamiiowrite.html'
language: zh-CN
chinese_source: worker-translation
---

# AXI4-Stream IIO Write

## 端口

### 输入

### **Data** — 要写入 DMA 缓冲区的数据帧，*N*×1 数组

此端口输出在 DMA 缓冲区传输中写入内存的 *N*×1 向量。在 **Valid** 端口启用之前，此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`
### 输出

### **Valid** — 流写入 IP 核的状态，标量

此端口输出一个验证标志，指示数据是否成功写入 IP 核，其中 `1` 表示成功写入。

#### 依赖关系

要启用此端口，请将 **数据超时 (seconds)** 设置为有限值。

**数据类型：** `Boolean`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条上的 **仿真** 选项卡中，从 **准备** 库中选择 **属性检查器**。

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

### **IIO 设备名称** — IP 核设备的文件名 `mwipcore0:mm2s0`（默认）| character array

以冒号分隔的列表形式输入 FPGA 上 IP 核的名称和通道。如果您使用 HDL Coder™ 生成 IP 核，HDL Coder 会将 IP 核映射到 `mwipcore0` 并使用通道 `mm2s0`。有关获取 IIO 设备名称和通道的详细信息，请参阅提示。

#### 编程用法

|  |
| --- |
| **模块参数：** `devName` |

### **数据超时 (seconds)** — DMA 流读取的超时 `Inf`（默认）| 正标量

指定 DMA 流写入的最大超时延迟。

#### 编程用法

|  |
| --- |
| **模块参数：** `DataTimeout` |

## 所属库

Embedded Coder Support Package for AMD SoC Devices

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**R2018b 中引入**

## 描述

使用 IIO 写入 AXI4-Stream 数据

此模块使用 Industrial I/O (IIO) 库驱动程序将数据写入指定 AXI4-Stream IP 核设备的直接内存访问 (DMA) 缓冲区。AXI4-Stream IIO Write 模块支持从处理器上的模型到 FPGA 上 IP 核的低延迟、高吞吐量数据传输。
