---
type: simulink-block
title: 'Serializer1D'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Operations'
documentation_page: 'serializer1d'
documentation_source_path: 'ref/serializer1d.html'
language: zh-CN
chinese_source: worker-translation
---

# Serializer1D

## 端口

### 输入

### **P** — 并行数据输入信号 `scalar` | `vector`

要串行化的输入信号。不支持总线数据类型。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **ValidIn** — 有效输入控制信号 `scalar`

指示有效输入信号的输入控制信号。当选中 **ValidIn** 复选框时，此端口可用。

**数据类型：** `Boolean`

### 输出

### **S** — 串行化数据输出信号 `scalar` | `vector`

串行化输出信号。不支持总线数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **StartOut** — 起始输出控制信号 `scalar`

指示串行化开始的输出控制信号。您可以将此信号用作 Deserializer1D 模块的 **StartIn** 输入。要使用此端口，请选中 **StartOut** 复选框。

**数据类型：** `Boolean`

### **ValidOut** — 有效输出控制信号 `scalar`

指示有效输出信号的输出控制信号。您可以将此信号用作 Deserializer1D 模块的 **ValidIn** 输入。当选中 **ValidOut** 复选框时，此端口可用。

**数据类型：** `Boolean`

## 参数

### **Ratio (Output Vector Size/Input Vector Size)** — 输入向量大小与输出向量大小的比率 1（默认）

串行化因子，指定为正标量。

该比率等于输入向量大小除以输出向量大小。输入向量大小必须能被该比率整除。

### **Idle Cycles** — 空闲周期数 0（默认）

输入在每个输出末尾添加的空闲周期数。

### **StartIn** — 启用 StartIn 控制端口 off（默认）| on

选择以激活 StartIn 端口。

### **ValidIn** — 启用 ValidIn 控制端口 off（默认）| on

选择以激活 ValidIn 端口。

### **ValidOut** — 启用 ValidOut 控制端口 off（默认）| on

选择以激活 ValidOut 端口。

### **Input data port dimensions (-1 for inherited)** — 输入数据信号的大小 -1（默认）

输入数据信号的大小。输入向量大小必须能被该比率整除。默认情况下，模块根据模型中的上下文继承大小。

### **Input sample time (-1 for inherited)** — 输入采样时间 -1（默认）

采样时间命中之间的时间间隔，或另一个合适的采样时间，例如连续采样时间。默认情况下，模块根据模型中的上下文继承采样时间。有关详细信息，请参阅 Sample Time。

### **Input signal type** — 模块的输入信号类型 auto（默认）| real | complex

模块的输入信号类型，指定为 `auto`、`real` 或 `complex`。默认值为 `auto`。

## 所属库

HDL Coder / HDL Operations

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 生成用于 FPGA 和 ASIC 设计的 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

**注意**

为了使仿真结果与生成的 HDL 代码匹配，在“配置参数”对话框的“求解器”窗格中，清除 **将每个离散速率视为单独任务** 复选框。清除该复选框后，将启用单任务模式。如果选中此复选框对模块进行仿真，输出数据可以在同一周期更新，但在生成的 HDL 代码中，输出数据会晚一个周期更新。

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 常规 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计中移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 在生成的代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 在生成的代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |

## 版本历史

**在 R2014b 中引入**

### R2024a：半精度和 Boolean 数据支持

该模块现在支持使用 `Half` 或 `Boolean` 类型的输入数据进行 HDL 代码生成。

## 描述

将向量信号转换为标量或更小的向量

Serializer1D 模块基于 **Ratio** 和 **Idle Cycle** 值，将较慢的向量信号转换为较快的标量信号流或较小大小的向量信号流。为了匹配更快的串行化输出，采样时间根据以下等式变化：

Output Sample Time=Input Sample Time/(Ratio+Idle Cycles)

考虑以下示例：输入数据是大小为 4 的向量，**Ratio** 设置为 4。

Serializer 模块输入和输出的时序图

输出数据将每个向量信号串行化为四个标量信号。输出端的采样时间为：Output Sample Time=Input Sample Time/4。

要在每个输出末尾添加空闲周期，对于 **Idle Cycles**，指定一个大于零的整数。考虑以下示例：**Ratio** 设置为 4，**Idle Cycles** 设置为 2。

带空闲周期的 Serializer 模块输入和输出时序图

对于每个慢速向量信号，输出有六个快速周期，由四个串行化标量信号和两个空闲周期组成。输出端的采样时间为 Output Sample Time=Input Sample Time/6。

Serializer1D 模块提供三个控制信号：**ValidIn**、**ValidOut** 和 **StartOut**。您可以使用 **ValidIn** 控制 **ValidOut** 和 **StartOut**。串行化输出不依赖于 **ValidIn**。要确定输出串行化数据是否有效，请使用 **ValidIn** 和 **ValidOut**。如果向 **ValidIn** 提供高输入，并且没有空闲周期，则 **ValidOut** 输出高电平，表示输出串行化数据有效。

考虑一个示例：输入数据为大小为 4 的向量，**Ratio** 设置为 4，**Idle Cycles** 设置为 2，并使用所有三个控制信号。

带空闲周期和三个控制信号的 Serializer 模块输入和输出时序图

对于第一个输入向量 `ABCD`，**ValidIn** 为 false。**StartOut** 和 **ValidOut** 变为 false。这意味着输出数据值无效。在波形中，数据值表示为 `X`，对应 *don’t care* 值。

对于第二个输入向量 `ABCE`，**ValidIn** 为 true。输出数据将该向量串行化为四个标量信号。控制信号 **StartOut** 在输出 `A` 处变为 true，以指示串行化开始。在下一个周期，**StartOut** 信号变为 false。**ValidOut** 对于所有四个输出信号均为 true，表示这四个周期的输出数据有效。**ValidOut** 在空闲周期变为 false，输出数据值为 *don’t care* 值。
