---
type: simulink-block
title: 'Check Signal Attributes'
family: 'signal-management'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Management / Signal Attributes'
documentation_page: 'checksignalattributes'
documentation_source_path: 'ref/checksignalattributes.html'
language: zh-CN
chinese_source: worker-translation
---

# Check Signal Attributes

## 端口

### 输入

### **Input** — 输入信号 scalar | vector | matrix | N-D array

要检查的输入信号，指定为标量、向量、矩阵或 N-D 数组。输入可以是任意实值或复值信号。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`

### 输出

### **Output** — 输出信号 scalar | vector | matrix | N-D array

输出信号，返回为标量、向量、矩阵或 N-D 数组，其值与输入信号相同。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32` | `Boolean` | `fixed point` | `enumerated`

## 参数

### **Error when input** — 当输入时生成错误 `Does not match attributes exactly` (default) | `Matches attributes exactly`

指定当输入*确实*具备或*确实不具备* *所有*所需属性时，模块是否生成错误。

当将此参数设置为 `Does not match attributes exactly` 时，如果输入未能匹配*任何*指定属性，模块将生成错误。只有具备*所有*指定属性的信号才会原样传播到输出，并且不会导致模块生成错误。

当将此参数设置为 `Matches attributes exactly` 时，仅当输入具备*所有*指定属性时，模块才生成错误。不具备*所有*指定属性的信号会原样传播到输出，并且不会导致模块生成错误。

### **Complexity** — 指定复/实性 `Ignore` (default) | `Real` | `Complex`

指定要检查输入的复/实性为 `Real` 或 `Complex`。您可以通过附加一个选中 **Probe complex signal** 的 Probe (Simulink) 模块，在模型中显示此信息。或者，在 **Debug** 选项卡中，选择 **Information Overlays** > **Port Data Type**。

当将此参数设置为 `Ignore` 时，模块不检查输入的复/实性。

### **Dimensionality** — 维度检查 `Ignore` (default) | `Is...` | `Is not...`

指定要检查输入是否符合还是不符合从属 **Dimensions** 参数中的属性。当将此参数设置为 `Ignore` 时，模块不检查输入的维度。

### **Dimensions** — 指定维度 `1-D` (default) | `2-D` | `Scalar (1-D or 2-D)` | `Vector (1-D or 2-D)` | `Vector (1-D or 2-D) or scalar` | `Row vector (2-D)` | `Row vector (2-D) or scalar` | `Column vector (2-D)` | `Column vector (2-D) or scalar` | `Full matrix (2-D)` | `Square matrix (2-D)`

指定要检查输入的维度。

检查输入的维度是否符合或不符合此参数中的属性。请参阅下表。除非另有说明，*M* 和 *N* 为正整数。

| Dimensions | 是... | 不是... |
| --- | --- | --- |
| 1-D | 1-D 向量，   1-D 标量 | *M*×*N* 矩阵，   1×*N* 矩阵（行向量），   *M*×1 矩阵（列向量），   1×1 矩阵（2-D 标量） |
| 2-D | *M*×*N* 矩阵，   1×*N* 矩阵（行向量），   *M*×1 矩阵（列向量），   1×1 矩阵（2-D 标量） | 1-D 向量，   1-D 标量 |
| Scalar   (1-D or 2-D) | 1-D 标量，   1×1 矩阵（2-D 标量） | 长度>1 的 1-D 向量，   *M*×*N* 矩阵，其中 *M*>1 和/或 *N*>1 |
| Vector   (1-D or 2-D) | 1-D 向量，   1-D 标量，   1×*N* 矩阵（行向量），   *M*×1 矩阵（列向量），   1×1 矩阵（2-D 标量）   Vector (1-D or 2-D) or scalar | *M*×*N* 矩阵，其中 *M*>1 且 *N*>1 |
| Row Vector   (2-D) | 1×*N* 矩阵（行向量），   1×1 矩阵（2-D 标量）   Row vector (2-D) or scalar | 1-D 向量，   1-D 标量，   *M*×*N* 矩阵，其中 *M*>1 |
| Column Vector   (2-D) | *M*×1 矩阵（列向量）， 1×1 矩阵（2-D 标量）   Column vector (2-D) or scalar | 1-D 向量，   1-D 标量，   *M*×*N* 矩阵，其中 *N*>1 |
| Full matrix | *M*×*N* 矩阵，其中 *M*>1 且 *N*>1 | 1-D 向量，   1-D 标量，   1×*N* 矩阵（行向量），   *M*×1 矩阵（列向量），   1×1 矩阵（2-D 标量） |
| Square matrix | *M*×*N* 矩阵，其中 *M*=*N*，   1-D 标量，   1×1 矩阵（2-D 标量 | *M*×*N* 矩阵，其中 *M*≠*N*，   1-D 向量，   1×*N* 矩阵（行向量），   *M*×1 矩阵（列向量） |

