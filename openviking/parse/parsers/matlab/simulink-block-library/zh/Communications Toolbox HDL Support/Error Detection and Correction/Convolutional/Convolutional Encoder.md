---
type: simulink-block
title: 'Convolutional Encoder'
family: 'wireless-hdl'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'convolutionalencoder'
documentation_source_path: '../wireless-hdl/ref/convolutionalencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Convolutional Encoder

## 端口
```yaml
ports:
- name: data
  summary: 输入数据位 标量
  direction: input
  data_types: Boolean | fixed point
- name: valid
  summary: 输入数据的有效性 标量
  direction: input
  data_types: Boolean
- name: reset
  summary: 清除内部状态 标量
  direction: input
  data_types: Boolean
- name: ctrl
  summary: 伴随样本流的控制信号 samplecontrol 总线
  direction: input
  data_types: bus
- name: ISt
  summary: 每个帧开始时的初始状态 标量
  direction: input
  data_types: single | double | fixed point
- name: data
  summary: 编码输出数据 列向量
  direction: output
  data_types: Boolean
- name: valid
  summary: 输出样本的有效性 标量
  direction: output
  data_types: Boolean
- name: ctrl
  summary: 伴随样本流的控制信号 samplecontrol 总线
  direction: output
  data_types: bus
- name: FSt
  summary: 每个帧结束时的最终状态 标量
  direction: output
  data_types: single | double | fixed point
```

### 输入

### **data** — 输入数据位 标量

输入数据位，指定为 `Boolean` 或 `ufix1`。

**数据类型：** `Boolean` | `fixed point`

### **valid** — 输入数据的有效性 标量

控制信号，用于指示输入数据是否有效。当该值为 `1`（true）时，模块接受 **data** 输入端口上的值。当该值为 `0`（false）时，模块忽略 **data** 输入端口上的值。

#### 依赖关系

要启用此端口，请将 **Operation mode** 参数设置为 `Continuous`。

**数据类型：** `Boolean`

### **reset** — 清除内部状态 标量

清除内部状态，指定为 `Boolean` 标量。当该值为 `1`（`true`）时，模块停止当前计算并清除所有编码器状态。

#### 依赖关系

要启用此端口，请将 **Operation mode** 参数设置为 `Continuous`，并选中 **Enable reset input port** 参数。

**数据类型：** `Boolean`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包含 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界以及输入样本的有效性。

- `start` — 指示输入帧的开始。
- `end` — 指示输入帧的结束。
- `valid` — 指示输入 **data** 端口上的数据有效。

#### 依赖关系

要启用此端口，请将 **Operation mode** 参数设置为 `Truncated` 或 `Terminated`。

**数据类型：** `bus`

### **ISt** — 每个帧开始时的初始状态 标量

模块在每个帧开始时的初始状态，指定为 `fixdt(0,constraint length -1,0)`。输入状态是模块帧开始时移位寄存器中的二进制位数，从最高有效位（MSB）读取到最低有效位（LSB）。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

#### 依赖关系

要启用此端口，请将 **Operation mode** 参数设置为 `Truncated`，并选中 **Enable initial state input port** 参数。

**数据类型：** `single` | `double` | `fixed point`
### 输出

### **data** — 编码输出数据 列向量

输出数据，如果码率为 1/n，则返回为 1×*n* 列向量。*n* 的取值范围为 2 到 7。

**数据类型：** `Boolean`

### **valid** — 输出样本的有效性 标量

控制信号，用于指示 **data** 输出端口的数据是否有效。当该值为 `1`（true）时，模块在 **data** 输出端口上返回有效数据。当 **valid** 为 `false`（`0`）时，**data** 输出端口上的值无效。

#### 依赖关系

要启用此端口，请将 **Operation mode** 参数设置为 `Continuous`。

**数据类型：** `Boolean`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，返回为 `samplecontrol` 总线。该总线包含 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界以及样本的有效性。

- `start` — 指示输出帧的开始。
- `end` — 指示输出帧的结束。
- `valid` — 指示输出 **data** 端口上的数据有效。

#### 依赖关系

要启用此端口，请将 **Operation mode** 参数设置为 `Truncated` 或 `Terminated`。

**数据类型：** `bus`

### **FSt** — 每个帧结束时的最终状态 标量

模块在每个帧结束时的最终状态，返回为 `fixdt(0,constraint length -1,0)`。最终状态是模块帧结束时移位寄存器中的二进制位数，从最高有效位（MSB）读取到最低有效位（LSB）。

模块返回与 **ISt** 相同的数据类型。

#### 依赖关系

要启用此端口，请将 **Operation mode** 参数设置为 `Truncated`，并选中 **Enable final state output port** 参数。

