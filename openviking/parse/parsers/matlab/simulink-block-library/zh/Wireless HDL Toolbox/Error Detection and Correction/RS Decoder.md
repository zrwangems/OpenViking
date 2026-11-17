---
type: simulink-block
title: 'RS Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'rsdecoder'
documentation_source_path: 'ref/rsdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# RS Decoder

## 端口
```yaml
ports:
- name: data
  summary: 输入码字数据 标量
  direction: input
  data_types: double | single | uint8 | uint16 | fixed point
- name: ctrl
  summary: 伴随样本流的控制信号 samplecontrol 总线
  direction: input
  data_types: bus
- name: erasure
  summary: 擦除位置 标量
  direction: input
  data_types: Boolean
- name: data
  summary: 解码后的消息数据 标量
  direction: output
  data_types: double | single | uint8 | uint16 | fixed point
- name: ctrl
  summary: 伴随样本流的控制信号 samplecontrol 总线
  direction: output
  data_types: bus
- name: err
  summary: 接收数据损坏指示 标量
  direction: output
  data_types: Boolean
- name: nextFrame
  summary: 模块就绪指示 标量
  direction: output
  data_types: Boolean
- name: numErrors
  summary: 已纠正错误数量 非负标量
  direction: output
  data_types: uint8
```

### 输入

### **data** — 输入码字数据 标量

输入码字数据，指定为表示一个符号的标量。

由 **Codeword length (N)** 参数指定的以符号为单位的码字长度必须是一个整数，等于 2*M* – 1，其中 *M* 是范围从 3 到 16 的整数。

输入数据字长必须是一个无符号整数，等于 `ceil`(log2(**Codeword length (N)**))。对于码字长度 `7`，输入数据字长必须为 3。

`double` 和 `single` 数据类型允许用于仿真，但不允许用于 HDL 代码生成。

**数据类型：** `double` | `single` | `uint8` | `uint16` | `fixed point`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

- `start` — 指示输入帧的开始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **erasure** — 擦除位置 标量

*自 R2024b 起*

擦除位置，指定为 `Boolean` 标量。

当 erasure 为 `1` 时，表示码字中该符号被擦除的位置。当 erasure 为 `0` 时，表示没有擦除的位置。

#### 依赖关系

要启用此端口，请选择 **Enable erasure input port** 参数。

**数据类型：** `Boolean`
### 输出

### **data** — 解码后的消息数据 标量

解码后的消息数据，以标量形式返回。此输出数据宽度与输入数据宽度相同。

**数据类型：** `double` | `single` | `uint8` | `uint16` | `fixed point`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，以 `samplecontrol` 总线形式返回。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

- `start` — 指示输出帧的开始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **err** — 接收数据损坏指示 标量

接收数据损坏的指示，以标量形式返回。

当此值为 `1`（`true`）时，输出包含错误。当此值为 `0`（`false`）时，输出包含零个错误。

如果输入码字中的错误数量大于 (**Codeword length (N)** – **Message length (K)**)/2，则该模块输出数据而不纠正错误，并将 **err** 端口设置为 `1`（`true`），以指示输入码字中存在无法纠正的错误。

**数据类型：** `Boolean`

### **nextFrame** — 模块就绪指示 标量

模块就绪指示，以标量形式返回。

当模块准备好接受下一帧的开始时，模块将此信号设置为 `1`（`true`）。如果模块在 **nextFrame** 为 `0`（`false`）时接收到输入 **ctrl.start** 信号，则模块丢弃正在进行的帧并开始处理新数据。

**数据类型：** `Boolean`

### **numErrors** — 已纠正错误数量 非负标量

已纠正错误数量，以非负标量形式返回。

RS 码可以纠正的最大错误数量等于 (**Codeword length (N)** – **Message length (K)**)/2。如果输入码字中的错误数量大于 (**Codeword length (N)** – **Message length (K)**)/2，则该模块输出数据而不纠正错误，并将 **numErrors** 端口设置为 `0`，以指示这些错误中没有一个可以被纠正。

#### 依赖项

要启用此端口，请选择 **Output number of corrected symbol errors** 参数。

