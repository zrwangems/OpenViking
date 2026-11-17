---
type: simulink-block
title: 'Constant Ramp'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Signal Operations'
documentation_page: 'constantramp'
documentation_source_path: 'ref/constantramp.html'
language: zh-CN
chinese_source: worker-translation
---

# Constant Ramp

## 端口

### 输入

### **Port\_1** — 输入信号 标量 | 向量 | 矩阵 | N 维数组

用于生成斜坡信号的输入信号，指定为标量、向量、矩阵或 N 维数组。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`
### 输出

### **Port\_1** — 输出信号 向量

输出信号，以无方向向量形式返回。该模块根据输入信号的长度以及 **Ramp
length equals number of** 或 **Dimension**
参数来确定输出的长度。

**数据类型：** `single` | `double` | `int8` | `int16` | `int32` | `int64` | `uint8` | `uint16` | `uint32` | `uint64` | `Boolean` | `fixed point`

## 参数

### 主要

### **Ramp length equals number of** — 用于确定斜坡长度的维度 `Rows`（默认） | `Columns` | `Elements in specified dimension`

指定输出斜坡的长度是输入的行数、列数，还是指定维度的长度。

### **Dimension** — 确定输出斜坡长度的维度 `1`（默认） | 正整数

将输入数组中用于确定输出斜坡长度的基于一的维度指定为正整数标量。

#### 依赖关系

要启用此参数，请将 **Ramp length equals number
of** 设置为 `Elements in specified
dimension`。

### **Slope** — 斜坡的斜率 `1`（默认） | 标量

将斜坡的斜率指定为实值双精度标量。

### **Offset** — 斜坡的 *y* 截距 `0`（默认） | 标量

将斜坡的标量 *y* 截距指定为实值双精度标量。

### 数据类型

### **Output data type** — 输出数据类型 `Inherit: Same as input`（默认） | `Inherit: Inherit via back propagation` | `double` | `single` | `int8` | `uint8` | `int16` | `uint16` | `int32` | `uint32` | `int64` | `uint64` | `boolean` | `fixdt(1,16)` | `fixdt(1,16,0)` | `<data type expression>`

指定此模块的输出数据类型。您可以选择以下选项之一：

- 继承数据类型的规则，例如
  `Inherit: Same as input`。
- 内置数据类型，例如 `double`
- 求值后得到有效数据类型的表达式，例如
  `fixdt(1,16)`

有关设置数据类型参数的帮助，请通过点击 **Show data type
assistant** 按钮
来显示 **Data Type
Assistant**。

有关详细信息，请参阅 Control Data Types of Signals (Simulink)。

### 数据类型助手参数

### **Mode** — 数据类型模式 `Inherit`（默认） | `Built in` | `Fixed point` | `Expression`

选择您希望如何指定 **Output data type** 的数据类型属性。您可以选择：

- `Inherit` — 允许您
  指定继承数据类型的规则，例如，
  `Inherit: Same as input`
- `Built in`— 允许您
  指定内置数据类型，例如，
  `double`
- `Fixed point` — 允许您
  指定数据类型的定点属性。
- `Expression` — 允许您
  指定求值后得到有效数据类型的表达式，
  例如，`fixdt(1,16)`

有关详细信息，请参阅 使用数据类型助手指定数据类型 (Simulink)。

### **Signedness** — 定点数据的有符号性 `Signed`（默认） | `Unsigned`

指定定点数据是有符号还是无符号。
`Signed` 数据可以表示正值和
负值，但 `Unsigned` 数据仅表示
正值。有关详细信息，请参阅 使用数据类型助手指定数据类型 (Simulink)。

### **Word length** — 保存量化整数的字长位数 `16`（默认） | 2 到 128 之间的整数

将保存量化整数的字长位数指定为 2 到 128 之间的整数标量。有关详细信息，请参阅 使用数据类型助手指定数据类型 (Simulink)。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为
`Fixed point`

### **Scaling** — 定点数据的定标方法 `Best precision`（默认） | `Binary point`

指定定点数据的定标方法，以避免溢出
情况并最小化量化误差。有关详细信息，请参阅
使用数据类型助手指定数据类型 (Simulink)。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为
`Fixed point`

### **Data type override** — 数据类型覆盖模式 `Inherit`（默认） | `Off`

选择此信号的数据类型覆盖模式。您可以选择：

- `Inherit` — 继承为模型指定的数据类型覆盖设置。
- `Off` — 忽略为模型指定的数据类型覆盖设置
  并使用您指定的定点数据类型。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为 `Built
in` 或 `Fixed point`。有关
详细信息，请参阅 使用数据类型助手指定数据类型 (Simulink)。

### **Fraction length** — 定点数据类型的小数长度 `0`（默认） | 整数标量

将定点数据类型的小数长度指定为正整数
或负整数标量。

#### 依赖关系

要启用此参数，请将 **Mode** 设置为
`Fixed point`，并将
**Scaling** 设置为 `Binary
point`。

## 所属库

DSP System Toolbox / Signal Operations

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

生成的代码在某些条件下依赖 `memcpy` 或
`memset` 函数（`string.h`）。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2006a 之前推出**

## 描述

基于输入维度生成具有相应长度的斜坡信号

Constant Ramp 模块生成恒定斜坡信号

```
y = (0:L-1)*m + b
```

其中 *m* 是由标量
**Slope** 参数指定的斜率，*b* 是由标量 **Offset**
参数指定的 *y* 截距。

对于无方向向量输入，*L* 等于输入向量的长度。对于 N 维输入数组，输出斜坡的长度 *L*
等于输入在 **Ramp
length equals number of** 或 **Dimension** 参数所指定维度上的长度。输出
*y* 始终为无方向向量。
