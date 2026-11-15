---
type: simulink-block
title: 'Turbo Decoder'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'PHY Components / Error Detection and Correction / Convolutional Coding'
documentation_page: 'turbodecoder'
documentation_source_path: 'ref/turbodecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Turbo Decoder

## 端口

### 输入

### **In** — 并行级联码字列向量

并行级联码字，指定为长度为 *M* 的列向量，其中 *M* 是并行级联码字的长度。

**数据类型：** `double` | `single`

### **IntrInd** — 交织器索引整数列向量

交织器索引，指定为整数列向量。该向量的长度必须为 *L*。向量的每个元素必须是范围 [1, *L*] 内的整数，且必须唯一。*L* 是解码后的二进制输出消息 `Out` 的长度。交织器索引定义用于在解码器处置换输入位的映射。

#### 依赖关系

要启用此端口，请将 **交织器索引源** 参数设置为 `Input port`。

**数据类型：** `double`

### **InInd** — 输入索引整数列向量

用于完全编码数据的位排序和删余的输入索引，指定为整数列向量。**InInd** 向量的长度必须等于输入数据向量 **In** 的长度。向量中的元素值必须相对于编码方案的完全编码数据，包括所有流的尾位。

#### 依赖关系

要启用此端口，请将 **输入索引源** 参数设置为 `Input port`。

**数据类型：** `double`
### 输出

### **Out** — 解码消息二进制列向量

解码消息，返回为长度为 *L* 的二进制列向量，其中 *L* 是解码后的二进制输出消息的长度。此输出继承 `In` 输入的数据类型。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### **网格结构** — 分量卷积码的网格描述 `poly2trellis(4,[13 15],13)` (default) | structure

将网格指定为 MATLAB® 结构，其中包含速率 *K* ∕ *N* 分量卷积码的网格描述。*K* 是输入位流的数量，*N* 是输出位流的数量。

**注意**

对于 Turbo 编码器，*K* 必须为 1。有关详细信息，请参阅编码速率。

您可以使用 `poly2trellis` 函数创建网格结构，也可以手动创建。有关此结构的详细信息，请参阅卷积码的网格描述和 `istrellis` 函数。

网格结构包含以下字段。

### **numInputSymbols** — 输入到编码器的符号数 2*K*

输入到编码器的符号数，指定为等于 2*K* 的整数，其中 *K* 是输入位流的数量。

### **numOutputSymbols** — 从编码器输出的符号数 2*N*

从编码器输出的符号数，指定为等于 2*N* 的整数，其中 *N* 是输出位流的数量。

### **numStates** — 编码器中的状态数 2 的幂

编码器中的状态数，指定为 2 的幂。

### **nextStates** — 下一状态整数矩阵

当前状态和当前输入的所有组合的下一状态，指定为整数矩阵。矩阵大小必须为 `numStates` 乘 2*K*。

### **outputs** — 八进制数输出矩阵

当前状态和当前输入的所有组合的输出，指定为八进制数矩阵。矩阵大小必须为 `numStates` 乘 2*K*。

### **交织器索引源** — 交织器索引源 `Property` (default) | `Input port`

将交织器索引源指定为 `Property` 或 `Input port`。

- 当您将此参数设置为 `Property` 时，模块使用 **交织器索引** 参数指定交织器索引。
- 当您将此参数设置为 `Input port` 时，模块使用 `IntrInd` 输入端口指定交织器索引。

### **交织器索引** — 交织器索引 `(64:-1:1).'` (default) | 整数列向量

将交织器索引指定为整数列向量，这些索引定义用于置换输入到解码器的码字位的映射。该向量的长度必须为 *L*。向量的每个元素必须是范围 [1, *L*] 内的整数，且必须唯一。*L* 是解码后的二进制输出消息的长度。

#### 依赖关系

要启用此参数，请将 **交织器索引源** 参数设置为 `Property`。

### **输入索引源** — 输入索引源 `Auto` | `Property` | `Input port`

将输入索引源指定为 `Auto`、`Property` 或 `Input port`。

- 当您将此参数设置为 `Auto` 时，模块计算输入索引，这些索引假定第二个系统流被删余，并且所有尾位都包含在输入中。
- 当您将此参数设置为 `Property` 时，模块使用您为 **输入索引** 参数指定的输入索引。
- 当您将此参数设置为 `Input port` 时，模块使用 **InInd** 输入端口指定输入索引。输入索引和编码输入信号的向量长度和值可以在模块每次执行时更改。

### **输入索引** — 输入索引 `getTurboIOIndices(64,2,3)` (default) | 整数列向量

将用于完全编码数据的位排序和删余的输入索引指定为整数列向量。此参数的向量长度必须等于输入数据向量 **In** 的长度。

#### 依赖关系

要启用此参数，请将 **输入索引源** 参数设置为 `Property`。

### **解码算法** — 解码算法 `True APP` (default) | `Max*` | `Max`

将分量 APP 解码器用于解码输入信号的解码算法指定为 `True APP`、`Max*`、`Max`。当您将此参数设置为 `True APP` 时，模块实现真正的后验概率解码。当您将此参数设置为 `Max*` 或 `Max` 时，模块使用近似来提高计算速度。有关详细信息，请参阅 APP 解码器。

### **缩放位数** — 缩放位数 `3` (default) | 范围 [0, 8] 内的整数

将分量 APP 解码器为避免在计算期间丢失精度而必须用于缩放输入数据的位数指定为范围 [0, 8] 内的整数。分量解码器将输入乘以 2k，并将预输出除以同一因子。*k* 是 **缩放位数** 参数的值。有关详细信息，请参阅 APP 解码器。

#### 依赖关系

要启用此参数，请将 **解码算法** 参数设置为 `Max*`。

### **解码迭代次数** — 解码迭代次数 `6` (default) | 正整数

将模块使用的解码迭代次数指定为正整数。模块进行迭代并更新未编码输出位的对数似然比 (LLR)。模块的输出是最终 LLR 更新的硬判决输出。

### **仿真方式** — 要运行的仿真类型 `Interpreted execution` (default) | `Code generation`

要运行的仿真类型，指定为 `Interpreted execution` 或 `Code generation`。

- `Interpreted execution` — 使用 MATLAB 解释器仿真模型。此选项需要较少的启动时间，但后续仿真的速度比使用 `Code generation` 选项时慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为模块生成 C 代码。除非模型更改，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比使用 `Interpreted execution` 选项时快。

有关详细信息，请参阅解释执行与代码生成 (Simulink)。

## 所属库

Communications Toolbox / Error Detection and Correction / Convolutional

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2011b 中引入**

## 描述

使用并行级联解码方案对输入信号进行解码

Turbo Decoder 模块使用并行级联解码方案对输入信号进行解码。该迭代解码方案使用后验概率 (APP) 解码器作为分量解码器、一个交织器和一个解交织器。两个分量解码器使用相同的网格结构和解码算法。有关详细信息，请参阅并行级联卷积解码方案和 APP 解码器。

此图标显示启用了所有端口的模块。

启用了可选端口（IntrInd 和 InInd）的 Turbo Decoder 模块
