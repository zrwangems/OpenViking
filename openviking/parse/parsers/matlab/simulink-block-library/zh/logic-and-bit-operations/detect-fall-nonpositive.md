---
type: simulink-block
title: 'Detect Fall Nonpositive'
family: logic-and-bit-operations
documentation_release: R2025b
official_category: 'Logic and Bit Operations'
documentation_page: 'detectfallnonpositive'
language: zh-CN
chinese_source: worker-translation
---

# Detect Fall Nonpositive

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

输入信号，指定为标量、向量或矩阵。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出信号 标量 | 向量 | 矩阵

检测下降沿的输出信号，指定为标量、向量或矩阵。

- 当输入信号小于或等于零，且其先前值大于零时，输出为 true（等于 `1`）。
- 当输入信号大于零，或者如果其为非正值且其先前值也为非正值时，输出为 false（等于 `0`）。

**数据类型：** `uint8` | `Boolean`

## 参数

### **初始条件** — 布尔表达式 `U/z <= 0` 的初始条件 0（默认） | 标量 | 向量 | 矩阵

设置布尔表达式 `U/z <= 0` 的初始条件。

#### 程序化使用

|  |
| --- |
| **模块参数：** `vinit` |
| **类型：** character vector |
| **值：** 标量 | 向量 | 矩阵 |
| **默认：** `'0'` |

### **输入处理** — 指定基于采样或基于帧的处理 `Elements as channels (sample based)`（默认） | `Columns as channels (frame based)`

指定该模块执行基于采样还是基于帧的处理：

- `Columns as channels (frame based)` — 将输入的每一列视为单独通道（基于帧的处理）。

  **注意**

  基于帧的处理需要 DSP System Toolbox™ 许可证。

  有关详细信息，请参阅 Sample- and Frame-Based Concepts (DSP System Toolbox)。
- `Elements as channels (sample based)` — 将输入的每个元素视为单独通道（基于采样的处理）。

使用 **输入处理** 指定该模块执行基于采样还是基于帧的处理。有关这两种处理模式的详细信息，请参阅 Sample- and Frame-Based Concepts (DSP System Toolbox)。

#### 程序化使用

|  |
| --- |
| **模块参数**： `InputProcessing` |
| **类型**： character vector |
| **值**： `'Columns as channels (frame based)'` | `'Elements as channels (sample based)'` |
| **默认**： `'Elements as channels (sample based)'` |

### **输出数据类型** — 输出数据类型 `boolean`（默认） | `uint8`

将输出数据类型指定为 `boolean` 或 `uint8`。

#### 程序化使用

|  |
| --- |
| **模块参数：** `OutDataTypeStr` |
| **类型：** character vector |
| **值：** `'boolean' | 'uint8'` |
| **默认：** `'boolean'` |

## 所属库

Simulink / 逻辑和位运算

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `yes` |
| **多维信号** | `yes` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖 `memcpy` 或 `memset` 函数（`string.h`）。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供额外配置选项，这些选项会影响 HDL 实现和综合逻辑。

**HDL 架构**

此模块有一种默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计中移动现有延迟，放置在输出处的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入生成代码中的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入生成代码中的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成 Structured Text 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

当信号值下降到非正值，且其先前值严格为正时，检测下降沿

Detect Fall Nonpositive 模块判断输入是否小于或等于零，且其先前值大于零。

- 当输入信号小于或等于零，且其先前值大于零时，输出为 true（等于 `1`）。
- 当输入信号大于零，或者如果其为非正值且其先前值也为非正值时，输出为 false（等于 `0`）。

此模块仅支持离散采样时间。
