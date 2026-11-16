---
type: simulink-block
title: 'Register Read'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory / Processor Software Connectivity'
documentation_page: 'registerread'
documentation_source_path: 'ref/registerread.html'
language: zh-CN
chinese_source: worker-translation
---

# Register Read

## 端口

### 输入

### **msg** — 来自寄存器标量的数据消息

此消息端口从已连接的 Register Channel 或 IO Data Source 模块接收数据消息。当 Task Manager 模块触发包含 Register Read 模块的任务时，这些消息会进行处理。有关消息的详细信息，请参阅 Messages。

**数据类型：** `SoCData`

### 输出

### **data** — 输出信号向量

此端口发出从 Register Channel 中指定寄存器读取的数据向量，起始位置为从 IP 核基地址开始的 **Offset address**。

**数据类型：** `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

## 参数

### **Device name** — IP 核设备的路径和文件名 `/dev/mwipcore`（默认）| character array

输入 IP 核设备的路径和文件名。

### **Offset address** — 从 IP 核基地址到寄存器的偏移 `hex2dec('0100')`（默认）| 正整数

输入从 IP 核基地址到寄存器的偏移。该模块从此寄存器读取数据。当使用以 character vector 表示的十六进制数指定偏移地址时，请使用 `hex2dec` 函数。可以使用 Hardware Mapping 工具选择偏移地址。

### **Output data type** — IP 核使用的数据类型 uint32（默认）| single | int8 | uint8 | int16 | int32 | uint32 | boolean | fixed-point

输入 IP 核使用的数据类型。

### **Output vector size** — 来自 IP 核的数据向量大小 `1`（默认）| 正整数

输入从 IP 核设备读取的数据向量大小。

### **Sample time** — 采样时间 `0.1`（默认）| 正数

输入采样时间，单位为 seconds。当此模块在定时器驱动任务中使用时，已连接的 Register Channel 或 IO Data Source 模块将按此速率轮询。

## 所属库

SoC Blockset / Processor I/O

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

要为您的设计自动生成 C 代码并在 SoC 设备上执行，请使用 SoC Builder 工具。要为您的 SoC 模型生成并执行 C 代码，需要 Embedded Coder® 功能。有关为 SoC 设计生成代码的详细信息，请参阅 Use SoC Builder to Generate SoC Design。

SoC Builder 使用 FPGA 和处理器 IP 实现 Register Read 模块，这些 IP 使用 AXI4 接口协议。AXI4 接口协议允许处理器算法从 FPGA 上的连续寄存器组读取向量数据。此模块适用于简单、低吞吐量的内存映射通信，例如从控制和状态寄存器读取。此图显示了所生成代码实现的概括表示。

## 版本历史

**在 R2019a 中引入**

## 描述

从指定 IP 核上的寄存器区域读取数据

Register Read 模块从指定 IP 核上的寄存器区域读取数据。在仿真中，定时器驱动或事件驱动的任务子系统包含 Register Read 模块。来自 Register Read 模块的数据信号连接到管理这些寄存器及其事务的 Register Channel 模块。

在开发或分析 SoC 应用的软件侧时，可以将 Register Read 模块连接到 IO Data Source 模块。在此配置中，IO Data Source 模块提供先前记录的或人工的数据，从而能够更有针对性地仿真应用的软件和处理器侧，而无需显式对硬件和内存交互进行建模。
