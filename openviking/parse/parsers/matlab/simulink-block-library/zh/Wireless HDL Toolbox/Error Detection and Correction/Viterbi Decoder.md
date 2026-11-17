---
type: simulink-block
title: 'Viterbi Decoder'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction'
documentation_page: 'viterbidecoder'
documentation_source_path: 'ref/viterbidecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Viterbi Decoder

## 端口
```yaml
ports:
- name: data
  summary: 输入样本列向量
  direction: input
  data_types: int8 | int16 | uint8 | uint16 | Boolean | fixdt(0,1,0) | fixdt(S,WL,0) | single | double
- name: valid
  summary: 输入样本的有效性 标量
  direction: input
  data_types: Boolean
- name: erasure
  summary: 中性符号位置 列向量
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
- name: data
  summary: 输出样本 标量
  direction: output
  data_types: int8 | int16 | uint8 | uint16 | Boolean | fixdt(0,1,0) | fixdt(S,WL,0) | single | double
- name: valid
  summary: 输出样本的有效性 标量
  direction: output
  data_types: Boolean
- name: ctrl
  summary: 伴随样本流的控制信号 samplecontrol 总线
  direction: output
  data_types: bus
```

### 输入

### **data** — 输入样本列向量

输入样本，指定为 *n*×1 列向量，其中 *n* 是生成多项式的长度。当输入数据类型为定点或整数时，该模块执行软判决解码；当输入数据类型为 `Boolean` 或 `fixdt(0,1,0)` 时，该模块执行硬判决解码。对于 `single` 和 `double` 数据类型，该模块执行非量化软判决解码，但这些数据类型不支持 HDL 代码生成。

对于软判决输入样本，该模块支持高达 16 位的字长。对于 HDL 代码生成，由于硬件资源使用的原因，不建议使用超过 8 位的字长。输入数据的小数长度必须为 0。

**数据类型：** `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixdt(0,1,0)` | `fixdt(S,WL,0)` | `single` | `double`

### **valid** — 输入样本的有效性 标量

控制信号，指示来自 **data** 输入端的样本何时有效。当 **valid** 输入端为 `1`（`true`）时，该模块捕获 **data** 输入端的值。当 **valid** 输入端为 `0`（`false`）时，该模块忽略输入样本。

#### 依赖关系

要启用此端口，请将 **Operation mode** 设置为 `Continuous`。

**数据类型：** `Boolean`

### **erasure** — 中性符号位置 列向量

中性符号位置，指定为与输入 **data** 向量大小相同的二进制值列向量。当 **erasure** 元素为 `1`（`true`）时，对应的输入 **data** 元素为去穿刺中性值，解码器不更新分支度量。当 **erasure** 元素为 `0`（`false`）时，该模块使用对应的输入 **data** 元素更新分支度量。您可以使用 Depuncturer 模块来驱动此端口。

#### 依赖关系

要启用此端口，请选择 **Enable erasure input port**。

**数据类型：** `Boolean`

### **reset** — 清除内部状态 标量

清除内部状态，指定为 `Boolean` 标量。当 **reset** 为 `1`（`true`）时，经过一个周期后，该模块停止当前计算并清除内部支路和状态度量。

#### 依赖关系

要启用此端口，请将 **Operation mode** 设置为 `Continuous` 并选择 **Enable reset input port**。

**数据类型：** `Boolean`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和输入样本的有效性。

#### 依赖关系

要启用此端口，请将 **Operation mode** 设置为 `Terminated` 或 `Truncated`。

**数据类型：** `bus`
### 输出

### **data** — 输出样本 标量

输出样本，返回为与输入样本具有相同数据类型的标量。

**数据类型：** `int8` | `int16` | `uint8` | `uint16` | `Boolean` | `fixdt(0,1,0)` | `fixdt(S,WL,0)` | `single` | `double`

### **valid** — 输出样本的有效性 标量

控制信号，指示来自 **data** 输出端的样本何时有效。当输出 **data** 端存在有效样本时，该模块将 **valid** 端口设置为 `1`（`true`）。

#### 依赖关系

要启用此端口，请将 **Operation mode** 设置为 `Continuous`。

**数据类型：** `Boolean`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，返回为 `samplecontrol` 总线。该总线包括 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

#### 依赖关系

要启用此端口，请将 **Operation mode** 设置为 `Terminated` 或 `Truncated`。

**数据类型：** `bus`
## 参数
```yaml
parameters:
- name: Constraint length
  summary: 网格约束长度 7（默认）| [3, 9] 范围内的整数
  group: ''
- name: Code generator
  summary: 码生成多项式 [171, 133]（默认）| 八进制值向量
  group: ''
- name: Enable erasure input port
  summary: 使用可选 erasure 信号 off（默认）| on
  group: ''
- name: Traceback depth
  summary: 网格分支数 32（默认）| [3, 256] 范围内的整数
  group: ''
- name: Operation mode
  summary: 帧结束行为 Continuous（默认）| Truncated | Terminated
  group: ''
- name: Enable reset input port
  summary: 使用可选 reset 信号 off（默认）| on
  group: ''
```

