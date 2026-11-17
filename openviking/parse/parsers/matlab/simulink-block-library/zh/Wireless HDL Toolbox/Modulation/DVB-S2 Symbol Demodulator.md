---
type: simulink-block
title: 'DVB-S2 Symbol Demodulator'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Modulation'
documentation_page: 'dvbs2symboldemodulator'
documentation_source_path: 'ref/dvbs2symboldemodulator.html'
language: zh-CN
chinese_source: worker-translation
---

# DVB-S2 Symbol Demodulator

## 端口

### 输入

### **data** — 数据符号 实值标量 | 复值标量

数据符号，指定为实值或复值标量。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

对于 HDL 代码生成，输入数据类型必须为 `signed fixed point`，且该模块支持的最大输入字长为 32 位。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**复数支持：** 是

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包含 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

- `start` — 指示输入帧的起始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **valid** — 指示输入数据是否有效 标量

控制信号，用于指示输入数据是否有效。当该值为 `1` 时，模块接受 **data** 输入端口上的值。当该值为 `0` 时，模块忽略 **data** 输入端口上的值。

#### 依赖关系

要启用此端口，请将 **Output type** 参数设置为 `Scalar`。

**数据类型：** `Boolean`

### **modIdx** — 调制索引 `0` | `1` | `2` | `3` | `4`

调制索引，指定为 `0`、`1`、`2`、`3` 或 `4`。每个值代表一种特定的调制类型，如下表所示。

| 调制索引 | 调制类型 |
| --- | --- |
| `0` | QPSK |
| `1` | 8-PSK |
| `2` | 16-APSK |
| `3` | 32-APSK |
| `4` | π/2-BPSK |

如果指定的值不在此表中列出，模块将显示警告消息并应用 QPSK 调制。对于 HDL 代码生成，请以 `fixdt(0,3,0)` 格式指定此值。

#### 依赖关系

要启用此端口，请将 **Modulation source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `fixdt(0,3,0)`

### **codeRateIdx** — 码率索引 `5` | `6` | `7` | `8` | `9` | `10`

码率索引，指定为 `5`、`6`、`7`、`8`、`9` 或 `10`。每个值代表一种特定的码率，如下表所示。

| 码率索引 | 码率 |
| --- | --- |
| `5` | 2/3 |
| `6` | 3/4 |
| `7` | 4/5 |
| `8` | 5/6 |
| `9` | 8/9 |
| `10` | 9/10 |

此表中的码率适用于 **modIdx** 输入端口值 `2` 和 `3`，分别表示 16-APSK 和 32-APSK 调制。当将 **modIdx** 端口值设置为 `0`、`1` 或 `4` 时，模块忽略 **codeRateIdx** 输入端口值。

请以 `fixdt(0,4,0)` 格式指定此值。

#### 依赖关系

要启用此端口，请将 **Modulation source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `fixdt(0,4,0)`

### **nVar** — 噪声方差 实值正标量

噪声方差，指定为实值正标量。

此值的数据类型必须为 `fixdt(0,k,m)`，其中 *k* 小于或等于 16，*m* 小于或等于 *k*。

当 **Output type** 参数设置为 `Scalar` 时，模块在输入 **valid** 为 `1` 时采样 **nVar** 端口。

当 **Output type** 参数设置为 `Vector` 时，模块基于 `samplecontrol` 总线采样 **nVar** 端口。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

#### 依赖关系

要启用此端口，请选中 **Enable noise variance input port** 参数。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `unsigned fixed point`
### 输出

### **data** — 解调后的 LLR 值或数据比特 标量 | 八元素实值列向量

解调后的 LLR 值或数据比特，当 **Output type** 参数设置为 `Scalar` 时以标量形式返回，当 **Output type** 参数设置为 `Vector` 时以八元素实值列向量形式返回。

- 当 **Decision type** 参数设置为 `Approximate log-likelihood ratio` 时：

  - 对于 `double` 和 `single` 输入，输出数据类型与输入数据类型相同。
  - 对于 `fixed point` 输入，当您选中 **Enable noise variance input port** 参数时，模块提供的输出具有 14 位的整数位增长；当您清除该参数时，整数位增长为 3 位。
- 当 **Decision type** 参数设置为 `Hard` 时，对于任何支持的输入数据类型，输出数据类型为 `Boolean`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `Boolean` | `fixed point`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，以 `samplecontrol` 总线形式返回。该总线包含 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

- `start` — 指示输出帧的起始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

**数据类型：** `bus`

### **valid** — 有效输出数据指示 `0` | `1`

控制信号，指示来自 **data** 输出端口的数据是否有效。当该值为 `1` 时，模块在 **data** 输出端口上返回有效数据。当该值为 `0` 时，**data** 输出端口上的值无效。

#### 依赖关系

