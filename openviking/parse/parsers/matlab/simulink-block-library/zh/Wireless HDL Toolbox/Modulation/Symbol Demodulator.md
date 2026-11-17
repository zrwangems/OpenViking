---
type: simulink-block
title: 'Symbol Demodulator'
family: 'wireless-hdl'
product_id: 'wireless-hdl'
product_name: 'Wireless HDL Toolbox'
documentation_release: R2025b
official_category: 'Modulation'
documentation_page: 'symboldemodulator'
documentation_source_path: 'ref/symboldemodulator.html'
language: zh-CN
chinese_source: worker-translation
---

# Symbol Demodulator

## 端口

### 输入

### **data** — 数据符号 实值标量 | 复值标量

数据符号，指定为实值或复值标量。

仿真支持 `double` 和 `single` 数据类型，但不支持 HDL 代码生成。

对于 HDL 代码生成，输入数据类型必须为 `signed fixed point`，且该模块支持的最大输入字长为 32 位。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `signed fixed point`
**复数支持：** 是

### **valid** — 有效输入数据指示 标量

控制信号，用于指示输入数据是否有效。当该值为 `1`（true）时，模块接受 **data** 输入端口上的值。当该值为 `0`（false）时，模块忽略 **data** 输入端口上的值。

#### 依赖关系

要启用此端口，请将 **Output type** 参数设置为 `Scalar`。

**数据类型：** `Boolean`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，指定为 `samplecontrol` 总线。该总线包含 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

- `start` — 指示输入帧的开始
- `end` — 指示输入帧的结束
- `valid` — 指示输入 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

#### 依赖关系

要启用此端口，请将 **Modulation source** 参数设置为 `Input port`，并将 **Output type** 参数设置为 `Vector`。

**数据类型：** `bus`

### **modSel** — 调制选择 `0` | `1` | `2` | `3` | `4` | `5` | `6` | `7`

调制选择，指定为 `0`、`1`、`2`、`3`、`4`、`5`、`6` 或 `7`。每个值代表一种特定的调制类型，如下表所示。

| 调制选择值 | 调制类型 |
| --- | --- |
| `0` | BPSK |
| `1` | QPSK |
| `2` | 8-PSK |
| `3` | 16-PSK |
| `4` | 16-QAM |
| `5` | 32-PSK |
| `6` | 64-QAM |
| `7` | 256-QAM |

如果指定的值不在上表所列值中，或大于通过 **Maximum modulation** 参数在模块掩码上指定的值，模块将显示警告消息并应用 BPSK 调制。通过 **modSel** 端口指定的值必须相对于通过 **Maximum modulation** 参数设置的值。

例如，如果 **Maximum modulation** 参数设置为 `32-PSK`，模块允许的 **modSel** 值为 `0`、`1`、`2`、`3`、`4` 和 `5`。对于 **modSel** 值 `6` 和 `7`，模块将显示警告消息并应用 BPSK 调制。

#### 依赖关系

要启用此端口，请将 **Modulation source** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `fixdt(0,3,0)`

### **nVar** — 噪声方差 实值正标量

噪声方差，指定为实值正标量。

该值的数据类型必须为 `fixdt(0,k,m)`，其中 *k* 小于或等于 32，*m* 小于或等于 *k*。

当 **Output type** 参数设置为 `Scalar` 或 `Vector` 时，模块在输入 **valid** 设置为 `1` 时对此端口上的值进行采样。

该软件支持 `double` 和 `single` 数据类型用于仿真，但不支持 HDL 代码生成。

#### 依赖关系

要启用此端口，请选择 **Enable noise variance input port** 参数。

**数据类型：** `single` | `double` | `uint8` | `uint16` | `unsigned fixed point`
### 输出

### **data** — 解调后的 LLR 值或数据比特 标量 | 实值列向量

解调后的 LLR 值或数据比特，当 **Output type** 参数设置为 `Scalar` 时以标量形式返回，当 **Output type** 参数设置为 `Vector` 时以实值列向量形式返回。

如果将 **Modulation source** 参数设置为 `Property`，输出向量大小基于 **Modulation** 参数值。如果将 **Modulation source** 参数设置为 `Input port`，输出向量大小基于 **Maximum modulation** 参数值。

- 当 **Decision type** 参数设置为 `Approximate log-likelihood ratio` 时

  - 对于 `double` 和 `single` 输入，输出数据类型与输入数据类型相同。仿真数据类型支持 `double` 和 `single` 数据类型。
  - 对于 `fixed point` 输入，该模块提供整数位增长为 4 位的输出，并支持 HDL 代码生成。如果选中 **Enable noise variance input port** 参数，输出的整数位增长为 13 位。
- 当 **Decision type** 参数设置为 `Hard` 时，无论输入数据类型如何，输出数据类型均为 `Boolean`。

**数据类型：** `single` | `double` | `Boolean` | `signed fixed point`

### **ctrl** — 伴随样本流的控制信号 `samplecontrol` 总线

