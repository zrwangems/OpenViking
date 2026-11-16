---
type: simulink-block
title: 'AXI4-Stream IIO Read (HOST)'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Host I/O'
documentation_page: 'axi4streamiioreadhost'
documentation_source_path: 'ref/axi4streamiioreadhost.html'
language: zh-CN
chinese_source: worker-translation
---

# AXI4-Stream IIO Read (HOST)

## 端口

### 输出

### **data** — 来自 DMA 缓冲区的数据帧向量

此端口输出从 DMA 缓冲区传输接收到的 *N*×1 向量。使用 **Frame size** 参数设置每次 DMA 传输读取的样本数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `ufix128`

### **valid** — 来自 DMA 缓冲区的有效数据帧标量

一个标志，指示从内存通道读取的有效数据帧。

#### 依赖关系

要启用此端口，请将 **Timeout (sec)** 参数设置为有限值。

**数据类型：** `Boolean`

## 参数

### **Device name** — IP 核设备的名称 `mwipcore0:s2mm0` (默认) | IP 核名称和通道

以冒号分隔的列表形式输入 FPGA 上 IP 核的名称和通道。

**注意**

如果您使用 HDL Coder 生成 IP 核，HDL Coder 会将 IP 核映射到 `mwipcore0` 并使用通道 `s2mm0`。

### **Remote IP address** — SoC 设备的网络地址 `192.168.1.101` (默认) | 有效 URI 字符串

输入所连接 SoC 设备的网络地址。

**示例：** `10.0.0.201`

### **Timeout (sec)** — DMA 流读取的超时 `Inf` (默认) | 正标量

指定 DMA 流读取的最大超时延迟。

### **Output data type** — 设备上 IP 核的数据类型 `uint32` (默认) | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(0,128,0)`

选择设备上 IP 核使用的数据类型。

### **Frame size** — 要从 IP 核读取的数据向量大小 `1024` (默认) | 正整数

输入要从 IP 核设备读取的数据向量大小。

### **Sample time** — 采样时间，以秒为单位 `0.1` (默认) | 正标量

AXI4-Stream IIO Read 模块输出的信号数据使用 AXI4-Stream 协议从 DMA 缓冲区进行轮询。子系统的 **Sample time** 或基础速率指定 DMA 缓冲区的轮询速率。

### **Enable simulation I/O** — 从板卡读取和写入数据 on (默认) | off

当连接到板卡时，此模块直接将数据写入板卡。在仿真环境中使用时，清除此参数可启用仿真，而不会因缺少 IIO 连接而出错。清除后，**data** 输出端口中显示的数据不反映实际数据。

## 所属库

SoC Blockset Support Package for AMD FPGA and SoC Devices / Common / Host I/O

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

## 描述

从 IP 核设备读取 DDR 内存缓冲区到仿真模型

AXI4-Stream IIO Read (HOST) 模块将数据从已连接的 Xilinx® SoC 设备上指定 AXI4-Stream IP 核设备的直接内存访问 (DMA) 缓冲区读取到正在运行的 Simulink® 模型中。此模块可在您的仿真模型与 SoC 设备上的 IP 核之间实现低延迟、高吞吐量的数据传输。

AXI4-Stream IIO Read (HOST) 模块在主机上接收来自 SoC 设备的 DDR 内存缓冲区副本。此模块使用 Industrial I/O (IIO) 库驱动程序在 SoC 设备上创建网络服务器守护进程，并在客户端主机上创建客户端，以将缓冲区数据副本传递到运行模型仿真部分的主机。此图显示了 HDL Coder™ 生成的 IP 核、DDR 内存缓冲区以及到正在运行的 Simulink 模型的通信桥之间的连接。

AXI4-Stream IIO Read 图
