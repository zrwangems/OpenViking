---
type: simulink-block
title: 'MIL-188 QAM Demodulator Baseband'
family: 'modulation'
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

### **In** — MIL-STD-188 标准特定 QAM 调制信号 标量 | 向量 | 矩阵

MIL-STD-188 标准特定 QAM 调制信号，指定为标量、向量或矩阵。当此输入为矩阵时，每一列被视为一个独立通道。在启用 `Var` 端口之前，此端口未命名。

**数据类型：** `double` | `single`
**复数支持：** Yes

### **Var** — 噪声方差 正标量 | 正值向量

噪声方差，指定为正标量或正值向量。当噪声方差或信号功率导致涉及极大正值或负值的计算时，有关解调判决类型注意事项，请参阅 MIL-STD-188-110 QAM Soft Demodulation。

#### 依赖关系

要启用此端口，请将 **噪声方差源** 参数设置为 `Input port`。

### 输出

### **Out** — 解调信号 标量 | 向量 | 矩阵

解调信号，以标量、向量或矩阵形式返回。解调信号的维度取决于指定的 **输出类型** 和 **判决类型** 参数值。此端口在模块上未命名。

| **输出类型** | **判决类型** | 解调信号描述 | **解调信号的维度** |
| --- | --- | --- | --- |
| `Integer` | — | 范围为 [0, (*M* – 1)] 的解调整数值 | 输出信号与输入信号具有相同的维度。 |
| `Bit` | `Hard decision` | 解调比特 | 输出信号中的行数是输入信号中行数的 log2(*M*) 倍。每个解调符号映射到一列中的一组 log2(*M*) 个元素，其中第一个元素表示 MSB，最后一个元素表示 LSB。 |
| `Log-likelihood ratio` | 每个比特的对数似然比值 |
| `Approximate log-likelihood ratio` | 每个比特的近似对数似然比值 |
| *M* 是 **调制阶数** 的值。 | | | |

使用 **输出数据类型** 指定输出数据类型。

## 参数

要以交互方式编辑模块参数，请使用属性检查器。在 Simulink® 工具条的 **仿真** 选项卡上，在 **准备** 库中选择 **属性检查器**。

### **调制阶数** — 调制阶数 `16` (默认) | `32` | `64` | `256`

调制阶数 *M*，指定为 `16`、`32`、`64` 或 `256`。调制阶数指定输入信号星座中的总点数。

### **星座缩放** — 星座缩放 `As specified in standard` (默认) | `Unit average power`

星座缩放，指定为：

- `As specified in standard` – 模块根据相关标准 [1] 中的规范缩放星座。
- `Unit average power` – 模块将星座缩放为参考于 1 ohm 的平均功率 1 watt。

### **输出类型** — 输入类型 `Integer` (默认) | `Bit`

输出类型，指定为 `Integer` 或 `Bit`。要使用 `Integer`，输入信号必须由范围为 [0, (*M* – 1)] 的整数组成。要使用 `Bit`，输入信号必须包含二进制值，并且行数必须是 log2(*M*) 的整数倍，其中 *M* 是 **调制阶数**。

### **判决类型** — 解调判决类型 `Hard decision` (默认) | `Log-likelihood ratio` | `Approximate log-likelihood ratio`

解调判决类型，指定为 `Hard decision`、`Log-likelihood ratio` 或 `Approximate log-likelihood ratio`。有关算法选择注意事项，请参阅 MIL-STD-188-110 QAM Soft Demodulation。

#### 依赖关系

当您将 **输出类型** 设置为 `Bit` 时，此参数适用。

### **噪声方差源** — 噪声方差源 `Property` (默认) | `Input port`

噪声方差源，指定为：

- `Property` — 使用噪声方差参数设置噪声方差。
- `Input port` — 使用 **Var** 输入端口设置噪声方差。

#### 依赖关系

当您将 **判决类型** 设置为 `Log-likelihood ratio` 或 `Approximate log-likelihood ratio` 时，此参数适用。

### **噪声方差** — 噪声方差 `1` (默认) | 正标量 | 正值向量

噪声方差，指定为正标量或正值向量。

- 当指定为标量时，该值用于输入信号中的所有元素。
- 当指定为向量时，向量长度必须等于输入信号中的列数。每个噪声方差向量元素应用于输入信号中的对应列。

当噪声方差或信号功率导致涉及极大正值或负值的计算时，有关解调判决类型注意事项，请参阅 MIL-STD-188-110 QAM Soft Demodulation。

#### 依赖关系

当您将 **噪声方差** 设置为 `Property`，并将 **判决类型** 设置为 `Log-likelihood ratio` 或 `Approximate log-likelihood ratio` 时，此参数适用。

### **输出数据类型** — 输出数据类型 `double` (默认) | `...`

输出数据类型，指定为此表中可接受的值之一。可接受的 **输出数据类型** 值取决于 **输出类型** 和 **判决类型** 参数值。

| **输出类型** | **判决类型** | **输出数据类型** 选项 |
| --- | --- | --- |
| `Integer` | 不适用 | `double`, `single`, `int8`, `uint8`, `int16`, `uint16`, `int32`, 或 `uint32` |
| `Bit` | `Hard decision` | `double`, `single`, `int8`, `uint8`, `int16`, `uint16`, `int32`, `uint32`, 或 `logical` |
| `Log-likelihood ratio` 或 `Approximate log-likelihood ratio` | 输出信号与输入信号具有相同的数据类型。 |

#### 依赖关系

当您将 **输出类型** 设置为 `Integer`，或者将 **输出类型** 设置为 `Bit` 并将 **判决类型** 设置为 `Hard decision` 时，此参数适用。

### **仿真方式** — 要运行的仿真类型 `Interpreted execution` (默认) | `Code generation`

要运行的仿真类型，指定为 `Interpreted execution` 或 `Code generation`。

- `Interpreted execution` — 使用 MATLAB® 解释器仿真模型。此选项需要的启动时间较短，但后续仿真速度比 `Code generation` 选项慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码仿真模型。首次运行仿真时，Simulink 会为模块生成 C 代码。除非模型发生变化，否则模型会为后续仿真重用该 C 代码。此选项需要额外的启动时间，但后续仿真速度比 `Interpreted execution` 选项快。

有关详细信息，请参阅 Interpreted Execution vs. Code Generation (Simulink)。

## 所属库

Communications Toolbox / Modulation / Digital Baseband Modulation / AM Communications Toolbox / Modulation / Digital Baseband Modulation / Standard-Compliant

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

## 描述

MIL-STD-188-110 B/C 标准特定的正交幅度解调

MIL-188 QAM Demodulator Baseband 模块使用 MIL-STD-188-110 标准特定的正交幅度调制 (QAM) 解调输入信号。有关 MIL-STD-188 兼容解调的说明，请参阅 MIL-STD-188-110 QAM Hard Demodulation 和 MIL-STD-188-110 QAM Soft Demodulation。

此图标显示启用了所有端口的模块：
