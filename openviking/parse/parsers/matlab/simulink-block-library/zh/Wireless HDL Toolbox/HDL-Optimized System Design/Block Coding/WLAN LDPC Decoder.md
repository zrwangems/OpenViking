---
type: simulink-block
title: 'WLAN LDPC Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'HDL-Optimized System Design / Block Coding'
documentation_page: 'wlanldpcdecoder'
documentation_source_path: 'ref/wlanldpcdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# WLAN LDPC Decoder

## 端口

### 输入

### **data** — LLR 值，标量 | 列向量

LLR 值，指定为标量或大小为 8×1 的列向量。

对于 HDL 代码生成，请以 `signed fixed point` 格式指定此值。输入字长必须在 4 到 16 范围内。

**数据类型：** `int8` | `int16` | `signed fixed point`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界以及样本的有效性。

- `start` — 指示输入帧的起始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **blkLenIdx** — 块长度索引 `0` | 1 | 2

块长度索引，指定为 `0`、`1` 或 `2`。块长度根据指定的块长度索引而变化。

此表显示了块长度索引值及其对应的块长度。

| blkLenIdx 值 | 块长度 |
| --- | --- |
| `0` | 648 |
| `1` | 1296 |
| `2` | 1944 |

当指定的值不是 `0`、`1` 或 `2` 时，模块会丢弃该帧，并将 **nextFrame** 输出端口设置为 `1`。

#### 依赖关系

要启用此端口，请将 **Standard** 参数设置为 `IEEE 802.11 n/ac/ax`。

**数据类型：** `fixdt(0,2,0)`

### **codeRateIdx** — 码率索引 `0` | 1 | 2 | 3

码率索引，指定为 `0`、`1`、`2` 或 `3`。码率根据指定的标准和码率索引而变化。

此表显示了基于标准的码率索引值及其对应的码率。

| Standard 参数值 | codeRateIdx 值 | 码率 |
| --- | --- | --- |
| `IEEE 802.11 n/ac/ax` | `0` | 1/2 |
| `1` | 2/3 |
| `2` | 3/4 |
| `3` | 5/6 |
| `IEEE 802.11 ad` | `0` | 1/2 |
| `1` | 5/8 |
| `2` | 3/4 |
| `3` | 13/16 |

**数据类型：** `fixdt(0,2,0)`

### **iter** — 迭代次数 标量

迭代次数，指定为 1 到 63 范围内的无符号整数。

如果指定的 **iter** 值大于 63 或小于 1，模块将覆盖你的指定值，并在解码前将 **iter** 值设置为 `8`。

#### 依赖关系

要启用此端口，请将 **Decoding termination criteria** 参数设置为 `Max`，并将 **Source for number of iterations** 参数设置为 `Input port`。

**数据类型：** `uint8`
### 输出

### **data** — 解码比特，标量 | 列向量

解码比特，以标量或大小为 8×1 的列向量形式返回。

对于向量输入，如果输出数据长度不是 8 的倍数，模块会在输出末尾追加零，使其成为 8 的倍数。

例如，当您将 **Standard** 参数设置为 `IEEE 802.11 n/ac/ax`，将 **blkLenIdx** 输入端口设置为 `0`，并将 **codeRateIdx** 输入端口设置为 `2` 时，模块不会返回 486 个样本，而是向 486 个样本追加两个零，使其成为 8 的倍数。在这种情况下，模块会在 61 (488/8) 个时钟周期内返回 488 个样本。

**数据类型：** `Boolean`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，返回为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界以及样本的有效性。

- `start` — 指示输出帧的起始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **nextFrame** — 模块就绪指示符 Boolean 标量

模块就绪指示符，以 Boolean 标量形式返回。

当模块准备好接受下一帧的起始时，模块会将此信号设置为 `1` (`true`)。如果模块在 **nextFrame** 为 `0` (`false`) 时接收到输入 **ctrl.start** 信号，则模块会丢弃正在处理的帧，并开始处理新数据。

**数据类型：** `Boolean`

### **actIter** — 实际迭代次数 标量

模块解码输出所采用的实际迭代次数，以标量形式返回。

#### 依赖关系

要启用此端口，请将 **Decoding termination criteria** 参数设置为 `Early`。

**数据类型：** `uint8`

### **parityCheck** — 奇偶校验状态指示符 标量

