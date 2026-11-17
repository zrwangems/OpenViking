---
type: simulink-block
title: 'Deserializer1D'
family: 'hdlcoder'
product_id: 'hdlcoder'
product_name: 'HDL Coder'
documentation_release: R2025b
official_category: 'HDL Operations'
documentation_page: 'deserializer1d'
documentation_source_path: 'ref/deserializer1d.html'
language: zh-CN
chinese_source: worker-translation
---

# Deserializer1D

## 端口
```yaml
ports:
- name: S
  summary: 串行输入数据信号 标量
  direction: input
  data_types: single | double | half | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point
    | enumerated
- name: ValidIn
  summary: 有效输入控制信号 标量
  direction: input
  data_types: Boolean
- name: StartIn
  summary: 启动输入控制信号 标量
  direction: input
  data_types: Boolean
- name: P
  summary: 反序列化（并行）数据输出信号 标量 | 向量
  direction: output
  data_types: single | double | int8 | int16 | int32 | int64 | uint8 | uint16 | uint32 | uint64 | Boolean | fixed point |
    enumerated
- name: ValidOut
  summary: 有效输出控制信号 标量
  direction: output
  data_types: Boolean
```

### 输入

### **S** — 串行输入数据信号 标量

要反序列化的输入信号。不支持总线数据类型。

**数据类型：** `single` | `double` | `half` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **ValidIn** — 有效输入控制信号 标量

指示有效输入信号。与 Serializer1D 模块配合使用。当您选中 **ValidIn** 复选框时，此端口可用。

**数据类型：** `Boolean`

### **StartIn** — 启动输入控制信号 标量

输入控制信号指示何时开始反序列化。与 Serializer1D 模块配合使用。数据采集在 StartIn 信号的上升沿开始。

当您选中 **StartIn** 复选框时，此端口可用。

**数据类型：** `Boolean`
### 输出

### **P** — 反序列化（并行）数据输出信号 标量 | 向量

反序列化输出信号。不支持总线数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point` | `enumerated`

### **ValidOut** — 有效输出控制信号 标量

指示有效输出信号。当您选中 **ValidOut** 复选框时，此端口可用。

**数据类型：** `Boolean`
## 参数
```yaml
parameters:
- name: Ratio (Output Vector Size/Input Vector Size)
  summary: 输出向量大小与输入向量大小之比 1（默认）
  group: ''
- name: Idle Cycles
  summary: 空闲周期数 0（默认）
  group: ''
- name: Initial condition
  summary: 初始输出数据信号值 0（默认）
  group: ''
- name: StartIn
  summary: 启用 StartIn 控制端口 off（默认）| on
  group: ''
- name: ValidIn
  summary: 启用 ValidIn 控制端口 off（默认）| on
  group: ''
- name: ValidOut
  summary: 启用 ValidOut 控制端口 off（默认）| on
  group: ''
- name: Input data port dimensions (-1 for inherited)
  summary: 输入数据信号的大小 0（默认）
  group: ''
- name: Input sample time (-1 for inherited)
  summary: 输入采样时间 -1（默认）
  group: ''
- name: Input signal type
  summary: 输入信号类型 auto（默认）| real | complex
  group: ''
