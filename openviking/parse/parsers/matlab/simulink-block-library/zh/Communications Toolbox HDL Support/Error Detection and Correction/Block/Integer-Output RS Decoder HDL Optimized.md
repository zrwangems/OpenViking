---
type: simulink-block
title: 'Integer-Output RS Decoder HDL Optimized'
family: 'communications-toolbox-hdl-support'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Block'
documentation_page: 'integeroutputrsdecoderhdloptimized'
documentation_source_path: '../comm/ref/integeroutputrsdecoderhdloptimized.html'
language: zh-CN
chinese_source: worker-translation
---

# Integer-Output RS Decoder HDL Optimized

## 端口
```yaml
ports:
- name: dataIn
  summary: 输入数据 标量
  direction: input
  data_types: double | uint8 | uint16 | uint32 | uint64 | fixed point
- name: startIn
  summary: 输入帧起始指示 标量
  direction: input
  data_types: Boolean
- name: endIn
  summary: 输入帧结束指示 标量
  direction: input
  data_types: Boolean
- name: validIn
  summary: 有效输入数据指示 标量
  direction: input
  data_types: Boolean
- name: dataOut
  summary: 解码后的消息数据 标量
  direction: output
  data_types: double | uint8 | uint16 | uint32 | uint64 | fixed point
- name: startOut
  summary: 输出帧起始指示 标量
  direction: output
  data_types: Boolean
- name: endOut
  summary: 输出帧结束指示 标量
  direction: output
  data_types: Boolean
- name: validOut
  summary: 有效输出数据指示 标量
  direction: output
  data_types: Boolean
- name: errOut
  summary: 接收数据损坏指示 标量
  direction: output
  data_types: Boolean
- name: numErrors
  summary: 已纠正错误数量 非负标量
  direction: output
  data_types: uint8
```

### 输入

### **dataIn** — 输入数据 标量

输入数据，指定为表示一个符号的标量。对于二进制小数点定标，输入数据类型必须为无符号整数或无符号定点数。`double` 数据类型允许用于仿真，但不允许用于 HDL 代码生成。

**数据类型：** `double` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **startIn** — 输入帧起始指示 标量

输入帧起始指示，指定为布尔标量。

**数据类型：** `Boolean`

### **endIn** — 输入帧结束指示 标量

输入帧结束指示，指定为布尔标量。

**数据类型：** `Boolean`

### **validIn** — 有效输入数据指示 标量

有效输入数据指示，指定为布尔标量。

这是一个控制信号，用于指示 **dataIn** 端口上的数据是否有效。

**数据类型：** `Boolean`
### 输出

### **dataOut** — 解码后的消息数据 标量

解码后的消息数据，以标量形式返回。此输出数据位宽与输入数据位宽相同。

**数据类型：** `double` | `uint8` | `uint16` | `uint32` | `uint64` | `fixed point`

### **startOut** — 输出帧起始指示 标量

输出帧起始指示，以布尔标量形式返回。

**数据类型：** `Boolean`

### **endOut** — 输出帧结束指示 标量

输出帧结束指示，以布尔标量形式返回。

**数据类型：** `Boolean`

### **validOut** — 有效输出数据指示 标量

有效输出数据指示，以布尔标量形式返回。

这是一个控制信号，用于指示 **dataOut** 端口上的数据是否有效。

**数据类型：** `Boolean`

### **errOut** — 接收数据损坏指示 标量

接收数据损坏指示，以布尔标量形式返回。

当此值为 `1`（`true`）时，输出包含至少一个错误。当此值为 `0`（`false`）时，输出包含零个错误。

如果输入码字中的错误数量大于（**Codeword length** – **Message length**）/`2`，则该模块输出数据时不纠正错误，并将 **errOut** 端口设置为 `1`（`true`），以指示输入码字中存在无法纠正的错误。

**数据类型：** `Boolean`

### **numErrors** — 已纠正错误数量 非负标量

已纠正错误数量，以非负标量形式返回。

