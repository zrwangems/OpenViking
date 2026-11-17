---
type: simulink-block
title: 'DVB-S2 LDPC Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'dvbs2ldpcdecoder'
documentation_source_path: 'ref/dvbs2ldpcdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# DVB-S2 LDPC Decoder

## 端口
```yaml
ports:
- name: data
  summary: LLR 值 标量 | 列向量 *(自 R2025a 起)*
  direction: input
  data_types: int8 | int16 | signed fixed point
- name: ctrl
  summary: 伴随样本流的控制信号 samplecontrol 总线
  direction: input
  data_types: bus
- name: frameType
  summary: FEC 帧类型 标量
  direction: input
  data_types: Boolean
- name: codeRateIdx
  summary: 码率索引 整数
  direction: input
  data_types: fixdt(0,4,0)
- name: iter
  summary: 迭代次数 标量
  direction: input
  data_types: uint8
- name: scalingFactorIdx
  summary: 缩放因子索引 标量
  direction: input
  data_types: uint8
- name: data
  summary: 解码比特 标量 | 列向量 *(自 R2025a 起)*
  direction: output
  data_types: Boolean
- name: ctrl
  summary: 伴随样本流的控制信号 samplecontrol 总线
  direction: output
  data_types: bus
- name: nextFrame
  summary: 模块就绪指示标量
  direction: output
  data_types: Boolean
- name: parityCheck
  summary: 奇偶校验状态指示标量
  direction: output
  data_types: Boolean
- name: actIter
  summary: 实际迭代次数标量
  direction: output
  data_types: uint8
```

### 输入

### **data** — LLR 值 标量 | 列向量 *(自 R2025a 起)*

LLR 值，指定为标量或八元素列向量。

对于 HDL 代码生成，请以有符号定点格式指定此值。输入字长必须在 4 到 16 的范围内。

**数据类型：** `int8` | `int16` | `signed fixed point`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界以及样本的有效性。

- `start` — 指示输入帧的起始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **frameType** — FEC 帧类型 标量

FEC 帧类型，指定为布尔标量。

- `0` — 指示正常帧
- `1` — 指示短帧

#### 依赖关系

要启用此端口，请将 **FEC frame source** 参数设置为 `Input port`。

**数据类型：** `Boolean`

### **codeRateIdx** — 码率索引 整数

码率索引，指定为整数。码率索引值的范围为 0 到 10。每个码率索引值代表一个特定的码率，如下表所示。

| `codeRateIdx` 值 | 码率 |
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
| `10` | 9/10（短帧不支持） |

必须以 `fixdt(0,4,0)` 格式指定此值。

#### 依赖关系

要启用此端口，请执行以下操作之一：

- 将 **FEC frame source** 参数设置为 `Input port`。
- 将 **FEC frame source** 参数设置为 `Property`，并将 **Code rate source** 参数设置为 `Input port`。

**数据类型：** `fixdt(0,4,0)`

### **iter** — 迭代次数 标量

迭代次数，指定为 1 到 63 范围内的无符号整数。

如果指定的 **iter** 值大于 63 或小于 1，模块将覆盖您的指定值，并在解码前将 **iter** 值设置为 `8`。

#### 依赖关系

要启用此端口，请将 **Decoding termination criteria** 参数设置为 `Max` 或 `Early`，并将 **Source for number of iterations** 参数设置为 `Input port`。

**数据类型：** `uint8`

### **scalingFactorIdx** — 缩放因子索引 标量

*自 R2024b 起*

缩放因子索引，指定为标量。每个缩放因子索引值代表一个特定的缩放因子，如下表所示。

| `scalingFactorIdx` 值 | 缩放因子 |
| --- | --- |
| `0` | 0.5 |
| `1` | 0.5625 |
| `2` | 0.6250 |
| `3` | 0.6875 |
| `4` | 0.7500 |
| `5` | 0.8125 |
| `6` | 0.8750 |
| `7` | 0.9375 |
| `8` | 1 |

必须以 `fixdt(0,4,0)` 格式指定此值。如果指定的值不是此表中列出的值，模块将显示警告消息，并将缩放因子索引应用为 `4` 并继续其操作。

#### 依赖关系

要启用此端口，请将 **Algorithm** 参数设置为 `Normalized min-sum`，然后将 **Source for scaling factor** 参数设置为 `Input port`。

**数据类型：** `uint8`
### 输出

### **data** — 解码比特 标量 | 列向量 *(自 R2025a 起)*

解码比特，返回为标量或大小为 8 的列向量。