```

### **Ratio (Output Vector Size/Input Vector Size)** — 输出向量大小与输入向量大小之比 1（默认）

输入反序列化比率，指定为正标量

该比率是输出向量大小除以输入向量大小。该比率必须能被输入向量大小整除。

### **Idle Cycles** — 空闲周期数 0（默认）

输入添加到每个串行化输入末尾的空闲周期数。

**Idle Cycles** 的值会影响反序列化输出速率。例如，如果 **Ratio** 为 `2`，输入信号为 `A, B, B, C, D, D, ...`，在没有空闲周期时，输出为 `AB, BC, DD...`。然而，对于相同的输入和比率，当 **Idle Cycles** 设置为 `1` 时，输出为 `AB, CD...`。空闲周期 `B` 和 `D` 被丢弃。

如果 **Idle Cycles** 不为零，并且 **ValidIn** 或 **StartIn** 开启，Deserializer1D 的行为会发生变化。空闲周期值仅影响输出速率，而 **ValidIn** 和 **StartIn** 控制哪些输入数据被反序列化。

### **Initial condition** — 初始输出数据信号值 0（默认）

指定仿真的初始输出。

### **StartIn** — 启用 StartIn 控制端口 off（默认）| on

选择以激活 StartIn 端口。

### **ValidIn** — 启用 ValidIn 控制端口 off（默认）| on

选择以激活 ValidIn 端口。

### **ValidOut** — 启用 ValidOut 控制端口 off（默认）| on

选择以激活 ValidOut 端口。

### **Input data port dimensions (-1 for inherited)** — 输入数据信号的大小 0（默认）

输入输入数据信号的大小。输入大小必须能被比率加上空闲周期数整除。默认情况下，模块根据模型中的上下文继承大小。

### **Input sample time (-1 for inherited)** — 输入采样时间 -1（默认）

输入采样时间命中之间的时间间隔，或指定其他适当的采样时间，例如连续。默认情况下，模块根据模型中的上下文继承其采样时间。有关更多信息，请参阅采样时间。

### **Input signal type** — 输入信号类型 auto（默认）| real | complex

将模块的输入信号类型指定为 `auto`、`real` 或 `complex`。
## 所属库

HDL Coder / HDL Operations

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

**注意**

为了使仿真结果与生成的 HDL 代码匹配，请在配置参数对话框的求解器窗格中，清除 **Treat each discrete rate as a separate task** 复选框。清除该复选框后，将启用单任务模式。如果在选中该复选框的情况下对模块进行仿真，输出数据可能会在同一周期更新，但在生成的 HDL 代码中，输出数据会延迟一个周期更新。

此模块有一个默认 HDL 架构。

**HDL 模块属性**

| 通用 | |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出端放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline。 |

## 版本历史

**在 R2014b 中引入**

### R2024a：半精度和布尔数据支持

该模块现在支持使用 `Half` 或 `Boolean` 类型的输入数据进行 HDL 代码生成。

## 描述

将标量流或较小向量转换为向量信号

Deserializer1D 模块将较快的标量流或向量信号缓冲为较大的、较慢的向量信号。根据 **Ratio** 和 **Idle Cycle** 的值，较快的输入信号被转换为较慢的信号，该转换会改变采样时间。此外，输出信号会延迟一个慢信号周期，因为串行化数据需要先被采集，然后才能作为向量输出。更多细节请参见以下示例。

您可以将反序列化配置为依赖于有效输入信号 ValidIn 和启动信号 StartIn。如果 **ValidIn** 和 **StartIn** 模块参数均被选中，则仅当 ValidIn 和 StartIn 信号均为 true 时才开始数据采集。请考虑以下示例：

时序图展示了 Output 随 ValidIn、StartIn 和 Input 信号变化而发生的变化。

- **Ratio** 为 `2`，**Idle Cycles** 为 `0`，因此每个输出周期长度为两个输入信号，且所有数据点均被考虑。
- **ValidIn** 和 **StartIn** 被选中，因此仅当 StartIn 和 ValidIn 信号均为 true 时才能开始数据采集。
- **ValidOut** 被选中。

在第一个周期中，ValidIn 和 StartIn 为 true，因此开始采集 A 和 B 的数据。该模块在下一个有效周期输出反序列化后的向量，因此 AB 向量在下一个周期输出。第二个周期中 C 和 D 的情况也是如此。

在第三个周期中，从 E 开始，StartIn 为 true，但 ValidIn 不为 true。E 被丢弃。在 F 处，ValidIn 为 true，但 StartIn 不为 true，因此 F 也被丢弃。由于无法采集 E 或 F 的数据，Deserializer1D 输出前一个周期的向量 CD，但 ValidOut 变为 false。

另一个需要考虑的场景是 StartIn 信号到达过早。如果两个 StartIn 信号之间的长度不足以采集完整的 ratio 周期，则不足的信号数据会被丢弃。请考虑以下示例：

时序图展示了 Output 随 ValidIn、StartIn 和 Input 信号变化而发生的变化。

- **Ratio** 为 `3`，因此每个周期长度为两个区段。
- **Idle Cycles** 为 `0`，因此所有数据输入均被考虑。
- **ValidIn** 和 **StartIn** 被选中，因此仅当 StartIn 和 ValidIn 信号均为 true 时才能开始数据采集。
- **ValidOut** 被选中。

在第一个周期中，ValidIn 和 StartIn 为 true，因此可以开始采集 A 和 B 的数据。然而，在 C 处，在能够采集三个信号之前，另一个 StartIn 信号到达。由于 StartIn 到达过早，A 和 B 被丢弃，并且在第一个周期内没有采集到有效向量。因此，第二个周期的输出仍然为零。反序列化从 C 处的 StartIn 开始，针对 C、D 和 E 进行。该向量在下一个有效周期输出，即周期 3。类似地，反序列化在 F 处的 StartIn 再次开始，并在第四个周期输出 FGH 向量。

您可以通过 **Initial condition** 参数的值指定第一个采样周期的模块输出。
