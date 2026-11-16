---
type: simulink-block
title: 'DVB-S2 BCH Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'dvbs2bchdecoder'
documentation_source_path: 'ref/dvbs2bchdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# DVB-S2 BCH Decoder

## 端口

### 输入

### **data** — 码字数据位 标量 | 向量

码字数据位，指定为 `Boolean` 标量或 8 元素列向量。

输入数据的长度必须根据 DVB-S2 标准基于 FEC 帧类型和码率确定。有关详细信息，请参阅 [1] 中的第 5.3 节。

例如，如果 **FEC frame type** 参数设置为 `Normal`，并且 **Code rate** 参数设置为 `3/5`，则输入数据的长度必须为 38,880。

**数据类型：** `Boolean`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧边界和样本有效性。

- `start` — 指示输入帧的开始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **frameType** — 帧类型 标量

*自 R2024b 起*

帧类型，指定为 `Boolean` 标量。如果指定 `0`，模块将输入数据视为正常帧；如果指定 `1`，模块将输入数据视为短帧。

#### 依赖

要启用此端口，请将 **Frame type source** 参数设置为 `Input port`。

**数据类型：** `Boolean`

### **codeRateIdx** — 码率索引 整数

码率索引，指定为整数。码率索引值范围为 0 到 10。每个码率索引值表示特定码率，如下表所示。

| codeRateIdx 值 | 码率 |
| --- | --- |
| `0` | 1/4 |
| `1` | 1/3 |
| `2` | 2/5 |
| `3` | 1/2 |
| `4` | 3/5 |
| `5` | 2/3 |
| `6` | 3/4 |
| `7` | 4/5 |
| `8` | 5/6 |
| `9` | 8/9 |
| `10` | 9/10 |

#### 依赖

要启用此端口，请将 **Code rate source** 参数设置为 `Input port`。

**数据类型：** `fixdt(0,4,0)`

### 输出

### **data** — 解码消息位 标量 | 向量

解码消息位，以 `Boolean` 标量或 8 元素列向量返回。输出数据类型和维度与输入相同。

**数据类型：** `Boolean`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，以 `samplecontrol` 总线返回。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧边界和样本有效性。

- `start` — 指示输出帧的开始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **numCorrErr** — 已纠正错误数量 标量

已纠正错误数量，以标量返回。

- – 1 — 表示模块输出中包含无法纠正的错误
- 0 — 表示模块输出中不包含错误
- 范围从 1 到 12 — 表示模块输出中纠正的错误数量

#### 依赖

要启用此端口，请选择 **Output number of corrected symbol errors** 参数。

**数据类型：** `fixdt(1,5,0)`

### **nextFrame** — 模块就绪指示符 标量

模块就绪指示符，以 `Boolean` 标量返回。

当模块准备好接受下一帧的开始时，模块将此信号设置为 `1` (`true`)。如果模块在 **nextFrame** 为 `0` (`false`) 时接收到输入 **ctrl.start** 信号，则模块丢弃正在处理的帧并开始处理新数据。

**数据类型：** `Boolean`

## 参数

### **FEC frame type source** — FEC 帧类型源 `Property` (default) | `Input port`

*自 R2024b 起*

将 FEC 帧类型源选择为 `Property` 或 `Input port`。

- `Property` — 选择此选项以启用 **FEC frame type** 参数。
- `Input port` — 选择此选项以启用 **frameType** 端口。

有关正常和短 FEC 帧类型的详细信息，请参阅 [1]。

### **FEC frame type** — FEC 帧类型 `Normal` (default) | `Short`

将 FEC 帧类型选择为 `Normal` 或 `Short`。

有关正常和短 FEC 帧类型的详细信息，请参阅 [1]。

### **Code rate source** — 码率源 `Property` (default) | `Input port`

将码率源选择为 `Property` 或 `Input port`。

- `Property` — 选择此选项以启用 **Code rate** 参数。
- `Input port` — 选择此选项以启用 **codeRateIdx** 输入端口。

### **Code rate** — 码率 `1/4` (default) | `1/3` | `2/5` | `1/2` | `3/5` | `2/3` | `3/4` | `4/5` | `5/6` | `8/9` | `9/10`

选择码率。

#### 依赖

要启用此参数，请将 **Code rate source** 参数设置为 `Property`。

### **Output number of corrected errors** — 已纠正错误数量 `off` (default) | `on`

选择此参数以启用 **numCorrErr** 输出端口。此端口输出已纠正错误的数量。

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
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |

要在 Intel® Altera® 器件上获得有效的综合结果，请执行以下设置：

- 对于 VHDL — 在 Configuration Parameters 对话框中，转到 **HDL Code Generation > Global Settings > Coding style** 选项卡，并将 **RAM Architecture** 参数设置为 `Generic RAM without clock enable`。
- 对于 Verilog — 在 Configuration Parameters 对话框中，转到 **HDL Code Generation > Global Settings > Coding style** 选项卡，并清除 **Initialize all RAM blocks** 选项。

**限制**

不能为 Resettable Synchronous Subsystem (HDL Coder) 内的此模块生成 HDL。

## 版本历史

**在 R2022a 中引入**

### R2024b：支持基于帧的输入数据以及通过输入端口指定帧类型的选项

DVB-S2 BCH Decoder 模块现在支持基于帧的输入。该模块现在提供新参数 **FEC frame source**，您可以使用它通过输入端口或属性指定帧类型。该模块经过优化，可最大程度减少标量和基于帧的输入数据对 BRAM 的使用。

### R2023b：资源利用率改进

DVB-S2 BCH Decoder 模块现在改进了其资源利用率数值。可以看到 Block RAM 的使用量显著减少。

| 版本 | Slice LUTs | Slice Registers | DSPs | Block RAM |
| --- | --- | --- | --- | --- |
| R2022a | 5586 | 5294 | 4 | 638 |
| R2023b | 9057 | 5715 | 4 | 103 |

## 描述

根据 DVB-S2 标准从 BCH 码字中解码并恢复消息

DVB-S2 BCH Decoder 模块根据 Digital Video Broadcast Satellite Second Generation (DVB-S2) 标准 [1]，从 Bose-Chaudhuri-Hocquenghem (BCH) 码字中解码并恢复消息。该模块接受低密度奇偶校验 (LDPC) 解码后的码字数据位以及控制信号流。它输出解码后的消息数据位、控制信号流、指示模块何时准备好接受新输入的信号，以及提供输出中已纠正错误数量的可选信号。该模块支持标量或 8 元素列向量作为输入。

该模块支持两种前向纠错 (FEC) 帧类型：正常和短。该模块提供适合 HDL 代码生成和硬件部署的架构。您可以在卫星通信的 DVB-S2 接收机中使用此模块。
