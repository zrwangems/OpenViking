---
type: simulink-block
title: 'Video Stream Connector'
family: 'hardware-logic-connectivity'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Hardware Logic Connectivity'
documentation_page: 'videostreamconnector'
documentation_source_path: 'ref/videostreamconnector.html'
language: zh-CN
chinese_source: worker-translation
---

# Video Stream Connector

## 端口

### 输入

### **wrData** — 输入视频数据标量

来自数据源的输入视频数据。将此值指定为标量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **wrCtrlIn** — 伴随像素流的输入控制信号 `pixelControl` 总线

伴随像素流的控制信号，指定为包含五个信号的 `pixelcontrol` 总线。这些信号描述像素的有效性及其在帧中的位置。有关 `pixelcontrol` 总线类型的其他信息，请参阅 AXI4-Stream Video Interface。

**数据类型：** `pixelcontrol`

### **rdCtrlIn** — 来自下游接口的就绪信号 boolean 标量

控制信号，指示该模块是否可以将视频数据发送到下游接口。当此值为 (true) 时，下游模块已准备好接收数据。

### 输出

### **rdData** — 输出视频数据标量

将视频数据输出到下游目标 IP。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **rdCtrlOut** — 伴随输出像素流的输出控制信号 `pixelcontrol` 总线

伴随输出视频数据的控制信号，指定为包含五个信号的 `pixelcontrol` 总线。这些信号描述像素的有效性及其在帧中的位置。

**数据类型：** `pixelcontrol`

### **wrCtrlOut** — 到上游接口的就绪信号 boolean 标量

控制信号，指示该模块可以从上游接口接收流数据。

**数据类型：** `Boolean`

## 参数

R2025b 中未记录。

## 所属库

SoC Blockset / Hardware Logic Connectivity

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要自动为您的设计生成 HDL 代码，并在 SoC 设备上执行，请使用 **SoC Builder** 工具。请参阅 Use SoC Builder to Generate SoC Design。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2019a 中引入**

## 描述

连接两个具有视频流接口的 IP

Stream Connector 模块连接两个具有视频流接口的 IP。在 SoC 应用的 FPGA 模型中使用此模块来连接两个 IP。
