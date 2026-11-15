---
type: simulink-block
title: 'Stream Data Sink'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Memory / Memory Model'
documentation_page: 'streamdatasink'
documentation_source_path: 'ref/streamdatasink.html'
language: zh-CN
chinese_source: worker-translation
---

# Stream Data Sink

## 端口

### 输入

### **rdData** — 输入流数据 标量 | 向量

来自数据源的输入流数据。此值必须为标量或向量。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **rdCtrlIn** — 输入控制总线 bus

来自数据源的输入控制总线。此控制总线包含以下控制信号：

- `valid` — 指示 **rdData** 输入端口上的输入流数据有效
- `tlast` — 指示数据事务结束

**数据类型：** `StreamM2SBusObj`
### 输出

### **rdCtrlOut** — 输出控制总线 bus

输出到数据源的控制总线，指示该模块已准备好接受流数据。此控制总线包含一个 ready 信号。

**数据类型：** `StreamS2MBusObj`

## 参数

### **Save data in workspace** — 将数据保存在工作区 `off`（默认） | `on`

选择此参数以将输入流数据保存到 MATLAB® 工作区。

### **Variable name** — 工作区变量名称 `simOut`（默认） | 任何 MATLAB 支持的变量名称

指定将输入流数据保存到的工作区变量。此参数可以是任何 MATLAB 支持的变量名称。

#### 依赖项

要启用此参数，请选择 **Save data in workspace** 参数。

## 所属库

SoC Blockset / Hardware Logic Testbench

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### HDL 代码生成

使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要自动为您的设计生成 HDL 代码，并在 SoC 设备上执行，请使用 **SoC Builder** 工具。请参阅使用 SoC Builder 生成 SoC 设计。

### 定点转换

使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2019a 中引入**

## 描述

接收连续流数据

Stream Data Sink 模块从基于高级可扩展接口 AXI4 的流数据接口模块接收连续流数据。您可以将此模块用作测试接收模块，以仿真基于 AXI4 的流数据应用。

该模块接受流数据以及控制总线，并输出控制总线。
