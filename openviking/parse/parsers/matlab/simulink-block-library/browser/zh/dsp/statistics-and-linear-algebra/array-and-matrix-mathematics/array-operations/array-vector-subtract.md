---
type: simulink-block
title: 'Array-Vector Subtract'
family: 'dsp'
product_id: 'dsp'
product_name: 'DSP System Toolbox'
documentation_release: R2025b
official_category: 'Statistics and Linear Algebra / Array and Matrix Mathematics / Array Operations'
documentation_page: 'arrayvectorsubtract'
documentation_source_path: 'ref/arrayvectorsubtract.html'
language: zh-CN
chinese_source: worker-translation
---

# Array-Vector Subtract

## 端口

### 输入

### **A** — 输入数组 标量 | 向量 | 矩阵 | *N*-D 数组

将输入数组指定为标量、向量、矩阵或 *N*-D 数组。

如果输入为定点，则它必须是有符号整数或具有 2 的幂斜率和零偏置的有符号定点值。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持:** Yes

### **V** — 要减去的向量 向量

将要减去的向量 *V* 指定为长度等于输入 *A* 中指定维度长度的向量。

#### 依赖关系

要启用此参数，请将 **Vector (V) source** 参数设置为 `Input port`。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持:** Yes

### 输出

### **Output** — 输出 标量 | 向量 | 矩阵 | *N*-D 数组

Array-Vector Subtract 模块的输出，返回为标量、向量、矩阵或 *N*-D 数组。输出始终具有与输入信号相同的大小、数据类型和复/实性。

有关该模块如何计算输出的更多信息，请参阅算法。

**数据类型:** `single` | `double` | `int8` | `int16` | `int32` | `fixed point`
**复数支持:** Yes

## 参数

### 主选项卡

### **Subtract along dimension** — 沿其进行减法的维度 `1` (默认) | 正整数

将要从输入数组 *A* 中减去向量 *V* 元素的维度指定为正整数。此参数的值必须小于或等于输入 *A* 的维数。

### **Vector (V) source** — 向量 *V* 的来源 `Input port` (默认) | `Dialog parameter`

将向量 *V* 的来源指定为以下之一：

- `Input port` –– 使用输入端口 **V** 指定该向量。
- `Dialog parameter` –– 使用 **Vector (V)** 对话框参数指定该向量。

### **Vector (V)** — 要减去的向量 `[0.5 0.25]` (默认) | 向量

将要减去的向量 *V* 指定为长度等于输入 *A* 中指定维度长度的向量。

#### 依赖关系

要启用此参数，请将 **Vector (V) source** 参数设置为 `Dialog parameter`。

### 数据类型选项卡

**注意**

浮点继承优先于此选项卡上定义的数据类型设置。当输入为浮点时，该模块会忽略这些设置，并且所有内部数据类型均为浮点。

### **Rounding mode** — 舍入模式 `Floor` (默认) | `Ceiling` | `Convergent` | `Nearest` | `Round` | `Simplest` | `Zero`

将定点运算的舍入模式指定为以下之一：

- `Floor`
- `Ceiling`
- `Convergent`
- `Nearest`
- `Round`
- `Simplest`
- `Zero`

有关更多详细信息，请参阅舍入模式。

**注意**

当满足以下两个条件时，**Rounding mode** 和 **Saturate on integer overflow** 设置对数值结果没有影响：

- **Accumulator** 为 `Inherit: Inherit via internal rule`
- **Output** 为 `Inherit: Same as accumulator`

使用这些数据类型设置，该模块实际以全精度模式运行。

### **Saturate on integer overflow** — 整数溢出时饱和 `off` (默认) | `on`

选中此参数时，该模块会对其定点运算的结果进行饱和处理。清除此参数时，该模块会对其定点运算的结果进行绕回处理。有关 `saturate` 和 `wrap` 的详细信息，请参阅定点运算的溢出模式。

### **Vector (V)** — 向量数据类型 `Inherit: Same word length as input` (默认) | `fixdt([],16,0)`

使用此参数指定向量 *V* 元素的字长和小数长度。可将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Same word length as input`。
- 可求值为有效数据类型的表达式，例如 `fixdt([],16,0)`。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Accumulator** 参数。

有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

#### 依赖关系

仅当在模块对话框中的 **Main** 选项卡上为 **Vector (V) source** 参数选择 `Dialog parameter` 时，**Data Types** 选项卡上的 **Vector (V)** 参数才可见。当向量通过模块的输入端口传入时，其元素的数据类型和定标继承自驱动模块。

### **Accumulator** — 累加器数据类型 `Inherit: Inherit via internal rule` (默认) | `Inherit: Same as first input` | `fixdt([],16,0)`

指定累加器数据类型。有关说明此模块中累加器数据类型用法的图示，请参阅 Fixed-Point Data Types。可将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Inherit via internal rule`。有关此规则的更多信息，请参阅 Inherit via Internal Rule。
- 继承数据类型的规则，例如 `Inherit: Same as first input`。
- 可求值为有效数据类型的表达式，例如 `fixdt([],16,0)`。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Accumulator** 参数。

有关更多信息，请参阅 Specify Data Types Using Data Type Assistant (Simulink)。

### **Output** — 输出数据类型 `Inherit: Same as accumulator` (默认) | `Inherit: Same as first input` | `fixdt([],16,0)`

指定输出数据类型。有关说明此模块中输出数据类型用法的图示，请参阅 Fixed-Point Data Types。可将此参数设置为：

- 继承数据类型的规则，例如 `Inherit: Same as accumulator`
- 继承数据类型的规则，例如 `Inherit: Same as first input`。
- 可求值为有效数据类型的表达式，例如 `fixdt([],16,0)`。

单击 **Show data type assistant** 按钮以显示 **Data Type Assistant**，它可帮助您设置 **Output** 参数。

有关更多信息，请参阅 Control Data Types of Signals (Simulink)。

### **Output Minimum** — 输出最小值 `[]` (默认) | 标量

指定模块应输出的最小值。默认值为 `[]`（未指定）。Simulink® 使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink)）
- 定点数据类型的自动定标

### **Output Maximum** — 输出最大值 `[]` (默认) | 标量

指定模块应输出的最大值。默认值为 `[]`（未指定）。Simulink 使用此值执行：

- 仿真范围检查（请参阅 Specify Signal Ranges (Simulink)）
- 定点数据类型的自动定标

### **Lock data type settings against changes by the fixed-point tools** — 防止定点工具覆盖数据类型 `off` (默认) | `on`

选择此参数可防止定点工具覆盖您在模块对话框中指定的数据类型。

## 所属库

DSP System Toolbox / Math Functions / Matrices and Linear Algebra / Matrix Operations

## 模块特性

|  |  |
| --- | --- |
| **数据类型** | `double` | `fixed point` | `integer` | `single` |
| **直接馈通** | `no` |
| **多维信号** | `no` |
| **可变大小信号** | `yes` |
| **过零检测** | `no` |

## 扩展功能

### C/C++ 代码生成 使用 Simulink® Coder™ 生成 C 和 C++ 代码。

### 定点转换 使用 Fixed-Point Designer™ 设计和仿真定点系统。

## 版本历史

**在 R2007b 中引入**

## 描述

沿指定维度从数组中减去向量

Array-Vector Subtract 模块从 *N* 维输入数组 *A* 的指定维度中的值减去输入向量 *V* 中的值。Array-Vector Subtract 模块将 *V* 的每个元素从 *A* 的指定维度上对应元素中减去。

有关该模块如何计算输出的更多信息，请参阅算法。
