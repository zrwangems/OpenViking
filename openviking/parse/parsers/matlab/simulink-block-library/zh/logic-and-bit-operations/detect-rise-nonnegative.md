---
type: simulink-block
title: 'Detect Rise Nonnegative'
family: logic-and-bit-operations
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'detectrisenonnegative'
language: zh-CN
chinese_source: official
---

# Detect Rise Nonnegative

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

每当信号值增加到非值时，输出信号就表示出现上升沿，而其之前的值严格为负。输出可以是标量、向量或矩阵。

- 当输入信号大于或等于零，且其先前值小于零时，输出为真（等于 `1`）。
- 当输入信号小于零时，或者如果输入信号为非负，则其先前的值也是非负的，则输出为假（等于 `0`）。

**数据类型:** `uint8` | `Boolean`

## 参数

### **初始条件** — 布尔表达式 `U/z >= 0` 的初始条件 `0` (默认) | 标量 | 向量 | 矩阵

设置布尔表达式 `U/z >= 0` 的初始条件。

#### 编程用法

|  |
| --- |
| **模块参数**：`vinit` |
| **类型：**字符向量 |
| **值：**标量 | 向量 | 矩阵 |
| **默认值：**`'0'` |

### **输入处理** — 指定基于采样或基于帧的处理 **元素作为通道(基于采样)** (默认) | **列作为通道(基于帧)**

指定模块是执行基于采样还是基于帧的处理：

- **列作为通道(基于帧)** - 将输入信号的每一列视为一个单独的通道（基于帧的处理）。

  **注意**

  基于帧的处理需要具有 DSP System Toolbox™ 许可证。

  有关详细信息，请参阅Sample- and Frame-Based Concepts (DSP System Toolbox)。
- **元素作为通道(基于采样)** - 将输入信号的每个元素视为一个单独的通道（基于采样的处理）。

可以使用**输入处理**指定模块是执行基于采样的处理还是基于帧的处理。有关这两种处理模式的详细信息，请参阅Sample- and Frame-Based Concepts (DSP System Toolbox)。

#### 编程用法

|  |
| --- |
| **模块参数**：`InputProcessing` |
| **类型**：字符向量 |
| **值**：`'Columns as channels (frame based)'` | `'Elements as channels (sample based)'` |
| **默认值**：`'Elements as channels (sample based)'` |

### **输出数据类型** — 输出数据类型 `boolean` (默认) | `uint8`

将输出数据类型指定为 `boolean` 或 `uint8`。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型：**字符向量 |
| **值：**`'boolean' | 'uint8'` |
| **默认值：**`'boolean'` |

## 所属库

Simulink / Logic and Bit Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `是` |
| **多维信号** | `是` |
| **可变大小信号** | `是` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

生成的代码在特定条件下依赖于 `memcpy` 或 `memset` 函数 (`string.h`)。

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

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

当信号值增加到非值时检测上升沿，并且其先前的值严格为负

Detect Rise Nonnegative 模块确定输入是否大于或等于零，并且其先前的值是否小于零。

- 当输入信号大于或等于零，且其先前值小于零时，输出为真（等于 `1`）。
- 当输入信号小于零时，或者如果输入信号为非负，则其先前的值也是非负的，则输出为假（等于 `0`）。

此模块仅支持离散采样时间。
