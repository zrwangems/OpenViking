---
type: simulink-block
title: 'Vector Quantizer Encoder'
family: 'quantizers'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Quantizers'
documentation_page: 'vectorquantizerencoder'
documentation_source_path: 'ref/vectorquantizerencoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Vector Quantizer Encoder

## 端口

### 输入

### **U** — 输入数据值 向量 | 矩阵

将输入数据值指定为向量或矩阵。

数据、码本值和加权因子输入只要存在，就必须具有相同的数据类型。

如果输入是 fixed point，则它必须是带符号整数或具有 2 的幂斜率且零偏置的带符号 fixed point 值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **C** — 码本值 向量 | 矩阵

将码本值指定为 *k*×*N* 矩阵，其中 *k* ≥ 1 且 *N* ≥ 1。每个输入列向量都会与该码本进行比较。码本矩阵的每一列是一个码字，每个码字都有一个索引值。第一个码字向量对应索引值 0，第二个码字向量对应索引值 1，依此类推。

输入数据、码本值和加权因子必须具有相同的数据类型。

如果码本值是 fixed-point，则它们只能是带符号值。

#### 依赖关系

要启用此端口，请将 **Source of codebook** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **W** — 加权因子 向量

使用 **Weighting factor** 参数在计算失真度量时强调或弱化某些输入值。有关详细信息，请参阅 **Weighting factor**。

输入数据、码本值和加权因子必须具有相同的数据类型。

如果加权因子是 fixed-point，则它只能是带符号值。

#### 依赖关系

要启用此端口，请将 **Distortion measure** 参数设置为 `Weighted squared error`，并将 **Source of weighting factor** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### 输出

### **I** — 索引值 标量 | 行向量

基于欧几里得或加权欧几里得距离度量的最近码字索引值，以标量或行向量形式返回。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **Q(U)** — 输出码字 向量 | 矩阵

输出码字，以向量或矩阵形式返回。

该模块根据输入数据的数据类型分配输出码字的数据类型。如果输出码字是 fixed-point，则它只能是带符号值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### **D** — 量化误差 标量 | 行向量

量化误差，以标量或行向量形式返回。

该模块根据输入数据的数据类型分配量化误差的数据类型。如果量化误差是 fixed-point，则它只能是带符号值。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

## 参数

### 主选项卡

### **Source of codebook** — 码本来源 `Specify via dialog`（默认）| `Input port`

将码本来源指定为以下选项之一：

- `Specify via dialog` –– 在 **Codebook** 参数中指定码本值。
- `Input port` –– 通过输入端口 **C** 指定码本值。

### **Codebook** — 码本值 `[1.5 13.3 136.4 6.8 ; 2.5 14.3 137.4 7.8; 3.5 15.3 138.4 8.8]`（默认）

将码本值指定为 *k*×*N* 矩阵，其中 *k* ≥ 1 且 *N* ≥ 1。每个输入列向量都会与该码本进行比较。码本矩阵的每一列是一个码字，每个码字都有一个索引值。第一个码字向量对应索引值 0，第二个码字向量对应索引值 1，依此类推。码字向量必须与输入 **U** 具有相同的行数。

#### 依赖关系

要启用此参数，请将 **Source of codebook** 参数设置为 `Specify via dialog`。

### **Distortion measure** — 失真度量 `Squared error`（默认）| `Weighted squared error`

将失真度量指定为以下之一：

- `Squared error` –– 该模块通过计算输入列向量与码本中每个码字之间的欧几里得距离来计算失真。
- `Weighted squared error` –– 该模块通过使用加权因子计算加权欧几里得距离来计算失真，以强调或弱化某些输入值。

### **Source of weighting factor** — 加权因子的来源 `Specify via dialog`（默认）| `Input port`

将加权因子的来源指定为以下选项之一：

- `Specify via dialog` –– 在模块对话框的 **Weighting factor** 参数中指定加权因子。
- `Input port` –– 通过输入端口 **W** 指定加权因子。

#### 依赖关系

要启用此参数，请将 **Distortion measure** 参数设置为 `Weighted squared error`。

### **Weighting factor** — 加权因子 `[1 1 1]`（默认）| 向量

将加权因子指定为值的向量。此向量的长度必须等于输入 **U** 的行数。

使用 **Weighting factor** 参数在计算失真度量时强调或弱化某些输入值。例如，考虑第 *p* 个输入列向量，Up=[u1pu2p...ukp]′。当你希望忽略此向量的第一个元素的影响时，请输入 `[0 1 1 ... 1]` 作为 **Weighting factor** 参数。此加权因子用于通过以下方程计算加权平方误差：

D=∑j=1kwj(aji−ujp)2

