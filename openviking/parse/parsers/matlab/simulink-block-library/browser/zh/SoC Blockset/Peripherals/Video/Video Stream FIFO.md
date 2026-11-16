---
type: simulink-block
title: 'Video Stream FIFO'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory / Video Stream Connectivity'
documentation_page: 'videostreamfifo'
documentation_source_path: 'ref/videostreamfifo.html'
language: zh-CN
chinese_source: worker-translation
---

# Video Stream FIFO

## 端口

### 输入

### **pixelIn** — 输入像素数据标量

来自数据源的输入像素数据。将此值指定为标量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **ctrlIn** — 伴随输入像素数据的控制信号 `pixelcontrol` 总线

伴随像素流的控制信号，指定为包含五个信号的 `pixelcontrol` 总线。这些信号描述像素的有效性及其在帧中的位置。

**数据类型：** `pixelcontrol`

### **rdyFromDown** — 来自下游接口的就绪信号 `Boolean` 标量

控制信号，指示该模块是否可以将像素数据发送到下游接口。当此值为 `1`（true）时，下游接口已就绪，该模块可以发送像素数据。当此值为 `0`（false）时，下游接口未就绪，该模块无法发送像素数据。

**数据类型：** `Boolean`

### 输出

### **pixelOut** — 输出像素数据标量

向下游接口输出像素数据。此输出数据的数据类型与输入数据的数据类型相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **ctrlOut** — 伴随输出像素数据的控制信号 `pixelcontrol` 总线

伴随输出像素流的控制信号，返回为包含五个信号的 `pixelcontrol` 总线。这些信号描述像素的有效性及其在帧中的位置。

**数据类型：** `pixelcontrol`

### **rdyToUp** — 到上游接口的就绪信号 `Boolean` 标量

控制信号，指示该模块是否已准备好从上游接口接收像素数据。当此值为 `1`（true）时，该模块已准备好接受来自上游接口的像素数据。当此值为 `0`（false）时，该模块未准备好接受来自上游接口的像素数据。

**数据类型：** `Boolean`

## 参数

### **Depth of FIFO** — FIFO 深度 `16`（默认） | positive integer

指定 FIFO 的深度。此值必须为正标量整数，并且是在数据被丢弃之前可以缓冲的最大条目数。

### **Almost full threshold** — 几乎满阈值 `8`（默认） | positive integer

指定一个值，用于置位从该模块到数据源的反压信号。

为避免丢弃数据，请设置一个能让数据源有足够时间对反压做出响应的值。此值必须是正整数，并且小于 FIFO 深度。

## 所属库

SoC Blockset / Hardware Logic Connectivity

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要为您的设计自动生成 HDL 代码，并在 SoC 设备上执行，请使用 **SoC Builder** 工具。请参阅使用 SoC Builder 生成 SoC 设计。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2019a 中引入**

## 描述

控制硬件逻辑与上游视频接口之间的反压

Video Stream FIFO 模块控制从硬件逻辑到上游视频接口的反压。它还控制硬件逻辑的上游和下游像素数据接口之间的流。将该模块集成为用于 AXI4 视频流应用的可配置先进先出（FIFO）模块。该模块使您能够配置其深度并设置其几乎满阈值。
