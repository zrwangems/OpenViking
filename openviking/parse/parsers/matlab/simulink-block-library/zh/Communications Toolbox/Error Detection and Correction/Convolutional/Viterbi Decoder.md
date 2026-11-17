---
type: simulink-block
title: 'Viterbi Decoder'
family: 'error-detection-and-correction'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Error Detection and Correction / Convolutional'
documentation_page: 'viterbidecoder'
documentation_source_path: 'ref/viterbidecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Viterbi Decoder

## 端口

### 输入

### **In** — 卷积编码码字列向量

卷积编码码字，指定为列向量。如果解码器接受 *N* 个输入比特流（也就是说，它可以接收 2*N* 个可能的输入符号），则对于某个正整数 *L*，模块输入向量长度为 *L*×*N*。有关详细信息，请参阅输入和输出大小、输入值和判决类型以及 `Operation mode` 参数。

此端口在启用第二个输入端口之前没有名称。

**数据类型：** `double` | `single` | `Boolean` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `ufixn`

### **Era** — 码字中的删除位二值向量

码字中的删除位，指定为二值向量。向量中值为 `1` 对应删除位，值为 `0` 对应非删除位。

对于传入数据流中的这些删除位，解码器不更新分支度量。删除端口和输入数据端口的宽度及采样时间必须相同。

#### 依赖

要启用此端口，请选择 **Enable erasures input port**。

**数据类型：** `double` | `Boolean`

### **Rst** — 用于复位解码器寄存器状态的选项 `scalar`

用于复位解码器寄存器状态的选项，指定为标量值。当此端口接收到非零输入值时，模块在处理输入数据之前将其内部存储器设置为初始状态。将解码器寄存器复位到初始状态会设置：

- 全零状态度量为零
- 所有其他状态度量为最大值
- 回溯存储器为零

在此模块上使用复位端口类似于将 Convolutional Encoder 模块的 **Operation mode** 设置为 `Reset on nonzero input via port`。

#### 依赖

要启用此端口，请将 **Operation mode** 参数设置为 `Continuous`，并选择 **Enable reset input port**。

**数据类型：** `double` | `Boolean`

### 输出

### **Out** — 输出消息二值列向量

输出消息，以二值列向量形式返回。如果解码器产生 *K* 个输出比特流（也就是说，它可以产生 2*K* 个可能的输出符号），则对于某个正整数 *L*，模块输出向量长度为 *L*×*K*。有关详细信息，请参阅输入和输出大小。

此端口在模块图标上没有名称。

**数据类型：** `double` | `single` | `Boolean` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `ufix1`

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

#### 主要

### **Trellis structure** — 卷积码的网格描述 `poly2trellis(7,[171 133])`（默认）

卷积码的网格描述，指定为包含码率为 *K* ∕ *N* 的码的网格描述的结构体。*K* 是输入比特流数量，*N* 是输出比特流数量。

您可以使用 `poly2trellis` 函数创建网格结构体，也可以手动创建。有关此结构体的详细信息，请参阅卷积码的网格描述和 `istrellis` 函数。

网格结构体包含以下字段。

### **numInputSymbols** — 输入到编码器的符号数 2*K*

输入到编码器的符号数，指定为等于 2*K* 的整数，其中 *K* 是输入比特流数量。

### **numOutputSymbols** — 从编码器输出的符号数 2*N*

从编码器输出的符号数，指定为等于 2*N* 的整数，其中 *N* 是输出比特流数量。

### **numStates** — 编码器中的状态数 2 的幂

编码器中的状态数，指定为 2 的幂。

### **nextStates** — 下一状态整数矩阵

当前状态和当前输入的所有组合的下一状态，指定为整数矩阵。矩阵大小必须为 `numStates` 乘 2*K*。

### **outputs** — 八进制数输出矩阵

当前状态和当前输入的所有组合的输出，指定为八进制数矩阵。矩阵大小必须为 `numStates` 乘 2*K*。

### **Punctured code** — 用于启用码打孔指定的选项 `off`（默认）| `on`

选择此参数以查看并启用 **Puncture vector** 参数。

### **Puncture vector** — 打孔模式向量 `[1; 1; 0; 1; 0; 1]`（默认）| 向量

