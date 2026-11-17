---
type: simulink-block
title: 'LTE Turbo Encoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'lteturboencoder'
documentation_source_path: 'ref/lteturboencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# LTE Turbo Encoder

## 端口

### 输入

### **data** — 输入样本标量

输入样本，指定为二进制标量。`double` 和 `single` 支持仿真，但不支持 HDL 代码生成。

**数据类型：** `single` | `double` | `Boolean` | `ufix1`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

- `start` — 指示输入帧的起始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **blockSize** — Turbo 码块大小 整数

Turbo 码块大小，指定为整数。该值必须是 LTE 标准中指定的 188 个值之一，范围从 40 到 6144，按以下间隔分布：`[40:8:512 528:16:1024 1056:32:2048 2112:64:6144]`。

#### 依赖关系

当您将 **Block size source** 设置为 `Input port` 时，此端口出现。

**数据类型：** `single` | `double` | `uint16` | `fixdt(0,13,0)`
### 输出

### **data** — 编码样本流 3×1 列向量

编码样本流，以 3×1 列向量形式返回。每个编码样本由一个系统位和两个校验位表示。

输出数据类型与输入数据类型匹配。

**数据类型：** `single` | `double` | `Boolean` | `ufix1`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，以 `samplecontrol` 总线形式返回。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

- `start` — 指示输出帧的起始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **tail1, tail2** — 指示网格终止周期 标量

使用可选的 **tail1** 和 **tail2** 输出端口来指示输出数据流中尾比特的位置。对于每个编码器对应尾比特的周期，这些信号为 1（`true`）。

该模块按照 LTE 标准 TS 36.212 [1] 指定的顺序返回尾比特。每个编码器返回两个周期的编码尾比特。

| 周期 | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| **tail1** | 1 | 1 | 0 | 0 |
| **tail2** | 0 | 0 | 1 | 1 |
| **data** | [E1inK E1outK E1inK+1] | [E1outK+1 E1inK+2 E1outK+2] | [E2inK E2outK E2inK+1] | [E2outK+1 E2inK+2 E2outK+2] |

#### 依赖关系

通过选择 **Enable trellis termination valid ports** 来启用这些端口。

**数据类型：** `Boolean`

## 参数

### **Block size source** — 如何指定块大小 `Input port`（默认）| `Property`

选择是通过输入端口指定块大小，还是输入固定值作为参数。如果选择 `Property`，则出现 **Block size** 参数。如果选择 `Input port`，则出现 **blockSize** 端口。

### **Block size** — Turbo 码块大小 `6144`（默认）

Turbo 码块大小，指定为整数。该值必须是 LTE 标准中指定的 188 个值之一，范围从 40 到 6144，按以下间隔分布：`[40:8:512 528:16:1024 1056:32:2048 2112:64:6144]`。当 **ctrl**.`start` = 1（`true`）时，该值针对每一帧进行注册。

#### 依赖关系

当您将 **Block size source** 设置为 `Property` 时，此参数出现。

### **Enable trellis termination valid ports** — 启用指示尾比特输出样本的端口 off（默认）| on

当您选择此参数时，模块上会出现 **tail1** 和 **tail2** 端口。这些端口返回控制信号，用于指示输出样本为每个编码器尾比特的周期。

## 所属库

Wireless HDL Toolbox / Error Detection and Correction

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® 加速器和快速加速器模式的 C/C++ 代码生成，以及用于 DPI 组件生成。

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

## 版本历史

**在 R2017b 中引入**

## 描述

使用 turbo 算法对二进制样本进行编码

LTE Turbo Encoder 模块使用针对 HDL 代码生成和硬件部署优化的接口和架构，实现 LTE 标准 TS 36.212 [1] 所描述的 turbo 编码器。该编码器是一种并行级联卷积码（PCCC），具有两个 8 状态分量编码器和一个内部交织器。第一个编码器对输入数据流进行操作，第二个编码器对输入数据的交织版本进行操作。该模块用独立的尾比特终止每个编码器输出。编码率为 1/3。每个输入比特的编码输出比特以 3×1 向量 `[S P1 P2]` 返回。在该向量中，`S` 是系统比特，`P1` 和 `P2` 是两个编码器的奇偶校验比特。

该模块使用带相关控制信号总线的流式样本接口。该接口使模块能够独立于帧大小运行，并易于与其他 Wireless HDL Toolbox™ 模块连接。该模块接收并返回表示单个样本的值，以及包含三个控制信号的总线。这些信号指示每个样本的有效性以及帧边界。要将矩阵转换为样本流和这些控制信号，请使用 Frame To Samples 模块或 `whdlFramesToSamples` 函数。有关该接口的完整描述，请参阅 Streaming Sample Interface。

该模块可以在前一帧完成后接受新的输入数据。在输入帧之间至少施加 *BlockSize* + 16 个空闲周期。这 16 个周期包括算法中流水线延迟的 12 个周期，以及 4 个周期的尾比特。该延迟不随块大小变化。或者，您可以使用输出信号 **ctrl**.`end` 来确定模块何时准备好接受新输入。

该波形显示了一个 40 个样本的输入帧，帧之间有 57 个空闲周期。输入和输出 **ctrl** 总线被展开以显示控制信号。`start` 和 `end` 显示帧边界，`valid` 限定数据样本。可选的 **tail1** 和 **tail2** 信号指示来自每个编码器的尾比特有效的周期。

LTE Turbo Encoder 模块输入和输出信号的 Logic Analyzer 波形
