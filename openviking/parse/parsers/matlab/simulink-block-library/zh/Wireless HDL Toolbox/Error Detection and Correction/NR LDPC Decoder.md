---
type: simulink-block
title: 'NR LDPC Decoder'
family: 'error-detection-and-correction'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'nrldpcdecoder'
documentation_source_path: 'ref/nrldpcdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# NR LDPC Decoder

## 端口

### 输入

### **data** — Input LLR values scalar | column vector

输入对数似然比 (LLR) 值，指定为大小为 64 的标量或列向量。

此输入的数据类型必须为 signed fixed-point，字长从 4 到 16 位。有关如何指定向量输入数据的详细信息，请参阅 Specifying Vector Input。

**数据类型：** `int8` | `int16` | `fixed point`

### **ctrl** — Control signals accompanying sample stream `samplecontrol` bus

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，它们指示帧边界和样本有效性。

- `start` — 指示输入帧的开始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **bgn** — Base graph number scalar

基图编号，指定为标量。当此值为 `0` 时，模块应用 *bgn 1*。当此值为 `1` 时，模块应用 *bgn 2*。有关 *bgn 1* 和 *bgn 2* 的更多信息，请参阅 TS 38.212 [1] 的第 5.3.2 节。

**数据类型：** `Boolean`

### **liftingSize** — Input lifting size scalar

输入提升大小，指定为标量。

对于无效的 **liftingSize** 值，模块丢弃当前帧并等待新帧。有关支持的提升大小值的更多信息，请参阅 TS 38.212 [1] 的第 5.3.2 节。

**数据类型：** `uint16`

### **iter** — Number of iterations scalar

迭代次数，指定为 1 到 63 范围内的整数。

如果将 **iter** 指定为大于 63 的值，模块会自动将 **iter** 值设置为 `8` 并执行解码操作。

#### 依赖关系

要启用此端口，请将 **Source for number of iterations** 参数设置为 `Input port`。

**数据类型：** `uint8`

### **numRows** — Number of rows scalar

行数，指定为标量。

当将 **bgn** 值设置为 `0` 时，模块支持的行数范围为 4 到 46。当将 **bgn** 值设置为 `1` 时，模块支持的行数范围为 4 到 42。

#### 依赖关系

要启用此端口，请选中 **Enable multiple code rates** 参数。

**数据类型：** `fixdt(0,6,0)`

### 输出

### **data** — Decoded output data bits scalar | column vector

解码输出数据位，返回为大小为 64 的标量或列向量。

模块以与输入 LLR 值相似的格式输出数据位。以相似格式提取这些输出数据位以进行进一步处理。

**数据类型：** `Boolean`

### **ctrl** — Control signals accompanying sample stream `samplecontrol` bus

伴随样本流的控制信号，返回为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，它们指示帧边界和样本有效性。

- `start` — 指示输出帧的开始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **liftingSize** — Output lifting size scalar

输出提升大小，返回为标量。

**数据类型：** `uint16`

### **nextFrame** — Block ready indicator Boolean scalar

模块就绪指示，返回为 Boolean 标量。

当模块准备好接受下一帧的开始信号时，模块将此信号设置为 `1` (`true`)。如果模块在 **nextFrame** 为 `0` (`false`) 时接收到输入 **ctrl.start** 信号，模块会丢弃正在处理的帧并开始处理新数据。

**数据类型：** `Boolean`

### **actIter** — Actual number of iterations scalar

模块解码输出所采用的实际迭代次数，返回为标量。

#### 依赖关系

要启用此端口，请将 **Decoding termination criteria** 参数设置为 `Early`。

**数据类型：** `uint8`

### **parityCheck** — Parity check status indicator scalar

奇偶校验状态指示，返回为 Boolean 标量。该端口指示解码操作后的奇偶校验状态。

- `0` — 指示奇偶校验失败
- `1` — 指示奇偶校验通过

#### 依赖关系

要启用此端口，请选中 **Enable parity check output port** 参数。

**数据类型：** `Boolean`

## 参数

### **Algorithm** — 算法类型 `Min-sum` (默认) | `Normalized min-sum`

选择算法类型。有关更多信息，请参阅 Algorithm (5G Toolbox)。

### **Scaling factor** — 缩放因子 `0.75` (默认) | 0.5 到 1 范围内的值，以 0.0625 递增

指定缩放因子。

#### 依赖关系

要启用此参数，请将 **Algorithm** 参数设置为 `Normalized min-sum`。

### **Decoding termination criteria** — 终止条件 `Max` (默认) | `Early`

选择解码终止条件。

- `Max` — 当模块达到通过 **Number of iterations** 参数或 **iter** 输入端口指定的迭代次数时，终止解码
- `Early` — 当满足所有奇偶校验时，或当模块达到通过 **Maximum number of iterations** 参数或 **iter** 输入端口指定的最大迭代次数时，终止解码

### **Source for number of iterations** — 迭代次数的源选择 `Property` (默认) | `Input port`

选择用于指定迭代次数的源。

可以使用输入端口或参数设置迭代次数。

- 选择 `Property` 以启用 **Number of iterations** 参数或 **Maximum number of iterations** 参数。
- 选择 `Input port` 以启用 **iter** 端口。

### **Number of iterations** — 迭代次数 `8` (默认) | 1 到 63 范围内的整数

指定迭代次数。

#### 依赖关系

要启用此参数，请将 **Decoding termination criteria** 参数设置为 `Max`，并将 **Source for number of iterations** 参数设置为 `Property`。

### **Maximum number of iterations** — 最大迭代次数 `8` (默认) | 1 到 63 范围内的整数

指定最大迭代次数。

#### 依赖关系

要启用此参数，请将 **Decoding termination criteria** 参数设置为 `Early`，并将 **Source for number of iterations** 参数设置为 `Property`。

### **Enable multiple code rates** — 多个码率 `off` (默认) | `on`

选择此参数以启用 **numRows** 输入端口来支持多个码率。有关多个码率的更多信息，请参阅 Multiple Code Rates。

### **Enable parity check output port** — 奇偶校验状态 `off` (默认) | `on`

选择此参数以启用 **parityCheck** 输出端口来查看奇偶校验的状态。

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

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入到生成代码中的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入到生成代码中的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

不能在 Resettable Synchronous Subsystem (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2020a 中引入**

## 描述

根据 5G NR 标准解码 LDPC 码

NR LDPC Decoder 模块实现具有硬件友好控制信号的低密度奇偶校验 (LDPC) 解码器。该模块接受打孔对数似然比 (LLR) 值、控制信号流、基图编号和提升大小。该模块输出解码位、控制信号流、提升大小，以及指示模块何时准备好接受新输入的信号。

此模块提供用于实现分层置信传播的选项，可使用归一化最小和近似算法或最小和近似算法。此实现与函数 `nrLDPCDecode` (5G Toolbox) 的实现匹配。您可以按照 5G 新无线电 (NR) 标准 TS 38.212 [1]，将此模块用于下行链路和上行链路共享信道以及寻呼信道的信道编码。

NR LDPC Decoder 模块支持标量和 64 元素列向量输入。该模块支持提前终止功能，以帮助在高信噪比 (SNR) 条件下提高解码性能和加快收敛速度。该模块支持多个码率的解码，以帮助在高度码率灵活性下实现高吞吐量效率。该模块提供适合 HDL 代码生成和硬件部署的架构。有关更多信息，请参阅 Algorithms。
