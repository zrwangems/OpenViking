---
type: simulink-block
title: 'NR Polar Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'nrpolardecoder'
documentation_source_path: 'ref/nrpolardecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# NR Polar Decoder

## 端口
```yaml
ports:
- name: data
  summary: 输入样本标量
  direction: input
  data_types: fixed point | int8 | int16 | double | single
- name: ctrl
  summary: 伴随样本流的控制信号 samplecontrol 总线
  direction: input
  data_types: bus
- name: K
  summary: 信息块长度（以位为单位） 正整数
  direction: input
  data_types: fixdt(0,10,0)
- name: E
  summary: 速率匹配输出长度（以位为单位） 标量正整数
  direction: input
  data_types: fixdt(0,14,0)
- name: RNTI
  summary: 目标 RNTI 16 位无符号整数
  direction: input
  data_types: uint16
- name: data
  summary: 解码数据位 标量
  direction: output
  data_types: fixdt(0,1,0) | Boolean | double | single
- name: ctrl
  summary: 伴随样本流的控制信号 samplecontrol 总线
  direction: output
  data_types: bus
- name: err
  summary: CRC 结果 标量
  direction: output
  data_types: Boolean | ufix11 | ufix24
- name: nextFrame
  summary: 准备好接收新输入标量
  direction: output
  data_types: Boolean
```

### 输入

### **data** — 输入样本标量

输入样本，指定为标量对数似然比（LLR）。该模块支持内置类型，以及字长为 4 到 16 位的有符号定点值。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

**数据类型：** `fixed point` | `int8` | `int16` | `double` | `single`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

- `start` — 指示输入帧的起始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **K** — 信息块长度（以位为单位） 正整数

信息块长度（以位为单位），指定为正整数。对于下行链路消息，**K** 必须在 36 到 164 的范围内。对于上行链路消息，**K** 必须在 18 到 25 或 31 到 1023 的范围内。

#### 依赖关系

要启用此端口，请将 **Configuration source** 参数设置为 `Input port`。

**数据类型：** `fixdt(0,10,0)`

### **E** — 速率匹配输出长度（以位为单位） 标量正整数

速率匹配输出长度（以位为单位），指定为标量正整数。为 **E** 指定一个大于 **K** 且小于或等于 8192 的值。

#### 依赖关系

要启用此端口，请将 **Configuration source** 参数设置为 `Input port`。

**数据类型：** `fixdt(0,14,0)`

### **RNTI** — 目标 RNTI 16 位无符号整数

目标 RNTI，指定为 16 位无符号整数。该值可提高 DCI 消息的解码精度。例如，在解码 SIB1 DCI 消息时，启用此端口并将目标 RNTI 设置为 65,535。对于 MIB 解码，您可以禁用此端口或将目标 RNTI 设置为 0。

#### 依赖关系

要启用此端口，请将 **Link direction** 设置为 `Downlink` 并选中 **Enable target RNTI port** 参数。

**数据类型：** `uint16`
### 输出

### **data** — 解码数据位 标量

解码数据位，以标量形式返回。输出消息长度为 *A* 位，其中 `A = K – CRCLen`。对于下行链路消息，*CRCLen* 为 24。对于上行链路消息，*CRCLen* 为 11 或 6，如 5G NR 标准所定义。

**数据类型：** `fixdt(0,1,0)` | `Boolean` | `double` | `single`
**复数支持：** 是

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，以 `samplecontrol` 总线形式返回。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

- `start` — 指示输出帧的起始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **err** — CRC 结果 标量

CRC 结果，以标量形式返回。如果清除 **Full checksum mismatch** 参数，该值为布尔值。当选中 **Full checksum mismatch** 参数时，对于下行链路消息，该值为 `ufix24` 标量；对于上行链路消息，该值为 `ufix11` 或 `ufix6` 标量。

如果启用 **RNTI** 端口，该模块会将内部 CRC 校验和与目标 RNTI 值进行比较。否则，该模块会将 CRC 校验和与值 0 进行比较。

**数据类型：** `Boolean` | `ufix11` | `ufix24`

### **nextFrame** — 准备好接收新输入标量

当模块准备好接受下一帧的开始时，模块将该信号设置为 `1`。如果模块在 **nextFrame** 为 `0` 时接收到输入 **start** 信号，模块将丢弃正在进行的帧并开始处理新数据。

有关详细信息，请参阅使用 nextFrame 输出信号。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Link direction
  summary: 5G NR 链路方向 Downlink（默认）| Uplink
  group: ''
- name: List length
  summary: 解码路径数量 2（默认）| 4 | 8
  group: ''
- name: Configuration source
  summary: K 和 E 的来源 Property（默认）| Input port
  group: ''
- name: Message length (K)
  summary: 信息块长度（以位为单位） 56（默认）| 正整数
  group: ''
- name: Rate-matched length (E)
  summary: 速率匹配输出长度（以位为单位） 864（默认）| 正整数
  group: ''
- name: Full checksum mismatch
  summary: 从最终解码阶段返回校验和 off（默认）| on
  group: ''
- name: Enable target RNTI port
  summary: 用于指定目标 RNTI 值的可选端口 off（默认）| on
  group: ''
