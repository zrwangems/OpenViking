---
type: simulink-block
title: 'Real-Imag to Complex'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'realimagtocomplex'
documentation_source_path: '../simulink/slref/realimagtocomplex.html'
language: zh-CN
chinese_source: worker-translation
---

# Real-Imag to Complex

## 端口
```yaml
ports:
- name: Re
  summary: 复输出的实部 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point | bus
- name: Im
  summary: 复输出的虚部 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point | bus
- name: Port_1
  summary: 复输出的实部或虚部 标量 | 向量 | 矩阵
  direction: input
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point | bus
- name: Port_1
  summary: 复信号 标量 | 向量 | 矩阵
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输入

### **Re** — 复输出的实部 标量 | 向量 | 矩阵

要转换为复值输出信号的实数值，指定为标量、向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`

### **Im** — 复输出的虚部 标量 | 向量 | 矩阵

要转换为复值输出信号的虚数值，指定为标量、向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`

### **Port\_1** — 复输出的实部或虚部 标量 | 向量 | 矩阵

要转换为复输出信号的实数值或虚数值，指定为有限标量、向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`
### 输出

### **Port\_1** — 复信号 标量 | 向量 | 矩阵

由实部和虚部值构成的复信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## 参数
```yaml
parameters:
- name: Input
  summary: 实部、虚部或两者 Real（默认） | Imag | Real and imag
  group: ''
  block_parameter: Input
  type: 字符向量
  values: '''Real and imag'' | ''Real'' | ''Imag'''
  default: '''Real and imag'''
- name: Imag part
  summary: 复输出的虚部 0（默认） | 有限标量、向量或矩阵
  group: ''
  block_parameter: ConstantPart
  type: 字符向量
  values: 虚数值
  default: '''0'''
- name: Real part
  summary: 复输出的实部 0（默认） | 有限标量、向量或矩阵
  group: ''
  block_parameter: ConstantPart
  type: 字符向量
  values: 有限实值标量、向量或矩阵
  default: '''0'''
- name: Sample time (-1 for inherited)
  summary: 采样之间的时间间隔 -1（默认） | 标量 | 向量
  group: ''
  block_parameter: SampleTime
  values: '"-1"（默认） | 带引号的标量或向量'
```

### **Input** — 实部、虚部或两者 `Real`（默认） | `Imag` | `Real and imag`

指定输入类型：实部输入、虚部输入或两者。

#### 编程使用

|  |
| --- |
| **模块参数：** `Input` |
| **类型：** 字符向量 |
| **值：** `'Real and imag' | 'Real' | 'Imag'` |
| **默认值：** `'Real and imag'` |

### **Imag part** — 复输出的虚部 `0`（默认） | 有限标量、向量或矩阵

指定将输入转换为复值输出信号时要使用的虚数值。

#### 依赖关系

要启用此参数，请将 **Input** 设置为
`Real`。

#### 编程使用

|  |
| --- |
| **模块参数：** `ConstantPart` |
| **类型：** 字符向量 |
| **值：** 虚数值 |
| **默认值：** `'0'` |

### **Real part** — 复输出的实部 `0`（默认） | 有限标量、向量或矩阵

指定将输入转换为复值输出信号时要使用的常量实数值。

#### 依赖关系

要启用此参数，请将 **Input** 设置为
`Imag`。

#### 编程使用

|  |
| --- |
| **模块参数：** `ConstantPart` |
| **类型：** 字符向量 |
| **值：** 有限实值标量、向量或矩阵 |
| **默认值：** `'0'` |

### **Sample time (-1 for inherited)** — 采样之间的时间间隔 `-1`（默认） | 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数：** | `SampleTime` |
| **值：** | `"-1"`（默认） | 带引号的标量或向量 |
## 所属库

Simulink / Math Operations HDL Coder / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复信号的代码生成。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

将实部和/或虚部输入转换为复信号

Real-Imag to Complex 模块将实部和/或虚部输入转换为复值输出信号。

两个输入可以都是相同维度的数组（向量或矩阵），或者一个输入可以是数组而另一个是标量。如果模块具有数组输入，则输出是相同维度的复数数组。实部输入的元素映射到对应复数输出元素的实部。虚部输入类似地映射到复数输出信号的虚部。如果一个输入是标量，则它映射到所有复数输出信号的对应分量（实部或虚部）。
