---
type: simulink-block
title: 'Memory IIO Write'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Host I/O'
documentation_page: 'memoryiiowrite'
documentation_source_path: 'ref/memoryiiowrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Memory IIO Write

## 端口

### 输入

### **data** — 写入共享内存的数据 标量 | 向量

此端口接收其写入内存的数据向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `ufix128`

### **addr** — 写请求的内存地址偏移量 标量 | 向量

内存地址相对于设备上 IP 核基地址的偏移量。模块将数据写入此地址。

#### 依赖关系

要启用此端口，请选择 **Enable address offset port**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `ufix128`

## 参数

### **Device name** — IP 核设备名称 `mwipcore0:sharedmem0:wr0` (默认) | IP 核名称和通道

以冒号分隔的列表形式输入 FPGA 上 IP 核的名称和通道。

**注意**

如果您使用 HDL Coder™ 生成 IP 核，HDL Coder 会将 IP 核映射到 `mwipcore0`，并使用通道 `sharedmem0:wr0`。

### **Enable address offset port** — 启用地址偏移端口 off (默认) | on

选择此参数以使用来自端口的地址偏移。

- On — **Address offset** 参数被禁用，并且会创建一个 **addr** 输入端口。
- Off — **Address offset** 参数被启用。

### **Address offset** — 内存地址相对于 IP 核基地址的偏移量 `0` (默认)

输入内存相对于设备上 IP 核基地址的偏移量。模块从此地址读取数据。

**注意**

如果使用 HDL Coder 生成 IP 核，可以从 Custom IP Core Report (HDL Coder) 的 “Register Address Mapping” 部分获取地址偏移量的值。有关更多信息，请参阅 Register Address Mapping (HDL Coder)。

#### 依赖关系

要启用此参数，请清除 **Enable address offset port** 参数。

### **IP address** — SoC 设备的网络地址 `192.168.1.101` (默认) | 网络地址

输入已连接 SoC 设备的网络地址。

**示例：** `10.0.0.201`

### **Timeout** — 内存写入超时 `Inf` (默认) | 正标量

指定内存写入的最大超时延迟。

### **Enable simulation I/O** — 从板卡读取和写入数据 on (默认) | off

当主机连接到板卡且此参数为 on 时，此模块直接将数据写入板卡。在仿真环境中使用此参数时，请清除此参数以启用仿真，而不会因缺少 IIO 连接而出错。清除此参数后，**data** 输出端口显示的数据不反映实际数据。

## 所属库

SoC Blockset Support Package for AMD FPGA and SoC Devices / Common / Host I/O

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**R2023a 中引入**

## 描述

从仿真模型写入共享内存区域

Memory IIO Write 模块从主机上运行的 Simulink® 模型向已连接的 Xilinx® SoC 设备中的 DDR 内存执行随机访问写事务。此模块可在您的仿真模型与 SoC 设备上的 DDR 内存之间实现低延迟、高吞吐量数据传输。

Memory IIO Write 模块从主机向 SoC 设备上的 DDR 内存发送数据。此模块使用 Industrial I/O (IIO) 库驱动程序在 SoC 设备和客户端主机上创建网络服务器守护进程，以从运行模型仿真部分的主机传递数据。此图显示了 FPGA、DDR 内存以及与 Simulink 模型之间的通信桥接连接。

Memory IIO Write 示意图
