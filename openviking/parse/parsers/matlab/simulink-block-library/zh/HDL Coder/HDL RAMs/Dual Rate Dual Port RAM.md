---
type: simulink-block
title: 'Dual Rate Dual Port RAM'
family: 'hdl-rams'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL RAMs'
documentation_page: 'dualratedualportram'
documentation_source_path: 'ref/dualratedualportram.html'
language: zh-CN
chinese_source: worker-translation
---

# Dual Rate Dual Port RAM

## 端口

### 输入

### **din\_A** — 端口 A 写数据输入 `Scalar`（默认）

当 `we_A` 为 true 时，你写入 RAM 存储位置的数据。数据继承输入信号的宽度和数据类型。`din_A` 可以是 `double`、`single`、`integer` 或 `fixed-point (fi)` 对象，并且可以是实数或复数。

数据类型：标量定点、整数或复数

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **addr\_A** — 端口 A 写地址 `Scalar`（默认）

当 `we_A` 为 true 时，你将数据写入的地址。此值可以是 `fixed-point(fi)` 或 `integer`，必须为无符号，并且小数长度为 `0`。

**数据类型：** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **we\_A** — 端口 A 写使能 `Scalar`（默认）

RAM 端口 A 的写使能。将 `we_A` 设置为 `true` 表示写操作，或设置为 `false` 表示读操作。

**数据类型：** `Boolean`

### **din\_B** — 端口 B 写数据 `Scalar`（默认）

当 `we_B` 为 true 时，你写入 RAM 存储位置的数据。数据继承输入信号的宽度和数据类型。`din_B` 可以是 `double`、`single`、`integer` 或 `fixed-point (fi)` 对象，并且可以是实数或复数。

数据类型：标量定点、整数或复数

**数据类型：** `int8` | `int16` | `int32` | `int64` | `fixed point`

### **addr\_B** — 端口 B 写地址 `Scalar`（默认）

当 `we_B` 为 true 时，你将数据写入的地址。此值可以是 `fixed-point(fi)` 或 `integer`，必须为无符号，并且小数长度为 `0`。

数据类型：标量定点、整数或复数

**数据类型：** `int8` | `int16` | `int32` | `int64` | `fixed point`

### **we\_B** — 端口 B 写使能 `Scalar`（默认）

RAM 端口 B 的写使能。将 `we_B` 设置为 `true` 表示写操作，或设置为 `false` 表示读操作。

**数据类型：** `Boolean`
### 输出

### **dout\_A** — 端口 A 输出数据 `Scalar`（默认）

来自 RAM 端口 A 地址 `addr_A` 的输出数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **dout\_B** — 端口 B 输出数据 `Scalar`（默认）

来自 RAM 端口 B 地址 `addr_B` 的输出数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **地址端口宽度** — 地址位宽 8（默认）

最小位宽为 2，最大位宽为 28。

#### 编程使用

|  |
| --- |
| **模块参数：** `ram_size` |
| **类型：** string scalar | character vector |
| **值：** 最小值为 `2`，最大值为 `28` |
| **默认值：** `'8'` |

## 所属库

HDL Coder / HDL RAMs

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

**注意**

为使仿真结果与生成的 HDL 代码匹配，在 Configuration Parameters 对话框的 Solver 窗格中，清除 **Treat each discrete rate as a separate task** 复选框。清除该复选框后，将启用单任务模式。如果选中此复选框来仿真该模块，则输出数据可以在同一周期更新，但在生成的 HDL 代码中，输出数据会在一个周期后更新。

该模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出处的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |

**注意**

**RAMDirective** 属性不可用于 Dual Rate Dual Port RAM，因为该模块没有单时钟接口。

**复数数据支持**

该模块支持复数信号的代码生成。不能混合使用实数值和复数输入。

## 版本历史

**在 R2014a 中引入**

## 描述

支持两种速率的双端口 RAM

Dual Rate Dual Port RAM 模块建模了一个 RAM，该 RAM 支持在两个时钟速率下对不同地址进行同时读写操作。RAM 的端口 A 可以以一个速率运行，端口 B 可以以另一个速率运行。

在高性能硬件应用中，你可以使用此模块每个时钟周期访问 RAM 两次。如果生成 HDL 代码，此模块在大多数 FPGA 中映射为双时钟双端口 RAM。

### 同时访问

你可以同时从端口 A 和 B 访问不同地址。你也可以同时从端口 A 和 B 读取同一地址。

但是，不要在一个 RAM 端口正在从另一个 RAM 端口写入地址时访问该地址。在仿真期间，如果你从一个 RAM 端口访问某个地址的同时，从另一个 RAM 端口写入该地址，软件将报告错误。

### 写期间读行为

该 RAM 具有写优先行为。当你向 RAM 写入时，新的写入数据会立即出现在输出端口。
