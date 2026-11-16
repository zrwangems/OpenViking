---
type: simulink-block
title: 'Stream Data Source'
family: 'soc'
product_id: 'soc'
product_name: 'SoC Blockset'
documentation_release: R2025b
official_category: 'Hardware Logic Testbench'
documentation_page: 'streamdatasource'
documentation_source_path: 'ref/streamdatasource.html'
language: zh-CN
chinese_source: worker-translation
---

# Stream Data Source

## 端口

### 输入

### **wrCtrlIn** — 输入控制总线 bus

来自数据消费者的控制总线，表示数据消费者已准备好接受流数据。该控制总线包含一个 ready 信号。

**数据类型：** `StreamS2MBusObj`

### 输出

### **wrData** — 输出流数据 标量 | 向量

向数据消费者输出流数据。该值以标量或向量形式返回。

您可以更改输出流数据的数据类型。有关详细信息，请参阅 **Data type** 参数。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **wrCtrlOut** — 输出控制总线 bus

到数据消费者的控制总线，作为 bus 返回。该控制总线包含以下控制信号：

- `valid` — 指示 **wrData** 输出端口上的输出数据有效
- `tlast` — 指示数据事务结束

**数据类型：** `StreamM2SBusObj`

## 参数

### **Data type** — 输出数据类型 `uint8`（默认）| `double` | `single` | `int8` | `int16` | `int32` | `int64` | `uint16` | `uint32` | `uint64` | `fixdt(1,16,0)`

选择输出流数据的数据类型格式。

单击  按钮以显示 **Data Type Assistant**，它可帮助您为 **wrData** 输出端口设置数据类型。有关详细信息，请参阅使用 Data Type Assistant 指定数据类型。

### **Dimensions** — 输出数据维度 `10`（默认）| 正整数 | 数组

将输出流数据的维度指定为正标量或数组。

**示例：** `1` 指定标量样本。

**示例：** `[10 1]` 指定十个标量的向量。

### **Burst length** — 单个突发的长度 `20`（默认）| 正整数

单个突发的长度，指定为正整数。

### **Total bursts** — 突发总数 `4`（默认）| 正整数

从该模块生成的突发总数，指定为正整数。

### **Data generation** — 输出生成类型 `counter`（默认）| `random` | `ones` | `workspace`

将输出的生成类型指定为以下值之一：

- `counter` — 根据所选数据类型从计数器生成数据。
- `random` — 生成随机数据。
- `ones` — 根据所选数据类型生成所有位均为 1 的数据。
- `workspace` — 从 MATLAB® 工作区生成数据。

### **Counter init value** — 计数器初始值 `0`（默认）| 标量

指定计数器开始的值。计数器值的有效范围取决于为 **Data type** 参数选择的值。如果此值超出有效范围，则将其舍入到最接近的有效值。

例如，如果 **Data type** 为 `uint8` 且此值为 `6.787`，则此值舍入为 `7`。

#### 依赖关系

要启用此参数，请将 **Data generation** 参数设置为 `counter`。

### **Variable name** — 工作区变量名称 `simOut`（默认）| 任何 MATLAB 支持的变量名称

指定从其生成输出流数据的变量名称。此参数可以是任何 MATLAB 支持的变量名称。

**注意**

工作区变量必须是数值数组。

#### 依赖关系

要启用此参数，请将 **Data generation** 参数设置为 `workspace`。

### **Sample time** — 采样时间间隔 1（默认）| 正标量 | 向量

指定以 seconds 为单位的时间间隔，以定义模块的更新频率。

当您不希望输出具有时间偏移时，请将 **Sample time** 参数指定为标量。要向输出添加时间偏移，请将 **Sample time** 参数指定为 `1`-by-`2` 向量，其中第一个元素是采样周期，第二个元素是偏移。有关 Simulink® 中采样时间的详细信息，请参阅 Specify Sample Time。

### **Transfer delay (in samples)** — 突发之间的延迟 `0`（默认）| 非负整数

在此时间之后，下一个突发发生。此值必须为非负整数。

## 所属库

SoC Blockset / Hardware Logic Testbench

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

要自动为您的设计生成 HDL 代码，并在 SoC 设备上执行，请使用 **SoC Builder** 工具。请参阅使用 SoC Builder 生成 SoC 设计。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2019a 中引入**

## 描述

生成连续流数据

Stream Data Source 模块向基于高级可扩展接口 AXI4 的流数据接口模块生成流数据。您可以将此模块用作测试源模块，以仿真基于 AXI4 的流数据应用。

该模块接受一个控制总线，并输出流数据以及一个控制总线。
