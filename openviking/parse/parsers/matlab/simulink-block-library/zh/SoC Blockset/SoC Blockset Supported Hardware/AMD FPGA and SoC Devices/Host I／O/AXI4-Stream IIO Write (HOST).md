---
type: simulink-block
title: 'AXI4-Stream IIO Write (HOST)'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Host I/O'
documentation_page: 'axi4streamiiowritehost'
documentation_source_path: 'ref/axi4streamiiowritehost.html'
language: zh-CN
chinese_source: worker-translation
---

# AXI4-Stream IIO Write (HOST)

## 端口

### 输入

### **data** — 传输到 DMA 缓冲区的数据帧向量

此端口接收一个 *N*×1 向量，并通过 DMA 缓冲区传输写入 DDR 中的内存。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixdt(0,128,0)`

### 输出

### **status** — SoC 设备中流写入 IP 核的状态标量

此端口输出一个验证标志，指示数据已成功写入 SoC 设备中的 IP 核。值 `1` 表示写入成功。

#### 依赖项

要启用此端口，请将 **Data timeout (seconds)** 参数设置为有限值。

**数据类型：** `Boolean`

## 参数

### **Device name** — IP 核设备名称 `mwipcore0:mm2s0` (default) | IP 核名称和通道

输入 FPGA 上 IP 核的名称和通道，以冒号分隔的列表形式。

**注意**

如果使用 HDL Coder 生成 IP 核，HDL Coder 会将 IP 核映射到 `mwipcore0` 并使用通道
`s2mm0`。

### **Remote IP address** — SoC 设备的网络地址 `192.168.1.101` (default) | 有效的 URI 字符串

输入所连接 SoC 设备的网络地址。

**示例：** `10.0.0.201`

### **Data timeout (seconds)** — DMA 流写入的超时 `Inf` (default) | 正标量

指定 DMA 流写入的最大超时延迟。

### **Enable simulation I/O** — 从板卡读取和写入数据 on (default) | off

当连接到板卡时，此模块将数据直接写入板卡。在仿真环境中使用时，清除此参数以启用仿真，而不会因缺少 IIO 连接而出错。清除后，**data** 输出端口中显示的数据不反映实际数据。

## 所属库

SoC Blockset Support Package for AMD FPGA and SoC Devices / Common / Host I/O

## 模块特性

未在 R2025b 中记录。

## 扩展功能

未在 R2025b 中记录。

## 版本历史

**在 R2020b 中引入**

## 描述

从仿真模型将数组写入 IP 核设备的 DDR 内存缓冲区。

AXI4-Stream IIO Write (HOST) 模块从正在运行的 Simulink® 模型将数据写入所连接的 Xilinx® SoC 设备上指定 AXI4-Stream IP 核设备的直接内存访问 (DMA) 缓冲区。此模块可在您的仿真模型与 SoC 设备上的 IP 核之间实现低延迟高吞吐量数据传输。

AXI4-Stream IIO Write (HOST) 模块将主机计算机上的数据发送到 SoC 设备上的 DDR 内存缓冲区。此模块使用 Industrial I/O (IIO) 库驱动程序，在 SoC 设备上创建网络服务器守护进程，并在客户端主机计算机上创建客户端，以将缓冲区数据副本传递给运行模型仿真部分的主机计算机。此图显示了 HDL Coder™ 生成的 IP 核、DDR 内存缓冲区和到正在运行的 Simulink 模型的通信桥之间的连接。

AXI4-Stream IIO Write (HOST) 图
