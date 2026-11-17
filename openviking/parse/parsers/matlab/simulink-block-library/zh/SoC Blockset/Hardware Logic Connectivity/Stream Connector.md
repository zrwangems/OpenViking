---
type: simulink-block
title: 'Stream Connector'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Hardware Logic Connectivity'
documentation_page: 'streamconnector'
documentation_source_path: 'ref/streamconnector.html'
language: zh-CN
chinese_source: worker-translation
---

# Stream Connector

## 端口

### 输入

### **wrData** — 输入流数据标量

来自数据源的输入流数据。将此值指定为标量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **wrValid** — 有效输入流数据指示 布尔标量

控制信号，指示来自数据源的输入数据是否有效。
当此值为 (true) 时，模块接受 **wrData**
端口上的值。当此值为 (false) 时，模块忽略
**wrData** 端口上的值。

**数据类型：** `Boolean`

### **wrLast** — 突发中最后一拍指示 布尔标量

控制信号，指示来自上游 IP 的数据的最后一拍。

**数据类型：** `Boolean`

### **rdReady** — 来自下游接口的就绪信号 布尔标量

控制信号，指示模块是否可以将流数据发送到下游
接口。当此值为 (true) 时，下游模块已准备好接收
数据。

**数据类型：** `Boolean`
### 输出

### **rdData** — 输出流数据标量

输出到下游目标 IP 的流数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **rdValid** — 有效输出流数据指示 布尔标量

控制信号，指示输出流数据是否有效。

**数据类型：** `Boolean`

### **rdLast** — 指示突发中最后一拍 布尔标量

控制信号，指示输出流数据现在具有突发数据的最后一拍。

**数据类型：** `Boolean`

### **wrReady** — 到上游接口的就绪信号 布尔标量

控制信号，指示模块是否可以从上游接口接收流数据。

**数据类型：** `Boolean`

## 参数

R2025b 中未记录。

## 所属库

SoC Blockset / Hardware Logic Connectivity

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要为您的设计自动生成 HDL 代码，并在 SoC 设备上执行，
请使用 **SoC Builder** 工具。请参阅 Use SoC Builder to Generate SoC Design。

使用 SoC Blockset™，您可以在模型中建模简化的流协议。使用 HDL Coder™ 在 IP 核中生成 AXI4-Stream 接口。有关
AXI4-stream 协议的更多信息，请参阅 AXI4-Stream Interface。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2019a 中引入**

## 描述

连接两个具有数据流接口的 IP

Stream Connector 模块连接两个具有数据流接口的 IP。
在 SoC 应用的 FPGA 模型中使用此模块来连接两个 IP。
