---
type: simulink-block
title: 'Register Write'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory / Processor Software Connectivity'
documentation_page: 'registerwrite'
documentation_source_path: 'ref/registerwrite.html'
language: zh-CN
chinese_source: worker-translation
---

# Register Write

## 端口

### 输入

### **data** — 数据输入向量

此端口接收要写入 IP 核上寄存器的数据向量，从 IP 核基地址的 **Offset address** 开始。

**数据类型：** `single` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point`

### 输出

### **msg** — 输出寄存器数据消息标量

此消息端口将输出寄存器数据作为消息发送到连接的 Register Channel 或 IO Data Sink 模块。有关消息的详细信息，请参阅 Messages。

**数据类型：** `SoCData`

## 参数

### **Output sink** — 将输出定向到端口或基础工作区 `To output port`（默认） | `Base workspace` | `IP core register`

选择 `To output port` 将数据写入输出端口 `msg`。选择 `Base workspace` 将数据写入基础工作区中的变量。写入基础工作区时，模块会更新基础工作区中名称由 `Simulink.Parameter object name` 参数设置的 `Simulink.Parameter` 对象的值。选择 `IP core register` 写入具有相同 `Register name` 参数的 IP Core Register Read 模块。

**注意**

将 Register Write 模块放在 Initialize Function 模块子系统内，会在仿真开始时写入 `Simulink.Parameter` 对象。FPGA 参考模型中表示为 Constant 模块的寄存器，可以在仿真开始时用 `Simulink.Parameter` 对象的值进行初始化。这种写入 FPGA 寄存器的方法要求在整个仿真期间保持常量值，但可以减少 SoC 模型所需的仿真时间。

### **Simulink.Parameter object name** — `Simulink.Parameter` 对象的名称 `A`（默认） | 字符向量

要在 `Base workspace` 中创建的 `Simulink.Parameter` 对象的名称。

**示例：** `A`

#### 依赖关系

要启用此参数，请将 `Output sink` 设置为 `Base workspace`。

### **Register name** — IP Core 中寄存器的名称 `RegA`（默认） | 字符向量

FPGA 参考模型中 IP Core Register Read 模块中定义的寄存器名称。

**示例：** `RegA`

#### 依赖关系

要启用此参数，请将 `Output sink` 设置为 `IP core register`。

### **Device name** — IP 核设备的路径和文件名 `/dev/mwipcore`（默认） | 字符数组

输入 IP 核设备的路径和文件名。

### **Offset address** — 从 IP 核基地址到寄存器的偏移量 `hex2dec('0100')`（默认） | 正整数

输入从 IP 核基地址到寄存器的偏移量。该模块将数据写入此寄存器。当使用以字符向量表示的十六进制数指定偏移地址时，请使用 `hex2dec` 函数。可以使用 Hardware Mapping 工具选择偏移地址。

## 所属库

SoC Blockset / Processor I/O

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

若要为您的设计自动生成 C 代码，并在 SoC 设备上执行，请使用 SoC Builder 工具。若要为 SoC 模型生成并执行 C 代码，需要 Embedded Coder® 功能。有关为 SoC 设计生成代码的详细信息，请参阅 Use SoC Builder to Generate SoC Design。

SoC Builder 使用采用 AXI4 接口协议的 FPGA 和处理器 IP 实现 Register Write 模块。AXI4 接口协议允许处理器将来自处理器的向量数据写入 FPGA 上的一组连续寄存器。此模块可用于简单、低吞吐量的内存映射通信，例如写入控制和状态寄存器。此图显示了生成代码实现的通用表示。

## 版本历史

**在 R2019a 中引入**

## 描述

将数据写入指定 IP 核上的寄存器区域

Register Write 模块将来自处理器算法的数据写入指定 IP 核上的寄存器区域。在仿真中，定时器驱动或事件驱动的任务子系统包含 Register Write 模块。来自 Register Write 模块的数据信号连接到管理这些寄存器及其事务的 Register Channel 模块。

在开发或分析 SoC 应用的软件侧时，可以将 Register Write 模块连接到 IO Data Sink 模块。在此配置中，IO Data Sink 模块提供先前记录的数据或人工数据，从而能够更有针对性地仿真应用的软件和处理器侧，而无需显式建模硬件和内存交互。
