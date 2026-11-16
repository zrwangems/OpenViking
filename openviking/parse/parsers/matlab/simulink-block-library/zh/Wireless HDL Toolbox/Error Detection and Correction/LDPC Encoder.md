---
type: simulink-block
title: 'LDPC Encoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'ldpcencoder'
documentation_source_path: 'ref/ldpcencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# LDPC Encoder

## 端口

### 输入

### **data** — 数据位 标量 | 列向量 *(自 R2025a 起)*

数据位，指定为标量或大小为
*n* 的列向量，其中 *n* 必须是 **Block
size** 的因子。输入数据长度必须为
(*N*–*M*) x *Z*，其中
*M* 是奇偶校验矩阵中的行数，
*N* 是奇偶校验矩阵中的列数，*Z* 是块大小。

向量的大小必须是块大小的因子。当块大小为素数时，支持的向量大小为 1 和块大小本身。

**示例：** 如果块大小等于 56，支持的向量大小为 1、2、4、7、
8、14、28 和 56。

**示例：** 如果块大小等于 73，支持的向量大小为 1 和
73。

**数据类型：** `Boolean`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为
`samplecontrol` 总线。该总线包括 `start`、
`end` 和 `valid` 控制信号，这些信号指示帧的边界以及样本的有效性。

- `start` — 指示输入帧的开始
- `end` — 指示输入帧的结束
- `valid` — 指示输入
  **data** 端口上的数据有效

更多详细信息，请参阅样本控制总线。

**数据类型：** `bus`

### 输出

### **data** — 编码数据位 标量 | 列向量 *(自 R2025a 起)*

编码数据位，返回为标量或大小为
*n* 的列向量，其中 *n* 必须是 **Block
size** 的因子。

**数据类型：** `Boolean`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，返回为 `samplecontrol`
总线。该总线包括 `start`、`end` 和
`valid` 控制信号，这些信号指示帧的边界以及样本的有效性。

- `start` — 指示输出
  帧的开始
- `end` — 指示输出帧的结束
- `valid` — 指示输出
  **data** 端口上的数据有效

更多详细信息，请参阅样本控制总线。

**数据类型：** `bus`

### **nextFrame** — 准备好接受新输入 标量

当模块准备好接受下一帧的开始信号时，该模块将此信号设置为 `1`。如果该模块在 **nextFrame** 为 `0` 时接收到输入 **start** 信号，则该模块会丢弃正在进行的帧并开始处理新数据。

更多信息，请参阅使用 nextFrame 输出信号。

**数据类型：** `Boolean`

## 参数

### **Parity-check matrix** — QC-LDPC 矩阵 `[5 14 12 1 2 37 45 26 24 0 3 -1 34 7 46 10 -1 -1 -1 -1; 0 35 1 26 0 10 16 16 34 4 2 23 0 51 -1 49 20 -1 -1 -1; 12 28 22 46 3 16 51 2 25 29 19 18 52 -1 37 -1 34 39 -1 -1; 0 51 16 31 13 39 27 33 8 27 53 13 -1 52 33 -1 -1 38 7 -1; 36 6 3 51 4 19 4 45 48 9 -1 11 22 23 43 -1 -1 -1 14 1]`（默认）| 任何循环权重为 1 的 QC-LDPC 矩阵

指定大小为 *M*×*N* 的 QC-LDPC 奇偶校验矩阵，其中 *M* 是奇偶校验矩阵中的行数，*N* 是奇偶校验矩阵中的列数。*N* 必须在范围 [4, 128] 内。
*M* 必须小于 *N*，并且必须在范围 [3, *N*–1] 内。奇偶校验矩阵的最后 *M* 列在 GF(2) 中必须可逆。

要详细了解支持的奇偶校验矩阵，请参阅奇偶校验矩阵。

### **Block size** — 块大小 `56`（默认）| [2, 512] 范围内的整数

指定块大小。块大小必须是 [2, 512] 范围内的整数。

## 所属库

Wireless HDL Toolbox / Error Detection and Correction

## 模块特性

未在 R2025b 中记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® 加速模式和快速加速模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动已有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要插入生成代码中的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要插入生成代码中的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

不能在 Resettable Synchronous Subsystem (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2023a 中引入**

### R2025a：支持向量输入

LDPC Encoder 模块现在支持列向量作为输入。

## 描述

使用准循环低密度奇偶校验码对数据进行编码

LDPC Encoder 模块实现一个带有硬件友好控制信号的准循环低密度奇偶校验
(QC-LDPC) 编码器。该模块接受数据位和控制信号流，并输出编码位、控制信号流以及一个指示该模块是否准备好接受新输入的信号。

该模块支持具有指定奇偶校验矩阵和块大小的标量输入和向量输入。该模块还支持下三角或上三角、双对角以及混合对角奇偶校验矩阵。该模块支持循环权重为 1 的 LDPC 码。
更多信息，请参阅奇偶校验矩阵。

您可以使用此模块开发使用 QC-LDPC 进行前向纠错 (FEC) 编码的基于标准或通用发射机。该模块提供适合 HDL 代码生成和硬件部署的架构。请参阅算法。
