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
```yaml
ports:
- name: din
  summary: 写入数据输入 Scalar（默认）
  direction: input
  data_types: single | double | int8 | int16 | uint8 | uint16 | fixed point
- name: addr
  summary: 写入地址 Scalar（默认）
  direction: input
  data_types: uint8 | uint16 | fixed point
- name: we
  summary: 写入使能 Scalar（默认）
  direction: input
  data_types: Boolean
- name: dout
  summary: 输出数据 Scalar（默认）
  direction: output
```

### 输入

### **din** — 写入数据输入 `Scalar`（默认）

当 `we` 为 true 时写入 RAM 存储位置的数据。该数据从输入信号继承宽度和数据类型。`din` 可以是 `double`、`single`、`integer` 或 `fixed-point (fi)` 对象，并且可以是实数或复数。

**数据类型：** `single` | `double` | `int8` | `int16` | `uint8` | `uint16` | `fixed point`

### **addr** — 写入地址 `Scalar`（默认）

当 `we` 为 true 时写入数据的地址。该值可以是 `fixed-point(fi)` 或 `integer`，必须为无符号，且小数长度为 `0`。

**数据类型：** `uint8` | `uint16` | `fixed point`

### **we** — 写入使能 `Scalar`（默认）

当 `we` 为 true 时，RAM 将数据写入您指定的存储位置。

**数据类型：** `Boolean`
### 输出

### **dout** — 输出数据 `Scalar`（默认）

来自地址 `addr` 的输出数据。
## 参数
```yaml
parameters:
- name: Address port width
  summary: 地址位宽 8（默认）
  group: ''
  block_parameter: ram_size
  type: string scalar | character vector
  values: 最小值为 2，最大值为 29
- name: Output data during write
  summary: 控制输出数据 New data（默认） | Old data
  group: ''
  block_parameter: dout_type
  type: string scalar | character vector
  values: '"New data" | "Old data"'
```

### **Address port width** — 地址位宽 `8`（默认）

最小位宽为 2，最大位宽为 29。

#### 编程使用

|  |
| --- |
| **模块参数：** `ram_size` |
| **类型：** string scalar | character vector |
| **值：** 最小值为 `2`，最大值为 `29` |
| **默认：** `'8'` |

### **Output data during write** — 控制输出数据 `New data`（默认） | `Old data`

在写访问期间控制输出数据 `dout`。指定为以下之一：

- `New data`—在写入期间，新数据出现在输出端口 `dout`。
- `Old data`— 在写入期间，旧数据出现在输出端口 `dout`。

#### 编程使用

|  |
| --- |
| **模块参数：** `dout_type` |
| **类型：** string scalar | character vector |
| **值：** `"New data"` | `"Old data"` |
| **默认：** `'New data'` |
## 所属库

HDL Coder / HDL RAMs

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |
| **RAMDirective** | 指定是否将设计中的 RAM 模块映射到目标 FPGA 上的分布式 RAM、块 RAM 或 UltraRAM 存储器。另请参阅 RAMDirective。 |

**复数数据支持**

此模块支持复数信号的代码生成。

**Single Port RAM System**

Single Port RAM System 模块实现使用 MATLAB System 模块，该模块使用 `hdl.RAM` System object™。使用此模块执行顺序读写操作。在该模块的模块参数对话框中，您可以为 RAM 指定初始值。

使用此模块替换模型中的 Single Port RAM 模块。在模型中使用此模块时可获得更快的仿真结果。

要对不同地址执行同时读写操作，请改用 Simple Dual Port RAM System 或 Dual Port RAM System 模块。

## 版本历史

**在 R2014a 中引入**

### R2024b：即将移除

不再推荐使用 Single Port RAM。此模块将在未来版本中移除。请改用 Single Port RAM System 模块。有关详细信息，请参阅 Single Port RAM System。

## 描述

（即将移除）单端口 RAM

Single Port RAM 模块对支持顺序读写操作的 RAM 进行建模。

如果要对支持同时读写操作的 RAM 进行建模，请使用 Dual Port RAM 模块或 Simple Dual Port RAM 模块。
