---
type: simulink-block
title: 'Memory IIO Read'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Host I/O'
documentation_page: 'memoryiioread'
documentation_source_path: 'ref/memoryiioread.html'
language: zh-CN
chinese_source: worker-translation
---

# Memory IIO Read

## 端口

### 输出

### **data** — 来自共享内存的数据 标量 | 向量

此端口输出从内存接收的数据向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `ufix128`
### 输入

### **addr** — 读取请求的内存地址偏移 标量 | 向量

内存地址相对于设备上 IP 核基地址的偏移。模块从此地址读取数据。

#### 依赖关系

要启用此端口，请选择 **启用地址偏移端口**。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `ufix128`

## 参数

### **设备名称** — IP 核设备名称 `mwipcore0:sharedmem0:rd0` (默认) | IP 核名称和通道

输入 FPGA 上 IP 核的名称和通道，以冒号分隔的列表。

**注意**

如果您使用 HDL Coder™ 生成 IP 核，HDL Coder 会将 IP 核映射到 `mwipcore0` 并使用通道 `sharedmem0:rd0`。

### **启用地址偏移端口** — 启用地址偏移端口 off (默认) | on

选择此参数以使用来自端口的地址偏移。

- On — **地址偏移**参数被禁用，并创建一个 **addr** 输入端口。
- Off — **地址偏移**参数被启用。

### **地址偏移** — 内存地址相对于 IP 核基地址的偏移 `0` (默认)

输入内存相对于设备上 IP 核基地址的偏移。模块从此地址读取数据。

**注意**

如果使用 HDL Coder 生成 IP 核，可以从 Custom IP Core Report (HDL Coder) 的 “Register Address Mapping” 部分获取地址偏移的值。有关详细信息，请参阅 Register Address Mapping (HDL Coder)。

#### 依赖关系

要启用此参数，请清除 **启用地址偏移端口** 参数。

### **IP 地址** — SoC 设备的网络地址 `192.168.1.101` (默认) | 网络地址

输入已连接 SoC 设备的网络地址。

**示例：** `10.0.0.201`

### **超时** — 内存读取超时 `Inf` (默认) | 正标量

指定内存读取的最大超时延迟。

### **数据类型** — 设备上 IP 核的数据类型 `uint32` (默认) | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32`

选择设备上 IP 核使用的数据类型。

### **输出长度** — 要从内存读取的数据向量大小 `1024` (默认) | 正整数

输入要从内存读取的数据向量大小。

### **采样时间** — 采样时间，以 seconds 为单位 `0.1` (默认) | 正标量

Memory IIO Read 模块输出的信号数据使用 AXI4-Lite 协议直接从 IP 核轮询。**采样时间**参数值或子系统的基本速率指定内存的轮询速率。

### **启用仿真 I/O** — 从板卡读取和写入数据 on (默认) | off

当主机连接到板卡，并且此参数为 on 时，此模块直接从板卡读取数据。在仿真环境中使用此参数时，清除该参数可在没有 IIO 连接的情况下启用仿真而不出错。清除该参数后，**data** 输出端口显示的数据不会反映实际数据。

## 所属库

SoC Blockset Support Package for AMD FPGA and SoC Devices / Common / Host I/O

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2023a 中引入**

## 描述

从共享内存区域读取到仿真模型

Memory IIO Read 模块执行从连接的 Xilinx® SoC 设备中的 DDR 内存到主机上正在运行的 Simulink® 模型的随机访问读取事务。此模块可在您的仿真模型与 SoC 设备上的 DDR 内存之间实现低延迟、高吞吐量的数据传输。

Memory IIO Read 模块将数据从 SoC 设备上的 DDR 内存接收到主机。此模块使用 Industrial I/O (IIO) 库驱动程序在 SoC 设备和客户端主机上创建网络服务器守护进程，以将数据传递到运行模型仿真部分的主机。此图显示 FPGA、DDR 内存以及到正在运行的 Simulink 模型的通信桥之间的连接。

Memory IIO Read 图
