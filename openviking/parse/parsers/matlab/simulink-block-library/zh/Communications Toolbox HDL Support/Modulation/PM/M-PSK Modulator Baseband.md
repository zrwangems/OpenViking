---
type: simulink-block
title: 'M-PSK Modulator Baseband'
family: 'communications-toolbox-hdl-support'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Modulation / PM'
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

- 当 **Input type** 为 `Integer` 时，将输入信号元素指定为从 0 到 *M* – 1 的整数。
- 当 **Input type** 为 `Bit` 时，将输入信号指定为二进制向量，其中元素数量是每符号比特数的整数倍。每符号比特数等于 log2(*M*)。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`
### 输出

### **Out\_1** — 输出信号 标量 | 向量

输出信号，以复标量或复向量形式返回。输出是 PSK 调制信号的复基带表示。

**数据类型：** `single` | `double` | `fixed point`

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### 主要

### **M-ary number** — PSK 星座的调制阶数 `8`（默认）| 标量

将调制阶数指定为 2 的正整数次幂。

**示例：** `2` | `16`

### **Input type** — 输入信号类型 `Integer`（默认）| `Bit`

将输入信号元素指定为整数或比特。如果 **Input type** 为 `Bit`，则每帧样本数必须是每符号比特数的整数倍。每符号比特数为 log2(*M*)。

### **Constellation ordering** — 符号映射 `Gray`（默认）| `Binary` | `User-defined`

整数输入或 log2(*M*) 个比特为一组的输入的符号映射，指定为 `Gray`、`Binary` 或 `User-defined`。

- 当将 **Constellation ordering** 设置为 `Gray` 时，输入信号使用格雷编码信号星座映射到输出符号。
- 当将 **Constellation ordering** 设置为 `Binary` 时，调制符号为 exp(*jϕ*+*j2πm/M*)，其中 *ϕ* 是以弧度表示的相位偏移，*m* 是整数输入，满足 0 ≤ *m* ≤ M – 1，*M* 是调制阶数。
- 当将 **Constellation ordering** 设置为 `User-defined` 时，指定一个大小为 *M* 的向量，其中包含范围 [0, *M*–1] 内的唯一整数值。该向量的第一个元素对应于值为 e*jϕ* 的星座点，后续元素按逆时针方向排列。

**示例：** `[0 3 2 1]`

### **Constellation mapping** — 用户定义符号映射 `[0:7]`（默认）| 向量

用户定义符号映射，指定为包含范围 [0, *M* – 1] 内唯一整数值的 *M* 元素向量。使用此参数指定将输入整数映射到输出整数的自定义顺序。

该向量的第一个元素对应于 (0 + ϕ) 角度的星座点，后续元素按逆时针方向排列。最后一个元素对应于 (-2π/*M* + ϕ) 星座点。ϕ 是相位偏移（**Phase offset (rad)**）的值，*M* 是调制阶数（**M-ary number**）。

#### 依赖关系

此参数在将 **Constellation ordering** 设置为 `User-defined` 时适用。

### **Phase offset (rad)** — 以弧度表示的相位偏移 `pi/8`（默认）| 标量

以弧度为单位，将初始星座的相位偏移指定为实标量。

**示例：** `pi/4`

### **View constellation** — 绘制参考星座的选项 按钮

单击模块掩码上的 **View Constellation** 以可视化指定模块参数下的信号星座。在查看星座之前，请应用参数设置。有关详细信息，请参阅 View Constellation of Modulator Block。

### 数据类型

### **Output data type** — 输出数据类型 `double`（默认）| `single` | `Inherit via back propagation` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

指定调制输出信号的数据类型。将此参数设置为定点选项之一或 `<data type expression>`，以启用可指定其他详细信息的参数。将此参数设置为 `Inherit via back propagation`，以将输出数据类型和定标与模型中的下一个模块匹配。

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
| a 如果 ''input type'' 设置为 ''bit''，则输入为 ufix(1)。如果 ''input type'' 设置为 ''integer'' 用于 M 进制调制，则输入为 ufix(ceil(log2(M)))。  b 定点输出必须为有符号。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

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

**在 R2006a 之前引入**

## 描述

使用 M 进制相移键控进行调制

M-PSK Modulator Baseband 模块使用 M 进制相移键控 (PSK) 对输入信号进行调制，并返回复基带输出。调制阶数 *M* 等同于信号星座中的点数，由 **M-ary number** 参数确定。该模块接受标量或列向量输入信号。
