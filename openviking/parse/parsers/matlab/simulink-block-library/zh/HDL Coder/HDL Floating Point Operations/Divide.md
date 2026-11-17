---
type: simulink-block
title: 'Divide'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Floating Point Operations'
documentation_page: 'divide'
documentation_source_path: 'ref/divide.html'
language: zh-CN
chinese_source: worker-translation
---

# Divide

## 端口

### 输入

### **dividendDataIn** — 被除数数据信号 标量 | 向量

用于计算除法的被除数输入，指定为标量或向量。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **divisorDataIn** — 除数数据信号 标量 | 向量

用于计算除法的除数输入，指定为标量或向量。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **validIn** — 输入控制信号是否有效 标量

指示输入信号是否有效的输入控制信号，指定为标量。

**数据类型：** `Boolean`
### 输出

### **dataOut** — 输出数据信号 标量 | 向量

输出信号，为被除数和除数输入信号相除的结果，以标量或向量形式返回。

**数据类型：** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **validOut** — 输出控制信号是否有效 标量

指示输出信号是否有效的输出控制信号，以标量形式返回。

**数据类型：** `Boolean`

## 参数

### **Latency strategy** — 延迟策略 `Max`（默认）| `Min` | `Custom` | `Custom(PerIteration)` | `Zero`

指定使用最小延迟、最大延迟、自定义延迟还是零延迟。有关详细信息，请参阅延迟策略。

要为该模块使用自定义延迟，请将 **Latency strategy** 设置为 `Custom`，并在 **Custom latency** 字段中输入延迟值。

您还可以控制迭代算法的流水线级数。要为迭代算法自定义延迟，请将 **Latency strategy** 设置为 `Custom(PerIteration)`，并在 **IterationsPerPipeline** 字段中输入每个流水线的迭代次数。*（自 R2025a 起）*

#### 编程用法

|  |
| --- |
| **模块参数**：`latencyMode` |
| **类型**：字符向量 |
| **值**：`'Max'` | `'Min'` | `'Custom'` | `'Custom(PerIteration)'` | `'Zero'` |
| **默认值**：`'Max'` |

### **Custom latency** — 自定义延迟 `0`（默认）| `正整数`

指定自定义延迟值。延迟必须为范围 [0, *L*] 内的非负整数，其中 *L* 是 Divide 模块的最大延迟值。有关详细信息，请参阅 CustomLatency。

#### 依赖关系

要使用此参数，请将 **Latency strategy** 设置为 `Custom`。

#### 编程用法

|  |
| --- |
| **模块参数**：`customLatencyValue` |
| **类型**：整数 |
| **值**：`0 to Max latency` |
| **默认值**：`0` |

### **IterationsPerPipeline** — 每个流水线的迭代次数 `1`（默认）| `正整数`

*自 R2025a 起*

指定算法中每个流水线级使用的迭代次数。

#### 依赖关系

要启用此参数，请将 **Latency strategy** 设置为 `Custom(PerIteration)`。

#### 编程用法

|  |
| --- |
| **模块参数**：`iterationsPerPipelineValue` |
| **类型**：整数 |
| **值**：`Positive integer` |
| **默认值**：`1` |

### **Output data type** — 输出数据类型 `Inherit: Inherit via internal rule`（默认）| `Inherit: Same as first input` | `Inherit: Inherit via back propagation` | `Inherit: Keep MSB` | `Inherit: Match Scaling` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

指定输出数据类型。数据类型可以继承或直接指定。

#### 编程用法

|  |
| --- |
| **模块参数**：`OutDataTypeStr` |
| **类型**：字符向量 |
| **值**：`'Inherit: Inherit via internal rule'` | `'Inherit: Inherit via back propagation'` | `'Inherit: Same as first input'` | `'Inherit: Keep MSB'` | `'Inherit: Match Scaling'` | `'int8'` | `'uint8'` | `int16` | `'uint16'` | `'int32'` | `'uint32'` | `'int64'` | `'uint64'` | `fixdt(1,16,0)` | `'<data type expression>'` |
| **默认值**：`'Inherit: Inherit via internal rule'` |

