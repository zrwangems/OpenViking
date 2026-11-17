---
type: simulink-block
title: 'Bias'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Floating Point Operations'
documentation_page: 'bias'
documentation_source_path: '../simulink/slref/bias.html'
language: zh-CN
chinese_source: worker-translation
---

# Bias

## 端口
```yaml
ports:
- name: Port_1
  summary: 输入信号 标量 | 向量
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
- name: Port_1
  summary: 输出信号 标量 | 向量
  direction: output
  data_types: half | single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输入

### **Port\_1** — 输入信号 标量 | 向量

要添加偏置以生成输出信号的输入信号。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量

将偏置添加到输入信号后得到的输出信号。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## 参数
```yaml
parameters:
- name: Bias
  summary: 要添加到输入信号的偏移量 0.0（默认）| 标量 | 向量
  group: ''
  block_parameter: Bias
  type: 字符向量
  values: 实数、有限值
  default: '''0.0'''
- name: Saturate on integer overflow
  summary: 溢出操作方式 off（默认）| on
  group: ''
  block_parameter: SaturateOnIntegerOverflow
  values: '''off''（默认）| ''on'''
```

### **Bias** — 要添加到输入信号的偏移量 `0.0`（默认）| 标量 | 向量

指定要添加到输入信号的偏移量的值。Bias 模块隐式地将 `Bias` 添加到输入信号。要从信号中减去 `Bias`，请指定一个负值，其数据类型能够存储负值。

#### 编程使用

|  |
| --- |
| **模块参数：** `Bias` |
| **类型：** 字符向量 |
| **值：** 实数、有限值 |
| **默认值：** `'0.0'` |

### **Saturate on integer overflow** — 溢出操作方式 `off`（默认）| `on`

指定溢出时是饱和还是回绕。

- `on` — 溢出饱和到数据类型能够表示的最小值或最大值。
- `off` — 溢出回绕到数据类型能够表示的相应值。

例如，有符号 8 位整数 `int8` 能够表示的最大值是 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。

- 选中此参数时，模块输出饱和于 127。类似地，模块输出饱和于最小输出值 -128。
- 清除此参数时，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时为 -126。

#### 提示

- 当您的模型可能存在溢出并且您希望在生成的代码中显式提供饱和保护时，请考虑选中此参数。
- 当您希望优化生成代码的效率时，请考虑清除此参数。清除此参数还有助于避免过度指定模块如何处理超出范围的信号。有关详细信息，请参阅 Troubleshoot Signal Range Errors。
- 选中此参数时，饱和适用于模块上的每个内部运算，而不仅仅是输出或结果。
- 通常，代码生成过程可以检测到不可能发生溢出的情况。在这种情况下，代码生成器不会生成饱和代码。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SaturateOnIntegerOverflow` |
| **值：** | `'off'`（默认）| `'on'` |
## 所属库

Simulink / Math Operations HDL Coder / HDL Floating Point Operations HDL Coder / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `half` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

向输入添加偏置

Bias 模块根据以下公式向输入信号添加偏置或偏移量

*Y* = *U* + *bias*

其中 *U* 是模块输入，*Y* 是输出。
