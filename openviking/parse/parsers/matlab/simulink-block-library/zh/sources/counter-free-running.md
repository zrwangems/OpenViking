---
type: simulink-block
title: 'Counter Free-Running'
family: sources
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'counterfreerunning'
language: zh-CN
chinese_source: official
---

# Counter Free-Running

进行累加计数并在达到指定位数的最大值后溢出归零

## 所属库

Simulink / Sources HDL Coder / Sources

## 描述

Counter Free-Running 模块进行累加计数，直到达到最大值 2*Nbits* – 1，其中 *Nbits* 是位数。然后，该计数器将溢出归零并重新开始进行累加计数。

溢出之后，该计数器始终初始化为零。但是，如果您选择全局双精度值覆盖， Counter Free-Running 模块不会绕回到零。

**注意**

仿真期间，此模块不会报告溢出绕回警告。要报告这些警告，请参阅 `Simulink.restoreDiagnostic` 参考页。但此模块会报告由于溢出绕回而导致的错误。

## 端口

### 输出

### **Port\_1** — 计数值 标量

计数值，以无符号整数形式返回，长度由**位数**参数指定。当位数不是 8、16、32 或 64 时，输出类型是无符号定点数据类型。

**数据类型:** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **位数** — 位数 `16` (默认) | 标量

将位数指定为有限实数值。如果您指定：

- 正整数，例如 `8`，则该模块的最大计数为 `28 – 1`，即 `255`。
- 无符号整数表达式，例如 `uint8(8)`，则该模块的最大计数为 `uint8(2uint8(8) – 1)`，即 `254`。

#### 编程用法

|  |
| --- |
| **模块参数**：`NumBits` |
| **类型：**字符向量 |
| **值：**标量 |
| **默认值：**`'16'` |

### **采样时间** — 采样之间的时间间隔 `-1` (默认) | 标量 | 向量

将采样之间的时间间隔指定为标量 (`sampling period`) 或二元素向量 (`[sampling period, initial offset]`)。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅指定采样时间。

#### 编程用法

|  |
| --- |
| **模块参数**：`tsamp` |
| **类型：**字符向量 |
| **值：**标量 | 向量 |
| **默认值：**`'-1'` |

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `fixed point` | `integer` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不建议用于生产代码。涉及到嵌入式系统中常见的资源限制以及对速度和内存的限制。生成的代码可以包含动态分配和释放内存、递归、额外的内存开销以及长短不等的执行时间。虽然代码在功能上有效并且在资源丰富的环境中通常可接受，但较小的嵌入式目标通常不能支持此类代码。通常情况下，模块会向适合生产代码的方向发展。因此，适合生产代码的模块仍然适用。

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

## 版本历史记录

**在 R2006a 之前推出**
