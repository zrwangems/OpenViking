---
type: simulink-block
title: 'Real-Imag to Complex'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Math Operations'
documentation_page: 'realimagtocomplex'
documentation_source_path: 'slref/realimagtocomplex.html'
language: zh-CN
chinese_source: official
---

# Real-Imag to Complex

## 端口

### 输入

### **Re** — 复数输出的实部 标量 | 向量 | 矩阵

要转换为复数值输出信号的实数值，指定为标量、向量或矩阵。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`

### **Im** — 复数输出的虚部 标量 | 向量 | 矩阵

要转换为复数值输出信号的虚数值，指定为标量、向量或矩阵。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`

### **Port\_1** — 复数输出的实部或虚部 标量 | 向量 | 矩阵

要转换为复数输出信号的实数或虚数值，指定为有限标量、向量或矩阵。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point` | `bus`
### 输出

### **Port\_1** — 复信号 标量 | 向量 | 矩阵

复信号，由实数和虚数值构成。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **输入** — 实数输入，虚数输入，或两者同时存在 **实部** (默认) | **虚部** | **实部和虚部**

指定输入的类型：实数输入、虚数输入或者两者同时存在。

#### 编程用法

|  |
| --- |
| **模块参数**：`Input` |
| **类型：**字符向量 |
| **值：**`'Real and imag' | 'Real' | 'Imag'` |
| **默认值：**`'Real and imag'` |

### **虚部** — 复数输出的虚部 `0` (默认) | 有限标量、向量或矩阵

指定将输入转换为复数值输出信号时使用的虚数值。

#### 依赖关系

要启用此参数，请将**输入**设置为**实部**。

#### 编程用法

|  |
| --- |
| **模块参数**：`ConstantPart` |
| **类型：**字符向量 |
| **值：**虚数值 |
| **默认值：**`'0'` |

### **实部** — 复数输出的实部 `0` (默认) | 有限标量、向量或矩阵

指定将输入转换为复数值输出信号时使用的常量实数值。

#### 依赖关系

要启用此参数，请将**输入**设置为**虚部**。

#### 编程用法

|  |
| --- |
| **模块参数**：`ConstantPart` |
| **类型：**字符向量 |
| **值：**有限实数值标量、向量或矩阵 |
| **默认值：**`'0'` |

### **采样时间(-1 表示继承)** — 采样之间的时间间隔 `-1` (默认) | 标量 | 向量

指定采样时间间隔。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

#### 依赖关系

仅当您将此参数设置为 `-1` 以外的值时才可见。要了解详细信息，请参阅不建议设置采样时间的模块。

#### 编程用法

要以编程方式设置模块参数值，请使用 `set_param` 函数。

|  |  |
| --- | --- |
| **参数:** | `SampleTime` |
| **值:** | `"-1"` (默认) | scalar or vector in quotes |

## 所属库

Simulink / Math Operations HDL Coder / Math Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中现有延迟的方式来放置在输出端的寄存器的数量。分布式流水线不会重新分发这些寄存器。默认值为 `0`。有关详细信息，请参阅ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线阶段数。分布式流水线和受限输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅OutputPipeline (HDL Coder)。 |

**复数数据支持**

此模块支持复信号的代码生成。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

将实和/或虚输入转换为复信号

Real-Imag to Complex 模块将实和/或虚输入转换为具有复数值的输出信号。

这两个输入可以都是具有相同维度的数组（向量或矩阵）；也可以是一个输入为数组，另一个输入为标量。如果模块具有数组输入，则输出是具有相同维度的复数数组。实数输入的元素映射到对应的复数输出元素的实部。同样，虚数输入映射到复数输出信号的虚部。如果一个输入是标量，它将映射到所有复数输出信号的对应分量（实部或虚部）。
