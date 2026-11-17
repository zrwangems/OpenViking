---
type: simulink-block
title: 'M-APSK Demodulator Baseband'
family: 'modulation'
product_id: 'comm'
product_name: 'Communications Toolbox'
documentation_release: R2025b
official_category: 'Modulation / Digital Baseband Modulation / APSK'
documentation_page: 'mapskdemodulatorbaseband'
documentation_source_path: 'ref/mapskdemodulatorbaseband.html'
language: zh-CN
chinese_source: worker-translation
---

# M-APSK Demodulator Baseband

## 端口

### 输入

### **In** — APSK 调制信号 标量 | 向量 | 矩阵

APSK 调制信号，指定为标量、向量或矩阵。当此输入为矩阵时，每一列被视为一个独立通道。在启用 `Var` 端口之前，此端口未命名。

**数据类型：** `double` | `single`
**复数据支持：** Yes

### **Var** — 噪声方差 正标量 | 正数值向量

噪声方差，指定为正标量或正数值向量。当噪声方差或信号功率导致涉及极端正或负幅度的计算时，有关解调判决类型注意事项，请参阅 APSK 软解调。

#### 依赖关系

要启用此端口，请将 **噪声方差源** 设置为 `Input port`。

**数据类型：** `double` | `single`
### 输出

### **Out** — 解调信号 标量 | 向量 | 矩阵

解调信号，返回为标量、向量或矩阵。解调信号的数据类型和维度取决于 **输出类型** 和 **判决类型** 参数指定的值。此端口在模块上未命名。

| **输出类型** | **判决类型** | 解调信号描述 | 解调信号维度 |
| --- | --- | --- | --- |
| `Integer` | — | 解调后的整数值，范围 [0, (*M* – 1)] | 输出信号与输入信号具有相同的维度。 |
| `Bit` | `Hard decision` | 解调后的比特 | 输出信号的行数是输入信号行数的 log2(*M*) 倍。每个解调符号映射到一列中的一组 log2(*M*) 个元素，其中第一个元素表示 MSB，最后一个元素表示 LSB。 |
| `Log-likelihood ratio` | 每个比特的对数似然比值 |
| `Approximate log-likelihood ratio` | 每个比特的近似对数似然比值 |
| *M* 是 M-APSK 的调制阶数。 | | | |

使用 **输出数据类型** 指定输出数据类型。

**数据类型：** `single` | `double`

## 参数

要交互式编辑模块参数，请使用 Property Inspector。在 Simulink® 工具条的 **Simulation** 选项卡上的 **Prepare** 库中，选择 **Property Inspector**。

### **每个圆的星座点数** — 每个 PSK 环的星座点数 `[4,12]` (默认) | 向量

每个 PSK 环的星座点数，指定为包含多个元素的向量。每个向量元素表示其对应 PSK 环中的星座点数。第一个元素对应最内圆，依此类推，直到最后一个元素对应最外圆。**每个圆的星座点数** 中元素的总和确定调制阶数。元素值必须是四的倍数，并且调制阶数必须是 2 的幂。

**示例：** `[4,12,16]` 指定一个三 PSK 环星座，调制阶数为 32。

### **每个圆的半径** — 每个 PSK 环的半径 `[0.5,1]` (默认) | 向量

每个 PSK 环的半径，指定为与 **每个圆的星座点数** 长度相同的向量。每个向量元素表示其对应 PSK 环的半径。第一个元素对应最内圆，依此类推，直到最后一个元素对应最外圆。这些元素值必须是按递增顺序排列的正值。

**示例：** `[0.5,1,2]` 定义三个星座 PSK 环的半径。内环半径为 0.5，第二个环半径为 1.0，外环半径为 2.0。

### **每个圆的相位偏移 (rad)** — 每个 PSK 环的相位偏移 `[pi/4,pi/12]` (默认) | 标量 | 向量

每个 PSK 环的相位偏移（以弧度为单位），指定为标量或与 **每个圆的星座点数** 长度相同的向量。每个向量元素表示其对应 PSK 环的相位偏移。第一个元素对应最内圆，依此类推，直到最后一个元素对应最外圆。仅当 **每个圆的星座点数** 的所有元素都相同时，**每个圆的相位偏移 (rad)** 才可以是标量。

**示例：** `[pi/4,pi/12,pi/16]` 定义三个星座 PSK 环的相位偏移。内环相位偏移为 π/4，第二个环相位偏移为 π/12，外环相位偏移为 π/16。

### **符号映射** — 符号映射 `Auto` (默认) | `Contourwise-gray` | `Gray` | `User-defined`

符号映射，指定为以下之一：

- `Contourwise-gray` — 在每个 PSK 环的相位维度上沿轮廓使用格雷映射。
- `Gray` — 在幅度和相位维度上沿轮廓使用格雷映射。对于 Gray 符号映射，**每个圆的星座点数** 中的所有元素必须相等，并且 **每个圆的相位偏移 (rad)** 中的所有元素必须相等。有关所用 Gray 映射的描述，请参阅 [2]。
- `User-defined` — 请参阅 **自定义符号映射**。