**数据类型：** `uint8`
## 参数
```yaml
parameters:
- name: Codeword length (N)
  summary: 码字长度 7（默认）| 范围从 7 到 65,535
  group: ''
- name: Message length (K)
  summary: 消息长度 3（默认）| 范围从 3 到（Codeword length (N) – 2）的整数
  group: ''
- name: Source of primitive polynomial
  summary: 本原多项式来源 Auto（默认）| Property
  group: ''
- name: Primitive polynomial
  summary: 本原多项式 [1 0 1 1]（默认）| 二进制行向量
  group: ''
- name: Source of B, the starting power for roots of the primitive polynomial
  summary: 本原多项式根的起始幂次来源 Auto（默认）| Property
  group: ''
- name: B value
  summary: 根的起始幂次 1（默认）| 正整数
  group: ''
- name: Output number of corrected symbol errors
  summary: 已纠正符号错误数 off（默认）| on
  group: ''
- name: Enable erasure input port
  summary: 启用擦除输入端口 off（默认）| on
  group: ''
```

### **Codeword length (N)** — 码字长度 `7`（默认）| 范围从 7 到 65,535

指定码字长度。

码字长度 `N` 必须是一个等于 2*M* – 1 的整数，其中 *M* 是范围从 3 到 16 的整数。有关为 RS 码表示数据的详细信息，请参阅 Integer Format (Reed-Solomon Only)。

### **Message length (K)** — 消息长度 `3`（默认）| 范围从 3 到（**Codeword length (N)** – `2`）的整数

指定消息长度。

有关为 RS 码表示数据的详细信息，请参阅 Integer Format (Reed-Solomon Only)。

### **Source of primitive polynomial** — 本原多项式来源 `Auto`（默认）| `Property`

指定本原多项式的来源。

- 选择 `Auto`，根据 **Codeword length (N)** 参数值指定本原多项式。本原多项式的次数计算为 *M* = `ceil`(log2(**Codeword length (N)**))。
- 选择 `Property`，使用 **Primitive polynomial** 参数指定本原多项式。

### **Primitive polynomial** — 本原多项式 `[1 0 1 1]`（默认）| 二进制行向量

指定一个二进制行向量，按幂次降序表示本原多项式。

有关如何指定本原多项式的详细信息，请参阅 Primitive Polynomials and Element Representations。

#### 依赖项

要启用此参数，请将 **Source of primitive polynomial** 参数设置为 `Property`。

### **Source of B, the starting power for roots of the primitive polynomial** — 本原多项式根的起始幂次来源 `Auto`（默认）| `Property`

指定本原多项式根的起始幂次的来源。

- 选择 `Auto`，使用默认的 **B value** 参数值 `1`。
- 选择 `Property` 以启用 **B value** 参数。

### **B value** — 根的起始幂次 `1`（默认）| 正整数

指定本原多项式根的起始幂次。

#### 依赖项

要启用此参数，请将 **Source of B, the starting power for roots of the primitive polynomial** 参数设置为 `Property`。

### **Output number of corrected symbol errors** — 已纠正符号错误数 `off`（默认）| `on`

选择此参数以启用 **numErrors** 输出端口。此端口输出已纠正错误的数量。

### **Enable erasure input port** — 启用擦除输入端口 `off`（默认）| `on`

*自 R2024b 起*

选择此参数以启用 **erasure** 输入端口。
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

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

无法为可复位同步子系统 (HDL Coder) 内的此模块生成 HDL。

## 版本历史

**在 R2020a 中引入**

### R2024b：通过输入端口启用擦除

RS Decoder 模块现在提供了一个新参数，可用于通过输入端口启用擦除。要启用该端口，请选择 **Enable erasure input port** 参数。

## 描述

从 RS 码字解码并恢复消息

RS Decoder 模块从 Reed-Solomon (RS) 码字中解码并恢复消息。该模块接受码字数据和 `samplecontrol` 总线以及（可选）擦除信息，并输出解码后的消息数据、`samplecontrol` 总线、接收数据是否损坏、模块就绪指示以及（可选）已纠正错误的数量。该模块提供适用于 HDL 代码生成和硬件部署的架构，并支持缩短的消息长度。

由于该模块的延迟会变化，该模块提供输出端口 **nextFrame**，用于指示模块何时准备好接受新的输入码字数据。有关延迟的更多详细信息，请参阅算法部分。

您可以使用此模块对许多通信系统前向纠错 (FEC) 码进行建模。该模块支持数字用户线路 (DSL)、WiMAX（802.16 m 和 e）、数字视频广播手持 (DVB-H) 终端、数字视频广播卫星 (DVB-S) 服务，以及低于 3 MHz 的数字视频广播卫星手持服务 (DVB-SH) 设备。
