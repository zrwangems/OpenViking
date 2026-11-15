---
type: simulink-block
title: 'rSqrt'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Code Generation from Simulink / Model and Architecture Design / Model Design / Basic HDL Algorithms / HDL Math Library'
documentation_page: 'rsqrt'
documentation_source_path: 'ref/rsqrt.html'
language: zh-CN
chinese_source: worker-translation
---

# rSqrt

## 端口

### 输入

### **dataIn** — 输入数据信号 标量 | 向量

用于计算倒数平方根的输入信号，指定为标量或向量。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **validIn** — 输入控制信号是否有效 标量

输入控制信号，指示输入信号是否有效，指定为标量。

**数据类型：** `Boolean`
### 输出

### **dataOut** — 输出数据信号 标量 | 向量

输出信号，是输入信号的倒数平方根，以标量或向量形式返回。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

### **validOut** — 输出控制信号是否有效 标量

输出控制信号，指示输出信号是否有效，以标量形式返回。

**数据类型：** `Boolean`

## 参数

### **Architecture** — 使用的架构 `RecipSqrtNewtonSingleRate`（默认）

选择 rSqrt 模块的架构。

#### 程序化使用

|  |
| --- |
| **模块参数**：`architecture` |
| **类型**：character vector |
| **值**：`RecipSqrtNewtonSingleRate` |
| **默认值**：`'RecipSqrtNewtonSingleRate'` |

### **Number of iterations** — 使用的迭代次数 `3`（默认）| `Integer`

指定 rSqrt 算法的迭代次数。

#### 程序化使用

|  |
| --- |
| **模块参数**：`numOfIterations` |
| **类型**：character vector |
| **值**：`Integer values` |
| **默认值**：`'3'` |

### **Latency strategy** — 延迟策略 `Max`（默认）| `Min` | `Custom` | `Custom(PerIteration)` | `Zero`

指定使用最小、最大、自定义还是零延迟。有关详细信息，请参阅延迟策略。

要为模块使用自定义延迟，请将 **Latency strategy** 设置为 `Custom`，并在 **Custom latency** 字段中输入延迟值。

您还可以控制迭代算法的流水线级数。要自定义迭代算法的延迟，请将 **Latency strategy** 设置为 `Custom(PerIteration)`，并在 **IterationsPerPipeline** 字段中输入每个流水线的迭代值。*（自 R2025a 起）*

#### 程序化使用

|  |
| --- |
| **模块参数**：`latencyMode` |
| **类型**：character vector |
| **值**：`'Max'` | `'Min'` | `'Custom'` | `'Custom(PerIteration)'` | `'Zero'` |
| **默认值**：`'Max'` |

### **Custom latency** — 指定自定义延迟值 0（默认）

当将 **Latency strategy** 设置为 `Custom` 时，使用此参数指定自定义延迟值。延迟必须是范围 [0, *L*] 内的非负整数，其中 *L* 是 rSqrt 模块的最大延迟值。有关详细信息，请参阅 CustomLatency。

#### 依赖关系

要使用此参数，请将 **Latency strategy** 设置为 `Custom`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`customLatencyValue` |
| **类型**：Integer |
| **值**：`0 to Max latency` |
| **默认值**：`0` |

### **IterationsPerPipeline** — 每个流水线的迭代次数 `1`（默认）| `positive integer`

*自 R2025a 起*

指定算法中每个流水线级要使用的迭代次数。

#### 依赖关系

要启用此参数，请将 **Latency strategy** 设置为 `Custom(PerIteration)`。

#### 程序化使用

|  |
| --- |
| **模块参数**：`iterationsPerPipelineValue` |
| **类型**：Integer |
| **值**：`Positive integer` |
| **默认值**：`1` |

### **Output data type** — 选择模块的输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as first input` | `Inherit: Inherit via back propagation` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

指定输出数据类型。该数据类型可以继承或直接指定。

#### 程序化使用

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：character vector |
| **值**：`'Inherit: Inherit via internal rule'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `fixdt(1,16,0)` | `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Saturate on integer overflow** — 选择整数溢出时的行为 `off`（默认）| `on`

