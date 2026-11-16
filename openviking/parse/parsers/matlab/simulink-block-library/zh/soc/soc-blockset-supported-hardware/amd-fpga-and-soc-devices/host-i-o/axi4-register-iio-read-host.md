---
type: simulink-block
title: 'AXI4-Register IIO Read (HOST)'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'SoC Blockset Supported Hardware / AMD FPGA and SoC Devices / Host I/O'
documentation_page: 'axi4registeriioreadhost'
documentation_source_path: 'ref/axi4registeriioreadhost.html'
language: zh-CN
chinese_source: worker-translation
---

# AXI4-Register IIO Read (HOST)

## 端口

### 输出

### **data** — 来自 IP 核寄存器的数据向量

此模块输出从 IP 核上的内存映射寄存器读取的 *N*×1 向量，从 **Register offset** 开始。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### **Device name** — IP 核设备的路径和名称 `mwipcore0:mmrd0`（默认）

输入 IP 核的路径和名称。

**注意**

如果使用 HDL Coder™ 生成 IP 核，HDL Coder 会将 IP 核映射到 `mwipcore0:mmrd0`。

### **Address offset** — 寄存器相对于 IP 核基地址的偏移量 `hex2dec('0100')`（默认）

输入寄存器相对于设备上 IP 核基地址的偏移量。此模块从该寄存器读取数据。当使用十六进制数字字符向量指定地址偏移量时，请使用 `hex2dec` 函数。

**注意**

如果使用 HDL Coder 生成 IP 核，可以从 Custom IP Core Report (HDL Coder) 的 “Register Address Mapping” 部分获取地址偏移量的值。有关详细信息，请参阅 Register Address Mapping (HDL Coder)。

### **Remote IP address** — SoC 设备的网络地址 `192.168.1.101`（默认）| 网络地址

输入已连接 SoC 设备的网络地址。

**示例：** `10.0.0.201`

### **Timeout (sec)** — 寄存器读取超时 `Inf`（默认）| 正标量

指定寄存器读取的最大超时延迟。

### **Output data type** — 设备上 IP 核的数据类型 `uint32`（默认）| `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `boolean`

选择设备上 IP 核使用的数据类型。

### **Sample time** — 采样时间，单位为 seconds `0.001`（默认）| 正标量

AXI4-Register IIO Read (HOST) 模块输出的信号数据使用 AXI4-Lite 协议直接从 IP 核轮询。**Sample time** 参数值或子系统的基速率指定寄存器的轮询速率。

### **Enable simulation I/O** — 从板卡读取和写入数据 on（默认）| off

当连接到板卡时，此模块会直接将数据写入板卡。在仿真环境中使用时，清除此参数可在没有 IIO 连接的情况下进行仿真而不出错。清除后，**data** 输出端口中显示的数据不反映实际数据。

## 所属库

SoC Blockset Support Package for AMD FPGA and SoC Devices / Common / Host I/O

## 模块特性

在 R2025b 中未记录。

## 扩展功能

在 R2025b 中未记录。

## 版本历史

**在 R2020b 中引入**

## 描述

将内存映射寄存器读入仿真模型

AXI4-Register IIO Read (HOST) 模块从已连接 Xilinx® SoC 设备的可编程逻辑中的内存映射寄存器读取值，并将其传输到主机计算机上正在运行的 Simulink® 模型。此模块可在仿真模型与 SoC 设备上的 FPGA 寄存器之间实现低延迟、高吞吐量数据传输。

AXI4-Register IIO Read (HOST) 模块在主机计算机上接收来自 SoC 设备中可编程逻辑的内存映射寄存器副本。此模块使用 Industrial I/O (IIO) 库驱动程序在 SoC 设备上创建网络服务器守护进程，并在主机计算机上创建客户端，以将寄存器数据副本传递到运行模型仿真部分的主机计算机。此图显示了内存映射寄存器、中央互连以及到正在运行的 Simulink 模型的通信桥接之间的连接。

AXI4-Register IIO Read (HOST) 图
