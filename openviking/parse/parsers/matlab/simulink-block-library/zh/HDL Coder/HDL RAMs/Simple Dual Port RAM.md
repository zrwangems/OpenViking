---
type: simulink-block
title: 'Simple Dual Port RAM'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL RAMs'
documentation_page: 'simpledualportram'
documentation_source_path: 'ref/simpledualportram.html'
language: zh-CN
chinese_source: worker-translation
---

# Simple Dual Port RAM

## 端口

### 输入

### **wr\_din** — 写数据输入 `Scalar`（默认）

当 `wr_en` 为 true 时，写入 RAM 内存位置的数据。该数据从输入信号继承宽度和数据类型。`wr_din` 可以是 `double`、`single`、`integer` 或 `fixed-point (fi)` 对象，并且可以是实数或复数。

数据类型：标量 fixed point、integer 或 complex

**数据类型：** `int8` | `int16` | `int32` | `int64` | `fixed point`

### **wr\_addr** — 写地址 `Scalar`（默认）

写地址。

当 `wr_en` 为 true 时，将数据写入的地址。此值可以是 `fixed-point(fi)` 或 `integer`，必须为无符号，并且小数长度为 `0`。

**数据类型：** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **wr\_en** — 写使能 `Scalar`（默认）

当 `wr_en` 为 true 时，RAM 将数据写入你指定的内存位置。

**数据类型：** `Boolean`

### **rd\_addr** — 读地址 `Scalar`（默认）

从中读取数据的地址。此值可以是 `fixed-point(fi)` 或 `integer`，必须为无符号，并且小数长度为 `0`。

**数据类型：** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### 输出

### **rd\_dout** — 来自读地址的输出数据 `Scalar`（默认）

来自读地址 `rd_addr` 的输出数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **地址端口宽度** — 地址位宽 8（默认）

最小位宽为 2，最大位宽为 29。

#### 编程使用

|  |
| --- |
| **模块参数：** `ram_size` |
| **类型：** string scalar | character vector |
| **值：** 最小值 `2`，最大值 `29` |
| **默认：** `'8'` |

## 所属库

HDL Coder / HDL RAMs

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中的现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |
| **RAMDirective** | 指定是否将设计中的 RAM 模块映射到目标 FPGA 上的 distributed RAMs、block RAMs 或 UltraRAM memory。另请参阅 RAMDirective。 |

**复数数据支持**

此模块支持复数信号的代码生成。

**Simple Dual Port RAM System**

Simple Dual Port RAM System 模块实现使用一个 MATLAB System 模块，该模块使用 `hdl.RAM` System object™。使用此模块执行同时读写操作。它有一个用于读取数据的输出端口。在该模块的模块参数对话框中，可以为 RAM 指定初始值。

使用此模块替换模型中的 Simple Dual Port RAM 模块。在模型中使用此模块时，可以获得更快的仿真结果。

## 版本历史

**在 R2014a 中引入**

### R2024b：将移除

不再建议使用 Simple Dual Port RAM。此模块将在未来版本中移除。请改用 Simple Dual Port RAM System 模块。有关更多信息，请参阅 Simple Dual Port RAM System。

## 描述

（将移除）具有单个输出端口的双端口 RAM

Simple Dual Port RAM 模块对支持同时读写操作、并具有用于读取数据的单个输出端口的 RAM 进行建模。你可以使用此模块生成可映射到大多数 FPGA 中的 RAM 的 HDL 代码。

Simple Dual Port RAM 与 Dual Port RAM 类似，但 Dual Port RAM 同时具有写数据输出端口和读数据输出端口。

### 写期间读行为

在写操作期间，如果同一地址发生读操作，则输出端出现旧数据。
