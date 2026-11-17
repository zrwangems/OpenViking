---
type: simulink-block
title: 'LTE Convolutional Decoder'
family: 'error-detection-and-correction'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'lteconvolutionaldecoder'
documentation_source_path: 'ref/lteconvolutionaldecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# LTE Convolutional Decoder

## 端口

### 输入

### **data** — 输入样本 3×1 列向量

输入样本，指定为 3×1 列向量。当输入类型为有符号定点或有符号整数时，该模块执行软判决解码；当输入类型为 `Boolean` 或 `fixdt(0,1,0)` 时，该模块执行硬判决解码。对于 `single` 和 `double` 类型，该模块执行未量化的软判决解码，但 HDL 代码生成不支持此模式。

对于硬件软判决实现，建议使用位宽为三位或四位的整数或定点类型。当设计综合到 FPGA 时，该输入字长可在优化时序和资源使用的同时实现解码性能。输入数据类型必须小于 16 位宽。内部数据类型派生自该数据类型，而较低精度的类型可能导致解码性能损失。

小于零的值最可能表示逻辑 `0`，而大于零的值最可能表示逻辑 `1`。绝对值决定置信度水平。例如，下表显示了当输入为 `sfix4` (*WL*=4, *FL*=0) 时使用的置信度水平。

|  |  |  |  |
| --- | --- | --- | --- |
| **软值** | –8, –7, –6, –5, –4, –3, –2, –1 | 0 | 1, 2, 3, 4, 5, 6, 7 |
| **逻辑电平** | 逻辑 `0` | 未知 | 逻辑 `1` |
| **置信度** | 高 → 低 | 无 | 低 → 高 |

**数据类型：** `Boolean` | `fixdt(0,1,0)` | `fixdt(1,WL,FL)` | `int8` | `int16` | `single` | `double`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，这些信号指示帧的边界和样本的有效性。

- `start` — 指示输入帧的起始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关更多详细信息，请参阅样本控制总线。

**数据类型：** `bus`
### 输出

### **data** — 输出样本标量

输出样本，以二进制标量值返回。

`double` 和 `single` 支持仿真，但不支持 HDL 代码生成。

**数据类型：** `single` | `double` | `Boolean` | `ufix1`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，以 `samplecontrol` 总线返回。该总线包括 `start`、`end` 和 `valid` 控制信号，这些信号指示帧的边界和样本的有效性。

- `start` — 指示输出帧的起始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关更多详细信息，请参阅样本控制总线。

**数据类型：** `bus`

## 参数

### **Maximum message length** — 最大输入帧大小 1024（默认） | 正整数

最大输入帧大小，指定为 6 到 2048 之间的正整数。该模块使用此参数确定存储中间判决所需的 RAM 量。如果未指定 2 的幂，则该模块使用下一个最大的 2 的幂。

如果输入帧大于指定的最大消息长度，则该模块返回警告。

## 所属库

Wireless HDL Toolbox / Error Detection and Correction

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

此模块没有任何 HDL 模块属性。

## 版本历史

**在 R2017b 中引入**

## 描述

使用 Viterbi 算法解码卷积编码样本

LTE Convolutional Decoder 模块实现环绕 Viterbi 算法 (WAVA)，以解码由 LTE 标准 TS 36.212 [1] 指定的咬尾多项式编码的样本。该卷积码的约束长度为 7，并且是咬尾的，编码率为 1/3，八进制多项式为 **G0**=133、**G1**=171 和 **G2**=165。该模块提供硬件优化的架构和接口。

此模块使用流式样本接口，并通过总线传输相关控制信号。此接口使该模块能够独立于帧大小运行，并轻松连接到其他 Wireless HDL Toolbox™ 模块。该模块接受并返回表示单个样本的值，以及包含三个控制信号的总线。这些信号指示每个样本的有效性以及帧的边界。要将矩阵转换为样本流和这些控制信号，请使用 Frame To Samples 模块或 `whdlFramesToSamples` 函数。有关该接口的完整说明，请参阅流式样本接口。

该模块接受表示软判决或硬判决的输入样本。每个样本是一个 3×1 向量，其中三个值表示由三个多项式 `[G0 G1 G2]` 编码的位。

解码 *M* 个样本的消息需要 2\**M*+140 个周期，假设输入连续有效。因此，必须在输入帧之间至少留出这么多空闲周期。或者，您可以使用输出信号 **ctrl**.`end` 来确定该模块何时准备好接受新输入。

此波形显示一个包含 100 个样本的输入消息，帧之间有 340 个空闲周期。输入数据是三个编码位的向量。输入和输出 **ctrl** 总线被展开以显示控制信号。`start` 和 `end` 显示帧边界，`valid` 限定数据样本。
