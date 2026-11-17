---
type: simulink-block
title: 'Rectangular QAM Demodulator Baseband'
family: 'modulation'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / PAM/QAM'
documentation_page: 'rectangularqamdemodulatorbaseband'
documentation_source_path: 'ref/rectangularqamdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# Rectangular QAM Demodulator Baseband

## 端口

### 输入

### **In** — QAM 调制信号 标量 | 向量

QAM 调制信号，指定为标量或列向量。在启用 `Var` 端口之前，此端口未命名。

**数据类型：** `double` | `single` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
**复数支持：** Yes

### **Var** — 噪声方差 正标量 | 正值向量

噪声方差，指定为正标量或正值向量。当噪声方差或信号功率导致涉及极大正值或负值的计算时，请参阅 Soft Demodulation 以了解解调判决类型注意事项。

#### 依赖关系

要启用此参数，请将 **Noise variance source** 参数设置为 `Port`。

**数据类型：** `double`

### 输出

### **Out** — 解调信号 标量 | 向量

解调信号，返回为标量或向量。解调信号的维度取决于指定的 **Output type** 和 **Decision type**。此端口在模块上未命名。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### 主要

### **M-ary number** — 调制阶数 `16` (default) | 正整数

调制阶数，指定为 2 的正整数次幂。调制阶数 *M* 指定信号星座中的点数。*M* 必须具有 2*K* 的形式，其中 *K* 为某个正整数。此模块根据 **Normalization method** 参数的设置方式缩放信号星座。有关更多信息，请参阅星座大小和缩放。

### **Output type** — 输出类型 `Integer` (default) | `Bit`

确定模块生成整数还是整数的二进制表示。

- 当将 **Output type** 设置为 `Integer` 时，模块为每个符号生成范围 [0, (*M* – 1)] 内的整数。*M* 是 **M-ary number**。
- 当将 **Output type** 设置为 `Bit` 且将 **Decision type** 设置为 `Hard decision` 时，模块为每个符号生成一组 *K* 位，称为*二进制字*。*K*=log2(*M*)。
- 当将 **Output type** 设置为 `Bit` 且将 **Decision type** 设置为 `Log-likelihood ratio` 或 `Approximate log-likelihood ratio` 时，模块分别输出逐位 LLR 或近似 LLR。

### **Decision type** — 解调判决类型 `Hard decision` (default) | `Log-likelihood ratio` | `Approximate log-likelihood ratio`

解调判决类型，指定为 `Hard decision`、`Log-likelihood ratio` 或 `Approximate log-likelihood ratio`。有关算法选择注意事项，请参阅硬判决与软判决解调。

#### 依赖关系

当将 **Output type** 设置为 `Bit` 时，此参数出现。

### **Noise variance source** — 噪声方差源 `Dialog` (default) | `Port`

噪声方差源，指定为 `Dialog` 或 `Port`。

- 当选择 `Dialog` 时，必须使用 **Noise variance** 参数设置噪声方差。
- 当选择 `Port` 时，必须使用 `Var` 端口设置噪声方差。

#### 依赖关系

当将 **Decision type** 设置为 `Approximate log-likelihood ratio` 或 `Log-likelihood ratio` 时，此参数出现。

### **Noise variance** — 噪声方差 `1` (default) | 正标量 | 正值向量

噪声方差，指定为正标量或正值向量。

- 当将此参数指定为标量时，该值用于输入信号中的所有元素。
- 当将此参数指定为向量时，向量长度必须等于输入信号中的列数。每个噪声方差向量元素应用于输入信号中其对应的列。

此参数可在 normal mode、Accelerator mode 和 Rapid Accelerator mode 中调整。

如果使用 Simulink Coder™ 快速仿真（RSIM）目标构建 RSIM 可执行文件，则可以在不重新编译模型的情况下调整该参数。这对于 Monte Carlo 仿真很有用，在这种仿真中，您可以使用不同的噪声量多次运行仿真（也许在多台计算机上）。

精确 LLR 算法使用有限精度算术计算指数。对于涉及极大正值或负值的计算，精确 LLR 算法会产生：

- 如果噪声方差是非常大的值，则为 `Inf` 或 `-Inf`
- 如果噪声方差和信号功率都是非常小的值，则为 `NaN`

近似 LLR 算法不计算指数。您可以通过使用近似 LLR 算法来避免 `Inf`、`-Inf` 和 `NaN` 结果。

#### 依赖关系

要启用此参数，请将 **Decision type** 参数设置为 `Log-likelihood ratio` 或 `Approximate log-likelihood ratio`，并将 **Noise variance source** 参数设置为 `Dialog`。

### **Constellation ordering** — 符号映射顺序 `Binary` (default) | `Gray` | `User-defined`

