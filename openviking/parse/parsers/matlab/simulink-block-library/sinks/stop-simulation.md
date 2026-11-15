---
type: simulink-block
title: 'Stop Simulation'
family: sinks
languages: [en, zh-CN]
chinese_source: official
documentation_release: R2025b
official_category: 'Sinks'
documentation_page: 'stopsimulation'
---

# Stop Simulation

Stop simulation when input is nonzero

## 中文

当输入为非零值时使仿真停止

### 所属库

Simulink / Sinks HDL Coder / Sinks

### 描述

当输入为非零值时，Stop Simulation 模块将使仿真停止。在停止之前，仿真会完成当前时间步。如果模块的输入为向量，则任何非零的向量元素都会导致仿真停止。

如果您在 For Iterator 子系统中使用 Stop Simulation 模块，停止操作将在执行完子系统在一个时间步中的*所有*迭代之后发生。在下一个时间步开始之前，停止操作不会中断仿真。

您不能使用 Stop Simulation 模块暂停仿真。要创建暂停仿真的模块，请参阅使用 Assertion 模块暂停仿真。

### 端口

#### 输入

#### **Port\_1** — 输入信号 标量 | 向量 | 矩阵

当输入信号为非零值时使仿真停止。此端口接受 `double` 或 `Boolean` 数据类型的实信号。

**数据类型:** `double` | `Boolean`

### 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` |
| **直接馈通** | `否` |
| **多维信号** | `否` |
| **可变大小信号** | `否` |
| **过零检测** | `否` |

### 扩展功能

#### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 代码和 C++ 代码。

不建议用于生产代码。涉及到嵌入式系统中常见的资源限制以及对速度和内存的限制。生成的代码可以包含内存的动态分配和释放、递归、额外的内存开销以及长短不等的执行时间。虽然代码在功能上有效并且在资源丰富的环境中可接受，但较小的嵌入式目标通常不能支持此类代码。通常情况下，模块会向适合生产代码的方向发展。因此，适合生产代码的模块仍然适用。

当停止条件为 true 时，生成的代码停止执行。

#### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| **无 HDL** | 不为此模块生成 HDL 代码。 |

**HDL 模块属性**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | 控制是否删除未连接的逻辑。默认值为 `off`，这意味着未连接的逻辑不会保留在 HDL 代码中。有关详细信息，请参阅PreserveUpstreamLogic (HDL Coder)。 |

#### PLC 代码生成 使用 Simulink® PLC Coder™ 生成结构化文本代码。

### 版本历史记录

**在 R2006a 之前推出**

## Libraries

Simulink / Sinks HDL Coder / Sinks

## Description

The Stop Simulation block stops the simulation when the input is
nonzero. The simulation completes the current time step before terminating. If the block
input is a vector, any nonzero vector element causes the simulation to stop.

When you use the Stop Simulation block in a For Iterator subsystem, the stop action
occurs after execution of *all* iterations in the subsystem during a
time step. The stop action does not interrupt execution until the start of the next time
step.

You cannot use the Stop Simulation block to pause the simulation. To
create a block that pauses the simulation, see Pause Simulation Using Assertion Blocks.

## Ports

### Input

### **Port\_1** — Input signal scalar | vector | matrix

Stop simulation when input signal is nonzero. This port accepts real
signals of `double` or `Boolean` data
types.

**Data Types:** `double` | `Boolean`

## Block Characteristics

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` |
| **Direct Feedthrough** | `no` |
| **Multidimensional Signals** | `no` |
| **Variable-Size Signals** | `no` |
| **Zero-Crossing Detection** | `no` |

## Extended Capabilities

### C/C++ Code Generation Generate C and C++ code using Simulink® Coder™.

Not recommended for production code. Relates to resource limits and restrictions
on speed and memory often found in embedded systems. Generated code can contain
dynamic allocation and freeing of memory, recursion, additional memory overhead, and
widely varying execution times. While the code is functionally valid and acceptable
in resource-rich environments, smaller embedded targets often cannot support such
code. Usually, blocks evolve toward being suitable for production code. Thus, blocks
suitable for production code remain suitable.

Generated code stops executing when the stop condition is true.

### HDL Code Generation Generate VHDL, Verilog and SystemVerilog code for FPGA and ASIC designs using HDL Coder™.

**HDL Architecture**

| Architecture | Description |
| --- | --- |
| `No HDL` | Do not generate HDL code for this block. |

**HDL Block Properties**

|  |  |
| --- | --- |
| **PreserveUpstreamLogic** | Control the removal of unconnected logic. The default is `off`, which means unconnected logic is not preserved in HDL code. For more details, see PreserveUpstreamLogic (HDL Coder). |

### PLC Code Generation Generate Structured Text code using Simulink® PLC Coder™.

## Version History

**Introduced before R2006a**