奇偶校验状态指示符，以 Boolean 标量形式返回。该端口指示解码操作后的奇偶校验状态。

- `0` — 指示奇偶校验失败
- `1` — 指示奇偶校验通过

#### 依赖关系

要启用此端口，请选中 **Enable parity check output port** 参数。

**数据类型：** `Boolean`

## 参数

### **Standard** — 标准类型 `IEEE 802.11 n/ac/ax`（默认） | `IEEE 802.11 ad`

选择标准类型。有关更多信息，请参阅 [1]、[2] 和 [3]。

当您将 **Standard** 参数设置为 `IEEE 802.11 ad` 时，**blkLenIdx** 输入端口将被禁用，模块在其操作中会考虑固定的块长度 672。

### **Algorithm** — LDPC 解码算法 `Min-sum`（默认） | `Normalized min-sum`

选择 LDPC 解码算法的类型。有关更多信息，请参阅算法。

- `Min-sum` — 使用此选项可选择采用 min-sum 近似的分层置信传播算法。有关更多信息，请参阅 Min-Sum Approximation。
- `Normalized min-sum` — 使用此选项可选择采用归一化 min-sum 近似的分层置信传播算法。有关更多信息，请参阅 Normalized Min-Sum Approximation。

### **Scaling factor** — 用于归一化 min-sum 解码的缩放因子 `0.75`（默认） | 范围为 0.5 到 1、增量为 0.0625 的标量

将缩放因子指定为范围为 0.5 到 1、增量为 0.0625 的标量。

#### 依赖关系

要启用此参数，请将 **Algorithm** 参数设置为 `Normalized min-sum`。

### **Decoding termination criteria** — 终止条件 `Max`（默认） | `Early`

选择解码终止条件。

- `Max` — 当模块达到在模块掩码中或通过 **iter** 输入端口指定的迭代次数时，终止解码。
- `Early` — 当模块满足所有奇偶校验时，或当模块达到模块掩码中提供的最大迭代次数时，终止解码。

### **Source for number of iterations** — 迭代次数的源选择 `Property`（默认） | `Input port`

选择用于指定迭代次数的源。

您可以使用输入端口或参数来设置迭代次数。

- `Property` — 选择此选项可启用 **Number of iterations** 参数。
- `Input port` — 选择此选项可启用 **iter** 端口。

#### 依赖关系

要启用此参数，请将 **Decoding termination criteria** 参数设置为 `Max`。

### **Number of iterations** — 解码迭代次数 `8`（默认） | 范围为 1 到 63 的整数

指定解码迭代次数。

#### 依赖关系

要启用此参数，请将 **Decoding termination criteria** 参数设置为 `Max`，并将 **Source for number of iterations** 参数设置为 `Property`。

### **Maximum number of iterations** — 最大解码迭代次数 `8`（默认） | 范围为 1 到 63 的整数

指定最大解码迭代次数。

#### 依赖关系

要启用此参数，请将 **Decoding termination criteria** 参数设置为 `Early`。

### **Enable parity check output port** — 奇偶校验状态 `off`（默认） | `on`

选择此参数可启用 **parityCheck** 输出端口，以查看奇偶校验状态。

## 所属库

Wireless HDL Toolbox / Error Detection and Correction

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink® 加速模式和快速加速模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出处的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

不能在 Resettable Synchronous Subsystem (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2021b 中引入**

## 描述

根据 WLAN 标准解码 LDPC 码

WLAN LDPC Decoder 模块使用分层置信传播以及 min-sum 近似和归一化 min-sum 近似算法实现低密度奇偶校验 (LDPC) 解码器，以根据无线局域网 (WLAN) 标准 IEEE® 802.11n™、802.11ac™、802.11ax™ 和 802.11ad™ 解码 LDPC 码。该模块接受对数似然比 (LLR) 值、控制信号流、块长度和码率作为输入，并输出解码比特、控制信号流以及一个指示模块何时准备好接受新输入的信号。

WLAN LPDC Decoder 模块支持标量输入和向量输入。该模块支持提前终止，以帮助在高信噪比 (SNR) 条件下提高解码性能和收敛速度。有关 WLAN 标准的更多信息，请参阅 [1]、[2] 和 [3]。

该模块提供适用于 HDL 代码生成和硬件部署的架构。您可以在 WLAN 调制解调器开发中使用此模块。
