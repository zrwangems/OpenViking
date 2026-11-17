---
type: simulink-block
title: 'M-PSK Modulator Baseband'
family: 'modulation'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / PSK'
documentation_page: 'mpskmodulatorbaseband'
documentation_source_path: '../comm/ref/mpskmodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# M-PSK Modulator Baseband

## 端口

### 输入

### **In\_1** — 输入信号 标量 | 向量

将输入信号指定为整数标量、整数向量或二进制向量。

- 当 **输入类型** 为 `Integer` 时，将输入信号元素指定为从 0 到 *M* – 1 的整数。
- 当 **输入类型** 为 `Bit` 时，将输入信号指定为二进制向量，其中元素数量是每符号位数的整数倍。每符号位数等于 log2(*M*)。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### 输出

### **Out\_1** — 输出信号 标量 | 向量

输出信号，以复标量或复向量形式返回。输出是 PSK 调制信号的复基带表示。

**数据类型：** `single` | `double` | `fixed point`

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® Toolstrip 中，在 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### 主要

### **M 元数** — PSK 星座的调制阶数 `8` (默认) | 标量

将调制阶数指定为 2 的正整数次幂。

**示例：** `2` | `16`

### **输入类型** — 输入信号的类型 `Integer` (默认) | `Bit`

将输入信号元素指定为整数或位。如果 **输入类型** 为 `Bit`，则每帧样本数必须是每符号位数的整数倍。每符号位数是 log2(*M*)。

### **星座排序** — 符号映射 `Gray` (默认) | `Binary` | `User-defined`

整数或 log2(*M*) 位输入组的符号映射，指定为 `Gray`、`Binary` 或 `User-defined`。

- 当将 **星座排序** 设置为 `Gray` 时，使用格雷编码的信号星座将输入信号映射到输出符号。
- 当将 **星座排序** 设置为 `Binary` 时，调制符号为 exp(*jϕ*+*j2πm/M*)，其中 *ϕ* 是以弧度表示的相位偏移，*m* 是整数输入，满足 0 ≤ *m* ≤ M – 1，*M* 是调制阶数。
- 当将 **星座排序** 设置为 `User-defined` 时，指定大小为 *M* 的向量，该向量具有范围 [0, *M*–1] 中的唯一整数值。此向量的第一个元素对应于值为 e*jϕ* 的星座点，后续元素按逆时针方向排列。

**示例：** `[0 3 2 1]`

### **星座映射** — 用户定义的符号映射 `[0:7]` (默认) | 向量

用户定义的符号映射，指定为具有范围 [0, *M* – 1] 中唯一整数值的 *M* 元素向量。使用此参数指定将输入整数映射到输出整数的自定义顺序。

此向量的第一个元素对应于 (0 + ϕ) 角度的星座点，后续元素按逆时针方向排列。最后一个元素对应于 (-2π/*M* + ϕ) 星座点。ϕ 是相位偏移（**相位偏移 (rad)**）的值，*M* 是调制阶数（**M 元数**）。

#### 依赖关系

当将 **星座排序** 设置为 `User-defined` 时，此参数适用。

### **相位偏移 (rad)** — 相位偏移，以弧度为单位 `pi/8` (默认) | 标量

以弧度为单位，将初始星座的相位偏移指定为实数标量。

**示例：** `pi/4`

### **查看星座** — 绘制参考星座的选项 按钮

在模块封装上点击 **查看星座** 以可视化指定模块参数的信号星座。在查看星座之前，请应用参数设置。有关更多信息，请参阅 View Constellation of Modulator Block。

### 数据类型

### **输出数据类型** — 输出数据类型 `double` (默认) | `single` | `Inherit via back propagation` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

指定调制输出信号的数据类型。将此参数设置为定点选项之一或 `<data type expression>`，以启用用于指定其他详细信息的参数。将此参数设置为 `Inherit via back propagation`，以匹配模型中下一个模块的输出数据类型和定标。

有关指定数据类型的信息，请参阅 Data Type Assistant。

## 所属库

Communications Toolbox / Modulation / Digital Baseband Modulation / PSK Communications Toolbox HDL Support / Modulation / PM

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed pointa, b` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a 如果 ''输入类型'' 设置为 ''bit''，则输入为 ufix(1)。对于 M 元调制，如果 ''输入类型'' 设置为 ''integer''，则输入为 ufix(ceil(log2(M)))。  b 定点输出必须为有符号。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供了影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计中移动现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**R2006a 之前推出**

## 描述

使用 M 元相移键控进行调制

M-PSK Modulator Baseband 模块使用 M 元相移键控 (PSK) 对输入信号进行调制，并返回复基带输出。调制阶数 *M* 等效于信号星座中的点数，由 **M 元数** 参数确定。该模块接受标量或列向量输入信号。