默认符号映射取决于 **每个圆的星座点数** 和 **每个圆的相位偏移 (rad)** 参数。当 **每个圆的星座点数** 中的所有元素相等，并且 **每个圆的相位偏移 (rad)** 中的所有元素相等时，默认为 `Gray`。对于所有其他情况，默认为 `Contourwise-gray`。

### **自定义符号映射** — 自定义符号映射 `[0,4,12,8,1,3,2,6,7,5,13,15,14,10,11,9]` (默认) | 整数向量

自定义符号映射，指定为整数向量。此向量必须由 *M* 个唯一元素组成，值在范围 [0, (*M* – 1)] 内，其中 *M* 是 M-APSK 的调制阶数。**自定义符号映射** 中的第一个元素对应最内圆第一象限中的星座点，后续元素沿 PSK 环逆时针定位。

**示例：** 默认值 `[0,4,12,8,1,3,2,6,7,5,13,15,14,10,11,9]` 指定 contourwise-gray 符号映射。星座点的分布在所有轮廓上都是非均匀的。

#### 依赖关系

要启用此参数，请将 **符号映射** 设置为 `User-defined`。

### **输出类型** — 输出类型 `Integer` (默认) | `Bit`

输出类型，指定为 `Integer` 或 `Bit`。

### **判决类型** — 解调判决类型 `Hard decision` (默认) | `Log-likelihood ratio` | `Approximate log-likelihood ratio`

解调判决类型，指定为 `Hard decision`、`Log-likelihood ratio` 或 `Approximate log-likelihood ratio`。有关算法选择注意事项，请参阅 APSK 软解调。

#### 依赖关系

仅当 **输出类型** 设置为 `Bit` 时，此参数才适用。

### **噪声方差源** — 噪声方差源 `Property` (默认) | `Input port`

噪声方差源，指定为：

- `Property` — 使用 **噪声方差** 参数设置噪声方差。
- `Input port` — 使用 **Var** 输入端口设置噪声方差。

#### 依赖关系

仅当 **判决类型** 设置为 `Log-likelihood ratio` 或 `Approximate log-likelihood ratio` 时，此参数才适用。

### **噪声方差** — 噪声方差 `1` (默认) | 正标量 | 正数值向量

噪声方差，指定为正标量或正数值向量。

- 当指定为标量时，该值用于输入信号中的所有元素。
- 当指定为向量时，向量长度必须等于输入信号的列数。每个噪声方差向量元素应用于输入信号中其对应的列。

当噪声方差或信号功率导致涉及极端正或负幅度的计算时，有关 **判决类型** 指定注意事项，请参阅 APSK 软解调。

#### 依赖关系

仅当 **噪声方差源** 设置为 `Property`，并且 **判决类型** 设置为 `Log-likelihood ratio` 或 `Approximate log-likelihood ratio` 时，此参数才适用。

### **输出数据类型** — 输出数据类型 `double` (默认) | `...`

输出数据类型，指定为此表中的一个可接受值。可接受的 **输出数据类型** 值取决于 **输出类型** 和 **判决类型** 参数值。

| **输出类型** | **判决类型** | **输出数据类型** 选项 |
| --- | --- | --- |
| `Integer` | 不适用 | `double`, `single`, `int8`, `uint8`, `int16`, `uint16`, `int32`, or `uint32` |
| `Bit` | `Hard decision` | `double`, `single`, `int8`, `uint8`, `int16`, `uint16`, `int32`, `uint32`, or `logical` |
| `Log-likelihood ratio` 或 `Approximate log-likelihood ratio` | 输出信号与输入信号的数据类型相同。 |

#### 依赖关系

仅当 **输出类型** 设置为 `Integer`，或 **输出类型** 设置为 `Bit` 且 **判决类型** 设置为 `Hard decision` 时，此参数才适用。

### **模拟使用** — 要运行的模拟类型 `Interpreted execution` (默认) | `Code generation`

要运行的模拟类型，指定为 `Interpreted execution` 或 `Code generation`。

- `Interpreted execution` — 使用 MATLAB® 解释器模拟模型。此选项需要较少的启动时间，但后续模拟的速度比使用 `Code generation` 选项慢。在此模式下，您可以调试模块的源代码。
- `Code generation` — 使用生成的 C 代码模拟模型。第一次运行模拟时，Simulink 会为该模块生成 C 代码。除非模型更改，否则模型会在后续模拟中重用该 C 代码。此选项需要额外的启动时间，但后续模拟的速度比使用 `Interpreted execution` 选项快。

有关详细信息，请参阅解释执行与代码生成 (Simulink)。

## 所属库

Communications Toolbox / Modulation / Digital Baseband Modulation / APM

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

M 进制幅相键控 (APSK) 解调

M-APSK Demodulator Baseband 模块解调 *M* 进制幅相键控 (APSK) 调制信号的基带表示。*M* 是 M-APSK 的调制阶数。有关 *M*-APSK 解调的描述，请参阅 APSK 硬解调和 APSK 软解调。

**注意**

M-APSK Demodulator Baseband 专门适用于多环 PSK 星座。对于单环 PSK 星座，请使用 M-PSK Demodulator Baseband。

此图标显示了启用所有端口后的模块：
