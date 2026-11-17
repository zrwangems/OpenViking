---
type: simulink-block
title: 'Dual Port RAM'
family: 'hdl-rams'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL RAMs'
documentation_page: 'dualportram'
documentation_source_path: 'ref/dualportram.html'
language: zh-CN
chinese_source: worker-translation
---

# Dual Port RAM

## 端口

### 输入

### **wr\_din** — 写数据输入 `Scalar`（默认）

当 `wr_en` 为 true 时，写入到 RAM 内存位置的数据。该数据从输入信号继承宽度和数据类型。
`wr_din` 可以是 `double`、
`single`、`integer` 或 `fixed-point (fi)` 对象，并且可以是实数或复数。

数据类型：scalar fixed point、integer 或 complex

**数据类型：** `int8` | `int16` | `int32` | `int64` | `Boolean` | `fixed point`

### **wr\_addr** — 写地址 `Scalar`（默认）

当 `wr_en` 为 true 时，将数据写入的地址。此值可以是 `fixed-point(fi)` 或 `integer`，
必须为无符号，并且小数长度为 `0`。

**数据类型：** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **wr\_en** — 写使能 `Scalar`（默认）

当 `wr_en` 为 true 时，RAM 将数据写入您指定的内存位置。

**数据类型：** `Boolean`

### **rd\_addr** — 读地址 `Scalar`（默认）

从中读取数据的地址。此值可以是
`fixed-point(fi)` 或 `integer`，必须为无符号，
并且小数长度为 `0`。

**数据类型：** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **wr\_dout** — 来自写地址的输出数据 `Scalar`（默认）

来自写地址 `wr_addr` 的输出数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **rd\_dout** — 来自读地址的输出数据 `Scalar`（默认）

来自读地址 `rd_addr` 的输出数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **地址端口宽度** — 地址位宽 8（默认）

最小位宽为 2，最大位宽为 29。

#### 编程用法

|  |
| --- |
| **模块参数：** `ram_size` |
| **类型：** string scalar | character vector |
| **值：** 最小值 `2`，最大值 `29` |
| **默认：** `'8'` |

## 所属库

HDL Coder / HDL RAMs

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成
使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成
使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中的现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline。 |
| **RAMDirective** | 指定是否将设计中的 RAM 模块映射到目标 FPGA 上的 RAM 模块。不能将 Dual Port RAM 模块映射到 UltraRAM。映射到 UltraRAM 要求模块具有固定的读取行为。有关详细信息，请参阅 RAMDirective。 |

**复数数据支持**

此模块支持复数信号的代码生成。

**Dual Port RAM System**

Dual Port RAM System 模块实现使用一个 MATLAB System 模块，该模块使用
`hdl.RAM`
System object™。使用此模块执行同时读和写操作。它具有
读数据输出端口和写数据输出端口。在此模块的模块参数对话框
中，您可以为 RAM 指定初始值。如果不想使用
写数据输出端口，为实现更好的 RAM 推断，请改用 Simple Dual Port
RAM System 模块。

使用此模块替换模型中的 Dual Port RAM 模块。在模型中使用此模块时，您
可获得更快的仿真结果。

## 版本历史

**在 R2014a 中引入**

### R2024b：将移除

不再推荐使用 Dual Port RAM。此模块将在未来版本中移除。请改用 Dual Port RAM System 模块。有关
详细信息，请参阅 Dual Port RAM System。

## 描述

（将移除）具有两个输出端口的 Dual Port RAM

Dual Port RAM 模块对支持同时读写操作并同时具有读数据输出端口和写数据输出端口的 RAM 进行建模。您可以使用
此模块生成可映射到大多数 FPGA 中 RAM 的 HDL 代码。

如果不需要使用写输出数据 `wr_dout`，则可以通过使用 Simple Dual Port RAM 模块，
利用综合工具实现更好的 RAM 推断。

### 写时读行为

在写入期间，新数据出现在 Dual Port RAM 模块的写端口
（`wr_dout`）的输出端。如果读操作与写操作
同时发生在同一地址，则旧数据出现在读输出
端口（`rd_dout`）。