**数据类型：** `Boolean`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，以 `samplecontrol` 总线形式返回。该总线包含 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界以及样本的有效性。

- `start` — 指示输出帧的起始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **nextFrame** — 模块就绪指示标量

模块就绪指示，以布尔标量形式返回。

当模块准备好接受下一帧的起始时，模块将该信号设置为 `1`（`true`）。如果模块在 **nextFrame** 为 `0`（`false`）时接收到输入 **ctrl.start** 信号，模块将丢弃正在处理的帧并开始处理新数据。

**数据类型：** `Boolean`

### **parityCheck** — 奇偶校验状态指示标量

奇偶校验状态指示，以布尔标量形式返回。该端口指示解码操作后的奇偶校验状态。

- `0` — 指示奇偶校验失败
- `1` — 指示奇偶校验通过

#### 依赖关系

要启用此端口，请选择 **Enable parity check output port** 参数。

**数据类型：** `Boolean`

### **actIter** — 实际迭代次数标量

模块解码输出所采用的实际迭代次数，以标量形式返回。

#### 依赖关系

要启用此端口，请将 **Decoding termination criteria** 参数设置为 `Early`。

**数据类型：** `uint8`
## 参数
```yaml
parameters:
- name: FEC frame source
  summary: FEC 帧来源 Input port（默认）| Property
  group: ''
- name: FEC frame type
  summary: FEC 帧类型 Normal（默认）| Short
  group: ''
- name: Parallelism level
  summary: 并行度 45（默认）| 180
  group: ''
- name: Code rate source
  summary: 码率来源 Property（默认）| Input port
  group: ''
- name: Code rate
  summary: 码率 1/4（默认）| 1/3 | 2/5 | 1/2 | 3/5 | 2/3 | 3/4 | 4/5 | 5/6 | 8/9 | 9/10
  group: ''
- name: Algorithm
  summary: LDPC 解码算法 Min-sum（默认）| Normalized min-sum
  group: ''
- name: Source for scaling factor
  summary: 缩放因子来源 Property（默认）| Input port
  group: ''
- name: Scaling factor
  summary: 归一化最小和解码的缩放因子 0.75（默认）| 范围 0.5 到 1 的标量，以 0.0625 递增
  group: ''
- name: Decoding termination criteria
  summary: 终止条件 Max（默认）| Early
  group: ''
- name: Source for number of iterations
  summary: 迭代次数的来源选择 Property（默认）| Input port
  group: ''
- name: Number of iterations
  summary: 解码迭代次数 8（默认）| 范围从 1 到 63 的整数
  group: ''
- name: Maximum number of iterations
  summary: 最大解码迭代次数 8（默认）| 范围从 1 到 63 的整数
  group: ''
- name: Enable parity check output port
  summary: 奇偶校验状态 off（默认）| on
  group: ''
```

### **FEC frame source** — FEC 帧来源 `Input port`（默认）| `Property`

选择 FEC 帧来源为 `Input port` 或 `Property`。

- `Property` — 选择此选项以启用 **FEC frame type** 参数。
- `Input port` — 选择此选项以启用 **frameType** 端口。

### **FEC frame type** — FEC 帧类型 `Normal`（默认）| `Short`

选择 FEC 帧类型为 `Normal` 或 `Short`。

#### 依赖关系

要启用此参数，请将 **FEC frame source** 参数设置为 `Property`。

### **Parallelism level** — 并行度 `45`（默认）| `180`

*自 R2024b 起*

选择并行度为 `45` 或 `180`。

### **Code rate source** — 码率来源 `Property`（默认）| `Input port`

选择码率来源为 `Property` 或 `Input port`。

- `Property` — 选择此选项以启用 **Code rate** 参数。
- `Input port` — 选择此选项以启用 **codeRateIdx** 端口。

#### 依赖关系

要启用此参数，请将 **FEC frame source** 参数设置为 `Property`。

### **Code rate** — 码率 `1/4`（默认）| `1/3` | `2/5` | `1/2` | `3/5` | `2/3` | `3/4` | `4/5` | `5/6` | `8/9` | `9/10`

选择码率。

**注意**

短帧不支持码率 `9/10`。

#### 依赖关系

要启用此参数，请将 **FEC frame source** 参数设置为 `Property`，并将 **Code rate source** 参数设置为 `Property`。

### **Algorithm** — LDPC 解码算法 `Min-sum`（默认）| `Normalized min-sum`

选择 LDPC 解码算法的类型。有关更多信息，请参阅 Algorithm。

