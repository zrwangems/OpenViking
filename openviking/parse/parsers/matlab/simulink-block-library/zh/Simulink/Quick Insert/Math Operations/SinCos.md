---
type: simulink-block
title: 'SinCos'
family: 'hdlcoder'
product_id: 'simulink'
product_name: 'Simulink'
documentation_release: R2025b
official_category: 'HDL Floating Point Operations'
documentation_page: 'sincos'
documentation_source_path: '../hdlcoder/ref/sincos.html'
language: zh-CN
chinese_source: worker-translation
---

# SinCos

## 端口

### 输入

### **dataIn** — 输入数据信号 标量 | 向量

用于计算正弦和余弦函数的输入数据信号，指定为标量或向量。输入值范围为 -2π 到 2\*π。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

### **validIn** — 输入控制信号是否有效 标量

输入控制信号，用于指示输入信号是否有效，指定为标量。

**数据类型：** `Boolean`
### 输出

### **sinOut** — 正弦输出数据信号 标量 | 向量

输出数据信号，为输入信号的正弦，返回为标量或向量。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

### **cosOut** — 余弦输出数据信号 标量 | 向量

输出数据信号，为输入信号的余弦，返回为标量或向量。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

### **validOut** — 输出控制信号是否有效 标量

输出控制信号，用于指示输出信号是否有效，返回为标量。

**数据类型：** `Boolean`

## 参数

### **迭代次数** — CORDIC 算法的迭代次数 `11` (默认) | `positive Integer`

指定 CORDIC 算法的迭代次数。

#### 程序化使用

|  |
| --- |
| **模块参数**：`iter` |
| **类型**：character vector |
| **值**：`Integer values` |
| **默认**：`'11'` |

### **延迟策略** — 延迟策略 `Max` (默认) | `Min` | `Custom` | `Custom(PerIteration)` | `Zero`

指定使用最小、最大、自定义还是零延迟。有关更多信息，请参阅延迟策略。

要为该模块使用自定义延迟，请将 **延迟策略** 设置为 `Custom`，然后在 **自定义延迟** 字段中输入延迟值。

您还可以控制迭代算法的流水线级数。要为迭代算法自定义延迟，请将 **延迟策略** 设置为 `Custom(PerIteration)`，然后在 **IterationsPerPipeline** 字段中输入每个流水线的迭代值。*(自 R2025a 起)*

#### 程序化使用

|  |
| --- |
| **模块参数**：`latencyMode` |
| **类型**：character vector |
| **值**：`'Max'` | `'Min'` | `'Custom'` | `'Custom(PerIteration)'` | `'Zero'` |
| **默认**：`'Max'` |

### **自定义延迟** — 自定义延迟 0 (默认) | `positive Integer`

指定自定义延迟值。延迟必须为范围 [0, *L*] 中的非负整数，其中 *L* 是 SinCos 模块的最大延迟值。有关更多信息，请参阅 CustomLatency。

#### 依赖关系

要启用此参数，请将 **延迟策略** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`customLatencyValue` |
| **类型**：Integer |
| **值**：`0 to Max latency` |
| **默认**：`0` |

### **IterationsPerPipeline** — 每个流水线迭代次数 `1` (默认) | `positive integer`

*自 R2025a 起*

指定算法中每个流水线级使用的迭代次数。

#### 依赖关系

要启用此参数，请将 **延迟策略** 设置为 `Custom(PerIteration)`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`iterationsPerPipelineValue` |
| **类型**：Integer |
| **值**：`Positive integer` |
| **默认**：`1` |

## 所属库

HDL Coder

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

该模块支持使用 HDL Coder™ 进行 HDL 代码生成。HDL Coder 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `Module` (默认) | 为子系统及其中的模块生成代码。 |
| `BlackBox` | 生成黑盒接口。生成的 HDL 代码仅包含子系统的输入/输出端口定义。因此，您可以在模型中使用子系统，为现有的手写 HDL 代码生成接口。  子系统的黑盒接口生成类似于 Model 模块接口生成，但不包含时钟信号。 |
| `No HDL` | 从生成的代码中移除子系统。您可以在仿真中使用该子系统，但在 HDL 代码中将其视为“空操作”。 |

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **AdaptivePipelining** | 基于综合工具、目标频率和乘法器字长自动插入流水线。默认值为 `inherit`。另请参阅 AdaptivePipelining。 |
| **BalanceDelays** | 检测沿一条路径引入的新延迟，并在其他路径上插入匹配的延迟。默认值为 `inherit`。另请参阅 BalanceDelays。 |
| **ClockRatePipelining** | 以更快的时钟速率而不是较慢的数据速率插入流水线寄存器。默认值为 `inherit`。另请参阅 ClockRatePipelining。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分布这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **DistributedPipelining** | 流水线寄存器分布，或寄存器重定时。默认值为 `inherit`。另请参阅 DistributedPipelining。 |
| **DSPStyle** | 用于乘法器映射的综合属性。默认值为 `none`。另请参阅 DSPStyle。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中移除子系统层级。默认值为 `inherit`。另请参阅 FlattenHierarchy。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |
| **SharingFactor** | 映射到单个共享资源的等效功能资源数量。默认值为 0。另请参阅 Resource Sharing。 |
| **StreamingFactor** | 被时间复用以转换为串行、标量数据路径的并行数据路径或向量的数量。默认值为 0，实现完全并行的数据路径。另请参阅 Streaming。 |

**目标规范**

此模块不能为 DUT，因此 **目标规范** 选项卡中的模块属性设置将被忽略。

**限制**

- 不能在 Synchronous Subsystem 模块中使用此模块。
- 该模块不支持资源共享优化。

## 版本历史

**在 R2020b 中引入**

### R2025a：控制每次迭代的流水线级数

您可以通过将 **LatencyStrategy** 参数 HDL 设置为 `Custom(PerIterations)`，然后使用 **IterationsPerPipeline** 参数指定每次迭代的流水线级数，来控制迭代算法的流水线级数。使用此设置可以控制生成代码中的流水线级数，并针对速度和资源利用率优化设计。

## 描述

使用 CORDIC 近似方法计算 SinCos 运算，并带延迟仿真

HDL 数学正弦模块

SinCos 模块使用坐标旋转数字计算机（CORDIC）近似方法计算输入信号的正弦和余弦。有关更多信息，请参阅算法中的 CORDIC 近似方法。该模块具有控制信号，用于指示输入和输出数据是否有效。您还可以指定算法的迭代次数和延迟策略。

要在 Simulink® 模型中使用此模块，请在 MATLAB® Command Window 中输入此命令以打开 `HDLMathLib` 库：

    open_system('HDLMathLib')

您可以带延迟仿真 SinCos 模块。有关更多信息，请参阅延迟注意事项。
