---
type: simulink-block
title: 'Unary Minus'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Floating Point Operations'
documentation_page: 'unaryminus'
documentation_source_path: '../simulink/slref/unaryminus.html'
language: zh-CN
chinese_source: worker-translation
---

# Unary Minus

## 端口
```yaml
ports:
- name: Port_1
  summary: 要求负的信号 标量 | 向量 | 矩阵 | N 维数组
  direction: input
  data_types: half | single | double | int8 | int16 | int32 | int64 | fixed point
- name: Port_1
  summary: 输入信号的负值 标量 | 向量 | 矩阵 | N 维数组
  direction: output
  data_types: half | single | double | int8 | int16 | int32 | int64 | fixed point
```

### 输入

### **Port\_1** — 要求负的信号 标量 | 向量 | 矩阵 | N 维数组

输入信号，指定为标量、向量、矩阵或 N 维数组。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
### 输出

### **Port\_1** — 输入信号的负值 标量 | 向量 | 矩阵 | N 维数组

输入信号的负值。输出与输入具有相同的数据类型和维度。

**数据类型：** `half` | `single` | `double` | `int8` | `int16` | `int32` | `int64` | `fixed point`
## 参数
```yaml
parameters:
- name: Saturate on integer overflow
  summary: 溢出操作的方法 off（默认）| on
  group: ''
  block_parameter: SaturateOnIntegerOverflow
  type: character vector
  values: '''off'' | ''on'''
  default: '''off'''
- name: Sample time (-1 for inherited)
  summary: 采样之间的间隔 -1（默认）| 标量 | 向量
  group: ''
  block_parameter: SampleTime
  values: '"-1"（默认）| 带引号的标量或向量'
```

### **Saturate on integer overflow** — 溢出操作的方法 `off`（默认）| `on`

选择此项以使整数溢出饱和。否则，溢出将回绕。

当您选中此复选框时，饱和将应用于模块上的每个内部操作，而不仅仅是输出或结果。通常，代码生成过程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

对于有符号整数数据类型，最负值的负值无法由该数据类型表示。在这种情况下，**Saturate on integer overflow** 复选框控制模块的行为：

| 参数设置 | 模块行为 | 示例 |
| --- | --- | --- |
| **Saturate on integer overflow** = `on` | 值饱和到整数数据类型的最大正值 | - 对于 8 位有符号整数，-128 映射到   127。 - 对于 16 位有符号整数，-32768 映射到   32767。 - 对于 32 位有符号整数，-2147483648 映射   到 2147483647。 |
| **Saturate on integer overflow** = `off` | 值回绕到整数数据类型的最负值 | - 对于 8 位有符号整数，-128 保持为   -128。 - 对于 16 位有符号整数，-32768 保持为   -32768。 - 对于 32 位有符号整数，-2147483648   保持为 -2147483648。 |

#### 编程使用

|  |
| --- |
| **模块参数**：`SaturateOnIntegerOverflow` |
| **类型**：character vector |
| **值**：`'off' | 'on'` |
| **默认值**：`'off'` |

### **Sample time (-1 for inherited)** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

指定采样之间的时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 依赖关系

仅当您将其设置为 `-1` 以外的值时，此参数才可见。要了解更多信息，请参阅 Blocks for Which Sample Time Is Not Recommended。

#### 编程使用

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **Parameter:** | `SampleTime` |
| **值**：| `"-1"`（默认）| 带引号的标量或向量 |
## 所属库

Simulink / Math Operations HDL Coder / HDL Floating Point Operations HDL Coder / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `double` | `fixed pointa` | `half` | `integera` | `single` |
| **Direct Feedthrough** | `yes` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |
|  |  |
| --- | --- |
| a 此模块仅支持有符号定点数据类型。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线阶段数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线阶段数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复数信号的代码生成。

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

此模块仅支持有符号定点数据类型。

## 版本历史

**在 R2006a 之前引入**

## 描述

对输入求负

Unary
Minus
模块对输入求负。
