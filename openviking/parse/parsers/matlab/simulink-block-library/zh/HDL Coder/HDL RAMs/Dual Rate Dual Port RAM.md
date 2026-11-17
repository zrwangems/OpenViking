---
type: simulink-block
title: 'Dual Rate Dual Port RAM'
family: 'hdlcoder'
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

当 `we_A` 为 true 时写入 RAM 存储位置的数据。该数据从输入信号继承宽度和数据类型。
`din_A` 可以是 `double`、
`single`、`integer` 或 `fixed-point
(fi)` 对象，并且可以是实数或复数。

数据类型：标量定点、整数或复数

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **addr\_A** — 端口 A 写地址 `Scalar`（默认）

当 `we_A` 为 true 时将数据写入的地址。该值可以是 `fixed-point(fi)` 或 `integer`，
必须为无符号，并且小数长度为 `0`。

**数据类型：** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **we\_A** — 端口 A 写使能 `Scalar`（默认）

RAM 端口 A 的写使能。将 `we_A` 设置为
`true` 以执行写操作，或设置为 `false` 以执行
读操作。

**数据类型：** `Boolean`

### **din\_B** — 端口 B 写数据 `Scalar`（默认）

当 `we_B` 为 true 时写入 RAM 存储位置的数据。该数据从输入信号继承宽度和数据类型。
`din_B` 可以是 `double`、
`single`、`integer` 或 `fixed-point
(fi)` 对象，并且可以是实数或复数。

数据类型：标量定点、整数或复数

**数据类型：** `int8` | `int16` | `int32` | `int64` | `fixed point`

### **addr\_B** — 端口 B 写地址 `Scalar`（默认）

当 `we_B` 为 true 时将数据写入的地址。该值可以是 `fixed-point(fi)` 或 `integer`，
必须为无符号，并且小数长度为 `0`。

数据类型：标量定点、整数或复数

**数据类型：** `int8` | `int16` | `int32` | `int64` | `fixed point`

### **we\_B** — 端口 B 写使能 `Scalar`（默认）

RAM 端口 B 的写使能。将 `we_B` 设置为
`true` 以执行写操作，或设置为 `false` 以执行
读操作。

**数据类型：** `Boolean`
### 输出

### **dout\_A** — 端口 A 输出数据 `Scalar`（默认）

来自 RAM 端口 A 地址 `addr_A` 的输出数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **dout\_B** — 端口 B 输出数据 `Scalar`（默认）

来自 RAM 端口 B 地址 `addr_B` 的输出数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

## 参数

### **Address port width** — 地址位宽 8（默认）

最小位宽为 2，最大位宽为 28。

#### 编程使用

|  |
| --- |
| **模块参数：** `ram_size` |
| **类型：** 字符串标量 | 字符向量 |
| **值：** 最小值为 `2`，最大值为 `28` |
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

**注意**

为使仿真结果与生成的 HDL 代码匹配，请在配置参数对话框的求解器窗格中，清除 **将每个离散速率视为单独任务** 复选框。清除该复选框后，将启用单任务模式。如果在选中该复选框的情况下对模块进行仿真，输出数据可能在同一周期更新，但在生成的 HDL 代码中，输出数据将在一个周期后更新。

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |

**注意**

**RAMDirective** 属性不可用于 Dual Rate Dual Port RAM，因为该模块没有单时钟接口。

**复数数据支持**

此模块支持复数信号的代码生成。不能混合使用实数值和复数输入。

## 版本历史

**在 R2014a 中引入**

## 描述

支持两种速率的双端口 RAM

Dual Rate Dual Port RAM 模块对支持以两种时钟速率对不同地址同时进行读写操作的 RAM 进行建模。RAM 的端口 A 可以以一种速率运行，端口 B 可以以不同速率运行。

在高性能硬件应用中，您可以使用此模块每个时钟周期访问 RAM 两次。如果生成 HDL 代码，此模块将映射到大多数 FPGA 中的双时钟双端口 RAM。

### 同时访问

您可以同时从端口 A 和端口 B 访问不同地址。您也可以同时从端口 A 和端口 B 读取同一地址。

但是，不要在一个 RAM 端口正在从另一个 RAM 端口写入某地址时，从该端口访问该地址。在仿真期间，如果您从一个 RAM 端口访问某地址的同时从另一个 RAM 端口写入该地址，软件将报告错误。

### 写期间读行为

该 RAM 具有写优先行为。当您写入 RAM 时，新的写入数据会立即出现在输出端口。
