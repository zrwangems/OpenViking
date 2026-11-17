---
type: simulink-block
title: 'LTE Convolutional Encoder'
family: 'error-detection-and-correction'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'lteconvolutionalencoder'
documentation_source_path: 'ref/lteconvolutionalencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# LTE Convolutional Encoder

## 端口

### 输入

### **data** — 输入样本标量

输入样本，指定为二进制标量。`double` 和 `single` 支持仿真，但不支持 HDL 代码生成。

**数据类型：** `single` | `double` | `Boolean` | `ufix1`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，它们指示帧的边界和样本的有效性。

- `start` — 指示输入帧的起始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### 输出

### **data** — 编码样本 3-by-1 列向量

编码样本，以 3-by-1 列向量形式返回。每个编码样本由三个比特表示，每个编码器多项式对应一个比特。

输出数据类型与输入数据类型匹配。

**数据类型：** `single` | `double` | `Boolean` | `ufix1`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，以 `samplecontrol` 总线形式返回。该总线包括 `start`、`end` 和 `valid` 控制信号，它们指示帧的边界和样本的有效性。

- `start` — 指示输出帧的起始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

## 参数

### **Maximum message length** — 最大输入帧大小 1024（默认）| 正整数

最大输入帧大小，指定为从 6 到 2^16 的正整数。此参数定义所需的帧内存量。如果未指定为 2 的幂，则该模块使用下一个最大的 2 的幂。

如果输入帧大于指定的最大消息长度，则该模块返回警告。

## 所属库

Wireless HDL Toolbox / Error Detection and Correction

## 模块特性

在 R2025b 中未记录。

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
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**在 R2017b 中引入**

## 描述

使用咬尾卷积算法对二进制样本进行编码

LTE Convolutional Encoder 模块实现 LTE 标准 TS 36.212 [1] 指定的编码多项式。该卷积码的约束长度为 7，并且是咬尾的，编码率为 1/3，八进制多项式为 **G0**=133、**G1**=171 和 **G2**=165。该模块提供硬件优化的架构和接口。

该模块使用流式样本接口，并带有一个用于相关控制信号的总线。此接口使模块能够独立于帧大小运行，并易于与其他 Wireless HDL Toolbox™ 模块连接。该模块接受并返回表示单个样本的值，以及一个包含三个控制信号的总线。这些信号指示每个样本的有效性以及帧的边界。要将矩阵转换为样本流和这些控制信号，请使用 Frame To Samples 模块或 `whdlFramesToSamples` 函数。有关该接口的完整描述，请参阅 Streaming Sample Interface。

消息大小可以动态更改。每个输入比特的编码输出比特以 3-by-1 向量 `[G0 G1 G2]` 形式返回。

该模块需要 *M* + 5 个周期来编码一帧 *M* 个样本。因此，必须在输入帧之间保留 *M* + 5 个空闲周期。或者，可以使用输出信号 **ctrl**.`end` 来确定模块何时准备好接受新输入。

此波形显示了一个包含 40 个样本的输入消息，帧之间有 45 个空闲周期。输出数据是一个包含三个编码比特的向量。输入和输出 **ctrl** 总线被展开以显示控制信号。`start` 和 `end` 显示帧边界，`valid` 标识数据样本有效。
