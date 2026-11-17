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

指定范围内的索引值，0 ≤ index < *N*，其中 *N* 是码本矩阵中不同码字向量的数量。

**数据类型：** `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

### **C** — 码本值向量 | 矩阵

将码本值指定为向量或矩阵。

#### 依赖关系

要启用此端口，请将**码本来源**参数设置为 `输入端口`。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
### 输出

### **Q(U)** — 量化输出值向量 | 矩阵

量化输出值，以与输入数据大小相同的向量或矩阵返回。

如果码本值通过 **C** 端口输入，则量化输出值的数据类型与输入码本值的数据类型相同。如果在模块对话框中指定码本值，则**码本和输出数据类型**参数决定量化输出值的数据类型。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `fixed point`

## 参数

### 主选项卡

### **超出范围索引值的操作** — 超出范围索引值的操作 `Clip`（默认） | `Clip and warn` | `Error`

指定当输入索引值超出范围 0 ≤ index <*N* 时模块必须采取的以下操作之一，其中 *N* 是码本向量的长度。选择 `Clip`，当您希望将任何小于 0 的索引值设置为 0，将任何大于或等于 *N* 的索引值设置为 *N*−1 时。选择 `Clip and warn`，当您希望在发生裁剪时收到警告时。选择 `Error`，当您希望仿真停止并且模块在索引值超出范围时显示错误时。

### **码本来源** — 码本来源 `Specify via dialog`（默认） | `Input port`

将码本值的来源指定为以下之一：

- `Specify via dialog` –– 在**码本值**参数中输入码本值。
- `Input port` –– 通过输入端口 **C** 指定码本值。

### **码本值** — 码本值 `[1:10]`（默认） | 向量 | 矩阵

将对应于每个索引值的所有可能的量化输出值输入为向量或矩阵。码本值的数据类型由**码本和输出数据类型**参数的设置决定。

**可调：** 是

#### 依赖关系

要启用此参数，请将**码本来源**参数设置为 `Specify via dialog`。

### 数据类型选项卡

### **码本和输出数据类型** — 码本和输出数据类型 `double`（默认） | `Same as input` | `single` | `Inherit via back propagation` | 数值类型

指定码本和量化输出值的数据类型。您可以选择以下之一：

- 继承数据类型的规则，例如 `Inherit: Same as input`。
- 内置数据类型，例如 `double`
- 求值为有效数据类型的表达式，例如 `fixdt(1,16)`

单击**显示数据类型助手**按钮以显示**数据类型助手**，它帮助您设置**输出数据类型**参数。

有关更多信息，请参阅 Control Data Types of Signals (Simulink)。

#### 依赖关系

此参数仅在您将**码本来源**参数设置为 `Specify via dialog` 时可用。如果您将**码本来源**参数设置为 `Input port`，则量化输出值的数据类型与输入码本值的数据类型相同。

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

Scalar Quantizer Decoder 模块将基于零的输入索引值转换为量化输出值。对于每个输入索引值，模块输出对应的量化输出值（或码字）。

所有可能的量化输出值的集合由**码本值**参数定义。