伴随样本流的控制信号，以 `samplecontrol` 总线形式返回。该总线包含 `start`、`end` 和 `valid` 控制信号，用于指示帧的边界和样本的有效性。

- `start` — 指示输出帧的起始
- `end` — 指示输出帧的结束
- `valid` — 指示输出 **data** 端口上的数据有效

有关更多详细信息，请参阅 Sample Control Bus。

#### 依赖关系

要启用此端口，请将 **Modulation source** 参数设置为 `Input port`，并将 **Output type** 参数设置为 `Vector`。

**数据类型：** `bus`

### **valid** — 有效输出数据指示 标量

控制信号，指示 **data** 输出端口的数据是否有效。当该值为 `1`（true）时，模块在 **data** 输出端口返回有效数据。当该值为 `0`（false）时，**data** 输出端口上的值无效。

#### 依赖关系

要启用此端口：

- 将 **Modulation source** 参数设置为 `Input port` 或 `Property`，并将 **Output type** 参数设置为 `Scalar`。
- 将 **Modulation source** 参数设置为 `Property`，并将 **Output type** 参数设置为 `Vector`。

**数据类型：** `Boolean`

### **ready** — 指示模块已就绪 标量

控制信号，指示模块何时准备好接受新的输入数据。当该值为 `1`（true）时，模块在下一个时间步接受输入数据。当该值为 `0`（false）时，模块在下一个时间步忽略输入数据。

**ready** 信号保持为 `0`（false），直到模块输出对应输入数据符号的数据。**ready** 信号保持为 `0`（false）的时钟周期数取决于所选的调制类型。

#### 依赖关系

要启用此端口，请将 **Output type** 参数设置为 `Scalar`。

**数据类型：** `Boolean`

## 参数

### **Modulation source** — 调制类型的来源 `Property`（默认） | `Input port`

要从 **Modulation** 参数指定调制类型，请选择 `Property`。要在运行时从 **modIdx** 端口指定调制类型，请选择 `Input port`。

### **Modulation** — 调制类型 `BPSK`（默认） | `QPSK` | `8-PSK` | `16-PSK` | `16-QAM` | `32-PSK` | `64-QAM` | `256-QAM`

选择调制类型。

#### 依赖关系

要启用此参数，请将 **Modulation source** 参数设置为 `Property`。

### **Maximum modulation** — 最大调制类型 `256-QAM`（默认）| `BPSK` | `QPSK` | `8-PSK` | `16-PSK` | `16-QAM` | `32-PSK` | `64-QAM`

选择最大调制类型。此参数值定义了模块可通过 **modSel** 端口支持的调制类型。

例如，当您使用此参数指定 `16-PSK` 时，模块为 `16-PSK` 调制类型生成的硬件资源数量可以容纳通过 **modSel** 端口指定的 `BPSK`、`QPSK` 和 `8-PSK` 调制类型的配置，但不能容纳 `16-QAM`、`32-PSK`、`64-QAM` 和 `256-QAM` 调制类型的配置。

#### 依赖关系

要启用此参数，请将 **Modulation source** 参数设置为 `Input port`。

### **Constellation ordering** — 星座排序 `Default`（默认）| `User-defined`

选择星座排序，即模块如何将二进制字分配给信号星座的点。

- `Default` — 指定默认星座排序值 `[2, 3, 1, 0, 6, 7, 5, 4, 14, 15, 13, 12, 10, 11, 9, 8]`
- `User defined` — 允许您使用 **Constellation mapping** 参数指定自定义星座排序值

#### 依赖关系

- 要启用此参数，请将 **Modulation source** 参数设置为 `Property`，并将 **Modulation** 参数设置为 `16-QAM`、`64-QAM` 或 `256-QAM`。
- 要启用此参数，请将 **Modulation source** 参数设置为 `Input port`，并将 **Maximum modulation** 参数设置为 `16-QAM`、`64-QAM` 或 `256-QAM`。

### **Constellation mapping** — 星座映射 `[2, 3, 1, 0, 6, 7, 5, 4, 14, 15, 13, 12, 10, 11, 9, 8]`（默认）| 唯一整数值格雷编码行向量

指定与使用 **Modulation** 参数或 **Maximum modulation** 参数选择的调制类型相对应的唯一整数值格雷编码行向量。此向量的第一个元素对应于星座的最左上点，后续元素按列从上到下、从左到右排列。最后一个元素对应于最右下点。有关支持的格雷码的详细信息，请参阅 Specify Gray Code。

此参数特定于 `16-QAM`、`64-QAM` 和 `256-QAM` 调制类型。

#### 依赖关系

要启用此参数，请将 **Constellation ordering** 参数设置为 `User defined`。

### **Decision type** — 解映射类型 `Approximate log-likelihood ratio`（默认）| `Hard`

选择解映射类型。

