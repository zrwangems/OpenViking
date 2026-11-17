---
type: simulink-block
title: 'Counter Free-Running'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'counterfreerunning'
documentation_source_path: '../simulink/slref/counterfreerunning.html'
language: zh-CN
chinese_source: worker-translation
---

# Counter Free-Running

## 端口

### 输出

### **Port\_1** — 计数值标量

计数值，以无符号整数形式返回，其长度由 **Number of Bits** 参数指定。当位数不是 8、16、32 或 64 时，输出类型为无符号定点数据类型。

**数据类型：** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

## 参数

### **Number of Bits** — 位数 `16`（默认）| 标量

将位数指定为有限实数。当您指定：

- 正整数，例如 `8`，模块计数到 `28 – 1`，即 `255`。
- 无符号整数表达式，例如 `uint8(8)`，模块计数到 `uint8(2uint8(8) – 1)`，即 `254`。

#### 编程使用

|  |
| --- |
| **模块参数：** `NumBits` |
| **类型：** 字符向量 |
| **值：** 标量 |
| **默认：** `'16'` |

### **Sample time** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

将采样之间的时间间隔指定为标量（`采样周期`），或二元素向量（`[采样周期, 初始偏移]`）。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 编程使用

|  |
| --- |
| **模块参数：** `tsamp` |
| **类型：** 字符向量 |
| **值：** 标量 | 向量 |
| **默认：** `'-1'` |

## 所属库

Simulink / Sources HDL Coder / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `fixed point` | `integer` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

不建议用于生产代码。涉及嵌入式系统中常见的资源限制以及速度和内存限制。生成的代码可能包含动态内存分配和释放、递归、额外内存开销以及变化很大的执行时间。虽然代码在功能上是有效的，并且在资源丰富的环境中通常可以接受，但较小的嵌入式目标通常无法支持此类代码。通常，模块会逐步演变为适合生产代码。因此，适合生产代码的模块仍然适合。

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

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

在达到指定位数的最大值后向上计数并溢出回零

Counter Free-Running 模块向上计数直到达到最大值 2*Nbits* – 1，其中 *Nbits* 是位数。然后计数器溢出到零并重新开始向上计数。

溢出后，计数器始终初始化为零。但是，如果您选择全局双精度覆盖，Counter Free-Running 模块不会回绕到零。

**注意**

此模块在仿真期间不会报告溢出回绕警告。要报告这些警告，请参阅 `Simulink.restoreDiagnostic` 参考页。此模块确实会报告因溢出回绕导致的错误。
