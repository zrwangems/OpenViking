---
type: simulink-block
title: 'CCSDS LDPC Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'ccsdsldpcdecoder'
documentation_source_path: 'ref/ccsdsldpcdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# CCSDS LDPC Decoder

## 端口
```yaml
ports:
- name: data
  summary: LLR 值 标量 | 列向量
  direction: input
  data_types: int8 | int16 | signed fixed point
- name: ctrl
  summary: 伴随样本流的控制信号 samplecontrol 总线
  direction: input
  data_types: bus
- name: codeRateIdx
  summary: 码率索引 0 | 1 | 2
  direction: input
  data_types: fixdt(0,2,0)
- name: blkLenIdx
  summary: 块长度索引 0 | 1 | 2
  direction: input
  data_types: fixdt(0,2,0)
- name: iter
  summary: 迭代次数 [1, 63] 范围内的整数
  direction: input
  data_types: uint8
- name: data
  summary: 解码比特 标量 | 列向量
  direction: output
  data_types: Boolean
- name: ctrl
  summary: 伴随样本流的控制信号 samplecontrol 总线
  direction: output
  data_types: bus
- name: nextFrame
  summary: 模块就绪指示 0 | 1
  direction: output
  data_types: Boolean
- name: actIter
  summary: 实际迭代次数 正标量
  direction: output
  data_types: uint8
- name: parityCheck
  summary: 奇偶校验状态指示 0 | 1
  direction: output
  data_types: Boolean
```

### 输入

### **data** — LLR 值 标量 | 列向量

LLR 值，指定为标量或八元素列向量。

对于 HDL 代码生成，请以有符号定点格式指定此值。输入字长必须为 [4, 16] 范围内的整数，小数长度必须在 [0, 15] 范围内。

**数据类型：** `int8` | `int16` | `signed fixed point`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

- `start` — 指示输入帧的开始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **codeRateIdx** — 码率索引 `0` | `1` | `2`

码率索引，指定为 `0`、`1` 或 `2`。必须以 `fixdt(0,2,0)` 格式指定此值。每个码率索引值代表特定的码率，如下表所示。

| `codeRateIdx` 值 | 码率 |
| --- | --- |
| `0` | 1/2 |
| `1` | 2/3 |
| `2` | 4/5 |

#### 依赖关系

要启用此端口，请将 **Configuration type** 参数设置为 `AR4JA LDPC`。

**数据类型：** `fixdt(0,2,0)`

### **blkLenIdx** — 块长度索引 `0` | `1` | `2`

块长度索引，指定为 `0`、`1` 或 `2`。必须以 `fixdt(0,2,0)` 格式指定此值。

块长度随指定的块长度索引而变化。输入块长度必须是 8 的倍数。下表显示了块长度索引值及其对应的块长度。

| `blkLenIdx` 值 | 块长度 |
| --- | --- |
| `0` | 1024 |
| `1` | 4096 |
| `2` | 16384 |

#### 依赖关系

要启用此端口，请将 **Configuration type** 参数设置为 `AR4JA LDPC`。

**数据类型：** `fixdt(0,2,0)`

### **iter** — 迭代次数 [1, 63] 范围内的整数

迭代次数，指定为 [1, 63] 范围内的无符号整数。

如果指定的 **iter** 值大于 63 或小于 1，则该模块将覆盖您的指定值，并在执行解码之前将 **iter** 值设置为 `8`。

#### 依赖关系

要启用此端口，请将 **Decoding termination criteria** 参数设置为 `Max`，并将 **Source for number of iterations** 参数设置为 `Input port`。

**数据类型：** `uint8`
### 输出

### **data** — 解码比特 标量 | 列向量

解码比特，以标量或八元素列向量形式返回。

**数据类型：** `Boolean`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，以 `samplecontrol` 总线形式返回。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

- `start` — 指示输出帧的开始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **nextFrame** — 模块就绪指示 `0` | `1`

模块就绪指示，以布尔标量形式返回。

