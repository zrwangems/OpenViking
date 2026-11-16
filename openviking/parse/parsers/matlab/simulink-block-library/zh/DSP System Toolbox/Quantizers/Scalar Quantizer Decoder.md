---
type: simulink-block
title: 'Scalar Quantizer Decoder'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Quantizers'
documentation_page: 'scalarquantizerdecoder'
documentation_source_path: 'ref/scalarquantizerdecoder.html'
language: zh-CN
chinese_source: worker-translation
---

# Scalar Quantizer Decoder

## 端口

### 输入

### **I** — 索引值向量

指定范围 0 ≤ index < *N* 内的索引值，其中 *N* 是码本矩阵中不同码字向量的数量。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **C** — 码本值向量 | 矩阵

将码本值指定为向量或矩阵。

#### 依赖关系

要启用此端口，请将 **Source of codebook** 参数设置为 `Input port`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`

### 输出

### **Q(U)** — 量化输出值向量 | 矩阵

量化输出值，返回为与输入数据大小相同的向量或矩阵。

如果码本值通过 **C** 端口输入，则量化输出值的数据类型与输入码本值的数据类型相同。如果码本值在模块对话框中指定，则 **Codebook and output data type** 参数确定量化输出值的数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

## 参数

### 主选项卡

### **Action for out of range index value** — 超出范围索引值的操作 `Clip`（默认） | `Clip and warn` | `Error`

当输入索引值超出范围 0 ≤ index <*N* 时，指定模块必须执行的以下操作之一，其中 *N* 是码本向量的长度。当您希望任何小于 0 的索引值设置为 0，并且任何大于或等于 *N* 的索引值设置为 *N*−1 时，选择 `Clip`。当您希望在发生裁剪时收到警告时，选择 `Clip and warn`。当您希望在索引值超出范围时停止仿真并且模块显示错误时，选择 `Error`。

### **Source of codebook** — 码本来源 `Specify via dialog`（默认） | `Input port`

将码本值的来源指定为以下之一：

- `Specify via dialog` —— 在 **Codebook values** 参数中输入码本值。
- `Input port` —— 通过输入端口 **C** 指定码本值。

### **Codebook values** — 码本值 `[1:10]`（默认） | 向量 | 矩阵

以向量或矩阵形式输入与每个索引值对应的所有可能的量化输出值。码本值的数据类型由 **Codebook and output data type** 参数的设置确定。

**可调：** 是

#### 依赖关系

要启用此参数，请将 **Source of codebook** 参数设置为 `Specify via dialog`。

### 数据类型选项卡

### **Codebook and output data type** — 码本和输出数据类型 `double`（默认） | `Same as input` | `single` | `Inherit via back propagation` | 数值类型

指定码本和量化输出值的数据类型。您可以选择以下之一：

- 继承数据类型的规则，例如 `Inherit: Same as input`。
- 内置数据类型，例如 `double`
- 求值结果为有效数据类型的表达式，例如 `fixdt(1,16)`

点击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Output data type** 参数。

有关详细信息，请参阅 Control Data Types of Signals (Simulink)。

#### 依赖关系

仅当将 **Source of codebook** 参数设置为 `Specify via dialog` 时，此参数才可用。如果将 **Source of codebook** 参数设置为 `Input port`，则量化输出值的数据类型与输入码本值的数据类型相同。

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

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前引入**

## 描述

将每个索引值转换为量化输出值

Scalar Quantizer Decoder 模块将从零开始的输入索引值转换为量化输出值。对于每个输入索引值，模块输出对应的量化输出值（或码字）。

所有可能的量化输出值集合由 **Codebook values** 参数定义。
