---
type: simulink-block
title: 'Turbo Encoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Convolutional'
documentation_page: 'turboencoder'
documentation_source_path: 'ref/turboencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Turbo Encoder

## 端口

### 输入

### **In** — 输入消息二进制列向量

输入消息，指定为长度为 *L* 的二进制列向量，其中 *L* 是未编码输入消息的长度。

**数据类型：** `double` | `int8` | `fi(data,0,1)`

### **IntrInd** — 交织器索引整数列向量

交织器索引，指定为整数列向量。该向量的长度必须为 *L*，其中 *L* 是二进制输入消息的长度。向量中的每个元素必须是范围 [1, *L*] 内的整数，且必须唯一。交织器索引定义了用于在编码器处置换输入比特的映射。

#### 依赖关系

要启用此端口，请将 **Source of interleaver indices** 属性设置为 `Input port`。

**数据类型：** `double`

### **OutInd** — 输出索引整数列向量

用于对完全编码数据进行比特排序和打孔的输出索引，指定为整数列向量。向量中的元素值必须相对于编码方案的完全编码数据，包括所有流的尾比特。

**可调：** 是

#### 依赖关系

要启用此端口，请将 **Source of output indices** 属性设置为 `Input port`。

**数据类型：** `double`
### 输出

### **Out** — 并行级联码字二进制列向量

并行级联码字，返回为长度为 *M* 的二进制列向量，其中 *M* 是并行级联码字中的比特数。此输出继承其数据类型自 `In` 输入。

**数据类型：** `double` | `int8` | `fi(data,0,1)`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### **Trellis structure** — 组成卷积码的网格描述 `poly2trellis(4,[13 15],13)`（默认）| 结构体

将网格指定为 MATLAB® 结构体，其中包含速率 *K* ∕ *N* 组成卷积码的网格描述。*K* 是输入比特流的数量，*N* 是输出比特流的数量。

**注意**

对于 Turbo 编码器，*K* 必须为 1。有关详细信息，请参阅 Coding Rate。

您可以使用 `poly2trellis` 函数创建网格结构，也可以手动创建。有关此结构的更多信息，请参阅 Trellis Description of a Convolutional Code 主题和 `istrellis` 函数。

网格结构包含以下字段。

### **numInputSymbols** — 编码器输入的符号数 2*K*

编码器输入的符号数，指定为等于 2*K* 的整数，其中 *K* 是输入比特流的数量。

### **numOutputSymbols** — 编码器输出的符号数 2*N*

编码器输出的符号数，指定为等于 2*N* 的整数，其中 *N* 是输出比特流的数量。

### **numStates** — 编码器中的状态数 2 的幂

编码器中的状态数，指定为 2 的幂。

### **nextStates** — 下一状态整数矩阵

所有当前状态和当前输入组合的下一状态，指定为整数矩阵。矩阵大小必须为 `numStates` × 2*K*。

### **outputs** — 输出八进制数矩阵

所有当前状态和当前输入组合的输出，指定为八进制数矩阵。矩阵大小必须为 `numStates` × 2*K*。

### **Source of interleaver indices** — 交织器索引的来源 `Property`（默认）| `Input port`

将交织器索引的来源指定为 `Property` 或 `Input port`。

- 当您将此参数设置为 `Property` 时，模块使用 **Interleaver indices** 参数来指定交织器索引。
- 当您将此参数设置为 `Input port` 时，模块使用 `IntrInd` 输入端口来指定交织器索引。

### **Interleaver indices** — 交织器索引 `(64:-1:1).'`（默认）| 整数列向量

将交织器索引指定为整数列向量。该向量的长度必须为 *L*，其中 *L* 是二进制输入消息的长度。向量中的每个元素必须是范围 [1, *L*] 内的整数，且必须唯一。交织器索引定义了用于在编码器处置换输入比特的映射。

#### 依赖关系

要启用此参数，请将 **Source of interleaver indices** 参数设置为 `Property`。

### **Source of output indices** — 输出索引的来源 `Auto` | `Property` | `Input port`

将输出索引的来源指定为 `Auto`、`Property` 或 `Input port`。

- 当您将此参数设置为 `Auto` 时，模块计算输出索引，对第二个系统流进行打孔并包括所有尾比特。
- 当您将此参数设置为 `Property` 时，模块使用您为 **Output indices** 参数指定的输出索引。
- 当您将此参数设置为 `Input port` 时，模块使用 **OutInd** 输入端口来指定输出索引。输出索引和编码输出信号的向量长度和值可以在模块的每次执行时更改。

### **Output indices** — 输出索引 `getTurboIOIndices(64,2,3)`（默认）| 整数列向量

将用于对完全编码数据进行比特排序和打孔的输出索引指定为整数列向量。编码器输出的比特数等于此参数的长度。最大长度不得超过完全编码长度 (*L*+*mLen*) × *N* × 2)，其中 *L* 是输入向量长度，*mLen* 是存储器长度，*N* 是组成编码器编码流的数量。

#### 依赖关系

要启用此参数，请将 **Source of output indices** 参数设置为 `Property`。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

要运行的仿真类型，指定为 `Interpreted execution` 或 `Code generation`。

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项需要较少的启动时间，但后续仿真的速度比 `Code generation` 选项慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 为模块生成 C 代码。除非模型更改，否则模型在后续仿真中重用 C 代码。此选项需要额外的启动时间，但后续仿真的速度比 `Interpreted execution` 选项快。

有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。

## 所属库

Communications Toolbox / Error Detection and Correction / Convolutional

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed pointa` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a 仅 ufix(1)。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011b 中引入**

## 描述

使用并行级联编码方案对二进制数据进行编码

Turbo Encoder 模块使用并行级联编码方案对二进制输入信号进行编码。此编码方案采用两个相同的卷积编码器和一个内部交织器。每个组成编码器由尾比特独立终止。有关组成编码器的更多信息，请参阅 Parallel Concatenated Convolutional Encoding Scheme。

此图标显示了启用所有端口的模块。

启用了可选端口（IntrInd 和 OutInd）的 Turbo Encoder 模块