- `Min-sum` — 使用此选项可选择采用最小和近似的分层置信传播算法。有关更多信息，请参阅 Min-Sum Approximation。
- `Normalized min-sum` — 使用此选项可选择采用归一化最小和近似的分层置信传播算法。有关更多信息，请参阅 Normalized Min-Sum Approximation。

### **Source for scaling factor** — 缩放因子来源 `Property`（默认）| `Input port`

*自 R2024b 起*

指定缩放因子。

- `Property` — 选择此选项以启用 **Scaling factor** 参数。
- `Input port` — 选择此选项以启用 **scalingFactorIdx** 端口。

#### 依赖关系

要启用此参数，请将 **Algorithm** 参数设置为
`Normalized min-sum`。

### **Scaling factor** — 归一化最小和解码的缩放因子 `0.75`（默认）| 范围 0.5 到 1 的标量，以 0.0625 递增

将缩放因子指定为范围 0.5 到 1 的标量，以 0.0625 递增。
为获得更好的性能，建议使用缩放因子 `0.75`
和 `1`。

#### 依赖关系

要启用此参数，请将 **Algorithm** 参数设置为
`Normalized min-sum`，并将 **Source for scaling
factor** 参数设置为 `Property`。

### **Decoding termination criteria** — 终止条件 `Max`（默认）| `Early`

选择解码终止条件。

- `Max` — 当模块达到模块掩码中指定的迭代次数或通过
  **iter** 输入端口指定的迭代次数时，终止解码。
- `Early` — 当模块满足所有奇偶校验时，或当模块达到模块掩码中提供的最大迭代次数时，终止解码。

### **Source for number of iterations** — 迭代次数的来源选择 `Property`（默认）| `Input port`

选择用于指定迭代次数的来源。

您可以通过使用输入端口或参数来设置迭代次数。

- `Property` — 选择此选项以启用
  **Number of iterations** 参数。
- `Input port` — 选择此选项以启用
  **iter** 端口。

### **Number of iterations** — 解码迭代次数 `8`（默认）| 范围从 1 到 63 的整数

指定解码迭代次数。

#### 依赖关系

要启用此参数，请将 **Decoding termination
criteria** 参数设置为 `Max`，并将
**Source for number of iterations** 参数设置为
`Property`。

### **Maximum number of iterations** — 最大解码迭代次数 `8`（默认）| 范围从 1 到 63 的整数

指定最大解码迭代次数。

#### 依赖关系

要启用此参数，请将 **Decoding termination
criteria** 参数设置为 `Early`，并将
**Source for number of iterations** 参数设置为
`Property`。

### **Enable parity check output port** — 奇偶校验状态 `off`（默认）| `on`

选择此参数以启用 **parityCheck** 输出端口，以
查看奇偶校验的状态。
## 所属库

Wireless HDL Toolbox / Error Detection and Correction

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和
综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

无法在可复位同步子系统 (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2022a 中引入**

### R2025a：支持向量输入

DVB-S2 LDPC Decoder 模块现在支持列向量作为输入。

### R2024b：支持并行度 180 以及通过输入端口指定缩放因子的选项

DVB-S2 LDPC Decoder 模块现在支持通过输入端口指定缩放因子，并支持为模块指定并行度以实现更快的解码。

- 要启用 **scalingFactorIdx** 输入端口，请将 **Algorithm** 参数设置为 `Normalized min-sum`，然后将 **Source for scaling factor** 参数设置为 `Input port`。
- 要为模块指定并行度，请将 **Parallelism level** 参数设置为 `45` 或 `180`。

## 描述

根据 DVB-S2 标准解码 LDPC 码

DVB-S2 LDPC Decoder 模块使用分层置信传播，并结合最小和近似与归一化最小和近似算法，实现低密度奇偶校验（LDPC）解码器，以根据数字视频广播卫星第二代（DVB-S2）标准解码 LDPC 码。该模块接受对数似然比（LLR）值、控制信号流、帧类型和码率作为输入，并输出解码比特、控制信号流以及指示模块何时准备好接受新输入的信号。

DVB-S2 LDPC Decoder 模块支持提前终止，以帮助在高信噪比（SNR）条件下提高解码性能和收敛速度。该模块支持 45 和 180 两个级别的并行度。该模块通过输入/输出（I/O）接口支持标量和向量值。它还支持 normal 和 short 类型的纠错（FEC）帧，并支持 DVB-S2 标准所支持的所有码率。有关 DVB-S2 标准的更多信息，请参阅 [1]。

该模块提供适合 HDL 代码生成和硬件部署的架构。您可以在 DVB-S2 调制解调器开发中使用此模块。