### **Constraint length** — 网格约束长度 `7`（默认）| [3, 9] 范围内的整数

网格约束长度，指定为 [3, 9] 范围内的整数。

### **Code generator** — 码生成多项式 `[171, 133]`（默认）| 八进制值向量

码生成多项式，指定为 1×*n* 的八进制值向量，其中 *n* 是多项式的长度。该模块接受长度为 2 到 7 个元素的多项式。

该模块不支持带反馈连接的码。

### **Enable erasure input port** — 使用可选 erasure 信号 `off`（默认）| `on`

选择此参数以启用 **erasure** 端口。

### **Traceback depth** — 网格分支数 `32`（默认）| [3, 256] 范围内的整数

用于构造每条回溯路径的网格分支数，指定为整数。该模块支持 [3, 256] 范围内的回溯深度。对于非穿刺样本，建议深度为 5×**constraintLength**。对于穿刺样本，建议深度为 10×**constraintLength**。这些值在解码精度和所用内存量之间取得平衡。

对于 HDL 代码生成，由于硬件资源使用的原因，不建议使用超过 128 的回溯深度。

### **Operation mode** — 帧结束行为 `Continuous`（默认）| `Truncated` | `Terminated`

帧结束行为，指定为以下模式之一：

- `Continuous` – 该模块不清除内部状态度量。输入 **valid** 信号限定输入样本。
- `Truncated` – 该模块在每帧后重置状态度量，回溯路径从具有最佳度量的状态开始，并在全零状态结束。输入 **ctrl** 总线限定输入样本并标记帧边界。

  **注意**

  此模式要求帧之间至少有 **Constraint length**–1 个周期的间隔。
- `Terminated` – 该模块在每帧后重置状态度量，回溯路径始终从全零状态开始并在全零状态结束。输入 **ctrl** 总线限定输入样本并标记帧边界。

### **Enable reset input port** — 使用可选 reset 信号 `off`（默认）| `on`

选择此参数以启用 **reset** 端口。当 **reset** 为 `1`（`true`）时，经过一个周期后，该模块停止当前计算并清除内部支路和状态度量。

#### 依赖关系

要启用此参数，请将 **Operation mode** 设置为 `Continuous`。
## 所属库

Wireless HDL Toolbox / Error Detection and Correction

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

该模块支持用于 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

该模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

无法在可复位同步子系统 (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2018b 中引入**

## 描述

使用 Viterbi 算法解码卷积编码数据

Viterbi Decoder 模块使用基于 RAM 的回溯实现来解码卷积编码数据。Viterbi 解码广泛用于 LTE 标准 TS 36.212 [1] 以及其他前向纠错 (FEC) 应用，例如无线网络 (802.11a/b/g/n/ac)、数字卫星通信、数字视频广播 (DVB)、IEEE 802.16 和 HiperLAN。为了支持这些标准中的任何一种，该模块接受约束长度为 3 到 9、码率为 1/2 到 1/7 的卷积码，并提供连续、终止和截断模式。该模块提供适合 HDL 代码生成的架构和接口。

该模块通过提供可选的 **erasure** 输入端口来支持穿刺码的解码。您可以使用 Depuncturer 模块在穿刺样本流中插入中性值，并生成 **erasure** 信号。

Viterbi Decoder 模块接受硬判决二进制值或软判决对数似然比 (LLR) 形式的输入样本。每个样本是一个列向量，其长度取决于编码方案。第一个波形显示了使用默认模块参数的连续操作模式，输入样本为有符号 4 位数据。**Traceback depth** 为 `32`。该模块在 148 个时钟周期后返回第一个解码输出数据样本。解码延迟为 4×**Traceback depth** + **Constraint length** + 13 个有效输入周期。

连续操作模式的 Logic Analyzer 波形

第二个波形显示了终止操作模式下的三个帧。输入为无符号 4 位样本，该模块使用网格 (7,[171 133 112])。**Traceback depth** 为 `32`。输入和输出 **ctrl** 总线被展开以显示其三个控制信号。从每个输入 **ctrl**.`start` 到输出 **ctrl**.`start` 的延迟也是 148 个时钟周期。

总线中的控制信号指示每个样本的有效性和帧的边界。要将矩阵转换为样本流和相应的控制信号，请使用 Frame To Samples 模块或 `whdlFramesToSamples` 函数。有关流式样本接口的完整描述，请参阅 Streaming Sample Interface。

终止操作模式的 Logic Analyzer 波形
