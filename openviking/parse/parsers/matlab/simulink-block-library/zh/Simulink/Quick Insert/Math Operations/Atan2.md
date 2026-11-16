---
type: simulink-block
title: 'Atan2'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Floating Point Operations'
documentation_page: 'atan2'
documentation_source_path: 'ref/atan2.html'
language: zh-CN
chinese_source: official
---

# Atan2

## 端口

### 输入

### **y\_dataIn** — *y* 坐标数据 标量 | 向量

*y* 坐标数据，指定为标量或向量。输入信号必须为实数值数据。

**数据类型:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

### **x\_dataIn** — *x* 坐标数据 标量 | 向量

*x* 坐标数据，指定为标量或向量。输入信号必须为实数值数据。

**数据类型:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

### **validIn** — 输入控制信号是否有效 标量

指示输入信号是否有效的输入控制信号，指定为标量。

**数据类型:** `Boolean`
### 输出

### **thetaOut** — 四象限反正切 标量 | 向量

*x* 和 *y* 坐标输入信号的四象限反正切，以标量或向量形式返回。此信号是从 `x_dataIn` 或 `y_dataIn` 信号处的值到正 *x* 轴的向量之间的角度。

**数据类型:** `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `bus`

### **validOut** — 输出控制信号是否有效 标量

指示输出信号是否有效的输出控制信号，以标量形式返回。

**数据类型:** `Boolean`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。从 Simulink 工具条中，在**仿真**选项卡上的**准备**库中，选择**属性检查器**。

### **迭代次数** — CORDIC 算法的迭代次数 `11` (默认) | `positive integer`

指定 CORDIC 算法的迭代次数。

#### 编程用法

|  |
| --- |
| **模块参数**：`iter` |
| **类型**：字符向量 |
| **值**：`Integer values` |
| **默认值**：`'11'` |

### **延迟策略** — 延迟策略 `Max` (默认) | `Min` | `Custom` | `Custom(PerIteration)` | `Zero`

指定是使用最小值、最大值、自定义还是零延迟。有关详细信息，请参阅延迟策略。

要对模块使用自定义延迟，请将**延迟策略**设置为**自定义**并在**自定义延迟**字段中输入延迟值。

您也可以控制迭代算法的流水线阶段数。要自定义迭代算法的延迟，请将**延迟策略**设置为 **Custom(PerIteration)** 并在 **IterationsPerPipeline** 字段中输入每个流水线的迭代次数值。 *(自 R2025a 起)*

#### 编程用法

|  |
| --- |
| **模块参数**：`latencyMode` |
| **类型**：字符向量 |
| **值**：`'Max'` | `'Min'` | `'Custom'` | `'Custom(PerIteration)'` | `'Zero'` |
| **默认值**：`'Max'` |

### **自定义延迟** — 自定义延迟 `0` (默认) | `positive integer`

指定自定义延迟值。延迟必须是在范围 [0, *L*] 内的非负整数，其中 *L* 是 Atan2 模块的最大延迟值。有关详细信息，请参阅 延迟注意事项。

#### 依赖关系

要启用此参数，请将**延迟策略**设置为**自定义**。

#### 编程用法

|  |
| --- |
| **模块参数**：`customLatencyValue` |
| **类型**：整数 |
| **值**：`0 to Max latency` |
| **默认值**：`0` |

### **IterationsPerPipeline** — 每个流水线的迭代次数 `1` (默认) | `positive integer`

*自 R2025a 起*

指定算法中每个流水线阶段要使用的迭代次数。

#### 依赖关系

要启用此参数，请将**延迟策略**设置为 **Custom(PerIteration)**。

#### 编程用法

|  |
| --- |
| **模块参数**：`iterationsPerPipelineValue` |
| **类型**：整数 |
| **值**：`Positive integer` |
| **默认值**：`1` |

## 所属库

HDL Coder

## 模块特性

R2025b 官方文档未提供。

## 扩展功能

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

该模块支持使用 HDL Coder™ 生成 HDL 代码。HDL Coder 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

| 架构 | 描述 |
| --- | --- |
| **模块**（默认值） | 为子系统及其内部的模块生成代码。 |
| **黑盒** | 生成黑盒接口。生成的 HDL 代码仅包括子系统的输入/输出端口定义。因此，您可以在模型中使用子系统来生成与手动编写的现有 HDL 代码的接口。  子系统的黑盒接口生成类似于没有时钟信号的 Model 模块接口生成。 |
| **无 HDL** | 从生成的代码中删除子系统。您可以在仿真中使用子系统，但在 HDL 代码中将其视为“无操作”。 |

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **AdaptivePipelining** | 基于综合工具、目标频率和乘法器字长的自动流水线插入。默认值为 **inherit**。另请参阅AdaptivePipelining。 |
| **BalanceDelays** | 检测沿一条路径引入的新延迟，并在其他路径上插入匹配的延迟。默认值为 **inherit**。另请参阅BalanceDelays。 |
| **ClockRatePipelining** | 以较快的时钟频率而不是较慢的数据速率插入流水线寄存器。默认值为 **inherit**。另请参阅ClockRatePipelining。 |
| **ConstrainedOutputPipeline** | 通过移动设计中的现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline。 |
| **DistributedPipelining** | 流水线寄存器分布，或寄存器重定时。默认值为 **inherit**。另请参阅DistributedPipelining。 |
| **DSPStyle** | 乘法器映射的综合属性。默认值为 **none**。另请参阅DSPStyle。 |
| **FlattenHierarchy** | 从生成的 HDL 代码中删除子系统层次结构。默认值为 **inherit**。另请参阅FlattenHierarchy。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线阶段数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅InputPipeline。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线阶段数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline。 |
| **SharingFactor** | 映射到单个共享资源的功能等效资源的数量。默认值为 0。另请参阅Resource Sharing。 |
| **StreamingFactor** | 并行数据路径或向量的数量，这些路径或向量通过时间多路复用的方式变换为串行标量数据路径。默认值为 0，表示实现完全并行的数据路径。另请参阅Streaming。 |

**目标设定**

此模块不能为 DUT，因此**目标设定**选项卡中的模块属性设置将被忽略。

**限制**

- 您无法在 Synchronous Subsystem 模块中使用此模块。
- 该模块不支持资源复用优化。

## 版本历史

**在 R2020b 中推出**

### R2025a: 控制每次迭代的流水线阶段数

您可以通过将 **LatencyStrategy** 参数 HDL 设置为 **Custom(PerIterations)**，然后使用 **IterationsPerPipeline** 参数指定每次迭代的流水线阶段数，来控制迭代算法的流水线阶段。使用此设置可以控制生成代码中的流水线阶段，并优化设计的速度和资源利用率。

## 描述

使用 CORDIC 逼近方法计算 Atan2 运算并带延迟进行仿真

Atan2 模块通过使用坐标旋转数字计算 (CORDIC) 逼近方法执行实数值输入信号的四象限反正切。有关详细信息，请参阅算法中的 CORDIC 逼近方法。该模块具有指示输入和输出数据是否有效的控制信号。您也可以指定算法的迭代次数和延迟策略。

要在您的 Simulink® 模型中使用此模块，请在 MATLAB® 命令行窗口中输入以下命令来打开 `HDLMathLib` 库：

```
open_system("HDLMathLib")
```

您可以带延迟对 Atan2 模块进行仿真。有关详细信息，请参阅 延迟注意事项。
