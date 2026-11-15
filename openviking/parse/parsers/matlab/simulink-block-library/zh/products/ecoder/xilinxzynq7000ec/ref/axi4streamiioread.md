---
type: simulink-block
title: 'AXI4-Stream IIO Read'
family: 'ecoder'
product_id: 'ecoder'
product_name: 'Embedded Coder'
documentation_release: R2025b
official_category: 'Deployment, Integration, and Supported Hardware / Embedded Coder Supported Hardware / AMD SoC Devices / Modeling'
documentation_page: 'axi4streamiioread'
documentation_source_path: 'xilinxzynq7000ec/ref/axi4streamiioread.html'
language: zh-CN
chinese_source: worker-translation
---

# AXI4-Stream IIO Read

## 端口

### 输出

### **Data** — 来自 DMA 缓冲区的数据帧 *N*-by-1 向量

此端口输出从 DMA 缓冲区传输接收到的 *N*-by-1 向量。使用 **帧大小** 参数确定每次 DMA 传输读取的样本数。在启用 **Valid** 端口之前，此端口未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64`

### **Valid** — 来自 IP 核的流读取状态 `Boolean` 值

此端口输出一个验证标志，指示从 IP 核成功读取数据，其中 `1` 表示成功读取。

#### 依赖关系

要启用此端口，请将 **数据超时 (seconds)** 设置为有限值。

**数据类型：** `Boolean`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

要以编程方式设置模块参数值，请使用 `set_param` 函数。

要以编程方式获取模块参数值，请使用 `get_param` 函数。

### **IIO 设备名称** — IP 核设备的文件名 `mwipcore0:s2mm0`（默认）| 字符数组

以冒号分隔的列表形式输入 FPGA 上 IP 核的名称和通道。如果您使用 HDL Coder™ 生成 IP 核，HDL Coder 会将 IP 核映射到 `mwipcore0` 并使用通道 `s2mm0`。有关获取 IIO 设备名称和通道的详细信息，请参阅提示。

#### 编程用法

|  |
| --- |
| **模块参数：** `devName` |

### **帧大小** — 要从 IP 核读取的数据向量大小 `1024`（默认）| 正整数

输入要从 IP 核设备读取的数据向量大小。

#### 编程用法

|  |
| --- |
| **模块参数：** `SamplesPerFrame` |

### **数据类型** — IP 核的数据类型 `uint32`（默认）| `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32`

选择 IP 核使用的数据类型。

#### 编程用法

|  |
| --- |
| **模块参数：** `dataTypeStr` |

### **采样时间** — 以 seconds 为单位的采样时间 `0.1`（默认）| 正标量

AXI4-Stream IIO Read 模块输出的信号数据使用 AXI4-Stream 协议从 DMA 缓冲区轮询。**采样时间** 或子系统的基本速率指定 DMA 缓冲区的轮询速率。

#### 编程用法

|  |
| --- |
| **模块参数：** `SampleTime` |

### **数据超时 (seconds)** — DMA 流读取的超时 `Inf`（默认）| 正标量

指定 DMA 流读取的最大超时延迟。

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

**在 R2018b 中引入**

## 描述

使用 IIO 读取 AXI4-Stream 数据

此模块使用 Industrial I/O (IIO) 库驱动程序从指定的 AXI4-Stream IP 核设备的直接内存访问 (DMA) 缓冲区读取数据。AXI4-Stream IIO Read 模块使您能够在部署于处理器上的模型与 FPGA 上的 IP 核之间实现低延迟、高吞吐量的数据传输。
