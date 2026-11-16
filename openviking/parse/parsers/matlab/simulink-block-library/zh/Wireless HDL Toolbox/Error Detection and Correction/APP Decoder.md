---
type: simulink-block
title: 'APP Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'appdecoder'
documentation_source_path: 'ref/appdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# APP Decoder

## 端口

### 输入

### **LLRc** — 编码 LLR 值实值列向量

编码 LLR 值，指定为大小为 *N*×1 的实值列向量，其中 *N* 是解码速率，范围为 2 到 7。

输入向量大小取决于模块的码率。该模块从模块掩码中指定的代码生成器多项式值推导码率。该模块支持以下码率：1/2、1/3、1/4、1/5、1/6 或 1/7。

`double` 和 `single` 数据类型支持仿真，但不支持 HDL 代码生成。对于 HDL 代码生成，该模块支持 `fixdt(1,WL,FL)` 数据类型，并且输入字长 (WL) 必须在 4 到 16 的范围内。

**数据类型：** `single` | `double` | `int8` | `int16` | `signed fixed point`

### **LLRu** — 未编码 LLR 值实值标量

未编码 LLR 值，指定为实值标量。

`double` 和 `single` 数据类型支持仿真，但不支持 HDL 代码生成。对于 HDL 代码生成，该模块支持 `fixdt(1,WL,FL)` 数据类型，并且输入字长 (WL) 必须在 4 到 16 的范围内。

**数据类型：** `single` | `double` | `int8` | `int16` | `signed fixed point`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包含 `start`、`end` 和 `valid` 控制信号，它们指示帧的边界和样本的有效性。

- `start` — 指示输入帧的起始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### 输出

### **LLRu** — 未编码 LLR 值实值标量

未编码 LLR 值，返回为实值标量。输出数据类型与输入数据类型相同。

对于 `fixed point` 数据类型的输入，输出字长增加
`floor`(log2(*N*)) +
`floor`(log2(*K* – 1)) + 2
bits。*N* 是码率，*K* 是该模块的约束长度。

**数据类型：** `single` | `double` | `int8` | `int16` | `fixed point`

### **LLRc** — 编码 LLR 值实值列向量

编码 LLR 值，返回为大小为 *N*×1 的实值列向量。输出数据类型与输入数据类型相同。

对于 `fixed point` 输入，输出字长增加
`floor`(log2(*N*)) +
`floor`(log2(*K* – 1)) + 2
bits，其中 *N* 是码率，*K* 是该模块的约束长度。

**数据类型：** `single` | `double` | `int8` | `int16` | `fixed point`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，返回为 `samplecontrol` 总线。该总线包含 `start`、`end` 和 `valid` 控制信号，它们指示帧的边界和样本的有效性。

- `start` — 指示输出帧的起始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **nextFrame** — 模块就绪指示符 Boolean 标量

模块就绪指示符，返回为 Boolean 标量。

当模块准备好接受下一帧的起始时，该模块将此信号设置为 `1` (`true`)。如果模块在 **nextFrame** 为 `0` (`false`) 时接收到输入 **ctrl.start** 信号，则该模块会丢弃正在进行的帧并开始处理新数据。

**数据类型：** `Boolean`

## 参数

### **Code generator** — 代码生成器多项式 `[171,133]`（默认）| 2 到 7 个元素的行向量

指定由八进制值组成的 1×*n* 向量，其中 *n* 是多项式的长度。该模块接受长度为 2 到 7 个元素的多项式。

该模块基于指定的代码生成器多项式推导约束长度和码率。指定代码生成器多项式时，应使约束长度在 3 到 9 范围内，码率为 1/2、1/3、1/4、1/5、1/6 或 1/7。

有关如何为解码模块指定代码生成器多项式的详细信息，请参阅 Trellis Description of a Convolutional Code。

### **Feedback connection** — 代码生成器多项式 `171`（默认）| 八进制值

*自 R2023b 起*

指定一个参考代码生成器值的标量八进制值。如果指定 `0` 或 `[]`，模块将在无反馈的情况下执行解码。

### **Termination method** — 帧结束行为 `Truncated`（默认）| `Terminated`

选择终止方法以指定帧结束行为。

- `Truncated` — 该模块在每帧之后重置状态度量，从全零状态开始，并以非全零状态结束。输入 **ctrl** 总线限定输入样本并标记帧边界。
- `Terminated` — 该模块在每帧之后重置状态度量，并以全零状态开始和结束。输入 **ctrl** 总线限定输入样本并标记帧边界。

### **Algorithm** — 解码算法类型 `Max Log MAP (max)`（默认）| `Log MAP (max*)`

选择解码算法的类型。

- `Max Log MAP (max)` — 最大对数 MAP 近似
- `Log MAP (max*)` — 对数 MAP 近似

有关这些算法的详细信息，请参阅 [1]。

### **Window length** — 要对其执行 MAP 算法的窗口 `64`（默认）| 3 到 128 范围内的整数

要对其执行 MAP 算法的窗口，指定为 3 到 128 范围内的整数。此整数表示窗口长度。

为获得更好的模块性能结果，建议窗口长度至少为约束长度的五倍。

### **Disable LLRc output port** — 禁用 LLRc 输出端口的选项 `off`（默认）| `on`

选择此参数可禁用模块上的输出端口 **LLRc**。清除此参数可启用模块上的输出端口 **LLRc**。

## 所属库

Wireless HDL Toolbox / Error Detection and Correction

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入生成代码中的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入生成代码中的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

不能在 Resettable Synchronous Subsystem (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2021b 中引入**

### R2023b：支持网格反馈结构

APP Decoder 模块现在通过新参数 **Feedback connection** 支持网格反馈结构。此参数支持标量值。

## 描述

使用 MAP 算法解码卷积编码的 LLR 值

APP Decoder 模块使用最大后验概率 (MAP) 解码算法对卷积编码的对数似然比 (LLR) 值进行解码。该模块接受编码和未编码 LLR 值以及 `samplecontrol` 总线，对编码 LLR 值进行解码，并输出编码和未编码 LLR 值以及 `samplecontrol` 总线的更新版本。

该模块支持两种解码算法：`Max Log MAP (max)` 和 `Log MAP (max*)`。您可以通过设置 **Algorithm** 参数来选择算法。该模块支持 `Terminated` 和 `Truncated` 模式以及以下解码速率：1/2、1/3、1/4、1/5、1/6 和 1/7。该模块提供适用于 HDL 代码生成和硬件部署的架构。

该模块支持对串行和并行级联码进行解码。使用此模块，您可以构建 Turbo 解码器、用于级联码的自定义解码器以及用于迭代解码的乘积码。
