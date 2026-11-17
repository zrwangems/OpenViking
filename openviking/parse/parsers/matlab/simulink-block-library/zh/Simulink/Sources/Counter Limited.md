---
type: simulink-block
title: 'Counter Limited'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'Sources'
documentation_page: 'counterlimited'
documentation_source_path: 'slref/counterlimited.html'
language: zh-CN
chinese_source: worker-translation
---

# Counter Limited

## 端口
```yaml
ports:
- name: Port_1
  summary: 计数值标量
  direction: output
  data_types: uint8 | uint16 | uint32 | uint64 | fixed point
```

### 输出

### **Port\_1** — 计数值标量

计数值，以 8 位、16 位、32 位、64 位或 ufix128 的无符号整数形式返回。该模块使用表示上限所需的最小位数。

**数据类型：** `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`
## 参数
```yaml
parameters:
- name: Upper limit
  summary: 上限 7（默认）| 标量
  group: ''
  block_parameter: uplimit
  type: character vector
  values: scalar
  default: '''7'''
- name: Sample time
  summary: 采样之间的间隔 -1（默认）| 标量 | 向量
  group: ''
  block_parameter: tsamp
  type: character vector
  values: scalar | vector
  default: '''-1'''
```

### **Upper limit** — 上限 `7`（默认）| 标量

将模块计数到的上限指定为有限实值标量。

#### 编程使用

|  |
| --- |
| **模块参数**：`uplimit` |
| **类型**：character vector |
| **值**：scalar |
| **默认值**：`'7'` |

### **Sample time** — 采样之间的间隔 `-1`（默认）| 标量 | 向量

将采样之间的时间间隔指定为标量（`sampling
period`），或双元素向量（`sampling period,
initial offset`）。要继承采样时间，请将此参数设置为 `-1`。有关详细信息，请参阅 Specify Sample Time。

#### 编程使用

|  |
| --- |
| **模块参数**：`tsamp` |
| **类型**：character vector |
| **值**：scalar | vector |
| **默认值**：`'-1'` |
## 所属库

Simulink / Sources HDL Coder / Sources

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `fixed point` | `integer` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

- 代码生成器不会在生成的代码中显式地将构成非原子掩码子系统模块的图元模块分组。这种灵活性允许更高效的代码生成。在某些情况下，您可以通过选择 **Treat as atomic
  unit** 选项将掩码子系统模块配置为作为原子单元执行来实现分组。
- 不推荐用于生产代码。涉及嵌入式系统中常见的资源限制以及速度和内存限制。生成的代码可能包含动态内存分配和释放、递归、额外的内存开销以及变化很大的执行时间。虽然代码在功能上是有效的，并且在资源丰富的环境中通常可以接受，但较小的嵌入式目标通常无法支持此类代码。通常，模块会逐渐演变为适合生产代码。因此，适合生产代码的模块仍然适合。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

计数到指定上限后回绕到零

Counter Limited 模块向上计数，直到达到指定的上限。然后计数器回绕到零，并重新开始向上计数。计数器始终初始化为零。

**注意**

此模块在仿真期间不会报告溢出回绕警告。要报告这些警告，请参阅 `Simulink.restoreDiagnostic`
参考页。该模块确实会报告因溢出回绕而导致的错误。
