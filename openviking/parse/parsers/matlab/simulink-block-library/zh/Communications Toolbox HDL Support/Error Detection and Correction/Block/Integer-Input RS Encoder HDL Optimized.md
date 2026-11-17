---
type: simulink-block
title: 'Integer-Input RS Encoder HDL Optimized'
family: 'communications-toolbox-hdl-support'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Block'
documentation_page: 'integerinputrsencoderhdloptimized'
documentation_source_path: '../comm/ref/integerinputrsencoderhdloptimized.html'
language: zh-CN
chinese_source: worker-translation
---

# Integer-Input RS Encoder HDL Optimized

## 端口

### 输入

### **dataIn** — 输入数据标量

输入数据，指定为表示一个符号的标量。对于二进制点缩放，输入数据类型必须是无符号整数或无符号定点数。每个符号的字长必须等于 `ceil`(log2(**Codeword length**) + 1。`double` 数据类型允许用于仿真，但不允许用于 HDL 代码生成。

**数据类型：** `double` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **startIn** — 输入帧起始指示标量

输入帧起始指示，指定为布尔标量。

**数据类型：** `Boolean`

### **endIn** — 输入帧结束指示标量

输入帧结束指示，指定为布尔标量。

**数据类型：** `Boolean`

### **validIn** — 有效输入数据指示标量

有效输入数据指示，指定为布尔标量。

这是一个控制信号，用于指示 **dataIn** 端口上的数据是否有效。

**数据类型：** `Boolean`
### 输出

### **dataOut** — 输出数据标量

输出数据，以标量形式返回。此输出数据宽度与输入数据宽度相同。

**数据类型：** `double` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **startOut** — 输出帧起始指示标量

输出帧起始指示，以布尔标量形式返回。

**数据类型：** `Boolean`

### **endOut** — 输出帧结束指示标量

输出帧结束指示，以布尔标量形式返回。

**数据类型：** `Boolean`

### **validOut** — 有效输出数据指示标量

有效输出数据指示，以布尔标量形式返回。

这是一个控制信号，用于指示 **dataOut** 端口上的数据是否有效。

**数据类型：** `Boolean`

## 参数

### **Codeword length** — 码字长度 `7`（默认）| 范围从 7 到 65, 535

指定码字长度。

码字长度 `N` 必须是等于 2*M* – 1 的整数，其中 *M* 是范围从 3 到 16 的整数。有关表示 RS 码数据的详细信息，请参阅 Integer Format (Reed-Solomon Only)。

### **Message length** — 消息长度 `3`（默认）| 正整数

指定消息的长度。

有关表示 RS 码数据的详细信息，请参阅 Integer Format (Reed-Solomon Only)。

每个输入帧，即 **startIn** 和 **endIn** 端口值之间的有效数据样本数，必须包含多于 *N*– *K* 个符号且小于或等于 *K* 个符号。当帧中的输入数据样本数小于 *K* 时，将推断为缩短码。

### **Source of primitive polynomial** — 本原多项式来源 `Auto`（默认）| `Property`

指定本原多项式的来源。

- 选择 `Auto` 以根据 **Codeword length** 参数值指定本原多项式。本原多项式的次数计算为 *M* = `ceil`(log2(**Codeword length**)。
- 选择 `Property` 以使用 **Primitive polynomial** 参数指定本原多项式。

### **Primitive polynomial** — 本原多项式提供者 `[ 1 0 1 1 ]`（默认）| 二进制行向量

指定一个二进制行向量，按幂次降序表示本原多项式。

有关如何指定本原多项式的详细信息，请参阅 Primitive Polynomials and Element Representations。

#### 依赖关系

要启用此参数，请将 **Source of primitive polynomial** 参数设置为 `Property`。

### **Source of puncture pattern** — 打孔图案来源 `None`（默认）| `Property`

选择 `Property` 以启用 **Puncture pattern vector** 参数。

### **Puncture pattern vector** — 打孔向量 `[ones(2,1); zeros(2,1)]`（默认）| 二进制列向量

指定长度为 *N*–*K* 的列向量。在打孔向量中，值 `1` 表示数据符号原样通过。值 `0` 表示数据符号被打孔（即从数据流中移除）。

#### 依赖关系

要启用此参数，请将 **Source of puncture pattern** 参数设置为 `Property`。

### **Source of B, the starting power for roots of the primitive polynomial** — 本原多项式根的起始幂 `Auto`（默认）| `Property`

指定本原多项式根的起始幂的来源。

- 选择 `Property` 以启用 **B value** 参数。
- 选择 `Auto`，以使用 **B value** 参数的默认值 `1`。

### **B value** — 根的起始指数 `1`（默认）| 正整数

根的起始指数。

#### 依赖关系

要启用此参数，请将 **Source of B, the starting power for roots of the primitive polynomial** 参数设置为 `Property`。

## 所属库

Communications Toolbox HDL Support / Error Detection and Correction / Block

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

使用说明和限制：

- 不建议用于生产代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

无法在可复位同步子系统 (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2012b 中引入**

### R2023b：添加了资源和性能数据综合结果

添加了一个新章节，包含 Integer-Input RS Encoder HDL Optimized 模块的资源和性能数据综合结果。

## 描述

使用 Reed-Solomon (RS) 编码器对数据进行编码

Integer-Input RS Encoder HDL Optimized 模块使用 RS 编码器对数据进行编码。RS 编码遵循与任何其他循环冗余码相同的标准。使用此模块对通信系统前向纠错 (FEC) 码进行建模。该模块提供了适用于 HDL 代码生成和硬件部署的架构。

有关 RS 编码器的详细信息，请参阅 Integer-Input RS Encoder 模块。有关表示 RS 码数据的详细信息，请参阅 Integer Format (Reed-Solomon Only)。