**数据类型：** `single` | `double` | `fixed point`
## 参数
```yaml
parameters:
- name: Constraint length
  summary: 模块的约束长度 7（默认）| [3, 9] 范围内的整数
  group: 主要
- name: Code generator
  summary: 码生成多项式 [171 133]（默认）| 八进制值向量
  group: 主要
- name: Feedback connection
  summary: 反馈连接多项式 0（默认）| 标量八进制数
  group: 主要
- name: Operation mode
  summary: 操作模式 Continuous（默认）| Terminated | Truncated
  group: 主要
- name: Enable reset input port
  summary: 复位输入信号 off（默认）| on
  group: 控制端口
- name: Enable initial state input port
  summary: 初始状态输入信号 Off（默认）| On
  group: 控制端口
- name: Enable final state output port
  summary: 最终状态输出信号 Off（默认）| On
  group: 控制端口
```

### 主要

### **Constraint length** — 模块的约束长度 `7`（默认）| [3, 9] 范围内的整数

模块的约束长度，指定为 [3, 9] 范围内的整数。

### **Code generator** — 码生成多项式 `[171 133]`（默认）| 八进制值向量

码生成多项式，指定为 1×*n* 的八进制值向量，其中 *n* 为多项式的长度，范围为 2 到 7。

### **Feedback connection** — 反馈连接多项式 `0`（默认）| 标量八进制数

反馈多项式，指定为标量八进制数。如果反馈连接为 `0`，则不启用反馈连接。

要启用反馈连接，请指定一个八进制值，其二进制表示必须是最高有效位（MSB）为 `1` 的 K 位数，其中 *K* 为 **Constraint length**。有关如何构造反馈多项式的更多信息，请参阅 Convolutional Codes。

### **Operation mode** — 操作模式 `Continuous`（默认）| `Terminated` | `Truncated`

操作模式，指定为以下模式之一：

- `Continuous` — 在此模式下，模块从全零状态开始，并在每次输入结束时保留编码器状态，以供下一次输入使用。
- `Terminated` — 在此模式下，模块独立地处理每个输入帧。模块的编码器状态在每个帧结束时通过追加位重置为全零状态。

  **注意**

  此模式要求帧之间具有最小的帧间隙，即 **Constraint length** – 1 个周期。如果未提供足够的帧间隙，模块将停止处理旧帧并开始处理新帧。
- `Truncated` — 在此模式下，模块独立地处理每个输入帧。编码器状态在每次输入开始时重置为全零状态。

### 控制端口

### **Enable reset input port** — 复位输入信号 `off`（默认）| `on`

选中此参数以启用 **reset** 端口。当 **reset** 为 `1`（`true`）时，模块在下一个时钟周期复位编码器状态。

#### 依赖关系

要启用此参数，请将 **Operation mode** 参数设置为 `Continuous`。

### **Enable initial state input port** — 初始状态输入信号 `Off`（默认）| `On`

选中此参数以启用 **ISt** 端口。

#### 依赖关系

要启用此参数，请将 **Operation mode** 参数设置为 `Truncated`。

### **Enable final state output port** — 最终状态输出信号 `Off`（默认）| `On`

选中此参数以启用 **FSt** 端口。

#### 依赖关系

要启用此参数，请将 **Operation mode** 参数设置为 `Truncated`。
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

## 版本历史

**在 R2019b 中引入**

## 描述

使用卷积编码对数据位进行编码 — 针对 HDL 代码生成进行了优化

Convolutional Encoder 模块使用卷积编码对数据位进行编码。该模块支持 1/2 到 1/7 的码率以及 3 到 9 的约束长度，包括递归和非递归多项式。该模块提供了适用于 HDL 代码生成和硬件部署的架构。

该模块以三种模式运行：带可选复位端口的连续模式、终止模式，以及带可选初始状态和最终状态端口的截断模式。在 `Continuous` 模式下，模块接受数据位以及有效信号，并输出带有有效信号的编码位。在 `Terminated` 和 `Truncated` 模式下，模块接受数据位以及 `samplecontrol` 总线，并输出带有 `samplecontrol` 总线的编码位。

该模块支持 Wi-Fi（802.11a/b/g/n/ac）、数字卫星通信、数字视频广播（DVB）、3GPP2、IEEE 802.16、HIPERLAN 等通信标准及其他技术。您可以使用此模块实现其他信道码，例如 LTE 标准中使用的 turbo 码。

此波形显示了模块在 `Terminated` 模式下的编码输出，此时模块参数 **Constraint length** 设置为 `7`，**Code generator** 设置为 `[133 171]`，**Feedback connection** 设置为 `0`。输入和输出 **ctrl** 总线被展开以显示其控制信号。

该模块的延迟为三个时钟周期，因此模块在三个时钟周期后返回第一个编码输出数据。在 `Terminated` 模式下，帧结束后，模块通过追加（**Constraint length** – 1）位将编码状态重置为全零状态。因此，该波形显示了帧结束（**ctrlIn.endIn**）与下一帧开始 **ctrlln.startIn** 之间六个（**Constraint length** – 1）时钟周期的帧间隙。
