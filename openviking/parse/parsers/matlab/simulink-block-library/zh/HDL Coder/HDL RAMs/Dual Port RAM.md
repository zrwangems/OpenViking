---
type: simulink-block
title: 'Dual Port RAM'
family: 'hdlcoder'
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
```yaml
ports:
- name: wr_din
  summary: 写入数据输入 Scalar（默认）
  direction: input
  data_types: int8 | int16 | int32 | int64 | Boolean | fixed point
- name: wr_addr
  summary: 写入地址 Scalar（默认）
  direction: input
  data_types: uint8 | uint16 | uint32 | uint64 | fixed point
- name: wr_en
  summary: 写入使能 Scalar（默认）
  direction: input
  data_types: Boolean
- name: rd_addr
  summary: 读取地址 Scalar（默认）
  direction: input
  data_types: uint8 | uint16 | uint32 | uint64 | fixed point
- name: wr_dout
  summary: 来自写入地址的输出数据 Scalar（默认）
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus
- name: rd_dout
  summary: 来自读取地址的输出数据 Scalar（默认）
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated | bus
```

### 输入

### **wr\_din** — 写入数据输入 `Scalar`（默认）

当 `wr_en` 为 true 时写入 RAM 存储位置的数据。该数据从输入信号继承宽度和数据类型。`wr_din` 可以是 `double`、`single`、`integer` 或 `fixed-point (fi)` 对象，并且可以是实数或复数。

数据类型：标量定点、整数或复数

**数据类型：** `int8` | `int16` | `int32` | `int64` | `Boolean` | `fixed point`

### **wr\_addr** — 写入地址 `Scalar`（默认）

当 `wr_en` 为 true 时将数据写入的地址。该值可以是 `fixed-point(fi)` 或 `integer`，必须为无符号，且小数长度为 `0`。

**数据类型：** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **wr\_en** — 写入使能 `Scalar`（默认）

当 `wr_en` 为 true 时，RAM 将数据写入您指定的存储位置。

**数据类型：** `Boolean`

### **rd\_addr** — 读取地址 `Scalar`（默认）

从中读取数据的地址。该值可以是 `fixed-point(fi)` 或 `integer`，必须为无符号，且小数长度为 `0`。

**数据类型：** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **wr\_dout** — 来自写入地址的输出数据 `Scalar`（默认）

来自写入地址 `wr_addr` 的输出数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`

### **rd\_dout** — 来自读取地址的输出数据 `Scalar`（默认）

来自读取地址 `rd_addr` 的输出数据。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated` | `bus`
## 参数
```yaml
parameters:
- name: Address port width
  summary: 地址位宽 8（默认）
  group: ''
  block_parameter: ram_size
  type: 字符串标量 | 字符向量
  values: 最小值为 2，最大值为 29
```

### **Address port width** — 地址位宽 8（默认）

最小位宽为 2，最大位宽为 29。

#### 编程使用

|  |
| --- |
| **模块参数：** `ram_size` |
| **类型：** 字符串标量 | 字符向量 |
| **值：** 最小值为 `2`，最大值为 `29` |
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

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |
| **RAMDirective** | 指定是否将设计中的 RAM 模块映射到目标 FPGA 上的 RAM 模块。不能将双端口 RAM 模块映射到 UltraRAM。映射到 UltraRAM 要求模块具有固定的读取行为。有关更多详细信息，请参阅 RAMDirective。 |

**复数数据支持**

此模块支持复数信号的代码生成。

**双端口 RAM 系统**

双端口 RAM 系统模块实现使用 MATLAB System 模块，该模块使用 `hdl.RAM` System object™。使用此模块执行同时读写操作。它具有读数据输出端口和写数据输出端口。在模块的“模块参数”对话框中，可以为 RAM 指定初始值。如果不希望使用写数据输出端口，为实现更好的 RAM 推断，请改用简单双端口 RAM 系统模块。

使用此模块替换模型中的双端口 RAM 模块。在模型中使用此模块时可获得更快的仿真结果。

## 版本历史

**在 R2014a 中引入**

### R2024b：将被移除

不再推荐使用双端口 RAM。此模块将在未来版本中移除。请改用双端口 RAM 系统模块。有关更多信息，请参阅双端口 RAM 系统。

## 描述

（将被移除）具有两个输出端口的双端口 RAM

双端口 RAM 模块对支持同时读写操作且同时具有读数据输出端口和写数据输出端口的 RAM 进行建模。可以使用此模块生成映射到大多数 FPGA 中 RAM 的 HDL 代码。

如果不需要使用写输出数据 `wr_dout`，可以通过使用简单双端口 RAM 模块，利用综合工具实现更好的 RAM 推断。

### 写期间读行为

在写入期间，新数据出现在双端口 RAM 模块的写端口（`wr_dout`）输出端。如果读操作与写操作同时发生在同一地址，则旧数据出现在读输出端口（`rd_dout`）。
