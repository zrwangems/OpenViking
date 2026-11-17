---
type: simulink-block
title: 'DVBS-APSK Demodulator Baseband'
family: 'modulation'
product_id: 'satcom'
product_name: 'Satellite Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation'
documentation_page: 'dvbsapskdemodulatorbaseband'
documentation_source_path: 'ref/dvbsapskdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# DVBS-APSK Demodulator Baseband

## 端口

### 输入

### **In** — DVB-S2/S2X/SH 标准专用 APSK 调制信号 标量 | 向量 | 矩阵

DVB-S2/S2X/SH 标准专用 APSK 调制信号，指定为标量、向量或矩阵。当此输入为矩阵时，每一列视为一个独立信道。在启用 `Var` 端口之前，此端口未命名。

**数据类型：** `double` | `single`
**复数支持：** Yes

### **Var** — 噪声方差 正标量 | 正值向量

噪声方差，指定为正标量或正值向量。当噪声方差或信号功率导致涉及极大正负幅度的计算时，请参阅符合 DVB 的 APSK 软解调以了解解调判决类型注意事项。

#### 依赖关系

当 **Noise variance source** 设置为 `Input port` 时，此参数适用。

**数据类型：** `double` | `single`

### 输出

### **Out** — 解调信号 标量 | 向量 | 矩阵

解调信号，返回为标量、向量或矩阵。解调信号的维度取决于指定的 **Output type** 和 **Decision type**。此端口在模块上未命名。

| **Output type** | **Decision type** | **解调信号描述** | **解调信号维度** |
| --- | --- | --- | --- |
| `Integer` | — | 范围 [0, (*M* – 1)] 内的解调整数值 | 输出信号与输入信号具有相同的维度。 |
| `Bit` | `Hard decision` | 解调后的比特 | 输出信号的行数是输入信号行数的 log2(*M*) 倍。每个解调符号映射到某一列中一组 log2(*M*) 个元素，其中第一个元素表示 MSB，最后一个元素表示 LSB。 |
| `Log-likelihood ratio` | 每个比特的对数似然比值 |
| `Approximate log-likelihood ratio` | 每个比特的近似对数似然比值 |
| *M* 是 **Modulation order** 的值。 | | | |

使用 **Output data type** 指定输出数据类型。

## 参数

要以交互方式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **DVB standard suffix** — 标准后缀 `S2` | `S2X` | `SH`

用于 DVB 调制变体的标准后缀，指定为 `S2`、`S2X` 或 `SH`。

### **Frame length** — 帧长度 `Normal`（默认） | `Short`

帧长度，指定为 `Normal` 或 `Short`。

#### 依赖关系

此参数仅在 **DVB standard suffix** 设置为 `S2` 或 `S2X` 时适用。

### **Modulation order** — 调制阶数 `16`（默认） | integer

调制阶数，指定为 2 的幂。调制阶数指定输入信号星座中的总点数。有效的调制阶数列表取决于 **DVB standard suffix** 和 **Frame length** 的设置。

| **DVB standard suffix** | **Frame length** | **Modulation order** 选项 |
| --- | --- | --- |
| `S2` | `Normal` 或 `Short` | `16` 或 `32` |
| `S2X` | `Normal` | `8`、`16`、`32`、`64` 或 `256` |
| `Short` | `16` 或 `32` |
| `SH` | 不适用 | `16` |

### **Code identifier** — 码标识符 `2/3` | character vector

码标识符，指定为字符向量。有效的码标识符值列表取决于 **DVB standard suffix**、**Frame length** 和 **Modulation order** 的设置。此表列出了 **Code identifier** 值的可用选项。

| **Modulation order** | **DVB standard suffix** | **Frame length** | **Code identifier** 选项 |
| --- | --- | --- | --- |
| `8` | `S2X` | `Normal` | `100/180` 或 `104/180` |
| `16` | `S2` 或 `S2X` | `Normal` | `2/3`、`3/4`、`4/5`、`5/6`、`8/9` 或 `9/10` |
| `Short` | `2/3`、`3/4`、`4/5`、`5/6` 或 `8/9` |
| `16` | `S2X` | `Normal` | `26/45`、`3/5`、`28/45`、`23/36`、`25/36`、`13/18`、`140/180`、`154/180`、`100/180`、`96/180`、`90/180`、`18/30` 或 `20/30` |
| `Short` | `7/15`、`8/16`、`26/45`、`3/5` 或 `32/45` |
| `32` | `S2` 或 `S2X` | `Normal` | `3/4`、`4/5`、`5/6`、`8/9` 或 `9/10` |
| `Short` | `3/4`、`4/5`、`5/6` 或 `8/9` |
| `32` | `S2X` | `Normal` | `128/180`、`132/180`、`140/180` 或 `2/3` |
| `Short` | `2/3` 或 `32/45` |
| `64` | `S2X` | `Normal` | `128/180`、`132/180`、`7/9`、`4/5` 或 `5/6` |
| `128` | `S2X` | `Normal` | `135/180` 或 `140/180` |
| 256 | `S2X` | `Normal` | `116/180`、`124/180`、`128/180`、`20/30` 或 `135/180` |