符号映射顺序，指定为 `Gray`、`Binary` 或 `User-defined`。此参数确定模块如何将每个符号映射到一组输出位或整数。

### **Constellation mapping** — 用户定义星座映射 `[0:15]` (default) | 向量

您定义的星座映射，指定为包含范围 [0, (*M* – 1)] 内唯一整数值的 *M* 元素向量。

此向量的第一个元素对应于星座的最左上点，后续元素按列向下、从左到右排列。最后一个元素对应于最右下点。

#### 依赖关系

当将 **Constellation ordering** 设置为 `User-defined` 时，此参数出现。

### **Normalization method** — 星座缩放方法 `Min. distance between symbols` (default) | `Average Power` | `Peak Power`

星座缩放方法，指定为 `Min. distance between symbols`、`Average Power` 或 `Peak Power`。有关更多信息，请参阅星座大小和缩放

### **Minimum distance** — 两个最近星座点之间的距离 `2` (default) | 正标量

两个最近星座点之间的距离，指定为正标量。

#### 依赖关系

当将 **Normalization method** 设置为 `Min. distance between symbols` 时，此参数出现。

### **Average power, referenced to 1 ohm (watts)** — 平均功率 `1` (default) | 正标量

星座中符号的平均功率，以 watts 为单位，指定为正标量。功率值假设标称阻抗为 1 ohm。

#### 依赖关系

当将 **Normalization method** 设置为 `Average Power` 时，此参数出现。

### **Peak power, referenced to 1 ohm (watts)** — 最大功率 `1` (default) | 正标量

星座中符号的最大功率，以 watts 为单位，指定为正标量。功率值假设标称阻抗为 1 ohm。

#### 依赖关系

当将 **Normalization method** 设置为 `Peak Power` 时，此参数出现。

### **Phase offset (rad)** — 信号星座旋转 `0` (default) | 数值标量

信号星座的旋转，以 rad 为单位，指定为数值标量。

### 数据类型

### **Output data type** — 输出数据类型 `Inherit via internal rule` (default) | `Smallest unsigned integer` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `boolean`

输出数据类型，指定为 `Inherit via internal rule`、`Smallest unsigned integer`、`double`、`single`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32` 或 `boolean`。

- 当选择 `Inherit via internal rule` 时，模块根据内部规则继承数据类型。有关此规则的更多信息，请参阅 Inherit via Internal Rule。如果输入类型为 `single` 或 `double`，则输出数据类型将与输入数据类型相同。否则，输出数据类型将如同将此参数设置为 `'Smallest unsigned integer'`。
- 当此参数设置为 `'Smallest unsigned integer'` 时，模块根据模型 Configuration Parameters 对话框的 **Hardware Implementation** 窗格中使用的设置来设置输出数据类型。如果在 **Hardware Implementation** 窗格中选择 `ASIC/FPGA`，则输出数据类型为理想最小大小，即位输出为 `ufix(1)`，整数输出为 `ufix(ceil(log2(M)))`。对于所有其他选择，它是具有最小可用字长的无符号整数，该字长足够大以容纳理想最小大小，通常对应于 char 的大小（例如 `uint8`）。
- 对于整数输出，此参数可设置为 `Smallest unsigned integer`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`single` 和 `double`。对于位输出，选项为 `Smallest unsigned integer`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32`、`boolean`、`single` 或 `double`。

### **Derotate factor** — 去旋转因子数据类型 `Inherit: Same word length as input` (default) | `fixdt(1,16)` | `<data type expression>`

将去旋转因子数据类型指定为 `Inherit: Same word length as input`、`fixdt(1,16)` 或 `<data type expression>`。

有关指定数据类型的信息，请参阅 Data Type Assistant。

#### 依赖关系

此参数仅当输入为定点且 **Phase offset (rad)** 不是 π/2 的倍数时适用。

### **Denormalization factor** — 反归一化因子数据类型 `Inherit: Same word length as input` (default) | `fixdt(1,16)` | `<data type expression>`

将反归一化因子数据类型指定为 `Inherit: Same word length as input`、`fixdt(1,16)` 或 `<data type expression>`。此缩放因子派生自 **Normalization method** 和模块对话框中的其他参数值。始终使用最佳精度小数长度。

有关指定数据类型的信息，请参阅 Data Type Assistant。

#### 依赖关系

此参数仅当输入为定点且派生的反归一化因子非单位值（不等于 1）时适用。

### **Product output** — 乘积输出数据类型 `Inherit: Inherit via internal rule` (default) | `fixdt(1,16)` | `<data type expression>`

将乘积数据类型指定为 `Inherit: Inherit via internal rule`、`fixdt(1,16)` 或 `<data type expression>`。