```

### **Link direction** — 5G NR 链路方向 `Downlink`（默认）| `Uplink`

5G NR 链路方向，指定为 `Downlink` 或 `Uplink`。当您选择 `Downlink` 时，模块按照 5G NR 标准执行解交织。当您选择 `Uplink` 时，模块省略解交织逻辑。

下行解码使用 24 位的 CRC 长度。上行解码使用 6 位 CRC 长度（**K** 在 18 到 25 范围内）或 11 位（**K** 在 31 到 1023 范围内）。

### **List length** — 解码路径数量 `2`（默认）| `4` | `8`

此参数是解码树中维护的最大并行路径数。增加列表长度会提高纠错性能，但会使用更多硬件资源并增加解码延迟。当您使用列表长度 `4` 和 `8` 时，延迟可能因输入信号的信噪比而变化，对于给定的 **K** 和 **E** 值不是恒定的。使用 **nextFrame** 输出信号来确定模块何时可用于新消息。

### **Configuration source** — K 和 E 的来源 `Property`（默认）| `Input port`

选择 `Input port` 以启用 **K** 和 **E** 端口。选择 `Property` 以使用 **Message length (K)** 和 **Rate-matched length (E)** 参数。

### **Message length (K)** — 信息块长度（以位为单位） `56`（默认）| 正整数

对于下行消息，**K** 必须在 36 到 164 范围内。对于上行消息，**K** 必须在 18 到 25 或 31 到 1023 范围内。

#### 依赖关系

要启用此参数，请将 **Configuration source** 参数设置为 `Property`。

### **Rate-matched length (E)** — 速率匹配输出长度（以位为单位） `864`（默认）| 正整数

为 **E** 指定一个大于 **K** 且小于或等于 8192 的值。

#### 依赖关系

要启用此参数，请将 **Configuration source** 参数设置为 `Property`。

### **Full checksum mismatch** — 从最终解码阶段返回校验和 `off`（默认）| `on`

当您清除此参数时，模块在 **err** 端口上返回一个布尔标量，指示 CRC 是否成功。当您选择此参数时，模块在 **err** 端口上返回完整的 CRC 校验和。如果您的设计解码 DCI 消息并利用 RNTI 余数，请选择此参数。

如果您启用 **RNTI** 端口，模块将内部 CRC 校验和与目标 RNTI 值进行比较。否则，模块将 CRC 校验和与值 0 进行比较。

`nrPolarDecode`（5G Toolbox）函数返回包含 CRC 位的解码消息。此模块返回不包含 CRC 位的解码消息，并在 **err** 端口上单独返回 CRC 状态。此行为等效于在使用 `nrPolarDecode` 函数后调用 `nrCRCDecode`（5G Toolbox）函数。不重新计算 CRC 位可节省硬件延迟和资源。

### **Enable target RNTI port** — 用于指定目标 RNTI 值的可选端口 `off`（默认）| `on`

选择此参数以启用 **RNTI** 输入端口。提供目标 RNTI 值可提高 DCI 消息的解码精度。例如，在解码 SIB1 DCI 消息时，启用此端口并将目标 RNTI 设置为 65535。对于 MIB 解码，您可以禁用此端口或将目标 RNTI 设置为 0。

启用此端口还会改变模块计算 **err** 输出端口值的方式。如果您启用 **RNTI** 端口，模块将内部 CRC 校验和与目标 RNTI 值进行比较。否则，模块将 CRC 校验和与值 0 进行比较。

#### 依赖关系

要启用此参数，请将 **Link direction** 参数设置为
`Downlink`。
## 所属库

Wireless HDL Toolbox / Error Detection and Correction

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink® 加速模式和快速加速模式的 C/C++ 代码生成，以及 DPI 组件生成。

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

**在 R2020a 中引入**

## 描述

根据 5G NR 标准执行极性解码

NR Polar Decoder 模块实现具有硬件友好控制信号的流式极性解码器。
5G NR 标准使用极性码对 DCI、UCI 和 BCH 传输信道进行信道编码。

您必须指定链路方向，因为 5G NR 标准定义的编码方案在下行链路和上行链路消息中是不同的。下行链路消息使用交织进行编码，并使用 24 位的 CRC 长度。上行链路消息不使用交织，并使用 6 或 11 的 CRC 长度。

此模块实现 CRC 辅助的连续消除列表解码器。此实现与 `nrPolarDecode` (5G Toolbox) 函数的性能相匹配。您可以选择列表长度为 2、4 或 8。增加列表长度会提高纠错性能，但会使用更多硬件资源并增加解码延迟。您可以通过使用可选的 **RNTI** 端口指定预期的 RNTI 值来提高 DCI 消息的解码性能。

此模块还对消息执行 CRC 解码，等效于 `nrCRCDecode` (5G Toolbox) 函数。该模块根据您指定的链路方向和您提供的 **K** 值来选择 CRC 长度。该模块根据 **K** 和 **E** 的值检测 DCI 消息，并自动在消息前添加 1，等效于 `nrPolarDecode` (5G Toolbox) 函数的 `padCRC` 输入参数。

由于极性解码操作的延迟可能变化，该模块提供一个输出信号 **nextFrame**，用于指示模块何时准备好接受新输入。有关更多详细信息，请参阅本页面的延迟部分。