| 操作 | 采取此操作的原因 | 溢出时会发生什么 | 示例 |
| --- | --- | --- | --- |
| 选中此复选框。 | 您的模型可能发生溢出，并且您希望在生成的代码中具有显式饱和保护。 | 溢出饱和到数据类型可表示的最小值或最大值。 | `int8`（有符号 8 位整数）数据类型可表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。选中该复选框后，模块输出饱和在 127。类似地，模块输出饱和在最小输出值 -128。 |
| 不选中此复选框。 | 您希望优化生成代码的效率。您希望避免过度指定模块处理超出范围信号的方式。有关详细信息，请参阅 Troubleshoot Signal Range Errors。 | 溢出回绕为数据类型可表示的值。 | `int8`（有符号 8 位整数）数据类型可表示的最大值为 127。任何大于此最大值的模块运算结果都会导致 8 位整数溢出。清除该复选框后，软件将导致溢出的值解释为 `int8`，这可能会产生意外结果。例如，模块结果 130（二进制 1000 0010）表示为 `int8` 时是 -126。 |

选中此复选框时，饱和适用于模块上的每个内部运算，而不仅仅是输出或结果。通常，代码生成过程可以检测到何时不可能发生溢出。在这种情况下，代码生成器不会生成饱和代码。

#### 程序化使用

|  |
| --- |
| **模块参数**：`SaturateOnIntegerOverflow` |
| **类型**：character vector |
| **值**：`'off'` | `'on'` |
|  |
| **默认值**：`'off'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** character vector |
| **值：** `'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'Round' | 'Simplest' | 'Zero'` |
| **默认值：** `'Floor'` |

## 所属库

HDL Coder

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

该模块支持使用 HDL Coder™ 进行 HDL 代码生成。HDL Coder 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `Module`（默认） | 为子系统及子系统内的模块生成代码。 |
| `BlackBox` | 生成黑盒接口。生成的 HDL 代码仅包含子系统的输入/输出端口定义。因此，您可以使用模型中的子系统生成到现有手动编写的 HDL 代码的接口。子系统的黑盒接口生成类似于 Model 模块接口生成，但不含时钟信号。 |
| `No HDL` | 从生成的代码中移除该子系统。但是，您可以在仿真中使用该子系统，在 HDL 代码中将其视为“无操作”。 |

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **AdaptivePipelining** | 基于综合工具、目标频率和乘法器字长的自动流水线插入。默认值为 `inherit`。另请参阅 AdaptivePipelining。 |
| **BalanceDelays** | 检测沿一条路径引入的新延迟，并在其他路径上插入匹配的延迟。默认值为 `inherit`。另请参阅 BalanceDelays。 |
| **ClockRatePipelining** | 以更快的时钟速率而不是较慢的数据速率插入流水线寄存器。默认值为 `inherit`。另请参阅 ClockRatePipelining。 |
| **ConstrainedOutputPipeline** | 通过移动设计中的现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **DistributedPipelining** | 流水线寄存器分布或寄存器重定时。默认值为 `inherit`。另请参阅 DistributedPipelining。 |
| **DSPStyle** | 用于乘法器映射的综合属性。默认值为 `none`。另请参阅 DSPStyle。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中移除子系统层级。默认值为 `inherit`。另请参阅 FlattenHierarchy。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |
| **SharingFactor** | 要映射到单个共享资源的等效功能资源数量。默认值为 0。另请参阅资源分享。 |
| **StreamingFactor** | 并行数据路径或向量的数量，这些路径或向量经过时间复用转换为串行标量数据路径。默认值为 0，表示实现完全并行的数据路径。另请参阅流式处理。 |

**目标规范**

此模块不能作为 DUT，因此 **Target Specification** 选项卡中的模块属性设置会被忽略。

**限制**

- 该模块不支持向量输入。
- 该模块不支持总线输入。
- 不能在 Synchronous Subsystem 中使用。
- 不支持资源共享优化。

## 版本历史

**在 R2020b 中引入**

### R2025a: 控制每次迭代的流水线级数

您可以通过将 **LatencyStrategy** 参数 HDL 设置为 `Custom(PerIterations)`，然后使用 **IterationsPerPipeline** 参数指定每次迭代的流水线级数，来控制迭代算法的流水线级数。使用此设置可以控制生成代码中的流水线级数，并针对速度和资源利用率优化设计。

## 描述

计算倒数平方根运算并带延迟仿真

rSqrt 模块对输入数据信号执行倒数平方根运算。该模块具有指示输入和输出数据是否有效的控制信号。您还可以指定算法的迭代次数和延迟策略。

要在 Simulink® 模型中使用此模块，请在 MATLAB® 命令窗口中输入以下命令打开 `HDLMathLib` 库：

```
open_system("HDLMathLib")
```

您可以带延迟仿真 rSqrt 模块。有关详细信息，请参阅延迟注意事项。