### **Integer rounding mode** — 定点运算的舍入模式 `Zero`（默认）| `Ceiling` | `Convergent` | `Floor` | `Nearest` | `Round` | `Simplest`

指定定点运算的舍入模式。有关详细信息，请参阅舍入模式。

#### 程序化使用

|  |
| --- |
| **模块参数：** `RndMeth` |
| **类型：** 字符向量 |
| **值：** `'Zero' | 'Ceiling' | 'Convergent' | 'Floor' | 'Nearest' | 'ROund' | 'Simplest'` |
| **默认：** `'Zero'` |

## 所属库

HDL Coder

## 模块特性

R2025b 中未记录。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

该模块支持使用 HDL Coder™ 进行 HDL 代码生成。HDL Coder 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| `Module`（默认） | 为子系统及子系统内的模块生成代码。 |
| `BlackBox` | 生成黑盒接口。生成的 HDL 代码仅包含子系统的输入/输出端口定义。因此，您可以在模型中使用子系统来生成与现有手写 HDL 代码的接口。子系统的黑盒接口生成类似于不带时钟信号的 Model 模块接口生成。 |
| `No HDL` | 从生成的代码中移除该子系统。您可以在仿真中使用该子系统，但在 HDL 代码中将其视为“空操作”。 |

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **AdaptivePipelining** | 基于综合工具、目标频率和乘法器字长自动插入流水线。默认值为 `inherit`。另请参阅 AdaptivePipelining。 |
| **BalanceDelays** | 检测在一条路径上引入的新延迟，并在其他路径上插入匹配的延迟。默认值为 `inherit`。另请参阅 BalanceDelays。 |
| **ClockRatePipelining** | 以更快的时钟速率而非较慢的数据速率插入流水线寄存器。默认值为 `inherit`。另请参阅 ClockRatePipelining。 |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **DistributedPipelining** | 流水线寄存器分布，或寄存器重定时。默认值为 `inherit`。另请参阅 DistributedPipelining。 |
| **DSPStyle** | 用于乘法器映射的综合属性。默认值为 `none`。另请参阅 DSPStyle。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中移除子系统层级。默认值为 `inherit`。另请参阅 FlattenHierarchy。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |
| **SharingFactor** | 映射到单个共享资源的功能等效资源数量。默认值为 0。另请参阅资源共享。 |
| **StreamingFactor** | 被时间复用以转换为串行标量数据路径的并行数据路径或向量数量。默认值为 0，表示实现完全并行的数据路径。另请参阅流式处理。 |

**目标规范**

该模块不能作为 DUT，因此**目标规范**选项卡中的模块属性设置将被忽略。

**限制**

- 您不能在 Synchronous Subsystem 模块中使用该模块。
- 该模块不支持资源共享优化。

## 版本历史

**在 R2020b 中引入**

### R2025a：控制每次迭代的流水线级数

你可以通过将 **LatencyStrategy** 参数 HDL 设置为
`Custom(PerIterations)`，然后使用 **IterationsPerPipeline** 参数指定每次迭代的流水线
级数，来控制迭代算法的流水线级数。使用此设置可以控制生成代码中的流水线级数，并针对速度和资源利用率优化设计。

## 描述

计算除法运算并模拟延迟

Divide 模块对输入数据信号执行除法运算。
该模块具有控制信号，用于指示输入和输出数据是否有效。你
还可以指定算法的迭代次数和延迟策略。

要在 Simulink® 模型中使用此模块，请在 MATLAB® 命令
窗口中输入以下命令以打开 `HDLMathLib` 库：

```
open_system("HDLMathLib")
```

你可以
模拟该模块的延迟。有关详细信息，请参阅 Latency Considerations。
