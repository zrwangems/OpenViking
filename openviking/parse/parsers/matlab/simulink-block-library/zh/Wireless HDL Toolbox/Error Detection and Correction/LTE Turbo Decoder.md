---
type: simulink-block
title: 'LTE Turbo Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'lteturbodecoder'
documentation_source_path: 'ref/lteturbodecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# LTE Turbo Decoder

## 端口

### 输入

### **data** — 输入样本三元向量

输入样本，指定为三元整数向量。这些值表示软编码概率。如果值为负，则该位更可能为 0。如果值为正，则该位更可能为 1。第一个元素是顺序位，另外两个元素是校验位。该模块期望输入帧为 *BlockSize* + 12 个样本。此帧大小包括尾比特，顺序按照 LTE 标准 TS 36.212 [1] 中指定的顺序。

对于硬件实现，请使用具有两到三个整数位和一到四个小数位的定点类型。内部数据类型由此数据类型派生，较低精度的类型可能导致解码精度损失。如果输入数据类型具有零个小数位或少于两个整数位，该模块将返回警告。`double` 和 `single` 支持仿真，但不支持 HDL 代码生成。

**数据类型：** `fixdt(1,WL,FL)` | `single` | `double`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

- `start` — 指示输入帧的开始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **blockSize** — Turbo 码块大小 整数

Turbo 码块大小，指定为整数。此值必须是 LTE 标准中指定的 188 个值之一，范围从 40 到 6144，间隔如下：`[40:8:512 528:16:1024 1056:32:2048 2112:64:6144]`。

#### 依赖关系

当您将 **Block size source** 设置为 `Input port` 时，此端口出现。

**数据类型：** `single` | `double` | `uint16` | `fixdt(0,13,0)`
### 输出

### **data** — 输出样本 标量

输出样本，返回为二进制标量。`double` 和 `single` 支持仿真，但不支持 HDL 代码生成。

**数据类型：** `single` | `double` | `Boolean` | `ufix1`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，返回为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

- `start` — 指示输出帧的开始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

## 参数

### **Block size source** — 如何指定块大小 `Input port`（默认）| `Property`

选择是通过输入端口指定块大小，还是输入固定值作为参数。如果选择 `Property`，则出现 **Block size** 参数。如果选择 `Input port`，则出现 **blockSize** 端口。

### **Block size** — Turbo 码块大小 `6144`（默认）

Turbo 码块大小，指定为整数。此值必须是 LTE 标准中指定的 188 个值之一，范围从 40 到 6144，间隔如下：`[40:8:512 528:16:1024 1056:32:2048 2112:64:6144]`。当 **ctrl**.`start` = 1（`true`）时，此值针对每一帧进行注册。

#### 依赖关系

当您将 **Block size source** 设置为 `Property` 时，此参数出现。

### **Number of decoding iterations** — 要执行的 MAX 解码迭代次数 `6`（默认）| 正整数

要执行的 MAX 解码迭代次数，指定为正整数。解码器实现使用单个 MAX 解码器，每次半迭代的输出数据被路由回输入。更高的迭代次数会提高精度并增加延迟。大约 15 次迭代后，该算法不再提供进一步的精度提升。

## 所属库

Wireless HDL Toolbox / Error Detection and Correction

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

无法在 Resettable Synchronous Subsystem (HDL Coder) 或 Enabled Synchronous Subsystem (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2017b 中引入**

## 描述

解码 turbo 编码样本

LTE Turbo Decoder 模块实现了 LTE 标准 TS 36.212 [1] 所要求的 turbo 解码器，并提供了针对 HDL 代码生成和硬件部署优化的接口和架构。该模块对两个 MAX 解码器进行迭代。您可以指定迭代次数。编码速率为 1/3。该模块接受编码比特作为 3×1 的软编码值向量 `[S P1 P2]`。在该向量中，`S` 是系统比特，`P1` 和 `P2` 是来自两个编码器的校验比特。

该模块使用带有关联控制信号总线的流式样本接口。该接口使模块能够独立于帧大小运行，并易于与其他 Wireless HDL Toolbox™ 模块连接。该模块接受并返回表示单个样本的值，以及包含三个控制信号的总线。这些信号指示每个样本的有效性和帧边界。要将矩阵转换为样本流和这些控制信号，请使用 Frame To Samples 模块或 `whdlFramesToSamples` 函数。有关该接口的完整描述，请参阅 Streaming Sample Interface。

该模块只有在完成前一帧的解码后才能接受下一帧。您必须在输入帧之间留出
*Iterations*\*2\**HalfIterationLatency*+*BlockSize*+4
个空闲周期。半迭代延迟在算法部分中描述。或者，您可以使用输出信号
**ctrl**.`end` 来确定模块何时准备好接收新输入。

此波形显示了 120 个样本（+ 4 个尾比特）的输入帧，以及帧之间的 2632 个空闲周期。每个输入样本是三个定点软判决值的向量。输入和输出 **ctrl** 总线被展开以显示控制信号。`start` 和 `end` 显示帧边界，`valid` 限定数据样本。

LTE Turbo Decoder 模块输入和输出信号的 Logic Analyzer 波形