用于对解码数据打孔的打孔模式向量，指定为向量。该向量必须包含 `1` 和 `0`，其中 `0` 表示打孔位的位置。此打孔模式必须与卷积编码器使用的打孔模式匹配。

有关特定码率和多项式的某些常用打孔模式，请参阅 Yasuda [4]、Haccoun [5] 和 Begin [6] 参考文献。

#### 依赖

仅当选择 **Punctured code** 参数时，才会显示此参数。

### **Enable erasures input port** — 用于启用删除输入端口的选项 `off`（默认）| `on`

选择此参数可向模块添加 `Era` 输入端口。

### **Decision type** — 解码器判决类型 `Unquantized`（默认）| `Hard decision` | `Soft decision`

解码器判决类型，指定为 `Unquantized`、`Hard decision` 或 `Soft Decision`。

- `Unquantized` — 解码器使用欧几里得距离计算分支度量。输入数据必须是未量化的 double- 或 single-precision 软值实值向量。该对象将正值映射为逻辑 `1`，将负值映射为逻辑 `0`
- `Hard decision` — 解码器使用汉明距离计算分支度量。输入必须是硬判决值向量，即 `0` 或 `1`。输入的数据类型必须为 double precision、single precision、logical 或 numeric。
- `Soft Decision` — 解码器使用汉明距离计算分支度量。输入需要量化的软值向量，这些值表示为 0 到 2*SoftInputWordLength* – 1 之间的整数。输入的数据类型必须为 double precision、single precision、logical 或 numeric。或者，您可以使用 `fi` (Fixed-Point Designer) 对象将数据类型指定为无符号且未缩放的定点对象，其字长（*SoftInputWordLength*）等于为 **Number of soft decision bits** 参数指定的字长。`0` 被视为最置信的 `0`，而 2*SoftInputWordLength* – 1 被视为最置信的 `1`。

### **Number of soft decision bits** — 软输入字长 `4`（默认）| 正整数

软输入字长，表示每个量化软输入值的位数，指定为整数。

#### 依赖

仅当将 **Decision type** 参数设置为 `Soft decision` 时，才会显示此参数。

### **Error if quantized input values are out of range** — 如果量化输入值超出范围则报错的选项 `off`（默认）| `on`

选择此参数可在量化输入值超出范围时报错。如果未选择此参数，则忽略超出范围的输入值。

#### 依赖

仅当将 **Decision type** 参数设置为 `Hard decision` 或 `Soft decision` 时，才会显示此参数。

### **Traceback depth** — 回溯深度 `34`（默认）| 正整数

回溯深度，指定为整数，表示用于构造每条回溯路径的网格分支数。

回溯深度影响解码延迟。解码延迟是输出中第一个解码符号之前的零符号数。

- 对于连续操作模式，解码延迟等于回溯深度符号数。
- 对于截断或终止操作模式，解码延迟为零。在这种情况下，回溯深度必须小于或等于每个输入中的符号数。