- `Approximate log-likelihood ratio` — 将数据符号解映射为 LLR 值。每个比特的此 LLR 值指示该比特为 `1` 或 `0` 的可能性。
- `Hard` — 将数据符号解映射为比特 `1` 或 `0`。

### **Phase offset** — 星座点的相位偏移 `pi/2`（默认）| `pi/4` | `pi/8` | `pi/16` | `pi/32` | `0` | `-pi/32` | `-pi/16` | `-pi/8` | `-pi/4` | `-pi/2`

选择相位偏移。此参数特定于 `BPSK`、`QPSK`、`8-PSK`、`16-PSK` 和 `32-PSK` 调制类型。

#### 依赖关系

- 要启用此参数，请将 **Modulation source** 参数设置为 `Property`，并将 **Modulation** 参数设置为 `BPSK`、`QPSK`、`8-PSK`、`16-PSK` 或 `32-PSK`。
- 要启用此参数，请将 **Modulation source** 参数设置为 `Input port`，无论为 **Maximum modulation** 参数指定的调制类型是什么。

### **Output type** — 输出类型 `Vector`（默认）| `Scalar`

选择输出类型为 `Vector` 或 `Scalar`。

- `Vector` — 使用此选项从输出 **data** 端口以向量格式接收数据。

  当您将 **Modulation source** 参数设置为 `Property` 时，输出向量大小基于 **Modulation** 参数值。当您将 **Modulation source** 参数设置为 `Input port` 时，输出向量大小基于 **Maximum modulation** 参数值。
- `Scalar` — 使用此选项从输出 **data** 端口以标量格式接收数据。

### **Normalization method** — 缩放信号星座 `Unit average power`（默认）| `Custom`

选择模块如何缩放信号星座。

- `Unit average power` — 将星座归一化为单位平均功率
- `Custom` — 允许您通过使用 **Minimum distance between symbols** 参数指定星座点之间的最小距离来归一化星座

**注意**

当您使用 **modSel** 输入端口指定 `0`、`1`、`2`、`3` 或 `5` 时，模块在其操作期间忽略此参数。此参数适用于基于 QAM 的调制。

#### 依赖关系

- 要启用此参数，请将 **Modulation source** 参数设置为 `Property`，并将 **Modulation** 参数设置为 `16-QAM`、`64-QAM` 或 `256-QAM`。
- 要启用此参数，请将 **Modulation source** 参数设置为 `Input port`，并将 **Maximum modulation** 参数设置为 `16-QAM`、`64-QAM` 或 `256-QAM`。

### **Minimum distance between symbols** — 符号之间的最小距离 `2`（默认）| 范围从 1/32 到 2 的值

使用范围从 1/32 到 2 的值指定符号之间的最小距离。

**注意**

当您使用 **modSel** 输入端口指定 `0`、`1`、`2`、`3` 或 `5` 时，模块在其操作期间忽略此参数。此参数适用于基于 QAM 的调制。

#### 依赖关系

要启用此参数，请将 **Normalization method** 参数设置为 `Custom`。

### **Enable noise variance input port** — 启用噪声方差端口的选项 `off`（默认）| `on`

选择此参数以启用噪声方差输入端口。

## 所属库

Wireless HDL Toolbox / Modulation

## 模块特性

R2025b 中未记录。

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

此模块支持用于 Simulink® 加速器和快速加速器模式以及 DPI 组件生成的 C/C++ 代码生成。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder 提供影响 HDL 实现和综合逻辑的额外配置选项。

**HDL 架构**

此模块具有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过在设计内移动现有延迟来放置在输出端的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 在生成代码中插入的输入流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 在生成代码中插入的输出流水线级数。分布式流水线和约束输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

无法在可重置同步子系统 (HDL Coder) 内为此模块生成 HDL。

## 版本历史

**在 R2022a 中引入**

## 描述

将复星座符号解调为一组 LLR 值或数据比特

Symbol Demodulator 模块将复星座符号解调为一组对数似然比（LLR）值或数据比特。该模块接受均衡后的复数据符号以及 `samplecontrol` 总线或 `valid` 信号，并根据所选的输出类型输出解调后的 LLR 值或数据比特以及 `samplecontrol` 总线或 `valid` 信号。该模块提供将输出类型选择为向量或标量的选项，并提供一个输入端口用于指定噪声方差。

该模块支持 BPSK、QPSK、8-PSK、16-PSK、32-PSK、16-QAM、64-QAM 和 256-QAM 调制。对于给定符号，解调后的 LLR 值或数据比特的数量取决于调制类型，如下表所示。

| 调制类型 | 每符号的 LLR 值或数据比特数 |
| --- | --- |
| BPSK | 1 |
| QPSK | 2 |
| 8-PSK | 3 |
| 16-PSK | 4 |
| 16-QAM | 4 |
| 32-PSK | 5 |
| 64-QAM | 6 |
| 256-QAM | 8 |

该模块为使用 HDL Coder™ 进行 HDL 代码生成提供了接口和架构。您可以在数字接收机的开发中使用该模块。
