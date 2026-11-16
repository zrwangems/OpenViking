---
type: simulink-block
title: 'M-PSK Demodulator Baseband'
family: 'communications-toolbox-hdl-support'
product_id: 'communications-toolbox-hdl-support'
product_name: 'Communications Toolbox HDL Support'
documentation_release: R2025b
official_category: 'Modulation / PM'
documentation_page: 'mpskdemodulatorbaseband'
documentation_source_path: '../comm/ref/mpskdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# M-PSK Demodulator Baseband

## 端口

### 输入

### **In** — 输入信号 标量 | 向量

输入端口，接受 PSK 调制信号的基带表示。

在启用 **Var** 端口之前，此端口在模块上未命名。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean`

### **Var** — 噪声方差估计 正标量

噪声方差估计，指定为正标量。

**注意**

精确 LLR 算法使用有限精度算术计算指数。对于涉及非常大正数或负数幅度的计算，精确 LLR 算法会产生：

- 如果噪声方差是非常大的值，则产生 `Inf` 或 `-Inf`
- 如果噪声方差和信号功率都是非常小的值，则产生 `NaN`

近似 LLR 算法不计算指数。通过使用近似 LLR 算法，可以避免 `Inf`、`-Inf` 和 `NaN` 结果。

#### 依赖关系

当 **Noise variance source** 设置为 `Port` 时，此参数适用。

**数据类型：** `double` | `single`

### 输出

### **Out** — 输出信号 标量 | 向量

输出信号，以标量或向量形式返回。输出是 PSK 调制信号解调后的版本。

**数据类型：** `single` | `double` | `fixed point`

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中，选择 **Property Inspector**。

### 主要

### **M-ary number** — PSK 星座的调制阶数 `8`（默认）| 标量

将调制阶数指定为 2 的正整数次幂。

**示例：** `2` | `16`

### **Output type** — 输出信号数据类型 `Integer`（默认）| `Bit`

将输入信号的元素指定为整数或位。如果 **Output type** 为 `Bit`，则每帧样本数是每符号位数 log2(*M*) 的整数倍。

### **Decision type** — 解调器输出 `Hard decision`（默认）| `Log-likelihood ratio` | `Approximate log-likelihood ratio`

将解调器输出指定为硬判决、对数似然比 (LLR) 或近似 LLR。LLR 和近似 LLR 输出与支持软判决输入的错误解码器（例如 Viterbi Decoder）一起使用，以获得更优性能。有关详细信息，请参阅 Algorithms。

`Log-likelihood ratio` 和 `Approximate log-likelihood ratio` 判决类型的输出值的数据类型与输入值相同。

#### 依赖关系

当 **Output type** 设置为 `Bit` 时，此参数适用。

### **Noise variance source** — 噪声方差估计源 `Dialog`（默认）| `Port`

噪声方差估计源，指定为以下选项之一。

- 将此参数设置为 `Dialog`，以使用 **Noise variance** 参数定义噪声方差。
- 将此参数设置为 `Port`，以使用 **Var** 端口定义噪声方差。

指定噪声方差估计源。

- 要从对话框指定噪声方差，请选择 `Dialog`。
- 要从输入端口输入噪声方差，请选择 `Port`。

#### 依赖关系

当 **Decision type** 设置为 `Log-likelihood ratio` 或 `Approximate log-likelihood ratio` 时，此参数适用。

### **Noise variance** — 噪声方差估计 `1`（默认）| 正标量

将噪声方差估计指定为正标量。

此参数在所有仿真模式下均可调。如果使用 Simulink Coder™ 快速仿真 (RSIM) 目标构建 RSIM 可执行文件，则可以在不重新编译模型的情况下调整该参数。避免重新编译对于 Monte Carlo 仿真很有用，因为在此类仿真中，您会使用不同噪声量多次运行仿真（可能在多台计算机上）。

**注意**

精确 LLR 算法使用有限精度算术计算指数。对于涉及非常大正数或负数幅度的计算，精确 LLR 算法会产生：

- 如果噪声方差是非常大的值，则产生 `Inf` 或 `-Inf`
- 如果噪声方差和信号功率都是非常小的值，则产生 `NaN`

近似 LLR 算法不计算指数。通过使用近似 LLR 算法，可以避免 `Inf`、`-Inf` 和 `NaN` 结果。

**可调：** 是

#### 依赖关系

当 **Noise variance source** 设置为 `Dialog` 时，此参数适用。

### **Constellation ordering** — 符号映射 `Gray`（默认）| `Binary` | `User-defined`

指定整数或 log2(*M*) 位组如何映射到对应符号。

- 将 **Constellation ordering** 设置为 `Gray` 时，输出符号使用格雷编码信号星座映射到输入信号。
- 将 **Constellation ordering** 设置为 `Binary` 时，调制符号为 e^(j(φ+2πm/M))，其中 φ 是相位偏移（弧度），m 是整数输出，满足 0 ≤ m ≤ M – 1，M 是调制阶数。
- 将 **Constellation ordering** 设置为 `User-defined` 时，指定大小为 *M* 的向量，其中包含范围 [0, *M*–1] 内的唯一整数值。此向量的第一个元素对应于值为 e^(jφ) 的星座点，后续元素逆时针排列。

**示例：** 对于 QPSK 星座，为 `[0 3 2 1]`。

### **Constellation mapping** — 用户定义符号映射 `[0:7]`（默认）| 向量

指定输入整数映射到输出整数的顺序。当 **Constellation ordering** 为 `User-defined` 时，此参数可用，并且必须是大小为 *M* 的行向量或列向量，其中包含范围 [0, *M* – 1] 内的唯一整数值。

此向量的第一个元素对应于 (0 + φ) 角度的星座点，后续元素逆时针排列。最后一个元素对应于 (–2π/*M* + φ) 星座点。φ 是相位偏移（弧度）（**Phase offset (rad)**），*M* 是调制阶数（**M-ary number**）。

#### 依赖关系

当 **Constellation ordering** 设置为 `User-defined` 时，此参数适用。

### **Phase offset (rad)** — 以弧度表示的相位偏移 `pi/8`（默认）| 标量

初始星座的相位偏移（弧度），指定为标量。

**示例：** `pi/4`

### 数据类型

### **Output data type** — 输出数据类型 `Inherit via internal rule`（默认）| `Smallest unsigned integer` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32`

指定解调输出信号的数据类型。

有关指定数据类型的信息，请参阅 Data Type Assistant。

## 所属库

Communications Toolbox / Modulation / Digital Baseband Modulation / PSK Communications Toolbox HDL Support / Modulation / PM

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed pointa, b, c` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a M = 2, 4, 8 only.  b Fixed-point inputs must be signed.  c When ASIC/FPGA is selected in the Hardware Implementation Pane, output is ufix(1) for bit outputs, and ufix(ceil(log2(M))) for integer outputs. | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟，在输出处放置的寄存器数。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和受约束输出流水线可以移动这些寄存器。默认值为 `0`。有关详细信息，请参阅 OutputPipeline (HDL Coder)。 |

## 版本历史

**R2006a 之前引入**

## 描述

解调 PSK 调制数据

M-PSK Demodulator Baseband 模块对 PSK 调制信号的基带表示进行解调。调制阶数 *M* 等于信号星座中的点数，由 **M-ary number** 参数确定。该模块接受标量或列向量输入信号。
