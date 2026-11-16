---
type: simulink-block
title: 'Discrete Impulse'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Generation, Manipulation, and Analysis / Signal Generation'
documentation_page: 'discreteimpulse'
documentation_source_path: 'ref/discreteimpulse.html'
language: zh-CN
chinese_source: worker-translation
---

# Discrete Impulse

## 端口

### 输出

### **Port\_1** — 离散冲激信号 标量 | 向量 | 矩阵

输出信号在输出样本 `D(i)+1` 处包含一个离散冲激，其中 `D` 是由 **Delay** 参数指定的标量或向量。有关详细信息，请参阅描述。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### 主要

### **Delay (samples)** — 零值输出样本数 `0`（默认）| 标量 | 向量

零值输出样本数 `D`，位于冲激之前，指定为大于或等于零的整数标量或向量。长度为 *N* 的向量指定 *N* 通道输出。

### **Sample time** — 输出样本周期 `1`（默认）| 正标量

输出信号的样本周期 *Ts*，指定为正有限标量。输出帧周期为 *M**Ts*。

### **Samples per frame** — 每帧样本数 `1`（默认）| 正整数

每个输出帧中的样本数 *M*，指定为正整数标量。

### 数据类型

### **Output data type** — 输出数据类型 `double`（默认）| `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16)` | `fixdt(1,16,0)` | `Inherit: Inherit via back propagation` | `<data type expression>`

指定此模块的输出数据类型。您可以选择以下之一：

- 用于继承数据类型的规则，例如 `Inherit: Inherit via back propagation`。选择此选项时，输出数据类型和定标与下一个下游模块匹配。
- 内置数据类型，例如 `double`
- 计算结果为有效数据类型的表达式，例如 `fixdt(1,16)`

有关设置数据类型参数的帮助，请单击 **显示数据类型助手** 按钮以显示 **数据类型助手**。

有关详细信息，请参阅控制信号的数据类型 (Simulink)。

### 数据类型助手

### **Mode** — 数据类型模式 `Inherit`（默认）| `Built in` | `Fixed point` | `Expression`

选择希望如何指定 **Output data type** 的数据类型属性。您可以选择：

- `Inherit` — 允许您指定继承数据类型的规则，例如 `Inherit: Same as input`
- `Built in` — 允许您指定内置数据类型，例如 `double`
- `Fixed point` — 允许您指定数据类型的定点属性。
- `Expression` — 允许您指定计算结果为有效数据类型的表达式，例如 `fixdt(1,16)`

有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **Signedness** — 定点数据的符号性 `Signed`（默认）| `Unsigned`

指定定点数据是有符号还是无符号。`Signed` 数据可表示正值和负值，但 `Unsigned` 数据仅表示正值。有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

### **Scaling** — 定点数据的定标方法 `Best precision`（默认）| `Binary point`

指定定点数据的定标方法，以避免溢出情况并最小化量化误差。有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Word length** — 保存量化整数的字长位数 `16`（默认）| 2 到 128 的整数

将保存量化整数的字长位数指定为 2 到 128 的正整数。有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`。

### **Fraction length** — 定点数据类型的小数长度 `0`（默认）| 整数标量

将定点数据类型的小数长度指定为正整数或负整数标量。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Fixed point`，并将 **Scaling** 设置为 `Binary point`。

### **Data type override** — 数据类型覆盖模式 `Inherit`（默认）| `Off`

选择此信号的数据类型覆盖模式。您可以选择：

- `Inherit` — 继承为模型指定的数据类型覆盖设置。
- `Off` — 忽略为模型指定的数据类型覆盖设置，并使用您指定的定点数据类型。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Built in` 或 `Fixed point`。有关详细信息，请参阅使用数据类型助手指定数据类型 (Simulink)。

## 所属库

DSP System Toolbox / Sources

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `fixed point` | `integer` | `single` |
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

生成离散冲激

Discrete Impulse 模块在输出样本 `D+1` 处生成一个冲激（值 `1`），其中您使用 **Delay** 参数指定 `D`（`D` ≥ `0`）。样本 `D+1` 之前和之后的所有输出样本均为零。

当 `D` 是长度为 *N* 的向量时，该模块生成 *M*×*N* 矩阵输出，表示 *N* 个不同通道，其中您使用 **Samples per frame** 参数指定帧大小 *M*。第 `i` 个通道的冲激出现在样本 `D(i)+1` 处。

**Sample time** 参数值 *Ts* 指定输出信号样本周期。得到的帧周期为 *M**Ts*。
