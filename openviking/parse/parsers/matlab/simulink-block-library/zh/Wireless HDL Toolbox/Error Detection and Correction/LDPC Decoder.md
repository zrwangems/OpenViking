---
type: simulink-block
title: 'LDPC Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'ldpcdecoder'
documentation_source_path: 'ref/ldpcdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# LDPC Decoder

## 端口
```yaml
ports:
- name: data
  summary: 输入 LLR 值 标量 | 列向量
  direction: input
  data_types: int8 | int16 | fixed point
- name: ctrl
  summary: 伴随样本流的控制信号 samplecontrol 总线
  direction: input
  data_types: bus
- name: iter
  summary: 迭代次数 标量
  direction: input
  data_types: uint8
- name: data
  summary: 解码后的数据位 标量 | 列向量
  direction: output
  data_types: Boolean
- name: ctrl
  summary: 伴随样本流的控制信号 samplecontrol 总线
  direction: output
  data_types: bus
- name: actIter
  summary: 实际迭代次数 标量
  direction: output
  data_types: uint8
- name: parityCheck
  summary: 奇偶校验状态指示 标量
  direction: output
  data_types: Boolean
- name: nextFrame
  summary: 准备好接收新输入 标量
  direction: output
  data_types: Boolean
```

### 输入

### **data** — 输入 LLR 值 标量 | 列向量

输入对数似然比（LLR）值，指定为标量或大小为 *n* 的列向量，其中 *n* 必须是 **Block size** 的因子。

此输入的数据类型必须是有符号定点类型，字长范围为 [4, 16]，小数长度范围为 [0, 15]。

**数据类型：** `int8` | `int16` | `fixed point`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

- `start` — 指示输入帧的开始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **iter** — 迭代次数 标量

迭代次数，指定为范围 [1, 63] 内的整数。

如果将 **iter** 指定为大于 63 的值，该模块会自动将 **iter** 值设置为 `8` 并执行解码操作。

#### 依赖关系

要启用此端口，请将 **Source for number of iterations** 参数设置为 `Input port`。

**数据类型：** `uint8`
### 输出

### **data** — 解码后的数据位 标量 | 列向量

解码后的输出数据位，以标量或大小为 *n* 的列向量形式返回，其中 *n* 必须是 **Block size** 的因子。

**数据类型：** `Boolean`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，以 `samplecontrol` 总线形式返回。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

- `start` — 指示输出帧的开始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **actIter** — 实际迭代次数 标量

该模块解码输出所采用的实际迭代次数，以标量形式返回。

#### 依赖关系

要启用此端口，请将 **Decoding termination criteria** 参数设置为 `Early`。

**数据类型：** `uint8`

### **parityCheck** — 奇偶校验状态指示 标量

奇偶校验状态指示，以布尔标量形式返回。该端口指示解码操作后的奇偶校验状态。

- `0` — 指示奇偶校验失败
- `1` — 指示奇偶校验通过

#### 依赖关系

要启用此端口，请选择 **Enable parity check output port** 参数。

**数据类型：** `Boolean`

### **nextFrame** — 准备好接收新输入 标量

当该模块准备好接受下一帧的开始时，模块将此信号设置为 `1`。如果模块在 **nextFrame** 为 `0` 时接收到输入 **start** 信号，模块将丢弃正在进行的帧并开始处理新数据。

有关更多信息，请参阅 Using the nextFrame Output Signal。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Parity-check matrix
  summary: QC-LDPC 矩阵 [5 14 12 1 2 37 45 26 24 0 3 -1 34 7 46 10 -1 -1 -1 -1; 0 35 1 26 0 10 16 16 34 4 2 23 0 51 -1 49 20
    -1 -1 -1; 12 28 22 46 3 16 51 2 25 29 19 18 52 -1 37 -1 34 39 -1 -1; 0 51 16 31 13 39 27 33 8 27 53 13 -1 52 33 -1 -1
    38 7 -1; 36 6 3 51 4 19 4 45 48 9 -1 11 22 23 43 -1 -1 -1 14 1]（默认）| 任何具有循环权重 1 的 QC-LDPC 矩阵
  group: ''
- name: Block size
  summary: 块大小 56（默认）| 范围 [2, 512] 内的整数
  group: ''
- name: Algorithm
  summary: 算法类型 Min-sum（默认）| Normalized min-sum
  group: ''
- name: Scaling factor
  summary: 缩放因子 0.75（默认）| 范围从 0.5 到 1、以 0.0625 递增的值
  group: ''
- name: Decoding termination criteria
  summary: 终止条件 Max（默认）| Early
  group: ''
- name: Source for number of iterations
  summary: 迭代次数来源选择 Property（默认）| Input port
  group: ''
- name: Number of iterations
  summary: 迭代次数 8（默认）| 范围 [1, 63] 内的整数
  group: ''
- name: Maximum number of iterations
  summary: 最大迭代次数 8（默认）| 范围 [1, 63] 内的整数
  group: ''
- name: Enable parity check output port
  summary: 奇偶校验状态 off（默认）| on
  group: ''