由于此示例中使用的加权因子，加权平方误差不受输入矩阵第一个元素的影响。因此，输入列向量的第一个元素不再影响 Vector Quantizer Encoder 模块输出的索引值选择。

#### 依赖关系

要启用此参数，请将 **Source of weighting factor** 参数设置为 `Specify via dialog`。

### **Tie-breaking rule** — 平局规则 `Choose the lower index`（默认）| `Choose the higher index`

设置此参数以确定当输入列向量与两个码字等距时模块的行为。当希望输入列向量由具有较低索引值的码字表示时，选择 `Choose the lower index`。要通过具有较高索引值的码字表示输入列向量，选择 `Choose the higher index`。

### **Output codeword** — 输出码字 `off`（默认）| `on`

选中 **Output codeword** 复选框，以在端口 **Q(U)** 输出与每个索引值对应的码字向量。当输入为矩阵时，对应的码字向量会水平串联为一个矩阵。

### **Output quantization error** — 输出量化误差 `off`（默认）| `on`

选中 **Output quantization error** 复选框，以在端口 **D** 输出当模块用其最近码字表示输入列向量时产生的量化误差。当输入为矩阵时，量化误差值会水平串联。

### **Index output data type** — 索引输出数据类型 `int32`（默认）| `int8` | `uint8` | `int16` | `uint16` | `uint32` | `Inherit via back propagation`

将模块在端口 **I** 的索引输出的数据类型指定为以下之一：

- `int8`
- `uint8`
- `int16`
- `uint16`
- `int32`
- `uint32`

要继承索引输出数据类型，请选择 `Inherit via back propagation`。

### 数据类型选项卡

### **Rounding mode** — 舍入模式 `Floor`（默认）| `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将 fixed-point 运算的舍入模式指定为以下之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关详细信息，请参阅舍入模式。

### **Saturate on integer overflow** — 整数溢出时饱和 `off`（默认）| `on`

选中此参数时，模块会对其 fixed-point 运算的结果进行饱和处理。清除此参数时，模块会对其 fixed-point 运算的结果进行回绕处理。有关详细信息，请参阅 fixed-point 运算的溢出模式。

### **Product output** — 乘积输出数据类型 `Same as input`（默认）| `Binary point scaling`

如上图所示，乘法器的输出被放入乘积输出数据类型和定标中。使用此参数指定希望如何指定此乘积输出的字长和小数长度。

- 当选择 `Same as input` 时，这些特性与模块输入的特性匹配。
- 当选择 `Binary point scaling` 时，可以输入乘积输出的字长和小数长度（以位为单位）。

### **Word length** — 乘积输出字长 `16`（默认）| [2,128] 范围内的正整数

将乘积输出字长指定为 [2,128] 范围内的正整数。

#### 依赖关系

要启用此参数，请将 **Product output** 参数设置为 `Binary point scaling`。

### **Fraction length** — 乘积输出小数长度 `15`（默认）| 整数

将乘积输出小数长度指定为整数。

#### 依赖关系

要启用此参数，请将 **Product output** 参数设置为 `Binary point scaling`。

### **Accumulator** — 累加器数据类型 `Same as product output`（默认）| `Same as input` | `Binary point scaling`

如图所示，累加器的输入会被转换为累加器数据类型。当输入的每个元素被加到其上时，加法器的输出保持为累加器数据类型。使用此参数指定希望如何指定累加器的字长和小数长度。

- 当选择 `Same as product output` 时，这些特性与乘积输出的特性匹配。
- 当选择 `Same as input` 时，这些特性与模块输入的特性匹配。
- 当选择 `Binary point scaling` 时，可以输入累加器的字长和小数长度（以位为单位）。

### **Word length** — 累加器字长 `16`（默认）| [2,128] 范围内的正整数

将累加器字长指定为 [2,128] 范围内的正整数。

#### 依赖关系

要启用此参数，请将 **Accumulator** 参数设置为 `Binary point scaling`。

### **Fraction length** — 累加器小数长度 `15`（默认）| 整数

将累加器小数长度指定为整数。

#### 依赖关系

要启用此参数，请将 **Accumulator** 参数设置为 `Binary point scaling`。

## 所属库

DSP System Toolbox / Quantizers

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

在某些条件下，生成的代码依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

## 版本历史

**R2006a 之前引入**

## 描述

基于欧几里得或加权欧几里得距离度量的最近码字索引

Vector Quantizer Encoder 模块将每个输入列向量与码本矩阵中的码字向量进行比较。此码本矩阵的每一列是一个码字。该模块找到最接近输入列向量的码字向量，并返回其从零开始的索引。此模块在所有输入端口上支持实数浮点和定点信号。

Vector Quantizer Encoder 模块接受实数浮点和定点输入。有关详细信息，请参阅 **端口** 部分。
