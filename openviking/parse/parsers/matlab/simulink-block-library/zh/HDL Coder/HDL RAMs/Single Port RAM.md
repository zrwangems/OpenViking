---
type: simulink-block
title: 'Single Port RAM'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL RAMs'
documentation_page: 'singleportram'
documentation_source_path: 'ref/singleportram.html'
language: zh-CN
chinese_source: worker-translation
---

# Single Port RAM

## 端口

### 输入

### **din** — 写入数据输入 `Scalar`（默认）

当 `we` 为 true 时，写入到 RAM 内存位置的数据。数据继承输入信号的宽度和数据类型。`din` 可以是 `double`、`single`、`integer` 或 `fixed-point (fi)` 对象，并且可以是实数或复数。

**数据类型：** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `fixed point`

### **addr** — 写入地址 `Scalar`（默认）

当 `we` 为 true 时，将数据写入的地址。此值可以是 `fixed-point(fi)` 或 `integer`，必须为无符号，且小数长度为 `0`。

**数据类型：** `uint8` | `uint16` | `fixed point`

### **we** — 写使能 `Scalar`（默认）

当 `we` 为 true 时，RAM 将数据写入你指定的内存位置。

**数据类型：** `Boolean`
### 输出

### **dout** — 输出数据 `Scalar`（默认）

来自地址 `addr` 的输出数据。

## 参数

### **地址端口宽度** — 地址位宽 `8`（默认）

最小位宽为 2，最大位宽为 29。

#### 程序化使用

|  |
| --- |
| **模块参数：** `ram_size` |
| **类型：** string scalar | character vector |
| **值：** 最小值为 `2`，最大值为 `29` |
| **默认：** `'8'` |

### **写入期间的输出数据** — 控制输出数据 `New data`（默认） | `Old data`

控制写入访问期间的输出数据 `dout`。
指定为以下之一：

- `New data`—在写入期间，新数据出现在输出端口 `dout`。
- `Old data`—在写入期间，旧数据出现在输出端口 `dout`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `dout_type` |
| **类型：** string scalar | character vector |
| **值：** `"New data"` | `"Old data"` |
| **默认：** `'New data'` |

## 所属库

HDL Coder / HDL RAMs

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一种默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline。 |
| **RAMDirective** | 指定是否将设计中的 RAM 块映射到目标 FPGA 上的 distributed RAMs、block RAMs 或 UltraRAM memory。另请参阅 RAMDirective。 |

**复数数据支持**

此模块支持复数信号的代码生成。

**Single Port RAM System**

Single
Port RAM System 模块实现使用一个 MATLAB System 模块，该模块使用
`hdl.RAM`
System object™。使用此模块执行顺序读取和写入操作。
在该模块的模块参数对话框中，可以指定
RAM 的初始值。

使用此模块替换模型中的 Single Port RAM 模块。在模型中使用此模块可获得更快的仿真结果。

要对不同地址执行同时读取和写入操作，请改用
Simple Dual Port RAM System 或 Dual Port RAM
System 模块。

## 版本历史

**在 R2014a 中引入**

### R2024b：将移除

不再推荐使用 Single Port RAM。此模块将在未来版本中
移除。请改用 Single Port RAM System
模块。有关详细信息，请参阅 Single Port RAM System。

## 描述

（将移除）Single port RAM

Single Port RAM 模块对支持顺序读取和写入操作的 RAM 进行建模。

如果要对支持同时读取和写入操作的 RAM 进行建模，请使用
Dual Port RAM 模块或 Simple Dual Port RAM 模块。
