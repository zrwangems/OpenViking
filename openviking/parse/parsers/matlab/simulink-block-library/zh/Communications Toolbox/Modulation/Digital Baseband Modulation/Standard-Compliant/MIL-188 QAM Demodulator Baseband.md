---
type: simulink-block
title: 'MIL-188 QAM Demodulator Baseband'
family: 'comm'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / PAM/QAM'
documentation_page: 'mil188qamdemodulatorbaseband'
documentation_source_path: 'ref/mil188qamdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# MIL-188 QAM Demodulator Baseband

## 端口

### 输入

### **In** — MIL-STD-188 标准特定的 QAM 调制信号 标量 | 向量 | 矩阵

MIL-STD-188 标准特定的 QAM 调制信号，指定为标量、向量或矩阵。当此输入为矩阵时，每一列被视为一个独立通道。在启用 `Var` 端口之前，此端口未命名。

**数据类型：** `double` | `single`
**复数支持：** 是

### **Var** — 噪声方差 正标量 | 正值向量

噪声方差，指定为正标量或正值向量。当噪声方差或信号功率导致涉及极端正负幅度的计算时，请参阅 MIL-STD-188-110 QAM 软解调以了解解调判决类型注意事项。

#### 依赖关系

要启用此端口，请将 **Noise variance source** 参数设置为 `Input port`。
### 输出

### **Out** — 解调信号 标量 | 向量 | 矩阵

解调信号，返回为标量、向量或矩阵。解调信号的维度取决于指定的 **Output type** 和 **Decision type** 参数值。此端口在模块上未命名。

| **Output type** | **Decision type** | 解调信号描述 | **解调信号的维度** |
| --- | --- | --- | --- |
| `Integer` | — | 范围为 [0, (*M* – 1)] 的解调整数值 | 输出信号与输入信号具有相同的维度。 |
| `Bit` | `Hard decision` | 解调比特 | 输出信号的行数是输入信号行数的 log2(*M*) 倍。每个解调符号映射到一列中的一组 log2(*M*) 个元素，其中第一个元素表示 MSB，最后一个元素表示 LSB。 |
| `Log-likelihood ratio` | 每个比特的对数似然比值 |
| `Approximate log-likelihood ratio` | 每个比特的近似对数似然比值 |
| *M* 是 **Modulation order** 的值。 | | | |

使用 **Output data type** 指定输出数据类型。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **Simulation** 选项卡上，在 **Prepare** 库中选择 **Property Inspector**。

### **Modulation order** — 调制阶数 `16`（默认）| `32` | `64` | `256`

调制阶数 *M*，指定为 `16`、`32`、`64` 或 `256`。调制阶数指定输入信号星座图中的总点数。

### **Constellation scaling** — 星座图缩放 `As specified in standard`（默认）| `Unit average power`

星座图缩放，指定为：

- `As specified in standard` – 模块根据相关标准中的规范缩放星座图 [1]。
- `Unit average power` – 模块将星座图缩放至参考 1 欧姆的平均功率 1 瓦。

### **Output type** — 输入类型 `Integer`（默认）| `Bit`

输出类型，指定为 `Integer` 或 `Bit`。要使用 `Integer`，输入信号必须由范围 [0, (*M* – 1)] 内的整数组成。要使用 `Bit`，输入信号必须包含二进制值，并且行数必须是 log2(*M*) 的整数倍，其中 *M* 是 **Modulation order**。

### **Decision type** — 解调判决类型 `Hard decision`（默认）| `Log-likelihood ratio` | `Approximate log-likelihood ratio`

解调判决类型，指定为 `Hard decision`、`Log-likelihood ratio` 或 `Approximate log-likelihood ratio`。有关算法选择注意事项，请参阅 MIL-STD-188-110 QAM 软解调。

#### 依赖关系

当您将 **Output type** 设置为 `Bit` 时，此参数适用。

### **Noise variance source** — 噪声方差源 `Property`（默认）| `Input port`

噪声方差源，指定为：

- `Property` — 使用 Noise variance 参数设置噪声方差。
- `Input port` — 使用 **Var** 输入端口设置噪声方差。

#### 依赖关系

当您将 **Decision type** 设置为 `Log-likelihood ratio` 或 `Approximate log-likelihood ratio` 时，此参数适用。

### **Noise variance** — 噪声方差 `1`（默认）| 正标量 | 正值向量

噪声方差，指定为正标量或正值向量。

- 当指定为标量时，该值用于输入信号中的所有元素。
- 当指定为向量时，向量长度必须等于输入信号的列数。每个噪声方差向量元素应用于输入信号中对应的列。

当噪声方差或信号功率导致涉及极端正负幅度的计算时，请参阅 MIL-STD-188-110 QAM 软解调以了解解调判决类型注意事项。

#### 依赖关系

当您将 **Noise variance** 设置为 `Property` 并将 **Decision type** 设置为 `Log-likelihood ratio` 或 `Approximate log-likelihood ratio` 时，此参数适用。

### **Output data type** — 输出数据类型 `double`（默认）| `...`

输出数据类型，指定为此表中的可接受值之一。可接受的 **Output data type** 值取决于 **Output type** 和 **Decision type** 参数值。

| **Output type** | **Decision type** | **Output data type** 选项 |
| --- | --- | --- |
| `Integer` | 不适用 | `double`、`single`、`int8`、`uint8`、`int16`、`uint16`、`int32` 或 `uint32` |
| `Bit` | `Hard decision` | `double`、`single`、`int8`、`uint8`、`int16`、`uint16`、`int32`、`uint32` 或 `logical` |
| `Log-likelihood ratio` 或 `Approximate log-likelihood ratio` | 输出信号与输入信号具有相同的数据类型。 |

#### 依赖关系

当您将 **Output type** 设置为 `Integer`，或将 **Output type** 设置为 `Bit` 并将 **Decision type** 设置为 `Hard decision` 时，此参数适用。

### **Simulate using** — 要运行的仿真类型 `Interpreted execution`（默认）| `Code generation`

要运行的仿真类型，指定为 `Interpreted execution` 或 `Code generation`。

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项需要较少的启动时间，但后续仿真的速度比 `Code generation` 选项慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为该模块生成 C 代码。除非模型发生变化，否则模型会在后续仿真中重用该 C 代码。此选项需要额外的启动时间，但后续仿真的速度比 `Interpreted execution` 选项快。

有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。

## 所属库

Communications Toolbox / Modulation / Digital Baseband Modulation / AM Communications Toolbox / Modulation / Digital Baseband Modulation / Standard-Compliant

## 模块特性

|  |  |
| --- | --- |
| **Data Types** | `Boolean` | `double` | `integer` | `single` |
| **Multidimensional Signals** | `yes` |
| **Variable-Size Signals** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2018b 中引入**

## 描述

MIL-STD-188-110 B/C 标准特定的正交幅度解调

MIL-188 QAM Demodulator Baseband 模块使用 MIL-STD-188-110 标准特定的正交幅度调制 (QAM) 对输入信号进行解调。有关符合 MIL-STD-188 的解调的描述，请参阅 MIL-STD-188-110 QAM 硬解调和 MIL-STD-188-110 QAM 软解调。

此图标显示了启用所有端口的模块：