```

### **Parity-check matrix** — QC-LDPC 矩阵 `[5 14 12 1 2 37 45 26 24 0 3 -1 34 7 46 10 -1 -1 -1 -1; 0 35 1 26 0 10 16 16 34 4 2 23 0 51 -1 49 20 -1 -1 -1; 12 28 22 46 3 16 51 2 25 29 19 18 52 -1 37 -1 34 39 -1 -1; 0 51 16 31 13 39 27 33 8 27 53 13 -1 52 33 -1 -1 38 7 -1; 36 6 3 51 4 19 4 45 48 9 -1 11 22 23 43 -1 -1 -1 14 1]`（默认）| 任何具有循环权重 1 的 QC-LDPC 矩阵

指定大小为 *M*×*N* 的 QC-LDPC 奇偶校验矩阵，其中 *M* 是奇偶校验矩阵中的行数，*N* 是奇偶校验矩阵中的列数。*N* 必须在范围 [4, 128] 内。*M* 必须小于 *N*，并且必须在范围 [3, *N*–1] 内。奇偶校验矩阵的最后 *M* 列在 GF(2) 中必须是可逆的。

要了解有关支持的奇偶校验矩阵的更多信息，请参阅 Parity-Check Matrix。

### **Block size** — 块大小 `56`（默认）| 范围 [2, 512] 内的整数

指定块大小。块大小必须是范围 [2, 512] 内的整数。

### **Algorithm** — 算法类型 `Min-sum`（默认）| `Normalized min-sum`

选择 LDPC 解码算法的类型。有关更多信息，请参阅 Algorithms。

- `Min-sum` — 使用此选项选择采用最小和近似的分层置信传播算法。有关更多信息，请参阅 Min-Sum Approximation。
- `Normalized min-sum` — 使用此选项选择采用归一化最小和近似的分层置信传播算法。有关更多信息，请参阅 Normalized Min-Sum Approximation。

### **Scaling factor** — 缩放因子 `0.75`（默认）| 范围从 0.5 到 1、以 0.0625 递增的值

指定缩放因子。

#### 依赖关系

要启用此参数，请将 **Algorithm** 参数设置为 `Normalized min-sum`。

### **Decoding termination criteria** — 终止条件 `Max`（默认）| `Early`

选择解码终止条件。

- `Max` — 当块达到通过 **Number of iterations** 参数或通过 **iter** 输入端口指定的迭代次数时，终止解码。
- `Early` — 当满足所有奇偶校验时，或当块达到通过 **Maximum number of iterations** 参数或通过 **iter** 输入端口指定的最大迭代次数时，终止解码。

### **Source for number of iterations** — 迭代次数来源选择 `Property`（默认）| `Input port`

选择用于指定迭代次数的来源。

您可以使用输入端口或参数来设置迭代次数。

- 选择 `Property` 以启用 **Number of iterations** 参数或 **Maximum number of iterations** 参数。
- 选择 `Input port` 以启用 **iter** 端口。

### **Number of iterations** — 迭代次数 `8`（默认）| 范围 [1, 63] 内的整数

指定迭代次数。

#### 依赖关系

要启用此参数，请将 **Decoding termination criteria** 参数设置为 `Max`，并将 **Source for number of iterations** 参数设置为 `Property`。

### **Maximum number of iterations** — 最大迭代次数 `8`（默认）| 范围 [1, 63] 内的整数

指定最大迭代次数。

#### 依赖关系

要启用此参数，请将 **Decoding termination criteria** 参数设置为 `Early`，并将 **Source for number of iterations** 参数设置为 `Property`。

### **Enable parity check output port** — 奇偶校验状态 `off`（默认）| `on`

选择此参数以启用 **parityCheck** 输出端口，以查看奇偶校验的状态。
## 所属库

Wireless HDL Toolbox / Error Detection and Correction

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

无法为可复位同步子系统 (HDL Coder) 内的此模块生成 HDL。

## 版本历史

**在 R2023b 中引入**

## 描述

解码准循环低密度奇偶校验码

LDPC Decoder 模块实现了一个具有硬件友好控制信号的准循环低密度奇偶校验 (QC-LDPC) 解码器。该模块接受对数似然比 (LLR) 值和控制信号流，并输出解码比特、控制信号流以及一个指示模块是否准备好接受新输入信号的信号。

此模块提供了一个选项，可使用归一化最小和近似算法或最小和近似算法来实现分层置信传播。LDPC Decoder 模块支持具有指定奇偶校验矩阵和块大小的标量和 N 元素列向量输入。该模块支持提前终止功能，以帮助在高信噪比 (SNR) 条件下提高解码性能和加快收敛速度。该模块支持循环权重为 1 的 QC-LDPC 码。

该模块支持多种码率的解码，以帮助在高度码率灵活性的情况下实现高吞吐效率。您可以使用此模块开发基于标准的或通用的接收机，该接收机使用 QC-LDPC 进行前向纠错 (FEC) 编码。该模块提供适用于 HDL 代码生成和硬件部署的架构。有关更多信息，请参阅算法。
