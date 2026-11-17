---
type: simulink-block
title: 'Vector Quantizer Decoder'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Quantizers'
documentation_page: 'vectorquantizerdecoder'
documentation_source_path: 'ref/vectorquantizerdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Vector Quantizer Decoder

## 端口

### 输入

### **I** — 索引值 标量 | 行向量

将索引值指定为范围在 0 ≤ *index* < *N* 内的标量或行向量，其中 *N* 是码本矩阵的列数。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **C** — 码本值 向量 | 矩阵

将码本值指定为向量或矩阵，

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
### 输出

### **Q(U)** — 量化输出值 行向量 | 矩阵

量化输出值，以向量或矩阵形式返回。

这些量化输出值始终与码本值具有相同的数据类型。当您通过输入端口指定码本值时，模块会为 **Q(U)** 输出端口分配相同的数据类型。当您通过对话框指定码本值时，使用 **Codebook and output data type** 参数来指定 **Q(U)** 输出端口的数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

## 参数

### 主选项卡

### **Action for out of range index value** — 超出范围索引值的操作 `Clip`（默认）| `Clip and warn` | `Error`

指定当输入索引值超出范围时采取的操作，其中 0 ≤ *index* < *N*，*N* 是码本向量的长度（或码本矩阵的列数）。

当您希望将任何小于 0 的索引值设置为 0，并将任何大于或等于 *N* 的索引值设置为 *N*−1 时，选择 `Clip`。选择 `Clip and warn` 以在模块将任何小于 0 的索引值设置为 0 并将任何大于或等于 *N* 的索引值设置为 *N*−1 时发出警告。选择 `Error` 以在索引值超出范围时停止仿真并显示错误。

### **Source of codebook** — 码本来源 `Specify via dialog`（默认）| `Input port`

将码本值的来源指定为以下选项之一：

- `Specify via dialog` —— 在 **Codebook values** 参数中指定码本值。
- `Input port` —— 通过输入端口 **C** 指定码本值。

### **Codebook values** — 码本值 `[1.5 13.3 136.4 6.8; 2.5 14.3 137.4 7.8; 3.5 15.3 138.4 8.8]`（默认）

将码本值指定为 *k*×*N* 的量化输出值矩阵，其中 *k* ≥ 1 且 *N* ≥ 1。该矩阵的每一列是一个码字向量，每个码字向量对应一个索引值。索引值从零开始。第一个码字向量对应索引值 0，第二个码字向量对应索引值 1，依此类推。

#### 依赖关系

要启用此参数，请将 **Source of codebook** 参数设置为 `Specify via dialog`。

### 数据类型选项卡

### **Codebook and output data type** — 码本和输出数据类型 `double`（默认）| `Inherit: Inherit via back propagation` | `Inherit: Same as input` | `single` | `fixdt(1,16)` | `fixdt(1,16,0)`

指定码本和量化输出值的数据类型。您可以选择以下之一：

- 继承数据类型的规则，例如 `Inherit: Same as input`。
- 内置数据类型，例如 `double`
- 求值为有效数据类型的表达式，例如 `fixdt(1,16)`

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Output data type** 参数。

有关详细信息，请参阅 Control Data Types of Signals (Simulink)。

#### 依赖关系

要启用此参数，请将 **Source of codebook** 参数设置为 `Specify via dialog`。如果您将 **Source of codebook** 参数设置为 `Input port`，则输出值具有与输入码本值相同的数据类型。

## 所属库

DSP System Toolbox / Quantizers

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `fixed point` | `integer` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `no` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

生成的代码在某些条件下依赖于 `memcpy` 或 `memset` 函数（`string.h`）。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

查找与从零开始的索引值对应的向量量化器码字

Vector Quantizer Decoder 模块将每个输入索引值与一个码字关联，该码字表示为 **Codebook values** 参数中定义的量化输出值的列向量。当您向此模块输入多个索引值时，模块输出量化输出向量的矩阵。模块通过水平串联与每个索引值对应的码字向量来创建此矩阵。
