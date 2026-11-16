---
type: simulink-block
title: 'NR Polar Encoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'nrpolarencoder'
documentation_source_path: 'ref/nrpolarencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# NR Polar Encoder

## 端口

### 输入

### **data** — 输入数据 bit 标量

输入数据 bit，指定为标量。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持用于 HDL 代码生成。

**数据类型：** `fixdt(0,1,0)` | `Boolean` | `double` | `single`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` bus

伴随样本流的控制信号，指定为 `samplecontrol` bus。该 bus 包括 `start`、`end` 和 `valid` 控制信号，这些信号指示帧的边界和样本的有效性。

- `start` — 指示输入帧的起始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **K** — 以 bits 为单位的信息块长度，正整数

以 bits 为单位的信息块长度，指定为正整数。对于下行消息，**K** 必须在 36 到 164 的范围内。对于上行消息，**K** 必须在 18 到 25 或 31 到 1023 的范围内。

#### 依赖关系

要启用此端口，请将 **Configuration source** 参数设置为 `Input port`。

**数据类型：** `fixdt(0,10,0)`

### **E** — 以 bits 为单位的速率匹配输出长度，正整数

以 bits 为单位的速率匹配输出长度，指定为正整数。为 **E** 指定一个大于 **K** 且小于或等于 8192 的值。

#### 依赖关系

要启用此端口，请将 **Configuration source** 参数设置为 `Input port`。

**数据类型：** `fixdt(0,14,0)`

### 输出

### **data** — 编码数据 bit 标量

编码数据 bit，以标量形式返回。该模块返回包含 *N* 个连续 bits 的消息。*N* 是根据 **K** 和 **E** 的值确定的 2 的幂。当 **Link direction** 为 `Downlink` 时，最大输出消息大小为 512 bits；当 **Link direction** 为 `Uplink` 时，最大输出消息大小为 1024 bits。

**数据类型：** `fixdt(0,1,0)` | `Boolean` | `double` | `single`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` bus

伴随样本流的控制信号，以 `samplecontrol` bus 形式返回。该 bus 包括 `start`、`end` 和 `valid` 控制信号，这些信号指示帧的边界和样本的有效性。

- `start` — 指示输出帧的起始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **nextFrame** — 准备好接受新输入的标量

当模块准备好接受下一帧的起始时，该模块将此信号设置为 `1`。如果模块在 **nextFrame** 为 `0` 时接收到输入 **start** 信号，则该模块丢弃正在处理的帧并开始处理新数据。

有关更多信息，请参阅 Using the nextFrame Output Signal。

**数据类型：** `Boolean`

## 参数

### **Link direction** — 5G NR 链路的方向 `Downlink`（默认值） | `Uplink`

当选择 `Downlink` 时，该模块按照 5G NR 标准的规定执行交织。当选择 `Uplink` 时，该模块省略交织逻辑。

### **Configuration source** — K 和 E 的来源 `Property`（默认值） | `Input port`

选择 `Input port` 以启用 **K** 和 **E** 端口。选择 `Property` 以使用 **Message length (K)** 和 **Rate-matched length (E)** 参数。

### **Message length (K)** — 以 bits 为单位的信息块长度 `56`（默认值） | 正整数

对于下行消息，**K** 必须在 36 到 164 的范围内。对于上行消息，**K** 必须在 18 到 25 或 31 到 1023 的范围内。

#### 依赖关系

要启用此参数，请将 **Configuration source** 参数设置为 `Property`。

### **Rate-matched length (E)** — 以 bits 为单位的速率匹配输出长度 `864`（默认值） | 正整数

为 **E** 指定一个大于 **K** 且小于或等于 8192 的值。

#### 依赖关系

要启用此参数，请将 **Configuration source** 参数设置为 `Property`。

## 所属库

Wireless HDL Toolbox / Error Detection and Correction

## 模块特性

在 R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持针对 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

不能在 Resettable Synchronous Subsystem (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2020a 中引入**

## 描述

根据 5G NR 标准执行极化编码

NR Polar Encoder 模块实现具有硬件友好控制信号的流式极化编码器。5G NR 标准要求对 DCI、UCI 和 BCH 发射信道进行信道编码时使用极化编码。

编码器实现与 `nrPolarEncode`（5G Toolbox）函数匹配。

必须指定链路方向，因为 5G NR 标准定义的编码方案对于下行和上行消息是不同的。下行消息使用交织进行编码，上行消息不使用交织。

由于此操作的延迟可能变化，该模块提供输出信号 **nextFrame**，用于指示模块何时准备好接受新输入。有关更多详细信息，请参见本页的延迟部分。
