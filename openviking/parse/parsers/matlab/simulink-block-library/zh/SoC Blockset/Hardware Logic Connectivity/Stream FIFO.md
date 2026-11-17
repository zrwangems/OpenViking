---
type: simulink-block
title: 'Stream FIFO'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Hardware Logic Connectivity'
documentation_page: 'streamfifo'
documentation_source_path: 'ref/streamfifo.html'
language: zh-CN
chinese_source: worker-translation
---

# Stream FIFO

## 端口
```yaml
ports:
- name: dataIn
  summary: 输入流数据 标量
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: dValidIn
  summary: 有效输入流数据指示 Boolean 标量
  direction: input
  data_types: Boolean
- name: rdyFromDown
  summary: 来自下游接口的准备好信号 Boolean 标量
  direction: input
  data_types: Boolean
- name: dataOut
  summary: 输出流数据 标量
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: dValidOut
  summary: 有效输出流数据指示 Boolean 标量
  direction: output
  data_types: Boolean
- name: rdyToUp
  summary: 发送到上游接口的准备好信号 Boolean 标量
  direction: output
  data_types: Boolean
```

### 输入

### **dataIn** — 输入流数据 标量

来自数据源的输入流数据。将此值指定为标量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **dValidIn** — 有效输入流数据指示 `Boolean` 标量

控制信号，指示来自数据源的输入流数据是否有效。当此值为 `1`（true）时，模块接受 **dataIn** 端口上的值。当此值为 `0`（false）时，模块忽略 **dataIn** 端口上的值。

**数据类型：** `Boolean`

### **rdyFromDown** — 来自下游接口的准备好信号 `Boolean` 标量

控制信号，指示模块是否可以向所述下游接口发送流数据。当此值为 `1`（true）时，下游接口已准备好，模块可以发送流数据。当此值为 `0`（false）时，下游接口未准备好，模块无法发送流数据。

**数据类型：** `Boolean`
### 输出

### **dataOut** — 输出流数据 标量

发送到下游接口的输出流数据。此输出数据的数据类型与输入数据的数据类型相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **dValidOut** — 有效输出流数据指示 `Boolean` 标量

控制信号，指示输出流数据是否有效。当此值为 `1`（true）时，**dataOut** 端口上的输出流数据有效。当此值为 `0`（false）时，**dataOut** 端口上的输出流数据无效。

**数据类型：** `Boolean`

### **rdyToUp** — 发送到上游接口的准备好信号 `Boolean` 标量

控制信号，指示模块是否已准备好从上游接口接收流数据。当此值为 `1`（true）时，模块已准备好接受来自上游接口的流数据。当此值为 `0`（false）时，模块未准备好接受来自上游接口的流数据。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Depth of FIFO
  summary: FIFO 深度 16（默认）| 大于或等于四的整数
  group: ''
- name: Almost full threshold
  summary: 几乎满阈值 8（默认）| 正整数
  group: ''
```

### **Depth of FIFO** — FIFO 深度 `16`（默认）| 大于或等于四的整数

将 FIFO 的深度指定为大于或等于四的整数。此值是数据被丢弃之前可以缓冲的最大条目数。

### **Almost full threshold** — 几乎满阈值 `8`（默认）| 正整数

指定一个值，用于从模块向数据源发出反压信号。

为避免丢弃数据，请设置一个允许数据源有足够时间对反压做出反应的值。此值必须为正整数，且小于 FIFO 深度。
## 所属库

SoC Blockset / Hardware Logic Connectivity

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要为您的设计自动生成 HDL 代码，并在 SoC 设备上执行，请使用 **SoC Builder** 工具。请参阅 Use SoC Builder to Generate SoC Design。

使用 SoC Blockset™，您可以在模型中建模简化的流协议。使用 HDL Coder™ 在 IP 核中生成 AXI4-Stream 接口。有关 AXI4-stream 协议的更多信息，请参阅 AXI4-Stream Interface。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2019a 中引入**

## 描述

控制硬件逻辑与上游数据接口之间的反压

Stream FIFO 模块控制从硬件逻辑到上游数据接口的反压。它还控制硬件逻辑的上游和下游数据接口之间的流。将此模块集成为用于 AXI4 数据流应用的可配置先进先出（FIFO）模块。该模块使您能够配置其深度并设置其几乎满阈值。