当模块准备好接受下一帧的开始时，模块将此信号设置为 `1`。如果模块在 **nextFrame** 为 `0` 时接收到输入 **ctrl.start** 信号，则模块将丢弃正在进行的帧并开始处理新数据。

**数据类型：** `Boolean`

### **actIter** — 实际迭代次数 正标量

模块解码输出所采用的实际迭代次数，以正标量形式返回。

#### 依赖关系

要启用此端口，请将 **Decoding termination criteria** 参数设置为 `Early`。

**数据类型：** `uint8`

### **parityCheck** — 奇偶校验状态指示 `0` | `1`

奇偶校验状态指示，以布尔标量形式返回。该端口指示解码操作后奇偶校验的状态。

- `0` — 表示奇偶校验失败
- `1` — 表示奇偶校验通过

#### 依赖关系

要启用此端口，请选中 **Enable parity check output port** 参数。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Configuration type
  summary: 配置类型 (8160,7136) LDPC（默认）| AR4JA LDPC
  group: ''
- name: Decoding termination criteria
  summary: 终止条件 Max（默认）| Early
  group: ''
- name: Source for number of iterations
  summary: 迭代次数的来源选择 Property（默认）| Input port
  group: ''
- name: Number of iterations
  summary: 解码迭代次数 8（默认）| [1, 63] 范围内的整数
  group: ''
- name: Maximum number of iterations
  summary: 最大解码迭代次数 8（默认）| [1, 63] 范围内的整数
  group: ''
- name: Enable parity check output port
  summary: 奇偶校验状态 off（默认）| on
  group: ''
```

### **Configuration type** — 配置类型 `(8160,7136) LDPC`（默认）| `AR4JA LDPC`

选择配置类型。有关支持的配置的详细信息，请参阅 [1]。

### **Decoding termination criteria** — 终止条件 `Max`（默认）| `Early`

选择解码终止条件。

- `Max` — 当块达到模块掩码或 **iter** 输入端口指定的迭代次数时终止解码。
- `Early` — 当块完成所有奇偶校验或当块达到模块掩码指定的最大迭代次数时终止解码。

### **Source for number of iterations** — 迭代次数的来源选择 `Property`（默认）| `Input port`

选择指定迭代次数的来源。

您可以使用输入端口或参数来设置迭代次数。

- `Property` — 选择此选项以启用 **Number of iterations** 参数。
- `Input port` — 选择此选项以启用 **iter** 端口。

### **Number of iterations** — 解码迭代次数 `8`（默认）| [1, 63] 范围内的整数

指定解码迭代次数。

#### 依赖关系

要启用此参数，请将 **Decoding termination criteria** 参数设置为 `Max`，并将 **Source for number of iterations** 参数设置为 `Property`。

### **Maximum number of iterations** — 最大解码迭代次数 `8`（默认）| [1, 63] 范围内的整数

指定最大解码迭代次数。

#### 依赖关系

要启用此参数，请将 **Decoding termination criteria** 参数设置为 `Early`，并将 **Source for number of iterations** 参数设置为 `Property`。

### **Enable parity check output port** — 奇偶校验状态 `off`（默认）| `on`

选中此参数以启用 **parityCheck** 输出端口。使用此输出端口查看奇偶校验的状态。
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

无法在可复位同步子系统 (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2022b 中引入**

## 描述

根据 CCSDS 标准解码 LDPC 码

CCSDS LPDC 解码器模块使用分层置信传播算法和最小和近似实现低密度奇偶校验（LDPC）解码器，用于根据空间数据系统咨询委员会（CCSDS）标准 [1] 解码 LDPC 码。该模块接受对数似然比（LLR）值、控制信号流、块长度和码率作为输入。该模块输出解码比特、控制信号流以及一个指示模块何时准备好接受新输入的信号。

该模块支持标量输入和大小为 8 的向量输入。该模块支持提前终止，以在高信噪比（SNR）条件下提高解码性能和收敛速度。

该模块提供适合 HDL 代码生成和硬件部署的架构。您可以在卫星通信的 CCSDS 接收机中使用该模块。