要启用此端口，请将 **Output type** 参数设置为 `Scalar`。

**数据类型：** `Boolean`

### **ready** — 指示模块已就绪 `0` | `1`

控制信号，指示模块何时准备好接受新的输入数据。当该值为 `1` 时，模块在下一个时间步接受输入数据。当该值为 `0` 时，模块在下一个时间步忽略输入数据。

**ready** 信号保持为 `0`，直到模块输出对应输入数据符号的数据。**ready** 信号保持为 `0` 的时钟周期数取决于所选的调制类型。

#### 依赖关系

要启用此端口，请将 **Output type** 参数设置为 `Scalar`。

**数据类型：** `Boolean`

## 参数

### **Modulation source** — 调制类型的来源 `Input port`（默认）| `Property`

要使用 **Modulation** 参数指定调制类型，请选择 `Property`。要在运行时使用 **modIdx** 端口指定调制类型，请选择 `Input port`。

### **Modulation** — 调制类型 `QPSK`（默认）| `8-PSK` | `16-APSK` | `32-APSK` | `pi/2-BPSK`

选择调制类型。

#### 依赖关系

要启用此参数，请将 **Modulation source** 参数设置为 `Property`。

### **Code rate** — 码率 `3/4`（默认）| `2/3` | `4/5` | `5/6` | `8/9` | `9/10`

选择码率。

#### 依赖关系

要启用此参数，请将 **Modulation source** 参数设置为 `Property`，并将 **Modulation** 参数设置为 `16-APSK` 或 `32-APSK`。

### **Decision type** — 解映射类型 `Approximate log-likelihood ratio`（默认）| `Hard`

选择解映射类型。

- `Approximate log-likelihood ratio` — 将数据符号解映射为 LLR 值。每个比特的该 LLR 值指示该比特为 `1` 或 `0` 的可能性。
- `Hard` — 将数据符号解映射为比特 `1` 或 `0`。

### **Output type** — 输出类型 `Vector`（默认）| `Scalar`

选择输出类型为 `Vector` 或 `Scalar`。

- `Vector` — 使用此选项可从输出 **data** 端口接收 8 元素列向量格式的数据。
- `Scalar` — 使用此选项可从输出 **data** 端口接收标量格式的数据。

### **Unit average power** — 单位平均功率 `off`（默认）| `on`

选择此参数以使用归一化星座执行符号解调。清除此参数以使用标准 [1] 中定义的星座执行符号解调。

当您在 **modIdx** 输入端口指定 `0`、`1` 或 `4`，或将 **Modulation** 参数设置为 `QPSK`、`8-PSK` 或 `pi/2-BPSK` 时，模块在其操作期间忽略此参数。

#### 依赖关系

要启用此参数，请将 **Modulation source** 参数设置为 `Input port`，或将 **Modulation source** 设置为 `Property` 并将 **Modulation** 参数设置为 `16-APSK` 或 `32-APSK`。

### **Enable noise variance input port** — 启用噪声方差端口 `off`（默认）| `on`

选择此参数以启用噪声方差输入端口。

#### 依赖关系

要启用此参数，请将 **Decision type** 参数设置为 `Approximate log-likelihood ratio`。

## 所属库

Wireless HDL Toolbox / Modulation

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

**限制**

无法在可复位同步子系统 (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2021b 中引入**

### R2022a：模块增强

在 2021b 中，该模块名为 DVBS2 Symbol Demodulator，现在在 R2022a 中重命名为 DVB-S2 Symbol Demodulator。

在 2022a 中，该模块支持将复星座符号解调为一组数据比特。此外，该模块提供参数选项以选择：

- Output type — Scalar 或 Vector
- Decision type — Hard 或 Approximate log-likelihood ratio
- 噪声方差输入端口

## 描述

根据 DVB-S2 标准，将复星座符号解调为一组 LLR 值或数据比特

DVB-S2 符号解调器模块基于数字视频广播卫星第二代（DVB-S2）标准 [1] 所支持的调制类型，将复数据符号解调为对数似然比（LLR）值或数据比特。该模块接受均衡后的复数据符号以及 `samplecontrol` 总线或 `valid` 信号。它根据所选的输出类型，输出解调后的 LLR 值或数据比特以及 `samplecontrol` 总线或 `valid` 信号。该模块提供将输出类型选择为向量或标量的选项。给定符号的解调 LLR 值或数据比特的数量取决于调制类型，如下表所示。

| 调制类型 | 每符号的 LLR 值或数据比特数 |
| --- | --- |
| π/2-BPSK | 1 |
| QPSK | 2 |
| 8-PSK | 3 |
| 16-APSK | 4 |
| 32-APSK | 5 |

该模块提供适合 HDL 代码生成和硬件部署的架构。您可以在 DVB-S2 接收机的开发中使用该模块。