当选择 `Inherit: Inherit via internal rule` 时，模块计算全精度乘积字长和小数长度。有关全精度 **Product output** 内部规则的信息，请参阅 Internal Rule for Product Data Types。

当定点计算的结果不能精确映射到由存储结果的数据类型和定标表示的数字时，模块使用舍入模式。有关更多信息，请参阅 Rounding Modes 或 Rounding Mode: Simplest (Fixed-Point Designer)。

有关指定数据类型的信息，请参阅 Data Type Assistant。

#### 依赖关系

此参数仅当输入为定点信号且存在非单位值（不等于 1）的反归一化因子时适用。

### **Rounding mode** — 定点运算的舍入模式 `Wrap` (default) | `Saturate`

将 **Product output** 定点运算的舍入模式指定为 `Wrap` 或 `Saturate`。当定点计算的结果不能精确映射到数据类型可表示的数字时，模块使用舍入模式。有关更多信息，请参阅 Rounding Modes 或 Rounding Mode: Simplest (Fixed-Point Designer)。

#### 依赖关系

此参数仅适用于 Product output。

### **Saturate on integer overflow** — 整数溢出时饱和的选项 `off` (default) | `on`

选中此复选框以在整数溢出时饱和。

#### 依赖关系

此参数仅适用于 Product output。

### **Sum** — 和数据类型 `Inherit: Inherit via internal rule` (default) | `Inherit: Same as product output` | `fixdt(1,16)` | `<data type expression>`

将和数据类型指定为 `Inherit: Inherit via internal rule`、`Inherit: Same as product output`、`fixdt(1,16)` 或 `<data type expression>`。

- 当选择 `Inherit: Inherit via internal rule` 时，模块基于定点 Hard Decision Algorithm 信号流图中 Sum 的两个输入计算全精度和字长及小数长度。该规则与 Sum (Simulink) 模块内部 **Accumulator data type** 参数的定点继承规则相同。
- 当选择 `Inherit: Same as product output` 且使用 **Product output** 时，模块将 **Sum** 参数的数据类型配置为与 **Product output** 数据类型相同。如果未使用 **Product output**，则忽略此设置，并使用 `Inherit: Inherit via internal rule` 和 **Sum** 参数设置。

有关指定数据类型的信息，请参阅 Data Type Assistant。

#### 依赖关系

此参数仅当输入为定点信号时适用。

## 所属库

Communications Toolbox / Modulation / Digital Baseband Modulation / AM Communications Toolbox HDL Support / Modulation / AM

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed pointa, b, c` | `integer` | `single` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
|  |  |
| --- | --- |
| a 仅方形 QAM。  b 定点输入必须为有符号。  c 当在 Hardware Implementation 窗格中选择 ASIC/FPGA 时，对于位输出，输出为 ufix(1)；对于整数输出，输出为 ufix(ceil(log2(M)))。 | |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### HDL 代码生成 使用 HDL Coder™ 为 FPGA 和 ASIC 设计生成 VHDL、Verilog 和 SystemVerilog 代码。

HDL Coder™ 提供影响 HDL 实现和综合逻辑的附加配置选项。

**HDL 架构**

此模块有一个默认 HDL 架构。

**HDL 模块属性**

|  |  |
| --- | --- |
| **ConstrainedOutputPipeline** | 通过移动设计中的现有延迟，在输出处放置的寄存器数量。分布式流水线不会重新分配这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 ConstrainedOutputPipeline (HDL Coder)。 |
| **InputPipeline** | 要在生成的代码中插入的输入流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 InputPipeline (HDL Coder)。 |
| **OutputPipeline** | 要在生成的代码中插入的输出流水线级数。分布式流水线和受约束的输出流水线可以移动这些寄存器。默认值为 `0`。有关更多详细信息，请参阅 OutputPipeline (HDL Coder)。 |

**限制**

- 此模块不支持在 HDL 代码生成中使用 `single` 或 `double` 数据类型。
- HDL Coder 支持以下 **Output type** 选项：

  - `Integer`
  - 仅当 **Decision Type** 为 `Hard decision` 时才支持 `Bit`。
- 必须将 **Normalization Method** 设置为 `Minimum Distance Between Symbols`，并将 **Minimum distance** 设置为 2。
- 必须将 **Phase offset (rad)** 设置为 `pi`/4 的倍数。

## 版本历史

**在 R2006a 之前引入**

## 描述

解调矩形 QAM 调制数据

Rectangular QAM Demodulator Baseband 模块解调使用 M 进制正交幅度调制且星座位于矩形格上的信号。

**注意**

所有功率值均假设标称阻抗为 1 ohm。