作为一般估计，典型的回溯深度值约为 (*ConstraintLength* – 1) / (1 – *coderate*) 的两到三倍。码的约束长度 *ConstraintLength* 等于 (log2(`trellis`.`numStates`) + 1)。*coderate* 等于 (*K* / *N*) × (length(*PuncturePattern*) / sum(*PuncturePattern*)。

*K* 是输入符号数，*N* 是输出符号数，*PuncturePattern* 是打孔模式向量。

例如，应用此一般估计会得到以下近似回溯深度。

- 码率 1/2 的码的回溯深度为 5(*ConstraintLength* – 1)。
- 码率 2/3 的码的回溯深度为 7.5(*ConstraintLength* – 1)。
- 码率 3/4 的码的回溯深度为 10(*ConstraintLength* – 1)。
- 码率 5/6 的码的回溯深度为 15(*ConstraintLength* – 1)。

有关详细信息，请参阅 [7]。

### **Operation mode** — 编码帧的终止方法 `Continuous`（默认）| `Truncated` | `Terminated`

在连续输入帧之间转换的方法，指定为以下模式值之一。

- `Continuous` — 模块在每个输入结束时保存其内部状态度量，以供下一帧使用。每条回溯路径单独处理。对于码率 *K*/*N* 的卷积码，此模式导致 **Traceback depth**×*K* 个零比特的解码延迟。*K* 是消息符号数，*N* 是编码符号数。如果选择了 **Enable reset input port**，则当 `Rst` 端口接收到非零值时，解码器状态会复位。
- `Truncated` — 模块独立处理每个输入。回溯路径从具有最佳度量的状态开始，并始终以全零状态结束。当对应的 Convolutional Encoder 模块将其 **Operation mode** 设置为 `Truncated (reset every frame)` 时，此模式适用。此模式没有输出延迟。
- `Terminated` — 模块独立处理每个输入，回溯路径始终从全零状态开始并以全零状态结束。当未编码消息信号（即对应 Convolutional Encoder 模块的输入）在每个输入末尾有足够的零以填充前馈编码器的所有存储器寄存器时，此模式适用。具体而言，对于具有 `k` 个输入流和约束长度向量 `constr`（使用多项式描述）的编码器，输入末尾至少有 `k*max(constr-1)` 个零。对于反馈编码器，如果对应的 Convolutional Encoder 模块将 **Operation mode** 设置为 `Terminate trellis by appending bits`，则此模式适用。

**注意**

当模块在仿真期间输出长度可变的序列，并且您将 **Operation mode** 设置为 `Truncated` 或 `Terminated` 时，解码器状态在每个输入时间步都会复位。

当输入信号仅包含一个符号时，请使用 `Continuous` 操作模式。

### **Enable reset input port** — 用于添加复位输入端口的选项 `off`（默认）| `on`

选择此参数可添加 `Rst` 输入端口。

#### 依赖

仅当将 **Operation mode** 参数设置为 `Continuous` 时，才会显示此参数。

### **Delay reset action to next time step** — 用于将复位操作延迟到下一时间步的选项 `off`（默认）| `on`

选择此参数可将解码器的复位延迟到计算当前时间步接收到的编码数据之后。必须启用此选项才能支持 HDL。生成 HDL 代码需要 HDL Coder™ 软件。

#### 依赖

仅当将 **Operation mode** 参数设置为 `Continuous` 并选择 **Enable reset input port** 时，才会显示此参数。

#### 数据类型

### **State metric word length** — 状态度量字长 `16`（默认）| 正整数

状态度量字长，指定为正整数。

### **Output data type** — 输出数据类型 `Inherit via internal rule`（默认）| `Smallest unsigned integer` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

输出数据类型，指定为 `double`、`single`、`boolean`、`int8`、`uint8`、`int16`、`uint16`、`int32` 或 `uint32`，或者设置为 `'Inherit via internal rule'` 或 `'Smallest unsigned integer'`。

- 当设置为 `'Smallest unsigned integer'` 时，将基于模型的 Configuration Parameters 对话框的 **Hardware Implementation** 窗格中使用的设置选择输出数据类型。如果在 **Hardware Implementation** 窗格中选择了 `ASIC/FPGA`，则输出数据类型为 `ufix(1)`。对于所有其他选择，它是与 char 值对应的最小指定字长的无符号整数（例如 `uint8`）。
- 当设置为 `'Inherit via internal rule'` 时，模块：

  - 对于 double 输入，输出数据类型为 double
  - 对于 single 输入，输出数据类型为 single
  - 对于所有其他数据类型输入，行为类似于 `'Smallest unsigned integer'` 选项

## 所属库

Communications Toolbox / Error Detection and Correction / Convolutional Communications Toolbox HDL Support / Error Detection and Correction / Convolutional

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed pointa` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a 对于硬判决，输入可以是 ufix(1)；对于软判决，输入可以是 ufix(N)；输出只能是 ufix(1)。 | |

## 扩展功能

### C/C++ 代码生成

使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成

使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

**注意**

对于解码使用截断或终止模式或打孔码编码的数据，请使用 Viterbi Decoder (Wireless HDL Toolbox) 模块。Wireless HDL Toolbox™ 模块提供针对 HDL 优化的算法，具有硬件友好的控制信号，并在 Simulink 中模拟 HDL 算法的延迟。

HDL Coder 提供影响 HDL 实现和综合逻辑的额外配置选项。

HDL Coder 支持 Viterbi Decoder 模块的以下功能：

- 具有前馈网格和简单移位寄存器生成配置的非递归编码器/解码器
- 连续模式
- 基于采样的输入
- 解码器码率从 1/2 到 1/7
- 约束长度从 3 到 9

当将 **Decision type** 设置为 `Soft decision` 时，定点输入和输出数据类型支持 HDL 代码生成。输入定点数据类型必须为 `ufixN`。`N` 是软判决位数。有符号内置数据类型（`int8`、`int16`、`int32`）不支持 HDL 代码生成。

当将 **Decision type** 设置为 `Hard decision` 时，数据类型为 `ufix1` 和 `Boolean` 的输入支持 HDL 代码生成。double 和 single 输入数据类型不支持 HDL 代码生成。

Viterbi Decoder 模块通过回溯您为模块定义的回溯深度来解码每个比特。该模块为每个判决位实现完整回溯，使用寄存器在回溯解码单元中存储最小状态索引和分支判决。有两种方法可优化回溯逻辑：基于流水线寄存器的实现或基于 RAM 的架构。请参阅 Generate HDL Code for Viterbi Decoder 示例。

**基于寄存器的回溯**

您可以指定回溯解码单元采用流水线，以提高生成电路的速度。您可以通过指定每个流水线寄存器的回溯级数来向回溯单元添加流水线寄存器。

使用 `TracebackStagesPerPipeline` 实现参数，您可以根据系统要求平衡电路性能。较小的参数值表示需要添加更多寄存器以提高回溯电路的速度。增大参数值会导致寄存器更少，同时电路速度降低。

**基于 RAM 的回溯**

您可以选择使用 RAM 而不是寄存器来保存幸存分支信息。使用基于 RAM 的回溯时，代码生成器不支持 **Enable reset input port**。

1. 右键单击模块并打开 **HDL Code** > **HDL Block Properties**。将 **Architecture** 属性设置为 `RAM-based Traceback`。
2. 双击模块，并在 Viterbi Decoder 模块掩码上设置 **Traceback depth**。

基于 RAM 的回溯和基于寄存器的回溯在以下方面有所不同：

- 基于 RAM 的实现通过一组数据进行回溯，以找到用于解码上一组数据的初始状态。基于寄存器的实现将回溯和解码操作合并为一个步骤。它使用最小操作中找到的最佳状态作为解码初始状态。
- 基于 RAM 的实现回溯 M 个样本，按相反顺序解码前 M 个比特，并在每个时钟周期按顺序释放一个比特。基于寄存器的实现在一个完整回溯之后解码一个比特。

由于两种回溯算法的差异，基于 RAM 的实现产生的数值结果与基于寄存器的回溯不同。在基于 RAM 的回溯中，建议使用更长的回溯深度，例如约束长度的 10 倍。此深度可实现与基于寄存器实现相似的误码率 (BER)。实现所需的 RAM 大小取决于网格和回溯深度。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放在输出处的寄存器数。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |
| **TracebackStagesPerPipeline** | 请参阅基于寄存器的回溯。 |

**限制**

- **Punctured code**：不要选择此选项。打孔码需要基于帧的输入，HDL Coder 不支持。
- **Decision type**：代码生成器不支持 `Unquantized` 判决类型。
- **Error if quantized input values are out of range**：代码生成器不支持此选项。
- **Operation mode**：代码生成器仅支持 `Continuous` 模式。
- **Enable reset input port**：当同时启用 **Enable reset input port** 和 **Delay reset action to next time step** 时，支持 HDL。您必须选择 `Continuous` 操作模式，并使用基于寄存器的回溯。
- 不能在 Resettable Synchronous Subsystem (HDL Coder) 内使用 Viterbi Decoder 模块。

## 版本历史

**在 R2006a 之前引入**

### R2022b: 版本历史

范围 [–1012, 1012] 之外的未量化输入值分别被裁剪为 –1012 和 1012。

## 描述

使用 Viterbi 算法解码卷积编码数据

Viterbi Decoder 模块使用 Viterbi 算法将卷积编码输入符号解码为二进制输出符号。网格结构体指定卷积编码方案。有关详细信息，请参阅卷积码的网格描述。

此模块可以一次处理多个符号以提高性能，并且可以接受在仿真期间长度变化的输入。有关可变大小信号的详细信息，请参阅可变大小信号基础知识 (Simulink)。

此图标显示启用所有可选模块端口的情况。

启用了可选删除端口和复位端口的 Viterbi Decoder 模块