在 **Debug** 选项卡中，当选择 **Information Overlays** > **Signal Dimensions** 时，Simulink® 将 1-D 向量信号的大小显示为不带括号的整数，并将 2-D 信号的维度显示为一对带括号的整数 `[MxN]`。Simulink *不显示* 1-D 或 2-D 标量信号的任何大小信息。您还可以通过附加一个选中 **Probe signal dimensions** 的 Probe 模块，在模型中显示信号的维度信息。

#### 依赖关系

要启用此参数，请将 **Dimensionality** 设置为 `Is...` 或 `Is not...`。

### **Data type** — 数据类型检查 `Ignore` (default) | `Is...` | `Is not...`

指定要检查输入符合 `Is...` 还是不符合 `Is not...` 从属 **General data type** 参数中的属性。当将此参数设置为 `Ignore` 时，模块不检查输入数据类型。

请参阅下表。您可以从从属 **Specific data type** 参数中单独选择 `(Is...)` 列中列出的任何特定数据类型。

| General Data Type | 是... | 不是... |
| --- | --- | --- |
| Boolean | `boolean` | `single, double, uint8, int8, uint16, int16, uint32, int32`, fixed point, enumerated |
| Enumerated | 用户定义的枚举数据类型。请参阅 Data Types (Simulink)。 | `boolean, single, double, uint8, int8, uint16, int16, uint32, int32`, fixed point |
| Floating point | `single, double` | `boolean, uint8, int8, uint16, int16, uint32, int32`, fixed point, enumerated |
| Floating point or Boolean | `single, double, boolean` | `uint8, int8, uint16, int16, uint32, int32`, fixed point, enumerated |
| Fixed point | fixed point, `uint8, int8, uint16, int16, uint32, int32` | `boolean, single, double`, enumerated |
| Integer | 有符号整数   `int8`, `int16`, `int32`无符号整数   `uint8`, `uint16`, `uint32` | `boolean, single, double`, fixed point, enumerated |

要显示数据类型信息，请在 **Debug** 选项卡中，选择 **Information Overlays** > **Port Data Type**。

### **General data type** — 常规数据类型检查 `Boolean` (default) | `Enumerated` | `Floating-point` | `Floating-point or boolean` | `Fixed-point` | `Integer`

指定要检查输入的常规数据类型。

#### 依赖关系

要启用此参数，请将 **Data type** 设置为 `Is...` 或 `Is not...`。

### **Specific floating-point** — 特定浮点检查 `Any floating-point` (default) | `Double precision` | `Single precision`

指定要检查输入的浮点数据类型。

#### 依赖关系

要启用此参数，请将 **General data type** 设置为 `Floating-point` 或 `Floating-point or boolean`。

### **Specific fixed-point** — 特定定点检查 `Any fixed-point` (default) | `Signed fixed-point` | `Unsigned fixed-point`

指定要检查输入的定点数据类型。

#### 依赖关系

要启用此参数，请将 **General data type** 设置为 `Fixed-point`。

### **Specific integer** — 特定整数检查 `Any integer` (default) | `Signed integer` | `Unsigned integer` | `int8` | `int16` | `int32` | `uint8` | `uint16` | `uint32`

指定要检查输入的整数数据类型。

#### 依赖关系

要启用此参数，请将 **General data type** 设置为 `Integer`。

### **Sample time** — 采样时间检查 `Ignore` (default) | `Discrete` | `Continuous`

指定要检查输入的采样时间为 `Discrete` 或 `Continuous`。当将此参数设置为 `Ignore` 时，模块不检查输入的采样时间。

模块检查信号是离散时间还是连续时间。在 **Debug** 选项卡中，当选择 **Information Overlays** > **Colors** 时，Simulink 将连续时间信号线显示为黑色或灰色，并将离散时间信号线显示为与相对速率对应的颜色。

当您将启用了 **Probe sample time** 的 Probe 模块附加到连续时间信号时，模块图标显示 `Ts:[0 To]`，其中 `To` 是采样时间偏移量。对于连续时间信号，`To` 的有效值为 `0` 和 `1`。当 `To` 为 `0` 时，更新在每个主时间步和次时间步发生。当 `To` 为 `1` 时，更新仅在主时间步发生，并且采样时间*在次时间步中固定*。

当您将启用了 **Probe sample time** 的 Probe 模块附加到离散时间信号时，对于基于采样的信号，模块图标显示 `Ts:[Ts To]`；对于基于帧的信号，显示 `Tf:[Tf To]`。`Ts` 和 `Tf` 分别是正采样周期和帧周期。`To` 是偏移量，使得 0 ≤ *`offset`* < *`period`*。基于帧的信号几乎总是离散时间。

## 所属库

DSP System Toolbox / Signal Management / Signal Attributes

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `Boolean` | `double` | `enumerated` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

## 版本历史

**在 R2006a 之前引入**

## 描述

当输入信号完全匹配或不匹配所选属性时出错

当输入特性与您在模块参数中指定的特性不同时，Check Signal Attributes 模块会终止仿真并生成错误。

Check Signal Attributes 模块最多可测试五种不同的信号属性。当您为任何参数选择 `Ignore` 时，模块不会检查信号的相应属性。例如，当您将 **Complexity** 设置为 `Ignore` 时，实输入或复输入都不会导致模块生成错误。