RS 码可纠正的最大错误数量等于（**Codeword length** – **Message length**）/2。如果输入码字中的错误数量大于（**Codeword length** – **Message length**）/2，则该模块输出数据时不纠正错误，并将 **numErrors** 端口设置为 `0`，以指示这些错误均无法纠正。

#### 依赖关系

要启用此端口，请选中 **Output number of corrected symbol errors** 参数。

**数据类型：** `uint8`
## 参数
```yaml
parameters:
- name: Codeword length
  summary: 码字长度 7（默认）| 范围从 7 到 65,535
  group: ''
- name: Message length
  summary: 消息长度 3（默认）| 正整数
  group: ''
- name: Source of primitive polynomial
  summary: 本原多项式来源 Auto（默认）| Property
  group: ''
- name: Primitive polynomial
  summary: 本原多项式 [ 1 0 1 1 ]（默认）| 二进制行向量
  group: ''
- name: Source of B, the starting power for roots of the primitive polynomial
  summary: 本原多项式根的起始幂来源 Auto（默认）| Property
  group: ''
- name: B value
  summary: 根的起始指数 1（默认）| 正整数
  group: ''
- name: Output number of corrected symbol errors
  summary: 已纠正符号错误数量 off（默认）| on
  group: ''
```

### **Codeword length** — 码字长度 `7`（默认）| 范围从 7 到 65,535

指定码字长度。

码字长度 `N` 必须为等于 2*M* – 1 的整数，其中 *M* 为范围从 3 到 16 的整数。有关表示 RS 码数据的详细信息，请参阅 Integer Format (Reed-Solomon Only)。

### **Message length** — 消息长度 `3`（默认）| 正整数

指定消息长度。

有关表示 RS 码数据的详细信息，请参阅 Integer Format (Reed-Solomon Only)。

### **Source of primitive polynomial** — 本原多项式来源 `Auto`（默认）| `Property`

指定本原多项式的来源。

- 选择 `Auto`，根据 **Codeword length** 参数值指定本原多项式。本原多项式的阶数计算为 *M* = `ceil`(log2(**Codeword length**)。
- 选择 `Property`，使用 **Primitive polynomial** 参数指定本原多项式。

### **Primitive polynomial** — 本原多项式 `[ 1 0 1 1 ]`（默认）| 二进制行向量

指定一个二进制行向量，按幂次降序表示本原多项式。

有关如何指定本原多项式的详细信息，请参阅 Primitive Polynomials and Element Representations。

#### 依赖关系

要启用此参数，请将 **Source of primitive polynomial** 参数设置为 `Property`。

### **Source of B, the starting power for roots of the primitive polynomial** — 本原多项式根的起始幂来源 `Auto`（默认）| `Property`

指定本原多项式根的起始幂的来源。

- 选择 `Property` 以启用 **B value** 参数。
- 选择 `Auto`，以使用 **B value** 参数的默认值 `1`。

### **B value** — 根的起始指数 `1`（默认）| 正整数

根的起始指数。

#### 依赖关系

要启用此参数，请将 **Source of B, the starting power for roots of the primitive polynomial** 参数设置为 `Property`。

### **Output number of corrected symbol errors** — 已纠正符号错误数量 `off`（默认）| `on`

选中此参数以启用 **numErrors** 输出端口。此端口输出已纠正错误的数量。
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
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

无法在可复位同步子系统 (Resettable Synchronous Subsystem) (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2012b 中引入**

### R2023b：添加了资源和性能数据综合结果

添加了一个新章节，包含 Integer-Output RS Decoder HDL Optimized 模块的资源和性能数据综合结果。

## 描述

使用 Reed-Solomon (RS) 解码器解码数据

Integer-Output RS Decoder HDL Optimized 模块使用 RS 解码器解码数据。RS 解码遵循与任何其他循环冗余码相同的标准。使用此模块对通信系统前向纠错 (FEC) 码进行建模。该模块提供了适用于 HDL 代码生成和硬件部署的架构。

有关 RS 解码器的详细信息，请参阅 Integer-Output RS Decoder 模块。有关表示 RS 码数据的详细信息，请参阅 Integer Format (Reed-Solomon Only)。
