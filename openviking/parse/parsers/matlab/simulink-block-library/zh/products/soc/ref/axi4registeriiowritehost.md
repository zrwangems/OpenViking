---
type: simulink-block
title: 'AXI4-Register IIO Write (HOST)'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Host I/O'
documentation_page: 'axi4registeriiowritehost'
documentation_source_path: 'ref/axi4registeriiowritehost.html'
language: zh-CN
chinese_source: worker-translation
---

# AXI4-Register IIO Write (HOST)

## 端口

### 输入

### **data** — 要写入 DMA 缓冲区的数据帧向量

此端口接受一个 *N*×1 向量，该向量在 DMA 缓冲区传输中被写入内存。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `ufix64` | `ufix128`

## 参数

### **设备名称** — IP 核设备的文件名 `mwipcore0:mmwr0`（默认）

以冒号分隔的列表形式输入 FPGA 上 IP 核设备的名称和通道。如果使用 HDL Coder 生成 IP 核，HDL Coder 会将 IP 核映射到 `mwipcore0`，并使用通道 `mm2s0`。

### **地址偏移** — 寄存器相对 IP 核基地址的偏移 `hex2dec('0100')`（默认）

输入设备上寄存器相对 IP 核基地址的偏移。模块将数据写入此寄存器。当使用十六进制数字字符向量指定地址偏移时，请使用 `hex2dec` 函数。

**注意**

如果使用 HDL Coder 生成 IP 核，可以从 Custom IP Core Report (HDL Coder) 的“寄存器地址映射”部分获取地址偏移值。有关详细信息，请参阅“寄存器地址映射 (HDL Coder)”。

### **远程 IP 地址** — SoC 设备的网络地址 `192.168.1.101`（默认）| 有效 URI 字符串

输入所连接 SoC 设备的网络地址。

**示例：** `10.0.0.201`

### **启用仿真 I/O** — 从板读取和写入数据 on（默认）| off

连接到板时，此模块会直接将数据写入板。在仿真环境中使用时，清除此参数可启用仿真，而不会因缺少 IIO 连接而报错。清除后，**data** 输出端口中显示的数据不反映实际数据。

## 所属库

SoC Blockset Support Package for AMD FPGA and SoC Devices / Common / Host I/O

## 模块特性

R2025b 中未记录。

## 扩展功能

R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

## 描述

从仿真模型向存储器映射寄存器写入数据

AXI4-Register IIO Write (HOST) 模块从主机计算机上运行的 Simulink® 模型向所连接 Xilinx® SoC 设备可编程逻辑中的存储器映射寄存器写入数据。此模块可在仿真模型与 SoC 设备上的 FPGA 寄存器之间实现低延迟高吞吐量数据传输。

AXI4-Stream IIO Write (HOST) 模块将主机计算机上的数据发送到 SoC 设备上 IP 核中的寄存器。此模块使用 Industrial I/O (IIO) 库驱动程序在 SoC 设备和主机计算机上创建网络服务器守护进程，以在运行模型仿真部分的主机计算机与 SoC 设备之间传递数据。此图显示了 HDL Coder™ 生成的 IP 核、存储器映射寄存器以及到正在运行的 Simulink 模型的通信桥之间的连接。

AXI4-Register IIO Write (HOST) 图