有关更多信息，请参阅 DVB-S2 标准 [1] 中的表 9 和表 10，以及 DVB-S2X 标准 [2] 中的表 17a。

#### 依赖关系

此参数仅在 **DVB standard suffix** 设置为 `S2` 或 `S2X` 时适用。

### **Constellation scaling** — 星座缩放 `Outer radius as 1`（默认） | `Unit average power`

星座缩放，指定为 `Outer radius as 1` 或 `Unit average power`。

#### 依赖关系

此输入参数仅在 **DVB standard suffix** 设置为 `S2` 或 `S2X` 时适用。

### **Output type** — 输出类型 `Integer`（默认） | `Bit`

输出类型，指定为 `Integer` 或 `Bit`。

### **Decision type** — 解调判决类型 `Hard decision`（默认） | `Log-likelihood ratio` | `Approximate log-likelihood ratio`

解调判决类型，指定为 `Hard decision`、`Log-likelihood ratio` 或 `Approximate log-likelihood ratio`。有关算法选择注意事项，请参阅符合 DVB 的 APSK 软解调。

#### 依赖关系

当 **Output type** 设置为 `Bit` 时，此参数适用。

### **Noise variance source** — 噪声方差源 `Property`（默认） | `Input port`

噪声方差源，指定为：

- `Property` — 使用 **Noise variance** 参数设置噪声方差。
- `Input port` — 使用 **Var** 输入端口设置噪声方差。

### **Noise variance** — 噪声方差 `1`（默认） | 正标量 | 正值向量

噪声方差，指定为正标量或正值向量。

- 当指定为标量时，该值用于输入信号中的所有元素。
- 当指定为向量时，向量长度必须等于输入信号的列数。每个噪声方差向量元素应用于输入信号中的对应列。

当噪声方差或信号功率导致涉及极大正负幅度的计算时，请参阅符合 DVB 的 APSK 软解调以了解解调判决类型注意事项。

#### 依赖关系

当 **Noise variance source** 设置为 `Property` 且 **Decision type** 设置为 `Log-likelihood ratio` 或 `Approximate log-likelihood ratio` 时，此参数适用。

### **Output data type** — 输出数据类型 `double`（默认） | `...`

输出数据类型，指定为此表中可接受的值之一。可接受的 **Output data type** 值取决于 **Output type** 和 **Decision type** 参数值。

| **Output type** | **Decision type** | **Output data type** 选项 |
| --- | --- | --- |
| `Integer` | 不适用 | `double`、`single`、`int8`、`uint8`、`int16`、`uint16`、`int32` 或 `uint32` |
| `Bit` | `Hard decision` | `double`、`single`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32` 或 `logical` |
| `Log-likelihood ratio` 或 `Approximate log-likelihood ratio` | 输出信号与输入信号具有相同的数据类型。 |

#### 依赖关系

此参数仅在 **Output type** 设置为 `Integer` 时适用，或者当 **Output type** 设置为 `Bit` 且 **Decision type** 设置为 `Hard decision` 时适用。

### **Simulate using** — 要运行的仿真类型 `Code generation`（默认） | `Interpreted execution`

要运行的仿真类型，指定为 `Code generation` 或 `Interpreted execution`。

- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为模块生成 C 代码。除非模型更改，否则模型在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比使用 `Interpreted execution` 选项更快。
- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项可缩短启动时间，但后续仿真的速度比使用 `Code generation` 选项更慢。在此模式下，可以调试模块的源代码。

## 所属库

Satellite Communications Toolbox / Modulation / Digital Baseband Modulation

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `integer` | `single` |
| **多维信号** | `yes` |
| **可变大小信号** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

### R2024b：从 Communications Toolbox 移至 Satellite Communications Toolbox

以前，`DVBS-APSK Demodulator Baseband` 需要 Communications Toolbox™。

## 描述

DVB-S2/S2X/SH 标准专用 APSK 解调

DVBS-APSK Demodulator Baseband 模块使用数字视频广播（DVB-S2/S2X/SH）标准专用幅相键控（APSK）解调对输入信号进行解调。

此图标显示所有端口均已启用的模块：已启用所有端口的 DVBS-APSK Demodulator Baseband 模块图标
